import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import build_backrefs
import deep_enrich_sources
import deep_enrich_taxonomy
import ingest_folder
import llm_client
import audit_wiki_quality
import audit_wiki_strict
import add_source_boundaries
import sync_source_metadata
import repair_source_summaries
import repair_journals_from_crossref
import deep_review_sources


class FakeLLM:
    def __init__(self, responses):
        self.responses = list(responses)
        self.prompts = []

    def complete(self, prompt, *, max_tokens, temperature, timeout):
        self.prompts.append(prompt)
        return self.responses.pop(0)


SOURCE_RESPONSE = json.dumps({
    "methodology": {
        "approach": "采用状态空间和节点分析组合方法。",
        "equations": [{"latex": "i=C\\frac{dv}{dt}", "description": "电容电流关系"}],
        "algorithm_steps": ["建立节点方程", "求解状态变量"],
        "parameters": {"time_step": "50 us"},
    },
    "simulation_results": [
        {"test_case": "IEEE 39节点", "description": "误差小于0.5%", "comparison": "速度提升2倍"}
    ],
    "quantitative_findings": ["误差<0.5%", "速度提升2倍"],
    "key_equations": [{"latex": "Gv=i", "name": "节点方程", "context": "EMT求解"}],
    "validation_details": {
        "method": "仿真对比",
        "test_system": "IEEE 39节点",
        "tools": "PSCAD",
        "results_summary": "与基线误差<0.5%",
    },
    "applicability_boundaries": {
        "valid_when": ["接口频率分量可由有限阶动态相量表示"],
        "invalid_when": ["强非周期暂态主导且动态相量阶数不足"],
        "assumptions": ["据方法推断：接口两侧变量可同步交换"],
        "evidence_gaps": ["原文未报告硬件实时仿真的延迟上界"],
    },
})


def make_source_page(tmp_path):
    source = tmp_path / "paper.md"
    source.write_text(
        """---
title: "Paper"
type: source
sources: ["EMT_Doc/01/paper.pdf"]
---

# Paper

## 摘要

abstract text that is long enough for the prompt.

## 核心贡献

- old
""",
        encoding="utf-8",
    )
    return source


def test_source_dry_run_does_not_write(tmp_path, monkeypatch):
    source = make_source_page(tmp_path)
    original = source.read_text(encoding="utf-8")
    monkeypatch.setattr(deep_enrich_sources, "get_enhanced_text", lambda filename: "full paper text with numeric result 1%")

    result = deep_enrich_sources.process_single_file("paper.md", source, FakeLLM([SOURCE_RESPONSE]), dry_run=True)

    assert result[1] is True
    assert "dry-run" in result[2]
    assert source.read_text(encoding="utf-8") == original


def test_source_enrichment_replaces_legacy_sections(tmp_path, monkeypatch):
    source = make_source_page(tmp_path)
    source.write_text(source.read_text(encoding="utf-8") + "\n## 方法细节\n\nlegacy\n", encoding="utf-8")
    monkeypatch.setattr(deep_enrich_sources, "get_enhanced_text", lambda filename: "full paper text with numeric result 1%")

    result = deep_enrich_sources.process_single_file("paper.md", source, FakeLLM([SOURCE_RESPONSE]), force=True)
    content = source.read_text(encoding="utf-8")

    assert result[1] is True
    assert "legacy" not in content
    assert deep_enrich_sources.DEEP_SECTION_MARKER_START in content
    assert "## 方法细节" in content
    assert "## 验证详情" in content
    assert "## 适用边界" in content
    assert "原文未报告硬件实时仿真的延迟上界" in content


def test_source_enrichment_skips_inactive_source_pages(tmp_path, monkeypatch):
    source = tmp_path / "duplicate.md"
    source.write_text(
        """---
title: "Duplicate"
type: duplicate-source
canonical: "[[canonical]]"
---

# Duplicate
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(deep_enrich_sources, "get_enhanced_text", lambda filename: "full paper text with numeric result 1%")

    result = deep_enrich_sources.process_single_file("duplicate.md", source, FakeLLM([SOURCE_RESPONSE]), force=True)

    assert result == ("duplicate.md", True, "skipped inactive source")
    assert "## 方法细节" not in source.read_text(encoding="utf-8")


def test_source_queue_reprocesses_checkpoint_items_missing_new_required_sections(tmp_path, monkeypatch, capsys):
    source_dir = tmp_path / "sources"
    source_dir.mkdir()
    checkpoint = tmp_path / "checkpoint.json"
    old_done = source_dir / "old-done.md"
    old_done.write_text(
        """---
title: "Old"
type: source
---

# Old

## 方法细节
ok

## 仿真结果
ok

## 量化发现
原文未报告可核验的数值结果。

## 关键公式
ok

## 验证详情
ok
""",
        encoding="utf-8",
    )
    inactive = source_dir / "inactive.md"
    inactive.write_text("---\ntype: duplicate-source\n---\n# Duplicate\n", encoding="utf-8")
    checkpoint.write_text(json.dumps({"done": ["old-done.md", "inactive.md"], "failed": []}), encoding="utf-8")

    monkeypatch.setattr(deep_enrich_sources, "WIKI_SOURCES", source_dir)
    monkeypatch.setattr(deep_enrich_sources, "CHECKPOINT", checkpoint)
    monkeypatch.setattr(deep_enrich_sources, "make_llm_client", lambda provider=None, model=None: FakeLLM([SOURCE_RESPONSE]))
    monkeypatch.setattr(deep_enrich_sources, "get_enhanced_text", lambda filename: "full paper text with numeric result 1%")

    deep_enrich_sources.main(dry_run=True, limit=10, concurrency=1)
    output = capsys.readouterr().out

    assert "Remaining: 1" in output
    assert "old-done.md" in output
    assert "inactive.md" not in output


def test_source_files_sort_by_strict_risk(tmp_path):
    strict_report = tmp_path / "strict.json"
    strict_report.write_text(
        json.dumps(
            [
                {"page_type": "source", "path": "wiki/sources/high.md", "score": 56},
                {"page_type": "topic", "path": "wiki/topics/skip.md", "score": 100},
                {"page_type": "source", "path": "wiki/sources/low.md", "score": 12},
            ]
        ),
        encoding="utf-8",
    )
    files = [tmp_path / "none.md", tmp_path / "low.md", tmp_path / "high.md"]

    sorted_files = deep_enrich_sources.sort_source_files_by_priority(files, strict_report)

    assert [path.name for path in sorted_files] == ["high.md", "low.md", "none.md"]


def test_add_source_boundaries_adds_conservative_boundary():
    content = """---
title: "Paper"
type: source
authors: ['未知']
journal: ""
sources: ["EMT_Doc/01/paper.pdf"]
---

# Paper

## 摘要
Short.

## 核心贡献
- 提出快速 EMT 等值方法。

## 使用的方法
- [[state-space-method]]

## 量化发现
原文未报告可核验的数值结果。
"""

    updated = add_source_boundaries.add_boundary(content)

    assert "## 适用边界" in updated
    assert "### 适用条件" in updated
    assert "### 失效边界" in updated
    assert "### 证据缺口" in updated
    assert "作者元数据仍需" in updated
    assert "不能据此声称具体精度" in updated


def test_add_source_boundaries_skips_inactive_and_existing():
    duplicate = "---\ntype: duplicate-source\n---\n# Duplicate\n"
    existing = "---\ntype: source\n---\n# Paper\n\n## 适用边界\nold\n"

    assert add_source_boundaries.add_boundary(duplicate) == duplicate
    assert add_source_boundaries.add_boundary(existing) == existing


def test_sync_source_metadata_repairs_placeholders_from_metadata():
    content = """---
title: "27&28/placeholder"
type: source
authors: ['未知']
year: None
journal: ""
sources: ["EMT_Doc/01/Author 等 - 2024 - Real Paper Title.pdf"]
---

# 27&28/placeholder

**作者**:
**年份**: None

## 摘要
Short.
"""
    metadata = {
        "title": "Real Paper Title",
        "authors": "Alice Author, Bob Writer",
        "subject": "IEEE Transactions on Power Delivery",
        "year": 2024,
        "abstract": "This abstract is long enough to replace a short placeholder and describes EMT simulation evidence.",
    }

    updated = sync_source_metadata.sync_page(content, metadata)

    assert 'title: "Real Paper Title"' in updated
    assert "authors: ['Alice Author', 'Bob Writer']" in updated
    assert 'journal: "IEEE Transactions on Power Delivery"' in updated
    assert "year: 2024" in updated
    assert "# Real Paper Title" in updated
    assert "**作者**: Alice Author; Bob Writer" in updated
    assert "This abstract is long enough" in updated


def test_sync_source_metadata_uses_filename_author_when_metadata_author_bad():
    content = """---
title: "Paper"
type: source
authors: ['CNKI']
journal: ""
sources: ["EMT_Doc/01/Dufour 等 - 2011 - A combined state-space nodal method.pdf"]
---

# Paper
**作者**: CNKI
"""

    updated = sync_source_metadata.sync_page(content, {"authors": "CNKI"})

    assert "authors: ['Dufour 等']" in updated
    assert "**作者**: Dufour 等" in updated


def test_sync_source_metadata_treats_ieee_as_placeholder_author():
    content = """---
title: "Paper"
type: source
authors: ['IEEE']
journal: ""
sources: ["EMT_Doc/01/Morched 等 - 2004 - Paper.pdf"]
---

# Paper
**作者**: IEEE
"""

    updated = sync_source_metadata.sync_page(content, {"authors": "IEEE"})

    assert "authors: ['Morched 等']" in updated
    assert "**作者**: Morched 等" in updated


def test_repair_source_summaries_uses_extracted_text_and_deep_sections(monkeypatch):
    content = """---
title: "Published in IEEE"
type: source
authors: ['CNKI']
year: 2025
journal: ""
sources: ["EMT_Doc/01/paper.pdf"]
---

# Published in IEEE

**作者**: CNKI
**年份**: 2025

## 摘要

This paper has a short broken abstract.

## 核心贡献

- old

## 方法细节

### 方法概述

该方法面向电磁暂态仿真中的接口误差问题，先构造频率相关网络等值，再把端口导纳拟合为可在 EMTP 时间步循环中调用的 RLC 模块。算法步骤包括抽取端口、计算宽频导纳、进行矩阵消去、生成等值网络，并在暂态仿真中更新端口响应。

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |
|---|---|---|
| IEEE 39节点 | 与详细模型对比，电压误差为0.5%。 | PSCAD 基线 |

## 量化发现

- 误差 0.5%。
- 速度提升 2 倍。

## 验证详情

- **验证方式**: 与 PSCAD/EMTDC 详细模型对比。
- **测试系统**: IEEE 39 节点。
- **仿真工具**: PSCAD/EMTDC。

## 适用边界

### 适用条件

- 适用于端口频率响应可由有限阶 RLC 等值拟合的网络。
"""
    paper_text = """## A Frequency Dependent Equivalent for EMT
Alice Author, Bob Writer
IEEE Transactions on Power Delivery

**摘要：** 为解决大规模电力系统电磁暂态仿真中外部网络详细建模计算量过大的问题，本文提出频率相关网络等值方法。该方法在保留研究区域端口响应的同时，用可综合的 RLC 模块逼近外部网络导纳，减少多案例暂态仿真的重复计算。
**关键词：** 电磁暂态；网络等值
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: paper_text)

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert 'title: "A Frequency Dependent Equivalent for EMT"' in updated
    assert "authors: ['Alice Author', 'Bob Writer']" in updated
    assert 'journal: "IEEE Transactions on Power Delivery"' in updated
    assert "This paper has a short broken abstract" not in updated
    assert "大规模电力系统电磁暂态仿真" in updated
    assert "问题定位：" in updated
    assert "方法机制：" in updated
    assert "验证证据：" in updated
    assert "验证证据：-" not in updated


def test_repair_source_summaries_does_not_invent_missing_journal(monkeypatch):
    content = """---
title: "Paper"
type: source
authors: ['Good Author']
year: 2024
journal: ""
sources: ["EMT_Doc/01/paper.pdf"]
---

# Paper

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法面向电磁暂态仿真的矩阵求解瓶颈，通过重新组织节点方程和状态变量，降低每个时间步的重复计算量，并保留与传统 EMTP 伴随模型一致的接口变量。

## 仿真结果

在 IEEE 测试系统中与 EMTP 对比。

## 量化发现

- 原文未报告可核验的数值结果。

## 验证详情

- **仿真工具**: EMTP。

## 适用边界

适用于线性网络分块明确的 EMT 场景。
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: "")

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert 'journal: ""' in updated
    assert "短。" not in repair_source_summaries.section_text(updated, "摘要")


def test_repair_source_summaries_infers_journal_from_source_path(monkeypatch):
    content = """---
title: "Passivity Enforcement"
type: source
authors: ['Good Author']
year: 2008
journal: ""
sources: ["EMT_Doc/31/TPWRD.2008.919034.pdf.pdf"]
---

# Passivity Enforcement

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法面向电磁暂态仿真中的传输线模型稳定性问题，通过检查频域模型的无源性并施加修正，降低由宽频拟合造成的时域发散风险。

## 验证详情

- **仿真工具**: PSCAD。

## 适用边界

- 适用于传输线宽频模型。
- 期刊/会议元数据未在当前页面中可靠给出。
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: "")

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert 'journal: "IEEE Transactions on Power Delivery"' in updated
    assert "期刊/会议元数据未在当前页面中可靠给出" not in updated


def test_repair_source_summaries_infers_journal_from_metadata_subject(monkeypatch):
    content = """---
title: "Lessons learned"
type: source
authors: ['P. Le-Huy']
year: 2023
journal: ""
sources: ["EMT_Doc/25/paper.pdf"]
---

# Lessons learned

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法总结离线大规模 EMT 仿真向实时平台迁移时的模型转换、接口校验和运行性能问题，用经验案例约束后续仿真平台建设。

## 验证详情

- **验证方式**: 工程案例复盘。

## 适用边界

- 适用于实时仿真迁移经验总结。
"""
    metadata = {"subject": "Electric Power Systems Research, 223 (2023) 109663. doi:10.1016/j.epsr.2023.109663"}
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: "")

    updated = repair_source_summaries.repair_content(content, "paper.md", metadata)

    assert 'journal: "Electric Power Systems Research"' in updated
    assert "109663" not in repair_source_summaries.frontmatter_value(updated, "journal")


def test_repair_source_summaries_normalizes_metadata_subject_variants(monkeypatch):
    content = """---
title: "PESGM Paper"
type: source
authors: ['Good Author']
year: 2025
journal: ""
sources: ["EMT_Doc/25/paper.pdf"]
---

# PESGM Paper

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法面向电磁暂态仿真中的接口建模问题，给出适合会议论文场景的模型构造和案例验证流程。

## 验证详情

- **验证方式**: 算例对比。

## 适用边界

- 适用于会议论文元数据规范化测试。
"""
    metadata = {"subject": "2025 IEEE Power &amp; Energy Society General Meeting (PESGM);2025; ; ;10.1109/PESGM52009.2025.11225688"}
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: "")

    updated = repair_source_summaries.repair_content(content, "paper.md", metadata)

    assert 'journal: "IEEE Power & Energy Society General Meeting"' in updated


def test_repair_source_summaries_maps_doi_prefixes_in_extracted_text(monkeypatch):
    content = """---
title: "Access Paper"
type: source
authors: ['Good Author']
year: 2026
journal: ""
sources: ["EMT_Doc/25/paper.pdf"]
---

# Access Paper

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法面向动态相量大规模仿真，通过多速率积分组织慢变量和快变量的计算，以减少统一小步长仿真的计算量。

## 验证详情

- **验证方式**: 算例对比。

## 适用边界

- 适用于动态相量仿真。
"""
    paper_text = """Received 9 January 2026.
Digital Object Identifier 10.1109/ACCESS.2026.3661338
# Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: paper_text)

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert 'journal: "IEEE Access"' in updated


def test_repair_source_summaries_maps_chinese_doi_prefixes(monkeypatch):
    content = """---
title: "中文论文"
type: source
authors: ['陈来军']
year: 2010
journal: ""
sources: ["EMT_Doc/01/paper.pdf"]
---

# 中文论文

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法面向多相交直流电力系统电磁暂态仿真，通过混合并行算法拆分元件级和网络级计算以提升仿真效率。

## 验证详情

- **验证方式**: 仿真算例。

## 适用边界

- 适用于并行电磁暂态仿真。
"""
    paper_text = "DOI：10.13335/j.1000-3673.pst.2010.01.001\n## 一种混合并行算法"
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: paper_text)

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert 'journal: "电网技术"' in updated


def test_repair_source_summaries_uses_short_metadata_evidence(monkeypatch):
    content = """---
title: "短证据中文论文"
type: source
authors: ['岳程燕']
year: 2004
journal: ""
sources: ["EMT_Doc/36/paper.pdf"]
---

# 短证据中文论文

## 摘要

短。

## 核心贡献

- old

## 方法细节

该方法面向电力系统电磁暂态实时仿真中的网络分割并行处理问题，通过并行计算组织实时数字仿真流程。

## 验证详情

- **验证方式**: 实时仿真案例。

## 适用边界

- 适用于实时电磁暂态仿真。
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: "")
    monkeypatch.setattr(
        repair_source_summaries,
        "metadata_evidence_text",
        lambda filename: "DOI: 10.13334/j.0258-8013.pcsee.2004.12.001\n中国电机工程学报",
    )

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert 'journal: "中国电机工程学报"' in updated


def test_crossref_repair_accepts_high_similarity_container():
    content = """---
title: "A link between EMTP-RV and FLUX3D for transformer energization studies"
type: source
authors: ['S. Dennetière']
year: 2009
journal: ""
sources: ["EMT_Doc/02/Dennetière 等 - 2009 - A link between EMTP-RV and FLUX3D for transformer energization studies.pdf"]
---

# A link between EMTP-RV and FLUX3D for transformer energization studies
"""

    def fake_query(title):
        return [
            {
                "title": ["A link between EMTP-RV and FLUX3D for transformer energization studies"],
                "container-title": ["Electric Power Systems Research"],
                "DOI": "10.1016/j.epsr.2008.09.006",
                "score": 76,
            }
        ]

    original = repair_journals_from_crossref.query_crossref
    repair_journals_from_crossref.query_crossref = fake_query
    try:
        match = repair_journals_from_crossref.best_match(content)
    finally:
        repair_journals_from_crossref.query_crossref = original

    assert match["container"] == "Electric Power Systems Research"
    assert match["similarity"] >= 0.99


def test_crossref_repair_rejects_low_similarity_container():
    content = """---
title: "Application of EMTP in the research of UHV AC power transmission"
type: source
journal: ""
sources: ["EMT_Doc/09/Cao - 2006 - Application of EMTP in the research of UHV AC power transmission.pdf"]
---

# Application of EMTP in the research of UHV AC power transmission
"""

    def fake_query(title):
        return [
            {
                "title": ["Research and application of UHV power transmission in China"],
                "container-title": ["High Voltage"],
                "DOI": "10.1049/hve.2018.0003",
                "score": 34,
            }
        ]

    original = repair_journals_from_crossref.query_crossref
    repair_journals_from_crossref.query_crossref = fake_query
    try:
        match = repair_journals_from_crossref.best_match(content)
    finally:
        repair_journals_from_crossref.query_crossref = original

    assert match is None


def test_repair_source_summaries_replaces_keyword_polluted_authors(monkeypatch):
    content = """---
title: "Parallel-in-Time Simulation Algorithm"
type: source
authors: ['Index Terms —Electro-magnetic transient simulation', 'parallel-in-time']
year: 2019
journal: ""
sources: ["EMT_Doc/30/JESTPE.2019.2947411.pdf.pdf"]
---

# Parallel-in-Time Simulation Algorithm
**作者**: Index Terms —Electro-magnetic transient simulation; parallel-in-time

## 摘要

Short.

## 核心贡献

- old

## 方法细节

该方法面向 MMC-HVDC 电磁暂态仿真的时间并行加速问题，将非线性开关系统组织为可迭代校正的并行时间区间以提升仿真吞吐。

## 验证详情

- **验证方式**: 与串行时间推进结果对比。

## 适用边界

- 适用于可分解为多个时间区间的电力电子 EMT 仿真。
"""
    paper_text = """# Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System
**Suman Debnath, Member, IEEE**

**Abstract**—The complexity in simulating power electronics requires simulation algorithms.
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: paper_text)

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert "authors: ['Suman Debnath']" in updated
    assert "Index Terms" not in updated
    assert 'journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics"' in updated


def test_repair_source_summaries_filters_ieee_membership_authors(monkeypatch):
    content = """---
title: "Copyright string"
type: source
authors: ['IEEE']
year: 2018
journal: ""
sources: ["EMT_Doc/01/Song 等 - 2018 - Efficient GPU EMT.pdf"]
---

# Copyright string
**作者**: IEEE

## 摘要

Short English.

## 核心贡献

- old

## 方法细节

提出面向线程的 GPU 电磁暂态仿真方法，将电气系统转换为基础元件网络并把控制系统组织为分层有向无环图，以减少线程分歧和访存开销。

## 验证详情

- **验证方式**: 与 CPU 基线程序对比。
- **测试系统**: IEEE 33 节点系统。

## 量化发现

- 原文报告 GPU 加速效果随系统规模增加更明显。

## 适用边界

- 适用于 GPU 并行 EMT 仿真。
"""
    paper_text = """# Efficient GPU-based Electromagnetic Transient Simulation for Power Systems
YANKAN SONG$^{1}$, YING CHEN$^{1}$, (Member, IEEE), SHAOWEI HUANG$^{1}$, (Member, IEEE), YIN XU$^{1}$, (Member, IEEE), ZHITONG YU$^{1}$, AND WEI XUE$^{2}$
VOLUME 7, 2019

Abstract Electromagnetic transients simulation is computationally intensive.
"""
    monkeypatch.setattr(repair_source_summaries, "extracted_text", lambda filename: paper_text)

    updated = repair_source_summaries.repair_content(content, "paper.md")

    assert "(Member" not in updated
    assert "$^" not in updated
    assert "IEEE)" not in updated
    assert "YANKAN SONG" in updated


def test_source_prompt_requires_evidence_backed_numbers():
    prompt = deep_enrich_sources.build_prompt(
        "full paper text",
        "enhanced paper text",
        "# Current\n\n## 摘要\nold",
    )

    assert "不得编造" in prompt
    assert "原文未报告可核验的数值结果" in prompt
    assert "applicability_boundaries" in prompt
    assert "适用边界" in deep_enrich_sources.REQUIRED_DEEP_SECTIONS


def test_source_enrichment_complete_allows_explicit_no_numeric_report():
    content = "\n".join(
        f"## {section}\n原文未报告可核验的数值结果。"
        for section in deep_enrich_sources.REQUIRED_DEEP_SECTIONS
    )

    assert deep_enrich_sources.has_complete_deep_enrichment(content) is True


def test_backrefs_normalize_alias_and_preserve_following_section(tmp_path):
    source_dir = tmp_path / "sources"
    source_dir.mkdir()
    source = source_dir / "paper.md"
    source.write_text(
        """---
title: "Aliased Paper"
year: 2024
---

## 使用的方法
- [[vector-fitting|矢量拟合]]
""",
        encoding="utf-8",
    )
    taxonomy = tmp_path / "vector-fitting.md"
    taxonomy.write_text(
        """# Vector Fitting

## 来源论文

| 论文 | 年份 |
|------|------|
| [[old|old]] | 2000 |

## 后续章节

keep me
""",
        encoding="utf-8",
    )

    links = build_backrefs.collect_wikilinks(str(source_dir))
    assert "vector-fitting" in links
    build_backrefs.update_page(str(taxonomy), links["vector-fitting"], "vector-fitting")

    content = taxonomy.read_text(encoding="utf-8")
    assert "[[paper|Aliased Paper]]" in content
    assert "## 后续章节" in content
    assert "keep me" in content


def test_taxonomy_uses_all_batches_and_dry_run_does_not_write(tmp_path):
    taxonomy = tmp_path / "topic.md"
    taxonomy.write_text("# Topic\n", encoding="utf-8")
    all_sources = {
        f"paper-{i}": (
            {"title": f"Paper {i}", "year": "2024", "core_contributions": "贡献", "simulation_results": "误差1%", "quantitative_findings": "1%"},
            ["topic"],
        )
        for i in range(31)
    }
    responses = ["batch one evidence", "batch two evidence", "final taxonomy"]
    llm = FakeLLM(responses)

    result = deep_enrich_taxonomy.process_taxonomy(taxonomy, "topic", all_sources, llm, dry_run=True)

    assert result[1] is True
    assert len(llm.prompts) == 3
    assert "覆盖31篇" in llm.prompts[-1]
    assert taxonomy.read_text(encoding="utf-8") == "# Topic\n"


def test_openai_client_uses_responses_http(monkeypatch):
    captured = {}

    class FakeHTTPResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return json.dumps({"output_text": "ok"}).encode("utf-8")

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url
        captured["timeout"] = timeout
        captured["headers"] = dict(request.header_items())
        captured["payload"] = json.loads(request.data.decode("utf-8"))
        return FakeHTTPResponse()

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    client = llm_client.OpenAILLMClient(model="gpt-test", api_key="test-key", base_url="https://api.example/v1")
    result = client.complete("prompt text", max_tokens=123, temperature=0.2, timeout=9.0)

    assert result == "ok"
    assert captured["url"] == "https://api.example/v1/responses"
    assert captured["headers"]["Authorization"] == "Bearer test-key"
    assert captured["payload"]["model"] == "gpt-test"
    assert captured["payload"]["input"] == "prompt text"
    assert captured["payload"]["max_output_tokens"] == 123


def test_codex_client_loads_config_and_auth(tmp_path, monkeypatch):
    codex_home = tmp_path / ".codex"
    codex_home.mkdir()
    config = codex_home / "config.toml"
    config.write_text(
        """model_provider = "codex"
model = "gpt-test"

[model_providers.codex]
base_url = "https://relay.example/v1"
wire_api = "responses"
""",
        encoding="utf-8",
    )
    (codex_home / "auth.json").write_text(json.dumps({"OPENAI_API_KEY": "test-key"}), encoding="utf-8")

    captured = {}

    class FakeHTTPResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def read(self):
            return json.dumps({"output_text": "ok"}).encode("utf-8")

    def fake_urlopen(request, timeout):
        captured["url"] = request.full_url
        captured["headers"] = dict(request.header_items())
        captured["payload"] = json.loads(request.data.decode("utf-8"))
        return FakeHTTPResponse()

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)
    monkeypatch.setenv("CODEX_CONFIG", str(config))

    client = llm_client.make_llm_client("codex")
    assert client.complete("hello", max_tokens=10, temperature=0.1, timeout=1) == "ok"
    assert captured["url"] == "https://relay.example/v1/responses"
    assert captured["headers"]["Authorization"] == "Bearer test-key"
    assert captured["payload"]["model"] == "gpt-test"


def test_ingest_dry_run_skips_existing_source(tmp_path, monkeypatch):
    sources = tmp_path / "sources"
    sources.mkdir()
    existing = sources / "existing.md"
    existing.write_text('---\nsources: ["EMT_Doc/01/paper.pdf"]\n---\n', encoding="utf-8")
    metadata = tmp_path / "metadata.json"
    metadata.write_text(
        json.dumps({
            "papers": [{
                "folder": "01",
                "title": "A Good Paper",
                "authors": "A. Author",
                "year": 2024,
                "subject": "Journal",
                "abstract": "This paper has an abstract long enough.",
                "relative_path": "01/paper.pdf",
                "file_path": str(tmp_path / "paper.pdf"),
            }]
        }),
        encoding="utf-8",
    )

    monkeypatch.setattr(ingest_folder, "SOURCES_DIR", str(sources))
    monkeypatch.setattr(ingest_folder, "METADATA_PATH", str(metadata))
    monkeypatch.setattr(ingest_folder, "LOG_PATH", str(tmp_path / "log.md"))

    result = ingest_folder.ingest_folder("01", dry_run=True)

    assert result["created"] == []
    assert result["updated"] == []
    assert len(result["skipped"]) == 1
    assert len(list(sources.glob("*.md"))) == 1


def test_ingest_dry_run_would_create_missing_source(tmp_path, monkeypatch):
    sources = tmp_path / "sources"
    sources.mkdir()
    metadata = tmp_path / "metadata.json"
    metadata.write_text(
        json.dumps({
            "papers": [{
                "folder": "02",
                "title": "Missing Source Paper",
                "authors": "A. Author",
                "year": 2025,
                "subject": "Journal",
                "abstract": "This paper has an abstract long enough.",
                "relative_path": "02/missing.pdf",
                "file_path": str(tmp_path / "missing.pdf"),
            }]
        }),
        encoding="utf-8",
    )

    monkeypatch.setattr(ingest_folder, "SOURCES_DIR", str(sources))
    monkeypatch.setattr(ingest_folder, "METADATA_PATH", str(metadata))
    monkeypatch.setattr(ingest_folder, "LOG_PATH", str(tmp_path / "log.md"))

    result = ingest_folder.ingest_folder("02", dry_run=True)

    assert result["created"] == ["missing-source-paper.md"]
    assert result["skipped"] == []
    assert not list(sources.glob("*.md"))


def test_quality_audit_scores_rich_source_higher_than_thin_source(tmp_path):
    rich = tmp_path / "rich.md"
    rich.write_text(
        """---
title: "Rich"
type: source
---

## 摘要
This paper solves interface errors in EMT simulation.

## 核心贡献
- 提出动态相量接口模型，降低换流器附近故障的接口误差。

## 使用的方法
- [[dynamic-phasor]]

## 涉及的模型
- [[vsc-model]]

## 相关主题
- [[co-simulation]]

## 主要发现
在 IEEE 39 节点系统中误差降低 35%，计算时间减少 20%。

## 方法细节
该方法输入三相电压电流，输出 Norton/Thevenin 等值参数。状态变量包括动态相量系数和接口节点电压。
算法先估计基频分量，再构造 DPIM，然后与 EMT 子系统交换接口变量。该流程说明了模型机制、变量和边界。
适用边界是假设接口附近频率分量可由有限阶动态相量表示，不适用于强非周期暂态。

## 仿真结果
| 系统 | 工具 | 结果 |
|---|---|---|
| IEEE 39 节点 | PSCAD/EMTDC | 误差 0.5%，速度提升 2 倍 |

## 量化发现
- 误差 0.5%
- 速度提升 2 倍
- 时间步长 50 us

## 关键公式
$$ V_k = \\frac{1}{T}\\int_{t-T}^{t} v(\\tau)e^{-jk\\omega\\tau}d\\tau $$

## 验证详情
- **验证方式**: 与 PSCAD/EMTDC 对比
- **测试系统**: IEEE 39 节点
- **仿真工具**: PSCAD
- **验证结果**: 误差 0.5%
""",
        encoding="utf-8",
    )
    thin = tmp_path / "thin.md"
    thin.write_text(
        """---
title: "Thin"
type: source
---

## 摘要
Short.

## 核心贡献
提高精度和效率。
""",
        encoding="utf-8",
    )

    rich_audit = audit_wiki_quality.audit_source(rich)
    thin_audit = audit_wiki_quality.audit_source(thin)

    assert rich_audit.score > thin_audit.score
    assert rich_audit.grade in {"A", "B"}
    assert "missing sections" in "; ".join(thin_audit.issues)


def test_quality_audit_skips_inactive_sources(tmp_path, monkeypatch):
    wiki = tmp_path / "wiki"
    sources = wiki / "sources"
    sources.mkdir(parents=True)
    active = sources / "active.md"
    active.write_text(
        """---
title: "Active"
type: source
---

## 摘要
active
""",
        encoding="utf-8",
    )
    duplicate = sources / "duplicate.md"
    duplicate.write_text("---\ntype: duplicate-source\n---\n", encoding="utf-8")
    out_of_scope = sources / "out-of-scope.md"
    out_of_scope.write_text("---\ntype: out-of-scope-source\n---\n", encoding="utf-8")
    for dirname in audit_wiki_quality.TAXONOMY_DIRS:
        (wiki / dirname).mkdir()

    monkeypatch.setattr(audit_wiki_quality, "WIKI_DIR", wiki)

    audits = audit_wiki_quality.collect_audits()

    assert [audit.path for audit in audits] == [str(active)]


def test_quality_audit_taxonomy_detects_synthesis(tmp_path):
    page = tmp_path / "method.md"
    page.write_text(
        """# Method

## 概述
该方法用于 EMT 仿真。

## 核心原理详解
公式 $$ i=C dv/dt $$ 描述状态更新。

## 性能分析
| 论文 | 结果 |
|---|---|
| [[paper-a]] | 误差 1%，速度 2 倍，50 us |

## 最佳实践与注意事项
适用边界包括线性化假设和固定步长限制。

## 开放问题
未来需要验证大规模系统。

## 来源论文
- [[paper-a]]
- [[paper-b]]
- [[paper-c]]
- [[paper-d]]
- [[paper-e]]
""",
        encoding="utf-8",
    )

    result = audit_wiki_quality.audit_taxonomy(page)

    assert result.score >= 65
    assert result.metrics["has_synthesis"] is True
    assert result.metrics["has_limits"] is True


def test_quality_audit_taxonomy_accepts_current_synthesis_structure(tmp_path):
    page = tmp_path / "topic.md"
    page.write_text(
        """# Topic

## 定义与概述
该主题解释 EMT 中的一个问题。

## 作用机制
核心形式为 $$ y = Gx + h $$，用于说明端口变量关系。

## 适用边界
适用边界包括模型假设和失败边界。

## 代表性来源
- [[paper-a]]
- [[paper-b]]
- [[paper-c]]

## 验证共识
验证通常需要 PSCAD 对比、误差 1% 和算例说明。

## 相关页面
[[paper-a]] [[paper-b]] [[paper-c]] [[paper-d]] [[paper-e]] [[paper-f]] [[paper-g]] [[paper-h]] [[paper-i]] [[paper-j]]
""",
        encoding="utf-8",
    )

    result = audit_wiki_quality.audit_taxonomy(page)

    assert result.metrics["has_synthesis"] is True
    assert "may be mostly index/list content" not in result.issues


def test_quality_audit_entities_are_singular_entity(tmp_path):
    entity_dir = tmp_path / "entities"
    entity_dir.mkdir()
    page = entity_dir / "tool.md"
    page.write_text(
        """# Tool

## 概述
This tool is used in EMT simulation.
""",
        encoding="utf-8",
    )

    result = audit_wiki_quality.audit_taxonomy(page)

    assert result.page_type == "entity"


def test_strict_audit_flags_source_review_risks(tmp_path):
    page = tmp_path / "risky.md"
    page.write_text(
        """---
title: "untitled"
type: source
authors: ['未知']
journal: ""
---

# Risky

## 摘要
Short.

## 核心贡献
提高精度。
""",
        encoding="utf-8",
    )

    result = audit_wiki_strict.audit_source(page)

    assert result is not None
    assert result.score >= 50
    assert "bad or placeholder author metadata" in result.issues
    assert "missing explicit applicability boundary section" in result.issues


def test_strict_audit_flags_likely_out_of_scope_active_source(tmp_path):
    page = tmp_path / "oncology.md"
    page.write_text(
        """---
title: "j.epsr placeholder"
type: source
authors: ['未知']
journal: ""
---

# Placeholder

## 摘要
Annals of Oncology clinical study about colon cancer chemotherapy.

## 核心贡献
This is a clinical oncology abstract, not an EMT simulation paper.
""",
        encoding="utf-8",
    )

    result = audit_wiki_strict.audit_source(page)

    assert result is not None
    assert "likely out-of-scope extracted content" in result.issues


def test_strict_audit_skips_inactive_sources(tmp_path):
    duplicate = tmp_path / "duplicate.md"
    duplicate.write_text("---\ntype: duplicate-source\n---\n", encoding="utf-8")

    assert audit_wiki_strict.audit_source(duplicate) is None


def test_strict_audit_accepts_declared_journal_gap_and_numeric_evidence(tmp_path):
    page = tmp_path / "source.md"
    page.write_text(
        """---
title: "Paper"
type: source
authors: ['A. Author']
journal: ""
---

# Paper

## 摘要
本文提出一种电磁暂态仿真方法，面向大规模网络等值和多时间尺度暂态分析，说明了问题、机制与验证路径。该方法以频率相关网络等值为核心，把外部系统压缩为端口响应模型，并在仿真步长循环中保持与详细模型可比较的电压、电流接口。页面明确记录验证系统、量化误差和期刊字段缺口，因此空期刊不应再被视为未处理的内容质量问题；后续只需回到 PDF 首页或 DOI 记录补齐出版源。

## 核心贡献
- 问题定位：解决大规模 EMT 仿真中外部网络详细建模计算量过大、重复多案例计算成本过高的问题。
- 方法机制：用频率相关等值网络替代外部系统，并在 EMTP 时间步中更新端口响应，使研究区域仍保留电压、电流接口变量。
- 验证证据：在 IEEE 39 节点系统中与 PSCAD 基线对比，量化记录误差和计算速度，避免把概括性“有效”当作唯一证据。

## 量化发现
- 误差 0.5%，速度提升 2 倍。

## 验证详情
- **测试系统**: IEEE 39 节点。

## 适用边界
### 证据缺口
- 期刊/会议元数据未在当前页面中可靠给出。
""",
        encoding="utf-8",
    )

    result = audit_wiki_strict.audit_source(page)

    assert result is not None
    assert "blank journal metadata" not in result.issues
    assert "strong numeric or quality claims need evidence check" not in result.issues
    assert "missing reader-facing deep review" in result.issues


def test_strict_audit_accepts_complete_deep_review(tmp_path):
    page = tmp_path / "source.md"
    review_body = "\n".join(
        [
            "<!-- deep-review:start -->",
            "## 研究解读",
            "",
            "### 1. 需求、对象、挑战与贡献",
            "大规模电磁暂态仿真需要在保留接口电压电流响应的同时降低外部网络计算量。研究对象是频率相关网络等值模型，挑战在于宽频响应、无源性和混合仿真接口同时约束模型。本文贡献是把端口频响拟合为可进入EMT时间步的等值网络，并用基线仿真对比验证接口响应。这个说明还明确区分了研究区域和外部系统：研究区域保留详细EMT模型，外部系统通过等值端口进入求解，因此读者可以理解为什么该方法不是普通降阶，而是面向混合仿真接口的网络等值。",
            "",
            "### 2. 模型、算法与实现技术",
            "模型以端口电压、电流和频率相关导纳为核心接口量，通过拟合外部系统频域响应并转化为时域递推项嵌入EMTP求解。算法流程包括端口选择、频响采样、向量拟合、无源性处理和时间步接口更新。端口导纳函数负责描述外部网络在宽频范围内对研究区域的响应，时域递推项负责把该频域模型放进离散时间步计算。无源性处理用于避免等值网络在暂态仿真中注入非物理能量，接口更新则保证每个时步的端口电压和电流仍能与详细网络基线比较。",
            "",
            "### 3. 验证、优势与不足",
            "验证使用IEEE 39节点系统和PSCAD基线，报告0.5%误差和2倍速度提升。优势是降低外部网络重复求解成本并保留接口波形；不足是未覆盖所有拓扑变化、强非线性设备和保护动作。该验证能够支持“在给定测试系统和扰动条件下，等值模型可近似详细模型”的结论，但不能支持“所有外部网络都可安全替换”的结论。若后续页面要复用该方法，需要重新核对端口数量、拟合频带、扰动类型和原文是否包含保护/控制器切换场景。",
            "",
            "### 4. 价值、认知与可复用场景",
            "该工作说明混合仿真精度瓶颈不仅来自步长，也来自接口等值的频率响应。它适合支撑网络等值、混合仿真和频率相关建模页面，但不能直接外推到未验证的暂态保护或器件级开关过程。它的复用价值在于提供一种判断框架：如果研究目标只需要外部网络在端口处的宽频响应，则可以考虑FDNE；如果目标是外部网络内部保护动作、非线性饱和或开关器件行为，则必须回到更详细模型或重新验证等值误差。",
            "",
            "### 证据边界",
            "- 测试系统和误差来自页面给出的验证段。",
            "- 未覆盖场景来自验证范围外推，需标注为边界判断。",
            "- 深审块还必须说明哪些信息不能从当前页面升级为确定结论，例如保护动作、非线性设备、端口选择规则和频带范围都需要回到原文或实验设置复核。",
            "- 该样例故意保持完整结构和足够长度，避免只有标题齐全但内容过短的页面被严格审计误判为已深审。",
            "<!-- deep-review:end -->",
        ]
    )
    page.write_text(
        f"""---
title: "Paper"
type: source
authors: ['A. Author']
journal: ""
---

# Paper

## 摘要
本文提出一种电磁暂态仿真方法，面向大规模网络等值和多时间尺度暂态分析，说明了问题、机制与验证路径。该方法以频率相关网络等值为核心，把外部系统压缩为端口响应模型，并在仿真步长循环中保持与详细模型可比较的电压、电流接口。页面明确记录验证系统、量化误差和期刊字段缺口，因此空期刊不应再被视为未处理的内容质量问题；后续只需回到 PDF 首页或 DOI 记录补齐出版源。

{review_body}

## 核心贡献
- 问题定位：解决大规模 EMT 仿真中外部网络详细建模计算量过大、重复多案例计算成本过高的问题。
- 方法机制：用频率相关等值网络替代外部系统，并在 EMTP 时间步中更新端口响应，使研究区域仍保留电压、电流接口变量。
- 验证证据：在 IEEE 39 节点系统中与 PSCAD 基线对比，量化记录误差和计算速度，避免把概括性“有效”当作唯一证据。

## 量化发现
- 误差 0.5%，速度提升 2 倍。

## 验证详情
- **测试系统**: IEEE 39 节点。

## 适用边界
### 证据缺口
- 期刊/会议元数据未在当前页面中可靠给出。
""",
        encoding="utf-8",
    )

    assert audit_wiki_strict.audit_source(page) is None


def test_deep_review_manifest_selects_only_listed_active_files(tmp_path, monkeypatch):
    source_dir = tmp_path / "wiki" / "sources"
    source_dir.mkdir(parents=True)
    checkpoint = tmp_path / "checkpoint.json"
    manifest = tmp_path / "manifest.txt"
    selected = source_dir / "selected.md"
    skipped_done = source_dir / "done.md"
    skipped_inactive = source_dir / "inactive.md"
    unlisted = source_dir / "unlisted.md"
    selected.write_text("---\ntype: source\n---\n# Selected\n", encoding="utf-8")
    skipped_done.write_text("---\ntype: source\n---\n# Done\n", encoding="utf-8")
    skipped_inactive.write_text("---\ntype: duplicate-source\n---\n# Duplicate\n", encoding="utf-8")
    unlisted.write_text("---\ntype: source\n---\n# Unlisted\n", encoding="utf-8")
    checkpoint.write_text(json.dumps({"done": ["done.md"], "failed": []}), encoding="utf-8")
    manifest.write_text(
        "\n".join(
            [
                "wiki/sources/selected.md",
                "wiki/sources/done.md",
                "wiki/sources/inactive.md",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(deep_review_sources, "ROOT", tmp_path)
    monkeypatch.setattr(deep_review_sources, "WIKI_SOURCES", source_dir)

    files = deep_review_sources.select_files(0, False, False, checkpoint, manifest)

    assert files == [selected]


def test_deep_review_writes_custom_checkpoint_and_report(tmp_path):
    checkpoint = tmp_path / "nested" / "checkpoint.json"
    report = tmp_path / "reports" / "run.json"

    deep_review_sources.save_checkpoint({"done": ["paper.md"], "failed": []}, checkpoint)
    loaded = deep_review_sources.load_checkpoint(checkpoint)
    deep_review_sources.write_report(report, [{"name": "paper.md", "ok": True, "message": "reviewed"}], 1.25)
    report_data = json.loads(report.read_text(encoding="utf-8"))

    assert loaded["done"] == ["paper.md"]
    assert report_data["counts"] == {"items": 1, "ok": 1, "failed": 0}


def test_deep_review_run_records_worker_exceptions(tmp_path, monkeypatch):
    source_dir = tmp_path / "wiki" / "sources"
    source_dir.mkdir(parents=True)
    source = source_dir / "paper.md"
    source.write_text("---\ntype: source\n---\n# Paper\n", encoding="utf-8")
    manifest = tmp_path / "manifest.txt"
    manifest.write_text("wiki/sources/paper.md\n", encoding="utf-8")
    checkpoint = tmp_path / "checkpoint.json"
    report = tmp_path / "report.json"

    monkeypatch.setattr(deep_review_sources, "ROOT", tmp_path)
    monkeypatch.setattr(deep_review_sources, "WIKI_SOURCES", source_dir)
    monkeypatch.setattr(deep_review_sources, "make_llm_client", lambda provider=None, model=None: object())

    def fail_process(*args, **kwargs):
        raise RuntimeError("quota exhausted")

    monkeypatch.setattr(deep_review_sources, "process_file", fail_process)
    args = type(
        "Args",
        (),
        {
            "limit": 0,
            "force": False,
            "retry_failed": False,
            "checkpoint": checkpoint,
            "manifest": manifest,
            "llm_provider": "codex",
            "model": None,
            "concurrency": 1,
            "dry_run": False,
            "report": report,
        },
    )()

    deep_review_sources.run(args)
    checkpoint_data = json.loads(checkpoint.read_text(encoding="utf-8"))
    report_data = json.loads(report.read_text(encoding="utf-8"))

    assert checkpoint_data == {"done": [], "failed": ["paper.md"]}
    assert report_data["counts"] == {"items": 1, "ok": 0, "failed": 1}
    assert "quota exhausted" in report_data["items"][0]["message"]


def test_strict_audit_flags_taxonomy_structure(tmp_path, monkeypatch):
    wiki = tmp_path / "wiki"
    topics = wiki / "topics"
    topics.mkdir(parents=True)
    page = topics / "topic.md"
    page.write_text(
        """# Topic
# Topic Again

## 概述
brief

[[missing-page]]
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(audit_wiki_strict, "WIKI_DIR", wiki)

    result = audit_wiki_strict.audit_taxonomy(page)

    assert result is not None
    assert "duplicate or missing H1" in result.issues
    assert "missing boundaries or limitations" in result.issues
    assert "contains missing wikilinks" in result.issues
    assert result.page_type == "topic"


def test_strict_audit_entities_are_singular_entity(tmp_path):
    entity_dir = tmp_path / "entities"
    entity_dir.mkdir()
    page = entity_dir / "tool.md"
    page.write_text(
        """# Tool

## 概述
This tool is used in EMT simulation.
""",
        encoding="utf-8",
    )

    result = audit_wiki_strict.audit_taxonomy(page)

    assert result is not None
    assert result.page_type == "entity"

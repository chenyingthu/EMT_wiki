# EMT Wiki Quality Standard

This document defines what it means for the EMT Wiki to "understand" a paper,
method, model, or topic. More text is not automatically better. A good page
should make the technical position, mechanism, evidence, and limits clear.

## Quality Levels

### C: Indexable

The page is usable for search and navigation.

- Has title, source metadata, abstract or overview.
- Has basic wikilinks to methods, models, topics, or related source pages.
- Has at least a short contribution or summary.
- May still be generic, shallow, or missing experimental detail.

### B: Understandable

The page explains the work well enough for a reader to know what is being done
and why it matters.

- States the concrete EMT problem or bottleneck.
- Explains the proposed method/model/mechanism, not only the outcome.
- Names inputs, outputs, state variables, interface variables, or model objects
  where relevant.
- Includes key equations, algorithm steps, or parameter rules when the paper is
  mathematical or algorithmic.
- Gives validation evidence: test system, simulator/tool, baseline, metric, and
  numerical result when available.
- States assumptions or applicability limits.

### A: Reusable

The page is good enough to support technical reuse or comparison.

- A reader can identify when to use or avoid the method/model.
- The page separates paper evidence from inference.
- Key equations and algorithm steps are connected to their role in the method.
- Quantitative results are specific and comparable.
- Limitations and unvalidated cases are explicit.
- Cross-links explain why a method/model/topic is related, not just that it is.

## Source Page Criteria

Each active source page should answer:

1. What concrete EMT problem does the paper solve?
2. What existing limitation motivates the work?
3. What is the proposed method/model and how does it work?
4. What are the assumptions and applicability boundaries?
5. What equations, algorithm steps, or model structures are central?
6. What test system, simulator, baseline, metric, and numerical result support it?
7. What are the paper's true contributions versus generated inference?
8. Which topic/method/model pages should this paper support, and why?

Minimum B-level source pages should include these sections:

- `## 核心贡献`
- `## 使用的方法`
- `## 涉及的模型`
- `## 相关主题`
- `## 主要发现`
- `## 方法细节`
- `## 仿真结果`
- `## 量化发现`
- `## 关键公式`
- `## 验证详情`

## Taxonomy Page Criteria

Topic, method, model, and entity pages should be synthesis pages, not paper
lists. A good taxonomy page should answer:

1. What is the concept/method/model?
2. Why is it important in EMT simulation?
3. What are the main branches or variants?
4. What mathematical form or algorithmic pattern defines it?
5. What problems does it solve well, and where does it fail?
6. Which source papers are representative, and what did each add?
7. What trends, unresolved problems, or engineering tradeoffs remain?

## Red Flags

These patterns lower quality:

- Generic claims such as "提高精度和效率" without the specific mechanism.
- Results described only as "一致", "良好", or "有效" without metrics or setup.
- Contributions inferred from tags rather than supported by source text.
- Taxonomy pages that are mostly long source tables without synthesis.
- Equations pasted without explaining what variables mean or why the equation matters.
- Missing limitations or assumptions.
- Duplicate source pages treated as independent evidence.

## Audit Scoring

The audit script assigns each page a score from 0 to 100.

- A: 85-100
- B: 65-84
- C: 40-64
- D: 0-39

Scores are only triage signals. Human review is required before major rewrites
or claims of final quality.

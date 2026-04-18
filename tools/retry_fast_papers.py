#!/home/chenying/anaconda3/bin/python3
"""
Fast re-analysis for low-quality papers using pdftotext + LLM.
"""

import os
import re
import json
import subprocess
import time
from pathlib import Path

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://coding.dashscope.aliyuncs.com/apps/anthropic"),
)

WIKI_SOURCES = Path("wiki/sources")
CHECKPOINT = Path(".retry_fast.json")

TAXONOMY_WIKILINKS = {
    'mmc': '[[mmc-model|MMC]]', 'mmc-model': '[[mmc-model|MMC]]',
    'vsc': '[[vsc-model|VSC]]', 'vsc-model': '[[vsc-model|VSC]]',
    'lcc': '[[lcc-model|LCC]]', 'lcc-model': '[[lcc-model|LCC]]',
    'dfig': '[[dfig-model|DFIG]]', 'dfig-model': '[[dfig-model|DFIG]]',
    'pmsm': '[[pmsm-model|PMSM]]', 'pmsm-model': '[[pmsm-model|PMSM]]',
    'transformer': '[[transformer-model|变压器]]',
    'transmission-line': '[[transmission-line-model|输电线路]]',
    'synchronous-machine': '[[synchronous-machine-model|同步电机]]',
    'fdne': '[[fdne-model|FDNE]]', 'cable': '[[cable-model|电缆]]',
    'co-simulation': '[[co-simulation|混合仿真]]',
    'real-time': '[[real-time-simulation|实时仿真]]',
    'dynamic-phasor': '[[dynamic-phasor|动态相量法]]',
    'parallel': '[[parallel-computing|并行计算]]',
    'frequency-dependent': '[[frequency-dependent-modeling|频率相关建模]]',
    'network-equivalent': '[[network-equivalent|网络等值]]',
    'vsc-hvdc': '[[vsc-hvdc|VSC-HVDC]]', 'hvdc': '[[vsc-hvdc|VSC-HVDC]]',
    'ferroresonance': '[[ferroresonance|铁磁谐振]]',
    'harmonic': '[[harmonic-analysis|谐波分析]]',
    'wind-farm': '[[wind-farm-modeling|风电场建模]]',
    'vector-fitting': '[[vector-fitting|矢量拟合]]',
    'average-value-model': '[[average-value-model|平均值模型]]',
    'nodal-analysis': '[[nodal-analysis|节点分析]]',
    'state-space': '[[state-space-method|状态空间法]]',
    'numerical-integration': '[[numerical-integration|数值积分]]',
    'passivity': '[[passivity-enforcement|无源性强制]]',
    'multirate': '[[multirate-method|多速率方法]]',
    'fixed-admittance': '[[fixed-admittance|恒导纳模型]]',
    'interpolation': '[[interpolation-method|插值方法]]',
    'prony': '[[prony-analysis|Prony 分析]]',
}

checkpoint = {"done": [], "failed": [], "skipped": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed")

done_set = set(checkpoint.get('done', []))


def is_low_quality(filepath: Path) -> bool:
    content = filepath.read_text(encoding='utf-8')
    if len(content) < 1000:
        return True
    cc_match = re.search(r'## 核心贡献\n+\n*(.+?)\n+##', content, re.DOTALL)
    if cc_match:
        cc_text = cc_match.group(1)
        bullet_count = len([l for l in cc_text.split('\n') if l.strip().startswith('-')])
        if bullet_count < 2:
            return True
    return False


def extract_with_pdftotext(pdf_path: str) -> str:
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=30
        )
        return result.stdout[:20000]
    except Exception as e:
        print(f"pdftotext error: {e}")
        return ""


def analyze_with_llm(title: str, abstract: str, full_text: str) -> dict:
    # Use Chinese prompt for better results
    content = f"论文标题：{title}\n"
    if abstract:
        content += f"摘要：{abstract}\n"
    if full_text:
        content += f"\n论文内容（前 5 页）：\n{full_text[:5000]}"

    prompt = f"""分析以下 EMT 仿真领域论文，用中文输出 JSON。

```json
{{
  "core_contributions": ["核心贡献 1", "核心贡献 2"],
  "methods": ["[[方法 wikilink]]", ...],
  "models": ["[[模型 wikilink]]", ...],
  "topics": ["[[主题 wikilink]]", ...],
  "key_findings": ["主要发现 1", "主要发现 2"]
}}
```

可用 wikilink: {', '.join(TAXONOMY_WIKILINKS.keys())}

只输出 JSON，不要其他文字。

{content}"""

    try:
        response = client.messages.create(
            model="qwen3.6-plus",
            max_tokens=1500,
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}],
        )
        # Parse response
        text_result = ""
        for block in response.content:
            if hasattr(block, 'text') and block.text:
                text_result = block.text.strip()
                break
            elif hasattr(block, 'content'):
                text_result = str(block.content).strip()
                break

        if not text_result:
            return {"error": "Empty response"}

        json_match = re.search(r'```json\s*\n?(.*?)\n?```', text_result, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        return json.loads(text_result)
    except Exception as e:
        return {"error": str(e)}


def update_source_file(filepath: Path, analysis: dict) -> bool:
    try:
        content = filepath.read_text(encoding='utf-8')
        sections = {
            'core_contributions': '## 核心贡献',
            'methods': '## 使用的方法',
            'models': '## 涉及的模型',
            'topics': '## 相关主题',
            'key_findings': '## 主要发现',
        }

        for key, header in sections.items():
            if key not in analysis:
                continue
            items = analysis[key]
            if isinstance(items, list) and items:
                if key in ['methods', 'models', 'topics']:
                    new_content = '\n- ' + '\n- '.join(str(i) for i in items)
                else:
                    new_content = '\n\n- ' + '\n- '.join(str(i) for i in items)

                pattern = rf'({header}\n+\n*)(.*?)(\n+## |\Z)'
                content = re.sub(pattern, lambda m: m.group(1) + new_content + (m.group(3) if m.group(3).strip() else ''), content, flags=re.DOTALL)

        filepath.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Update failed: {e}")
        return False


def get_pdf_path(filepath: Path) -> str:
    content = filepath.read_text(encoding='utf-8')
    match = re.search(r'sources:\s*\["([^"]*EMT_Doc[^"]*)"\]', content)
    if match:
        pdf_rel_path = match.group(1)
        pdf_path = f"/home/chenying/researches/EMT_LLM_Wiki/{pdf_rel_path}"
        if os.path.exists(pdf_path):
            return pdf_path
    return None


def get_abstract(filepath: Path) -> str:
    content = filepath.read_text(encoding='utf-8')
    match = re.search(r'## 摘要\n+\n*(.+?)(\n+## |\Z)', content, re.DOTALL)
    return match.group(1).strip() if match else ""


def save_checkpoint():
    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)


# Main
print("=" * 60)
print("Scanning for low-quality papers...")
print("=" * 60)

lowquality_papers = []
for src_file in WIKI_SOURCES.glob("*.md"):
    if src_file.name in done_set:
        continue
    if is_low_quality(src_file):
        pdf_path = get_pdf_path(src_file)
        if pdf_path:
            lowquality_papers.append((src_file, pdf_path))
        else:
            checkpoint['skipped'].append(src_file.name)

print(f"Found {len(lowquality_papers)} low-quality papers")
print(f"Estimated time: {len(lowquality_papers) * 0.1:.1f} minutes")

if not lowquality_papers:
    print("No papers to process!")
    exit(0)

print("\n" + "=" * 60)
total = len(lowquality_papers)
count = len(checkpoint['done'])
start_time = time.time()

for idx, (src_file, pdf_path) in enumerate(lowquality_papers):
    count += 1
    filename = src_file.name
    elapsed = (time.time() - start_time) / 60

    print(f"[{count}/{total}] {filename[:50]}... ", end='', flush=True)

    text = extract_with_pdftotext(pdf_path)
    if not text:
        print("pdftotext FAILED")
        checkpoint['failed'].append(filename)
        save_checkpoint()
        continue

    print(f"pdftotext: {len(text)} chars, ", end='', flush=True)

    abstract = get_abstract(src_file)
    title = src_file.stem.replace('-', ' ')
    analysis = analyze_with_llm(title, abstract, text)

    if 'error' in analysis:
        print(f"LLM error: {analysis['error']}")
        checkpoint['failed'].append(filename)
    else:
        if update_source_file(src_file, analysis):
            cc = len(analysis.get('core_contributions', []))
            kf = len(analysis.get('key_findings', []))
            print(f"✅ cc={cc}, findings={kf}")
            checkpoint['done'].append(filename)
        else:
            print("Update failed")
            checkpoint['failed'].append(filename)

    save_checkpoint()

elapsed = (time.time() - start_time) / 60
print(f"\n{'=' * 60}")
print(f"Completed in {elapsed:.1f} minutes")
print(f"Done: {len(checkpoint['done'])}")
print(f"Failed: {len(checkpoint['failed'])}")
print(f"Skipped: {len(checkpoint['skipped'])}")

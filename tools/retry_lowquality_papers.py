#!/home/chenying/anaconda3/bin/python3
"""
Retry MinerU extraction + LLM analysis for low-quality papers.

Strategy:
1. Identify low-quality papers:
   - Content length < 1000 chars OR
   - Core contributions < 2 items OR
   - Key findings < 1 item
2. Re-extract PDF using MinerU API (with longer timeout)
3. Re-analyze with LLM using full PDF text
4. Update source file with new analysis
"""

import os
import re
import json
import time
import requests
from pathlib import Path

MINERU_API = "http://localhost:8000"
WIKI_SOURCES = Path("wiki/sources")
CHECKPOINT = Path(".retry_lowquality.json")

# Anthropic API client
import anthropic
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://coding.dashscope.aliyuncs.com/apps/anthropic"),
)

# Load checkpoint
checkpoint = {"done": [], "failed": [], "skipped": []}
if CHECKPOINT.exists():
    with open(CHECKPOINT, 'r') as f:
        checkpoint = json.load(f)
    print(f"Loaded checkpoint: {len(checkpoint['done'])} done, {len(checkpoint['failed'])} failed, {len(checkpoint['skipped'])} skipped")

done_set = set(checkpoint.get('done', []))

# Taxonomy wikilinks for validation
TAXONOMY_WIKILINKS = {
    'mmc': '[[mmc-model|MMC]]', 'mmc-model': '[[mmc-model|MMC]]',
    'vsc': '[[vsc-model|VSC]]', 'vsc-model': '[[vsc-model|VSC]]',
    'lcc': '[[lcc-model|LCC]]', 'lcc-model': '[[lcc-model|LCC]]',
    'dfig': '[[dfig-model|DFIG]]', 'dfig-model': '[[dfig-model|DFIG]]',
    'pmsm': '[[pmsm-model|PMSM]]', 'pmsm-model': '[[pmsm-model|PMSM]]',
    'transformer': '[[transformer-model|变压器]]', 'transformer-model': '[[transformer-model|变压器]]',
    'transmission-line': '[[transmission-line-model|输电线路]]', 'transmission-line-model': '[[transmission-line-model|输电线路]]',
    'synchronous-machine': '[[synchronous-machine-model|同步电机]]', 'synchronous-machine-model': '[[synchronous-machine-model|同步电机]]',
    'fdne': '[[fdne-model|FDNE]]', 'fdne-model': '[[fdne-model|FDNE]]',
    'cable': '[[cable-model|电缆]]', 'cable-model': '[[cable-model|电缆]]',
    'co-simulation': '[[co-simulation|混合仿真]]', 'cosimulation': '[[co-simulation|混合仿真]]',
    'real-time': '[[real-time-simulation|实时仿真]]', 'realtime': '[[real-time-simulation|实时仿真]]',
    'dynamic-phasor': '[[dynamic-phasor|动态相量法]]', 'dynamic phasor': '[[dynamic-phasor|动态相量法]]',
    'parallel': '[[parallel-computing|并行计算]]', 'parallel-computing': '[[parallel-computing|并行计算]]',
    'frequency-dependent': '[[frequency-dependent-modeling|频率相关建模]]', 'freq-dependent': '[[frequency-dependent-modeling|频率相关建模]]',
    'network-equivalent': '[[network-equivalent|网络等值]]', 'net-equivalent': '[[network-equivalent|网络等值]]',
    'vsc-hvdc': '[[vsc-hvdc|VSC-HVDC]]', 'hvdc': '[[vsc-hvdc|VSC-HVDC]]',
    'ferroresonance': '[[ferroresonance|铁磁谐振]]',
    'harmonic': '[[harmonic-analysis|谐波分析]]', 'harmonic-analysis': '[[harmonic-analysis|谐波分析]]',
    'wind-farm': '[[wind-farm-modeling|风电场建模]]', 'wind-farm-modeling': '[[wind-farm-modeling|风电场建模]]',
    'vector-fitting': '[[vector-fitting|矢量拟合]]',
    'average-value-model': '[[average-value-model|平均值模型]]', 'avm': '[[average-value-model|平均值模型]]',
    'nodal-analysis': '[[nodal-analysis|节点分析]]',
    'state-space': '[[state-space-method|状态空间法]]',
    'numerical-integration': '[[numerical-integration|数值积分]]', 'trapezoidal': '[[numerical-integration|数值积分]]',
    'passivity': '[[passivity-enforcement|无源性强制]]', 'passivity-enforcement': '[[passivity-enforcement|无源性强制]]',
    'multirate': '[[multirate-method|多速率方法]]', 'multi-rate': '[[multirate-method|多速率方法]]',
    'fixed-admittance': '[[fixed-admittance|恒导纳模型]]', 'nodal': '[[fixed-admittance|恒导纳模型]]',
    'interpolation': '[[interpolation-method|插值方法]]',
    'prony': '[[prony-analysis|Prony 分析]]',
}


def is_low_quality(filepath: Path) -> bool:
    """Check if a source file has low quality content"""
    content = filepath.read_text(encoding='utf-8')

    # Check content length
    if len(content) < 1000:
        return True

    # Check core contributions count
    cc_match = re.search(r'## 核心贡献\n+\n*(.+?)\n+##', content, re.DOTALL)
    if cc_match:
        cc_text = cc_match.group(1)
        bullet_count = len([l for l in cc_text.split('\n') if l.strip().startswith('-')])
        if bullet_count < 2:
            return True

    # Check key findings count
    kf_match = re.search(r'## 主要发现\n+\n*(.+?)\n+##', content, re.DOTALL)
    if kf_match:
        kf_text = kf_match.group(1)
        bullet_count = len([l for l in kf_text.split('\n') if l.strip().startswith('-')])
        if bullet_count < 1:
            return True

    return False


def save_checkpoint():
    with open(CHECKPOINT, 'w') as f:
        json.dump(checkpoint, f, indent=2, ensure_ascii=False)


def extract_with_mineru(pdf_path: str, timeout_min: int = 20) -> tuple[str, bool]:
    """Extract text using MinerU API. Returns (text, success)"""
    try:
        with open(pdf_path, 'rb') as f:
            files = {'files': (os.path.basename(pdf_path), f, 'application/pdf')}
            data = {
                'backend': 'pipeline',
                'return_md': 'true',
                'formula_enable': 'true',
                'table_enable': 'true'
            }
            response = requests.post(f"{MINERU_API}/tasks", files=files, data=data, timeout=60)

        if response.status_code != 202:
            print(f"Submit failed: {response.status_code}")
            return "", False

        task_id = response.json().get('task_id')
        if not task_id:
            return "", False

        print(f"Task {task_id[:8]} submitted", end='', flush=True)

        # Poll for result (max timeout_min minutes)
        max_polls = timeout_min * 12  # 5 seconds per poll
        for i in range(max_polls):
            time.sleep(5)
            result = requests.get(f"{MINERU_API}/tasks/{task_id}/result", timeout=30)
            if result.status_code == 200:
                data = result.json()
                status = data.get('status', 'unknown')
                if status == 'completed':
                    markdown = data.get('markdown', '')
                    if markdown:
                        print(f" done! {len(markdown)} chars")
                        return markdown[:20000], True
                    else:
                        print(" done but empty")
                        return "", False
                elif status == 'failed':
                    print(f" failed: {data.get('message', 'unknown')}")
                    return "", False
                else:
                    if i % 12 == 0:  # Print every minute
                        print(f" {status}({i//12+1}m)...", end='', flush=True)

        print(f" timeout after {timeout_min} min")
        return "", False
    except Exception as e:
        print(f" error: {e}")
        return "", False


def analyze_with_llm(title: str, abstract: str, full_text: str) -> dict:
    """Analyze paper content using LLM"""

    # Build prompt with full text
    text_preview = full_text[:8000] if len(full_text) > 8000 else full_text

    prompt = f"""You are a power systems expert analyzing academic papers on electromagnetic transient (EMT) simulation.

Paper Title: {title}

Abstract:
{abstract}

Full Text (extracted from PDF):
{text_preview}

Analyze this paper and extract the following information in JSON format:

1. **core_contributions** (array of 2-4 strings): Key novel contributions of this paper
2. **methods** (array of wikilinks): Simulation methods used, e.g., [[state-space-method]], [[nodal-analysis]], [[average-value-model]]
3. **models** (array of wikilinks): Component models studied, e.g., [[mmc-model]], [[vsc-model]], [[transmission-line-model]]
4. **topics** (array of wikilinks): Research topics, e.g., [[real-time-simulation]], [[co-simulation]], [[harmonic-analysis]]
5. **key_findings** (array of 2-4 strings): Main experimental/analytical findings

Use these valid wikilinks: {', '.join(TAXONOMY_WIKILINKS.keys())}

Return ONLY valid JSON:
```json
{{
  "core_contributions": ["...", "..."],
  "methods": ["[[...]]", "..."],
  "models": ["[[...]]", "..."],
  "topics": ["[[...]]", "..."],
  "key_findings": ["...", "..."]
}}
```"""

    try:
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        # Parse JSON from response
        text = response.content[0].text
        json_match = re.search(r'```json\s*(.+?)\s*```', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        else:
            return json.loads(text)
    except Exception as e:
        return {"error": str(e)}


def update_source_file(filepath: Path, analysis: dict) -> bool:
    """Update source file with new analysis"""
    try:
        content = filepath.read_text(encoding='utf-8')

        # Update each section
        sections = {
            'core_contributions': ('## 核心贡献', '\n\n- '),
            'methods': ('## 使用的方法', '\n\n- '),
            'models': ('## 涉及的模型', '\n\n- '),
            'topics': ('## 相关主题', '\n\n- '),
            'key_findings': ('## 主要发现', '\n\n- '),
        }

        for key, (header, prefix) in sections.items():
            if key not in analysis:
                continue

            items = analysis[key]
            if isinstance(items, list):
                new_section = header + prefix + '\n- '.join(items) + '\n\n'

                # Find and replace section
                pattern = rf'({header}\n+\n*)(.*?)(\n+##|\Z)'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    content = re.sub(pattern, lambda m: new_section + m.group(3), content, flags=re.DOTALL)

        filepath.write_text(content, encoding='utf-8')
        return True
    except Exception as e:
        print(f"Update failed: {e}")
        return False


def get_pdf_path(filepath: Path) -> str:
    """Extract PDF path from source file"""
    content = filepath.read_text(encoding='utf-8')

    match = re.search(r'sources:\s*\["([^"]*EMT_Doc[^"]*)"\]', content)
    if match:
        pdf_rel_path = match.group(1)
        pdf_path = f"/home/chenying/researches/EMT_LLM_Wiki/{pdf_rel_path}"
        if os.path.exists(pdf_path):
            return pdf_path

    return None


def get_abstract(filepath: Path) -> str:
    """Extract abstract from source file"""
    content = filepath.read_text(encoding='utf-8')
    match = re.search(r'## 摘要\n+\n*(.+?)(\n+##|\Z)', content, re.DOTALL)
    return match.group(1).strip() if match else ""


# Main processing
print("=" * 60)
print("Scanning for low-quality papers...")
print("=" * 60)

lowquality_papers = []

for src_file in WIKI_SOURCES.glob("*.md"):
    if src_file.name in done_set:
        continue  # Already retried

    if is_low_quality(src_file):
        pdf_path = get_pdf_path(src_file)
        if pdf_path:
            lowquality_papers.append((src_file, pdf_path))
        else:
            print(f"  SKIP (PDF not found): {src_file.name[:50]}")
            checkpoint['skipped'].append(src_file.name)

print(f"\nFound {len(lowquality_papers)} low-quality papers with PDFs available")
print(f"To retry: {len(lowquality_papers)} papers")

if len(lowquality_papers) == 0:
    print("\nNo low-quality papers to process!")
    exit(0)

# Process papers
total = len(lowquality_papers)
count = len(checkpoint['done'])
start_time = time.time()

print(f"\n{'=' * 60}")
print(f"Starting batch processing ({len(lowquality_papers)} papers, ~10 min each)")
print(f"Estimated time: {len(lowquality_papers) * 10 / 60:.1f} hours")
print(f"{'=' * 60}\n")

for idx, (src_file, pdf_path) in enumerate(lowquality_papers):
    count += 1
    filename = src_file.name
    elapsed = (time.time() - start_time) / 60

    print(f"[{count}/{total}] {filename[:50]}... ({elapsed:.0f}m elapsed)", end='', flush=True)

    # Extract PDF text with MinerU
    text, success = extract_with_mineru(pdf_path, timeout_min=12)

    if not success:
        print(f"  -> MinerU FAILED")
        checkpoint['failed'].append(filename)
        save_checkpoint()
        continue

    # Get abstract and title
    title = src_file.stem.replace('-', ' ')
    abstract = get_abstract(src_file)

    # Analyze with LLM
    print(f"  -> LLM analyzing... ", end='', flush=True)
    analysis = analyze_with_llm(title, abstract, text)

    if 'error' in analysis:
        print(f"LLM error: {analysis['error']}")
        checkpoint['failed'].append(filename)
    else:
        # Update source file
        if update_source_file(src_file, analysis):
            cc = len(analysis.get('core_contributions', []))
            m = len(analysis.get('methods', []))
            mo = len(analysis.get('models', []))
            t = len(analysis.get('topics', []))
            kf = len(analysis.get('key_findings', []))
            print(f"✅ cc={cc}, methods={m}, models={mo}, topics={t}, findings={kf}")
            checkpoint['done'].append(filename)
        else:
            print("Update failed")
            checkpoint['failed'].append(filename)

    # Save checkpoint every file
    save_checkpoint()

save_checkpoint()

elapsed = (time.time() - start_time) / 60
print(f"\n{'=' * 60}")
print(f"Completed in {elapsed:.1f} minutes")
print(f"Done: {len(checkpoint['done'])}")
print(f"Failed: {len(checkpoint['failed'])}")
print(f"Skipped: {len(checkpoint['skipped'])}")
print(f"{'=' * 60}")

if checkpoint['failed']:
    print(f"\nFailed files (can retry again):")
    for f in checkpoint['failed'][:20]:
        print(f"  - {f}")

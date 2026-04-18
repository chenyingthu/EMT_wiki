#!/usr/bin/env python3
"""
Deep re-analysis of ALL 699 source pages using MinerU for PDF extraction + LLM.
Replaces pdftotext with MinerU API for full-text extraction (LaTeX formulas, tables, images).
Re-analyzes ALL 5 sections: 核心贡献/使用的方法/涉及的模型/相关主题/主要发现
"""

import os
import re
import glob
import json
import time
import argparse
import subprocess

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://coding.dashscope.aliyuncs.com/apps/anthropic"),
)

# Taxonomy wikilinks for validation
TAXONOMY_WIKILINKS = {
    'mmc': '[[mmc-model|MMC]]',
    'mmc-model': '[[mmc-model|MMC]]',
    'vsc': '[[vsc-model|VSC]]',
    'vsc-model': '[[vsc-model|VSC]]',
    'lcc': '[[lcc-model|LCC]]',
    'lcc-model': '[[lcc-model|LCC]]',
    'dfig': '[[dfig-model|DFIG]]',
    'dfig-model': '[[dfig-model|DFIG]]',
    'pmsm': '[[pmsm-model|PMSM]]',
    'pmsm-model': '[[pmsm-model|PMSM]]',
    'transformer': '[[transformer-model|变压器]]',
    'transformer-model': '[[transformer-model|变压器]]',
    'transmission-line': '[[transmission-line-model|输电线路]]',
    'transmission-line-model': '[[transmission-line-model|输电线路]]',
    'synchronous-machine': '[[synchronous-machine-model|同步电机]]',
    'synchronous-machine-model': '[[synchronous-machine-model|同步电机]]',
    'fdne': '[[fdne-model|FDNE]]',
    'fdne-model': '[[fdne-model|FDNE]]',
    'cable': '[[cable-model|电缆]]',
    'cable-model': '[[cable-model|电缆]]',
    'co-simulation': '[[co-simulation|混合仿真]]',
    'cosimulation': '[[co-simulation|混合仿真]]',
    'co_simulation': '[[co-simulation|混合仿真]]',
    'real-time': '[[real-time-simulation|实时仿真]]',
    'realtime': '[[real-time-simulation|实时仿真]]',
    'dynamic-phasor': '[[dynamic-phasor|动态相量法]]',
    'dynamic phasor': '[[dynamic-phasor|动态相量法]]',
    'parallel': '[[parallel-computing|并行计算]]',
    'parallel-computing': '[[parallel-computing|并行计算]]',
    'frequency-dependent': '[[frequency-dependent-modeling|频率相关建模]]',
    'freq-dependent': '[[frequency-dependent-modeling|频率相关建模]]',
    'network-equivalent': '[[network-equivalent|网络等值]]',
    'net-equivalent': '[[network-equivalent|网络等值]]',
    'vsc-hvdc': '[[vsc-hvdc|VSC-HVDC]]',
    'hvdc': '[[vsc-hvdc|VSC-HVDC]]',
    'ferroresonance': '[[ferroresonance|铁磁谐振]]',
    'harmonic': '[[harmonic-analysis|谐波分析]]',
    'harmonic-analysis': '[[harmonic-analysis|谐波分析]]',
    'wind-farm': '[[wind-farm-modeling|风电场建模]]',
    'wind-farm-modeling': '[[wind-farm-modeling|风电场建模]]',
    'vector-fitting': '[[vector-fitting|矢量拟合]]',
    'average-value-model': '[[average-value-model|平均值模型]]',
    'avm': '[[average-value-model|平均值模型]]',
    'nodal-analysis': '[[nodal-analysis|节点分析]]',
    'state-space': '[[state-space-method|状态空间法]]',
    'numerical-integration': '[[numerical-integration|数值积分]]',
    'trapezoidal': '[[numerical-integration|数值积分]]',
    'gear': '[[numerical-integration|数值积分]]',
    'dirk': '[[numerical-integration|数值积分]]',
    'passivity': '[[passivity-enforcement|无源性强制]]',
    'passivity-enforcement': '[[passivity-enforcement|无源性强制]]',
    'multirate': '[[multirate-method|多速率方法]]',
    'multi-rate': '[[multirate-method|多速率方法]]',
    'multirate-method': '[[multirate-method|多速率方法]]',
    'fixed-admittance': '[[fixed-admittance|恒导纳模型]]',
    'nodal': '[[fixed-admittance|恒导纳模型]]',
    'interpolation': '[[interpolation-method|插值方法]]',
    'prony': '[[prony-analysis|Prony分析]]',
    'bergeron': '[[transmission-line-model|Bergeron线路模型]]',
}


MINERU_API = os.environ.get("MINERU_API_URL", "http://localhost:8000")


def extract_pdf_text(pdf_path, max_retries=1):
    """Extract FULL text from PDF using MinerU API (async task).
    Returns markdown text with LaTeX formulas, tables, and images.
    Falls back to pdftotext if MinerU fails."""
    if not pdf_path or not os.path.exists(pdf_path):
        return None

    # Try MinerU API first
    for retry in range(max_retries + 1):
        try:
            import http.client
            import mimetypes

            # Submit async task via multipart form data
            boundary = "----MineruBoundary"
            headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}

            body_parts = []
            # File part
            body_parts.append(f"--{boundary}\r\n".encode())
            body_parts.append(
                f'Content-Disposition: form-data; name="files"; filename="{os.path.basename(pdf_path)}"\r\n'.encode()
            )
            body_parts.append(b"Content-Type: application/pdf\r\n\r\n")
            with open(pdf_path, 'rb') as f:
                body_parts.append(f.read())
            # Options
            for field, value in [("is_ocr", "false"), ("formula_enable", "true"), ("table_enable", "true")]:
                body_parts.append(f"\r\n--{boundary}\r\n".encode())
                body_parts.append(f'Content-Disposition: form-data; name="{field}"\r\n\r\n{value}'.encode())
            body_parts.append(f"\r\n--{boundary}--\r\n".encode())

            body = b"".join(body_parts)

            conn = http.client.HTTPConnection("localhost:8000", timeout=120)
            conn.request("POST", "/tasks", body=body, headers=headers)
            resp = conn.getresponse()
            submit_data = json.loads(resp.read().decode())
            conn.close()

            task_id = submit_data.get("task_id")
            if not task_id:
                break

            # Poll until completed (max 5 min)
            for _ in range(60):
                time.sleep(5)
                conn = http.client.HTTPConnection("localhost:8000", timeout=10)
                conn.request("GET", f"/tasks/{task_id}")
                resp = conn.getresponse()
                task_data = json.loads(resp.read().decode())
                conn.close()

                status = task_data.get("status", "")
                if status in ("completed", "success"):
                    break
                if status == "failed":
                    error_msg = task_data.get("error", "unknown")
                    if "CUDA out of memory" in str(error_msg):
                        if retry < max_retries:
                            time.sleep(10)
                            continue
                    break

            # Get result
            conn = http.client.HTTPConnection("localhost:8000", timeout=60)
            conn.request("GET", f"/tasks/{task_id}/result")
            resp = conn.getresponse()
            result_data = json.loads(resp.read().decode())
            conn.close()

            # Extract markdown
            results = result_data.get("results", {})
            if isinstance(results, list) and results:
                results = results[0]
            for key, val in results.items():
                if isinstance(val, dict) and "md_content" in val:
                    md = val["md_content"]
                    return md[:15000]  # Cap for LLM context

            break

        except Exception:
            if retry < max_retries:
                time.sleep(10)
                continue
            break

    # Fallback to pdftotext
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=60
        )
        text = result.stdout
        return text[:15000] if text else None
    except Exception:
        return None


def get_abstract(filepath):
    """Extract abstract from source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    abs_match = re.search(r'## 摘要\s*\n\n(.+?)(?=\n##|$)', content, re.DOTALL)
    if abs_match:
        return abs_match.group(1).strip()
    abs_match2 = re.search(r'abstract:\s*["\']?(.+?)["\']?\s*\n(?:abstract:|authors:|year:|tags:|sources:|---)', content, re.DOTALL)
    if abs_match2:
        return abs_match2.group(1).strip().strip("'\"").strip()
    return None


def get_pdf_path(filepath, base_dir='/home/chenying/researches/EMT_LLM_Wiki'):
    """Get PDF path from source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    src_match = re.search(r'sources:\s*\["(.*?)"\]', content)
    if src_match:
        path = src_match.group(1)
        full_path = os.path.join(base_dir, path)
        if os.path.exists(full_path):
            return full_path
    return None


def analyze_with_llm(title, abstract, full_text):
    """Use LLM to generate ALL 5 sections from full MinerU text."""
    # Use up to 12000 chars of MinerU text (includes LaTeX formulas)
    text_snippet = full_text[:12000] if full_text else ""

    content = f"论文标题：{title}\n"
    if abstract:
        content += f"摘要：{abstract}\n"
    if text_snippet:
        content += f"\n论文全文（MinerU提取）：\n{text_snippet}"

    prompt = f"""分析以下EMT（电磁暂态）仿真领域论文，用中文输出JSON，包含以下5个字段：

```json
{{
  "core_contributions": ["核心贡献/创新点，1-3条，每条20-40字，描述论文最主要的技术贡献"],
  "methods": ["使用的方法/技术，如：矢量拟合、Bergeron模型、动态相量法、多速率仿真、节点分析、平均值模型等"],
  "models": ["涉及的设备/模型，如：MMC、VSC、LCC、DFIG、PMSM、变压器、输电线路、电缆、同步电机、FDNE等"],
  "topics": ["相关主题，如：实时仿真、混合仿真、并行计算、频率相关建模、网络等值、VSC-HVDC、铁磁谐振、谐波分析、风电场建模等"],
  "key_findings": ["主要发现/实验结果，1-3条，每条20-40字，描述论文的实验结论或仿真验证结果"]
}}
```

要求：
1. core_contributions 和 key_findings 要具体、有技术细节，不要泛泛而谈
2. methods/models/topics 要从论文实际内容中提取，匹配已有术语
3. 只输出JSON，不要其他文字
4. 如果某个字段没有内容可以省略或为空数组

{content}"""

    try:
        response = client.messages.create(
            model="qwen3.6-plus",
            max_tokens=1000,
            temperature=0.1,
            messages=[{"role": "user", "content": prompt}],
        )
        for block in response.content:
            if block.type == "text" and block.text:
                text_result = block.text.strip()
                json_match = re.search(r'```json\s*\n(.*?)\n```', text_result, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group(1))
                return json.loads(text_result)
    except Exception as e:
        return {'error': str(e)}


def format_wikilink(item, section_type):
    """Convert item to wikilink format."""
    slug = re.sub(r'[^\w\u4e00-\u9fff]+', '-', item.lower()).strip('-')
    for key, wikilink in TAXONOMY_WIKILINKS.items():
        if key in slug or slug in key:
            return wikilink
    return f'[[{slug}|{item}]]'


def update_source_file(filepath, analysis):
    """Update ALL 5 sections in source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'error' in analysis:
        return False

    updated = False

    # 核心贡献
    if 'core_contributions' in analysis and analysis['core_contributions']:
        items = analysis['core_contributions']
        section_content = '\n'.join(f'- {item}' for item in items)
        pattern = r'(## 核心贡献\s*\n).*?(?=\n##|$)'
        replacement = rf'\1\n{section_content}\n\n'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            updated = True

    # 使用的方法
    if 'methods' in analysis and analysis['methods']:
        links = [format_wikilink(item, '方法') for item in analysis['methods']]
        section_content = '\n'.join(f'- {l}' for l in links)
        pattern = r'(## 使用的方法\s*\n).*?(?=\n##|$)'
        replacement = rf'\1\n{section_content}\n\n'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            updated = True

    # 涉及的模型
    if 'models' in analysis and analysis['models']:
        links = [format_wikilink(item, '模型') for item in analysis['models']]
        section_content = '\n'.join(f'- {l}' for l in links)
        pattern = r'(## 涉及的模型\s*\n).*?(?=\n##|$)'
        replacement = rf'\1\n{section_content}\n\n'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            updated = True

    # 相关主题
    if 'topics' in analysis and analysis['topics']:
        links = [format_wikilink(item, '主题') for item in analysis['topics']]
        section_content = '\n'.join(f'- {l}' for l in links)
        pattern = r'(## 相关主题\s*\n).*?(?=\n##|$)'
        replacement = rf'\1\n{section_content}\n\n'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            updated = True

    # 主要发现
    if 'key_findings' in analysis and analysis['key_findings']:
        items = analysis['key_findings']
        section_content = '\n'.join(f'- {item}' for item in items)
        pattern = r'(## 主要发现\s*\n).*?(?=\n##|$)'
        replacement = rf'\1\n{section_content}\n\n'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return updated


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=0, help='Limit to N files (0=all)')
    parser.add_argument('--start', type=int, default=0, help='Start from index N')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    parser.add_argument('--skip-mineru', action='store_true', help='Use existing extracted text (debug)')
    args = parser.parse_args()

    source_files = sorted(glob.glob('wiki/sources/*.md'))
    print(f"Total source files: {len(source_files)}")

    # Checkpoint
    checkpoint_file = '.reanalyze_mineru.json'
    if os.path.exists(checkpoint_file):
        with open(checkpoint_file) as f:
            done = json.load(f).get('done', [])
        source_files = [f for f in source_files if f not in done]
        print(f"Resuming: {len(done)} done, {len(source_files)} remaining")

    if args.start > 0:
        source_files = source_files[args.start:]

    if args.limit > 0:
        source_files = source_files[:args.limit]

    print(f"Processing {len(source_files)} files")

    success = 0
    failed = 0

    for i, filepath in enumerate(source_files):
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()
        title_match = re.search(r'title:\s*["\'](.+?)["\']', raw)
        title = title_match.group(1) if title_match else 'unknown'

        abstract = get_abstract(filepath)
        pdf_path = get_pdf_path(filepath)

        print(f"  [{i+1}/{len(source_files)}] {title[:60]}...", end=' ', flush=True)

        # Extract PDF text via MinerU API (with pdftotext fallback)
        if not args.skip_mineru:
            full_text = extract_pdf_text(pdf_path)
            text_len = len(full_text) if full_text else 0
            # Detect if MinerU worked (contains LaTeX) or fell back to pdftotext
            is_mineru = full_text and ('$$' in full_text or '\\mathbf' in full_text or '\\left' in full_text)
            source = "MinerU" if is_mineru else "pdftotext"
            print(f"{source}: {text_len} chars, ", end='', flush=True)
        else:
            full_text = None

        # LLM analysis
        analysis = analyze_with_llm(title, abstract, full_text or "")
        if 'error' in analysis:
            print(f"LLM ❌ {analysis['error'][:80]}")
            failed += 1
        else:
            if not args.dry_run:
                ok = update_source_file(filepath, analysis)
                if ok:
                    cc = len(analysis.get('core_contributions', []))
                    m = len(analysis.get('methods', []))
                    mo = len(analysis.get('models', []))
                    t = len(analysis.get('topics', []))
                    kf = len(analysis.get('key_findings', []))
                    print(f"✅ cc={cc}, methods={m}, models={mo}, topics={t}, findings={kf}")
                    success += 1
                else:
                    print("❌ Update failed")
                    failed += 1
            else:
                print(f"✅ (dry-run) {json.dumps(analysis, ensure_ascii=False)[:120]}")
                success += 1

        # Checkpoint every 5
        if (i + 1) % 5 == 0 and not args.dry_run:
            # Track all processed files
            all_done = set()
            if os.path.exists(checkpoint_file):
                try:
                    with open(checkpoint_file) as f:
                        all_done = set(json.load(f).get('done', []))
                except:
                    pass
            for f_done in source_files[:i+1]:
                all_done.add(f_done)
            json.dump({'done': list(all_done)}, open(checkpoint_file, 'w'), ensure_ascii=False, indent=2)

        time.sleep(2)

    # Save final checkpoint
    if not args.dry_run:
        all_done = set()
        if os.path.exists(checkpoint_file):
            try:
                with open(checkpoint_file) as f:
                    all_done = set(json.load(f).get('done', []))
            except:
                pass
        for f_done in source_files:
            all_done.add(f_done)
        json.dump({'done': list(all_done)}, open(checkpoint_file, 'w'), ensure_ascii=False, indent=2)

    print(f"\n=== Summary ===")
    print(f"Success: {success}, Failed: {failed}")


if __name__ == '__main__':
    main()

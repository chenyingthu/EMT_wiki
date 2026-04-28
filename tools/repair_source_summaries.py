#!/usr/bin/env python3
"""Repair source-page abstracts, contributions, and lightweight metadata.

This pass is deliberately evidence-bound. It uses each source page's existing
deep sections plus locally extracted paper text, and it records uncertainty
instead of inventing missing bibliographic facts.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "wiki" / "sources"
METADATA_PATH = SOURCE_DIR / "metadata.json"
ENHANCED_DIR = ROOT / "extracted_text" / "markdown_enhanced"
MARKDOWN_DIR = ROOT / "extracted_text" / "markdown"
PDFTOTEXT_DIR = ROOT / "extracted_text" / "pdftotext"
DEFAULT_STRICT_REPORT = ROOT / "reports" / "wiki_strict_audit.json"

BAD_AUTHOR_RE = re.compile(
    r"未知|CNKI|IEEE|Periodicals|作者|Member|\[\]|''|\"\"|\(!|"
    r"Index\s+Terms|INDEX\s+TERMS|Keywords?|Fig\.|From\s+left\s+to\s+right|"
    r"University|Department|Institute|Laboratory|Hydro-Quebec|"
    r"Chicago|Trondheim|Norway|Ste-Catherine|EFI",
    re.IGNORECASE,
)
BAD_TITLE_RE = re.compile(r"untitled|Published in|Translations and content mining|\.dvi$|\.pdf$", re.IGNORECASE)

JOURNAL_PATTERNS = [
    (re.compile(r"中国电机工程学报|Proceedings\s*of\s*the\s*CSEE", re.IGNORECASE), "中国电机工程学报"),
    (re.compile(r"10\.13334/j\.0258-8013\.pcsee|10\.1\s*333\s*4\s*/j\.\s*025\s*8", re.IGNORECASE), "中国电机工程学报"),
    (re.compile(r"电\s*网\s*技\s*术|Power\s+System\s+Technology|10\.13335/j\.1000-3673\.pst", re.IGNORECASE), "电网技术"),
    (re.compile(r"电\s*力\s*自\s*动\s*化\s*设\s*备|Electric\s+Power\s+Automation\s+Equipment|10\.16081[／/]j\.(?:epae|issn\.1006[-－]6047)", re.IGNORECASE), "电力自动化设备"),
    (re.compile(r"DOI[:：]\s*10\.7500/AEPS|电\s*力\s*系\s*统\s*自\s*动\s*化", re.IGNORECASE), "电力系统自动化"),
    (re.compile(r"CSEE\s+Journal\s+of\s+Power\s+and\s+Energy\s+Systems|10\.17775/CSEEJPES", re.IGNORECASE), "CSEE Journal of Power and Energy Systems"),
    (re.compile(r"IET\s+Generation,\s*Transmission\s*&?\s*Distribution|10\.1049/gtd2", re.IGNORECASE), "IET Generation, Transmission & Distribution"),
    (re.compile(r"IEEE\s+Transactions\s+on\s+Power\s+Delivery|Trans(?:actions)?\.\s+Power\s+Delivery", re.IGNORECASE), "IEEE Transactions on Power Delivery"),
    (re.compile(r"IEEE\s+Transactions\s+on\s+Power\s+Systems", re.IGNORECASE), "IEEE Transactions on Power Systems"),
    (re.compile(r"IEEE\s+Transactions\s+on\s+Power\s+Electronics", re.IGNORECASE), "IEEE Transactions on Power Electronics"),
    (re.compile(r"IEEE\s+Journal\s+of\s+Emerging\s+and\s+Selected\s+Topics\s+in\s+Power\s+Electronics", re.IGNORECASE), "IEEE Journal of Emerging and Selected Topics in Power Electronics"),
    (re.compile(r"IEEE\s+Open\s+Access\s+Journal\s+of\s+Power\s+and\s+Energy", re.IGNORECASE), "IEEE Open Access Journal of Power and Energy"),
    (re.compile(r"IEEE\s+Open\s+Journal\s+of\s+Power\s+Electronics", re.IGNORECASE), "IEEE Open Journal of Power Electronics"),
    (re.compile(r"IEEE\s+Access", re.IGNORECASE), "IEEE Access"),
    (re.compile(r"IEEE\s+(?:Power\s*(?:&|and)\s*Energy\s+Society|PES)\s+General\s+Meeting", re.IGNORECASE), "IEEE Power & Energy Society General Meeting"),
    (re.compile(r"Electric\s+Power\s+Systems\s+Research", re.IGNORECASE), "Electric Power Systems Research"),
    (re.compile(r"10\.1016/j\.epsr", re.IGNORECASE), "Electric Power Systems Research"),
    (re.compile(r"International\s+Journal\s+of\s+Electrical\s+Power\s+&?\s+Energy\s+Systems", re.IGNORECASE), "International Journal of Electrical Power & Energy Systems"),
    (re.compile(r"Electrical\s+Power\s+and\s+Energy\s+Systems", re.IGNORECASE), "International Journal of Electrical Power & Energy Systems"),
    (re.compile(r"10\.1016/j\.ijepes", re.IGNORECASE), "International Journal of Electrical Power & Energy Systems"),
]

JOURNAL_SOURCE_PATTERNS = [
    (re.compile(r"(?:^|[/_.-])tpwrd|10\.1109[/_.-]?(?:tpwrd|61)\b", re.IGNORECASE), "IEEE Transactions on Power Delivery"),
    (re.compile(r"(?:^|[/_.-])tpwrs|10\.1109[/_.-]?(?:tpwrs|59)\b", re.IGNORECASE), "IEEE Transactions on Power Systems"),
    (re.compile(r"(?:^|[/_.-])tpel|10\.1109[/_.-]?(?:tpel|63)\b", re.IGNORECASE), "IEEE Transactions on Power Electronics"),
    (re.compile(r"(?:^|[/_.-])jestpe|10\.1109[/_.-]?(?:jestpe|62466)\b", re.IGNORECASE), "IEEE Journal of Emerging and Selected Topics in Power Electronics"),
    (re.compile(r"(?:^|[/_.-])oajpe|10\.1109[/_.-]?oajpe", re.IGNORECASE), "IEEE Open Access Journal of Power and Energy"),
    (re.compile(r"(?:^|[/_.-])ojpel|10\.1109[/_.-]?ojpel", re.IGNORECASE), "IEEE Open Journal of Power Electronics"),
    (re.compile(r"(?:^|[/_.-])access|10\.1109[/_.-]?access", re.IGNORECASE), "IEEE Access"),
    (re.compile(r"(?:^|[/_.-])pes(?:gm|[._-]?\d{4}|gm\d+)|10\.1109[/_.-]?pesgm", re.IGNORECASE), "IEEE Power & Energy Society General Meeting"),
    (re.compile(r"j\.epsr|epsr|s0378[-_]?7796|s03787796", re.IGNORECASE), "Electric Power Systems Research"),
    (re.compile(r"elsevier\s*com\s*locate\s*epsr|wwwelseviercomlocateepsr", re.IGNORECASE), "Electric Power Systems Research"),
    (re.compile(r"j\.ijepes|ijepes|s0142[-_]?0615|s01420615", re.IGNORECASE), "International Journal of Electrical Power & Energy Systems"),
]


def frontmatter(content: str) -> str:
    match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL | re.MULTILINE)
    return match.group(1) if match else ""


def frontmatter_value(content: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter(content), re.MULTILINE)
    return match.group(1).strip().strip('"') if match else ""


def section_text(content: str, section: str) -> str:
    match = re.search(rf"^## {re.escape(section)}\s*\n(.*?)(?=^## |\Z)", content, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else ""


def replace_section(content: str, section: str, replacement: str) -> str:
    pattern = rf"(^## {re.escape(section)}\s*\n)(.*?)(?=^## |\Z)"
    return re.sub(
        pattern,
        lambda match: f"{match.group(1)}\n{replacement.strip()}\n\n",
        content,
        count=1,
        flags=re.DOTALL | re.MULTILINE,
    )


def append_to_section(content: str, section: str, line: str) -> str:
    current = section_text(content, section)
    if line in current:
        return content
    return replace_section(content, section, current.rstrip() + "\n" + line)


def replace_frontmatter_value(content: str, key: str, rendered_value: str) -> str:
    if re.search(rf"^{re.escape(key)}:", frontmatter(content), re.MULTILINE):
        return re.sub(rf"^{re.escape(key)}:\s*.*$", f"{key}: {rendered_value}", content, count=1, flags=re.MULTILINE)
    return content


def is_inactive_source(content: str) -> bool:
    return "type: duplicate-source" in content or "type: out-of-scope-source" in content


def first_source(content: str) -> str:
    match = re.search(r'sources:\s*\["([^"]+)"\]', content)
    return match.group(1) if match else ""


def load_metadata() -> dict[str, dict]:
    if not METADATA_PATH.exists():
        return {}
    data = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    by_source = {}
    for paper in data.get("papers", []):
        rel = paper.get("relative_path") or ""
        if rel:
            by_source[f"EMT_Doc/{rel}"] = paper
            by_source[Path(rel).name] = paper
    return by_source


def candidate_extracted_paths(filename: str) -> list[Path]:
    stem = filename[:-3] if filename.endswith(".md") else filename
    base_stem = re.sub(r"-(?:\d+|fix)$", "", stem)
    names = [f"{stem}.md"]
    if base_stem != stem:
        names.append(f"{base_stem}.md")
    candidates = [ENHANCED_DIR / name for name in names]
    candidates.extend(MARKDOWN_DIR / name for name in names)
    candidates.extend(PDFTOTEXT_DIR / name.replace(".md", ".txt") for name in names)
    return candidates


def extracted_text(filename: str) -> str:
    for path in candidate_extracted_paths(filename):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        if len(text) >= 500 and not text.lower().startswith("please provide the academic paper text"):
            return text
    return ""


def metadata_evidence_text(filename: str) -> str:
    parts = []
    for path in candidate_extracted_paths(filename):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        if text and not text.lower().startswith("please provide the academic paper text"):
            parts.append(text[:3000])
    return "\n".join(parts)


def clean_inline(text: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$[^$]{0,12}\$", "", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", text)
    text = re.sub(r"\[\[([^\]|]+)\|?([^\]]*)\]\]", lambda m: m.group(2) or m.group(1), text)
    text = re.sub(r"[*_`#|]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def first_paragraph(text: str, min_len: int = 60) -> str:
    for part in re.split(r"\n\s*\n", text):
        cleaned = clean_inline(part)
        if len(cleaned) >= min_len and not cleaned.startswith(("公式", "表", "Fig", "图", "-", "|")):
            return cleaned
    return clean_inline(text)


def clip_sentence(text: str, limit: int) -> str:
    text = clean_inline(text)
    if len(text) <= limit:
        return text
    cut = max(text.rfind("。", 0, limit), text.rfind("；", 0, limit), text.rfind(".", 0, limit))
    if cut >= 80:
        return text[: cut + 1]
    return text[:limit].rstrip("，,;；") + "。"


def extract_abstract_from_text(text: str) -> str:
    if not text:
        return ""
    patterns = [
        r"(?:\*\*)?摘要[:：](?:\*\*)?\s*(.*?)(?=(?:\*\*)?关键词[:：]|中图分类号|##\s*0\s*引言|#?\s*0\s+引言)",
        r"(?:###\s*)?Abstract\s*(.*?)(?=(?:\*\*)?Keywords?[:：]|##\s*1\.?\s*INTRODUCTION|##\s*1\.?\s*Introduction)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if not match:
            continue
        abstract = clean_inline(match.group(1))
        if len(abstract) >= 80:
            return abstract[:1200]
    return ""


def title_from_extracted(text: str) -> str:
    for raw in text.splitlines()[:20]:
        line = clean_inline(raw)
        if not line:
            continue
        line = line.lstrip("#").strip()
        if len(line) < 8 or line.lower() in {"abstract", "keywords"}:
            continue
        if re.search(r"doi|vol\.|第\s*\d+\s*卷|文章编号|copyright|translations", line, re.IGNORECASE):
            continue
        return line
    return ""


def clean_author_name(name: str) -> str:
    name = re.sub(r"\$[^$]{0,12}\$", "", name)
    name = re.sub(r"\*\*([^*]+)\*\*", r"\1", name)
    name = re.sub(r"\b\d+\b|[*†,，]+$", "", name)
    name = re.sub(r"\bAND\b", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\([^)]*(?:Member|IEEE)[^)]*\)", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\(?\b(?:Senior|Student)?\s*Member\b.*$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\bIEEE\)?", "", name, flags=re.IGNORECASE)
    name = re.sub(r"[\$\{\}\^_]+", "", name)
    name = clean_inline(name)
    return name.strip(" ,，;；")


def looks_like_author_name(name: str) -> bool:
    if not name or BAD_AUTHOR_RE.search(name):
        return False
    if len(name) > 80 or len(name) < 2:
        return False
    if re.search(r"[@:/]|Abstract|摘要|关键词|Published|Manuscript|Copyright|Digital Object Identifier", name, re.IGNORECASE):
        return False
    if re.search(r"\b(?:N-\d+|\d+(?:st|nd|rd|th)\b|Floor\b|USA\b|Canada\b)\b", name, re.IGNORECASE):
        return False
    if re.search(r"大学|学院|研究院|实验室|公司|地址|基金", name):
        return False
    if re.search(r"[A-Za-z]", name):
        return bool(re.search(r"[A-Z][A-Za-zÀ-ÖØ-öø-ÿ.'-]+", name))
    return bool(re.fullmatch(r"[\u4e00-\u9fff·]{2,12}", name))


def split_author_line(line: str) -> list[str]:
    line = re.sub(r"^\*\*|\*\*$", "", line.strip())
    line = re.sub(r"\s+AND\s+", ", ", line, flags=re.IGNORECASE)
    line = re.sub(r"\s+and\s+", ", ", line)
    line = re.sub(r"<sup>.*?</sup>", "", line)
    line = re.sub(r"(?<=[A-Za-z])\d+\b", "", line)
    line = re.sub(r"\([^)]*(?:Member|IEEE)[^)]*\)", "", line, flags=re.IGNORECASE)
    line = re.sub(r"\(?\b(?:Senior|Student)?\s*Member\b.*?(?=,|$)", "", line, flags=re.IGNORECASE)
    parts = re.split(r"\s*[,;；、]\s*", line)
    names = [clean_author_name(part) for part in parts]
    return [name for name in names if looks_like_author_name(name)]


def authors_from_text(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines()[:25] if line.strip()]
    for index, raw in enumerate(lines):
        line = raw.lstrip("#").strip()
        if not line or re.search(r"摘要|Abstract|关键词|Key words|Received|University|Institute|Department|DOI|Vol\.", line, re.IGNORECASE):
            continue
        if index == 0 and len(clean_inline(line)) > 20:
            continue
        if re.search(r"[\u4e00-\u9fff]", line) and re.search(r"[，、,]", line):
            names = split_author_line(line)
            if names:
                return names[:12]
        if "<sup>" in line or re.search(r"\d", line):
            if "," in line and not re.search(r"University|Institute|Department|Laboratory|College", line, re.IGNORECASE):
                names = split_author_line(line)
                if len(names) >= 2:
                    return names[:12]
        if "|" in line:
            names = [clean_author_name(item) for item in line.split("|")]
            names = [name for name in names if looks_like_author_name(name)]
            if names:
                return names[:12]
        if "," in line and len(line) < 220 and not re.search(r"University|Institute|Department|Laboratory|College", line, re.IGNORECASE):
            names = split_author_line(line)
            if len(names) >= 2:
                return names[:12]
        if " and " in line and len(line) < 160 and not re.search(r"University|Institute|Department|Laboratory|College", line, re.IGNORECASE):
            names = [clean_author_name(item) for item in re.split(r"\s+and\s+", line)]
            names = [name for name in names if looks_like_author_name(name)]
            if len(names) >= 2:
                return names[:12]
        if re.search(r"[A-Z]\.\s*[A-Z]?", line) and "," in line and len(line) < 220:
            names = split_author_line(line)
            if names:
                return names[:12]
        single = clean_author_name(line)
        if 0 < index <= 4 and looks_like_author_name(single):
            return [single]
    return []


def authors_from_source_path(source: str) -> list[str]:
    stem = re.sub(r"\.pdf(?:\.pdf)?$", "", Path(source).name, flags=re.IGNORECASE)
    match = re.match(r"(.+?)\s*[-–]\s*(?:19|20)\d{2}\s*[-–]\s*.+", stem)
    if not match:
        return []
    prefix = clean_author_name(match.group(1))
    if not looks_like_author_name(prefix):
        return []
    return [prefix]


def journal_from_text(text: str) -> str:
    head = text[:5000]
    for pattern, journal in JOURNAL_PATTERNS:
        if pattern.search(head):
            return journal
    return journal_from_source(head)


def journal_from_title(title: str) -> str:
    if re.search(r"Power\s+Delivery,\s*IEEE\s+Transactions\s+on", title, re.IGNORECASE):
        return "IEEE Transactions on Power Delivery"
    if re.search(r"Power\s+Systems,\s*IEEE\s+Transactions\s+on", title, re.IGNORECASE):
        return "IEEE Transactions on Power Systems"
    if re.search(r"Electrical\s+Power\s+and\s+Energy\s+Systems", title, re.IGNORECASE):
        return "Electrical Power and Energy Systems"
    return ""


def journal_from_metadata(metadata: dict) -> str:
    subject = (metadata.get("subject") or "").replace("&amp;", "&").strip()
    if not subject or subject.lower() in {"科目", "subject"}:
        return ""
    return journal_from_text(subject) or journal_from_source(subject)


def journal_from_source(source: str) -> str:
    haystack = source.replace("%28", "(").replace("%29", ")")
    for pattern, journal in JOURNAL_SOURCE_PATTERNS:
        if pattern.search(haystack):
            return journal
    return ""


def looks_bad_journal(journal: str) -> bool:
    if not journal or journal == "科目" or len(journal) > 80:
        return True
    return bool(re.search(r"节点|University\)|验证结果|摘要|Transmission Lines$", journal))


def yaml_list(values: list[str]) -> str:
    escaped = [value.replace("\\", "\\\\").replace("'", "\\'") for value in values]
    return "[" + ", ".join(f"'{value}'" for value in escaped) + "]"


def display_authors(authors: list[str]) -> str:
    shown = "; ".join(authors[:5])
    if len(authors) > 5:
        shown += " 等"
    return shown


def frontmatter_authors(content: str) -> list[str]:
    raw = frontmatter_value(content, "authors")
    if not raw.startswith("["):
        return []
    return [item.strip().strip("'\"") for item in raw.strip("[]").split(",") if item.strip().strip("'\"")]


def sanitized_existing_authors(content: str) -> list[str]:
    cleaned = []
    for author in frontmatter_authors(content):
        name = clean_author_name(author)
        if not looks_like_author_name(name):
            continue
        cleaned.append(name)
    return cleaned[:12]


def strip_bullets(text: str) -> list[str]:
    bullets = []
    for raw in text.splitlines():
        line = clean_inline(raw.lstrip("-0123456789.、 ").strip())
        line = re.sub(r"^验证方式\s*:\s*", "", line)
        line = re.sub(r"^测试系统\s*:\s*", "", line)
        line = re.sub(r"^仿真工具\s*:\s*", "", line)
        line = re.sub(r"^验证结果\s*:\s*", "", line)
        if len(line) >= 20 and not line.startswith(("公式", "测试场景", "---------")):
            bullets.append(line)
    return bullets


def has_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def build_summary(content: str, paper_text: str) -> str:
    extracted_abstract = extract_abstract_from_text(paper_text)
    method = first_paragraph(section_text(content, "方法细节"), 80)

    if has_chinese(extracted_abstract) and len(extracted_abstract) >= 80:
        base = clip_sentence(extracted_abstract, 700)
    else:
        base = clip_sentence(method, 520)

    pieces = [base]
    if len(base) < 220:
        validation = "；".join(strip_bullets(section_text(content, "验证详情") + "\n" + section_text(content, "仿真结果"))[:2])
        if validation:
            pieces.append("验证信息：" + clip_sentence(validation, 180))
    summary = "".join(pieces)
    summary = re.sub(r"###\s*\S+", "", summary)
    return clip_sentence(summary, 900)


def build_contributions(content: str, summary: str) -> str:
    method = first_paragraph(section_text(content, "方法细节"), 80)
    validation = "；".join(strip_bullets(section_text(content, "验证详情") + "\n" + section_text(content, "仿真结果"))[:3])
    findings = strip_bullets(section_text(content, "量化发现") + "\n" + section_text(content, "主要发现"))
    boundary = "；".join(strip_bullets(section_text(content, "适用边界"))[:2])

    bullets = [
        "问题定位：" + clip_sentence(summary, 170),
        "方法机制：" + clip_sentence(method, 220),
    ]
    if validation:
        bullets.append("验证证据：" + clip_sentence(validation, 190))
    if findings:
        bullets.append("量化与结论：" + clip_sentence("；".join(findings[:4]), 190))
    if boundary:
        bullets.append("适用边界：" + clip_sentence(boundary, 170))
    return "\n".join(f"- {bullet}" for bullet in bullets if len(bullet) >= 30)


def bad_or_short_abstract(text: str) -> bool:
    return len(clean_inline(text)) < 180 or (not has_chinese(text) and re.search(r"\b(the|this|paper|abstract)\b", text[:500], re.I))


def sync_metadata(
    content: str,
    paper_text: str,
    metadata: dict | None = None,
    filename: str = "",
    metadata_text: str = "",
) -> str:
    updated = content
    metadata = metadata or {}
    source = first_source(content)
    title = frontmatter_value(updated, "title")
    extracted_title = title_from_extracted(paper_text)
    if extracted_title and (not title or BAD_TITLE_RE.search(title)):
        escaped = extracted_title.replace('"', '\\"')
        updated = replace_frontmatter_value(updated, "title", f'"{escaped}"')
        updated = re.sub(r"^# .+$", f"# {extracted_title}", updated, count=1, flags=re.MULTILINE)

    authors = frontmatter_value(updated, "authors")
    new_authors = authors_from_text(paper_text) or authors_from_source_path(source)
    if new_authors and (not authors or BAD_AUTHOR_RE.search(authors)):
        updated = replace_frontmatter_value(updated, "authors", yaml_list(new_authors))
        updated = re.sub(r"^\*\*作者\*\*:.*$", f"**作者**: {display_authors(new_authors)}", updated, count=1, flags=re.MULTILINE)
    elif authors and any(re.search(r"Member|IEEE|\$|\{|\}|\^|\(!", author, re.IGNORECASE) for author in frontmatter_authors(updated)):
        cleaned_authors = sanitized_existing_authors(updated)
        if cleaned_authors:
            updated = replace_frontmatter_value(updated, "authors", yaml_list(cleaned_authors))
            updated = re.sub(r"^\*\*作者\*\*:.*$", f"**作者**: {display_authors(cleaned_authors)}", updated, count=1, flags=re.MULTILINE)

    journal = frontmatter_value(updated, "journal")
    new_journal = (
        journal_from_metadata(metadata)
        or journal_from_text(metadata_text)
        or journal_from_text(paper_text)
        or journal_from_title(frontmatter_value(updated, "title"))
        or journal_from_source(source)
        or journal_from_source(filename)
    )
    if new_journal and looks_bad_journal(journal):
        updated = replace_frontmatter_value(updated, "journal", f'"{new_journal.replace(chr(34), chr(92) + chr(34))}"')
    elif journal and looks_bad_journal(journal):
        updated = replace_frontmatter_value(updated, "journal", '""')
    return updated


def remove_stale_metadata_gap_markers(content: str) -> str:
    if not frontmatter_value(content, "journal").strip('"'):
        return content
    content = re.sub(r"(?m)^- 期刊/会议元数据未在当前页面中可靠给出。\n?", "", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content


def ensure_metadata_gap_markers(content: str) -> str:
    if is_inactive_source(content):
        return content
    if frontmatter_value(content, "journal").strip('"'):
        return remove_stale_metadata_gap_markers(content)
    if "期刊/会议元数据未在当前页面中可靠给出" in content:
        return content
    if "## 适用边界" in content:
        return append_to_section(content, "适用边界", "- 期刊/会议元数据未在当前页面中可靠给出。")
    return content


def repair_content(content: str, filename: str, metadata: dict | None = None) -> str:
    if is_inactive_source(content):
        return content
    paper_text = extracted_text(filename)
    metadata_text = metadata_evidence_text(filename)
    updated = sync_metadata(content, paper_text, metadata, filename, metadata_text)
    updated = ensure_metadata_gap_markers(updated)
    updated = remove_stale_metadata_gap_markers(updated)

    summary = build_summary(updated, paper_text)
    current_abstract = section_text(updated, "摘要")
    if len(summary) >= 80 and has_chinese(summary) and (
        bad_or_short_abstract(current_abstract) or "验证层面，-" in current_abstract or "适用上，-" in current_abstract
    ):
        updated = replace_section(updated, "摘要", summary)

    contributions = build_contributions(updated, section_text(updated, "摘要") or summary)
    current_contributions = section_text(updated, "核心贡献")
    if len(contributions) >= 220 and (
        len(clean_inline(current_contributions)) < 220 or "验证证据：-" in current_contributions or "适用边界：-" in current_contributions
    ):
        updated = replace_section(updated, "核心贡献", contributions)
    return updated


def load_strict_names(strict_report: Path) -> list[str]:
    if not strict_report.exists():
        return []
    data = json.loads(strict_report.read_text(encoding="utf-8"))
    return [Path(item["path"]).name for item in data if item.get("page_type") == "source"]


def process_sources(limit: int = 0, dry_run: bool = False, strict_only: bool = False) -> list[Path]:
    metadata_by_source = load_metadata()
    if strict_only:
        names = load_strict_names(DEFAULT_STRICT_REPORT)
        paths = [SOURCE_DIR / name for name in names if (SOURCE_DIR / name).exists()]
    else:
        paths = sorted(SOURCE_DIR.glob("*.md"))
    changed = []
    for path in paths:
        content = path.read_text(encoding="utf-8")
        source = first_source(content)
        metadata = metadata_by_source.get(source) or metadata_by_source.get(Path(source).name) or {}
        updated = repair_content(content, path.name, metadata)
        if updated == content:
            continue
        changed.append(path)
        if not dry_run:
            path.write_text(updated, encoding="utf-8")
        if limit and len(changed) >= limit:
            break
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair source abstracts/contributions from local evidence")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--strict-only", action="store_true")
    args = parser.parse_args()
    changed = process_sources(limit=args.limit, dry_run=args.dry_run, strict_only=args.strict_only)
    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(changed)} source pages")
    for path in changed[:40]:
        print(path.relative_to(ROOT))
    if len(changed) > 40:
        print(f"... {len(changed) - 40} more")


if __name__ == "__main__":
    main()

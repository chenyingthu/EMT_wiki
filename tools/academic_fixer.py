#!/usr/bin/env python3
"""Batch academic expression fixer.

Applies known high-confidence replacements from academic-style-guide.md
across all entity/method/model/topic pages.

Usage:
    python3 tools/academic_fixer.py              # fix all pages
    python3 tools/academic_fixer.py --dry-run     # preview without changing
    python3 tools/academic_fixer.py --dir entities # fix only entities
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
TAXONOMY_DIRS = ("entities", "methods", "models", "topics")


FIX_RULES: list[tuple[str, str, str]] = [
    (r'全球领先', '有研究成果', '全球领先->有研究成果'),
    (r'国际领先', '有研究成果', '国际领先->有研究成果'),
    (r'世界领先', '有研究成果', '世界领先->有研究成果'),
    (r'最经典(?!的算法|的方法|的工具|的软件)', '经典', '最经典->经典'),
    (r'(学界|行业)泰斗', '学者', '泰斗->学者'),
    (r'金标准', '参考标准', '金标准->参考标准'),
    (r'彻底解决', '能够处理', '彻底解决->能够处理'),
    (r'完美解决', '有效处理', '完美解决->有效处理'),
    (r'独一无二|无可替代', '', 'unique->removed'),
    (r'革命性(?:的)?(?:技术|突破|创新|产品|方案)', '新技术', '革命性->新'),
    (r'颠覆性(?:的)?(?:技术|创新|突破|方案)', '创新技术', '颠覆性->创新'),
    (r'独具(?:特色|优势|匠心)', '具有特征', '独具->具有'),
    (r'广泛使用', '用于', '广泛使用->用于'),
    (r'广泛认可', '被认可', '广泛认可->被认可'),
    (r'最广泛', '主要', '最广泛->主要'),
    (r'最重要(?!的组成部分|的环节|的步骤|的因素)', '重要', '最重要->重要'),
    (r'论文提出', '该研究提出', '论文提出->该研究提出'),
    (r'本文提出(?!了\s*(?:[^。]{0,20}(?:等|作者|学者)))', '原文提出', '本文提出->原文提出'),
    (r'本文介绍', '原文介绍', '本文介绍->原文介绍'),
    (r'该文提出', '该研究提出', '该文提出->该研究提出'),
    (r'文献提出', '已有研究提出', '文献提出->已有研究提出'),
]


# 突破 -> 贡献 (handled separately with safety checks)
TUPO_RE = re.compile(r'突破(?!电压|电流|阈值|电晕|闪络|强度|性|了)')


def is_safe_context(content: str, pos: int) -> bool:
    """Check if the match at pos is in a safe context for replacement."""
    line_start = content.rfind('\n', 0, pos) + 1
    line_end = content.find('\n', pos)
    if line_end == -1:
        line_end = len(content)
    line = content[line_start:line_end].strip()
    if line.startswith('```') or line.startswith('---'):
        return False
    return True


def fix_file(path: Path, dry_run: bool = False) -> list[str]:
    content = path.read_text(encoding='utf-8')
    original = content
    changes: list[str] = []

    for pattern_str, replacement, desc in FIX_RULES:
        pattern = re.compile(pattern_str)
        offset = 0
        while True:
            match = pattern.search(content[offset:])
            if not match:
                break
            abs_pos = offset + match.start()
            if not is_safe_context(content, abs_pos):
                offset = abs_pos + 1
                continue
            start = max(0, abs_pos - 20)
            end = min(len(content), abs_pos + match.end() - match.start() + 20)
            context = content[start:end].replace('\n', ' ').strip()
            matched = match.group()
            if matched[0].isupper():
                replacement_str = replacement[0].upper() + replacement[1:]
            else:
                replacement_str = replacement
            content = content[:abs_pos] + replacement_str + content[abs_pos + len(matched):]
            offset = abs_pos + len(replacement_str)
            changes.append(f'  [{desc}]  [..{context}..]')

    # Special case: 突破 -> 贡献
    offset = 0
    while True:
        match = TUPO_RE.search(content[offset:])
        if not match:
            break
        abs_pos = offset + match.start()
        if not is_safe_context(content, abs_pos):
            offset = abs_pos + 1
            continue
        # Check surrounding context for false positives
        before = content[max(0, abs_pos - 15):abs_pos]
        if any(w in before for w in ['技术', '理论', '方法', '算法', '模型', '实现', '取得', '获得', '重要', '重大', '关键']):
            start_ctx = max(0, abs_pos - 20)
            end_ctx = min(len(content), abs_pos + 10)
            context = content[start_ctx:end_ctx].replace('\n', ' ').strip()
            matched = match.group()
            content = content[:abs_pos] + '贡献' + content[abs_pos + len(matched):]
            offset = abs_pos + 4
            changes.append(f'  [突破->贡献]  [..{context}..]')
        else:
            offset = abs_pos + 1

    if content != original:
        if not dry_run:
            path.write_text(content, encoding='utf-8')
        return changes
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Academic expression batch fixer")
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--dir', choices=TAXONOMY_DIRS, help='Fix only one directory')
    args = parser.parse_args()

    dirs = [args.dir] if args.dir else TAXONOMY_DIRS

    total_fixes = 0
    total_files = 0
    for dirname in dirs:
        for path in sorted((WIKI_DIR / dirname).glob('*.md')):
            changes = fix_file(path, dry_run=args.dry_run)
            if changes:
                rel = path.relative_to(ROOT)
                print(f"\n{rel} ({len(changes)} fixes):")
                for c in changes:
                    print(c)
                total_fixes += len(changes)
                total_files += 1

    mode = 'DRY RUN' if args.dry_run else 'FIXED'
    print(f"\n{mode}: {total_files} files, {total_fixes} fixes")


if __name__ == '__main__':
    main()

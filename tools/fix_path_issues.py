#!/usr/bin/env python3
"""
修复路径问题 - 将 [[methods/xxx]] 转换为 [[xxx]]
"""

import re
from pathlib import Path

WIKI_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki")
SOURCES_DIR = WIKI_DIR / "sources"

def fix_paths_in_file(filepath):
    """修复文件中的路径问题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    fixed = 0
    
    # 修复 [[methods/xxx]] -> [[xxx]]
    pattern = r'\[\[methods/([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'
    
    def replace(match):
        nonlocal fixed
        target = match.group(1)
        display = match.group(2)
        fixed += 1
        if display:
            return f'[[{target}|{display}]]'
        return f'[[{target}]]'
    
    content = re.sub(pattern, replace, content)
    
    # 修复 [[models/xxx]] -> [[xxx]]
    pattern2 = r'\[\[models/([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'
    content = re.sub(pattern2, replace, content)
    
    if fixed > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return fixed

def main():
    total = 0
    files = list(SOURCES_DIR.glob("*.md"))
    
    for filepath in files:
        try:
            fixed = fix_paths_in_file(filepath)
            total += fixed
        except Exception as e:
            print(f"Error: {filepath}: {e}")
    
    print(f"✅ 完成！修复了 {total} 个路径问题")

if __name__ == "__main__":
    main()

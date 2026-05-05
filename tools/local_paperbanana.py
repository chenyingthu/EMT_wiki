#!/usr/bin/env python3
"""
Local PaperBanana Implementation
使用本地资源和 Claude VLM 能力实现学术图表生成

借鉴自: https://github.com/llmsresearch/paperbanana
"""

import json
import requests
import base64
from pathlib import Path
from typing import Optional
import sys

# 配置
LOCAL_IMAGE_URL = "http://localhost:8000/v1/images/generations"
OUTPUT_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki/assets/figures")

# 学术风格指南 (借鉴自 PaperBanana NeurIPS style)
ACADEMIC_STYLE_GUIDE = """
## Academic Journal Figure Style Guidelines

### Background
- Use PURE WHITE background (#FFFFFF) for all figures
- No gradients, textures, or decorative elements
- Clean, paper-like appearance suitable for printing

### Color Palette (Use natural language descriptions)
- Primary: Deep navy blue, dark slate
- Secondary: Steel blue, slate gray
- Accents: Soft teal, muted green
- Positive indicators: Deep green
- Negative indicators: Deep red
- Avoid bright/saturated colors; prefer muted, professional tones

### Typography
- Headers: Bold, clean sans-serif font
- Body: Regular weight, high readability
- Mathematical notation: Italic for variables (x, y, A, B)
- All text in the target language (Chinese for our use case)

### Layout
- Use rectangular modules with sharp corners (no rounded corners)
- Clear visual hierarchy from left-to-right or top-to-bottom
- Adequate white space between sections
- Thin, consistent borders (1-2px)

### Visual Elements
- Flow arrows in medium gray
- Modular boxes with subtle fill colors
- Clear labels and annotations
- No decorative icons or illustrations

### Quality Standards
- Publication-ready clarity
- High contrast for readability
- Professional, minimal aesthetic
- Suitable for IEEE/journal figures
"""

# 参考图表描述 (简化版)
REFERENCE_EXAMPLES = """
Example 1 (Architecture Diagram):
A left-to-right flow diagram showing an encoder-decoder architecture.
The encoder section contains three stacked rectangular blocks labeled "Self-Attention",
"Feed-Forward", and "Output". Each block has a soft blue fill with darker blue borders.
Arrows connect the blocks horizontally. The decoder section mirrors this structure
with an additional "Cross-Attention" block. Background is pure white.

Example 2 (Method Pipeline):
A top-to-bottom process flow with four stages enclosed in rounded rectangles.
Stage 1 "Input Processing" at top, followed by Stage 2 "Feature Extraction",
Stage 3 "Model Inference", and Stage 4 "Output Generation" at bottom.
Each stage has a light teal fill with consistent border styling.
Vertical arrows connect each stage. Annotations on the right explain each step.

Example 3 (Comparison Framework):
A two-column comparison layout. Left column titled "Method A" with three components
in light gray boxes. Right column titled "Method B" with corresponding components.
A central "Comparison Metrics" box connects both columns with horizontal arrows.
White background, navy blue titles, consistent typography.
"""


def generate_diagram_description(
    source_context: str,
    caption: str,
    aspect_ratio: str = "4:3"
) -> str:
    """
    Phase 1: Generate detailed diagram description
    融合 PaperBanana 方法论与 SenseNova-U1 优化格式
    """
    prompt = f"""Create a professional academic infographic diagram.

Title: "{caption}"

Design Style:
- Scientific journal publication quality (IEEE/Elsevier standard)
- Pure WHITE background (#FFFFFF) - this is critical
- Clean, professional color palette
- Rectangular boxes with sharp corners only
- Thin consistent borders (1-2px)
- Clear visual hierarchy
- No decorative elements, shadows, or gradients
- All text in Chinese

Content Sections:

【核心内容】
{source_context}

【图表结构设计】
根据上述内容，设计清晰的信息架构:
- 主要概念用矩形模块表示
- 流程用箭头连接
- 层次关系用上下或左右布局
- 每个模块有清晰的中文标签

【颜色方案】
- 主色: 深海军蓝 (#1a365d)
- 辅色: 钢蓝色 (#4a5568)
- 强调色: 柔和青色 (#38b2ac)
- 正向指示: 深绿色 (#276749)
- 负向指示: 深红色 (#c53030)
- 背景: 纯白色 (#FFFFFF)

【文字规范】
- 所有标签使用中文
- 数学符号使用标准格式
- 变量使用斜体: x, y, A, B
- 清晰易读的字体

Style Requirements:
- Background MUST be pure WHITE (#FFFFFF)
- Use rectangular shapes with sharp corners only
- All text labels in Chinese
- Professional academic publication quality
- No decorative elements
- No shadows or gradients
- Clean, minimal aesthetic
- Suitable for IEEE/journal figures
"""
    return prompt


def refine_with_style(description: str, source_context: str, caption: str) -> str:
    """
    Phase 2: Refine description for visual aesthetics
    融合 PaperBanana 的 Stylist 设计
    """
    prompt = f"""You are refining an academic diagram description for publication quality.

Title: "{caption}"

Design Style:
- Scientific journal publication quality
- Pure WHITE background (#FFFFFF)
- Clean, professional color palette
- Rectangular boxes with sharp corners
- Thin consistent borders
- Clear visual hierarchy

Source Context:
{source_context}

Current Description:
{description}

Refinement Requirements:
1. Ensure pure WHITE background
2. Use muted, professional colors (navy blue, steel blue, soft teal)
3. Specify consistent thin borders
4. All text in Chinese
5. Clear visual hierarchy
6. No decorative elements
7. No shadows or gradients

Output ONLY the refined description for image generation.
"""
    return prompt


def generate_image(prompt: str, aspect_ratio: str = "4:3", output_path: str = None, num_steps: int = 40) -> str:
    """
    使用本地图像生成服务
    优化参数: num_steps=40, cfg_scale=4.0
    """
    # 尺寸映射
    size_map = {
        "4:3": "2048x1536",
        "3:4": "1536x2048",
        "16:9": "2048x1152",
        "9:16": "1152x2048",
        "1:1": "1536x1536",
    }
    size = size_map.get(aspect_ratio, "2048x1536")

    response = requests.post(
        LOCAL_IMAGE_URL,
        json={
            "prompt": prompt,
            "size": size,
            "num_steps": num_steps,
            "cfg_scale": 4.0,  # 优化的CFG scale
            "seed": 42  # 固定seed确保可复现
        },
        timeout=300
    )

    result = response.json()

    if "data" in result and len(result["data"]) > 0:
        image_data = result["data"][0].get("b64_json") or result["data"][0].get("url")

        if output_path is None:
            output_path = OUTPUT_DIR / "generated_diagram.png"

        if image_data.startswith("http"):
            import urllib.request
            urllib.request.urlretrieve(image_data, output_path)
        else:
            with open(output_path, "wb") as f:
                f.write(base64.b64decode(image_data))

        return str(output_path)
    else:
        raise Exception(f"Image generation failed: {result}")


def main():
    """Main workflow"""
    if len(sys.argv) < 3:
        print("Usage: python local_paperbanana.py <input_file> <caption> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    caption = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    # 读取输入
    with open(input_file, 'r', encoding='utf-8') as f:
        source_context = f.read()

    print("=" * 60)
    print("Local PaperBanana - Academic Diagram Generation")
    print("=" * 60)

    # Phase 1: Generate description
    print("\n[Phase 1] Generating diagram description...")
    description_prompt = generate_diagram_description(source_context, caption)
    print("Description prompt generated.")

    # Phase 2: Refine with style
    print("\n[Phase 2] Refining for academic style...")
    refined_prompt = refine_with_style(description_prompt, source_context, caption)
    print("Style refinement complete.")

    # Phase 3: Generate image
    print("\n[Phase 3] Generating image...")
    output_path = generate_image(refined_prompt, "4:3", output_file)
    print(f"Image saved to: {output_path}")

    # 保存 prompt 供参考
    prompt_file = Path(output_path).with_suffix('.txt')
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(f"# Input: {input_file}\n")
        f.write(f"# Caption: {caption}\n\n")
        f.write("=== REFINED PROMPT ===\n\n")
        f.write(refined_prompt)

    print(f"Prompt saved to: {prompt_file}")
    print("\nDone!")

    return output_path


if __name__ == "__main__":
    main()

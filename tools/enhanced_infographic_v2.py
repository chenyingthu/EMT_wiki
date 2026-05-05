#!/usr/bin/env python3
"""
Enhanced Academic Infographic Generator V2
借鉴 SenseNova-U1 官方示例的最佳实践

关键改进：
1. 详细结构化prompt（1500-3000字符）
2. 清晰的布局描述（位置、视觉元素、文本）
3. 视觉隐喻和逻辑流
4. 专业配色方案
"""

import requests
import base64
from pathlib import Path
from typing import Optional
import sys
import json

# 配置
LOCAL_IMAGE_URL = "http://localhost:8000/v1/images/generations"
OUTPUT_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki/assets/figures")


def generate_academic_infographic_prompt(
    source_context: str,
    caption: str,
    aspect_ratio: str = "4:3"
) -> str:
    """
    生成高质量学术信息图prompt
    借鉴 SenseNova-U1 官方示例的详细描述风格
    """

    # 解析源内容的关键信息
    lines = [l.strip() for l in source_context.strip().split('\n') if l.strip()]

    prompt = f"""该信息图以"{caption}"为主题，采用专业学术期刊风格，整体设计简洁现代，具有科技感和专业性。背景采用深蓝色渐变色调，配以细微的网格线条，营造出严谨的学术氛围。画面长宽比为{aspect_ratio}。

**标题区域**
顶部中央以醒目的青蓝色粗体字呈现标题"{caption}"，标题下方配有一条金色装饰线，增强视觉层次感。标题右侧配有一个抽象的电路板图案图标，象征电力系统与仿真技术。

**核心内容区域**
整个信息图从左上至右下形成清晰的逻辑流，分为多个核心模块，每个模块均配有编号、标题、详细说明文字及对应视觉元素。

"""

    # 添加内容模块
    prompt += """**模块布局设计**

根据主题内容，设计以下信息架构：

1. **核心概念模块**（左上区域）
   - 视觉元素：使用矩形框表示核心概念，框内填充浅蓝色背景
   - 包含：主题定义、关键术语、核心公式
   - 连接方式：用中灰色箭头指向下一模块

2. **机制流程模块**（中部区域）
   - 视觉元素：使用流程图形式，从左到右排列
   - 每个步骤使用圆角矩形框，框内为深蓝色背景配白色文字
   - 步骤间用箭头连接，表示数据流或逻辑关系

3. **应用场景模块**（右侧区域）
   - 视觉元素：使用堆叠的卡片式设计
   - 每张卡片包含图标和简短描述
   - 用不同颜色区分不同应用类型

4. **对比分析模块**（底部区域）
   - 视觉元素：使用双列对比布局
   - 左列标注"适用场景"，使用绿色背景
   - 右列标注"限制边界"，使用橙色背景

"""

    # 添加源内容摘要
    prompt += f"""**具体内容**

{source_context[:1500]}

"""

    # 添加设计规范
    prompt += """**设计规范**

1. **颜色方案**
   - 主色：深海军蓝 (#1a365d)
   - 辅色：钢蓝色 (#4a5568)
   - 强调色：青蓝色 (#38b2ac)
   - 正向指示：翠绿色 (#276749)
   - 限制警示：琥珀色 (#c05621)
   - 背景：深蓝渐变

2. **文字规范**
   - 所有标签使用中文
   - 英文术语保留原文
   - 数学公式使用标准格式
   - 变量使用斜体：x, y, A, B
   - 使用清晰的无衬线字体

3. **视觉元素**
   - 矩形框：表示概念模块
   - 圆角矩形：表示流程步骤
   - 箭头：表示流程方向
   - 图标：表示功能类型
   - 装饰线条：分隔区域

4. **布局原则**
   - 从左到右的阅读流
   - 从上到下的信息层级
   - 模块间保持适当间距
   - 重要信息使用颜色强调

**输出要求**
- 所有文本使用简体中文
- 专业学术风格，适合IEEE期刊
- 清晰的信息层级和逻辑流
- 无装饰性元素干扰信息传达
"""

    return prompt


def generate_image(
    prompt: str,
    aspect_ratio: str = "4:3",
    output_path: str = None,
    num_steps: int = 50,
    cfg_scale: float = 4.0,
    seed: int = 42
) -> str:
    """使用本地图像生成服务"""

    # 尺寸映射（使用官方支持的分辨率）
    size_map = {
        "1:1": "2048x2048",
        "4:3": "2368x1760",
        "3:4": "1760x2368",
        "16:9": "2720x1536",
        "9:16": "1536x2720",
        "3:2": "2496x1664",
        "2:3": "1664x2496",
    }
    size = size_map.get(aspect_ratio, "2048x2048")

    print(f"  Resolution: {size}")
    print(f"  Steps: {num_steps}, CFG: {cfg_scale}, Seed: {seed}")
    print(f"  Prompt length: {len(prompt)} chars")
    print("  Generating...")

    response = requests.post(
        LOCAL_IMAGE_URL,
        json={
            "prompt": prompt,
            "size": size,
            "num_steps": num_steps,
            "cfg_scale": cfg_scale,
            "seed": seed
        },
        timeout=600
    )

    result = response.json()

    if "data" in result and len(result["data"]) > 0:
        image_data = result["data"][0].get("b64_json") or result["data"][0].get("url")

        if output_path is None:
            output_path = OUTPUT_DIR / "generated_infographic.png"

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
        print("Usage: python enhanced_infographic_v2.py <input_file> <caption> [output_file]")
        print("\nBatch mode: python enhanced_infographic_v2.py --batch <config.json>")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if sys.argv[1] == "--batch":
        # 批量模式
        config_file = sys.argv[2]
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)

        results = []
        for item in config.get("pages", []):
            print(f"\n[{item['name']}]")

            with open(item['source'], 'r', encoding='utf-8') as f:
                source_context = f.read()

            prompt = generate_academic_infographic_prompt(
                source_context,
                item['caption'],
                item.get('aspect_ratio', '4:3')
            )

            output_name = item.get('output_name', Path(item['source']).stem + "-infographic-v2")
            output_path = OUTPUT_DIR / f"{output_name}.png"

            try:
                result = generate_image(
                    prompt,
                    item.get('aspect_ratio', '4:3'),
                    str(output_path),
                    num_steps=item.get('num_steps', 50),
                    seed=item.get('seed', 42)
                )
                results.append((item['name'], True, result))

                # 保存prompt
                with open(output_path.with_suffix('.txt'), 'w', encoding='utf-8') as f:
                    f.write(f"# Source: {item['source']}\n")
                    f.write(f"# Caption: {item['caption']}\n\n")
                    f.write(prompt)

            except Exception as e:
                print(f"  ❌ Failed: {e}")
                results.append((item['name'], False, str(e)))

        print("\n" + "="*60)
        print("Batch Generation Summary")
        print("="*60)
        for name, success, path in results:
            status = "✅" if success else "❌"
            print(f"  {status} {name}")
            if success:
                print(f"      {path}")

    else:
        # 单文件模式
        input_file = sys.argv[1]
        caption = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None

        print("="*60)
        print("Enhanced Academic Infographic Generator V2")
        print("="*60)

        with open(input_file, 'r', encoding='utf-8') as f:
            source_context = f.read()

        prompt = generate_academic_infographic_prompt(source_context, caption)

        if output_file is None:
            output_file = OUTPUT_DIR / f"{Path(input_file).stem}-infographic-v2.png"

        output_path = generate_image(prompt, "4:3", str(output_file))
        print(f"\n✅ Done! Output: {output_path}")

        # 保存prompt
        prompt_file = Path(output_path).with_suffix('.txt')
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(f"# Input: {input_file}\n")
            f.write(f"# Caption: {caption}\n\n")
            f.write("=== PROMPT ===\n\n")
            f.write(prompt)

        print(f"Prompt saved to: {prompt_file}")


if __name__ == "__main__":
    main()

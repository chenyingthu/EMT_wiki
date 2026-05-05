#!/usr/bin/env python3
"""
Enhanced Academic Infographic Generator
融合 PaperBanana 方法论与 SenseNova-U1 直接模型加载

改进点:
1. 直接加载模型，绕过HTTP API，获得更多控制
2. 优化参数: cfg_scale=4.0, timestep_shift=3.0, num_steps=40
3. 结构化prompt模板，清晰的设计规范
4. 学术风格专门优化
"""

import torch
from transformers import AutoConfig, AutoModel, AutoTokenizer
from PIL import Image
import numpy as np
from pathlib import Path
import sys
import os

# 添加sensenova_u1模块路径
sys.path.insert(0, "/home/chenying/project/SenseNova-U1-code/src")

# 尝试导入sensenova_u1
try:
    import sensenova_u1
    from sensenova_u1 import check_checkpoint_compatibility
except ImportError as e:
    print(f"Error: sensenova_u1 not found: {e}")
    print("Make sure the module is available at /home/chenying/project/SenseNova-U1-code/src/")
    sys.exit(1)

# 配置
MODEL_PATH = "/home/chenying/project/SenseNova-U1-8B-MoT"
OUTPUT_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki/assets/figures")

NORM_MEAN = (0.5, 0.5, 0.5)
NORM_STD = (0.5, 0.5, 0.5)


def denorm(x: torch.Tensor) -> torch.Tensor:
    """Invert normalization back to [0, 1]."""
    mean = torch.tensor(NORM_MEAN, device=x.device, dtype=x.dtype).view(1, 3, 1, 1)
    std = torch.tensor(NORM_STD, device=x.device, dtype=x.dtype).view(1, 3, 1, 1)
    return (x * std + mean).clamp(0, 1)


def to_pil(batch: torch.Tensor) -> list:
    """Convert tensor to PIL images."""
    arr = denorm(batch.float()).permute(0, 2, 3, 1).cpu().numpy()
    arr = (arr * 255.0).round().astype(np.uint8)
    return [Image.fromarray(a) for a in arr]


def create_device_map():
    """Create optimized device map for low VRAM (16GB)."""
    device_map = {
        'vision_model': 0,
        'language_model.model.embed_tokens': 0,
    }
    # 前16层放在GPU上
    for i in range(16):
        device_map[f'language_model.model.layers.{i}'] = 0
    # 后26层放在CPU上
    for i in range(16, 42):
        device_map[f'language_model.model.layers.{i}'] = 'cpu'
    device_map['language_model.model.norm'] = 'cpu'
    device_map['language_model.model.norm_mot_gen'] = 'cpu'
    device_map['language_model.lm_head'] = 'cpu'
    device_map['fm_modules'] = 'cpu'
    return device_map


class AcademicInfographicGenerator:
    """学术信息图生成器，融合PaperBanana方法论"""

    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path
        self.model = None
        self.tokenizer = None
        self._load_model()

    def _load_model(self):
        """加载模型（延迟加载，只加载一次）"""
        if self.model is not None:
            return

        print("Loading SenseNova-U1 model...")
        config = AutoConfig.from_pretrained(self.model_path)
        check_checkpoint_compatibility(config)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)

        torch.cuda.empty_cache()
        device_map = create_device_map()
        self.model = AutoModel.from_pretrained(
            self.model_path,
            config=config,
            torch_dtype=torch.bfloat16,
            device_map=device_map,
            low_cpu_mem_usage=True
        )
        self.model.eval()
        print("Model loaded successfully!")

    def generate_description(self, source_context: str, caption: str) -> str:
        """
        Phase 1: 生成详细的设计描述
        借鉴PaperBanana的Planner设计
        """
        prompt = f"""Create a professional academic infographic diagram.

Title: "{caption}"

Design Style:
- Scientific journal publication quality
- Pure WHITE background (#FFFFFF) - this is critical
- Clean, professional color palette: navy blue, slate gray, soft teal
- Rectangular boxes with sharp corners (no rounded corners)
- Thin consistent borders (1-2px)
- Clear visual hierarchy
- No decorative elements, shadows, or gradients
- All text in Chinese

Content Sections:

【核心概念】
{source_context[:500]}

【图表结构】
- 左到右或上到下的流程布局
- 模块化矩形框
- 清晰的标签和注释
- 流程箭头使用中灰色

【颜色方案】
- 主色：深海军蓝 (Deep Navy Blue)
- 辅色：钢蓝色 (Steel Blue)
- 强调：柔和青色 (Soft Teal)
- 背景：纯白色 (Pure White #FFFFFF)

【文字要求】
- 所有标签使用中文
- 数学符号使用标准格式
- 变量使用斜体: x, y, A, B
- 清晰易读的无衬线字体

【布局要求】
- 白色背景，无纹理
- 矩形框带细微填充
- 模块间有适当留白
- 专业的学术出版物风格

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

    def generate_infographic(
        self,
        prompt: str,
        output_path: str,
        width: int = 2048,
        height: int = 1536,
        steps: int = 40,
        seed: int = 42
    ) -> bool:
        """生成信息图"""
        print(f"  Resolution: {width}x{height}")
        print(f"  Steps: {steps}, Seed: {seed}")
        print("  Generating...")

        try:
            result = self.model.t2i_generate(
                self.tokenizer,
                prompt,
                image_size=(width, height),
                cfg_scale=4.0,
                cfg_norm="none",
                timestep_shift=3.0,
                cfg_interval=(0.0, 1.0),
                num_steps=steps,
                batch_size=1,
                seed=seed,
                think_mode=False,
            )

            images = to_pil(result)
            images[0].save(output_path)

            file_size = os.path.getsize(output_path) / 1024 / 1024
            print(f"  ✅ Saved: {output_path} ({file_size:.2f} MB)")
            return True

        except Exception as e:
            print(f"  ❌ Failed: {e}")
            import traceback
            traceback.print_exc()
            return False

    def generate_for_wiki_page(
        self,
        source_file: str,
        caption: str,
        output_name: str = None,
        aspect_ratio: str = "4:3"
    ) -> str:
        """
        为wiki页面生成信息图

        Args:
            source_file: 源文本文件路径
            caption: 图表标题
            output_name: 输出文件名（不含扩展名）
            aspect_ratio: 宽高比 ("4:3", "3:4", "16:9", "1:1")
        """
        # 读取源文本
        with open(source_file, 'r', encoding='utf-8') as f:
            source_context = f.read()

        # 生成设计描述
        description = self.generate_description(source_context, caption)

        # 确定分辨率
        size_map = {
            "4:3": (2048, 1536),
            "3:4": (1536, 2048),
            "16:9": (2048, 1152),
            "9:16": (1152, 2048),
            "1:1": (1536, 1536),
        }
        width, height = size_map.get(aspect_ratio, (2048, 1536))

        # 生成输出路径
        if output_name is None:
            output_name = Path(source_file).stem + "-infographic"
        output_path = OUTPUT_DIR / f"{output_name}.png"

        # 生成图像
        success = self.generate_infographic(
            description,
            str(output_path),
            width=width,
            height=height
        )

        if success:
            # 保存prompt供参考
            prompt_file = output_path.with_suffix('.txt')
            with open(prompt_file, 'w', encoding='utf-8') as f:
                f.write(f"# Source: {source_file}\n")
                f.write(f"# Caption: {caption}\n\n")
                f.write("=== PROMPT ===\n\n")
                f.write(description)
            return str(output_path)
        else:
            return None


def main():
    """主函数 - 支持命令行和批量模式"""
    if len(sys.argv) < 3:
        print("Usage: python enhanced_infographic.py <input_file> <caption> [output_name]")
        print("\nBatch mode: python enhanced_infographic.py --batch <config_file>")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generator = AcademicInfographicGenerator()

    if sys.argv[1] == "--batch":
        # 批量模式
        import json
        config_file = sys.argv[2]
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)

        results = []
        for item in config.get("pages", []):
            print(f"\n[{item['name']}]")
            result = generator.generate_for_wiki_page(
                item['source'],
                item['caption'],
                item.get('output_name'),
                item.get('aspect_ratio', '4:3')
            )
            results.append((item['name'], result is not None))

        print("\n" + "="*60)
        print("Batch Generation Summary")
        print("="*60)
        for name, success in results:
            status = "✅" if success else "❌"
            print(f"  {status} {name}")

    else:
        # 单文件模式
        input_file = sys.argv[1]
        caption = sys.argv[2]
        output_name = sys.argv[3] if len(sys.argv) > 3 else None

        print("="*60)
        print("Enhanced Academic Infographic Generator")
        print("="*60)

        output_path = generator.generate_for_wiki_page(input_file, caption, output_name)

        if output_path:
            print(f"\n✅ Done! Output: {output_path}")
        else:
            print("\n❌ Generation failed")


if __name__ == "__main__":
    main()

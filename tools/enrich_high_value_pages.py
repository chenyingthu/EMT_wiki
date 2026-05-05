#!/usr/bin/env python3
"""
高价值页面内容增强脚本 - 基于EMT专业知识自动填充stub页面
"""
import os
import re
import glob

# EMT领域知识库 - 用于自动填充页面内容
EMT_KNOWLEDGE = {
    "电力系统网络": {
        "definition": "电力系统网络是由发电、输电、变电、配电和用电设备互联构成的能量传输与分配系统。在EMT仿真中，网络被建模为节点导纳矩阵，描述各节点电压与注入电流的关系。",
        "emt_role": [
            "建立节点导纳矩阵，求解网络电压电流分布",
            "处理开关事件引起的拓扑变化",
            "模拟故障条件下的网络响应",
            "分析谐波在网络中的传播特性"
        ],
        "branches": [
            "集中参数网络：基于RLC元件的等效电路模型",
            "分布参数网络：考虑波过程的传输线模型",
            "混合网络：结合集中与分布参数的多尺度模型",
            "等值网络：对外部系统的简化等值表示"
        ],
        "formal": """
节点电压方程：
$$\\mathbf{Y}(t)\\mathbf{v}(t) = \\mathbf{i}(t)$$

其中 $\\mathbf{Y}(t)$ 为时变导纳矩阵，$\\mathbf{v}(t)$ 为节点电压向量，$\\mathbf{i}(t)$ 为节点注入电流向量。

三相网络序分量变换：
$$\\begin{bmatrix} V_0 \\\\ V_1 \\\\ V_2 \\end{bmatrix} = \\frac{1}{3}\\begin{bmatrix} 1 & 1 & 1 \\\\ 1 & a & a^2 \\\\ 1 & a^2 & a \\end{bmatrix}\\begin{bmatrix} V_a \\\\ V_b \\\\ V_c \\end{bmatrix}$$

其中 $a = e^{j2\\pi/3}$ 为旋转算子。
        """,
        "boundaries": [
            "大规模网络节点数超过10,000时，直接求解计算代价高",
            "网络等值会丢失内部细节，不适合分析内部故障",
            "频率相关参数模型计算复杂度高"
        ],
        "relations": [
            "[[nodal-analysis]] - 节点分析法基础",
            "[[transmission-line-model]] - 输电线路建模",
            "[[network-equivalent]] - 网络等值方法",
            "[[emt-simulation]] - EMT仿真基础"
        ],
        "sources": [
            "EMTP Theory Book - 网络建模理论",
            "Power System Analysis by Grainger & Stevenson"
        ]
    },

    "电磁暂态-emt-仿真": {
        "definition": "电磁暂态（EMT）仿真是对电力系统电磁过程进行时域数值模拟的方法，能够精确描述纳秒至秒级时间范围内的电压电流瞬态变化。",
        "emt_role": [
            "分析开关操作、故障、雷击引起的快速暂态过程",
            "研究电力电子设备的开关特性和控制策略",
            "验证保护装置的暂态响应特性",
            "评估绝缘配合和过电压水平"
        ],
        "branches": [
            "离线仿真：高精度的非实时仿真",
            "实时仿真：满足硬实时约束的仿真",
            "硬件在环仿真：与物理控制器交互的仿真",
            "多速率仿真：不同时间尺度的混合仿真"
        ],
        "formal": """
EMT仿真的核心离散化方程：

梯形法则离散：
$$x_{n+1} = x_n + \\frac{h}{2}(f(t_n, x_n) + f(t_{n+1}, x_{n+1}))$$

节点导纳方程：
$$\\mathbf{Y}_n\\mathbf{v}_n = \\mathbf{i}_n^{hist} + \\mathbf{i}_n^{src}$$

其中 $\\mathbf{i}_n^{hist}$ 为历史电流源，$\\mathbf{i}_n^{src}$ 为独立电流源。

时间步长选择准则：
$$h \\leq \\frac{1}{10 f_{max}}$$

$f_{max}$ 为关注的最高频率分量。
        """,
        "boundaries": [
            "计算精度受时间步长和数值积分方法影响",
            "大规模系统实时仿真的计算资源需求高",
            "模型参数准确性直接影响仿真结果可信度"
        ],
        "relations": [
            "[[numerical-integration]] - 数值积分方法",
            "[[real-time-simulation]] - 实时仿真技术",
            "[[hil-simulation]] - 硬件在环仿真",
            "[[multirate-method]] - 多速率仿真方法"
        ],
        "sources": [
            "Dommel, H.W. (1969). Digital Computer Solution of Electromagnetic Transients",
            "EMTP-RV Theory Manual"
        ]
    },

    "机电暂态模型": {
        "definition": "机电暂态模型描述电力系统机电耦合动态过程，重点关注转子运动、频率变化和功角稳定性，时间尺度通常为0.1秒至几十秒。",
        "emt_role": [
            "分析功角稳定和暂态稳定性",
            "研究频率响应和负荷特性",
            "评估系统扰动后的恢复过程",
            "与电磁暂态模型接口实现混合仿真"
        ],
        "branches": [
            "经典模型：恒定电压源 behind 暂态电抗",
            "详细模型：考虑励磁系统和调速器动态",
            "简化模型：用于大规模系统稳定性分析",
            "等值模型：对同调机群的聚合表示"
        ],
        "formal": """
摇摆方程（Swing Equation）：
$$M\\frac{d^2\\delta}{dt^2} = P_m - P_e - D\\frac{d\\delta}{dt}$$

其中 $M$ 为惯性常数，$\\delta$ 为功角，$P_m$ 为机械功率，$P_e$ 为电磁功率，$D$ 为阻尼系数。

电磁功率方程：
$$P_e = \\frac{EV}{X}\\sin\\delta$$

小信号线性化：
$$\\Delta \\dot{x} = A\\Delta x + B\\Delta u$$
        """,
        "boundaries": [
            "忽略电磁暂态过程，不适用于快速暂态分析",
            "假设系统三相平衡，不对称故障需要特殊处理",
            "模型简化可能丢失关键动态特性"
        ],
        "relations": [
            "[[electromechanical-electromagnetic-hybrid-simulation]] - 机电电磁混合仿真",
            "[[synchronous-machine-model]] - 同步电机模型",
            "[[transient-stability]] - 暂态稳定性分析",
            "[[power-system-stability]] - 电力系统稳定性"
        ],
        "sources": [
            "Kundur, P. (1994). Power System Stability and Control",
            "Anderson & Fouad. Power System Control and Stability"
        ]
    },

    "故障穿越": {
        "definition": "故障穿越（Fault Ride Through, FRT）是指电力设备（如风机、光伏逆变器）在电网故障期间维持并网运行而不脱网的能力，是现代并网标准的核心要求。",
        "emt_role": [
            "验证新能源设备在低电压穿越（LVRT）期间的动态响应",
            "分析故障期间的无功功率支撑能力",
            "评估故障清除后的有功功率恢复特性",
            "研究不对称故障下的负序电流控制"
        ],
        "branches": [
            "低电压穿越（LVRT）：电压跌落时的维持运行",
            "高电压穿越（HVRT）：电压升高时的维持运行",
            "零电压穿越（ZVRT）：完全失压时的短时支撑",
            "不对称故障穿越：负序电压存在时的控制策略"
        ],
        "formal": """
低电压穿越要求：

电压-时间曲线：
- 电压跌落至20%额定电压：维持运行至少625ms
- 电压跌落至0：维持运行至少150-200ms

无功电流注入要求：
$$I_q \\geq K(0.9 - U_t)I_N$$

其中 $K$ 为无功增益系数（通常1.5-2），$U_t$ 为端电压标幺值，$I_N$ 为额定电流。

有功功率恢复：
$$P(t) = P_0(1 - e^{-t/\\tau_{rec}})$$

恢复时间常数 $\\tau_{rec}$ 通常2-5s。
        """,
        "boundaries": [
            "故障期间设备电流容量限制",
            "直流母线电压波动对逆变器的影响",
            "多机并联时的环流和协调控制问题"
        ],
        "relations": [
            "[[lvrt-control]] - 低电压穿越控制",
            "[[gfl-inverter-model]] - 跟网型逆变器模型",
            "[[gfm-inverter-model]] - 构网型逆变器模型",
            "[[fault-analysis-methods]] - 故障分析方法"
        ],
        "sources": [
            "Grid Code Requirements for Wind Turbine Generators",
            "IEEE 1547-2018 Standard for Interconnection"
        ]
    }
}

def get_stub_pages():
    """获取所有高价值stub页面"""
    stub_pages = []
    for filepath in glob.glob('wiki/**/*.md', recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'high-value-link' in content and '本页面为高价值断链' in content:
                # 提取标题
                match = re.search(r'title:\s*"([^"]+)"', content)
                if match:
                    title = match.group(1)
                    stub_pages.append((filepath, title))
        except:
            pass
    return stub_pages

def generate_enhanced_content(title):
    """基于知识库生成增强内容"""
    # 尝试匹配知识库中的条目
    for key, data in EMT_KNOWLEDGE.items():
        if key in title or title in key:
            return generate_page_content(title, data)

    # 通用模板
    return generate_generic_content(title)

def generate_page_content(title, data):
    """生成完整的页面内容"""
    return f"""---
title: "{title}"
type: method
tags: [{title.lower().replace(' ', '-')}, high-value-link, auto-enriched]
created: "2026-05-05"
---

# {title}

## 定义与边界

{data['definition']}

**边界限定**：适用于电力系统电磁暂态仿真分析，时间尺度覆盖微秒至秒级。

## EMT中的作用

{chr(10).join(['- ' + item for item in data['emt_role']])}

## 主要分支与机制

{chr(10).join(['- ' + item for item in data['branches']])}

## 形式化表达

{data['formal']}

## 适用边界与失败模式

{chr(10).join(['- ' + item for item in data['boundaries']])}

## 与相关页面的关系

{chr(10).join(['- ' + item for item in data['relations']])}

## 代表性来源

{chr(10).join(['- ' + item for item in data['sources']])}

---

*本页面由自动增强脚本生成并补充专业内容。最后更新：2026-05-05*
"""

def generate_generic_content(title):
    """生成通用内容模板"""
    return f"""---
title: "{title}"
type: method
tags: [{title.lower().replace(' ', '-')}, high-value-link]
created: "2026-05-05"
---

# {title}

## 定义与边界

{title}是电力系统电磁暂态仿真中的重要概念，涉及电力网络的分析与建模。

**边界限定**：待进一步完善。

## EMT中的作用

- 支撑电力系统暂态过程分析
- 为保护和控制设计提供仿真验证
- 与[[emt-simulation]]紧密相关

## 主要分支与机制

- 基础理论与方法
- 数值实现技术
- 工程应用案例

## 形式化表达

- 待补充数学模型与公式

## 适用边界与失败模式

- 模型精度与计算效率的权衡
- 参数敏感性分析

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础

## 代表性来源

- 待补充学术文献

---

*本页面为自动生成的增强模板，需要进一步补充专业内容。*
"""

def main():
    print("=" * 60)
    print("高价值页面内容增强脚本")
    print("=" * 60)

    stub_pages = get_stub_pages()
    print(f"发现高价值stub页面: {len(stub_pages)}个")

    # 处理所有剩余页面
    batch_size = len(stub_pages)
    processed = 0

    print(f"\n开始增强（本次处理全部{batch_size}个）...")

    for filepath, title in stub_pages:
        try:
            # 生成增强内容
            new_content = generate_enhanced_content(title)

            # 写回文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✓ 增强: {title}")
            processed += 1
        except Exception as e:
            print(f"  ✗ 失败: {title} - {e}")

    print(f"\n本批次共增强: {processed} 个页面")
    print(f"剩余待增强: {len(stub_pages) - processed} 个")

    return len(stub_pages) - processed

if __name__ == '__main__':
    import sys
    remaining = main()
    sys.exit(0 if remaining == 0 else 1)

---
title: "Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Access;2025;13; ;10.1109/ACCESS.2025.3561788"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Nurunnabi 等 - 2025 - Advancing Grid-Forming Inverter Technology Comprehensive PQ Capability and Performance Analysis.pdf"]
---

# Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis

**作者**: 
**年份**: 2025
**来源**: `06/Nurunnabi 等 - 2025 - Advancing Grid-Forming Inverter Technology Comprehensive PQ Capability and Performance Analysis.pdf`

## 摘要

This paper presents a performance analysis of grid-forming (GFM) inverter technology, which is essential to ensure stable and reliable operation of power systems with high penetration of inverter-based resources (IBRs). Recognizing that IBR operational constraints are distinct from those of synchronous generators, this study develops advanced PQ capability models and algorithmic frameworks that accurately characterize GFM inverter operational constraints across various coupling filter configurations (L, LC, and LCL). Electromagnetic transient (EMT) simulations show that the Enhanced Voltage Regulation (EVR) and Controlled Proportional-Integral Droop (CPID) strategies proposed in this paper improve voltage and frequency stability under dynamic loading and fault conditions, outperforming con

## 核心贡献


- 提出考虑PWM饱和与电流约束的构网型逆变器PQ能力边界建模算法
- 设计增强型电压调节与比例积分下垂控制策略以提升动态稳定性
- 揭示L/LC/LCL滤波器拓扑对逆变器谐波抑制与运行域的影响机制


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时硬件在环验证|实时硬件在环验证]]
- [[下垂控制|下垂控制]]
- [[增强型电压调节|增强型电压调节]]
- [[pq能力边界算法|PQ能力边界算法]]
- [[pwm饱和约束建模|PWM饱和约束建模]]


## 涉及的模型


- [[构网型逆变器-gfm|构网型逆变器(GFM)]]
- [[跟网型逆变器-gfl|跟网型逆变器(GFL)]]
- [[l-lc-lcl耦合滤波器|L/LC/LCL耦合滤波器]]
- [[pwm调制模型|PWM调制模型]]
- [[随机混合负载|随机混合负载]]


## 相关主题


- [[构网型逆变器控制|构网型逆变器控制]]
- [[pq能力分析|PQ能力分析]]
- [[低惯量电网稳定性|低惯量电网稳定性]]
- [[电能质量与谐波抑制|电能质量与谐波抑制]]
- [[实时仿真验证|实时仿真验证]]
- [[ieee-1547标准符合性|IEEE 1547标准符合性]]


## 主要发现


- EMT仿真表明EVR与CPID策略在动态负载与故障下电压频率稳定性更优
- 硬件实验证实所提控制能有效抑制谐波并实现故障后快速恢复
- 不同滤波器配置下PQ边界模型准确刻画了逆变器实际运行约束



## 方法细节

### 方法概述

本文提出一种综合考虑PWM饱和与额定电流约束的构网型（GFM）逆变器PQ能力边界建模方法。首先，基于L、LC、LCL三种耦合滤波器拓扑推导PCC点有功/无功功率方程，建立逆变器输出特性模型。其次，设计PQ能力边界计算算法，通过求解额定电流圆（RIC）与PWM饱和约束圆的交集，精确刻画不同PCC电压与直流母线电压下的实际运行域。在控制层面，对比基础下垂控制（FDR）与增强型电压调节（EVR）策略，引入内环PI控制器与抗积分饱和机制，优化动态电压/频率响应。最后，通过电磁暂态（EMT）仿真与实时硬件在环（HIL）实验，在随机混合负载、故障穿越及GFM/GFL并联场景下验证所提模型与控制策略的有效性，确保系统满足IEEE 1547标准。

### 数学公式


**公式1**: $$$P_{PCC} \approx V_{PCC} \frac{E_{inv}}{X_F} \delta_{inv}$$$

*PCC点有功功率近似方程，用于分析相角差对有功传输的影响*


**公式2**: $$$Q_{PCC} \approx V_{PCC} \frac{E_{inv} - V_{PCC\_F}}{X_F}$$$

*PCC点无功功率近似方程，用于分析电压幅值差对无功传输的影响*


**公式3**: $$$\sqrt{(P^*_{PCC})^2 + (Q^*_{PCC})^2} \le S_{rated}$$$

*基于额定视在功率的PQ指令约束条件*


**公式4**: $$$|\vec{I}_{PCC}| \le I_{rated}$$$

*基于额定电流的PQ能力约束，防止低电压工况下过流*


**公式5**: $$$|\vec{E}_{inv}| \le E_{max}$$$

*PWM调制饱和约束，$E_{max}$取决于调制策略与直流母线电压*


**公式6**: $$$f_{ik} = f_{set} + m_{pi}(P_{kset\_i} - P_{ki})$$$

*有功-频率下垂控制方程，实现无通信自主频率调节*


**公式7**: $$$V_{ik} = V_{set} + m_{qi}(Q_{kset\_i} - Q_{ki})$$$

*无功-电压下垂控制方程，实现无通信自主电压调节*


### 算法步骤

1. 设定系统基准参数（额定容量、直流母线电压、PCC额定电压、滤波器阻抗参数）。

2. 根据当前PCC实际电压与直流母线电压，计算所选PWM策略（SPWM或SVPWM）下的最大允许逆变器输出电压幅值$E_{max}$。

3. 基于额定电流$I_{rated}$与当前PCC电压，在PQ复平面上绘制额定电流约束圆（RIC），确定电流安全边界。

4. 结合滤波器拓扑等效阻抗$X_F$与$E_{max}$，推导并绘制PWM饱和约束边界曲线，确定电压调制极限。

5. 计算RIC与PWM约束边界的几何交集区域，该交集即为当前工况下的实际PQ能力运行域。

6. 若PCC电压或直流电压发生波动，动态更新约束圆半径与边界曲线，实时修正下发给控制器的PQ指令限值，防止过流或调制饱和。


### 关键参数

- **额定容量**: 100 kVA

- **直流母线电压**: 1500 V

- **PCC线电压**: 690 V / 60 Hz

- **L滤波器参数**: L=4 mH, R=0.012 Ω

- **LC滤波器参数**: C=25 μF, L/R同L滤波器

- **LCL滤波器参数**: 两侧L=2 mH, R=0.006 Ω, C=25 μF

- **P-f下垂系数**: 1%

- **Q-V下垂系数**: 3%

- **短路容量(Ssc)**: 316 kVA



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 阻性负载阶跃变化 | 负载从25kW逐步增加至100kW（步长25kW）。EVR策略下电压偏差始终控制在±5%以内，暂态跌落后毫秒级恢复至稳态。 | 相比FDR策略，EVR在负载突变时的电压恢复速度提升显著，稳态偏差降低约60%。 |

| 感性负载切换与下垂系数优化 | 依次切换0.6滞后、1.0、0.9滞后功率因数负载。采用3% Q-V下垂系数时，系统暂态超调最小，稳态电压精度最高。 | 3%下垂系数在恢复速度与稳态精度间取得最优平衡，频率波动始终<0.1Hz，优于其他测试系数。 |

| 容性负载突投 | 容性负载突然重连导致电压暂态超调约15%。EVR策略配合LCL滤波器有效抑制振荡。 | EVR将最大电压偏差限制在2.9%以内，频率偏差仅0.37%，远优于传统下垂控制的超调水平。 |



## 量化发现

- SVPWM调制下最大允许输出电压达1.53 p.u.，较SPWM的1.33 p.u.提升约15%，显著扩大PQ运行域。
- 逆变器输出端短路容量计算值为316 kVA，为故障穿越与限流保护提供精确基准。
- EVR策略在动态负载下将电压最大偏差限制在2.9%以内，频率最大偏差控制在0.37%以内，严格满足IEEE 1547标准。
- 3% Q-V下垂系数使暂态电压恢复时间缩短至毫秒级，稳态电压精度提升约40%。
- 不同滤波器拓扑对PQ边界影响微弱，但LC滤波器在容性负载切换时电压波动略高，需配合EVR策略抑制。


## 关键公式

### PCC点功率传输方程

$$$P_{PCC} \approx V_{PCC} \frac{E_{inv}}{X_F} \delta_{inv}, \quad Q_{PCC} \approx V_{PCC} \frac{E_{inv} - V_{PCC\_F}}{X_F}$$$

*用于推导L/LC/LCL滤波器拓扑下的有功/无功传输特性，是下垂控制与PQ建模的基础*

### PQ能力双重约束方程

$$$|\vec{I}_{PCC}| \le I_{rated} \quad \text{且} \quad |\vec{E}_{inv}| \le E_{max}$$$

*用于实时计算并限制逆变器指令，防止低电压工况过流与PWM调制饱和*

### 基础下垂控制律

$$$f_{ik} = f_{set} + m_{pi}(P_{kset\_i} - P_{ki}), \quad V_{ik} = V_{set} + m_{qi}(Q_{kset\_i} - Q_{ki})$$$

*实现GFM逆变器无通信自主功率分配与电压/频率支撑，构成FDR与EVR策略的核心*



## 验证详情

- **验证方式**: 电磁暂态(EMT)仿真与实时硬件在环(HIL)实验验证
- **测试系统**: 含L/LC/LCL耦合滤波器的100kVA GFM逆变器并网系统，接入随机混合负载及并联GFL逆变器
- **仿真工具**: MATLAB/Simulink (EMT建模与仿真), 实时硬件实验平台 (HIL验证)
- **验证结果**: 仿真与硬件结果高度一致，验证了EVR与CPID策略在动态负载、故障穿越及谐波抑制方面的优越性。系统THD、电压/频率偏差均严格满足IEEE 1547标准，PQ能力边界算法有效防止了过流与调制饱和，证实了GFM/GFL并联运行的可行性与低惯量电网下的稳定性。

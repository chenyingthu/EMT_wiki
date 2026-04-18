---
title: "An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3003250"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation.pdf"]
---

# An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation

**作者**: 
**年份**: 2020
**来源**: `07&08/An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation.pdf`

## 摘要

—When lightning strikes a transmission line tower or shield wires, electromagnetic waves propagate through the tower back and forth, increasing the voltage across insulator strings. Tis can eventually lead to a back-ﬂashover (BF), which may cause damage to equipment or costly power outages. To calculate the over-voltages and predict the probability of a BF, an accurate model of the tower and its grounding system is needed in electromagnetic transient (EMT) type simulators. Tere are a number of theoretical models for the equivalent circuit of a transmission tower. However, they either are not accurate enough or they are derived for a certain type of transmission tower, which limits their applicability. Numerical electromagnetic analyses have less simpliﬁcations compared to the theoretical s

## 核心贡献


- 提出基于细线近似与NEC4的自动化建模流程，精确计算任意杆塔冲击阻抗
- 采用频域冲击阻抗定义，消除电流波形依赖性，实现仅依赖几何特性的通用计算
- 完整考虑杆塔结构细节与接地极有限电阻，突破传统简化理论模型的适用局限


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[细线近似|细线近似]]
- [[nec4数值电磁计算|NEC4数值电磁计算]]
- [[频域阻抗分析|频域阻抗分析]]
- [[自动化线网生成|自动化线网生成]]


## 涉及的模型


- [[输电杆塔|输电杆塔]]
- [[接地系统|接地系统]]
- [[水平接地极|水平接地极]]
- [[损耗大地模型|损耗大地模型]]


## 相关主题


- [[雷电冲击过电压|雷电冲击过电压]]
- [[杆塔冲击阻抗|杆塔冲击阻抗]]
- [[反击闪络预测|反击闪络预测]]
- [[数值电磁分析|数值电磁分析]]
- [[接地系统建模|接地系统建模]]


## 主要发现


- 数值模型精确计及杆塔细节与接地电阻，所得冲击阻抗显著区别于传统简化理论模型
- 频域阻抗定义完全独立于注入电流波形，为电磁暂态仿真提供稳定通用的参数表征
- 仿真验证了模型在不同接地极长度与土壤电阻率下准确计及接地电阻的能力



## 方法细节

### 方法概述

本文提出一种基于细线近似与矩量法(MoM)的杆塔冲击阻抗数值计算模型。该方法摒弃传统理论模型对杆塔几何形状的过度简化（如圆柱或圆锥近似），直接利用NEC4电磁求解器对杆塔全尺寸结构进行离散化建模。核心创新在于采用频域冲击阻抗定义$Z(f)=V(f)/I(f)$，彻底消除时域定义对注入雷电流波形的依赖性，使阻抗仅取决于杆塔几何与电磁特性。同时，开发自动化流程将CAD文件转换为NEC4线网坐标，并完整计及横担、斜材等结构细节及接地极有限电阻，为EMT仿真提供高精度、通用性强的杆塔等效模型。

### 数学公式


**公式1**: $$$z(t) = \frac{v(t)}{i(t)}$$$

*瞬态冲击阻抗时域定义，仅适用于电压与电流波形相同的纯电阻电路*


**公式2**: $$$z(t) = \frac{v(t)}{\max[i(t)]}$$$

*基于阶跃或斜坡电流注入的冲击阻抗定义，仍受波形影响*


**公式3**: $$$Z = \frac{\max[v(t)]}{I}$$$

*工程常用时域定义（电压峰值与对应时刻电流之比），但严重依赖注入电流波形*


**公式4**: $$$Z(f) = \frac{V(f)}{I(f)}$$$

*本文采用的频域冲击阻抗定义，仅依赖几何与电磁特性，消除波形依赖性*


### 算法步骤

1. 获取杆塔三维CAD模型（.step格式），提取所有结构部件（主腿、横担、斜材等）的精确几何坐标。

2. 运行自动化转换脚本，将CAD几何数据解析并映射为NEC4可识别的细线网格（wire-grid）表示，生成各线段的起点与终点坐标矩阵。

3. 在NEC4环境中构建电磁计算模型，设置边界条件为完美电导体(PEC)地面或含有限电阻率及水平接地极的损耗大地模型。

4. 在杆塔顶部设置电流注入端口，布置水平延伸的电压参考线与电流引线（长度115m），末端接入匹配电阻$R_c$以吸收行波、抑制反射干扰。

5. 调用基于矩量法(MoM)的频域求解器，在0.1~250 MHz频率范围内求解电场积分方程，获取顶部电压$V(f)$与注入电流$I(f)$的频域响应。

6. 根据频域定义$Z(f)=V(f)/I(f)$直接计算冲击阻抗谱，必要时通过逆傅里叶变换(IFFT)重构时域电压/电流波形。

7. 对比不同结构细节（如是否包含横担、斜材）及接地条件（土壤电阻率、接地极长度）对阻抗的影响，输出最终等效参数供EMT仿真调用。


### 关键参数

- **frequency_range**: 0.1 ~ 250 MHz

- **cylinder_validation_height**: 3 m 与 15 m

- **cylinder_radius**: 2.5 mm 与 25.4 mm

- **lead_length**: 115 m (确保反射波在观测窗口外)

- **voltage_probe_resistance**: 10 kΩ

- **soil_resistivity**: 100 Ωm 与 1000 Ωm

- **counterpoise_length**: 5 ~ 20 m

- **current_rise_time_range**: 10 ns ~ 80 ns (阶跃/斜坡), 10 μs ~ 200 μs (双指数)

- **matching_resistance**: $R_c$ (引线末端匹配)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 15m垂直圆柱体PEC地面验证 | 注入上升沿5ns的阶跃电流，计算$t_0=2h/c$时刻阻抗。仿真波形与文献实测数据高度吻合，实测冲击阻抗为320Ω，仿真结果在幅值与波形上升沿上精确复现。 | 与Hara等人实测数据误差极小，验证了NEC4细线模型在简单几何体上的高精度与可靠性。 |

| 时域阻抗波形依赖性分析 | 对15m圆柱注入不同上升沿(10~80ns)的阶跃电流，按传统峰值定义计算阻抗。阻抗值从324.6Ω降至293Ω；双指数波形下从316.8Ω(T1=10μs)降至232.5Ω(T1=200μs)。 | 证明传统时域定义受波形影响显著（最大偏差达9.7%），而本文频域定义完全独立于波形，提供稳定基准。 |

| 400kV双回路杆塔全细节建模 | 自动化生成包含横担、斜材的完整线网模型，计及接地极有限电阻。计算结果与传统简化理论模型（如Wagner、Jordan等给出的129~285Ω）存在显著差异。 | 突破传统模型仅适用于特定塔型的局限，提供全几何细节下的高保真阻抗参数，显著提升EMT仿真中反击闪络预测的准确性。 |



## 量化发现

- 传统时域峰值定义下，15m圆柱冲击阻抗随阶跃电流上升沿(10~80ns)增加从324.6Ω下降至293Ω，相对变化达9.7%。
- 双指数雷电流波形下，冲击阻抗随波头时间(T1=10μs至200μs)增加从316.8Ω大幅降至232.5Ω，证实时域定义的波形强依赖性。
- 频域阻抗定义$Z(f)=V(f)/I(f)$完全消除波形影响，仅由杆塔几何尺寸与电磁参数决定，为EMT仿真提供稳定通用基准。
- 自动化CAD转线网流程成功应用于400kV双回路杆塔，完整保留横担与斜材结构，计算结果显著区别于传统简化模型（差异可达数十至百欧姆量级）。
- 模型可灵活配置土壤电阻率(100/1000Ωm)与接地极长度(5~20m)，精确计及接地系统有限电阻对高频暂态的衰减与波速调整作用。


## 关键公式

### 频域冲击阻抗定义

$$$Z(f) = \frac{V(f)}{I(f)}$$$

*用于消除时域定义对雷电流波形的依赖，仅反映杆塔几何与电磁特性，适用于任意波形输入的EMT仿真建模与反击闪络概率计算。*



## 验证详情

- **验证方式**: 数值仿真与已发表实验数据对比验证
- **测试系统**: 垂直圆柱体(3m/15m高)置于PEC地面，及400kV双回路输电杆塔（含横担、斜材及水平接地极）
- **仿真工具**: NEC4 (Numerical Electromagnetic Code v4, 基于MoM的频域电磁求解器)
- **验证结果**: 仿真电流/电压波形与Hara等人实测数据在幅值和波形上高度一致；频域阻抗计算稳定可靠，成功验证了细线近似与自动化建模流程在复杂杆塔暂态分析中的有效性与高精度，为EMT型仿真器提供了无需波形假设的通用杆塔阻抗模型。

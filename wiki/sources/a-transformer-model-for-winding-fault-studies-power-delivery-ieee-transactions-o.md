---
title: "A transformer model for winding fault studies - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/04/61.296246.pdf.pdf"]
---

# A transformer model for winding fault studies - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `04/61.296246.pdf.pdf`

## 摘要

This paper deals with a method of modeling intemal faults in a power transformer. The method leads to a model which is entirely compatible with the EMTP software. It enables simulation of faults between any turn and the earth or between any two turns of the transformer windings. Implementation of the proposed method assumes knowledge of how to evaluate the leakage factors between the various coils of the transformer. A very simple method is proposed to evaluate these leakage factors. At last, an experimental validation of the model allows the estimation of its accuracy. INTRODUCTION The development and the validation of algorithms for a digital differential transformer protection require the preliminary determination of a power transformer model [SI. This model must allow to simulate all t

## 核心贡献


- 提出线圈分割法构建变压器内部故障模型，将EMTP标准6阶RL矩阵扩展为7或8阶
- 结合一致性、漏磁与比例原则，推导故障子绕组自感与互感矩阵元素的解析计算公式
- 建立仅依赖几何尺寸与故障位置的漏磁系数快速评估方法，免除额外短路试验需求


## 使用的方法


- [[bctran例程|BCTRAN例程]]
- [[矩阵扩展法|矩阵扩展法]]
- [[漏磁系数计算|漏磁系数计算]]
- [[多绕组耦合建模|多绕组耦合建模]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[绕组故障模型|绕组故障模型]]
- [[匝间短路模型|匝间短路模型]]
- [[对地短路模型|对地短路模型]]


## 相关主题


- [[变压器内部故障|变压器内部故障]]
- [[继电保护验证|继电保护验证]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[漏磁参数辨识|漏磁参数辨识]]


## 主要发现


- 扩展矩阵模型可精确复现匝间及对地故障暂态波形，实验测量数据与仿真结果高度吻合
- 几何漏磁系数评估法在无需额外试验条件下，仍能保证故障短路电流计算的高精度
- 模型在正常工况下与原BCTRAN矩阵等效，故障时能准确表征漏抗突变对电流的影响



## 方法细节

### 方法概述

本文提出一种基于矩阵扩展的变压器内部故障建模方法，完全兼容EMTP软件。核心思想是将发生故障的绕组按故障点位置分割为多个子绕组（匝地故障分为2个，匝间故障分为3个），从而将BCTRAN例程生成的标准6阶电阻[R]和电感[L]矩阵扩展为7阶或8阶。通过引入“一致性、漏磁、比例性”三大物理原则，构建关于子绕组自感与互感的非线性方程组，并结合变压器几何尺寸与故障位置快速计算漏磁系数，无需额外短路试验。最终求解得到的扩展矩阵可直接作为EMTP中的互耦R-L支路进行电磁暂态仿真。

### 数学公式


**公式1**: $$$L_3 = L_a + L_b + 2M_{ab}$$$

*一致性原则：子绕组串联后的等效电感必须等于原BCTRAN矩阵中的绕组自感$L_3$*


**公式2**: $$$\sigma_{ab} = 1 - \frac{M_{ab}^2}{L_a L_b}$$$

*漏磁原则：定义子绕组a与b之间的漏磁系数，反映磁耦合损耗程度*


**公式3**: $$$\frac{L_a}{L_b} = \left(\frac{n_a}{n_b}\right)^2$$$

*比例性原则：假设无漏磁时，子绕组自感比等于匝数比的平方，用于近似求解*


**公式4**: $$$k_c = \frac{L_{cc1}^{\text{BCTRAN}}}{L_{cc1}^{\text{geometric}}}$$$

*几何修正系数：利用BCTRAN基准漏感校准纯几何计算法得出的漏感，消除经验误差*


### 算法步骤

1. 步骤1：调用EMTP内置BCTRAN例程，基于正序/零序励磁与短路试验数据，生成标准6阶电阻矩阵[R]和电感矩阵[L]作为无故障基准模型。

2. 步骤2：根据故障类型与位置，将故障绕组分割为子绕组（匝地故障分为a、b两段；匝间故障分为a、b、c三段），记录各段匝数$n_a, n_b, n_c$。

3. 步骤3：基于变压器几何尺寸（铁芯高度h、半径R、绕组厚度$a_1, a_2$及间隙$a_{12}$），利用安培环路定律与磁场能量积分法计算理论漏磁系数$\sigma_{ij}$，并引入修正系数$k_c$进行校准。

4. 步骤4：结合一致性、漏磁与比例性三大原则，构建包含未知自感($L_a, L_b, L_c$)与互感($M_{ab}, M_{ac}, M_{bc}$)的非线性代数方程组。

5. 步骤5：采用数值迭代算法（如IMSL Fortran库例程）求解该非线性方程组，获得扩展矩阵中所有新增的电感元素。

6. 步骤6：按匝数比例分配原绕组电阻，构建对应的7阶或8阶电阻矩阵[R]。

7. 步骤7：将扩展后的[R, L]矩阵导出为EMTP可读格式，作为互耦R-L支路接入系统网络进行暂态仿真。


### 关键参数

- **n_a, n_b, n_c**: 故障分割后各子绕组的匝数，由故障位置直接决定

- **σ_ij**: 子绕组i与j之间的漏磁系数，取值范围(0,1)，越接近1表示耦合越弱

- **k_c**: 几何漏感修正系数，用于补偿理论磁场分布假设带来的偏差，通常接近1

- **L_3**: BCTRAN计算的原故障绕组总自感，作为一致性约束的基准值

- **k**: 匝数比参数$k = n_a/n_b$，用于比例性近似计算



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 高压侧匝地故障（A相第583匝对地） | 仿真电流波形与实测波形高度重合，暂态峰值与稳态幅值匹配良好，相位偏移极小。 | 相比传统固定参数模型，该模型能动态反映故障点位置变化引起的漏抗突变，幅值误差<10%，相位误差<10°。 |

| 高压侧匝间故障（A相第1167匝与1266匝短路，间隔半层） | 成功复现匝间短路引起的环流暂态过程，子绕组重叠区域对漏磁系数的影响被准确捕捉。 | 在无需额外短路试验数据的前提下，仿真精度与实测数据偏差控制在10%以内，显著优于依赖经验参数的等效电路法。 |



## 量化发现

- 在16次匝地故障与数十次匝间故障测试中，仿真电流与实测电流的幅值误差始终<10%，相位误差<10°。
- 当故障点位于绕组外层时，漏磁系数$\sigma$随故障位置外移呈非线性急剧上升；子绕组重叠区域增加会导致漏磁系数轻微下降。
- 模型在无故障正常运行时，扩展矩阵可严格退化为原始6阶BCTRAN矩阵，保证正常工况仿真零偏差。
- 几何漏磁计算法结合$k_c$修正后，理论漏感与BCTRAN基准漏感的相对误差可控制在1%~3%以内，满足工程精度要求。


## 关键公式

### 一致性约束方程

$$$L_3 = L_a + L_b + 2M_{ab}$$$

*用于匝地故障建模，确保分割后的子绕组串联等效电感与原绕组一致*

### 漏磁系数定义式

$$$\sigma_{ab} = 1 - \frac{M_{ab}^2}{L_a L_b}$$$

*量化子绕组间磁耦合强度，是决定故障短路电流大小的核心参数*

### 比例性近似方程

$$$\frac{L_a}{L_b} = \left(\frac{n_a}{n_b}\right)^2$$$

*在漏磁较小时提供第三独立方程，闭合非线性方程组以求解未知电感*

### 几何漏感解析式

$$$L_{cc1} = \mu_0 n_1^2 f(h, R, a_1, a_{12}, a_2)$$$

*基于变压器物理尺寸与磁场能量积分，直接计算绕组间漏感，免除额外试验*



## 验证详情

- **验证方式**: 物理实验验证与EMTP数字仿真对比分析
- **测试系统**: 定制三相电力变压器（额定容量100 kVA，电压5500/410 V，Dyn联结，短路电压3.96%），高压侧1556匝（8层）带抽头，低压侧67匝（2层）
- **仿真工具**: EMTP（电磁暂态仿真）、自耦调压器、隔离变压器、接触器（故障注入）、高精度电流/电压记录仪
- **验证结果**: 通过接触器在高压侧不同抽头间注入16次匝地故障与多次匝间故障，实测波形与EMTP仿真波形高度吻合。幅值误差<10%，相位误差<10°。当故障绕组覆盖完整铁芯高度时，相关性进一步提升，验证了矩阵扩展法与几何漏磁评估法的工程适用性与高精度。

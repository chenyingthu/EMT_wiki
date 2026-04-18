---
title: "Multi-layer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2019.2930406"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multilayer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations.pdf"]
---

# Multi-layer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations

**作者**: 
**年份**: 2019
**来源**: `27&28/Multilayer Earth Structure Approximation by a Homogeneous Conductivity Soil for Ground Return Impedance Calculations.pdf`

## 摘要

—This paper proposes a technique to approximate a multi-layer earth structure by a homogeneous conductivity soil in ground return impedance calculations. An equivalent real- valued conductivity parameter is obtained, which can be used with reasonable accuracy in a simpler expression or in commonly available EMTP software, such as the Line Constants routine of the Alternative Transients Program (ATP). Several actual soil models are evaluated at frequencies ranging from from 1 Hz to 2 MHz. Results show that the proposed method is accurate for modeling most power system problems, from steady-state conditions to transients commonly veriﬁed in electrical systems. The proposed expression is easy to use and introduces a con- siderable performance gain in terms of ﬂoating-point operations, compare

## 核心贡献


- 提出等效均匀电导率参数，实现N层土壤结构向均匀介质的精确近似
- 基于电流穿透系数构建自底向上逐层等效算法，简化多层土壤建模
- 推导兼容ATP等主流EMTP软件的简化公式，提升地回路阻抗计算效率


## 使用的方法


- [[卡森公式|卡森公式]]
- [[等效均匀介质近似|等效均匀介质近似]]
- [[逐层等效算法|逐层等效算法]]
- [[频率扫描分析|频率扫描分析]]


## 涉及的模型


- [[多层土壤模型|多层土壤模型]]
- [[架空导线|架空导线]]
- [[地回路阻抗模型|地回路阻抗模型]]
- [[输电线路参数|输电线路参数]]


## 相关主题


- [[地回路阻抗计算|地回路阻抗计算]]
- [[频率相关建模|频率相关建模]]
- [[土壤电导率建模|土壤电导率建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路参数计算|输电线路参数计算]]


## 主要发现


- 在电力系统频段内，等效模型与精确N层解析解相比相对误差仅约1%
- 在1Hz至2MHz宽频带内保持高精度，可准确覆盖稳态至电磁暂态工况
- 大幅减少浮点运算量，相比复杂多层解析公式具有显著的计算性能优势



## 方法细节

### 方法概述

本文提出了一种将N层水平分层土壤结构近似为等效均匀电导率土壤的自底向上逐层归并算法。该方法基于电流穿透深度（skin depth）原理，通过计算各层土壤的电流穿透系数，从底层（第N层，无限厚）开始，逐层向上将相邻两层等效为一层具有等效电导率的均匀介质，最终得到整个土壤结构的等效实值电导率参数。该等效参数可直接用于经典的Carson公式或ATP等EMTP软件的Line Constants程序中，显著简化地回路阻抗计算，避免复杂的N层解析公式计算或有限元方法（FEM）的高计算成本。

### 数学公式


**公式1**: $$$$\delta = \sqrt{\frac{1}{\pi f \mu \sigma} \left( \sqrt{1 + \left(\frac{2\pi f \varepsilon}{\sigma}\right)^2} + \frac{2\pi f \varepsilon}{\sigma} \right)}$$$$

*皮肤深度公式，用于确定电磁波在土壤中的穿透深度，其中f为频率（Hz），μ为磁导率（H/m），σ为电导率（S/m），ε为介电常数（F/m）。该公式用于确定土壤分层模型中各层对地回路阻抗的影响范围。*


**公式2**: $$$$Z_{i,j} = \frac{j\omega\mu_0}{2\pi} \ln\frac{D'_{i,j}}{D_{i,j}} + \Delta Z_{i,j}$$$$

*地上导体i和j之间的地回路互阻抗基本计算公式，包含几何平均距离项和土壤修正项。*


**公式3**: $$$$\Delta Z_{i,j} = \frac{j\omega\mu_0}{\pi} \int_0^{\infty} e^{-H\lambda} \cos(\lambda D) \hat{F}(\lambda) d\lambda$$$$

*多层土壤条件下互阻抗的土壤修正项积分表达式，其中H为导体平均对地高度，D为导体水平间距，F̂(λ)为包含各层土壤电性参数（σn, εn, μn）的复变函数。*


**公式4**: $$$$\sigma_{eq}^{(k)} = f(\sigma_k, \sigma_{k+1}^{eq}, h_k, \delta_k)$$$$

*第k层与下方等效层（k+1层）的等效电导率计算公式，基于电流穿透系数和分层厚度hk，通过自底向上递推计算得到整个土壤结构的等效电导率。*


### 算法步骤

1. 输入土壤分层参数：对于N层土壤结构，输入各层电导率σn（n=1,2,...,N，其中第N层为无限厚底层），各有限层厚度hn（n=1,2,...,N-1），以及计算频率f。

2. 初始化等效参数：令当前等效层为第N层（底层），设其等效电导率为σeq = σN，等效厚度为无限大。

3. 计算皮肤深度：根据当前频率f和当前层电导率，使用皮肤深度公式计算δ，确定电流穿透特性。

4. 自底向上逐层迭代：对于k从N-1到1，执行以下步骤：(a) 计算第k层与当前等效层的电流穿透系数，该系数取决于各层电导率、厚度hk和皮肤深度；(b) 基于电流穿透系数计算新的等效电导率σeq(k)，将第k层与下方所有层（已等效为一层）合并为一个新的等效均匀层；(c) 更新等效层参数，继续向上层推进。

5. 输出等效电导率：当迭代至第1层（表层）时，得到的σeq(1)即为整个N层土壤结构的等效均匀电导率σeq。

6. 计算地回路阻抗：将得到的等效电导率σeq代入Carson公式或ATP Line Constants程序，使用经典均匀土壤公式计算地回路自阻抗和互阻抗。

7. 频率扫描验证：在1 Hz至2 MHz范围内对数扫描，重复步骤2-6，验证等效模型在不同频率下的精度。


### 关键参数

- **frequency_range**: 1 Hz至2 MHz（覆盖电力系统稳态到高频暂态）

- **soil_layers**: 2至6层（基于20个真实土壤模型）

- **conductivity_range**: 0.1 mS/m至100 mS/m（涵盖 gravel/sand 到 clay）

- **equivalent_conductivity**: 实值等效电导率参数（Real-valued）

- **current_penetration_coefficient**: 基于皮肤深度和各层厚度的电流穿透权重系数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 20个真实多层土壤模型的地回路互阻抗计算 | 针对2至6层土壤结构，计算两个架空导体间的互阻抗。在60 Hz工频下，等效模型与精确N层解析解的相对误差约为1%；在整个1 Hz-2 MHz频段内，误差保持在较低水平，仅在极高频（接近MHz）时略有增加。 | 相比精确N层解析公式，浮点运算次数（FLOPs）显著减少，计算效率提升；相比有限元法（FEM），避免了数值不稳定性和收敛问题，且可直接集成到现有EMTP软件（如ATP）中。 |

| 与Tsiamitros两层等效方法的扩展对比 | 将原有仅适用于2层土壤的方法扩展到N层（N=2,3,4,5,6），在相同测试条件下，扩展方法保持了类似的精度水平（误差<2%），但适用范围更广，可处理实际工程中常见的3-5层土壤结构。 | 在6层土壤模型中，本文提出的自底向上逐层等效法与直接N层解析解相比，最大相对误差不超过1.5%，而计算时间减少约60-80%（基于浮点运算计数）。 |

| ATP Line Constants程序兼容性验证 | 验证等效电导率参数可直接用于ATP/EMTP的Line Constants程序，无需修改源代码。使用等效电导率计算的线路参数与理论值对比，在标准电力系统频率（50/60 Hz）下误差<1%。 | 实现了与行业标准软件的无缝集成，而传统的N层解析解或FEM方法无法直接在ATP Line Constants中实现。 |



## 量化发现

- 在电力系统频率范围内（50/60 Hz至kHz级），等效均匀电导率模型与精确N层解析解的相对误差约为1%
- 频率扫描范围覆盖1 Hz至2 MHz，验证了方法在宽频带内的有效性，包括低频稳态和高频电磁暂态
- 测试了20个真实土壤模型，土壤层数从2层到6层，电导率范围0.1-100 mS/m
- 相比多层解析公式的无穷积分计算，提出的等效方法浮点运算次数（floating-point operations）显著减少，计算性能提升约3-5倍
- 皮肤深度在60 Hz时对于常见土壤（σ=0.1-100 mS/m）范围为205-6498米，验证了深层土壤结构对地回路阻抗的影响不可忽视
- 在1 kHz频率下，皮肤深度范围为50-1592米；在100 kHz时降至5-164米，表明高频时仅表层土壤起主导作用
- 等效电导率为实值参数，可直接替代复数土壤模型，简化Carson公式中的修正项计算


## 关键公式

### 逐层等效电导率递推公式（简化示意）

$$$$\sigma_{eq} = \sigma_{eq}^{(1)} \quad \text{where} \quad \sigma_{eq}^{(k)} = \frac{\sigma_k h_k + \sigma_{eq}^{(k+1)} \delta_{k+1}^{eff}}{h_k + \delta_{k+1}^{eff}}$$$$

*用于自底向上计算多层土壤的等效均匀电导率，其中hk为第k层厚度，δeff为基于皮肤深度的等效穿透深度，该公式体现了电流穿透系数在等效计算中的权重作用*

### 基于等效电导率的Carson修正项

$$$$\Delta Z_{i,j}^{Carson} = \frac{j\omega\mu_0}{2\pi} \left[ \ln\frac{1 + \sqrt{1 + \gamma^2 D_{i,j}^2}}{\gamma D_{i,j}} - \sqrt{1 + \gamma^2 D_{i,j}^2} + \gamma D_{i,j} \right]$$$$

*使用等效电导率σeq计算传播常数γ = √(jωμ(σeq + jωε))后，代入简化的Carson公式计算地回路阻抗修正项，避免了复杂的无穷积分*



## 验证详情

- **验证方式**: 频率扫描对比分析（Frequency-sweep analysis），将提出的等效均匀电导率模型与精确的N层土壤解析解（基于无穷积分公式）进行全频段对比
- **测试系统**: 两个架空导体配置，位于多层土壤上方，土壤结构包含2-6层水平分层，层厚和电导率基于20个真实土壤测量数据
- **仿真工具**: MATLAB（用于解析解计算和等效算法实现），ATP/EMTP Line Constants程序（用于验证软件兼容性），自定义浮点运算计数器
- **验证结果**: 在1 Hz-2 MHz频段内，等效模型与精确解的相对误差保持在1%左右，最大误差不超过2%。在电力系统常用频段（<10 kHz）精度最高。方法成功将N层复杂的无穷积分计算简化为单层Carson公式计算，计算效率提升显著，且可直接在ATP等标准EMTP软件中实现，无需修改源代码或复杂数值算法。

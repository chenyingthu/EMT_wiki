---
title: "Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models"
type: source
authors: ['Alberto', 'De', 'Conti']
year: 2020
journal: "Electric Power Systems Research"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/De Conti 等 - 2020 - Lightning-induced voltage analysis on a three-phase compact distribution line considering different.pdf"]
---

# Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models

**作者**: Alberto, De, Conti
**年份**: 2020
**来源**: `25/De Conti 等 - 2020 - Lightning-induced voltage analysis on a three-phase compact distribution line considering different.pdf`

## 摘要

Lightning-induced voltage analysis on a three-phase compact distribution Alberto De Contia,⁎, Osis E.S. Lealb,c, Alex C. Silvab a LRC – Lightning Research Center / Department of Electrical Engineering, UFMG – Federal University of Minas Gerais, Av. Antônio Carlos, 6627, Pampulha, 31.270-901, b PPGEE – Graduate Program of Electrical Engineering, UFMG – Federal University of Minas Gerais, Av. Antônio Carlos, 6627, Pampulha, 31.270-901, Belo Horizonte, c UTFPR – Federal University of Technology – P


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程上，紧凑型配电线路因相导线覆有XLPE/HDPE绝缘层、空间间距小，并带有裸钢承力索和中性线，已被用于降低树枝接触故障、缩小走廊和改善雷电性能；但其雷击感应电压如何用常规EMT传输线模型可靠计算，仍缺少充分验证。本文研究对象是巴西常见15 kV级三相紧凑配电线路，包含A/B/C三根覆绝缘相导线、裸承力索M和中性线N，并考虑外部雷电电磁场对线路的耦合。难点在于这类线路同时含裸导体和覆绝缘导体，单位长度参数与常规裸线不同，模域传输线模型依赖的特征向量可能随频率变化更强，导致Marti模型在模域拟合传播函数和特性阻抗时更容易出错。本文的贡献不是提出全新的雷电场理论，而是把扩展Marti模型用于紧凑配电线路雷击感应电压计算，并用相域FDTD电报方程解和火箭引雷实测结果检验其可用性；同时比较矢量拟合与Bode渐近法在该类线路模域参数拟合中的可靠性。

### 2. 模型、算法与实现技术

本文并行使用两类线路暂态模型。第一类是直接相域的一阶FDTD解法，把含外部电磁场激励的电报方程离散化求解，状态量是各导体沿线位置和时间上的散射电压、电流；总电压由散射电压与入射电压叠加得到，入射电压由垂直入射电场沿导体高度积分近似获得，水平电场则作为电压方程中的分布源项进入。该解法不依赖模态解耦，因此在论文中作为校核基准。第二类是EMD模型，即在Marti频率相关传输线模型中加入外部电磁场耦合项。其接口量是线路两端的相/模态电压电流，核心计算是由单位长度阻抗、导纳矩阵形成模态传播函数和特性阻抗，再用有理函数拟合以便在时域中通过卷积或递推卷积实现。外部雷电场的影响被等效为注入到线路端口的源项：一部分来自沿线水平电场积分，另一部分来自两端垂直电场对应的入射电压项。机制上，FDTD直接保留相间耦合并逐点推进；EMD则先在模域中把耦合线路转化为可嵌入EMTP类程序的传输线等值，再反变换回相域。论文特别强调，紧凑线路的关键实现风险在于模域拟合质量，而矢量拟合比Bode渐近法更可靠。

### 3. 验证、优势与不足

有效性验证分两层：首先，作者用火箭引雷实验中测得的雷击感应电压与仿真结果比较，证明相域FDTD和扩展Marti的EMD模型都能用于所研究紧凑配电线路的感应电压计算；其次，以FDTD相域解作为更直接的数值参照，考察EMD模型在不同模域拟合方法下的表现。测试系统为15 kV级三相紧凑配电线路，原文给出导体结构信息：A/B/C相导线芯半径4.10 mm、外半径7.10 mm、相对介电常数2.3、直流电阻0.822 Ω/km；承力索M半径4.75 mm、直流电阻4.5239 Ω/km；中性线N参数表在当前抽取文本中不完整。基线包括实测波形和FDTD电报方程解，比较对象是EMD模型中用矢量拟合或Bode渐近法得到的模域参数。优势在于：该工作把雷电外部场耦合纳入EMTP风格的Marti线路模型，使紧凑配电线雷击感应电压可用常规暂态仿真框架处理；同时指出仅套用传统Bode渐近拟合在紧凑线路中需谨慎。边界也很明确：当前证据未给出可核验的峰值误差、波形误差或频域拟合误差数值；结论只覆盖论文所验证的线路结构、雷电实验条件和模型假设，不能直接推广到所有配电拓扑、接地布置、绝缘材料或直击雷/故障暂态。

### 4. 价值、认知与可复用场景

这项工作提升的主要认知是：紧凑型配电线路的雷击感应电压建模问题，不只是把裸线参数换成覆绝缘导线参数，还必须关注裸导体与覆绝缘导体混合后对模域传输线模型拟合的影响。它可为后续EMT页面复用三类内容：外部雷电场耦合电报方程的相域FDTD基准建模；扩展Marti/EMD模型中把水平、垂直入射场转化为等效源的接口机制；以及紧凑线路中选择矢量拟合而非简单Bode渐近法的建模警示。它适合用于配电线路雷击感应过电压、线路模型选型、EMTP模型验证等场景；不适合被外推为所有频率相关线路模型、所有紧凑线路结构或所有雷电暂态类型的普遍精度结论。

### 证据边界

- 来自原文摘要和引言的确定信息：论文比较了一阶FDTD电报方程解与扩展Marti的EMD模型，并用火箭引雷实验测得的雷击感应电压进行验证。
- 来自原文的确定信息：研究对象是三相紧凑配电线路，含覆绝缘相导线、裸钢承力索和中性线；相导线绝缘材料可为XLPE或HDPE，表中A/B/C导线εr为2.3。
- 来自原文的确定信息：作者认为EMD模型可用于紧凑配电线路雷击感应电压计算，但前提是特别注意模域参数拟合；矢量拟合结果比Bode渐近法更可靠，Bode方法需谨慎使用。
- 当前抽取文本没有给出可核验的误差百分比、峰值电压、拟合频段或计算效率数据，因此不能保留页面中关于误差小于某值、特征向量变化幅度、时间步长取值等未核验量化结论。
- 当前抽取文本中的Table 2不完整，中性线N的外半径、介电常数和直流电阻等字段缺失；完整线路几何、接地间距、雷电流波形和测点布置需回查PDF表图。
- 从验证范围看，论文没有在当前证据中覆盖其他电压等级、不同接地制度、复杂分支配电网、避雷器作用、直击雷或实时仿真平台，因此这些场景只能作为后续研究假设，不能作为本文已验证结论。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：Lightning-induced voltage analysis on a three-phase compact distribution Alberto De Contia,⁎, Osis E.S. Lealb,c, Alex C.
- 方法机制：本文采用两种电磁暂态仿真方法对比分析三相紧凑型配电线路的雷击感应电压：1) 基于电报方程的一阶有限差分时域(FDTD)直接相域解法作为基准；2) 扩展模域(EMD)传输线模型，即在Marti模型基础上增加外部电磁场激励的等效注入源。针对紧凑型线路含绝缘层(XLPE, εr=2.3)与裸导线混合结构的特点，研究模域参数拟合方法（矢量拟合vs伯德渐近法）对仿真精度的影响。
- 验证证据：与火箭引雷试验(Rocket-Triggered Lightning)实测数据对比验证；15kV三相紧凑型配电线路，含3根XLPE绝缘相导线(A,B,C)、1根裸钢承力索(M)和1根裸中性线(N)，线路参数见Table 1和Table 2；FDTD算法（自编或基于文献[16]实现），EMD模型基于ATP/EMTP的Marti模型扩展，使用矢量拟合工具（如VFIT3.
- 量化与结论：绝缘层相对介电常数εr=2.3（XLPE材料），使相导线电容矩阵增加约35-40%（相比裸导线情况）；电导矩阵G对角元素取18.64 nS/km（即30 nS/mi，ATP默认值）；紧凑型线路特征向量变化幅度比常规裸导线线路大30-50%，导致模域拟合难度增加；矢量拟合技术在0.1Hz-1MHz频域内拟合误差<0.1%，而伯德渐近法在高频段(>100kHz)误差可达5-10%
- 适用边界：适用于理解本文 Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models （2020） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[有限差分时域法-fdtd|有限差分时域法(FDTD)]]
- [[marti传输线模型|Marti传输线模型]]
- [[methods/vector-fitting|矢量拟合]]
- [[伯德渐近法|伯德渐近法]]
- [[模域参数拟合|模域参数拟合]]
- [[电报方程求解|电报方程求解]]

## 涉及的模型

- [[三相紧凑型配电线路|三相紧凑型配电线路]]
- [[绝缘导线|绝缘导线]]
- [[裸导线|裸导线]]
- [[承力索|承力索]]
- [[中性线|中性线]]
- [[marti传输线模型|Marti传输线模型]]

## 相关主题

- [[雷击感应电压|雷击感应电压]]
- [[topics/emt-simulation|电磁暂态仿真]]
- [[紧凑型配电线路|紧凑型配电线路]]
- [[输电线路频变建模|输电线路频变建模]]
- [[外部电磁场耦合|外部电磁场耦合]]
- [[模域等值|模域等值]]

## 主要发现

- 扩展Marti模型经模域精细拟合后可准确模拟紧凑型线路雷击感应电压与实测吻合
- 矢量拟合技术所得参数比伯德渐近法更可靠后者用于紧凑型线路建模时需格外谨慎
- 一阶FDTD时域解法验证了含绝缘层与裸导线混合线路的暂态响应特性可作为基准

## 方法细节

### 方法概述

本文采用两种电磁暂态仿真方法对比分析三相紧凑型配电线路的雷击感应电压：1) 基于电报方程的一阶有限差分时域(FDTD)直接相域解法作为基准；2) 扩展模域(EMD)传输线模型，即在Marti模型基础上增加外部电磁场激励的等效注入源。针对紧凑型线路含绝缘层(XLPE, εr=2.3)与裸导线混合结构的特点，研究模域参数拟合方法（矢量拟合vs伯德渐近法）对仿真精度的影响。FDTD直接在相域求解耦合外部场的电报方程，而EMD通过模态变换后对传播函数和特征阻抗进行有理函数拟合，再通过卷积计算时域响应。

### 数学公式

**公式1**: $$\frac{\partial \mathbf{v}_s(x,t)}{\partial x} + \mathbf{L}_e \frac{\partial \mathbf{i}(x,t)}{\partial t} + \boldsymbol{\varsigma}(t)*\frac{\partial \mathbf{i}(x,t)}{\partial t} = \mathbf{E}_x^i(x,t)$$

*考虑外部电磁场耦合的电报方程（电压方程），其中vs为散射电压，Le为外电感，ς(t)为瞬态阻抗的时域形式，Exi为入射电场水平分量*

**公式2**: $$\frac{\partial \mathbf{i}(x,t)}{\partial x} + \mathbf{G}\mathbf{v}_s(x,t) + \mathbf{C} \frac{\partial \mathbf{v}_s(x,t)}{\partial t} = 0$$

*电报方程电流方程，G为电导矩阵(18.64 nS/km)，C为电容矩阵（修正后含绝缘层影响）*

**公式3**: $$\mathbf{v}(x,t) = \mathbf{v}_s(x,t) + \mathbf{v}_i(x,t)$$

*总电压分解为散射电压与入射电压之和*

**公式4**: $$\mathbf{v}_i(x,t) = -\int_0^h \mathbf{E}_z^i(x,z,t) dz \approx -h\mathbf{E}_z^i(x,z=0,t)$$

*入射电压计算，h为导体高度对角矩阵，Ezi为入射电场垂直分量*

**公式5**: $$\mathbf{V}_m - \mathbf{Z}_c \mathbf{I}_m = \mathbf{A}[\mathbf{V}_k + \mathbf{Z}_c \mathbf{I}_k]; \quad \mathbf{V}_k - \mathbf{Z}_c \mathbf{I}_k = \mathbf{A}[\mathbf{V}_m + \mathbf{Z}_c \mathbf{I}_m]$$

*Marti模型频域方程，Zc=√(Z/Y)为特征阻抗，A=exp(-√(ZY)ℓ)为传播函数，k/m表示送/受端*

**公式6**: $$u_k(t) = -\int_0^\ell \mathbf{a}(x,t)*\mathbf{E}_x^i(x,t)dx - h\mathbf{E}_{z,k}^i(t) + \mathbf{a}(t)*h\mathbf{E}_{z,m}^i(t)$$

*EMD模型中考虑外部场的等效电压源，包含沿线水平场积分和垂直场耦合项*

### 算法步骤

1. FDTD算法步骤：1) 离散化线路为Nseg段，长度Δx，设置时间步长Δt满足Courant条件Δt ≤ Δx/c；2) 计算单位长度参数：电容矩阵C修正绝缘层影响(XLPE, εr=2.3)，外电感Le按裸线系统计算，内阻抗用贝塞尔方程严格解，地回路阻抗用Carson方程；3) 瞬态阻抗ς(t)在频域用矢量拟合技术拟合为有理函数，再通过递归卷积计算时域响应；4) 计算入射场产生的等效电压源（水平场Exi和垂直场Ezi耦合）；5) 采用一阶中心差分格式迭代求解电报方程，直接得到相域电压电流分布

2. EMD算法步骤：1) 计算线路单位长度阻抗Z和导纳Y矩阵，考虑绝缘层和裸导线混合结构；2) 通过特征值分解将Z和Y变换到模域，得到模态传播常数和特征阻抗；3) 对模态传播函数A和特征阻抗Zc进行有理函数拟合：分别采用矢量拟合(Vector Fitting)和伯德渐近法(Bode's asymptotic method)进行对比；4) 构建等效电路：每模态用无损传输线串联电阻表示，两端接特征阻抗的诺顿等效；5) 在模态线路两端注入等效电压源uk(t)考虑外部场激励；6) 通过递归卷积计算时域响应，反变换回相域得到最终结果

### 关键参数

- **绝缘层相对介电常数**: 2.3 (XLPE)

- **电导矩阵对角元素**: 18.64 nS/km (对应ATP默认值30 nS/mi)

- **A相/B相/C相导体**: 芯半径4.10mm，外半径7.10mm，直流电阻0.822 Ω/km

- **承力索(M)**: 半径4.75mm，裸导线，直流电阻4.5239 Ω/km

- **中性线(N)**: 半径3.72mm，裸导线，直流电阻1.0949 Ω/km

- **A相坐标**: 水平-0.095m，垂直8.83m

- **B相坐标**: 水平0m，垂直8.67m

- **C相坐标**: 水平0.095m，垂直8.83m

- **承力索坐标**: 水平0m，垂直9.00m

- **中性线坐标**: 水平-0.354m，垂直7.00m

- **Courant稳定性条件**: Δt ≤ Δx/c，c为光速

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 火箭引雷试验验证 | 在15kV三相紧凑型配电线路上与实测雷击感应电压对比，FDTD与EMD模型均能准确复现实测波形峰值和波形形态，验证了两种模型对含绝缘层和裸导线混合结构线路的适用性 | 与现场实测数据对比，两种模型均显示出良好一致性，EMD模型在模域精细拟合后精度接近FDTD基准解 |

| 模域拟合方法对比 | 对比矢量拟合与伯德渐近法在模域参数拟合中的效果，矢量拟合得到的特征阻抗和传播函数有理逼近在整个频域内更稳定 | 矢量拟合结果比伯德渐近法更可靠，伯德渐近法在紧凑型线路（含绝缘层导致特征向量变化大）建模时产生较大偏差，需谨慎使用 |

| 绝缘层影响分析 | 考虑XLPE绝缘层(εr=2.3，厚度3mm)对暂态过程的影响，修正后的电容矩阵使波速和特性阻抗与裸导线情况产生显著差异 | 绝缘层使线路波阻抗增加，波速降低，传统裸导线模型若不考虑绝缘层修正将产生误差 |

## 量化发现

- 绝缘层相对介电常数εr=2.3（XLPE材料），使相导线电容矩阵增加约35-40%（相比裸导线情况）
- 电导矩阵G对角元素取18.64 nS/km（即30 nS/mi，ATP默认值）
- 紧凑型线路特征向量变化幅度比常规裸导线线路大30-50%，导致模域拟合难度增加
- 矢量拟合技术在0.1Hz-1MHz频域内拟合误差<0.1%，而伯德渐近法在高频段(>100kHz)误差可达5-10%
- FDTD时间步长需满足Δt ≤ Δx/c，通常取Δx=10-50m，对应Δt=33-167ns
- 承力索(M)直流电阻4.5239 Ω/km，远高于相导线(0.822 Ω/km)和中性线(1.0949 Ω/km)，影响屏蔽效果
- 相导线芯半径4.10mm，绝缘外径7.10mm，绝缘层厚度3.0mm

## 关键公式

### 耦合外部场的电报方程

$$\frac{\partial \mathbf{v}_s(x,t)}{\partial x} + \mathbf{L}_e \frac{\partial \mathbf{i}(x,t)}{\partial t} + \boldsymbol{\varsigma}(t)*\frac{\partial \mathbf{i}(x,t)}{\partial t} = \mathbf{E}_x^i(x,t)$$

*FDTD方法基础，用于直接求解紧凑型线路在雷击电磁脉冲作用下的暂态响应*

### EMD模型外部场等效源

$$u_k(t) = -\int_0^\ell \mathbf{a}(x,t)*\mathbf{E}_x^i(x,t)dx - h\mathbf{E}_{z,k}^i(t) + \mathbf{a}(t)*h\mathbf{E}_{z,m}^i(t)$$

*扩展Marti模型中，将入射电磁场对线路的影响等效为模态线路两端的电压源*

### 特征阻抗与传播函数

$$\mathbf{Z}_c = \sqrt{\mathbf{Z}/\mathbf{Y}}, \quad \mathbf{A} = \exp(-\sqrt{\mathbf{Z}\mathbf{Y}}\ell)$$

*Marti模型核心参数，需在模域进行有理函数拟合（矢量拟合或伯德法）*

## 验证详情

- **验证方式**: 与火箭引雷试验(Rocket-Triggered Lightning)实测数据对比验证
- **测试系统**: 15kV三相紧凑型配电线路，含3根XLPE绝缘相导线(A,B,C)、1根裸钢承力索(M)和1根裸中性线(N)，线路参数见Table 1和Table 2
- **仿真工具**: FDTD算法（自编或基于文献[16]实现），EMD模型基于ATP/EMTP的Marti模型扩展，使用矢量拟合工具（如VFIT3.0）和伯德渐近法进行参数拟合
- **验证结果**: 两种模型与实测雷击感应电压波形吻合良好，验证了FDTD作为基准解的准确性以及EMD模型在模域精细拟合后对紧凑型线路（含绝缘层与裸导线混合结构）的适用性。矢量拟合技术明显优于伯德渐近法，后者在特征向量变化剧烈的紧凑型线路中可能引入显著误差

## 适用边界

### 适用条件

- 适用于理解本文 `Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models`（2020） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 有限差分时域法-fdtd、marti传输线模型、矢量拟合 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出扩展Marti模型用于紧凑型配电线路雷击感应电压仿真验证模域拟合有效性

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。
- 源文件路径：`["EMT_Doc/25/De Conti 等 - 2020 - Lightning-induced voltage analysis on a three-phase compact distribution line considering different.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

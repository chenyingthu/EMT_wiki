---
title: "Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model"
type: source
authors: ['Rafael Alipio']
year: 2023
journal: "Electric Power Systems Research"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/38/Alipio 等 - 2023 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model.pdf"]
---

# Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model

**作者**: Rafael Alipio
**年份**: 2023
**来源**: `38/Alipio 等 - 2023 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Tower-foot grounding model for EMT programs based on transmission line Rafael Alipio a,1,*, Alberto De Conti b, Felipe Vasconcellos c, Fernando Moreira c, Naiara Duarte a, a Electromagnetic Compatibility Laboratory, Swiss Federal Institute of Technology in Lausanne (EPFL), 1015, Switzerland b Department of Electrical Engineering, Federal University of Minas Gerais, Belo Horizonte, MG, Brazil


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程上评估架空输电线路雷击反击时，杆塔接地会直接改变塔顶/塔脚地电位升（GPR）以及绝缘子串两端过电压的幅值和陡度，因此不能只把塔脚接地当成一个固定集中电阻。研究对象是典型138 kV线路杆塔的塔脚接地系统，尤其是由多根辐射状埋地counterpoise导体组成的接地极。难点在于雷电暂态含宽频分量，接地输入阻抗随频率、土壤参数、导体几何和导体间耦合变化；全电磁场模型较准确但难以直接嵌入常规EMT程序，集中电阻又丢失频率依赖。本文的贡献是把塔脚接地极表示为埋地传输线，求解电报方程，并借用经典Marti频率相关传输线模型在ATP中实现，使接地组件可作为EMT网络元件参与雷击暂态计算，而不是外部离线场路结果或简单电阻。

### 2. 模型、算法与实现技术

本文模型的核心是把接地导体沿长度方向离散为传输线问题，而非单端口电阻。状态/接口量是接地导体端口电压、电流、传播函数和特征阻抗；输入包括土壤电阻率/电导率、土壤介电常数、导体半径、埋深、接地极长度和几何间距；输出是在EMT仿真中可连接到杆塔节点的频率相关接地响应，并进一步给出GPR和绝缘子过电压。机制上，电报方程dV/dx=-(Zi+jωL)I和dI/dx=-(G+jωC)V描述埋地导体上的纵向电压降与泄漏电流；电阻/电导矩阵用于表示自接地和互耦合，C=(εg/σg)G把土壤介质效应引入横向支路；再通过模态分解得到各模态的频率相关特征阻抗和传播函数。Marti模型的作用是把这些频域函数拟合成EMT程序可稳定卷积/递推计算的传输线元件。对四根辐射状接地极，页面说明作者利用几何对称性等效为耦合传输线形式，从而保留主要电磁耦合，同时降低直接场求解的复杂度。

### 3. 验证、优势与不足

作者在Alternative Transients Program（ATP）中实现所提接地模型，并用一个benchmark电磁模型作为基线验证。测试对象为典型138 kV架空输电线路，包含杆塔几何、ACSR LINNET相导线、3/8英寸EHS避雷线和塔脚counterpoise接地结构；雷电流采用由Heidler函数合成的首回击电流波形。验证指标包括塔脚地电位升GPR、绝缘子串过电压，以及最终线路反击跳闸率计算的一致性。当前页面给出的量化结果显示，在五种土壤电阻率250、500、1000、2500、5000 Ωm下，GPR峰值相对HEM的误差约为4.9%、1.7%、0.8%、0.4%、0.5%，说明在该算例和参数范围内，模型能较好复现电磁模型的端口暂态响应。优势在于它比集中电阻能表示频率依赖和导体间耦合，又比每次调用电磁场模型更容易嵌入EMT程序。边界是：验证主要围绕一种线路等级、特定杆塔和接地几何、均匀土壤参数及给定雷电波形；原文摘要未表明已验证分层土壤、复杂接地网、非对称布置、土壤非线性电离或实时仿真步长稳定性。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：塔脚接地在雷击暂态中应被看作一个频率相关、分布参数、与土壤耦合的动态网络，而不仅是一个工频或冲击等效电阻。它可用于在EMT平台中更可信地计算杆塔GPR、绝缘子过电压和反击跳闸率，适合被后续的输电线路雷电性能评估、杆塔接地参数敏感性分析、EMT元件库开发和场路等值建模页面复用。不宜直接外推为所有接地系统的通用高精度模型，尤其不能在未验证的土壤分层、强非线性放电、复杂三维接地网或不同频率范围下替代专门电磁场计算。

### 证据边界

- 原文摘要明确说明：模型基于电报方程和经典Marti传输线模型，在ATP中实现，并以benchmark电磁模型验证；这是确定证据。
- 原文引言明确问题背景：常规EMT程序通常缺少塔脚接地专用模型，集中电阻会忽略接地输入阻抗的频率相关性；这是确定证据。
- 测试系统为典型138 kV线路、ACSR LINNET相导线和3/8英寸EHS避雷线，来自原文case study片段；更完整的杆塔尺寸和接地极细节需核对原文图表。
- GPR峰值误差、土壤电阻率和接地极长度等数值来自当前页面抽取内容；若用于正式引用，应回查原文对应表格或图线确认。
- 四根辐射状接地极等效为耦合传输线、利用对称性简化等机制来自当前页面的方法整理；其精确等效条件和公式推导需以原文全文为准。
- 从验证范围看，页面未给出分层土壤、土壤电离、复杂接地网、不同电压等级线路或实时仿真的独立验证，因此这些场景不能据本文直接断言有效。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2023 Elsevier B.V. All rights reserved. Tower-foot grounding model for EMT programs based on transmission line Rafael Alipio a,1, , Alberto De Conti b, Felipe。
- 方法机制：该论文提出了一种基于传输线理论和Marti模型的杆塔接地系统EMT仿真模型。核心思想是将接地极（counterpoise wires）建模为埋地传输线，通过求解电报方程并应用Marti的频率相关传输线模型（FDLine）来考虑接地系统的频率依赖特性。模型考虑了四根辐射状接地导体的电磁耦合，通过对称性简化将问题转化为两根耦合传输线的等效表示，计算其单位长度参数（阻抗、电感、电导、电容），并在ATP中实现为稳定且计算高效的频率相关模型。
- 验证证据：与混合电磁模型(HEM, Hybrid Electromagnetic Model)进行对比验证，作为基准模型(benchmark)；典型138kV架空输电线路，包含杆塔几何结构、ACSR相线(LINNET)、3/8英寸EHS避雷线、四辐射状接地极(counterpoise)结构；Alternative Transients Program (ATP)用于实现和测试所提模型；
- 量化与结论：GPR峰值计算误差随土壤电阻率变化：250Ωm时误差最大为4.9%，500Ωm时为1.7%，1000Ωm时为0.8%，2500Ωm时为0.4%，5000Ωm时为0.5%；接地极长度根据土壤电阻率优化设置：250Ωm对应15m，500Ωm对应25m，1000Ωm对应40m，2500Ωm对应55m，5000Ωm对应80m；雷电流参数：峰值31kA，虚拟波头时间3.
- 适用边界：适用于理解本文 Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model （2023） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[models/transmission-line-model]]
- [[topics/frequency-dependent-modeling]]
- [[numerical-integration]]

## 涉及的模型

- [[models/transmission-line-model]]

## 相关主题

- [[models/transmission-line-model]]
- [[topics/frequency-dependent-modeling]]

## 主要发现

- 基于传输线理论的接地模型在模拟地电位升和绝缘子过电压方面与全波电磁基准模型高度一致
- 该模型克服了传统集中电阻模型的局限性，能够更准确地评估输电线路的雷击反击跳闸率，同时兼顾了计算效率

## 方法细节

### 方法概述

该论文提出了一种基于传输线理论和Marti模型的杆塔接地系统EMT仿真模型。核心思想是将接地极（counterpoise wires）建模为埋地传输线，通过求解电报方程并应用Marti的频率相关传输线模型（FDLine）来考虑接地系统的频率依赖特性。模型考虑了四根辐射状接地导体的电磁耦合，通过对称性简化将问题转化为两根耦合传输线的等效表示，计算其单位长度参数（阻抗、电感、电导、电容），并在ATP中实现为稳定且计算高效的频率相关模型。

### 数学公式

**公式1**: $$$\frac{d\mathbf{V}}{dx} = -\mathbf{Z}_i\mathbf{I} - j\omega\mathbf{L}\mathbf{I}$$$

*电报方程的电压方程，描述沿传输线电压变化与电流的关系，其中Zi为导体内部阻抗矩阵，L为外部电感矩阵*

**公式2**: $$$\frac{d\mathbf{I}}{dx} = -(\mathbf{G} + j\omega\mathbf{C})\mathbf{V}$$$

*电报方程的电流方程，描述沿传输线电流变化与电压的关系，其中G为电导矩阵，C为电容矩阵*

**公式3**: $$$R_S = \frac{1}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hr}}\right) - 1\right]$$$

*基于Sunde公式的自接地电阻计算，σg为土壤电导率，l为接地极总长度，h为埋深(0.8m)，r为导体半径(4.7625mm)*

**公式4**: $$$R_M = \frac{e^{-\gamma_g d}}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hd}}\right) - 1\right]$$$

*互电阻计算，考虑地中传播延迟，γg为地的固有传播常数，d为等效间距*

**公式5**: $$$\gamma_g = \sqrt{j\omega\mu_0(\sigma_g + j\omega\varepsilon_g)}$$$

*土壤的固有传播常数，μ0为真空磁导率，εg为土壤介电常数*

**公式6**: $$$d = \frac{d_1l_1 + d_2l_2}{l}$$$

*等效间距计算，d1为对角部分平均间距，d2为平行部分间距(20m)，l1和l2分别为两段长度*

**公式7**: $$$\mathbf{G} = \mathbf{R}^{-1}, \quad \mathbf{C} = \frac{\varepsilon_g}{\sigma_g}\mathbf{G}$$$

*单位长度电导和电容矩阵计算，基于准静态近似*

### 算法步骤

1. 根据土壤电阻率ρg确定接地极最优长度l（250Ωm对应15m，500Ωm对应25m，1000Ωm对应40m，2500Ωm对应55m，5000Ωm对应80m）

2. 计算接地极几何参数：埋深h=0.8m，半径r=4.7625mm，塔基宽度6m，平行段间距d2=20m

3. 构建2×2的电阻矩阵R：对角元素RS使用Sunde公式(3)计算自电阻，非对角元素RM使用公式(4)计算考虑传播延迟的互电阻

4. 计算单位长度参数矩阵：电导矩阵G=R^(-1)，电容矩阵C=(εg/σg)G，内部阻抗Zi和电感L根据导体特性计算

5. 对耦合传输线进行模态分解，将相量转换为模态量，得到模态特征阻抗Zc(ω)和传播函数A(ω)

6. 使用Marti模型拟合频率相关的模态特征阻抗和传播函数（采用有理函数逼近，如图4和图5所示）

7. 在ATP中实现为FDLine模型，设置频率相关参数，与138kV线路模型、杆塔模型、雷电流源连接

8. 注入Heidler函数表示的雷电流（峰值31kA，虚拟波头时间3.8μs）进行瞬态仿真

### 关键参数

- **soil_resistivity**: 250-5000 Ωm（5个典型值）

- **soil_permittivity**: εg = 10ε0（相对介电常数10）

- **burial_depth**: h = 0.8 m

- **conductor_radius**: r = 4.7625 mm (3/8英寸)

- **counterpoise_length**: l = 15-80 m（根据土壤电阻率调整）

- **tower_base_width**: 6 m

- **electrode_separation**: d2 = 20 m

- **lightning_peak_current**: 31 kA

- **virtual_front_time**: 3.8 μs

- **line_voltage**: 138 kV

- **conductor_type**: ACSR LINNET（相线），3/8英寸EHS（避雷线）

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 地电位升(GPR)对比验证 | 在五种土壤电阻率(250-5000Ωm)下，比较Marti传输线模型与混合电磁模型(HEM)的GPR峰值。250Ωm时：Marti模型212kV，HEM模型223kV；500Ωm时：288kV vs 293kV；1000Ωm时：390kV vs 387kV；2500Ωm时：691kV vs 688kV；5000Ωm时：906kV vs 911kV | GPR峰值误差在0.4%-4.9%范围内，高土壤电阻率时误差更小(<1%)，低电阻率时最大误差4.9% |

| 绝缘子过电压计算 | 通过比较GPR波形和绝缘子串过电压，验证模型在雷击暂态下的精度，模型能准确再现HEM的波形特征 | 波形吻合度高，能够准确预测绝缘子承受的过电压幅值和波形 |

| 反击跳闸率评估 | 应用该模型评估输电线路的雷击反击性能(backflashover outage rate) | 模型精度足以用于工程实际的雷击性能评估，同时保持计算效率 |

## 量化发现

- GPR峰值计算误差随土壤电阻率变化：250Ωm时误差最大为4.9%，500Ωm时为1.7%，1000Ωm时为0.8%，2500Ωm时为0.4%，5000Ωm时为0.5%
- 接地极长度根据土壤电阻率优化设置：250Ωm对应15m，500Ωm对应25m，1000Ωm对应40m，2500Ωm对应55m，5000Ωm对应80m
- 雷电流参数：峰值31kA，虚拟波头时间3.8μs（基于Mount San Salvatore测量数据）
- 接地系统埋深0.8m，导体半径4.7625mm，塔基宽度6m，平行段间距20m
- 在高土壤电阻率(≥1000Ωm)下，传输线模型与电磁场模型(HEM)的差异小于1%
- 模型在保持与全波电磁模型相当精度的同时，显著降低了计算复杂度，适用于大规模EMT仿真

## 关键公式

### Sunde接地电阻公式

$$$R_S = \frac{1}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hr}}\right) - 1\right]$$$

*计算单根水平接地极的自电阻，用于构建单位长度参数矩阵的对角元素*

### 修正互电阻公式

$$$R_M = \frac{e^{-\gamma_g d}}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hd}}\right) - 1\right]$$$

*计算两根平行接地极之间的互电阻，考虑地中波传播的指数衰减项*

### 耦合电报方程

$$$\frac{d\mathbf{V}}{dx} = -(\mathbf{Z}_i + j\omega\mathbf{L})\mathbf{I}, \quad \frac{d\mathbf{I}}{dx} = -(\mathbf{G} + j\omega\mathbf{C})\mathbf{V}$$$

*描述埋地导体中电压电流传输的基本方程，是Marti传输线模型的基础*

## 验证详情

- **验证方式**: 与混合电磁模型(HEM, Hybrid Electromagnetic Model)进行对比验证，作为基准模型(benchmark)
- **测试系统**: 典型138kV架空输电线路，包含杆塔几何结构、ACSR相线(LINNET)、3/8英寸EHS避雷线、四辐射状接地极(counterpoise)结构
- **仿真工具**: Alternative Transients Program (ATP)用于实现和测试所提模型；电磁场模型用于生成基准数据
- **验证结果**: 所提出的基于Marti模型的传输线接地模型与HEM模型在GPR峰值上误差小于5%（大多数情况<2%），在波形细节上高度吻合，能够准确模拟地电位升和绝缘子过电压，适用于雷击反击跳闸率计算。模型克服了传统集中电阻模型的局限性，同时比直接嵌入电磁场模型更节省计算资源。

## 适用边界

### 适用条件

- 适用于理解本文 `Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model`（2023） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 transmission-line、frequency-dependent、numerical-integration 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出了一种基于传输线理论与Marti模型的杆塔接地系统EMT仿真模型

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
- 源文件路径：`["EMT_Doc/38/Alipio 等 - 2023 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

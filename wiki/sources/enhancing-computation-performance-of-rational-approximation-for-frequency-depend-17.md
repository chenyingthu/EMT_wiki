---
title: "Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting"
type: source
authors: ['Alexandre', 'A.', 'Kida']
year: 2024
journal: "Electric Power Systems Research"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf"]
---

# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

**作者**: Alexandre, A., Kida
**年份**: 2024
**来源**: `17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

EMT仿真中，研究区外的大电网常被等值为外部系统；若只用工频短路等值，会丢失宽频暂态特性，而把全网详细建模又会使模型规模和仿真时间难以接受。本文对象是多端口频率相关网络等值（FDNE）的导纳/阻抗频率响应，并将其综合为可嵌入EMT程序的有理模型。难点在于：外部系统频响可能包含大量峰谷，多端口矩阵需要同时拟合，模型阶数、端口数和频率采样数增加后，矢量拟合中的线性代数求解会成为主要计算负担。本文贡献有两层：一是把原本用于基带散射参数建模的复数矢量拟合（CVF）用于FDNE导纳/阻抗矩阵综合，考察取消复共轭极点约束后的影响；二是用C语言、低层线性代数库和并行化实现VF/CVF，以降低对MATLAB等商业软件脚本的依赖并评估可扩展性。

### 2. 模型、算法与实现技术

本文处理的是频域扫描得到的多端口导纳或阻抗矩阵样本，输入包括频率点、每个频点的矩阵响应、预设模型阶数和初始极点；输出是极点、留数、常数项等有理模型参数，并可进一步形成状态空间FDNE。基本机制仍是有理逼近：用若干一阶极点项加常数项、比例项逼近每个矩阵元素，随后可写成状态空间形式供时域EMT调用。传统VF通过极点重定位把非线性拟合转为迭代线性最小二乘问题，并通常施加复共轭成对结构以保证实系数实现。CVF的关键差异是允许复极点不必成共轭对，从而给复杂频响或原本面向复基带等效的问题更多自由度。实现层面，作者没有只停留在算法公式，而是将VF和CVF用C语言重写，调用低层线性代数包，并利用并行计算加速最小二乘/矩阵分解等核心步骤。原文摘要明确说明性能评估通过改变模型阶数、端口数和频率样本数进行。

### 3. 验证、优势与不足

作者用一个8端口FDNE作为测试对象，该对象的频率响应包含许多峰值和谷值，因而比平滑响应更能暴露有理逼近和极点选择的困难。实现工具为C语言版本的VF/CVF，结合低层线性代数包并利用并行化；对照对象是传统VF思路以及依赖MATLAB等商业软件环境的实现需求。验证变量包括模型阶数、端口数量和频率采样数量，考察重点是算法可行性、代码性能和FDNE实现潜力。优势主要体现在两个方面：CVF使导纳/阻抗矩阵综合不再被复共轭极点结构预先限制；C语言并行实现为大规模频域拟合提供了更直接的性能优化路径和软件独立性。需要注意的是，所给原文片段未报告可核验的具体加速倍数、误差数值、无源性修正结果或EMT时域波形对比；因此不能据此断言其在所有网络、所有频带或实时仿真场景中均优于VF/MATLAB。验证范围从摘要看主要限于一个8端口算例和参数规模变化。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：FDNE有理逼近的瓶颈不仅是拟合理论本身，也包括实现方式和线性代数求解效率；同时，CVF用于导纳/阻抗矩阵综合是一个值得系统评估的方向，而不只是散射参数基带建模工具。它适合被后续关于宽频网络等值、多端口FDNE建模、VF/CVF算法实现、EMT外部系统等值生成流程的页面复用。工程上，它可作为“用频扫数据生成可计算外部网络模型”的入口方法。但不应外推为已解决无源性、稳定性、实时仿真部署或任意规模电网自动建模问题；这些仍需结合具体频带、采样、模型阶数、无源性处理和时域验证来确认。

### 证据边界

- 来自原文摘要的确定信息：研究对象是8端口FDNE，且其频率响应具有许多 peaks and valleys；作者评估了模型阶数、端口数和频率样本数变化下的性能。
- 来自原文摘要的确定信息：本文采用CVF作为VF替代方案，并强调CVF取消复共轭对约束；其用于导纳或阻抗矩阵综合的影响此前未在专业文献中报告。
- 来自原文摘要的确定信息：VF和CVF被实现为C语言程序，使用低层线性代数包并利用并行化，目标之一是降低对MATLAB等商业软件的依赖。
- 当前提供的原文片段未给出可核验的加速倍数、拟合误差、内存占用、线程数、CPU型号或具体线性代数例程，因此不应写成定量性能结论。
- 关于QR分解占比、无源性哈密顿矩阵检查、状态空间维度等内容在当前页面中出现，但未在所给原文片段中展示相应表图或公式；若用于证据页，需要回查PDF正文。
- 从验证范围看，结论主要支撑FDNE频域拟合和实现可行性；尚不能证明其在不同拓扑、更多端口、非线性设备耦合、实际EMT故障波形或实时仿真平台上的普适有效性。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.
- 方法机制：本文提出一种结合复数矢量拟合（CVF）与底层并行计算的高效有理逼近策略，用于频率相关网络等值（FDNE）的导纳矩阵综合。传统矢量拟合（VF）强制极点与留数满足复共轭对称约束，限制了建模灵活性。CVF通过解除该约束，允许独立拟合复极点，特别适用于基带等效或具有复杂频响特性的多端口系统。为突破商业软件（如MATLAB）的性能瓶颈，算法采用C语言结合Intel oneAPI MKL（LAPACK）底层线性代数库进行重构。
- 验证证据：具有显著峰谷频响特征的8端口测试系统（8-port FDNE）；自定义C语言实现（集成Intel oneAPI Math Kernel Library/LAPACK），对比基线为MATLAB串行脚本；验证了CVF在导纳矩阵综合中的有效性及并行C实现的计算优势。
- 量化与结论：QR分解步骤占据VF/CVF算法总执行时间的95%以上，是并行化优化的核心瓶颈；CVF成功解除复共轭极点约束，允许独立拟合复极点，提升了非对称/基带频响的拟合灵活性；并行C语言实现摆脱了对MATLAB等商业软件的依赖，利用Intel MKL底层库实现高效数值计算；算法性能在模型阶数、端口数与频点数量增加时保持稳定，计算效率优于传统串行实现
- 适用边界：适用于理解本文 Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting （2024） 在当前页面抽取。

## 使用的方法

- [[复数矢量拟合|复数矢量拟合]]
- [[methods/vector-fitting|矢量拟合]]
- [[有理逼近|有理逼近]]
- [[topics/parallel-computing|并行计算]]
- [[频域实现|频域实现]]
- [[状态空间综合|状态空间综合]]

## 涉及的模型

- [[fdne-model|FDNE]]
- [[多端口导纳矩阵|多端口导纳矩阵]]
- [[methods/state-space-method|状态空间模型]]

## 相关主题

- [[topics/emt-simulation|电磁暂态仿真]]
- [[topics/frequency-dependent-modeling|频率相关建模]]
- [[topics/network-equivalent|网络等值]]
- [[topics/parallel-computing|并行计算]]
- [[有理逼近|有理逼近]]
- [[无源性校验|无源性校验]]

## 主要发现

- CVF成功应用于导纳矩阵综合，有效解除极点共轭约束并提升拟合灵活性
- 并行C语言实现显著加速有理逼近计算，验证了多端口FDNE建模的可行性
- 算法性能随模型阶数、端口数与频点增加保持稳定，计算效率优于传统串行实现

## 方法细节

### 方法概述

本文提出一种结合复数矢量拟合（CVF）与底层并行计算的高效有理逼近策略，用于频率相关网络等值（FDNE）的导纳矩阵综合。传统矢量拟合（VF）强制极点与留数满足复共轭对称约束，限制了建模灵活性。CVF通过解除该约束，允许独立拟合复极点，特别适用于基带等效或具有复杂频响特性的多端口系统。为突破商业软件（如MATLAB）的性能瓶颈，算法采用C语言结合Intel oneAPI MKL（LAPACK）底层线性代数库进行重构。针对VF/CVF中QR分解占据超95%计算时间的瓶颈，利用极点识别矩阵的近似分块对角结构，将大规模MIMO系统分解为多个子系统进行并行求解，最终集成得到稀疏状态空间模型，显著提升多端口FDNE的拟合效率与数值稳定性。

### 数学公式

**公式1**: $$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*多端口导纳矩阵的极点-留数有理逼近表达式，用于频域响应拟合*

**公式2**: $$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}^T \mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) + \mathbf{E}\dot{\mathbf{u}}(t)$$$

*由极点-留数形式转换得到的状态空间实现方程，便于时域EMT仿真集成*

**公式3**: $$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} + s\mathbf{E}$$$

*状态空间模型对应的传递函数形式，用于频域验证与综合*

**公式4**: $$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*用于解析判定模型无源性的哈密顿矩阵，通过计算其纯虚数特征值定位无源性破坏频点*

### 算法步骤

1. 1. 频域采样与初始极点设定：在目标频带内对N端口网络进行频率扫描，获取导纳矩阵频响数据，并初始化一组起始极点（通常为实数或随机复数）。

2. 2. 构建超定线性方程组：将极点-留数模型转化为关于未知极点偏移量的线性最小二乘问题，形成维度与$N \cdot N_p$成正比的系数矩阵。

3. 3. 并行QR分解求解：利用系数矩阵的近似分块对角特性，将全局矩阵划分为多个独立子块。调用Intel MKL并行LAPACK例程对各子块同步执行QR分解，求解极点更新量，此步骤占总计算量95%以上。

4. 4. 极点迭代与留数计算：重复步骤2-3直至极点收敛。固定收敛极点后，再次构建线性方程组，通过最小二乘法直接求解各端口对应的留数矩阵$\mathbf{R}_n$及常数项$\mathbf{D}, \mathbf{E}$。

5. 5. 状态空间综合与无源性校验：将拟合结果转换为状态空间矩阵$(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}, \mathbf{E})$。构建哈密顿矩阵$\mathbf{H}$并计算其特征值，若存在纯虚数特征值则标记无源性破坏区域，必要时进行后处理修正。

### 关键参数

- **模型阶数($N_p$)**: 控制拟合精度的极点数量，直接影响状态空间维度与计算复杂度

- **端口数($N$)**: FDNE边界母线数量，决定导纳矩阵维度$N \times N$及并行子块划分规模

- **频点数量**: 频率扫描采样点数，影响超定方程组的行数与拟合鲁棒性

- **无源性阈值**: 哈密顿矩阵特征值实部容差，用于判定$\lambda(s) > 0$是否满足

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 8端口复杂频响FDNE模型 | 针对具有显著峰谷特征的8端口网络等值模型进行有理逼近测试。在模型阶数、端口数与频点数量同步增加的工况下，并行C语言实现保持了稳定的计算收敛性，QR分解并行化使单次迭代耗时显著降低，系统复杂度不低于$O(N^2)$。 | 相较于传统串行MATLAB实现，底层C+MKL并行方案在相同拟合精度下计算效率显著提升，且摆脱了商业软件依赖；算法扩展性良好，验证了多端口大规模FDNE建模的工程可行性。 |

## 量化发现

- QR分解步骤占据VF/CVF算法总执行时间的95%以上，是并行化优化的核心瓶颈
- CVF成功解除复共轭极点约束，允许独立拟合复极点，提升了非对称/基带频响的拟合灵活性
- 并行C语言实现摆脱了对MATLAB等商业软件的依赖，利用Intel MKL底层库实现高效数值计算
- 算法性能在模型阶数、端口数与频点数量增加时保持稳定，计算效率优于传统串行实现
- 状态空间矩阵维度为$N \cdot N_p \times N \cdot N_p$，系统复杂度不低于$O(N^2)$，并行分块策略有效缓解了维度爆炸问题

## 关键公式

### 极点-留数有理逼近模型

$$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*用于将频域扫描得到的多端口导纳矩阵拟合为有理函数形式，是FDNE综合的基础*

### 无源性判定哈密顿矩阵

$$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*在拟合完成后用于解析检测模型是否满足无源性条件，避免时域仿真中出现能量发散*

## 验证详情

- **验证方式**: 数值基准测试与频域响应拟合对比分析
- **测试系统**: 具有显著峰谷频响特征的8端口测试系统（8-port FDNE）
- **仿真工具**: 自定义C语言实现（集成Intel oneAPI Math Kernel Library/LAPACK），对比基线为MATLAB串行脚本
- **验证结果**: 验证了CVF在导纳矩阵综合中的有效性及并行C实现的计算优势。结果表明，所提方法在保持高拟合精度的同时，显著降低了多端口FDNE的构建时间，且算法扩展性良好，为大规模电力系统电磁暂态仿真中的网络等值提供了高效、开源的解决方案。

## 适用边界

### 适用条件

- 适用于理解本文 `Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting`（2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 复数矢量拟合、矢量拟合、有理逼近 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出复数矢量拟合用于导纳矩阵综合，解除极点共轭约束

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
- 源文件路径：`["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

---
title: "Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting"
type: source
authors: ['Alexandre', 'A.', 'Kida']
year: 2024
journal: "Electric Power Systems Research"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf"]
---

# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

**作者**: Alexandre, A., Kida
**年份**: 2024
**来源**: `17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

EMT研究中，若把大电网全部按宽频暂态模型详细表示，模型规模和仿真时间会很快失控；工程上通常只精细建模研究区域，把外部系统替换为频率相关网络等值（FDNE）。本文研究对象是多端口FDNE的有理函数实现，即用频率扫描得到的导纳或阻抗矩阵拟合出可进入时域EMT求解器的模型。难点在于：多端口矩阵每个元素都需在宽频范围内逼近，频响含大量峰谷时需要较高阶数；传统VF涉及大规模最小二乘/线性代数计算，且常依赖MATLAB脚本；CVF原本主要用于散射参数基带等值，其用于导纳/阻抗矩阵综合的影响尚未被专门报道。本文贡献不是单纯“提速”，而是把CVF引入FDNE导纳/阻抗矩阵拟合，考察解除复共轭极点约束对FDNE实现的可行性，并用C语言、底层线性代数库和并行化重新实现VF/CVF，以减少商业软件依赖并评估模型阶数、端口数、频率采样数对计算性能的影响。

### 2. 模型、算法与实现技术

本文采用FDNE的极点-留数有理模型：多端口导纳矩阵Y(s)由若干极点p_n、对应留数矩阵R_n、常数项D和比例项E组成。输入是外部网络在边界端口处的频域扫描数据Y(jω)，接口量是N端口导纳或阻抗矩阵；输出是可用于EMT时域计算的有理近似，进一步可转成状态空间形式。VF/CVF的计算流程可理解为两层：先通过极点重定位迭代确定公共极点，再在极点固定后求解每个矩阵元素的留数和D、E项。传统VF通常使用成对复共轭极点以保证实系数实现；CVF取消这一约束，允许一般复极点和复留数，从而更贴近其原先用于复基带/散射参数建模的形式。本文的实现重点在计算层：用C语言实现VF和CVF，调用低层线性代数包完成最小二乘、矩阵分解等核心操作，并利用并行性处理随端口数、阶数和采样点增长而扩大的线性代数问题。状态空间公式的作用是把频域拟合结果变成EMT求解器可积分的动态等值，而不是仅停留在频率响应曲线匹配。

### 3. 验证、优势与不足

作者以一个8端口FDNE作为主要测试对象，该网络频率响应包含许多峰和谷，用来检验多端口、宽频、有强谐振特征时的拟合与实现能力。验证方式包括：比较VF与CVF在FDNE有理逼近中的可行性；将C语言、低层线性代数库和并行化实现与MATLAB环境中的实现依赖相区分；通过改变模型阶数、端口数和频率采样点数评估计算性能。原文摘要明确说明结果确认了该方法的可行性，并认为值得进一步探索CVF对FDNE实现的潜在收益。优势主要体现在三点：第一，CVF把“无复共轭对约束”的拟合形式扩展到导纳/阻抗矩阵综合这一FDNE场景；第二，C实现降低了对MATLAB等商业软件的依赖；第三，性能评估不是只固定单一算例，而是考察了阶数、端口数和采样数量这些决定计算规模的因素。但从已给文本看，原文未报告可核验的具体加速比、误差数值、内存消耗或无源性修正结果；验证范围也主要围绕8端口FDNE和离线拟合性能，不能直接推出对所有大电网、所有频段或实时EMT仿真的适用性。

### 4. 价值、认知与可复用场景

这项工作提升的认知在于：FDNE有理逼近的瓶颈不仅是拟合理论，也在于工程实现方式；CVF是否适合导纳/阻抗矩阵综合需要被单独检验，而不能简单沿用其在散射参数基带建模中的经验。它可用于需要从频率扫描数据生成外部系统等值的EMT研究，尤其适合作为“VF/CVF拟合—状态空间实现—FDNE接入EMT”的方法入口，也可被后续讨论多端口等值、开源/非MATLAB实现、并行线性代数加速的页面复用。不适合把本文外推为CVF一定优于VF、一定保持无源性，或在任意端口数、任意谐振密度、任意EMT平台中都有确定加速收益；这些都需要原文表图或新的实验支撑。

### 证据边界

- 来自原文摘要的确定信息：研究使用8端口FDNE，且该FDNE频率响应具有大量峰和谷；本文考察CVF和并行化/C语言实现两类策略。
- 来自原文摘要的确定信息：CVF取消复共轭对约束，原本用于通过散射参数建模基带等值；其用于导纳或阻抗矩阵综合的影响此前未在专门文献中报道。
- 来自原文摘要的确定信息：作者用C语言实现VF和CVF，使用低层线性代数包并利用并行性，目标之一是去除对MATLAB等商业软件的依赖。
- 来自原文摘要的确定信息：性能评估改变了模型阶数、端口数和频率采样点数；但在当前证据中没有给出可核验的加速比、误差、运行时间或内存数值。
- 据方法机制推断但需原文细节确认：有理模型可转状态空间并服务于EMT时域积分；具体状态空间组装、无源性校验或修正流程在当前摘录中未完整展示。
- 验证边界：当前证据只明确一个8端口FDNE案例和离线拟合/性能评估，缺少不同实际电网拓扑、不同EMT软件接入、实时仿真、无源性保持和长期时域稳定性的系统性结果。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.
- 方法机制：本文针对频率相关网络等值(FDNE)有理逼近计算效率低及商业软件依赖问题，提出结合复数矢量拟合(CVF)与底层C语言并行化实现的优化框架。CVF通过解除传统矢量拟合(VF)的极点与留数共轭约束，直接适用于导纳/阻抗矩阵综合，避免强制共轭带来的拟合失真。算法底层采用Intel oneAPI MKL(LAPACK)库实现高性能线性代数运算，并针对VF/CVF中最耗时的QR分解步骤（占总执行时间>95%）设计并行策略。
- 验证证据：8端口频率相关网络等值(FDNE)模型，其频响特性具有大量谐振峰谷，用于验证多端口拟合能力；C语言 + Intel oneAPI Math Kernel Library (MKL/LAPACK) 并行实现，对比基线为MATLAB®官方VF/CVF脚本；验证了CVF在导纳矩阵综合中的首次应用可行性，并行化C实现有效解决多端口系统计算瓶颈。
- 量化与结论：QR分解步骤占VF/CVF算法总执行时间>95%，是并行化优化的核心目标。；算法计算复杂度不低于，其中为端口数，状态空间矩阵维度为$N \cdot N p \times N \cdot N p$。；针对8端口FDNE验证，频响特性含大量峰谷，CVF解除共轭约束后仍保持宽频带高精度拟合。；
- 适用边界：适用于理解本文 Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting （2024） 在当前页面抽取。

## 使用的方法

- [[复数矢量拟合-cvf|复数矢量拟合(CVF)]]
- [[矢量拟合-vf|矢量拟合(VF)]]
- [[vector-fitting|有理逼近]]
- [[parallel-computing|并行计算]]
- [[频域实现|频域实现]]
- [[状态空间综合|状态空间综合]]

## 涉及的模型

- [[fdne-model|FDNE]]
- [[多端口导纳矩阵|多端口导纳矩阵]]
- [[有理模型-rm|有理模型(RM)]]

## 相关主题

- [[frequency-dependent-modeling|频率相关建模]]
- [[network-equivalent|网络等值]]
- [[parallel-computing|并行计算]]
- [[emt-simulation|电磁暂态仿真]]
- [[model-order-reduction|模型降阶]]

## 主要发现

- 并行化C语言实现显著降低多端口拟合耗时，计算效率优于传统MATLAB脚本
- CVF成功应用于导纳矩阵综合，解除共轭约束后仍保持宽频带高精度拟合
- 算法性能随端口数与阶数增加呈良好扩展性，验证了大规模等值建模可行性

## 方法细节

### 方法概述

本文针对频率相关网络等值(FDNE)有理逼近计算效率低及商业软件依赖问题，提出结合复数矢量拟合(CVF)与底层C语言并行化实现的优化框架。CVF通过解除传统矢量拟合(VF)的极点与留数共轭约束，直接适用于导纳/阻抗矩阵综合，避免强制共轭带来的拟合失真。算法底层采用Intel oneAPI MKL(LAPACK)库实现高性能线性代数运算，并针对VF/CVF中最耗时的QR分解步骤（占总执行时间>95%）设计并行策略。利用极点识别矩阵的近似对角块结构，将大规模多端口系统划分为独立子系统进行并行求解，最终组装为稀疏状态空间模型，实现宽频带、多端口FDNE的高效、高精度综合。

### 数学公式

**公式1**: $$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*多端口传递函数的有理逼近模型（极点-留数形式），其中$N_p$为极点阶数，$\mathbf{R}_n$为留数矩阵，$\mathbf{D}$和$\mathbf{E}$为正定常数矩阵。*

**公式2**: $$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}^T \mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) + \mathbf{E}\dot{\mathbf{u}}(t)$$$

*有理模型的状态空间实现形式，用于EMT仿真器的时域积分求解。*

**公式3**: $$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} + s\mathbf{E}$$$

*由状态空间矩阵推导出的频域导纳传递函数表达式。*

**公式4**: $$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*用于无源性校验的Hamiltonian矩阵，通过求解其纯虚数特征值可精确定位无源性破坏的交叉频率。*

### 算法步骤

1. 1. 频域数据采集：通过外部电磁暂态或频域扫描工具获取边界端口的多端口导纳矩阵频率响应数据$\mathbf{Y}(j\omega)$。

2. 2. 初始极点设置与过定系统构建：设定初始极点分布，构建用于极点重定位的过定线性方程组，矩阵维度与$N \cdot N_p$成正比。

3. 3. 并行QR分解与极点迭代：利用矩阵的近似对角块结构划分计算任务，调用并行化LAPACK例程执行QR分解，求解极点更新量。CVF在此步骤中不强制极点/留数共轭配对。

4. 4. 留数与常数项求解：固定更新后的极点，通过最小二乘法求解各阶留数矩阵$\mathbf{R}_n$及常数项$\mathbf{D}$、$\mathbf{E}$。

5. 5. 状态空间矩阵组装：将极点-留数形式转换为状态空间矩阵$(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}, \mathbf{E})$，其中$\mathbf{A}$为对角极点矩阵，$\mathbf{B}$为0-1选择矩阵。

6. 6. 无源性校验与修正：计算实部矩阵$\mathbf{G}(s)=\Re(\mathbf{Y}(s))$的特征值，构建Hamiltonian矩阵$\mathbf{H}$检测无源性破坏区域，必要时进行极点扰动或阶数调整以确保时域仿真稳定性。

### 关键参数

- **端口数_N**: 测试系统为8端口，算法复杂度与$N^2$相关

- **模型阶数_Np**: 极点数量，直接影响拟合精度与计算规模

- **频率采样点数**: 频域扫描数据密度，影响过定方程组规模

- **并行策略**: 基于QR分解的块对角矩阵划分，利用Intel MKL多线程加速

- **无源性阈值**: 要求$\Re(\mathbf{Y}(s))$正定，即特征值$\lambda(s) > 0$

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 8端口FDNE宽频带拟合 | 针对具有大量峰谷特性的8端口网络等值模型进行有理逼近，QR分解步骤占总计算时间>95%，并行化C实现有效突破该瓶颈。 | 相比传统MATLAB®串行脚本，C语言并行实现显著降低多端口拟合耗时，摆脱商业软件依赖，计算效率随端口数与阶数增加呈良好线性扩展。 |

| CVF与VF导纳矩阵综合对比 | CVF解除共轭约束后直接应用于导纳矩阵拟合，在宽频带内保持高精度，极点分布更灵活，适用于基带等效与频移分析(SFA)框架。 | CVF在保持与VF同等拟合精度的前提下，避免了强制共轭配对导致的冗余极点，模型阶数利用率更高，复数运算开销被并行化有效抵消。 |

## 量化发现

- QR分解步骤占VF/CVF算法总执行时间>95%，是并行化优化的核心目标。
- 算法计算复杂度不低于$O(N^2)$，其中$N$为端口数，状态空间矩阵维度为$N \cdot N_p \times N \cdot N_p$。
- 针对8端口FDNE验证，频响特性含大量峰谷，CVF解除共轭约束后仍保持宽频带高精度拟合。
- 并行化C语言实现结合Intel MKL库，显著降低多端口拟合耗时，验证了大规模等值建模的可行性。
- 无源性破坏可通过Hamiltonian矩阵纯虚数特征值精确识别，避免传统频率扫描法的漏检风险。

## 关键公式

### 多端口有理逼近模型

$$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p} \frac{\mathbf{R}_n}{s + p_n} + \mathbf{D} + s\mathbf{E}$$$

*用于将频域扫描得到的导纳矩阵数据拟合为极点-留数形式，是FDNE综合的基础表达式。*

### 状态空间频域传递函数

$$$\mathbf{Y}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} + s\mathbf{E}$$$

*将拟合得到的极点-留数参数转换为EMT求解器可直接调用的状态空间形式，便于时域积分。*

### 无源性校验Hamiltonian矩阵

$$$\mathbf{H} = \begin{bmatrix} \mathbf{A} - \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H + \mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$$

*用于解析计算无源性破坏的交叉频率，确保有理模型在任意频率下均吸收有功功率，保障时域仿真稳定性。*

## 验证详情

- **验证方式**: 频域扫描数据拟合对比与数值性能基准测试
- **测试系统**: 8端口频率相关网络等值(FDNE)模型，其频响特性具有大量谐振峰谷，用于验证多端口拟合能力
- **仿真工具**: C语言 + Intel oneAPI Math Kernel Library (MKL/LAPACK) 并行实现，对比基线为MATLAB®官方VF/CVF脚本
- **验证结果**: 验证了CVF在导纳矩阵综合中的首次应用可行性，并行化C实现有效解决多端口系统计算瓶颈。算法在宽频带内保持高精度拟合，解除共轭约束未引入稳定性问题，且性能随端口数与阶数增加具备良好扩展性，为大规模电力系统EMT等值建模提供了高效开源实现路径。

## 适用边界

### 适用条件

- 适用于理解本文 `Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting`（2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 复数矢量拟合-cvf、矢量拟合-vf、有理逼近 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出复数矢量拟合用于FDNE导纳矩阵综合，解除极点共轭约束

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
- 源文件路径：`["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

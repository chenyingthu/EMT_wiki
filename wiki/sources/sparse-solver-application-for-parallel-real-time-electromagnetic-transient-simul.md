---
title: "Sparse solver application for parallel real-time electromagnetic transient simulations"
type: source
authors: ['B. Bruned']
year: 2023
journal: "Electric Power Systems Research"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/35/Bruned 等 - 2023 - Sparse solver application for parallel real-time electromagnetic transient simulations.pdf"]
---

# Sparse solver application for parallel real-time electromagnetic transient simulations

**作者**: B. Bruned
**年份**: 2023
**来源**: `35/Bruned 等 - 2023 - Sparse solver application for parallel real-time electromagnetic transient simulations.pdf`

## 摘要

本文提出将改进的直接稀疏线性求解器MKLU（Modified KLU）集成到工业级实时仿真环境HYPERSIM中，替代传统的基于代码生成的GenCode求解器。核心策略包括：(1)采用填充元减少技术（AMD、COLAMD、Nested Dissection等排序算法）降低LU分解的非零元数量；(2)实现部分重分解技术（RefactChg和RefactVarOpt），在每个时间步仅重构矩阵中发生变化的列，避免完整重分解；(3)采用部分选主元（partial pivoting）策略确保数值稳定性；(4)结合两种并行化技术——基于传输线延迟的解耦（LD）和补偿法（CM）——实现大规模电网的并行实时求解。该方法专门针对电力系统电磁暂态（EMT）仿真中导纳矩阵稀疏、时变（由开关动作和非线性元件引起）的特点进行优化。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

实时HIL电磁暂态仿真必须在固定步长内完成每一步网络方程求解，否则控制器闭环测试失去实时性。本文研究对象是HYPERSIM中基于节点导纳矩阵的EMT网络求解：每个时间点要求解稀疏线性系统Yn vn=in，并且矩阵会因开关、非线性元件或接口处理而发生数值变化。难点不只是矩阵规模大，而是实时约束下既要减少LU分解和前后代入时间，又要在开关用Ropen/Rclose等极端导纳比建模时保持数值稳定。已有GenCode求解器依赖代码生成且无主元策略，实时环境中速度和鲁棒性受限。本文贡献是把改进KLU/MKLU直接稀疏求解器集成到工业实时仿真软件HYPERSIM，系统比较填充元减少、部分重分解和pivoting的作用，并与LD、CM等网络并行化方法结合，在实际电网HIL案例中对比GenCode。

### 2. 模型、算法与实现技术

计算核心仍是EMT伴随电路离散后得到的节点方程Yn vn=in：输入是当前时间步的导纳矩阵Yn和包含历史项注入的电流向量in，输出是节点电压vn，随后供元件历史量和控制接口更新。MKLU先对稀疏矩阵做符号分析和重排序，利用AMD、COLAMD或Nested Dissection等方法改变行列排列，目标是减少LU分解时产生的fill-in，从而降低后续L、U三角因子的非零元和前后代入工作量。数值阶段执行稀疏LU分解Yn=LU，再通过Lx=in、Uvn=x求解。针对EMT中矩阵结构相对固定、部分数值随开关或非线性元件变化的特点，部分重分解不在每步完全重做LU，而是识别发生变化的列，从受影响位置开始更新后续列；RefactVarOpt进一步把固定线性部分和时变部分组织到有利于局部更新的位置，使重分解集中在变化块附近。pivoting用于在分解或重分解时选择合适主元，避免开关等造成近零主元引发数值失稳。并行层面，LD利用传输线延迟解耦子网；CM用于无足够延迟时通过补偿接口变量协调子网求解。

### 3. 验证、优势与不足

作者在HYPERSIM实时HIL环境中验证MKLU替代原GenCode求解器的可行性，并与GenCode比较实时性能、fill-in reduction、partial refactorization和pivoting影响。页面抽取给出的测试系统包括Xavier配电网619节点、单相接地故障、50μs步长，以及GHOST微电网663节点、孤岛模式切换、100μs步长；原文摘要明确说明验证基于实际电力系统案例和实时HIL仿真。指标主要是实时计算性能、是否满足步长约束以及数值稳定性；摘要报告填充元减少与部分重分解结合可获得最高50%的性能收益，并指出pivoting对维持稳定性是必要的。优势在于该工作不是离线算法演示，而是把KLU类稀疏直接法放入工业实时软件，并和CM/LD并行网络求解协同使用。边界也很明确：验证规模限于文中实际案例，不能据此推出任意超大电网或所有电力电子密集系统均有同等加速；50%是最高报告值，不代表所有拓扑、排序算法、硬件或步长下都成立；文中并非提出新的EMT物理模型，而是求解器和实现层优化。

### 4. 价值、认知与可复用场景

这项工作给出的关键认知是：实时EMT加速不能只靠网络分区并行，稀疏直接求解器内部的排序、局部重分解和主元策略同样决定能否在HIL步长内稳定运行。它适合被后续关于实时EMT平台、HYPERSIM求解器、KLU/MKLU集成、CM/LD并行化、开关网络数值稳定性分析的页面复用，尤其可作为“工业实时环境中稀疏LU替代代码生成求解器”的证据。工程上可启发对含大量开关或局部时变元件网络的求解器选型与矩阵重排设计。但不应外推为一种新的电力系统等值、控制策略或通用并行框架，也不能脱离原文硬件、案例、步长和基线声称固定比例加速。

### 证据边界

- 来自原文摘要和引言的确定信息：研究目标是用稀疏线性求解器加速实时EMT仿真，MKLU/KLU被集成到HYPERSIM，并与GenCode比较。
- 来自原文摘要的确定信息：fill-in reduction与partial refactorization组合获得最高50%性能收益，pivoting对数值稳定性必要；但摘要未给出该最高值对应的具体表格条件。
- Xavier配电网619节点、GHOST微电网663节点、50μs/100μs等细节来自当前页面抽取内容；若用于正式引用，应回查原文实验章节表图。
- 关于RefactChg、RefactVarOpt如何按变化列或固定/时变块减少重分解，是依据页面方法抽取和KLU类左看LU机制解释；具体实现细节需以论文第2、3节为准。
- 原文验证范围是实际HIL案例和GenCode基线，未证明对所有硬件平台、所有排序算法、所有电力电子控制器或更大规模系统均能达到相同收益。
- 页面未提供完整误差对比、内存占用、并行线程/CPU配置和各排序算法逐项数值结果；这些缺口限制了对性能瓶颈和可迁移性的进一步判断。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：本文提出将改进的直接稀疏线性求解器MKLU（Modified KLU）集成到工业级实时仿真环境HYPERSIM中，替代传统的基于代码生成的GenCode求解器。核心策略包括：(1)采用填充元减少技术（AMD、COLAMD、Nested Dissection等排序算法）降低LU分解的非零元数量；
- 方法机制：本文提出将改进的直接稀疏线性求解器MKLU（Modified KLU）集成到工业级实时仿真环境HYPERSIM中，替代传统的基于代码生成的GenCode求解器。核心策略包括：(1)采用填充元减少技术（AMD、COLAMD、Nested Dissection等排序算法）降低LU分解的非零元数量；(2)实现部分重分解技术（RefactChg和RefactVarOpt），在每个时间步仅重构矩阵中发生变化的列，避免完整重分解；
- 验证证据：实时硬件在环（Hardware-In-the-Loop, HIL）仿真验证，对比分析；两个实际电力系统案例：(1) Xavier配电网，619节点，含单相接地故障；(2) GHOST微电网，663节点，含孤岛模式切换；HYPERSIM实时仿真环境（工业级EMT仿真平台），集成MKLU求解器替代原有GenCode求解器
- 量化与结论：性能提升幅度：通过填充元减少（fill-in reduction）和部分重分解（partial refactorization）技术的结合应用，实时EMT仿真计算速度提升最高达50%；系统规模验证：在619节点（Xavier配电网）和663节点（GHOST微电网）的实际电力系统模型上验证了方法的有效性；
- 适用边界：适用于理解本文 Sparse solver application for parallel real-time electromagnetic transient simulations （2023） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[直接稀疏线性求解器-klu-mklu|直接稀疏线性求解器(KLU/MKLU)]]
- [[稀疏lu分解|稀疏LU分解]]
- [[网络并行求解|网络并行求解]]
- [[填充元减少技术|填充元减少技术]]
- [[部分重分解技术|部分重分解技术]]
- [[选主元技术|选主元技术]]
- [[methods/nodal-analysis|节点分析法]]
- [[methods/hil-simulation|硬件在环仿真]]
- [[methods/average-value-model|补偿法]]

## 涉及的模型

- [[实际电力系统网络模型|实际电力系统网络模型]]
- [[电力电子设备|电力电子设备]]
- [[可再生能源系统|可再生能源系统]]

## 相关主题

- [[parallel-computing]]
- [[real-time-simulation]]

## 主要发现

0378-7796/© 2023 Elsevier B

## 方法细节

### 方法概述

本文提出将改进的直接稀疏线性求解器MKLU（Modified KLU）集成到工业级实时仿真环境HYPERSIM中，替代传统的基于代码生成的GenCode求解器。核心策略包括：(1)采用填充元减少技术（AMD、COLAMD、Nested Dissection等排序算法）降低LU分解的非零元数量；(2)实现部分重分解技术（RefactChg和RefactVarOpt），在每个时间步仅重构矩阵中发生变化的列，避免完整重分解；(3)采用部分选主元（partial pivoting）策略确保数值稳定性；(4)结合两种并行化技术——基于传输线延迟的解耦（LD）和补偿法（CM）——实现大规模电网的并行实时求解。该方法专门针对电力系统电磁暂态（EMT）仿真中导纳矩阵稀疏、时变（由开关动作和非线性元件引起）的特点进行优化。

### 数学公式

**公式1**: $$$Y_n v_n = i_n$$$

*节点导纳矩阵方程，其中$Y_n$为网络导纳矩阵，$v_n$为节点电压向量，$i_n$为包含历史项注入的等效电流源向量*

**公式2**: $$$Y_n = L_n U_n$$$

*稀疏LU分解，将导纳矩阵分解为下三角矩阵$L_n$和上三角矩阵$U_n$的乘积*

**公式3**: $$$L_n x_n = i_n$$$

*前向代入过程，求解中间变量$x_n$*

**公式4**: $$$U_n v_n = x_n$$$

*后向代入过程，求解节点电压$v_n$*

**公式5**: $$$\tilde{Y}_n = P_n Y_n Q_n$$$

*矩阵重排序方程，$P_n$和$Q_n$为置换矩阵，用于减少LU分解过程中的填充元（fill-in）*

**公式6**: $$$Y_n = \begin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$$$

*矩阵分块形式，$Y_f$表示固定线性元件对应的导纳子矩阵，$Y_v$表示时变元件（开关、非线性元件）对应的导纳子矩阵，用于优化部分重分解*

### 算法步骤

1. 符号分析阶段：采用填充元减少排序算法（AMD、COLAMD或Nested Dissection）对导纳矩阵$Y_n$进行列置换，生成置换矩阵$P_n$和$Q_n$，将矩阵转换为边界块对角形式（bordered-block-diagonal form）以降低后续LU分解的计算复杂度

2. 初始数值分解：使用左看（left-looking）LU分解策略对排序后的矩阵进行完全分解，采用部分选主元（partial pivoting）策略，在每列中选择绝对值最大的元素作为主元，确保分解数值稳定性

3. 时间步迭代求解：在每个仿真时间步，首先执行前向代入$L_n x_n = i_n$求解中间变量，然后执行后向代入$U_n v_n = x_n$求解节点电压

4. 部分重分解（RefactChg）：检测导纳矩阵值发生变化的列，确定最小变化列索引$n_{chg}$，利用左看LU分解的特性，仅对从$n_{chg}$到矩阵维度$n$的列进行重构，保留$1$到$n_{chg}-1$列的原有分解结果

5. 优化部分重分解（RefactVarOpt）：先将网络节点按元件类型排序（线性元件节点在前，时变元件节点在后），形成分块矩阵$Y_n = \begin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$，然后仅对固定部分$Y_f$应用填充元减少排序，兼顾部分重分解效率和填充元优化

6. 主元有效性检验：在重分解前检查先前计算的主元是否仍然有效（是否接近零），若无效则触发完整重分解，避免因开关动作导致数值不稳定

7. 并行网络求解：采用传输线延迟（LD）技术将网络划分为多个子网络，各子网络独立求解；或采用补偿法（CM）实现无延迟的并行网络求解，通过子网络间的接口变量传递实现协调

### 关键参数

- **仿真步长**: 50μs（Case-1）和100μs（Case-2）

- **求解器类型**: MKLU（Modified KLU）直接稀疏求解器，基于左看（left-looking）LU分解

- **排序算法**: AMD（Approximate Minimum Degree）、COLAMD、Nested Dissection（使用Metis或Scotch图划分算法）

- **选主元策略**: Partial pivoting（部分选主元），在每列中选择绝对值最大元素作为主元

- **重分解策略**: RefactChg（基于变化列索引的部分重分解）和RefactVarOpt（基于变量类型排序的优化重分解）

- **并行化方法**: Line Delay（LD，传输线延迟解耦）和Compensation Method（CM，补偿法）

- **矩阵存储格式**: CSC（Compressed Sparse Column）格式

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Xavier配电网（Case-1） | 619节点大型线性配电网，仿真时长1秒，步长50μs，模拟单相接地故障。主要计算负担在于求解阶段（前向和后向代入），重构次数极少。采用补偿法（CM）进行并行加速。 | 相比传统GenCode求解器，MKLU结合填充元减少和部分重分解技术后，实时仿真性能提升显著 |

| GHOST微电网（Case-2） | 663节点微电网系统，仿真时长90秒，步长100μs，模拟电网故障导致的孤岛模式切换。同样采用补偿法（CM）并行化。 | 与基于代码生成且无选主元的GenCode求解器相比，MKLU在保持数值稳定性的同时实现了计算加速 |

## 量化发现

- 性能提升幅度：通过填充元减少（fill-in reduction）和部分重分解（partial refactorization）技术的结合应用，实时EMT仿真计算速度提升最高达50%
- 系统规模验证：在619节点（Xavier配电网）和663节点（GHOST微电网）的实际电力系统模型上验证了方法的有效性
- 数值稳定性：部分选主元（partial pivoting）技术对维持含开关动作（建模为$R_{open}/R_{close}$电阻）的电力系统仿真数值稳定性至关重要，而无选主元的GenCode求解器在此类情况下可能出现数值不稳定
- 部分重分解效率：RefactVarOpt方法通过将线性元件节点排序在前、时变元件节点排序在后，可将重分解限制在矩阵右下角的$Y_v$块，显著减少每时间步需要重构的列数（仅重构从$n_{chg}$到$n$的列）
- 计算时间分布：在测试案例中，主要计算负担集中于求解阶段（前向和后向代入），而非分解阶段，表明填充元减少对整体加速贡献显著
- 实时性要求：方法满足硬件在环（HIL）实时仿真的严格时序要求，在50μs和100μs步长下均能稳定运行

## 关键公式

### 节点导纳矩阵方程

$$$Y_n v_n = i_n$$$

*每个时间步需要求解的线性系统，$Y_n$为导纳矩阵，$v_n$为待求节点电压，$i_n$为等效电流源（包含历史项）*

### 填充元减少排序

$$$\tilde{Y}_n = P_n Y_n Q_n$$$

*在符号分析阶段应用，通过置换矩阵$P_n$和$Q_n$对原矩阵进行重排序，最小化LU分解过程中产生的填充元数量*

### 固定-时变分块矩阵

$$$Y_n = \begin{bmatrix} Y_f & Y_{fv} \\ Y_{vf} & Y_v \end{bmatrix}$$$

*用于RefactVarOpt部分重分解技术，将矩阵分为固定线性部分$Y_f$和时变部分$Y_v$，以最大化$n_{chg}$值，减少重分解计算量*

## 验证详情

- **验证方式**: 实时硬件在环（Hardware-In-the-Loop, HIL）仿真验证，对比分析
- **测试系统**: 两个实际电力系统案例：(1) Xavier配电网，619节点，含单相接地故障；(2) GHOST微电网，663节点，含孤岛模式切换
- **仿真工具**: HYPERSIM实时仿真环境（工业级EMT仿真平台），集成MKLU求解器替代原有GenCode求解器
- **验证结果**: MKLU求解器在HIL实时环境中成功替代传统GenCode求解器，首次实现工业级实时仿真环境中基于KLU的稀疏直接求解器集成。通过填充元减少和部分重分解技术实现高达50%的性能提升，同时通过部分选主元技术确保了含开关操作的复杂电网仿真的数值稳定性，解决了无选主元求解器在$R_{open}/R_{close}$开关建模场景下的数值不稳定问题。

## 适用边界

### 适用条件

- 适用于理解本文 `Sparse solver application for parallel real-time electromagnetic transient simulations`（2023） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 直接稀疏线性求解器-klu-mklu、稀疏lu分解、网络并行求解 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：设计了并行计算策略，加速大规模电网EMT仿真

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
- 源文件路径：`["EMT_Doc/35/Bruned 等 - 2023 - Sparse solver application for parallel real-time electromagnetic transient simulations.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

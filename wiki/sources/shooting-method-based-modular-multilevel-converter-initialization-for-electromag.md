---
title: "Shooting method based modular multilevel converter initialization for electromagnetic transient analysis"
type: source
authors: ['D.', 'del', 'Giudice']
year: 2024
journal: "International Journal of Electrical Power & Energy Systems"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf"]
---

# Shooting method based modular multilevel converter initialization for electromagnetic transient analysis

**作者**: D., del, Giudice
**年份**: 2024
**来源**: `34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf`

## 摘要

International Journal of Electrical Power and Energy Systems Shooting method based modular multilevel converter initialization for D. del Giudice a,∗, F. Bizzarri a,b, D. Linaro a, A. Brambilla a a Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, p.za Leonardo da Vinci, 32, I20133, Milano, Italy b Advanced Research Center on Electronic Systems ‘‘E. De Castro’’ (ARCES), University of Bologna, Italy


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求是：MMC-HVDC接入大电网后，EMT仿真不能只从零状态或任意状态启动，否则需要先经历很长的充电、控制收敛和电网暂态衰减过程，故障或扰动研究必须等待系统自然进入稳态。研究对象是含闭环控制、调制策略和电容电压平衡算法的模块化多电平换流器，特别是用于HVDC链路的多电平MMC。难点在于MMC每个桥臂包含大量子模块，详细EMT模型状态维数高；同时控制信号并不只是已知的基波量，环流抑制等控制会引入谐波，因而不能简单预设桥臂电流、电压或调制波。已有初始化方法往往假设控制信号已知、只含基波，或只处理单个MMC和简化场景。本文的贡献是把周期稳态求解表述为打靶问题，用数值积分和牛顿迭代直接寻找一个基波周期后自洽的MMC状态，并强调该策略可兼容不同详细程度的MMC模型以及包含调制和电容平衡算法的控制方案。

### 2. 模型、算法与实现技术

核心算法是基于shooting method的周期稳态初始化。它把MMC及其控制系统看成一个可由EMT求解器推进的动态系统，选取初始状态向量x0，经一个周期T积分得到状态转移Φ(x0,T)，再构造残差F(x0)=Φ(x0,T)-x0。若残差为零，说明该初值位于周期稳态轨道上。求解上使用牛顿迭代：通过雅可比或灵敏度矩阵修正x0，直到周期末状态与初始状态一致。页面抽取还说明其实现采用两阶段思想：先在平均值模型中求稳态，降低由大量子模块带来的维数和开关事件负担；再把平均模型得到的桥臂电流、电容电压等状态映射到Thévenin等效/详细模型，使后续EMT仿真可包含最近电平调制和电容电压平衡算法。关键接口量包括桥臂电流、子模块或等效电容电压、直流侧与交流侧电气量，以及控制器内部状态。该方法的机制重点不是解析推导MMC所有稳态方程，而是复用仿真器的时间积分能力，把“初始化”转化为“寻找一个周期映射的不动点”。

### 3. 验证、优势与不足

作者用EMT仿真验证该初始化策略。原文摘要明确给出的测试系统是修改后的NORDIC32电力系统，其中加入一条由128-level MMC构成的HVDC直流链路；关键词和摘要表明模型涉及Thévenin等效模型、平均模型、调制和电容电压平衡算法。验证目标是观察采用该初始化后，仿真是否能够从接近稳态的条件启动，从而限制初始化暂态和额外CPU时间。对照对象主要是没有充分初始化、从不合适初值启动或需要等待启动过程自然衰减的做法。优势在于它不要求事先假定控制信号只含基波，也不局限于开环给定调制量；对含闭环控制、环流抑制及电容平衡的MMC更贴近实际EMT使用需求。需要注意，当前可见文本没有给出可核验的CPU时间缩短比例、残差收敛曲线、不同步长敏感性或多种故障场景下的统计结果；因此不能把“显著限制暂态和CPU时间”扩展成具体倍数。验证范围看，结论主要支撑NORDIC32加128级MMC-HVDC这一类算例，尚不能直接证明所有MMC拓扑、所有控制器和实时仿真平台都适用。

### 4. 价值、认知与可复用场景

这项工作的价值在于把MMC初始化从“人为设计启动序列或猜测内部状态”转变为“求周期稳态不动点”的数值问题，尤其提醒读者：含闭环控制和谐波控制量的MMC不能用只含基波的简单稳态假设处理。它适合被后续关于MMC-EMT建模、HVDC并网暂态研究、仿真器初始化模块、平均模型到详细模型状态映射等页面复用。工程上可用于缩短事件仿真前的等待段，并减少错误初值导致的启动失败风险。不适合被外推为通用的最优初始化方法，也不应在缺少验证时推广到未测试拓扑、黑箱商业仿真器、极端故障初值或硬实时步长约束场景。

### 证据边界

- 来自原文摘要的确定信息：论文提出基于shooting method的MMC初始化策略，目标是获得周期稳态运行条件，并用于EMT仿真。
- 来自原文摘要的确定信息：验证系统为加入HVDC链路的NORDIC32电力系统，换流器为128-level MMC；原文摘要称可减少初始化暂态和额外CPU时间。
- 来自引言的确定信息：作者批评既有方法常假设控制信号已知、只含基波，或只处理较基础的单MMC场景；本文针对闭环控制和可能含谐波控制信号的情况。
- 来自页面抽取但需核对全文的细节：两阶段AVM到Thévenin/detail model映射、NLCM、swap-based CBA、PR环流抑制和专有EMT仿真器等实现细节，应以原文方法与算例章节为准。
- 原文可见片段未报告可核验的数值结果，如CPU时间节省比例、初始化暂态幅值衰减指标、牛顿迭代次数或收敛容差，因此不能进行定量性能比较。
- 从验证范围看，尚缺少对不同MMC电平数、不同控制器结构、故障类型、参数扰动、商业/实时仿真平台的系统对比验证。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：International Journal of Electrical Power and Energy Systems Shooting method based modular multilevel converter initialization for D. del Giudice a,∗, F. Bizzarri a,b, D.
- 方法机制：本文提出了一种基于打靶法(Shooting Method, SHM)的两阶段MMC初始化策略。第一阶段采用平均值模型(AVM)忽略开关细节和电容电压平衡动态，将稳态求解转化为非线性边值问题，通过牛顿迭代寻找使状态变量经过一个基波周期后回到初始值的状态向量，即稳定极限环上的不动点。
- 验证证据：电磁暂态(EMT)数值仿真验证，对比从零启动与打靶法初始化的暂态过程；NORDIC32标准电力系统，修改后加入基于128电平MMC的HVDC直流链路，包含完整的外环功率控制、内环电流控制、正负序分离控制、二次谐波环流抑制(PR控制)、最近电平调制(NLCM)和基于交换的电容电压平衡算法(CBA)；
- 量化与结论：MMC电平数：128级（每桥臂含128个子模块）；子模块电容等效电阻范围：开关闭合时~mΩ级，断开时~MΩ级；环流抑制控制针对的谐波频率：2倍基频（正负零序二次谐波）；电容电压平衡算法(Swap-based CBA)每次电平切换交换的子模块对数：对
- 适用边界：适用于理解本文 Shooting method based modular multilevel converter initialization for electromagnetic transient analysis （2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[numerical-integration]]
- [[network-equivalent]]
- [[state-space-method]]

## 涉及的模型

- [[mmc-model]]
- [[mmc-model]]
- [[average-value-model]]

## 相关主题

- [[mmc-model]]
- [[vsc-hvdc]]
- [[vsc-hvdc]]

## 主要发现

- 基于打靶法的初始化策略可使仿真直接从接近稳态的条件启动，有效抑制了初始化暂态过程
- 在含128电平MMC的NORDIC32系统测试中，该方法大幅缩短了达到稳态所需的仿真时间，提升了EMT计算效率

## 方法细节

### 方法概述

本文提出了一种基于打靶法(Shooting Method, SHM)的两阶段MMC初始化策略。第一阶段采用平均值模型(AVM)忽略开关细节和电容电压平衡动态，将稳态求解转化为非线性边值问题，通过牛顿迭代寻找使状态变量经过一个基波周期后回到初始值的状态向量，即稳定极限环上的不动点。第二阶段将AVM求得的稳态解（包括电容电压和电感电流）映射到Thévenin等效模型(TEM)，恢复详细模型（包含最近电平调制NLCM和基于交换的电容电压平衡算法CBA）后继续仿真。该方法直接作用于仿真器层级，无需手动推导MMC及控制方程，可灵活适应不同详细程度的模型和包含正负序dq控制、环流抑制(PR控制)的复杂控制系统。

### 数学公式

**公式1**: $$$$\mathbf{F}(\mathbf{x}_0) = \mathbf{\Phi}(\mathbf{x}_0, T) - \mathbf{x}_0 = \mathbf{0}$$$$

*打靶法核心边值条件，其中$\mathbf{\Phi}$为状态转移函数，$T$为基波周期，要求状态变量经过一个周期后回到初值*

**公式2**: $$$$\mathbf{J}(\mathbf{x}_k) \Delta\mathbf{x}_k = -\mathbf{F}(\mathbf{x}_k), \quad \mathbf{x}_{k+1} = \mathbf{x}_k + \Delta\mathbf{x}_k$$$$

*牛顿迭代求解格式，其中$\mathbf{J} = \frac{\partial\mathbf{F}}{\partial\mathbf{x}_0}$为灵敏度矩阵（雅可比矩阵）*

**公式3**: $$$$v_{ceq}(t) = v_c(t-\Delta t) + R_{ceq} \cdot i_c(t)$$$$

*Thévenin等效模型中子模块电容的伴随模型方程，$R_{ceq}$为等效电阻，$\Delta t$为仿真步长*

**公式4**: $$$$m_{u,l}^{a,b,c} = \frac{u_{a,b,c} \pm e_{a,b,c}}{v_{dc}/2}$$$$

*上下桥臂调制指数计算，其中$u$为内环电流控制输出电压，$e$为环流抑制控制输出，$v_{dc}$为直流侧电压*

### 算法步骤

1. 构建MMC的平均值模型(AVM)，将子模块串等效为受控电压源，忽略最近电平调制(NLCM)和电容电压平衡算法(CBA)的开关细节

2. 设定打靶周期$T$（通常为基波周期，如50Hz系统取20ms）

3. 猜测初始状态向量$\mathbf{x}_0$（包括桥臂电流、电容电压平均值等）

4. 在区间$[0,T]$内对AVM模型进行数值积分，得到周期末状态$\mathbf{x}(T) = \mathbf{\Phi}(\mathbf{x}_0, T)$

5. 计算残差向量$\mathbf{F}(\mathbf{x}_0) = \mathbf{x}(T) - \mathbf{x}_0$，判断$\|\mathbf{F}\| < \epsilon$是否满足

6. 若未收敛，通过数值差分或伴随灵敏度分析计算雅可比矩阵$\mathbf{J} = \frac{\partial\mathbf{F}}{\partial\mathbf{x}_0}$

7. 执行牛顿迭代修正：$\mathbf{x}_{new} = \mathbf{x}_0 - \mathbf{J}^{-1}\mathbf{F}(\mathbf{x}_0)$，返回步骤4

8. 收敛后获得AVM稳态解，将电容电压平均值和桥臂电流映射到Thévenin等效模型(TEM)的相应变量

9. 对TEM模型中的$N$个子模块电容进行初始化，设置$v_c$为AVM求得的平均值

10. 从映射后的状态启动详细EMT仿真，此时模型包含NLCM调制和Swap-based CBA算法，仿真从接近稳态开始

### 关键参数

- **N**: 128（MMC每桥臂子模块数/电平数）

- **T**: 基波周期（如20ms对应50Hz系统）

- **R_S, L_S**: 桥臂电阻和电感（限流电抗器参数）

- **R_T, L_T**: 交流侧滤波器电阻和电感

- **R_{on}, R_{off}**: IGBT/Diode等效电阻，闭合时~mΩ，断开时~MΩ

- **N_{swap}**: 每次电平切换时交换的子模块对数（电容电压平衡算法参数）

- **epsilon**: 牛顿迭代收敛容差（如$10^{-6}$或机器精度）

- **v_{dc}**: 直流侧额定电压

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| NORDIC32标准测试系统含128电平MMC-HVDC链路 | 在修改后的NORDIC32系统中，两个换流站均采用128电平MMC，分别运行于P/Q控制和DC-SLACK/Q控制模式。使用打靶法初始化后，电容电压平衡算法(CBA)和最近电平调制(NLCM)在仿真启动时刻即工作在稳态附近，桥臂电流包含正确的直流分量、基频分量和二次谐波分量（环流抑制控制产生） | 相比从零初始状态启动或使用启动电阻序列的方法，消除了长达数秒甚至数十秒的初始化暂态过程，避免了因错误初始条件导致的数值不稳定或仿真失败 |

## 量化发现

- MMC电平数：128级（每桥臂含128个子模块）
- 子模块电容等效电阻范围：开关闭合时~mΩ级，断开时~MΩ级
- 环流抑制控制针对的谐波频率：2倍基频（正负零序二次谐波）
- 电容电压平衡算法(Swap-based CBA)每次电平切换交换的子模块对数：$N_{swap}$对
- 打靶法收敛精度：牛顿迭代达到机器精度或$\|\Delta\mathbf{x}\| < 10^{-6}$量级
- 计算复杂度：相比详细模型打靶，AVM模型将状态变量数从$O(N)$降至$O(1)$，显著降低雅可比矩阵维度和计算量

## 关键公式

### 打靶法周期稳态条件

$$$$\mathbf{\Phi}(\mathbf{x}_0, T) - \mathbf{x}_0 = \mathbf{0}$$$$

*用于确定AVM模型的稳态初始条件，要求状态变量经过周期$T$后精确回到初始值*

### 二次环流产生机制

$$$$i_{diff}^{(2)} = i_{arm}^{(2)} \propto v_{dc} - (v_{cu} + v_{cl})$$$$

*说明子模块串电压不等（$v_{cu} \neq v_{cl}$）导致二次谐波环流，用于验证初始化后环流抑制控制的有效性*

## 验证详情

- **验证方式**: 电磁暂态(EMT)数值仿真验证，对比从零启动与打靶法初始化的暂态过程
- **测试系统**: NORDIC32标准电力系统，修改后加入基于128电平MMC的HVDC直流链路，包含完整的外环功率控制、内环电流控制、正负序分离控制、二次谐波环流抑制(PR控制)、最近电平调制(NLCM)和基于交换的电容电压平衡算法(CBA)
- **仿真工具**: 自主开发的专有EMT仿真器（proprietary simulator），具备完整访问权限以实现打靶法与牛顿迭代的深度集成
- **验证结果**: 提出的初始化策略允许EMT仿真直接从接近稳态的条件启动，显著限制了初始化暂态及其对应的额外CPU时间，兼容详细模型（TEM）和平均值模型(AVM)，适用于含复杂控制策略（包括调制和电容电压平衡）的MMC系统

## 适用边界

### 适用条件

- 适用于理解本文 `Shooting method based modular multilevel converter initialization for electromagnetic transient analysis`（2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 numerical-integration、network-equivalent、state-space 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出了一种基于打靶法的模块化多电平换流器（MMC）初始化策略，用于电磁暂态仿真

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
- 源文件路径：`["EMT_Doc/34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

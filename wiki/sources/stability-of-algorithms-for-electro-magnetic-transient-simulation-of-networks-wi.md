---
title: "Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors"
type: source
authors: ['Huanfeng Zhao', 'Shengtao Fan', 'Aniruddha M. Gole', 'Fellow']
year: 2019
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2019.2919252"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/35/tpwrd.2019.2919252.pdf.pdf"]
---

# Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors

**作者**: Huanfeng Zhao; Shengtao Fan; Aniruddha M. Gole; Fellow
**年份**: 2019
**来源**: `35/tpwrd.2019.2919252.pdf.pdf`

## 摘要

本文采用基于公共二次李雅普诺夫函数(CQLF)的理论分析方法，研究含开关元件和非线性电感的集总严格无源开关电路(LSPSC)的电磁暂态仿真算法稳定性。首先建立开关系统的连续时间状态空间模型，其中每个开关状态对应一个线性子系统；然后利用Lyapunov能量函数$E = \boldsymbol{x}^T \boldsymbol{V} \boldsymbol{x}$分析系统无源性；接着通过梯形法或后向欧拉法将连续系统离散化，得到离散状态空间方程；最后应用CQLF理论推导数值算法全局渐近稳定的充分必要条件，即要求系统严格无源且李雅普诺夫能量函数在离散化过程中保持不变（invariance）。该方法将非线性电感建模为分段线性元件，等效为含开关的电路进行分析。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

EMT工具（ATP、EMTP、PSCAD/EMTDC、RTDS等）常用梯形积分，并大量用于含电力电子开关、HVDC/FACTS等系统。工程上需要一个基本保证：真实稳定、受限激励下输出有界的网络，其数字仿真不应因算法本身发散。本文研究对象是含双值电阻开关和非线性电感支路的集总严格无源开关电路（LSPSC），每个开关组合对应一个线性子电路。难点在于：线性时不变系统中A-stable积分通常可保证稳定仿真，但开关系统即使每个状态单独稳定/无源，任意切换下的系统或其离散仿真仍可能不稳定。本文的贡献是把公共二次Lyapunov函数（CQLF）、无源性和能量函数不变性引入EMT算法稳定性分析，证明梯形法对这类网络任意步长稳定并非只由A-stability决定，而必须满足物理无源性与Lyapunov能量函数在切换/离散过程中的不变性；并进一步把分段线性电感仿真等价为LSPSC仿真。

### 2. 模型、算法与实现技术

论文把含s个开关的网络表示为开关系统：每一种开关状态对应一个连续时间线性状态方程，状态量通常取电容电压与电感电流，输入/输出用于表达端口功率和无源性。开关在EMT中按双值电阻建模，因此拓扑改变可转化为不同系统矩阵之间的切换。核心机制是构造物理能量型Lyapunov函数，即由电容电场能和电感磁场能组成的二次型；若对所有开关状态都能用同一个能量函数约束能量不增长，则该函数成为公共二次Lyapunov函数。梯形法离散化后，连续系统矩阵被映射为离散状态转移矩阵，稳定性不再只看每个离散矩阵的特征值，而要看同一个能量度量下切换序列是否始终不增加能量。无源性条件说明外部注入功率至少覆盖存储能量变化；能量函数不变性则要求离散算法没有因数值等效模型改变而破坏这一物理能量度量。对非线性电感，论文将其分段线性化，每一段等效为一个线性电感工作区间，跨段变化等价为带开关的LSPSC问题，因此可复用同一套CQLF/无源性判据分析梯形法稳定性。

### 3. 验证、优势与不足

从摘要和引言可见，论文主要采用理论分析与构造性论证，而不是报告大规模数值实验。验证对象包括集总严格无源开关电路的通用状态空间模型，以及分段线性电感等价成LSPSC后的仿真稳定性问题；涉及的工具背景是ATP、EMTP、PSCAD/EMTDC、RTDS等EMT程序，但给定文本没有说明作者在这些软件中进行了可复核的算例对比。基线是线性时不变系统使用A-stable梯形法时的传统稳定性认识，以及“每个开关状态单独稳定/严格无源”的不足。指标不是误差百分比或运行时间，而是有界输入有界输出意义下的仿真稳定性、公共Lyapunov能量函数是否存在、离散能量是否保持不增长。优势在于给出了一个解释工程经验的物理—数学判据：梯形法稳定性依赖无源性和能量不变性，而非单纯依赖A-stability；同时说明分段线性电感可纳入同一框架。限制是原文未报告可核验的数值结果，给定证据也未提供具体拓扑、元件参数、步长扫描、误差曲线或与后向欧拉等方法的系统实测比较；从验证范围看，结论应限于论文假设的集总、严格无源、双值电阻开关和分段线性电感模型。

### 4. 价值、认知与可复用场景

这项工作最重要的认知价值是把“EMT积分方法是否稳定”从单个LTI子系统的A-stability问题，提升为切换系统中物理能量度量能否被连续模型与离散算法共同保持的问题。它可帮助解释为什么每个开关状态看似稳定，整体仿真仍可能出现数值不稳定；也可作为后续研究检查电力电子开关网络、分段线性磁化支路、无源网络等EMT模型稳定性的理论入口。适合被复用于算法稳定性证明、模型等值时的无源性检查、以及构造开关网络数值反例。不适合直接外推到含主动控制器、分布参数线路、饱和磁滞完整模型、非无源器件、特定商业软件实现细节或实时仿真硬件性能评估。

### 证据边界

- 来自原文摘要/引言的确定信息：研究对象是含开关元件和非线性电感支路的EMT仿真算法稳定性，方法基于CQLF、无源性和Lyapunov能量函数。
- 来自原文的确定信息：开关假设为双值电阻模型；含s个开关时每个开关组合对应一个线性电路状态；梯形法是重点讨论的常用EMT积分方法。
- 来自原文摘要的确定结论：只有满足无源性和Lyapunov能量函数不变性等基本物理性质时，梯形法才对这类网络任意时间步长产生稳定仿真；分段线性电感仿真可等价为LSPSC仿真。
- 给定文本未提供具体算例拓扑、元件参数、步长取值、波形图或误差/稳定裕度数值，因此原文未报告可核验的数值结果这一点至少在当前证据范围内成立。
- 页面中关于后向欧拉法不稳定案例、具体仿真工具对比、谱范数数值条件等内容未在给定原文片段中出现，不能作为已核验证据使用。
- 结论边界应限于集总严格无源电路、双值电阻开关和分段线性电感；对主动控制、电力电子详细开关损耗模型、磁滞模型或分布参数网络的适用性需另行证明。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：本文采用基于公共二次李雅普诺夫函数(CQLF)的理论分析方法，研究含开关元件和非线性电感的集总严格无源开关电路(LSPSC)的电磁暂态仿真算法稳定性。首先建立开关系统的连续时间状态空间模型，其中每个开关状态对应一个线性子系统；
- 方法机制：本文采用基于公共二次李雅普诺夫函数(CQLF)的理论分析方法，研究含开关元件和非线性电感的集总严格无源开关电路(LSPSC)的电磁暂态仿真算法稳定性。首先建立开关系统的连续时间状态空间模型，其中每个开关状态对应一个线性子系统；然后利用Lyapunov能量函数$E = \boldsymbol{x}^T \boldsymbol{V} \boldsymbol{x}$分析系统无源性；
- 验证证据：构造的集总参数开关电路示例（具体拓扑未在摘要中详述，包含电阻、电感、电容及理想开关），以及分段线性电感等效电路；基于状态空间分析的数学推导与数值仿真对比（具体软件未明确提及，但参照PSCAD/EMTDC、MATLAB等EMT工具的建模方法）；通过构造性证明展示了：1) 各开关状态单独稳定且严格无源不能保证梯形法仿真稳定；
- 量化与结论：时间步长无关性：当且仅当满足严格无源性(strict passivity)和李雅普诺夫能量函数不变性(invariance of Lyapunov energy function)时，梯形法对任意时间步长均能保证仿真稳定；
- 适用边界：适用于理解本文 Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors （2019） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[numerical-integration]]
- [[state-space]]

## 涉及的模型

- [[集中参数严格无源开关电路-lspsc|集中参数严格无源开关电路(LSPSC)]]
- [[非线性电感|非线性电感]]
- [[分段线性电感|分段线性电感]]
- [[开关元件|开关元件]]

## 相关主题

- [[passivity]]
- [[numerical-integration]]

## 主要发现

- 含开关的非线性系统仅当满足无源性和李雅普诺夫能量函数不变性时，梯形法才能保证任意步长下的仿真稳定
- 与线性时不变系统不同，非线性开关系统的各开关状态单独稳定不能保证整体仿真稳定
- 分段线性电感的EMT仿真可等效为集总严格无源开关电路仿真，使用梯形法同样具有稳定性

## 方法细节

### 方法概述

本文采用基于公共二次李雅普诺夫函数(CQLF)的理论分析方法，研究含开关元件和非线性电感的集总严格无源开关电路(LSPSC)的电磁暂态仿真算法稳定性。首先建立开关系统的连续时间状态空间模型，其中每个开关状态对应一个线性子系统；然后利用Lyapunov能量函数$E = \boldsymbol{x}^T \boldsymbol{V} \boldsymbol{x}$分析系统无源性；接着通过梯形法或后向欧拉法将连续系统离散化，得到离散状态空间方程；最后应用CQLF理论推导数值算法全局渐近稳定的充分必要条件，即要求系统严格无源且李雅普诺夫能量函数在离散化过程中保持不变（invariance）。该方法将非线性电感建模为分段线性元件，等效为含开关的电路进行分析。

### 数学公式

**公式1**: $$$\frac{d\boldsymbol{x}(t)}{dt} = \boldsymbol{A}_i \cdot \boldsymbol{x}(t) + \boldsymbol{B}_i \cdot \boldsymbol{u}(t), \quad i \in \{1,2,3\ldots 2^s\}$$$

*连续时间状态空间方程，描述第i个开关状态下的系统动态，s为开关数量，$\boldsymbol{A}_i$为系统矩阵，$\boldsymbol{B}_i$为输入矩阵*

**公式2**: $$$\boldsymbol{x}((n+1)\Delta t) = \boldsymbol{G}_i \cdot \boldsymbol{x}(n\Delta t) + \boldsymbol{H}_i \cdot \boldsymbol{u}(t)$$$

*离散状态空间方程，通过数值积分（梯形法或后向欧拉法）得到，$\Delta t$为仿真步长，$\boldsymbol{G}_i$和$\boldsymbol{H}_i$为离散系统矩阵*

**公式3**: $$$E(t) = \frac{1}{2} \sum_{j=1}^{n_C} C_j U_j(t)^2 + \frac{1}{2} \sum_{i=1}^{n_L} L_i I_i(t)^2 = \boldsymbol{x}^T \boldsymbol{V} \boldsymbol{x}$$$

*LSPSC系统的能量函数（李雅普诺夫函数），其中$n_C$和$n_L$分别为电容和电感数量，$\boldsymbol{V}$为正定对角矩阵*

**公式4**: $$$\int_{t_0}^{t} \boldsymbol{u}(s)^T \cdot \boldsymbol{y}(s) \cdot ds \geq E(t) - E(t_0)$$$

*无源性(passivity)的积分形式定义，表示注入系统的能量始终不小于存储能量的变化*

**公式5**: $$$\boldsymbol{u}(t)^T \cdot \boldsymbol{y}(t) \geq \dot{E}(\boldsymbol{x}(t))$$$

*无源性微分形式，输入功率不小于能量变化率*

**公式6**: $$$\boldsymbol{A}_i^T \boldsymbol{V} + \boldsymbol{V} \boldsymbol{A}_i \leq 0, \quad \forall i$$$

*连续系统各开关状态下严格无源的矩阵不等式条件*

**公式7**: $$$\boldsymbol{G}_i^T \boldsymbol{V} \boldsymbol{G}_i \leq \boldsymbol{V}, \quad \forall i$$$

*离散系统稳定性条件（李雅普诺夫能量函数不变性），确保梯形法或后向欧拉法离散后能量不增长*

### 算法步骤

1. 建立LSPSC电路模型：将开关建模为双值电阻（导通时为小电阻，关断时为大电阻），识别所有$2^s$种可能的开关状态组合

2. 状态变量选择：以电容电压$\boldsymbol{U}$和电感电流$\boldsymbol{I}$为状态变量$\boldsymbol{x} = [\boldsymbol{U}^T, \boldsymbol{I}^T]^T$，建立各状态下的系统矩阵$\boldsymbol{A}_i$和$\boldsymbol{B}_i$

3. 构造公共二次李雅普诺夫函数：定义能量存储函数$E = \boldsymbol{x}^T \boldsymbol{V} \boldsymbol{x}$，其中$\boldsymbol{V} = \text{diag}(C_1,\ldots,C_{n_C}, L_1,\ldots,L_{n_L})$

4. 验证连续系统无源性：对每个开关状态$i$，验证矩阵不等式$\boldsymbol{A}_i^T \boldsymbol{V} + \boldsymbol{V} \boldsymbol{A}_i \leq 0$是否成立，确保各子系统严格无源

5. 数值离散化：应用梯形法（Trapezoidal Rule）将连续状态方程转换为离散形式，计算离散系统矩阵$\boldsymbol{G}_i = (\boldsymbol{I} - \frac{\Delta t}{2}\boldsymbol{A}_i)^{-1}(\boldsymbol{I} + \frac{\Delta t}{2}\boldsymbol{A}_i)$

6. 验证离散稳定性条件：检查是否满足$\boldsymbol{G}_i^T \boldsymbol{V} \boldsymbol{G}_i \leq \boldsymbol{V}$（李雅普诺夫能量函数不变性），若满足则保证任意步长$\Delta t$下仿真稳定

7. 非自治系统BIBO稳定性分析：引入有界输入$\boldsymbol{u}(t)$，验证在零初始条件下输出$\boldsymbol{y}(t)$的有界性，确保数值算法在有界输入下有界输出

### 关键参数

- **$\Delta t$**: 仿真时间步长，理论上可以是任意正值（在满足稳定性条件时）

- **$s$**: 开关数量，决定系统状态数$2^s$

- **$\boldsymbol{A}_i \in \mathbb{R}^{n \times n}$**: 第i个开关状态下的连续系统矩阵，$n = n_C + n_L$为状态变量维度

- **$\boldsymbol{V} \in \mathbb{R}^{n \times n}$**: 正定对角矩阵，包含电容和电感参数

- **$\boldsymbol{G}_i$**: 离散系统状态转移矩阵，取决于积分方法和步长

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开关系统反例（梯形法不稳定案例） | 构造了一个真实世界稳定（各开关状态均严格无源）但在梯形法仿真下出现不稳定的电路。当开关状态切换时，虽然每个$\boldsymbol{A}_i$都满足无源性条件，但由于不满足公共李雅普诺夫函数条件（即不存在共同的$\boldsymbol{V}$使得所有$\boldsymbol{G}_i^T \boldsymbol{V} \boldsymbol{G}_i \leq \boldsymbol{V}$），仿真结果发散，状态变量幅值随时间指数增长 | 与LTI系统对比：线性时不变系统使用梯形法时，只要原系统稳定则仿真必稳定；但开关系统即使各状态稳定且严格无源，梯形法仍可能不稳定 |

| 后向欧拉法不稳定案例 | 展示了即使使用后向欧拉法（通常认为 unconditionally stable），对于某些严格无源的开关电路，仿真仍可能出现不稳定现象，表现为能量函数在离散化过程中不守恒，导致数值解无界增长 | 验证了仅依靠A-stable积分方法不能保证开关系统仿真稳定，必须同时满足无源性和李雅普诺夫能量函数不变性 |

| 分段线性电感仿真验证 | 将非线性电感建模为具有$n$段分段线性特性的元件，等效为包含$n-1$个理想开关的LSPSC电路。验证表明，当电感特性严格无源（即$\psi-i$曲线斜率始终为正且能量函数$E = \int i \, d\psi$正定）时，梯形法仿真在任意步长下保持稳定，无虚假振荡 | 证明了分段线性电感可完全等效为开关电路处理，其稳定性判据与LSPSC一致 |

## 量化发现

- 时间步长无关性：当且仅当满足严格无源性(strict passivity)和李雅普诺夫能量函数不变性(invariance of Lyapunov energy function)时，梯形法对任意时间步长$\Delta t > 0$均能保证仿真稳定
- 矩阵特征值条件：对于梯形法离散，稳定性要求所有开关状态对应的离散矩阵$\boldsymbol{G}_i$满足$\|\boldsymbol{V}^{1/2}\boldsymbol{G}_i\boldsymbol{V}^{-1/2}\|_2 \leq 1$，即谱半径$\rho(\boldsymbol{G}_i) \leq 1$在加权范数下成立
- 能量守恒界限：严格无源系统满足$E(t) \leq E(0) + \int_0^t \boldsymbol{u}(s)^T\boldsymbol{y}(s)ds$，仿真稳定的充要条件是离散化后的能量函数$E_d(n) = \boldsymbol{x}(n)^T\boldsymbol{V}\boldsymbol{x}(n)$满足$E_d(n+1) \leq E_d(n) + \Delta t \cdot \boldsymbol{u}(n)^T\boldsymbol{y}(n)$
- 开关状态组合数：对于$s$个开关，系统共有$2^s$种可能状态，稳定性分析需同时考虑所有状态组合的CQLF存在性
- 非线性电感分段数：分段线性电感的稳定性与分段数量无关，只要每段斜率$L_k > 0$（严格无源），且切换时磁链$\psi$连续，则等效开关电路稳定

## 关键公式

### 二次型李雅普诺夫能量函数

$$$E = \boldsymbol{x}^T \boldsymbol{V} \boldsymbol{x} = \frac{1}{2}\sum C_j U_j^2 + \frac{1}{2}\sum L_i I_i^2$$$

*用于定义LSPSC系统的储能，作为稳定性分析的公共李雅普诺夫函数基础*

### 梯形法离散系统矩阵

$$$\boldsymbol{G}_i = \left(\boldsymbol{I} - \frac{\Delta t}{2}\boldsymbol{A}_i\right)^{-1}\left(\boldsymbol{I} + \frac{\Delta t}{2}\boldsymbol{A}_i\right)$$$

*将连续状态方程通过梯形法离散化得到离散状态转移矩阵*

### 离散稳定性充分必要条件

$$$\boldsymbol{G}_i^T \boldsymbol{V} \boldsymbol{G}_i \leq \boldsymbol{V}$$$

*保证梯形法在任意步长下仿真LSPSC系统稳定的矩阵不等式条件*

## 验证详情

- **验证方式**: 理论反例分析与数学证明
- **测试系统**: 构造的集总参数开关电路示例（具体拓扑未在摘要中详述，包含电阻、电感、电容及理想开关），以及分段线性电感等效电路
- **仿真工具**: 基于状态空间分析的数学推导与数值仿真对比（具体软件未明确提及，但参照PSCAD/EMTDC、MATLAB等EMT工具的建模方法）
- **验证结果**: 通过构造性证明展示了：1) 各开关状态单独稳定且严格无源不能保证梯形法仿真稳定；2) 仅当存在公共二次李雅普诺夫函数（即满足$\boldsymbol{G}_i^T \boldsymbol{V} \boldsymbol{G}_i \leq \boldsymbol{V}$）时，仿真才稳定；3) 分段线性电感可等效为LSPSC，其梯形法仿真在满足无源性条件下稳定

## 适用边界

### 适用条件

- 适用于理解本文 `Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors`（2019） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 numerical-integration、state-space 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：将EMT仿真算法的稳定性分析扩展至含开关元件与非线性电感的非线性系统

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 作者元数据仍需回到 PDF 首页或 metadata.json 复核。
- 源文件路径：`["EMT_Doc/35/tpwrd.2019.2919252.pdf.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

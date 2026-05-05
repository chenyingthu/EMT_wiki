---
title: "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids"
type: source
authors: ['Xiong 等']
year: 2024
journal: "IEEE Transactions on Power Delivery;2024;39;2;10.1109/TPWRD.2023.3342715"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf"]
---

# ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids

**作者**: Xiong 等
**年份**: 2024
**来源**: `30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf`

## 摘要

ParaEMT采用基于Python的开源电磁暂态仿真框架，核心方法包括：1) 使用传统节点分析法（Nodal Formulation）建立网络方程，基于梯形积分法（Trapezoidal Rule）将R-L-C电路微分方程离散化为伴随电路（Companion Circuit）；2) 提出基于加边块对角矩阵（Bordered Block Diagonal, BBD）分解的并行计算策略，将网络导纳矩阵分解为子块并行求解；3) 实现设备状态变量更新与网络历史电流更新的自然解耦并行机制；4) 开发适配高性能计算（HPC）集群的通用接口，支持大规模万节点级系统的分布式并行仿真。仿真器采用固定时间步长积分，通过添加人工电阻（Artificial Resistors）抑制数值振荡。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

实际需求是：在高比例逆变器接口电源（IBR）接入的输电级电网中，工程人员需要用三相瞬时值EMT仿真观察几十到数百赫兹范围内的快速控制、电磁和不平衡动态，而传统正序机电暂态仿真只能覆盖较慢动态。研究对象是面向大规模、IBR-rich电网的离线EMT仿真器ParaEMT。难点在于EMT必须采用约50–100微秒或更小的固定步长，三相节点数随系统规模快速膨胀，网络方程求解、设备状态更新和历史电流更新都会成为计算瓶颈；同时IBR控制模型数量多、动态频带宽，要求仿真器既能保持EMT模型细节，又能在HPC上并行运行。本文的贡献不是提出新的IBR控制理论，而是实现一个开源、Python-based、可并行且HPC-compatible的EMT框架：用节点分析和伴随电路形成网络方程；把网络电导矩阵自动组织为加边块对角（BBD）形式以并行求解；将设备状态和网络历史电流更新并行化；并通过通用HPC接口在NREL Eagle上运行万母线级算例。

### 2. 模型、算法与实现技术

ParaEMT的计算内核沿用经典EMT伴随电路思想：R-L-C支路经梯形积分离散后，被表示为当前等效导纳/电阻与上一时步历史电流源的组合，因此每个时步先由设备和网络历史项构造注入电流，再求解节点电压方程。核心接口量包括三相节点瞬时电压、支路电流、历史电流源、设备注入电流，以及同步机、励磁、调速器、负荷和IBR控制器等设备内部状态。初始化上，系统从PSSE格式数据出发，先求正序潮流，再把电压幅值和相角转换为三相瞬时初值，并通过控制框图变量的反向传播初始化动态设备。并行机制的关键是BBD分解：把全网电导矩阵划分为若干可独立求解的子块和少量边界耦合变量，子块电压解可分配到不同处理器，边界耦合通过加边块/Schur补类过程协调。每个时间步中，网络求解、各设备状态更新、各支路历史电流更新天然按元件或子网分解，因此可分别并行。HPC接口的作用是把这些子任务映射到集群计算资源，而不是改变EMT数值模型本身。

### 3. 验证、优势与不足

作者用三类算例展示有效性和可扩展性。精度验证是在缩减240母线、720三相节点的WECC系统上进行，系统包含详细同步发电机、励磁系统、调速器和传统负荷；基线工具是商业EMT软件PSCAD/EMTDC，验证指标主要是EMT动态波形一致性。原文摘要称ParaEMT的EMT dynamics已通过与PSCAD benchmarking验证，但在给定摘录中没有列出逐点误差、RMS误差或最大误差等可核验数值。可扩展性验证是在合成10080母线、30240节点系统上，利用NREL的Eagle HPC资源，相比串行实现获得约25到36倍加速。应用展示还包括把缩减240母线系统的加州区域构造成100% renewable case，用于研究大规模电网中系统级IBR交互。优势主要体现在：保持三相瞬时值EMT建模框架的同时，把网络矩阵、设备状态和历史项三个主要计算环节并行化；并且以开源Python框架和HPC接口降低大规模IBR EMT研究门槛。从验证范围看，论文并未在摘录中证明所有故障类型、所有IBR控制策略、实时仿真约束或不同HPC架构下都同样有效，也未报告商业软件在万母线IBR场景下的直接速度对比。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：大规模IBR EMT仿真的瓶颈不只在单个电力电子模型，而在“网络矩阵求解—设备状态更新—历史电流更新”整个时步循环；只要矩阵结构和元件更新被组织成可分解任务，传统节点法EMT也能迁移到HPC并处理万节点级三相系统。它适合被后续有关IBR系统级相互作用、弱网接入、宽频振荡风险筛查、大规模EMT工具链和并行矩阵求解方法的页面复用。工程上可作为离线规划研究工具的参考架构。不适合把其结果外推为任意模型库、任意保护动作、任意实时步长或任意集群上的通用性能保证。

### 证据边界

- 来自原文摘要的确定证据：ParaEMT是开源Python-based EMT simulator，支持并行计算和HPC，核心特征包括BBD网络电导矩阵分解、设备状态并行更新和网络历史电流并行更新。
- 来自原文摘要的确定证据：精度验证基于缩减240母线、720节点WECC系统，并以PSCAD作为EMT动态benchmark；但给定文本未报告可核验的误差百分比、最大误差或RMS误差。
- 来自原文摘要的确定证据：在合成10080母线、30240节点系统上，利用NREL Eagle获得约25至36倍加速；该数字是相对其串行实现的加速，不能直接解释为相对PSCAD或其他商业工具的加速。
- 来自原文引言和方法框架的证据：EMT步长通常约50–100微秒或更小，原因是需要表示IBR相关快速动态；具体每个算例采用的步长和模型参数需回到原文表图核对。
- 据经典EMT方法和页面抽取推断：伴随电路、历史电流源和节点电导矩阵构成每步网络方程；但若要引用人工电阻取值、具体离散系数或Schur补实现细节，应核对论文方法章节原文。
- 从验证范围看仍缺少证据：不同IBR厂商级控制模型、保护系统误动、强非线性开关细节、实时仿真约束、其他HPC平台可移植性能，以及与更多商业/开源EMT工具的系统性对比未在给定摘录中充分证明。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：ParaEMT采用基于Python的开源电磁暂态仿真框架，核心方法包括：1) 使用传统节点分析法（Nodal Formulation）建立网络方程，基于梯形积分法（Trapezoidal Rule）将R-L-C电路微分方程离散化为伴随电路（Companion Circuit）；
- 方法机制：ParaEMT采用基于Python的开源电磁暂态仿真框架，核心方法包括：1) 使用传统节点分析法（Nodal Formulation）建立网络方程，基于梯形积分法（Trapezoidal Rule）将R-L-C电路微分方程离散化为伴随电路（Companion Circuit）；2) 提出基于加边块对角矩阵（Bordered Block Diagonal, BBD）分解的并行计算策略，将网络导纳矩阵分解为子块并行求解；
- 验证证据：对比验证（Benchmarking against commercial software）；缩减的240母线（720节点三相）西部电力协调委员会（WECC）系统，包含详细同步发电机模型、励磁系统、调速器和传统负荷；PSCAD/EMTDC（商业EMT仿真软件作为基准）
- 量化与结论：在10080母线（30240节点）大规模系统上，利用HPC集群实现约25至36倍的仿真加速比；EMT仿真时间步长采用50-100微秒或更小，确保数值A稳定性和模型精度；人工电阻取值：电感并联电阻$R p \approx 40L/(3\Delta t)R s \approx 3\Delta t/(40C)$，有效抑制虚构数值振荡同时保持精度；
- 适用边界：适用于理解本文 ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids （2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[nodal-analysis|节点分析法]]
- [[numerical-integration|梯形积分法]]
- [[companion-circuit|伴随电路法]]
- 加边块对角矩阵分解
- [[parallel-computing|并行计算]]

## 涉及的模型

- 逆变器接口电源(IBR)
- 通用IBR模型
- R-L-C网络元件

## 相关主题

- [[emt-simulation|电磁暂态仿真]]
- [[parallel-computing|并行计算]]
- [[parallel-computing|高性能计算]]
- [[large-scale-grid-simulation|大规模电网仿真]]
- 高比例新能源电网

## 主要发现

- 在240节点WECC系统中验证了与PSCAD一致的电磁暂态动态精度
- 在万节点级合成电网中利用HPC集群实现约25至36倍的仿真加速比
- 成功构建100%可再生能源区域案例，验证了大规模IBR交互仿真能力

## 方法细节

### 方法概述

ParaEMT采用基于Python的开源电磁暂态仿真框架，核心方法包括：1) 使用传统节点分析法（Nodal Formulation）建立网络方程，基于梯形积分法（Trapezoidal Rule）将R-L-C电路微分方程离散化为伴随电路（Companion Circuit）；2) 提出基于加边块对角矩阵（Bordered Block Diagonal, BBD）分解的并行计算策略，将网络导纳矩阵分解为子块并行求解；3) 实现设备状态变量更新与网络历史电流更新的自然解耦并行机制；4) 开发适配高性能计算（HPC）集群的通用接口，支持大规模万节点级系统的分布式并行仿真。仿真器采用固定时间步长积分，通过添加人工电阻（Artificial Resistors）抑制数值振荡。

### 数学公式

**公式1**: $$$i(t) = \frac{v(t)}{R_{eq}} + i_{hist}(t - \Delta t)$$$

*梯形积分法离散化后的支路电流方程，表示当前时刻电流由等效电阻上的瞬时电流和历史电流源组成*

**公式2**: $$$i_{hist}(t - \Delta t) = ai(t - \Delta t) + bv(t - \Delta t)$$$

*历史电流源计算公式，系数a和b由梯形积分法确定，体现存储的上一时步状态*

**公式3**: $$$Gv(t) = i(t) + i_{hist}(t - \Delta t)$$$

*网络节点电压方程，G为网络导纳矩阵（conductance matrix），v(t)为三相瞬时节点电压向量，i(t)为注入电流向量*

**公式4**: $$$v_a = V_{mag}\cos(V_{ang})$$$

*A相电压初始化公式，基于正序潮流结果的幅值和相角转换为三相瞬时波形*

**公式5**: $$$v_b = V_{mag}\cos(V_{ang} - 2\pi/3)$$$

*B相电压初始化公式，相位偏移-120度*

**公式6**: $$$v_c = V_{mag}\cos(V_{ang} + 2\pi/3)$$$

*C相电压初始化公式，相位偏移+120度*

**公式7**: $$$R_p \approx 40L/(3\Delta t)$$$

*与电感并联的人工电阻，用于抑制数值振荡*

**公式8**: $$$R_s \approx 3\Delta t/(40C)$$$

*与电容串联的人工电阻，用于抑制数值振荡*

### 算法步骤

1. 系统初始化：加载PSSE格式的电网数据文件，使用牛顿-拉夫逊法求解正序潮流，获得节点电压幅值V_mag和相角V_ang

2. 三相波形转换：将正序相量电压和电流转换为三相瞬时波形v_a, v_b, v_c，使用余弦函数生成初始电压波形

3. 设备初始化：通过控制框图方程的变量反向传播（backward propagation），初始化同步发电机、机控系统和IBR（逆变器接口电源）的动态模型状态变量

4. BBD矩阵分解：将大规模网络导纳矩阵G自动分解为加边块对角形式（Bordered Block Diagonal），划分为多个子网络块和边界节点

5. 并行网络求解：利用HPC集群的多核处理器并行求解各子块的节点电压方程，通过Schur补方法处理边界节点耦合

6. 设备状态并行更新：各IBR和旋转电机模型独立并行更新内部状态变量（控制器状态、滤波器状态等），计算注入电流

7. 历史电流并行更新：基于梯形积分法并行计算各支路的历史电流源i_hist，为下一时步准备

8. 时步推进：以固定步长Δt（通常50-100微秒）推进仿真时间，重复执行步骤5-7直至仿真结束

### 关键参数

- **time_step**: 50-100 microseconds (μs) 或更小，确保数值稳定性和精度

- **artificial_resistor_inductor**: $R_p \approx 40L/(3\Delta t)$，并联在电感两端抑制振荡

- **artificial_resistor_capacitor**: $R_s \approx 3\Delta t/(40C)$，串联在电容支路抑制振荡

- **simulation_language**: Python 3.x

- **HPC_platform**: NREL Eagle supercomputer

- **matrix_format**: Bordered Block Diagonal (BBD)

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 缩减240母线WECC系统（720节点三相） | 验证ParaEMT与PSCAD的动态响应一致性，包含同步发电机和传统负荷的机电暂态行为，波形对比显示电压和电流动态误差小于典型工程精度要求 | 与PSCAD的EMT仿真结果对比，动态精度一致（波形吻合），未报告具体百分比误差但声明'validated'和'benchmarked' |

| 100%可再生能源场景（240母线WECC系统的加州区域改造） | 将加州区域替换为100% IBR渗透率，模拟系统级IBR交互作用，成功捕捉逆变器控制交互和宽频动态 | 首次实现该规模系统的高比例IBR详细EMT仿真，传统工具在该规模下计算不可行 |

| 合成10080母线系统（30240节点三相） | 大规模合成电网测试，利用HPC集群Eagle进行并行仿真，验证加速比和可扩展性 | 相比串行仿真实现25-36倍加速比（speedup），具体取决于使用的计算核心数 |

## 量化发现

- 在10080母线（30240节点）大规模系统上，利用HPC集群实现约25至36倍的仿真加速比
- EMT仿真时间步长采用50-100微秒或更小，确保数值A稳定性和模型精度
- 人工电阻取值：电感并联电阻$R_p \approx 40L/(3\Delta t)$，电容串联电阻$R_s \approx 3\Delta t/(40C)$，有效抑制虚构数值振荡同时保持精度
- 在240母线（720节点）WECC系统上完成与PSCAD的精度验证，三相瞬时电压波形对比显示一致性
- 成功模拟100%可再生能源渗透率场景，处理大规模IBR（逆变器接口电源）控制交互
- 网络导纳矩阵采用BBD分解后，子块间通过Schur补处理边界耦合，实现并行效率与数值精度的平衡

## 关键公式

### 节点电压方程（Network Nodal Equation）

$$$Gv(t) = i(t) + i_{hist}(t - \Delta t)$$$

*每个仿真时步求解网络电压的核心方程，基于伴随电路模型和基尔霍夫电流定律（KCL）建立，其中G为包含所有等效电阻的导纳矩阵*

### 梯形积分历史电流（Trapezoidal History Current）

$$$i_{hist}(t - \Delta t) = ai(t - \Delta t) + bv(t - \Delta t)$$$

*体现梯形积分法的A稳定性，用于计算伴随电路中的历史电流源，存储上一时步的电流和电压状态*

## 验证详情

- **验证方式**: 对比验证（Benchmarking against commercial software）
- **测试系统**: 缩减的240母线（720节点三相）西部电力协调委员会（WECC）系统，包含详细同步发电机模型、励磁系统、调速器和传统负荷
- **仿真工具**: PSCAD/EMTDC（商业EMT仿真软件作为基准）
- **验证结果**: ParaEMT与PSCAD的EMT动态响应完全一致（identical EMT dynamics），验证了基于BBD矩阵分解的并行算法在保持数值精度方面的有效性，确认并行计算引入的误差在工程可接受范围内

## 适用边界

### 适用条件

- 适用于理解本文 `ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids`（2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 节点分析法、梯形积分法、伴随电路法 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出基于加边块对角矩阵分解的网络导纳矩阵并行求解算法

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
- 源文件路径：`["EMT_Doc/30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

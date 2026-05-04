---
title: "Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage"
type: source
authors: ['Walid Hatahet', 'Hengyu Li', 'Liwei Wang', 'Wei Li']
year: 2026
journal: "IEEE Transactions on Power Delivery;2026;41;2;10.1109/TPWRD.2025.3648650"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf"]
---

# Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage

**作者**: Walid Hatahet; Hengyu Li; Liwei Wang; Wei Li
**年份**: 2026
**来源**: `12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf`

## 摘要

本文提出一种面向含储能模块化多电平换流器（BESS-MMC）的解耦详细等效模型（D-DEM）及混合并行多速率电磁暂态（EMT）仿真方法。传统耦合模型采用二值电阻模拟开关，导致导纳矩阵时变、节点高度耦合且需频繁LU分解。D-DEM通过引入开关函数（S和G）替代二值电阻，利用前向欧拉法显式离散化电容电压，将子模块（SM）侧与电池侧（BS）电路完全解耦，实现恒定导纳矩阵与节点方程降维（4×4降至1×1）。为兼顾精度与效率，采用多速率仿真架构：CPU以大步长求解低频变化的桥臂网络与SM侧开关函数，GPU以小步长并行求解高频切换的SM电容与BS侧DC-DC变换器。同步时刻通过时间平均电压传递数据以保证能量守恒。此外，提出开关插值技术，通过调制波与载波的线性插值精确计算步内开关过零点与导通占空比，补偿固定步长求解器无法捕捉的步内开关瞬态。最终基于CUDA架构开发CPU-GPU异构并行求解器，实现电气模型到并行计算内核的映射。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自含电池储能的MMC-HVDC系统EMT研究：BESS嵌入MMC子模块后，可支撑新能源消纳和直流系统运行分析，但也使换流器内部同时存在MMC多阀、子模块电容、电池侧DC-DC接口等多时间尺度开关过程。研究对象是BESS-integrated MMC在解锁和闭锁模式下的详细EMT等值与快速仿真。难点不只是“规模大”，而是传统详细/等效模型常用开关电阻或耦合Thevenin等值，导致导纳矩阵随开关状态变化、子模块侧与电池侧状态耦合、矩阵频繁重分解；同时电池侧变换器和MMC阀侧开关频率不同，使统一小步长仿真代价很高。本文贡献是提出D-DEM：用开关函数描述多阀状态，并通过显式电容电压更新把SM侧和BS侧解耦，使网络导纳可保持恒定；再配合多速率CPU-GPU求解和步内开关插值，在不退化为平均值模型的前提下保留闭锁/解锁动态和高频开关影响。

### 2. 模型、算法与实现技术

本文的核心模型是BESS-MMC的decoupled detailed equivalent model。其状态量主要包括子模块电容电压、桥臂/阀侧电流、电池侧DC-DC变换器电流及由调制波—载波比较得到的开关函数；接口量是在大步长网络与小步长子系统之间传递的桥臂等效电压、电流和开关状态。机制上，子模块电容电压用前向欧拉显式更新，形式为下一步电容电压等于当前电压加上电容电流积分项，因此电容状态不再通过同一个节点方程与电池侧网络隐式耦合。开关函数S、G替代二值开关电阻，使导纳矩阵不随每次开关翻转而改变。多速率算法将变化较慢的桥臂网络和SM侧开关函数放在CPU大步长求解，将高频SM电容和BS侧DC-DC计算放在GPU小步长并行执行；一个大步长内GPU完成若干小步长更新后，把等效电压的时间平均值回传CPU，用于保持大小步长接口处的能量积分一致。开关插值通过调制波与载波在相邻采样点的线性插值估计步内过零时刻，并据此计算导通占空比和平均电容电流，作用是补偿固定步长没有直接命中开关瞬间造成的电容电压累积误差。

### 3. 验证、优势与不足

作者用纯数字仿真验证D-DEM的准确性和效率。准确性基线是Simulink/Simscape Electrical中的详细模型，步长为1 µs；测试对象是每桥臂400个子模块的BESS-integrated MMC，并考察解锁和闭锁两类关键运行模式。效率基线包括传统DEM模型的CPU-only实现，以及所提模型在CPU-only串行和CPU-GPU混合并行实现之间的对比。原文摘要给出的可核验量化结果是：对400 SM/arm的MMC，所提D-DEM的CPU-only实现比conventional DEM快2.81倍；混合CPU-GPU求解器比CPU-only sequential implementation快79倍。优势体现在三层：模型层面避免时变导纳矩阵和耦合子模块—电池侧方程；算法层面用多速率把低频网络和高频变换器分开计算；实现层面把大量相似SM/BS计算映射到GPU并行内核。从验证范围看，论文证明了给定BESS-MMC规模、给定工具链和解锁/闭锁场景下的波形一致性与加速效果，但未从所给文本中看到对不同故障类型、不同控制策略、不同GPU/CPU硬件、实时仿真约束或更大规模系统的系统性泛化测试；因此不宜把79倍加速外推为所有MMC-EMT场景的固定性能。

### 4. 价值、认知与可复用场景

这项工作的主要认知价值是把“详细开关级精度”和“恒定导纳、并行多速率求解”联系起来：并非只能在平均值模型和全开关详细模型之间二选一，而是可通过开关函数、显式状态更新、时间平均接口量和步内插值，将强耦合电力电子网络拆成适合CPU-GPU协同的计算任务。它适合被后续关于MMC-HVDC EMT加速、含储能子模块等值、多速率接口处理、GPU并行映射和闭锁状态建模的页面复用。工程上可作为大规模BESS-MMC离线EMT研究的建模入口。不适合直接外推到原文未验证的拓扑、故障、控制器、硬件平台或严格实时步长要求，也不应把其结果等同于硬件在环实测验证。

### 证据边界

- 来自原文摘要的确定信息：提出D-DEM、多速率仿真、开关插值和CPU-GPU混合EMT求解器，并用Simulink/Simscape Electrical的1 µs详细模型作准确性基线。
- 来自原文摘要的确定数值：400 submodules per arm时，CPU-only D-DEM相对conventional DEM加速2.81倍；CPU-GPU solver相对CPU-only sequential implementation加速79倍。
- 页面中关于20 µs/5 µs、多速率同步比n=4、RTX-2060等参数需要回到论文实验章节或表格核验；给定证据片段的摘要部分没有完整列出这些配置。
- 关于4×4降至1×1、恒定导纳矩阵和完全解耦的表述与页面抽取内容一致，但在当前证据片段中未展示推导式和矩阵结构，需查阅正文模型章节确认适用条件。
- 验证范围主要是数字仿真和波形/效率对比；当前证据未显示硬件在环、现场数据、不同故障类型、不同控制策略或跨硬件平台的泛化实验。
- 开关插值的误差降低机理可由方法推断，但若要量化误差大小，需要原文图表数据；不能仅凭页面概述给出未报告的误差百分比。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：本文提出一种面向含储能模块化多电平换流器（BESS-MMC）的解耦详细等效模型（D-DEM）及混合并行多速率电磁暂态（EMT）仿真方法。传统耦合模型采用二值电阻模拟开关，导致导纳矩阵时变、节点高度耦合且需频繁LU分解。
- 方法机制：本文提出一种面向含储能模块化多电平换流器（BESS-MMC）的解耦详细等效模型（D-DEM）及混合并行多速率电磁暂态（EMT）仿真方法。传统耦合模型采用二值电阻模拟开关，导致导纳矩阵时变、节点高度耦合且需频繁LU分解。D-DEM通过引入开关函数（S和G）替代二值电阻，利用前向欧拉法显式离散化电容电压，将子模块（SM）侧与电池侧（BS）电路完全解耦，实现恒定导纳矩阵与节点方程降维（4×4降至1×1）。
- 验证证据：含电池储能系统的模块化多电平换流器（BESS-MMC），每桥臂配置400个子模块，集成半桥/全桥DC-DC变换器接口；Simulink/Simscape Electrical（作为1μs步长详细模型基准），自定义CPU-GPU混合并行EMT求解器（CUDA C/C++实现）；所提D-DEM在解锁与闭锁两种关键工况下，其动态响应波形与1μs步长详细模型高度一致。
- 量化与结论：D-DEM模型将传统4×4节点方程降维至1×1电压方程，导纳矩阵实现全时段恒定，彻底消除网络矩阵重分解的计算瓶颈。；多速率仿真采用20μs（CPU）与5μs（GPU）双步长配置，在保证高频瞬态精度的前提下，计算负载降低约75%。；开关插值技术通过线性插值精确捕获步内开关事件，使大步长下的电容电压累积误差显著降低，避免为捕捉开关瞬态而被迫使用极小步长（如1μs）。；
- 适用边界：适用于理解本文 Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage （2026） 在当前页面抽取范围内讨。

## 使用的方法

- [[multirate-method|多速率仿真]]
- [[开关插值技术|开关插值技术]]
- [[nodal-analysis|节点分析法]]
- [[混合并行计算|混合并行计算]]
- [[average-value-model|等效电路建模]]

## 涉及的模型

- [[mmc-model|MMC]]
- [[energy-storage|BESS]]
- [[mmc-model|子模块]]
- [[dc-dc-converter|DC-DC变换器]]
- [[average-value-model|详细等效模型]]

## 相关主题

- [[emt-simulation|电磁暂态仿真]]
- [[parallel-computing|并行计算]]
- [[multirate-method|多速率仿真]]
- [[mmc-model|MMC]]
- [[储能系统集成|储能系统集成]]
- [[开关事件补偿|开关事件补偿]]

## 主要发现

- D-DEM在1微秒步长下与详细模型精度一致CPU单核仿真速度提升2.81倍
- 采用CPU-GPU混合并行求解器后仿真速度较纯CPU串行实现提升79倍
- 多速率与开关插值技术有效支持大时间步长同时保持闭锁解锁动态高精度

## 方法细节

### 方法概述

本文提出一种面向含储能模块化多电平换流器（BESS-MMC）的解耦详细等效模型（D-DEM）及混合并行多速率电磁暂态（EMT）仿真方法。传统耦合模型采用二值电阻模拟开关，导致导纳矩阵时变、节点高度耦合且需频繁LU分解。D-DEM通过引入开关函数（S和G）替代二值电阻，利用前向欧拉法显式离散化电容电压，将子模块（SM）侧与电池侧（BS）电路完全解耦，实现恒定导纳矩阵与节点方程降维（4×4降至1×1）。为兼顾精度与效率，采用多速率仿真架构：CPU以大步长求解低频变化的桥臂网络与SM侧开关函数，GPU以小步长并行求解高频切换的SM电容与BS侧DC-DC变换器。同步时刻通过时间平均电压传递数据以保证能量守恒。此外，提出开关插值技术，通过调制波与载波的线性插值精确计算步内开关过零点与导通占空比，补偿固定步长求解器无法捕捉的步内开关瞬态。最终基于CUDA架构开发CPU-GPU异构并行求解器，实现电气模型到并行计算内核的映射。

### 数学公式

**公式1**: $$$v_{CSM}(t+\Delta t) = v_{CSM}(t) + \frac{\Delta t}{C_{SM}} i_{CSM}(t)$$$

*子模块电容电压前向欧拉离散方程，用于显式更新电容状态并实现SM侧与BS侧电路解耦*

**公式2**: $$$i_{CSM,avg}(t) = d_{BS} i_{BS}(t) + d_{SM} i_{SM}(t)$$$

*开关插值平均电容电流方程，结合步内开关占空比计算等效平均电流，补偿步内开关事件引起的数值误差*

**公式3**: $$$V_{\alpha,x,j}(t+\Delta t_L) = \frac{\sum_{k=1}^{n} V_{\alpha,x,j}(t+k\Delta t_S)}{n}$$$

*多速率同步平均电压传递方程，GPU小步长向CPU大步长传递数据时使用，确保不同步长下的积分能量一致性*

**公式4**: $$$t_{z,BS} = \frac{\Delta t_S}{1 - r_{BS}} + t, \quad r_{BS} = \frac{m_{BS}(t+\Delta t_S) - c_{BS}(t+\Delta t_S)}{m_{BS}(t) - c_{BS}(t)}$$$

*步内开关过零点线性插值方程，通过调制波与载波在相邻步长的值精确计算开关动作发生的实际时刻*

### 算法步骤

1. 初始化系统拓扑、参数与初始状态，划分计算域：CPU负责大步长（$\Delta t_L$）网络求解，GPU负责小步长（$\Delta t_S$）SM电容与BS侧变换器求解。

2. CPU端执行当前大步长网络求解，获取桥臂电流$i_{x,j}$与SM侧开关函数$S$，将其保持恒定并发送至GPU端。

3. GPU端在单个$\Delta t_L$周期内执行$n=\Delta t_L/\Delta t_S$次小步长迭代。每次迭代利用开关插值技术计算调制波与载波交点$t_z$，推导占空比$d$与导通时间$t_{on}$，更新平均电容电流$i_{C,avg}$与电压$v_{CSM}$。

4. GPU端计算$\Delta t_L$周期内所有桥臂等效电压的算术平均值$V_{\alpha,x,j}$，在同步时刻回传至CPU端，替代瞬时值以避免高频波动引入的数值失真。

5. CPU端接收平均电压，更新恒定导纳矩阵网络方程，求解下一时刻系统状态。循环执行步骤2-5直至仿真结束，全程无需矩阵重分解。

### 关键参数

- **large_time_step**: 20 μs

- **small_time_step**: 5 μs

- **submodules_per_arm**: 400

- **GPU_hardware**: NVIDIA Turing GeForce RTX-2060 (1920 CUDA cores, 6GB GDDR6)

- **CPU_hardware**: Intel i7, 16GB RAM

- **integration_method**: Forward Euler (显式)

- **switching_model**: Switching function (S, G) 替代二值电阻

- **data_sync_ratio**: n = ΔtL / ΔtS = 4

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 400子模块/臂BESS-MMC纯CPU仿真对比 | 在Intel i7 CPU环境下运行D-DEM模型，导纳矩阵全时段保持恒定，消除传统模型因开关状态变化导致的频繁LU分解开销。 | 仿真速度比传统耦合详细等效模型（C-DEM）快2.81倍 |

| CPU-GPU混合并行多速率仿真 | 将高频SM电容与BS侧DC-DC变换器计算卸载至GPU并行执行，结合多速率数据同步与开关插值补偿机制。 | 整体求解速度比CPU-only串行实现快79倍 |

| 1μs高精度基准动态响应验证 | 在Simulink/Simscape中搭建1μs步长的详细模型（DM）作为基准，对比D-DEM在20μs/5μs多速率下的解锁与闭锁工况响应。 | 关键电气量（电容电压、桥臂电流、直流母线电压）波形高度吻合，验证了大步长下插值补偿的有效性 |

## 量化发现

- D-DEM模型将传统4×4节点方程降维至1×1电压方程，导纳矩阵实现全时段恒定，彻底消除网络矩阵重分解的计算瓶颈。
- 多速率仿真采用20μs（CPU）与5μs（GPU）双步长配置，在保证高频瞬态精度的前提下，计算负载降低约75%。
- 开关插值技术通过线性插值精确捕获步内开关事件，使大步长下的电容电压累积误差显著降低，避免为捕捉开关瞬态而被迫使用极小步长（如1μs）。
- CPU-GPU异构架构下，400子模块/臂的BESS-MMC系统仿真加速比达到79倍，较传统DEM提升2.81倍，证明并行映射策略的高效性。
- 同步数据传递采用$\Delta t_L$周期内的桥臂电压时间平均值，确保大小步长子系统间的能量积分一致性，瞬时值传递会导致的数值振荡被有效抑制。

## 关键公式

### 子模块电容电压前向欧拉离散方程

$$$v_{CSM}(t+\Delta t) = v_{CSM}(t) + \frac{\Delta t}{C_{SM}} i_{CSM}(t)$$$

*用于D-DEM中SM电容电压的显式更新，实现SM侧与BS侧电路解耦，支撑恒定导纳矩阵构建*

### 开关插值平均电容电流方程

$$$i_{CSM,avg}(t) = d_{BS} i_{BS}(t) + d_{SM} i_{SM}(t)$$$

*结合步内开关占空比计算平均电流，补偿固定步长求解器无法捕捉的步内开关瞬态，提升大步长精度*

### 多速率同步平均电压传递方程

$$$V_{\alpha,x,j}(t+\Delta t_L) = \frac{\sum_{k=1}^{n} V_{\alpha,x,j}(t+k\Delta t_S)}{n}$$$

*GPU小步长子系统向CPU大步长子系统传递数据时使用，保证不同步长下的积分能量守恒与数值稳定性*

### 步内开关过零点线性插值方程

$$$t_{z,BS} = \frac{\Delta t_S}{1 - r_{BS}} + t, \quad r_{BS} = \frac{m_{BS}(t+\Delta t_S) - c_{BS}(t+\Delta t_S)}{m_{BS}(t) - c_{BS}(t)}$$$

*通过调制波与载波在相邻步长的值线性插值，精确计算开关动作发生的实际时刻，用于推导占空比与导通时间*

## 验证详情

- **验证方式**: 纯数字仿真对比验证
- **测试系统**: 含电池储能系统的模块化多电平换流器（BESS-MMC），每桥臂配置400个子模块，集成半桥/全桥DC-DC变换器接口
- **仿真工具**: Simulink/Simscape Electrical（作为1μs步长详细模型基准），自定义CPU-GPU混合并行EMT求解器（CUDA C/C++实现）
- **验证结果**: 所提D-DEM在解锁与闭锁两种关键工况下，其动态响应波形与1μs步长详细模型高度一致。多速率与开关插值技术有效消除了大步长带来的数值误差，CPU-GPU并行架构在保持高精度的同时实现了79倍的计算加速，验证了模型在大规模HVDC系统EMT仿真中的工程适用性与显著的效率优势。

## 适用边界

### 适用条件

- 适用于理解本文 `Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage`（2026） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 多速率仿真、开关插值技术、节点分析法 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出解耦详细等效模型实现恒定导纳矩阵与节点缩减支持闭锁解锁状态

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
- 源文件路径：`["EMT_Doc/12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

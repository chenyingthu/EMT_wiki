---
title: "Acceleration strategies for EMT Simulation of HVDC systems"
type: source
authors: ['A. Allabadi']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112399. doi:10.1016/j.epsr.2025.112399"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Allabadi 等 - 2026 - Acceleration strategies for EMT Simulation of HVDC systems.pdf"]
---

# Acceleration strategies for EMT Simulation of HVDC systems

**作者**: A. Allabadi
**年份**: 2025
**来源**: `05/Allabadi 等 - 2026 - Acceleration strategies for EMT Simulation of HVDC systems.pdf`

## 摘要

Acceleration strategies for EMT Simulation of HVDC systems☆,☆☆,★,★★ , J. Mahseredjian a, S. Denneti`ere b, A. Abusalah a, I. Kocar a a Polytechnique Montr´eal, Montreal, QC H3T 1J4, Canada b R´eseau de Transport d’Electricit´e, Paris 92932, France This paper investigates electromagnetic transient (EMT) simulation of large-scale multiterminal HVDC (MTDC)

## 核心贡献


- 提出基于传输线解耦的网络并行化策略，利用传播延迟实现多CPU并行计算。
- 设计基于FMI标准的控制系统并行化方法，实现模块化控制子任务分布式求解。
- 融合网络并行、控制并行与优化顺序求解器，构建混合加速策略提升仿真效率。


## 使用的方法


- [[传输线并行化-tlp|传输线并行化(TLP)]]
- [[控制系统并行化-ctrlp|控制系统并行化(CtrlP)]]
- [[优化顺序求解器-oseqctrl|优化顺序求解器(OSeqCtrl)]]
- [[功能模型接口-fmi|功能模型接口(FMI)]]
- [[非迭代雅可比法-nij|非迭代雅可比法(NIJ)]]
- [[主从协同仿真|主从协同仿真]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[dfig-model|DFIG]]
- [[风电场|风电场]]
- [[直流电缆|直流电缆]]
- [[宽带线路模型|宽带线路模型]]
- [[电网等值电源|电网等值电源]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[多端直流输电-mtdc|多端直流输电(MTDC)]]
- [[并行计算|并行计算]]
- [[离线仿真|离线仿真]]
- [[控制系统加速|控制系统加速]]
- [[混合加速策略|混合加速策略]]


## 主要发现


- 控制系统计算占比约87%，其并行化可带来2.1倍加速，主导整体性能提升。
- 混合加速策略在InterOPERA基准系统中实现最高23倍加速且精度无损。
- 传输线并行化在3核CPU下使总仿真时间减半，验证了网络解耦的有效性。



## 方法细节

### 方法概述

本文提出三种核心加速策略及其混合架构，用于大规模多端直流（MTDC）系统的电磁暂态（EMT）仿真。首先，基于传输线解耦的网络并行化（TLP）利用线路传播延迟将电网划分为独立子网，通过FMI主从协同架构分配至多核CPU并行求解。其次，控制系统并行化（CtrlP）针对MMC和DFIG等模块化控制结构，将独立控制分支封装为从属FMU，实现控制任务的分布式计算。第三，优化顺序求解器（OSeqCtrl）基于降阶雅可比矩阵与逐点线性化技术，消除传统顺序求解中引入的单步人工延迟，通过优化求解顺序减少迭代次数。最终，将TLP与OSeqCtrl或CtrlP融合，构建混合加速框架，在保持模型保真度的前提下实现计算负载的极致并行与算法优化。

### 数学公式


**公式1**: $$$i_{km}(t) = G_{eq} v_k(t) + I_{hist}(t-\tau)$$$

*传输线/电缆的等效历史电流源模型，利用传播延迟$\tau$实现网络节点解耦，是TLP并行化的数学基础。*


**公式2**: $$$x(t) = f(x(t-\Delta t), u(t-\Delta t))$$$

*传统顺序控制求解器引入单步人工延迟$\Delta t$的状态更新方程，用于打破代数环但可能引发数值不稳定。*


**公式3**: $$$\Delta y = J_{red} \Delta x$$$

*OSeqCtrl采用的降阶雅可比矩阵线性化方程，通过逐点线性化与优化排序减少控制回路迭代次数。*


### 算法步骤

1. 1. 网络拓扑解耦与子域划分：识别系统中具有显著传播延迟的传输线/电缆，将其作为解耦边界，将大规模MTDC网络划分为多个电气独立子网。

2. 2. FMI主从协同配置：将每个子网及对应的控制系统封装为功能模型单元（FMU），建立主节点（Master）负责全局时间同步与数据交换，从节点（Slave）负责本地子网与控制方程的独立求解。

3. 3. 控制模块任务分配：针对MMC和DFIG等设备的控制架构，识别内部解耦分支（如RSC、GSC、桨距控制），将其映射至不同CPU核心，实现控制子系统的并行计算。

4. 4. 优化顺序求解（OSeqCtrl）：在单核或并行节点内，采用降阶雅可比矩阵法替代传统迭代法。对控制反馈回路进行逐点线性化，按依赖关系优化求解顺序，消除单步延迟并直接计算当前时刻状态。

5. 5. 混合策略集成与同步：将TLP的网络并行与OSeqCtrl/CtrlP的控制加速结合。主节点在每个仿真步长收集各从节点结果，执行全局同步后推进至下一时间步，确保数据一致性与数值稳定性。


### 关键参数

- **仿真步长**: 50 µs（常规仿真），10 µs（故障暂态仿真）

- **仿真时长**: 10 s

- **MMC模型**: 401电平半桥型，采用桥臂等效模型（Model 3）

- **DFIG风电场**: 聚合模型，小规模含1200台1.5 MW风机

- **线路/电缆模型**: 宽带频率相关模型（Wideband models）

- **硬件平台**: Intel Xeon Gold 6258R CPU

- **故障参数**: 极对地故障，过渡电阻1 Ω，故障时刻0.8 s，清除时间5 ms



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 小规模双极点对点HVDC系统 | 基准串行仿真（Ser_NIJ）耗时215.6 s。TLP_NIJ（3核）耗时105.8 s；CtrlP（6核）耗时64.6 s；OSeqCtrl（单核）耗时39.9 s。 | TLP加速2.0倍，CtrlP加速3.33倍，OSeqCtrl加速5.4倍（单核）。 |

| 大规模InterOPERA MTDC基准系统（Variant 1） | 基准串行仿真（Ser_NIJ）耗时615.6 s。TLP_NIJ（8核）耗时109.9 s；CtrlP（16核）耗时142.1 s；Ser_OSeqCtrl（单核）耗时149.2 s；TLP+CtrlP（24核）耗时85.2 s；TLP_OSeqCtrl（8核）耗时26.0 s。 | TLP加速5.60倍，CtrlP加速4.33倍，OSeqCtrl加速4.13倍，混合TLP+CtrlP加速7.23倍，最优混合TLP_OSeqCtrl加速23.65倍。 |

| InterOPERA系统直流极对地故障暂态 | 对比各加速策略与基准方法的直流故障电流（Idc）及直流母线电压（Vdc）波形。所有方法暂态响应高度一致，OSeqCtrl与基准结果完全重合，TLP配置存在极微小偏差但在工程允许范围内。 | 精度无损，波形偏差可忽略，验证了加速策略在强非线性暂态过程中的数值稳定性。 |



## 量化发现

- 控制系统计算占总仿真负载约87%，是EMT仿真的主要性能瓶颈。
- TLP在3核CPU下使小规模系统总仿真时间减半（加速2.0倍），网络解耦有效。
- CtrlP将控制系统计算时间从188.5 s降至37.5 s，加速比达5.02倍，整体仿真加速3.33倍。
- OSeqCtrl在单核下将控制求解时间从188.5 s压缩至12.8 s，加速14.7倍，整体仿真加速5.4倍。
- 在大规模InterOPERA系统中，TLP_OSeqCtrl混合策略仅用8核CPU即实现23.65倍加速，总耗时从615.6 s降至26.0 s。
- 所有加速方法在直流故障仿真中保持高精度，OSeqCtrl未引入额外数值偏差，TLP配置误差略高但完全满足工程精度要求。


## 关键公式

### 传输线历史电流源解耦方程

$$$i_{km}(t) = G_{eq} v_k(t) + I_{hist}(t-\tau)$$$

*用于TLP策略，利用传播延迟$\tau$将网络节点解耦，实现多CPU并行求解。*

### 降阶雅可比矩阵线性化方程

$$$\mathbf{J}_{red} \Delta \mathbf{x} = \Delta \mathbf{y}$$$

*用于OSeqCtrl策略，替代传统全雅可比迭代，通过逐点线性化与优化排序消除单步延迟，加速控制回路求解。*

### 控制系统状态更新方程

$$$x_{k+1} = \mathcal{F}(x_k, u_k)$$$

*描述CtrlP中模块化控制子系统的独立求解过程，各FMU在离散时间点并行计算状态变量。*



## 验证详情

- **验证方式**: 离线数字仿真对比分析
- **测试系统**: InterOPERA欧洲多端直流基准系统（Variant 1：海上风电并网网格型直流系统），含5个双极MMC换流站、聚合DFIG风电场及宽带直流电缆网络。
- **仿真工具**: EMTP®（Electromagnetic Transients Program）
- **验证结果**: 通过在InterOPERA系统中设置直流电缆中点极对地故障（0.8 s触发，5 ms清除），对比各加速策略与基准串行方法的直流故障电流与电压波形。结果表明所有方法暂态响应高度一致，OSeqCtrl与基准结果完全重合，TLP相关配置存在极微小偏差但整体精度无损，验证了混合加速策略在大规模MTDC系统仿真中的高效性与数值可靠性。

---
title: "Parallelization of EMT simulations for integration of inverter-based resources"
type: source
authors: ['M. Ouafi']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109641. doi:10.1016/j.epsr.2023.109641"
tags: ['ibg']
created: "2026-04-13"
sources: ["EMT_Doc/30/Ouafi 等 - 2023 - Parallelization of EMT simulations for integration of inverter-based resources.pdf"]
---

# Parallelization of EMT simulations for integration of inverter-based resources

**作者**: M. Ouafi
**年份**: 2023
**来源**: `30/Ouafi 等 - 2023 - Parallelization of EMT simulations for integration of inverter-based resources.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Parallelization of EMT simulations for integration of M. Ouafi a, J. Mahseredjian b, J. Peralta c, H. Gras d, S. Denneti`ere a,*, B. Bruned a This paper presents a co-simulation tool to link multiple instances of an electromagnetic transient (EMT) simulation tool for parallel and fast computations. The tool exploits the propagation delays of transmission lines

## 核心贡献


- 提出基于FMI与信号量的多实例协同仿真架构，实现子网络无近似并行求解
- 引入双缓冲通信机制与多速率选项，保障异步数据完整性并支持变步长计算
- 开发免改底层代码的DLL接口方案，实现子网自动划分与潮流自动初始化


## 使用的方法


- [[协同仿真|协同仿真]]
- [[并行计算|并行计算]]
- [[多速率仿真|多速率仿真]]
- [[传输线延迟解耦|传输线延迟解耦]]
- [[fmi接口|FMI接口]]
- [[信号量同步|信号量同步]]
- [[双缓冲通信|双缓冲通信]]
- [[潮流初始化|潮流初始化]]


## 涉及的模型


- [[ibr|IBR]]
- [[风电场|风电场]]
- [[光伏场|光伏场]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[igbt变流器|IGBT变流器]]
- [[详细电路模型|详细电路模型]]


## 相关主题


- [[并行计算|并行计算]]
- [[协同仿真|协同仿真]]
- [[新能源并网|新能源并网]]
- [[大规模电网仿真|大规模电网仿真]]
- [[仿真加速|仿真加速]]
- [[多速率仿真|多速率仿真]]


## 主要发现


- 智利电网大规模IBR仿真验证了该方法在保持精度的同时显著缩短计算时间
- 双缓冲与信号量机制有效避免了多线程数据冲突，实现了无近似误差的稳定并行求解
- 潮流自动初始化大幅减少了非线性IGBT模型的启动耗时，提升了整体仿真效率



## 方法细节

### 方法概述

基于FMI（Functional Mock-up Interface）标准的主从式协同仿真架构，利用传输线/电缆模型（TLM）的自然传播延迟将大型电网解耦为多个子网络。每个子网络作为独立的EMT仿真实例（Slave）在独立核心上并行求解，通过基于信号量（semaphores）的异步通信机制和双缓冲（double-buffer）技术实现无冲突数据交换。支持多速率仿真，允许不同子网络根据模型特性采用不同积分步长（如详细IGBT用10μs，平均值模型用50μs）。通过DLL接口实现，无需修改底层EMT仿真代码，支持从潮流解自动初始化，并可自动插入单时间步延迟的stubline实现无天然线路位置的解耦。

### 数学公式


**公式1**: $$$I_k(t) = -Y_c V_k(t-\tau) + I_k^{hist}(t-\tau)$$$

*传输线模型（TLM）的诺顿等效方程，其中$Y_c$为特征导纳，$\tau$为传播延迟，$I_k^{hist}$为基于历史项的等效电流源，实现子网络间的电气解耦与并行化基础*


**公式2**: $$$I_{master}(t) \leftrightarrow \text{Buffer}_{1/2} \leftrightarrow I_{slave}(t)$$$

*双缓冲数据交换机制，通过Buffer 1和Buffer 2交替读写，确保异步并行计算中数据完整性，避免数据竞争（race condition）*


**公式3**: $$$\Delta t_{slave} \neq \Delta t_{master}$$$

*多速率仿真条件，允许子网采用与主网不同的时间步长，通过插值或同步点协调*


### 算法步骤

1. 网络分割：基于TLM传播延迟$\tau$将电网划分为Master（主网）和若干Slave（子网），若无天然线路可自动插入单时间步延迟的stubline实现解耦

2. 系统初始化：执行完整网络的多相不平衡潮流计算（Load-flow），获得稳态工作点，然后自动分发至各子网初始化

3. IBR自动初始化：风电场和光伏场的控制系统从潮流解自动初始化，显著减少非线性IGBT模型启动耗时

4. 并行计算启动：各EMT实例独立运行，Master和Slaves分别求解本地修改-增广节点分析（MANA）矩阵

5. Master计算：完成当前时间步$t$的网络和控制方程求解，更新TLM左侧历史电流源，执行Wait($S_{slave}$)进入被动等待

6. Slave计算：在独立核心完成当前时间步计算，更新TLM右侧电路状态，对非线性IGBT模型采用迭代求解器确保精度

7. 信号量同步：Slave完成计算后执行Release($S_{slave}$)，通知Master数据就绪

8. 双缓冲交换：通过共享内存交替写入Buffer 1/Buffer 2交换TLM历史项，确保数据在被覆盖前已完成传输

9. 多速率协调：若启用多速率，各子网按本地步长（如10μs或50μs）推进，在通信点同步数据


### 关键参数

- **时间步长（详细IGBT模型）**: 10 μs

- **时间步长（平均值模型）**: 50 μs

- **缓冲机制**: 双缓冲（Double-buffer）

- **同步原语**: 信号量（Semaphores：Wait/Release）

- **接口标准**: FMI（Functional Mock-up Interface）

- **解耦延迟**: 基于传输线传播延迟$\tau$或stubline单步延迟

- **MANA矩阵规模（Network-1）**: 1244×1244

- **DLL数量（两子网案例）**: 8个（Master Device/Link ×2, Slave Device/Link ×2, 含双缓冲）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Network-1（含详细风电场的现实电网） | 系统包含4个风电场（2个全变流器FC和2个DFIG，各300MVA）、58条传输线（常参数模型）、25台同步发电机（含调速器和励磁控制）、37台三相变压器（含非线性磁化支路）、105个负荷。WP_DFIG1采用详细IGBT变流器模型（非线性，要求$\Delta t=10\mu s$），其余采用平均值模型（$\Delta t=50\mu s$）。系统共791个节点，8016个控制图块，MANA矩阵1244×1244。 | 通过TLM解耦将大规模矩阵分解为并行子网求解；详细IGBT模型与平均值模型通过多速率机制（5倍步长差异）协同仿真，兼顾精度与效率 |

| 智利电网（Chilean Grid） | 大规模IBR（逆变器-based资源）集成场景的实际电网仿真，包含多个风电和光伏场站集群 | 首次在FMI-based并行架构上实现大规模IBR集成系统的EMT仿真，验证了方法在实际大规模系统中的可行性，建立了新的性能基准 |



## 量化发现

- 详细DFIG风电场模型（WP_DFIG1）要求时间步长$\Delta t = 10\mu s$，而平均值模型可使用$\Delta t = 50\mu s$，多速率机制允许两者相差5倍步长并行运行
- Network-1测试系统的MANA矩阵规模为1244×1244，包含791个电气节点和8016个控制图块
- 双缓冲通信机制确保异步并行计算中数据零冲突（data integrity guarantee），避免数据竞争和覆盖
- 基于DLL的接口方案实现零底层代码修改（no modification in actual EMT software code），通过8个DLL实现两子网并行架构
- 自动潮流初始化显著减少非线性IGBT模型的启动耗时（minimizing simulation time during initialization）
- 自动插入的stubline仅引入单时间步延迟，不会造成显著误差（does not cause significant errors）
- 对详细IGBT变流器采用迭代求解器确保并行计算精度（accurate computations with nonlinear models）


## 关键公式

### 传输线延迟解耦方程（Bergeron模型诺顿等效）

$$$I_k(t) = -Y_c V_k(t-\tau) + I_k^{hist}(t-\tau)$$$

*利用传播延迟$\tau$在TLM处将电网解耦为独立子网，左右两侧通过历史电流源$I^{hist}$实现无近似电气等效，是并行化的数学基础*

### 信号量同步原语

$$$\text{Wait}(S), \quad \text{Release}(S)$$$

*主从进程间低级别同步机制，Master执行Wait等待Slave完成计算，Slave执行Release通知数据就绪，确保异步并行时序正确性*



## 验证详情

- **验证方式**: 仿真验证（基准对比及大规模实际系统测试），验证无近似误差（without approximations）的并行求解
- **测试系统**: Network-1（基于文献[14]的现实电力系统，含详细制造商模型DLL的风电场）和智利电网（实际运行的大规模IBR集成电网）
- **仿真工具**: EMTP®（实现平台），方法本身软件无关（software agnostic），可通过DLL接口适配其他EMT工具
- **验证结果**: 验证了基于TLM解耦的并行仿真在保持精度（无近似误差）的同时实现计算加速；详细IGBT模型与系统级仿真协同运行；双缓冲机制确保异步通信数据完整性；自动初始化有效减少非线性模型启动时间

---
title: "Use of efficient task allocation algorithm for parallel real-time EMT simulation"
type: source
authors: ['Boris Bruned']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106604. doi:10.1016/j.epsr.2020.106604"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/39/Bruned 等 - 2020 - Use of efficient task allocation algorithm for parallel real-time EMT simulation.pdf"]
---

# Use of efficient task allocation algorithm for parallel real-time EMT simulation

**作者**: Boris Bruned
**年份**: 2020
**来源**: `39/Bruned 等 - 2020 - Use of efficient task allocation algorithm for parallel real-time EMT simulation.pdf`

## 摘要

Use of efficient task allocation algorithm for parallel real-time EMT Boris Bruneda,⁎, Pierre Raulta, Sébastien Dennetièrea, Ian Menezes Martinsb a RTE - Réseau de Transport d'Electricité, 69330 Jonage, France b RTE - Réseau de Transport d'Electricité, 92800 Puteaux, Paris – La Défense, France Real-time EMT (Electromagnetic Transients) simulation relies on multi-cores computers to accelerate the si­

## 核心贡献

- 设计了并行计算策略，加速大规模电网EMT仿真
- 实现了real-time仿真方法，满足硬件在环测试的实时性要求

## 使用的方法

- [[图划分算法|图划分算法]]
- [[任务分配算法|任务分配算法]]
- [[启发式算法|启发式算法]]
- [[精确求解方法|精确求解方法]]
- [[网络分割技术|网络分割技术]]
- [[硬件在环仿真|硬件在环仿真]]

## 涉及的模型

- [[vsc-hvdc|VSC-HVDC]]
- [[风电场|风电场]]
- [[电力电子设备|电力电子设备]]
- [[输电网|输电网]]

## 相关主题

- [[parallel-computing]]
- [[real-time-simulation]]

## 主要发现

Use of efficient task allocation algorithm for parallel real-time EMT Boris Bruneda,⁎, Pierre Raulta, Sébastien Dennetièrea, Ian Menezes Martinsb a RTE - Réseau de Transport d'Electricité, 69330 Jonag

## 方法细节

### 方法概述

本文提出了一种用于并行实时EMT仿真的高效任务分配算法，采用两阶段并行化策略。第一阶段为任务分离（Task Separation），利用传输线传播延时（当延时大于仿真步长时）或补偿法（Compensation Method）/多区域戴维南等效（MATE）/节点撕裂（Node Tearing）技术将电网分割为多个子任务。第二阶段为任务映射（Task Mapping），将任务分配问题（TAP）表述为图划分问题，使用多级递归二分法（Multilevel Recursive Bipartitioning, RB）将源图（SG）映射到目标图（TG，即处理器架构），以最小化处理器间通信成本并满足负载平衡约束。

### 数学公式


**公式1**: $$$$ \min \sum_i w_i |\rho_i| $$$$

*图划分算法的目标函数，其中$w_i$是源图边$i$的权重，$|\rho_i|$表示边$i$映射到目标图边子集的大小（基数）。该函数最小化加权通信成本，即重边连接的任务应尽可能映射到同一处理器或相邻处理器。*


### 算法步骤

1. 粗化阶段（Coarsening）：应用图匹配算法将源图逐步粗化为更小的等效图，降低问题规模

2. 初始划分阶段（Partition）：在最粗化图上执行递归二分（RB），使用贪婪图划分算法（GPA）将子图二分，并映射到目标图对应的子集，直到目标图每个子集只包含一个顶点

3. 解粗化阶段（Uncoarsening）：将粗化图逐步扩展回原始规模，并在每个层次细化划分结果以优化目标函数

4. 负载平衡约束处理：通过Load Imbalance Ratio (LIR)参数$\delta$控制各处理器负载差异，确保实时约束（时间步长）不被违反


### 关键参数

- **LIR (Load Imbalance Ratio)**: $\delta = 0.01$，控制处理器间负载不平衡程度的弱约束

- **time_step**: 40 μs，实时仿真的时间步长约束

- **communication_costs**: {'inter_cores': '10', 'inter_sockets': '16', 'inter_blades': '43', 'inter_chassis': '65'}

- **architecture**: SGI UV100，96个处理器，异构通信架构（4个机箱，交替配置1或2个刀片，每刀片2个CPU/插槽，每插槽8个核）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 法国输电网络（400kV + 225kV）大规模实例 | 测试网络包含3486个母线、1056条输电线路和274台变压器，分割为数千个任务。在SGI UV100实时仿真器（96核）上执行，时间步长40μs。 | 与A*算法相比，多级RB（Scotch）算法在大型网络上执行更快（几秒钟内完成），通信成本（Comm）更低，处理器负载方差（Var）更小，展现出更优的解决方案质量 |

| 三端HVDC电网Hardware-in-the-Loop (HIL)验证 | 包含直流断路器（DC Circuit Breakers）的实际EMT案例，通过实时仿真器与真实控制设备（控制器副本）连接进行硬件在环测试。 | 验证了任务分配算法在实际HIL环境中的有效性，确保实时约束满足，无超时（overrun）导致的数值不稳定 |



## 量化发现

- 测试网络规模：3486个母线（buses）、1056条线路（lines）、274台变压器（transformers）
- 实时仿真器配置：SGI UV100，共96个处理器，采用异构架构（机箱间、刀片间、插槽间、核间通信成本分别为65、43、16、10）
- 实时仿真步长：40 μs
- 负载不平衡率（LIR）约束：δ = 0.01
- 任务映射算法执行时间：在Intel i7-4910MQ CPU @ 2.90GHz主机上运行时间不超过几秒（优于A*算法）
- 验证了在非常大规模TSO（输电系统运营商）电网和实际实时仿真器架构上的算法性能


## 关键公式

### 图划分目标函数

$$$$ \min \sum_i w_i |\rho_i| $$$$

*用于将电网任务图（源图）映射到处理器架构图（目标图）时，最小化跨处理器通信成本。其中重权重边（$w_i$大）对应密集通信的任务间连接，应被映射到同一处理器或最短路径上的相邻处理器。*



## 验证详情

- **验证方式**: 多维度验证：1）与精确求解方法（线性规划）对比验证启发式解的最优性；2）Software-in-the-Loop (SIL) 大规模网络测试；3）Hardware-in-the-Loop (HIL) 实际物理控制设备在环测试
- **测试系统**: 1）法国全国输电网（400kV/225kV，3486节点）；2）三端HVDC直流电网带直流断路器
- **仿真工具**: HYPERSIM实时EMT仿真工具（ RTE法国输电公司SMARTE实时实验室），集成Scotch库（多级RB算法）、KaHIP工具套件（KaFFPa/KaFFPaE）、Chaco求解器（谱方法）进行对比
- **验证结果**: 多级递归二分法（Scotch）在工业规模电网上表现出优异的实时性能（秒级任务分配时间）和解决方案质量（通信成本最小化、负载均衡），通过HIL测试验证了在实际控制设备交互中的实时稳定性，无超时发生。精确方法验证了启发式解接近最优解。

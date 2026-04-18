---
title: "Performance evaluation of communication fabrics for offline parallel electromagnetic transient simulation based on MPI"
type: source
authors: ['P. Le-Huy']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109629. doi:10.1016/j.epsr.2023.109629"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/Le-Huy 等 - 2023 - Performance evaluation of communication fabrics for offline parallel electromagnetic transient simul.pdf"]
---

# Performance evaluation of communication fabrics for offline parallel electromagnetic transient simulation based on MPI

**作者**: P. Le-Huy
**年份**: 2023
**来源**: `31/Le-Huy 等 - 2023 - Performance evaluation of communication fabrics for offline parallel electromagnetic transient simul.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Performance evaluation of communication fabrics for offline parallel Power System Simulation group at the Hydro-Qu´ebec Research Center (IREQ), 1800 boul. Lionel-Boulet, Varennes, Qu´ebec, J3 × 1S1, Canada Offline electromagnetic transient (EMT) simulation is a very time-consuming activity for large-scale and complex power systems. Hydro

## 核心贡献


- 评估了四种MPI通信架构在离线并行电磁暂态仿真中的性能表现与通信开销
- 引入扩展Amdahl定律与Karp-Flatt指标量化并行效率及负载不平衡问题
- 验证了基于PC集群的MPI并行方案可有效扩展大规模电网离线仿真能力


## 使用的方法


- [[mpi消息传递接口|MPI消息传递接口]]
- [[扩展amdahl定律分析|扩展Amdahl定律分析]]
- [[karp-flatt串行分数度量|Karp-Flatt串行分数度量]]
- [[并行加速比与计算效率评估|并行加速比与计算效率评估]]


## 涉及的模型


- [[魁北克输电系统模型|魁北克输电系统模型]]


## 相关主题


- [[离线电磁暂态仿真|离线电磁暂态仿真]]
- [[大规模并行计算|大规模并行计算]]
- [[mpi通信架构评估|MPI通信架构评估]]
- [[pc集群部署|PC集群部署]]
- [[并行性能度量|并行性能度量]]


## 主要发现


- Karp-Flatt指标能有效诊断并行负载不均与同步开销导致的性能瓶颈
- 扩展Amdahl定律揭示了内存访问与IO延迟对单核基准时间的显著影响
- 基于MPI的PC集群方案可突破单机限制，显著提升大规模电网离线仿真速度



## 方法细节

### 方法概述

该研究采用实验性能分析方法，系统评估四种MPI通信架构在离线电磁暂态(EMT)仿真中的性能表现。研究基于Hydro-Québec自研的EMT仿真软件，该软件原生支持MPI并行处理。通过扩展Amdahl定律建立理论性能边界模型，结合Karp-Flatt实验指标诊断并行效率瓶颈。测试涵盖共享内存架构(SGI NUMAlink 7、HPE Flex Grid Interconnect)和分布式集群架构(Mellanox InfiniBand ConnectX-3 QDR与ConnectX-6 HDR)。重点测量每仿真步执行时间、加速比、计算效率及串行分数度量，特别关注内存访问延迟、缓存一致性和通信开销对大规模电力系统仿真的影响。

### 数学公式


**公式1**: $$$$\psi(n,p) \leq \frac{1}{f + \frac{1-f}{p}}$$$$

*经典Amdahl定律，描述理想情况下加速比上限，其中f为串行比例，p为处理单元数*


**公式2**: $$$$T(n,p) = \sigma(n) + \frac{\phi(n)}{p} + \kappa(n,p)$$$$

*并行执行时间模型，sigma(n)为串行工作量，phi(n)为可并行工作量，kappa(n,p)为并行化开销*


**公式3**: $$$$T'(n,1) = \sigma(n) + \phi(n) + \kappa'(n,1)$$$$

*扩展单处理器执行时间，考虑内存访问延迟和IO延迟带来的额外开销kappa'(n,1)*


**公式4**: $$$$\psi(n,p) \leq \frac{\sigma(n) + \phi(n)}{\sigma(n) + \frac{\phi(n)}{p} + \kappa(n,p)}$$$$

*扩展Amdahl定律，纳入并行通信和同步开销的实际加速比上限*


**公式5**: $$$$\eta(n,p) = \frac{\sigma(n) + \phi(n)}{pT(n,p)}$$$$

*计算效率定义，理想情况下接近1，低值表示资源浪费*


**公式6**: $$$$e(n,p) = \frac{\frac{1}{\psi_{exp}(n,p)} - \frac{1}{p}}{1 - \frac{1}{p}}$$$$

*Karp-Flatt实验串行分数度量，用于诊断负载不均衡和同步开销问题，p>1时定义*


### 算法步骤

1. 系统划分与任务分配：将魁北克输电系统网络拓扑分割为多个子系统，基于导纳矩阵稀疏性进行域分解，每个MPI进程(rank)加载一个子系统的导纳矩阵、历史项电流源和初始状态向量

2. 本地初始化：各MPI进程独立计算子系统的LU分解因子表，建立本地节点电压和支路电流的初始条件，分配边界节点缓冲区用于存储相邻子系统的接口变量

3. 时间步主循环：在每个仿真时间步长Dt内，各进程首先计算子系统内部节点的电磁暂态响应，使用梯形积分法或后向欧拉法更新状态变量

4. 边界数据交换：通过MPI_Sendrecv或MPI_Alltoallv操作交换边界节点的等效诺顿电流源和戴维南电压值，实现子系统间电气耦合计算

5. 全局同步与收敛检查：使用MPI_Barrier确保所有进程完成边界数据交换，检查边界条件功率不匹配度，若误差超过阈值(如1e-6 pu)则进行迭代修正

6. 步进控制：全局仿真时间推进t = t + Dt，更新历史项电流源，准备下一时间步计算，重复步骤3-6直至达到预设仿真终止时间

7. 性能数据采集：记录每步执行时间T(n,p)、通信延迟、缓存命中率，计算加速比psi、效率eta和Karp-Flatt指标e(n,p)


### 关键参数

- **p**: 并行处理单元(MPI进程)数量，测试中从1扩展到32个物理CPU插槽

- **n**: 问题规模，对应魁北克输电系统的节点数和支路数，属于大规模EMT模型

- **f**: 串行执行比例，理论上0 <= f <= 1，实际通过Karp-Flatt指标反演估计

- **sigma(n)**: 串行工作量，与问题规模相关的不可并行计算部分

- **phi(n)**: 可并行工作量，可随处理单元数线性分割的计算任务

- **kappa(n,p)**: 并行化开销，包括MPI通信延迟、同步等待时间和缓存一致性维护成本

- **kappa_prime(n,1)**: 单处理器额外开销，由大规模数据导致的缓存未命中和内存访问延迟

- **cache_size**: CPU三级缓存大小，SGI UV300为60MB，HPE SDF为24.75MB，直接影响单核性能基线

- **network_latency**: 通信架构延迟，NL7/FGI为缓存一致性NUMA访问延迟，InfiniBand为HCA硬件卸载延迟



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| SGI UV300 NUMAlink 7架构测试 | 在8机箱配置(32路CPU，320核)上执行魁北克输电系统EMT仿真，利用ccNUMA缓存一致性内存架构实现单系统镜像并行。每仿真步通信延迟低于1微秒，但随着进程数p增加，Karp-Flatt指标e(n,p)呈现非单调增长，表明存在负载不均衡问题 | 相比单核基准，在理想负载均衡下理论加速比受限于Amdahl定律，实际测量显示当p>64时效率eta(n,p)下降至0.7以下 |

| HPE Superdome Flex Grid Interconnect测试 | 在4机箱配置(16路CPU，128核)上测试，采用Intel Xeon Scalable Gold 6144处理器(3.5GHz)。FGI保留NL7的全对全拓扑结构，单跳通信延迟约130ns。仿真结果显示当系统规模n超过L3缓存容量(24.75MB)时，单核基准时间T'(n,1)显著增加 | 与SGI UV300相比，由于缓存容量较小(24.75MB vs 60MB)，在相同问题规模n下kappa'(n,1)开销更大，导致扩展Amdahl定律中的有效串行比例增加 |

| Mellanox InfiniBand ConnectX-3 QDR集群测试 | 在基于InfiniBand QDR(Quad Data Rate)的PC集群上执行，使用MPI over InfiniBand协议。HCA硬件卸载机制减少CPU通信负担，但节点间延迟(~1-2微秒)高于NUMA系统。测试表明随着p增加，通信开销kappa(n,p)单调递增，符合扩展Amdahl定律预测 | 相比共享内存架构，集群方案在p>32时Karp-Flatt指标e(n,p)增长更平滑，但绝对值较高，反映网络通信开销大于内存访问开销 |

| Mellanox ConnectX-6 HDR高带宽测试 | 采用HDR(High Data Rate) InfiniBand技术，提供200Gb/s带宽。在魁北克输电系统大模型仿真中，每步边界数据交换量随子系统界面节点数增加而增加。HDR的高带宽有效减少了大数据包传输时间，使通信开销kappa(n,p)增长斜率降低约40% | 与ConnectX-3 QDR相比，HDR架构在相同进程数p下将通信时间占比从15-20%降低至8-12%，效率eta(n,p)提升约0.1-0.15 |



## 量化发现

- 扩展Amdahl定律揭示：当问题规模n超过单节点L3缓存容量(24.75MB)时，单核基准时间T'(n,1)相比理想值T(n,1)增加15-30%，主要由缓存未命中和内存访问延迟导致
- Karp-Flatt指标e(n,p)诊断：在SGI NUMAlink架构上，当处理单元数p从8增加到64时，e(n,p)从0.05非单调增长至0.12，表明存在负载不均衡和同步开销混合瓶颈
- 通信延迟量化：SGI NL7和HPE FGI的缓存一致性内存访问延迟约为130-200ns，而InfiniBand QDR节点间MPI延迟为1.2-1.5微秒，HDR降低至0.6-0.8微秒
- 并行效率阈值：在魁北克输电系统模型中，当MPI进程数p超过128时，所有测试架构的效率eta(n,p)均下降至0.6以下，主要由kappa(n,p)中的全局同步开销主导
- 内存墙效应：测试证实当EMT仿真状态向量大小超过60MB(SGI UV300 L3缓存)时，单核性能出现显著拐点，验证kappa'(n,1)在公式(6)中的不可忽略性
- 加速比上限：基于扩展Amdahl定律计算，对于串行比例f≈0.02的EMT仿真，即使使用p=256个处理单元，理论加速比上限为50倍，实际测量加速比为35-40倍


## 关键公式

### Karp-Flatt实验串行分数度量

$$$$e(n,p) = \frac{\frac{1}{\psi_{exp}(n,p)} - \frac{1}{p}}{1 - \frac{1}{p}}$$$$

*用于诊断并行EMT仿真中的性能瓶颈，通过测量实际加速比psi_exp反演计算等效串行分数。当e(n,p)随p增加而平滑上升时表明同步开销主导；不规则上升表明负载不均衡*

### 扩展单核执行时间模型

$$$$T'(n,1) = \sigma(n) + \phi(n) + \kappa'(n,1)$$$$

*在大规模电力系统EMT仿真中，当问题规模n导致工作集超过缓存容量时，必须考虑内存访问和IO延迟开销kappa'(n,1)，否则会导致虚假的超线性加速比*



## 验证详情

- **验证方式**: 基于实际大型输电系统的离线仿真对比分析，结合理论性能建模与实测数据验证
- **测试系统**: 魁北克输电系统(Hydro-Québec power transmission system)，包含大量换流器、输电线路和复杂控制系统的实际大规模电网模型
- **仿真工具**: Hydro-Québec自研EMT仿真软件(支持实时和离线双模式，基于MPI标准实现并行处理)，运行于四种硬件平台：SGI UV300(NUMAlink 7)、HPE Superdome Flex(FGI)、InfiniBand ConnectX-3 QDR集群、InfiniBand ConnectX-6 HDR集群
- **验证结果**: 验证了扩展Amdahl定律对大规模EMT仿真加速比预测的准确性，证实Karp-Flatt指标能有效区分负载不均衡与通信开销导致的性能损失。InfiniBand HDR架构在PC集群上实现了接近共享内存系统的并行效率(差异<15%)，证明基于MPI的PC集群方案可有效扩展离线EMT仿真能力至数百核规模

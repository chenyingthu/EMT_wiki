---
title: "并行计算"
type: topic
tags: []
created: "2026-04-13"
---

# 并行计算

## 定义
并行计算在 EMT 语境中指通过网络分区、元件级解耦、时间并行、任务映射或硬件并行来降低大规模暂态仿真的墙钟时间。它既包括离线 HPC/GPU 加速，也包括满足确定步长约束的实时并行仿真。

## 合成定位
在 P0 taxonomy 中，并行计算是 [[real-time-simulation]] 和大规模 [[co-simulation]] 的计算底座。它与 [[frequency-dependent-modeling]] 的快速拟合/宽频模型实现、[[multirate-method]] 的分区调度、以及 [[mmc-model]]、[[vsc-model]] 等细粒度电力电子模型强相关。

## 分类或机制
- 网络级并行：利用传输线延迟、连接域提取、块对角分解、Woodbury 公式或稀疏求解器分解系统矩阵。
- 元件级并行：将 MMC、VSC、风电场、变压器或控制系统拆成可并行更新的子模块。
- 时间并行与多速率：通过 Parareal、PEGR、粗细步长或 [[multirate-method]] 提升长时域仿真效率。
- 硬件与通信平台：CPU 多线程、GPU、FPGA、MPI 集群、FMI/FMU 接口和实时仿真器互联。

## 形式化表示
并行 EMT 的收益通常用加速比和并行效率描述：

$$
S_p=\frac{T_1}{T_p},\qquad E_p=\frac{S_p}{p}
$$

其中 $T_1$ 是串行运行时间，$T_p$ 是 $p$ 个计算单元上的运行时间。对强耦合 EMT 网络，实际收益常受通信、同步、负载不均衡和接口迭代次数限制。

## 适用边界与失败边界
并行计算适合系统规模或元件细节成为主要瓶颈、且模型能被稳定分解的场景。失败边界包括分区接口强耦合、负载不均衡、通信延迟超过计算收益、时间并行不收敛、硬件精度不足、或为了并行而引入不可接受的解耦误差。原页面/来源汇总未给出统一加速比基准，不能把单篇案例数字外推到所有系统。

## 代表性论文
- “A hybrid parallel computation algorithm and its application to multi-phase systems”：早期元件级与网络级混合并行。
- “Parallel Massive-Thread Electromagnetic Transient Simulation on GPU”：GPU 大规模线程 EMT 仿真代表。
- “A Novel Linking-Domain Extraction Decomposition Method for Parallel Electromagnetic Transient Simulation”：连接域提取分解路线。
- “Use of efficient task allocation algorithm for parallel real-time EMT simulation”：实时并行任务分配与验证。
- “An open-source parallel EMT simulation framework” / “ParaEMT”：开源并行 EMT 框架趋势。

## 验证共识
该主题需要同时验证数值一致性和并行收益。常见证据包括与串行 EMT/商业软件波形对比、单步时间或总运行时间、并行效率、负载均衡、通信开销，以及实时场景下是否满足固定步长 deadline。

## 相关方法
- [[state-space-method|状态空间法]] - 子系统状态空间并行求解
- [[fixed-admittance|恒导纳模型]] - 避免导纳矩阵重构的并行优化
- [[multirate-method|多速率方法]] - 不同子系统差异化步长并行
- [[numerical-integration|数值积分]] - 并行积分算法实现
- [[nodal-analysis|节点分析]] - 网络分割与并行求解

## 相关模型
- [[mmc-model|MMC模型]] - 子模块级并行建模
- [[vsc-model|VSC模型]] - 换流器并行仿真
- [[fdne-model|频变网络等值(FDNE)]] - 外部网络并行等值
- [[synchronous-machine-model|同步电机模型]] - 电机集群并行计算

## 相关主题
- [[real-time-simulation|实时仿真]] - 实时约束下的并行策略
- [[co-simulation|混合仿真]] - 多求解器并行协同
- [[frequency-dependent-modeling|频率相关建模]] - 频变模型并行计算
- [[gpu-accelerated-simulation|GPU加速仿真]] - GPU并行架构应用
- [[hil-simulation|硬件在环仿真]] - 分布式HIL并行测试

## 论文方法分析
> 基于 48 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|
| 并行计算技术 | 3 | An open-source parallel EMT simulation framework |
| 电磁暂态仿真 | 3 | Analysis on non-characteristic harmonic circulating current in paralle |
| 并行仿真框架 | 2 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 多绕组变压器详细建模 | 2 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 补偿法(Compensation Method) | 2 | Compensation method for parallel real-time EMT studies✰ |
| 复数向量拟合（CVF） | 2 | Enhancing computation performance of rational approximation for freque |
| 向量拟合（VF） | 2 | Enhancing computation performance of rational approximation for freque |
| C语言底层线性代数库实现 | 2 | Enhancing computation performance of rational approximation for freque |
| 有理函数逼近 | 2 | Enhancing computation performance of rational approximation for freque |
| 多线程并行计算 | 2 | Equivalent Modeling Method of Parallel Elements for Fast Electromagnet |
| 解耦EMT建模 | 1 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 子模块解耦技术 | 1 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 解耦建模 | 1 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 电磁暂态(EMT)分析 | 1 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 连接域提取（LDE）分解法 | 1 | A Novel Linking-Domain Extraction Decomposition Method for Parallel El |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|
| 逆变器型资源(IBR) | 3 |
| 模块化固态变压器(MSST) | 2 |
| 多绕组变压器 | 2 |
| 多有源桥(MAB) | 2 |
| 大规模电力系统网络 | 2 |
| 大规模电力系统 | 2 |
| 电力电子设备 | 2 |
| 频率相关网络等值（FDNE） | 2 |
| 8端口网络等值模型 | 2 |
| 风力发电机组 | 2 |
| 复杂控制系统 | 2 |
| 电力电子变换器 | 2 |
| 风电场 | 2 |
| 模块化多电平换流器(MMC) | 2 |
| 通用线路模型(ULM) | 2 |
### 验证方式分布
- **仿真**: 16 篇
- **仿真与对比**: 7 篇
- **仿真/对比**: 6 篇
- **仿真对比**: 6 篇
- **仿真与硬件实验对比**: 1 篇
- **仿真与现场故障录波数据对比**: 1 篇
- **仿真与硬件在环实验**: 1 篇
- **仿真对比（与商业EMT软件ANSYS/Simplorer和PSCAD/EMTDC结果对比验证）**: 1 篇
- **对比分析**: 1 篇
- **仿真与物理实验对比**: 1 篇
- **仿真对比（与MATLAB/Simulink传统物理模型进行验证）**: 1 篇
- **仿真对比与FPGA实验验证**: 1 篇
- **实时硬件在环(HIL)仿真与对比验证**: 1 篇
- **仿真与实验**: 1 篇
- **仿真与文献实测数据对比验证**: 1 篇
- **仿真/实验**: 1 篇
- **实验与对比**: 1 篇
## 技术演进脉络
### 2009年 (1篇)
- **Independent power producer parallel operation modeling in transient network anal**
  - 💡 将S域控制传递函数通过离散化技术无缝集成至ATP-EMTP的TACS模块中，实现了独立发电商完整控制系统的高精度电磁暂态仿真。
  - 提出了一种基于ATP-EMTP和TACS的独立发电商同步发电机及其控制系统的暂态建模方法。
  - 实现了S域传递函数到ATP-EMTP时域的离散化转换，用于调速器和电压调节器的精确仿真。
### 2010年 (1篇)
- **Chen 等 | A hybrid parallel computation algorithm and its application to multi-ph**
  - 💡 提出将多相电机进行元件级拆分并与网络级并行相结合的混合并行架构，突破了传统长输电线解耦对分区灵活性的限制，有效提升了大规模交直流系统电磁暂态仿真的并行效率。
  - 提出了一种结合元件级与网络级分解的混合并行计算算法，用于提升综合电力系统电磁暂态仿真效率。
  - 通过将计算量大的多相电机拆分为多个耦合子电机，显著降低了单元件计算负担并提高了系统分区的灵活性。
### 2011年 (1篇)
- **Massively Parallel Implementation of AC Machine Modeling for Real-Time Simulatio**
  - 💡 利用交流电机大响应时间特性与纳秒级仿真步长，提出了一种无需预测校正、支持电气/机械解耦并行求解的大规模FPGA硬件架构。
  - 提出了一种适用于FPGA实时仿真的交流电机通用并行实现方法。
  - 设计了针对交流电机数学模型的大规模并行定制硬件架构。
### 2012年 (1篇)
- **Modal Domain Based Modeling of Parallel Transmission Lines**
  - 💡 通过独立FD-line模型结合宽频状态空间互感模型与模态揭示变换，在保留计算效率的同时实现了平行线路互感耦合的高精度暂态仿真。
  - 提出独立FD-line与宽频状态空间模型相结合的混合建模架构以精确表征互感耦合。
  - 引入模态揭示变换防止相间模态被共模分量掩盖，提升耦合计算精度。
### 2014年 (1篇)
- **Parallel Massive-Thread Electromagnetic Transient Simulation on GPU**
  - 💡 通过节点映射与导纳矩阵稀疏化重构，将传统串行EMT算法转化为适配GPU大规模线程架构的并行计算模式，突破了大规模电力系统暂态仿真的算力瓶颈。
  - 提出了基于GPU的大规模线程电磁暂态仿真程序MT-EMTP。
  - 开发了线性无源元件、通用线路模型和通用电机模型的大规模线程并行计算模块。
### 2015年 (1篇)
- **A Parallel Multi-Modal Optimization Algorithm for Simulation-Based Design of Pow**
  - 💡 首次将并行计算架构与代理模型技术深度融合于电力系统多模态优化中，实现了高效的多解搜索与仿真驱动设计。
  - 提出了一种适用于高度并行计算环境的多模态优化算法，显著加速了电力系统的仿真优化设计流程。
  - 引入代理模型在疑似局部最优区域估计目标函数，有效降低计算成本并支持后续灵敏度分析。
### 2018年 (4篇)
- **CPU based parallel computation of electromagnetic transients for large power gri**
  - 💡 利用传输线/电缆的自然解耦特性实现KLU稀疏矩阵的自动并行划分，无需人工干预即可大幅提升大规模电网EMT仿真效率。
  - 实现了基于KLU求解器的CPU并行计算框架，显著提升EMT仿真速度。
  - 提出基于传输线自然解耦的自动子矩阵检测算法，消除人工干预需求。
- **Functional Mock-up Interface Based Approach for Parallel and Multistep Simulatio**
  - 💡 利用FMI标准将控制系统封装为独立FMU，实现了传统多核计算机上EMT仿真的并行化与多步长计算，有效解决了传统多步长技术依赖人工干预且难以自动化的问题。
  - 提出了一种基于FMI标准的EMT并行与多步长协同仿真新方法。
  - 将计算密集的控制系统解耦并封装为内存独立的FMU从站子系统。
- **The diode-clamped half-bridge MMC structure with internal spontaneous capacitor **
  - 💡 提出了一种基于二极管钳位与自发电容并联平衡机制的新型半桥MMC拓扑，从根本上消除了对复杂电压平衡控制算法和大量传感器的依赖。
  - 提出了一种新型二极管钳位半桥MMC拓扑，通过在每个子模块集成钳位二极管与阻尼电阻实现了电容电压的自发并联平衡。
  - 揭示了该拓扑中存在的6种自发电容并联行为(SCPBs)，证明了其无需依赖特定调制或触发技术即可自然平衡子模块电压。
- **面向指数积分方法的电磁暂态仿真GPU并行算法**
  - 💡 将指数积分方法的高度数据并行特性与GPU计算资源深度融合，通过CPU-GPU任务划分实现电磁暂态仿真计算效率的大幅提升。
  - 提出了一种面向指数积分方法的电力系统电磁暂态仿真GPU并行算法。
  - 设计了CPU与GPU异构协同的计算架构，将大规模矩阵运算交由GPU处理，复杂系统状态判别与更新保留在CPU。
### 2019年 (2篇)
- **Functional Mock-Up Interface Based Parallel Multistep Approach With Signal Corre**
  - 💡 提出了一种结合变时间步长异步并行架构与线性外推信号校正的FMI协同仿真方法，实现了EMT仿真灵活性、效率与精度的同步提升。
  - 将原有并行异步模式扩展为支持不同解耦子系统使用不同时间步长。
  - 引入基于线性外推的信号校正程序，有效降低了多步长仿真中的接口数据误差。
- **Parallel-in-Time Simulation Algorithm for Power Electronics: MMC-HVdc System**
  - 💡 提出了一种结合粗细时间步长与状态转换机制的并行时间仿真算法，有效突破了传统空间并行在MMC仿真中的线程数限制。
  - 提出了一种基于并行时间方法的电力电子系统仿真算法，突破了传统空间并行度的限制。
  - 构建了粗细时间步长协同计算框架，分别利用平均值模型和详细模型进行状态求解。
### 2020年 (5篇)
- **A Novel Linking-Domain Extraction Decomposition Method for Parallel Electromagne**
  - 💡 提出基于连接域提取与Woodbury恒等式的矩阵分解求逆算法，实现大规模网络导纳矩阵的直接并行计算，彻底消除传统重叠域分解的迭代开销。
  - 提出基于连接域提取（LDE）的新型网络分解方法，将导纳矩阵解耦为连接域矩阵与对角块矩阵之和。
  - 推导LDM数学引理并结合Woodbury恒等式，建立矩阵求逆通用公式，实现导纳矩阵的直接并行求逆。
- **GPU-based power converter transient simulation with matrix exponential integrati**
  - 💡 将矩阵指数积分法与GPU缓存管理相结合，通过复用开关动作产生的矩阵指数数据，解决了传统GPU仿真中频繁数据传输与显存占用过高的问题。
  - 提出了一种面向电力电子变换器暂态仿真的GPU矩阵指数积分方法。
  - 设计了并行指数积分算法以充分利用GPU多线程计算能力。
- **Hierarchical Device-Level Modular Multilevel Converter Modeling for Parallel and**
  - 💡 将器件级MMC模型通过拓扑重构与网络等效转化为大量相同单元，结合GPU并行与CPU/GPU异构多速率计算，实现了HVDC系统高精度瞬态仿真的高效求解。
  - 提出多层分层建模方法，结合拓扑重构与网络等效技术大幅降低大规模MMC器件级仿真的计算负担。
  - 设计基于GPU的核函数单指令多线程架构，实现大量相同电路单元的大规模并行处理。
- **Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power S**
  - 💡 将Parareal并行时间算法与面向对象组件架构相结合，有效突破了传统串行EMT仿真在含传输线延迟的大规模电力系统中的计算瓶颈。
  - 提出基于节点分析法与Parareal算法的系统级并行电磁暂态仿真方法
  - 设计新型解释方案以解决含传输线延迟的并行仿真收敛问题
- **Use of efficient task allocation algorithm for parallel real-time EMT simulation**
  - 💡 将图划分启发式算法与线性规划精确验证相结合，系统解决了大规模并行实时EMT仿真中的多核任务分配优化难题，并通过工业级HIL实验验证了其有效性。
  - 首次系统评估图划分启发式算法在大规模工业级EMT仿真任务分配中的计算性能与解质量。
  - 构建线性规划精确求解模型作为基准，严格验证了启发式算法所得分配方案的最优性。
### 2021年 (5篇)
- **A parallelization-in-time approach for accelerating EMT simulations**
  - 💡 将PEGR技术从状态空间推广至MANA公式，并结合KLU求解器与OpenMP多线程实现自适应CPU并行加速。
  - 提出了一种基于并行时间方程分组与重排序(PEGR)的新型EMT仿真加速方法。
  - 将PEGR理论从状态空间公式推广并扩展至改进增广节点分析(MANA)公式。
- **Compensation method for parallel real-time EMT studies✰**
  - 💡 将补偿法创新性地引入无自然延迟场景下的网络手动解耦，实现了复杂电力电子网络的并行实时EMT仿真。
  - 详细提出了补偿法在并行实时EMT仿真中用于网络解耦的具体实现方案。
  - 在离线与实时环境下对配电网和HVDC网络测试案例进行了性能评估。
- **Evaluation of the extended modal-domain model in the calculation of lightning-in**
  - 💡 系统评估了扩展模态域模型在复杂配电线路雷击感应电压计算中的适用性，并明确了其在EMT仿真器中实际应用时的精度边界与拟合限制。
  - 评估了EMD模型在平行和双回配电线路雷击感应电压计算中的适用性。
  - 探究了实常数变换矩阵及拟合技术对感应电压波形精度的具体影响。
- **Parallel computation of power system EMTs through Polyphase-QMF filter banks**
  - 💡 将Kron降阶的Laplace域模型与多相QMF滤波器组并行卷积相结合，为电力系统EMT仿真提供了一种高效、可硬件加速的新型计算架构。
  - 提出一种结合Laplace域综合、Kron降阶与时域卷积的新型EMT仿真方法。
  - 设计基于多相QMF滤波器组的并行卷积算法，有效降低计算复杂度并支持高效并行处理。
- **Parallelization of MMC detailed equivalent model**
  - 💡 通过将MMC桥臂模型与电容均压算法封装为独立DLL并在多核CPU上并行调度，实现了离线电磁暂态仿真的高效加速。
  - 提出了一种在多核CPU上并行化MMC详细等效模型(DEM)计算的方法。
  - 将每个桥臂封装为独立的DLL并通过标准接口与主求解器交互，实现了电路方程的解耦与并行。
### 2022年 (3篇)
- **Analysis on non-characteristic harmonic circulating current in parallel inverter**
  - 💡 突破传统仅针对固定频率特征次谐波环流的研究局限，系统分析了电气距离较远且频率不固定的非特征次谐波环流机理并提出针对性抑制方案。
  - 揭示了并联变流器系统中非特征谐波环流的产生机理及其与级联H桥拓扑的强关联性。
  - 基于现场故障录波与FFT分析，明确了非特征谐波环流的频率特征与环流路径。
- **Coupling model for time-domain analysis of nonparallel overhead wires and buried**
  - 💡 首次提出可直接嵌入EMT仿真器的非平行架空-埋地导体时域耦合闭式解析模型，有效解决了有耗大地条件下的电磁暂态耦合计算难题。
  - 提出了一种适用于EMT仿真的非平行架空导线与埋地导体时域耦合模型。
  - 基于薄线散射理论推导了单位长度阻抗和导纳矩阵的闭式解析表达式。
- **Time-Domain Coupling Model for Nonparallel Frequency-Dependent Overhead Multicon**
  - 💡 提出基于MFDTD算法的时域DSFTL模型，突破了传统MTL理论的均匀性限制，实现了非平行多导体线路在频变损耗地面上的高效精确时域耦合仿真。
  - 提出了一种适用于非均匀、非平行多导体架空线路的时域色散散射场传输线(DSFTL)模型。
  - 推导了时域闭式方程，克服了传统多导体传输线理论对线路均匀性和无限长假设的依赖。
### 2023年 (9篇)
- **A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized**
  - 💡 首次将多绕组变压器详细建模、子模块解耦技术与并行计算架构相结合，解决了MSST在宽频带瞬态仿真中精度与效率难以兼顾的瓶颈问题。
  - 提出了一种针对多绕组变压器的详细EMT建模方法，提升了宽频带动态特性的描述精度。
  - 设计了子模块解耦建模策略，有效克服了复杂电力电子开关网络导致的状态方程维数灾难。
- **A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized**
  - 💡 提出结合多绕组变压器精细建模、子模块解耦与并行计算的EMT仿真框架，突破了MSST宽频带高精度与快速仿真的技术瓶颈。
  - 提出多绕组变压器的详细EMT建模方法，有效拓宽了模型的动态频带范围。
  - 设计子模块解耦策略，显著降低了大规模节点导纳矩阵的求解复杂度。
- **Equivalent Modeling Method of Parallel Elements for Fast Electromagnetic Transie**
  - 💡 提出基于二值导纳预存与诺顿等效聚合的并行建模方法，结合多线程框架实现大规模电力电子变压器电磁暂态仿真的万倍级提速。
  - 提出基于导纳固定条件的功率模块划分方法，将H桥单元简化为仅含两种等效导纳的二值导纳单元。
  - 结合导纳参数预存与叠加定理，实现功率模块诺顿等效电路参数的快速求解与串行聚合建模。
- **Locating arc faults on coupling two parallel transmission lines using the novel **
  - 💡 提出基于新相模变换矩阵的时域测距方法，通过单一模量转移特性结合最小二乘法，实现了抗过渡电阻与系统阻抗干扰的高精度双回线电弧故障定位。
  - 推导了适用于同塔双回线系统的新相模变换矩阵，实现了用单一模量反映所有故障类型。
  - 提出了一种基于新模量变换的时域故障定位算法，利用故障模量电弧电压与电流的转移特性构造测距方程。
- **Massively Parallel Modeling of Battery Energy Storage Systems for AC/DC Grid Hig**
  - 💡 首创基于CPU-GPU异构并行与多速率调度的EMT-TS联合仿真框架，突破了海量储能系统高精度暂态仿真的算力瓶颈。
  - 提出CPU与GPU异构计算架构，实现设备级EMT与系统级TS仿真的同步高效计算。
  - 利用GPU多流多线程技术设计异步顺序-并行处理机制，最大化利用异构计算资源。
- **Modeling for large-scale offshore wind farm using multi-thread parallel computin**
  - 💡 将风机集成等效降阶建模与多线程并行求解技术相结合，有效突破了大规模海上风电场微秒级EMT仿真的计算瓶颈。
  - 提出考虑电气集电网络的风机集成等效建模方法，消除内部节点并降低导纳矩阵阶数。
  - 将多线程并行计算技术融入EMT整体求解流程，实现仿真计算效率的进一步提升。
- **Parallelization of EMT simulations for integration of inverter-based resources**
  - 💡 将TLM网络解耦、FMI标准接口与信号量同步机制深度融合，实现了高精度、多速率的大规模IBR电网并行EMT协同仿真。
  - 提出了一种基于FMI标准的EMT协同仿真架构，实现多求解器实例的并行计算。
  - 利用传输线传播延迟实现电网无近似解耦，各子网络可独立并行求解。
- **Performance evaluation of communication fabrics for offline parallel electromagn**
  - 💡 首次将多种高性能通信架构引入离线EMT并行仿真领域进行系统性对比评估，填补了仿真平台向PC集群迁移的性能基准空白。
  - 系统评估了四种支持MPI的通信架构在离线并行EMT仿真中的性能表现。
  - 建立了针对大规模EMT仿真单步时间成本与并行效率的量化评估指标。
- **Sparse solver application for parallel real-time electromagnetic transient simul**
  - 💡 首次将MKLU稀疏求解器及其核心优化技术与并行化方法深度融合，应用于工业级实时EMT仿真平台，在保障数值稳定性的同时实现计算效率的大幅提升。
  - 首次将MKLU稀疏求解器集成至工业级实时仿真环境HYPERSIM中，替代传统基于代码生成的求解器。
  - 系统评估并确定了填充减少、部分重分解与主元策略等稀疏求解技术对实时EMT仿真的加速效果。
### 2024年 (6篇)
- **An open-source parallel EMT simulation framework**
  - 💡 首个面向大规模高比例IBR电网的开源并行EMT仿真框架，有效解决了商业软件封闭性与传统串行计算的性能瓶颈问题。
  - 开发了名为ParaEMT的开源、通用且模块化的电磁暂态仿真框架。
  - 设计了可扩展的并行计算架构以有效突破大规模IBR电网仿真的计算瓶颈。
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 首次将复数向量拟合（CVF）引入FDNE矩阵综合，并结合底层并行C语言实现，在摆脱商业软件依赖的同时大幅提升了宽频网络等值的计算效率。
  - 首次将复数向量拟合（CVF）应用于FDNE的导纳/阻抗矩阵综合，打破了传统VF必须满足共轭复数对的限制。
  - 开发了基于C语言与底层线性代数库的并行化VF/CVF算法实现，摆脱了对MATLAB等商业软件的依赖。
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 首次将复数向量拟合（CVF）引入导纳矩阵综合，并结合并行C语言底层实现，大幅提升了FDNE有理近似的计算效率与软件独立性。
  - 首次将复数向量拟合（CVF）应用于FDNE的导纳/阻抗矩阵综合，突破了传统VF必须满足共轭复数对的限制。
  - 开发了基于C语言与底层线性代数库的并行化VF/CVF算法实现，摆脱了对MATLAB等商业软件的依赖。
- **Key Technologies and Prospects for Electromagnetic Transient Parallel Simulation**
  - 💡 系统构建了新型电力系统电磁暂态并行仿真的技术框架，并前瞻性地提出算法与硬件深度融合是贡献仿真效率瓶颈的核心路径。
  - 梳理了新型电力系统对电磁暂态仿真的新需求与挑战
  - 系统总结了电磁暂态分网并行算法与多速率仿真方法
- **Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Sc**
  - 💡 将数据驱动机器学习建模与面向数据的ECS并行架构深度融合，首次实现百万级可再生能源系统的高精度、超大规模并行EMT瞬态仿真。
  - 提出了一种结合人工神经网络与ECS架构的数据驱动EMT仿真新方法。
  - 构建了基于CPU-GPU异构平台的大规模并行计算框架以突破传统仿真规模瓶颈。
- **ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for La**
  - 💡 将加边块对角矩阵分解、并行状态更新与通用HPC接口深度融合，实现了面向海量IBR电网的高效、可扩展开源EMT仿真。
  - 开发了开源、基于Python且支持并行与HPC的EMT仿真器ParaEMT。
  - 提出基于加边块对角矩阵分解的网络并行求解方法及设备状态/历史电流并行更新机制。
### 2025年 (6篇)
- **Co-simulation and compensation method for parallel simulation of electromagnetic**
  - 💡 首次将无延迟补偿法与FMI协同仿真架构深度融合，并引入自适应步长/阶数机制，突破了传统延迟解耦方法的精度瓶颈，实现了高精度、高扩展性的EMT并行计算。
  - 提出了一种基于补偿法的无延迟并行EMT协同仿真工具，支持在网络任意位置解耦方程而不损失精度。
  - 将补偿法推广至修正增广节点分析(MANA)公式，并基于FMI标准构建了可扩展的协同仿真接口。
- **Double-Ended Fault-Locating Method for Parallel Lines Without Measuring Parallel**
  - 💡 提出了一种仅依赖故障线路本地同步量与远端零序电流即可估计平行线路零序互感电流的双端故障定位新算法，突破了传统方法需直接测量平行线路电流的限制。
  - 提出一种无需直接测量平行线路零序电流的双端阻抗故障定位方法
  - 利用故障线路本地同步电压电流与远端零序电流有效估计平行线路零序互感电流
- **Efficient modeling of parallel counterpoise wires using an FDTD-based transmissi**
  - 💡 首次发现平行接地极的有效长度与其间距无关，显著简化了高压输电线路接地系统的设计流程。
  - 提出了一种结合FDTD与传输线理论的高效平行接地极建模方法，并计及了频变参数效应。
  - 通过与严格电磁场模型对比验证了所提方法的准确性，全工况偏差低于5%。
- **Fine-Grained Optimal Allocation of Wind Farm Decoupled Models for CPU-GPU Parall**
  - 💡 首次将风电场解耦模型的CPU-GPU硬件分配转化为步级整数非线性规划问题，实现细粒度计算资源的最优匹配与仿真加速。
  - 提出自底向上的量化方法，通过分解顺序与并行计算步骤精确评估解耦模型的计算资源与求解时间
  - 首次将风电场解耦模型的硬件分配构建为整数非线性规划问题，实现步级计算任务的最优分配
- **Low-Dimensional Equivalent Models and Multithreading-Based Parallel EMT Simulati**
  - 💡 通过半隐式积分解耦与相级等效电路合成构建多VSC低维模型，并结合OpenMP多线程技术实现高精度、高效率的并行EMT仿真。
  - 提出基于半隐式混合积分的VSC与电网解耦方法，有效降低系统节点导纳矩阵维度与计算复杂度。
  - 推导了适用于不同直流侧连接场景的多VSC低维等效电路模型，兼顾系统内外电气特性。
- **Transient Electromagnetic Power Compensation‐Based Adaptive Inertia Control Stra**
  - 💡 将暂态电磁功率补偿机制与自适应惯量控制相融合，针对性解决了并联储能VSC因单元间角加速度差异引发的频率振荡问题。
  - 推导了并联VSC-ESS的状态空间方程与传递函数，阐明了关键控制参数对系统稳定性及频率响应特性的影响规律。
  - 提出了一种暂态电磁功率补偿控制策略，有效抑制了频率调节过程中的有功功率超调与振荡。
### 2026年 (2篇)
- **Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulat**
  - 💡 融合解耦等效建模、多速率步长分配、开关插值补偿与CPU-GPU异构并行技术，突破了含储能MMC在EMT仿真中计算维度高与步长受限的瓶颈。
  - 提出适用于BESS-MMC的解耦详细等效模型，可准确复现解锁与闭锁工况下的动态特性。
  - 引入多速率仿真策略，针对不同频率子系统分配差异化时间步长以提升计算效率。
- **GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of P**
  - 💡 首次将多粒度GPU并行计算架构与指数积分器算法深度融合，并引入高效的矩阵指数预计算机制，突破了传统EMT仿真在速度与稳定性上的瓶颈。
  - 提出了一种多粒度GPU并行率指数积分器算法，利用GPU架构并行计算多个离散化步骤及步内矩阵向量运算。
  - 开发了一种基于GPU的高效矩阵指数预计算框架，显著提升了仿真循环前的数值计算效率。
## 关键发现汇总
- [2009] **Independent power producer parallel operation modeling in tr**: 验证了调速器和电压调节器在系统扰动下的动态响应特性与控制效果。
- [2009] **Independent power producer parallel operation modeling in tr**: 展示了独立发电商与配电网并联运行时的暂态稳定性及系统动态行为。
- [2010] **Chen 等 | A hybrid parallel computation algorithm and its app**: 典型综合电力系统算例验证了所提混合并行算法的正确性与有效性。
- [2010] **Chen 等 | A hybrid parallel computation algorithm and its app**: 该算法通过元件级拆分与流程优化，显著提升了电磁暂态仿真的计算效率与分区灵活性。
- [2011] **Massively Parallel Implementation of AC Machine Modeling for**: 在FPGA平台上实现了交流电机实时仿真，单步计算时间仅为44 ns。
- [2011] **Massively Parallel Implementation of AC Machine Modeling for**: 成功验证了永磁同步电机及感应电机驱动系统在纳秒级步长下的并行仿真架构。
- [2011] **Massively Parallel Implementation of AC Machine Modeling for**: 所提方法在无需预测-校正的情况下，保持了仿真的高精度与数值稳定性。
- [2012] **Modal Domain Based Modeling of Parallel Transmission Lines**: 新方法显著降低了传统FD-line模型在平行线路耦合干扰仿真中的误差。
- [2012] **Modal Domain Based Modeling of Parallel Transmission Lines**: 能够高精度复现线路投切与变压器励磁涌流引起的暂态耦合波形。
- [2012] **Modal Domain Based Modeling of Parallel Transmission Lines**: 与ULM模型及逆数值拉普拉斯变换结果对比，证实了全频带内的高准确性。
- [2014] **Parallel Massive-Thread Electromagnetic Transient Simulation**: 在包含2458个三相母线的大规模系统上成功实现了详细建模的并行仿真。
- [2014] **Parallel Massive-Thread Electromagnetic Transient Simulation**: 与主流商业软件EMTP-RV相比，MT-EMTP在保持等效仿真精度的前提下显著提升了计算性能。
- [2015] **A Parallel Multi-Modal Optimization Algorithm for Simulation**: 并行执行版本相比顺序执行版本大幅缩短了优化计算时间，有效解决了多模态算法计算开销大的瓶颈。
- [2015] **A Parallel Multi-Modal Optimization Algorithm for Simulation**: 代理模型能够准确估计目标函数在局部最优区域的特性，为后优化阶段的参数敏感性研究提供了可靠依据。
- [2015] **A Parallel Multi-Modal Optimization Algorithm for Simulation**: 在VSC-HVDC系统设计中成功识别出多个可行最优解，证明了算法处理非凸多峰优化问题的有效性。
- [2018] **CPU based parallel computation of electromagnetic transients**: 并行计算框架大幅缩短了大规模电网EMT仿真的计算时间。
- [2018] **CPU based parallel computation of electromagnetic transients**: 自动网络撕裂技术在不损失精度的前提下实现了高效的并行任务划分。
- [2018] **CPU based parallel computation of electromagnetic transients**: 该方法在含大量非线性模型的真实电网中表现出良好的可扩展性。
- [2018] **Functional Mock-up Interface Based Approach for Parallel and**: 异步与同步两种仿真模式均实现了显著的计算时间缩减。
- [2018] **Functional Mock-up Interface Based Approach for Parallel and**: 在大幅提升计算效率的同时，仿真精度得到了有效保持。
- [2018] **Functional Mock-up Interface Based Approach for Parallel and**: 该方法成功应用于含复杂控制系统的大规模电网保护仿真场景。
- [2018] **The diode-clamped half-bridge MMC structure with internal sp**: 新型拓扑在不依赖闭环电压平衡控制的情况下，成功实现了所有子模块电容电压的自动均衡。
- [2018] **The diode-clamped half-bridge MMC structure with internal sp**: 优化RC参数后，相邻子模块的电容电压纹波保持一致，显著改善了电压波动特性。
- [2018] **The diode-clamped half-bridge MMC structure with internal sp**: PSCAD/EMTDC仿真与降比例样机实验结果一致验证了该拓扑在减少传感器数量方面的有效性及良好的动态性能。
- [2018] **面向指数积分方法的电磁暂态仿真GPU并行算法**: 所提算法在17台和100台风机风电场算例中均成功验证了计算正确性与有效性。
- [2018] **面向指数积分方法的电磁暂态仿真GPU并行算法**: GPU并行算法的加速效果随着电力系统仿真规模的增加而愈发明显。
- [2019] **Functional Mock-Up Interface Based Parallel Multistep Approa**: 支持主从子系统采用不同时间步长进行异步并行计算，大幅提升了仿真架构的灵活性。
- [2019] **Functional Mock-Up Interface Based Parallel Multistep Approa**: 线性外推信号校正技术有效抑制了多步长同步过程中的接口误差，提高了仿真精度。
- [2019] **Functional Mock-Up Interface Based Parallel Multistep Approa**: 数值测试表明，改进后的方法在计算效率和准确性上均显著优于原有FMI并行方案。
- [2019] **Parallel-in-Time Simulation Algorithm for Power Electronics:**: 在使用5个计算核心的条件下，算法实现了最高3.47倍的仿真加速比。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow|Multiprocessor based generator module for a real-time power ]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat|Nested fast and simultaneous solution for time-domain simula]] | 2006 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[the-computer-simulation-and-real-time-stabilization-control-for-the-inverted-pen|The Computer Simulation and Real-Time Stabilization Control ]] | 2009 |
| [[chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas|Chen 等 | A hybrid parallel computation algorithm and its app]] | 2010 |
| [[能量回馈型电力电子负载的控制方法|能量回馈型电力电子负载的控制方法]] | 2010 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[synchronous-machine-exciter-circuit-model-in-a|Synchronous Machine Exciter Circuit Model In A]] | 2013 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g|Comparative study on electromechanical and electromagnetic t]] | 2014 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[a-parallel-multi-modal-optimization-algorithm-for-simulation-based-design-of-pow|A Parallel Multi-Modal Optimization Algorithm for Simulation]] | 2015 |
| [[a-parallel-multi-modal-optimization-algorithm-for-simulation-based-design-of-pow|A Parallel Multi-Modal Optimization Algorithm for Simulation]] | 2015 |
| [[modulation-index-dependent-thevenin-equivalent-circuit-model-of-vsc-and-apdr|Modulation Index Dependent Thévenin Equivalent Circuit Model]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[30tpwrd20172714639-2|30/TPWRD.2017.2714639]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[32tpwrd20182812753-2|32/TPWRD.2018.2812753]] | 2018 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio|Functional Mock-up Interface Based Approach for Parallel and]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-|The diode-clamped half-bridge MMC structure with internal sp]] | 2018 |
| [[面向指数积分方法的电磁暂态仿真gpu并行算法|面向指数积分方法的电磁暂态仿真GPU并行算法]] | 2018 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[accelerated-sparse-matrix-based-computation-of-electromagnetic-transients|Accelerated Sparse Matrix-Based Computation of Electromagnet]] | 2019 |
| [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre|Functional Mock-Up Interface Based Parallel Multistep Approa]] | 2019 |
| [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre|Functional Mock-Up Interface Based Parallel Multistep Approa]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[three-phase-adaptive-auto-reclosing-for-single-outgoing-line-of-wind-farm-based-|Three-phase Adaptive Auto-Reclosing for Single Outgoing Line]] | 2019 |
| [[a-hierarchical-low-rank-approximation-based-network-solver-for-emt-simulation|A Hierarchical Low-Rank Approximation Based Network Solver f]] | 2020 |
| [[a-hierarchical-low-rank-approximation-based-network-solver-for-emt-simulation|A Hierarchical Low-Rank Approximation Based Network Solver f]] | 2020 |
| [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|A Novel Linking-Domain Extraction Decomposition Method for P]] | 2020 |
| [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|A Novel Linking-Domain Extraction Decomposition Method for P]] | 2020 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[fpga-based-sub-microsecond-level-real-time-simulation-for-microgrids-with-a-netw|FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Mi]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Use of efficient task allocation algorithm for parallel real]] | 2020 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations]] | 2021 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[an-fpga-based-electromagnetic-transient-analysis-of-power-distribution-network|An FPGA based electromagnetic transient analysis of power di]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[flexible-time-stepping-dynamic-emulation-of-acdc-grid-for-faster-than-scada-appl|Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for F]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-|Acceleration of electromagnetic transient simulations in mod]] | 2022 |
| [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix|Analysis and Prospect of Development of China]] | 2022 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode|Efficient steady state analysis of the grid using electromag]] | 2022 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode|Efficient steady state analysis of the grid using electromag]] | 2022 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode|Efficient steady state analysis of the grid using electromag]] | 2022 |
| [[fast-simulation-model-of-voltage-source-converters-with-arbitrary-topology-using|Fast Simulation Model of Voltage Source Converters With Arbi]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报|中  国  电  机  工  程  学  报]] | 2022 |
| [[电力系统机电-电磁混合仿真边界解耦算法研究|电力系统机电-电磁混合仿真边界解耦算法研究]] | 2022 |
| [[电力系统机电-电磁混合仿真边界解耦算法研究|电力系统机电-电磁混合仿真边界解耦算法研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法|直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法]] | 2022 |
| [[直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法|直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi|Improved methods for optimization of power systems with rene]] | 2023 |
| [[improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi|Improved methods for optimization of power systems with rene]] | 2023 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
| [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad|Real-Time Simulation of Power System Electromagnetic Transie]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Sparse solver application for parallel real-time electromagn]] | 2023 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[交直流电力系统分割并行电磁暂态数字仿真方法|交直流电力系统分割并行电磁暂态数字仿真方法]] | 2023 |
| [[交直流电力系统分割并行电磁暂态数字仿真方法|交直流电力系统分割并行电磁暂态数字仿真方法]] | 2023 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[基于一致性算法的多虚拟同步机功率振荡协调抑制|基于一致性算法的多虚拟同步机功率振荡协调抑制]] | 2023 |
| [[基于一致性算法的多虚拟同步机功率振荡协调抑制|基于一致性算法的多虚拟同步机功率振荡协调抑制]] | 2023 |
| [[新能源高占比电力系统电磁暂态并行仿真的优化分网方法|新能源高占比电力系统电磁暂态并行仿真的优化分网方法]] | 2023 |
| [[新能源高占比电力系统电磁暂态并行仿真的优化分网方法|新能源高占比电力系统电磁暂态并行仿真的优化分网方法]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc|Machine-Learning-Reinforced Massively Parallel Transient Sim]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large|ParaEMT: An Open Source, Parallelizable, and HPC-Compatible ]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener-1|A Component-Level Modeling and Fine-Grained Simulation Metho]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based|A state-variable-preserving method for the efficient modelli]] | 2025 |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based|A state-variable-preserving method for the efficient modelli]] | 2025 |
| [[acceleration-strategies-for-emt-simulation-of-hvdc-systems|Acceleration strategies for EMT Simulation of HVDC systems]] | 2025 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Co-simulation and compensation method for parallel simulatio]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[equivalent-modelling-method-of-single-active-network-for-fast-electromagnetic-tr|Equivalent Modelling Method of Single Active Network for Fas]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall|Fine-Grained Optimal Allocation of Wind Farm Decoupled Model]] | 2025 |
| [[low-dimensional-equivalent-models-and-multithreading-based-parallel-emt-simulati|Low-Dimensional Equivalent Models and Multithreading-Based P]] | 2025 |
| [[low-dimensional-equivalent-models-and-multithreading-based-parallel-emt-simulati|Low-Dimensional Equivalent Models and Multithreading-Based P]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[partial-refactorization-techniques-for-electromagnetic-transient-simulations|Partial Refactorization Techniques for Electromagnetic Trans]] | 2025 |
| [[中-国-电-机-工-程-学-报-37|中  国  电  机  工  程  学  报]] | 2025 |
| [[分布式光伏电源分散式自适应主动频率支撑控制|分布式光伏电源分散式自适应主动频率支撑控制]] | 2025 |
| [[分布式光伏电源分散式自适应主动频率支撑控制|分布式光伏电源分散式自适应主动频率支撑控制]] | 2025 |
| [[基于fpga的变电站实时仿真培训系统|基于FPGA的变电站实时仿真培训系统]] | 2025 |
| [[改善暂态稳定性的多构网型变换器频率同步协同控制|改善暂态稳定性的多构网型变换器频率同步协同控制]] | 2025 |
| [[dead-time-effect-modeling-for-hybrid-modular-multilevel-converter-using-twin-map|Dead-time effect modeling for hybrid modular multilevel conv]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor|EMT Model Boundary Determination Using Floquet Theory-based ]] | 2026 |
| [[equivalent-modeling-of-electromagnetic-transient-for-mmc-hvdc-based-on-semi-impl|Equivalent modeling of electromagnetic transient for MMC-HVD]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |
| [[基于矩阵对角化的电磁暂态时间并行计算方法|基于矩阵对角化的电磁暂态时间并行计算方法]] | 2026 |
| [[基于矩阵对角化的电磁暂态时间并行计算方法|基于矩阵对角化的电磁暂态时间并行计算方法]] | 2026 |
| [[适用于实时仿真的mmc子模块电容电压优化均衡方法|适用于实时仿真的MMC子模块电容电压优化均衡方法]] | 2026 |
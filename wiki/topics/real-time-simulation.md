---
title: "实时仿真"
type: topic
tags: []
created: "2026-04-13"
---

# 实时仿真

## 论文方法分析
> 基于 52 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 电磁暂态(EMT)建模 | 3 | Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies fo |
| 补偿法 | 2 | An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on F |
| FPGA硬件实现 | 2 | Development of phase domain frequency-dependent transmission line mode |
| VHDL编程 | 2 | Development of phase domain frequency-dependent transmission line mode |
| FPGA实时仿真 | 2 | FPGA-based simulation of grid-tied converters using frequency-dependen |
| 浮点运算 | 2 | High performance computing engines for the FPGA-based simulation of th |
| CPU-FPGA协同多速率实时仿真框架 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 离散电感解耦方法 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 关联离散电路模型解析参数选择策略 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 最小损耗误差准则优化 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 基于FEA数据的降阶建模(ROM) | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 磁链定义法(Flux-Defined) | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 高效三线性插值算法 | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 电流导数直接计算法(免查表求逆) | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 开关函数详细等效模型(SFB-DEM) | 1 | A Numerically Efficient and Accurate Model for Real-Time Simulation of |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 负载 | 3 |
| 变压器 | 3 |
| 模块化多电平换流器(MMC) | 3 |
| 串联补偿线路 | 2 |
| 光伏阵列 | 2 |
| 同步发电机 | 2 |
| 双馈感应发电机(DFIG) | 2 |
| 电力电子变换器 | 2 |
| 风力发电机(WT) | 2 |
| 输电线路 | 2 |
| 风电场 | 2 |
| 可控线路换相换流器高压直流系统(CLCC-HVDC) | 1 |
| CLCC换流器阀组 | 1 |
| 永磁同步电机(PMSM) | 1 |
| 电动汽车(EV)动力总成 | 1 |
### 验证方式分布
- **仿真对比**: 5 篇
- **仿真**: 5 篇
- **仿真/对比**: 5 篇
- **仿真与对比**: 3 篇
- **实验验证与CPU离线仿真对比**: 1 篇
- **仿真与硬件实验对比**: 1 篇
- **仿真与MATLAB对比验证**: 1 篇
- **实验与仿真对比**: 1 篇
- **仿真与硬件在环(HIL)实验**: 1 篇
- **仿真对比验证**: 1 篇
- **仿真验证与对比**: 1 篇
- **仿真与FPGA硬件实验验证**: 1 篇
- **硬件仿真与商业软件(DSATools/TSAT)对比验证**: 1 篇
- **实验**: 1 篇
- **硬件实验与离线仿真对比**: 1 篇
- **仿真验证与FPGA硬件实现对比**: 1 篇
- **实时仿真器仿真验证与详细模型对比**: 1 篇
- **仿真与FPGA硬件实现验证**: 1 篇
- **硬件在环(HIL)实时仿真与双模型对比**: 1 篇
- **仿真与硬件在环实验（HIL）及现场工程验证**: 1 篇
- **实时仿真波形对比与性能评估**: 1 篇
- **FPGA硬件实验验证**: 1 篇
- **仿真对比验证（与Matlab/Simulink离线仿真结果对比）**: 1 篇
- **仿真与硬件实验验证**: 1 篇
- **对比**: 1 篇
- **FPGA硬件实时仿真与案例验证**: 1 篇
- **仿真对比与硬件实验验证**: 1 篇
- **仿真与硬件在环实验**: 1 篇
- **仿真与实验**: 1 篇
- **仿真验证**: 1 篇
- **HIL硬件在环实验与离线仿真对比**: 1 篇
- **实时仿真与离线ATP对比及示波器实测**: 1 篇
- **仿真与基准测试对比**: 1 篇
- **HIL硬件在环仿真与对比验证**: 1 篇
- **仿真与对比验证**: 1 篇
- **仿真与实物实验对比**: 1 篇
- **仿真/案例验证**: 1 篇
- **硬件在环实验与仿真对比**: 1 篇
## 技术演进脉络
### 2004年 (2篇)
- **Multiprocessor based generator module for a real-time power system simulator - P**
  - 💡 将多微处理器并行计算与模拟三相正弦振荡器相结合，构建了可通过软件编程灵活配置、步长极小且精度高的混合式实时发电机仿真模块。
  - 开发了基于多微处理器的实时发电机仿真模块，仅需修改程序即可灵活模拟任意类型发电机。
  - 提出四微处理器并行求解微分方程的方法，大幅缩短仿真步长以满足实时模拟需求。
- **Real-time digital simulator of the electromagnetic transients of power transmiss**
  - 💡 首次提出基于时域公式的输电线路电磁暂态实时数字仿真方法，实现了高精度、低成本的纯数字化线路建模。
  - 提出了一种基于时域公式的输电线路电磁暂态实时数字仿真器。
  - 实现了平衡与不平衡电源激励下三相输电线路的实时暂态性能计算。
### 2007年 (1篇)
- **Real-Time Transient Simulation Based on a Robust**
  - 💡 提出了一种兼顾稳定性、正实性与宽频带高精度的鲁棒双层网络等值方法，并实现了模型最优阶数的自动确定。
  - 提出了一种鲁棒的双层网络等值(TLNE)架构，将外部系统划分为表层与深层区域以有效降低模型阶数。
  - 结合拟合与优化技术生成低阶等值模型，在宽频带内保持高精度并具备最优阶数自动确定功能。
### 2009年 (2篇)
- **FPGA-Based Real-Time EMTP**
  - 💡 将传统串行EMTP算法重构为深度流水线并行架构，首次在单片FPGA上实现高精度浮点实时电磁暂态仿真。
  - 提出了一种基于单片FPGA的实时电磁暂态仿真器硬件架构，充分利用FPGA的并行性与高时钟频率。
  - 设计了深度流水线并行算法并采用浮点运算，在保障计算精度的同时大幅提升数据吞吐量。
- **The Computer Simulation and Real-Time Stabilization Control for the Inverted Pen**
  - 💡 将LQR最优控制理论与Simulink实时仿真技术结合，实现了倒立摆系统从理论建模、计算机仿真到物理实时控制的完整验证闭环。
  - 建立了基于详细力学分析的倒立摆系统精确数学模型。
  - 提出了基于LQR理论的状态反馈控制器，实现摆角与小车位置的并行稳定控制。
### 2011年 (2篇)
- **An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA**
  - 💡 首次在FPGA上全硬件实现基于补偿法与牛顿-拉夫逊算法的并行迭代求解器，结合稀疏技术与深度流水线浮点运算，突破了非线性电磁暂态实时仿真的算力与收敛瓶颈。
  - 提出了一种基于FPGA的迭代式非线性电磁暂态实时求解器，突破了传统CPU/DSP在实时仿真中的算力瓶颈。
  - 结合补偿法与牛顿-拉夫逊算法，并引入稀疏技术、深度流水线浮点运算及并行高斯-约当消元法，显著提升了非线性方程组的求解效率。
- **Massively Parallel Implementation of AC Machine Modeling for Real-Time Simulatio**
  - 💡 将纳秒级仿真步长与大规模并行FPGA硬件架构深度融合，实现了无需预测-校正迭代的交流电机高效解耦实时仿真。
  - 提出了一种适用于FPGA平台的交流电机暂态通用并行实现方法。
  - 利用电机大响应时间与纳秒级步长，彻底消除了电气与机械变量的预测-校正迭代过程。
### 2012年 (1篇)
- **The Reconﬁgurable-Hardware Real-Time and**
  - 💡 提出基于FPGA的硬件可重构与大规模并行架构，首次实现24 ns级超高速实时与超实时电磁暂态仿真。
  - 开发了基于FPGA的可重构硬件实时仿真器（RH-RTS），支持动态适配不同电力系统拓扑。
  - 设计了针对特定系统数学模型的大规模并行定制化硬件架构。
### 2016年 (1篇)
- **Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromag**
  - 💡 将几何基非线性磁等效电路与全并行流水线FPGA架构相结合，实现了Sen变压器的高保真实时电磁暂态HIL仿真。
  - 提出了一种基于磁等效电路的Sen变压器高保真实时电磁暂态模型
  - 在FPGA上采用全并行与流水线架构及32位浮点精度实现了该模型
### 2018年 (2篇)
- **Real-Time FPGA-RTDS Co-Simulator for Power Systems**
  - 💡 融合FPGA并行高速计算与RTDS灵活建模优势，构建了一种避免传统TS-EMT接口误差的大规模电力系统实时协同仿真新架构。
  - 提出了一种结合FPGA高算力与RTDS建模灵活性的实时协同仿真平台。
  - 设计了FPGA与RTDS之间的专用接口，有效避免了传统TS-EMT混合仿真中的接口误差。
- **Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phaso**
  - 💡 将移位相量理论引入MMC子模块与桥臂的等效建模，实现了计算复杂度与子模块数量解耦的高精度实时电磁暂态仿真。
  - 提出基于移位相量的子模块Thevenin等效模型，有效提升了MMC电磁暂态仿真精度。
  - 构建开关依赖型桥臂等效电路，使计算负担几乎不随子模块数量增加而变化。
### 2019年 (2篇)
- **Modeling a voltage source converter assisted resonant current DC breaker for rea**
  - 💡 提出了一种兼顾计算效率与外部电气特性精度的VARC直流断路器RTDS实时仿真模型，填补了该类断路器在系统级实时保护研究中的建模空白。
  - 在RTDS平台上建立了VARC直流断路器的详细实时仿真模型。
  - 确保模型的外部伏安特性能够准确复现真实设备的电气行为，适用于系统级研究。
- **Real-Time MPSoC-Based Electrothermal Transient Simulation of Fault Tolerant MMC **
  - 💡 将系统级等效电路与器件级电热模型深度融合，在MPSoC平台上实现了复杂CDSM MMC拓扑的高精度实时电热暂态仿真。
  - 提出了适用于CDSM MMC的器件级电热模型，可精确计算开关损耗、结温及开关暂态波形。
  - 采用等效电路模型与器件级模型相结合的混合架构，在保证精度的同时有效控制了计算资源消耗以满足实时性要求。
### 2020年 (4篇)
- **FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids With a Netw**
  - 💡 提出一种结合固定导纳模型与延迟插入法的网络解耦算法，实现了微电网在FPGA上的亚微秒级并行实时仿真，突破了仿真步长随系统规模增大的限制。
  - 提出了一种基于FPGA的微电网亚微秒级实时仿真方法。
  - 利用固定导纳模型与延迟插入法实现分布式电源的网络解耦与并行计算。
- **High performance computing engines for the FPGA-based simulation of the ULM**
  - 💡 通过计算重调度与历史项优化管理，在FPGA上实现了ULM模型的高频、低延迟实时仿真。
  - 提出了一种基于FPGA的ULM仿真设计方法，显著提升了计算性能。
  - 采用状态空间法对特征导纳和传播函数的极点-留数形式进行时域仿真。
- **Real-time simulation with an industrial DCCB controller in a HVDC grid**
  - 💡 将工业级物理DCCB与MMC控制器集成于实时HIL平台，实现了多厂商直流电网保护控制系统的工厂级互操作性与协调性验证。
  - 开发了适用于实时仿真的混合式直流断路器等效模型
  - 构建了集成物理MMC控制器与12个DCCB控制器的三端直流电网HIL测试平台
- **Use of efficient task allocation algorithm for parallel real-time EMT simulation**
  - 💡 首次将图划分算法与精确验证方法结合，系统解决超大规模电网并行实时EMT仿真的任务分配优化问题，并通过硬件在环实验完成工业级验证。
  - 将并行实时EMT仿真的任务映射问题形式化为任务分配问题(TAP)并引入运筹学技术求解
  - 首次系统评估了图划分启发式算法在超大规模工业电网与真实仿真器架构上的性能与解质量
### 2021年 (8篇)
- **An FPGA based electromagnetic transient analysis of power distribution network**
  - 💡 将共轭梯度求解器直接部署于FPGA硬件，突破了传统FPGA仿真依赖预存逆矩阵的瓶颈，实现了配电网电磁暂态的高效、高精度求解。
  - 提出了一种基于FPGA的配电网电磁暂态仿真框架。
  - 在FPGA上实现了共轭梯度求解器，避免了传统方法预存时变元件逆矩阵的局限性。
- **Compensation method for parallel real-time EMT studies✰**
  - 💡 将补偿方法引入无自然延迟的电网并行解耦，突破了传统依赖传输线延迟的并行仿真限制，实现了复杂电力电子系统的高效实时EMT计算。
  - 详细给出了补偿方法用于网络解耦以实现并行实时EMT仿真的具体实现流程。
  - 在离线与实时环境下系统评估了该方法在配电网和HVDC网络中的计算性能。
- **Damping of Subsynchronous Control Interactions in Large-Scale PV Installations T**
  - 💡 将基于FPGA的EMT-TS协同超实时仿真应用于大型光伏电站SSCI的预测与主动阻尼控制，实现了百倍级加速比下的快速干预。
  - 分析了典型光伏网络的次同步控制相互作用（SSCI）振荡模式。
  - 提出了一种基于FPGA的EMT-TS协同超实时动态仿真架构。
- **Development of phase domain frequency-dependent transmission line model on FPGA **
  - 💡 通过全流水线并行架构与自定义48位浮点运算在FPGA上实现频变相域传输线模型，突破了传统实时仿真中计算精度与步长的瓶颈。
  - 提出了一种专为EMT实时数字仿真器设计的基于FPGA的频变相域传输线模型。
  - 采用全流水线与并行化硬件架构设计，实现了极低的仿真步长以满足实时性要求。
- **Development of phase domain frequency-dependent transmission line model on FPGA **
  - 💡 首次在FPGA上实现全流水线并行化的相域频变输电线路模型，并结合自定义48位浮点格式突破实时仿真步长与精度瓶颈。
  - 开发了适用于FPGA实时数字仿真器的频变相域输电线路模型。
  - 通过全流水线与并行化硬件架构设计，实现了最低仿真步长。
- **Large-scale hybrid real time simulation modeling and benchmark for nelson river **
  - 💡 首创将大规模多馈入HVDC系统模块化拆分，并融合RTDS软件电网模型与实际硬件控制器的混合实时HIL仿真架构，直接支撑了实际重大直流工程的现场投运。
  - 构建了结合RTDS软件模型（Bipole I/II）与Bipole III硬件控制器的混合实时HIL仿真平台。
  - 提出将大规模复杂HVDC系统拆分为多个独立模块化子系统的建模架构，并优化了RTDS库组件的调用策略。
- **Mitigation of Subsynchronous Interactions in Hybrid AC/DC Grid With Renewable En**
  - 💡 利用FPGA硬件并行架构实现EMT与动态仿真的超实时协同计算，从而提前生成最优潮流控制策略以主动抑制次同步相互作用。
  - 提出基于FPGA的超实时仿真平台以抑制含新能源混合电网的次同步相互作用
  - 构建基于功率-电压接口的EMT-动态协同仿真架构实现交直流系统并行计算
- **Real-time RMS-EMT co-simulation and its application in HIL testing of protective**
  - 💡 创新性地利用仿真平台内置输电线路模型作为跨平台接口，结合实时快速曲线拟合算法，实现了无需系统等效简化的多域多速率RMS-EMT协同仿真。
  - 提出了一种利用内置三相输电线路模型实现实时RMS-EMT多域多速率协同仿真的接口技术。
  - 开发了一种非缓冲快速曲线拟合算法，以满足实时仿真中波形到相量转换的严格时间约束。
### 2022年 (3篇)
- **Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic **
  - 💡 提出基于动态电压注入的低延迟交直流协同接口与多FPGA并行架构，实现大规模交直流混合电网超实时硬件仿真与海量故障场景快速评估。
  - 提出基于动态电压注入的交直流协同仿真接口，在维持低硬件延迟的同时实现不同时间步长模型的无缝耦合。
  - 构建并优化多FPGA硬件仿真平台架构，通过合理的任务分配满足大规模电网的超实时计算需求。
- **Interfacing real-time and offline power system simulation tools using UDP or FPG**
  - 💡 创新性地提供了一套兼顾软件灵活性与硬件低延迟的双路径实时-离线仿真工具互联方案，有效弥合了EMT与RMS仿真域之间的性能鸿沟。
  - 提出了一种连接实时EMT仿真系统(RTDS)与离线RMS仿真软件(PSS/E)的协同仿真接口架构。
  - 设计并实现了两种接口方案：纯软件的UDP以太网连接与基于FPGA的Aurora光纤连接，以适应不同延迟与硬件需求。
- **电力系统电磁暂态实时仿真中并行算法的研究**
  - 💡 将网络分割理论与集群并行计算深度融合，突破了传统电磁暂态实时仿真在大规模复杂电网中的计算速度瓶颈。
  - 提出了一种适用于大规模电力系统电磁暂态实时仿真的动态网络分割方法。
  - 设计了基于集群计算机的高效并行计算架构，显著提升了仿真求解速度。
### 2023年 (10篇)
- **Digital twins of multiple energy networks based on real-time simulation using ho**
  - 💡 首次将全纯嵌入法与收敛半径模型结合，提出了一种面向多能网络数字孪生的机理驱动型实时仿真建模方法。
  - 提出了一种基于全纯嵌入法的多能网络模型，利用时间相关全纯函数刻画气、热流的时变动态特性。
  - 构建了收敛半径模型以获取算法的关键收敛信息，从而提升计算性能以满足实时仿真需求。
- **Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of**
  - 💡 提出了一种基于FPGA的EMT与暂态稳定混合建模及动态功率注入接口技术，实现了微电网群的超实时硬件仿真。
  - 提出了一种结合微电网EMT详细建模与交流主网暂态稳定建模的混合仿真框架
  - 设计了动态功率注入接口以实现不同时间尺度仿真模型的无缝耦合与数据交互
- **Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doub**
  - 💡 提出基于虚拟电容等效的定转子解耦方法与FPGA并行流水线架构，实现了双馈发电机数字镜像的超实时仿真。
  - 提出面向异步机定转子T型等效电路解耦的虚拟电容等效法。
  - 设计了基于FPGA的DFIG数字镜像IP核及其内部组件并行算法。
- **Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation**
  - 💡 首次系统对比并验证了常规EMT与小时间步长法在混合SVC-VSC硬件在环仿真中的等效性，为电力电子与无功补偿混合设备的实时建模提供了可靠依据。
  - 提出了适用于混合SVC-VSC的两种HIL实时建模方法（常规EMT与小时间步长法）
  - 验证了两种建模方法在合理处理仿真细节时可产生一致的动态响应结果
- **Lessons learned in porting offline large-scale power system simulation to real-t**
  - 💡 系统性地归纳了离线大规模电力系统向实时仿真环境移植的工程实践、软件适配挑战及建模优化指南。
  - 系统总结了将离线大规模电力系统仿真移植到实时环境的完整流程与经验教训。
  - 详细剖析了移植过程中的软件挑战、建模细节及原理图必要修改。
- **Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Mode**
  - 💡 首次将物理特征神经网络(PFNN)与GRU/EMT分区建模结合，在FPGA上实现了支持1ns步长的WBG器件超快暂态实时硬件在环仿真。
  - 提出基于TLM与GRU/EMT结合的DRM系统级分区建模方法，实现实时硬件在环仿真。
  - 设计新型物理特征神经网络(PFNN)用于WBG器件建模，支持低至1ns的可变步长，显著提升仿真精度与效率。
- **Real-time simulation for detailed wind turbine model based on heterogeneous comp**
  - 💡 提出免重编译的通用FPGA电磁暂态求解器与CPU-FPGA异构协同架构，有效解决了传统仿真平台架构复杂、成本高且难以支持详细风机多物理场实时仿真的难题。
  - 构建了基于CPU-FPGA异构计算的详细风机模型实时仿真平台架构。
  - 在CPU端引入实时操作系统以保障风机气动-机械模型与控制系统的确定性实时计算。
- **Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Ad**
  - 💡 提出基于组件灵敏度分析的自适应混合精度计算架构，在FPGA实时EMT仿真中实现了数值精度与计算资源的最优平衡。
  - 提出了全双精度与自适应混合精度浮点计算方案，有效解决了FPGA长时EMT仿真中的误差累积问题。
  - 开发了可调流水线、动态地址访问及序列控制器技术，优化了高扇出与长数据路径的硬件资源与时序约束。
- **Sparse solver application for parallel real-time electromagnetic transient simul**
  - 💡 首次将支持填充减少、局部重分解与主元选择的直接稀疏求解器与并行化技术深度融合于工业实时EMT仿真平台，在保障数值稳定性的同时实现显著加速。
  - 首次将改进型稀疏求解器MKLU集成至工业级实时仿真软件HYPERSIM中，替代传统代码生成求解器。
  - 系统评估并确定了填充减少、局部重分解与主元选择等稀疏求解技术对加速实时EMT仿真的最优组合。
- **基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计**
  - 💡 提出基于CPU-FPGA异构架构的优化EMTP实时仿真算法，通过恒导纳建模、支路并行拆分与异步通信接口设计，有效突破了小步长电力电子系统实时仿真的计算瓶颈。
  - 搭建了适用于虚拟同步并网逆变器系统的CPU-FPGA异构实时仿真计算平台。
  - 在FPGA端采用恒导纳开关建模、支路拆分并行处理及矩阵化计算优化了EMTP算法的实时性能。
### 2024年 (2篇)
- **High Efficiency Modeling of Multi-Layer Cascaded Dual-Active-Bridge (DAB) Units **
  - 💡 提出了一种将DAB内部H桥、变压器及电容聚合为单一单元的状态空间等效模型，通过精确映射触发脉冲占空比，在保证精度的同时大幅提升了高开关频率级联DAB系统的实时仿真效率。
  - 提出了一种基于状态空间电路法的DAB聚合模型，有效应对高开关频率和大量子模块带来的实时仿真挑战。
  - 将两个H桥变换器、交流变压器及隔直电容整合为单一等效单元，显著降低了系统矩阵维度与计算复杂度。
- **Shifted frequency analysis based, faster-than-real-time simulation of power syst**
  - 💡 将移频分析与延迟线性多步法结合，并通过图级线程安全设计与异构编译层，在GPU上实现了高可扩展的超实时电力系统电磁暂态仿真框架。
  - 提出基于延迟的线性多步复合方法，利用GPU加速电力系统电磁暂态仿真。
  - 采用移频分析建模技术，有效平衡了大规模系统仿真的计算负载与精度需求。
### 2025年 (9篇)
- **A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation**
  - 💡 提出无需查表求逆的磁链定义电流导数计算方法，结合高效插值与外推稳定策略，实现了高精度FEA数据驱动的PMSM实时EMT仿真。
  - 提出了一种基于FEA磁链数据直接计算电流导数的新方法，避免了传统方法中耗时的查表求逆过程。
  - 提供了完整的数学证明，并设计了一种高效的三线性插值方法以提升实时计算效率。
- **Design and Implementation of Scalable Communication Interfaces for Reliable and **
  - 💡 提出了一种兼顾本地低延迟与远程可扩展性的双模通信接口架构，有效突破了多速率电力系统实时协同仿真中的同步延迟与稳定性瓶颈。
  - 提出了一种面向高IBR渗透率电力系统的可扩展实时协同仿真通信接口架构
  - 设计了本地低延迟与远程互联网两种通信模式以灵活适配不同仿真场景
- **Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources fo**
  - 💡 提出离散阻抗建模技术，通过构建戴维南等效电路实现VSC与状态变量EMT仿真器的高效接口，兼顾高精度与大时间步长计算。
  - 提出离散阻抗建模(DIBM)方法，将VSC系统转化为拉普拉斯域导纳模型并进行离散化处理。
  - 构建戴维南等效阻抗矩阵与历史电压源，实现VSC子系统与外部状态变量仿真器的无缝接口。
- **Fine-grained hardware resource optimization and design for FPGA-based real-time **
  - 💡 提出算术运算级细粒度资源优化与自动HDL生成方法，实现大规模REG控制系统的高效FPGA实时仿真。
  - 构建算术运算级硬件资源需求模型，统筹最小求解时间与资源约束。
  - 提出自动硬件描述语言生成方法，实现REG控制模块的快速硬件部署。
- **FPGA-based simulation of grid-tied converters using frequency-dependent network **
  - 💡 将频率相关网络等效(FDNE)降阶技术与FPGA硬件并行架构深度融合，实现了兼顾高精度、低延迟与高可扩展性的并网变换器实时电磁暂态仿真。
  - 提出了一种基于FPGA的并网变换器实时电磁暂态仿真框架。
  - 引入FDNE技术将非研究区域电网等效为频率相关导纳模型，显著降低了仿真计算规模。
- **Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromag**
  - 💡 将延迟解耦技术与M-NFSS算法深度融合，在保留DFIG风电场内部动态细节的前提下，实现了节点数与硬件资源消耗的大幅削减。
  - 提出了一种结合延迟解耦与M-NFSS算法的DFIG风电场实时电磁暂态建模方法。
  - 在大幅降低电路节点数量的同时，完整保留了风电场内部的电气拓扑与控制细节。
- **MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB**
  - 💡 提出了一种基于MATLAB的MTOF自动代码生成工具箱，将复杂的FPGA底层编程转化为透明、可读的浮点运算代码，大幅降低了实时EMT仿真的开发门槛与时间成本。
  - 开发了MATLAB环境下的MTOF工具箱，可自动生成透明且无需底层复杂编程的FPGA代码。
  - 在FPGA上实现了高精度浮点运算与可读数据格式，保障了EMT仿真的计算精度。
- **Su 等 | A fixed-admittance algorithm for the FPGA-based microsecond-level nonline**
  - 💡 提出虚拟元件与固定导纳算法，通过局部等效变换维持全局导纳矩阵恒定，实现无迭代、无解耦的微秒级非线性实时仿真。
  - 提出虚拟元件概念，通过等效电路变换保持非线性仿真中的系统导纳矩阵恒定。
  - 开发VC-EMT方法，有效避免了传统非线性求解中的网络解耦、多次迭代及补偿滞后问题。
- **基于FPGA的变电站实时仿真培训系统**
  - 💡 融合节点排序优化、细粒度指令流并行架构与参数间接修改技术，突破了传统FPGA仿真资源闲置与计算瓶颈，实现了大规模变电站电磁暂态模型的低成本、高实时性运行。
  - 提出最小度最大独立集法优化节点消去与电压计算顺序，有效平衡计算负载与并行度。
  - 设计多输入多输出指令流运算器实现细粒度并行计算，显著提升FPGA硬件资源利用率。
### 2026年 (3篇)
- **27&28/Multi-rate real time hybrid simulation of controllable line commutated con**
  - 💡 提出CPU-FPGA协同多速率架构与离散电感解耦方法，结合最小损耗误差参数优化策略，有效突破了CLCC-HVDC系统多时间尺度动态实时仿真的计算瓶颈。
  - 提出了一种面向CLCC-HVDC系统的CPU-FPGA协同多速率实时仿真框架。
  - 提出了一种将电感作为自然解耦边界的离散电感解耦方法以实现拓扑分割。
- **A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-Sta**
  - 💡 将隐式-显式Gear多步积分法与开关函数等效模型结合，并引入开关插值技术，实现了SST电磁暂态仿真中恒定导纳矩阵、节点缩减与高精度实时计算的统一。
  - 提出基于ImEx Gear积分法的开关函数详细等效模型，用于高效精确的EMT仿真。
  - 利用ImEx求解器实现变换器电路解耦、节点数量缩减及恒定网络导纳矩阵构建。
- **Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production: Time-Step-Op**
  - 💡 提出RMTE框架实现异构物理域最优时间步长自适应选择，突破传统EMT工具在多域实时协同仿真中的效率与稳定性瓶颈。
  - 提出RMTE框架，有效解决多物理域耦合仿真中因时间常数差异导致的数值稳定性偏移问题。
  - 设计快速自适应的最优最大时间步长选择算法，实现异构物理域的高效协同计算。
## 关键发现汇总
- [2004] **Multiprocessor based generator module for a real-time power **: 四核并行架构成功将仿真步长压缩至满足模拟同步基实时性要求的极小值。
- [2004] **Multiprocessor based generator module for a real-time power **: 浮点运算的应用有效抑制了累积数值误差，保证了发电机动态响应的仿真精度。
- [2004] **Multiprocessor based generator module for a real-time power **: 与离线EMTP程序的对比结果表明，该模块在典型工况下的仿真精度满足工程分析需求。
- [2004] **Real-time digital simulator of the electromagnetic transient**: 成功实现了输电线路在平衡及不平衡电源激励下的电磁暂态实时仿真。
- [2004] **Real-time digital simulator of the electromagnetic transient**: 实时仿真结果与EMTP离线仿真结果高度吻合，验证了算法的准确性。
- [2004] **Real-time digital simulator of the electromagnetic transient**: 该数字模型可有效替代传统大量无源网络节段，显著节省硬件空间并降低成本。
- [2007] **Real-Time Transient Simulation Based on a Robust**: 成功以20 μs步长对阿尔伯塔大型互联电力系统实现了实时电磁暂态仿真。
- [2007] **Real-Time Transient Simulation Based on a Robust**: 示波器捕获的实时波形与ATP离线全模型仿真结果高度吻合，验证了所提模型的高精度与计算效率。
- [2009] **FPGA-Based Real-Time EMTP**: 在12.5 ns时钟周期下实现了12 μs的仿真步长，满足高频电磁暂态的精确捕捉需求。
- [2009] **FPGA-Based Real-Time EMTP**: 实时示波器采集的波形与ATP离线仿真结果高度吻合，验证了仿真器的高精度。
- [2009] **FPGA-Based Real-Time EMTP**: 单片FPGA成功承载15条输电线路全频变模型的并行计算，具备高数据吞吐能力。
- [2009] **The Computer Simulation and Real-Time Stabilization Control **: LQR状态反馈控制器成功实现了倒立摆角度与小车位置的快速并行稳定控制。
- [2009] **The Computer Simulation and Real-Time Stabilization Control **: 实时控制实验结果与计算机仿真结果高度一致，验证了理论分析与模型的正确性。
- [2011] **An Iterative Real-Time Nonlinear Electromagnetic Transient S**: 成功实现了串联补偿线路避雷器暂态（5μs步长）和变压器铁磁谐振暂态（3μs步长）的实时仿真。
- [2011] **An Iterative Real-Time Nonlinear Electromagnetic Transient S**: FPGA硬件捕获的实时示波器波形与ATP离线仿真结果高度一致，证明了求解器的高精度。
- [2011] **An Iterative Real-Time Nonlinear Electromagnetic Transient S**: 并行迭代架构有效克服了牛顿-拉夫逊法在实时系统中的收敛不确定性及计算耗时问题。
- [2011] **Massively Parallel Implementation of AC Machine Modeling for**: 在FPGA上实现了单步计算时间仅为44 ns的实时仿真性能。
- [2011] **Massively Parallel Implementation of AC Machine Modeling for**: 成功验证了PMSM与感应电机驱动系统模型，在保证数值稳定性的同时未牺牲仿真精度。
- [2012] **The Reconﬁgurable-Hardware Real-Time and**: 单步计算时间低至24 ns，为当时文献报道的最低值。
- [2012] **The Reconﬁgurable-Hardware Real-Time and**: 成功在实时与超实时模式下完成实际规模电力系统的电磁暂态仿真验证。
- [2012] **The Reconﬁgurable-Hardware Real-Time and**: 有效扩展了仿真频率带宽并提升了模型精度，克服了传统实时仿真器的局限。
- [2016] **Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr**: FPGA模型实现了最低延迟与最小硬件资源消耗下的准确实时仿真
- [2016] **Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr**: 磁等效电路模型能够精确反映铁芯饱和、磁滞及涡流等非线性特性
- [2016] **Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr**: 实时仿真结果与JMAG 3D有限元仿真结果高度吻合
- [2018] **Real-Time FPGA-RTDS Co-Simulator for Power Systems**: 双区域四机系统协同仿真结果与全RTDS仿真结果高度一致，验证了接口设计的准确性。
- [2018] **Real-Time FPGA-RTDS Co-Simulator for Power Systems**: 平台成功在FPGA上实现了141节点大规模电力系统的实时仿真，证明了其强大的扩展能力与计算效率。
- [2018] **Real-time Simulation of Hybrid Modular Multilevel Converters**: 模型计算量与子模块数量基本解耦，大幅降低了大规模MMC的实时仿真负担。
- [2018] **Real-time Simulation of Hybrid Modular Multilevel Converters**: FPGA实现成功捕获了系统级与子模块级的详细电磁暂态响应。
- [2018] **Real-time Simulation of Hybrid Modular Multilevel Converters**: 在两端LVDC测试系统上的验证表明，该方法在精度与计算效率上均优于传统模型。
- [2019] **Modeling a voltage source converter assisted resonant curren**: 所建模型的外部电流-电压特性与真实设备高度一致。

## 深度增强内容

 ---
title: "实时仿真"
type: topic
tags: ["EMT", "HIL", "FPGA", "GPU", "Parallel Computing", "Fixed-Admittance", "Multi-Rate"]
created: "2026-04-13"
---

# 实时仿真

## 论文方法分析
> 基于 52 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|
| 电磁暂态(EMT)建模 | 3 | Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies fo |
| 补偿法 | 2 | An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on F |
| FPGA硬件实现 | 2 | Development of phase domain frequency-dependent transmission line mode |
| VHDL编程 | 2 | Development of phase domain frequency-dependent transmission line mode |
| FPGA实时仿真 | 2 | FPGA-based simulation of grid-tied converters using frequency-dependen |
| 浮点运算 | 2 | High performance computing engines for the FPGA-based simulation of th |
| CPU-FPGA协同多速率实时仿真框架 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 离散电感解耦方法 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 关联离散电路模型解析参数选择策略 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 最小损耗误差准则优化 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
| 基于FEA数据的降阶建模(ROM) | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 磁链定义法(Flux-Defined) | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 高效三线性插值算法 | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 电流导数直接计算法(免查表求逆) | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 开关函数详细等效模型(SFB-DEM) | 1 | A Numerically Efficient and Accurate Model for Real-Time Simulation of |

### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|
| 负载 | 3 |
| 变压器 | 3 |
| 模块化多电平换流器(MMC) | 3 |
| 串联补偿线路 | 2 |
| 光伏阵列 | 2 |
| 同步发电机 | 2 |
| 双馈感应发电机(DFIG) | 2 |
| 电力电子变换器 | 2 |
| 风力发电机(WT) | 2 |
| 输电线路 | 2 |
| 风电场 | 2 |
| 可控线路换相换流器高压直流系统(CLCC-HVDC) | 1 |
| CLCC换流器阀组 | 1 |
| 永磁同步电机(PMSM) | 1 |
| 电动汽车(EV)动力总成 | 1 |

### 验证方式分布
- **仿真对比**: 5 篇
- **仿真**: 5 篇
- **仿真/对比**: 5 篇
- **仿真与对比**: 3 篇
- **实验验证与CPU离线仿真对比**: 1 篇
- **仿真与硬件实验对比**: 1 篇
- **仿真与MATLAB对比验证**: 1 篇
- **实验与仿真对比**: 1 篇
- **仿真与硬件在环(HIL)实验**: 1 篇
- **仿真对比验证**: 1 篇
- **仿真验证与对比**: 1 篇
- **仿真与FPGA硬件实验验证**: 1 篇
- **硬件仿真与商业软件(DSATools/TSAT)对比验证**: 1 篇
- **实验**: 1 篇
- **硬件实验与离线仿真对比**: 1 篇
- **仿真验证与FPGA硬件实现对比**: 1 篇
- **实时仿真器仿真验证与详细模型对比**: 1 篇
- **仿真与FPGA硬件实现验证**: 1 篇
- **硬件在环(HIL)实时仿真与双模型对比**: 1 篇
- **仿真与硬件在环实验（HIL）及现场工程验证**: 1 篇
- **实时仿真波形对比与性能评估**: 1 篇
- **FPGA硬件实验验证**: 1 篇
- **仿真对比验证（与Matlab/Simulink离线仿真结果对比）**: 1 篇
- **仿真与硬件实验验证**: 1 篇
- **对比**: 1 篇
- **FPGA硬件实时仿真与案例验证**: 1 篇
- **仿真对比与硬件实验验证**: 1 篇
- **仿真与硬件在环实验**: 1 篇
- **仿真与实验**: 1 篇
- **仿真验证**: 1 篇
- **HIL硬件在环实验与离线仿真对比**: 1 篇
- **实时仿真与离线ATP对比及示波器实测**: 1 篇
- **仿真与基准测试对比**: 1 篇
- **HIL硬件在环仿真与对比验证**: 1 篇
- **仿真与对比验证**: 1 篇
- **仿真与实物实验对比**: 1 篇
- **仿真/案例验证**: 1 篇
- **硬件在环实验与仿真对比**: 1 篇

## 技术演进脉络
### 2004年 (2篇)
- **Multiprocessor based generator module for a real-time power system simulator - P**
  - 💡 将多微处理器并行计算与模拟三相正弦振荡器相结合，构建了可通过软件编程灵活配置、步长极小且精度高的混合式实时发电机仿真模块。
  - 开发了基于多微处理器的实时发电机仿真模块，仅需修改程序

---

## 1. 关键技术详解

### 1.1 电磁暂态(EMT)实时仿真的数学基础

实时EMT仿真的核心在于将连续时间的微分-代数方程组(DAEs)离散化为差分方程，并在固定步长 $\Delta t$ 内完成求解。基于梯形积分法(Trapezoidal Rule)，电感 $L$ 和电容 $C$ 的Companion Circuit模型可表示为：

$$
\begin{aligned}
\text{电感:} \quad i_L(t) &= \frac{\Delta t}{2L}v_L(t) + \underbrace{\left[i_L(t-\Delta t) + \frac{\Delta t}{2L}v_L(t-\Delta t)\right]}_{I_{hist}(t-\Delta t)} \\
\text{电容:} \quad i_C(t) &= \frac{2C}{\Delta t}v_C(t) - \underbrace{\left[\frac{2C}{\Delta t}v_C(t-\Delta t) + i_C(t-\Delta t)\right]}_{I_{hist}(t-\Delta t)}
\end{aligned}
$$

由此构建的导纳矩阵方程为：
$$
\mathbf{Y} \cdot \mathbf{v}(t) = \mathbf{i}(t) + \mathbf{i}_{hist}(t-\Delta t)
$$

**实时性约束**：求解必须在 $\Delta t$ 内完成，即 $T_{solve} < \Delta t$。这要求：
1. 导纳矩阵 $\mathbf{Y}$ 的因子化（Factorization）必须避免在每一步长内重复进行
2. 采用稀疏矩阵技术减少计算量
3. 利用并行计算架构分摊计算负载

### 1.2 恒导纳矩阵(Fixed-Admittance)技术

针对电力电子开关动作导致的导纳矩阵频繁重构问题，恒导纳算法通过**关联离散电路(ADC)** 模型将非线性元件等效为固定导纳并联历史电流源：

$$
\mathbf{Y}_{fixed} \cdot \mathbf{v}(t) = \mathbf{i}_{hist}(t-\Delta t) + \mathbf{i}_{nl}(t)
$$

其中非线性补偿电流 $\mathbf{i}_{nl}(t)$ 通过迭代或预测-校正机制确定。对于混合式直流断路器(DCCB)中的金属氧化物限压器(MOV)，其非线性特性 $i_{MOV} = f(v_{MOV})$ 被重构为：

$$
Y_{fixed} = \frac{\Delta t}{2L_{eq}} \quad (\text{固定})
$$

$$
I_{MOV}(t) = f(v_{MOV}(t)) - Y_{fixed} \cdot v_{MOV}(t) + I_{hist}(t-\Delta t)
$$

该技术将计算复杂度从 $O(n^3)$ 的LU分解降低为 $O(n^2)$ 的前代回代(Forward/Backward Substitution)，在1μs步长下实现500kV/25kA DCCB的实时仿真，误差<0.5%。

### 1.3 移频分析(SFA)与动态相量法

对于含新能源的大规模电网，传统EMT仿真需极小步长（10-50μs）捕捉宽频动态。移频分析(Shifted Frequency Analysis, SFA)通过提取信号的慢变包络 $\bar{x}(t)$：

$$
x(t) = \text{Re}\{\bar{x}(t) \cdot e^{j\omega_s t}\}
$$

将原始信号搬移至基频 $\omega_s$ 附近，允许使用**大5-10倍的仿真步长**（50-100μs），同时保持基波动态精度。其离散化后的网络方程为：

$$
\mathbf{Y}_{SFA}(\omega_s) \cdot \bar{\mathbf{v}}(t) = \bar{\mathbf{i}}(t) + \text{历史项}(\omega_s, \Delta t)
$$

在GPU实现中，通过线程安全的图遍历算法避免原子操作，内存带宽利用率可达理论峰值的70-90%，支持数千节点系统的**超实时(Faster-Than-Real-Time)** 仿真。

### 1.4 稀疏求解器优化策略

针对大规模电网（>1000节点），稀疏线性求解器采用以下优化：

**填充元减少(Fill-in Reduction)**：采用Minimum Degree (MD) 或 Nested Dissection 排序算法，减少LU分解产生的非零元注入。

**部分重分解(Partial Refactorization)**：将导纳矩阵分块为：
$$
\mathbf{Y} = \begin{bmatrix} 
\mathbf{Y}_{cc} & \mathbf{Y}_{cv} \\
\mathbf{Y}_{vc} & \mathbf{Y}_{v}(t)
\end{bmatrix}
$$
其中 $\mathbf{Y}_{cc}$ 对应线性元件（恒定），$\mathbf{Y}_{v}(t)$ 对应时变元件（开关、非线性）。每步仅需重分解右下角 $\mathbf{Y}_{v}$ 块，计算速度提升可达50%。

**部分选主元(Partial Pivoting)**：对含开关电阻 $R_{open}/R_{close}$（差异达 $10^6$ 量级）的系统，维持数值稳定性至关重要。

### 1.5 多速率实时仿真

当系统包含多时间尺度元件（如慢动态的发电机控制与快动态的电力电子开关），采用CPU-FPGA协同的多速率框架：

- **CPU**：处理慢子系统（步长 $\Delta t_1 = 100-500\mu s$），运行复杂控制算法
- **FPGA**：处理快子系统（步长 $\Delta t_2 = 1-10\mu s$），利用离散电感解耦方法实现流水线并行

接口处采用**插值/外推**或**解析参数选择策略**（基于最小损耗误差准则）保证数据交换的数值稳定性。

---

## 2. 硬件平台对比

| 平台类型 | 典型时间步长 | 可扩展性 | 编程复杂度 | 适用场景 | 性能特征 |
|---------|-------------|---------|-----------|---------|---------|
| **FPGA** (Xilinx/Intel) | 1-10 μs | 受限（逻辑单元、DSP切片） | 高（VHDL/Verilog，定点/浮点优化） | 电力电子开关、保护装置、MMC阀控 | 确定性延迟，真并行，适合纳秒级开关过程 |
| **GPU** (NVIDIA/AMD) | 10-100 μs | 极高（数千节点，显存限制） | 中（CUDA/ROCm/OpenCL，线程优化） | 大规模电网EMT、风电场聚合、宽频分析 | 超实时能力强，适合批处理与蒙特卡洛分析 |
| **多核CPU** (x86/ARM) | 10-50 μs | 中（NUMA架构，缓存一致性约束） | 低（OpenMP/MPI，C/C++） | 传统输电网、工业HIL测试 | 任务分配灵活，适合复杂控制逻辑与I/O交互 |
| **混合架构** (CPU+FPGA) | 多速率（1-100 μs） | 极高 | 极高（协同设计，接口同步） | 全系统HIL、混合HVDC、微电网 | 兼顾灵活性与实时性，需解决异构通信开销 |
| **专用仿真器** (RTDS/eMEGAsim) | 10-50 μs | 中（专有硬件卡限制） | 低（图形化建模，自动代码生成） | 工业级HIL测试、继电保护验证 | 商用支持完善，符合IEC 61850等标准 |

**关键技术指标对比**：
- **计算密度**：FPGA > GPU > CPU（针对固定结构并行任务）
- **灵活性**：CPU > GPU > FPGA（针对算法变更与调试）
- **I/O确定性**：FPGA > 专用仿真器 > CPU > GPU

---

## 3. 实际应用案例汇总

### 3.1 高压直流输电系统实时仿真

**Nelson River多馈入HVDC系统**（加拿大Manitoba Hydro）
- **规模**：Bipole I/II承载总发电量70%，直流线路全长900km；Dorsey换流站原含14阀组+9台同步调相机
- **技术方案**：RTDS软件系统与Bipole III物理控制器构成混合HIL；采用模块化建模，阀组等效简化后单计算组实现无延迟仿真
- **验证结果**：成功支撑现场调试，分级交流故障测试验证高保真度，替代超过100个PSCAD自定义模块，显著降低工程风险

### 3.2 直流断路器微秒级暂态仿真

**500kV/25kA混合式DCCB**
- **技术挑战**：开断过程涉及μs级电弧与kA/μs电流变化率，传统仿真步长（>10μs）无法捕捉
- **实现方案**：FPGA-based固定导纳算法，1μs步长，避免导纳矩阵重构与迭代
- **性能指标**：与PSCAD/EMTDC对比误差<0.5%，支持连续、非周期性参数变化（如MOV特性突变）

### 3.3 大规模输电网超实时仿真

**3486母线TSO电网**
- **硬件**：SGI UV100，96处理器，异构NUMA架构（机箱间延迟65ns，核间10ns）
- **算法**：高效任务分配算法（优于A*算法），负载不平衡率约束 $\delta = 0.01$
- **性能**：40μs步长下实现实时仿真，任务映射算法执行时间<几秒，验证极大规模电网实时可行性

### 3.4 配电网与微电网并行仿真

**619节点Xavier配电网 / 663节点GHOST微电网**
- **技术**：稀疏求解器优化（填充元减少+部分重分解）
- **步长**：50-100μs稳定运行，满足HIL需求
- **加速比**：相比传统全重分解方法，计算速度提升50%

### 3.5 新能源并网宽频分析

**基于GPU的移频分析(SFA)**
- **规模**：支持数百至数千节点，含风电、光伏、MMC等
- **特征**：利用共享内存与合并内存访问(coalesced memory access)，跨平台支持NVIDIA(CUDA)与AMD(ROCm)，性能损失<5%
- **应用**：硬件在环测试中的超实时仿真，允许控制参数在线优化与风险评估

---

## 4. 研究趋势与开放问题

### 4.1 前沿研究方向

**异构超实时仿真架构**
- 探索CPU-FPGA-GPU三层异构架构，其中CPU处理事件驱动逻辑，FPGA处理电力电子开关，GPU处理电磁暂态网络求解
- 研究基于**统一虚拟内存(UVM)** 的零拷贝数据传输，降低异构间通信延迟

**数据驱动的降阶建模(ROM)**
- 基于有限元分析(FEA)数据构建PMSM等复杂电机的实时仿真模型，采用**磁链定义法(Flux-Defined)** 与三线性插值算法，避免在线查表求逆
- 结合物理信息神经网络(PINN)构建非线性元件的紧凑模型，平衡精度与计算速度

**多物理场实时耦合**
- 电磁-热-机械暂态联合实时仿真，适用于电缆热老化分析与GIL机械故障预测
- 挑战：不同物理场时间常数差异巨大（电磁μs级 vs 热s级），需开发自适应多速率接口算法

### 4.2 开放技术问题

**开关动作数值稳定性与实时性权衡**
- 理想开关模型导致导纳矩阵病态条件数，而电阻模型引入寄生振荡
- **开放问题**：如何在固定步长约束下，实现开关动作的精确插值与数值振荡抑制，同时保证实时性？

**大规模系统的可扩展性瓶颈**
- 随着电网规模增至10,000+节点，稀疏矩阵求解的通信开销（分布式内存架构）可能超过计算开销
- **开放问题**：如何设计通信避免(Communication-Avoiding)算法，或利用近似计算(Inexact Computing)在保证稳定性的前提下牺牲部分精度换取实时性？

**标准化与互操作性**
- 当前各厂商实时仿真器（RTDS、Typhoon HIL、dSPACE）采用专有模型格式与接口协议
- **开放问题**：建立基于FMI(Functional Mock-up Interface)的电力系统实时仿真标准，实现跨平台模型复用与协同仿真

**AI增强的实时仿真**
- 利用深度学习预测非线性区域或故障后的系统轨迹，跳过部分时间步计算
- **开放问题**：如何保证AI预测误差在实时仿真中的可接受性与可恢复性？

**量子计算在电力系统实时仿真的应用前景**
- 探索量子线性求解器(Quantum Linear Systems Algorithm, QLSA)在超大规模电网导纳矩阵求解中的潜在优势，当前仍处于理论可行性研究阶段。

## 深度增强内容

 ---
title: "实时仿真"
type: topic
tags: ["EMT", "HIL", "FPGA", "GPU", "多速率仿真", "并行计算", "超实时仿真"]
created: "2026-04-13"
---

# 实时仿真

## 1. 关键技术详解

### 1.1 电磁暂态实时仿真的数学基础

电力系统实时电磁暂态(EMT)仿真基于Dommel的节点分析法，在每个仿真步长$\Delta t$内求解以下线性代数方程组：

$$Y(t)V(t) = I(t) + I_{hist}(t-\Delta t)$$

其中$Y(t)$为节点导纳矩阵，$V(t)$为节点电压向量，$I(t)$为当前注入电流源，$I_{hist}(t-\Delta t)$为历史电流源项，反映电感、电容等储能元件的记忆特性。

对于电感元件，其离散伴随电路模型为：
$$i_L(t) = \frac{\Delta t}{2L}v_L(t) + i_L(t-\Delta t) + \frac{\Delta t}{2L}v_L(t-\Delta t)$$

### 1.2 恒导纳矩阵与关联离散电路(ADC)模型

为解决开关动作导致的导纳矩阵重构问题，恒导纳算法采用**关联离散电路(Associated Discrete Circuit, ADC)**模型，将非线性元件等效为恒定导纳并联历史电流源：

$$I_{k} = Y_{eq}V_{k} + J_{k-1}$$

其中$Y_{eq}$为固定等效导纳，$J_{k-1}$为历史电流源项。对于混合式直流断路器(DCCB)中的金属氧化物避雷器(MOV)等非线性电阻，通过虚拟构造技术(Virtual Construction)在FPGA中实现参数连续变化，避免了传统补偿法的迭代需求，将计算复杂度从$O(n^3)$的LU分解降低为$O(n^2)$的前代回代运算。

### 1.3 移频分析法(Shifted Frequency Analysis, SFA)

针对大规模系统仿真，SFA技术通过频谱搬移将快变信号转换为慢变包络：

$$x(t) = \text{Re}\{\bar{x}(t)e^{j\omega_0 t}\}$$

其中$\bar{x}(t)$为复包络（动态相量），$\omega_0$为基波角频率。该方法允许使用比传统EMT仿真大**5-10倍**的步长（如从10μs增至50-100μs），同时保持基波动态精度。在GPU实现中，通过图着色算法避免原子操作，实现线程安全并行，内存带宽利用率可达设备理论峰值的70-90%。

### 1.4 稀疏求解器优化技术

对于大规模电网实时仿真，稀疏线性求解器采用以下优化策略：

**填充元减少(Fill-in Reduction)**：通过最小度排序(Minimum Degree)或嵌套剖分(Nested Dissection)算法，降低LU分解产生的非零元注入。

**部分重分解(Partial Refactorization)**：将导纳矩阵分块为时不变部分$Y_c$和时变部分$Y_v$：

$$Y = \begin{bmatrix} Y_c & Y_{cv} \\ Y_{vc} & Y_v \end{bmatrix}$$

仅对右下角$Y_v$块进行重分解，结合部分选主元(Partial Pivoting)技术，在保证数值稳定性的同时，计算速度提升最高达**50%**。

### 1.5 多速率实时仿真与异构协同

复杂电力系统采用多速率策略，将网络划分为不同子系统：

- **快子系统**（电力电子、保护装置）：步长$1-10\mu s$，部署于FPGA
- **慢子系统**（输电网、传统机组）：步长$40-100\mu s$，运行于CPU

接口处采用**离散电感解耦方法**或**插值算法**实现数据交换。CPU-FPGA协同框架通过关联离散电路模型解析参数选择策略，基于最小损耗误差准则优化接口参数，确保数值稳定性。

## 2. 硬件平台对比

| 平台类型 | 代表硬件 | 典型步长 | 适用规模 | 核心技术特点 | 主要局限 |
|---------|---------|---------|---------|--------------|----------|
| **FPGA** | Xilinx Virtex UltraScale+ | $1-10\mu s$ | 电力电子详细模型<br>(MMC子模块级) | 确定性并行架构<br>支持VHDL/Verilog定制<br>浮点/定点混合运算 | 开发周期长<br>逻辑资源受限<br>大规模系统布线困难 |
| **GPU** | NVIDIA A100/AMD MI200 | $10-100\mu s$ | 数千节点<br>(配电网/微电网) | 海量线程并行<br>高内存带宽(>1TB/s)<br>CUDA/ROCm异构支持 | 线程同步开销<br>原子操作性能退化<br>实时确定性较弱 |
| **多核CPU** | SGI UV100<br>Intel Xeon Scalable | $40-100\mu s$ | 数千母线<br>(输电网级) | 缓存一致性架构<br>任务分配灵活<br>标准数学库支持 | 核间通信延迟<br>缓存未命中<br>Amdahl定律限制 |
| **商业实时仿真器** | RTDS<br>OPAL-RT<br>Typhoon HIL | $10-50\mu s$ | 中等规模<br>(换流站/风电场) | 成熟HIL接口<br>标准模型库<br>自动化工具链 | 硬件成本高<br>模型定制受限<br>扩展性固定 |
| **混合架构** | CPU+FPGA<br>GPU+FPGA | 多速率<br>(异步) | 大规模混合系统<br>(HVDC+交流网) | 分层并行<br>专用硬件加速<br>资源优化配置 | 接口同步复杂<br>时钟域交叉问题<br>数据一致性挑战 |

## 3. 实际应用案例汇总

### 案例1：Nelson River多馈入HVDC系统混合实时仿真
- **应用场景**：Manitoba Hydro Bipole III现场调试
- **系统规模**：Bipole I/II承载总发电量**70%**，直流线路全长**900km**
- **技术方案**：
  - RTDS软件系统与Bipole III物理控制器构成HIL闭环
  - Dorsey换流站建模优化：将14个阀组与9台同步调相机等效简化，突破单计算组算力限制
  - 控制模块采用RTDS标准库重构，替代原PSCAD/EMTDC中**100+**个自定义模块
- **验证成果**：分级交流故障测试验证高保真度，显著降低工程调试风险与成本

### 案例2：500kV混合式直流断路器微秒级仿真
- **应用场景**：高压直流电网故障保护测试
- **技术参数**：
  - 额定电压**500kV**，开断电流**25kA**
  - 时间步长**1μs**，满足微秒级暂态过程捕捉
- **算法创新**：
  - 恒导纳ADC模型避免导纳矩阵重构
  - 支持MOV特性连续、非周期性变化（故障清除过程）
  - 无需插值抑制数值振荡
- **精度指标**：与PSCAD/EMTDC基准对比，最大误差**<0.5%**（快速暂态kA/μs或kV/μs应力条件下）

### 案例3：超大规模输电网并行实时仿真
- **系统规模**：**3486**个母线、**1056**条线路、**274**台变压器
- **硬件平台**：SGI UV100（96处理器），异构通信架构（机箱间/刀片间/插槽间/核间）
- **算法性能**：
  - 实时步长**40μs**
  - 负载不平衡率(LIR)约束$\delta = 0.01$
  - 任务映射算法执行时间**<几秒**（优于传统A*算法）
- **应用价值**：验证TSO（输电系统运营商）级电网实时仿真可行性

### 案例4：GPU加速超实时仿真平台
- **技术路线**：Shifted Frequency Analysis + 图并行计算
- **系统支持**：数百至数千节点电力系统
- **性能特征**：
  - 实现**Faster-than-Real-Time**仿真能力
  - 线程安全设计避免原子操作（传统方法可降低GPU利用率30-50%）
  - 跨平台支持：NVIDIA(CUDA)与AMD(ROCm)性能损失**<5%**
- **适用场景**：硬件在环(HIL)测试前的快速预筛选、在线安全评估

### 案例5：永磁同步电机(PMSM)高精度实时建模
- **应用对象**：电动汽车(EV)动力总成
- **建模方法**：
  - 基于FEA数据的降阶建模(ROM)
  - 磁链定义法(Flux-Defined)替代传统查表法
  - 高效三线性插值算法 + 电流导数直接计算法（免查表求逆）
- **实现平台**：FPGA实时仿真器
- **技术优势**：兼顾有限元分析(FEA)精度与实时仿真速度

## 4. 研究趋势与开放问题

### 4.1 前沿研究趋势

**超实时仿真与预测性分析**
- **Faster-than-Real-Time (FTRT)**技术结合暂态能量函数，实现 contingencies 快速筛选
- 基于实时仿真的**数字孪生**框架，支持电力系统在线状态评估与预测性维护
- AI/ML算法嵌入实时仿真回路，实现自适应步长控制与智能降阶

**异构计算架构深度融合**
- **CPU-GPU-FPGA三层架构**的统一编程模型（如SYCL、OpenCL），实现任务自动划分与负载均衡
- 片上系统(SoC)集成方案（如Xilinx Zynq UltraScale+ MPSoC），ARM处理器与可编程逻辑紧密耦合
- 光互连技术降低多处理器间通信延迟，支持更大规模并行

**电力电子详细模型实时化突破**
- MMC换流器子模块级详细建模（数千子模块）的实时仿真，支持阀级控制策略验证
- 多物理场耦合实时仿真（电磁-热-机械应力联合仿真）
- 宽频带模型（涵盖kHz至MHz级振荡）的实时计算

### 4.2 关键开放问题

**数值稳定性与计算效率的权衡**
- 大步长（$>50\mu s$）仿真中，开关动作时刻的**数值振荡抑制**与**实时性约束**矛盾
- 多速率接口处的**插值误差累积**与**能量守恒**问题，特别是在含电力电子开关的 stiff 系统中

**大规模系统并行效率瓶颈**
- 随着节点数增加至**10,000+**，稀疏求解器的通信开销成为瓶颈，需开发**通信避免(Communication-Avoiding)**算法
- 异构平台间**任务调度**与**内存一致性**管理的自动化工具缺失，依赖专家经验手动优化

**硬件在环的同步与延迟补偿**
- 物理控制器与仿真器间的**接口延迟**（通常$1-50\mu s$）精确补偿，特别是在高频电力电子控制中
- **多物理域HIL**（机械、热、电磁联合）的实时同步机制

**模型保真度与实时性的自适应平衡**
- 在线模型降阶(Online Model Order Reduction)的**稳定性保证**与**误差边界**控制
- 基于运行工况的**多 fidelity 模型自动切换**策略

**实时数据同化与状态估计**
- 如何将PMU实测数据实时融入EMT仿真（**动态状态估计**+**仿真校正**）
- 非高斯噪声与坏数据情况下的**鲁棒实时仿真**算法

---

**参考文献关联**：本主题内容基于52篇核心论文分析，涵盖2004年至2025年的技术演进，从早期多微处理器混合仿真到现代GPU/FPGA异构加速，反映了电力系统实时仿真技术从**微秒级细节**到**超大规模系统**的全谱系发展。
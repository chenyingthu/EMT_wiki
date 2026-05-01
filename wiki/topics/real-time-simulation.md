---
title: "实时仿真"
type: topic
tags: []
created: "2026-04-13"
---

# 实时仿真

## 定义
实时仿真要求每个仿真步在真实时间截止期限内完成，并能与控制器、保护装置或硬件在环系统交换信号。与普通离线 EMT 相比，它首先受固定步长、确定性调度、I/O 延迟和硬件资源约束。

## 合成定位
在 P0 taxonomy 中，实时仿真是模型精度、计算架构和工程验证的交汇点。它依赖 [[parallel-computing]]、[[multirate-method]]、[[fixed-admittance]]、[[state-space-method]]、[[frequency-dependent-modeling]]，并经常与 [[co-simulation]] 和 HIL 测试共同出现。

## 分类或机制
- 数字实时 EMT：在 CPU、RTDS、FPGA 或 MPSoC 上实现固定步长的节点分析、状态空间或固定导纳求解。
- FPGA/异构实时：用流水线、并行矩阵运算、自定义浮点或 CPU-FPGA 分工满足小步长约束。
- 实时协同与 HIL：连接离线 RMS/EMT 工具、控制器硬件、保护装置或外部仿真器，关注接口延迟和同步。
- 超实时仿真：目标是快于真实时间完成故障扫描、控制策略预演或数字孪生预测，但仍需说明与实时 HIL 的验证差异。

## 形式化表示
实时 EMT 的基本约束是每个步长内计算与 I/O 必须完成：

$$
T_{\mathrm{solve}}+T_{\mathrm{io}}+T_{\mathrm{sync}}\le \Delta t_{\mathrm{real}}
$$

其中 $\Delta t_{\mathrm{real}}$ 是实时步长，$T_{\mathrm{solve}}$ 是网络和设备模型求解时间，$T_{\mathrm{io}}$ 是硬件接口延迟，$T_{\mathrm{sync}}$ 是多核、多机或协同仿真的同步开销。

## 适用边界与失败边界
适用场景包括控制保护闭环测试、HVDC/MMC/IBR 设备验证、大规模电网扰动预演和现场工程调试。失败边界包括模型阶数过高、开关事件过密、非线性迭代不收敛、I/O 或通信延迟过大、硬件精度不足、或为了满足 deadline 过度简化导致关键暂态丢失。原页面/来源汇总没有统一的实时步长或延迟阈值，需按平台和案例报告。

## 代表性论文
- “FPGA-Based Real-Time EMTP”：代表 FPGA 流水线实时 EMT 早期路线。
- “An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA”：非线性 EMT 实时迭代求解器。
- “Development of phase domain frequency-dependent transmission line model on FPGA”：频变线路模型的 FPGA 实时实现。
- “Real-time RMS-EMT co-simulation and its application in HIL testing of protective relays”：实时 RMS-EMT 协同与保护 HIL。
- “Lessons learned in porting offline large-scale power system simulation to real-time”：离线大系统迁移到实时平台的工程经验。

## 验证共识
实时仿真验证不只看波形精度，还要证明 deadline 可满足。常见证据包括与离线 EMT/商业软件/实验波形对比、硬件在环闭环测试、单步执行时间、最坏情况延迟、资源占用和长时间稳定运行记录。

## 相关方法
- [[fixed-admittance|恒导纳模型]] - 避免矩阵重分解的实时优化
- [[state-space-method|状态空间法]] - 快速状态空间求解
- [[multirate-method|多速率方法]] - 实时多速率调度
- [[numerical-integration|数值积分]] - 实时稳定积分方法
- [[interpolation-method|插值方法]] - 实时接口数据同步

## 相关模型
- [[mmc-model|MMC模型]] - MMC实时等效建模
- [[vsc-model|VSC模型]] - 换流器实时仿真
- [[fdne-model|频变网络等值(FDNE)]] - 外部系统实时等值
- [[transmission-line-model|输电线路模型]] - 行波模型实时实现

## 相关主题
- [[parallel-computing|并行计算]] - 多核/FPGA实时并行
- [[co-simulation|混合仿真]] - 实时协同仿真
- [[frequency-dependent-modeling|频率相关建模]] - 频变模型实时实现
- [[fpga-real-time-simulation|FPGA实时仿真]] - 硬件级实时加速
- [[gpu-accelerated-simulation|GPU加速仿真]] - GPU实时计算
- [[hil-simulation|硬件在环仿真]] - HIL实时测试

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

## 来源论文

| 论文 | 年份 |
|------|------|
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Use of efficient task allocation algorithm for parallel real]] | 2020 |
| [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Sparse solver application for parallel real-time electromagn]] | 2023 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等 | A fixed-admittance algorithm for the FPGA-based micro]] | 2025 |
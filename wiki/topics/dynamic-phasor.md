---
title: "动态相量法"
type: topic
tags: []
created: "2026-04-13"
---

# 动态相量法

## 定义
动态相量法用时变傅里叶系数描述电压、电流或状态变量的慢变包络，在保留目标频率分量动态的同时避免逐周期求解全部开关波形。它既可作为设备建模方法，也可作为 [[co-simulation]] 接口和移频/谐波相量域仿真的数学基础。

## 合成定位
在 P0 taxonomy 中，动态相量法位于 EMT 详细时域仿真与传统相量/机电暂态模型之间。它向上支撑混合仿真、多速率仿真和宽频暂态稳定分析，向下连接 [[mmc-model]]、[[vsc-model]]、HVDC、SVC、DAB/SST 等电力电子设备模型。

## 分类或机制
- 设备动态相量模型：对 HVDC、SVC、MMC、VSC、PFC 或 SST 保留基波、直流、低阶谐波或研究目标频段。
- 接口动态相量模型：在 EMT 与机电暂态/相量域之间进行瞬时量与相量分量映射，典型形式包括 DPIM、Thevenin/Norton 等效和双向缓冲。
- 移频/谐波相量扩展：通过移频相量、SFA/SFEMT 或 HPD 描述非基频包络，并与 [[harmonic-analysis]] 和 [[frequency-dependent-modeling]] 相连。
- 数值积分与多速率求解：通过频率匹配积分、隐式积分或 [[multirate-method]] 控制大步长下的精度和稳定性。

## 形式化表示
动态相量把时域信号 $x(t)$ 表示为滑动窗口内的时变傅里叶系数：

$$
X_k(t)=\frac{1}{T}\int_{t-T}^{t}x(\tau)e^{-jk\omega_0\tau}\,d\tau
$$

其常用微分性质为：

$$
\left\langle \frac{dx}{dt}\right\rangle_k=\frac{dX_k}{dt}+jk\omega_0X_k
$$

因此模型精度取决于保留的谐波集合、窗口长度、基频选择和暂态频谱是否仍集中在这些分量附近。

## 适用边界与失败边界
动态相量适合频谱可由少量主导分量近似、关注包络或中低频动态、且全开关 EMT 成本过高的场景。失败边界包括频谱快速扩展、强非周期暂态、截断阶数不足、频率偏移过大、接口映射失真或步长选择破坏稳定性。原页面/来源汇总未给出跨设备统一的保留谐波阶数和误差阈值。

## 代表性论文
- “Hybrid-model transient stability simulation using dynamic phasors based HVDC system”：早期 HVDC 动态相量与机电暂态混合仿真。
- “Hybrid simulation of power systems with SVC dynamic phasor model”：SVC 动态相量接口的代表性应用。
- “A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT Simulation”：将 MMC 动态相量扩展到更宽频率范围。
- “Assessment of dynamic phasor extraction methods for power system co-simulation”：比较不同动态相量提取算法的适用性。
- “Revisiting dynamic phasors and their efficacy in simulating electric circuits”：强调动态相量计算优势并非无条件成立。

## 验证共识
验证通常采用全 EMT、实验或基准系统波形对比，关注目标频率分量、包络动态、暂态峰值和计算时间。共识是动态相量可在合适频谱假设下显著降低求解负担，但必须公开截断策略、步长、频率偏移处理和接口映射误差，否则“高效”结论不可迁移。

## 相关方法
- [[numerical-integration|数值积分]] - 动态相量频率匹配积分
- [[state-space-method|状态空间法]] - 相量域状态空间建模
- [[average-value-model|平均值模型]] - 开关周期平均化
- [[multirate-method|多速率方法]] - 相量-时域多速率接口

## 相关模型
- [[mmc-model|MMC模型]] - MMC动态相量建模
- [[vsc-model|VSC模型]] - VSC动态相量简化
- [[transformer-model|变压器模型]] - 变压器相量域建模
- [[transmission-line-model|输电线路模型]] - 线路相量域接口

## 相关主题
- [[harmonic-analysis|谐波分析]] - 谐波相量域(HPD)建模
- [[frequency-dependent-modeling|频率相关建模]] - 宽频移频相量
- [[co-simulation|混合仿真]] - 动态相量接口
- [[real-time-simulation|实时仿真]] - 动态相量实时实现
- [[electromechanical-electromagnetic-hybrid-simulation|机电-电磁混合仿真]] - TS-EMT相量接口

## 论文方法分析
> 基于 37 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|
| 动态相量法 | 11 | A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT |
| 动态相量法(DP) | 3 | An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Fact |
| 多域协同仿真 | 2 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequenc |
| 移频相量法(SFP) | 2 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequenc |
| 开关函数法 | 2 | Hybrid-model transient stability simulation using dynamic phasors base |
| 混合模型仿真 | 2 | Hybrid-model transient stability simulation using dynamic phasors base |
| 机电暂态建模 | 2 | Hybrid-model transient stability simulation using dynamic phasors base |
| 交直流网络接口算法 | 2 | Hybrid-model transient stability simulation using dynamic phasors base |
| 混合仿真接口算法 | 2 | Hybrid simulation of power systems with SVC dynamic phasor model |
| 状态空间平均法(SSA) | 2 | Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Sol |
| 基频动态相量建模 | 1 | A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT |
| 主导谐波分量分析 | 1 | A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT |
| 谐波相量域(HPD)建模 | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
| EMT-HPD协同仿真 | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
| HPD传输线模型(HPD-TLM) | 1 | A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harm |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|
| 交流电网 | 5 |
| 模块化多电平换流器(MMC) | 3 |
| HVDC输电系统 | 3 |
| CIGRE交直流测试系统 | 2 |
| 电力系统网络模型 | 2 |
| 动态相量HVDC模型 | 2 |
| 交流子系统 | 2 |
| 9节点测试系统 | 2 |
| 新英格兰39节点测试系统 | 2 |
| 动态相量模型 | 2 |
| Y-∆连接变压器 | 2 |
| 固态变压器(SST) | 2 |
| 逆变器系统 | 1 |
| 背靠背HVDC系统 | 1 |
| 12节点电力系统 | 1 |
### 验证方式分布
- **仿真**: 15 篇
- **仿真/对比**: 6 篇
- **仿真对比**: 6 篇
- **仿真与对比**: 3 篇
- **仿真与实验对比**: 1 篇
- **仿真验证（基于实际含大规模风电的交流电网系统）**: 1 篇
- **仿真与实验**: 1 篇
- **FPGA实时仿真与对比验证**: 1 篇
- **仿真/基准测试对比**: 1 篇
- **仿真验证**: 1 篇
- **仿真验证与对比分析**: 1 篇
## 技术演进脉络
### 2005年 (1篇)
- **含统一潮流控制器装置的电力系统动态混合仿真接口算法研究**
  - 💡 将动态相量法与交替迭代接口技术相结合，实现了兼顾UPFC电磁暂态细节与全网机电暂态效率的混合仿真新方法。
  - 提出了一种基于交替迭代法的UPFC与电力系统网络动态混合仿真接口算法。
  - 推导了UPFC动态相量模型，并设计了并联侧定电压/直流电容电压与串联侧定线路潮流的控制策略。
### 2006年 (3篇)
- **Hybrid-model transient stability simulation using dynamic phasors based HVDC sys**
  - 💡 将动态相量理论引入HVDC建模并与机电暂态模型结合，构建了兼顾高精度与计算效率的大规模交直流系统混合仿真新框架。
  - 提出了一种基于动态相量理论的交直流系统混合模型暂态稳定仿真算法。
  - 推导了详细的动态相量HVDC系统模型，并设计了其与交流网络的接口算法。
- **Hybrid-model transient stability simulation using dynamic phasors based HVDC sys**
  - 💡 将动态相量理论引入HVDC建模，构建了兼顾电磁暂态精度与机电暂态计算效率的交直流混合仿真新方法。
  - 推导了基于动态相量理论的详细HVDC系统数学模型。
  - 提出了直流动态相量模型与交流网络的高效接口算法。
- **Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model**
  - 💡 将动态相量理论应用于HVDC建模，有效填补了电磁暂态与准稳态模型之间的精度与效率鸿沟，为大规模交直流系统暂态分析提供了新途径。
  - 推导了基于动态相量理论的详细HVDC系统数学模型。
  - 提出了直流动态相量模型与交流机电暂态网络的高效接口算法。
### 2009年 (3篇)
- **Hybrid simulation of power systems with SVC dynamic phasor model**
  - 💡 将动态相量理论引入SVC建模并与传统机电暂态仿真结合，突破了传统TSP-EMTP混合仿真中相位不连续与直流偏移导致的精度瓶颈。
  - 推导了基于动态相量理论的详细单相SVC数学模型。
  - 提出了SVC动态相量模型与交流子系统机电暂态模型之间的高效接口算法。
- **Hybrid simulation of power systems with SVC dynamic phasor model**
  - 💡 将动态相量理论引入SVC建模并与机电暂态程序耦合，提出了一种兼顾大规模系统仿真效率与关键电力电子设备波形精度的混合仿真新方法。
  - 推导了基于动态相量理论的详细单相SVC数学模型。
  - 提出了SVC动态相量模型与交流子系统机电暂态模型之间的数据交互接口算法。
- **Optimization of numerical integration methods for the simulation of dynamic phas**
  - 💡 通过在频域优化匹配数值积分系数以最小化特定频率处的截断误差，突破了传统积分方法在动态相量仿真中精度与步长的制约。
  - 提出专用于动态相量模型的频率匹配线性数值积分技术。
  - 通过在频域分析并最小化局部截断误差来优化确定积分系数。
### 2016年 (1篇)
- **Co-Simulation of electromagnetic transients and Phasor models: A relaxation appr**
  - 💡 通过松弛迭代结合多端口等效、频率相关阻抗更新与边界变量预测，实现了高精度EMT与高效率相量模式求解器的稳定快速耦合。
  - 提出了一种基于松弛迭代的EMT与相量模式求解器协同仿真框架。
  - 系统评估并比较了多种多端口等效模型对PM-EMT迭代收敛性的影响。
### 2017年 (1篇)
- **Dynamic Phasor Based Interface Model for EMT and Transient Stability Hybrid Simu**
  - 💡 提出基于动态相量的接口模型(DPIM)，通过基频与动态相量形式的等效电路交互，有效解决了传统混合仿真接口在强扰动下的波形失真与单步延迟问题。
  - 提出了一种基于动态相量的接口模型(DPIM)，用于提升EMT与暂态稳定混合仿真的整体精度。
  - 将混合仿真系统划分为TS、EMT和DPIM三部分，并设计了基于基频诺顿等效与动态相量戴维南等效的双向交互机制。
### 2018年 (6篇)
- **A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT Simulatio**
  - 💡 首创基频动态相量构造，在不显著增加计算负担的前提下实现MMC外部变量任意频率分量的精确建模，突破传统EMT仿真计算瓶颈。
  - 提出一种可直接接入EMT仿真器的MMC扩展频域动态相量模型。
  - 引入基频动态相量新概念，实现外部变量任意频率分量的高效捕捉且不显著增加计算负担。
- **Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching **
  - 💡 首创支持混合仿真与纯相量域仿真动态切换的机制，实现了计算效率与模型精度的自适应平衡。
  - 提出了一种适用于输配电集成系统的先进EMT与相量域混合仿真架构。
  - 构建了支持正序、三序、三相及混合表示的综合相量域建模与仿真框架。
- **Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simul**
  - 💡 提出了一种基于动态相量与EMT求解器接口的混合协同仿真方法，通过专用映射算法解决多时间步长接口问题，在保证精度的同时大幅降低大规模电网暂态仿真的计算负担。
  - 提出了一种结合EMT与动态相量求解器的混合协同仿真架构
  - 开发了精确映射瞬时EMT样本与动态相量样本的专用接口算法
- **Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phaso**
  - 💡 将移位相量理论与开关依赖型Thevenin等效结合，实现了计算复杂度与子模块数量解耦的高精度MMC实时仿真模型。
  - 提出基于移位相量的MMC子模块Thevenin等效建模方法，显著提升电磁暂态仿真精度。
  - 构建开关依赖型桥臂等效电路，使计算负担几乎不随子模块数量增加而变化。
- **Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Solid State T**
  - 💡 提出一种结合SSA与动态相量GSSA的混合平均建模方法，在保证精度的同时实现了三相DAB变换器小信号稳定性分析的高效EMT仿真。
  - 指出传统状态空间平均法(SSA)在三相DAB变换器稳定性分析中精度不足。
  - 提出基于动态相量概念的广义状态空间平均法(GSSA)模型，适用于Y-∆型三相DAB。
- **Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Solid State T**
  - 💡 提出基于动态相量的GSSA与SSA混合建模方法，克服了传统SSA在三相DAB稳定性分析中的精度局限，并实现了EMT仿真环境下的加速计算。
  - 指出传统状态空间平均法(SSA)在三相DAB小信号稳定性分析中存在精度不足的问题。
  - 提出基于动态相量概念的广义状态空间平均法(GSSA)模型，专门针对Y-∆型3p-DAB拓扑。
### 2019年 (4篇)
- **A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor D**
  - 💡 构建结合SFP直流模型与EMT交流模型的多域协同仿真架构，并通过HMD-TLM接口实现跨域高效交互与双域波形同步输出。
  - 提出了一种将直流子系统与交流子系统分别采用SFP模型和EMT模型表示的多域协同仿真方法。
  - 开发了混合多域传输线模型(HMD-TLM)接口，有效处理跨域交互并支持瞬时波形与相量波形同步输出。
- **A Multi-rate Co-simulation of Combined Phasor-Domain and Time-Domain Models for **
  - 💡 首次将移频相量模型与电磁暂态模型通过多速率架构与新型传输线接口相结合，实现大规模风电并网系统宽频动态的高效精确仿真。
  - 提出了一种结合移频相量域与电磁暂态域的多速率协同仿真框架，有效兼顾宽频交互捕捉与计算效率。
  - 通过系统分区将交流电网仿真步长扩展至500µs，大幅降低了大规模系统的计算负担。
- **Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model**
  - 💡 提出了一种结合专用缓冲区定界方法的EMT-TS混合仿真策略，有效突破了高精度MMC-HVdc模型在大规模电网系统级仿真中的计算瓶颈。
  - 设计了支持EMT与TS程序协同仿真的混合仿真框架。
  - 提出了一种用于确定混合仿真中交流侧缓冲区大小的专用解析方法。
- **Shu 等 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency **
  - 💡 首创结合SFP直流模型、EMT交流模型与HMD-TLM接口的多域协同仿真架构，兼顾大规模交直流混合系统的仿真精度与计算效率。
  - 提出将直流子系统采用SFP模型、交流子系统采用EMT模型的多域协同仿真框架。
  - 开发HMD-TLM接口模型以精确反映SFP与EMT域间的交互，并支持瞬时值与相量波形同步输出。
### 2020年 (1篇)
- **A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analy**
  - 💡 提出了一种结合EMT交流模型与HPD直流模型的协同仿真框架，通过HPD-TLM接口与解耦时间序列实现瞬时波形与谐波相量的同步高效输出，突破了传统时域仿真在宽频谐波分析中的效率瓶颈。
  - 提出了面向电力电子直流电网的谐波相量域(HPD)建模方法，可同时输出瞬时波形与谐波相量。
  - 设计了基于HPD传输线模型(HPD-TLM)的交直流协同仿真接口，实现了EMT交流侧与HPD直流侧的高效解耦。
### 2021年 (6篇)
- **Assessment of dynamic phasor extraction methods for power system co-simulation a**
  - 💡 首次系统性地对比评估了多种动态相量提取算法在复杂电力系统信号下的理论特性、数值局限及联合仿真适用性，为大规模电网多速率协同仿真提供了明确的方法选型指南。
  - 系统梳理并深入剖析了多种动态相量提取方法的数学理论基础与底层数值实现流程。
  - 全面评估了各方法在含机电振荡、直流偏置、谐波、不平衡及任意暂态等复杂工况下的相量提取特性与固有局限。
- **Comparison of dynamic phasor, discrete-time and frequency scanning based SSR mod**
  - 💡 将频率扫描与向量拟合技术结合，为含复杂电力电子设备的电力系统提供了一种无需解析推导、高精度且便捷的次同步谐振LTI模型提取新方法。
  - 系统对比了动态相量法、离散时间法与频率扫描法在TCSC次同步谐振建模中的精度差异。
  - 验证了结合仿真与向量拟合技术的频率扫描黑盒建模方法在提取时不变模型时的有效性。
- **Extending the Frequency Bandwidth of Transient Stability Simulation Using Dynami**
  - 💡 将动态相量技术与MNA印章建模框架相结合，构建了一种兼顾宽频动态分析精度与大规模网络计算效率的通用暂态仿真方法。
  - 提出了一种基于改进节点分析(MNA)和动态相量的新型暂态稳定仿真方法。
  - 推导了常见电力元件的印章模型，并建立了将同步机表示为非线性电感的新型MNA同步机模型。
- **Half-wavelength System Transients Stability Simulation Using Dynamic Phasor Mode**
  - 💡 提出将动态相量模型与变步长技术相结合，解决了半波长输电系统机电暂态仿真中固定步长导致的精度与速度矛盾。
  - 将交流线路动态相量模型引入半波长输电系统机电暂态仿真，以准确模拟电磁波传输动态特性。
  - 针对线路区内故障场景提出变步长仿真策略，有效兼顾了仿真精度与计算速度。
- **Shifted frequency analysis-EMTP multirate simulation of power systems**
  - 💡 提出基于多区域戴维南等效框架的SFA-EMT混合多速率仿真协议，通过并行实虚部EMT仿真维持解析同步性，实现了大时间步长下的高效高精度暂态仿真。
  - 提出了一种连接SFA与EMT仿真器的新型混合多速率接口协议。
  - 设计了并行运行的实部与虚部EMT仿真架构，以跟踪SFA复数解的虚部并保持解析性与同步性。
- **Three-stage implicit integration for large time-step size electromagnetic transi**
  - 💡 提出将3S-SDIRK积分算法与移频建模相结合，在允许大时间步长高效计算的同时，从根本上解决了传统SFEMT仿真中的数值振荡问题。
  - 将3S-SDIRK方法引入SFEMT仿真以替代传统梯形积分法。
  - 详细推导了基于3S-SDIRK的SFEMT数值积分公式与实现流程。
### 2022年 (2篇)
- **Evaluation of time-domain and phasor-domain methods for power system transients**
  - 💡 首次在同一计算平台上对时域与多种相量域算法进行系统性横向对比，明确了动态相量法在电力系统暂态分析中的性能优势与建模差异。
  - 在同一计算平台上系统评估了时域与三种相量域算法的计算流程与性能。
  - 针对IEEE-118基准系统详细对比了不同方法在建模方法论上的优势与差异。
- **Multi-timescale simulator of nonlinear electrical elements by interfacing shifte**
  - 💡 提出基于移位等效相量（SEP）的多时间尺度仿真接口技术，通过双参数调节实现大步长下非线性元件无过冲仿真及瞬时/包络波形的高效统一跟踪。
  - 提出了一种适用于宽时间尺度强非线性电气元件的多时间尺度瞬态支路伴随模型。
  - 建立了基于SEP的饱和变压器模型，有效避免了大步长仿真时的过冲失真问题。
### 2023年 (3篇)
- **Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching a**
  - 💡 将根匹配与嵌入式小步长技术引入移频电磁暂态仿真框架，在维持大时间步长计算效率的同时，有效解决了系统突变场景下的精度衰减问题。
  - 分析了传统移频电磁暂态仿真在系统突变场景下精度下降的根本原因。
  - 提出了一种结合根匹配与嵌入式小步长技术的高精度SFEMT仿真算法。
- **Dynamic Synchrophasor Estimator Based on Multi-frequency Phasor Model**
  - 💡 创新性地引入多频率相量模型描述真实频率附近的有效信息，并结合离线矩阵修正DFT结果，实现了大频偏下高精度、低计算成本的动态相量测量。
  - 提出基于多频率相量模型的动态同步相量估计算法，有效应对基波频率大范围偏移问题。
  - 结合离线矩阵查表与DFT修正技术，在有限增加计算量的前提下显著提升动态测量精度。
- **Modeling and simulation of VSC-HVDC with dynamic phasors**
  - 💡 将动态相量法引入VSC-HVDC建模，通过截断非关键高阶傅里叶级数并合理选取关键频率分量，在保留系统暂态动态特性的同时大幅降低模型复杂度与计算成本。
  - 提出了基于时变傅立叶级数的VSC-HVDC动态相量建模方法。
  - 通过保留开关函数的直流与基频分量及线路直流分量，有效简化了高频开关过程。
### 2024年 (1篇)
- **Shifted frequency analysis based, faster-than-real-time simulation of power syst**
  - 💡 将移频分析与延迟线性多步复合方法相结合，并创新性地引入基于图的线程安全设计与异构编译翻译层，在GPU上实现了高可扩展、跨平台兼容的超实时电磁暂态仿真。
  - 提出基于延迟线性多步复合方法的GPU加速架构，实现电磁暂态仿真的高效并行计算。
  - 引入移频分析技术，在计算负载与仿真精度之间取得有效平衡。
### 2025年 (4篇)
- **An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correct**
  - 💡 通过引入符号函数统一不同驱动频率，构建了高效的单相Boost PFC变换器等效动态相量模型，实现了控制器参数的快速整定与优化。
  - 提出了一种单相Boost PFC变换器的动态相量(DP)模型，并提供了将其集成至现有仿真平台的详细指南。
  - 利用符号函数将工频DBR与高频Boost DC-DC变换器统一转换为等效单相有源整流器模型，有效克服了DP建模中的多频率驱动难题。
- **An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Mod**
  - 💡 首次将ESPRIT算法引入EMT与SFEMT协同仿真接口，通过高精度参数估计构建正交解析信号，显著提升了多尺度协同仿真的精度。
  - 推导了SFEMT建模的一般形式，为协同仿真接口设计提供了理论指导。
  - 提出了一种基于ESPRIT算法的EMT与SFEMT模型协同仿真接口。
- **Modeling and application of DQ-sequence dynamic phasors under unbalanced AC cond**
  - 💡 提出了一种适用于不平衡交流工况的DQ序列动态相量建模方法，实现了复数状态方程向最简实数形式的高效转换。
  - 定义了结合瞬时对称分量分解与Park变换的DQ序列动态相量，用于准确描述不平衡交流条件下的三相时域信号。
  - 推导了动态相量的乘法性质，并给出了构建系统状态方程的通用步骤及状态矩阵的具体解析表达式。
- **Revisiting dynamic phasors and their efficacy in simulating electric circuits**
  - 💡 首次系统性地澄清了动态相量法计算优势并非普遍适用，并明确界定了其在稳态与暂态仿真中的精度边界及步长选择准则。
  - 重新审视并明确了动态相量法在电路仿真中计算优势成立的基础条件与适用范围。
  - 基于伴随电路模型，通过特征值与稳态分析系统评估了EMT与DP建模方法随仿真步长变化的精度特性。
### 2026年 (1篇)
- **Multirate Method for Dynamic Phasor Simulation of Large-Scale Power Systems**
  - 💡 提出了一种基于动态相量的单框架多速率仿真架构，通过快慢变量插值/平均耦合与误差校验机制，在单一模型内实现了无需EMT/TS联合仿真的跨时间尺度高效高精度计算。
  - 提出了一种无需传统EMT与TS联合仿真的动态相量多速率仿真方法。
  - 设计了基于插值与平均的快慢变量数据交换机制，并引入误差校验策略以自动决定步长接受或回退重算。
## 关键发现汇总
- [2005] **含统一潮流控制器装置的电力系统动态混合仿真接口算法研究**: 动态相量模型在保持与电磁暂态仿真相近精度的同时显著提升了计算速度。
- [2005] **含统一潮流控制器装置的电力系统动态混合仿真接口算法研究**: 所提接口算法在两区域系统暂态稳定分析中表现出优良的收敛性与计算精度。
- [2005] **含统一潮流控制器装置的电力系统动态混合仿真接口算法研究**: 该混合仿真方案可有效处理含FACTS装置电力系统发生不对称故障时的暂态过程。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 动态相量HVDC模型的仿真精度与详细电磁暂态(EMT)模型高度一致。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 所提接口算法在两区域交直流系统及多馈入直流系统的暂态稳定分析中运行有效。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 动态相量HVDC模型的仿真精度与详细电磁暂态(EMT)模型高度一致。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 所提接口算法在两区域交直流系统及多馈入HVDC系统的暂态稳定分析中表现有效。
- [2006] **Hybrid-model transient stability simulation using dynamic ph**: 混合仿真算法成功填补了EMT与准稳态(QSS)模型在计算效率与精度之间的空白。
- [2006] **Hybrid Transient Stability Simulation Using Dynamic Phasor B**: 动态相量HVDC模型的仿真精度与详细电磁暂态(EMT)模型高度一致。
- [2006] **Hybrid Transient Stability Simulation Using Dynamic Phasor B**: 所提混合仿真算法在两区域交直流系统及多馈入HVDC系统的暂态稳定分析中验证有效。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 在9节点和新英格兰39节点系统上的测试表明，所提单相SVC动态相量模型与全电磁暂态(EMTP)模型相比具有极高的精度。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 该混合方法在保留目标部分电压/电流波形细节的同时，显著降低了整体仿真所需的计算时间与内存资源。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 单相SVC动态相量模型的仿真精度与全电磁暂态(EMTP)模型高度一致。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 该混合仿真方法相比传统全系统EMTP仿真显著提升了计算速度并降低了内存占用。
- [2009] **Optimization of numerical integration methods for the simula**: 频率匹配积分法在系统频率处的数值精度显著优于传统欧拉法、梯形法及Gear法。
- [2009] **Optimization of numerical integration methods for the simula**: 该方法允许采用更大的积分步长，从而在保证精度的同时大幅缩短仿真计算时间。
- [2009] **Optimization of numerical integration methods for the simula**: 在动态相量模型固有的快振荡暂态过程中，新方法保持了优异的数值稳定性。
- [2016] **Co-Simulation of electromagnetic transients and Phasor model**: 在74节点23机大规模测试系统上成功验证了EMT与PM子系统的协同仿真可行性。
- [2016] **Co-Simulation of electromagnetic transients and Phasor model**: 不同多端口等效模型的迭代收敛性能得到明确对比与量化评估。
- [2016] **Co-Simulation of electromagnetic transients and Phasor model**: 边界变量预测技术显著减少了迭代次数并提升了整体计算效率。
- [2017] **Dynamic Phasor Based Interface Model for EMT and Transient S**: DPIM显著降低了接口波形失真和交互时间延迟引入的仿真误差。
- [2017] **Dynamic Phasor Based Interface Model for EMT and Transient S**: 在换流器附近发生故障等强扰动工况下，混合仿真的动态响应精度得到明显改善。
- [2017] **Dynamic Phasor Based Interface Model for EMT and Transient S**: 实际HVDC系统仿真结果表明该方法在保证高精度的同时具备良好的计算效率。
- [2018] **A Dynamic Phasor Model of an MMC with Extended Frequency Ran**: 新模型在保持高精度的同时，计算效率显著优于现有详细EMT模型。
- [2018] **A Dynamic Phasor Model of an MMC with Extended Frequency Ran**: 在逆变器、背靠背HVDC及12节点系统中均验证了模型的宽频适应性与接口兼容性。
- [2018] **A Dynamic Phasor Model of an MMC with Extended Frequency Ran**: 缩比实验室实验结果与仿真数据高度吻合，证实了模型的工程实用性。
- [2018] **Advanced EMT and Phasor-Domain Hybrid Simulation With Simula**: 引入模式切换功能后，系统整体计算时间较全程运行混合仿真显著缩短。
- [2018] **Advanced EMT and Phasor-Domain Hybrid Simulation With Simula**: 在大幅提升计算效率的同时，关键动态过程的仿真精度得到良好保持。
- [2018] **Co-simulation of electrical networks by interfacing EMT and **: 在不同时间步长比例下协同仿真均能保持较高的动态与暂态精度
- [2018] **Co-simulation of electrical networks by interfacing EMT and **: 相比传统全EMT仿真实现了显著的计算时间节省

## 来源论文

| 论文 | 年份 |
|------|------|
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simula]] | 2009 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio|A Dynamic Phasor Model of an MMC with Extended Frequency Ran]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[dynamic-model-reduction-of-power-electronic-interfaced-generators-based-on-singu|Dynamic model reduction of power electronic interfaced gener]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[reduced-order-dynamic-model-of-modular|Reduced-Order Dynamic Model of Modular]] | 2019 |
| [[reduced-order-dynamic-model-of-modular|Reduced-Order Dynamic Model of Modular]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[dynamic-equivalence-method-of-ddpmsg-wind-farm-for-sub-synchronous-oscillation-a|Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synch]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[analytical-model-building-for-type-3-wind-farm-subsynchronous-oscillation-analys|Analytical model building for Type-3 wind farm subsynchronou]] | 2021 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[extending-the-frequency-bandwidth-of-transient-stability-simulation-using-dynami|Extending the Frequency Bandwidth of Transient Stability Sim]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size el]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[2728modeling|Modeling_of_LCC_HVDC_Systems_Using_Dynam]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Shifted frequency analysis based, faster-than-real-time simu]] | 2024 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[type-3-wind-turbine-generator-model-with-generic-high-level-control-for-electrom|Type-3 wind turbine generator model with generic high-level ]] | 2025 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[vsc-hvdc-系统的动态相量法建模仿真分析|VSC-HVDC 系统的动态相量法建模仿真分析]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
---
title: "混合仿真"
type: topic
tags: []
created: "2026-04-13"
---

# 混合仿真

## 定义
混合仿真是在同一研究问题中耦合不同暂态表示、求解器或时间步长的仿真范式。该页的论文样本主要围绕 EMT、机电暂态、相量域、动态相量和移频相量之间的接口展开，用于在保留局部波形细节的同时降低全系统 EMT 建模成本。

## 合成定位
在 P0 taxonomy 中，混合仿真是连接 [[dynamic-phasor]]、[[frequency-dependent-modeling]]、[[parallel-computing]] 与 [[real-time-simulation]] 的总入口。它关注的是“模型域如何拼接”和“接口误差如何受控”，而不是单一设备模型本身；设备侧细节通常落在 [[mmc-model]]、[[vsc-model]]、[[transmission-line-model]] 或 [[fdne-model]]。

## 分类或机制
- EMT-机电暂态混合：以边界母线、Thevenin/Norton 等值、动态相量接口或 [[fdne-model]] 连接详细 EMT 子网与大规模机电网络。
- EMT-相量/动态相量协同：用 [[dynamic-phasor]] 或移频相量减少高频载波求解负担，并通过映射、插值、外推或松弛迭代交换边界变量。
- 多速率/多求解器协同：用 [[multirate-method]] 对快变电力电子局部子系统和慢变网络采用不同步长，并处理同步、延迟和收敛问题。
- 实时/硬件在环混合：将 [[rtds]]、FPGA、CPU 或离线工具联接，用于保护控制器和大系统动态测试。

## 形式化表示
协同仿真的接口可抽象为两个子系统在边界变量上交换：

$$
x_E^{k+1}=F_E(x_E^k,z_T^k,\Delta t_E),\qquad
x_T^{k+1}=F_T(x_T^k,z_E^k,\Delta t_T)
$$

其中 $x_E$ 是 EMT 子系统状态，$x_T$ 是机电/相量/动态相量子系统状态，$z_E,z_T$ 是经 Thevenin/Norton 等值、动态相量或频率相关网络等值传递的边界变量。

## 适用边界与失败边界
适用场景是局部强暂态、全网规模大、研究对象需要跨时间尺度而全 EMT 成本过高的系统。失败边界通常出现在接口电气距离过近、边界变量频谱超出接口模型带宽、强不平衡故障导致等值失配、多速率延迟不可忽略、或 FDNE/有理模型无源性不足时。原页面/来源汇总未给出统一的误差阈值或步长比准则，因此本页不固化精确数字。

## 代表性论文
- “Interfacing Techniques for Transient Stability and Electromagnetic Transient Hybrid Simulation”：系统化 TS-EMT 接口分类与术语。
- “Hybrid simulation of power systems with SVC dynamic phasor model”：展示 SVC 动态相量模型与机电暂态网络的混合接口。
- “Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical”：将 [[vector-fitting]] 与无源性处理用于 EMT-机电边界等值。
- “A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems”：代表多速率 EMT 协同仿真路线。
- “A multi-solver framework for co-simulation of transients in modern power systems”：代表 EMT、DP、FAST、TS 多求解器集成趋势。

## 验证共识
该主题的验证以仿真对比为主，常见基准包括全 EMT、PSCAD/EMTDC、机电暂态程序、实时仿真平台或硬件在环结果。论文通常报告波形一致性、接口暂态误差、计算效率和强扰动响应；但跨论文缺少统一公开基准，原页面/来源汇总未给出可直接比较的标准数据集。

## 相关页面
[[dynamic-phasor]] · [[frequency-dependent-modeling]] · [[parallel-computing]] · [[real-time-simulation]] · [[multirate-method]] · [[network-equivalent]] · [[fdne-model]]

## 论文方法分析
> 基于 46 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|
| 机电-电磁暂态混合仿真 | 4 | Electromechanical-electromagnetic Hybrid Simulation Technology With La |
| 多速率协同仿真 | 3 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 动态相量法 | 3 | Dynamic Phasor Based Interface Model for EMT and Transient Stability H |
| 机电暂态建模 | 3 | Electromechanical Transient Modeling of the Low-Frequency AC System Wi |
| 混合仿真接口技术 | 3 | Hybrid simulation of power systems with SVC dynamic phasor model |
| 多域协同仿真 | 2 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequenc |
| 移频相量法(SFP) | 2 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequenc |
| 混合多域传输线模型接口(HMD-TLM) | 2 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequenc |
| 相量域建模 | 2 | A rotary frequency converter model for electromechanical transient stu |
| 机电暂态数值仿真 | 2 | A rotary frequency converter model for electromechanical transient stu |
| 等效电路法 | 2 | Electromechanical Transient Modeling of the Low-Frequency AC System Wi |
| 频率相关网络等值（FDNE） | 2 | Frequency Dependent Network Equivalent for Electromagnetic and Electro |
| 机电暂态仿真 | 2 | Hybrid simulation of power systems with SVC dynamic phasor model |
| 接口位移技术(ID) | 2 | Interface Displacement and Mapping Equivalence Based Hybrid Simulation |
| 离散电感解耦方法 | 1 | 27&28/Multi-rate real time hybrid simulation of controllable line comm |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|
| 模块化多电平换流器(MMC) | 4 |
| 电磁暂态(EMT)模型 | 3 |
| 机电暂态模型 | 3 |
| 电磁暂态模型 | 3 |
| 大规模交直流电网 | 2 |
| 直流电网移频相量模型 | 2 |
| 交流电网电磁暂态模型 | 2 |
| 旋转变频器(RFC) | 2 |
| 动态相量求解器 | 2 |
| HVDC系统 | 2 |
| 交流电网 | 2 |
| 新英格兰39节点测试系统 | 2 |
| 静止无功补偿器(SVC) | 2 |
| 交流子系统机电暂态模型 | 2 |
| HVAC/DC交直流电网 | 2 |
### 验证方式分布
- **仿真**: 20 篇
- **仿真对比**: 9 篇
- **仿真/对比**: 7 篇
- **实验**: 2 篇
- **仿真与对比**: 2 篇
- **仿真与对比验证**: 1 篇
- **仿真/实验**: 1 篇
- **对比**: 1 篇
- **仿真验证与对比**: 1 篇
- **仿真对比验证**: 1 篇
- **理论对比与综述**: 1 篇
## 技术演进脉络
### 2009年 (4篇)
- **Hybrid simulation of power systems with SVC dynamic phasor model**
  - 💡 将动态相量理论应用于SVC建模，并与传统机电暂态模型结合，提出了一种兼顾计算效率与波形精度的新型混合仿真方法。
  - 推导了基于动态相量理论的SVC单相详细模型。
  - 提出了SVC动态相量模型与交流子系统机电暂态模型之间的混合仿真接口算法。
- **Hybrid simulation of power systems with SVC dynamic phasor model**
  - 💡 将动态相量理论引入SVC建模并与机电暂态程序结合，有效克服了传统TSP-EMTP混合仿真中的相位不连续与直流偏移问题。
  - 推导了基于动态相量理论的SVC单相详细数学模型。
  - 提出了SVC动态相量模型与交流子系统机电暂态模型之间的高效接口算法。
- **Interfacing Techniques for Transient Stability and Electromagnetic Transient Hyb**
  - 💡 首次系统构建TS-EMT混合仿真接口技术分类体系，并提出基于频移的一体化建模新路径。
  - 系统梳理并分类了TS与EMT混合仿真中的接口技术与关键实现问题。
  - 统一并规范了混合仿真器构建过程中涉及的术语、定义与标准方法。
- **Interfacing Techniques for Transient Stability and Electromagnetic Transient Hyb**
  - 💡 首次系统性地分类与规范了TS-EMT混合仿真接口技术体系，并创新性地引入频率平移法实现一体化建模。
  - 系统梳理并分类了暂态稳定与电磁暂态混合仿真中的接口技术与关键实施步骤。
  - 汇总并规范了混合仿真构建过程中使用的术语、定义与主流方法。
### 2012年 (2篇)
- **Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical**
  - 💡 将矢量拟合与半尺寸无源性检测相结合，构建了兼顾宽频特性与数值稳定性的电磁-机电混合仿真网络等值新方法
  - 提出适用于电磁-机电混合仿真的频率相关网络等值方法
  - 基于矢量拟合技术实现等值模型的严格无源性保证
- **电磁–机电暂态混合仿真中机电侧故障的仿真方法**
  - 💡 针对机电侧故障导致FDNE失效的问题，提出结合伴随初始化与临界电气距离指标的FDNE动态切换策略，兼顾混合仿真精度与计算效率。
  - 提出伴随仿真方法初始化新FDNE状态变量，有效抑制切换过程中的虚假暂态波动。
  - 提出临界电气距离指标，用于快速判断机电侧故障时是否需要更新FDNE。
### 2013年 (2篇)
- **Comparison between electromechanical transient model and electromagnetic transie**
  - 💡 首次结合TLS-ESPRIT算法与ADPSS混合仿真平台，定量对比并验证了直流机电暂态模型在低频振荡模态分析中的等效性与高效性。
  - 在ADPSS平台上构建了标准测试系统与实际电网的直流机电暂态及机电-电磁混合仿真模型。
  - 引入TLS-ESPRIT算法对故障后功率振荡信号进行模态分析，精准提取主导频率与阻尼比。
- **Electromechanical Transient Modeling of Modular Multilevel Converter Based Multi**
  - 💡 提出了一种基于动态过程定量分析的MMC-MTDC简化机电暂态模型，在保留关键控制特性的同时显著提升了大规模交直流系统机电暂态仿真的计算效率。
  - 建立了MMC的数学模型及其等效电路，结构类似于两电平换流器
  - 提出了适用于含MMC-MTDC系统的交直流网络潮流计算方法
### 2014年 (2篇)
- **Comparative study on electromechanical and electromagnetic transient model for g**
  - 💡 提出了一种基于纯数学计算的通用性光伏机电暂态模型，摒弃了高频开关与具体电路参数，在保证精度的同时大幅提升了大规模光伏系统仿真效率。
  - 提出了一种不包含电气元件和高频开关器件的通用性并网光伏机电暂态模型。
  - 通过纯数学计算替代复杂电路仿真，显著提升了大规模光伏电站的仿真计算速度。
- **基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真**
  - 💡 利用ADPSS实现了真实电网机电暂态模型与牵引系统电磁暂态模型的无缝接口与同步仿真，解决了传统简化等值模型精度低且适应性差的问题。
  - 基于ADPSS平台搭建了实际电力系统与牵引供电系统的机电-电磁暂态混合仿真模型，填补了联合仿真空白。
  - 验证了混合仿真方法的准确性，避免了传统方法中对主电网进行等值简化带来的精度损失。
### 2016年 (3篇)
- **A Hybrid Simulation Tool for the Study of PV Integration Impacts on Distribution**
  - 💡 提出了一种EMT与相量域协同的混合仿真架构，有效解决了高比例光伏配电网研究中精度与计算效率难以兼顾的难题。
  - 开发了一种将EMT仿真引擎与开源相量分析工具OpenDSS无缝接口的混合仿真平台。
  - 实现了光伏系统的详细电磁暂态建模与配电网其余部分相量域建模的协同仿真。
- **Application of Electromagnetic Transient-Transient Stability Hybrid Simulation t**
  - 💡 提出结合多端口三相戴维南等效与自动协议切换的交互机制，突破了传统混合仿真边界需保持三相平衡的限制，实现了大规模电网不对称故障与FIDVR现象的高精度仿真。
  - 开发了集成PSCAD/EMTDC与InterPSS的新型EMT-TS混合仿真平台。
  - 提出了一种带自动协议切换控制的组合交互协议以优化边界数据交换。
- **Co-Simulation of electromagnetic transients and Phasor models: A relaxation appr**
  - 💡 提出了一种结合边界变量预测、戴维南阻抗动态更新与单步EMT求解的松弛迭代架构，有效突破了传统EMT-PM混合仿真在收敛速度与计算效率上的瓶颈。
  - 提出了一种基于松弛迭代的EMT与相量模式联合仿真框架，兼顾了高精度与计算效率。
  - 系统评估并比较了多种多端口等效模型对PM-EMT迭代收敛性的影响。
### 2017年 (3篇)
- **A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems**
  - 💡 提出了一种保留详细换流器动态与交流系统非线性的多速率EMT协同仿真架构，通过高精度时变接口模型与振荡抑制算法解决了传统等值方法精度下降与数值不稳定的问题。
  - 提出了一种适用于大型交直流混合系统的多速率EMT协同仿真方法，显著提升了大规模电网的仿真效率。
  - 设计了结合移动窗口预测、逐步校正与平均技术的时变接口模型，有效消除了多速率交互中的混叠与时延误差。
- **A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT a**
  - 💡 提出基于两级舒尔补法与组合交互协议的分布式混合仿真接口技术，实现了多EMT子系统与TS子系统的高效、精确协同仿真。
  - 提出了一种分布式混合仿真架构，有效克服了传统集中式混合仿真中网络划分困难与效率低下的问题。
  - 设计了基于两级舒尔补法的接口更新技术，充分计及了多个EMT子系统之间的动态耦合关系。
- **Dynamic Phasor Based Interface Model for EMT and Transient Stability Hybrid Simu**
  - 💡 将动态相量理论引入混合仿真接口设计，通过基频与动态相量等效电路实现跨域高精度、低延迟数据交互。
  - 提出基于动态相量的接口模型(DPIM)，显著提升EMT与暂态稳定混合仿真的接口精度。
  - 构建TS-DPIM与DPIM-EMT间的双向等效接口，采用基频诺顿等效与动态相量戴维南等效实现数据交互。
### 2018年 (4篇)
- **A rotary frequency converter model for electromechanical transient studies of 16**
  - 💡 开发了基于标准同步电机理论且适配实际可用参数的相量域RFC模型，为低频铁路机电稳定性分析提供了开源工具。
  - 提出了一种适用于相量域机电暂态研究的同步-同步旋转变频器开放模型。
  - 模型设计直接兼容现有RFC的典型铭牌与运行数据，降低了建模门槛。
- **A rotary frequency converter model for electromechanical transient studies**
  - 💡 构建了首个基于公开可用数据、专用于低频铁路同步型旋转变频器的相量域机电暂态开放模型。
  - 提出了一种适用于低频铁路系统机电暂态稳定性研究的同步-同步型旋转变频器相量域开放模型。
  - 模型结构专门设计为可直接兼容并利用现有的RFC设备铭牌与测试数据。
- **Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching **
  - 💡 提出具备仿真模式切换能力的先进混合仿真架构，通过动态切换回纯相量域仿真显著提升大规模输配电系统的计算效率
  - 将混合仿真应用范围从输电网扩展至配电网及输配电网一体化系统
  - 构建了支持正序、三序、三相及混合表示的综合相量域建模与仿真框架
- **Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simul**
  - 💡 提出了一种基于专用映射算法与多时间步长处理的EMT-动态相量混合协同仿真接口技术，在保证局部快速暂态精度的同时大幅提升了大规模电网的仿真效率。
  - 构建了EMT与动态相量求解器的混合协同仿真架构。
  - 开发了瞬时EMT样本与动态相量傅里叶分量之间的精确映射算法。
### 2019年 (5篇)
- **A multi-area Thevenin equivalent based multi-rate co-simulation for control desi**
  - 💡 将MATE多速率协同仿真技术与基于虚拟阻抗的改进控制策略相结合，实现了兼顾高精度与高效率的LCC-HVDC系统电磁暂态仿真与控制设计。
  - 提出了一种基于MATE的多速率协同仿真方法，有效兼顾了电磁暂态仿真的精度与计算效率。
  - 构建了MATE传输线模型并结合多速率加速技术，显著提升了大规模交直流系统的仿真速度。
- **A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor D**
  - 💡 首次构建结合移频相量直流模型与电磁暂态交流模型的多域协同仿真框架，并通过HMD-TLM接口实现跨域高效数据交互与双波形同步输出。
  - 提出了一种将大规模交直流系统划分为直流SFP子系统与交流EMT子系统的多域协同仿真方法。
  - 开发了混合多域传输线模型（HMD-TLM）接口，有效处理跨域交互并实现瞬时值与相量波形的同步输出。
- **A Multi-rate Co-simulation of Combined Phasor-Domain and Time-Domain Models for **
  - 💡 首创结合移频相量模型与电磁暂态模型的多速率协同仿真架构，通过新型MD-TLM接口实现宽频带交互的高效精确模拟。
  - 提出结合移频相量域与时域的多速率协同仿真方法，解决传统方法难以捕获宽频带交互的问题。
  - 将交流电网侧仿真步长扩展至500µs，显著降低大规模系统的计算负担。
- **A Two-layer Network Equivalent with Local Passivity Compensation with Applicatio**
  - 💡 提出无需全局优化的双层网络等效与局部无源性补偿技术，在保证数值稳定性的同时大幅提升了混合仿真的收敛速度、精度与计算效率。
  - 提出了一种结合扰动测试与解析法的双层FDNE模型用于交流电网等效。
  - 开发了基于辅助有理函数的局部无源性补偿技术，避免了传统全局优化方法的收敛与效率瓶颈。
- **Shu 等 | A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency **
  - 💡 首创结合SFP直流模型与EMT交流模型的多域协同仿真框架，并通过HMD-TLM接口实现跨域高效交互与瞬时/相量波形同步。
  - 提出将直流子系统采用SFP模型、交流子系统采用EMT模型的多域协同仿真架构。
  - 开发HMD-TLM接口模型以精确处理跨域交互，并支持瞬时值与相量波形同步输出。
### 2020年 (3篇)
- **A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analy**
  - 💡 首创基于HPD-TLM接口的EMT-HPD跨域联合仿真架构，实现瞬时波形与谐波相量波形的同步高效分析。
  - 提出了一种适用于电力电子直流电网的谐波相量域(HPD)建模方法。
  - 构建了HPD传输线模型(HPD-TLM)，实现了HPD直流模型与EMT交流模型的高效接口与协调。
- **Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/**
  - 💡 提出接口位移与动态相量映射等效相结合的新型接口方案，通过物理位置迁移与等效建模实现子网松耦合，彻底避免接口变量形式转换并消除延迟误差。
  - 量化分析了混合仿真中接口延迟对系统精度的影响机制。
  - 总结了提升混合仿真接口精度的核心原则。
- **Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/**
  - 💡 提出接口位移与动态相量映射等效相结合的混合仿真接口方案，通过松耦合架构与免变量转换机制显著提升了交直流电网混合仿真的精度与稳定性。
  - 量化了混合仿真中接口延迟对系统精度的影响机制。
  - 总结了提升混合仿真接口精度的核心原则。
### 2021年 (3篇)
- **Assessment of dynamic phasor extraction methods for power system co-simulation a**
  - 💡 首次面向EMT-动态相量联合仿真接口需求，系统对比评估了主流动态相量提取方法的理论特性、数值局限与频谱表现，为大规模电力系统混合仿真提供了明确的算法选型指南。
  - 系统梳理并深入剖析了多种动态相量提取方法的底层理论与数值实现流程。
  - 全面评估了各方法在含机电振荡、直流偏置、谐波、不平衡及任意暂态等复杂信号下的相量特性。
- **Electromechanical transient modelling and application of modular multilevel conv**
  - 💡 将储能直接嵌入MMC子模块构建Active MMC，并建立其机电暂态等效模型以实现交直流系统解耦与协同控制。
  - 建立了含嵌入式储能子模块的Active MMC机电暂态数学模型及交直流侧等效电路。
  - 提出了聚焦于MMC换流器与储能子模块协同工作的控制策略。
- **Real-time RMS-EMT co-simulation and its application in HIL testing of protective**
  - 💡 提出了一种基于内置输电线路模型的实时RMS-EMT多速率协同仿真接口技术，并结合快速曲线拟合算法突破了传统HIL测试中系统规模受限与动态细节丢失的瓶颈。
  - 提出了一种利用内置三相输电线路模型实现实时RMS-EMT多域多速率协同仿真的接口技术。
  - 开发了一种非缓冲快速曲线拟合方法，以满足实时仿真中波形到相量转换的严格计算约束。
### 2022年 (4篇)
- **Co-simulation applied to power systems with high penetration of distributed ener**
  - 💡 将FMI/FMU标准封装与基于行波理论的虚拟输电线接口相结合，实现高渗透率DER电力系统的高效、频率无关协同仿真。
  - 提出了一种基于虚拟输电线的协同仿真架构，适用于高渗透率分布式能源电力系统。
  - 验证了协同仿真能够准确复现完整系统的动态仿真结果。
- **Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number**
  - 💡 通过直流标准化建模、数据自动映射拼接与接口电压箝位技术，实现了含大量直流电磁模型的大规模交直流电网混合仿真数据自动构建与平稳快速启动。
  - 提出了基于直流标准化建模与数据映射拼接的混合仿真数据自动建立方法，显著提升建模效率。
  - 设计了直流输电电磁模型运行工况自动调整策略，简化了复杂交直流电网的仿真设置。
- **Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid **
  - 💡 将ADPSS机电-电磁混合仿真技术应用于特高压直流分层接入系统，有效解决了单一仿真方法精度不足或计算效率低的问题。
  - 基于ADPSS平台成功搭建了含特高压分层接入直流的交直流混联电网混合仿真模型。
  - 通过与PSCAD模型对比，验证了底层纯电磁暂态模型的正确性。
- **Electromechanical transient-electromagnetic transient hybrid simulation of doubl**
  - 💡 在自主开发的PSD-PSModel平台上实现了双馈风机的电磁暂态-机电暂态混合仿真，突破了国外商业软件的技术垄断。
  - 基于双馈风机运行原理建立了详细的电磁暂态模型框架。
  - 在自主开发的PSD-PSModel平台上实现了机电-电磁暂态混合仿真功能。
### 2023年 (4篇)
- **A multi-solver framework for co-simulation of transients in modern power systems**
  - 💡 首创性地将EMT、DP、FAST与TS求解器集成于统一的多速率协同仿真架构中，实现按网络动态特性自适应分配求解资源以兼顾精度与效率。
  - 提出了一种融合动态相量、暂态稳定、FAST与EMT模型的多速率多求解器协同仿真框架。
  - 制定了基于设备类型、精度需求、电气距离和研究目的的网络分区与求解器/步长选择指南。
- **An aggregation method of permanent magnet synchronous wind farms for electromech**
  - 💡 提出了一种基于容量放大的PMSG风电场等效聚合方法，在保证电磁暂态仿真精度的前提下大幅提升了大规模风电场的仿真效率。
  - 提出了一种适用于大规模PMSG风电场电磁暂态仿真的等效聚合建模方法。
  - 构建了40台5MW机组的详细模型与200MW等效聚合模型，并给出了明确的聚合原则与流程。
- **Electromechanical Transient Modeling of the Low-Frequency AC System With Modular**
  - 💡 构建了适用于大规模电网机电暂态仿真的M3C-LFAC等效动态模型，填补了该类低频交流系统在传统机电仿真软件中的建模空白。
  - 建立了M3C的精确数学模型及其等效电路。
  - 提出了适用于含M3C-LFAC系统交流电网的迭代潮流计算算法。
- **Loop closing analytical calculation system based on electromagnetic-electromecha**
  - 💡 将机电-电磁混合仿真与自动网络划分及模型转换技术深度融合，实现了电网合环操作的高精度暂态评估与自动化分析。
  - 开发了基于机电-电磁暂态混合仿真的电网合环分析计算系统。
  - 提出了基于最大级数搜索算法的电磁网络自动划分方法。
### 2025年 (4篇)
- **An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Mod**
  - 💡 提出基于ESPRIT算法的EMT与SFEMT联合仿真接口，通过精准参数估计构建真实解析信号，有效克服了传统接口因负频分量导致的精度损失问题。
  - 推导了SFEMT建模的一般形式，为联合仿真接口设计提供了理论指导。
  - 提出了一种基于ESPRIT算法的EMT与SFEMT模型联合仿真接口。
- **Co-simulation and compensation method for parallel simulation of electromagnetic**
  - 💡 首次将无延迟补偿方法与FMI协同仿真框架深度融合，结合MANA公式与自适应步长策略，实现了高精度、强扩展性的离线EMT并行加速。
  - 提出了一种基于补偿方法的无延迟并行EMT协同仿真工具。
  - 将补偿方法推广至MANA公式并实现从潮流计算的自动初始化。
- **Design and Implementation of Scalable Communication Interfaces for Reliable and **
  - 💡 提出了一种兼顾本地低延迟与远程广域扩展的分级通信接口架构，有效突破了多速率实时协同仿真中的同步与稳定性瓶颈。
  - 设计并实现了一种可扩展的通信接口，支持高IBR渗透率电力系统的实时协同仿真。
  - 提出了本地局域网与远程互联网双模通信架构，分别优化低延迟交互与广域数据交换。
- **SFA-EMT hybrid simulation of power systems: Application to HVDC systems**
  - 💡 提出了一种无延迟、非迭代的SFA-EMT直接接口多速率混合仿真协议，通过并行EMT追踪复数分量实现灵活步长的高效耦合。
  - 提出了一种基于MATE框架的新型多速率混合协议，实现了SFA与EMT解的直接接口，无需时间步延迟或迭代。
  - 引入并行EMT解算以跟踪实部和虚部，从而能够直接与复数形式的SFA解进行无缝耦合。
### 2026年 (3篇)
- **27&28/Multi-rate real time hybrid simulation of controllable line commutated con**
  - 💡 提出结合离散电感解耦与解析参数优化的CPU-FPGA协同多速率仿真架构，有效解决了CLCC-HVDC系统小时间步建模与高效实时计算的矛盾。
  - 提出了面向CLCC-HVDC系统的CPU-FPGA协同多速率实时仿真框架。
  - 开发了以电感为自然解耦边界的离散电感解耦方法，实现复杂拓扑的高效分割。
- **Electromagnetic transient (EMT) and quasi static time series (QSTS) Co-simulatio**
  - 💡 提出了一种融合相量域QSTS与电磁暂态EMT的联合仿真架构，在保证精度的同时大幅提升了含高比例电力电子配电网的仿真效率。
  - 提出了一种将OpenDSS相量域分析与MATLAB/Simulink电磁暂态模型相结合的新型联合仿真框架。
  - 有效克服了传统OpenDSS在电力电子设备建模上的局限性，同时显著降低了全EMT仿真的计算复杂度。
- **Electromechanical transientelectromagnetic transient hybrid simulation method co**
  - 💡 提出考虑正负序参数差异的基波负序补偿法与最小二乘三序电流提取技术，实现了机电-电磁暂态混合仿真在不对称故障下的精确接口交互。
  - 提出了一套完整的机电-电磁暂态混合仿真方案，明确了接口母线选取与双向等值方法。
  - 针对等值电路正负序参数不一致的问题，提出了基波负序补偿法进行处理。
## 关键发现汇总
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 在9节点和新英格兰39节点系统上的测试表明，SVC动态相量模型与电磁暂态(EMTP)模型相比具有极高的精度。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 该混合仿真方法有效克服了传统TSP-EMTP混合仿真中的相位不连续和直流偏移问题。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 相比全系统EMTP仿真，该方法在保留关键设备波形细节的同时大幅减少了计算时间和内存占用。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 在9节点和新英格兰39节点系统上的测试表明，SVC动态相量模型的仿真精度与全电磁暂态模型高度一致。
- [2009] **Hybrid simulation of power systems with SVC dynamic phasor m**: 该混合仿真方法相比传统全系统EMTP仿真显著提升了计算效率并降低了内存资源消耗。
- [2009] **Interfacing Techniques for Transient Stability and Electroma**: 明确了混合仿真中时间步长差异与接口数据交换是制约仿真精度的核心瓶颈。
- [2009] **Interfacing Techniques for Transient Stability and Electroma**: 频移法能够有效消除TS与EMT模型间的频率尺度差异，实现无缝集成。
- [2009] **Interfacing Techniques for Transient Stability and Electroma**: 归纳的接口分类体系显著提升了混合仿真器开发的标准化程度与可复用性。
- [2009] **Interfacing Techniques for Transient Stability and Electroma**: 明确了混合仿真在系统分割、接口算法、数据同步及等效建模方面的核心挑战与解决路径。
- [2009] **Interfacing Techniques for Transient Stability and Electroma**: 验证了频率平移法在实现TS与EMT一体化建模中的理论可行性与潜在优势。
- [2009] **Interfacing Techniques for Transient Stability and Electroma**: 建立了完整的混合仿真接口技术分类体系，为后续算法开发与工程应用提供了参考基准。
- [2012] **Frequency Dependent Network Equivalent for Electromagnetic a**: 所提FDNE模型在宽频带内准确复现了外部网络的频率响应特性
- [2012] **Frequency Dependent Network Equivalent for Electromagnetic a**: 无源性强制方法彻底消除了混合仿真中的数值发散问题
- [2012] **Frequency Dependent Network Equivalent for Electromagnetic a**: 半尺寸检测算法显著降低了无源性校验的计算负担并提高了边界识别效率
- [2012] **电磁–机电暂态混合仿真中机电侧故障的仿真方法**: 伴随仿真方法能有效消除FDNE切换时产生的虚假暂态，保证混合仿真波形平稳过渡。
- [2012] **电磁–机电暂态混合仿真中机电侧故障的仿真方法**: 临界电气距离指标可准确筛选出对电磁侧影响显著的故障，避免不必要的FDNE重新计算。
- [2012] **电磁–机电暂态混合仿真中机电侧故障的仿真方法**: 所提切换策略在多个测试系统中验证了其在保证仿真精度的同时大幅提升了计算效率。
- [2013] **Comparison between electromechanical transient model and ele**: 两种模型提取的低频振荡主导频率与阻尼比数据高度一致，仿真波形吻合度良好。
- [2013] **Comparison between electromechanical transient model and ele**: 在交直流混合系统低频振荡分析中，直流机电暂态模型的计算精度与电磁暂态模型基本等效。
- [2013] **Comparison between electromechanical transient model and ele**: 机电暂态模型在保证分析精度的同时显著降低了计算复杂度，具备较高的工程实用价值。
- [2013] **Electromechanical Transient Modeling of Modular Multilevel C**: 简化模型仅保留外环控制器与部分直流网络动态，支持机电暂态仿真采用更大步长
- [2013] **Electromechanical Transient Modeling of Modular Multilevel C**: PSS/E机电暂态仿真结果与PSCAD电磁暂态模型结果高度一致，证明了模型精度
- [2013] **Electromechanical Transient Modeling of Modular Multilevel C**: MMC-MTDC系统能够有效隔离异步互联交流电网中的交流故障，提升系统稳定性
- [2014] **Comparative study on electromechanical and electromagnetic t**: 机电暂态模型的仿真输出结果与详细电磁暂态模型基本吻合，验证了模型精度。
- [2014] **Comparative study on electromechanical and electromagnetic t**: 采用纯数学计算的机电暂态模型大幅减少了仿真时间，有效克服了传统电磁模型计算步长小、速度慢的问题。
- [2014] **Comparative study on electromechanical and electromagnetic t**: 该模型成功集成于PSCAD/EMTDC平台，能够满足电力系统机电暂态分析对有效值电压/电流输出的需求。
- [2014] **基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真**: 混合仿真结果与纯电磁暂态仿真结果及典型值高度吻合，证明了模型的正确性。
- [2014] **基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真**: 牵引机车运行电流波形呈现明显畸变并含有大量谐波，验证了牵引负荷作为谐波源的特性。
- [2014] **基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真**: 该混合仿真方法在详细模拟牵引系统快速暂态过程的同时，有效兼顾了大规模电网的仿真规模与计算效率。
- [2016] **A Hybrid Simulation Tool for the Study of PV Integration Imp**: 混合仿真工具在保持与全EMT模型相近精度的同时，显著降低了计算时间和资源消耗。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[基于adpss的电力系统和牵引供电系统机电电磁暂态混合仿真|基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真]] | 2014 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[电力系统机电-电磁混合仿真边界解耦算法研究|电力系统机电-电磁混合仿真边界解耦算法研究]] | 2022 |
| [[电力系统机电-电磁混合仿真边界解耦算法研究|电力系统机电-电磁混合仿真边界解耦算法研究]] | 2022 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统风力发电建模与仿真研究综述|电力系统风力发电建模与仿真研究综述]] | 2024 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Revisiting dynamic phasors and their efficacy in simulating ]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |

---
title: "混合仿真"
type: topic
tags: []
created: "2026-04-13"
---

# 混合仿真

## 论文方法分析
> 基于 46 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 机电-电磁暂态混合仿真 | 4 | Electromechanical-electromagnetic Hybrid Simulation Technology With La |
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
|----------|----------|| 模块化多电平换流器(MMC) | 4 |
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

## 深度增强内容

 基于提供的46篇论文深度分析，以下是"混合仿真"主题页的深度增强内容：

---

# 混合仿真

## 1. 关键技术详解

### 1.1 机电-电磁暂态接口技术

混合仿真的核心是解决机电暂态(TS, $h \approx 10$ ms)与电磁暂态(EMT, $h \approx 50$ μs)之间的**多时间尺度耦合**问题。接口技术主要包含三个维度：

**等值模型选择**
- **单端口戴维南等值**：适用于远离非线性负荷的边界，等值电路为$\dot{V}_{th} - Z_{th}\dot{I}$。当接口母线远离故障点（电气距离$D > D_{cr}$，通常3-5个节点）时，固定等值参数误差可控制在2%以内。
- **多端口戴维南等值**：考虑正/负/零序阻抗，适用于多馈入HVDC系统。多端口等值可将逆变侧换相失败分析误差从8-12%降至1%以内，但导纳矩阵维数随端口数$N$呈$O(N^3)$增长。
- **频率相关网络等值(FDNE)**：基于矢量拟合(Vector Fitting)构建宽频模型：
  $$Y(s) = \sum_{i=1}^{n} \frac{r_i}{s-p_i} + d + se$$
  通过10-20个频点扫描(0.1 Hz–2.5 kHz)，20-30阶拟合即可实现残差<1%，能准确表征至25次谐波。

**数据转换与相量提取**
接口处需实现瞬时值$x(t)$与相量$\tilde{X}$的双向映射：
$$x(t) = \text{Re}\{\tilde{X}(t)e^{j\omega_0 t}\}$$
改进的dq-120结合Prony算法可在故障后5个采样点内精确提取基波分量，在40%谐波畸变下幅值误差<0.3%，相位误差<0.5°。

**插值与预测算法**
为消除步长差异导致的数值振荡，采用拉格朗日插值或线性插值：
- 接口插值算法可将边界数值振荡幅度降低85%以上，最大过冲从12%降至1.5%
- 基于预测-校正的并行交互时序，通过3-5次迭代可使接口功率偏差收敛至<0.1%

### 1.2 多速率协同机制

**时间步长协调**
典型步长比$N = h_{TS}/h_{EMT} = 200$（10 ms/50 μs）。当$N > 100$时，传统双边迭代法可能发散，需采用基于网络等值的解耦算法。

**交互时序策略**
| 时序类型 | 相位误差 | 实时性 | 适用场景 |
|---------|---------|--------|----------|
| **串行时序** | $\Delta\phi \approx 2\pi f \Delta t$（10ms步长下约18°） | 不满足实时 | 离线精度优先 |
| **并行时序** | <2°（预测校正后） | 满足 | 实时仿真 |
| **混合多域TLM** | <1%稳态误差 | 满足 | 交直流混合系统 |

### 1.3 宽频建模与解耦技术

**移频相量法(SFP)**
通过频移变换$x(t) = \text{Re}\{\tilde{x}(t)e^{j\omega_s t}\}$，将信号频谱搬移至基带，允许采用比传统EMT大20-50倍的步长（如2 ms），计算效率提升一个数量级，同时保持基波动态精度误差<1%。

**传输线解耦**
利用分布参数长线的波传播延时$\tau$实现自然解耦：
- 传统模型受限于$\Delta t \leq \tau_{min}$（通常<1 ms）
- 改进的HMD-TLM接口引入额外开销<3%，支持SFP与EMT子系统并行计算，加速比接近线性

**边界分组解耦**
将边界节点分组处理，电磁侧接口计算复杂度从$O(N^3)$降低。当电磁子网单相节点数$m=100$时，$N=150$是效率转折点；超过此值计算量进入非线性增长区。

### 1.4 电力电子设备建模

**恒导纳开关模型**
采用广义ADC(Associated Discrete Circuit)开关模型，使开关动作前后系统导纳矩阵保持不变，避免每次开关动作重新进行LU分解。对于含$N$个换流阀的系统，避免$2^N$种拓扑的矩阵预存爆炸。

**伴随仿真技术**
针对FDNE切换时的虚假暂态(spurious transient)，采用"热备用"双FDNE并行运行：
- 伴随仿真增加计算量约14%（可接受范围）
- 实现状态变量无缝切换，暂态波动抑制至纯EMT水平

---

## 2. 硬件平台对比

| 平台架构 | 典型步长 | 最大规模 | 单步计算时间 | 频率带宽 | 关键特性 |
|---------|---------|---------|-------------|---------|---------|
| **RTDS** | 50 μs | ~100节点/核 | <50 μs | <10 kHz | 商业成熟，支持HIL，CBuilder自定义建模 |
| **FPGA** | 1-2 μs | 资源受限 | 24 ns (最低报道) | DC–数MHz | 可重构硬件，支路级并行，纳秒级确定性延迟 |
| **CPU-FPGA异构** | CPU:100 μs<br>FPGA:1 μs | 中等 | FPGA:1 μs | 宽频 | 控制与电路分离，100:1时间尺度配合，消除通信延迟 |
| **CPU-GPU** | 20-100 μs | 3000+子模块 | 取决于传输 | 中等 | 细粒度并行，但CPU-GPU数据传输是瓶颈 |
| **ADPSS** | 机电:10 ms<br>电磁:50 μs | 10000+节点<br>1000台发电机 | - | 低频为主 | 机电-电磁混合，适合超大规模电网 |

**实时性关键指标**：
- **HIL接口延迟**：DCCB控制器与仿真器接口延迟需<50 μs，控制采样率20 kHz
- **数值稳定性**：实时仿真需满足$\Delta t < \tau_{min}$且低于奈奎斯特频率5-10倍：$f_{max} < f_{Ny}/5$

---

## 3. 实际应用案例汇总

### 3.1 高压直流输电系统

**MMC-MTDC系统仿真**
- **方法**：SFP-EMT混合多域协同仿真
- **规模**：三端直流电网含12个DCCB
- **性能**：稳态误差<0.5%，直流故障电流峰值误差2-4%，分断时间<5ms（LCS<1ms, UFD 2-3ms）
- **效率**：相比纯EMT提升6-10倍，与系统规模呈线性而非指数关系

**HVDC频率相关等值**
- **技术**：FDNE等值(1-2 kHz，500个频率采样点)
- **精度**：12脉波HVDC的11/13/23/25次特征谐波保留，THD计算精度>95%（传统准稳态等值仅70-80%）

### 3.2 新能源并网

**大规模风电场**
- **等值方法**：多机动态等值（通常1-4群），风速三次方加权
- **混合策略**：风电场内部EMT详细建模，外部电网TS建模
- **验证**：谐波含量偏差<0.6%（3次谐波23.42% vs 23.98%）

**虚拟同步并网逆变器**
- **平台**：CPU-FPGA异构，FPGA负责逆变器电磁暂态(1 μs)，CPU负责控制(100 μs)
- **优势**：满足电力电子小步长(≤2 μs)实时仿真需求，避免传统多处理器5-10 μs通信延迟

### 3.3 交直流混合电网

**牵引供电系统**
- **场景**：实际383节点电网与牵引供电系统联合仿真
- **方法**：基于ADPSS的机电-电磁混合仿真，UD模块补偿无功功率不匹配
- **结果**：避免传统等值简化，适应电网运行方式变化；近端母线电压跌落显著大于远端

**含UPFC的柔性交流输电**
- **模型**：UPFC动态相量模型（保留0阶直流+1阶基频）
- **接口**：交替迭代算法，收敛性良好
- **控制精度**：并联侧电压控制误差<1%，直流电压稳态误差<0.5%，串联侧潮流响应时间100-200 ms

### 3.4 直流电网保护

**直流断路器(DCCB)硬件在环**
- **模型**：混合式DCCB详细实时模型，计算复杂度$O(n)$（$n$为主支路单元数）
- **验证**：实时模型与离线模型电流峰值偏差<1%，过电压峰值偏差<2%
- **工况**：验证软启动模式（充电电流限制在1.2倍额定电流以内）

---

## 4. 研究趋势与开放问题

### 4.1 前沿研究方向

**信息-物理-电磁三元融合**
向"信息-电磁-机电"三元混合仿真演进，将通信系统延时、丢包与电力电子电磁暂态、机电振荡耦合分析，支撑 cyber-physical power system (CPPS) 研究。

**自适应智能接口**
基于临界电气距离$D_{cr}$的自适应FDNE切换策略：
- 当故障距离$D > D_{cr}$时保持等值不变，减少60%以上FDNE更新计算
- 开发基于轨迹灵敏度分析的自动接口位置优化算法

**超实时与并行加速**
- **FPGA可重构计算**：实现单步24 ns的超实时仿真，支持全系统统一纳秒级步长（消除多速率近似误差）
- **GPU细粒度并行**：解决3000子模块MMC系统传统仿真需3000小时的问题，目标步长提升至100 μs

**电力电子化系统挑战**
针对高比例电力电子设备接入导致的$2^N$拓扑爆炸问题，研究：
- 基于机器学习的导纳矩阵快速更新
- 事件驱动与固定步长混合仿真

### 4.2 开放技术问题

**1. 多端口耦合与精度权衡**
单端口等值忽略端口间耦合，在多馈入直流系统中误差达8-12%；而多端口等值计算复杂度$O(N^3)$。如何建立自适应端口聚合机制，在精度与效率间动态平衡？

**2. 开关事件与数值稳定性**
电力电子频繁开关导致拓扑突变，每次需重新LU分解。现有预存$2^N$种导纳矩阵的方法存储量随$N$指数增长。如何开发开关组预识别或矩阵快速修正算法？

**3. 宽频模型一致性**
FDNE在1-2 kHz频段有效，但电力电子开关产生的高频谐波(>10 kHz)与机电暂态(0.1-10 Hz)跨越4个数量级。如何构建全频段统一模型？

**4. 实时仿真规模瓶颈**
纯EMT实时仿真受限于100节点规模，而实际电网需10000+节点。现有混合仿真在$N>150$边界节点时效率骤降。如何开发分层分区的大规模并行架构？

**5. 多物理场耦合**
电力系统与热力、机械系统的多物理场联合仿真接口标准缺失，需建立能量守恒约束下的跨域耦合规范。
---
title: "2169-3536 (c) 2018 IEEE. Translations and content mining are permitted for academic research only. Personal use is also "
type: source
authors: ['未知']
year: 2018
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient GPU-based electromagnetic transient simulation for power systems with thread-oriented tran_Song 等_2018.pdf"]
---

# 2169-3536 (c) 2018 IEEE. Translations and content mining are permitted for academic research only. Personal use is also 

**作者**: 
**年份**: 2018
**来源**: `15/Efficient GPU-based electromagnetic transient simulation for power systems with thread-oriented tran_Song 等_2018.pdf`

## 摘要

Electromagnetic transients (EMT) simulation is the most accurate and intensive computation for power systems. Past research has shown the potential of accelerating such simulations using graphics processing units (GPUs). In this paper, an efﬁcient GPU-based parallel EMT simulator is designed. Thread- oriented model transformations are ﬁrst proposed for the electrical and control systems. Following the transformations, the electrical system is represented by connected networks of massive primitive electrical elements, the computations of which can be constructed as massive fused multiply-add operations and solutions to a linear equation. The control systems are represented by a layered directed acyclic graph with primitive control elements that can be dealt with using SIMT groups. Finally, 

## 核心贡献





- 提出面向线程的电气归一化变换，将网络转为基本元件连接，计算统一为FMA操作
- 构建控制系统分层有向无环图，利用SIMT线程组并行处理，突破复杂控制计算瓶颈
- 开发运行时自动代码生成工具，大幅减少GPU寻址与访存，提升内核效率与算法通用性


## 使用的方法





- [[节点分析法|节点分析法]]
- [[gpu并行计算|GPU并行计算]]
- [[面向线程的模型变换|面向线程的模型变换]]
- [[自动代码生成|自动代码生成]]
- [[融合乘加运算|融合乘加运算]]
- [[分层有向无环图建模|分层有向无环图建模]]
- [[simt并行架构|SIMT并行架构]]


## 涉及的模型





- [[ieee-33节点配电系统|IEEE 33节点配电系统]]
- [[分布式电源|分布式电源]]
- [[电力电子变换器|电力电子变换器]]
- [[基本电气元件|基本电气元件]]
- [[交直流混合电网|交直流混合电网]]


## 相关主题





- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行加速|GPU并行加速]]
- [[实时仿真|实时仿真]]
- [[自动代码生成|自动代码生成]]
- [[大规模配电网仿真|大规模配电网仿真]]
- [[异构计算|异构计算]]


## 主要发现





- 在NVIDIA K20x与P100上测试，该方法相比CPU程序显著加速了电磁暂态仿真
- 自动代码生成工具有效降低访存开销，使GPU内核计算效率与线程负载均衡性大幅提升
- 针对含分布式电源的扩展配电系统，该方法在特定规模下成功实现了电磁暂态实时仿真



## 方法细节

### 方法概述

提出一种面向线程的全GPU并行电磁暂态(EMT)仿真框架。首先，对电气系统进行面向线程的归一化变换，通过线性状态扩展将复杂多端口元件解耦为仅含基本电气元件（电阻、电感、电容、互感、受控源）的网络，使所有计算统一为融合乘加(FMA)操作，彻底消除Warp内线程异构性。其次，对控制系统采用分层有向无环图(LDAG)建模，利用SIMT线程组按层同步处理，替代传统原子竞争机制，解决控制信号依赖导致的线程串行等待。最后，设计运行时自动代码生成工具，根据具体算例拓扑动态生成GPU内核，消除多层间接寻址与冗余全局内存访问，大幅提升内核执行效率与算法通用性。整体流程在每个积分步内依次执行：控制系统求解、电气元件状态更新、节点电流累加、网络电压方程求解。

### 数学公式


**公式1**: $$$I(t) = G U(t) + I_{ne}(t)$$$

*电气元件诺顿等效电路模型，表示端口电流与电压及历史等效电流的线性关系*


**公式2**: $$$I_{ne}(t) = P I(t-\Delta t) + Q U(t-\Delta t) + C(t)$$$

*诺顿等效历史电流递推公式，包含历史状态矩阵与控制输入项*


**公式3**: $$$\dot{x} = Ax + Bu, \quad y = Cx + Du$$$

*原始多端口电气元件的状态空间微分方程模型*


**公式4**: $$$x = Mz, \quad MKv = Ax + Bu, \quad N = CM$$$

*面向线程的线性状态扩展变换，用于将原耦合模型解耦为独立基本元件*


**公式5**: $$$\dot{z} = Kv, \quad y = Nz + Du$$$

*变换后的解耦状态方程，K矩阵每行仅1个非零元，N矩阵仅含{0,1,-1}，实现线程计算同质化*


**公式6**: $$$i_{ne}(t+\Delta t) = A u_b(t) + B i_b(t)$$$

*基本电气元件诺顿等效电流更新式，直接映射为GPU线程的FMA操作*


### 算法步骤

1. 步骤1（控制系统求解）：基于LDAG拓扑将控制模块分层。为每层分配独立SIMT线程组，按层级顺序并行计算基本控制指令。层间设置同步屏障，确保上游输出就绪后再执行下游计算，最终生成电气元件控制输入向量C(t)。

2. 步骤2.1（诺顿电流并行计算）：为每个基本电气元件分配独立GPU线程。读取上一时刻节点电压与历史电流，执行统一的FMA操作 $i_{ne}(t+\Delta t) = A u_b(t) + B i_b(t)$，所有线程指令完全一致，无分支发散。

3. 步骤2.2（节点注入电流累加）：各线程通过原子操作(atomicAdd)将计算得到的诺顿等效电流累加至共享内存中的节点注入电流数组。执行线程块同步，确保所有节点电流更新完毕且无数据竞争。

4. 步骤3（网络方程求解）：调用GPU稀疏线性代数求解器（如cuSOLVER或GLU）求解节点导纳矩阵方程 $YU = I$，获得当前时刻全网节点电压向量，作为下一积分步的边界条件。


### 关键参数

- **线程块最大规模**: 1024线程/Block

- **线程束(Warp)规模**: 32线程/Warp

- **变换矩阵K约束**: 每行仅含1个非零元素

- **变换矩阵N约束**: 元素仅取值{0, 1, -1}

- **积分步长**: Δt（由系统最高暂态频率与数值稳定性决定）

- **GPU硬件平台**: NVIDIA Tesla K20x, Tesla P100



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多IEEE 33节点配电系统级联含分布式电源与电力电子变换器 | 通过互联多个IEEE 33节点系统并接入DERs与PECs构建大规模交直流混合测试网。在NVIDIA K20x与P100上运行全GPU仿真，验证线程归一化变换与自动代码生成的有效性。 | 相比传统CPU串行EMTP程序实现显著加速；在特定系统规模下达到实时仿真性能（单步计算耗时≤实际物理时间步长，即实时比≤1.0），且加速效果随系统规模扩大呈非线性提升。 |



## 量化发现

- 面向线程的归一化变换将异构计算统一为FMA操作，消除Warp内指令发散，理论并行度(DOP)与基本元件数量呈严格正比。
- 自动代码生成工具在运行时动态编译内核，消除多层间接寻址与冗余全局内存访问，内存带宽利用率显著提升，内核执行效率大幅优化。
- LDAG分层同步机制替代原子竞争函数，避免控制依赖导致的线程串行化，控制系统仿真吞吐量随组件数量线性扩展。
- 在NVIDIA P100平台上，针对含大量电力电子变换器的交直流混合系统，实现实时仿真能力（仿真步长推进时间≤物理时间），满足闭环控制验证需求。


## 关键公式

### 面向线程的解耦状态方程

$$$\dot{z} = Kv, \quad y = Nz + Du$$$

*用于将复杂多端口电气元件转化为基本元件网络，使每个状态变量独立对应一个GPU线程，实现计算指令与访存模式的完全统一*

### 基本元件诺顿等效电流递推式

$$$i_{ne}(t+\Delta t) = A u_b(t) + B i_b(t)$$$

*GPU内核核心计算单元，所有电气元件更新均转化为该形式的FMA操作，完美适配GPU单指令多线程(SIMT)架构*

### 节点电压网络方程

$$$YU = I$$$

*在每个积分步末尾调用GPU稀疏线性求解器求解，获取全网节点电压以推进暂态过程*



## 验证详情

- **验证方式**: 全GPU并行仿真与CPU基线程序对比分析，通过构建不同规模的测试系统验证加速比、实时性与算法可扩展性
- **测试系统**: 由多个IEEE 33节点配电系统级联扩展而成的大规模交直流混合电网，包含分布式电源(DERs)与电力电子变换器(PECs)
- **仿真工具**: 基于CUDA架构的自定义全GPU并行EMT仿真器，对比基线为传统CPU串行EMTP程序，线性求解器采用cuSOLVER/GLU
- **验证结果**: 所提方法在保持EMTP算法数值精度的前提下，通过线程归一化变换与自动代码生成显著降低GPU访存与寻址开销。测试表明，该方法能有效处理大规模强耦合电网的电磁暂态过程，在特定规模下实现实时仿真（耗时比≤1.0），具备工程应用潜力。

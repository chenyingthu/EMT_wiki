---
title: "Massively Parallel Modeling of Battery Energy Storage Systems for AC/DC Grid High-Performance Transient Simulation"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;3;10.1109/TPWRS.2022.3196286"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Lin 等 - 2023 - Massively Parallel Modeling of Battery Energy Storage Systems for ACDC Grid High-Performance Transi.pdf"]
---

# Massively Parallel Modeling of Battery Energy Storage Systems for AC/DC Grid High-Performance Transient Simulation

**作者**: 
**年份**: 2023
**来源**: `25/Lin 等 - 2023 - Massively Parallel Modeling of Battery Energy Storage Systems for ACDC Grid High-Performance Transi.pdf`

## 摘要

—Extensive integration of power electronics appara- tuses complicates the modern power grid and consequently necessi- tates time-domain transients study for its planning and operation. In this work, a heterogeneous computing architecture utilizing the CPU and graphics processing unit (GPU) is proposed for the efﬁcient study of interactions between a power grid network and massive utility-scale battery energy storage systems (BESSs). The device-level electromagnetic transient (EMT) simulation aiming at enhanced ﬁdelity of the BESS is conducted simultaneously with electro-mechanical transient stability (TS) simulation which suf- ﬁces system-level dynamic security assessment. Since the reser- vation of a large amount of energy storage units is computation- ally intensive for the CPU, the conc

## 核心贡献


- 提出CPU-GPU异构架构实现EMT-TS联合仿真，兼顾设备级高精度与系统级动态评估
- 构建向量化电池与TLL变流器模型，将储能异构性转为同构性以实现GPU细粒度并行
- 引入多流异步处理与多速率机制，优化异构资源调度与跨步长数据交互效率


## 使用的方法


- [[emt-ts联合仿真|EMT-TS联合仿真]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]
- [[多速率仿真|多速率仿真]]
- [[多流异步处理|多流异步处理]]
- [[向量化建模|向量化建模]]
- [[传输线链接-tll-模型|传输线链接(TLL)模型]]
- [[状态空间法|状态空间法]]
- [[后向欧拉离散|后向欧拉离散]]


## 涉及的模型


- [[电池储能系统-bess|电池储能系统(BESS)]]
- [[电力电子变流器|电力电子变流器]]
- [[戴维南等效电池模型|戴维南等效电池模型]]
- [[交直流电网|交直流电网]]
- [[ieee-118节点系统|IEEE 118节点系统]]


## 相关主题


- [[高性能计算|高性能计算]]
- [[并行计算|并行计算]]
- [[混合仿真|混合仿真]]
- [[电磁暂态|电磁暂态]]
- [[暂态稳定|暂态稳定]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 异构架构在含大规模储能的IEEE 118节点系统中实现超200倍仿真加速
- 设备级精度经MATLAB/Simulink验证，系统级精度经DSATools验证
- 多速率与向量化模型有效降低计算负担，保障跨时间尺度数据交互实时性



## 方法细节

### 方法概述

本文提出一种基于CPU-GPU异构计算架构的EMT-TS联合仿真方法，用于高效分析含海量公用级电池储能系统（BESS）的交直流电网暂态交互。针对传统CPU串行处理大规模异构储能单元计算负担重的问题，采用向量化建模技术将不同化学类型（锂离子、铅酸、镍镉）电池的戴维南等效模型转化为同构向量形式，以充分适配GPU的细粒度SIMT并行架构。电力电子变流器侧采用传输线链接（TLL）模型进行拓扑解耦与导纳矩阵降维。仿真框架引入多速率机制（EMT微秒级步长与TS毫秒级步长）与CUDA多流异步处理技术，实现异构计算资源的灵活调度、跨步长数据高效交互与PCIe传输延迟掩盖，从而在单一计算节点上兼顾设备级高精度电磁暂态捕捉与系统级机电暂态稳定评估。

### 数学公式


**公式1**: $$$$V_{\text{Bat}} = E_0 + E_{\text{pol}} + E_{\text{exp}} + S_{\text{ch}} E_{\text{chg}} + (1 - S_{\text{ch}}) E_{\text{dsc}}$$$$

*电池戴维南等效电压源表达式，包含恒定电压、极化电压、指数区电压及充放电动态电压，$S_{\text{ch}}$为充放电状态二值标志。*


**公式2**: $$$$\frac{d}{dt} E_{\text{exp}}(t) = (B \cdot |i(t)|)(S_{\text{ch}} A - E_{\text{exp}}(t))$$$$

*指数区电压在时域的微分方程形式，由s域传递函数经拉普拉斯逆变换推导得出，用于描述电池非线性极化动态。*


**公式3**: $$$$E_{\text{exp}}(t) = (1 - |i(t)| B \Delta t) E_{\text{exp}}(t - \Delta t) + B \cdot |i(t)| S_{\text{ch}} A \Delta t$$$$

*采用后向欧拉法对指数区电压微分方程进行离散化，实现EMT仿真中的递推计算。*


**公式4**: $$$$\text{SOC}(t) = \text{SOC}(t_0) + \int_{t_0}^{t} \frac{i(\tau)}{Q} d\tau$$$$

*电池荷电状态（SOC）积分表达式，$Q$为额定容量，用于实时追踪储能单元剩余能量。*


**公式5**: $$$$V_{\text{Bat}} = E_0 + E_{\text{pol}} + E_{\text{exp}} + S_{\text{ch}} \circ E_{\text{chg}} + (I - S_{\text{ch}}) \circ E_{\text{dsc}}$$$$

*向量化电池电压通用表达式，$\circ$表示逐元素运算，将异构电池参数统一为向量形式以支持GPU并行。*


**公式6**: $$$$I_{\text{Beq}} = V_{\text{Bat}} \circ G_B$$$$

*电池阵列诺顿等效电流源向量化计算，$G_B$为内部电导向量，用于接入电网节点导纳矩阵求解。*


### 算法步骤

1. 1. 系统初始化与内存分配：在CPU端加载交直流电网拓扑、TS模型参数及多速率步长配置；在GPU端分配全局内存，将海量BESS的初始状态（SOC、电压、电流、化学类型系数$A,B,K_Q,Q,i_{\text{sat}}$）打包为同构向量并传输至设备端。

2. 2. 多速率步长同步与任务划分：设定EMT仿真步长$\Delta t_{\text{EMT}}$（微秒级）与TS仿真步长$\Delta t_{\text{TS}}$（毫秒级）。在每个$\Delta t_{\text{TS}}$周期内，GPU需执行$N = \Delta t_{\text{TS}} / \Delta t_{\text{EMT}}$次EMT子步计算，CPU执行一次TS网络潮流与机电暂态求解。

3. 3. GPU向量化EMT并行计算：利用CUDA内核启动细粒度线程块，每个线程独立处理一个BESS单元。按公式(9)逐元素计算向量化电池电压，结合TLL变流器模型进行开关状态更新与状态空间离散求解，同步更新SOC向量。

4. 4. CPU TS网络求解与接口映射：CPU基于正序相量模型求解系统级微分代数方程。在耦合节点处，将GPU计算的EMT侧诺顿等效源（$I_{\text{Beq}}, G_B$）经多速率插值/外推转换为TS侧等效注入，实现跨域数据交互。

5. 5. 多流异步调度与数据重叠：利用CUDA Streams将GPU计算划分为多个独立流。在流1执行EMT内核计算的同时，流2异步进行主机-设备间的数据传输（PCIe），流3处理结果回传与TS接口数据打包，有效掩盖通信延迟。

6. 6. 迭代推进与收敛判断：完成当前时间步的EMT-TS数据交换后，检查全局残差或预设仿真时长。若未结束，则更新状态向量并跳转至步骤3，直至完成全时段暂态过程仿真。


### 关键参数

- **EMT_time_step**: 微秒级（通常10~50 μs）

- **TS_time_step**: 毫秒级（通常1~10 ms）

- **battery_coefficients**: A, B, K_Q, Q, i_sat（依锂离子、铅酸、镍镉类型区分）

- **array_configuration**: N_p × N_s（电池串并联阵列规模）

- **GPU_streams**: 多CUDA流（用于异步计算与数据传输重叠）

- **interface_method**: TLL解耦与诺顿/戴维南等效源映射



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 118节点交直流电网集成海量分布式BESS | 在标准IEEE 118节点系统中接入大规模公用级电池储能阵列，执行全系统EMT-TS联合暂态仿真。系统成功捕捉了变流器开关级微秒暂态与电网机电振荡的交互过程，设备级电压/电流波形与系统级频率/功角动态均保持稳定。 | 相较于传统纯CPU串行EMT仿真软件，异构架构实现加速比超过200倍，使原本计算不可行的大规模系统离线仿真变为可行。 |



## 量化发现

- 异构CPU-GPU架构实现仿真加速比 > 200倍
- EMT仿真步长设定为微秒级（μs），TS仿真步长为毫秒级（ms），多速率耦合有效降低计算冗余
- 向量化建模将异构电池参数统一为同构向量，消除GPU并行中的分支发散，提升SM利用率
- 多流异步处理技术有效掩盖PCIe数据传输延迟，实现计算与通信的重叠执行
- TLL模型实现变流器与电网的解耦，显著降低节点导纳矩阵维度与求逆计算复杂度


## 关键公式

### 后向欧拉离散递推公式

$$$$E_{\text{exp}}(t) = (1 - |i(t)| B \Delta t) E_{\text{exp}}(t - \Delta t) + B \cdot |i(t)| S_{\text{ch}} A \Delta t$$$$

*用于EMT仿真中电池指数区极化电压的时域步进计算，保证数值稳定性与微秒级暂态精度。*

### 向量化电池电压模型

$$$$V_{\text{Bat}} = E_0 + E_{\text{pol}} + E_{\text{exp}} + S_{\text{ch}} \circ E_{\text{chg}} + (I - S_{\text{ch}}) \circ E_{\text{dsc}}$$$$

*将多类型电池的非线性动态统一为逐元素向量运算，是GPU细粒度并行加速的核心数学基础。*

### 诺顿等效电流源向量化

$$$$I_{\text{Beq}} = V_{\text{Bat}} \circ G_B$$$$

*将电池阵列转换为并联电导与电流源形式，便于直接注入电网节点导纳矩阵进行KCL求解。*



## 验证详情

- **验证方式**: 对比仿真验证（设备级与系统级双维度交叉验证）
- **测试系统**: IEEE 118节点交直流电网系统（集成大量分布式BESS阵列）
- **仿真工具**: MATLAB/Simulink（设备级EMT基准）、DSATools/TSAT（系统级TS基准）、自研CPU-GPU异构并行仿真平台
- **验证结果**: 设备级BESS电压/电流/SOC动态与MATLAB/Simulink结果高度吻合；系统级频率、电压及功角稳定性指标与DSATools/TSAT正序相量仿真结果一致。在保持工程允许误差范围内，异构平台实现超200倍加速，验证了大规模交直流电网高精度暂态仿真的可行性与准确性。

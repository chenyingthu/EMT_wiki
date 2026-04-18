---
title: "Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Systems;2025;40;1;10.1109/TPWRS.2024.3409729"
tags: ['renewable']
created: "2026-04-13"
sources: ["EMT_Doc/25/Cheng 等 - 2025 - Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy.pdf"]
---

# Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems

**作者**: 
**年份**: 2024
**来源**: `25/Cheng 等 - 2025 - Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy.pdf`

## 摘要

—Renewable energy systems (RESs) are pivotal in the transition to eco-friendly smart grids. The complexity and uncer- tainty of RESs, driven by uncontrollable natural forces like sun- light and wind, bring challenges to integrating RESs into modern power systems. Electromagnetic transient (EMT) simulation is an effective method for studying the integration of RESs. Currently, the EMT simulation of RESs is limited to small-scale and lumped RES models due to the model complexity and nonlinearity, which cannot reﬂect the detailed characteristics of large-scale RESs in practice. This paper introduces a data-oriented, machine learning- enhanced approach to achieve massively parallel EMT simulation on CPU-GPU, designed to efﬁciently model and simulate large- scale, detailed RES. It incorporates 

## 核心贡献


- 提出基于MLP与GRU神经网络的新能源数据驱动建模方法替代传统非线性迭代
- 构建面向数据的实体组件系统架构与GPU实例化策略实现ANN模型高效并行集成
- 采用蒙特卡洛方法生成训练数据精准拟合光伏阵列局部遮荫等多变量非线性特性


## 使用的方法


- [[人工神经网络-ann|人工神经网络(ANN)]]
- [[多层感知机-mlp|多层感知机(MLP)]]
- [[门控循环单元-gru|门控循环单元(GRU)]]
- [[蒙特卡洛数据生成|蒙特卡洛数据生成]]
- [[实体组件系统-ecs-架构|实体组件系统(ECS)架构]]
- [[gpu实例化技术|GPU实例化技术]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]


## 涉及的模型


- [[光伏阵列-pv|光伏阵列(PV)]]
- [[dfig-model|DFIG]]
- [[储能电池系统|储能电池系统]]
- [[风电场|风电场]]
- [[微电网|微电网]]
- [[ieee-118节点系统|IEEE 118节点系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大规模新能源并网|大规模新能源并网]]
- [[并行计算|并行计算]]
- [[机器学习建模|机器学习建模]]
- [[gpu加速仿真|GPU加速仿真]]
- [[数据驱动建模|数据驱动建模]]
- [[新能源场站建模|新能源场站建模]]


## 主要发现


- 在含两百万新能源实体的系统中仿真速度较传统CPU非线性迭代提升四百倍
- 神经网络模型经MATLAB验证精度满足电磁暂态仿真要求且计算结构统一
- 采用单精度浮点数与统一矩阵运算显著降低GPU显存开销与主机设备数据交换延迟



## 方法细节

### 方法概述

本文提出一种面向数据、机器学习增强的CPU-GPU异构大规模并行电磁暂态(EMT)仿真方法。针对传统新能源系统(RES)EMT仿真中因非线性特性导致的牛顿-拉夫逊迭代计算瓶颈及GPU并行效率低下问题，采用人工神经网络(ANN)替代传统物理非线性迭代求解。具体而言，对时不变组件（如光伏阵列）采用多层感知机(MLP)建模，对时变动态组件（如双馈风机DFIG、储能电池）采用门控循环单元(GRU)建模。通过蒙特卡洛方法基于传统物理模型生成高质量训练数据。在软件架构层面，引入面向数据的实体-组件-系统(ECS)架构与GPU实例化技术，实现ANN模型的高效插件化集成与海量实体并行计算。模型采用Float32单精度浮点数运算，显著降低内存带宽压力并提升GPU张量计算效率，最终实现超大规模新能源系统的快速暂态仿真。

### 数学公式


**公式1**: $$$z = f(Wx + b)$$$

*MLP单层前向传播公式，其中$x$为输入状态向量，$W$为权重矩阵，$b$为偏置向量，$f$为非线性激活函数，$z$为层输出向量，用于光伏阵列等静态非线性映射。*


**公式2**: $$$z_t = \sigma(W_{xz} x_t + U_{hz} h_{t-1})$$$

*GRU更新门公式，控制上一时刻隐藏状态$h_{t-1}$被新候选状态更新的比例。*


**公式3**: $$$r_t = \sigma(W_{xr} x_t + U_{hr} h_{t-1})$$$

*GRU重置门公式，决定计算候选隐藏状态时保留多少上一时刻的隐藏状态信息。*


**公式4**: $$$\tilde{h}_t = \tanh(W x_t + U (r_t \odot h_{t-1}))$$$

*GRU候选隐藏状态公式，结合当前输入与经重置门过滤的历史状态生成新状态候选。*


**公式5**: $$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$$

*GRU最终隐藏状态输出公式，通过更新门加权融合历史状态与候选状态，用于DFIG与储能电池的时序动态建模。*


### 算法步骤

1. 数据生成阶段：基于传统物理EMT模型，采用蒙特卡洛方法对光伏阵列局部遮荫、风机动态响应及电池充放电等多变量非线性工况进行随机采样，生成覆盖全工况的高保真输入-输出时序数据集。

2. 模型训练阶段：针对时不变特性组件构建MLP网络，针对含记忆特性的时变组件构建GRU网络。利用生成的数据集进行监督学习训练，优化权重矩阵与偏置，使ANN拟合误差满足工程精度要求。

3. 架构集成阶段：采用面向数据的实体-组件-系统(ECS)架构重构仿真内核。将训练好的ANN模型封装为独立组件，通过插件化接口无缝替换传统非线性求解器。利用GPU实例化技术将海量相同结构的ANN模型映射至GPU显存，实现数据布局优化。

4. 并行求解阶段：在CPU-GPU异构平台上执行仿真。CPU负责电网拓扑解析、线性网络方程求解及任务调度；GPU利用CUBLAS/CUDNN库并行执行所有ANN组件的前向推理计算（采用Float32精度），避免频繁的Host-Device内存交换与复杂分支预测开销。

5. 迭代与输出阶段：在每个仿真步长内，GPU完成所有RES实体的状态更新后，将结果返回CPU进行全局网络方程联立求解，循环推进直至仿真结束，并输出暂态波形数据。


### 关键参数

- **计算精度**: Float32 (ANN推理) / Float64 (传统NR迭代对比)

- **网络架构**: MLP (光伏阵列), GRU (DFIG风机/储能电池)

- **并行策略**: GPU实例化 + ECS数据导向架构

- **测试规模**: 200万新能源实体

- **基础测试系统**: 基于IEEE 118节点系统的交直流混合微电网



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 基于IEEE 118节点系统的交直流混合微电网大规模新能源接入仿真 | 在包含200万个新能源实体（光伏阵列、DFIG风机、储能电池）的测试场景中，成功完成电磁暂态全过程仿真，系统稳定运行且波形输出完整，验证了数据驱动模型在超大规模系统中的数值稳定性。 | 相比传统CPU非线性迭代计算方法，整体仿真速度提升400倍。 |



## 量化发现

- 在200万新能源实体规模下，实现400倍于传统CPU非线性迭代计算的加速比。
- ANN模型采用Float32单精度浮点运算，相比传统牛顿-拉夫逊法所需的Float64双精度，显著降低GPU计算延迟与显存带宽占用。
- 蒙特卡洛数据生成方法有效覆盖光伏阵列局部遮荫等多变量非线性工况，确保ANN模型在复杂气象条件下的拟合精度。
- 基于ECS架构与GPU实例化技术，消除了传统GPU求解中因频繁Host-Device内存交换和复杂分支预测导致的并行效率瓶颈。


## 关键公式

### 多层感知机(MLP)前向传播公式

$$$z = f(Wx + b)$$$

*用于光伏阵列等时不变非线性组件的静态输入-输出映射建模*

### GRU单元状态更新公式

$$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$$

*用于DFIG风机与储能电池等含时间序列依赖特性的动态组件暂态行为建模*



## 验证详情

- **验证方式**: 对比验证（传统物理EMT模型数据训练 + MATLAB/Simulink基准对比）
- **测试系统**: 基于IEEE 118节点系统构建的合成交直流混合微电网系统
- **仿真工具**: MATLAB/Simulink, 自定义CPU-GPU异构EMT仿真平台
- **验证结果**: 通过MATLAB/Simulink对ANN模型输出进行交叉验证，确认数据驱动模型能够精准复现传统物理模型的非线性暂态特性。在200万实体规模下，验证了ECS架构与GPU实例化策略的工程可行性，实现400倍加速且保持数值稳定性，满足大规模新能源并网系统详细EMT仿真的实时性与精度要求。

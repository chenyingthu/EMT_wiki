---
title: "基于FPGA的变电站实时仿真培训系统"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/张炳达和王岚禹 - 2017 - 基于FPGA的变电站实时仿真培训系统.pdf"]
---

# 基于FPGA的变电站实时仿真培训系统

**作者**: 
**年份**: 2025
**来源**: `33/张炳达和王岚禹 - 2017 - 基于FPGA的变电站实时仿真培训系统.pdf`

## 摘要

Real-time simulation training system for substation based on field-programmable gate array (FPGA) is proposed in order to reduce the construction cost of substation simulation training system and enhance the quality of real-time digital simulation. A minimum degree maximum independent set method is adopted to arrange the sequence of nodes elimination and voltage computation, which has a good balance of computation burden and degree of parallelism. Fine granularity parallel computing is realized by adopting a multi-input and multi-output instruction stream arithmetic unit, therefore improving FPGA resource utilization. The simulation parameters are indirectly modified by the status word and effect word, thus reducing the simulation time and saving data memory space. Simulation example shows

## 核心贡献



- 提出基于FPGA的变电站实时仿真培训系统，采用最小度最大独立集法优化节点消去与电压计算顺序，有效平衡计算负载与并行度。
- 设计多输入多输出指令流运算器实现细粒度并行计算，并提出基于状态字和影响字的参数间接修改方法，显著提升FPGA资源利用率并降低存储与计算开销。

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]

## 相关主题


- [[real-time]]
- [[parallel]]

## 主要发现



- 所提架构可在单块EP4CGX150 FPGA芯片上以40 μs步长稳定运行542节点变电站模型。
- 细粒度并行计算与参数间接修改策略大幅提高了硬件资源利用率，同时有效减少了仿真计算时间与数据存储空间占用。

## 方法细节

### 方法概述

提出基于FPGA的变电站实时仿真培训系统架构，采用最小度最大独立集法（Minimum Degree Maximum Independent Set Method）优化节点消去与电压计算的顺序，以平衡运算量与并行度。设计多输入多输出（MIMO）指令流运算器（Instruction Stream Arithmetic Unit）实现细粒度并行计算，通过深度流水线设计和FIFO缓冲机制提高FPGA资源利用率。引入状态字（Status Word）和影响字（Effect Word）机制实现仿真参数的间接修改，避免实时计算导纳参数的时间开销，支持开关状态、故障设置和变压器磁饱和状态的快速切换。

### 数学公式


**公式1**: $$$$I'_j = - I_i G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right)$$$$

*节点i消去后，在相邻节点j处添加的等效理想电流源计算公式，其中$I_i$为节点i的注入电流，$G_{ij}$为节点i与j之间的互电导，$G_i$为节点i的对地电导*


**公式2**: $$$$G'_j = G_i G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right)$$$$

*节点i消去后，在相邻节点j处添加的等对地电导计算公式*


**公式3**: $$$$G'_{jk} = G_{ik} G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right), \quad k = 1, 2, \dots, n; \ k \neq j$$$$

*节点i消去后，在相邻节点j与k之间添加的等效互电导计算公式*


**公式4**: $$$$u_i = \left( I_i + \sum_{p=1}^{n} G_{ip} u_p \right) / \left( G_i + \sum_{p=1}^{n} G_{ip} \right)$$$$

*已知相邻节点电压$u_1, u_2, \dots, u_n$时，计算节点i电压的公式，体现节点电压计算的量与节点度n的关系*


**公式5**: $$$$P = (Y_1 + Y_2)C_{max}D_{max} + Y_3D_{max} + Y_4$$$$

*母线节点自导纳查询时的偏移量计算公式，其中$Y_1$-$Y_4$分别为状态字A-D段位为1的个数，$C_{max}$为可设置金属性故障总数+1，$D_{max}$为可设置非金属性故障总数+1*


**公式6**: $$$$P = (2Y_3 + Y_2(Y_2 + 1) + Y_1(Y_1 + 1)(2Y_1 + 4)/6) + D$$$$

*变压器中性点自导纳查询时的偏移量计算公式，$Y_1$-$Y_3$分别为A-C段中最大值、中间值、最小值，$D$为D段值（中性点刀闸状态）*


### 算法步骤

1. 采用梯形法对变电站模型中的RLC元件、线路等进行差分化处理，形成等效电导与历史电流源并联的伴随电路；对变压器励磁电感采用分段线性化处理磁饱和特性

2. 构建网络节点方程，将各元件用伴随电路替代，形成新的电路网络，其中每个节点表示为理想电流源$I_i$、对地电导$G_i$和互电导$G_{ij}$的形式

3. 应用最小度最大独立集法安排节点消去顺序：选取度（相邻节点数）最小的节点作为起始消去节点，将其相邻节点标记为已访问；在未访问节点中继续选取度最小的节点作为下一个消去节点，直到所有节点被访问；这些消去节点形成一个最大节点独立集，可并行消去；重复此过程直到所有节点被安排

4. 按照节点消去顺序执行前向消去运算，使用公式组(1)计算消去后的等效电流源和等效电导，整理化简网络

5. 计算最简网络的节点电压后，按照节点消去相反的次序（逆序回代）使用公式(2)求出其余节点的电压

6. 在FPGA指令流运算器中执行计算：通过16位自定义指令流控制MUX选择器，实现单输出运算（如$b/c$、$d \times e$）和多输出运算（如$(b/c, b/c \times e, b/c \times e + g)$）；利用深度流水线（乘法器5级、除法器10级、加法器7级）和FIFO缓冲机制（长度1-24级）处理数据依赖性

7. 仿真参数间接修改：当开关状态、故障设置或变压器磁饱和状态变化时，通过影响字（Effect Word）修改对应的状态字（Status Word）；根据状态字通过查询表（Inquiry-Data机制）直接读取预存的仿真参数实际值，避免实时计算


### 关键参数

- **simulation_step**: 40 μs

- **clock_frequency**: 200 MHz

- **fpga_chip**: Altera EP4CGX150

- **logic_elements**: 约150K个

- **multipliers**: 360个18×18内嵌乘法器

- **ram_capacity**: 6480 Kbit片内RAM

- **node_count**: 542个节点

- **fifo_lengths**: 读数据口FIFO长度1-11级，写数据口FIFO长度2-24级

- **instruction_width**: 不超过16个8位二进制数

- **transceivers**: 8个3.125-Gbps收发器



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 主变压器T1空载合闸励磁涌流仿真 | 模拟SFPSZ7-120000/220主变压器空载合闸过程，合闸时刻选在B相和C相电压瞬时值近似相等时刻。观察到由于铁芯磁通不能突变，各相磁通为稳态交流分量和衰减直流分量叠加，当磁通超过饱和阈值时产生大幅值励磁电流。基于FPGA的实时仿真结果与Matlab/Simulink离线仿真对比，波形吻合。 | 与Matlab/Simulink离线仿真结果相比，误差在5%以内 |

| 铁磁谐振现象仿真（PT饱和） | 模拟311馈线2km处A相接地消失时35kV I段母线的铁磁谐振现象。通过增加线路对地电容，观察到三相电压波形畸变且具有规律性。查看PT励磁电感状态确认其大部分时间处于饱和状态，验证了铁磁谐振现象的理论分析。 | 与Matlab/Simulink离线仿真结果相比，误差在5%以内，满足仿真精度要求 |

| 542节点变电站实时仿真性能 | 在单块EP4CGX150芯片上实现542节点变电站实时仿真，包含2台主变压器、220kV双母线4回馈线、110kV和35kV单母分段各6回馈线，可在母线、变压器出口、断路器与隔离开关间等位置设置相间和对地短路故障。 | 指令流执行时间34.5μs，满足40μs实时仿真步长要求；资源占用率：逻辑资源41%、乘法器56%、存储资源52% |



## 量化发现

- 542节点规模的变电站模型可在单块EP4CGX150 FPGA芯片上实现实时仿真
- 实时仿真步长达到40μs，时钟频率200MHz，满足电磁暂态实时仿真要求
- 与Matlab/Simulink离线仿真结果相比，电压电流波形误差小于5%
- 指令流运算器执行时间估计为34.5μs，小于仿真步长40μs，满足实时性要求
- FPGA资源占用：逻辑单元41%、18×18乘法器56%、片内RAM 52%
- 采用状态字和影响字机制后，仿真参数修改时间显著减少，存储空间节约（仅需存储一套可能的仿真参数实际值）
- 指令流采用不超过16个8位二进制数表示，降低存储需求
- FIFO缓冲长度根据运算器流水线深度配置，范围1-24级，确保数据正确性


## 关键公式

### 节点消去等效变换公式

$$$$\begin{cases} I'_j = - I_i G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \\ G'_j = G_i G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \\ G'_{jk} = G_{ik} G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \end{cases}$$$$

*在使用最小度最大独立集法确定消去顺序后，对选定节点进行高斯消去时，计算相邻节点处需要添加的等效电流源和等效电导*

### 节点电压计算公式

$$$$u_i = \left( I_i + \sum_{p=1}^{n} G_{ip} u_p \right) / \left( G_i + \sum_{p=1}^{n} G_{ip} \right)$$$$

*在逆序回代阶段，当已知相邻节点电压时，计算当前节点电压；也用于分析节点度n与计算量的关系，支撑最小度最大独立集法的优化策略*



## 验证详情

- **验证方式**: 对比验证（与Matlab/Simulink离线仿真结果对比）
- **测试系统**: 542节点变电站系统，包含2台SFPSZ7-120000/220型主变压器（220kV/110kV/35kV），220kV侧双母线带4回馈线，110kV和35kV侧均为单母分段各带6回馈线；支持在母线、变压器出口、断路器与隔离开关间、馈线段间等位置设置金属性和非金属性短路故障
- **仿真工具**: Matlab/Simulink（离线仿真对比基准），Altera Quartus II（FPGA开发），TimeQuest（时序验证）
- **验证结果**: 基于FPGA的实时仿真与Matlab/Simulink离线仿真在变压器空载合闸励磁涌流、PT铁磁谐振等典型暂态工况下的波形对比显示，两者误差在5%以内，验证了所提方法在542节点规模下40μs步长实时仿真的准确性和可行性

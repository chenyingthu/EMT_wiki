---
title: "The Reconﬁgurable-Hardware Real-Time and"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/37/tpwrd.2012.2229723.pdf.pdf"]
---

# The Reconﬁgurable-Hardware Real-Time and

**作者**: 
**年份**: 2012
**来源**: `37/tpwrd.2012.2229723.pdf.pdf`

## 摘要

—The reconﬁgurable-hardware real-time power system simulator (RH-RTS) is a ﬁeld-programmable gate-array (FPGA)-based real-time simulator that is developed based on the concept of simulators hardware reconﬁgurability (i.e., to change the underlying hardware architecture of the simulator to accommodate various power system topologies). The uniqueness of the RH-RTS is the underlying hardware architecture. The RH-RTS has a massively parallel customized hardware architec- ture that is tailored to the solution of the mathematical model of the power system under consideration. The RH-RTS enables the simulation of large power systems with a computation-time per simulation time-step in the range of tens of nanoseconds. Not only does the RH-RTS provide a means for real-time operation (e.g.,

## 核心贡献



- 提出基于FPGA的可重构硬件实时仿真器(RH-RTS)，实现底层硬件架构动态重构以适应不同电网拓扑
- 实现大规模电力系统电磁暂态仿真，单步计算时间低至24纳秒，支持实时与超实时双模式运行

## 使用的方法


- [[parallel]]
- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[network-equivalent]]

## 相关主题


- [[real-time]]
- [[co-simulation]]
- [[harmonic]]

## 主要发现



- RH-RTS单步计算时间可低至24纳秒，为目前技术文献报道的最低水平
- 该仿真器有效突破了传统实时仿真器在最小时间步长、频率带宽和模型精度上的限制，可高效支持硬件在环测试与统计开关研究

## 方法细节

### 方法概述

RH-RTS采用基于FPGA的可重构硬件架构，通过将电力系统模型分解为适合并行实现的独立方程组，利用数值积分将微分方程转换为代数方程，并采用节点分析法求解。核心思想是通过硬件重构（reconfigurability）动态改变底层硬件架构以适应不同电力系统拓扑，实现计算引擎与求解算法的深度匹配。该方法利用细粒度并行性（fine-grained parallelism）在原始操作级别实现并行计算，避免传统多处理器架构中的通信延迟和内存访问开销。

### 数学公式


**公式1**: $$$\frac{dx}{dt} = f(x,t)$$$

*电力系统元件的一阶常微分方程(ODE)基本形式，描述电压电流动态关系*


**公式2**: $$$x(t) = k \cdot f(x,t) + h(t)$$$

*数值积分后的代数方程，将ODE转换为离散时间代数关系，其中k为常数，h(t)为历史项*


**公式3**: $$$h(t) = \alpha x(t-\Delta t) + \beta h(t-\Delta t)$$$

*历史项递推计算公式，α和β为由元件参数和时间步长确定的常数，用于伴随电路中的等效电流源更新*


**公式4**: $$$G \cdot v(t) = i(t) + h(t)$$$

*节点电压方程（Nodal Equation），G为节点导纳矩阵，v(t)为节点电压向量，i(t)为电流源向量，h(t)为历史电流源向量*


**公式5**: $$$A \cdot x = b$$$

*线性方程组标准形式，对应节点分析中的矩阵求解问题*


### 算法步骤

1. 系统分解与模型离散化：将电力系统分解为研究区和外部区，对研究区内各元件采用数值积分方法（如梯形法）将微分方程转换为伴随电路模型，生成等效电导和电流源

2. 构建节点导纳矩阵：基于所有元件的伴随电路表示，组装恒定不变的节点导纳矩阵G，该矩阵在固定时间步长仿真中保持常量

3. 并行求解节点电压：在每个时间步，求解线性方程组 G·v(t) = i(t) + h(t) 计算当前时刻所有节点电压，利用FPGA的细粒度并行架构同时处理多个节点方程

4. 更新历史电流源：根据计算的节点电压值，使用公式 h(t) = α·x(t-Δt) + β·h(t-Δt) 更新各元件伴随电路中的历史项（等效电流源），该步骤必须在电压计算完成后顺序执行

5. 时间推进与迭代：将仿真时间推进一个步长Δt，重复步骤3-4直到仿真结束，支持实时（real-time）和超实时（faster-than-real-time）两种运行模式


### 关键参数

- **time_step**: 24 ns（最低计算时间）至数百纳秒范围

- **matrix_G**: 节点导纳矩阵（常量）

- **history_term_constants**: α和β，由元件参数和时间步长Δt确定

- **frequency_bandwidth**: 突破传统10 kHz限制，支持DC至数MHz范围



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 大规模电力系统实时仿真 | 在 realistic size systems（实际规模系统）上实现单步计算时间低至24纳秒，支持闭环硬件在环(HIL)测试配置 | 相比传统基于多处理器或计算机集群的实时仿真器（典型时间步长10-80 μs），计算速度提升约1000倍（从微秒级降至纳秒级） |

| 超实时统计开关研究 | 实现快于实时的仿真运行模式，可在短时间内完成大量开关场景(statistical switching studies)的仿真测试 | 相比传统实时仿真器，总运行时间显著缩短，支持大规模统计研究 |



## 量化发现

- 单步计算时间（computation-time per simulation time-step）低至24纳秒，为技术文献报道的最低水平
- 传统实时仿真器典型时间步长范围为10-80微秒（μs），而RH-RTS可达数十纳秒（ns）级别，时间步长缩小约1000倍
- 传统实时仿真器频率带宽限制在约10 kHz以下，RH-RTS可支持DC至数MHz的电磁暂态频率范围
- 现有基于多处理器架构的仿真器存在5-10微秒的通信延迟（communication latency），而RH-RTS通过定制硬件架构消除了此开销
- 采用多速率仿真时，传统方法对含电力电子变换器的小部分系统采用数百纳秒至数微秒步长，RH-RTS可在整个系统实现统一纳秒级步长


## 关键公式

### 节点电压方程（Nodal Analysis Equation）

$$$G \cdot v(t) = i(t) + h(t)$$$

*在每个仿真时间步求解系统节点电压的核心方程，其中G为恒定导纳矩阵，h(t)为基于历史值的等效电流源向量*

### 历史项递推公式（History Term Update）

$$$h(t) = \alpha x(t-\Delta t) + \beta h(t-\Delta t)$$$

*用于更新伴随电路中等效电流源的历史值，基于前一时间步的电压/电流值递归计算*

### 数值积分离散化方程

$$$x(t) = k \cdot f(x,t) + h(t)$$$

*将连续时间ODE通过数值积分（如梯形法）转换为离散代数形式，构成伴随电路的基础*



## 验证详情

- **验证方式**: 案例研究验证（Case Study）与性能评估，通过与现有技术文献对比验证计算速度，通过实时和超实时运行验证功能
- **测试系统**: realistic size systems（具有实际规模的电力系统），包含输电线路、电缆及多种电力系统元件，系统被划分为研究区和外部区（study zone and external zone）
- **仿真工具**: 基于Xilinx FPGA的可重构硬件平台（Field-Programmable Gate Array），采用定制并行硬件架构实现，未使用传统商业仿真软件如PSCAD/EMTDC或RTDS
- **验证结果**: 验证了24 ns的单步计算时间，确认RH-RTS能够突破传统实时仿真器在最小时间步长、频率带宽和模型精度方面的限制，成功支持硬件在环(HIL)测试和统计开关研究

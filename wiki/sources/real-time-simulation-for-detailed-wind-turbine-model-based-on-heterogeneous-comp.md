---
title: "Real-time simulation for detailed wind turbine model based on heterogeneous computing"
type: source
authors: ['Bing Li']
year: 2023
journal: "International Journal of Electrical Power and Energy Systems, 155 (2024) 109486. doi:10.1016/j.ijepes.2023.109486"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/32/Li 等 - 2024 - Real-time simulation for detailed wind turbine model based on heterogeneous computing.pdf"]
---

# Real-time simulation for detailed wind turbine model based on heterogeneous computing

**作者**: Bing Li
**年份**: 2023
**来源**: `32/Li 等 - 2024 - Real-time simulation for detailed wind turbine model based on heterogeneous computing.pdf`

## 摘要

Electrical Power and Energy Systems 155 (2024) 109486 0142-0615/© 2023 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- International Journal of Electrical Power and Energy Systems Real-time simulation for detailed wind turbine model based on School of Electrical Engineering, Shandong University, Jinan 250061, China

## 核心贡献


- 提出CPU-FPGA异构计算平台，实现详细风机模型低成本实时仿真
- 设计通用FPGA电磁暂态求解器，支持电路拓扑变更免重编译
- 揭示电网故障下风机扭转与非扭转振动特性，验证机电耦合动态


## 使用的方法


- [[异构计算|异构计算]]
- [[多速率仿真|多速率仿真]]
- [[节点分析法|节点分析法]]
- [[实时操作系统|实时操作系统]]
- [[有限状态机控制|有限状态机控制]]


## 涉及的模型


- [[详细风机模型-dwtm|详细风机模型(DWTM)]]
- [[dfig-model|DFIG]]
- [[vsc-model|VSC]]
- [[变压器|变压器]]
- [[气动与机械动力学模型|气动与机械动力学模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[多时间尺度耦合|多时间尺度耦合]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电耦合动态|机电耦合动态]]


## 主要发现


- 平台实现微秒级电气与毫秒级机械动态的高精度实时耦合仿真
- 故障工况下风机呈现显著扭转与非扭转振动，验证机电耦合机理
- 通用FPGA求解器免重编译特性有效缩短开发周期并保障实时性



## 方法细节

### 方法概述

提出CPU-FPGA异构计算架构的详细风力发电机模型(DWTM)实时仿真平台。CPU侧基于Linux-RT实时操作系统补丁，运行毫秒级 turbine 模型(OpenFAST，12.5ms步长)和控制系统(Matlab/Simulink代码生成，主控12.5ms/VSC 200μs)；FPGA侧实现微秒级电磁暂态仿真(10μs步长)，包含通用电磁暂态求解器(支持拓扑免重编译)、PWM发生器和接口逻辑。双平台通过8Gbps PCIe 3.0高速互联，采用多速率仿真机制(1250:1步长比)和一阶保持(First-Order Hold)采样方法实现机电耦合数据同步交换，支持HSS转速ωᵣ和电磁转矩Tᵉ等边界条件实时交互。

### 数学公式


**公式1**: $$$G_{\text{eq}} V(t) = I(t) - I_{\text{hist}}$$$

*节点电压方程，基于节点分析法(NA)的电磁暂态求解基本方程，其中G_eq为等效导纳矩阵，I_hist为历史电流源项*


**公式2**: $$$I_{\text{hist}}(t) = \sigma I_{\text{hist}}(t-\Delta t) + \eta V(t-\Delta t)$$$

*历史电流源更新公式，σ和η为加权积分系数，实现伴随电路模型的状态递推*


**公式3**: $$$G_{\text{eq}}^{L} = \frac{\theta \Delta t}{L}, \quad \sigma^{L} = 1, \quad \eta^{L} = \frac{\Delta t}{L}$$$

*电感元件在加权数值积分下的离散化参数，θ为积分权重系数(0.5为梯形法，1.0为后向欧拉)*


**公式4**: $$$G_{\text{eq}}^{C} = \frac{C}{\theta \Delta t}, \quad \sigma^{C} = \frac{\theta-1}{\theta}, \quad \eta^{C} = \frac{(2\theta-1)C}{\theta^2 \Delta t}$$$

*电容元件的离散化伴随电路参数，支持通过调整θ改变积分方法而无需修改FPGA硬件代码*


**公式5**: $$$G_{\text{eq}}^{RL} = \frac{\theta \Delta t}{L+\theta \Delta t R}, \quad \sigma^{RL} = \frac{L+(1-\theta)\Delta t R}{L+\theta \Delta t R}, \quad \eta^{RL} = \frac{\Delta t L}{(L+\Delta t \theta R)^2}$$$

*RL串联支路的等效导纳和历史项更新系数，用于网络 solver 中的统一支路处理*


### 算法步骤

1. 初始化阶段：CPU侧加载OpenFAST涡轮模型（含入流风、气动、传动链、塔架动态）和Simulink生成的控制代码；FPGA侧加载通用EMT求解器比特流，通过配置寄存器设置电路拓扑参数(G_eq, σ, η)而无需重编译

2. FSM状态机控制：FPGA内部有限状态机(FSM)按10μs周期调度计算流程，依次执行源求解器(Source Solver)和网络求解器(Network Solver)状态

3. 源求解器计算：在每个电气时间步，计算异步发电机和理想电压源的诺顿等效电流源，更新历史项I_hist = σ·I_hist_old + η·V_old

4. 网络求解器计算：构建节点导纳矩阵G，求解线性方程组G·V = I得到全网节点电压，矩阵乘法器和向量加法器在FPGA流水线中并行执行

5. 多速率数据交换：每12.5ms(1250个电气步长)通过PCIe 3.0接口交换一次耦合变量：CPU向FPGA发送高速轴转速ωᵣ，FPGA向CPU返回电磁转矩Tᵉ，采用一阶保持插值处理步长差异

6. 控制信号交互：每200μs(20个电气步长)VSC控制器采集电气量，计算GSC和RSC的PWM占空比并发送至FPGA，FPGA PWM发生器产生开关信号驱动变流器模型

7. 实时同步机制：通信模块确保CPU和FPGA时间戳一致，通过中断和缓冲机制保证硬实时约束，CPU端Linux-RT补丁提供<100μs的时钟抖动性能


### 关键参数

- **电气仿真步长**: 10 μs

- **涡轮/主控步长**: 12.5 ms

- **VSC控制步长**: 200 μs

- **PCIe通信带宽**: 8 Gbps

- **加权积分参数θ**: 0.5-1.0可调(0.5为隐式梯形法，1.0为后向欧拉法)

- **涡轮模型频率范围**: 0-4 Hz

- **电气模型最高频率**: 10 kHz(对应电力电子开关动态)

- **机电步长比**: 1250:1



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 正常电网稳态运行 | 平台成功实现DFIG风力发电机在额定工况下的连续实时仿真，电气量(电压、电流)与机械量(转速、桨距角)保持同步更新，PCIe通信延迟稳定在微秒级 | 与RTDS+Bladed联合仿真方案相比，硬件架构复杂度降低50%以上，成本显著降低(无需商业软件授权费) |

| 电网对称故障下的机电耦合动态 | 在电网三相短路故障期间，观测到明显的轴系扭转振动(torsional vibration)和塔架非扭转振动(non-torsional vibration)，电磁转矩Tᵉ出现2-3p.u.的瞬时脉动，传动链转速波动范围±15%额定转速 | 验证了通用FPGA求解器在故障期间拓扑不变性假设下的计算稳定性，无需像传统FPGA方案那样因故障重构而重编译代码 |

| 风速突变与湍流风况 | 平台准确捕捉风剪切和塔影效应引起的3p频率(3倍转频)转矩脉动，气动-机械-电气多时间尺度动态耦合特征清晰，功率输出波动与理论值偏差小于典型工程精度要求 | 实现了OpenFAST(气动/机械)与FPGA EMT(电气)的紧密耦合，避免了多平台联合仿真的接口延迟和同步误差 |



## 量化发现

- 实时仿真实现了10μs级电磁暂态与12.5ms级机械动态的严格同步，时间步长跨度达1250倍
- FPGA通用求解器通过参数化配置(G_eq, σ, η)支持电路拓扑变更，将传统FPGA方案数小时的重编译时间缩短至毫秒级参数重载时间
- CPU侧Linux-RT实时补丁保证了控制任务的确定性执行，时钟抖动控制在100μs以下，满足主控制器12.5ms周期的硬实时约束
- 8Gbps PCIe 3.0接口实现了CPU-FPGA间微秒级延迟的数据交换，支持每步长双向传输HSS转速、电磁转矩及多路控制信号
- 电磁暂态模型覆盖高达10kHz的电力电子开关频率，采用θ=0.5的梯形法时，单个电气步长(10μs)内可等效模拟100个开关状态变化
- 故障工况下观测到轴系扭转振动频率通常在1-3Hz范围，与传动链固有模态一致，验证了机电耦合建模的必要性


## 关键公式

### 加权数值积分离散化公式

$$$G_{\text{eq}}^{i} = \frac{\theta \Delta t}{L_{i}}$, $\sigma^{i} = 1$, $\eta^{i} = \frac{\Delta t}{L_{i}}$ (for inductor)$$

*通用FPGA求解器核心，通过改变θ值(0.5-1.0)在梯形法与后向欧拉法间切换，适应不同刚度电路而无需重编译硬件代码*

### 节点电导矩阵方程

$$$\begin{bmatrix} G_{11} & G_{12} & \cdots \\ G_{21} & G_{22} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix} \begin{bmatrix} V_{1} \\ V_{2} \\ \vdots \end{bmatrix} = \begin{bmatrix} I_{1} - I_{\text{hist},1} \\ I_{2} - I_{\text{hist},2} \\ \vdots \end{bmatrix}$$$

*FPGA网络求解器在每个10μs步长内求解的线性方程组，通过流水线并行计算实现实时求解*



## 验证详情

- **验证方式**: 与商业离线仿真平台(PSCAD/EMTDC或MATLAB/Simulink)的对比验证，以及不同工况(稳态、故障、风扰动)下的物理合理性检验
- **测试系统**: 详细风力发电机模型(DWTM-Type 3 DFIG)，包含：①气动模块(OpenFAST)：三叶片、轮毂、机舱、塔架、平台；②电气模块：DFIG发电机(5-6阶模型)、背靠背VSC变流器(GSC+RSC)、滤波器、变压器、集电线路；③控制系统：主控(功率/桨距/偏航)+VSC控(矢量控制/电压定向)
- **仿真工具**: OpenFAST v3.x(气动/机械动态)，Matlab/Simulink Embedded Coder(控制代码生成)，Xilinx FPGA(电气EMT求解)，Linux kernel with RT-PREEMPT patch(实时操作系统)
- **验证结果**: 验证了CPU-FPGA异构平台在严格实时约束(10μs电气步长)下的计算正确性和数值稳定性，成功复现了电网故障引发的机电耦合振荡现象(扭转/非扭转振动)，证明了通用FPGA求解器在避免代码重编译情况下的多拓扑适应能力和实时性能

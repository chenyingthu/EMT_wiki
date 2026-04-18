---
title: "Mitigation of Subsynchronous Interactions in Hybrid AC/DC Grid With Renewable Energy Using Faster-Than-Real-Time Dynamic Simulation"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Systems;2021;36;1;10.1109/TPWRS.2020.2984732"
tags: ['real-time', 'renewable']
created: "2026-04-13"
sources: ["EMT_Doc/26/Cao 等 - 2021 - Mitigation of Subsynchronous Interactions in Hybrid ACDC Grid With Renewable Energy Using Faster-Th.pdf"]
---

# Mitigation of Subsynchronous Interactions in Hybrid AC/DC Grid With Renewable Energy Using Faster-Than-Real-Time Dynamic Simulation

**作者**: 
**年份**: 2021
**来源**: `26/Cao 等 - 2021 - Mitigation of Subsynchronous Interactions in Hybrid ACDC Grid With Renewable Energy Using Faster-Th.pdf`

## 摘要

—Transmission line capacity enhancement by series compensation is commonly used in power systems, which conse- quently faces potential subsynchronous interaction (SSI). In this work, faster-than-real-time (FTRT) simulation based on the ﬁeld- programmable gate arrays is proposed to mitigate the disastrous SSI in a hybrid AC/DC grid integrated with wind farms. Dynamic simulation is applied to the AC system to gain a high speedup over real-time, and a detailed multi-mass model is speciﬁcally introduced to the synchronous generator to show the electrical- mechanical interaction. Meanwhile, the DC grid undergoes elec- tromagnetic transient simulation to reﬂect the impact of power converters’ control on the overall grid, and consequently, the EMT- dynamic co-simulation running concurrently due t

## 核心贡献


- 提出基于FPGA的超实时仿真架构，实现交直流混合电网并行加速计算
- 构建同步发电机五质量块轴系模型，精确刻画次同步相互作用机电耦合
- 设计功率电压接口实现EMT与动态仿真并发，兼顾直流控制与交流暂态


## 使用的方法


- [[超实时仿真-ftrt|超实时仿真(FTRT)]]
- [[fpga硬件并行计算|FPGA硬件并行计算]]
- [[emt-动态混合仿真|EMT-动态混合仿真]]
- [[功率-电压接口技术|功率-电压接口技术]]
- [[微分代数方程-dae-求解|微分代数方程(DAE)求解]]


## 涉及的模型


- [[同步发电机九阶模型|同步发电机九阶模型]]
- [[五质量块扭振轴系模型|五质量块扭振轴系模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[风电场|风电场]]
- [[励磁控制系统-avr-pss|励磁控制系统(AVR/PSS)]]


## 相关主题


- [[次同步相互作用-ssi-抑制|次同步相互作用(SSI)抑制]]
- [[交直流混合电网|交直流混合电网]]
- [[超实时仿真|超实时仿真]]
- [[fpga并行加速|FPGA并行加速]]
- [[机电暂态协同仿真|机电暂态协同仿真]]
- [[暂态稳定分析|暂态稳定分析]]


## 主要发现


- 超实时平台可在故障后提前生成精确潮流调整策略，有效抑制次同步振荡
- 五质量块模型成功复现轴系扭振放大现象，验证了机电交互仿真准确性
- 混合仿真结果与Matlab离线工具高度一致，且具备显著超实时加速比



## 方法细节

### 方法概述

本文提出一种基于FPGA的超实时（FTRT）动态仿真架构，用于抑制含风电的混合交直流电网中的次同步相互作用（SSI）。方法核心在于将电网解耦为交流侧与直流侧：交流侧采用机电暂态/动态仿真，允许较大时间步长，并引入同步发电机九阶电气模型与五质量块扭振轴系模型，精确刻画机电耦合与轴系扭振；直流侧采用电磁暂态（EMT）仿真，以高分辨率捕捉换流器开关动态与控制响应。两侧通过功率-电压接口进行数据交互，利用FPGA硬件并行特性实现并发计算。在检测到严重故障后，FTRT平台在物理时间之前超前推演系统动态，量化潮流变化，并提前计算HVDC系统的最优有功注入/吸收策略，从而在失稳发生前实施主动控制。

### 数学公式


**公式1**: $$$\dot{x}(t) = f(x(t), u(t))$$$

*同步发电机及控制系统的状态微分方程，描述机电暂态动态演化*


**公式2**: $$$g(x(t), V(t)) = 0$$$

*网络代数方程，描述节点电压与注入功率的潮流约束*


**公式3**: $$$\dot{\delta}(t) = \omega_R \cdot \Delta\omega(t)$$$

*转子相对功角变化率方程，关联基准角速度与转速偏差*


**公式4**: $$$\dot{\Delta\omega}(t) = \frac{1}{2H}[T_m(t) - T_e(t) - D \cdot \Delta\omega(t)]$$$

*单质量块摇摆方程，刻画机械转矩、电磁转矩与阻尼对转速的影响*


**公式5**: $$$\dot{\psi}_{fd}(t) = \omega_R \cdot [e_{fd}(t) - R_{fd} i_{fd}(t)]$$$

*d轴励磁绕组磁链微分方程，反映励磁电压与绕组电阻的动态关系*


**公式6**: $$$\dot{v}_1(t) = \frac{1}{T_R} \cdot [v_t(t) - v_1(t)]$$$

*AVR电压测量滤波环节，用于提取机端电压动态分量*


**公式7**: $$$\dot{\Delta\omega}_1 = \frac{1}{2H_1}[K_{12}(\delta_2 - \delta_1) - T_e - D_1 \cdot \Delta\omega_1]$$$

*发电机转子（质量块1）扭振动力学方程，直接耦合电磁转矩与相邻轴段弹性扭矩*


### 算法步骤

1. 系统初始化与稳态潮流计算：通过离线潮流分析确定各节点电压幅值/相角、发电机初始功角、轴系相对位置及控制器初始状态，构建FTRT仿真的初始状态向量$x_0$。

2. FPGA硬件并行划分与逻辑映射：将交流网络DAE求解器、同步机九阶电气模型、五质量块轴系模型、AVR/PSS控制器分配至动态仿真逻辑块（采用较大步长）；将VSC-HVDC换流器开关模型、直流线路及控制环路分配至EMT仿真逻辑块（采用微秒级步长）。

3. 功率-电压接口同步与数据交换：在每个仿真步长内，通过功率-电压接口提取交流侧等效电压源与直流侧注入功率，实现两侧状态变量的双向耦合更新。接口隔离了不同时间尺度的求解器，确保并发计算的数值稳定性。

4. 故障触发与超前推演：实时监测电网状态，一旦检测到三相接地故障或大负荷突变，立即启动FTRT模式。利用FPGA硬件并行加速特性，以远快于物理时间的速度推演未来数秒至数十秒的系统动态轨迹，重现次同步振荡与轴系扭矩放大过程。

5. 抑制策略生成与下发：基于推演结果，量化次同步振荡幅值与轴系应力，通过优化算法计算HVDC换流站所需的最优有功功率调节量及持续时间，生成控制指令并提前下发至实际系统执行，实现主动阻尼。


### 关键参数

- **串联补偿度**: 55%

- **同步机电气模型阶数**: 9阶（含d轴2绕组、q轴2阻尼绕组）

- **轴系质量块数量**: 5个（4段汽轮机+1段发电机）

- **轴系状态变量维度**: 17维

- **传统动态仿真步长范围**: 1 ms ~ 10 ms

- **次同步谐振目标频率**: 约36 Hz

- **接口类型**: 功率-电压接口（Power-Voltage Interface）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE First Benchmark Model (FBM) 三相接地故障 | 在55%串联补偿度下施加变压器高压侧三相接地故障，激发次同步振荡。FFT频谱分析显示主导振荡频率为36 Hz，与特征值分析得到的固有频率35.9691 Hz高度吻合。 | FTRT仿真结果与Matlab/Simulink离线基准完全一致，频率偏差<0.1%，验证了多质量块模型在捕捉扭振模态上的高精度。 |

| 含风电混合交直流电网大扰动 | 模拟严重故障后，FTRT平台在物理时间到达前完成动态推演，成功计算出HVDC有功调节量以抑制轴系扭矩放大（TA）。 | 相比传统CPU顺序仿真，FPGA并行架构显著缩短求解时间，实现超实时（FTRT）运行，为实际系统预留了充足的控制决策窗口，且动态响应误差<0.5%。 |



## 量化发现

- 次同步振荡频率匹配误差极小：FFT分析值36 Hz与特征值计算值35.9691 Hz偏差仅0.0309 Hz（相对误差<0.09%）
- 同步机机电耦合模型维度：采用9阶电气方程结合5质量块轴系，共包含17个微分状态变量，完整覆盖10~35 Hz范围内的扭振模态
- 串联补偿度阈值：55%的线路补偿度足以激发显著的次同步谐振现象，验证了模型对SSI的敏感性
- 仿真加速机制：通过FPGA硬件并行处理与动态仿真大时间步长容忍特性，突破传统CPU顺序计算瓶颈，实现超实时推演
- 控制策略量化：FTRT可精确输出HVDC有功注入/吸收的幅值与持续时间，实现故障后毫秒级至秒级的主动抑制


## 关键公式

### 发电机转子扭振动力学方程

$$$\dot{\Delta\omega}_1 = \frac{1}{2H_1}[K_{12}(\delta_2 - \delta_1) - T_e - D_1 \cdot \Delta\omega_1]$$$

*用于五质量块轴系模型中发电机转子（Mass 1）的角速度变化计算，直接关联电磁转矩与相邻质量块弹性扭矩，是捕捉次同步扭振放大的核心方程*

### 电力系统动态仿真微分代数方程组(DAE)

$$$\dot{x}(t) = f(x(t), u(t)), \quad g(x(t), V(t)) = 0$$$

*描述交流系统动态仿真的通用数学框架，其中微分方程刻画同步机及控制器状态演化，代数方程描述网络潮流约束，是FTRT求解的基础*

### 多质量块轴系通用运动方程

$$$\dot{\delta}_n = \omega_R \cdot \Delta\omega_n, \quad \dot{\Delta\omega}_n = \frac{1}{2H_n}[T_n + K_{n,n+1}(\delta_{n+1} - \delta_n) - K_{n-1,n}(\delta_n - \delta_{n-1}) - D_n \Delta\omega_n]$$$

*适用于中间质量块（Mass 2-4）的扭振动态建模，通过刚度系数K与阻尼系数D耦合相邻质量块，完整再现汽轮机-发电机轴系的弹性形变与能量传递*



## 验证详情

- **验证方式**: 离线仿真对比验证与频域/时域联合分析
- **测试系统**: IEEE First Benchmark Model (FBM) 及含多端HVDC与风电场的混合交直流电网
- **仿真工具**: FPGA硬件平台（实现FTRT动态-EMT混合仿真）, Matlab/Simulink（作为离线高精度基准工具）
- **验证结果**: FTRT仿真在时域动态响应与频域特征提取上均与Matlab/Simulink离线结果高度一致。次同步谐振频率误差低于0.1%，多质量块轴系扭矩振荡波形准确复现。验证了功率-电压接口在并发仿真中的数值稳定性，以及FTRT架构在故障后超前推演与HVDC控制策略生成方面的工程可行性。

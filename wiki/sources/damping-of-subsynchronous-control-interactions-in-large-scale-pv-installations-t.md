---
title: "Damping of Subsynchronous Control Interactions in Large-Scale PV Installations Through Faster-Than-Real-Time Dynamic Emulation"
type: source
authors: ['未知']
year: 2021
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/12/Damping_of_Subsynchronous_Control_Interactions_in_Large-Scale_PV_Installations_Through_Faster-Than-Real-Time_Dynamic_Emulation.pdf"]
---

# Damping of Subsynchronous Control Interactions in Large-Scale PV Installations Through Faster-Than-Real-Time Dynamic Emulation

**作者**: 
**年份**: 2021
**来源**: `12/Damping_of_Subsynchronous_Control_Interactions_in_Large-Scale_PV_Installations_Through_Faster-Than-Real-Time_Dynamic_Emulation.pdf`

## 摘要

Large-scale photovoltaic (PV) power plant has witnessed a dramatic increase in the integration into transmission and distribution network, manifesting subsynchronous control interaction (SSCI) when the host grid is weak. In this work, the oscillation modes of a typical PV network are analyzed, and a faster-than- real-time (FTRT) emulation is proposed for predicting the SSCI and consequently mitigating its impacts on AC grid by taking the effective active/reactive power control action. The electromagnetic transient (EMT) simulation is utilized to model the PV panels and converter stations to reﬂect the actual dynamic process. Meanwhile, the AC grid undergoes transient stability (TS) simulation to obtain a high speed up over real-time, and consequently, a power-voltage interface is adopted f

## 核心贡献


- 提出基于FPGA的EMT-TS混合仿真架构，实现超实时动态推演
- 设计功率-电压接口实现电磁暂态与机电暂态模型的并行协同计算
- 利用光伏逆变器等效STATCOM，通过有功无功注入抑制次同步振荡


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[混合仿真|混合仿真]]
- [[fpga硬件仿真|FPGA硬件仿真]]
- [[并行计算|并行计算]]
- [[特征值分析|特征值分析]]
- [[功率-电压接口|功率-电压接口]]


## 涉及的模型


- [[光伏电站|光伏电站]]
- [[电压源换流器|电压源换流器]]
- [[交流电网|交流电网]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[pv-statcom|PV-STATCOM]]


## 相关主题


- [[次同步控制交互|次同步控制交互]]
- [[超实时仿真|超实时仿真]]
- [[硬件仿真|硬件仿真]]
- [[混合仿真|混合仿真]]
- [[弱电网稳定性|弱电网稳定性]]
- [[光伏并网|光伏并网]]
- [[并行计算|并行计算]]


## 主要发现


- 提出的FPGA硬件仿真平台实现了122倍超实时加速比，满足快速预测需求
- 通过有功无功功率控制策略有效阻尼了弱电网下光伏电站的次同步振荡
- 硬件仿真结果与Matlab及TSAT离线工具高度吻合，验证了模型准确性



## 方法细节

### 方法概述

本文提出一种基于FPGA的超实时（FTRT）电磁暂态-机电暂态（EMT-TS）混合仿真架构，用于预测并抑制弱电网下大型光伏电站的次同步控制交互（SSCI）。该方法将光伏阵列与电压源换流器（VSC）采用EMT详细建模以捕捉高频开关与控制动态，而交流主网采用TS模型以提升计算速度。通过功率-电压接口实现双域数据同步：EMT侧每200 µs计算一次，TS侧每5 ms计算一次，EMT在单个TS步长内并行迭代25次。利用FPGA的硬件并行性与可重构性，系统实现122倍超实时运行。当检测到SSCI时，控制平台利用FTRT推演能力快速扫描多种有功/无功注入方案，将光伏系统等效为PV-STATCOM，动态调整功率输出以提供次同步阻尼，从而在振荡恶化前实现主动抑制。

### 数学公式


**公式1**: $$$I_{PV} = N_p I_s [1 - C_1 (e^{\frac{U_{dc}}{C_2 N_s U_T}} - 1)]$$$

*光伏阵列伏安特性方程，描述光照与温度对输出电流的非线性影响*


**公式2**: $$$U_{dc} \cdot C \frac{dU_{dc}}{dt} = U_{dc} \cdot I_{PV} - U_{td} \cdot I_d$$$

*直流侧滤波电容动态方程，反映光伏输出与并网电流的功率平衡*


**公式3**: $$$\frac{d\theta_{pll}}{dt} = K_{p4}U_{tq} + K_{i4}x_{pll} + \omega_0$$$

*锁相环（PLL）相位动态方程，决定系统同步稳定性与次同步模态阻尼*


**公式4**: $$$L_g \frac{dI_d}{dt} = U_{td} - U_{gd} + \omega L_g I_q$$$

*d轴并网电流微分方程，用于构建系统状态空间模型*


**公式5**: $$$\Delta \dot{x} = A \Delta x + B \Delta u$$$

*系统线性化状态空间方程，用于特征值分析获取振荡频率与模态*


**公式6**: $$$SCR = \frac{U_N^2}{Z_g \cdot S_N}$$$

*短路比定义式，量化电网强度，SCR<3判定为弱电网*


**公式7**: $$$x_{n+1} = x_n + \frac{1}{6}(RK_1 + 2RK_2 + 2RK_3 + RK_4)$$$

*四阶Runge-Kutta数值积分公式，用于TS域同步发电机微分方程求解*


**公式8**: $$$G_{pv} = \frac{G_d + G_{sh}}{G_d R_s + R_s G_{sh} + 1}$$$

*光伏单元诺顿等效电导，实现非线性二极管线性化以适配FPGA并行计算*


### 算法步骤

1. 初始化FPGA硬件模块，加载IEEE 39节点交流系统（TS域）与4端HVDC及400MW光伏电站（EMT域）的离散化微分代数方程及初始运行点参数。

2. TS域采用4阶Runge-Kutta算法以5 ms步长求解同步发电机9阶微分方程与网络代数方程；EMT域以200 µs步长并行求解光伏二极管线性化模型、VSC控制环路及PLL动态。

3. 执行时间步长同步：EMT子系统在每个TS步长内独立迭代25次，累积计算瞬时P+jQ功率值，确保多速率仿真时序对齐。

4. 数据接口同步：EMT将更新后的P+jQ作为时变负荷注入TS网络导纳矩阵；TS求解网络潮流后，将PCC节点电压幅值与相角（$U \angle \theta$）反馈至EMT侧的PLL与电压外环控制器。

5. 实时监测与SSCI检测：通过FFT或特征值轨迹跟踪系统模态频率，当检测到次同步振荡（如频率约12 Hz且幅值发散）时触发预警信号。

6. FTRT预测推演：利用122倍超实时裕度，在FPGA上并行扫描多组有功/无功补偿指令，评估各方案对振荡模态的阻尼效果与系统暂态响应。

7. 最优控制执行：选取使系统恢复稳定的功率设定值，通过PV-STATCOM控制逻辑动态注入有功/无功，抑制次同步谐振。

8. 全局稳定性校验：持续监测同步机功角、频率与电压，若功率注入引发频率越限（>1%），则联动HVDC系统调整有功传输直至频率恢复至额定值。


### 关键参数

- **SCR弱电网阈值**: < 3

- **TS仿真步长**: 5 ms

- **EMT仿真步长**: 200 µs

- **FPGA时钟周期**: 10 ns

- **FTRT加速比**: 122倍

- **光伏电站额定容量**: 400 MW

- **初始运行点**: 有功287 MW，无功170 MVar

- **触发SSCI线路电感**: 从0.1 H突增至1.1 H

- **PLL比例增益临界值**: Kp_pll = 10时系统失稳

- **次同步振荡频率**: 约11.82 Hz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case 1: 弱电网下SSCI触发与抑制 | 在t=1.0 s时线路电感增至1.1 H，系统激发约11.82 Hz的次同步振荡，PCC电压与电流幅值呈指数发散趋势。t=1.09 s时执行FTRT优化控制，光伏有功增加48 MW，无功降至75 MVar。振荡在0.1 s内被有效阻尼，电压与电流波形恢复至稳态。 | FTRT硬件仿真波形与Matlab/Simulink离线EMT仿真结果在幅值、相位及动态响应上完全重合，误差可忽略不计，但计算速度提升122倍，为控制决策提供充足时间裕度。 |

| Case 2: 功率注入对交流主网频率的影响与恢复 | 光伏功率注入导致同步机频率上升并超过1%安全阈值。t=5.0 s时联动4端HVDC系统，将有功传输从400 MW降至300 MW。系统频率在t=9.5 s精确恢复至60 Hz，同步机功角与端电压同步恢复至扰动前水平。 | 验证了FTRT平台不仅能抑制局部SSCI，还能通过多端协调控制维持全局暂态稳定，结果与DSATools/TSAT离线机电暂态仿真曲线高度一致。 |



## 量化发现

- FTRT硬件仿真加速比达到122倍（EMT步长200 µs对应FPGA延迟163个时钟周期，TS步长5 ms对应1529个时钟周期）
- SSCI振荡模态频率经特征值分析为11.8207 Hz，与FFT时域分析结果（约12 Hz）高度一致，验证了线性化模型的准确性
- 电网短路比（SCR）降至1.8时，系统特征值λ5、λ6移至右半平面，确认弱电网是诱发SSCI的关键因素
- 控制动作响应时间仅0.09 s（t=1.0 s扰动，t=1.09 s注入补偿），有效阻止振荡扩散至主网
- 功率注入导致系统频率上升超过1%阈值，通过HVDC有功从400 MW降至300 MW，频率在t=9.5 s精确恢复至60 Hz


## 关键公式

### 短路比定义式

$$$SCR = \frac{U_N^2}{Z_g \cdot S_N}$$$

*用于量化交流电网强度，SCR<3判定为弱电网，是SSCI易发与特征值右移的关键边界条件*

### 线性化状态空间方程

$$$\Delta \dot{x} = A \Delta x + B \Delta u$$$

*在平衡点线性化DAE系统，用于特征值分析获取次同步振荡模态频率、阻尼比及参数灵敏度*

### 四阶Runge-Kutta积分公式

$$$x_{n+1} = x_n + \frac{1}{6}(RK_1 + 2RK_2 + 2RK_3 + RK_4)$$$

*用于TS域同步发电机微分方程的高精度数值求解，在FPGA上平衡计算速度与硬件资源消耗*

### 光伏单元诺顿等效电导

$$$G_{pv} = \frac{G_d + G_{sh}}{G_d R_s + R_s G_{sh} + 1}$$$

*将非线性光伏二极管线性化后构建两节点EMT模型，实现FPGA上的高效并行计算与接口数据交换*



## 验证详情

- **验证方式**: 离线仿真对比验证
- **测试系统**: IEEE 39节点交流系统 + 4端HVDC系统 + 400 MW光伏电站（经长距离输电线路接入Bus 39）
- **仿真工具**: Matlab/Simulink（EMT验证）、DSATools套件中的TSAT（TS验证）、Xilinx Vivado HLS（FPGA硬件综合与IP核生成）
- **验证结果**: FTRT硬件仿真输出的PCC电压、电流及功率波形与Matlab/Simulink和TSAT离线结果在幅值、相位及动态响应上完全一致，验证了混合接口同步策略的准确性；同时证实了基于FTRT预测的有功/无功功率注入策略可在0.09 s内有效抑制11.82 Hz次同步振荡，且通过HVDC协调控制可避免频率越限，整体系统恢复稳定。

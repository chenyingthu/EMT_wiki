---
title: "A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC HVDC system"
type: source
authors: ['Yupeng Li']
year: 2019
journal: "Electrical Power and Energy Systems, 115 (2019) 105479. doi:10.1016/j.ijepes.2019.105479"
tags: ['lcc', 'cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Li 等 - 2020 - A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC.pdf"]
---

# A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC HVDC system

**作者**: Yupeng Li
**年份**: 2019
**来源**: `02/Li 等 - 2020 - A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC.pdf`

## 摘要

A multi-area Thevenin equivalent based multi-rate co-simulation for control Yupeng Lia, Dewu Shua,⁎, Jingwei Hua, Zheng Yana, Yun Zhoua, Haifeng Wangb a High-Performance Simulation Center, Key Lab of Control and Power Transmission and Conversion, Department of Electrical Engineering, Shanghai Jiaotong University, b State Grid Shanghai Municipal Electric Power Company, China The line commutated converter (LCC) based HVDC transmission is often adopted to transmit the large capacity

## 核心贡献


- 提出基于多区域戴维南等值的输电线路接口模型，实现交直流宽频交互精确解耦
- 构建多速率协同仿真架构，结合MATE技术大幅提升大规模电网电磁暂态仿真效率
- 提出基于虚拟阻抗的改进控制策略，有效降低换相失败概率并加快直流系统恢复


## 使用的方法


- [[多速率协同仿真|多速率协同仿真]]
- [[多区域戴维南等值-mate|多区域戴维南等值(MATE)]]
- [[输电线路模型-tlm|输电线路模型(TLM)]]
- [[网络分割技术|网络分割技术]]
- [[虚拟阻抗控制|虚拟阻抗控制]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[交直流电网|交直流电网]]
- [[输电线路|输电线路]]
- [[戴维南等效模型|戴维南等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[换相失败抑制|换相失败抑制]]
- [[网络等值|网络等值]]
- [[多速率仿真|多速率仿真]]
- [[弱交流系统|弱交流系统]]
- [[控制策略设计|控制策略设计]]


## 主要发现


- 实际交直流电网仿真验证了所提多速率协同仿真方法在精度与效率上的显著优势
- 虚拟阻抗控制策略有效降低了弱交流系统下的换相失败概率，并提升了直流电压恢复速度
- MATE-TLM接口模型在保证宽频交互精度的同时，大幅降低了大规模网络求解计算负担



## 方法细节

### 方法概述

本文提出一种基于多区域戴维南等值（MATE）的多速率协同仿真方法，用于实际LCC-HVDC系统的控制设计与电磁暂态分析。首先，依据长线路阻抗大、弱耦合节点及最小连接母线原则，将大规模交直流电网解耦为直流子系统与多个交流子系统。交流子系统通过MATE技术进一步划分为独立子网络，各子系统间通过MATE-TLM（基于MATE的输电线路模型）接口进行宽频交互。仿真采用多速率架构：直流侧采用小步长Δt捕捉电力电子快速开关动态，交流侧采用大步长ΔT（ΔT=nΔt）降低计算负担。接口变量通过交流侧线性插值与直流侧平均值法进行跨步长同步。此外，提出基于虚拟阻抗的改进VDCOL控制策略，通过引入直流电压/电流变化量的虚拟压降修正电流指令，实现故障下直流电流的快速下调，从而抑制换相失败并加速系统恢复。

### 数学公式


**公式1**: $$$$\begin{bmatrix} Y_1 & & M_1 \\ & \ddots & \vdots \\ & & Y_N & M_N \\ M_1^T & \cdots & M_N^T & Z_b \end{bmatrix} \begin{bmatrix} v_1(t) \\ \vdots \\ v_N(t) \\ i_b(t) \end{bmatrix} = \begin{bmatrix} i_{h1}(t-\Delta T) \\ \vdots \\ i_{hN}(t-\Delta T) \\ 0 \end{bmatrix}$$$$

*MATE网络整体动态方程，描述N个子系统导纳矩阵、节点电压、历史电流及接口支路戴维南阻抗与电流的耦合关系。*


**公式2**: $$$$e_{thk}(t) = M_2^T [Y_2]^{-1} i_{h2}(t-\Delta T), \quad Z_{thk} = M_2^T [Y_2]^{-1} M_2$$$$

*MATE-TLM接口戴维南等效参数计算公式，用于将交流子系统等效为电压源与阻抗，供直流侧调用。*


**公式3**: $$$$\bar{u}_k(t) = L\{u_k[(k-1)\Delta T], u_k[(k-2)\Delta T]\}, \quad \bar{i}_k(t) = L\{i_k[(k-1)\Delta T], i_k[(k-2)\Delta T]\}$$$$

*交流侧接口变量线性插值公式，用于在直流侧小步长仿真时提供连续的边界条件。*


**公式4**: $$$$\bar{u}_n(t) = \frac{1}{n} \sum_{i=1}^n u_n[(k-1)\Delta T + i\Delta t], \quad \bar{i}_n(t) = \frac{1}{n} \sum_{i=1}^n i_n[(k-1)\Delta T + i\Delta t]$$$$

*直流侧接口变量平均值公式，用于在一个交流大步长周期结束后，将直流侧高频动态聚合反馈给交流侧。*


**公式5**: $$$$\Delta U_{dc} = R_i \cdot \Delta I_{dc} + K_u \cdot \Delta U_{dc}$$$$

*虚拟阻抗修正项计算公式，将直流电流过流与电压跌落转化为附加控制信号，用于加速VDCOL响应。*


### 算法步骤

1. 1. 初始化全网潮流，根据长线路、弱耦合点及最小连接母线原则，将整体网络划分为直流子系统与交流子系统，并利用MATE技术将交流网络进一步分割为N个独立子区域。

2. 2. 构建MATE-TLM接口模型，计算各交流子系统的戴维南等效电压源与阻抗，设定直流侧仿真步长Δt与交流侧步长ΔT（ΔT=nΔt）。

3. 3. 进入协同仿真循环。在交流侧每个大步长区间[(k-1)ΔT, kΔT]内，直流侧独立执行n次电磁暂态求解（步长Δt），交流侧各子区域独立执行1次求解（步长ΔT）。

4. 4. 接口数据同步：直流侧在每次小步长计算时，通过线性插值获取交流侧边界电压/电流；交流侧在大步长结束时，对直流侧n次计算结果进行算术平均，获取等效接口变量。

5. 5. 更新MATE-TLM接口参数与历史电流源，将等效电流注入各子系统，更新节点电压与支路状态。

6. 6. 判断是否达到总仿真时间Tmax。若未达到，k=k+1并返回步骤3；若达到，则终止仿真并输出全局动态响应曲线。


### 关键参数

- **直流额定参数**: 500 kV / 3 kA，直流电缆长度577 km

- **交流系统规模**: 2412个母线，599台发电机，1291个负荷，3537条线路

- **仿真步长设置**: 直流侧Δt = 50 μs；交流侧ΔT = 50 μs, 100 μs, 500 μs

- **速率比n**: 1, 2, 10

- **虚拟阻抗参数**: R_i (虚拟电阻), K_u (虚拟电压增益)，具体数值依系统整定，用于调节VDCOL输入信号U_dc_ord



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 逆变器侧三相接地短路故障（t=2.1s，持续0.11s） | 在ΔT=500μs（n=10）下，接口变量平均误差为0.0092~0.0116，直流子系统误差为0.0116。改进控制策略使电压跌落改善2.55%，过电流改善6.55%，有效减少VT3与VT6阀的连续换相失败次数，并加速故障清除后的直流电压恢复。 | 相比传统单速率全步长仿真（7200s），计算时间降至49.453s，加速比达150倍，且精度满足工程要求。 |

| 逆变器侧单相接地短路故障（t=2.1s，清除于2.21s） | 在ΔT=500μs下，接口变量平均误差为0.0084~0.0112，直流子系统误差为0.0109。改进控制策略使电压跌落改善14.03%，过电流改善3.45%，将传统策略下的VT3/VT6连续换相失败抑制为仅发生1次，显著缩短熄弧角恢复时间。 | 计算时间降至44.703s，加速比达160倍。相比传统VDCOL，动态响应速度显著提升，且未引发额外的无功功率消耗。 |

| 不同控制策略对比（传统VDCOL vs 换相失败预测 vs 本文虚拟阻抗策略） | 在ΔT=500μs多速率仿真下，本文策略与PSCAD/EMTDC高精度参考曲线高度吻合。换相失败预测策略虽能减少CF，但会导致交流侧无功消耗意外增加；本文策略在同等CF抑制效果下，避免了无功越限问题。 | 本文方法在保持与PSCAD参考曲线一致精度的同时，计算效率提升两个数量级，且控制策略的鲁棒性与经济性更优。 |



## 量化发现

- 在交流侧步长扩展至500 μs时，三相接地故障场景仿真速度提升150倍，单相接地故障场景提升160倍。
- 多速率协同仿真在n=10（ΔT=500 μs）时，接口变量平均误差E_avg控制在0.0084~0.0116之间，直流子系统误差<0.012，满足高精度要求。
- 基于虚拟阻抗的改进控制策略在单相故障下使电压跌落改善14.03%，过电流抑制3.45%；在三相故障下电压跌落改善2.55%，过电流抑制6.55%。
- 改进策略将传统控制引发的VT3与VT6连续换相失败次数从多次降低至仅1次，显著缩短熄弧角恢复时间。
- 相比换相失败预测控制，本文策略在同等抑制换相失败效果下，避免了交流侧无功功率的意外增加。


## 关键公式

### 虚拟阻抗修正的VDCOL输入指令方程

$$$$U_{dc\_ord} = U_{d\_INV} + R_i \cdot \Delta I_{dc} + K_u \cdot \Delta U_{dc}$$$$

*用于交流故障导致直流电压跌落或电流过冲时，快速修正电流指令限值，加速直流电流下调以抑制换相失败。*

### 改进型VDCOL输出电流指令分段函数

$$$$I_{ord} = \begin{cases} I_{max}, & U_{dc\_ord} \ge U_{max} \\ I_{min}, & U_{dc\_ord} \le U_{min} \\ I_{min} + \frac{I_{max}-I_{min}}{U_{max}-U_{min}}(U_{dc\_ord}-U_{min}), & U_{min} < U_{dc\_ord} < U_{max} \end{cases}$$$$

*根据修正后的电压指令U_dc_ord，在最大/最小限值之间线性调节直流电流参考值，实现故障穿越与快速恢复。*

### 平均仿真误差评估公式

$$$$E_{avg} = \frac{1}{N} \sum_{i=1}^{N} |x_{i,m} - x_{i,u}|$$$$

*用于定量评估多速率协同仿真结果与PSCAD高精度参考曲线之间的偏差，验证接口模型与多速率架构的数值精度。*



## 验证详情

- **验证方式**: 电磁暂态仿真对比验证（与PSCAD/EMTDC高精度单速率模型进行精度与效率对比，并对比不同控制策略的动态响应）
- **测试系统**: 中国南方电网实际交直流系统（观音岩LCC-HVDC工程），包含2412节点大规模交流电网与500kV/3kA双端直流输电系统
- **仿真工具**: 自主开发的多速率协同仿真程序（基于MATE-TLM架构），PSCAD/EMTDC（作为高精度参考基准）
- **验证结果**: 验证表明，所提MATE-TLM多速率协同仿真在交流步长放大至500μs时仍保持<1.2%的平均误差，计算效率提升150~160倍。基于虚拟阻抗的改进控制策略有效降低了弱交流系统下的换相失败概率，避免了无功越限，并显著加快了直流电压与电流的故障恢复速度，完全满足实际工程控制设计与大规模电网EMT仿真的精度与效率需求。

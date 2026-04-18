---
title: "Dynamic Performance of Embedded HVDC with"
type: source
authors: ['Mengjia', 'Xiao', '(Student)']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/PESGM.2015.7286425.pdf.pdf"]
---

# Dynamic Performance of Embedded HVDC with

**作者**: Mengjia, Xiao, (Student)
**年份**: 2015
**来源**: `13&14/files/PESGM.2015.7286425.pdf.pdf`

## 摘要

—An embedded HVDC system is a HVDC link connected in parallel with an AC transmission line or a mashed AC system. This paper proposes a control strategy cooperating with conventional d-q vector control for embedded HVDC system. The novel control method employs frequency features at two terminal stations to eliminate power oscillation. Dynamic simulation models are constructed in PSCAD platform to compare the transient stability of the proposed strategy with the conventional d-q vector control. According to the simulation results, the average Critical Clearing Time after contingencies is improved by 22.93% when equipped with the proposed frequency control method. Index Terms—Embedded HVDC; VSC-HVDC;

## 核心贡献


- 提出协同传统d-q矢量控制的嵌入式VSC-HVDC频率控制新策略
- 利用两端频率差线性化交流功率方程并补偿振荡，提升暂态稳定裕度


## 使用的方法


- [[d-q矢量控制|d-q矢量控制]]
- [[双环pi控制|双环PI控制]]
- [[派克变换|派克变换]]
- [[频率差补偿控制|频率差补偿控制]]
- [[临界切除时间计算|临界切除时间计算]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[同步发电机|同步发电机]]
- [[交流输电线路|交流输电线路]]
- [[ieee-4机6节点系统|IEEE 4机6节点系统]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[vsc-model|VSC]]
- [[暂态稳定性|暂态稳定性]]
- [[功率振荡抑制|功率振荡抑制]]
- [[频率控制|频率控制]]


## 主要发现


- 仿真表明所提策略使系统平均临界切除时间较传统控制提升22.93%
- 频率控制能有效衰减故障后受端有功功率振荡，验证了动态稳定性提升



## 方法细节

### 方法概述

本文提出一种协同传统d-q矢量控制的嵌入式VSC-HVDC频率控制新策略。该方法基于嵌入式HVDC两端处于同一同步交流网络、频率相同的物理特性，通过实时监测两端频率差与相角差，对交流联络线有功功率传输方程进行小信号线性化处理。控制架构采用双环PI结构：外环负责有功功率与交流电压控制，内环负责d-q轴电流跟踪。核心机制是将线性化后提取的交流功率振荡分量动态叠加至直流侧有功功率参考值，生成新的直流参考指令。通过该补偿机制，交流侧的功率振荡被主动转移至直流链路中，使受端交流电网注入功率保持恒定，从而有效抑制故障后的低频振荡，提升系统暂态稳定极限。

### 数学公式


**公式1**: $$$P_{\text{Bus 2}} = P_{\text{dc 2}} + P_{\text{ac 12}}$$$

*受端母线总有功功率等于直流侧传输功率与交流侧传输功率之和，为功率补偿提供基础拓扑关系。*


**公式2**: $$$P_{\text{ac 12}} = \frac{E_1 E_2}{x_{12}} \sin(\delta_1 - \delta_2)$$$

*交流联络线有功功率传输基本方程，描述两端电压幅值、相角差与线路电抗对传输功率的影响。*


**公式3**: $$$P_{\text{ac 12}} \approx K_1 \cdot \Delta \omega t + K_2$$$

*基于小频率差$\Delta \omega$和小相角差$\Delta \theta$假设下的交流功率线性化近似表达式，用于分离稳态分量与动态振荡分量。*


**公式4**: $$$P_{\text{dc 2}}^{\text{NEW }*} = P_{\text{dc 2}}^* + P_{\text{oscillation}}$$$

*频率补偿控制核心方程，将提取的交流振荡分量叠加至直流功率参考值，实现振荡能量向直流链路的转移。*


### 算法步骤

1. 采集VSC-HVDC两端交流母线电压与频率信号，通过派克变换（Park Transformation）将三相abc坐标系下的电压、电流转换至同步旋转d-q坐标系。

2. 执行传统外环控制：根据设定的直流电压（整流侧）或有功功率/交流电压（逆变侧）目标值，结合PI调节器生成d轴与q轴电流参考指令$i_{d}^*$和$i_{q}^*$。

3. 执行内环电流控制：将实际d-q电流与参考值比较，经PI调节器及前馈解耦项生成调制电压信号，通过PWM模块产生IGBT开关脉冲。

4. 实时计算两端频率差$\Delta \omega = \omega_1 - \omega_2$与初始相角差$\Delta \theta = \theta_{10} - \theta_{20}$。

5. 利用线性化模型$P_{\text{ac 12}} \approx K_1 \cdot \Delta \omega t + K_2$，分离出交流功率的稳态分量$K_2$与动态振荡分量$P_{\text{oscillation}} = K_1 \cdot \Delta \omega t$。

6. 将提取的振荡分量$P_{\text{oscillation}}$实时叠加至原直流功率参考值$P_{\text{dc 2}}^*$，计算得到补偿后的新直流参考值$P_{\text{dc 2}}^{\text{NEW }*}$。

7. 将$P_{\text{dc 2}}^{\text{NEW }*}$作为外环有功控制的新设定值输入VSC控制器，使直流链路主动吸收或释放振荡功率，维持受端交流侧注入功率恒定。

8. 持续监测直流链路容量限制，若补偿需求超出VSC额定容量，则触发限幅保护，剩余振荡分量由交流线路承担，待功率回落至容量范围内后恢复全量补偿。


### 关键参数

- **系统基准**: 230 kV, 60 Hz

- **初始潮流分配**: 总传输功率350 MW（交流200 MW，直流150 MW）

- **同步发电机参数**: Ra=0.0025, Xd=1.8, Xd'=0.30, Xq'=0.55, Td0'=8.0 s, H=6.175 s

- **故障切除时间评估阈值**: 区域间相角差>180°判定为失稳

- **直流链路容量限制**: 受VSC额定容量约束，超限时功率振荡呈方波截断特性



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 母线三相接地故障（Bus 1-6） | 在Scenario II下，各母线故障的临界切除时间（CCT）均显著提升，例如Bus 1从0.43s提升至0.53s，Bus 3从0.57s提升至0.71s，Bus 6从0.39s提升至0.50s。 | 较传统d-q控制（Scenario I）平均提升22.93%，母线故障场景下CCT增幅普遍高于线路故障。 |

| 线路三相接地故障（Line 1-2, 2-5, 4-6, 3-4） | 线路故障CCT同步改善，如Line 3-4从0.50s增至0.66s，Line 4-6从0.42s增至0.54s。Line 5-6故障因直流链路保持互联，系统不失稳，无CCT限制。 | 线路故障CCT平均提升约15%-20%，验证了频率控制对网络拓扑变化的鲁棒性。 |

| 受端区域有功功率振荡衰减（Bus 6故障0.2s） | Scenario I中受端交流功率持续低频振荡且衰减缓慢；Scenario II中直流功率参考值动态跟踪振荡分量，受端注入功率在故障清除后约6秒内恢复至稳态参考值，发电机相对功角差快速收敛。 | 振荡衰减时间缩短至6秒以内，功角摆动幅值显著降低，系统恢复同步速度大幅加快。 |



## 量化发现

- 系统平均临界切除时间（CCT）较传统控制策略提升22.93%。
- 受端交流侧功率振荡在故障清除后约6秒内完全衰减至稳态水平。
- 直流链路容量限制导致故障期间及清除后前3秒内补偿功率呈方波截断，超出容量部分的振荡仍反映在交流线路上。
- 发电机相对功角差（Angle14, Angle24, Angle34）在频率控制作用下摆动幅值减小，收敛速度显著优于传统控制。


## 关键公式

### 交流功率线性化方程

$$$P_{\text{ac 12}} \approx K_1 \cdot \Delta \omega t + K_2$$$

*用于在故障后小频率差与小相角差条件下，将非线性交流功率传输方程近似为线性时变函数，以分离振荡分量。*

### 直流功率参考值补偿方程

$$$P_{\text{dc 2}}^{\text{NEW }*} = P_{\text{dc 2}}^* + P_{\text{oscillation}}$$$

*频率控制策略核心，将提取的交流振荡功率叠加至直流参考值，实现振荡能量向直流链路的转移。*



## 验证详情

- **验证方式**: 电磁暂态（EMT）仿真对比分析
- **测试系统**: IEEE 4机6节点系统（230 kV, 60 Hz），包含4台同步发电机、2个负荷节点、1条长距离交流联络线及并联的VSC-HVDC链路
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 仿真验证表明，所提频率控制策略能有效将交流侧功率振荡转移至直流侧，使受端注入功率保持平稳。在多种母线与线路三相接地故障下，系统暂态稳定裕度显著提升，平均CCT提高22.93%，且发电机功角振荡快速收敛，证明了该策略在提升嵌入式HVDC系统动态性能方面的有效性。

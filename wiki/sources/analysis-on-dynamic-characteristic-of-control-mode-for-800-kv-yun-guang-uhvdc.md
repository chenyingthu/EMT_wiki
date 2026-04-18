---
title: "Analysis on dynamic characteristic of control mode for +/-800 kV Yun-Guang UHVDC"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Analysis on dynamic characteristic of control mode for 卤800 kV Yun-Guang UHVDC.pdf"]
---

# Analysis on dynamic characteristic of control mode for +/-800 kV Yun-Guang UHVDC

**作者**: 
**年份**: 2025
**来源**: `07&08/Analysis on dynamic characteristic of control mode for 卤800 kV Yun-Guang UHVDC.pdf`

## 摘要

：When Yun-Guang ±800kV ultra high voltage direct current （U HVDC）project is completeda parallel AC／DC power system with long distance and heavy capacity will come out．And the U HVDC control mode has im- portant influence on the power system stability．ConsequentlyYun-Guang ±800 kV U HVDC bipolar model was established in EMT DC．T he effect of AC system faults on the U HVDC transmission system in both constant current and constant power control modes and the response of U HVDC control system were computed and analyzedrespec- tively．Moreoverthe dynamic characteristic of the AC／DC system in two control strategies was comparatively ana- lyzed．T he results show thatcompared with the constant current modeall the electrical variables change more slowly than in constant power mode during the p

## 核心贡献


- 构建云广±800kV特高压直流双极电磁暂态详细仿真模型
- 对比分析定电流与定功率控制下交直流系统多类故障的动态响应特性
- 揭示不同控制策略对换相失败发生概率及故障后系统恢复时间的影响机制


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[pi控制|PI控制]]
- [[低压限流控制-vdcol|低压限流控制(VDCOL)]]
- [[详细换流器建模|详细换流器建模]]


## 涉及的模型


- [[12脉动换流器|12脉动换流器]]
- [[换流变压器|换流变压器]]
- [[平波电抗器|平波电抗器]]
- [[分布参数直流输电线路|分布参数直流输电线路]]
- [[交直流滤波器|交直流滤波器]]


## 相关主题


- [[特高压直流输电|特高压直流输电]]
- [[交直流相互作用|交直流相互作用]]
- [[换相失败|换相失败]]
- [[控制策略对比|控制策略对比]]
- [[故障动态特性|故障动态特性]]


## 主要发现


- 定功率控制下故障期间电气量变化较缓，但故障清除后直流电流突增易引发短时换相失败
- 定电流控制下整流侧故障不引发换相失败，逆变侧短路致换相失败但恢复较快
- 定功率控制方式下系统故障清除后的恢复时间显著长于定电流控制方式



## 方法细节

### 方法概述

本文基于PSCAD/EMTDC电磁暂态仿真平台，构建云广±800kV特高压直流双极详细模型，涵盖12脉动换流器、换流变压器、交直流滤波器、平波电抗器及分布参数线路。针对整流侧分别配置定电流与定功率控制策略，逆变侧配置定关断角、定电流及VDCOL协调控制。通过在整流侧与逆变侧交流母线注入三相短路、单相接地及两相短路等故障，记录换流母线电压、直流电压电流、触发角及关断角等电气量动态响应。对比分析两种控制模式下故障期间的电气量变化速率、换相失败触发条件及故障清除后的系统恢复特性，揭示控制策略对交直流系统暂态稳定性的影响机制。

### 数学公式


**公式1**: $$$\gamma = \arccos\left(\frac{2 I_d X_c k}{U_L} + \cos\beta\right)$$$

*关断角动态计算公式，用于实时评估换相裕度并判定是否发生换相失败（$\gamma < 5^\circ$）*


**公式2**: $$$I_{dc,pu} = 0.9 \cdot U_{dc,pu}$$$

*VDCOL低压限流环节线性段特性方程，用于故障期间根据直流电压跌落程度动态限制电流指令*


### 算法步骤

1. 在PSCAD/EMTDC中搭建云广±800kV双极直流系统一次设备详细模型，配置分布参数线路与交直流滤波器，设定额定运行点（单极2500MW，800kV）

2. 搭建二次控制系统，整流侧分别整定定电流与定功率PI控制器，逆变侧配置定关断角（$\gamma_{min}=5^\circ$）与VDCOL模块，完成控制逻辑闭环

3. 设置仿真步长与初始稳态，在0.8s时刻于整流侧或逆变侧交流母线注入指定类型故障（三相短路、单相金属性/经电阻接地、两相短路），故障持续0.1s后于0.9s清除

4. 实时采集并记录故障期间及清除后的交流母线电压标幺值、直流电流/功率标幺值、触发角$\alpha$、关断角$\gamma$及VDCOL动作状态

5. 对比定电流与定功率模式下电气量变化斜率、换相失败发生时刻及系统恢复至稳态所需时间，输出动态特性对比结论


### 关键参数

- **整流侧定电流PI增益**: $K_p=1.0989, T_i=0.01092\text{ s}$

- **逆变侧定电流PI增益**: $K_p=0.63, T_i=0.01524\text{ s}$

- **定关断角PI增益**: $K_p=0.7506, T_i=0.0544\text{ s}$

- **VDCOL线性段斜率**: 0.9（$0.4 < U_{dc,pu} < 0.9$）

- **基准值**: $U_{base}=800\text{ kV}, I_{base}=3125\text{ A}, P_{base}=2500\text{ MVA}$

- **故障时序**: 0.8s发生，0.9s清除（持续0.1s）

- **最小关断角阈值**: $\gamma_{min}=5^\circ$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 整流侧交流母线三相短路 | 定电流模式下触发角迅速降至$5^\circ$，直流功率归零，故障清除后0.3s恢复稳态；定功率模式下电气量变化更缓，清除后直流电流突增引发短时换相失败，恢复时间约0.3s | 定功率控制故障期间电压/电流变化率较定电流降低约25%，但清除后换相失败风险增加，恢复时间相当 |

| 逆变侧交流母线单相金属性接地 | 定电流模式下$I_{dc,pu}$峰值升至1.5，$\gamma$降至0引发换相失败，紧急移相后快速恢复；定功率模式下双极仍传输部分功率，清除后恢复时间>0.4s | 定功率控制避免了故障期间的完全功率中断，但系统恢复时间较定电流模式延长0.1s以上 |

| 逆变侧交流母线两相金属性短路 | 定电流模式下$I_{dc,pu}$峰值达1.6，$\gamma=0$导致换相失败，整流侧增大$\alpha$限流，清除后0.2s恢复稳态 | 定电流控制下电流冲击更大（1.6 pu vs 1.5 pu），但恢复速度更快（0.2s） |

| 逆变侧单相经过渡电阻接地 | 定电流模式下电压不对称度较低，未发生换相失败，直流功率仅较稳态值微降，系统全程维持运行 | 过渡电阻有效削弱了故障冲击，两种控制模式均未触发换相失败，定功率模式波动更小 |



## 量化发现

- 定功率控制下故障期间电气量变化速率较定电流控制降低约20%~30%，表现为电压/电流跌落斜率更平缓
- 逆变侧单相金属性接地时，定电流控制下直流电流标幺值峰值达1.5 pu，定功率控制下故障清除后恢复时间延长至0.4 s以上
- 逆变侧两相短路时，定电流控制下直流电流标幺值峰值达1.6 pu，系统恢复时间为0.2 s
- VDCOL在$0.4 < U_{dc,pu} < 0.9$区间内，电流指令严格按电压标幺值的0.9倍线性跟随，有效抑制故障电流越限
- 定功率控制整流侧故障清除后，直流电流突增导致短时换相失败持续时间约0.05~0.1 s，随后系统自动恢复


## 关键公式

### 关断角动态计算公式

$$$\gamma = \arccos\left(\frac{2 I_d X_c k}{U_L} + \cos\beta\right)$$$

*用于实时监测逆变器换相裕度，当计算值$\gamma < 5^\circ$时判定为换相失败，触发控制系统紧急移相*

### VDCOL低压限流特性方程

$$$I_{dc,pu} = 0.9 \cdot U_{dc,pu}$$$

*当直流电压标幺值跌落至0.4~0.9区间时启用，用于限制直流电流指令，防止故障电流过大导致连续换相失败*



## 验证详情

- **验证方式**: 电磁暂态仿真对比分析（PSCAD/EMTDC详细模型）
- **测试系统**: 云广±800kV特高压直流双极输电系统（送端云南楚雄，受端广东增城，线路长1438km，额定功率5000MW，单极2500MW）
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 仿真验证了定电流与定功率控制在不同交流故障下的动态响应差异。定电流控制恢复快但故障期间电流冲击大（1.5~1.6 pu），易引发换相失败；定功率控制故障期间电气量变化平缓，但清除后电流突增导致短时换相失败且恢复时间延长（>0.4s）。VDCOL与PI控制参数整定合理，模型能准确捕捉换流阀开关动态及控制系统调节过程，克服了机电暂态程序无法精确模拟换相失败与不对称故障的局限。

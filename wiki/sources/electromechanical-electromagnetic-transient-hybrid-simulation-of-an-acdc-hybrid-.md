---
title: "Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Xiong 等 - 2020 - Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV.pdf"]
---

# Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV

**作者**: CNKI
**年份**: 2022
**来源**: `17/Xiong 等 - 2020 - Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV.pdf`

## 摘要

UHVDC hierarchical connection to a system not only improves the voltage support of the receiving end grid but also brings problems such as the complex coupling relationship between different layers of the system. In order to study the operating characteristics of an AC/DC hybrid system with a UHVDC hierarchical connection, this paper examines the ±800 kV Yazhong-Jiangxi UHVDC transmission project. An AC/DC hybrid simulation model with UHVDC hierarchical connection mode is built based on ADPSS. First, the correctness of the electromagnetic transient model is verified. Then the accuracy and superiority of the hybrid simulation model are verified by comparing the simulation results under extinction angle step response of independent control command with the electromagnetic transient model. Fi

## 核心贡献


- 基于ADPSS构建含特高压分层直流的交直流混联电网机电电磁暂态混合仿真模型。
- 提出以换流变交流母线为边界的网络分割与戴维南等值接口方法实现子网交互。
- 验证混合仿真在独立控制与故障下的准确性计算效率较纯电磁暂态提升约23%。


## 使用的方法


- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[网络分割与戴维南等值|网络分割与戴维南等值]]
- [[用户自定义建模-udm|用户自定义建模(UDM)]]
- [[阶跃响应与故障对比测试|阶跃响应与故障对比测试]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[lcc-model|LCC]]
- [[换流变压器|换流变压器]]
- [[交直流滤波器|交直流滤波器]]
- [[平波电抗器|平波电抗器]]
- [[直流输电线路|直流输电线路]]
- [[500kv-1000kv交流电网|500kV/1000kV交流电网]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[特高压直流分层接入|特高压直流分层接入]]
- [[交直流混联电网|交直流混联电网]]
- [[机电-电磁暂态接口|机电-电磁暂态接口]]
- [[换相失败预防控制|换相失败预防控制]]
- [[仿真效率与精度评估|仿真效率与精度评估]]


## 主要发现


- 混合仿真能准确跟踪关断角独立控制指令并反映交流网络机电暂态特性。
- 相比纯电磁暂态仿真混合仿真计算耗时减少约23%显著提升计算效率。
- 交流故障下混合仿真直流波形细节更丰富较纯机电模型更精确反映动态响应。



## 方法细节

### 方法概述

本文基于ADPSS平台构建机电-电磁暂态混合仿真框架，针对±800kV雅中-江西特高压直流分层接入系统（高端接1000kV，低端接500kV）。核心方法采用网络分割与戴维南/诺顿等值接口技术，以换流变压器交流侧母线为边界将大电网划分为机电暂态子网（交流主网）与电磁暂态子网（直流系统及近区交流）。在PSASP中建立机电模型并验证，在ETSDAC中搭建包含双12脉动换流阀、独立控制策略（定关断角、CFPREV、VDCOL等）的电磁模型。通过边界节点电压电流的实时等值交互，实现两子网数据同步与联合求解，兼顾大电网机电动态与直流系统高频电磁暂态特性。

### 数学公式


**公式1**: $$$V_{eq}(t) = V_{oc}(t) - Z_{eq} \cdot I_{bdry}(t)$$$

*混合仿真边界戴维南等值接口方程，用于机电侧向电磁侧传递等效开路电压与等值阻抗，实现子网间电气量交互*


**公式2**: $$$\alpha_{inv} = \alpha_{base} - \Delta\alpha_{CFPREV}$$$

*逆变侧触发角控制方程，结合换相失败预防控制(CFPREV)输出修正量，用于分层接入下的独立阀组控制*


### 算法步骤

1. 机电侧建模与分网：在PSASP中搭建江西电网及联络线机电暂态模型，以换流变压器交流母线为分割边界，将直流系统及近区交流划出，完成机电侧潮流计算与数据校验。

2. 电磁侧建模与验证：在ETSDAC中搭建±800kV分层直流一次系统（含换流变、滤波器、平波电抗器）及控制系统（独立关断角控制、CEC、VDCOL、CFPREV），并与PSCAD/EMTDC纯电磁模型进行阶跃与故障对比，验证模型正确性。

3. 接口等值与数据映射：在边界母线处应用戴维南/诺顿等值原理，配置ADPSS混合仿真数据接口，设定机电侧与电磁侧的步长协调机制，实现边界电压电流的实时双向传递。

4. 任务分配与联合求解：提交分网数据与接口配置，启动ADPSS混合仿真引擎。机电侧求解网络代数方程与发电机微分方程，电磁侧求解开关器件与RLC网络微分方程，通过接口等值电路迭代收敛。

5. 结果对比与评估：分别设置关断角阶跃指令与交流故障场景，提取混合仿真波形，与纯电磁暂态（PSCAD）及纯机电暂态（PSASP）结果进行幅值、相位、动态响应时间及计算耗时的定量对比分析。


### 关键参数

- **额定输送功率**: 10000 MW

- **额定直流电压/电流**: ±800 kV / 6.25 kA

- **受端500kV/1000kV短路比**: 4.53 / 6.10

- **稳态关断角**: 17°

- **换流变压器参数**: 整流侧1551MVA/23%，逆变500kV侧1470MVA/19%，逆变1000kV侧1470MVA/20%

- **故障测试等效电感**: 0.35 H



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 关断角独立控制阶跃响应 | 4s时500kV逆变器关断角指令阶跃增加10°，7s恢复至稳态。混合仿真中500kV侧快速跟踪指令，1000kV侧关断角保持17°不变，验证了分层独立控制特性。因无功消耗增加，500kV换流母线电压出现下降。 | 混合仿真波形与纯电磁暂态模型高度吻合，暂态响应趋势一致，且能同时输出交流系统各节点电压动态。 |

| 500kV换流母线三相接地故障 | 3s时发生持续0.1s的三相感性接地故障（0.35H）。故障导致换相电压跌落，高端逆变器关断角迅速降至0°并发生换相失败，直流功率下降；直流电流骤升引发1000kV侧逆变器连锁换相失败。 | ADPSS混合仿真与PSCAD纯电磁暂态模型的暂态响应曲线拟合度极高，动态过程与换相失败机理完全一致。 |

| 永修-梦山线路三相短路故障 | 10s时线路发生持续0.1s的三相接地短路。混合仿真与PSASP机电模型在交流节点电压暂态趋势上基本一致，但混合仿真直流系统波形细节更丰富，机电模型因基波相量法导致直流响应波动幅度偏大且恢复较慢。 | 混合仿真在保留大电网机电动态特性的同时，直流暂态波形还原精度显著优于纯机电暂态模型。 |



## 量化发现

- 混合仿真计算耗时约138 s，较纯电磁暂态仿真（PSCAD约170 s）效率提升约23%。
- 关断角阶跃响应中，500 kV侧指令阶跃+10°，1000 kV侧关断角偏差保持在稳态17°，验证了分层独立控制的有效性。
- 500 kV母线三相故障持续0.1 s期间，高端逆变器关断角迅速降至0°，直流功率出现显著跌落，换相失败过程被精确捕捉。
- 机电暂态模型直流响应波动幅度较混合仿真偏大，混合仿真在保留机电动态特性的同时，直流波形细节还原度显著优于基波相量法模型。


## 关键公式

### 戴维南边界等值接口方程

$$$V_{th} = V_{oc} - Z_{th} \cdot I_{bdry}$$$

*用于机电-电磁子网在换流变交流母线边界处的电气量交互与数据同步，是混合仿真联合求解的核心数学基础*



## 验证详情

- **验证方式**: 多模型对比仿真验证（混合仿真 vs 纯电磁暂态 vs 纯机电暂态）
- **测试系统**: ±800 kV雅中-江西特高压直流分层接入系统（高端接1000kV，低端接500kV）及2020年规划江西电网网架
- **仿真工具**: ADPSS（含PSASP机电模块与ETSDAC电磁模块）、PSCAD/EMTDC
- **验证结果**: 混合仿真模型在关断角独立阶跃响应与交流故障工况下，动态波形与纯电磁暂态模型高度一致，验证了接口等值与联合求解的准确性；相较于纯机电模型，能更精细刻画直流系统高频暂态过程；计算效率提升23%，兼顾了大规模交直流混联电网的仿真精度与速度。

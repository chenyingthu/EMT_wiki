---
title: "An aggregation method of permanent magnet synchronous wind farms for electromechanical transient stability analysis"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Yang 等 - 2011 - An aggregation method of permanent magnet synchronous generators wind farm model for electromagnetic.pdf"]
---

# An aggregation method of permanent magnet synchronous wind farms for electromechanical transient stability analysis

**作者**: CNKI
**年份**: 2023
**来源**: `06/Yang 等 - 2011 - An aggregation method of permanent magnet synchronous generators wind farm model for electromagnetic.pdf`

## 摘要

An aggregation method to build the model of large-scale wind farm utilizing permanent magnet synchronous generators (PMSG), which is used in the electromagnetic transient analysis of the wind farm, is presented. A simplified transient model of PMSG-based wind farm is built and the simulation results from the simplified transient model and those from corresponding detailed electromagnetic transient simulation model are compared and verified. The response characteristics of PMSG unit under various power grid faults are analyzed; on this basis two kinds of wind farm simulation models, namely a detailed model of wind farm, which consists of forty PMSGs and the capacity of each PMSG is 5MW, and an equivalent aggregation model with the capacity of 200MW for the very wind farm, are built. The agg

## 核心贡献


- 提出基于功率等效原则的PMSG风电场聚合建模方法，适用于大规模电磁暂态仿真。
- 建立保留变流器d-q轴电流控制的PMSG简化模型，忽略机械动态以降低计算量。
- 推导集电网络与升压变压器等值参数计算方法，实现百兆瓦级风场快速等效建模。


## 使用的方法


- [[聚合等值方法|聚合等值方法]]
- [[简化电磁暂态建模|简化电磁暂态建模]]
- [[d-q坐标系pi控制|d-q坐标系PI控制]]
- [[π型等值电路|π型等值电路]]
- [[功率等效原则|功率等效原则]]


## 涉及的模型


- [[pmsg|PMSG]]
- [[全功率变流器|全功率变流器]]
- [[升压变压器|升压变压器]]
- [[集电线路|集电线路]]
- [[风电场详细模型|风电场详细模型]]
- [[风电场聚合模型|风电场聚合模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[模型聚合|模型聚合]]
- [[电网故障响应|电网故障响应]]
- [[电压跌落分析|电压跌落分析]]


## 主要发现


- 聚合模型与详细模型在电压跌落故障下的动态响应高度一致，验证了方法有效性。
- 升压变压器参数对聚合模型精度影响显著，必须在等值过程中予以保留和精确建模。
- 集电线路对百兆瓦级风场聚合模型仿真结果影响较小，在常规精度要求下可忽略不计。



## 方法细节

### 方法概述

本文提出一种适用于电磁暂态(EMT)仿真的PMSG风电场聚合建模方法。首先针对10秒以内的短时暂态过程，忽略风速变化、桨距角调节及传动链机械动态，假设故障期间直流母线电压恒定，省略直流电压控制环节，仅保留网侧变流器在d-q同步旋转坐标系下的有功/无功电流PI控制及前馈解耦网络，构建单机简化模型。随后基于功率等效原则进行风场聚合：保证聚合前后公共连接点(PCC)电压、总装机容量及输出有功/无功功率严格相等。在等值过程中，将各机组出口升压变压器容量相加且标幺值参数保持不变；集电网络采用π型等值电路，通过等值前后有功与无功损耗相等的原则反推等效线路长度。最终构建包含等效发电机、升压变压器及集电线路的200MW聚合模型，并通过与40台5MW详细模型在电网故障下的动态响应对比，验证模型精度及内部元件对聚合精度的影响。

### 数学公式


**公式1**: $$$S_{G\_AWF} = \sum_{i=1}^{n} S_{WTGi}$$$

*风电场聚合模型发电机额定容量等于各单台机组额定容量之和*


**公式2**: $$$P_{AWF} = \sum_{i=1}^{n} P_{WTGi} - \sum_{i=1}^{n} P_{TFi} - P_L$$$

*聚合模型输出有功功率等于各机组有功功率之和减去升压变压器有功损耗与集电线路有功损耗*


**公式3**: $$$Q_{AWF} = \sum_{i=1}^{n} Q_{WTGi} - \sum_{i=1}^{n} Q_{TFi} + \sum Q_C - Q_L$$$

*聚合模型输出无功功率等于各机组无功功率之和减去变压器无功损耗，加上无功补偿容量，再减去线路无功损耗*


### 算法步骤

1. 步骤1：构建PMSG单机简化电磁暂态模型。忽略风速变化、风能利用系数变化、变桨控制及传动轴系动态；假设电网故障期间直流母线电压恒定，省略直流电压控制环节；保留网侧变流器在d-q同步旋转坐标系下的有功/无功电流PI控制及前馈解耦网络。

2. 步骤2：确定聚合边界与等效原则。设定聚合前后公共连接点(PCC)电压幅值与相位一致；聚合模型总装机容量为所有单机容量代数和；聚合模型在PCC点输出的有功功率和无功功率与详细模型严格相等。

3. 步骤3：计算升压变压器等值参数。将风电场内所有机组出口升压变压器的额定容量相加得到等效变压器容量，其标幺值短路电阻与短路电感保持与单台变压器一致。

4. 步骤4：计算集电网络等值参数。采用π型等值电路表示内部集电线路，根据等值前后线路有功损耗和无功损耗相等的原则，反推计算等效线路长度$l_{eq}$及对应的R、L、C参数。

5. 步骤5：组装聚合模型并进行故障仿真验证。将等效发电机、等效升压变压器、等效集电线路及主变压器连接至PCC点，施加三相对地短路故障（电压跌落至20%，持续100ms），对比聚合模型与40台详细模型的PCC电压、有功/无功功率动态响应曲线。

6. 步骤6：灵敏度分析。分别设置包含等值线路与变压器、仅含变压器、两者均忽略三种算例，量化评估内部网络元件对聚合精度的影响程度。


### 关键参数

- **单机额定容量**: 5 MW

- **机组数量**: 40台

- **风场总容量**: 200 MW

- **主变压器T1**: 220/35 kV, 240 MVA, 短路阻抗13%

- **升压变压器T2**: 35/0.69 kV, 6 MVA, 短路阻抗6%

- **集电线路参数**: 长度2 km, 正序电阻0.12 Ω/km, 正序电感1.05 mH/km, 正序电容11 nF/km

- **故障设置**: 三相对地短路, PCC电压跌落至20%, 持续时间100 ms

- **仿真时间尺度**: < 10 s (电磁暂态)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 200MW风场三相对地短路故障对比 | 在PCC点施加电压跌落至20%、持续100ms的故障。聚合模型与40台详细模型的PCC电压恢复曲线、有功功率跌落与恢复过程、无功功率支撑响应完全重合。 | 聚合模型与详细模型的动态响应曲线高度一致，暂态超调量与稳态偏差均<1%，模型节点数减少约97.5%，大幅降低EMT仿真计算负担。 |

| 内部元件影响灵敏度分析(算例1/2/3) | 算例1(含等值线路与变压器)、算例2(忽略线路)、算例3(忽略线路与变压器)对比。结果显示算例1与算例2曲线几乎重合，算例3在故障恢复期出现明显有功/无功功率偏差。 | 升压变压器阻抗对聚合精度影响显著(忽略后误差>5%)，而2km集电线路阻抗影响可忽略(误差<0.5%)，验证了保留变压器等值、简化线路的合理性。 |



## 量化发现

- 聚合模型将40台5MW机组等效为单台200MW机组，模型规模缩减97.5%，适用于大规模风场EMT仿真。
- 在电压跌落至20%、持续100ms的三相对地短路故障下，聚合模型与详细模型的PCC电压、有功/无功功率动态响应偏差<1%。
- 升压变压器标幺值参数(短路电阻0.002 pu, 短路电感0.06 pu)对聚合模型暂态响应影响显著，必须保留等值。
- 集电线路(2km, R=0.12Ω/km, L=1.05mH/km)对200MW级风场聚合精度的影响可忽略不计，在工程建模中可简化。
- 简化模型假设直流母线电压恒定且忽略机械动态，在10秒以内的电磁暂态仿真中可提供足够的精度，但不适用于机电暂态长过程分析。


## 关键公式

### 聚合容量等效公式

$$$S_{G\_AWF} = \sum_{i=1}^{n} S_{WTGi}$$$

*用于确定聚合模型中等效发电机的额定视在功率，保证容量规模一致*

### 聚合有功功率平衡方程

$$$P_{AWF} = \sum_{i=1}^{n} P_{WTGi} - \sum_{i=1}^{n} P_{TFi} - P_L$$$

*用于计算聚合模型在PCC点的净输出有功功率，扣除内部变压器与线路损耗*

### 聚合无功功率平衡方程

$$$Q_{AWF} = \sum_{i=1}^{n} Q_{WTGi} - \sum_{i=1}^{n} Q_{TFi} + \sum Q_C - Q_L$$$

*用于计算聚合模型在PCC点的净输出无功功率，计入无功补偿装置并扣除内部损耗*



## 验证详情

- **验证方式**: 对比仿真验证与灵敏度分析
- **测试系统**: 200 MW PMSG风电场(40×5 MW)，经35 kV集电网络与220/35 kV主变压器接入220 kV电网
- **仿真工具**: MATLAB/Simulink
- **验证结果**: 仿真结果表明，所提聚合模型在稳态运行与三相对地短路暂态过程中，其PCC电压、有功/无功功率动态响应与40台详细模型高度一致。升压变压器等值对精度至关重要，集电线路等值在中小规模风场中可忽略。该方法有效降低了EMT仿真计算量，适用于大规模PMSG风电场的电磁暂态稳定性分析。

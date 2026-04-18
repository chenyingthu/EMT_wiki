---
title: "Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synchronous Oscillation Analysis"
type: source
authors: ['未知']
year: 2020
journal: "2020 IEEE Power & Energy Society General Meeting (PESGM);2020; ; ;10.1109/PESGM41954.2020.9281733"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/pesgm41954.2020.9281733.pdf.pdf"]
---

# Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synchronous Oscillation Analysis

**作者**: 
**年份**: 2020
**来源**: `13&14/files/pesgm41954.2020.9281733.pdf.pdf`

## 摘要

—Single or multiple wind turbine generators (WTGs) model have already been used in sub-synchronous oscillation (SSO) analysis. However, there is little researches on the equivalence method of wind farm (WF) for the SSO study. The general equivalence method may lose the weak damping SSO mode. In this paper, a DDPMSG WF multi-machine equivalence method is proposed for SSO analysis. According to their SSO modes, the DDPMSGs are grouped in two steps. The oscillation frequency or damping is only considered in each step. The parameters of equivalent DDPMSG model are calculated by aggregation in each group. Furthermore, an online application processing method is proposed. The simulation verification is carried out based on small signal model and electromagnetic transient model of WF. The results 

## 核心贡献


- 提出基于次同步振荡频率与阻尼比的两步聚类方法，实现直驱风机精准分组
- 构建多机等值参数聚合算法，有效保留风电场次同步振荡弱阻尼模态
- 提出适用于次同步振荡分析的风场动态等值在线应用处理流程


## 使用的方法


- [[质量阈值-qt-聚类算法|质量阈值(QT)聚类算法]]
- [[参数聚合等值法|参数聚合等值法]]
- [[小信号模态分析|小信号模态分析]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[直驱永磁同步发电机-ddpmsg|直驱永磁同步发电机(DDPMSG)]]
- [[风电场|风电场]]
- [[网侧变流器及控制系统|网侧变流器及控制系统]]
- [[锁相环-pll|锁相环(PLL)]]


## 相关主题


- [[次同步振荡-sso-分析|次同步振荡(SSO)分析]]
- [[风电场动态等值|风电场动态等值]]
- [[弱阻尼模态保留|弱阻尼模态保留]]
- [[在线等值应用|在线等值应用]]


## 主要发现


- 所提等值方法能精准保留详细风电场模型中的次同步振荡弱阻尼模态
- 小信号与电磁暂态仿真验证了多机等值模型在次同步振荡分析中的准确性
- 两步聚类法有效避免了传统单机等值丢失关键振荡模态的问题



## 方法细节

### 方法概述

本文提出一种面向次同步振荡(SSO)分析的直驱永磁同步发电机(DDPMSG)风电场多机等值方法。针对传统基于有功功率聚类易丢失弱阻尼SSO模态的问题，本方法以SSO模态特征为核心，采用两步聚类策略：第一步仅依据振荡频率，利用质量阈值(QT)聚类算法进行分组，无需预设聚类数且能自适应匹配实际工况；第二步在各频率组内，依据阻尼比与临界阈值将风机划分为强阻尼组与弱阻尼组（及理论负阻尼组）。分组后，提供两种参数聚合策略（方法A侧重组内模态均值，方法B聚焦最弱阻尼模态）计算等值机电气与控制参数，并结合电压损耗恒定原则等值集电网络阻抗。此外，针对在线应用，提出基于环境激励响应的模态辨识流程，利用随机减量技术(RDT)与TLS-ESPRIT算法从系统随机噪声响应中提取自由振荡信号，实时获取各风机SSO频率与阻尼比，实现等值模型的动态更新与在线部署。

### 数学公式


**公式1**: $$$X_{eq} = \sum_{i=1}^{n_f} X_i$$$

*方法A的功率等值公式，将组内所有风机的有功/无功功率直接累加，适用于保留组内平均模态特征。*


**公式2**: $$$X_{eq} = \begin{cases} n_{f1} X_{weakest}, & \text{弱阻尼组} \\ \sum_{i=1}^{n_f} X_i - n_{f1} X_{weakest}, & \text{强阻尼组} \end{cases}$$$

*方法B的功率等值公式，弱阻尼组以最弱阻尼风机功率为基准放大，强阻尼组按总功率守恒原则修正，旨在精准保留最弱阻尼模态。*


**公式3**: $$$M_{eq} = \sum_{i=1}^{n_f} M_i, \quad N_{eq} = \frac{1}{n_f} \sum_{i=1}^{n_f} \frac{1}{N_i}, \quad O_{eq} = \frac{1}{n_f} \sum_{i=1}^{n_f} O_i$$$

*控制与电气参数等值公式。M类参数（如机侧功率、直流电容、外环PI）直接累加；N类参数（如滤波阻抗、内环PI）采用调和平均；O类参数（如PLL PI）采用算术平均。*


**公式4**: $$$Z_{eq} = \left[ \sum_{i=1}^{n_f} \left( \sum_{k=1}^{i} \left( Z_k \sum_{j=k}^{m_f} P_j \right) P_i \right) \right] / \left( \sum_{i=1}^{n_f} P_i \right)^2$$$

*基于电压损耗恒定原则的集电线路等值阻抗公式，确保等值前后线路压降特性一致。*


**公式5**: $$$Z_{Teq} = \frac{1}{\sum_{i=1}^{n_f} \frac{1}{Z_{Ti}}}$$$

*同组内多台箱式变压器并联等值阻抗公式。*


### 算法步骤

1. 步骤1：获取全场各风机的SSO模态参数。通过小信号分析或在线辨识，提取每台风机$i$的次同步振荡频率$f_i$与阻尼比$\zeta_i$。

2. 步骤2：第一步频率聚类。设定QT聚类半径$r_0$，计算所有风机样本间的距离。以包含样本数最多的候选组作为首个频率簇，移除已聚类样本，迭代执行直至所有风机归属某一频率组。

3. 步骤3：第二步阻尼分类。设定阻尼临界阈值$\zeta_{weak}$。在每个频率组内，按$\zeta_i \ge \zeta_{weak}$划入强阻尼组，按$0 < \zeta_i < \zeta_{weak}$划入弱阻尼组，若存在$\zeta_i \le 0$则划入负阻尼组。

4. 步骤4：选择参数聚合策略。根据分析需求选择方法A（保留组内平均特性）或方法B（聚焦最弱阻尼特性），利用式(1)或(2)计算等值有功/无功功率。

5. 步骤5：等值其余参数与网络。利用式(3)计算等值机控制参数与电气参数；利用式(4)和式(5)分别计算等值集电线路阻抗与箱变阻抗，完成单组等值机建模。

6. 步骤6：在线应用处理（可选）。在系统正常运行时注入或采集环境白噪声激励，记录各风机有功响应。应用RDT提取自由振荡衰减信号，输入TLS-ESPRIT算法实时辨识$f$与$\zeta$，循环执行步骤2-5实现模型在线更新。


### 关键参数

- **QT聚类半径_r0**: 0.5

- **阻尼临界阈值_ζ_weak**: 1.5%

- **风机额定功率**: 1.5 MW

- **等值策略**: 方法A（模态均值）或方法B（最弱阻尼聚焦）

- **辨识算法**: RDT + TLS-ESPRIT



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case 1: 66机风电场小信号模型验证 | 系统状态矩阵阶数由812阶大幅降至56阶。等值模型成功分离出两组频率（约19.6Hz与17.6Hz），并精准保留弱阻尼模态。方法A的频率误差为0.0298~0.0909Hz，阻尼比误差为0.164%~0.751%；方法B聚焦最弱模态，频率误差仅0.0103Hz，阻尼比误差0.118%。 | 相比传统基于有功功率的多机等值与单机等值，本方法完整保留了双频模态结构，弱阻尼模态阻尼比误差降低至0.12%以内，传统方法则完全丢失弱阻尼特征。 |

| Case 2: 4机风电场电磁暂态(EMT)仿真验证 | 在PSCAD中施加三相瞬时故障(1ms)。详细模型弱阻尼机(WTG1)频率4.431Hz、阻尼0.617%。所提等值机(Eq_Pro1)频率4.401Hz、阻尼0.553%。传统等值机(Eq_Con1)频率4.476Hz、阻尼1.145%。 | 故障后有功功率响应曲线显示，传统等值模型衰减速度明显偏快（阻尼偏大），而所提等值模型的功率振荡衰减轨迹与详细模型高度重合，动态响应误差<5%，验证了弱阻尼模态在时域仿真中的高保真度。 |



## 量化发现

- 模型降维效果显著：66机详细系统状态矩阵从812阶降至56阶，计算规模缩减约93%。
- 频域特征误差极小：所提方法A的频率最大绝对误差为0.0909Hz，阻尼比最大绝对误差为0.751%；方法B的频率误差控制在0.0103Hz以内，阻尼比误差仅0.118%。
- 时域动态响应高保真：EMT故障仿真中，所提等值机有功振荡衰减曲线与详细模型几乎重合，传统方法阻尼比偏差达0.528%，导致振荡衰减过快。
- 在线辨识可行性：基于RDT与TLS-ESPRIT的环境激励模态提取方法，可在无大扰动工况下实现频率与阻尼比的实时估计，支撑等值模型在线更新。


## 关键公式

### 方法B功率聚合公式

$$$X_{eq} = \begin{cases} n_{f1} X_{weakest}, & \text{弱阻尼组} \\ \sum_{i=1}^{n_f} X_i - n_{f1} X_{weakest}, & \text{强阻尼组} \end{cases}$$$

*当分析目标为精准捕捉风电场最危险的弱阻尼次同步振荡模态时使用，通过放大最弱阻尼机权重避免模态被强阻尼机平均化掩盖。*

### 多机控制与电气参数等值公式

$$$M_{eq} = \sum_{i=1}^{n_f} M_i, \quad N_{eq} = \frac{1}{n_f} \sum_{i=1}^{n_f} \frac{1}{N_i}, \quad O_{eq} = \frac{1}{n_f} \sum_{i=1}^{n_f} O_i$$$

*在完成风机分组后，用于计算等值单机的直流电容、PI控制器参数、滤波阻抗及PLL参数，确保等值机动态特性与组内原机群一致。*

### 箱式变压器并联等值阻抗公式

$$$Z_{Teq} = \frac{1}{\sum_{i=1}^{n_f} \frac{1}{Z_{Ti}}}$$$

*用于将同一分组内多台风机出口的箱变阻抗等效为单一阻抗，简化集电网络拓扑，同时保持端口电气特性不变。*



## 验证详情

- **验证方式**: 小信号特征值分析对比 + 电磁暂态(EMT)时域仿真验证 + 传统方法横向对比
- **测试系统**: Case 1: 66台1.5MW DDPMSG经集电线路接入无穷大电网；Case 2: 4台1.5MW DDPMSG经线路接入无穷大电网
- **仿真工具**: MATLAB (小信号状态矩阵构建与特征值计算), PSCAD/EMTDC (电磁暂态时域仿真与故障响应测试)
- **验证结果**: 验证表明，所提两步聚类多机等值方法能有效克服传统方法丢失弱阻尼模态的缺陷。小信号分析证实等值模型特征值与详细模型高度吻合（频率误差<0.1Hz，阻尼误差<0.75%）；EMT仿真证实故障后弱阻尼机有功振荡衰减轨迹与详细模型一致，模型阶数降低93%的同时保持了次同步振荡分析所需的高精度，具备在线工程应用潜力。

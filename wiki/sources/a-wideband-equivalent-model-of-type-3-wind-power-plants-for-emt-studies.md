---
title: "A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies"
type: source
authors: ['未知']
year: 2016
journal: "IEEE Transactions on Power Delivery;2016;31;5;10.1109/TPWRD.2016.2551287"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Hussein 等 - 2016 - A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies.pdf"]
---

# A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies

**作者**: 
**年份**: 2016
**来源**: `05/Hussein 等 - 2016 - A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies.pdf`

## 摘要

—This paper presents the development and validation of an accurate and computationally efﬁcient wideband reduced-order dynamic equivalent model for the Type-3-based wind power plant (WPP). The proposed Type-3 WPP equivalent model reproduces the dynamic behavior of the WPP in response to an electromag- netic transient in the host power system and is composed of two parts: 1) a static frequency-dependent network equivalent model which represents the response of all passive components of the WPP in a wideband frequency range, and 2) a dynamic low-frequency equivalent model that represents the aggregated dynamic model of the doubly-fed asynchronous generator (which is also referred to as doubly-fed induction generator) wind turbine generators, their local controls, and the WPP supervisory cont

## 核心贡献


- 提出宽频降阶动态等值模型，结合频变网络与低频动态模块精准复现暂态响应
- 采用矢量拟合技术构建无源网络频响模型，结合伴随电路法实现高效时域接口
- 建立聚合双馈风机及控制系统的低频动态等值模块，显著降低仿真计算负担


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[频变网络等值|频变网络等值]]
- [[伴随电路法|伴随电路法]]
- [[动态低频等值|动态低频等值]]
- [[降阶建模|降阶建模]]
- [[双线性变换|双线性变换]]


## 涉及的模型


- [[type-3风电场|Type-3风电场]]
- [[双馈异步发电机|双馈异步发电机]]
- [[风力发电机组|风力发电机组]]
- [[集电网络|集电网络]]
- [[背靠背变流器|背靠背变流器]]
- [[风电场协调控制|风电场协调控制]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[宽频等值建模|宽频等值建模]]
- [[实时仿真|实时仿真]]
- [[故障穿越|故障穿越]]
- [[风电场降阶等值|风电场降阶等值]]
- [[频率相关建模|频率相关建模]]


## 主要发现


- 相比详细模型大幅降低计算负担，在PSCAD中验证保持高精度暂态响应
- 联合频变网络与低频动态模块，准确复现外部扰动下的端口响应与故障穿越特性
- 模型计算效率满足实际硬件资源限制，具备应用于大规模系统实时仿真的能力



## 方法细节

### 方法概述

本文提出一种适用于电磁暂态(EMT)研究的Type-3风电场宽频降阶动态等值模型。该模型由静态频变网络等值(FDNE)与动态低频等值(DLFE)两部分构成。FDNE利用矢量拟合技术将集电网络等无源元件的宽频阻抗响应拟合为有理函数，并通过双线性变换与伴随电路法实现时域接口。DLFE聚焦0~20Hz低频动态，聚合双馈风机的气动特性、传动链、本地控制及风电场协调控制。通过忽略定子磁链导数并抵消RSC控制交叉耦合项，将发电机与变流器系统简化为PI控制器与一阶惯性环节。两者在并网点通过受控电流源并联，在保持高精度的同时大幅降低微分方程数量与计算负担。

### 数学公式


**公式1**: $$$f_{fit}(s) = \sum_{i=1}^n \frac{c_i}{s-a_i} + d + sh$$$

*矢量拟合(VF)得到的频变网络有理函数传递函数，用于表征无源元件宽频阻抗/导纳特性*


**公式2**: $$$P_{mech} = \frac{1}{2} \rho A v_{wind}^3 C_p(\lambda, \beta) / S_{base}^{WTG}$$$

*风机等效气动机械功率计算公式，将风能转化为标幺值机械功率*


**公式3**: $$$\lambda = \frac{(\omega_{req}/G) \cdot r}{v_{wind}}$$$

*叶尖速比定义式，关联等效转速、齿轮箱比、叶片半径与风速*


**公式4**: $$$C_p(\lambda, \beta) = c_1 \left( \frac{c_2}{\lambda_i} - c_3 \beta - c_4 \beta^{c_5} - c_6 \right) \exp\left(\frac{-c_7}{\lambda_i}\right)$$$

*风机功率系数$C_p$的解析表达式，包含9个待辨识常数*


**公式5**: $$$F = \frac{\|P_{mech} - P_{morg}\|}{\|P_{morg}\|}$$$

*气动参数辨识的最小二乘优化目标函数，用于最小化等值模型与原始模型机械功率偏差*


**公式6**: $$$2(H_t + H_g) \frac{d\omega}{dt} = T_m - T_e - D\omega$$$

*单质量块传动链简化微分方程，描述聚合风机转子低频机械动态*


**公式7**: $$$\sigma \tau_r \frac{d\vec{i}_r}{dt} + \vec{i}_r = \frac{\vec{V}_r}{R_r} - j \frac{(1-\sigma)\tau_r}{L_m} \Delta \omega \vec{\psi}_s - j \Delta \omega \sigma \tau_r \vec{i}_r$$$

*忽略定子磁链导数后的降阶转子电流动态方程，用于构建发电机-变流器等值模块*


### 算法步骤

1. 1. 无源网络频响提取与拟合：获取风电场集电系统、变压器及滤波器等无源元件的宽频导纳/阻抗频率响应数据，采用矢量拟合(VF)算法迭代求解极点与留数，构建有理传递函数模型。

2. 2. 伴随电路时域接口转换：对拟合得到的有理函数应用双线性变换，将其离散化为电导矩阵与历史电流源并联的伴随电路形式，以便无缝嵌入EMT仿真求解器的节点导纳矩阵。

3. 3. 气动与传动链参数辨识：基于详细模型仿真或实测数据，构建最小二乘目标函数，利用MATLAB优化工具箱辨识$C_p$曲线参数$c_1 \sim c_9$，并建立双质量块或单质量块传动链微分方程组。

4. 4. 发电机-变流器降阶推导：忽略定子磁链变化率，将转子电压方程与RSC内环dq电流控制结合，抵消交叉耦合项与反馈项，将复杂电磁暂态模型等效为单PI控制器串联一阶惯性环节。

5. 5. 协调控制与FRT逻辑集成：构建包含最大功率跟踪/调度指令切换、无功/电压协调控制、故障穿越(FRT)电流限幅及有功-无功优先级分配的监督控制模块，输出dq电流参考值。

6. 6. 模型并联与验证：将FDNE与DLFE在PCC处通过三相电流控制电流源并联，在PSCAD/EMTDC中搭建测试系统，施加对称/不对称故障及重合闸操作，对比等值模型与详细模型的端口电压、电流及功率波形。


### 关键参数

- **DLFE有效频带**: 0~20 Hz

- **传动链动态频带**: 最高约3 Hz

- **变流器额定容量占比**: 30%~40% (相对于风机额定功率)

- **漏磁系数**: $\sigma = 1 - L_m^2/(L_s L_r)$

- **转子时间常数**: $\tau_r = (1+\sigma_r)L_m/R_r$

- **气动优化参数**: $c_1 \sim c_9$ (通过最小二乘辨识)

- **测试系统风机规模**: 8台 × 1.7 MW Type-3 DFAG



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case I: 三相接地故障(L-L-L-G) | 故障发生于t=3.8s，距PCC 15km处，持续150ms。故障前WPP向系统输送12MW有功。故障期间PCC电压跌落至35%额定值，等值模型无功电流精确升至1.0 p.u.，有功电流降至0，故障清除后电压与功率快速恢复。 | 等值模型与详细全阶模型在PCC电压、三相注入电流、有功/无功功率波形上高度重合，最大动态偏差<1%，计算时间显著缩短，满足实时仿真硬件限制。 |

| Case II: 单相接地故障(L-G) | 验证不对称故障下的负序响应与电压波动特性。等值模型准确复现了非故障相电压抬升、负序电流注入及FRT控制下的无功支撑过程。 | 在不对称工况下，等值模型端口响应与详细模型误差极小，证明宽频等值架构对正/负序分量均具备高精度表征能力，且未引入数值振荡。 |



## 量化发现

- DLFE模块精准覆盖0~20Hz低频动态范围，传动链机械模型适用频率上限约为3Hz。
- 故障期间PCC电压最低跌至35%额定值时，等值模型无功电流响应精确达到1.0 p.u.，有功电流降至0，与详细模型完全一致。
- 背靠背变流器容量设计为风机额定功率的30%~40%，等值模型在此容量约束下准确复现了限流逻辑与FRT特性。
- 相比详细全阶模型，微分方程数量大幅减少，计算负担显著降低，在PSCAD/EMTDC中验证具备应用于实际硬件资源限制下实时仿真的能力。
- 气动参数辨识优化目标函数收敛，确保等效机械功率$P_{mech}$与原始详细模型偏差最小化，支撑了宽频等值模型的高精度基础。


## 关键公式

### 频变网络有理拟合方程

$$$f_{fit}(s) = \sum_{i=1}^n \frac{c_i}{s-a_i} + d + sh$$$

*用于FDNE模块构建，将无源集电网络的宽频阻抗响应转化为时域可解的伴随电路形式*

### 降阶转子电流动态方程

$$$\sigma \tau_r \frac{d\vec{i}_r}{dt} + \vec{i}_r = \frac{\vec{V}_r}{R_r} - j \frac{(1-\sigma)\tau_r}{L_m} \Delta \omega \vec{\psi}_s - j \Delta \omega \sigma \tau_r \vec{i}_r$$$

*在忽略定子磁链导数假设下，结合RSC控制推导得出，是DLFE中发电机-变流器等值模块的核心状态方程*

### 单质量块传动链方程

$$$2(H_t + H_g) \frac{d\omega}{dt} = T_m - T_e - D\omega$$$

*用于DLFE中聚合风机机械动态建模，适用于0~3Hz低频暂态过程分析*



## 验证详情

- **验证方式**: 离线电磁暂态仿真对比分析（等值模型 vs 详细全阶模型）
- **测试系统**: 包含8台1.7MW Type-3双馈风机、13.8/115kV升压变压器、13.8kV集电网络、2.3kV风机侧DVR及Yg/Δ变压器、风电场监督控制系统的基准测试网络
- **仿真工具**: PSCAD/EMTDC (离线EMT时域仿真), MATLAB (参数优化与辨识)
- **验证结果**: 在对称三相短路(150ms, 15km外)与不对称单相接地故障下，等值模型在PCC处的电压跌落(至35%)、无功电流注入(1.0 p.u.)、有功/无功功率动态响应与详细全阶模型高度一致。验证了宽频等值模型在外部扰动下的高精度与强鲁棒性，同时计算效率满足实时仿真需求，未牺牲暂态波形保真度。

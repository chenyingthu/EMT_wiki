---
title: "A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings"
type: source
authors: ['R. Yonezawa']
year: 2023
journal: "Electric Power Systems Research, 219 (2023) 109248. doi:10.1016/j.epsr.2023.109248"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/03/Yonezawa - 2023 - A phase-domain synchronous machine modeling technique by using magnetic circuit representation of ar.pdf"]
---

# A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings

**作者**: R. Yonezawa
**年份**: 2023
**来源**: `03/Yonezawa - 2023 - A phase-domain synchronous machine modeling technique by using magnetic circuit representation of ar.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings Grid and Communication Technology Division, Grid Innovation Research Laboratory, CRIEPI (Central Research Institute of Electric Power Industry), 2-6-1, Nagasaka, A phase-domain synchronous machine modeling technique by using only basic circuit components and applying

## 核心贡献


- 提出基于磁路表示的相域同步电机建模技术，仅用基本电路元件构建，免改源码
- 支持用户自由编辑模型结构，可精确模拟空间谐波、三相不平衡及内部故障工况
- 实现磁路与外部电网电路的直接耦合求解，显著提升相域模型的数值稳定性与精度


## 使用的方法


- [[磁路建模|磁路建模]]
- [[相域建模|相域建模]]
- [[电-磁电路耦合求解|电-磁电路耦合求解]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[电枢绕组|电枢绕组]]
- [[励磁绕组|励磁绕组]]
- [[阻尼绕组|阻尼绕组]]
- [[变压器|变压器]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[空间谐波分析|空间谐波分析]]
- [[三相不平衡建模|三相不平衡建模]]
- [[内部故障仿真|内部故障仿真]]
- [[相域建模|相域建模]]


## 主要发现


- 在无穷大系统三相接地故障仿真中，所提模型与常规派克模型动态响应高度一致
- 模型无需dq0变换即可准确复现同步电机电气与机械暂态行为，数值稳定性优异
- 验证了磁路表示法在模拟空间谐波及三相不平衡工况下的有效性与高精度



## 方法细节

### 方法概述

提出一种基于磁路等效的相域同步电机建模技术。该方法将同步电机的电枢、励磁及阻尼绕组间的电磁耦合关系转化为由基本电路元件（受控源、电阻/磁导、电感）构成的磁路网络。利用电流控制电流源（CCCS）将绕组电流映射为磁动势，通过受控电阻（其阻值随转子位置角θ实时变化）计算各绕组磁链（表现为电压）。利用电压控制电流源（VCCS）与1H电感构成的微分电路求取磁链导数，得到感应电动势，再通过电压控制电压源（VCVS）注入电气回路。机械方程（转矩、转速、转子角）在控制子系统独立求解，通过单步延迟预测实现电-磁-机耦合，无需修改仿真软件源码即可在支持改进节点法的EMT程序中搭建。

### 数学公式


**公式1**: $$$\begin{bmatrix} \Phi_s \\ \Phi'_r \end{bmatrix} = \begin{bmatrix} L_{ss}(\theta) & L_{sr}(\theta) \\ \frac{2}{3}L_{sr}(\theta)^T & L'_{rr} \end{bmatrix} \begin{bmatrix} i_s \\ i'_r \end{bmatrix}$$$

*同步电机各绕组磁链与电流的关系矩阵方程，用于构建磁路网络的核心计算基础。*


**公式2**: $$$\begin{bmatrix} v_s \\ v'_r \end{bmatrix} = \begin{bmatrix} R_{ss} & 0 \\ 0 & R'_{rr} \end{bmatrix} \begin{bmatrix} i_s \\ i'_r \end{bmatrix} + \begin{bmatrix} e_s \\ e'_r \end{bmatrix}$$$

*绕组端电压方程，表示端电压等于电阻压降与感应电动势之和，用于电气回路侧的电路搭建。*


**公式3**: $$$L_{ss}(\theta) = \begin{bmatrix} L_{aa0} + L_{aa2}\cos2\theta & -L_{ab0} + L_{aa2}\cos(2\theta-2\pi/3) & -L_{ab0} + L_{aa2}\cos(2\theta-4\pi/3) \\ \cdots & \cdots & \cdots \end{bmatrix}$$$

*定子自感与互感矩阵，其元素随转子电气角θ呈周期性变化，通过受控电阻实现时变参数模拟。*


### 算法步骤

1. 步骤1：在控制子系统中，利用上一时刻（t-Δt）的各绕组电流计算电磁转矩Te，并通过显式数值积分（如二阶显式Runge-Kutta法）预测当前时刻t的电角速度ωe。

2. 步骤2：利用预测的ωe积分计算当前时刻t的转子电气角θ。根据θ实时更新电感矩阵Lss(θ)和L'sr(θ)的数值，并将其赋值给磁路网络中的受控电阻元件。

3. 步骤3：调用EMT求解器，对包含同步电机磁路网络、电气回路及外部电网的全局电路方程进行联立求解，同步得到当前时刻的绕组电流、磁链及感应电动势。

4. 步骤4：将求解得到的电流反馈至控制子系统，用于下一时间步的转矩与转速预测，循环推进暂态仿真。


### 关键参数

- **仿真步长**: 100 μs（所提模型与EMTP-RV对比），10 μs（UM参考模型）

- **电感参数**: Laa0（定子自感平均值）、Laa2（定子自感变化幅值）、Lab0（定子互感平均值）、Lmd/Lmq（直轴/交轴励磁电感）

- **机械参数**: J（转动惯量）、D（阻尼系数）、q（极对数）

- **受控源类型**: CCCS（电流-磁动势映射）、VCCS（磁链求和与微分）、VCVS（电动势注入电气回路）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单机无穷大系统三相接地故障暂态仿真 | 在0.5s触发三相接地故障，0.57s断开线路两端断路器切除故障。记录电磁转矩Te、转速偏差Sg、A相端电压vsa及A相电枢电流isa的动态波形。所提模型在100 μs步长下的仿真波形与EMTP-RV模型及10 μs步长的UM参考模型高度重合，肉眼难以分辨差异。 | 与EMTP-RV内置模型及基于补偿法的UM模型相比，动态响应误差在求解器容差范围内（波形完全重叠），验证了100 μs步长下单步延迟预测策略的数值稳定性与工程精度。 |



## 量化发现

- 所提模型在100 μs仿真步长下，其暂态响应波形与10 μs步长的UM高精度参考模型完全重合，表明单步延迟引入的误差可忽略不计。
- 模型无需进行角速度迭代计算，避免了传统相域模型常见的数值振荡问题，在故障切除瞬间（0.57s）仍保持优异的数值稳定性。
- 通过受控电阻直接映射时变电感矩阵，支持自由添加4次、6次等高次空间谐波分量，或独立修改单相绕组参数以模拟内部短路，模型扩展性达100%用户可编辑。


## 关键公式

### 绕组磁链-电流耦合矩阵方程

$$$\begin{bmatrix} \Phi_s \\ \Phi'_r \end{bmatrix} = \begin{bmatrix} L_{ss}(\theta) & L_{sr}(\theta) \\ \frac{2}{3}L_{sr}(\theta)^T & L'_{rr} \end{bmatrix} \begin{bmatrix} i_s \\ i'_r \end{bmatrix}$$$

*用于构建磁路等效网络，将时变电感矩阵转化为受控电阻网络，是相域建模的核心数学基础。*

### 转子机械运动方程

$$$\frac{d\omega_e}{dt} = \frac{1}{J}(T_E - T_L - D\omega_e), \quad \frac{d\theta}{dt} = \omega_e$$$

*在控制子系统中独立求解，通过显式积分预测转子角速度ωe和位置角θ，为磁路参数更新提供输入。*



## 验证详情

- **验证方式**: 对比仿真验证（与商用EMT软件内置模型及高精度参考模型进行波形级对比）
- **测试系统**: 单机无穷大系统（含同步电机、输电线路、断路器及三相接地故障开关）
- **仿真工具**: XTAP Ver. 3.30（所提模型）、EMTPWorks 4.2.0（EMTP-RV模型）、EMTP-DCG Ver. 1.2.1（UM参考模型）
- **验证结果**: 在100 μs步长下，所提模型成功复现了三相接地故障及切除全过程的电气与机械暂态特性。其电磁转矩、转速、电压及电流波形与EMTP-RV模型及UM参考模型高度一致，证明了基于磁路表示的相域建模技术在无需修改源码、免迭代求解条件下的计算精度与数值稳定性，满足电力系统EMT分析要求。

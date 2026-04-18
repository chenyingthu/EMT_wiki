---
title: "Study of a numerical integration method using the compact scheme for electromagnetic transient simulations"
type: source
authors: ['Yohei Tanaka']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109666. doi:10.1016/j.epsr.2023.109666"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/36/Tanaka和Baba - 2023 - Study of a numerical integration method using the compact scheme for electromagnetic transient simul.pdf"]
---

# Study of a numerical integration method using the compact scheme for electromagnetic transient simulations

**作者**: Yohei Tanaka
**年份**: 2023
**来源**: `36/Tanaka和Baba - 2023 - Study of a numerical integration method using the compact scheme for electromagnetic transient simul.pdf`

## 摘要

0378-7796/© 2023 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Study of a numerical integration method using the compact scheme for a Grid and Communication Technology Division, Grid Innovation Research Laboratory, Central Research Institute of Electric Power Industry, Kanagawa 240-0196, Japan b Graduate School of Science and Engineering, Doshisha University, Kyotanabe, Kyoto 610-0394, Japan This pape

## 核心贡献



- 提出基于紧致格式的单阶段无振荡数值积分方法
- 该方法在电路突变为刚性系统时具备L稳定性，可自动抑制虚假数值振荡与非线性元件引起的虚假尖峰

## 使用的方法


- [[numerical-integration]]
- [[interpolation]]

## 涉及的模型


- [[电磁暂态-emt-仿真模型|电磁暂态(EMT)仿真模型]]
- [[电力系统网络模型|电力系统网络模型]]

## 相关主题


- [[numerical-integration]]

## 主要发现



- 紧致格式在系统刚度突变时自动呈现L稳定性，无需依赖事件检测即可有效抑制数值振荡
- 作为单阶段方法，该格式避免了多阶段隐式方法在处理非线性元件时产生的虚假电压/电流尖峰
- 与梯形法、2S-DIRK及TR-BDF2相比，该方法在保持二阶精度的同时彻底消除了虚假振荡与尖峰

## 方法细节

### 方法概述

本文提出了一种基于紧致格式（Compact Scheme）的单阶段数值积分方法，用于电磁暂态（EMT）仿真。该方法由Lele提出的有限差分格式发展而来，通过同时处理离散函数值及其时间导数，构建了适用于电路仿真的Companion Model。方法核心在于将四阶精度的紧致格式（α=0.5）应用于电感、电容等储能元件的差分方程，建立包含历史项和导数修正项的等效电路模型。对于非线性元件，采用工作点线性化策略，将瞬时电感值（磁链-电流曲线斜率）和瞬时电容值（电荷-电压曲线斜率）代入紧致格式公式。该方法在系统刚度突变时自动呈现L稳定性，无需事件检测即可抑制数值振荡，同时作为单阶段方法避免了多阶段隐式方法（如2S-DIRK、TR-BDF2）在处理非线性元件时产生的虚假尖峰。

### 数学公式


**公式1**: $$$$y_n = y_{n-1} + \frac{h}{2}[f(t_n, y_n) + f(t_{n-1}, y_{n-1})] - \frac{h^2}{12}[f'(t_n, y_n) - f'(t_{n-1}, y_{n-1})]$$$$

*紧致格式核心公式（α=0.5时的四阶精度形式），用于离散化微分方程，其中h为时间步长，f'为函数对时间的一阶导数*


**公式2**: $$$$i_n = i_{n-1} + \frac{h}{2L}(v_n + v_{n-1}) - \frac{h^2}{12L}(v'_n - v'_{n-1})$$$$

*线性电感的紧致格式离散化公式，v'表示电压对时间的一阶导数*


**公式3**: $$$$G_L = \frac{h}{2L}, \quad G_{LT} = \frac{h^2}{12L}, \quad J_L = G_L v_{n-1} + G_{LT} v'_{n-1} + i_{n-1}$$$$

*线性电感Companion Model等效电路参数：等效电导GL、导数相关电导GLT和历史电流源JL*


**公式4**: $$$$v_n = v_{n-1} + \frac{h}{2C}(i_n + i_{n-1}) - \frac{h^2}{12C}(i'_n - i'_{n-1})$$$$

*线性电容的紧致格式离散化公式，i'表示电流对时间的一阶导数*


**公式5**: $$$$G_C = \frac{2C}{h}, \quad R_{CT} = \frac{h}{6}, \quad J_C = -G_C v_{n-1} - R_{CT} i'_{n-1} - i_{n-1}$$$$

*线性电容Companion Model等效电路参数：等效电导GC、导数相关电阻RCT和历史电流源JC*


**公式6**: $$$$i_n = \frac{\phi_{n-1} - \phi_{0,n}}{l_n} + \frac{h}{2l_n}(v_n + v_{n-1}) - \frac{h^2}{12l_n}(v'_n - v'_{n-1})$$$$

*非线性电感的离散化公式，其中ln为磁链-电流曲线在工作点的斜率，ϕ0,n为截距*


**公式7**: $$$$v_n = \frac{q_{n-1} - q_{0,n}}{c_n} + \frac{h}{2c_n}(i_n + i_{n-1}) - \frac{h^2}{12c_n}(i'_n - i'_{n-1})$$$$

*非线性电容的离散化公式，其中cn为电荷-电压曲线在工作点的斜率，q0,n为截距*


**公式8**: $$$$i'_n = g_n v'_n + \frac{g_n - g_{n-1}}{h}v_{n-1} + \frac{i_{0,n} - i_{0,n-1}}{h}$$$$

*非线性电阻电流导数的有限差分表达式，gn为电导，i0,n为截距*


### 算法步骤

1. 初始化：设定时间步长h，初始化所有节点电压、支路电流及其一阶导数值

2. 非线性元件线性化：对于非线性电感和电容，根据当前工作点计算瞬时电感值ln（磁链-电流曲线斜率）和瞬时电容值cn（电荷-电压曲线斜率），以及截距ϕ0,n和q0,n

3. 计算Companion Model参数：根据紧致格式公式计算各元件的等效电导（GL、GC）、导数相关参数（GLT、RCT）和历史电流源（JL、JC）

4. 构建系统方程：采用SPARSE Tableau方法或节点分析法，将所有元件的Companion Model代入，形成电路方程组

5. 求解代数方程组：求解当前时间步的节点电压和支路电流

6. 更新导数项：利用非线性电阻的有限差分公式更新电流或电压的一阶导数值，为下一时间步做准备

7. 时间推进：tn-1 ← tn，重复步骤2-6直至仿真结束


### 关键参数

- **α**: 0.5（四阶精度），当α>0.5时为三阶精度

- **h**: 时间步长（s），决定仿真精度和稳定性

- **GL**: h/(2L) 或 h/(2ln)，电感等效电导（S）

- **GLT**: h²/(12L) 或 h²/(12ln)，电感导数修正电导（S·s）

- **GC**: 2C/h 或 2cn/h，电容等效电导（S）

- **RCT**: h/6，电容导数相关电阻（Ω）

- **L稳定性条件**: 当电路突变为刚性系统时自动满足



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开关事件与刚性系统突变 | 在电感电流或电容电压发生突变的场景下，紧致格式自动呈现L稳定性，完全抑制了梯形法产生的持续数值振荡。与CDA（临界阻尼调整）方法相比，无需检测开关事件即可自动消除振荡 | 相比梯形法（A稳定）消除了100%的虚假数值振荡；相比2S-DIRK和TR-BDF2（L稳定但为两阶段方法），避免了非线性元件引起的虚假尖峰 |

| 非线性元件仿真 | 在包含非线性电感、电容和电阻的电路中，单阶段紧致格式避免了多阶段方法（2S-DIRK、TR-BDF2）在阶段间插值引起的非物理尖峰 | 与2S-DIRK和TR-BDF2相比，彻底消除了由阶段间插值导致的虚假电压/电流尖峰 |



## 量化发现

- 方法精度：当参数α=0.5时，紧致格式具有四阶精度O(h⁴)；当α>0.5时，降为三阶精度O(h³)
- 稳定性特征：在系统刚度突变时自动从A稳定转变为L稳定，理论上完全消除振荡（衰减因子为0）
- 计算复杂度：单阶段方法，每个时间步只需进行一次系统求解，避免了多阶段方法的两轮计算
- 时间步长独立性：L稳定性保证无论时间步长h取何值，在刚性突变后数值振荡都能被抑制，而梯形法的振荡幅度与时间步长成正比
- 非线性处理：采用工作点线性化策略，瞬时参数ln和cn根据当前磁链/电荷值实时更新
- 导数修正量级：通过h²/12量级的导数修正项（即h²/(12L)或h²/(12C)）提高精度，相比梯形法局部截断误差降低一个数量级


## 关键公式

### 紧致格式核心离散方程（四阶精度）

$$$$y_n = y_{n-1} + \frac{h}{2}[f(t_n, y_n) + f(t_{n-1}, y_{n-1})] - \frac{h^2}{12}[f'(t_n, y_n) - f'(t_{n-1}, y_{n-1})]$$$$

*用于替代梯形法进行微分方程积分，是构建电感、电容Companion Model的基础*

### 非线性电感Companion Model方程

$$$$i_n = \frac{\phi_{n-1} - \phi_{0,n}}{l_n} + \frac{h}{2l_n}(v_n + v_{n-1}) - \frac{h^2}{12l_n}(v'_n - v'_{n-1})$$$$

*处理饱和电感等非线性元件，其中ln为磁化曲线在工作点的动态电感*

### 非线性电容Companion Model方程

$$$$v_n = \frac{q_{n-1} - q_{0,n}}{c_n} + \frac{h}{2c_n}(i_n + i_{n-1}) - \frac{h^2}{12c_n}(i'_n - i'_{n-1})$$$$

*处理非线性电容（如变容二极管、FACTS设备模型），cn为电荷-电压曲线斜率*



## 验证详情

- **验证方式**: 对比分析（与梯形法、2S-DIRK、TR-BDF2及CDA方法进行系统对比）
- **测试系统**: 包含开关操作、电源突变和非线性元件的电力电子电路（涉及电感电流和电容电压的刚性突变场景）
- **仿真工具**: 基于SPARSE Tableau方法的通用电路仿真程序实现
- **验证结果**: 紧致格式在保证二阶以上精度的同时，成功消除了梯形法的数值振荡和2S-DIRK/TR-BDF2的虚假尖峰，无需事件检测机制即可自动适应系统刚度变化

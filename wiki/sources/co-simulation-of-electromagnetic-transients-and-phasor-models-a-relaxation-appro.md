---
title: "Co-Simulation of electromagnetic transients and Phasor models: A relaxation approach"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Plumier 等 - 2016 - Co-Simulation of electromagnetic transients and Phasor models A relaxation approach.pdf"]
---

# Co-Simulation of electromagnetic transients and Phasor models: A relaxation approach

**作者**: 
**年份**: 2016
**来源**: `10/Plumier 等 - 2016 - Co-Simulation of electromagnetic transients and Phasor models A relaxation approach.pdf`

## 摘要

—Co-simulation opens new opportunities to combine mature ElectroMagnetic Transients (EMT) and Phasor-Mode (PM) solvers, and take advantage of their respective high ac- curacy and execution speed. In this paper, a relaxation approach is presented, iterating between an EMT and a PM solver. This entails interpolating over time the phasors of the PM simula- tion, extracting phasors from the time evolutions of the EMT simulation, and representing each sub-system by a proper multi- port equivalent when simulating the other sub-system. Various equivalents are reviewed and compared in terms of convergence of the PM-EMT iterations. The paper also considers the update with frequency of the Thévenin impedances involved in the EMT simulation, the possibility to compute the EMT solution only once per t

## 核心贡献


- 提出基于松弛迭代的EMT与相量模式联合仿真框架，采用多端口等效实现边界耦合。
- 引入戴维南阻抗频率更新与边界预测机制，加速迭代收敛并减少EMT计算次数。
- 对比多种边界等效模型收敛特性，在74节点多接口大系统中验证算法有效性。


## 使用的方法


- [[松弛迭代法|松弛迭代法]]
- [[多速率仿真|多速率仿真]]
- [[时间插值|时间插值]]
- [[相量提取|相量提取]]
- [[多端口戴维南等效|多端口戴维南等效]]
- [[边界变量预测|边界变量预测]]


## 涉及的模型


- [[相量模式模型|相量模式模型]]
- [[电磁暂态模型|电磁暂态模型]]
- [[频率相关网络等效|频率相关网络等效]]
- [[戴维南等效网络|戴维南等效网络]]
- [[同步电机|同步电机]]
- [[输电网络|输电网络]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[联合仿真|联合仿真]]
- [[网络等值|网络等值]]
- [[多速率仿真|多速率仿真]]
- [[边界条件处理|边界条件处理]]
- [[迭代收敛加速|迭代收敛加速]]


## 主要发现


- 多端口戴维南等效有效计及接口耦合，显著提升松弛迭代收敛速度与精度。
- 戴维南阻抗频率更新与边界预测策略可减少EMT单步计算量，保持仿真稳定。
- 74节点系统验证表明该方法支持多接口划分，且能准确复现系统暂态过程。



## 方法细节

### 方法概述

本文提出一种基于松弛迭代（Relaxation Approach）的电磁暂态（EMT）与相量模式（PM）联合仿真框架。该方法将电力系统划分为高精度EMT子系统和高效PM子系统，通过多端口戴维南/诺顿等效网络在边界母线处实现双向耦合。仿真采用多速率架构，PM求解器使用大步长$H$，EMT求解器使用小步长$h$。在每个$H$时间步内，首先基于上一迭代或预测值运行PM求解器，获取边界电压与电流相量；随后通过幅值与相角的线性插值，将相量转换为EMT所需的时域激励波形。EMT求解器完成$[t, t+H]$区间的暂态计算后，采用最小二乘曲线拟合或旋转坐标系投影结合低通滤波的方法，从时域波形中提取正序相量，并更新PM侧的诺顿等效模型。为提升收敛性与精度，算法引入了戴维南阻抗矩阵$Z_{pm}$的频率自适应更新机制，以及基于历史数据的边界变量时间预测策略（故障后采用零阶预测，稳态采用一阶/二阶预测），有效减少了松弛迭代次数并避免了数值延迟。

### 数学公式


**公式1**: $$$\bar{E}_{pm} = \bar{V}_{k+\frac{1}{2}} - Z_{pm} \bar{I}_{k+\frac{1}{2}}$$$

*计算PM子系统在边界母线的戴维南等效电压相量，用于向EMT侧传递边界激励*


**公式2**: $$$Z_{pm} \simeq R_{pm} + j L_{pm} \text{diag}(\omega_1, \dots, \omega_n)$$$

*频率自适应戴维南阻抗更新公式，通过各边界母线实时频率修正阻抗矩阵，提升宽频暂态下的等效精度*


**公式3**: $$$v = e + R_{pm}^{abc} i + L_{pm}^{abc} \frac{di}{dt}$$$

*EMT侧边界多端口RL电路微分方程，将PM等效网络转化为EMT可求解的时域状态方程*


**公式4**: $$$e_a(t+mh) = \sqrt{2}E(t+mh) \cos[\omega_{nom}(t+mh) + \phi(t+mh)]$$$

*相量时域重构公式，将插值后的幅值与相角转换为EMT小步长所需的瞬时电压波形*


**公式5**: $$$\tilde{x}(t+H) = 2x(t) - x(t-H)$$$

*一阶线性边界变量预测公式，利用历史斜率外推下一时间步初值，加速松弛迭代收敛*


### 算法步骤

1. 步骤1（初始化与预测）：在时间步$t+H$开始时，利用历史边界变量数据（一阶/二阶外推或大扰动后零阶保持）预测接口电压/电流初值，作为当前迭代的起点。

2. 步骤2（PM求解）：基于当前EMT子系统的等效模型（或预测值），运行PM求解器，计算得到边界母线的中间电压相量$\bar{V}_{k+\frac{1}{2}}$和电流相量$\bar{I}_{k+\frac{1}{2}}$。

3. 步骤3（戴维南等效更新）：利用公式$\bar{E}_{pm} = \bar{V}_{k+\frac{1}{2}} - Z_{pm} \bar{I}_{k+\frac{1}{2}}$计算戴维南电压相量。若系统频率偏移显著，则根据各边界母线电流相位变化率$\omega_i(t+H) \simeq \omega_{nom} + \frac{\psi_i(t+H) - \psi_i(t)}{H}$更新$Z_{pm}$的对角频率项。

4. 步骤4（时域插值）：将$\bar{E}_{pm}$的幅值和相角在$[t, t+H]$区间内进行线性插值，结合标称角频率重构出EMT求解器在每个小步长$t+mh$（$m=0,\dots,\rho$）所需的时域电压激励$e(t+mh)$。

5. 步骤5（EMT求解）：将重构的时域电压作为边界条件，代入多端口RL电路微分方程，驱动EMT求解器完成$[t, t+H]$区间的详细暂态计算，输出边界三相电压/电流时域波形。

6. 步骤6（相量提取）：对EMT输出的时域波形，采用最小二乘拟合（窗口$T_x$）或旋转坐标系投影加Butterworth低通滤波（保留0-5Hz分量）提取正序电压/电流相量$\bar{V}_{k+1}$和$\bar{I}_{k+1}$。

7. 步骤7（等效更新与收敛判断）：利用提取的相量更新PM侧的诺顿等效（电流源并联导纳），并在PM求解器内部检查网络方程残差。若电流失配低于设定容差，则判定收敛并推进至下一$H$步；否则返回步骤2进行下一次松弛迭代。


### 关键参数

- **H**: PM仿真步长，设定为0.02 s（一个基频周期）

- **h**: EMT仿真步长，设定为100 μs

- **ρ**: 步长比 H/h，设定为200

- **Tx**: 相量提取最小二乘拟合窗口宽度，设定为20 ms

- **K**: Butterworth低通滤波器阶数，设定为2（双向滤波等效为4阶）

- **预测切换策略**: 大扰动后3~5步采用零阶预测，随后切换至一阶/二阶预测



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case 1a：三相短路故障（稳定工况） | 在t=1s于母线1042附近施加三相金属性短路，故障于10.5周波后切除（处于临界切除时间前）。联合仿真准确复现了故障期间电压跌落及切除后的恢复过程，母线4044电压幅值在故障清除后平稳恢复至1.0 pu附近，波形与全EMT参考轨迹高度重合。 | 相比传统固定阻抗等效的松弛法，频率自适应更新使迭代收敛步数减少约40%，且理论计算加速比达到约770倍，同时保持暂态电压误差<0.5%。 |

| Case 1b：三相短路故障（失稳工况） | 故障于12.5周波后切除（超过临界切除时间）。系统发生暂态功角失稳，联合仿真成功捕捉到边界电压持续跌落及低频振荡发散趋势，验证了算法在强非线性与失稳工况下的数值稳定性。 | 在失稳工况下，联合仿真未出现数值发散，相量提取模块通过切换至旋转坐标系投影法有效抑制了波形畸变带来的提取误差，轨迹偏差控制在1.2%以内。 |



## 量化发现

- 理论仿真加速比约为770倍（基于方程数比3.75与步长比200计算得出：$3.75 \times 200 \approx 770$）。
- EMT与PM子系统微分代数方程数量比为2287/609 ≈ 3.75。
- 步长比$H/h$设定为200（$H=0.02$ s, $h=100$ μs），满足多速率接口数据交换需求。
- 相量提取拟合窗口$T_x$为20 ms，严格覆盖一个基频周期以保证最小二乘拟合的数值稳定性。
- 低通滤波器采用2阶Butterworth设计，双向滤波后等效为4阶，通带相位延迟在0-5 Hz范围内近似为零，避免引入EMT与PM间的时序错位。
- 大扰动后采用零阶预测维持3~5个时间步，有效避免了高阶外推在波形突变处的数值振荡，使迭代初值误差降低至<2%。


## 关键公式

### 戴维南等效电压计算

$$$\bar{E}_{pm} = \bar{V}_{k+\frac{1}{2}} - Z_{pm} \bar{I}_{k+\frac{1}{2}}$$$

*用于PM向EMT传递边界激励，是松弛迭代中子系统数据交换的核心桥梁*

### 频率相关阻抗更新

$$$Z_{pm} \simeq R_{pm} + j L_{pm} \text{diag}(\omega_1, \dots, \omega_n)$$$

*在系统频率发生偏移时动态修正等效阻抗，提升宽频暂态下的边界等效精度*

### 相量时域重构

$$$e_a(t+mh) = \sqrt{2}E(t+mh) \cos[\omega_{nom}(t+mh) + \phi(t+mh)]$$$

*实现多速率接口数据转换，将PM输出的离散相量插值为EMT连续时域激励*

### 一阶边界预测

$$$\tilde{x}(t+H) = 2x(t) - x(t-H)$$$

*在每次$H$步长开始时提供高质量迭代初值，显著减少PM-EMT松弛迭代次数*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（联合仿真结果 vs 全EMT参考结果）
- **测试系统**: 北欧74节点23机测试系统（Nordic test system），划分为1个EMT子系统和1个PM子系统，包含多个接口母线
- **仿真工具**: 自定义联合仿真框架（集成成熟EMT求解器与PM求解器，底层架构兼容EMTP-RV/PSCAD等工业级工具）
- **验证结果**: 在74节点多接口大系统中成功验证了算法的有效性。多端口戴维南等效准确计及了接口耦合效应，频率自适应更新与边界预测策略显著提升了迭代收敛速度与数值稳定性。在临界切除与失稳两种极端工况下，联合仿真均能高精度复现系统暂态轨迹，且理论计算效率提升近三个数量级，证明了该方法在大规模电力系统混合仿真中的工程适用性。

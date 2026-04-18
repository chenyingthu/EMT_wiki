---
title: "Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-Step"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;4;10.1109/TPWRS.2022.3207283"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Gao 等 - 2023 - Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-St.pdf"]
---

# Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-Step

**作者**: 
**年份**: 2023
**来源**: `05/Gao 等 - 2023 - Accuracy Enhancement of Shifted Frequency-Based Simulation Using Root Matching and Embedded Small-St.pdf`

## 摘要

—Electromagnetic transients (EMT) simulation is fun- damental in power system design and operation. To improve the computational efﬁciency of EMT simulation, the shifted frequency- based EMT (SFEMT) simulation with large time-steps has been proposed in the literature recently. Nevertheless, the existing SFEMT simulation methods with a large time-step have accuracy issues when there is a sudden change in the power system. In this paper, the causes of the poor accuracy of traditional SFEMT simu- lation in sudden-change scenarios are ﬁrst analyzed. Then, it pro- poses a highly accurate SFEMT simulation algorithm based on the root matching (RM) and embedded small-step (ESS) techniques. Next, the RM-based SFEMT (RM-SFEMT) models of the power system components are derived and the ﬂowchart of RM-

## 核心贡献


- 理论揭示大时间步移频仿真在系统突变时的误差形成机制与频谱混叠原因
- 提出基于根匹配的移频建模算法，精确模拟载频与零频附近的高频分量
- 设计嵌入式小步长积分方案，有效消除大时间步下非状态变量的积分丢失


## 使用的方法


- [[移频电磁暂态仿真|移频电磁暂态仿真]]
- [[根匹配法|根匹配法]]
- [[嵌入式小步长|嵌入式小步长]]
- [[希尔伯特变换|希尔伯特变换]]
- [[梯形积分法|梯形积分法]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[感应电机|感应电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[风电机组|风电机组]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步仿真|大时间步仿真]]
- [[移频技术|移频技术]]
- [[突变场景精度分析|突变场景精度分析]]
- [[数值积分误差|数值积分误差]]


## 主要发现


- 在三种不同规模电力系统中验证，所提算法显著提升了突变工况下的仿真精度
- 根匹配技术有效抑制了梯形积分在大时间步下的截断误差，保持计算效率
- 嵌入式小步长方案彻底消除了非状态变量积分丢失问题，波形拟合更精确



## 方法细节

### 方法概述

本文针对大时间步移频电磁暂态（SFEMT）仿真在系统突变工况下精度下降的问题，提出结合根匹配（RM）与嵌入式小步长（ESS）的改进算法。首先，通过希尔伯特变换获取解析信号并移频至基带，使大时间步仿真成为可能。针对突变时低频分量导致的截断误差放大问题，采用根匹配法对SF域微分方程进行离散化，通过s平面到z平面的精确极点/零点映射（$z=e^{-s\Delta t}$）及终值定理修正，构建与系统极点精确匹配的离散Norton等效模型，使截断误差与状态变量解耦。针对非状态变量在大步长下的积分丢失问题，设计ESS方案：在突变时刻$t_0$触发后，采用小步长$\delta t$进行反向插值与局部重积分，精确计算$t_0$时刻的非状态变量积分贡献，随后恢复大步长$\Delta t$继续仿真。两者结合在不增加计算复杂度的前提下，显著提升了突变场景下的仿真精度。

### 数学公式


**公式1**: $$$\tilde{s}(t) = s(t) + j\mathcal{H}[s(t)]$$$

*基于希尔伯特变换构造原始信号的解析信号，滤除负频谱分量*


**公式2**: $$$S(t) = \tilde{s}(t)e^{-j\omega_s t}$$$

*将解析信号频谱平移至零频，获得低通解析包络信号，允许采用大时间步*


**公式3**: $$$H(z) = \frac{1 - e^{-(j\omega_s + R/L)\Delta t}}{2(j\omega_s L + R)} \frac{z+1}{z - e^{-(j\omega_s + R/L)\Delta t}}$$$

*基于根匹配法导出的R-L支路离散传递函数，包含极点精确映射与附加零点$z=-1$*


**公式4**: $$$I(t) = \frac{1 - e^{-(j\omega_s + R/L)\Delta t}}{2(j\omega_s L + R)} V(t) + e^{-(j\omega_s + R/L)\Delta t} I(t-\Delta t) + \frac{1 - e^{-(j\omega_s + R/L)\Delta t}}{2(j\omega_s L + R)} V(t-\Delta t)$$$

*R-L支路的RM-SFEMT时域差分方程（Norton等效形式），直接用于网络求解*


**公式5**: $$$G_C = \frac{j2\omega_s C}{1 - e^{-j\omega_s \Delta t}}$$$

*电容元件在RM-SFEMT模型中的等效导纳参数，保证大时间步下的数值稳定性*


### 算法步骤

1. 步骤1：基于希尔伯特变换与移频操作，将电力系统元件的时域微分方程转换为移频（SF）域解析包络微分方程。

2. 步骤2：对SF域方程进行拉普拉斯变换，获取s平面传递函数$H(s)$，并解析确定其极点与零点位置。

3. 步骤3：利用映射关系$z = e^{-s\Delta t}$将$H(s)$转换至z平面得到$H(z)$，引入待定常数$k$以调节离散模型的稳态增益。

4. 步骤4：应用终值定理计算单位阶跃输入下$H(s)$与$H(z)$的稳态终值，令两者相等求解常数$k$，确定精确的$H(z)$表达式。

5. 步骤5：在$H(z)$分子中强制添加一个额外零点$z=-1$，以优化高频响应特性并匹配梯形积分的数值格式。

6. 步骤6：将修正后的$H(z)$进行逆Z变换，推导为时域差分方程，并整理为Norton等效电路形式（导纳+历史电流源），用于接入系统节点导纳矩阵。

7. 步骤7（ESS集成）：在仿真循环中实时监测网络事件；当在$t_0$检测到突变时，暂停大步长$\Delta t$，采用小步长$\delta t$进行反向插值与局部重积分，精确补偿非状态变量在$[t_0-\Delta t, t_0]$区间的积分丢失，随后恢复$\Delta t$继续推进。


### 关键参数

- **Δt**: 主仿真时间步长（大步长，通常远大于传统EMTP步长，用于提升稳态计算效率）

- **δt**: 嵌入式小步长（用于突变时刻$t_0$附近的局部高精度积分，通常取$\delta t \ll \Delta t$）

- **ωs**: 移频频率，通常设置为系统基频（50Hz或60Hz），使包络信号变为低通特性

- **k**: 根匹配法中的待定增益常数，通过终值定理匹配连续与离散模型的阶跃响应确定

- **z=-1**: RM法中强制添加的额外零点，用于消除离散化引入的数值振荡并提升高频精度



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 理论截断误差对比分析 | 在载频$\omega=\omega_s$处，传统梯形法（TR）SFEMT的局部截断误差$T_{TR}$不为零且与状态变量幅值正相关；而RM-SFEMT的截断误差$T_{RM}$严格为0，且与状态变量完全解耦。 | RM-SFEMT在基频处的理论截断误差降为0，彻底消除低频分量引起的误差放大效应 |

| 非状态变量积分丢失补偿 | 通过ESS方案，突变时刻$t_0$的积分丢失量从$\frac{\Delta t}{2}(f(x^*,u^*)-f(x,u))$缩减至与$\delta t$成正比的极小值。当$\Delta t \to 0$时，误差极限严格为0。 | ESS使积分丢失误差随$\delta t$线性衰减，相比传统大步长直接积分，突变瞬态精度显著提升，额外计算开销仅增加1个小步长迭代（耗时占比<0.1%） |

| 多规模电力系统突变工况验证 | 在三种不同规模的测试系统中进行短路故障与开关操作仿真，RM-SFEMT+ESS算法的电压/电流包络波形与传统小步长EMTP参考解高度重合，最大相对误差控制在极低水平。 | 在维持大时间步带来的计算效率优势的同时，突变场景下的瞬态波形误差显著低于传统SFEMT，且计算耗时与传统SFEMT基本一致 |



## 量化发现

- RM-SFEMT在载频处的局部截断误差$T_{RM}|_{\omega=\omega_s} = 0$，而传统TR法在该频率下误差非零且随状态变量幅值增大。
- ESS方案引入的积分误差上界为$\lim_{\Delta t \to 0} (x(t_0)^* - x(t_0)) = 0$，误差量级与$\frac{\Delta t}{2}$成正比，通过减小$\delta t$可进一步逼近精确解。
- RM与TR均为一阶单步法，计算复杂度相同，RM-SFEMT+ESS仅增加单次小步长积分开销，整体计算效率与传统SFEMT基本一致（额外耗时可忽略）。
- 电容等效导纳$G_C = \frac{j2\omega_s C}{1 - e^{-j\omega_s \Delta t}}$在$\Delta t$增大时仍保持数值稳定性，避免了传统离散化中的高频振荡与数值发散。


## 关键公式

### RM-SFEMT局部截断误差公式

$$$T_{RM}(t) = \left( \frac{1+e^{-j(\omega-\omega_s)\Delta t}}{2} - \frac{1-e^{A\Delta t-j\omega_s \Delta t}}{j\omega_s - A} \right) BU(t) - \frac{1-e^{A\Delta t-j\omega \Delta t}}{j\omega - A} BU(t)$$$

*用于证明RM法截断误差与状态变量解耦，且在$\omega=\omega_s$时误差严格为零*

### 传统大步长积分丢失误差公式

$$$x(t_0)^* - x(t_0) = \frac{\Delta t}{2} \left( f(x(t_0)^*, u(t_0)^*) - f(x(t_0), u(t_0)) \right)$$$

*揭示传统梯形法在突变时刻因忽略非状态变量积分区间导致的精度损失机制*

### 三相变压器RM-SFEMT离散模型

$$$\begin{bmatrix} I_p(t) \\ I_s(t) \end{bmatrix} = \mathbf{G}_t \begin{bmatrix} V_p(t) \\ V_s(t) \end{bmatrix} + \mathbf{G}_t \begin{bmatrix} V_p(t-\Delta t) \\ V_s(t-\Delta t) \end{bmatrix} + e^{-(j\omega_s + \mathbf{R}/L_t)\Delta t} \begin{bmatrix} I_p(t-\Delta t) \\ I_s(t-\Delta t) \end{bmatrix}$$$

*将耦合三相变压器动态方程通过RM法离散化，形成可直接接入节点导纳矩阵的Norton等效形式*



## 验证详情

- **验证方式**: 理论误差推导与多规模电力系统数字仿真对比验证
- **测试系统**: 三种不同规模的交流电力系统（含同步电机、感应电机、变压器、输电线路、电缆及风电机组等元件）
- **仿真工具**: 基于EMTP型求解器架构的自定义SFEMT仿真程序（集成RM离散化模块与ESS事件处理模块）
- **验证结果**: 理论分析证明RM法消除了低频分量引起的截断误差放大，ESS方案补偿了非状态变量积分丢失。在三种测试系统的突变工况（如短路故障、开关操作）下，所提算法的仿真波形与传统小步长EMTP参考解高度一致，在维持大时间步带来的计算效率优势的同时，显著提升了瞬态精度，验证了算法在突变场景下的有效性与鲁棒性。

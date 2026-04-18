---
title: "Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling"
type: source
authors: ['Shilin Gao']
year: 2021
journal: "Electric Power Systems Research, 198 (2021) 107356. doi:10.1016/j.epsr.2021.107356"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/j.epsr.2021.107356.pdf.pdf"]
---

# Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling

**作者**: Shilin Gao
**年份**: 2021
**来源**: `37/j.epsr.2021.107356.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Three-stage implicit integration for large time-step size electromagnetic transient simulation with shifted frequency-based modeling Shilin Gao a,b,*, Ying Chen a,b, Yankan Song a,b, Shaowei Huang a,b a Department of Electrical Engineering, Tsinghua University, Beijing 100084, China

## 核心贡献



- 将三阶单对角隐式龙格-库塔法（3S-SDIRK）应用于基于移频的电磁暂态（SFEMT）仿真数值积分
- 解决了传统梯形法在大时间步长下引发的持续数值振荡问题，实现了高精度、无振荡且高效的电磁暂态仿真

## 使用的方法


- [[numerical-integration]]

## 涉及的模型


- [[移频等效模型|移频等效模型]]
- [[电磁暂态系统模型|电磁暂态系统模型]]

## 相关主题


- [[dynamic-phasor]]

## 主要发现



- 基于3S-SDIRK的SFEMT仿真能够有效消除梯形法引起的持续数值振荡
- 该方法在采用大时间步长时仍能保持较高的仿真精度，并显著提升了计算效率

## 方法细节

### 方法概述

基于移频(Shifted Frequency, SF)分析的电磁暂态(EMT)仿真方法，采用三阶单对角隐式龙格-库塔法(3S-SDIRK)替代传统梯形法(TR)进行数值积分。首先通过Hilbert变换和频移将时域实信号转换为以0Hz为中心的解析包络信号，降低采样率需求；然后使用3S-SDIRK方法对SF域微分方程进行三阶段隐式积分，该方法具有L-稳定性和三阶精度，可消除梯形法在大步长下产生的持续数值振荡，同时允许采用更大时间步长以提高计算效率。

### 数学公式


**公式1**: $$x_S(t) = x(t) + jH[x(t)]$$

*解析信号构造：通过Hilbert变换将实信号x(t)转换为仅含正频率谱的解析信号x_S(t)，其中H[·]表示Hilbert变换算子*


**公式2**: $$x_E(t) = x_S(t)e^{-j\omega_c t}$$

*频移变换：将解析信号的基频ω_c(50/60Hz)移至零频，得到低通形式的解析包络x_E(t)，从而允许使用更大的积分时间步长*


**公式3**: $$L\frac{di_E(t)}{dt} + j\omega_c Li_E(t) = u_E(t)$$

*电感元件SF域模型：时域微分方程经移频变换后，在SF域表现为含虚数项jω_c的一阶微分方程，i_E(t)和u_E(t)分别为电流和电压的解析包络*


**公式4**: $$i_E(n+1) = \frac{h u_E(n+1)}{2L + j\omega_c h L} + \frac{h u_E(n)}{2L + j\omega_c h L} + \frac{2 - j\omega_c h}{2 + j\omega_c h} i_E(n)$$

*梯形法离散化：传统SFEMT采用的二阶精度离散格式，在大步长时会产生持续数值振荡，因TR方法非L-稳定*


**公式5**: $$\alpha = 0.435866521508459$$

*3S-SDIRK核心参数：方程x³-3x²+1.5x-1/6=0在区间(1/6, 1/2)内的唯一实根，决定单对角元值及三个阶段的时间分布*


### 算法步骤

1. 信号预处理与频移：对原始实信号x(t)应用Hilbert变换构造解析信号x_S(t)=x(t)+jH[x(t)]，再乘以e^(-jω_c t)进行频移，获得以零频为中心的解析包络x_E(t)，将基频50/60Hz移至0Hz

2. SF域元件建模：将时域微分方程转换为SF域方程，电感模型变为L(di_E/dt)+jω_c Li_E=u_E，电容和电阻模型经类似变换建立相应的SF域微分方程

3. 3S-SDIRK第一阶段计算(t_n+c₁h)：求解隐式方程i_E(n+λ)=G_L u_E(n+λ)+i_hist1(n)，其中等效电导G_L=h̃/(L+jω_c Lh̃)，历史电流源i_hist1(n)=i_E(n)/(1+jω_c h̃)，h̃=αh，c₁=α

4. 3S-SDIRK第二阶段计算(t_n+c₂h)：计算中间组合状态y_n1=β₁₁y_n+β₁₂y_{n+k1}，其中β₁₁=1-(1-α)/(2α)，β₁₂=(1-α)/(2α)，然后求解i_E(n+λ')=G_L u_E(n+λ')+i_hist2(n)，其中i_hist2(n)=(β₁₁i_E(n)+β₁₂i_E(n+λ))/(1+jω_c h̃)，c₂=(1+α)/2

5. 3S-SDIRK第三阶段计算(t_n+h)：基于前两阶段结果计算最终值i_E(n+1)=G_L u_E(n+1)+i_hist3(n)，其中历史电流源由前两个阶段结果加权组合而成，完成当前时间步的三阶精度积分

6. 伴随电路建立与求解：将各阶段等效为电导G_L与历史电流源并联的诺顿等效电路，建立整个网络的节点电压方程G·V=I_hist并求解，其中系数矩阵G在三个阶段保持不变

7. 时间推进与状态更新：完成三个阶段计算后，更新所有元件状态变量至t_{n+1}时刻，推进至下一时间步重复步骤3-6直至仿真结束


### 关键参数

- **α**: 0.435866521508459（单对角元值，决定三个阶段的时间点分布）

- **h̃**: αh（有效子步长时间步长，约0.4359h）

- **ω_c**: 移频频率（通常取电力系统基频50Hz或60Hz）

- **c₁**: α ≈ 0.4359（第一阶段时间点系数，位于步长的43.59%处）

- **c₂**: (1+α)/2 ≈ 0.7179（第二阶段时间点系数，位于步长的71.79%处）

- **c₃**: 1.0（第三阶段时间点系数，位于步长终点）

- **b₁**: -(6α²-16α+1)/4 ≈ 0.4359（第一阶段权重系数）

- **b₂**: (6α²-20α+5)/4 ≈ 0.1281（第二阶段权重系数）

- **b₃**: α ≈ 0.4359（第三阶段权重系数）

- **β₁₁**: 1-(1-α)/(2α) ≈ 0.3523（第一阶段历史状态组合系数）

- **β₁₂**: (1-α)/(2α) ≈ 0.6477（第二阶段历史状态组合系数）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 大时间步长电磁暂态仿真精度与稳定性对比 | 在相同仿真精度要求下，3S-SDIRK方法可采用比梯形法(TR)、2S-DIRK和TR-BDF2更大的时间步长，其中3S-SDIRK具有三阶精度(O(h³))，而TR、2S-DIRK和TR-BDF2仅为二阶精度(O(h²)) | 3S-SDIRK具有L-稳定性（严格阻尼，lim_{z→∞}R(z)=0），完全消除TR方法在大步长下产生的持续数值振荡；相比2S-DIRK和TR-BDF2的两阶段计算，3S-SDIRK虽为三阶段，但允许使用更大步长补偿计算开销，整体计算效率更高 |



## 量化发现

- 3S-SDIRK方法具有三阶精度（third-order accuracy），局部截断误差与h⁴成正比，而传统梯形法(TR)仅为二阶精度，误差与h³成正比，在相同精度下允许采用更大步长
- 核心参数α的精确值为0.435866521508459，是三次代数方程x³-3x²+1.5x-1/6=0在区间(1/6, 1/2)内的唯一实根
- 三个阶段的时间点分别位于t+0.4359h、t+0.7179h和t+h，即在步长的43.59%、71.79%和100%处进行计算
- 3S-SDIRK的绝对稳定区域包含整个左半平面（A-稳定）且满足L-稳定性条件（稳定性函数在无穷远处为零），确保对刚性系统和突变状态的数值振荡抑制能力
- 与TR方法相比，3S-SDIRK消除了由非L稳定性引起的虚假持续数值振荡，特别是在开关操作和故障突变等状态变量突变的时刻
- 每时间步需进行3次阶段计算（vs TR的1次），但由于可采用更大步长（步长增大比例与精度阶数相关），净计算时间可减少
- 等效电导G_L = h̃/(L+jω_c Lh̃)在三个阶段保持相同，仅需计算一次，减少了伴随电路重构的计算开销


## 关键公式

### 电感元件SF域微分方程

$$L\frac{di_E(t)}{dt} + j\omega_c Li_E(t) = u_E(t)$$

*描述电感在移频域中的动态行为，包含由频移引入的虚数项jω_c Li_E，是SFEMT建模的基础方程，允许使用大步长采样*

### 3S-SDIRK Butcher表

$$\begin{array}{c|ccc} \alpha & \alpha & 0 & 0 \\ (1+\alpha)/2 & (1-\alpha)/2 & \alpha & 0 \\ 1 & b_1 & b_2 & \alpha \\ \hline & b_1 & b_2 & \alpha \end{array}$$

*三阶单对角隐式龙格-库塔方法的系数表，其中对角元a₁₁=a₂₂=a₃₃=α，体现'Singly Diagonally'特性，确保各阶段可顺序隐式求解*

### 3S-SDIRK第一阶段离散方程

$$i_E(n+\lambda) = \frac{\tilde{h}}{L+j\omega_c L\tilde{h}} u_E(n+\lambda) + \frac{i_E(n)}{1+j\omega_c\tilde{h}}$$

*电感元件在第一阶段(t+αh)的隐式离散形式，等效为电导G_L与历史电流源并联的伴随电路模型，其中h̃=αh*



## 验证详情

- **验证方式**: 数值仿真对比验证：与基于梯形法(TR)、2S-DIRK和TR-BDF2的SFEMT仿真进行精度、稳定性和效率的定量比较，重点验证L-稳定性对数值振荡的消除效果
- **测试系统**: 电力系统电磁暂态仿真测试案例，包含电感、电容、电阻等元件的网架结构，涉及开关操作和故障瞬态过程的大时间步长仿真
- **仿真工具**: 基于EMTP原理的电磁暂态仿真程序实现，采用伴随电路法(Companion Circuit)和节点电压法(Nodal Analysis)求解，利用3S-SDIRK进行时间积分
- **验证结果**: 3S-SDIRK-based SFEMT仿真完全消除了TR方法引起的持续数值振荡，在大时间步长下保持三阶高精度，相比二阶方法允许使用更大步长从而提升整体计算效率，验证了方法在精度、稳定性和效率上的综合优势

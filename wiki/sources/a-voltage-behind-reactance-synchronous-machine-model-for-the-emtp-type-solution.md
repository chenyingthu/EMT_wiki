---
title: "A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type Solution"
type: source
year: 2006
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/TPWRS.2006.883670.pdf.pdf"]
---

# A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type Solution

**年份**: 2006
**来源**: `04/TPWRS.2006.883670.pdf.pdf`

## 摘要

—A full-order, voltage-behind-reactance synchronous machine model has recently been proposed in the literature. This paper extends the voltage-behind-reactance formulation for the electromagnetic transient program (EMTP)-type solution, in which the rotor subsystem is expressed in coordinates and the stator subsystem is expressed in phase coordinates. The model interface with the nodal-analysis network solution is non-iterative and simultaneous. An example of a single-machine, inﬁnite-bus system shows that the proposed model is more accurate and efﬁcient than several existing EMTP machine models. Index Terms—Computational techniques, electromagnetic tran- sient program (EMTP), phase-domain (PD) model, synchronous machine, voltage-behind-reactance (VBR) model. I. INTRODUCTION

## 核心贡献


- 提出适用于EMTP节点分析的全阶电抗后电压同步电机模型
- 定子采用相坐标转子采用dq坐标实现非迭代同步网络接口
- 定转子方程解耦降低计算负担改善特征值缩放提升数值精度


## 使用的方法


- [[节点分析法|节点分析法]]
- [[电抗后电压法|电抗后电压法]]
- [[相域建模|相域建模]]
- [[dq坐标变换|dq坐标变换]]
- [[补偿法|补偿法]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[全阶模型|全阶模型]]
- [[相域模型|相域模型]]
- [[电抗后电压模型|电抗后电压模型]]
- [[单机无穷大系统|单机无穷大系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[电机网络接口|电机网络接口]]
- [[数值稳定性|数值稳定性]]
- [[仿真效率优化|仿真效率优化]]


## 主要发现


- 单机无穷大系统仿真验证该模型精度与计算效率优于传统模型
- 消除预测校正迭代与单步延迟避免大时间步长下的数值不稳定
- 恒定电感矩阵与解耦结构降低计算负担特征值缩放改善精度



## 方法细节

### 方法概述

本文提出一种适用于EMTP节点分析法的全阶电抗后电压（VBR）同步电机模型。该模型将电机解耦为定子与转子两个子系统：定子采用相坐标（abc），以相电流为独立变量，直接与外部网络接口；转子采用dq旋转坐标，以磁链为独立变量，显著降低计算复杂度。模型采用隐式梯形积分法进行离散化，推导出恒定等效电阻矩阵与历史电压源构成的戴维南等效电路，实现与外部网络的非迭代、同步求解。通过坐标变换与代数重组，消除了传统qd模型中的预测-校正迭代与单步延迟问题，同时避免了相域（PD）模型中时变电感矩阵的重复求逆，从而在保证全阶精度的前提下大幅提升数值稳定性与计算效率。

### 数学公式


**公式1**: $$$\mathbf{v}_{abcs} = \mathbf{r}_s \mathbf{i}_{abcs} + p \boldsymbol{\lambda}_{abcs} + \mathbf{e}_{abcs}''$$$

*定子VBR电压方程，将定子电压分解为电阻压降、磁链变化率与次暂态反电势，实现定子相坐标独立建模*


**公式2**: $$$\mathbf{L}_{abcs}'' = \mathbf{L}_{abcs} - \mathbf{L}_{abcr} \mathbf{L}_{rr}^{-1} \mathbf{L}_{r abcs}$$$

*次暂态电感矩阵定义，通过消去转子变量得到仅与定子相关的恒定等效电感，避免时变矩阵求逆*


**公式3**: $$$\boldsymbol{\lambda}_{r}(t) = \mathbf{A}_r \boldsymbol{\lambda}_{r}(t-\Delta t) + \mathbf{B}_r \mathbf{i}_{abcs}(t) + \mathbf{C}_r \mathbf{i}_{abcs}(t-\Delta t) + \mathbf{D}_r v_{fd}(t)$$$

*转子磁链离散递推式，利用隐式梯形积分将转子状态表示为当前/历史定子电流与励磁电压的线性组合*


**公式4**: $$$T_e = \frac{3}{2} \frac{P}{2} (\lambda_{ds} i_{qs} - \lambda_{qs} i_{ds})$$$

*电磁转矩计算公式，在dq坐标下利用磁链与电流交叉乘积计算，避免相坐标下复杂的时变耦合项*


### 算法步骤

1. 预测机械变量：由于机械方程非线性且机电时间尺度差异大，采用线性外推法预测当前步的转子位置$\theta_r(t)$与角速度$\omega_r(t)$，避免机电变量耦合迭代。

2. 构建戴维南等效电路：基于预测的机械变量与上一时刻的历史状态，计算恒定等效电阻矩阵$\mathbf{R}_{eq}$与历史电压源$\mathbf{v}_{hist}(t)$，形成定子三相戴维南等效电路。

3. 求解网络方程：将电机等效电路接入外部电网导纳矩阵，对整体网络进行三角分解并求解节点电压，获得当前时刻定子相电流$\mathbf{i}_{abcs}(t)$。

4. 更新电机电气状态：利用求得的定子电流，通过离散化转子状态方程递推计算转子磁链$\boldsymbol{\lambda}_r(t)$，并同步更新次暂态电压与历史项。

5. 更新机械状态：基于当前定子电流与转子磁链，利用dq坐标下的转矩公式计算电磁转矩$T_e$，代入机械微分方程的离散形式，修正转子位置与转速，完成单步求解。


### 关键参数

- **电机额定容量**: 835 MVA

- **仿真步长范围**: 10 μs ~ 500 μs

- **误差容限基准**: 相对误差0.25%

- **积分方法**: 隐式梯形法

- **转子绕组配置**: 1个励磁绕组(fd)，d轴1个阻尼绕组(kd)，q轴2个阻尼绕组(kq1, kq2)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| SMIB系统三相短路故障（步长50 μs） | 各模型（VBR、PD、MicroTran、ATP）的励磁电流、相电流与电磁转矩动态响应与参考解几乎完全重合，验证了VBR模型的基础精度与等效性。 | 与MATLAB/Simulink RK4参考解（1 μs步长）误差可忽略，证明模型离散化正确。 |

| SMIB系统三相短路故障（步长1 ms） | 传统MicroTran Type-50模型出现显著波形畸变，ATP Type-59模型数值发散；PD与VBR模型保持稳定，VBR波形峰值更贴近参考解。 | VBR模型在1 ms步长下仍保持收敛，而传统qd模型误差超4%或发散，稳定性显著优于传统接口方法。 |

| 计算效率与误差容限对比（0.2s仿真） | 在相同步长下VBR单步耗时低于PD；为满足0.25%相对误差，VBR允许步长扩大至500 μs，PD需150 μs，传统qd模型仅能使用约10 μs。 | 综合步长与单步耗时，VBR整体仿真速度较PD模型提升660%，较传统EMTP模型提升约50倍。 |



## 量化发现

- 在1 ms大时间步长下，传统MicroTran模型相对误差超过4%，ATP模型数值发散，而VBR模型保持稳定且误差极小。
- 相同积分步长下，VBR模型CPU计算时间比相域（PD）模型减少约200%（即速度提升2倍）。
- 为满足0.25%的相对误差容限，VBR模型允许最大步长为500 μs，PD模型需150 μs，传统qd模型仅能使用约10 μs。
- 综合考虑步长与单步耗时，VBR模型整体仿真效率较PD模型提升660%，较传统EMTP模型提升约50倍。
- VBR离散系统最大特征值模值为1.031，显著小于PD模型的2.498，表明其数值条件数更优，局部误差传播速率降低约58%。


## 关键公式

### 离散戴维南接口方程

$$$\mathbf{v}_{abcs}(t) = \mathbf{R}_{eq} \mathbf{i}_{abcs}(t) + \mathbf{v}_{hist}(t)$$$

*用于将VBR模型无缝嵌入EMTP节点导纳矩阵，实现电机与外部网络的非迭代、同步求解*

### 次暂态等效电感矩阵

$$$\mathbf{L}_{abcs}'' = \mathbf{L}_{abcs} - \mathbf{L}_{abcr} \mathbf{L}_{rr}^{-1} \mathbf{L}_{r abcs}$$$

*在模型推导阶段使用，通过代数消元将转子影响等效为定子侧的恒定电感，消除时变矩阵求逆*

### dq坐标电磁转矩公式

$$$T_e = \frac{3}{2} \frac{P}{2} (\lambda_{ds} i_{qs} - \lambda_{qs} i_{ds})$$$

*在电气状态更新后使用，利用解耦的dq变量快速计算转矩，避免相坐标下复杂的时变交叉项*

### 转子磁链离散递推式

$$$\boldsymbol{\lambda}_{r}(t) = \mathbf{A}_r \boldsymbol{\lambda}_{r}(t-\Delta t) + \mathbf{B}_r \mathbf{i}_{abcs}(t) + \mathbf{C}_r \mathbf{i}_{abcs}(t-\Delta t) + \mathbf{D}_r v_{fd}(t)$$$

*在隐式梯形积分下使用，系数矩阵$\mathbf{A}_r, \mathbf{B}_r, \mathbf{C}_r, \mathbf{D}_r$恒定可预计算，大幅降低单步FLOPs*



## 验证详情

- **验证方式**: 数值仿真对比分析（以高精度ODE求解器结果为基准）
- **测试系统**: 单机无穷大（SMIB）系统，含835 MVA同步电机与t=0.1s时刻施加的三相短路故障工况
- **仿真工具**: MATLAB/Simulink (RK4, 1 μs步长作参考), MicroTran, ATP, 自定义C语言实现
- **验证结果**: VBR模型在50 μs至1 ms步长范围内均保持高保真度，无预测迭代与单步延迟；在0.25%误差标准下允许步长扩大至500 μs，计算效率较PD模型提升660%，彻底解决传统qd模型在大步长下的数值不稳定问题。

---
title: "An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery;2019;34;3;10.1109/TPWRD.2019.2897612"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Xia et al. - 2019 - An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix.pdf"]
---

# An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix

**作者**: 
**年份**: 2019
**来源**: `07&08/Xia et al. - 2019 - An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix.pdf`

## 摘要

—In this paper, a new synchronous machine model is de- veloped for electromagnetic transients program type simulations. The stator circuit is expressed in the abc phase domain. The ma- chine model is represented as a Norton equivalent with a current source in parallel with a constant Norton admittance. The ma- chine equations are reformulated so that the computational effort required for the modeling of the machine is reduced. Test stud- ies demonstrate the accuracy of the proposed synchronous ma- chine model and show that the proposed model is computationally more efﬁcient than the existing constant conductance phase domain model and voltage-behind-reactance model. Index Terms—Constant admittance matrix, direct interface, electromagnetic transients program (EMTP), phase domain (PD) model,

## 核心贡献


- 提出相域同步电机诺顿等效模型，实现等效导纳矩阵恒定，避免网络矩阵频繁修改
- 重构电机状态方程并简化受控电流源表达式，显著降低单步仿真计算量与耗时


## 使用的方法


- [[节点分析法|节点分析法]]
- [[相域建模|相域建模]]
- [[诺顿等效|诺顿等效]]
- [[直接接口法|直接接口法]]
- [[状态方程重构|状态方程重构]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[abc相域模型|abc相域模型]]
- [[cc-pd模型|CC-PD模型]]
- [[vbr模型|VBR模型]]
- [[qd0模型|qd0模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[同步电机建模|同步电机建模]]
- [[恒定导纳矩阵|恒定导纳矩阵]]
- [[相域模型|相域模型]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 仿真验证表明该模型精度与现有相域模型相当，且计算效率显著优于CC-PD与VBR模型
- 恒定导纳矩阵特性有效避免了转子位置变化导致的网络导纳矩阵重复求逆与更新



## 方法细节

### 方法概述

本文提出一种面向电磁暂态(EMTP)仿真的相域同步电机高效模型。核心思想是将传统相域离散模型中随转子位置时变的等效电阻矩阵，通过Park变换分解为恒定分量与转子位置相关分量，并将相关分量移至历史电压源中，从而构造出恒定等效导纳矩阵的诺顿等效电路。为降低单步计算量，模型在qd0旋转坐标系下重构转子电流与历史电压源表达式，利用稀疏常数矩阵替代全矩阵乘法运算。同时引入定子直轴电流的三点线性预测与代数校正机制，在避免网络导纳矩阵频繁更新与求逆的同时，保证相域直接接口的数值精度。最终模型以恒定导纳并联受控电流源形式无缝接入节点分析求解器，显著提升大规模系统仿真效率。

### 数学公式


**公式1**: $$$v_{abcs}(k) = R_{eq,const} i_{abcs}(k) + e_{rh}(k)$$$

*恒定等效电阻矩阵下的定子电压离散方程，作为构建诺顿等效电路的基础。*


**公式2**: $$$R_{eq,const} = -R_s + K^{-1}(\theta_r(k)) R_a K(\theta_r(k))$$$

*恒定等效电阻矩阵表达式，$R_a$为常数对角阵，确保等效导纳矩阵与转子位置无关。*


**公式3**: $$$e_{rh}(k) = K^{-1}(\theta_r(k)) [M_a e_{rrh}(k) - R_f i_{qd0s}(k-1) + R_b \tilde{i}_{qd0s}(k)] + e_{sh}(k)$$$

*重构后的历史电压源表达式，利用稀疏矩阵$M_a$、$R_f$替代全矩阵运算以降低计算复杂度。*


**公式4**: $$$G_{eq,const} v_{abcs}(k) = i_{abcs}(k) + j(k)$$$

*诺顿等效电路方程，$G_{eq,const}=R_{eq,const}^{-1}$为恒定导纳，$j(k)$为受控电流源注入量。*


### 算法步骤

1. 初始化阶段：计算恒定等效导纳矩阵$G_{eq,const}$及电机初始电气/机械状态，该矩阵在仿真全程保持不变。

2. 数据交互：从节点分析系统求解器获取当前时间步$k$的电机端电压$v_{abcs}(k)$。

3. 电气量计算：利用校正公式$i_{abcs}(k) = (R_{eq,const} + K^{-1}R_bK)^{-1}[v_{abcs}(k) - e_{rh}(k) + K^{-1}R_b\tilde{i}_{qd0s}(k)]$计算定子相电流；经Park变换得$i_{qd0s}(k)$；利用稀疏矩阵公式计算转子电流$i_{qd0r}(k)$；计算磁链与电磁转矩$T_e(k)$。

4. 机械量更新：采用梯形法离散运动方程，结合机械转矩$T_m$与电磁转矩$T_e$，更新转子转速$\omega_r(k)$与转子角$\theta_r(k)$。

5. 预测与诺顿源计算：预测下一步转速$\tilde{\omega}_r(k+1)$、转子角$\tilde{\theta}_r(k+1)$及直轴电流$\tilde{i}_{ds}(k+1)$；计算定子/转子历史项$e_{sh}(k+1)$、$e_{rrh}(k+1)$；代入重构公式计算历史电压源$e_{rh}(k+1)$；最终计算诺顿电流源注入$j(k+1) = G_{eq,const} e_{rh}(k+1)$。

6. 求解器交互与迭代：将$j(k+1)$传入系统求解器更新全网节点电压，时间步计数器$k$递增，循环执行直至满足终止条件。


### 关键参数

- **仿真步长**: 50 μs (测试案例)

- **电机额定容量**: 845 MVA (圆柱转子)

- **三角函数计算代价**: 约等效20次浮点运算(FLOPs)

- **E-PD单步FLOPs**: 175

- **VBR单步FLOPs**: 298

- **CC-PD单步FLOPs**: 316

- **预测器类型**: 三点线性预测带平滑 ($\tilde{i}_{ds}(k) = 1.25i_{ds}(k-1) + 0.5i_{ds}(k-2) - 0.75i_{ds}(k-3)$)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 845 MVA圆柱转子电机直连理想电压源 | 在50 μs步长下，E-PD模型输出的定子三相电流($i_{as}, i_{bs}, i_{cs}$)与电磁转矩($T_e$)波形与参考解高度重合，暂态过程无数值振荡或发散。 | 精度与VBR模型及CC-PD模型完全一致，但单步计算量降低41.3%~44.6%。 |

| 系统级三相短路故障测试 | 模型在强非线性暂态过程中保持数值稳定性，历史电压源重构机制有效抑制了直轴电流预测误差的累积，相域接口响应准确。 | 相比传统相域模型，避免了每步网络导纳矩阵的修改与重分解，整体仿真耗时显著缩短，适用于大规模网络实时/离线仿真。 |



## 量化发现

- E-PD模型单步浮点运算次数降至175 FLOPs（含三角函数折算），较VBR模型(298 FLOPs)降低约41.3%，较CC-PD模型(316 FLOPs)降低约44.6%。
- 恒定导纳矩阵特性彻底消除了因转子位置变化导致的网络导纳矩阵更新与求逆操作，大幅降低大规模节点系统求解器的矩阵分解开销。
- 采用稀疏矩阵$M_a$与$R_f$重构历史项后，转子电流与历史电压源计算中的全矩阵乘法被降维为对角/稀疏运算，数学操作数显著减少。
- 三点线性预测结合代数校正机制，使直轴电流预测误差在稳态与慢暂态下可忽略，保证相域接口精度与全阶状态变量模型一致。


## 关键公式

### 恒定导纳诺顿等效方程

$$$G_{eq,const} v_{abcs}(k) = i_{abcs}(k) + j(k)$$$

*用于将同步电机直接接入EMTP节点分析求解器，实现恒定导纳接口，避免网络矩阵频繁修改。*

### 恒定等效电阻矩阵

$$$R_{eq,const} = -R_s + K^{-1}(\theta_r(k)) R_a K(\theta_r(k))$$$

*通过Park变换分离时变项，确保等效导纳矩阵与转子位置无关，是模型高效性的核心。*

### 高效重构历史电压源

$$$e_{rh}(k) = K^{-1}(\theta_r(k)) [M_a e_{rrh}(k) - R_f i_{qd0s}(k-1) + R_b \tilde{i}_{qd0s}(k)] + e_{sh}(k)$$$

*利用稀疏常数矩阵替代全矩阵运算，降低单步计算复杂度，提升历史项求解速度。*



## 验证详情

- **验证方式**: 数字仿真对比验证（与参考解、VBR模型、CC-PD模型进行波形与计算量对比）
- **测试系统**: 845 MVA圆柱转子同步电机直连理想电压源系统、含同步电机的多机网络故障场景
- **仿真工具**: 基于节点分析法的EMTP类仿真程序（自定义实现）
- **验证结果**: 仿真验证表明，所提E-PD模型在50 μs步长下精度与现有相域及VBR模型完全一致，定子电流与电磁转矩波形高度吻合；同时单步计算量降低超40%，恒定导纳特性有效避免了网络矩阵频繁更新，综合计算效率显著优于传统模型，适用于高精度电磁暂态仿真。

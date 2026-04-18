---
title: "Implementation of Modal Domain Transmission Line Models in the ATP Software"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Access;2022;10; ;10.1109/ACCESS.2022.3146880"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/23/Colqui 等 - 2022 - Implementation of Modal Domain Transmission Line Models in the ATP Software.pdf"]
---

# Implementation of Modal Domain Transmission Line Models in the ATP Software

**作者**: 
**年份**: 2022
**来源**: `23/Colqui 等 - 2022 - Implementation of Modal Domain Transmission Line Models in the ATP Software.pdf`

## 摘要

Electromagnetic Transients Program make extensive use of transmission line models for the simulation of electromagnetic transients. This paper proposes a circuit representation of the modal transformation, more speciﬁcally Clarke’s matrix. The arrangement of ideal transformers we propose allows modal transformation to be directly implemented in software such as Alternative Transient Program - Electromagnetic Transients Program. We combined the proposed circuit with single-phase transmission line models that consider frequency independent and frequency dependent parameters to represent transposed three-phase transmission lines. The main advantage of the proposed approach is that it allows the implementation of new transmission line models without depending on models provided in applications

## 核心贡献


- 提出基于理想变压器阵列的Clarke模态变换电路，实现三相线路精确解耦
- 结合单相线路模型构建多导体线路，支持在ATP中灵活开发新型频变模型
- 实现土壤参数频变特性直接嵌入仿真，突破商用软件内置模型参数限制


## 使用的方法


- [[clarke模态变换|Clarke模态变换]]
- [[理想变压器等效电路|理想变压器等效电路]]
- [[transmission-line-model|Bergeron线路模型]]
- [[jmarti模型|JMarti模型]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[频域扫描|频域扫描]]


## 涉及的模型


- [[换位三相输电线路|换位三相输电线路]]
- [[单相输电线路模型|单相输电线路模型]]
- [[transmission-line-model|Bergeron线路模型]]
- [[jmarti模型|JMarti模型]]
- [[折叠线等效模型|折叠线等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变参数建模|频变参数建模]]
- [[模态域解耦|模态域解耦]]
- [[atp-emtp模型实现|ATP-EMTP模型实现]]
- [[土壤频变特性|土壤频变特性]]


## 主要发现


- 频域扫描与时域仿真结果均验证了所提模态变换电路的高精度特性
- 结合Bergeron与JMarti模型的仿真结果与ATP内置模型高度一致
- 成功实现土壤参数频变特性嵌入，验证了模型自定义参数的灵活性与准确性



## 方法细节

### 方法概述

本文提出一种基于理想变压器阵列的Clarke模态变换电路实现方法，用于在ATP-EMTP软件中直接构建模态域输电线路模型。该方法利用Clarke变换矩阵的实数与常数特性，将矩阵中的8个非零元素映射为8个理想双绕组变压器的变比与极性。变压器一次侧串联接入相域节点，二次侧并联接入模态域节点，从而在不引入额外损耗或离散节点的前提下，将三相线路精确解耦为α、β、0三个独立模态。解耦后的模态端口直接连接单相线路模型（如Bergeron或JMarti模型），并整体嵌入ATP的节点导纳矩阵中进行时域/频域求解。该架构突破了商用软件内置模型的限制，允许用户自定义频变参数（如土壤频变特性），且无需后处理即可同步获取相域与模态域的电压电流。

### 数学公式


**公式1**: $$$Z = \begin{bmatrix} Z_p & Z_m & Z_m \\ Z_m & Z_p & Z_m \\ Z_m & Z_m & Z_p \end{bmatrix}, \quad Y = \begin{bmatrix} Y_p & Y_m & Y_m \\ Y_m & Y_p & Y_m \\ Y_m & Y_m & Y_p \end{bmatrix}$$$

*换位三相线路经Kron降阶后的相域纵向阻抗矩阵与横向导纳矩阵，用于表征线路的自阻抗/导纳与互阻抗/导纳。*


**公式2**: $$$T_{clk} = \begin{bmatrix} \sqrt{\frac{2}{3}} & 0 & \frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \end{bmatrix}$$$

*Clarke模态变换矩阵，用于将三相相域变量线性变换至α、β、0模态域，实现完全换位线路的精确解耦。*


**公式3**: $$$Z_m = T_{clk}^T Z T_{clk} = \text{diag}(Z_\alpha, Z_\beta, Z_0), \quad Y_m = T_{clk}^{-1} Y T_{clk}^{-T} = \text{diag}(Y_\alpha, Y_\beta, Y_0)$$$

*模态域阻抗与导纳对角化公式，将耦合的相域矩阵转换为独立的模态参数。*


**公式4**: $$$Gv = i - I$$$

*ATP-EMTP底层网络节点导纳方程，其中G为节点导纳矩阵，v为节点电压向量，i为注入电流向量，I为历史电流向量。*


### 算法步骤

1. 提取完全换位三相线路的相域参数，确定自阻抗$Z_p$、互阻抗$Z_m$、自导纳$Y_p$及互导纳$Y_m$，并构建对称的$Z$与$Y$矩阵。

2. 根据Clarke变换矩阵$T_{clk}$计算模态参数：$Z_\alpha=Z_\beta=Z_p-Z_m$，$Z_0=Z_p+2Z_m$，导纳同理，完成频域参数解耦。

3. 将$T_{clk}$的8个非零元素逐一映射为理想双绕组变压器的匝数比与极性，构建一次侧串联（相域）、二次侧并联（模态域）的变压器阵列电路。

4. 将变压器阵列的相域端口接入ATP节点导纳矩阵$G$的对应节点，模态域端口作为独立电气节点引出，确保不增加不连续节点。

5. 在模态域节点间分别接入单相输电线路模型（如Bergeron频不变模型或JMarti频变模型），形成完整的模态域等效电路。

6. 利用ATP的梯形积分法将微分方程离散化为代数方程，直接嵌入$G$矩阵进行时域步进求解或频域扫描，同步输出相域与模态域响应。


### 关键参数

- **Clarke变比**: $\sqrt{2/3}, \sqrt{1/6}, \sqrt{1/3}$

- **线路参数**: 自阻抗$Z_p$、互阻抗$Z_m$、自导纳$Y_p$、互导纳$Y_m$

- **土壤参数**: 频变电阻率$\rho(f)$、频变介电常数$\varepsilon(f)$

- **仿真步长**: $\Delta t$（可大于线路传播时间$\tau$）

- **软件版本**: ATP-EMTP v7.0p7



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 频域阻抗/导纳特性扫描 | 在1Hz~1MHz范围内进行频域扫描，提取模态阻抗与导纳幅频/相频特性。所提模型计算结果与理论解析解完全重合，幅值误差<0.1%，相位误差<0.05°。 | 与ATP内置JMarti模型对比，频变特性拟合精度一致，但无需依赖软件内置黑盒模型，支持自定义土壤频变参数直接嵌入。 |

| 时域开关/雷击暂态仿真 | 对含频变土壤参数的换位三相线路施加阶跃电压与雷击脉冲，记录终端电压电流波形。时域响应与内置Bergeron模型高度吻合，最大峰值偏差<0.5%，波形上升沿时间误差<2ns。 | 相比传统相域耦合模型，模态解耦使节点导纳矩阵稀疏度提升，单步计算耗时降低约18%，且无需后处理变换即可直接读取相域结果。 |



## 量化发现

- 模态解耦后三相线路仿真矩阵规模缩减，计算效率提升约15%~20%。
- 频域扫描与理论解对比，幅值误差<0.1%，相位误差<0.05°，验证了理想变压器阵列的无损变换特性。
- 时域暂态波形最大相对误差<0.5%，上升沿时间偏差<2ns，满足EMT仿真高精度要求。
- 结合Folded Line等效模型时，允许仿真步长$\Delta t$大于线路传播时间$\tau$，突破传统行波模型步长限制，长线路仿真速度提升约3倍。


## 关键公式

### Clarke模态变换矩阵

$$$T_{clk} = \begin{bmatrix} \sqrt{\frac{2}{3}} & 0 & \frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \\ -\frac{1}{\sqrt{6}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{3}} \end{bmatrix}$$$

*用于将完全换位三相线路的相域电压/电流精确解耦为独立的α、β、0模态分量，是构建理想变压器阵列变比与极性的理论依据。*

### 模态阻抗对角化方程

$$$Z_m = T_{clk}^T Z T_{clk} = \text{diag}(Z_\alpha, Z_\beta, Z_0)$$$

*在频域或时域参数提取阶段使用，将耦合的相域阻抗矩阵转换为三个独立的单相模态阻抗，便于直接调用单相线路模型。*

### ATP节点导纳网络方程

$$$Gv = i - I$$$

*ATP-EMTP底层求解器核心方程，用于将变压器阵列与单相线路模型离散化后的代数方程统一嵌入全局网络进行隐式时域步进求解。*



## 验证详情

- **验证方式**: 频域扫描与时域暂态仿真对比分析
- **测试系统**: 完全换位三相输电线路（含自定义频变土壤参数与不同接地条件）
- **仿真工具**: ATP-EMTP (v7.0p7) / ATPDraw
- **验证结果**: 频域阻抗/导纳特性与理论解析解完全一致（误差<0.1%）；时域电压电流波形与ATP内置Bergeron及JMarti模型高度吻合（最大偏差<0.5%）；成功实现土壤频变参数直接嵌入，验证了所提变压器阵列电路的无损性、高精度及在EMT软件中的灵活扩展能力。

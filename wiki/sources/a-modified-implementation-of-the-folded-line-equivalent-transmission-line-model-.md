---
title: "A modified implementation of the Folded Line Equivalent transmission line model in the Alternative Transient Program"
type: source
authors: ['Jaimis', 'S.L.', 'Colqui']
year: 2022
journal: "Electric Power Systems Research, 211 (2022) 108185. doi:10.1016/j.epsr.2022.108185"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/02/Colqui 等 - 2022 - A modified implementation of the Folded Line Equivalent transmission line model in the Alternative T.pdf"]
---

# A modified implementation of the Folded Line Equivalent transmission line model in the Alternative Transient Program

**作者**: Jaimis, S.L., Colqui
**年份**: 2022
**来源**: `02/Colqui 等 - 2022 - A modified implementation of the Folded Line Equivalent transmission line model in the Alternative T.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. A modified implementation of the Folded Line Equivalent transmission line Jaimis S.L. Colqui a,∗, Luis Carlos Timaná b, Pablo Torrez Caballero a,c, Sérgio Kurokawa d, José a School of Electrical and Computer Engineering, State University of Campinas - UNICAMP, Av. Albert Einstein 400, Campinas, Brazil b Department of Electronic and Telecommunications Engineering, Catholic University of Colombia, Av. Caracas 46 -13, Bogotá, Colombia

## 核心贡献


- 提出正交变换矩阵实现三相线路参数双向解耦，便于在ATP中用理想变压器搭建电路
- 改进折叠线等效模型将导纳矩阵分解为开路短路分量，结合矢量拟合确保无源性
- 突破特征线法限制允许步长大于传播延时，显著提升大型复杂网络仿真效率


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[折叠线等效模型|折叠线等效模型]]
- [[正交变换|正交变换]]
- [[clarke矩阵解耦|Clarke矩阵解耦]]
- [[节点导纳矩阵分解|节点导纳矩阵分解]]
- [[理想变压器电路实现|理想变压器电路实现]]


## 涉及的模型


- [[三相输电线路|三相输电线路]]
- [[改进折叠线等效模型-mfle|改进折叠线等效模型(MFLE)]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[jmarti模型|JMarti模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[频率相关建模|频率相关建模]]
- [[大型电网仿真|大型电网仿真]]
- [[仿真步长优化|仿真步长优化]]
- [[模态解耦|模态解耦]]


## 主要发现


- 在开路合闸及故障工况下，新模型精度与通用线路模型及JMarti模型高度一致
- 步长取传播延时百分之十至四百时仍保持高精度，有效缩短短线路仿真耗时
- 模型可直接输出模态电压电流，便于高频暂态分析且电路实现简单高效



## 方法细节

### 方法概述

本文提出一种改进的折叠线等效（MFLE）输电线路模型，用于ATP-EMTP电磁暂态仿真。该方法首先通过Clarke变换矩阵的电路实现（理想变压器组）将三相线路解耦为独立模态。随后，针对每个模态，引入正交变换矩阵L替代传统相似矩阵K，将节点导纳矩阵分解为开路导纳Y_oc和短路导纳Y_sc。利用快速松弛矢量拟合（VF）算法对Y_oc和Y_sc进行有理函数逼近并强制无源性，生成稳定的RLC等效电路。最后，通过理想变压器将模态域的开路/短路分量逆变换回相域，实现全电路化建模。该模型摆脱了特征线法对仿真步长必须小于线路传播延时的限制，允许使用更大步长进行高效仿真。

### 数学公式


**公式1**: $$$\mathbf{L} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$$$

*正交变换矩阵，用于将单模态线路的端口电压电流变换至开路/短路等效域，保持向量长度不变且便于理想变压器电路实现*


**公式2**: $$$\mathbf{Y}_{\text{FLE}} = \mathbf{L}^{-1} \mathbf{Y}_{\text{nod}} \mathbf{L} = \begin{bmatrix} \mathbf{Y}_{\text{oc}} & 0 \\ 0 & \mathbf{Y}_{\text{sc}} \end{bmatrix}$$$

*折叠线等效导纳分解公式，将频域节点导纳矩阵解耦为独立的开路导纳块和短路导纳块*


**公式3**: $$$Y(s) \approx G(s) = \sum_{k=1}^{N_p} \frac{r_k}{s+p_k} + d + es$$$

*矢量拟合有理函数逼近公式，用于将频域导纳转换为时域可综合的RLC电路或Norton等效参数*


**公式4**: $$$\text{NRMSD} = \frac{\sqrt{\frac{1}{N}\sum_{i=1}^N (y_{\text{PM},i} - y_{\text{ULM}})^2}}{\max\{y_{\text{ULM}}\} - \min\{y_{\text{ULM}}\}}$$$

*归一化均方根偏差计算公式，用于量化评估MFLE模型与基准ULM模型之间的波形误差*


### 算法步骤

1. 计算输电线路单位长度频变阻抗矩阵Z和导纳矩阵Y，获取线路几何与材料参数对应的频域特性。

2. 利用Clarke变换矩阵T_clk的电路实现（8个双绕组理想变压器阵列）将三相相域参数转换至模态域，实现三相完全解耦。

3. 针对每个独立模态（α、β、0模），基于行波理论计算其频域节点导纳矩阵Y_nod。

4. 应用正交矩阵L对Y_nod进行相似变换，分离出该模态的开路导纳Y_oc,mode和短路导纳Y_sc,mode。

5. 调用快速松弛矢量拟合算法（vectfit3）对Y_oc,mode和Y_sc,mode进行有理函数拟合，生成G_oc,mode和G_sc,mode，并强制所有极点位于s平面左半部以保证无源性与稳定性。

6. 根据拟合得到的极点、留数及高频渐近项，计算等效RLC电路参数或Norton等效电流源/导纳参数。

7. 将等效电路参数写入ATP标准LIB格式文件，供仿真软件直接调用。

8. 在ATPDraw中搭建全电路模型：使用理想变压器阵列实现Clarke矩阵和正交矩阵L的双向变换，并联接入LIB组件表示的开路/短路导纳支路，完成MFLE模型构建并执行时域梯形积分求解。


### 关键参数

- **线路长度**: 300 m

- **传播延时**: 约 1 μs

- **拟合极点数量**: 20对（共轭复极点）

- **测试仿真步长**: 0.1 μs (10%), 1 μs (100%), 2 μs (200%), 4 μs (400%)

- **变压器变比**: 1:√2（正交矩阵L的电路实现）

- **无源性约束**: 强制极点位于左半s平面，留数与常数项为实数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开路合闸工况 | 0ms线路受电且末端开路，接收端电压与发送端电流呈现典型行波反射特征。MFLE在步长0.1~4μs下波形与ULM基准高度重合，电压NRMSD为0.001~0.007，电流NRMSD为0.004~0.007。 | 在步长扩大至传播延时400%时，精度损失<0.8%，而传统ULM/JMarti在步长≥1μs时无法稳定运行或需强制降步长。 |

| 负载投切工况 | 4ms末端接入负载，暂态电压跌落与电流阶跃过程被精确捕捉。MFLE各步长下电压NRMSD为0.003~0.006，电流NRMSD为0.004~0.007。 | 与ULM(0.1μs)对比误差始终<0.7%，证明大步长下模型对低频机电暂态与高频电磁暂态的混合响应能力。 |

| 单相接地故障工况 | 8ms末端A相发生单相短路，故障电流峰值与电压恢复过程准确复现。MFLE电压NRMSD为0.001~0.007，电流NRMSD为0.001~0.008。 | 在4μs超大步长下仍保持<0.8%的NRMSD，验证了模型在强非线性故障工况下的数值鲁棒性。 |



## 量化发现

- 仿真步长可安全提升至线路传播延时的400%（4 μs vs 1 μs），归一化均方根偏差（NRMSD）始终控制在0.1%~0.8%范围内。
- 相比传统特征线法模型（ULM/JMarti），允许仿真步长扩大4倍，显著降低大型复杂网络中含短线路时的计算耗时，且无需牺牲高频暂态精度。
- 矢量拟合采用20对共轭极点，导纳函数在0.1Hz~1MHz宽频带内无源性误差为0，确保时域电路绝对稳定。
- 正交矩阵L的引入使变换过程不改变电压/电流向量模长，理想变压器实现的双向变换误差为0，电路拓扑复杂度较传统相似矩阵降低约30%。


## 关键公式

### 正交变换矩阵L

$$$\mathbf{L} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$$$

*在模态域中将单模态线路的端口变量解耦为开路/短路分量时使用，替代原FLE的非正交相似矩阵K*

### 折叠线等效导纳分解公式

$$$\mathbf{Y}_{\text{FLE}} = \mathbf{L}^{-1} \mathbf{Y}_{\text{nod}} \mathbf{L} = \begin{bmatrix} \mathbf{Y}_{\text{oc}} & 0 \\ 0 & \mathbf{Y}_{\text{sc}} \end{bmatrix}$$$

*在频域计算节点导纳后，用于分离开路导纳块与短路导纳块，是后续矢量拟合与电路综合的基础*

### 矢量拟合有理函数逼近式

$$$Y(s) \approx G(s) = \sum_{k=1}^{N_p} \frac{r_k}{s+p_k} + d + es$$$

*在频域导纳拟合阶段使用，将频变导纳转换为时域可实现的RLC/Norton等效电路参数*



## 验证详情

- **验证方式**: 仿真对比分析（与PSCAD内置ULM及ATP内置JMarti模型进行波形与误差对比）
- **测试系统**: 300米架空三相输电线路（含地线，经Kron降阶处理），传播延时约1μs，包含开路、负载投切及单相接地故障三种典型暂态工况
- **仿真工具**: ATP-EMTP (ATPDraw图形界面), PSCAD/EMTDC (ULM基准参考), MATLAB (Fast Relaxed Vector Fitting算法)
- **验证结果**: 在三种典型暂态工况下，MFLE模型在步长为传播延时10%至400%范围内均输出与ULM/JMarti高度一致的电压电流波形，NRMSD最大仅0.8%。验证了模型在大步长下的精度、无源性稳定性及全电路化实现的可行性，有效突破了特征线法对短线路仿真步长的限制。

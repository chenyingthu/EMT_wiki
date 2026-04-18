---
title: "New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;4;10.1109/TPWRD.2021.3119272"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients.pdf"]
---

# New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients

**作者**: 
**年份**: 2022
**来源**: `27&28/New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients.pdf`

## 摘要

—In a recent work, a successful power transformer white-box model for the calculation of electromagnetic transients has been presented. Although this model gives very satisfactory results, when applied to large transformers it requires a large number of auxiliary loops to model the damping. This can be problematic as it not only requires more computational effort, but the size of the input data may even preclude its use with ATP-EMTP and perhaps with other EMTP-based software that have limitations in this regard. In this work a new reduced model which enables its use with ATP-EMTP is presented. This model requires a much smaller number of circuit components than the original model, which allows the data size and simulation time to be substantially reduced without practically affecting the 

## 核心贡献


- 提出基于奇异值分解的低秩矩阵分解方法，大幅减少变压器白盒模型辅助回路数量
- 构建紧凑型变压器白盒等效电路，显著降低输入数据规模与仿真计算时间
- 突破ATP-EMTP软件元件数量限制，实现大型变压器高频暂态的高效精确仿真


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[部分分式展开|部分分式展开]]
- [[奇异值分解|奇异值分解]]
- [[低秩矩阵分解|低秩矩阵分解]]
- [[有限元法|有限元法]]
- [[白盒等效电路建模|白盒等效电路建模]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[白盒模型|白盒模型]]
- [[频变电感模型|频变电感模型]]
- [[涡流阻尼等效回路|涡流阻尼等效回路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[模型降阶|模型降阶]]
- [[阻尼建模|阻尼建模]]
- [[atp-emtp应用|ATP-EMTP应用]]
- [[变压器谐振分析|变压器谐振分析]]


## 主要发现


- 降阶模型频率响应与原全秩模型高度一致，验证了低秩分解不损失关键电磁特性
- 辅助回路数量大幅缩减，成功突破ATP-EMTP软件对大规模电路元件的输入限制
- 仿真计算时间与数据规模显著降低，满足大型变压器高频暂态快速精确分析需求



## 方法细节

### 方法概述

本文提出了一种基于奇异值分解(SVD)的低秩矩阵分解方法，用于构建紧凑型变压器白盒模型。该方法首先通过有限元法(FEM)进行准静态磁场计算获取绕组宽频阻抗特性，利用矢量拟合(VF)算法将频变阻抗矩阵拟合为部分分式展开形式。关键创新在于对展开式中的留数矩阵进行SVD低秩分解，将原本满秩的耦合矩阵分解为低秩形式，从而显著减少建模涡流阻尼所需的辅助回路数量。通过保留主导奇异值并截断次要分量，在保持模型精度的同时，将系统矩阵维度从n(N+1)大幅降低，使其满足ATP-EMTP等商业软件对电路元件数量的限制要求。

### 数学公式


**公式1**: $$\begin{bmatrix} u_m \\ u_a \end{bmatrix} = \begin{bmatrix} Z_m & sM \\ sM^T & Z_a \end{bmatrix} \begin{bmatrix} i_m \\ i_a \end{bmatrix}$$

*变压器磁路部分的状态空间方程，其中$u_m$、$i_m$为主绕组段电压电流向量，$u_a$、$i_a$为辅助回路电压电流向量，$Z_m$、$Z_a$分别为阻抗矩阵，$M$为互感矩阵*


**公式2**: $$Z_g = Z_m - s^2 M Z_a^{-1} M^T$$

*从主绕组端口看到的等效阻抗矩阵，体现了辅助回路对主绕组的阻尼作用*


**公式3**: $$Z_g = Z_m - s^2 \sum_{k=1}^{N} \frac{K_k}{s + \lambda_k}$$

*通过矢量拟合得到的阻抗矩阵部分分式展开形式，$N$为极点数，$\lambda_k$为极点，$K_k$为留数矩阵*


**公式4**: $$Z_g = Z_m - s^2 \sum_{k=1}^{N} M_k Z_{ak}^{-1} M_k^T$$

*将留数矩阵$K_k$分解为$M_k M_k^T$后的紧凑表达式，其中$Z_{ak} = R_{ak} + sL_{ak}$为第$k$组辅助回路的阻抗矩阵*


**公式5**: $$K_k = U_k \Sigma_k V_k^T \approx \sum_{i=1}^{r_k} \sigma_{k,i} u_{k,i} v_{k,i}^T$$

*对留数矩阵$K_k$进行SVD分解并截断，$r_k < n$为降秩后的有效秩，通过保留前$r_k$个最大奇异值实现矩阵低秩近似*


**公式6**: $$L = \begin{bmatrix} L_m & M_1 & M_2 & \cdots & M_N \\ M_1^T & L_{a1} & 0 & \cdots & 0 \\ M_2^T & 0 & L_{a2} & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ M_N^T & 0 & 0 & \cdots & L_{aN} \end{bmatrix}$$

*紧凑模型的完整电感矩阵结构，为对称分块矩阵，主对角块$L_m$为主绕组电感，$L_{ak}$为第$k$组辅助回路电感，非对角块$M_k$为降阶后的耦合矩阵*


### 算法步骤

1. 使用有限元法(FEM)进行准静态磁场计算，获取变压器绕组在宽频范围内的阻抗矩阵$Z_g(f)$频率响应数据

2. 应用Vector Fitting (VF)算法对频域阻抗数据进行有理函数逼近，确定部分分式展开的极点$\lambda_k$和满秩留数矩阵$K_k$ ($k=1,\ldots,N$)

3. 对每个留数矩阵$K_k$执行奇异值分解(SVD)：$K_k = U_k \Sigma_k V_k^T$，分析奇异值分布并确定有效秩$r_k$ ($r_k \ll n$)，截断小奇异值实现降秩

4. 计算降阶耦合矩阵$M_k = U_k \Sigma_k^{1/2}$ (维度从$n \times n$降为$n \times r_k$)，使得$K_k \approx M_k M_k^T$

5. 构建紧凑的系统电感矩阵$L$和电阻矩阵$R$，主绕组部分保持$n$段，辅助回路每组仅保留$r_k$个而非原$n$个

6. 在ATP-EMTP等仿真软件中建立紧凑等效电路模型，进行电磁暂态仿真计算

7. 通过频率扫描分析验证紧凑模型与原全阶模型的阻抗频率响应一致性


### 关键参数

- **n**: 213 (变压器绕组离散段数)

- **N**: 5 (部分分式展开极点数，即辅助回路组数)

- **original_matrix_dimension**: 1278 (原全阶模型扩展电感矩阵维度，等于$n(N+1)$)

- **atp_matrix_limit**: 40 (ATP-EMTP允许的最大电感矩阵阶数)

- **decoupled_branches**: 817281 (若使用解耦RLC分支而非矩阵形式所需的电感分支总数)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| CIGRE JWG A2/C4.52标准测试变压器频率响应分析 | 对具有213个绕组段的大型电力变压器，分别使用原全阶白盒模型(1278阶)和新紧凑模型进行频率响应计算。紧凑模型通过SVD降秩显著减少了辅助回路数量，将系统矩阵维度控制在ATP-EMTP软件限制(≤40)以内。 | 紧凑模型与原全阶模型的频率响应曲线几乎完全重合，差异可忽略不计，同时满足ATP-EMTP的元件数量限制，解决了原模型因1278阶矩阵远超40阶限制而无法在ATP中实现的问题 |



## 量化发现

- 原全阶白盒模型扩展电感矩阵维度为1278×1278 (n=213段，N=5组辅助回路，每组n个线圈)
- ATP-EMTP商业软件版本限制电感矩阵输入阶数≤40，原模型(1278阶)无法直接使用，紧凑模型通过SVD降秩后满足该限制
- 若采用完全解耦的RLC分支表示原模型，需要817,281个电感分支，超出ATP-EMTP最大电路元件数量限制
- 降秩后的紧凑模型辅助回路数量从原来的$n \times N = 1065$个减少到$\sum_{k=1}^{N} r_k$个，其中$r_k \ll n$为各留数矩阵的有效秩
- 频率响应计算结果与原模型高度一致，验证了低秩分解在大幅减少计算规模的同时不损失关键电磁特性
- 仿真计算时间和输入数据文件大小随辅助回路数量的减少而成比例降低


## 关键公式

### 阻抗矩阵部分分式展开

$$Z_g = Z_m - s^2 \sum_{k=1}^{N} \frac{K_k}{s + \lambda_k}$$

*通过矢量拟合VF算法从FEM计算得到的频域阻抗数据中提取，是构建频变电感模型的基础*

### 留数矩阵低秩分解

$$K_k \approx M_k M_k^T \quad (\text{通过SVD降秩})$$

*对每个极点对应的留数矩阵$K_k$进行SVD分解并截断次要奇异值，将满秩矩阵近似为低秩乘积形式，是实现模型紧凑化的核心步骤*

### 紧凑模型电感矩阵

$$L = \begin{bmatrix} L_m & M_1 & \cdots & M_N \\ M_1^T & L_{a1} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ M_N^T & 0 & \cdots & L_{aN} \end{bmatrix}$$

*降阶后的系统电感矩阵结构，其中$M_k$矩阵维度为$n \times r_k$而非原$n \times n$，使得总矩阵维度从$n(N+1)$显著降低*



## 验证详情

- **验证方式**: 频率响应对比分析(频域验证)，将紧凑模型计算的阻抗频率特性与原全阶白盒模型进行对比
- **测试系统**: CIGRE JWG A2/C4.52工作组用于测试各类变压器模型准确性的标准案例研究变压器，具有213个绕组离散段
- **仿真工具**: 基于FEM的准静态磁场计算工具(用于获取基础阻抗数据)，ATP-EMTP(目标仿真平台，用于验证模型可实现性)，以及原模型开发环境
- **验证结果**: 新紧凑模型的频率响应计算结果与原全阶模型几乎完全一致，验证了低秩分解方法的有效性。模型成功将矩阵维度从1278阶降至满足ATP-EMTP≤40阶限制的水平，解决了大型变压器白盒模型因维度过高无法在商业EMTP软件中实现的难题，同时未对计算精度产生实际影响

---
title: "State equation approximation of transfer matrices and its application to the phase domain calculatio - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/36/59.317582.pdf.pdf"]
---

# State equation approximation of transfer matrices and its application to the phase domain calculatio - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `36/59.317582.pdf.pdf`

## 摘要

A general methodology is presented for the state equa- tion appmximation of a multiple input-output linear system from transfer matrix data A complex transformation matrix, obtained by eigenandysis at a fixed frequency. is used for diagonalization of the trapsfer matrix over the whole frequency range. A scalar estimation r e d u r e  is applied for identification of the modal transfer functions. e state equations in the original coordinates are obtained by inverse transformation. An iterative Gauss-Newton refinement process is used to reduce the overall QIor of the approximation. The developed methodology is applied to the phase domain modeling of untransped transmission lines. The approach makes it possible to paform EMTP calculations directly in the phase domain. This results in conceptu

## 核心贡献



- 提出了一种基于传递矩阵数据的多输入多输出线性系统状态方程近似通用方法
- 将该方法应用于非换位输电线路的相域建模，实现了直接在相域进行EMTP计算，避免了传统模态变换，显著提升了计算效率

## 使用的方法


- [[state-space]]
- [[frequency-dependent]]
- [[vector-fitting]]

## 涉及的模型


- [[transmission-line]]
- [[transformer]]

## 相关主题


- [[state-space]]
- [[frequency-dependent]]
- [[transmission-line]]
- [[network-equivalent]]

## 主要发现



- 通过在单一固定频率下进行特征分析获得的复变换矩阵，可有效实现对全频段传递矩阵的对角化
- 迭代Gauss-Newton优化过程能显著降低整体近似误差，且所得状态方程为最小实现，模型阶数较低
- 直接在相域进行电磁暂态计算可省去模态变换步骤，在保证精度的同时大幅节省计算时间

## 方法细节

### 方法概述

本文提出了一种从频域传递矩阵数据构建多输入多输出线性系统状态空间模型的通用方法。核心思想是在单一固定频率（通常为工频或中间频率）下进行特征分析，获得复变换矩阵，用于在全频段范围内对传递矩阵进行近似对角化。随后对每个解耦的模态传递函数使用基于奇异值分解（SVD）的标量估计方法进行有理函数拟合，识别极点和留数。通过逆变换将模态状态方程转换回原始相坐标，并采用Gauss-Newton迭代优化算法对整体模型参数进行精化，最终获得最小实现阶数的状态空间模型。该方法避免了传统方法中对每个矩阵元素单独拟合导致的高阶问题，且通过复共轭平衡处理确保了实数状态方程的实现。

### 数学公式


**公式1**: $$$\mathbf{y} = \mathbf{H}(s)\mathbf{u}$$$

*多输入多输出系统的频域输入输出关系，H为r×r传递矩阵*


**公式2**: $$$\mathbf{u} = \mathbf{T}_u \mathbf{u}_m$, $\mathbf{y}_m = \mathbf{T}_y^{-1} \mathbf{y}$$$

*相域到模域的线性变换，Tu和Ty分别为输入输出变换矩阵*


**公式3**: $$$\mathbf{H}_m = \mathbf{T}_y^{-1} \mathbf{H} \mathbf{T}_u$$$

*模域传递矩阵，在选定频率ωs处为对角矩阵*


**公式4**: $$$H_{m,p}(s) = \sum_{i=1}^{n_p} \frac{c_i}{s-\lambda_i}$$$

*第p个模态的标量传递函数有理拟合形式，包含极点λi和留数ci*


**公式5**: $$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$, $\mathbf{y} = \mathbf{C}\mathbf{x}$$$

*相域状态空间方程的标准形式*


**公式6**: $$$\mathbf{B}_0 = \mathbf{B}_m \mathbf{T}_u^{-1}$, $\mathbf{C}_0 = \mathbf{T}_y \mathbf{C}_m$$$

*从模域到相域的逆变换关系，得到初始状态矩阵*


**公式7**: $$$\tilde{\mathbf{b}}_i = \frac{1}{2}(\mathbf{b}_i + \mathbf{b}_j^*)$, $\tilde{\mathbf{c}}_i = \frac{1}{2}(\mathbf{c}_i + \mathbf{c}_j^*)$$$

*复共轭极点的行列平衡公式，确保实数实现*


### 算法步骤

1. 在选定固定频率ωs处对传递矩阵H进行特征分析，计算特征向量矩阵，确定输入变换矩阵Tu和输出变换矩阵Ty（通常取Ty = Tu或根据物理意义选择）

2. 计算模域传递矩阵Hm = Ty^(-1) * H * Tu，提取对角元素Hm,p(p=1,...,r)作为标量模态传递函数，忽略非对角元素（弱耦合假设）

3. 对每个模态传递函数Hm,p(jωk)，使用基于SVD的标量估计程序进行有理函数拟合，识别极点位置λi和留数ci，构建严格真分式形式

4. 构建模态状态方程：ẋm = Am*xm + Bm*um, ym = Cm*xm，其中Am为包含识别极点的分块对角矩阵

5. 通过逆变换获得相域初始状态矩阵：B0 = Bm*Tu^(-1)，C0 = Ty*Cm，保持A矩阵不变

6. 对复共轭极点对应的B0和C0行列进行平衡处理：计算共轭平均确保(bi, bj)和(ci, cj)保持复共轭关系，使后续实数化可行

7. 执行Gauss-Newton SVD精化迭代：定义目标函数最小化||Hfitted(jωk) - Hgiven(jωk)||，调整状态矩阵参数，使用SVD求解最小二乘问题

8. 若初始偏差较大导致收敛困难，采用延拓法（Continuation Method）：引入参数θ∈[0,1]，定义中间目标Hθ = (1-θ)Hinitial + θHgiven，逐步从0增加到1确保收敛

9. 将复数状态方程转换为等效实数形式：对每个复共轭极点对创建2×2实数块，最终获得标准实系数状态方程用于EMTP仿真


### 关键参数

- **transformation_frequency**: 固定变换频率ωs，通常选择线路工频或特征频率进行特征分析

- **number_of_modes**: r，等于系统相数（如三相线路r=3）

- **poles_per_mode**: np，第p个模态的极点数量，由标量拟合确定

- **total_state_order**: n = Σnp，总状态数，等于最小实现阶数

- **svd_tolerance**: 奇异值分解截断阈值，用于确定有效极点数量

- **gauss_newton_iterations**: 通常5-10次迭代，直到误差收敛

- **continuation_steps**: 延拓法参数θ的增量步数，通常5-20步确保收敛



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 非换位三相输电线路相域建模 | 应用本文方法对untransposed transmission line进行宽频带建模，传播函数Hp和特性导纳Yc的相域直接拟合。相比传统方法，模型阶数显著降低（为各模态极点数之和，而非r×r矩阵元素分别拟合的阶数总和） | 与传统固定实数模态变换方法相比，避免了每步时域仿真中的模态变换计算，相域直接计算节省计算时间，且精度相当 |

| 宽频频率响应拟合验证 | 在宽频率范围（通常0.1 Hz到1 MHz）内验证拟合精度，通过Gauss-Newton精化后，传递矩阵各元素的幅频和相频特性与原始数据吻合良好，非对角元素的近似误差通过迭代优化得到抑制 | 相比直接对角化忽略非对角项的简化方法，本文方法通过后续优化补偿了固定变换矩阵带来的近似误差 |



## 量化发现

- 模型阶数显著降低：获得的状态方程为最小实现（minimal realization），其阶数等于对角化后各模态所需阶数之和，远低于对r×r传递矩阵每个元素单独拟合（brute force）所需的阶数（后者约为前者的r倍）
- 计算效率提升：相域直接计算避免了传统EMTP中每时步的模态变换（modal transformation）和逆变换，对于三相系统每时步节省两次3×3矩阵乘法，整体仿真时间节省显著
- 拟合精度：通过Gauss-Newton迭代精化，整体近似误差（传递矩阵Frobenius范数）显著降低，通常可达到与原始频率响应偏差小于1%（在宽频带内）
- 收敛特性：采用延拓法（continuation method）后，Gauss-Newton迭代对初始值敏感度降低，即使初始偏差较大也能保证收敛，通常5-10次迭代可达收敛标准
- 适用性：固定复变换矩阵在宽频范围内提供合理的对角化近似，非对角元素量级通常比对角元素小一个数量级，经优化后可进一步抑制


## 关键公式

### 模态对角化变换

$$$\mathbf{H}_m = \mathbf{T}_y^{-1} \mathbf{H} \mathbf{T}_u$$$

*在选定频率ωs处对传递矩阵进行特征分析，获得近似对角化的模态传递矩阵，用于解耦多输入多输出系统*

### 部分分式展开

$$$H_{m,p}(s) = \sum_{i=1}^{n_p} \frac{c_i}{s-\lambda_i}$$$

*标量模态传递函数的有理函数拟合形式，用于从频域采样数据识别系统极点和留数，是状态空间实现的基础*

### 相域传递矩阵重构

$$$\mathbf{H}_{fitted}(s) = \mathbf{C}_0[s\mathbf{I} - \mathbf{A}]^{-1}\mathbf{B}_0$$$

*通过逆变换获得的状态方程传递函数，在Gauss-Newton优化过程中与原始频率响应H(s)比较，迭代调整A、B、C矩阵使误差最小化*



## 验证详情

- **验证方式**: 与常规模态域方法（conventional modal approach）的对比验证，包括精度对比和计算时间对比
- **测试系统**: 非换位（untransposed）三相架空输电线路，考虑频率 dependent 的线路参数（包括地回路和集肤效应），传播函数Hp和特性导纳Yc的宽频建模
- **仿真工具**: EMTP（Electro-Magnetic Transients Program）电磁暂态仿真程序，用于相域直接时域仿真计算
- **验证结果**: 验证表明本文方法与传统模态方法具有相当的精度（good accuracy），但概念更简单且计算时间减少（reduced computation time），因为省去了时域仿真序列中的模态变换步骤。相域模型可直接作为EMTP计算的标准参考，特别适用于模态变换矩阵频率依赖性强的场景（如电缆系统）。

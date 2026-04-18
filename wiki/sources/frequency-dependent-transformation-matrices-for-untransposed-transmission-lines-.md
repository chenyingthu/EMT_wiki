---
title: "Frequency-Dependent Transformation Matrices for Untransposed Transmission Lines using Newton-Raphson - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/59.535695.pdf.pdf"]
---

# Frequency-Dependent Transformation Matrices for Untransposed Transmission Lines using Newton-Raphson - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `19、20、21/EMT_task_20/59.535695.pdf.pdf`

## 摘要

The frequency-dependent aspects of transmission line transformation matrices along with their asymptotic behav- iours at high and low frequencies are thoroughly investigated in this paper. The Newton-Raphson (NR) method for evalu- ating the transformation matrices as smooth functions of fre- quency is introduced. A different technique which utilizes a conventional diagonalization algorithm and a correlation technique for tracking the order of the eigenvectors and ei- genvalues is used to confirm the validity of the NR method. Transformation matrices for typical line configurations are evaluated and discussed. The paper concludes that the NR method is more efficient and appropriate for use in the time domain frequency-dependent line models in the Electromag- netic Transient Program (EMTP). 

## 核心贡献


- 提出基于牛顿拉夫逊法的频变变换矩阵求解算法，实现宽频范围内特征向量的平滑连续计算
- 引入模平方和归一化约束方程，避免特征向量数值溢出，保障有理函数拟合的数值稳定性
- 克服传统对角化算法的模态跳变缺陷，为EMTP时域频变线路模型提供高效计算方案


## 使用的方法


- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[特征值对角化算法|特征值对角化算法]]
- [[模态跟踪技术|模态跟踪技术]]
- [[有理函数拟合|有理函数拟合]]
- [[梯形积分法|梯形积分法]]
- [[卡森公式|卡森公式]]


## 涉及的模型


- [[非换位输电线路|非换位输电线路]]
- [[多回架空线路|多回架空线路]]
- [[频变线路模型|频变线路模型]]
- [[地下电缆|地下电缆]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[时域仿真|时域仿真]]
- [[模态变换|模态变换]]
- [[线路参数拟合|线路参数拟合]]
- [[电磁暂态程序|电磁暂态程序]]
- [[特征值求解|特征值求解]]


## 主要发现


- 牛顿法生成的模态参数平滑连续，可精确拟合为最小相位有理函数，保障时域仿真数值稳定
- 约束牛顿法彻底消除特征向量跳变现象，计算效率与连续性显著优于传统对角化算法
- 简化大地阻抗公式计算结果与卡森积分高度一致，在宽频暂态分析中误差可忽略不计



## 方法细节

### 方法概述

本文针对非换位多回架空线路在宽频范围内模态变换矩阵($T_v$)频变特性导致的传统对角化算法特征值/特征向量跳变问题，提出基于牛顿-拉夫逊(NR)法的直接求解策略。该方法将特征值问题转化为非线性方程组，通过引入特征向量元素平方和归一化约束条件，固定向量尺度并消除数值溢出风险。利用前一频率步的解作为当前步的初值进行迭代，确保全频段(1Hz-1MHz)内$T_v$矩阵元素平滑连续。所得平滑参数可直接采用最小相移有理函数进行拟合，结合梯形积分法无缝嵌入EMTP时域频变线路模型，彻底克服传统方法在复杂拓扑下的模态跟踪失效问题。

### 数学公式


**公式1**: $$$$ \frac{d^2V}{dx^2} = [ZY]V $$$$

*多相输电线路电报方程，描述电压沿线路的传播特性*


**公式2**: $$$$ T_v^{-1} [YZ] T_v = h $$$$

*模态变换对角化方程，$T_v$为电压变换矩阵，$h$为特征值对角阵*


**公式3**: $$$$ (S - \lambda_{kk}U)T_v^{(k)} = 0 $$$$

*单模态非线性齐次方程组，$S=YZ$，用于NR法逐模态求解*


**公式4**: $$$$ \sum_{i=1}^{n} (T_{v,ik})^2 = 1 $$$$

*特征向量归一化约束方程，防止迭代过程中元素趋零导致数值溢出*


**公式5**: $$$$ Z_{e,ij} = j\omega \frac{\mu_0}{2\pi} \ln \frac{D_{ij}'}{D_{ij}} $$$$

*Deri/Dubanton简化大地阻抗公式，替代Carson积分提升计算效率*


### 算法步骤

1. 初始频率求解：在起始频率点采用常规对角化算法（如幂法）计算初始特征值$\lambda$与特征向量$T_v$，作为后续迭代的种子值。

2. 频点步进与初值传递：按设定步长增加频率，将上一频点的收敛解直接作为当前频点NR迭代的初始猜测值，利用连续性加速收敛。

3. 构建非线性方程组：针对每个模态$k$，建立$(S(\omega) - \lambda_{kk}U)T_v^{(k)} = 0$，其中$S=YZ$为频变乘积矩阵，包含$n$个方程。

4. 引入约束条件：附加特征向量元素平方和等于1的约束方程，将未知数固定为$n+1$个（$n$个向量元素+1个特征值），消除尺度任意性。

5. 雅可比矩阵构造与迭代：基于上述$n$个齐次方程与1个约束方程构造$(n+1)\times(n+1)$雅可比矩阵，执行牛顿-拉夫逊迭代直至残差小于设定容差。

6. 全频段遍历与拟合：重复步进与迭代覆盖1Hz至1MHz全频段，获取平滑连续的$T_v(\omega)$与传播函数，随后采用最小相移有理函数进行频域拟合，为EMTP时域实现做准备。


### 关键参数

- **频率范围**: 1 Hz - 1 MHz

- **约束条件**: 特征向量元素平方和归一化（$\sum T_{v,ik}^2 = 1$）

- **拟合类型**: 最小相移有理函数（实负极点与零点）

- **大地阻抗近似**: Deri/Dubanton简化对数公式

- **初始算法**: 幂法(Power Method)

- **地线处理**: 低于塔距半波长时假设零电位，通过高斯消元降阶



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 垂直双回非换位架空线路（6相导线+地线） | 系统经高斯消元降阶为6个模态，NR法计算出的$T_v$矩阵第一列元素幅值在全频段内平滑变化，有理函数拟合曲线与精确解高度重合，最大拟合误差严格控制在1.0%以内。 | 相较于传统对角化算法在特定频点出现的特征值交换与向量跳变，NR法实现零跳变连续跟踪，计算效率与数值稳定性显著提升，完全满足EMTP时域卷积要求。 |



## 量化发现

- 全频段(1Hz-1MHz)模态变换矩阵元素有理函数拟合最大误差<1.0%
- 简化大地阻抗公式在kHz频段与Carson积分结果偏差仅百分之几，对宽频暂态计算影响可忽略
- NR法彻底消除传统算法的模态跳变现象，特征向量连续性满足最小相移有理函数拟合条件
- 地线在低于塔距半波长频率下可等效为零电位，通过高斯消元将模态数降至相导线数量，计算量显著降低


## 关键公式

### 模态特征值非线性方程

$$$$ (S - \lambda_{kk}U)T_v^{(k)} = 0 $$$$

*用于牛顿-拉夫逊法直接求解特定模态的特征值与特征向量，避免全局对角化导致的模态交叉*

### 特征向量归一化约束

$$$$ \sum_{i=1}^{n} (T_{v,ik})^2 = 1 $$$$

*固定特征向量尺度，防止迭代过程中元素趋零导致数值溢出，保障雅可比矩阵良态*

### 简化大地回路阻抗公式

$$$$ Z_{e,ij} = j\omega \frac{\mu_0}{2\pi} \ln \frac{D_{ij}'}{D_{ij}} $$$$

*替代Carson积分计算频变大地阻抗，兼顾计算效率与宽频暂态精度*



## 验证详情

- **验证方式**: 对比分析与有理函数拟合验证
- **测试系统**: 典型垂直双回非换位架空线路（6相导线+地线，导线直径4×3.84cm，间距50cm，地线直径1.75cm）
- **仿真工具**: 自定义牛顿-拉夫逊求解程序、EMTP（电磁暂态程序）
- **验证结果**: NR法生成的频变参数平滑无跳变，拟合函数与精确解最大偏差<1.0%；简化大地阻抗公式与Carson积分高度一致；验证了该方法在EMTP时域频变线路模型中实现梯形积分数值稳定的可行性与高效性。

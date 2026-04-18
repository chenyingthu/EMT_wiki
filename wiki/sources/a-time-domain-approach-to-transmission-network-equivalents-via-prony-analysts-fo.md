---
title: "A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS VIA PRONY ANALYSTS FOR ELECTROMAGNETIC TR - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/04/59.476042.pdf.pdf"]
---

# A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS VIA PRONY ANALYSTS FOR ELECTROMAGNETIC TR - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `04/59.476042.pdf.pdf`

## 摘要

This paper presents a method of obtaining transmission network equivalents from the network's response to a pulse excitation signal. Proposed metho(d is based on modal decomposition representation for- the large-scale interconnected system. In this framework we use Prony analysis to identify the network function of the system and to decompose the large system into a parallel combination of simple first-order systems. As a result network function of the transmission network can be identified easily, and Thevenin- type of discrete-time filter model can be generated. It can reproduce the driving-point impedance characteristic of the network. Furthermore proposed model can be implemented into the EMTP in a direct manner. The simulation results with the full system representation and the develo

## 核心贡献


- 提出基于时域脉冲响应与Prony分析的输电网络等值方法，避免频域迭代拟合。
- 利用模态分解将大规模系统转化为简单一阶系统并联，简化网络函数辨识过程。
- 构建可直接嵌入EMTP的戴维南型离散时间滤波器模型，精确复现驱动点阻抗。


## 使用的方法


- [[prony-analysis|Prony分析]]
- [[模态分解|模态分解]]
- [[线性预测模型|线性预测模型]]
- [[最小二乘估计|最小二乘估计]]
- [[有理函数逼近|有理函数逼近]]
- [[时域系统辨识|时域系统辨识]]


## 涉及的模型


- [[输电网络等值模型|输电网络等值模型]]
- [[戴维南等效电路|戴维南等效电路]]
- [[离散时间滤波器模型|离散时间滤波器模型]]
- [[一阶并联系统|一阶并联系统]]
- [[外部系统等值|外部系统等值]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[网络等值|网络等值]]
- [[时域建模|时域建模]]
- [[驱动点阻抗特性|驱动点阻抗特性]]
- [[大规模系统降阶|大规模系统降阶]]
- [[emtp实现|EMTP实现]]


## 主要发现


- 仿真结果表明，所提等值模型与完整系统响应高度吻合，验证了时域辨识精度。
- 离散时间滤波器模型能准确复现宽频带暂态信号下的驱动点阻抗频率特性。
- 该方法可直接集成至EMTP中，显著降低大规模电网电磁暂态仿真计算负担。



## 方法细节

### 方法概述

本文提出一种基于时域脉冲响应与Prony分析的输电网络等值方法。首先将外部系统视为线性时不变网络，在边界母线注入短时电流脉冲激励，利用EMTP获取电压响应序列。随后采用Prony分析对响应进行模态分解，通过奇异值分解(SVD)确定有效模型阶数，构建线性预测模型并求解特征多项式根与信号留数。结合脉冲激励特性，将信号留数转换为网络函数（驱动点阻抗）留数，实现大规模系统向一阶并联系统的降阶。最终将辨识出的有理函数转化为离散时间戴维南等效滤波器模型，该模型可直接嵌入EMTP进行电磁暂态仿真，避免了传统频域迭代拟合的复杂性，同时精确复现宽频带暂态特性。

### 数学公式


**公式1**: $$$y(k) = \sum_{i=1}^{n} a_i y(k-i)$$$

*线性预测模型(LPM)方程，用于建立当前采样值与历史采样值的线性关系，是Prony分析的第一步。*


**公式2**: $$$z^n - \sum_{i=1}^{n} a_i z^{n-i} = 0$$$

*特征多项式方程，通过求解该方程的根获得系统的离散特征值（模态频率与阻尼）。*


**公式3**: $$$R_l = B_l \frac{1 - \lambda_l^d}{1 - \lambda_l}$$$

*信号留数$B_l$到网络函数留数$R_l$的转换公式，其中$d$为脉冲持续时间，用于从响应信号反推系统传递函数。*


**公式4**: $$$v(n) = Z_{eq} i(n) + Hist(n-1)$$$

*离散时间戴维南等效递推公式，将外部系统等效为等效阻抗$Z_{eq}$与历史电压源$Hist$的串联，便于EMTP直接调用。*


### 算法步骤

1. 断开研究子系统与外部系统，关闭外部系统所有独立源，确保仅保留无源网络特性。

2. 在边界母线注入宽度为1个采样步长的矩形电流脉冲激励，利用EMTP计算并记录边界节点的电压响应序列$y(k)$。

3. 构建线性预测模型的数据矩阵$X$，对其进行奇异值分解(SVD)，根据显著奇异值的数量分布确定有效模型阶数$p$，剔除噪声主导的微小奇异值。

4. 利用最小二乘法求解LPM系数向量$a_i$，构建特征多项式并采用圆算术算法(Circular Arithmetic)高效求根，得到系统离散特征值$\lambda_l$。

5. 基于特征值构建范德蒙矩阵$A$，通过QR分解进行最小二乘估计，求解各模态的信号留数$B_l$。

6. 根据脉冲持续时间$d$，应用转换公式$R_l = B_l (1-\lambda_l^d)/(1-\lambda_l)$将信号留数映射为网络函数（驱动点阻抗）留数。

7. 剔除留数幅值接近零的冗余模态，得到最优低阶模型，将各一阶模态并联组合，最终整理为离散时间戴维南等效滤波器结构。


### 关键参数

- **采样步长**: 1.0e-4 s

- **有效频率范围**: 0~5 kHz

- **初始LPM测试阶数**: 50~85

- **SVD识别有效阶数p**: 74

- **最终等值模型阶数q**: 70

- **脉冲持续时间**: 1个采样步长

- **测试计算机硬件**: IBM PC 486DX2微处理器



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 边界母线阶跃响应验证 | 在边界节点施加阶跃电流激励，对比全系统与等值模型的电压响应波形。等值模型阶跃响应曲线与完整系统高度重合，辨识误差约为4.36e-4。 | 等值模型在阶跃暂态下的波形偏差极小，验证了驱动点阻抗复现精度，且模型阶数从>74阶优化至70阶，未损失关键动态特性。 |

| 200km空载线路合闸暂态 | 对研究子系统（200km开路输电线路）进行合闸操作，记录2个周期（33.3ms）的过电压暂态过程。等值模型输出波形与全系统EMTP仿真结果完全一致。 | 等值模型仿真耗时0.53秒，全系统（含频变分布参数线路）耗时19.8秒，计算速度提升约37.4倍，显著降低大规模电网暂态仿真负担。 |



## 量化发现

- 模型辨识均方根误差约为4.36e-4，证明时域Prony拟合精度极高。
- 通过SVD阈值截断，将初始高阶模型降阶至70阶，剔除近零留数模态后仍保持全频段阻抗特性。
- 等值模型暂态仿真计算时间仅为全系统的2.68%（0.53s vs 19.8s），计算效率提升约37倍。
- 在1.0e-4s采样步长下，有效复现0~5kHz宽频带驱动点阻抗特性，满足电磁暂态高频分析需求。


## 关键公式

### 离散时间戴维南等效递推方程

$$$v(n) = Z_{eq} i(n) + Hist(n-1)$$$

*用于EMTP时域步进求解，将外部系统等效为当前时刻等效阻抗与历史电压源的叠加，避免频域卷积计算。*

### 脉冲激励下的网络函数留数转换公式

$$$R_l = B_l \frac{1 - \lambda_l^d}{1 - \lambda_l}$$$

*在已知Prony信号留数$B_l$和脉冲宽度$d$时，用于反推系统传递函数的部分分式展开系数。*

### 线性预测系数最小二乘估计

$$$\hat{\mathbf{a}} = (X)^+ \mathbf{z}$$$

*通过Moore-Penrose伪逆求解LPM系数，结合SVD保证在矩阵秩亏或含噪情况下的数值稳定性。*



## 验证详情

- **验证方式**: 时域仿真对比验证（阶跃响应与线路合闸暂态波形对比）
- **测试系统**: 单相测试系统，含200km开路输电线路（研究子系统）及外部互联电网（等值对象），边界节点为Node 4
- **仿真工具**: EMTP/ATP（用于生成响应数据与全系统对比仿真），自编Prony分析程序（模型参数辨识与等值生成）
- **验证结果**: 等值模型在宽频暂态激励下能精确复现原系统驱动点阻抗特性，阶跃响应与合闸过电压波形与全系统仿真高度吻合。模型阶数优化至70阶，计算耗时大幅降低，验证了时域辨识方法的精度、数值稳定性及工程实用性。

---
title: "Noda | A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Noda - 2007 - A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi.pdf"]
---

# Noda | A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi

**作者**: 
**年份**: 2007
**来源**: `01/Noda - 2007 - A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi.pdf`

## 摘要

—Previously, a method for identifying a multiphase net- work equivalent for electromagnetic transient calculations using partitioned frequency response has been proposed. The method ac- curately and robustly identiﬁes an equivalent of the target network by dividing its frequency response into sections, but no speciﬁc al- gorithm for the frequency-region partitioning has been proposed. To make the entire identiﬁcation process automatic, this letter pro- poses a binary partitioning algorithm. Index Terms—Electromagnetic transient analysis, equivalent circuits, frequency response, interconnected power systems, power system modeling, power system simulation. I. INTRODUCTION E LECTROMAGNETIC TRANSIENT (EMT) simulations have become crucial for the design and operation of a power system. For redu

## 核心贡献


- 提出二分频率区域划分算法，实现多相网络等值辨识全自动化。
- 基于拟合精度与幅值极小值自适应划分频段，避免有理拟合病态。
- 结合增强型有理拟合与矩阵部分分式展开，实现宽频导纳高精度等值。


## 使用的方法


- [[增强型有理拟合|增强型有理拟合]]
- [[矩阵部分分式展开-mpfe|矩阵部分分式展开(MPFE)]]
- [[最小二乘法|最小二乘法]]
- [[二分频率划分算法|二分频率划分算法]]
- [[极点辨识|极点辨识]]


## 涉及的模型


- [[多相网络等值模型|多相网络等值模型]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[同步发电机|同步发电机]]
- [[导纳矩阵|导纳矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络等值|网络等值]]
- [[频率相关建模|频率相关建模]]
- [[频域系统辨识|频域系统辨识]]
- [[降阶建模|降阶建模]]


## 主要发现


- 算法在1%误差容限下自动划分9个频段，极点辨识精度极高。
- MPFE模型精确复现多相导纳矩阵各元素，频域拟合偏差极小。
- 等值模型用于开关暂态仿真，时域波形与全系统详细模型几乎一致。



## 方法细节

### 方法概述

本文提出一种基于二分法的频率区域自动划分算法，用于多相网络等值模型的频域辨识。该方法采用递归试错策略：首先对整个频带应用增强型有理拟合（enhanced rational fitting）进行极点识别；若拟合精度未满足预设容差，则将频带二分并递归处理子频段，直至所有子频段达到精度要求。为避免相邻频段识别出相同极点，边界确定策略首先将分界点设于频段中点，随后搜索距离中点最近的频率响应幅值局部最小值，若该最小值位于半带宽范围内，则将边界调整至该极值点，否则保持中点分界。极点确定后，利用全部频响数据通过最小二乘法计算各极点的留数矩阵，最终构建矩阵部分分式展开（MPFE）模型。该方法通过自适应划分解决了宽频范围内有理拟合的病态条件问题，实现了网络等值辨识的全自动化。

### 数学公式


**公式1**: $$\mathbf{H}(s) = \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D}$$

*矩阵部分分式展开(MPFE)模型，其中$\mathbf{H}(s)$为$N\times N$导纳矩阵传递函数，$p_m$为识别得到的极点，$\mathbf{R}_m$为对应的$N\times N$留数矩阵，$\mathbf{D}$为常数矩阵。*


**公式2**: $$\text{tr}(\mathbf{H}) = \sum_{i=1}^{N} h_{ii}$$

*矩阵迹（trace）计算，用于极点识别过程。通过对导纳矩阵的迹进行有理拟合来识别系统极点，避免直接处理矩阵带来的复杂性。*


### 算法步骤

1. 初始化：将整个频率响应范围设为当前处理区域，设定相对误差容限（如1%）。

2. 极点识别尝试：对当前频率区域应用增强型有理拟合（enhanced rational fitting），尝试识别该区域的极点。

3. 精度检验：评估拟合结果与原始频率响应的偏差，检查是否满足预设的相对误差容限。

4. 终止条件：若精度满足要求，记录该区域识别得到的极点，该区域处理完成。

5. 区域划分：若精度不满足，将当前区域划分为两个子区域。首先计算当前频段的中点作为初始边界。

6. 边界优化：从中点位置向两侧搜索最近的频率响应幅值$|\mathbf{H}|$的局部最小值。若找到的局部最小值距离中点小于当前频段半带宽，则将边界调整至该局部最小值；否则保持边界在中点。

7. 递归处理：对生成的两个子区域分别递归执行步骤2-6，直至所有子区域均满足精度要求。

8. 留数计算：收集所有子区域识别得到的极点$p_m$，利用整个频率范围内的原始数据，通过最小二乘法计算各极点的留数矩阵$\mathbf{R}_m$和常数矩阵$\mathbf{D}$，构建完整的MPFE模型。


### 关键参数

- **relative_tolerance**: 1%（相对误差容限，用于判断拟合精度是否满足要求）

- **frequency_sections**: 9（在1%容限下，测试案例最终被划分的频段数量）

- **bandwidth_threshold**: 半带宽（边界调整时判断局部最小值是否'临近'中点的距离阈值）

- **matrix_dimension**: N×N（多相网络导纳矩阵维度，N为相数或端口数）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 500-kV三相测试网络导纳等值辨识 | 对包含3台发电机及变压器、5个负荷、1组带变压器的电容器组、6回双回路输电线路的500-kV测试网络进行等值。从Bus A看入的三相导纳矩阵被成功等值，频率响应被自动划分为9个频段。导纳矩阵元素(1,1)和(1,2)的频域拟合偏差极小，原始曲线与拟合曲线几乎无法区分。 | 与未划分频段的直接拟合方法相比，避免了宽频拟合的病态条件；与完整系统详细模型的开关暂态仿真结果相比，时域波形几乎完全一致。 |



## 量化发现

- 在1%的相对误差容限下，算法自动将频率响应划分为9个频段
- 极点识别过程中，拟合曲线与原始频率响应曲线的偏差太小以至于在图中无法区分
- 导纳矩阵各元素的MPFE模型复现精度极高，频域偏差无法目视分辨
- 边界位置确定策略中，局部最小值搜索范围限制在频段半带宽（half the bandwidth）内
- 等值模型在开关暂态仿真中复现了与完整系统详细模型几乎完全一致的结果


## 关键公式

### 矩阵部分分式展开(MPFE)模型

$$\mathbf{H}(s) = \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D}$$

*作为最终的网络等值模型，用于EMT仿真。其中极点$p_m$通过二分频带划分和有理拟合识别，留数矩阵$\mathbf{R}_m$和常数项$\mathbf{D}$通过最小二乘法确定。*



## 验证详情

- **验证方式**: 频域精度验证与时域仿真对比验证。首先验证MPFE模型对原始频率响应的拟合精度，然后将等值模型应用于开关暂态仿真，与完整系统的详细模型进行时域结果对比。
- **测试系统**: 500-kV测试网络，包含3台同步发电机及配套变压器、5个负荷、1组带变压器的电容器组、6回双回路输电线路。网络采用完整三相模型表示，考虑了元件的频率依赖特性和三相不平衡性。
- **仿真工具**: 未明确指定具体商业软件名称，但涉及电磁暂态(EMT)仿真计算和频域系统辨识算法实现。
- **验证结果**: 在频域，MPFE模型精确复现了原始导纳矩阵的所有元素，特别是图3所示的(1,1)和(1,2)元素，拟合曲线与原始数据重合度极高。在时域，将辨识得到的等值模型应用于开关暂态仿真，其波形与完整系统详细模型的仿真结果几乎完全一致，验证了等值模型的准确性。

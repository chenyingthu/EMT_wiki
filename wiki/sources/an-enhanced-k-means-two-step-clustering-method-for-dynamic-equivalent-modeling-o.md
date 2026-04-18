---
title: "An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on LVRT characteristics"
type: source
authors: ['Junhua Xu']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112367. doi:10.1016/j.epsr.2025.112367"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Xu et al. - 2026 - An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms ba.pdf"]
---

# An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on LVRT characteristics

**作者**: Junhua Xu
**年份**: 2025
**来源**: `07&08/Xu et al. - 2026 - An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms ba.pdf`

## 摘要

0378-7796/© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on LVRT characteristics School of Electrical Engineering, Guangxi University, located in Nanning, China To enhance the accuracy of dynamic equivalent models for wind farms utilizing doubly-fed induction generators

## 核心贡献


- 提出基于有功出力与LVRT响应的两步聚类框架，实现风机精准预分类
- 融合K-Means++初始化、KD树加速与DBI指标，实现聚类参数自适应
- 构建计及LVRT特性的风电场等值模型，突破传统方法忽略故障动态局限


## 使用的方法


- [[两步聚类法|两步聚类法]]
- [[增强k-means算法|增强K-means算法]]
- [[k-means-初始化|K-Means++初始化]]
- [[kd树加速搜索|KD树加速搜索]]
- [[davies-bouldin指数|Davies-Bouldin指数]]
- [[动态等值建模|动态等值建模]]
- [[矢量控制|矢量控制]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[风电场|风电场]]
- [[转子侧变流器|转子侧变流器]]
- [[网侧变流器|网侧变流器]]
- [[电磁暂态详细模型|电磁暂态详细模型]]


## 相关主题


- [[动态等值建模|动态等值建模]]
- [[低电压穿越|低电压穿越]]
- [[风电场聚合|风电场聚合]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力系统稳定性分析|电力系统稳定性分析]]


## 主要发现


- 等值模型在故障期间与详细模型动态响应高度一致，仿真精度超过98%
- 相比传统详细模型，等效模型仿真计算时间大幅缩减约90%，显著提升效率
- 算法自动确定最佳聚类数与初始中心，有效消除人工设定参数的主观误差



## 方法细节

### 方法概述

本文提出一种基于低电压穿越（LVRT）特性的增强型K-means两步聚类风电场动态等值建模方法。首先，根据风机实时有功出力与LVRT动态响应特征，将全场风机划分为具有聚类特性（启动区、恒速区、恒功率区）与无聚类特性（MPPT区）两类。针对MPPT区风机，采用增强型K-means算法进行二次聚类。该算法融合K-Means++概率初始化策略优化初始中心选择，引入KD树索引加速高维数据最近邻搜索，并利用Davies-Bouldin指数（DBI）自适应确定最优聚类数，克服传统算法依赖人工设定参数与易陷局部最优的缺陷。最后，基于聚类结果按容量、阻抗、控制参数等比例聚合计算等值机参数，构建多机等值模型，实现故障期间动态响应的高精度复现与仿真效率的大幅提升。

### 数学公式


**公式1**: $$$$WCSS = \sum_{i=1}^{K} \sum_{x \in C_i} \| x - \mu_i \|^2$$$$

*聚类内平方和（WCSS）目标函数，用于衡量数据点到所属聚类中心的距离总和，指导K-means迭代优化。*


**公式2**: $$$$Var(X_d) = \frac{1}{a-1} \sum_{i=1}^{a} (v_{di} - \mu_d)^2$$$$

*KD树构建时的维度方差计算公式，用于选择方差最大的维度作为当前分裂轴。*


**公式3**: $$$$P(x) = \frac{D^2(x)}{\sum_{y \in T \setminus t} D^2(y)}$$$$

*K-Means++初始化中下一个聚类中心的概率选择公式，距离现有中心越远的点被选中的概率越大。*


**公式4**: $$$$DBI = \frac{1}{K} \sum_{i=1}^{K} \max_{j \neq i} \frac{S_i + S_j}{\| \mu_i - \mu_j \|}$$$$

*Davies-Bouldin指数，用于评估聚类质量，值越小表示类内越紧凑、类间分离度越高，用于自适应确定最优K值。*


**公式5**: $$$$E = \sqrt{\frac{1}{m} \sum_{i=1}^{m} \left( \frac{A_i - A_{eq,i}}{A_i} \right)^2}$$$$

*均方根误差（RMSE）评估公式，用于量化等值模型与详细模型在电气量动态响应上的偏差。*


### 算法步骤

1. 步骤1：构建KD树。计算数据集各维度方差，选取方差最大维度作为分裂轴，按中位数划分左右子树，递归构建直至子树节点数≤预设阈值（5）。

2. 步骤2：KD树加速分配。以各聚类中心为查询点在KD树中执行最近邻搜索，通过递归比较与回溯批量分配数据点，将分配阶段时间复杂度从O(a·K·D)降至O(a·log(a)·D)。

3. 步骤3：K-Means++概率初始化。随机选取首个中心，利用KD树计算剩余点到已选中心的最小欧氏距离D(x)，按概率P(x)=D²(x)/∑D²(y)随机采样下一个中心，重复至选满K个中心。

4. 步骤4：迭代聚类优化。基于WCSS目标函数分配数据点至最近中心，更新聚类中心坐标，循环迭代直至目标函数收敛或达到最大迭代次数。

5. 步骤5：DBI优选聚类数。遍历候选K值（K∈{2,3,…,a}），对每个K执行步骤3-4并计算DBI值，选取DBI最小值对应的K作为最优二次聚类数，完成最终风机分区。


### 关键参数

- **KD树节点阈值**: 5

- **聚类特征维度D**: 3

- **聚类特征变量**: 有功出力P、风速Vw、风能利用系数Cp

- **无功支撑系数K1**: 1.5~3 (依电网规范)

- **RSC电流限值ir_lim**: 1.6 p.u.

- **尾流模型推力系数CT**: 0.8

- **尾流衰减系数∂**: 0.075

- **风机叶片半径r0**: 38 m

- **故障电压跌落深度**: 0.2 p.u.

- **故障持续时间**: 625 ms



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 20台DFIG风电场三相电压跌落故障仿真 | 在PCC点施加0.2 p.u.三相电压跌落（持续625 ms），等值模型（Method A）的有功、无功及电压动态响应曲线与详细模型高度吻合，RMSE误差极低。 | 仿真计算时间较详细模型缩减约90%，单次聚类迭代耗时仅为传统K-means的25.1%（搜索时间减少约75%）。 |

| 不同聚类算法对比验证 | 对比传统K-means（Method B）、模糊C均值（Method C）与单机等值（Method D），所提方法在MPPT区风机分组上物理可解释性最强，EM1仅包含低风速机组，EM3聚合大部分MPPT机组。 | 聚类结果紧凑度与一致性显著优于Method B（存在功能相似机组碎片化分散）与Method C（遗漏相似机组），为高保真等值奠定基础。 |



## 量化发现

- 等值模型在故障期间动态响应精度超过98%（RMSE误差<2%）
- 仿真计算时间大幅缩减约90%，显著提升高比例风电系统稳定性分析效率
- KD树加速使聚类单次迭代耗时降至传统K-means的25.1%（数据搜索时间减少约75%）
- DBI指标自动确定最优二次聚类数K=2，实现类内紧凑与类间分离的最佳平衡
- 等值机参数聚合公式严格遵循容量、阻抗、电容的N倍/N分之一比例缩放，保证电磁暂态特性一致性


## 关键公式

### 聚类内平方和（WCSS）

$$$$WCSS = \sum_{i=1}^{K} \sum_{x \in C_i} \| x - \mu_i \|^2$$$$

*用于K-means算法迭代过程中评估聚类紧密度并更新聚类中心*

### Davies-Bouldin指数（DBI）

$$$$DBI = \frac{1}{K} \sum_{i=1}^{K} \max_{j \neq i} \frac{S_i + S_j}{\| \mu_i - \mu_j \|}$$$$

*用于自适应确定最优聚类数K，替代人工经验设定*

### 等值机参数聚合公式

$$$$X_{m,eq} = \frac{X_m}{N}, R_{s,eq} = \frac{R_s}{N}, C_{eq} = NC, Z_{T,eq} = \frac{Z_T}{N}$$$$

*将N台同聚类风机聚合为单台等值机时，电抗/电阻/变压器阻抗除以N，直流电容乘以N*

### 均方根误差（RMSE）

$$$$E = \sqrt{\frac{1}{m} \sum_{i=1}^{m} \left( \frac{A_i - A_{eq,i}}{A_i} \right)^2}$$$$

*用于量化评估等值模型与详细模型在故障期间电气量动态响应的偏差*



## 验证详情

- **验证方式**: 电磁暂态仿真对比分析
- **测试系统**: 中国南方某实际风电场拓扑，包含20台2.25 MW DFIG机组、集电线路、35/220 kV升压变压器及PCC节点
- **仿真工具**: PSCAD/EMTDC (v4.6.2)
- **验证结果**: 在0.2 p.u.三相电压跌落故障下，所提两步聚类等值模型动态响应与详细模型高度一致，精度>98%，计算时间减少90%。聚类结果物理可解释性强，显著优于传统K-means与模糊C均值法，验证了算法在LVRT工况下的有效性与工程实用性。

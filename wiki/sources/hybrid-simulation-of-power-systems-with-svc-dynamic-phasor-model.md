---
title: "Hybrid simulation of power systems with SVC dynamic phasor model"
type: source
authors: ['"E Zhijun', 'D.Z. Fang', 'K.W. Chan', 'S.Q. Yuan"']
year: 2009
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/22/Zhijun 等 - 2009 - Hybrid simulation of power systems with SVC dynamic phasor model.pdf"]
---

# Hybrid simulation of power systems with SVC dynamic phasor model

**作者**: "E Zhijun, D.Z. Fang, K.W. Chan 等
**年份**: 2009
**来源**: `22/Zhijun 等 - 2009 - Hybrid simulation of power systems with SVC dynamic phasor model.pdf`

## 摘要

Hybrid simulation of power systems with SVC dynamic phasor model E Zhijun a, D.Z. Fang a,*, K.W. Chan b, S.Q. Yuan a,b a Key Laboratory of Power System Simulation and Control of Ministry of Education of China, Tianjin University, 300072 Tianjin, China b Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong, China A novel hybrid method for simulation of power systems equipped with static var compensators (SVC) is

## 核心贡献


- 提出SVC单相动态相量模型，设计其与机电暂态子系统的混合仿真接口算法
- 采用较大积分步长求解动态相量方程，显著提升含SVC大电网的混合仿真速度
- 建立仅含基波与五次谐波的TCR动态相量模型，兼顾波形精度与计算效率


## 使用的方法


- [[动态相量法|动态相量法]]
- [[混合仿真|混合仿真]]
- [[接口算法|接口算法]]
- [[单相等效建模|单相等效建模]]
- [[状态空间平均法|状态空间平均法]]


## 涉及的模型


- [[svc|SVC]]
- [[tcr|TCR]]
- [[交流子系统|交流子系统]]
- [[rlc滤波器|RLC滤波器]]
- [[机电暂态模型|机电暂态模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[动态相量建模|动态相量建模]]
- [[机电-电磁暂态混合|机电-电磁暂态混合]]
- [[facts设备仿真|FACTS设备仿真]]
- [[大电网动态仿真|大电网动态仿真]]


## 主要发现


- 9节点与39节点系统测试表明，SVC动态相量模型波形精度与EMTP基准高度一致
- 较大积分步长下的动态相量仿真在保证精度的同时，大幅降低混合仿真计算耗时
- 忽略五次以上谐波的简化模型仍能准确反映SVC非线性动态特性，验证了方法有效性



## 方法细节

### 方法概述

提出一种基于动态相量（DP）理论的机电-电磁混合仿真新方法。将含SVC的电力系统划分为机电暂态（TSP）交流子系统和SVC动态相量子系统。针对SVC中的晶闸管控制电抗器（TCR），建立仅考虑基波与五次谐波的单相动态相量模型，利用时变傅里叶级数系数近似非线性开关波形。通过推导TCR、RL滤波电路及电容的DP状态方程，实现用较大积分步长求解SVC内部电磁暂态过程。设计DP模型与TSP子系统的接口算法，在接口母线处进行相量与时域量的双向数据交互，从而在保证SVC电压/电流波形精度的同时，显著提升大电网混合仿真的计算效率。

### 数学公式


**公式1**: $$$X_k(t) = \frac{c}{T} \int_{t-T}^{t} x(s)e^{-jk\omega_s s} ds$$$

*动态相量定义式，通过滑动窗口傅里叶变换提取时域波形的k次时变复系数*


**公式2**: $$$\frac{dX_k}{dt}(t) = \left[\frac{dx}{dt}\right]_k(t) - jk\omega_s X_k(t)$$$

*动态相量微分性质，用于将时域微分方程转换为相量域代数/微分方程*


**公式3**: $$$\langle xy \rangle_k = \sum_{i=-\infty}^{\infty} \langle x \rangle_{k-i} \langle y \rangle_i$$$

*动态相量乘积性质，用于处理开关函数与电压/电流的非线性乘积项*


**公式4**: $$$C\frac{dV_k}{dt} = -jk\omega_s C V_k + I_{lk} - I_k$$$

*TCR电容电压的k次动态相量状态方程*


**公式5**: $$$L\frac{dI_k}{dt} = V_{1,k} - jk\omega_s L I_k - R I_k$$$

*RL滤波电路电感电流的k次动态相量状态方程*


### 算法步骤

1. 系统划分与初始化：将含SVC的大电网划分为TSP交流子系统（采用单相机电暂态模型）和SVC动态相量子系统（采用单相DP模型），设定TSP步长（0.01~0.02 s）与DP求解步长，初始化各状态变量与接口边界条件。

2. TSP子系统求解：在当前仿真时刻，利用接口母线边界条件，采用隐式积分法求解交流网络代数方程与发电机微分方程，获得下一时刻的母线电压相量及网络状态。

3. 接口数据转换与注入：将TSP输出的接口母线电压通过相量提取算法转换为SVC DP模型所需的基波（k=1）与五次谐波（k=5）动态相量输入，作为SVC子系统的边界激励。

4. SVC DP模型步进求解：基于TCR开关函数与滤波电路的DP状态方程（k=1,5），采用较大步长数值积分求解SVC内部电容电压、电感电流及线路电流的动态相量，并通过时域重构公式恢复电压/电流波形。

5. 接口反馈与全局迭代：将SVC DP模型计算得到的等效注入电流/功率反馈至TSP子系统，修正接口母线导纳矩阵或作为电流源注入，推进至下一全局仿真步长，循环执行直至仿真结束。


### 关键参数

- **TSP积分步长**: 0.01 s 或 0.02 s (50Hz系统)

- **EMTP基准步长**: 50 μs

- **DP模型考虑谐波阶数**: k = 1 (基波), k = 5 (五次谐波)

- **TCR开关函数s(t)**: 导通时为1，关断时为0

- **滤波器参数**: Rf (电阻), Lf (电感), Cf (电容)

- **TCR控制参数**: 触发角α, 导通角σ



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 3机9节点测试系统 | 在标准扰动下，SVC单相动态相量模型输出的电压与电流波形与DCG/EMTP全电磁暂态基准结果高度吻合，验证了DP模型在局部非线性设备仿真中的波形捕捉能力。 | 在积分步长从50 μs提升至0.01~0.02 s（约200~400倍）的条件下，波形精度与全EMTP仿真保持一致，计算耗时显著降低。 |

| 新英格兰10机39节点测试系统 | 大规模系统测试表明，混合仿真成功捕捉SVC的快速无功调节动态，接口处未出现传统TSP-EMTP混合常见的相位不连续与直流偏移现象。 | 相比传统全EMTP仿真，内存占用大幅减少，仿真速度显著提升，同时保留了FACTS设备关键谐波（1次与5次）的动态响应精度。 |



## 量化发现

- 积分步长提升约200~400倍（从EMTP的50 μs提升至TSP兼容的0.01~0.02 s），大幅降低CPU计算时间。
- 谐波截断至5次（仅保留k=1和k=5）仍能准确反映SVC非线性动态特性，忽略7次及以上谐波对波形精度影响极小。
- 混合仿真有效消除了传统TSP-EMTP接口处的相位不连续与直流偏移误差，接口数据交互精度满足大电网动态分析要求。
- 在9节点与39节点系统中，SVC动态相量模型波形与EMTP基准高度一致，验证了单相等效建模在大规模系统仿真中的可行性。


## 关键公式

### 动态相量微分变换公式

$$$\frac{dX_k}{dt}(t) = \left[\frac{dx}{dt}\right]_k(t) - jk\omega_s X_k(t)$$$

*用于将TCR、RL电路及电容的时域微分方程转换为动态相量域状态方程，是构建DP模型的核心数学基础*

### 开关函数乘积动态相量展开式

$$$\langle sv \rangle_k = \sum_{l \in \{-5,-1,1,5\}} S_{k-l} V_l$$$

*用于处理TCR晶闸管开关动作与电容电压的非线性耦合项，实现开关过程在相量域的精确等效*

### RL滤波电路动态相量状态方程

$$$L\frac{dI_k}{dt} = V_{1,k} - jk\omega_s L I_k - R I_k \quad (k=1,5)$$$

*描述SVC滤波支路电感电流在基波与五次谐波下的动态演化，用于较大步长下的数值积分求解*



## 验证详情

- **验证方式**: 仿真对比分析（自研混合仿真程序与商业电磁暂态软件基准结果对比）
- **测试系统**: IEEE 3机9节点标准测试系统、新英格兰10机39节点标准测试系统
- **仿真工具**: 自研SVC动态相量混合仿真程序 vs DCG/EMTP（商业电磁暂态程序）
- **验证结果**: 在两种标准测试系统中，SVC单相动态相量模型的电压/电流波形响应与EMTP全电磁暂态基准高度一致；混合仿真在保留EMTP波形精度的同时，通过增大积分步长有效克服了传统TSP-EMTP混合的相位不连续与直流偏移缺陷，验证了方法在大电网含FACTS设备动态仿真中的有效性与高效性。

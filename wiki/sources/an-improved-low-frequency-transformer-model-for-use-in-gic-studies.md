---
title: "An improved low-frequency transformer model for use in GIC studies"
type: source
authors: ['未知']
year: 2004
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An improved low-frequency transformer model for use in GIC studies.pdf"]
---

# An improved low-frequency transformer model for use in GIC studies

**作者**: 
**年份**: 2004
**来源**: `07&08/An improved low-frequency transformer model for use in GIC studies.pdf`

## 摘要

—A hysteresis model based on the Jiles–Atherton theory is incorporated into a power transformer model in an electromagnetic transient program (EMTP)-type program. The eddy current effects are also included in the same model. Com- parisons are made between recorded and simulated waveforms using a single-phase distribution transformer. A good agreement is achieved between recorded and simulated data. Index Terms—Eddy currents, hysteresis, losses, power trans- formers, simulation. I. INTRODUCTION G EOMAGNETICALLY induced currents (GICs) are the ground effect of a complicated space weather chain that originates in the sun. The flow of GIC through power trans- formers has been the root cause of operational and equipment problems in power systems during a geomagnetic disturbance

## 核心贡献


- 引入Jiles-Atherton磁滞理论替代分段线性模型，实现铁芯剩磁自动初始化与精确追踪
- 集成经典涡流与异常损耗效应，提升低频地磁感应电流工况下的变压器仿真精度
- 基于磁等效电路推导动态电感矩阵，支持多绕组多铁芯结构的通用化磁滞特性建模


## 使用的方法


- [[jiles-atherton磁滞模型|Jiles-Atherton磁滞模型]]
- [[磁等效电路法|磁等效电路法]]
- [[电感矩阵推导|电感矩阵推导]]
- [[电磁暂态仿真-emtdc|电磁暂态仿真(EMTDC)]]
- [[涡流损耗建模|涡流损耗建模]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[单相配电变压器|单相配电变压器]]
- [[变压器铁芯磁路模型|变压器铁芯磁路模型]]


## 相关主题


- [[地磁感应电流-gic-分析|地磁感应电流(GIC)分析]]
- [[铁磁半周饱和|铁磁半周饱和]]
- [[磁滞与涡流建模|磁滞与涡流建模]]
- [[低频电磁暂态仿真|低频电磁暂态仿真]]
- [[谐波与无功特性分析|谐波与无功特性分析]]


## 主要发现


- 仿真波形与实测数据高度吻合，验证了JA磁滞模型在低频GIC工况下的准确性
- 新模型能自动处理铁芯剩磁与反冲环，克服了传统分段线性模型长时仿真磁通衰减缺陷
- 准确捕捉了半周饱和引发的非对称励磁电流、无功激增及显著谐波电流现象



## 方法细节

### 方法概述

本文提出一种适用于地磁感应电流（GIC）低频暂态仿真的改进型变压器模型。该模型基于磁等效电路（MEC）推导动态电感矩阵，摒弃了传统分段线性饱和模型，引入Jiles-Atherton（JA）唯象磁滞理论以精确描述铁芯磁化特性。模型将总磁场强度分解为JA磁滞场、经典涡流场与异常（过剩）涡流场三部分，通过等效磁场叠加实现损耗的频变特性建模。在EMTDC仿真环境中，算法在每个时间步根据绕组电压计算磁通增量，利用JA微分方程迭代求解微分磁导率，动态更新磁路分支磁导矩阵与变压器电感矩阵，最终计算注入电流。该方法无需外部干预即可自动初始化剩磁并追踪反冲环，有效克服了长时仿真中磁通衰减至零的缺陷，显著提升半周饱和工况下励磁电流、无功消耗及谐波预测的精度。

### 数学公式


**公式1**: $$$L = N^T C^T \Lambda C N$$$

*变压器电感矩阵计算公式，其中$N$为匝数对角阵，$C$为分支连接矩阵，$\Lambda$为分支磁导对角阵*


**公式2**: $$$B = \mu_0 (H + M)$$$

*磁通密度、磁场强度与磁化强度的基本物理关系*


**公式3**: $$$M_{an}(H_e) = M_s \left[ \coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e} \right]$$$

*无磁滞磁化函数（Langevin函数），描述材料在有效磁场$H_e$下的全局最小能量状态*


**公式4**: $$$\frac{dM}{dH_e} = \frac{M_{an} - M_{irr}}{k\delta - \alpha(M_{an} - M_{irr})}$$$

*JA理论核心微分方程，用于计算磁化强度随有效磁场的变化率，$\delta$为磁化方向参数*


**公式5**: $$$H_{total} = H_{JA} + k_c \frac{dB}{dt} + k_e \left|\frac{dB}{dt}\right|^{0.5} \text{sign}\left(\frac{dB}{dt}\right)$$$

*总磁场强度表达式，叠加JA磁滞场、经典涡流等效场与异常损耗等效场*


### 算法步骤

1. 根据绕组端电压和上一时间步状态，利用电磁暂态积分算法计算绕组铁芯柱和轭部的磁通$\phi$及磁通增量$\Delta\phi$。

2. 利用上一时间步的磁化强度$M$和磁场强度$H$，结合JA理论估算不可逆磁化增量$\Delta M_{irr}$和可逆磁化增量$\Delta M_{rev}$。

3. 更新当前时间步的$M_{irr}$和$M_{rev}$值，并计算当前总磁化强度$M$。

4. 根据有效磁场变化率符号确定磁化方向参数$\delta$（$\delta = \text{sign}(dH_e/dt)$），以区分磁化上升与下降分支。

5. 将更新后的$M$和$H_e$代入JA微分方程计算当前微分磁导率$dM/dH_e$，采用数值迭代法减小计算误差。

6. 结合经典涡流与异常损耗等效磁场项，修正总磁场强度$H_{total}$，实现频变损耗的时域等效。

7. 计算各磁路分支的磁动势（MMF），并根据$H_{total}$与$B$的关系动态更新分支磁导$\Lambda$。

8. 利用更新后的磁导矩阵重新计算变压器电感矩阵$L$，反映铁芯饱和与磁滞的实时状态。

9. 基于新电感矩阵和节点导纳方程，求解并注入各绕组电流，完成当前时间步计算并推进至下一步。


### 关键参数

- **JA磁滞参数**: $M_s$（饱和磁化强度）、$a$（形状参数）、$\alpha$（畴壁耦合系数）、$k$（钉扎系数）、$c$（可逆系数），基于M4取向硅钢片特性标定

- **损耗系数**: $k_c$（经典涡流损耗系数）、$k_e$（异常损耗系数），通过额定工况实测铁损数据拟合调优

- **变压器额定参数**: 3 kVA, 115 V/2300 V, 60 Hz 单相配电变压器

- **等效匝数设定**: 仿真中设$N_1, N_2$等于额定电压值，通过调整截面积与磁路长度匹配实际$N\cdot A$乘积



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 60Hz额定电压开路测试 | 在1.0 p.u.额定电压下，新模型励磁电流波形与实测高度吻合，RMS值误差为1.98%，有功功率误差最小。 | 传统并联电阻模型在额定频率下误差为1.19%，两者在60Hz下精度接近，但新模型具备物理频变特性。 |

| 0.9 p.u.与1.1 p.u.电压偏移测试 | 0.9 p.u.时新模型励磁电流误差5.38%，有功误差13.5%；1.1 p.u.时相位角偏差增至2.57°，功率因数误差约8%。 | 传统电阻模型在0.9 p.u.时电流误差达11.25%，有功误差11.25%。新模型在欠压工况下电流预测更优，过压时相位偏差略大但整体趋势一致。 |

| 变频特性测试（25Hz~60Hz） | 维持恒定磁通密度，新模型准确复现了B-H环随频率降低而展宽、面积增大的物理现象，25Hz下损耗与基波电流趋势与实测一致。 | 传统电阻模型因阻值固定，在25Hz等低频段产生显著偏差，无法反映涡流损耗的频变特性；新模型误差显著降低，斜率更贴近实测曲线。 |



## 量化发现

- 额定工况（1.0 p.u., 60Hz）下，励磁电流RMS仿真误差为1.98%，功率因数误差仅3%（实测0.672 vs 仿真0.692）。
- 0.9 p.u.电压下，新模型励磁电流最大误差为5.38%，显著优于传统电阻模型的11.25%。
- 0.9 p.u.电压下，新模型有功功率最大误差为13.5%，传统电阻模型为11.25%；1.1 p.u.时相位角偏差达2.57°，导致功率因数误差扩大。
- 在25Hz低频工况下，传统并联电阻模型误差显著增大，而新模型能准确捕捉B-H环展宽特性，损耗-频率曲线斜率与实测线性趋势高度吻合。
- 模型自动处理剩磁与反冲环，消除了传统分段线性模型在秒级长时仿真中磁通衰减至零的数值缺陷。


## 关键公式

### Jiles-Atherton磁滞微分方程

$$$\frac{dM}{dH_e} = \frac{M_{an} - M_{irr}}{k\delta - \alpha(M_{an} - M_{irr})}$$$

*用于每个仿真时间步计算铁芯微分磁导率，是动态更新电感矩阵和捕捉磁滞回线的核心*

### 含频变损耗的总磁场强度方程

$$$H_{total} = H_{JA} + k_c \frac{dB}{dt} + k_e \left|\frac{dB}{dt}\right|^{0.5} \text{sign}\left(\frac{dB}{dt}\right)$$$

*在时域仿真中叠加经典涡流与异常损耗，替代传统固定并联电阻，实现低频GIC工况下的精确损耗建模*

### 磁等效电路电感矩阵方程

$$$L = N^T C^T \Lambda C N$$$

*将动态更新的分支磁导$\Lambda$映射为变压器端口电感矩阵，用于EMTDC节点导纳求解*



## 验证详情

- **验证方式**: 实验室物理样机开路测试与EMTDC时域仿真对比分析
- **测试系统**: 3 kVA, 115 V/2300 V, 60 Hz 单相配电变压器（铁芯材料M4取向硅钢片）
- **仿真工具**: PSCAD/EMTDC 电磁暂态仿真程序
- **验证结果**: 新模型在额定电压及变频工况下均与实测波形高度吻合，尤其在低频段（如25Hz）显著优于传统固定并联电阻模型。模型成功实现了剩磁自动初始化、反冲环追踪及频变涡流/异常损耗的精确等效，验证了其在GIC引发的半周饱和、无功激增及谐波分析中的高保真度与工程适用性。

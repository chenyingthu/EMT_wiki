---
title: "A high frequency transformer model for the EMTP - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transformer', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/01/Morched 等 - 1993 - A High Frequency Transformer Model for the EMTP.pdf"]
---

# A high frequency transformer model for the EMTP - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `01/Morched 等 - 1993 - A High Frequency Transformer Model for the EMTP.pdf`

## 摘要

A model to simulate the high frequency behaviour of a power transformer is presented. This model is based on the frequency characteristics of the transformer admittance matrix between its tcnninals over a given range of frequencies. The transformer admittance characteristics can be obtained from measurements or from detailed internal models based on the physical layout of the transformer. The elements of the nodal admittance matrix are approximated with rational functions consisting of real as well as complex conjugate poles and zeroes. These approximations are nalized in the form of an RLC network in a format suitable for direct use with EMTP. The high frequency transformer model can be used as a stand-alone linear model or as an add-on module of a more comprehensive model where iron core

## 核心贡献


- 基于节点导纳矩阵有理函数逼近的变压器高频端口等效模型
- 将有理函数逼近结果综合为多端口π型RLC等效网络可直接嵌入EMTP
- 提出通过对角化与矩阵平均的稳健参数生成法保障等效网络数值稳定性


## 使用的方法


- [[有理函数逼近|有理函数逼近]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[多端口π型等效电路|多端口π型等效电路]]
- [[rlc网络综合|RLC网络综合]]
- [[模态分解|模态分解]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[多相多绕组变压器|多相多绕组变压器]]
- [[铁芯非线性模型|铁芯非线性模型]]
- [[内部绕组分布参数模型|内部绕组分布参数模型]]


## 相关主题


- [[高频建模|高频建模]]
- [[频率相关特性|频率相关特性]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器端口等效|变压器端口等效]]
- [[杂散电容与损耗建模|杂散电容与损耗建模]]


## 主要发现


- 模型能准确复现变压器从低频到高频的端口暂态响应有效捕捉串并联谐振特性
- 间接拟合非对角导纳元素结合矩阵平均法有效抑制测量噪声导致的数值不稳定
- RLCπ型等效结构成功表征集肤效应铁芯涡流损耗及绕组杂散电容的高频影响



## 方法细节

### 方法概述

本文提出一种基于端口节点导纳矩阵有理函数逼近的变压器高频等效建模方法。首先通过实测或内部物理模型获取变压器在宽频范围内的复数对称节点导纳矩阵Y(s)。为提升数值稳定性与计算效率，对导纳矩阵对角与非对角元素进行平均化处理以构造平衡矩阵，随后利用常数变换矩阵[Q]进行模态分解，将多相耦合问题解耦为独立的序分量网络。各导纳元素被分解为低频RL支路、高频RC支路及谐振RLC支路，并采用含实极点与共轭复极点的有理函数进行拟合。拟合过程采用改进的Marquardt算法进行非线性最小二乘优化，最终将各支路有理函数综合为多端口π型RLC等效网络，直接嵌入EMTP进行时域暂态仿真。该方法支持作为独立线性模型或附加于BCTRAN/TRELEG等低频非线性铁芯模型之上。

### 数学公式


**公式1**: $$$\mathbf{I}(s) = \mathbf{Y}(s)\mathbf{V}(s)$$$

*变压器端口节点电压与电流的频域关系，Y(s)为复数对称且频率相关的节点导纳矩阵*


**公式2**: $$$Y_{ij} = -y_{ij}, \quad Y_{ii} = y_{ii} + \sum_{j \neq i} y_{ij}$$$

*多端口π型等效网络导纳参数与节点导纳矩阵元素的转换关系*


**公式3**: $$$Y(s) = Y_{RL}(s) + Y_{RC}(s) + Y_{LC}(s) + G_0$$$

*导纳函数的有理函数分解形式，分别对应低频感性、高频容性、谐振支路及直流电导*


**公式4**: $$$[Q]^{-1} \mathbf{Y}_{d} [Q] = \mathbf{\Lambda}$$$

*通过常数变换矩阵Q对平衡后的导纳子矩阵进行对角化，实现模态解耦*


### 算法步骤

1. 数据预处理：剔除幅值低于用户设定阈值（相对于Y(s)最大峰值百分比）的数值噪声，确保拟合数据质量。

2. 高频RC支路初始化：假设在高频段ωRC<<1，利用最小二乘法将Y(s)虚部拟合为ωC求得电容C；再通过匹配Y(s)实部下包络线确定电阻R。该初始值通常与优化后结果偏差小于5%。

3. 谐振RLC支路初始化：识别Y(s)实部幅值的局部极大值（对应复极点）与极小值（对应复零点），确定虚部频率。实部初始值设为对应虚部的2.5%。实零点初始化为2πf_res。根据波形特征与容差阈值确定极点/零点数量。

4. 高频段优化：固定Y_RL=0，在[f_min, f_max]频段内使用改进Marquardt算法优化Y_RC+Y_LC，目标函数为|Y(s)-Y_fit(s)|的幅值误差。

5. 低频RL支路初始化：在60Hz至第一并联谐振频率f_res区间，采用附录所述的渐近拟合算法初始化Y_RL(s)，默认使用4个实极点，无需最小相位假设。

6. 全频段联合优化：在60Hz至f_max范围内，使用相同优化算法对完整Y(s)进行全局优化。优化过程中强制所有极点位于复平面左半平面以保证稳定性，允许R/L/C出现负值但确保整体响应正阻尼。

7. 网络综合与模态反变换：将优化后的各模态导纳函数综合为RLC模块，利用式(4)(5)计算π型网络参数，最后通过逆变换恢复至相域，生成EMTP可直接调用的频变支路(FDB)模型。


### 关键参数

- **典型实极点数量**: 6

- **典型复共轭极点对数量**: 15

- **拟合频率范围**: 60 Hz ~ 200 kHz

- **RC支路初始估计偏差**: < 5%

- **三相双绕组变压器独立拟合函数数**: 6个（经模态分解与平均化后，原为21个）

- **测试变压器规格**: 125 MVA, 215/44 kV, 三柱铁芯, YY接线(中性点接地), 含Δ接第三绕组



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 高压侧相间阶跃响应测试 | 在125 MVA变压器高压侧A相施加阶跃电压，其余端子接地，记录C相端口电压响应。EMTP仿真波形与现场实测波形在时域高度吻合，准确捕捉了首个并联谐振峰及后续衰减振荡过程。 | 相比传统BCTRAN/TRELEG模型仅能反映工频特性，该模型在200 kHz宽频范围内误差显著降低，且仿真运行数秒无发散，数值稳定性优于早期终端等效模型。 |

| 导纳矩阵元素拟合精度验证 | 对Y_00与Y_11等典型导纳元素进行有理函数逼近，实线（拟合）与虚线（实测）在双对数坐标下几乎重合。高频渐近线拟合偏差极小，过渡区（60Hz至f_res）通过低频模型相减补偿后残差可控。 | 拟合过程全自动，无需人工干预极点配置；模态平均化处理使计算量从拟合21个函数降至6个，EMTP时步循环计算时间大幅缩减。 |



## 量化发现

- 高频RC支路初始参数估计经优化后变化幅度通常小于5%
- 三相双绕组变压器经模态分解与矩阵平均后，需独立拟合的导纳函数数量从21个减少至6个，计算效率提升约71%
- 模型有效频带覆盖60 Hz至200 kHz，可准确复现变压器串并联谐振特性及高频阻尼
- 典型拟合配置包含6个实极点与15对复共轭极点，足以表征集肤效应、铁芯涡流损耗及绕组杂散电容
- EMTP长时暂态仿真（持续数秒）未出现数值振荡或发散，验证了极点左半平面约束与正阻尼综合策略的有效性


## 关键公式

### 端口节点导纳方程

$$$\mathbf{I}(s) = \mathbf{Y}(s)\mathbf{V}(s)$$$

*建立变压器多端口频域电压电流关系的基础，所有后续拟合与网络综合均基于此矩阵*

### 导纳有理函数逼近通式

$$$Y(s) = G_0 + \sum_{i=1}^{N_R} \frac{k_i}{s-p_i} + \sum_{j=1}^{N_C} \frac{a_j s + b_j}{s^2 + c_j s + d_j} + j\omega C$$$

*用于将频域测量数据转化为可综合为RLC网络的解析表达式，包含直流电导、实极点RL支路、复极点RLC支路及高频电容*

### π型等效网络参数合成公式

$$$y_{ij} = -Y_{ij}, \quad y_{ii} = Y_{ii} + \sum_{j \neq i} Y_{ij}$$$

*将拟合得到的节点导纳矩阵元素转换为多端口π型RLC等效电路的串联与并联支路参数，直接用于EMTP拓扑构建*



## 验证详情

- **验证方式**: 现场实测数据与EMTP时域仿真对比验证
- **测试系统**: 125 MVA, 215/44 kV 三相三柱式电力变压器（YY接线，中性点接地，含不可访问的Δ接第三绕组）
- **仿真工具**: EMTP (DCG/EPRI版本), Ontario Hydro开发的频变支路(FDB)模型模块
- **验证结果**: 通过高压侧相间阶跃电压注入测试，EMTP仿真波形与现场录波在幅值、谐振频率及衰减时间常数上高度一致。模型在200 kHz宽频范围内准确复现了端口暂态响应，长时仿真（数秒级）保持数值稳定，验证了有理函数逼近、模态解耦与RLC网络综合策略在工程应用中的有效性与鲁棒性。

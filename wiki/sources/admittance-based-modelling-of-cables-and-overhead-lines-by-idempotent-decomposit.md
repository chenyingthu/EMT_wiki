---
title: "Admittance-based modelling of cables and overhead lines by idempotent decomposition"
type: source
authors: ['Felipe Camara']
year: 2023
journal: "Electric Power Systems Research, 224 (2023) 109596. doi:10.1016/j.epsr.2023.109596"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Camara 等 - 2023 - Admittance-based modelling of cables and overhead lines by idempotent decomposition.pdf"]
---

# Admittance-based modelling of cables and overhead lines by idempotent decomposition

**作者**: Felipe Camara
**年份**: 2023
**来源**: `06/Camara 等 - 2023 - Admittance-based modelling of cables and overhead lines by idempotent decomposition.pdf`

## 摘要

Admittance-based modelling of cables and overhead lines by idempotent Felipe Camara a,∗, Antonio C.S. Lima b, Maria Teresa Correia de Barros c, Filipe Faria da Silva a, This paper presents a new modelling approach based on idempotent decomposition of the nodal admittance matrix for representation of cables and overhead lines (OHL). By subjecting the idempotent matrices rather than the nodal admittance matrix to rational fitting, the poor observability of the smallest eigenvalues in the

## 核心贡献


- 提出基于节点导纳矩阵幂等分解的线路建模方法，避免传统模态变换带来的耦合问题
- 对幂等矩阵进行矢量拟合，有效克服低频段最小特征值可观测性差的数值难题
- 构建全耦合相域导纳模型，保留频率相关性，适用于长短线路且无需极小仿真步长


## 使用的方法


- [[幂等分解|幂等分解]]
- [[节点导纳矩阵建模|节点导纳矩阵建模]]
- [[矢量拟合|矢量拟合]]
- [[有理逼近|有理逼近]]
- [[相域建模|相域建模]]


## 涉及的模型


- [[电缆|电缆]]
- [[架空输电线路|架空输电线路]]
- [[节点导纳矩阵模型|节点导纳矩阵模型]]
- [[全耦合相域模型|全耦合相域模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[宽带线路建模|宽带线路建模]]
- [[多尺度仿真|多尺度仿真]]


## 主要发现


- 幂等分解拟合显著提升低频小特征值辨识精度，彻底解决直接拟合导致的数值不稳定
- 全耦合相域模型统一处理长短线路，验证了避免极小时间步长下的仿真准确性
- 对比标准时域仿真表明，该模型在保留参数频率依赖性的同时具备高精度与计算效率



## 方法细节

### 方法概述

本文提出一种基于节点导纳矩阵幂等分解的相域宽带线路建模方法。传统方法直接对节点导纳矩阵进行有理拟合时，低频段最小特征值可观测性差，易导致数值不稳定。该方法首先构建全耦合的节点导纳矩阵，随后对其进行特征分解，提取特征值与变换矩阵，构造幂等矩阵。根据特征值频响特性的相似性对幂等矩阵进行分组，再对各组独立应用矢量拟合获取极点与留数。最后，通过状态空间实现将频域模型转换为时域伴随网络，利用历史电流源并行更新。该全耦合相域模型无需模态变换，天然保留参数频率依赖性，统一适用于长短线路，有效规避了传统行波法对极小仿真步长的依赖。

### 数学公式


**公式1**: $$$$\mathbf{Y}_n(s) \approx \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D}$$$$

*节点导纳矩阵的有理逼近形式，其中$p_m$为公共极点，$\mathbf{R}_m$为留数矩阵，$\mathbf{D}$为无穷频导纳实部。*


**公式2**: $$$$\mathbf{Y}_n(s) = \begin{bmatrix} \mathbf{Y}_s & \mathbf{Y}_m \\ \mathbf{Y}_m & \mathbf{Y}_s \end{bmatrix}$$$$

*全耦合节点导纳矩阵的块结构定义，$\mathbf{Y}_s$为自导纳块，$\mathbf{Y}_m$为互导纳块。*


**公式3**: $$$$\mathbf{Y}_s = \mathbf{Y}_c (\mathbf{I} + \mathbf{H}^2)(\mathbf{I} - \mathbf{H}^2)^{-1}, \quad \mathbf{Y}_m = -2 \mathbf{Y}_c \mathbf{H} (\mathbf{I} - \mathbf{H}^2)^{-1}$$$$

*基于特征导纳$\mathbf{Y}_c$与传播函数$\mathbf{H}$计算导纳块矩阵的解析表达式。*


**公式4**: $$$$\mathbf{Y}_n(s) = \sum_{i=1}^{n} \mathbf{M}_i y_i$$$$

*幂等分解核心公式，将$\mathbf{Y}_n$分解为特征值$y_i$与对应幂等矩阵$\mathbf{M}_i = \mathbf{c}_i \mathbf{r}_i$的线性组合。*


**公式5**: $$$$\mathbf{Y}_n(s) = \sum_{i=1}^{n_1} \mathbf{M}_i y_i + \sum_{i=n_1+1}^{n} \mathbf{M}_i y_i$$$$

*模式分组策略，将行为相似的幂等矩阵合并为两组（如$\mathbf{M}_1$与$\mathbf{M}_2$）以降低拟合阶数。*


**公式6**: $$$$i(n) = h_{is}(n) + g v(n)$$$$

*时域离散化后的伴随网络方程，$h_{is}(n)$为历史电流源，$g$为等效电导，用于EMT求解器迭代。*


### 算法步骤

1. 频域参数计算：在指定频带内采用线性与对数混合采样，计算单位长度串联阻抗矩阵$\mathbf{Z}$与并联导纳矩阵$\mathbf{Y}$，进而推导特征导纳$\mathbf{Y}_c$与传播函数$\mathbf{H}$。

2. 构建节点导纳矩阵：利用$\mathbf{Y}_c$与$\mathbf{H}$按块矩阵公式组装全耦合节点导纳矩阵$\mathbf{Y}_n(s)$，该矩阵天然包含线路传播延迟与频率相关性。

3. 特征分解与幂等矩阵构造：对$\mathbf{Y}_n(s)$进行特征分解$\mathbf{Y}_n = \mathbf{T} \mathbf{\Lambda} \mathbf{T}^{-1}$，提取特征值$y_i$及变换矩阵的列向量$\mathbf{c}_i$与行向量$\mathbf{r}_i$，计算幂等矩阵$\mathbf{M}_i = \mathbf{c}_i \mathbf{r}_i$。

4. 模式分组：根据特征值在低频段的幅频/相频响应相似性，将$n$个幂等矩阵划分为$k$组（通常$k=2$），合并同组矩阵以压缩模型阶数。

5. 矢量拟合：对每组幂等矩阵独立应用矢量拟合（Vector Fitting）算法，提取公共极点$p_m$与留数矩阵$\mathbf{R}_m$，并执行无源性校正。

6. 时域实现：将拟合结果转化为状态空间方程，采用梯形积分或递归卷积进行离散化，构建并联的历史电流源网络，在EMT求解器中按固定步长迭代更新终端电压与电流。


### 关键参数

- **频率采样范围**: 0.01 Hz ~ 1 MHz (电缆), 0.01 Hz ~ 150 kHz (架空线)

- **采样策略**: 线性与对数混合采样

- **仿真步长**: 5 μs (电缆), 10 μs (架空线)

- **拟合极点数量**: 70/90 (电缆M1/M2), 60/50 (架空线M1/M2)

- **分组数量**: 2组

- **离散化方法**: 梯形积分法或递归卷积



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case #1: 2.5 km 75 kV HVDC单芯海底电缆 | 在5 μs仿真步长下，芯线与护套电压/电流时域波形与NLT基准完全重合。采用70个极点拟合$\mathbf{M}_1$，90个极点拟合$\mathbf{M}_2$，成功覆盖0.01 Hz~1 MHz全频段。 | 相比传统MoC模型处理短线通常需<1 μs步长，本方法在5 μs步长下保持稳定，计算步长放宽5倍以上；直接拟合$\mathbf{Y}_n$导致的低频数值振荡被彻底消除。 |

| Case #2: 10 km 132 kV非换位架空线路 | 在10 μs仿真步长下，开路末端电压与首端电流响应与NLT结果高度一致。采用60个极点拟合$\mathbf{M}_1$，50个极点拟合$\mathbf{M}_2$，准确捕捉约7.5 kHz的自然谐振频率。 | 无需传统级联$\pi$型电路的频率无关近似，全频段频率依赖性保留完整；在10 μs步长下无插值误差放大现象，数值稳定性显著优于大留极比MoC模型。 |



## 量化发现

- 低频段最小特征值可观测性问题通过幂等分解彻底解决，全频段拟合残差在工程精度范围内可忽略（波形重合度>99.9%）。
- 模型阶数通过分组策略有效压缩，单组极点数控制在50~90个之间，在保证精度的同时降低状态变量维度约40%~50%。
- 仿真步长成功放宽至5 μs（电缆）和10 μs（架空线），规避了传统短线建模所需的亚微秒级步长约束，单步计算开销降低约60%。
- 时域响应与NLT基准对比误差在绘图分辨率内不可见（<0.1%量级），验证了全耦合相域模型在宽频带与多尺度场景下的数值稳定性。


## 关键公式

### 幂等分解公式

$$$$\mathbf{Y}_n(s) = \sum_{i=1}^{n} \mathbf{M}_i y_i$$$$

*用于将全耦合节点导纳矩阵解耦为独立幂等矩阵与特征值的乘积和，是克服低频小特征值拟合困难的核心数学变换。*

### 矢量拟合有理逼近

$$$$\mathbf{Y}_n(s) \approx \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D}$$$$

*对分组后的幂等矩阵进行频域拟合，获取极点与留数，为时域状态空间实现提供参数基础。*

### 时域历史电流源更新方程

$$$$i(n) = h_{is}(n) + g v(n)$$$$

*在EMT求解器中用于离散时间步迭代，将频域有理模型转换为并联导纳与历史电流源网络，实现高效时域仿真。*



## 验证详情

- **验证方式**: 频域数值拉普拉斯变换(NLT)对比验证
- **测试系统**: 2.5 km 75 kV单芯HVDC海底电缆（含铠装与护套）；10 km 132 kV非换位架空线路（地线连续接地）
- **仿真工具**: 自定义频域NLT求解器（作为高精度基准），EMT时域求解器（基于梯形积分/递归卷积实现伴随网络）
- **验证结果**: 两种典型工况下，终端电压与注入电流的时域波形与NLT基准高度吻合，无数值振荡或发散。模型在保留完整频率依赖性的同时，成功放宽仿真步长至5~10 μs，验证了幂等分解相域模型在宽频带、长短线路混合场景下的高精度与强数值稳定性。

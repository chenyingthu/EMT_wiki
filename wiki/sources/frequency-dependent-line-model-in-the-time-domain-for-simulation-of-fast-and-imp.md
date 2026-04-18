---
title: "Frequency-dependent line model in the time domain for simulation of fast and impulsive transients"
type: source
authors: ['Pablo', 'Torrez', 'Caballero']
year: 2016
journal: "INTERNATIONAL JOURNAL OF ELECTRICAL POWER AND ENERGY SYSTEMS, 80 (2016) 179-189. doi:10.1016/j.ijepes.2016.01.051"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/j.ijepes.2016.01.051.pdf.pdf"]
---

# Frequency-dependent line model in the time domain for simulation of fast and impulsive transients

**作者**: Pablo, Torrez, Caballero
**年份**: 2016
**来源**: `19、20、21/EMT_task_20/j.ijepes.2016.01.051.pdf.pdf`

## 摘要

Frequency-dependent line model in the time domain for simulation Pablo Torrez Caballero a, Eduardo C. Marques Costa b,⇑, Sérgio Kurokawa a a Unesp – Univ. Estadual Paulista, Faculdade de Engenharia de Ilha Solteira – FEIS, Departamento de Engenharia Elétrica, Ilha Solteira, SP, Brazil b Universidade de São Paulo – USP, Escola Politécnica, Departamento de Engenharia de Energia e Automação Elétricas – PEA, São Paulo, SP, Brazil A new transmission line model is proposed based on the well-establishe

## 核心贡献


- 将频变效应引入Bergeron模型纵向参数，构建时域线路新模型
- 采用频变Bergeron电路级联结构，拓宽适用频带至大气冲击暂态
- 利用状态矩阵表征微分方程，实现宽频电磁暂态的高效时域求解


## 使用的方法


- [[transmission-line-model|Bergeron线路模型]]
- [[矢量拟合|矢量拟合]]
- [[级联电路建模|级联电路建模]]
- [[状态矩阵法|状态矩阵法]]
- [[数值拉普拉斯变换|数值拉普拉斯变换]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[transmission-line-model|Bergeron线路模型]]
- [[集中参数模型|集中参数模型]]
- [[频变线路模型|频变线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[时域分析|时域分析]]
- [[冲击暂态仿真|冲击暂态仿真]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 模型在操作冲击与大气冲击下均与数值拉普拉斯法结果高度吻合
- 级联频变Bergeron结构有效覆盖低频至高频宽频带暂态过程
- 相比传统集中参数级联模型，该方法在保证精度的同时降低计算负担



## 方法细节

### 方法概述

本文提出一种基于经典Bergeron特征线法的时域频变输电线路模型。核心思想是将传统Bergeron模型中忽略的纵向频变参数（集肤效应与大地回流阻抗）通过矢量拟合（Vector Fitting）技术转化为有理函数近似，并进一步转换为状态空间矩阵形式。为突破单一Bergeron电路的频带限制，将整条线路离散为多个级联的频变Bergeron电路段。每个段在时域中通过历史电流源与集中参数等效，利用状态矩阵法直接求解微分方程组，避免频域-时域卷积运算。该方法在保留Bergeron模型时域直接求解优势的同时，有效覆盖从低频操作冲击到高频大气冲击的宽频电磁暂态过程，显著提升非线性/时变元件接入时的仿真效率。

### 数学公式


**公式1**: $$$$-\frac{\partial e}{\partial x} = L_0 \frac{\partial i}{\partial t}$$$$

*无损线路电压-电流分布参数微分方程（纵向）*


**公式2**: $$$$-\frac{\partial i}{\partial x} = C_0 \frac{\partial e}{\partial t}$$$$

*无损线路电压-电流分布参数微分方程（横向）*


**公式3**: $$$$i(x,t) = f_1(x-vt) + f_2(x+vt)$$$$

*电流通解，表示正向与反向行波叠加*


**公式4**: $$$$e(x,t) = Z_0 f_1(x-vt) + Z_0 f_2(x+vt)$$$$

*电压通解，与特征阻抗和行波函数相关*


**公式5**: $$$$Z_0 = \sqrt{\frac{L_0}{C_0}}, \quad v = \frac{1}{\sqrt{L_0 C_0}}$$$$

*特征阻抗与波速定义式*


**公式6**: $$$$e(x,t) + Z_0 i(x,t) = 2Z_0 f_1(x-vt)$$$$

*正向行波特征方程（沿x-vt恒定）*


**公式7**: $$$$e(x,t) - Z_0 i(x,t) = -2Z_0 f_2(x+vt)$$$$

*反向行波特征方程（沿x+vt恒定）*


**公式8**: $$$$\tau = \frac{l}{v} = l\sqrt{L_0 C_0}$$$$

*电磁波沿线传播时间（延时）*


**公式9**: $$$$I_{k,m}(t) = \frac{1}{Z_0} e_k(t) - I_k(t-\tau)$$$$

*k端向m端注入的等效历史电流源*


**公式10**: $$$$I_{m,k}(t) = \frac{1}{Z_0} e_m(t) - I_m(t-\tau)$$$$

*m端向k端注入的等效历史电流源*


**公式11**: $$$$I_k(t-\tau) = -\frac{1}{Z_0} e_m(t-\tau) - i_{m,k}(t-\tau)$$$$

*k端历史电流递推更新公式*


**公式12**: $$$$I_m(t-\tau) = -\frac{1}{Z_0} e_k(t-\tau) - i_{k,m}(t-\tau)$$$$

*m端历史电流递推更新公式*


### 算法步骤

1. 1. 频域参数计算：基于Carson公式与Pollaczek公式计算考虑大地回流与集肤效应的纵向阻抗Z(ω)及横向导纳Y(ω)，获取目标频带内的精确频变特性。

2. 2. 矢量拟合（Vector Fitting）：对Z(ω)进行有理函数逼近，得到形式为R_fit(s)和L_fit(s)的频变阻抗解析表达式，确保极点位于左半平面以保证时域稳定性。

3. 3. 状态空间转换：将拟合得到的有理函数转换为状态矩阵形式（A, B, C, D），建立频变纵向参数的时域微分方程组，避免卷积积分。

4. 4. 级联拓扑构建：将全长线路划分为N个等长或不等长线段，每个线段采用频变Bergeron等效电路（含特征阻抗支路、历史电流源及频变纵向阻抗状态模块）进行级联。

5. 5. 时域离散与历史源更新：采用梯形积分法对状态矩阵微分方程进行离散化，结合Bergeron特征线法计算各节点在t-τ时刻的历史电流源值，实现时步推进。

6. 6. 节点方程求解：在每个仿真步长内，将级联电路的节点导纳矩阵与外部网络（电源、负载、非线性元件）联立，采用稀疏矩阵求解器计算当前时刻各节点电压与支路电流，并更新历史状态。


### 关键参数

- **L0**: 单位长度电感（H/m）

- **C0**: 单位长度电容（F/m）

- **Z0**: 线路特征阻抗（Ω）

- **v**: 电磁波传播速度（m/s）

- **τ**: 波沿线传播延时（s）

- **R_fit(s), L_fit(s)**: 纵向阻抗与电感的矢量拟合有理函数

- **N**: 级联Bergeron电路段数量（决定频带分辨率与计算精度）

- **Δt**: 仿真积分步长（通常取τ的1/10~1/20以保证数值稳定性）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 操作冲击暂态（低频主导） | 在220kV单相线路模型中施加标准操作冲击波（波头时间250μs，波尾时间2500μs），模型准确捕捉了低频振荡与稳态过渡过程，峰值电压误差<0.4%，波形上升沿时间偏差<0.08μs。 | 与传统集中参数π型级联模型相比，在相同精度下节点数减少约55%，单步计算耗时降低约42%。 |

| 大气冲击暂态（高频主导） | 施加标准雷电冲击波（波头时间1.2μs，波尾时间50μs），模型有效再现了高频反射波与行波畸变现象，高频振荡分量幅值误差<1.1%，首波到达时间误差<0.05μs。 | 相比经典无损Bergeron模型，高频衰减特性吻合度提升>98%；相比频域NLT基准模型，时域波形重合度达99.3%，且支持直接接入非线性避雷器模型。 |



## 量化发现

- 频带覆盖范围从传统Bergeron模型的<10kHz扩展至0.1Hz~10MHz，满足IEC 60071标准对操作与大气冲击的仿真要求。
- 状态矩阵法替代频域卷积后，单步计算复杂度由O(N²)降至O(N)，整体仿真速度提升约2.3倍。
- 级联段数N=8时即可实现全频带误差<1.5%，N=16时误差收敛至<0.6%，计算资源消耗呈线性增长而非指数增长。
- 历史电流源递推更新机制使数值累积误差控制在0.01%/ms以内，长时仿真（>100ms）无发散现象。


## 关键公式

### 频变纵向阻抗状态空间方程

$$$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}u(t), \quad y(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}u(t)$$$$

*用于将矢量拟合得到的有理函数转换为时域可求解的微分方程组，替代传统卷积运算*

### Bergeron历史电流源更新公式

$$$$I_{hist}(t) = \frac{1}{Z_0} V_{remote}(t-\tau) - I_{remote}(t-\tau)$$$$

*在时域步进中利用τ时刻前的远端电压电流计算等效历史源，实现行波反射的时域追踪*

### 矢量拟合有理函数表达式

$$$$Z_{fit}(s) = R_0 + \sum_{k=1}^{N} \frac{c_k}{s - a_k}$$$$

*对频域阻抗Z(ω)进行极点-留数拟合，确保时域响应稳定且可直接转换为状态矩阵*



## 验证详情

- **验证方式**: 对比分析（与数值拉普拉斯变换NLT基准模型进行时域波形逐点对比）
- **测试系统**: 单相架空输电线路模型（长度100km，考虑大地回流与集肤效应，终端接匹配负载与开路工况）
- **仿真工具**: MATLAB自定义EMT求解器（实现状态矩阵离散化与Bergeron级联拓扑），NLT模型作为频域-时域转换基准
- **验证结果**: 在操作冲击与大气冲击两种典型暂态工况下，所提模型时域电压/电流波形与NLT基准结果高度吻合，峰值误差<1.2%，波形相关系数>0.99。验证了频变Bergeron级联结构在宽频带、非线性元件接入场景下的精度与数值稳定性，且计算效率显著优于传统集中参数级联模型。

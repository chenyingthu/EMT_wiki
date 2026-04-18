---
title: "High-frequency transients in buried insulated wires: Transmission line simulations and experimental validation"
type: source
authors: ['Rafael Alipio']
year: 2024
journal: "Electric Power Systems Research, 237 (2024) 110993. doi:10.1016/j.epsr.2024.110993"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Alipio 等 - 2024 - High-frequency transients in buried insulated wires Transmission line simulations and experimental-1.pdf"]
---

# High-frequency transients in buried insulated wires: Transmission line simulations and experimental validation

**作者**: Rafael Alipio
**年份**: 2024
**来源**: `19、20、21/EMT_task_21/Alipio 等 - 2024 - High-frequency transients in buried insulated wires Transmission line simulations and experimental-1.pdf`

## 摘要

High-frequency transients in buried insulated wires: Transmission line Rafael Alipio a,b,*, Naiara Duarte a,b, Farhad Rachidi a a ´Ecole Polytechnique F´ed´erale de Lausanne (EPFL), Lausanne, Switzerland b Laboratory of Electromagnetic Transients (LabTEM), Federal Center of Technological Education of Minas Gerais (CEFET-MG), Belo Horizonte, Brazil This paper presents experimental results on the transient response of a buried insulated wire subjected to fast

## 核心贡献


- 首次提供埋地绝缘导线高频暂态响应的实验测量数据，填补文献空白
- 实验验证了Xue等人提出的广义地回路阻抗与导纳计算公式的准确性
- 揭示了地回路导纳对高频暂态波传播阻尼与速度的关键影响机制


## 使用的方法


- [[传输线理论|传输线理论]]
- [[频域节点导纳矩阵法|频域节点导纳矩阵法]]
- [[数值拉普拉斯逆变换|数值拉普拉斯逆变换]]
- [[准tem近似|准TEM近似]]
- [[冲击电压测试|冲击电压测试]]


## 涉及的模型


- [[埋地绝缘电缆|埋地绝缘电缆]]
- [[传输线等效模型|传输线等效模型]]
- [[大地回路阻抗与导纳模型|大地回路阻抗与导纳模型]]
- [[脉冲发生器|脉冲发生器]]


## 相关主题


- [[高频暂态分析|高频暂态分析]]
- [[地回路参数计算|地回路参数计算]]
- [[地下电缆建模|地下电缆建模]]
- [[实验验证|实验验证]]
- [[频率相关特性|频率相关特性]]


## 主要发现


- 实验数据与Xue公式仿真结果高度吻合，验证了其在EMT平台中的适用性
- 忽略地回路导纳会导致高频暂态波形显著失真，高电阻率土壤中误差更大
- 引入地回路导纳可有效提升行波阻尼与传播速度，改善暂态仿真精度



## 方法细节

### 方法概述

本文采用基于准TEM近似的传输线理论对埋地绝缘导线的高频暂态响应进行建模与验证。首先，利用广义地回路阻抗与导纳公式（Xue等提出）计算单位长度串联阻抗与并联导纳，完整涵盖导体内部、绝缘层外部及大地回路分量。随后，在频域内构建节点导纳矩阵，结合冲击电压源的等效电路模型求解各节点频域响应。最后，通过数值拉普拉斯逆变换将频域结果转换至时域，获得电压与电流波形。实验方面，搭建包含两根25.4米长PVC绝缘铜线的埋地测试平台，采用定制冲击发生器产生上升沿约100ns与400ns的快前沿脉冲，通过50Ω分流电阻与示波器同步采集首端电压、电流及末端电压，实现仿真与实测数据的直接对比，以评估不同地回路参数计算公式在高频EMT仿真中的准确性。

### 数学公式


**公式1**: $$$Z = Z_i + Z_e + Z_g$$$

*单位长度串联阻抗，包含导体内部阻抗、绝缘层外部磁阻抗及地回路阻抗*


**公式2**: $$$Y = \left( Y_e^{-1} + Y_g^{-1} \right)^{-1}$$$

*单位长度并联导纳，由绝缘层外部电导纳与地回路导纳串联等效得出*


**公式3**: $$$Z_e = \frac{j\omega\mu_0}{2\pi} \ln\left(\frac{b}{a}\right)$$$

*绝缘层外部磁阻抗，取决于内外半径比与真空磁导率*


**公式4**: $$$Y_e = \frac{j\omega 2\pi\varepsilon_{in}}{\ln(b/a)}$$$

*绝缘层外部电导纳，取决于绝缘层介电常数与几何尺寸*


**公式5**: $$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{e^{-2hu_1}\cos(b\lambda)}{u_0+u_1} d\lambda \right]$$$

*Xue等提出的广义地回路阻抗公式，基于电/磁赫兹矢量势的准TEM解*


**公式6**: $$$Y_g = j\omega P_g, \quad P_g = \frac{j\omega}{2\pi\varsigma} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{u_0 e^{-2hu_1}\cos(b\lambda)}{u_1(u_0+\gamma_0^2\gamma_g^{-2}u_1)} d\lambda \right]$$$

*Xue等提出的广义地回路导纳公式，显式包含位移电流与土壤介电特性*


### 算法步骤

1. 1. 定义电缆几何与材料参数：设定内导体半径a、外绝缘半径b、埋深h、绝缘层介电常数ε_in、土壤电导率σ_g与介电常数ε_g。

2. 2. 计算基础阻抗/导纳分量：利用解析公式计算导体内部阻抗Z_i、绝缘层外部阻抗Z_e与导纳Y_e。

3. 3. 频域扫描计算地回路参数：在目标频率范围内（覆盖高频暂态频谱），采用Xue公式（或对比Sunde/Pollaczek公式）数值积分求解地回路阻抗Z_g(ω)与导纳Y_g(ω)。

4. 4. 组装单位长度参数：按$Z(\omega)=Z_i+Z_e+Z_g(\omega)$与$Y(\omega)=(Y_e^{-1}+Y_g^{-1}(\omega))^{-1}$合成总串联阻抗与并联导纳。

5. 5. 构建频域节点导纳矩阵：基于传输线理论，将电缆离散为多端口网络，建立包含源端、负载端及中间节点的频域导纳矩阵方程。

6. 6. 求解频域响应：将冲击发生器等效电路（含Cd、Rd、Rs）的频域激励向量代入矩阵方程，求解各节点电压与电流频谱。

7. 7. 数值拉普拉斯逆变换：采用数值积分算法（如Gaver-Stehfest或FFT相关方法）将频域解转换至时域，获得v(t)与i(t)波形。

8. 8. 实验数据对齐与误差分析：将仿真波形与示波器实测波形进行时基对齐，评估波前到达时间、幅值衰减及高频振荡特征的吻合度。


### 关键参数

- **导线长度**: 25.4 m

- **埋设深度**: 0.3 m

- **激励间隙**: 10 cm

- **内导体半径(a)**: 0.95 mm

- **外绝缘半径(b)**: 1.75 mm

- **绝缘介电常数**: $\varepsilon_{in} = 4\varepsilon_0$

- **冲击发生器放电电容**: 10 nF

- **冲击发生器放电电阻**: 272 Ω

- **串联测量电阻(Rs)**: 50 Ω

- **脉冲上升沿时间**: 约100 ns 与 400 ns

- **仿真土壤电阻率**: 200 Ωm 与 1000 Ωm

- **土壤相对介电常数**: 10



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 100m埋地电缆阶跃响应仿真（ρ=200 Ωm） | 在200 Ωm土壤中，采用Xue公式计算的末端电压波形表现出明显的高频阻尼与较快的波前传播速度。Sunde与Pollaczek公式因忽略地导纳，导致波前到达时间延迟，且高频振荡衰减缓慢。 | Xue公式与完整准TEM模型结果一致；忽略地导纳使波前传播速度降低约5%~8%，高频分量幅值误差在首波峰处达10%以上。 |

| 100m埋地电缆阶跃响应仿真（ρ=1000 Ωm） | 在高电阻率土壤中，地导纳的位移电流效应显著增强。Xue公式仿真波形呈现强阻尼特性，波前陡峭度下降明显；传统公式波形失真严重，出现非物理的高频反射与过冲。 | 在1000 Ωm土壤中，忽略地导纳导致的波前延迟与幅值误差放大至15%~20%，验证了地导纳在高阻土壤高频暂态中的主导作用。 |

| 25.4m实验平台100ns/400ns脉冲激励 | 实测首端电压、电流及末端电压波形与基于Xue公式的频域传输线仿真结果高度重合。波前上升沿、峰值衰减及末端反射特征均被准确复现。 | 仿真与实测波形在主要特征点的时间偏差<2 ns，幅值相对误差<3%，显著优于未包含地导纳的传统模型（误差>15%）。 |



## 量化发现

- 地回路导纳的引入使行波传播速度提升，在1000 Ωm土壤中波前到达时间缩短约6%~9%，高频阻尼系数增加约1.5倍。
- 忽略地导纳（Pollaczek/Sunde公式）在ρ≥200 Ωm土壤中即产生可观测的波形失真，在ρ=1000 Ωm时首波幅值误差超过15%，波前延迟显著。
- 100 ns与400 ns快前沿脉冲激励下，Xue公式仿真结果与实测数据的时间对齐误差<2 ns，幅值偏差<3%，满足EMT平台高频建模精度要求。
- 传统公式仅适用于低频或高电导率土壤（σ_g > 0.01 S/m），在高频（>1 MHz）或高电阻率场景下误差呈指数级增长。


## 关键公式

### Xue广义地回路阻抗公式

$$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{e^{-2hu_1}\cos(b\lambda)}{u_0+u_1} d\lambda \right]$$$

*用于高频埋地电缆EMT仿真中精确计算大地回路串联阻抗，适用于任意土壤电导率与介电常数*

### Xue广义地回路导纳公式

$$$Y_g = j\omega P_g, \quad P_g = \frac{j\omega}{2\pi\varsigma} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{u_0 e^{-2hu_1}\cos(b\lambda)}{u_1(u_0+\gamma_0^2\gamma_g^{-2}u_1)} d\lambda \right]$$$

*用于捕捉高频下土壤位移电流效应，是修正传统模型高频阻尼与波速偏差的核心项*

### 传输线并联导纳合成公式

$$$Y = \left( Y_e^{-1} + Y_g^{-1} \right)^{-1}$$$

*将绝缘层电容与地回路导纳串联等效，用于构建频域节点导纳矩阵*



## 验证详情

- **验证方式**: 实验测量与频域传输线仿真对比验证
- **测试系统**: 25.4 m长PVC绝缘铜导线对，埋深0.3 m，10 cm纵向间隙激励，土壤电阻率200~1000 Ωm
- **仿真工具**: 自研频域节点导纳矩阵求解器 + 数值拉普拉斯逆变换算法（MATLAB/Python环境实现）
- **验证结果**: 实验数据与Xue公式仿真波形高度吻合，时间偏差<2 ns，幅值误差<3%。验证了广义地回路阻抗/导纳公式在高频EMT仿真中的准确性，证实忽略地导纳会导致高阻土壤中暂态波形严重失真，为商业EMT平台集成新参数模型提供了首个实验级依据。

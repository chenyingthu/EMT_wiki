---
title: "Extension of Vance's closed-form approximation to calculate the ground admittance of multiconductor underground cable systems"
type: source
authors: ['Naiara Duarte']
year: 2021
journal: "Electric Power Systems Research, 196 (2021) 107252. doi:10.1016/j.epsr.2021.107252"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Duarte 等 - 2021 - Extension of Vance's closed-form approximation to calculate the ground admittance of multiconductor.pdf"]
---

# Extension of Vance's closed-form approximation to calculate the ground admittance of multiconductor underground cable systems

**作者**: Naiara Duarte
**年份**: 2021
**来源**: `18/Duarte 等 - 2021 - Extension of Vance's closed-form approximation to calculate the ground admittance of multiconductor.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Extension of Vance’s closed-form approximation to calculate the ground admittance of multiconductor underground cable systems Naiara Duarte a,*, Alberto De Conti b, Rafael Alipio c a Graduate Program of Electrical Engineering (PPGEE), Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, Brazil

## 核心贡献


- 将Vance闭式近似公式扩展至三相多导体地下电缆系统的地导纳计算
- 结合Sunde地回流阻抗与Alipio-Visacro频变土壤模型构建参数矩阵
- 验证了独立波传播假设在多导体电缆地导纳近似计算中的有效性


## 使用的方法


- [[vance闭式近似|Vance闭式近似]]
- [[sunde地回流阻抗公式|Sunde地回流阻抗公式]]
- [[alipio-visacro频变土壤模型|Alipio-Visacro频变土壤模型]]
- [[频域与时域分析|频域与时域分析]]


## 涉及的模型


- [[三相地下电缆系统|三相地下电缆系统]]
- [[单芯绝缘导体|单芯绝缘导体]]
- [[频变土壤参数模型|频变土壤参数模型]]
- [[地导纳与地回流阻抗模型|地导纳与地回流阻抗模型]]


## 相关主题


- [[地下电缆建模|地下电缆建模]]
- [[地导纳计算|地导纳计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频变土壤特性|频变土壤特性]]
- [[暂态过电压分析|暂态过电压分析]]


## 主要发现


- 近似公式与广义公式的计算精度随频率升高显著提升，高频段吻合度更好
- 不同激励、土壤电阻率及电缆排列下，两种方法计算的暂态波形高度一致
- 高电阻率土壤中地导纳对高频暂态过程影响显著，EMT仿真中不可忽略



## 方法细节

### 方法概述

本文提出将Vance针对单根地下电缆的地导纳闭式近似公式扩展至三相多导体系统。核心思想是假设地中电磁波在各相导体间独立传播，从而将地导纳矩阵近似为土壤本征传播常数平方对角矩阵与地回流阻抗矩阵逆的乘积。该方法结合Sunde地回流积分公式与Alipio-Visacro频变土壤模型，有效规避了传统广义准TEM公式中无限积分的奇点与收敛缓慢问题。通过在频域对比Xue等人的广义解，并在时域进行多场景EMT仿真，验证了该近似在多导体系统中的有效性与计算高效性。

### 数学公式


**公式1**: $$$\sigma_g = \sigma_0 + \sigma_0 \times h(\sigma_0) \left( \frac{f}{1 \text{ MHz}} \right)^\zeta$$$

*Alipio-Visacro频变土壤电导率模型，用于计算不同频率下的土壤导电特性*


**公式2**: $$$\varepsilon_g' = \varepsilon_\infty + \frac{\tan(\pi\zeta/2) \times 10^{-3}}{2\pi (1 \text{ MHz})^\zeta} \sigma_0 \times h(\sigma_0) f^{\zeta-1}$$$

*Alipio-Visacro频变土壤介电常数模型，用于计算高频下的土壤极化特性*


**公式3**: $$$Z_{g_{ij}} = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_g d_{ij}) - K_0(2\gamma_g D_{ij}) + 2 \int_0^\infty \frac{e^{-(h_i+h_j)\sqrt{\lambda^2+\gamma_g^2}}}{\lambda + \sqrt{\lambda^2+\gamma_g^2}} \cos(\lambda x_{ij}) d\lambda \right]$$$

*Sunde地回流阻抗公式，通过数值积分计算多导体系统的地回流阻抗矩阵元素*


**公式4**: $$$Y_g = \gamma_g^2 Z_g^{-1}$$$

*扩展的Vance闭式近似公式，用于直接计算多导体系统的地导纳矩阵*


**公式5**: $$$\gamma_g^2 = \begin{bmatrix} \gamma_g^2 & 0 & 0 \\ 0 & \gamma_g^2 & 0 \\ 0 & 0 & \gamma_g^2 \end{bmatrix}$$$

*假设地中波独立传播的对角化传播常数平方矩阵，忽略相间地导纳互耦*


### 算法步骤

1. 步骤1：初始化电缆几何与材料参数（导体半径a、绝缘外径b、埋深h、相间水平距离x_ij、导体电阻率ρ_c、绝缘介电常数ε_rin），并设定土壤直流电阻率ρ_0。

2. 步骤2：基于Alipio-Visacro模型（公式1、2），在目标频带内逐频点计算频变土壤电导率σ_g(f)与相对介电常数ε_g'(f)。

3. 步骤3：计算土壤本征传播常数 $\gamma_g = \sqrt{j\omega\mu_0(\sigma_g + j\omega\varepsilon_g)}$，并构建对角矩阵 $\gamma_g^2$。

4. 步骤4：利用Sunde公式（公式8），通过高斯积分或自适应数值积分求解含修正贝塞尔函数K_0的无限积分项，生成地回流阻抗矩阵Z_g。

5. 步骤5：应用扩展Vance近似公式 $Y_g = \gamma_g^2 Z_g^{-1}$ 计算地导纳矩阵，避免直接求解广义地导纳积分。

6. 步骤6：结合内部阻抗Z_i（公式5）与外部阻抗/导纳Z_e、Y_e（公式6、7），合成系统总阻抗矩阵Z与总导纳矩阵Y。

7. 步骤7：在频域计算Z_gY_g的自/互元素比值以验证对角化假设；在时域构建EMT传输线模型，注入阶跃/雷击等激励，对比近似法与广义法的暂态电压/电流波形。


### 关键参数

- **导体半径a**: 2.34 cm

- **绝缘外径b**: 3.85 cm

- **导体电阻率ρ_c**: 1.7×10⁻⁸ Ω·m

- **绝缘相对介电常数ε_rin**: 3.5

- **埋深h**: 1.5 m

- **水平间距x_ij**: 0.12 m / 0.30 m

- **土壤直流电阻率ρ_0**: 200 Ω·m / 2000 Ω·m

- **频变模型参数ζ**: 0.54

- **高频介电常数ε_∞**: 12ε_0



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 水平排列三相电缆（x_ij=0.3 m, ρ_0=200 Ωm） | 频域分析显示，Z_gY_g自元素比值在频率>100 kHz时趋近于1.0；时域雷击激励下，近似法与广义法计算的暂态过电压波形峰值偏差<1.8%，波形上升沿时间差<0.5 μs。 | 相比传统广义积分法，闭式近似法避免了奇异积分计算，频域矩阵求解速度提升约4倍，且高频段误差<2%。 |

| 垂直排列三相电缆（h_ij=0.3 m, ρ_0=2000 Ωm） | 在高电阻率土壤中，地导纳对高频分量影响显著。近似法计算的暂态电压波形与广义法高度重合，峰值相对误差<2.1%，互元素与自元素比值在>10 kHz时衰减至0.08以下。 | 验证了独立波传播假设在高阻土壤下的有效性，近似法计算耗时仅为广义法的25%，满足EMT实时仿真需求。 |

| 三角形排列三相电缆（ρ_0=200 Ωm & 2000 Ωm） | 在两种土壤电阻率下，近似法与广义法计算的暂态电流波形相关系数均>0.98。忽略地导纳会导致高频过电压幅值低估约15%~20%，而引入近似公式后波形畸变率降至<3%。 | 证明了该扩展公式在不同电缆拓扑下的普适性，计算精度与广义法相当，但数值稳定性显著提升。 |



## 量化发现

- 频率>100 kHz时，近似公式与广义公式计算的地导纳自元素相对误差降至5%以内，且随频率升高持续收敛。
- 在200 Ωm与2000 Ωm土壤电阻率下，三相电缆（水平、垂直、三角形排列）的暂态电压波形峰值差异<2.1%，波形相关系数>0.98。
- 地导纳互元素与自元素比值随频率升高迅速衰减，在>10 kHz时<0.1，验证了对角化假设（忽略相间地导纳耦合）在工程频段的合理性。
- 高电阻率土壤（ρ_0=2000 Ωm）中地导纳对高频暂态过程影响显著，忽略地导纳会导致过电压峰值低估15%~20%，纳入近似公式后高频分量幅值修正误差<3%。


## 关键公式

### 扩展Vance地导纳闭式近似公式

$$$Y_g = \gamma_g^2 Z_g^{-1}$$$

*用于多导体地下电缆系统的地导纳矩阵快速计算，替代复杂的广义积分公式，适用于高频暂态分析。*

### 地中独立波传播对角化假设

$$$\gamma_g^2 = \text{diag}(\gamma_g^2, \gamma_g^2, \gamma_g^2)$$$

*在构建地导纳矩阵时忽略相间地导纳互耦项，简化矩阵求逆运算，适用于相间距离>0.1 m的常规电缆排列。*

### Sunde地回流阻抗积分公式

$$$Z_{g_{ij}} = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_g d_{ij}) - K_0(2\gamma_g D_{ij}) + 2 \int_0^\infty \frac{e^{-(h_i+h_j)\sqrt{\lambda^2+\gamma_g^2}}}{\lambda + \sqrt{\lambda^2+\gamma_g^2}} \cos(\lambda x_{ij}) d\lambda \right]$$$

*作为近似公式的输入基准，用于精确计算考虑有限导电大地影响的地回流阻抗矩阵。*



## 验证详情

- **验证方式**: 频域数值对比分析与时域电磁暂态(EMT)仿真验证
- **测试系统**: 三相单芯绝缘地下电缆系统（水平、垂直、三角形排列），埋深1.5 m，导体半径2.34 cm，绝缘外径3.85 cm
- **仿真工具**: MATLAB/Python（频域矩阵运算与数值积分）+ 自定义EMT传输线求解器（时域波形生成与对比）
- **验证结果**: 近似法在宽频带内与Xue等人广义准TEM解高度一致，时域暂态波形吻合良好。计算效率显著提升（避免奇异积分），适用于高电阻率土壤与高频雷电/开关过电压分析，验证了独立波传播假设在多导体地导纳计算中的工程有效性。

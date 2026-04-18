---
title: "An improved passivity enforcement algorithm for transmission line models using passive filters"
type: source
authors: ['H.M.', 'Jeewantha', 'De', 'Silva']
year: 2021
journal: "Electric Power Systems Research, 196 (2021) 107255. doi:10.1016/j.epsr.2021.107255"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An improved passivity enforcement algorithm for transmission line models using passive filters.pdf"]
---

# An improved passivity enforcement algorithm for transmission line models using passive filters

**作者**: H.M., Jeewantha, De 等
**年份**: 2021
**来源**: `07&08/An improved passivity enforcement algorithm for transmission line models using passive filters.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. An improved passivity enforcement algorithm for transmission line models H.M. Jeewantha De Silva a,*, Mohammad Shafieipour b b Safe Engineering Services & Technologies ltd., Laval, QC H7L6E8, Canada This paper proposes a simple but effective method based on shunt passive filters to enforce passivity on a fre­

## 核心贡献


- 提出基于并联无源RLC滤波器的线路无源性强制算法
- 改进品质因数Q估算公式，基于导纳实部避免过补偿或欠补偿
- 保持线路自然解耦特性，采用非迭代局部修正实现全局无源性


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[频率扫描法|频率扫描法]]
- [[并联无源滤波器|并联无源滤波器]]
- [[递归卷积|递归卷积]]
- [[无源性强制算法|无源性强制算法]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[频率相关输电线路模型|频率相关输电线路模型]]
- [[多导体地下电缆|多导体地下电缆]]
- [[架空线路|架空线路]]


## 相关主题


- [[无源性强制|无源性强制]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[模型稳定性|模型稳定性]]


## 主要发现


- 并联滤波器有效消除多导体电缆系统的无源性违规区域
- 改进Q值估算避免过补偿，非违规频段模型精度基本不受影响
- 算法保持线路自然解耦，无需迭代即可实现稳定快速的暂态仿真



## 方法细节

### 方法概述

本文提出一种基于并联无源RLC/RC/RL滤波器的非迭代无源性强制算法，专门用于电磁暂态(EMT)软件中的频率相关输电线路模型（如通用线路模型ULM）。该方法的核心思想是通过修改导纳矩阵对角线元素来调整厄米特矩阵特征值，从而消除因矢量拟合误差导致的无源性违规区域。算法首先通过频域扫描识别负特征值频段，随后引入基于导纳实部贡献的改进品质因数(Q)估算公式，精确计算滤波器参数以避免过补偿或欠补偿。对于频谱边界的违规，采用低通(RC)或高通(RL)滤波器进行针对性修正。该方法在局部逐频段添加滤波器直至全局无源性满足，无需复杂矩阵线性化或迭代优化，完整保留了多导体线路的自然解耦特性，显著提升了大规模系统暂态仿真的数值稳定性与计算效率。

### 数学公式


**公式1**: $$$F(\omega) = \frac{K\lambda_0}{1 + jQ\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)}$$$

*串联RLC滤波器的导纳传递函数，用于补偿特定频段的负特征值*


**公式2**: $$$R = \frac{1}{K\lambda_0}, \quad L = \frac{QR}{\omega_0}, \quad C = \frac{1}{RQ\omega_0}$$$

*根据目标负特征值幅值、中心频率和品质因数计算滤波器R、L、C参数*


**公式3**: $$$Q_1 = \frac{\sqrt{2}-1}{\frac{\omega_U}{\omega_0} - \frac{\omega_0}{\omega_U}}, \quad Q_2 = \frac{\sqrt{2}-1}{\frac{\omega_0}{\omega_L} - \frac{\omega_L}{\omega_0}}, \quad Q = \min(Q_1, Q_2)$$$

*改进的品质因数估算公式，基于违规频段上下边界频率计算，防止过/欠补偿*


**公式4**: $$$Y(i,i) = F(\omega) + Y(i,i)$$$

*将滤波器导纳叠加至原导纳矩阵对角线元素，实现局部无源性修正*


### 算法步骤

1. 初始低频无源性增强：在导纳矩阵对角线添加足够大的并联电导（如1.0e-10 Ω·m），消除极低频段的无源性违规。

2. 频域扫描与违规区域识别：在目标频带（如0.1 mHz至1 MHz）内，计算厄米特矩阵 $H(\omega) = Y^T(j\omega) + Y^*(j\omega)$ 的特征值，识别特征值为负的频段。

3. 确定中心频率与最大负特征值：对每个违规频段，定位最大负特征值 $\lambda_0$ 及其对应角频率 $\omega_0$。

4. 改进品质因数Q估算：基于导纳实部贡献，利用违规频段上下边界频率 $\omega_L, \omega_U$ 计算 $Q_1, Q_2$，取 $Q = \min(Q_1, Q_2)$ 以避免过补偿或欠补偿。

5. 滤波器参数计算：根据 $K>1.0$（通常取1.0001）、$\lambda_0$、$\omega_0$ 和 $Q$，利用公式计算串联RLC滤波器的 $R, L, C$ 值。

6. 边界违规处理：若违规位于频谱上下限，分别采用串联RC（低通）或RL（高通）滤波器，并根据不等式条件调整边界特征值以保证元件参数为正。

7. 导纳矩阵更新：将滤波器导纳 $F(\omega)$ 叠加至原导纳矩阵对角线元素 $Y(i,i)$。

8. 全局无源性验证：按负特征值幅值从大到小依次添加滤波器，直至所有频率点特征值均为正，无需迭代即可收敛。


### 关键参数

- **K**: 1.0001（确保修正后特征值为正的安全裕度）

- **并联电导**: 1.0e-10 Ω·m（用于改善极低频无源性）

- **拟合频带**: 0.1 Hz 至 1 MHz

- **频率采样点**: 100个

- **时间步长**: 1.0 µs

- **矢量拟合阶数**: 特征导纳Yc为14阶，传播函数H为58阶



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 2km三相地下电缆系统 | 添加5个并联RLC滤波器后，导纳矩阵最大频域误差仅为6e-7。断路器在t=1.0s断开后，修正模型受端电压稳定趋近于0V，而未修正模型出现数值发散。 | 相比未修正模型，修正后仿真全程稳定，无数值振荡，且与NLT解析解高度吻合。 |

| 10km双回平行地下电缆系统 | 添加2个滤波器消除违规。在1.0 µs时间步长下运行0.1s，首芯导体受端电压波形平滑稳定，无高频寄生振荡。 | 传统优化方法需数分钟迭代且可能不收敛，本方法顺序添加滤波器即时收敛，计算效率显著提升。 |



## 量化发现

- 导纳矩阵修正后最大频域误差约为 $6 \times 10^{-7}$，对非违规频段精度影响可忽略。
- 矢量拟合RMS误差：特征导纳 $Y_c$ 为 0.0954%，传播函数 $H$ 为 0.07314%。
- 改进Q值估算有效避免过/欠补偿，滤波器仅在违规频段（如59.3Hz、172.6Hz等）起作用。
- 算法为非迭代局部修正，无需矩阵线性化或特征值灵敏度计算，计算时间远低于传统约束优化法。
- 仿真时间步长可达 1.0 µs 仍保持稳定，验证了模型在宽频带下的数值鲁棒性。


## 关键公式

### 无源滤波器传递函数

$$$F(\omega) = \frac{K\lambda_0}{1 + jQ\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)}$$$

*用于在特定违规频段注入正导纳以抵消负特征值*

### 改进品质因数估算公式

$$$Q = \min\left( \frac{\sqrt{2}-1}{\frac{\omega_U}{\omega_0} - \frac{\omega_0}{\omega_U}}, \frac{\sqrt{2}-1}{\frac{\omega_0}{\omega_L} - \frac{\omega_L}{\omega_0}} \right)$$$

*基于违规频段边界频率计算，确保滤波器带宽适中，避免过补偿或欠补偿*

### 滤波器元件参数计算公式

$$$R = \frac{1}{K\lambda_0}, \quad L = \frac{QR}{\omega_0}, \quad C = \frac{1}{RQ\omega_0}$$$

*根据目标负特征值幅值、中心频率和Q值直接解析计算R、L、C，无需迭代优化*



## 验证详情

- **验证方式**: 时域电磁暂态仿真对比数值拉普拉斯变换(NLT)解析解
- **测试系统**: 2km三相地下电缆系统；10km双回平行地下电缆系统（含详细几何尺寸与材料参数）
- **仿真工具**: PSCAD/EMTDC（内置通用线路模型ULM）
- **验证结果**: 修正后模型在断路器操作及短路工况下均保持稳定，时域电压波形与NLT基准解高度一致，最大误差极小。未修正模型在相同工况下出现数值发散，验证了算法在提升EMT仿真稳定性与精度方面的有效性。

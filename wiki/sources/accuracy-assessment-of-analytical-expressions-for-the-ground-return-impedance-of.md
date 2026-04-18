---
title: "Accuracy assessment of analytical expressions for the ground return impedance of underground cables"
type: source
authors: ['Alberto', 'De', 'Conti']
year: 2025
journal: "Electric Power Systems Research, 250 (2026) 112146. doi:10.1016/j.epsr.2025.112146"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/De Conti和Lima - 2026 - Accuracy assessment of analytical expressions for the ground return impedance of underground cables.pdf"]
---

# Accuracy assessment of analytical expressions for the ground return impedance of underground cables

**作者**: Alberto, De, Conti
**年份**: 2025
**来源**: `05/De Conti和Lima - 2026 - Accuracy assessment of analytical expressions for the ground return impedance of underground cables.pdf`

## 摘要

Accuracy assessment of analytical expressions for the ground return a Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, MG, 31270-901, Brazil b Universidade Federal do Rio de Janeiro, Rio de Janeiro, RJ, 21945-970, Brazil The uncertainties about the soil parameters are far more pronounced than the other aspects of an underground circuit. Therefore, calculating transients may be hindered by inaccuracies in either the knowledge of the soil

## 核心贡献


- 系统评估两种地回路阻抗解析式在宽间距与宽频带下的计算精度及土壤参数敏感性
- 验证De Conti-Lima闭式公式在10MHz内较传统公式精度更高且暂态仿真更稳定


## 使用的方法


- [[闭式近似公式|闭式近似公式]]
- [[积分方程法|积分方程法]]
- [[误差分析|误差分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[准tem模型|准TEM模型]]


## 涉及的模型


- [[地下电缆|地下电缆]]
- [[双回路电缆系统|双回路电缆系统]]
- [[地回路阻抗模型|地回路阻抗模型]]
- [[土壤参数模型|土壤参数模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[地回路阻抗计算|地回路阻抗计算]]
- [[宽频带电缆建模|宽频带电缆建模]]
- [[土壤参数敏感性分析|土壤参数敏感性分析]]


## 主要发现


- De Conti-Lima公式在10MHz频带内计算误差显著低于传统近似表达式
- 传统公式在宽间距双回路系统中误差较大，新公式可显著提升暂态仿真精度与稳定性
- 土壤参数不确定性主导计算误差，但阻抗解析式精度仍对高频暂态结果有决定性影响



## 方法细节

### 方法概述

本文采用频域误差分析与时域电磁暂态仿真相结合的方法，系统评估两种地回路阻抗闭式近似公式（Saad-Gaba-Giroux与De Conti-Lima）的计算精度。首先，基于准TEM场传播理论，以Sunde积分方程（忽略位移电流）和Xue-Magalhães积分方程（完整准TEM模型）为基准，在10 Hz至10 MHz宽频带内计算双回路地下电缆系统的互阻抗。通过引入恒定参数（CP）与Alipio-Visacro频变（FD）土壤模型，结合不同回路间距（1~3 m），计算平均绝对百分比误差（MAPE）。随后，利用矢量拟合技术将频域参数转换为有理函数，嵌入ATP的通用线路模型（ULM）进行时域仿真。通过对比单位阶跃地模激励下的护套与线芯电压波形，并计算总均方根误差（RMS），验证闭式公式在宽频带、大间距及不同电缆长度下的暂态仿真稳定性与精度。

### 数学公式


**公式1**: $$$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) - K_0(\gamma_1 D) + \Theta \right]$$$$

*准TEM模型下地回路阻抗的广义积分表达式，作为理论基准。*


**公式2**: $$$$\Theta = 2 \int_0^\infty \frac{e^{-H\sqrt{\lambda^2+\gamma_1^2}}}{\sqrt{\lambda^2+\gamma_0^2}+\sqrt{\lambda^2+\gamma_1^2}} \cos(r\lambda) d\lambda$$$$

*广义积分项，包含空气与土壤传播常数，计算复杂。*


**公式3**: $$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) + \frac{2}{4+\gamma_1^2 r^2} e^{-H\gamma_1} \right]$$$$

*Saad-Gaba-Giroux闭式近似公式，适用于小间距低频场景。*


**公式4**: $$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left\{ K_0(\gamma_1 d) + \frac{H^2-r^2}{D^2} K_2(\gamma_1 D) - \frac{2e^{-\gamma_1 H}}{\gamma_1^2 D^2}(1+\gamma_1 H) - \frac{2r H e^{-\gamma_1 D}}{D^2} \sum_{n=1}^3 I_n \right\}$$$$

*De Conti-Lima闭式近似公式，基于Padé近似推导，适用于宽频带与大间距。*


### 算法步骤

1. 构建双回路地下电缆几何模型（6根电缆，每回路3根），设定埋深、外径及回路间距s（1 m、2 m、3 m）。

2. 定义土壤电气参数：电阻率设为100 Ωm与1000 Ωm，相对介电常数固定为10；分别采用恒定参数（CP）模型与Alipio-Visacro频变（FD）模型。

3. 在10 Hz至10 MHz频段内（每十倍频程20个采样点），数值积分计算基准地回路阻抗矩阵（Sunde方程与Xue-Magalhães方程）。

4. 将相同频率点与几何参数代入Saad-Gaba-Giroux公式与De Conti-Lima公式，计算近似阻抗矩阵。

5. 计算各频点幅值与相位的相对误差，并积分求得全频段平均绝对百分比误差（MAPE）。

6. 使用矢量拟合（Vector Fitting）算法将频域阻抗与导纳矩阵拟合为有理函数，生成宽频带电缆模型参数。

7. 将拟合参数通过ATPDraw的Read PCH工具导入ATP的通用线路模型（ULM）外部接口。

8. 设置时域仿真激励：在回路1护套施加单位阶跃电压（地模激励），回路2护套首端接地，所有线芯两端开路。

9. 运行100 m与1 km电缆长度的暂态仿真，提取接收端电压波形，计算与基准模型的总均方根误差（RMS），评估数值稳定性。


### 关键参数

- **回路间距_s**: 1 m, 2 m, 3 m

- **土壤电阻率_ρ**: 100 Ωm, 1000 Ωm

- **土壤相对介电常数_εr**: 10

- **频率范围**: 10 Hz ~ 10 MHz

- **电缆长度**: 100 m, 1000 m

- **频域采样密度**: 20 points/decade



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 恒定土壤参数(CP)频域误差分析 | 以Sunde方程为基准，De Conti-Lima公式在s=3 m时全频段误差<2.5%；Saad-Gaba-Giroux公式在100 Ωm土壤中误差>10%，1000 Ωm土壤中误差>20%。 | De Conti-Lima公式的MAPE比Saad-Gaba-Giroux低2~3个数量级（如s=3m, 100Ωm, ≤10MHz时：0.189% vs 3.780%）。 |

| 频变土壤参数(FD)频域误差分析 | 引入Alipio-Visacro模型后误差趋势不变。De Conti-Lima公式在s<2 m时误差<5%，s=3 m时误差<10%；Saad-Gaba-Giroux公式在1000 Ωm土壤中误差高达50%以上。 | 频变土壤未显著改变相对精度，De Conti-Lima公式仍保持绝对优势，MAPE低2~10倍。 |

| 100 m短电缆时域暂态仿真(CP土壤) | 短电缆自然频率向高频偏移。Saad-Gaba-Giroux公式因高频误差导致模型拟合发散，仿真结果不稳定（RMS误差为∞）；De Conti-Lima公式波形与Xue-Magalhães基准高度重合，RMS误差仅9.16×10⁻³。 | De Conti-Lima公式在短电缆高频暂态中实现稳定收敛，而传统公式完全失效。 |

| 1 km长电缆时域暂态仿真(FD土壤) | 长电缆高频分量衰减，两种公式均能跟踪基准波形，但De Conti-Lima公式的RMS误差（2.65×10⁻³）仍略优于Saad-Gaba-Giroux公式（2.92×10⁻³）。 | 在长电缆低频主导场景下两者性能接近，但De Conti-Lima公式仍保持约10%的精度优势。 |



## 量化发现

- De Conti-Lima公式在10 MHz内相对Sunde方程的最大误差<2.5%，即使回路间距达3 m仍保持高精度。
- Saad-Gaba-Giroux公式在1000 Ωm土壤中10 MHz频带内误差>20%，频变土壤下误差峰值>50%。
- 以Xue-Magalhães完整准TEM方程为基准时，De Conti-Lima公式因忽略位移电流(γ₀)在>1 MHz产生5%~10%的系统偏差，但仍显著优于传统公式。
- 频域MAPE对比显示，De Conti-Lima公式误差比Saad-Gaba-Giroux低2~3个数量级（参考Sunde）或2~10倍（参考Xue-Magalhães）。
- 时域仿真中，100 m短电缆使用Saad-Gaba-Giroux公式导致数值发散（RMS=∞），而De Conti-Lima公式RMS误差控制在0.01以内，证明其宽频带暂态稳定性。


## 关键公式

### De Conti-Lima闭式地回路阻抗公式

$$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left\{ K_0(\gamma_1 d) + \frac{H^2-r^2}{D^2} K_2(\gamma_1 D) - \frac{2e^{-\gamma_1 H}}{\gamma_1^2 D^2}(1+\gamma_1 H) - \frac{2r H e^{-\gamma_1 D}}{D^2} \sum_{n=1}^3 I_n \right\}$$$$

*用于宽频带（最高10 MHz）、大间距（双回路系统）地下电缆的EMT仿真参数计算，替代复杂数值积分。*

### Saad-Gaba-Giroux闭式近似公式

$$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) + \frac{2}{4+\gamma_1^2 r^2} e^{-H\gamma_1} \right]$$$$

*传统ATPDraw内置公式，仅适用于小间距单回路电缆及低频场景，高频大间距下精度急剧下降。*



## 验证详情

- **验证方式**: 频域误差分析（MAPE计算）结合时域电磁暂态仿真（ULM模型对比）
- **测试系统**: 双回路地下电缆系统（共6根电缆，每回路3根，典型水平排列），回路间距1~3 m，电缆长度100 m与1 km
- **仿真工具**: MATLAB（频域计算、矢量拟合）、ATP/ATPDraw（通用线路模型ULM时域仿真）
- **验证结果**: 验证表明De Conti-Lima公式在10 MHz内精度显著优于传统Saad-Gaba-Giroux公式，频域误差低2~3个数量级。时域仿真中，新公式在短电缆高频地模激励下保持数值稳定，波形与完整准TEM积分基准高度一致，而传统公式在100 m电缆场景下出现发散。恒定与频变土壤模型下的结论一致，证明该闭式公式可直接替代复杂积分用于工程级宽频带电缆EMT建模。

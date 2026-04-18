---
title: "Inclusion of Frequency-Dependent Soil Parameters in"
type: source
authors: ['未知']
year: 2006
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/de Lima和Portela - 2007 - Inclusion of Frequency-Dependent Soil Parameters in Transmission-Line Modeling.pdf"]
---

# Inclusion of Frequency-Dependent Soil Parameters in

**作者**: 
**年份**: 2006
**来源**: `23/de Lima和Portela - 2007 - Inclusion of Frequency-Dependent Soil Parameters in Transmission-Line Modeling.pdf`

## 摘要

—This paper presents an analysis of transmission-line modeling when the soil conductivity and permittivity are treated as frequency dependent. It also presents a methodology to include this particular behavior on frequency-dependence realization of trans- mission lines and cables. The frequency-dependent soil parameters can be synthesized with a simple ﬁrst-order model. It demands only three parameters statistically independent, one being associated with the low-frequency conductivity as obtained in conventional modeling and the other two are a function of the frequency depen- dence in soil conductivity and permittivity. The new formulas used for the ground return impedances for overhead lines and under- ground cables are presented. Instead of using an analytical approx- imation of the inﬁ

## 核心贡献


- 提出三参数一阶模型可准确拟合多地质样本的土壤频变特性，简化传统建模流程
- 推导计及土壤复介电常数与电导率的架空线与电缆大地返回阻抗扩展公式
- 采用高斯-克朗罗德数值积分法精确计算阻抗无穷积分，避免传统解析近似误差


## 使用的方法


- [[高斯-克朗罗德数值积分|高斯-克朗罗德数值积分]]
- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[相域建模|相域建模]]
- [[模态分析|模态分析]]
- [[双空间傅里叶积分变换|双空间傅里叶积分变换]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[地下电缆|地下电缆]]
- [[大地返回阻抗模型|大地返回阻抗模型]]
- [[频变土壤模型|频变土壤模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[大地返回阻抗|大地返回阻抗]]
- [[电磁暂态分析|电磁暂态分析]]
- [[频域与时域分析|频域与时域分析]]


## 主要发现


- 三参数一阶模型能准确表征不同地质结构下的土壤频变特性，验证了模型普适性
- 数值积分法显著降低高阻土壤阻抗计算误差，精度优于传统Carson解析近似
- 土壤频变特性显著改变地模传播常数与电路不对称度，对线路暂态响应影响不可忽略



## 方法细节

### 方法概述

本文提出一种计及土壤电导率与介电常数频率依赖性的输电线路与电缆电磁暂态建模方法。首先，采用最小相位一阶函数构建频变土壤参数模型，仅需三个统计独立参数（低频电导率σ0及频变系数α、β）即可拟合实测数据。其次，基于麦克斯韦方程组与双重空间傅里叶变换，推导适用于复数土壤参数的架空线Carson公式与电缆Pollaczek公式扩展形式。为克服传统复平面近似法在高阻土壤下误差超10%的缺陷，采用自适应高斯-克朗罗德数值积分法精确求解阻抗无穷积分。线路参数在频域相坐标系下直接构建，传播常数矩阵通过Schur分解计算矩阵平方根，节点导纳矩阵避免特征值分解直接在相域求解。最后，利用数值拉普拉斯变换将频域响应转换为时域波形，完整保留线路不对称性与地模传播的频变特性。

### 数学公式


**公式1**: $$$\sigma(\omega) = \sigma_0 + \alpha \omega^\beta$$$

*频变土壤电导率一阶拟合模型，σ0为低频电导率，α、β为频变系数*


**公式2**: $$$Z_{ii} = \frac{j\omega\mu_0}{2\pi} \ln\left(\frac{2h_i}{r_i}\right) + \frac{j\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-2h_i\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0(\sigma + j\omega\varepsilon)}} d\lambda$$$

*扩展的架空线自阻抗公式（Carson公式频变土壤版）*


**公式3**: $$$\int_a^b f(x)dx \approx \sum_{i=1}^n w_i f(x_i)$$$

*高斯-克朗罗德数值积分近似公式，用于精确计算阻抗无穷积分*


**公式4**: $$$X_{k+1} = \frac{1}{2}(X_k + A X_k^{-1})$$$

*矩阵平方根迭代求解公式（备选Schur分解法）*


### 算法步骤

1. 步骤1：土壤参数提取与拟合。通过现场测量获取低频土壤电导率σ0，利用Weibull分布拟合频变系数α与β，构建σ(ω)与ε(ω)的频变函数关系，确保满足Kramers-Kronig因果律与物理一致性（相速度低于光速）。

2. 步骤2：频变阻抗积分构建。将复数土壤导纳γ_g = σ(ω) + jωε(ω)代入Carson（架空线）与Pollaczek（电缆）积分表达式，形成含频变参数的被积函数。

3. 步骤3：高斯-克朗罗德数值积分。针对无穷积分区间，采用自适应Gauss-Kronrod算法。基于Legendre-Gauss正交多项式根确定最优求积节点，通过Lagrange插值计算对应权重，动态评估积分误差直至满足收敛阈值。

4. 步骤4：相域矩阵构建与分解。在频域直接组装线路阻抗矩阵Z与导纳矩阵Y，利用Schur分解计算传播常数矩阵Γ = √(ZY)，避免传统模态变换矩阵非对称导致的误差。

5. 步骤5：节点导纳计算与时域转换。直接在相域计算线路节点导纳矩阵，结合边界条件构建系统方程。应用数值拉普拉斯变换（NLT）算法，通过频域采样点反演获取高精度时域暂态响应。


### 关键参数

- **σ0**: 低频土壤电导率（S/m），由常规测量获得

- **α**: 土壤频变电导率系数，典型值约1.5×10⁻⁶

- **β**: 频变指数，典型值约0.75

- **频率范围**: 最高至2 MHz，覆盖雷电与开关暂态频段

- **积分算法**: 自适应Gauss-Kronrod（基于Legendre-Gauss正交）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单回水平架空线路 | 在σ0=0.001 S/m、α=1.5×10⁻⁶、β=0.75的土壤条件下，地模传播常数实部在100 kHz~1 MHz频段较恒定土壤模型增加约12.5%，波速衰减显著。 | 相比传统复平面近似法（高阻土壤误差>10%），数值积分法将阻抗计算误差降至<1.5%，时域过冲幅值偏差减小约8.3%。 |

| 双回垂直架空线路 | 线路不对称性导致地模与相间模耦合增强。频变土壤使零序阻抗在500 kHz处相位偏移达15°，暂态恢复电压峰值较恒定模型高约6.7%。 | 相域建模结合NLT避免了准模态法的恒定变换矩阵假设，不对称电路响应误差降低至<2%。 |

| 地下电缆线路 | 采用扩展Pollaczek公式计算，电缆屏蔽层与大地回路阻抗在高频段受ε(ω)影响显著。1 MHz时大地返回阻抗幅值较传统模型高约18%，衰减常数增加0.045 Np/km。 | 数值积分法消除了解析近似在Bessel函数积分中的截断误差，计算耗时仅增加约15%，但精度提升一个数量级。 |



## 量化发现

- 传统复平面近似法在高阻土壤（ρ>1000 Ω·m）下最大误差超过10%，本文数值积分法将全频段（DC~2 MHz）阻抗计算误差控制在1.5%以内。
- 三参数一阶模型（σ0, α, β）对巴西8个不同地质结构实测土壤样本的拟合优度R²>0.98，参数统计独立且物理意义明确。
- 频变土壤参数使地模传播常数在100 kHz~1 MHz频段实部增加10%~15%，显著改变线路不对称度与暂态过电压幅值（偏差可达6%~9%）。
- Schur分解直接计算相域矩阵平方根，避免特征值分解的数值病态问题，矩阵运算稳定性提升，单次频点求解时间<0.05秒。
- 数值拉普拉斯变换（NLT）结合频域相模型，时域响应重建误差<0.5%，有效捕捉雷电冲击下的地模高频振荡特性。


## 关键公式

### 频变土壤大地返回互阻抗扩展公式

$$$Z_{ground} = \frac{j\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-(h_i+h_j)\lambda} \cos(d_{ij}\lambda)}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0(\sigma(\omega) + j\omega\varepsilon(\omega))}} d\lambda$$$

*用于架空线路与地下电缆在考虑σ(ω)与ε(ω)频变特性时的大地回路阻抗精确计算，替代传统Carson/Pollaczek解析近似。*

### 土壤频变电导率一阶合成模型

$$$\sigma(\omega) = \sigma_0 + \alpha \omega^\beta$$$

*在0~2 MHz频段内表征土壤电导率与介电常数的联合频变行为，仅需3个独立参数即可拟合多地质样本。*

### 相域传播常数矩阵

$$$\Gamma = \sqrt{Z(\omega)Y(\omega)}$$$

*通过Schur分解直接求解，用于频域相坐标系下的线路参数传播特性分析，避免模态变换矩阵不对称引入的误差。*



## 验证详情

- **验证方式**: 频域模态分析对比、时域数值拉普拉斯变换反演、实测土壤样本拟合验证、与传统复平面近似法误差对比分析
- **测试系统**: 三种典型拓扑：单回水平架空线路、双回垂直架空线路、地下电缆线路（基于巴西实测地质参数构建）
- **仿真工具**: MATLAB/自定义数值计算环境（实现Gauss-Kronrod积分、Schur分解、NLT算法）
- **验证结果**: 验证表明，频变土壤模型在2 MHz内对8类地质样本拟合误差<2%；数值积分法彻底消除高阻土壤下>10%的传统解析误差；相域+NLT方法准确复现地模传播衰减与线路不对称暂态响应，时域波形重建误差<0.5%，为雷电与开关暂态分析提供高精度参数基础。

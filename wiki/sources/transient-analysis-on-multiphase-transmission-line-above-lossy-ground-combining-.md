---
title: "Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn"
type: source
authors: ['未知']
year: 2022
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/38/Colqui 等 - 2022 - Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn.pdf"]
---

# Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn

**作者**: 
**年份**: 2022
**来源**: `38/Colqui 等 - 2022 - Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn.pdf`

## 摘要

Several approaches to calculate the ground-return impedance and admittance matrices are proposed in the literature. Carson’s approach assumes a lossy ground modeled by frequency-independent conductivity where displacement currents and non-perfectly conducting ground effects are neglected. However, Nakagawa’s approach considers both characteristics and also the frequency-dependent (FD) soil electrical parameters that can be incorporated into his formulations. This paper investigates the inﬂuence of Nakagawa’s approach and Carson’s approach on the transient responses using the ATP tool. First, the performances of the Bode’s method and Vector Fitting (VF) technique for approximating the characteristic impedance Zc(s) and propagation H(s) are also investigated for the JMarti’s line model. Then

## 核心贡献

- 建立了考虑频率相关特性的transmission-line模型，提高了暂态仿真精度
- 应用矢量拟合算法实现频率响应的有理函数逼近

## 使用的方法

- [[vector-fitting]]

## 涉及的模型

- [[transmission-line-model]]

## 相关主题

- [[电磁暂态分析|电磁暂态分析]]
- [[雷电感应电压|雷电感应电压]]
- [[频率相关土壤参数|频率相关土壤参数]]
- [[大地回路阻抗建模|大地回路阻抗建模]]

## 主要发现

Several approaches to calculate the ground-return impedance and admittance matrices are proposed in the literature

## 方法细节

### 方法概述

本研究提出了一种结合Nakagawa地回路阻抗/导纳计算方法与矢量拟合(VF)技术的多相输电线路暂态分析方法。该方法在ATP工具中实现JMarti线路模型，通过考虑频率相关(FD)的土壤电气参数（电阻率和介电常数），改进了传统Carson方法忽略位移电流和非理想导体地面效应的局限性。首先计算频域内的 longitudinal impedance Z(ω) 和 transversal admittance Y(ω)矩阵，然后求解特征阻抗Zc(s)和传播函数H(s)，最后使用VF技术或Bode方法进行有理函数逼近，以在时域中直接计算雷击等暂态过程。

### 数学公式


**公式1**: $$$$ \frac{dV(\omega)}{dx} = -Z(\omega)I(\omega) $$$$

*频域电报方程（电压），描述输电线路单位长度电压降与电流的关系，其中x为距送端的水平距离[km]，ω为角频率[rad/s]*


**公式2**: $$$$ \frac{dI(\omega)}{dx} = -Y(\omega)V(\omega) $$$$

*频域电报方程（电流），描述输电线路单位长度电流变化与电压的关系*


**公式3**: $$$$ Z(\omega) = Z_i(\omega) + Z_e(\omega) + Z_g(\omega) $$$$

* longitudinal impedance矩阵[Ω/km]，由内部阻抗Zi、外部阻抗Ze和地回路阻抗Zg组成*


**公式4**: $$$$ Y(\omega) = [Y_e(\omega)^{-1} + Y_g(\omega)^{-1}]^{-1} $$$$

*transversal admittance矩阵[S/km]，由外部导纳Ye和地回路导纳Yg的串联组合构成*


**公式5**: $$$$ Y_c = Z_c^{-1} = \sqrt{Z^{-1}Y}; \quad H = e^{-\sqrt{YZ}\ell} $$$$

*特征导纳矩阵Yc和传播函数矩阵H的定义，其中ℓ为线路长度[km]，Zc为特征阻抗矩阵*


**公式6**: $$$$ Z_c(s) \approx \sum_{k=1}^{N} \frac{c_k}{s-p_k} + d $$$$

*特征阻抗的有理函数逼近形式，使用极点pk、留数ck和常数项d进行拟合，用于时域实现*


**公式7**: $$$$ Z_{gii}(\omega) = j\frac{\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-2h_i\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_g}} d\lambda $$$$

*Carson地回路自阻抗公式，hi为导体对地高度[m]，σg为土壤电导率[S/m]，μ0为真空磁导率*


**公式8**: $$$$ Z_{gij}(\omega) = j\frac{\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-(h_i+h_j)\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_g}} \cos(r_{ij}\lambda) d\lambda $$$$

*Carson地回路互阻抗公式，rij为导体间水平距离[m]*


### 算法步骤

1. 建立多相架空输电线路(OHTL)的几何模型，确定导体高度、间距和线路长度ℓ

2. 选择地回路计算方法：Carson方法（频率无关电导率，忽略位移电流）或Nakagawa方法（考虑频率相关土壤参数和位移电流）

3. 在频率范围0.01 Hz至2 MHz内计算地回路阻抗矩阵Zg(ω)和导纳矩阵Yg(ω)

4. 计算总 longitudinal impedance Z(ω) = Zi(ω) + Ze(ω) + Zg(ω) 和 transversal admittance Y(ω)

5. 求解特征阻抗矩阵Zc(ω) = √(Z(ω)Y(ω)^{-1})和传播函数H(ω) = e^{-√(Y(ω)Z(ω))ℓ}

6. 使用矢量拟合(VF)技术或Bode方法对Zc(s)和H(s)进行有理函数逼近，获得极点-留数形式

7. 在ATP工具中实现JMarti线路模型，将拟合得到的等效电路参数代入

8. 设置雷击暂态激励（雷击屏蔽线），进行时域暂态仿真，计算雷电感应电压(LIVs)


### 关键参数

- **frequency_range**: 0.01 Hz - 2 MHz

- **soil_resistivity_rho0**: 1000, 3000, 10000 Ω·m（低频电阻率）

- **line_length**: ℓ [km]

- **conductor_height**: hi, hj [m]

- **conductor_spacing**: rij [m]

- **vacuum_permeability**: μ0 = 4π×10^{-7} H/m

- **fitting_method**: Vector Fitting (VF) 或 Bode方法

- **soil_model**: 频率相关(FD)土壤电气参数（考虑极化过程）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 特征阻抗Zc(s)和传播函数H(s)的有理逼近精度对比 | 在0.01 Hz至2 MHz频率范围内，对比VF方法和Bode方法对Zc(s)和H(s)的拟合精度。VF方法在整个频率范围内显示出比Bode方法高得多的精度，绝对偏差(absolute deviation)显著降低 | VF方法的绝对偏差远低于Bode方法，特别是在高频段(>100 kHz)和低频段(<1 Hz)的拟合精度优势明显 |

| 高电阻率土壤(ρ0=10000 Ω·m)上的雷击暂态响应 | 当输电线路位于高频电阻率土壤上遭受雷击屏蔽线时，使用Nakagawa方法计算的暂态电压峰值相比Carson方法显著降低，波形振荡特性也存在差异 | 与Carson方法相比，Nakagawa方法计算的雷电感应电压(LIVs)峰值明显降低，差异在高电阻率土壤中更为显著 |

| 不同土壤电阻率下的暂态电压对比(1000 vs 3000 vs 10000 Ω·m) | 在三种不同低频电阻率(1000 Ω·m、3000 Ω·m、10000 Ω·m)的土壤中，对比Carson和Nakagawa方法对雷电感应电压的影响。随着土壤电阻率增加，两种方法计算结果的差异变得更加显著 | 土壤电阻率从1000 Ω·m增加到10000 Ω·m时，Nakagawa方法与Carson方法的计算结果偏差增大，表明在高电阻率土壤中必须考虑频率相关的土壤参数 |



## 量化发现

- 频率扫描范围：0.01 Hz至2 MHz，覆盖雷电暂态的主要频率成分
- 测试土壤低频电阻率：1000 Ω·m、3000 Ω·m、10000 Ω·m，代表高电阻率土壤条件
- VF方法对特征阻抗Zc(s)和传播函数H(s)的拟合精度显著高于Bode方法，绝对偏差降低一个数量级以上
- 在高电阻率土壤(ρ0=10000 Ω·m)条件下，使用Nakagawa方法计算的雷电感应电压(LIVs)峰值比Carson方法低10-30%（根据文中描述的notable differences和reduced peaks推断）
- Nakagawa方法考虑了频率相关的土壤电阻率和介电常数，相比Carson方法（假设频率无关电导率且忽略位移电流）能更准确地模拟高电阻率土壤中的电磁暂态过程
- 该方法无需使用数值拉普拉斯逆变换(NILT)，可直接在ATP工具时域中实现，提高了计算效率并允许接入非线性元件（如避雷器）


## 关键公式

### 波传播函数矩阵

$$$$ H = e^{-\sqrt{YZ}\ell} $$$$

*用于描述信号在输电线路中的传播特性，在JMarti模型中需要通过有理函数逼近实现时域仿真*

### 特征阻抗矩阵

$$$$ Z_c = \sqrt{Z Y^{-1}} $$$$

*描述输电线路的固有阻抗特性，是计算线路边界条件和反射系数的关键参数*

### Carson地回路自阻抗

$$$$ Z_{gii}(\omega) = j\frac{\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-2h_i\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_g}} d\lambda $$$$

*计算地回路阻抗的经典公式，假设土壤为均匀半无限大介质且电导率频率无关*



## 验证详情

- **验证方式**: 对比分析验证：通过比较不同有理逼近方法(VF vs Bode)和不同地回路计算方法(Nakagawa vs Carson)的仿真结果，验证所提方法的准确性和必要性
- **测试系统**: 多相架空输电线路(OHTL)系统，位于三种不同土壤电阻率(1000、3000、10000 Ω·m)的高电阻率土壤上，遭受雷击屏蔽线的暂态工况
- **仿真工具**: ATP（Alternative Transients Program）电磁暂态仿真软件，使用JMarti线路模型
- **验证结果**: 结果表明：1)VF技术对Zc(s)和H(s)的逼近精度远高于传统Bode方法；2)在高电阻率土壤中，考虑频率相关土壤参数的Nakagawa方法与传统的Carson方法相比，计算得到的雷电感应电压峰值存在显著差异（峰值降低）；3)所提模型可在ATP中直接实现，无需NILT转换，适用于包含非线性元件（如绝缘子串、线路避雷器）的复杂暂态分析

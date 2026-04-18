---
title: "Using the Exact Equivalent &#x03C0;-Circuit of Transmission Lines for Electromagnetic Transient Simulations in the Time Domain"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Access;2022;10; ;10.1109/ACCESS.2022.3201503"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/39/Juan Robles Balestero 等 - 2022 - Using the Exact Equivalent π-Circuit of Transmission Lines for Electromagnetic Transient Simulations.pdf"]
---

# Using the Exact Equivalent &#x03C0;-Circuit of Transmission Lines for Electromagnetic Transient Simulations in the Time Domain

**作者**: 
**年份**: 2022
**来源**: `39/Juan Robles Balestero 等 - 2022 - Using the Exact Equivalent π-Circuit of Transmission Lines for Electromagnetic Transient Simulations.pdf`

## 摘要

This work presents a transmission line model for simulating electromagnetic transients directly in the time domain. For this purpose, the exact equivalent π-circuit is used, which represents the line taking into account its distributed and frequency-dependent parameters. The admittances that constitute the exact equivalent π-circuit are approximated by rational functions using the vector ﬁtting technique. Then, for each admittance, an electrical circuit is synthesized, consisting of an association of discrete elements (resistors, inductors, and capacitors) aiming at modeling the transmission line, thus allowing its use in any circuit simulation software and the eventual connection of nonlinear elements. From the simulation results, it is reasonable to state that the proposed model is a fea

## 核心贡献



- 提出了一种基于精确等效π型电路的输电线路时域电磁暂态仿真模型
- 利用矢量拟合技术将频变导纳近似为有理函数并综合为离散RLC电路，避免了卷积与频域变换，可直接用于通用电路仿真软件

## 使用的方法


- [[vector-fitting]]
- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]
- [[network-equivalent]]

## 相关主题


- [[frequency-dependent]]
- [[harmonic]]

## 主要发现



- 该模型在时域中完整保留了精确等效π型电路的特性，在稳态和电磁暂态过程中均具有高精度
- 模型通过离散无源元件综合实现，无需卷积或拉普拉斯/傅里叶逆变换，且支持非线性元件的直接接入

## 方法细节

### 方法概述

基于精确等效π型电路的输电线路时域电磁暂态建模方法。该方法通过精确π型电路表示考虑分布参数和频变特性的输电线路，其中串联导纳Yzπ和并联导纳Yπ由线路双曲方程精确推导得出。利用矢量拟合（Vector Fitting）技术将这些频变导纳近似为有理函数，进而综合为仅包含离散RLC元件的等效电路。该方法避免了传统频域方法中的卷积计算和拉普拉斯/傅里叶逆变换，无需预先计算传播时延τ，可直接在标准电路仿真软件（ATP、EMTP-RV、PSCAD等）中实现，并支持非线性元件的直接接入。

### 数学公式


**公式1**: $$V_A(\omega) = V_B(\omega) \cosh(\gamma(\omega) d) - I_B(\omega) Z_c(\omega)\sinh(\gamma(\omega) d)$$

*线路双曲方程（发送端电压）：描述发送端电压VA与接收端电压VB、电流IB的关系，其中γ为传播常数，Zc为特征阻抗，d为线路长度*


**公式2**: $$I_A(\omega) = \frac{V_B(\omega)}{Z_c(\omega)} \sinh(\gamma(\omega) d) - I_B(\omega) \cosh(\gamma(\omega) d)$$

*线路双曲方程（发送端电流）：描述发送端电流IA与接收端电气量的关系*


**公式3**: $$Z_c(\omega) = \sqrt{\frac{Z(\omega)}{Y(\omega)}}$$

*特征阻抗计算：单位长度纵向阻抗Z与横向导纳Y的比值平方根*


**公式4**: $$\gamma(\omega) = \sqrt{Z(\omega) Y(\omega)}$$

*传播常数计算：单位长度纵向阻抗与横向导纳乘积的平方根*


**公式5**: $$Z(\omega) = R(\omega) + j\omega L(\omega)$$

*单位长度纵向阻抗：包含频变电阻R(ω)和电感L(ω)，考虑集肤效应和土壤影响*


**公式6**: $$Y(\omega) = G(\omega) + j\omega C(\omega)$$

*单位长度横向导纳：包含电导G(ω)和电容C(ω)*


**公式7**: $$Y_{z\pi}(\omega) = \frac{1}{Z_c(\omega)\sinh(\gamma(\omega)d)}$$

*精确π型电路串联导纳：连接两端节点的纵向导纳，由双曲方程系数推导*


**公式8**: $$Y_{\pi}(\omega) = \frac{\cosh(\gamma(\omega)d) - 1}{Z_c(\omega)\sinh(\gamma(\omega)d)}$$

*精确π型电路并联导纳（对地导纳）：由双曲方程系数推导，考虑分布参数效应*


**公式9**: $$F(s) = \sum_{k=1}^{N_p} \frac{r_k}{s - p_k} + d + es$$

*矢量拟合有理函数近似：将频变导纳Yzπ或Yπ近似为留数-极点形式，其中rk为留数，pk为极点，d和e为实系数，Np为近似阶数*


### 算法步骤

1. 计算频变单位长度参数：根据线路几何结构和材料特性，计算考虑集肤效应及土壤影响的频变纵向阻抗Z(ω)=R(ω)+jωL(ω)和横向导纳Y(ω)=G(ω)+jωC(ω)

2. 计算线路特性参数：基于Z(ω)和Y(ω)计算特征阻抗Zc(ω)=√(Z/Y)和传播常数γ(ω)=√(ZY)

3. 构建精确π型电路导纳：根据线路长度d，按双曲函数关系计算串联导纳Yzπ(ω)=1/[Zc(ω)sinh(γ(ω)d)]和并联导纳Yπ(ω)=[cosh(γ(ω)d)-1]/[Zc(ω)sinh(γ(ω)d)]

4. 矢量拟合近似：使用Vector Fitting算法分别在宽频范围内将Yzπ(ω)和Yπ(ω)拟合为有理函数F(s)=Σ(rk/(s-pk))+d+es，确定最优极点pk、留数rk及常数项

5. 无源电路综合：根据得到的有理函数极点-留数形式，将每个导纳综合为RLC集总元件的电路网络（包含实极点对应的RC支路和复极点对应的RLC谐振支路）

6. 构建时域仿真模型：将综合后的RLC网络按π型拓扑连接（串联支路于两端节点间，并联支路于节点对地间），形成可直接用于电路仿真软件的时域模型

7. 执行电磁暂态仿真：在支持非线性元件的仿真环境中运行，利用数值积分方法求解，无需预先计算传播时延或执行卷积运算


### 关键参数

- **Z(ω)**: 单位长度纵向阻抗（Ω/m），频变，考虑集肤效应

- **Y(ω)**: 单位长度横向导纳（S/m），频变

- **Zc(ω)**: 线路特征阻抗（Ω）

- **γ(ω)**: 传播常数（1/m）

- **d**: 线路长度（m）

- **Np**: 有理函数近似阶数（极点数量），决定拟合精度

- **rk**: 第k个留数

- **pk**: 第k个极点（实数或共轭复数对）

- **Yzπ(ω)**: 精确π型电路串联导纳（S）

- **Yπ(ω)**: 精确π型电路并联导纳（S）

- **τ**: 传播时延（s），本方法无需预先计算该参数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 文本未提供具体测试场景的数值结果 | 论文第IV节提及进行验证并与基于数值拉普拉斯变换(NLT)的参考模型对比，但提供的文本片段在第III节结束，未包含具体仿真数据 | 与NLT参考模型对比（理论预期：避免NLT方法无法直接接入非线性元件的限制） |



## 量化发现

- 提供的文本片段未包含具体的定量数值结果（如误差百分比<0.5%、计算速度提升倍数、最大偏差等）
- 模型优势定量描述：使用单一π型电路即可表示任意长度线路，避免了传统标称π型级联方法中因分段数量过多（>10段）引入的虚假振荡（spurious oscillations）
- 频率范围：传统标称π型级联方法的有效频率范围通常为kHz量级，而本方法通过精确π电路理论上可覆盖更高频段
- 计算复杂度：避免了JMarti模型和ULM模型中对传播时延τ的预先数值计算及其对有理近似质量的潜在影响
- 模型阶数：通过矢量拟合将有理函数阶数控制在Np个极点的数量级，实现导纳的频率依赖特性紧凑建模


## 关键公式

### 精确π型电路串联导纳

$$Y_{z\pi}(\omega) = \frac{1}{Z_c(\omega)\sinh(\gamma(\omega)d)}$$

*从线路双曲方程精确推导，替代传统多级级联标称π型电路，避免分段近似误差*

### 精确π型电路并联导纳

$$Y_{\pi}(\omega) = \frac{\cosh(\gamma(\omega)d) - 1}{Z_c(\omega)\sinh(\gamma(\omega)d)}$$

*精确描述线路对地导纳，考虑分布参数的完整双曲函数关系*

### 矢量拟合有理函数

$$F(s) = \sum_{k=1}^{N_p} \frac{r_k}{s - p_k} + d + es$$

*将频域导纳转换为时域可实现的有理函数形式，是综合RLC等效电路的数学基础*



## 验证详情

- **验证方式**: 与基于数值拉普拉斯变换(NLT)的参考模型进行对比验证（论文提及第IV节将展示时域和频域结果）
- **测试系统**: 未在提供的文本片段中明确给出（如具体线路长度、电压等级、 IEEE标准测试系统等参数未披露）
- **仿真工具**: ATP、EMTP-RV、PSCAD等电磁暂态程序，以及通用电路仿真软件（如SPICE类）
- **验证结果**: 论文摘要指出模型在稳态和暂态过程中均保持高精度，可直接接入非线性元件，无需卷积或逆变换。具体数值验证结果（如波形对比、误差指标）未在提供的文本片段中给出。

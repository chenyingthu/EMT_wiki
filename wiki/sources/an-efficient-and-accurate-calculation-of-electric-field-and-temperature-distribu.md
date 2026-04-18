---
title: "An Efficient and Accurate Calculation of Electric Field and Temperature Distribution in HVDC Cables"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/tpwrd.2016.2545922.pdf.pdf"]
---

# An Efficient and Accurate Calculation of Electric Field and Temperature Distribution in HVDC Cables

**作者**: 
**年份**: 2016
**来源**: `06/tpwrd.2016.2545922.pdf.pdf`

## 摘要

— This paper presents novel approach to modeling of magnetic cores for high frequency transient analyses in power system applications. A method is presented of obtaining frequency dependent, nonlinear equivalent circuit model of magnetic cores, suitable for simulations of transients in high frequency and high current conditions. The model can be used in any EMTP-like simulation software for power system transient analyses and hardware design of transient mitigation solutions. The model has been developed based on the frequency characteristics of the complex impedance of a magnetic core, measured for different operating points on the magnetization curve. Based on the measured characteristics and on some basic material properties, a nonlinear equivalent model composed of a set of lumped elem

## 核心贡献


- 提出基于不同直流偏置电流下实测阻抗特性的磁芯频变非线性等效电路建模方法
- 通过组合多组线性RL集总元件电路，精确表征磁芯高频阻抗变化与磁饱和非线性特性
- 提供可直接嵌入EMTP类软件的通用建模流程，适用于高频暂态抑制装置的硬件设计


## 使用的方法


- [[集总参数等效电路法|集总参数等效电路法]]
- [[频变阻抗特性提取|频变阻抗特性提取]]
- [[非线性电路拟合|非线性电路拟合]]
- [[直流偏置扫描测量|直流偏置扫描测量]]


## 涉及的模型


- [[磁芯|磁芯]]
- [[纳米晶磁芯|纳米晶磁芯]]
- [[铁氧体磁芯|铁氧体磁芯]]
- [[非晶磁芯|非晶磁芯]]
- [[rl集总参数等效模型|RL集总参数等效模型]]


## 相关主题


- [[高频暂态分析|高频暂态分析]]
- [[频率相关建模|频率相关建模]]
- [[磁芯饱和效应|磁芯饱和效应]]
- [[暂态抑制|暂态抑制]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[快速暂态过电压|快速暂态过电压]]


## 主要发现


- 模型在宽频带与宽电流范围内，频域与时域仿真结果均与实测数据高度吻合
- 磁芯饱和效应会显著降低高频暂态抑制效果，所提非线性模型能准确捕捉该饱和特性
- 基于实测阻抗特性构建的集总参数电路可直接嵌入EMTP软件，有效支撑暂态抑制装置设计



## 方法细节

### 方法概述

本文提出一种基于实测频变阻抗特性的磁芯非线性等效电路建模方法。首先，在不同直流偏置电流下测量磁芯的复阻抗频率特性，覆盖从线性区到深度饱和区的工作点。随后，针对每个偏置电流点，利用有理函数拟合与部分分式展开技术，将频变阻抗综合为由多个RL并联支路构成的线性集总参数等效电路（Foster网络）。接着，对各支路电阻和电感值随电流的变化进行平滑插值，并通过积分运算推导出EMTP软件所需的电压-电流(V-I)和磁链-电流(Φ-I)非线性特性曲线。最后，采用指数离散化策略将特性曲线外推至10 kA高电流范围，确保模型在宽频带（kHz~MHz）与宽电流范围内均能精确表征磁芯的频变损耗与磁饱和非线性，可直接嵌入EMTP类暂态仿真软件。

### 数学公式


**公式1**: $$$Z(f, I) = R_S(f, I) + j\omega L_S(f, I)$$$

*磁芯串联等效阻抗模型，用于从复阻抗实部与虚部分离出频变电阻与电感*


**公式2**: $$$Z(s, I) = \sum_{k=1}^{N} \frac{r_k(I)}{s - p_k(I)}$$$

*基于部分分式展开的频域有理函数表达式，用于综合线性集总参数等效电路*


**公式3**: $$$V(I) = \int R(I) dI, \quad \Phi(I) = \int L(I) dI$$$

*通过对频变电阻和电感随电流的函数进行积分，获取EMTP非线性元件所需的V-I与Φ-I特性*


**公式4**: $$$I_j = \exp(j'/3)$$$

*指数离散化公式，用于在0~10 kA宽电流范围内合理分布采样点，兼顾饱和区快速变化与高电流区平缓变化*


### 算法步骤

1. 步骤1：搭建双磁芯测试回路，利用网络分析仪在14个直流偏置电流点（0, 1, 3, 5, 7, 11, 14, 17, 20, 25, 30, 40, 50 A）下测量磁芯复阻抗$Z(f, I_{dc})$，频率覆盖kHz至MHz范围，确保覆盖完整磁化曲线。

2. 步骤2：针对每个固定偏置电流$I_k$，将测得的$Z(f, I_k)$在s域拟合为实系数有理函数，并通过部分分式分解转化为Foster型集总参数等效电路，提取各并联支路的电阻$R_{k,m}$与电感$L_{k,m}$（$m=1\dots N$）。

3. 步骤3：在0~50 A测量范围内，对每个支路的$R_{k,m}(I)$和$L_{k,m}(I)$进行样条插值，获得连续光滑的电流依赖函数，消除离散测量噪声。

4. 步骤4：对插值后的$R(I)$和$L(I)$函数进行积分运算，分别得到电压特性$V(I)$和磁链特性$\Phi(I)$，作为EMTP非线性电感/电阻元件的输入数据。

5. 步骤5：采用指数步长$I_j = \exp(j'/3)$将$V(I)$和$\Phi(I)$外推离散至10 kA，生成约30个离散数据点，利用EMTP内置的线性插值功能完成模型部署，实现宽频宽流非线性仿真。


### 关键参数

- **磁芯材料**: 纳米晶（Nanocrystalline, Core 1, 初始相对磁导率$\mu_r=80,000$）

- **磁路长度$l_B$**: 0.588 m

- **有效截面积$A_e$**: 2.78 cm$^2$

- **测量偏置电流点数**: 14个（0~50 A）

- **等效电路支路数$N$**: 7（示例中采用5支路）

- **目标仿真频带**: kHz ~ MHz

- **目标仿真电流范围**: 0 ~ 10 kA

- **EMTP离散点数**: 约30点



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 频域阻抗特性验证（0 A, 11 A, 50 A偏置） | 在1 kHz~100 MHz范围内，模型计算的串联电感$L_S^{model}(f, I)$与实测值$L_S^{exp}(f, I)$高度吻合。在10 MHz高频点，模型准确复现了约0.3 μH的等效电感值，且阻抗幅值与相位误差在工程允许范围内。 | 相比传统固定RL并联模型，本模型在饱和区（50 A）的阻抗幅值预测误差降低至<5%，且完整保留了kHz~MHz的频变特性。 |

| 低频相位误差修正验证 | 在1~10 kHz低频段，由于引线电阻$R_c \approx 0.01 \Omega$的影响及相位测量灵敏度下降，实测相位角出现散射。模型通过阻抗外推处理使相位收敛至90°，有效消除了测量噪声对低频电感提取的干扰。 | 修正后低频电感提取稳定性显著提升，避免了传统方法中因相位跳变导致的负电阻或数值不稳定问题，确保50/60 Hz下阻抗趋近于0。 |



## 量化发现

- 模型适用频带覆盖kHz至MHz，电流范围扩展至0~10 kA，满足GIS快速暂态过电压(VFTO)抑制装置设计需求。
- 磁芯在$H_{dc}=85$ A/m（对应$I_{dc}=50$ A）时进入深度饱和，阻抗幅值与相位特性趋于平缓，模型通过指数离散化准确捕捉该非线性拐点。
- 低频段（1~10 kHz）引线电阻$R_c \approx 0.01 \Omega$对相位测量影响显著，模型通过阻抗外推使低频相位收敛至90°，确保纯电感特性。
- 10 MHz高频下磁芯等效电感降至约0.3 μH，此时阻抗呈强阻性，模型通过多支路RL网络精确拟合该频变损耗特性。
- EMTP实现仅需约30个离散点即可完整表征非线性特性，计算开销极低，可直接用于大规模电力系统暂态仿真。


## 关键公式

### 频变阻抗有理函数与部分分式展开式

$$$Z(s, I) = \frac{a_{n-1}s^{n-1} + \dots + a_0}{s^n + b_{n-1}s^{n-1} + \dots + b_0} = \sum_{k=1}^{N} \frac{r_k(I)}{s - p_k(I)}$$$

*用于将实测频域阻抗数据转化为s域解析表达式，进而综合为Foster型RL集总参数等效电路*

### EMTP非线性特性积分方程

$$$V(I) = \int R(I) dI, \quad \Phi(I) = \int L(I) dI$$$

*将频变电阻/电感随电流的函数转换为EMTP软件可直接调用的电压-电流与磁链-电流非线性查表曲线*

### 指数离散化外推公式

$$$I_j = \exp(j'/3)$$$

*在0~10 kA宽电流范围内生成非均匀采样点，确保饱和区（0~50 A）高分辨率与高电流区（>50 A）平滑过渡*



## 验证详情

- **验证方式**: 频域实测数据对比与EMTP时域仿真验证
- **测试系统**: 纳米晶磁芯（Core 1）双环测试回路，应用于GIS/VFTO暂态抑制场景
- **仿真工具**: Agilent 4294A阻抗分析仪（频域测量）、EMTP-ATP（时域仿真与模型部署）
- **验证结果**: 模型在kHz~MHz频带与0~10 kA电流范围内，频域阻抗幅值与相位与实测数据高度一致。低频段通过外推修正了测量相位散射问题，高频段准确复现了涡流与磁滞损耗导致的阻性主导特性。模型可直接嵌入EMTP，计算效率高，能精确捕捉磁饱和对高频暂态抑制效果的削弱作用，为暂态抑制装置硬件设计提供可靠仿真支撑。

---
title: "An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Open Journal of Power Electronics;2025;6; ;10.1109/OJPEL.2025.3560554"
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter.pdf"]
---

# An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter

**作者**: 
**年份**: 2025
**来源**: `07&08/An Equivalent Dynamic Phasor Model for a Single-Phase Boost Power-Factor-Correction Converter.pdf`

## 摘要

To mitigate harmonic current ﬂow in distribution systems, single-phase diode-bridge rectiﬁers (DBRs) are commonly equipped with active power factor correction (PFC) controllers. Achieving high power quality and dynamic performance in PFC controller design demands a precise understanding of PFC converter behavior. While detailed electromagnetic transient (EMT) simulations provide accurate insights, they are time-consuming. To address this, the dynamic phasor (DP) method offers a more efﬁcient modeling approach for power converters. This paper introduces and explores the DP model of a single-phase boost PFC converter, along with guidelines to integrate it with existing simulation platforms. To overcome challenges arising from differing driving frequencies (line frequency for the DBR and swit

## 核心贡献


- 提出基于符号函数变换的等效动态相量模型，解决多频激励下的PFC建模难题。
- 推导动态相量小信号模型，保留宽频谐波动态特性，适用于谐振补偿器设计。
- 建立系统化控制设计流程，利用DP模型精确整定开关模型与硬件原型控制参数。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[符号函数变换|符号函数变换]]
- [[小信号分析|小信号分析]]
- [[等效建模|等效建模]]
- [[线性化分析|线性化分析]]


## 涉及的模型


- [[单相boost-pfc变换器|单相Boost PFC变换器]]
- [[二极管整流桥|二极管整流桥]]
- [[等效有源整流器|等效有源整流器]]
- [[动态相量模型|动态相量模型]]
- [[小信号模型|小信号模型]]


## 相关主题


- [[动态相量建模|动态相量建模]]
- [[功率因数校正|功率因数校正]]
- [[控制器参数整定|控制器参数整定]]
- [[谐波分析|谐波分析]]
- [[仿真加速|仿真加速]]
- [[电力电子变换器|电力电子变换器]]


## 主要发现


- DP模型与详细EMT仿真结果高度吻合，且大幅缩短数值计算时间。
- DP小信号模型准确捕捉二次谐波与电感电流动态，验证了控制设计有效性。
- 硬件实验证实该模型可直接用于实际PFC变换器控制系统的参数整定与优化。



## 方法细节

### 方法概述

本文提出一种基于动态相量（DP）的单相Boost PFC变换器等效建模方法，旨在解决传统EMT仿真步长小、耗时久，以及常规平均值模型忽略二次谐波与电感动态的问题。核心思路是利用符号函数（sign function）将二极管整流桥（DBR）与Boost DC-DC变换器的动态方程从直流侧平移至交流侧，消除中间直流电平，将其转化为等效的单相有源整流器模型。随后，在DP域内对等效模型进行展开，保留交流侧基波与直流侧直流分量及二次谐波分量，构建包含8阶（含陷波器为10阶）的DP大信号模型。在此基础上，通过小信号线性化推导电流环与电压环的开闭环传递函数，揭示DP模型与传统状态空间平均模型在结构上的等效性及增益缩放关系。最终建立系统化的控制器参数整定流程，实现DP域设计参数向详细开关模型及硬件原型的精确映射。

### 数学公式


**公式1**: $$$\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jk\omega\tau} d\tau$$$

*动态相量定义式，通过滑动窗口$T$内的傅里叶平均将准周期信号分解为时变复系数，是DP建模的数学基础。*


**公式2**: $$$L_r \frac{di_s}{dt} = v_s - i_s R_r - m v_o, \quad C_o \frac{dv_o}{dt} = m i_s - v_o/R_o$$$

*符号函数等效变换方程，其中$m=\text{sgn}(v_s)d'$。将多频激励的PFC拓扑转化为单一基频激励的等效有源整流器，解决DP建模中的频率冲突。*


**公式3**: $$$G_{ov,dp}(s) = \frac{V_s/V_o}{sC_o + 1/R_o}$$$

*DP域电压环开环传递函数，用于分析直流母线电压对输入电流基波实部的响应特性，是电压环控制器设计的核心依据。*


**公式4**: $$$K_{pv} = \lambda_3 (2\varepsilon_v \omega_{bv} - \omega_{RC}), \quad K_{iv} = \omega_{bv}^2 / \lambda_3$$$

*DP模型电压环PI增益计算公式，其中$\lambda_3 = V_s/(V_o C_o)$。通过设定目标带宽$\omega_{bv}$直接计算控制器参数。*


### 算法步骤

1. 建立详细时域模型：构建包含DBR与Boost DC-DC的单相PFC电路，列写开关函数形式的状态方程，明确交流侧与直流侧的耦合关系。

2. 符号函数等效变换：利用$\text{sgn}(v_s)$将Boost电感动态方程从直流侧映射至交流侧，消去中间直流母线，得到等效有源整流器连续时间模型，统一激励频率基准。

3. DP域模型推导：设定滑动窗口长度$T$为电网周期，假设交流侧仅含基波、直流侧含直流与二次谐波，对等效模型进行动态相量展开，得到包含实部与虚部耦合项的微分方程组（式10a-10e）。

4. 控制策略DP域重构：将外环电压PI控制转化为对$\langle i_s \rangle_1^{R*}$的设定；内环电流控制采用前馈解耦消除交叉耦合项与电网电压扰动，构建双PI独立控制实/虚部电流的等效结构。

5. 小信号线性化与传递函数推导：在稳态工作点施加扰动，忽略高阶谐波与寄生电阻损耗，推导电流环与电压环的开环传递函数，对比传统平均模型确定增益缩放系数（电流环差$1/V_o$倍，电压环约差1/2倍）。

6. 控制器参数整定与映射：根据目标带宽（电压环设为$2\omega$的1/10~1/5）计算DP域PI参数，按推导的比例关系映射至详细开关模型或硬件控制器，完成闭环系统调参。


### 关键参数

- **EMT仿真步长**: 0.1 μs

- **DP仿真步长**: 0.5 ms

- **电压环设计带宽**: 5~15 Hz (约为$2\omega$的1/10~1/5)

- **初始直流母线电压**: 108 V

- **DP模型阶数**: 8阶（无陷波器）/ 10阶（含陷波器）

- **详细模型阶数**: 4阶（无陷波器）/ 6阶（含陷波器）

- **ODE求解器**: MATLAB ode15s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态与动态波形对比 | DP模型与详细EMT模型在输出电压、输入电流及二次谐波纹波上高度吻合，动态响应过程中电压超调量与恢复时间误差<1%，完整保留了100/120 Hz二次纹波特征。 | 相比传统平均值模型忽略二次谐波的问题，DP模型在保持波形精度的同时，数值积分步长从0.1 μs提升至0.5 ms，计算效率提升约5000倍。 |

| 控制器参数整定验证 | 基于DP小信号模型计算的PI参数（$K_{pv}, K_{iv}$）直接应用于详细开关模型，系统稳定运行，输入电流THD满足IEC61000-3-2标准，电压环带宽精确控制在5~15 Hz范围内。 | 传统方法需反复试凑或依赖复杂频域扫描，DP方法通过解析公式直接计算，参数映射误差<2%，大幅缩短控制设计周期。 |

| 整流电流谐波重构 | 利用DP域基波分量通过傅里叶级数重构整流电流$i_r$，直流分量$\langle i_{r0} \rangle_0 = \frac{2}{\pi}I_s$与偶次谐波幅值计算值与EMT仿真实测值偏差<0.5%。 | 克服了常规平均模型仅能获取直流分量的局限，实现了对偶次谐波动态的精确解析，无需额外高频仿真。 |



## 量化发现

- DP模型仿真步长可达0.5 ms，是传统EMT模型（0.1 μs）的5000倍，显著降低数值积分计算负担。
- DP小信号模型推导的电压环PI增益约为传统详细模型计算值的1/2，电流环增益相差$1/V_o$倍，揭示了DP域与开关域控制参数的精确映射关系。
- 电压环带宽设计为5~15 Hz（即$2\omega$的1/10~1/5），可有效抑制二次纹波，防止电感电流畸变，确保功率因数接近1。
- DP模型阶数为8阶（含陷波器为10阶），相比详细开关模型（4阶/6阶）保留了完整的二次谐波动态与电感暂态特性，且计算复杂度可控。
- 整流电流$i_r$的偶次谐波幅值按$\frac{4I_s}{\pi(k+1)(k-1)}$规律衰减，DP模型可精确捕捉至10次谐波，误差<0.5%。


## 关键公式

### 动态相量定义式

$$$\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jk\omega\tau} d\tau$$$

*用于将准周期时域信号分解为时变复系数，是构建DP模型的基础数学工具。*

### 符号函数等效变换方程

$$$L_r \frac{di_s}{dt} = v_s - i_s R_r - m v_o, \quad C_o \frac{dv_o}{dt} = m i_s - v_o/R_o$$$

*在DP建模前使用，通过$\text{sgn}(v_s)$消除多频激励冲突，将PFC拓扑转化为等效有源整流器。*

### DP域电压环开环传递函数

$$$G_{ov,dp}(s) = \frac{V_s/V_o}{sC_o + 1/R_o}$$$

*用于小信号分析与控制器带宽设计，建立直流母线电压与输入电流基波实部的频域关系。*

### DP模型电压环PI增益公式

$$$K_{pv} = \lambda_3 (2\varepsilon_v \omega_{bv} - \omega_{RC}), \quad K_{iv} = \omega_{bv}^2 / \lambda_3$$$

*在控制设计阶段使用，根据目标阻尼比$\varepsilon_v$和带宽$\omega_{bv}$直接计算外环控制器参数。*



## 验证详情

- **验证方式**: 仿真对比与实验验证
- **测试系统**: 单相Boost PFC变换器（含DBR与Boost DC-DC级联结构，额定功率与参数见表1）
- **仿真工具**: MATLAB/Simulink (详细开关模型), MATLAB ODE求解器(ode15s, DP模型), 硬件实验平台
- **验证结果**: DP模型在时域波形、二次谐波幅值及动态响应上与详细EMT模型高度一致，误差极小；基于DP小信号模型整定的控制器参数可直接用于开关模型与硬件原型，实现高精度、低计算成本的PFC系统设计与分析，验证了等效变换与小信号映射方法的工程实用性。

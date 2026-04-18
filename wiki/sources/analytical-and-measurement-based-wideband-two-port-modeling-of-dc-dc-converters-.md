---
title: "Analytical and measurement-based wideband two-port modeling of DC-DC converters for electromagnetic transient studies"
type: source
authors: ['H. Alameri']
year: 2023
journal: "Electric Power Systems Research, 220 (2023) 109305. doi:10.1016/j.epsr.2023.109305"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Alameri和Gomez - 2023 - Analytical and measurement-based wideband two-port modeling of DC-DC converters for electromagnetic.pdf"]
---

# Analytical and measurement-based wideband two-port modeling of DC-DC converters for electromagnetic transient studies

**作者**: H. Alameri
**年份**: 2023
**来源**: `09/Alameri和Gomez - 2023 - Analytical and measurement-based wideband two-port modeling of DC-DC converters for electromagnetic.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Analytical and measurement-based wideband two-port modeling of DC-DC a Computer Engineering Department, University of Baghdad, Baghdad, Iraq b Department of Electrical and Computer Engineering, Western Michigan University, Kalamazoo, MI 49008 United States of America Power-electronic converters are essential elements for the effective interconnection of renewable energy sources

## 核心贡献


- 提出基于拉普拉斯域模式平均与开关函数结合的变换器双端口导纳解析模型
- 建立基于端口电压电流测量的宽频双端口导纳模型重构方法适用于黑盒设备
- 实现变换器导纳模型与其他电网元件直接互联支持全频域暂态与稳定性分析


## 使用的方法


- [[拉普拉斯域分析|拉普拉斯域分析]]
- [[模式平均法|模式平均法]]
- [[双端口导纳建模|双端口导纳建模]]
- [[数值拉普拉斯逆变换|数值拉普拉斯逆变换]]
- [[基于测量的模型重构|基于测量的模型重构]]


## 涉及的模型


- [[buck变换器|Buck变换器]]
- [[boost变换器|Boost变换器]]
- [[双端口导纳模型|双端口导纳模型]]
- [[黑盒模型|黑盒模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[宽频建模|宽频建模]]
- [[频域分析|频域分析]]
- [[电力电子变换器建模|电力电子变换器建模]]
- [[导纳建模|导纳建模]]
- [[分布式能源并网|分布式能源并网]]


## 主要发现


- 解析模型与测量重构模型的仿真结果与EMTP基准高度吻合验证了宽频建模精度
- 引入开关函数后模型能准确捕捉高频开关动态显著提升暂态响应预测能力
- 仅凭端口测量数据即可有效重构黑盒变换器宽频特性无需依赖内部电路参数



## 方法细节

### 方法概述

本文提出两种基于拉普拉斯域的宽频双端口导纳建模方法。解析法首先对Buck/Boost变换器的两种开关模式进行频域导纳表示，通过模式平均法获得低频等效模型；随后引入开关函数（Buck）或纹波函数（Boost）以显式包含高频开关动态，形成非对称双端口导纳矩阵。测量法面向黑盒设备，通过施加多组不同源-负载组合获取端口电压电流时域波形，利用数值拉普拉斯变换（NLT）转换至频域，构建包含4个未知导纳元素的超定线性方程组，采用最小范数最小二乘法（MNLS）唯一求解导纳矩阵。最终，两种模型均通过数值拉普拉斯逆变换（INLT）计算任意外部激励下的时域暂态响应，并支持与其他导纳型电网元件直接矩阵互联。

### 数学公式


**公式1**: $$$$\begin{bmatrix} I_i \\ I_o \end{bmatrix} = \begin{bmatrix} d F_s(s) Y_L & -d Y_L \\ -d F_s(s) Y_L & Y_L + Y_C \end{bmatrix} \begin{bmatrix} V_i \\ V_o \end{bmatrix}$$$$

*Buck变换器含开关函数的双端口导纳模型，$F_s(s)$为开关函数，$Y_L=1/(sL)$，$Y_C=sC$，用于解析建模。*


**公式2**: $$$$F_s(s) = \frac{1 - e^{-s d T}}{d(1 - e^{-s T})}$$$$

*Buck变换器开关函数，占空比为$d$，开关周期为$T$，用于在频域中引入开关频率动态。*


**公式3**: $$$$\begin{bmatrix} I_{\text{test } 1} \\ I_{\text{test } 2} \\ \vdots \\ I_{\text{test } N} \end{bmatrix}_{2N \times 1} = \begin{bmatrix} V_{\text{test } 1} \\ V_{\text{test } 2} \\ \vdots \\ V_{\text{test } N} \end{bmatrix}_{2N \times 4} \begin{bmatrix} y_{11}(s) \\ y_{12}(s) \\ y_{21}(s) \\ y_{22}(s) \end{bmatrix}_{4 \times 1}$$$$

*基于测量的超定线性方程组，通过$N$次独立测试的端口电压电流数据重构4个导纳元素。*


**公式4**: $$$$\begin{bmatrix} V_i^R \\ V_o^R \end{bmatrix} = \begin{bmatrix} y_{11}(s) + y_i & y_{12}(s) \\ y_{21}(s) & y_{22}(s) + y_o \end{bmatrix}^{-1} \begin{bmatrix} I_{\text{inj},i} \\ I_{\text{inj},o} \end{bmatrix}$$$$

*重构导纳模型在外部网络（输入导纳$y_i$、输出导纳$y_o$及注入电流$I_{\text{inj}}$）下的节点电压求解公式。*


### 算法步骤

1. 步骤1（数据获取/解析推导）：对于解析法，根据电路拓扑推导开关模式1和模式2的频域导纳方程并进行占空比加权平均；对于测量法，在变换器端口施加$N$组（本文取$N=4$）不同的直流源电压与负载电阻组合，记录稳态及暂态过程中的输入/输出电压$v_i(t), v_o(t)$和电流$i_i(t), i_o(t)$。

2. 步骤2（频域转换）：利用数值拉普拉斯变换（NLT）算法将步骤1获取的时域电压电流波形转换为拉普拉斯域复频域数据$V(s)$和$I(s)$，覆盖目标宽频范围（如100 Hz至200 kHz）。

3. 步骤3（矩阵构建与求解）：将频域数据代入双端口导纳关系式$I(s)=Y(s)V(s)$。由于单次测试仅得2个方程但含4个未知导纳元素，需组合$N$次测试数据构建$2N \times 4$的超定电压矩阵。调用MATLAB的`lsqminnorm`函数执行最小范数最小二乘法（MNLS），唯一求解出$y_{11}(s), y_{12}(s), y_{21}(s), y_{22}(s)$。

4. 步骤4（时域响应计算）：将重构或解析得到的导纳矩阵与外部电网元件导纳矩阵直接相加求逆，结合注入电流向量计算节点电压频域解。最后应用数值拉普拉斯逆变换（INLT）算法将频域结果转换回时域，获得完整的电磁暂态波形。


### 关键参数

- **Buck变换器参数**: L=10 µH, C=40 µF, RL=8.5 Ω, 开关频率=100 kHz, 占空比d=0.25

- **Boost变换器参数**: L=70 µH, C=40 µF, RL=12.5 Ω, 开关频率=100 kHz, 占空比d=0.4

- **测试激励范围**: Buck: 输入80-220 V, 负载1-20 Ω; Boost: 输入12-200 V, 负载1-20 Ω

- **重构所需测试次数**: 4次独立源-负载组合测试



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 测试案例A（Buck变换器） | 输入电压在1.25 ms时由110 V阶跃降至70 V，负载固定为8.5 Ω。解析模型与测量重构模型均准确捕捉了电容电压与电感电流的暂态过渡过程及高频纹波。 | 与EMTP开关模型基准相比，解析法最大相对误差：电容电压1.1315%，电感电流3.0012%；测量法最大相对误差：电容电压0.3750%，电感电流1.3362%。测量法精度更高。 |

| 测试案例B（Boost变换器） | 输入电压在2.5 ms时由120 V阶跃升至170 V，负载固定为12.5 Ω。两种模型均能复现宽频暂态响应，频谱分析显示主谐振频率与开关频率成分均被准确保留。 | 与EMTP基准相比，解析法最大相对误差：电容电压1.3185%，电感电流2.5132%；测量法最大相对误差：电容电压0.1927%，电感电流0.2847%。解析法在Boost高频段因纹波函数近似存在轻微频谱偏差，而测量法全频段吻合度极佳。 |



## 量化发现

- 测量重构模型在Buck和Boost测试中的最大相对误差均低于1.4%（电压<0.38%，电流<1.34%），显著优于传统解析平均模型。
- 仅需4组不同工况的端口测量数据即可唯一且高精度地重构四元素宽频导纳矩阵，无需内部拓扑与参数先验知识。
- 模型有效频带覆盖100 Hz至200 kHz，能够同时准确表征低频暂态过渡与高频开关谐波动态。
- 解析法在Boost变换器高频段（>10 kHz）的频谱匹配度略低于测量法，最大电流误差达2.51%，主要受限于人工引入的纹波函数近似。
- 双端口导纳矩阵形式支持直接矩阵相加互联，避免了传统EMTP中因极小时间步长导致的计算成本指数级增长问题。


## 关键公式

### Buck变换器宽频双端口导纳矩阵

$$$$\begin{bmatrix} I_i \\ I_o \end{bmatrix} = \begin{bmatrix} d F_s(s) Y_L & -d Y_L \\ -d F_s(s) Y_L & Y_L + Y_C \end{bmatrix} \begin{bmatrix} V_i \\ V_o \end{bmatrix}$$$$

*用于解析建模，结合开关函数$F_s(s)$在拉普拉斯域直接表征Buck变换器的输入输出导纳特性及开关频率动态。*

### 测量数据超定线性方程组

$$$$[I]_{2N \times 1} = [V]_{2N \times 4} [Y]_{4 \times 1}$$$$

*用于黑盒模型重构，将多次测试的频域端口数据组合，通过最小二乘法唯一求解未知的四个导纳元素。*

### Boost变换器开关纹波函数

$$$$F_r(s) = \frac{4}{T_s^2} \left( \frac{1 - e^{-T_s s/2}}{1 - e^{-T_s s}} \right)^2 \frac{1}{s} - \frac{1}{s}$$$$

*用于解析法中Boost变换器的高频修正，通过叠加纹波分量近似模拟开关动作引起的电感电流与电容电压高频振荡。*



## 验证详情

- **验证方式**: 对比仿真验证（以EMTP详细开关模型为基准）
- **测试系统**: 独立DC-DC Buck变换器（测试A）与DC-DC Boost变换器（测试B），包含具体L、C、RL参数及宽范围输入电压/负载工况
- **仿真工具**: EMTP（生成基准开关模型波形及模拟测量数据）、MATLAB（执行NLT/INLT变换、`lsqminnorm`最小二乘求解、频谱分析与误差计算）
- **验证结果**: 两种建模方法在时域波形与频域频谱上均与EMTP基准高度一致。测量法最大误差<1.34%，解析法最大误差<3.01%。验证了拉普拉斯域双端口导纳模型在宽频电磁暂态分析中的高精度、黑盒适用性及直接互联能力，为大规模电力电子并网系统的稳定性与暂态仿真提供了高效替代方案。

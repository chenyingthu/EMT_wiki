---
title: "Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;3;10.1109/TPWRD.2021.3099008"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Zhao 等 - 2022 - Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms.pdf"]
---

# Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms

**作者**: 
**年份**: 2022
**来源**: `05/Zhao 等 - 2022 - Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms.pdf`

## 摘要

—This paper introduces a novel frequency domain tech- nique to globally evaluate the accuracy of electro-magnetic tran- sient simulations. It is shown that simulation accuracy at low frequencies can sometimes be poorer than at high frequency. A modiﬁed approach which quantiﬁes accuracy from a driving point as a function of frequency is also introduced that uses the Bilinear Transformation and Norton equivalents, to produce a “simulation accuracy spectrum”. This approach can be applied to large systems without explicitly forming state space equations. It also permits the accuracy analysis of networks with distributed components such as frequency dependent transmission lines. Two examples are used to verify the proposed technique, a small network with a frequency dependent transmission line 

## 核心贡献


- 提出频域全局评估方法，突破传统单一元件精度分析的局限性
- 结合双线性变换与诺顿等效，构建无需状态方程的仿真精度频谱
- 首次实现含频率相关线路等分布参数网络的系统级数值精度量化


## 使用的方法


- [[频域映射分析|频域映射分析]]
- [[双线性变换|双线性变换]]
- [[诺顿等效|诺顿等效]]
- [[状态空间法|状态空间法]]
- [[梯形积分|梯形积分]]
- [[驱动点导纳法|驱动点导纳法]]


## 涉及的模型


- [[频率相关输电线路|频率相关输电线路]]
- [[通用线路模型|通用线路模型]]
- [[lcc-model|LCC]]
- [[ieee-39节点系统|IEEE 39节点系统]]
- [[rlc集总网络|RLC集总网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真精度评估|仿真精度评估]]
- [[数值积分误差|数值积分误差]]
- [[分布参数网络|分布参数网络]]
- [[频域建模|频域建模]]


## 主要发现


- 系统级评估表明低频段仿真误差可能大于高频段，颠覆传统认知
- 驱动点精度频谱可准确量化大电网在不同频段的数值积分仿真误差
- 所提方法在含通用线路模型的IEEE 39节点LCC-HVDC系统中验证有效



## 方法细节

### 方法概述

提出一种基于频域的全局仿真精度评估方法，突破传统仅针对单一动态元件（如电感、电容）的局部误差分析局限。核心思想是将网络划分为边界节点与内部节点，利用节点导纳矩阵的高斯消元法推导边界端口的诺顿等效导纳。通过双线性变换将连续频域微分算子映射为离散频域算子，直接计算数值积分算法（如梯形积分）下的离散导纳矩阵。定义“仿真精度频谱”指标，量化不同频率下驱动点导纳的相对误差。该方法无需显式构建状态空间方程，可直接基于网络清单数据计算，并首次扩展至含通用线路模型（ULM）的频率相关分布参数网络，实现大电网系统级数值精度的全局量化。

### 数学公式


**公式1**: $$$z^{-1} = e^{-j\omega\Delta t}$$$

*离散时间域到连续频域的映射关系，用于将差分方程转换至频域进行对比分析。*


**公式2**: $$$s_{TR}(j\omega, \Delta t) = \frac{2(e^{j\omega\Delta t} - 1)}{\Delta t(e^{j\omega\Delta t} + 1)}$$$

*双线性变换公式，将连续频域变量$s$映射为梯形积分对应的离散频域变量，用于计算数值仿真下的等效导纳。*


**公式3**: $$$Y_b(s) = Y_{bb}(s) - Y_{bi}(s)Y_{ii}(s)^{-1}Y_{bi}^T(s)$$$

*边界端口诺顿等效导纳计算公式，通过高斯消元法消去内部节点得到。*


**公式4**: $$$\Delta Y_{bm}(j\omega, \Delta t)_{ij} = \frac{|Y_b(j\omega)_{ij} - Y_b^{TR}(j\omega, \Delta t)_{ij}|}{\max_k(|Y_b(j\omega)_{ik}|)}$$$

*改进的相对误差矩阵元素计算公式，分母采用端口最大导纳幅值以避免数值病态问题。*


**公式5**: $$$A(j\omega, \Delta t) = \max_{i,j} \Delta Y_{bm}(j\omega, \Delta t)_{ij}$$$

*仿真精度频谱指标，取相对误差矩阵中的最大值作为该频率下的全局精度量化值。*


### 算法步骤

1. 构建网络频域导纳矩阵：根据网络拓扑和元件参数，按边界节点($b$)和内部节点($i$)划分，形成连续频域导纳矩阵$Y_{Ni}(j\omega)$。

2. 计算理论诺顿等效导纳：利用高斯消元法对内部节点进行消去，得到边界端口的理论等效导纳$Y_b(j\omega) = Y_{bb} - Y_{bi}Y_{ii}^{-1}Y_{bi}^T$。

3. 应用双线性变换：将连续频域变量$s=j\omega$替换为梯形积分对应的离散映射$s_{TR}(j\omega, \Delta t) = \frac{2(e^{j\omega\Delta t}-1)}{\Delta t(e^{j\omega\Delta t}+1)}$。

4. 计算离散仿真导纳：将$s_{TR}$代入各元件导纳表达式，重新组网并执行相同的节点消元，得到数值积分下的仿真等效导纳$Y_b^{TR}(j\omega, \Delta t)$。

5. 构建精度频谱：计算相对误差矩阵$\Delta Y_{bm}$，取矩阵元素最大值作为该频率下的全局精度指标$A(j\omega, \Delta t)$，遍历目标频段绘制频谱。

6. 分布参数扩展（针对ULM）：对频率相关线路，采用通用线路模型的有理函数拟合$Y_C(s)$和$H(s)$，仅对有理部分应用双线性变换，延迟项$e^{-s\tau_k}$保留为物理延迟，再并入导纳矩阵计算。


### 关键参数

- **仿真步长_Δt**: 关键评估参数，文中测试了10μs、50μs、60μs、90μs

- **向量拟合误差阈值**: ULM模型参数拟合精度，测试了5%、2%、0.05%

- **目标评估频段**: 0~1557 Hz（覆盖开关暂态99.35%的能量）

- **精度容忍带**: ±10%（用于判定步长是否满足精度要求）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 简单RLC集总网络 | 在Δt=90μs时，550 Hz激励下仿真电流幅值为理论值的1.33倍（误差33%），相位偏移15.84°；理论预测Δt>50μs时550 Hz附近误差突破10%阈值。 | 颠覆传统‘频率越高误差越大’的认知，证明低频段系统级误差可能显著高于高频段，理论频谱预测与时域仿真结果完全吻合。 |

| 含频率相关线路的ULM网络 | 300km线路+RLC终端，Δt=10μs。向量拟合误差5%时，230 Hz处仿真不精确度达3.1%；拟合误差降至2%时，不精确度降至0.8%。 | 首次实现分布参数网络的精度量化，理论计算的精度频谱与EMT仿真电流差值峰值完全一致，验证了有理拟合误差对系统级精度的直接影响。 |

| IEEE 39节点系统+LCC-HVDC | 采用三相耦合π型线路模型以支持特征值对比，评估HVDC换流器产生的宽频谐波下的系统精度。 | 证明所提方法无需构建状态空间方程即可直接应用于大电网，克服了传统特征值法无法处理分布参数和大规模网络的局限。 |



## 量化发现

- 低频段误差可能大于高频段：550 Hz处误差达33%，颠覆传统认知。
- 步长阈值效应：当Δt > 50μs时，550 Hz附近仿真误差超过10%；Δt ≤ 50μs时误差控制在10%以内。
- 拟合精度与仿真误差强相关：向量拟合误差从5%降至2%，230 Hz处系统级仿真误差从3.1%降至0.8%。
- 能量覆盖频段：开关暂态99.35%的能量集中在0~1557 Hz，该频段可作为精度评估的核心目标区间。


## 关键公式

### 双线性变换映射公式

$$$s_{TR}(j\omega, \Delta t) = \frac{2(e^{j\omega\Delta t} - 1)}{\Delta t(e^{j\omega\Delta t} + 1)}$$$

*用于将连续频域导纳转换为梯形积分算法下的离散频域导纳，是构建仿真精度频谱的核心算子。*

### 仿真精度频谱指标

$$$A(j\omega, \Delta t) = \max_{i,j} \frac{|Y_b(j\omega)_{ij} - Y_b^{TR}(j\omega, \Delta t)_{ij}|}{\max_k(|Y_b(j\omega)_{ik}|)}$$$

*用于量化大电网在任意驱动端口、任意频率下的全局数值积分误差，无需状态空间方程。*

### 边界诺顿等效导纳

$$$Y_b(s) = Y_{bb}(s) - Y_{bi}(s)Y_{ii}(s)^{-1}Y_{bi}^T(s)$$$

*通过高斯消元法消去内部节点，将复杂网络简化为端口等效模型，支撑系统级精度分析。*



## 验证详情

- **验证方式**: 频域理论计算与EMT时域仿真对比验证
- **测试系统**: 简单RLC网络、300km频率相关输电线路(ULM)+RLC终端、IEEE 39节点系统接入12脉波LCC-HVDC
- **仿真工具**: 电磁暂态仿真器(EMT Simulator，基于Dommel算法)、MATLAB(向量拟合/频域矩阵计算)
- **验证结果**: 理论推导的“仿真精度频谱”与EMT时域仿真结果在幅值误差和相位偏差上高度吻合，验证了方法在集总参数和分布参数网络中的有效性。该方法成功量化了向量拟合误差对系统精度的影响，并证明无需构建状态空间方程即可直接应用于大电网，为EMT仿真步长选择和模型精度评估提供了全局频域依据。

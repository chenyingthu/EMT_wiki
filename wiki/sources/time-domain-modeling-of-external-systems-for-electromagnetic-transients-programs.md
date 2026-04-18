---
title: "Time domain modeling of external systems for electromagnetic transients programs - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/59.260813.pdf.pdf"]
---

# Time domain modeling of external systems for electromagnetic transients programs - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `37/59.260813.pdf.pdf`

## 摘要

An external network model to be used in Electromagnetic Tran- sients Programs (EMTPs) is developed based on techniques directly applicable in the time domain. This is in contrast to the currently available models which are derived based on the frequency domain methods. The model is in form of a discrete-time filter which is built from the EMTP simulation of the external system’s response to a multisine excitation sig- nal. The developed filter is converted into a Norton equivalent source and integrated into the EMTP model of the study (in- ternal) system. The proposed model is verified by simulating the energization transients on an open-ended transmission line connected to the (external) network in a three phase test sys- tem. Keywords: Network Equivalents, Electromagnetic Tran- sients, S

## 核心贡献



- 提出了一种直接在时域构建外部系统等效模型的方法，避免了传统频域拟合的复杂性
- 基于多正弦激励响应构建离散时间滤波器，并将其转换为诺顿等效源直接集成到EMTP中
- 提供了一种易于实现且可直接应用于现有电磁暂态仿真程序的外部网络等效技术

## 使用的方法


- [[network-equivalent]]

## 涉及的模型


- [[transmission-line]]
- [[network-equivalent]]

## 相关主题


- [[network-equivalent]]

## 主要发现



- 时域离散滤波器能够准确复现外部系统在宽频暂态过程中的动态响应
- 无需显式综合RLC元件网络，直接生成的诺顿等效源可无缝集成至现有EMTP程序
- 在空载输电线路合闸暂态测试中，该等效模型与完整系统仿真结果高度一致，验证了其有效性与计算效率

## 方法细节

### 方法概述

本文提出了一种直接在时域构建外部系统等效模型的方法，完全避免了传统频域拟合的复杂性。该方法基于系统辨识理论，通过向外部系统注入多正弦(multisine)激励信号获取宽频带响应数据，利用最小二乘法估计离散时间滤波器参数，构建外部系统的离散时间诺顿等效电路。关键创新在于无需合成显式的RLC集总参数网络，而是直接获得差分方程形式的时域等效模型，可无缝集成到现有EMTP程序中。模型阶数p通过迭代方式确定，以RMS拟合误差小于阈值(1.0%)为收敛准则。

### 数学公式


**公式1**: $$$H(s) = \frac{N(s)}{D(s)} = k\frac{n_0 + n_1s + \cdots + n_ps^p}{d_0 + d_1s + \cdots + d_ps^p}$$$

*外部系统驱动点导纳函数的传递函数表示，分子分母多项式阶数均为p，用于描述边界母线电压与注入电流的关系*


**公式2**: $$$i(t) + a_1i(t-\Delta t) + \cdots + a_pi(t-p\Delta t) = g_0v(t) + g_1v(t-\Delta t) + \cdots + g_pv(t-p\Delta t)$$$

*使用Backward Euler数值积分方法将连续域微分方程转换为p阶线性差分方程，其中Δt为积分时间步长*


**公式3**: $$$i(t) = -\sum_{k=1}^p a_k i(t-k\Delta t) + \sum_{k=0}^p g_k v(t-k\Delta t)$$$

*差分方程的紧凑形式，表示当前时刻电流由历史电流和电压的线性组合决定*


**公式4**: $$$i(t) = g_0 v(t) + h$，其中$h = \sum_{k=1}^p g_k v(t-k\Delta t) - \sum_{k=1}^p a_k i(t-k\Delta t)$$$

*诺顿等效电路形式，g0为等效电导，h为历史项(history term)，代表过去p个时间步的电压电流影响*


**公式5**: $$$e_{rms} = \sqrt{\frac{1}{N-p}\sum_{k=p+1}^N (i(k\Delta t) - \hat{i}(k\Delta t))^2}$$$

*模型拟合的均方根误差计算公式，用于评估估计参数与EMTP仿真响应的偏差，N为总采样点数*


**公式6**: $$$I(t) = G_0 V(t) + \sum_{k=1}^p [G_k V(t-k\Delta t) - A_k I(t-k\Delta t)]$$$

*多相系统的矩阵形式差分方程，Gk和Ak为M×M维系数矩阵，M为相数，适用于三相或多相外部系统*


### 算法步骤

1. 断开研究子系统与外部系统的连接，隔离外部系统

2. 关闭外部系统内部所有独立电源（电压源置零，电流源开路）

3. 在外部系统边界母线处连接周期性多正弦电压源作为宽频带激励信号，该信号具有平坦幅值谱、低波峰因数（crest factor）和高信噪比特性

4. 运行EMTP仿真，在持续时间T_obs（等于多正弦信号周期）内采集N个样本的边界母线电压v(t)和注入电流i(t)，获得外部系统时域稳态响应

5. 设定初始模型阶数p，使用最小二乘法基于N个样本数据估计差分方程参数a_k（k=1,...,p）和g_k（k=0,...,p）

6. 根据公式计算RMS拟合误差e_rms，若e_rms > ε（阈值设为1.0%），则增加模型阶数p=p+1并返回步骤5重新估计参数

7. 当首次满足e_rms ≤ 1.0%时停止迭代，此时的p为最佳最小阶数，对应的参数即为最终模型参数

8. 将估计的g0作为诺顿等效电导，构建包含历史项h的离散时间诺顿等效电路并接入EMTP仿真


### 关键参数

- **model_order_p**: 差分方程阶数，与所需模拟的频率带宽相关，通过迭代确定直至满足误差准则

- **time_step_Delta_t**: EMTP仿真积分时间步长，决定离散化精度

- **number_of_samples_N**: 总采样点数，覆盖多正弦信号完整周期T_obs

- **RMS_error_threshold_epsilon**: 1.0%（或写作0.01），模型收敛判据，确保等效模型与原始系统响应偏差小于1%

- **coefficients_a_k**: 自回归系数（k=1,...,p），描述历史电流对当前电流的影响

- **coefficients_g_k**: 滑动平均系数（k=0,...,p），描述当前及历史电压对当前电流的贡献

- **Norton_conductance_g0**: 等效电导，构成诺顿等效电路的瞬时项

- **history_term_h**: 由过去p个时间步的电压和电流计算的等效历史电流源



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相测试系统空载输电线路合闸暂态 | 在包含外部网络的三相测试系统中，对开断的输电线路进行合闸操作，比较完整系统仿真与使用时域等效模型的仿真结果。模型准确复现了边界母线处的电压和电流暂态波形，包括高频振荡和衰减特性 | 与完整系统详细EMTP仿真相比，等效模型在保持精度误差小于1%的同时，显著降低了计算复杂度，特别适用于需要进行大量统计过电压研究的场景 |



## 量化发现

- 模型参数估计的RMS误差收敛阈值设定为1.0%（ε=1.0%），可获得满足工程精度要求的最低阶等效模型
- 模型阶数p与所需有效频率范围（带宽）直接相关，频率范围越宽所需的滞后项数p越大
- 多正弦激励信号的观测周期T_obs选择需覆盖外部系统所有相关模态的响应时间，确保在宽频带内（通常覆盖工频到数千赫兹）充分激励系统
- 差分方程系数a_k和g_k通过最小二乘法从N个采样点中估计，N通常远大于2p+1以保证参数估计的数值稳定性
- 诺顿等效电导g0代表外部系统的瞬时导纳，其值由g_0系数直接给出，与频率无关的静态部分
- 对于平衡三相系统，通过Clarke变换可将3×3维系数矩阵Gk和Ak对角化，将三相耦合问题解耦为三个独立的模态（0, α, β）等效电路


## 关键公式

### 离散时间诺顿等效方程

$$$i(t) = g_0 v(t) + \sum_{k=1}^p g_k v(t-k\Delta t) - \sum_{k=1}^p a_k i(t-k\Delta t)$$$

*用于在EMTP中实现外部系统的时域等效，将外部网络替换为等效电导g0与历史电流源h的并联组合，在每个时间步更新历史项并求解网络方程*

### 模型验证误差准则

$$$e_{rms} = \sqrt{\frac{1}{N-p}\sum_{k=p+1}^N (i(k\Delta t) - \hat{i}(k\Delta t))^2} \leq 1.0\%$$$

*在模型阶数选择迭代过程中使用，当计算得到的均方根误差首次小于等于1.0%时确定最终模型阶数p，确保等效模型在宽频带内与原始外部系统响应的偏差控制在工程允许范围内*



## 验证详情

- **验证方式**: 仿真对比验证，将提出的时域等效模型与完整系统的详细EMTP仿真结果进行时域波形对比
- **测试系统**: 三相测试系统，包含外部网络和开断的输电线路，用于模拟线路合闸（energization）产生的电磁暂态过程
- **仿真工具**: EMTP（Electromagnetic Transients Program），使用Backward Euler数值积分方法进行离散化
- **验证结果**: 在空载输电线路合闸暂态测试中，基于多正弦激励辨识得到的离散时间滤波器等效模型与完整系统仿真结果高度一致，验证了该时域建模方法在宽频暂态模拟中的准确性和计算效率。等效模型无需显式构建RLC网络，可直接以诺顿等效源形式集成到现有EMTP程序中

---
title: "An ultra-fast MMC-HVDC fault location algorithm based on transient voltage features and regression neural network"
type: source
authors: ['Yunqi Zhang']
year: 2024
journal: "International Journal of Electrical Power and Energy Systems, 162 (2024) 110249. doi:10.1016/j.ijepes.2024.110249"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Zhang et al. - 2024 - An ultra-fast MMC-HVDC fault location algorithm based on transient voltage features and regression n.pdf"]
---

# An ultra-fast MMC-HVDC fault location algorithm based on transient voltage features and regression neural network

**作者**: Yunqi Zhang
**年份**: 2024
**来源**: `07&08/Zhang et al. - 2024 - An ultra-fast MMC-HVDC fault location algorithm based on transient voltage features and regression n.pdf`

## 摘要

An ultra-fast MMC-HVDC fault location algorithm based on transient State Key Laboratory for Security and Energy Saving, China Electric Power Research Institute, Beijing, China An ultra-fast fault location algorithm based on the single-ended transient voltage features and regression neural network (RNN) is proposed, which utilizes 2.5 ms postfualt data window and is suitable for modular multilevel converter-based high-voltage DC (MMC-HVDC) grids equipped with quick-action protections and hybrid D

## 核心贡献


- 提出基于单端暂态电压特征与RNN的超快定位算法，仅需2.5ms数据窗
- 揭示集中参数RLC电路下延迟时间与首负峰值同故障距离的精确映射
- 利用RNN补偿实际拓扑特征提取误差，实现复杂工况下的高精度定位


## 使用的方法


- [[集中参数rlc建模|集中参数RLC建模]]
- [[回归神经网络-rnn|回归神经网络(RNN)]]
- [[暂态特征提取|暂态特征提取]]
- [[传递函数分析|传递函数分析]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mmc-model|MMC]]
- [[直流输电线路|直流输电线路]]
- [[混合直流断路器-hdccb|混合直流断路器(HDCCB)]]


## 相关主题


- [[故障定位|故障定位]]
- [[mmc-model|MMC]]
- [[暂态电压分析|暂态电压分析]]
- [[数据驱动保护|数据驱动保护]]
- [[高阻故障定位|高阻故障定位]]


## 主要发现


- 算法在2.5ms数据窗内完成定位，对1005Ω高阻故障保持高精度
- 方法可容忍线路参数与限流电抗偏差，在40dB白噪声下仍稳定运行
- 经两万组独立案例验证，算法具备强泛化能力与跨系统良好适应性



## 方法细节

### 方法概述

提出一种基于单端暂态电压特征与回归神经网络（RNN）的超快故障定位算法。该方法针对配备快速保护与混合直流断路器（HDCCB）的MMC-HVDC系统，仅利用故障后2.5ms的极短数据窗。首先基于集中参数RLC等效电路推导，证明电压暂态响应的延迟时间、首个负峰值时刻及其幅值与故障距离存在精确映射关系。然而，实际MMC拓扑与线路分布参数会导致特征提取存在近似误差，因此引入训练好的RNN对这三个特征进行非线性映射补偿，实现复杂工况下的高精度、超快速故障距离估计。

### 数学公式


**公式1**: $$$Z_{eq} = \frac{sL_m}{3} + \frac{R_m}{3} + \frac{N}{6sC_m}$$$

*HB-MMC在故障暂态期间（闭锁前）的等效阻抗表达式，用于构建集中参数RLC故障回路模型。*


**公式2**: $$$k_3 = \frac{xNC}{6C_m}\left(1+\frac{xNC}{2L_m C_m + 6L_{dc} C_m}\right) + xC\left[N\left(\frac{L_m}{3}+L_{dc}+\frac{xL}{2}\right)+2R_m C_m\left(\frac{xR}{2}+\frac{R_m}{3}\right)\right]$$$

*系统传递函数特征方程的三次项系数，反映故障距离x与线路/换流器参数的耦合关系。*


**公式3**: $$$k_4 = \frac{2R_m C_m\left(1+\frac{xNC}{6C_m}\right)+xNC\frac{xR}{2}+R_f^3}{N}$$$

*特征方程的四次项系数，包含过渡电阻Rf与线路参数的非线性影响。*


**公式4**: $$$k_5 = \frac{3x^2 L C C_m}{C_m(2L_m+6L_{dc}+3xL)+xC C_m(3xR+6R_f)}$$$

*特征方程的高阶系数，用于解析暂态电压响应的极点分布与故障位置的关联。*


### 算法步骤

1. 数据采集与预处理：在故障发生瞬间启动录波，截取故障后2.5ms的单端直流母线电压暂态波形，进行去噪与基线校正处理，确保数据窗严格对齐故障起始点。

2. 暂态特征提取：对预处理后的电压波形进行极值与过零点检测，精确提取三个关键特征量：故障电压突变的延迟时间（$t_d$）、首个负向峰值出现的时刻（$t_{peak}$）以及该负峰值的幅值（$V_{peak}$）。

3. 特征归一化与向量化：将提取的三个特征量进行标准化处理，消除量纲差异与系统基准值影响，构建为固定维度的输入特征向量。

4. RNN推理计算：将特征向量输入预先离线训练好的回归神经网络（RNN）。网络通过多层非线性变换，补偿因实际分布参数、HDCCB动作特性及高阻故障导致的集中参数模型近似误差。

5. 故障距离输出：RNN输出层直接映射为故障点距测量端的物理距离（km），完成超快定位，全过程计算耗时远低于HDCCB动作时间。


### 关键参数

- **Rm**: 1 Ω (桥臂电阻)

- **Lm**: 29 mH (桥臂电感)

- **Cm**: 11000 μF (子模块电容)

- **N**: 220 (每桥臂子模块数)

- **Ldc**: 200 mH (直流侧限流电抗)

- **数据窗长度**: 2.5 ms

- **最大过渡电阻**: 1005 Ω

- **抗噪水平**: 40 dB 白噪声



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 全线路范围与高阻故障测试 | 在0~100%线路长度范围内设置故障，过渡电阻最高达1005 Ω。算法在2.5ms数据窗内完成计算，定位误差始终控制在1.2%以内，未出现发散或误判。 | 相比传统行波法在高阻/远端故障时因波头色散导致的定位失效（误差常>5%），本方法在1005Ω下仍保持高精度，且无需MHz级采样。 |

| 参数偏差与噪声鲁棒性测试 | 在线路参数（R/L/C）与限流电抗Ldc存在±15%合理偏差及叠加40dB高斯白噪声的工况下，算法输出结果波动极小，定位误差<1.5%。 | 传统基于集中参数RL解析法在参数偏差下误差显著放大（>8%），本方法通过RNN补偿使误差降低约80%以上。 |

| 跨系统适应性验证 | 将训练好的模型直接应用于不同拓扑结构与参数的MMC-HVDC系统，无需重新训练即可实现准确定位，平均定位误差<1.8%。 | 相比需针对特定系统重新整定参数的传统阻抗法或需大量同步数据的双端法，本方法具备即插即用的跨系统适应性，部署成本降低90%。 |



## 量化发现

- 算法仅需2.5ms故障后数据窗即可完成定位，满足HDCCB快速隔离（通常<5ms）的时间要求。
- 在高达1005Ω的过渡电阻下，定位误差<1.2%，克服了高阻故障行波衰减严重的难题。
- 经2.02×10^4组独立故障案例验证，算法在全线路范围内均表现出高准确率，平均绝对误差<0.8km。
- 在叠加40dB白噪声及线路参数/限流电抗合理偏差的恶劣工况下，定位误差仍控制在1.5%以内。
- RNN有效补偿了集中参数模型与实际分布参数拓扑之间的特征提取误差，实现了从近似特征到精确距离的非线性映射，推理耗时<0.1ms。


## 关键公式

### MMC暂态等效阻抗公式

$$$Z_{eq} = \frac{sL_m}{3} + \frac{R_m}{3} + \frac{N}{6sC_m}$$$

*用于构建故障初期的集中参数RLC等效电路，推导电压暂态响应特征与故障距离的理论映射关系。*

### RNN特征-距离映射模型

$$$\text{RNN}_{mapping}(t_d, t_{peak}, V_{peak}) \rightarrow x_{fault}$$$

*在实际工程中替代解析法，利用神经网络拟合复杂拓扑与参数偏差下的非线性关系，实现超快高精度定位。*



## 验证详情

- **验证方式**: 电磁暂态（EMT）数字仿真验证与大规模数据集测试
- **测试系统**: 半桥型MMC-HVDC直流输电系统（配备HDCCB与直流限流电抗，含详细子模块与线路分布参数模型）
- **仿真工具**: PSCAD/EMTDC（用于生成高精度EMT故障波形数据集）与 MATLAB/Python（用于RNN模型训练与推理验证）
- **验证结果**: 通过20200组独立故障样本验证，算法在2.5ms极短数据窗内实现全线路高精度定位。对1005Ω高阻故障、40dB强噪声干扰及线路/电抗参数偏差均表现出极强的鲁棒性与泛化能力，显著优于传统行波法与集中参数解析法，完全适配快速保护与HDCCB动作时序要求。

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



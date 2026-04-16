---
title: "Modal Domain Based Modeling of Parallel Transmission Lines"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Gustavsen - 2012 - Modal domain-based modeling of parallel transmission lines with emphasis on accurate representation.pdf"]
---

# Modal Domain Based Modeling of Parallel Transmission Lines

**作者**: 
**年份**: 2012
**来源**: `26/Gustavsen - 2012 - Modal domain-based modeling of parallel transmission lines with emphasis on accurate representation.pdf`

## 摘要

—Transient and harmonic coupling effects between par- allel overhead lines are normally modeled via frequency-depen- dent traveling-wave-type transmission-line models. Several elec- tromagnetic transient programs rely on a line model based on a constant transformation matrix and modes (FD-line). These line models can, however, give substantial errors in the studies of cou- pled disturbance from one line to a neighbor line. In this paper, we show that the accuracy of the FD-line in these applications can be greatly improved by representing the line system by independent FD-lines in combination with rational models that take the mutual coupling between the lines into account. A mode-revealing trans- formation is used for further enhancing the accuracy of the cou- pling effect. The approach i

## 核心贡献


- 提出将平行线路解耦为独立FD模型，结合宽频有理函数精确表征互感耦合
- 引入实值模态揭示变换矩阵，有效分离运行模态分量，避免零序分量掩盖
- 低频段分离容性与感性耦合路径，通过端电压电流组合提升互阻抗拟合精度


## 使用的方法


- [[fd线路模型|FD线路模型]]
- [[宽频有理函数拟合|宽频有理函数拟合]]
- [[模态揭示变换|模态揭示变换]]
- [[容性与感性耦合分离|容性与感性耦合分离]]
- [[逆数值拉普拉斯变换|逆数值拉普拉斯变换]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]


## 涉及的模型


- [[平行架空输电线路|平行架空输电线路]]
- [[铁路信号系统|铁路信号系统]]
- [[fd线路模型|FD线路模型]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[互感耦合分析|互感耦合分析]]
- [[电磁兼容|电磁兼容]]
- [[变压器励磁涌流|变压器励磁涌流]]
- [[铁路信号干扰|铁路信号干扰]]


## 主要发现


- 新方法在平行线路投切暂态中，耦合电压波形与通用线路模型结果高度吻合
- 准确复现了变压器励磁涌流及故障暂态对邻近铁路信号系统的电磁干扰水平
- 相比传统FD模型互感耦合计算误差显著降低，同时保持了较高的仿真效率



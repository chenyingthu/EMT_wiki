---
title: "Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting"
type: source
authors: ['Alexandre', 'A.', 'Kida']
year: 2024
journal: "Electric Power Systems Research, 234 (2024) 110778. doi:10.1016/j.epsr.2024.110778"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf"]
---

# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

**作者**: Alexandre, A., Kida
**年份**: 2024
**来源**: `17/Kida 等 - 2024 - Enhancing computation performance of rational approximation for frequency-dependent network equivale-1.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c

## 核心贡献


- 提出复数矢量拟合用于FDNE导纳矩阵综合，解除极点共轭约束
- 基于C语言实现VF与CVF并行化算法，摆脱商业软件依赖
- 构建多端口网络等值有理逼近框架，显著提升大规模系统拟合效率


## 使用的方法


- [[复数矢量拟合-cvf|复数矢量拟合(CVF)]]
- [[矢量拟合-vf|矢量拟合(VF)]]
- [[有理逼近|有理逼近]]
- [[并行计算|并行计算]]
- [[频域实现|频域实现]]
- [[状态空间综合|状态空间综合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[多端口导纳矩阵|多端口导纳矩阵]]
- [[有理模型-rm|有理模型(RM)]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[并行计算|并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[模型降阶|模型降阶]]


## 主要发现


- 并行化C语言实现显著降低多端口拟合耗时，计算效率优于传统MATLAB脚本
- CVF成功应用于导纳矩阵综合，解除共轭约束后仍保持宽频带高精度拟合
- 算法性能随端口数与阶数增加呈良好扩展性，验证了大规模等值建模可行性



---
title: "Algorithm for fast calculating the energization overvoltages along a power cable based on modal theory and numerical inverse Laplace transform"
type: source
authors: ['Han Li']
year: 2022
journal: "Electric Power Systems Research, 210 (2022) 108163. doi:10.1016/j.epsr.2022.108163"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Li 等 - 2022 - Algorithm for fast calculating the energization overvoltages along a power cable based on modal theo.pdf"]
---

# Algorithm for fast calculating the energization overvoltages along a power cable based on modal theory and numerical inverse Laplace transform

**作者**: Han Li
**年份**: 2022
**来源**: `06/Li 等 - 2022 - Algorithm for fast calculating the energization overvoltages along a power cable based on modal theo.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Algorithm for fast calculating the energization overvoltages along a power cable based on modal theory and numerical inverse Laplace transform Han Li a, Peixin Yu a, Shurong Li a, Xuefeng Zhao b, Junbo Deng a,*, Guanjun Zhang a a State Key Laboratory of Electrical Insulation and Power Equipment, Xi’an Jiaotong University, Xi’an, 710049, China

## 核心贡献


- 提出基于模态理论与数值拉普拉斯逆变换的电缆沿线过电压快速计算算法
- 推导复频域位置相关电压公式，解耦多导体回路并消除传统仿真最小步长限制
- 实现长电缆多分段场景下暂态过电压高效求解，避免复杂二端口网络建模


## 使用的方法


- [[模态理论|模态理论]]
- [[数值拉普拉斯逆变换|数值拉普拉斯逆变换]]
- [[拉普拉斯变换|拉普拉斯变换]]
- [[相模变换|相模变换]]
- [[电报方程求解|电报方程求解]]


## 涉及的模型


- [[电力电缆|电力电缆]]
- [[交叉互联电缆|交叉互联电缆]]
- [[频变相位模型|频变相位模型]]
- [[分布参数模型|分布参数模型]]


## 相关主题


- [[合闸过电压|合闸过电压]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电缆沿线电压分布|电缆沿线电压分布]]
- [[快速计算算法|快速计算算法]]


## 主要发现


- 在330kV/9.6km电缆算例中，算法结果与PSCAD频变模型相对误差小于1%
- 最大CPU耗时仅为传统模型的8%，在保障精度的前提下大幅提升计算速度
- 算法有效克服传统软件对长电缆多分段建模的复杂性，适用于紧急工况快速评估



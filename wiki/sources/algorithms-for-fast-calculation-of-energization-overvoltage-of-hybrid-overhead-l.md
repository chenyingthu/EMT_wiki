---
title: "Algorithms for fast calculation of energization overvoltage of hybrid overhead line-cable transmission lines based on full frequency-dependent parameters"
type: source
authors: ['Borui Gu']
year: 2023
journal: "Electric Power Systems Research, 225 (2023) 109875. doi:10.1016/j.epsr.2023.109875"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans-1.pdf"]
---

# Algorithms for fast calculation of energization overvoltage of hybrid overhead line-cable transmission lines based on full frequency-dependent parameters

**作者**: Borui Gu
**年份**: 2023
**来源**: `06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans-1.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Algorithms for fast calculation of energization overvoltage of hybrid overhead line-cable transmission lines based on full Borui Gu a, Han Li a, Shurong Li a, Xiaoguang Zhu a, Xuefeng Zhao b, Junbo Deng a,*, a State Key Laboratory of Electrical Insulation and Power Equipment, Xi’an Jiaotong University, Xi’an, 710049, China

## 核心贡献


- 提出基于全频域参数的混合线路过电压快速算法，突破传统EMT仿真步长限制
- 结合相模变换与改进数值拉普拉斯逆变换，实现复频域到时域的高效转换
- 构建基于拓扑的频变边界条件模型，简化复杂混合输电系统建模流程


## 使用的方法


- [[相模变换|相模变换]]
- [[数值拉普拉斯逆变换-nilt|数值拉普拉斯逆变换(NILT)]]
- [[全频域参数计算|全频域参数计算]]
- [[复频域边界条件推导|复频域边界条件推导]]
- [[电报方程求解|电报方程求解]]


## 涉及的模型


- [[混合架空线-电缆线路|混合架空线-电缆线路]]
- [[频变相模型-fdpm|频变相模型(FDPM)]]
- [[j-marti模型|J.Marti模型]]
- [[transmission-line-model|Bergeron线路模型]]
- [[π型集中参数模型|π型集中参数模型]]


## 相关主题


- [[合闸过电压计算|合闸过电压计算]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[输电线路模态分析|输电线路模态分析]]
- [[复频域时域转换|复频域时域转换]]


## 主要发现


- 算法计算结果与PSCAD频变相模型对比，最大相对误差低于0.261%
- 计算耗时仅为传统频变相模型的32.6%至58.6%，显著提升仿真效率
- 在330kV混合输电系统验证中，算法兼顾高精度与快速性，满足工程需求



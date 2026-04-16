---
title: "A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations"
type: source
authors: ['Ajinkya Sinkar']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112203. doi:10.1016/j.epsr.2025.112203"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/01/Sinkar 等 - 2025 - A Computationally Efficient Approach for Power Semiconductor Loss Estimation of Modular Multilevel C.pdf"]
---

# A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations

**作者**: Ajinkya Sinkar
**年份**: 2025
**来源**: `01/Sinkar 等 - 2025 - A Computationally Efficient Approach for Power Semiconductor Loss Estimation of Modular Multilevel C.pdf`

## 摘要

A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations a Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada b Manitoba Hydro International, Winnipeg, MB R3R 1A3, Canada This paper presents a computationally efficient approach for estimating the power semiconductor losses of a

## 核心贡献


- 提出基于桥臂级详细等效模型的MMC功率半导体损耗高效估计算法
- 将器件级损耗计算与EMT仿真DEM更新算法融合，显著提升仿真速度
- 支持稳态与暂态工况下的精确损耗评估，并可独立输出各子模块损耗


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[桥臂级详细等效模型|桥臂级详细等效模型]]
- [[分段线性波形近似|分段线性波形近似]]
- [[插值开关技术|插值开关技术]]
- [[集总参数热网络模型|集总参数热网络模型]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[igbt-二极管对|IGBT-二极管对]]
- [[半桥子模块|半桥子模块]]
- [[mmc-model|MMC]]


## 相关主题


- [[功率半导体损耗评估|功率半导体损耗评估]]
- [[emt仿真加速|EMT仿真加速]]
- [[热网络建模|热网络建模]]
- [[mmc-model|MMC]]
- [[开关损耗计算|开关损耗计算]]


## 主要发现


- 在两端MMC-HVDC测试系统中验证了算法精度，与器件级模型结果高度一致
- 相比传统逐开关建模方法，该桥臂级等效方法大幅降低了计算负担并提升仿真速度
- 能够准确捕捉稳态及暂态工况下的开关与导通损耗，支持子模块级损耗独立输出



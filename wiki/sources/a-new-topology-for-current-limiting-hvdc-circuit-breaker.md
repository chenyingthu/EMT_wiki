---
title: "A new topology for current limiting HVDC circuit breaker"
type: source
authors: ['Shuai Li']
year: 2018
journal: "Electrical Power and Energy Systems, 104 (2018) 933-942. doi:10.1016/j.ijepes.2018.07.042"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Li 等 - 2019 - A new topology for current limiting HVDC circuit breaker.pdf"]
---

# A new topology for current limiting HVDC circuit breaker

**作者**: Shuai Li
**年份**: 2018
**来源**: `02/Li 等 - 2019 - A new topology for current limiting HVDC circuit breaker.pdf`

## 摘要

A new topology for current limiting HVDC circuit breaker☆ Shuai Li⁎, Jiyuan Zhang, Jianzhong Xu, Chengyong Zhao The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China With the high voltage direct current Transmission (HVDC) booming, HVDC grid has received wide attention. As an essential component in HVDC grid, high voltage direct current circuit breakers (DCCB) requires urgent and

## 核心贡献


- 提出一种含主断路器与支路断路器的模块化限流直流断路器新拓扑
- 设计可灵活配置的电感支路结构，有效增强限流效果并降低单支路电流应力
- 实现疑似故障提前限流，将最大故障检测延时放宽至12ms且保障电流不越限


## 使用的方法


- [[pscad-emtdc电磁暂态仿真|PSCAD/EMTDC电磁暂态仿真]]
- [[等效电路分析|等效电路分析]]
- [[硬件实验验证|硬件实验验证]]


## 涉及的模型


- [[cl-dccb|CL-DCCB]]
- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[igbt模块|IGBT模块]]
- [[金属氧化物避雷器-moa|金属氧化物避雷器(MOA)]]
- [[超快机械开关-ufd|超快机械开关(UFD)]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[直流限流技术|直流限流技术]]
- [[过电压保护|过电压保护]]
- [[直流电网故障保护|直流电网故障保护]]
- [[故障检测延时优化|故障检测延时优化]]


## 主要发现


- 仿真与实验验证表明，该拓扑可将最大故障检测延时安全延长至12ms
- 增加电感支路数量或单支路电感值可显著提升限流效果并降低器件应力
- 提前限流机制有效配合ROCOV检测，确保故障电流始终低于断路器开断极限



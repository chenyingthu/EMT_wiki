---
title: "适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型"
type: source
authors: ['CNKI']
year: 2024
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/基于模块化多电平换流器的超级电容储能系统高效仿真方法_朱琼海和肖晃庆_2024.pdf"]
---

# 适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型

**作者**: CNKI
**年份**: 2024
**来源**: `15/基于模块化多电平换流器的超级电容储能系统高效仿真方法_朱琼海和肖晃庆_2024.pdf`

## 摘要

MMC-SCES 电磁暂态仿真方法。该仿真运用嵌套快速求解方法对MMC-SCES 进行建模，不仅可以大幅降低 Project supported by the Fundamental Research Funds for the Central Universities（2022ZYGXZR050） and the Science and Technology Planning Project of Guangzhou（202201010694）

## 核心贡献



- 提出基于桥臂戴维南等效电路的MMC-SCES高效电磁暂态仿真方法
- 设计嵌套快速求解算法，在保留换流器所有动态变量的同时大幅降低仿真计算规模

## 使用的方法


- [[average-value-model]]
- [[state-space]]
- [[nodal-analysis]]

## 涉及的模型


- [[mmc]]
- [[mmc-model]]
- [[average-value-model]]

## 相关主题


- [[real-time]]
- [[hvdc]]

## 主要发现



- 所提方法相比详细开关模型仿真速度最高可提升约518倍
- 仿真绝对误差标幺化积分控制在1%以内，精度显著优于传统平均值模型
- 能够准确拟合子模块内部动态变量，完整保留换流器动态特性
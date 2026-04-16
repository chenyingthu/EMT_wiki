---
title: "Fast Loss Evaluation Method Based on MMC Average Simulation Model; 基于MMC平均值仿真模型的损耗快速评估方法"
type: source
authors: ['Sun', 'Hao']
year: 2024
journal: "中国电机工程学报"
tags: ['mmc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Sun和Hao - 2024 - Fast Loss Evaluation Method Based on MMC Average Simulation Model; [基于 MMC 平均值仿真模型的损耗快速评估方法].pdf"]
---

# Fast Loss Evaluation Method Based on MMC Average Simulation Model; 基于MMC平均值仿真模型的损耗快速评估方法

**作者**: Sun, Hao
**年份**: 2024
**来源**: `19、20、21/EMT_task_19/Sun和Hao - 2024 - Fast Loss Evaluation Method Based on MMC Average Simulation Model; [基于 MMC 平均值仿真模型的损耗快速评估方法].pdf`

## 摘要

To address the problem that the calculation accuracy and speed of MMC losses are difficult to balance, a fast online evaluation method of losses is proposed based on the determined modulation model and the average simulation model of MMC. 

## 核心贡献



- 提出一种基于MMC平均值模型与确定调制策略的损耗快速在线评估方法，有效平衡计算精度与速度
- 提出基于衰减函数的开关损耗注入方法，避免注入电压尖峰并改善注入效果，实现损耗对仿真结果的实时表征

## 使用的方法


- [[average-value-model]]

## 涉及的模型


- [[mmc-model]]
- [[average-value-model]]

## 相关主题


- [[mmc]]
- [[hvdc]]

## 主要发现



- 利用平均值模型计算开关频率与损耗上限，结合开关频率曲面可实现实际开关损耗的快速高精度近似计算
- 基于衰减函数的损耗注入方法能有效避免传统注入产生的电压尖峰，显著提升在线评估的仿真稳定性与计算效率
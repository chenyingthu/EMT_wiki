---
title: "面向指数积分方法的电磁暂态仿真GPU并行算法"
type: source
authors: ['作者']
year: 2018
journal: "科目"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Zhao 等 - 2018 - GPU Based Parallel Algorithm Oriented to Exponential Integration Method for Electromagnetic Transien.pdf"]
---

# 面向指数积分方法的电磁暂态仿真GPU并行算法

**作者**: 作者
**年份**: 2018
**来源**: `19、20、21/EMT_task_21/Zhao 等 - 2018 - GPU Based Parallel Algorithm Oriented to Exponential Integration Method for Electromagnetic Transien.pdf`

## 摘要

(１．智能电网教育部重点实验室(天津大学),天津市３０００７２;２．国网经济技术研究院有限公司,北京市１０２２０９)

## 核心贡献



- 提出了一种面向指数积分方法的电力系统电磁暂态仿真GPU并行算法
- 设计了CPU-GPU协同计算架构，利用GPU处理大规模矩阵运算，CPU负责复杂状态判别与更新，显著提升仿真效率

## 使用的方法


- [[numerical-integration]]
- [[parallel]]

## 涉及的模型

- [[风机|风机]]
- [[风电场|风电场]]

## 相关主题


- [[wind-farm]]

## 主要发现



- 所提GPU并行算法能有效提升电磁暂态仿真计算速度，且在风电场算例中验证了正确性与有效性
- 算法的加速效果会随着系统规模的增加而愈发明显
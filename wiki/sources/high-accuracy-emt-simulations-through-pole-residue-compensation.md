---
title: "High-accuracy EMT simulations through pole-residue compensation"
type: source
authors: ['A.A. Kida']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112394. doi:10.1016/j.epsr.2025.112394"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Kida 等 - 2026 - High-accuracy EMT simulations through pole-residue compensation.pdf"]
---

# High-accuracy EMT simulations through pole-residue compensation

**作者**: A.A. Kida
**年份**: 2025
**来源**: `19、20、21/EMT_task_21/Kida 等 - 2026 - High-accuracy EMT simulations through pole-residue compensation.pdf`

## 摘要

High-accuracy EMT simulations through pole-residue compensation ⋆ A. A. Kida a,∗, A.C.S. Lima b, F. A. Moreira c, F. M. Vasconcellos c b Department of Electrical Engineering, COPPE/UFRJ, Federal University of Rio de Janeiro, Rio de Janeiro, Brazil c Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, BA, Brazil This paper addresses the frequency warping error in frequency-dependent equivalents to improve the accuracy of

## 核心贡献


- 提出极点留数频率畸变补偿算法，直接修正梯形积分法引入的频响失真。
- 推导预畸变对有理近似模型中电感与电容参数的解析修正公式。
- 构建无需重新拟合的频变等效模型补偿策略，兼容现有电磁暂态求解器。


## 使用的方法


- [[有理函数逼近|有理函数逼近]]
- [[极点-留数形式|极点-留数形式]]
- [[梯形积分法|梯形积分法]]
- [[预畸变技术|预畸变技术]]
- [[频率畸变补偿算法|频率畸变补偿算法]]
- [[矢量拟合|矢量拟合]]


## 涉及的模型


- [[频变等效模型|频变等效模型]]
- [[输电线路|输电线路]]
- [[配电系统|配电系统]]
- [[节点导纳矩阵|节点导纳矩阵]]
- [[rlcg等效电路|RLCG等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[数值积分误差|数值积分误差]]
- [[频响失真补偿|频响失真补偿]]
- [[时域仿真精度|时域仿真精度]]


## 主要发现


- 补偿算法使频变等效模型时域仿真精度较未补偿模型提升两个数量级。
- 算法引入的计算开销极低，可无缝集成至现有电磁暂态仿真程序中。
- 即使积分步长满足传统经验准则，频率畸变仍会显著降低长时仿真精度。



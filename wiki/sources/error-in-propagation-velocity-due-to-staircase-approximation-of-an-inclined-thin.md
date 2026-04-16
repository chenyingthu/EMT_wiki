---
title: "Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge Simulation"
type: source
authors: ['T. Noda', 'R. Yonezawa', 'S. Yokoyama', 'Y. Takahashi']
year: 2004
journal: "IEEE Transactions on Power Delivery;2004;19;4;10.1109/TPWRD.2004.835396"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Noda 等 - 2004 - Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge.pdf"]
---

# Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge Simulation

**作者**: T. Noda, R. Yonezawa, S. Yokoyama 等
**年份**: 2004
**来源**: `18/Noda 等 - 2004 - Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge.pdf`

## 摘要

—This paper presents the result of a study on the error in propagation velocity introduced by the staircase approximation of a thin wire in the ﬁnite difference time domain (FDTD) surge simulation. The FDTD method directly solves Maxwell’s equations by discretizing the space of interest into cubic cells. Thus, it is suit- able for solving very-fast surge phenomena which cannot be dealt with by conventional techniques based on the lumped- and dis- tributed-parameter circuit theories. However, FDTD has a limita- tion that the shape of a conductive object must be modeled by a combination of sides of cells with forced zero electric ﬁelds. This indicates that a thin wire, one of the most important components in the surge simulation, results in a staircase approximation, if the wire is not paral

## 核心贡献


- 提出并量化了FDTD中倾斜细线阶梯近似导致的波速误差特性
- 揭示了相邻导体单元间互感耦合对减缓波速误差的补偿机制
- 验证了阶梯近似在工程浪涌仿真中的实用精度与适用边界


## 使用的方法


- [[有限差分时域法-fdtd|有限差分时域法(FDTD)]]
- [[阶梯近似算法-sca|阶梯近似算法(SCA)]]
- [[麦克斯韦方程直接求解|麦克斯韦方程直接求解]]
- [[高斯脉冲激励|高斯脉冲激励]]


## 涉及的模型


- [[倾斜细线模型|倾斜细线模型]]
- [[双线导体系统|双线导体系统]]
- [[fdtd立方网格模型|FDTD立方网格模型]]


## 相关主题


- [[浪涌仿真|浪涌仿真]]
- [[波速误差分析|波速误差分析]]
- [[电磁暂态分析|电磁暂态分析]]
- [[空间离散化误差|空间离散化误差]]
- [[快速暂态现象|快速暂态现象]]


## 主要发现


- 阶梯近似使倾斜细线等效路径变长，理论最大波速减速可达42.3%
- 实际FDTD仿真中互感耦合显著补偿误差，最大波速误差小于14%
- 典型工程倾斜角度下阶梯近似仍能提供满足精度要求的浪涌结果



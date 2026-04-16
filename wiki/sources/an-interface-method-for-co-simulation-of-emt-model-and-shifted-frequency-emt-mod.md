---
title: "An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimation of Signal Parameters via Rotational Invariance Techniques"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Systems;2025;40;4;10.1109/TPWRS.2025.3555374"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimati.pdf"]
---

# An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimation of Signal Parameters via Rotational Invariance Techniques

**作者**: 
**年份**: 2025
**来源**: `07&08/An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimati.pdf`

## 摘要

—The shifted frequency-based electromagnetic tran- sient (SFEMT) simulation is much more efﬁcient than traditional electromagnetic transient (EMT) simulation for AC grids. This letterproposesanovelinterfacefortheco-simulationoftheSFEMT model and the conventional EMT model. The fundamentals of SFEMT modeling are ﬁrst derived. Then, an interface for the co-simulation of EMT and SFEMT models is proposed based on the estimation of signal parameters via rotational invariance techniques. Theoretical analyses and test results demonstrate the effectiveness of the proposed method. Index Terms—Analytical signal, co-simulation, interface, electr- omagnetic transient simulation, shifted-frequency simulation. I. INTRODUCTION T HE dynamics of a power system involve multi-scale tran- sients. As a result,

## 核心贡献


- 提出基于ESPRIT的EMT与SFEMT联合仿真接口，消除解析信号负频分量干扰
- 推导SFEMT建模通用形式，明确解析信号构造的频谱正交条件，奠定接口设计理论基础
- 利用短数据窗Hankel矩阵与奇异值分解，实现信号频率、幅值与相位的快速精确提取


## 使用的方法


- [[esprit算法|ESPRIT算法]]
- [[频移电磁暂态仿真-sfemt|频移电磁暂态仿真(SFEMT)]]
- [[hankel矩阵构建|Hankel矩阵构建]]
- [[奇异值分解-svd|奇异值分解(SVD)]]
- [[分布式输电线路接口|分布式输电线路接口]]
- [[解析信号构造|解析信号构造]]


## 涉及的模型


- [[传统emt模型|传统EMT模型]]
- [[sfemt模型|SFEMT模型]]
- [[交流电网|交流电网]]
- [[分布式输电线路|分布式输电线路]]


## 相关主题


- [[多尺度联合仿真|多尺度联合仿真]]
- [[频移仿真技术|频移仿真技术]]
- [[信号参数估计|信号参数估计]]
- [[解析信号构造|解析信号构造]]
- [[接口数据交互|接口数据交互]]
- [[电力系统暂态仿真|电力系统暂态仿真]]


## 主要发现


- 理论与测试表明，该接口能精确构造无负频解析信号，显著提升联合仿真精度
- 短数据窗下即可准确提取信号参数，有效克服传统接口因频谱混叠导致的精度损失
- 验证了接口在模型间数据交互的稳定性，适用于多尺度电力系统暂态仿真



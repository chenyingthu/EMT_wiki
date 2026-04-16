---
title: "A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems"
type: source
year: 2017
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Shu 等 - 2018 - A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems.pdf"]
---

# A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems

**年份**: 2017
**来源**: `02/Shu 等 - 2018 - A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems.pdf`

## 摘要

—This paper proposes a novel multi-rate co-simulation method to improve simulation efﬁciency of large-scale AC plus multi-terminal DC (MTDC) grids. In this method, the whole system is partitioned into different AC and MTDC subsystems. They each are simulated with different time-steps according to their requirements of accuracy. Unlike existing methods where simpliﬁed models are adopted, the proposed approach fully reserves both the detailed behavior of converters and the nonlinear dynamics of large-scale AC systems. To realize the coordination between different subsystems, updating and discretization of the interface models are signiﬁcant to guarantee the overall numerical accuracy and stability of the co-simulation method. Accordingly, the interface models of the partitioned AC and DC net

## 核心贡献


- 提出交直流多速率协同仿真架构，按动态特性分配步长，完整保留换流器细节与交流非线性。
- 构建时变戴维南/诺顿接口模型，结合滑动窗口预测与逐步校正，消除混叠与时延误差。
- 引入根匹配算法抑制接口数值振荡，基于增广网络方程同步求解，保障协同仿真稳定性。


## 使用的方法


- [[多速率协同仿真|多速率协同仿真]]
- [[时变戴维南-诺顿等效|时变戴维南/诺顿等效]]
- [[增广网络方程|增广网络方程]]
- [[根匹配算法|根匹配算法]]
- [[滑动窗口预测|滑动窗口预测]]
- [[逐步校正与平均技术|逐步校正与平均技术]]
- [[数值振荡抑制|数值振荡抑制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mtdc|MTDC]]
- [[大型交流系统|大型交流系统]]
- [[戴维南等效模型|戴维南等效模型]]
- [[诺顿等效模型|诺顿等效模型]]


## 相关主题


- [[多速率仿真|多速率仿真]]
- [[协同仿真|协同仿真]]
- [[接口建模|接口建模]]
- [[网络分割|网络分割]]
- [[数值稳定性|数值稳定性]]
- [[mmc-model|MMC]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 实际系统验证表明，该方法在保持高精度的同时显著提升大规模交直流系统计算效率。
- 接口预测校正策略有效消除多速率交互混叠与时延误差，关键变量波形与基准高度吻合。
- 根匹配算法有效抑制接口离散化数值振荡，保障强扰动下协同仿真的数值稳定性与收敛性。



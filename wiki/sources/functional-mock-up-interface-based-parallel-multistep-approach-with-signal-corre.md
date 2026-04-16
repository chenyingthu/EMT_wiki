---
title: "Functional Mock-Up Interface Based Parallel Multistep Approach With Signal Correction for Electromagnetic Transients Simulations"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Systems;2019;34;3;10.1109/TPWRS.2019.2902740"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRS.2019.2902740.pdf.pdf"]
---

# Functional Mock-Up Interface Based Parallel Multistep Approach With Signal Correction for Electromagnetic Transients Simulations

**作者**: 
**年份**: 2019
**来源**: `19、20、21/EMT_task_20/TPWRS.2019.2902740.pdf.pdf`

## 摘要

—This letter presents the latest improvements of a previously proposed parallel and multistep approach based on the functional mock-up interface standard for the simulation of electromagnetic transients. The im- proved approach extends the capacity of the original parallel asynchronous mode into accommodating the use of different time-steps in different decoupled subsystems. It also introduces a signal correction procedure using linear extrapolation in multistep simulations, greatly enhancing simulation ﬂexibility, efﬁciency, and accuracy. Numerical examples are provided to demonstrate the computational advantages of the improved approach. Index Terms—FMI, electromagnetic transients, parallel simulation, mul- tistep simulation. I. INTRODUCTION W ITH the ever-growing popularity of Electroma

## 核心贡献


- 扩展FMI并行异步模式，支持解耦子系统采用不同仿真步长运行
- 提出基于线性外推的信号校正算法，有效消除多步长数据交互误差
- 优化主从时间步同步机制，大幅提升含复杂控制系统仿真的灵活性


## 使用的方法


- [[fmi协同仿真|FMI协同仿真]]
- [[并行多步长算法|并行多步长算法]]
- [[异步时间步同步|异步时间步同步]]
- [[线性外推信号校正|线性外推信号校正]]


## 涉及的模型


- [[风电机组详细模型|风电机组详细模型]]
- [[风电场集电网络|风电场集电网络]]
- [[戴维南等值系统|戴维南等值系统]]
- [[复杂控制系统|复杂控制系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[多步长仿真|多步长仿真]]
- [[风电场建模|风电场建模]]
- [[仿真加速|仿真加速]]


## 主要发现


- 并行异步模式与同步模式精度相当，信号校正显著提升电压与功率波形精度
- 多步长异步配置下获得最高计算加速比，验证了方法在多核平台上的可扩展性
- 线性外推校正有效抑制了主从步长不匹配导致的数值误差，保障了仿真稳定性



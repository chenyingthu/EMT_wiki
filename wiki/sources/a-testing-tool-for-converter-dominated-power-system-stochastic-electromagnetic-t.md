---
title: "A Testing Tool for Converter-Dominated Power System: Stochastic Electromagnetic Transient Simulation"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics;2022;10;5;10.1109/JESTPE.2022.3146231"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/Chen 等 - 2022 - A Testing Tool for Converter-Dominated Power System Stochastic Electromagnetic Transient Simulation-1.pdf"]
---

# A Testing Tool for Converter-Dominated Power System: Stochastic Electromagnetic Transient Simulation

**作者**: 
**年份**: 2022
**来源**: `04/Chen 等 - 2022 - A Testing Tool for Converter-Dominated Power System Stochastic Electromagnetic Transient Simulation-1.pdf`

## 摘要

—To investigate the impact of uncertain vari- 1 ability and provide a rigorous testing environment for

## 核心贡献


- 建立基于随机微分方程的集总元件参数迁移模型，推导动态伴随电路兼容EMTP框架。
- 分析后向与梯形Milstein格式的数值稳定性，给出保证随机仿真稳定的必要条件。
- 设计兼容EMTP框架的数值算法，提出节点重分配与矩阵分解的网络求解加速技术。


## 使用的方法


- [[随机微分方程-sde|随机微分方程(SDE)]]
- [[动态伴随电路法|动态伴随电路法]]
- [[milstein数值积分格式|Milstein数值积分格式]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[矩阵分解加速技术|矩阵分解加速技术]]


## 涉及的模型


- [[参数迁移集总元件-r-l-c|参数迁移集总元件(R/L/C)]]
- [[三相两电平整流器|三相两电平整流器]]
- [[两端直流配电系统|两端直流配电系统]]
- [[变流器控制子系统|变流器控制子系统]]


## 相关主题


- [[随机电磁暂态仿真|随机电磁暂态仿真]]
- [[参数不确定性建模|参数不确定性建模]]
- [[数值稳定性分析|数值稳定性分析]]
- [[变流器主导电力系统|变流器主导电力系统]]
- [[emtp框架集成|EMTP框架集成]]


## 主要发现


- 工具能同步模拟参数随机迁移与系统动态，有效验证极端工况下控制子系统的协调性能。
- 确定性仿真可作为随机扰动在合理分布范围内的参考基准，验证了算法的数值稳定性。
- 节点重分配与矩阵分解技术显著提升了大规模系统随机暂态仿真的网络求解效率。



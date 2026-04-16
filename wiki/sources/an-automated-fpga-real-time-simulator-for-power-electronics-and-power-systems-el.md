---
title: "An automated FPGA real-time simulator for power electronics and power systems electromagnetic transient applications"
type: source
authors: ['R. Razzaghi']
year: 2016
journal: "Electric Power Systems Research, 141 (2016) 147-156. doi:10.1016/j.epsr.2016.07.022"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/06/j.epsr.2016.07.022.pdf.pdf"]
---

# An automated FPGA real-time simulator for power electronics and power systems electromagnetic transient applications

**作者**: R. Razzaghi
**年份**: 2016
**来源**: `06/j.epsr.2016.07.022.pdf.pdf`

## 摘要

1. Introduction phenomena such as EMTs in power converters or travelling wave transients taking place in transmission lines (e.g., faults and switch- Electromagnetic transient (EMT) real-time simulators (RTSs) are ing transients). essential tools in power systems and power electronics to design, ...

## 核心贡献


- 提出结合MANA与FAMNM的自动化FPGA求解器，避免复杂底层编程
- 集成开关电导参数优化算法与高效稀疏矩阵乘法器，提升仿真精度
- 实现电力电子与输电线路系统的统一实时仿真架构，支持极低步长


## 使用的方法


- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[固定导纳矩阵节点法-famnm|固定导纳矩阵节点法(FAMNM)]]
- [[后向欧拉积分法|后向欧拉积分法]]
- [[稀疏矩阵向量乘法器|稀疏矩阵向量乘法器]]
- [[开关电导参数优化|开关电导参数优化]]


## 涉及的模型


- [[集中参数元件-rlc|集中参数元件(RLC)]]
- [[transmission-line-model|Bergeron线路模型]]
- [[离散时间开关模型|离散时间开关模型]]
- [[三相两电平逆变器|三相两电平逆变器]]
- [[三相电力网络|三相电力网络]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环-hil|硬件在环(HIL)]]
- [[fpga并行计算|FPGA并行计算]]
- [[电磁暂态分析|电磁暂态分析]]
- [[自动化求解器生成|自动化求解器生成]]


## 主要发现


- 仿真结果与EMTP-RV离线数据高度吻合，验证了求解器的数值准确性
- 硬件在环测试证实该架构能精确复现逆变器开关暂态与线路行波传播
- 优化开关电导参数有效抑制了固定导纳矩阵法引入的人工振荡误差



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

- 提出了一种面向电力电子与电力系统的自动化FPGA实时电磁暂态仿真器
- 集成了MANA、FAMNM、最优开关电导参数选择及高效稀疏矩阵向量乘法器
- 实现了极低积分步长，且通过自动化流程避免了针对不同拓扑的复杂FPGA编程与代码重构

## 使用的方法

- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[固定导纳矩阵节点法-famnm|固定导纳矩阵节点法(FAMNM)]]
- [[开关电导参数优化选择|开关电导参数优化选择]]
- [[高效稀疏矩阵向量乘法|高效稀疏矩阵向量乘法]]
- [[改进增广节点分析法-mana|改进增广节点分析法 (MANA)]]
- [[固定导纳矩阵节点法-famnm|固定导纳矩阵节点法 (FAMNM)]]
- [[最优开关电导参数选择技术|最优开关电导参数选择技术]]
- [[高效稀疏矩阵-向量乘法器|高效稀疏矩阵-向量乘法器]]
- [[fpga并行硬件架构与自动化配置流程|FPGA并行硬件架构与自动化配置流程]]

## 涉及的模型

- [[电力电子器件|电力电子器件]]
- [[输电线路|输电线路]]
- [[三相两电平逆变器|三相两电平逆变器]]
- [[三相电力系统|三相电力系统]]
- [[三相两电平逆变器|三相两电平逆变器]]
- [[三相电力网络|三相电力网络]]
- [[输电线路|输电线路]]
- [[电力电子变换器|电力电子变换器]]

## 相关主题

- [[实时仿真|实时仿真]]
- [[电磁暂态|电磁暂态]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[硬件在环-hil|硬件在环(HIL)]]
- [[自动化仿真|自动化仿真]]
- [[实时仿真|实时仿真]]
- [[电磁暂态-emt|电磁暂态 (EMT)]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[硬件在环-hil-测试|硬件在环 (HIL) 测试]]
- [[电力系统与电力电子|电力系统与电力电子]]

## 主要发现

- 该仿真器能够实时、准确地复现电力电子设备中的电磁暂态过程及输电线路中的行波传播现象
- MANA-FAMNM求解器结构支持极低的积分时间步长，且无需为不同拓扑重新设计FPGA代码
- 仿真结果与离线EMTP-RV仿真及硬件在环测试结果高度吻合，验证了其在复杂拓扑下的准确性与工程实用性

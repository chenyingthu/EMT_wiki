---
title: "High performance computing engines for the FPGA-based simulation of the ULM"
type: source
authors: ['Tarek Ould-Bachir']
year: 2020
journal: "Electric Power Systems Research, 190 (2021) 106716. doi:10.1016/j.epsr.2020.106716"
tags: ['fpga']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/j.epsr.2020.106716.pdf.pdf"]
---

# High performance computing engines for the FPGA-based simulation of the ULM

**作者**: Tarek Ould-Bachir
**年份**: 2020
**来源**: `19、20、21/EMT_task_21/j.epsr.2020.106716.pdf.pdf`

## 摘要

High performance computing engines for the FPGA-based simulation of the Tarek Ould-Bachira,⁎,1, Hossein Chalangarb,1, Keyhan Sheshyekanib, Jean Mahseredjianb a Department of Computer Engineering and Software Engineering, Polytechnique Montréal, Montreal, Canada b Department of Electrical Engineering, Polytechnique Montréal, Montreal, Canada This paper presents a design methodology for the FPGA-based simulation of the Universal Line Model (ULM).

## 核心贡献


- 提出ULM的FPGA设计方法，优化计算调度与历史项管理以降低延迟
- 采用深度流水线与浮点运算架构，实现250MHz主频与200ns仿真步长
- 基于状态空间法求解极留数拟合模型，提升硬件资源利用率与计算性能


## 使用的方法


- [[状态空间法|状态空间法]]
- [[极留数有理拟合|极留数有理拟合]]
- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[深度流水线调度|深度流水线调度]]
- [[浮点运算架构|浮点运算架构]]
- [[线性插值时延处理|线性插值时延处理]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[诺顿等效电路|诺顿等效电路]]


## 相关主题


- [[fpga实时仿真|FPGA实时仿真]]
- [[硬件在环测试|硬件在环测试]]
- [[频率相关线路建模|频率相关线路建模]]
- [[行波故障定位|行波故障定位]]
- [[高性能计算架构|高性能计算架构]]


## 主要发现


- 仿真步长降至200ns且主频达250MHz，突破现有FPGA微秒级限制
- 与EMTP对比验证模型精度，满足行波故障定位硬件在环测试需求
- 优化调度策略有效降低延迟，浮点运算下实现高吞吐与低延迟平衡



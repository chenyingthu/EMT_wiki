---
title: "Field Validated Generic EMT-Type Model of a Full Converter Wind Turbine Based on a Gearless Externally Excited Synchronous Generator"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery;2018;33;5;10.1109/TPWRD.2018.2850848"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/TPWRD.2018.2850848.pdf.pdf"]
---

# Field Validated Generic EMT-Type Model of a Full Converter Wind Turbine Based on a Gearless Externally Excited Synchronous Generator

**作者**: 
**年份**: 2018
**来源**: `19、20、21/EMT_task_19/TPWRD.2018.2850848.pdf.pdf`

## 摘要

—The integration of wind power plants introduces new dynamics into power systems, forcing reconsiderations of how they are studied, planned, and operated. High quality models are essen- tial to these studies. Manufacturer-speciﬁc electromagnetic tran- sient (EMT) wind turbine models are usually available only as black-boxes, which hinders analysis and research. To overcome this issue, this paper proposes a generic EMT-type model for a speciﬁc type-IV wind turbine system, which is validated against ﬁeld measurements from a wind turbine of the same type. More precisely, it proposes a wind turbine model based on an externally excited synchronous generator system connected to a full converter composed of a six-pulse diode rectiﬁer, a dc–dc boost stage and a two-level voltage source converter. 

## 核心贡献


- 提出基于无齿轮外励磁同步机与全功率变流器的通用EMT型风机详细模型
- 开发结合开关等效电路与平均值模型的混合架构，支持大仿真步长与实时应用
- 实现符合多国电网规范的双故障穿越策略及内部保护，提升模型工程实用性


## 使用的方法


- [[平均值模型|平均值模型]]
- [[开关等效电路|开关等效电路]]
- [[混合建模|混合建模]]
- [[标幺值控制|标幺值控制]]
- [[故障穿越控制|故障穿越控制]]


## 涉及的模型


- [[外励磁同步发电机|外励磁同步发电机]]
- [[两电平电压源换流器|两电平电压源换流器]]
- [[六脉冲二极管整流器|六脉冲二极管整流器]]
- [[dc-dc升压变换器|DC-DC升压变换器]]
- [[lcl滤波器|LCL滤波器]]
- [[单质量块机械模型|单质量块机械模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[实时仿真|实时仿真]]
- [[故障穿越|故障穿越]]
- [[电力电子建模|电力电子建模]]
- [[现场实测验证|现场实测验证]]


## 主要发现


- 混合模型通过等效电路与平均值结合显著增大步长，大幅提升计算效率
- 现场实测验证了模型在故障穿越工况下的电压电流动态响应精度与可靠性
- 内置聚合参数可有效表征多机并联等值动态，满足大规模风电场仿真需求



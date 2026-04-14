---
title: "Fast Electromagnetic Transient Simulation Method of Modular Multilevel Converter Based on Improved Semi-Implicit Delay Model"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Mu 等 - 2019 - Fast Electromagnetic Transient Simulation Model of Doubly-fed Induction Generator Based Wind Turbine.pdf"]
---

# Fast Electromagnetic Transient Simulation Method of Modular Multilevel Converter Based on Improved Semi-Implicit Delay Model

**作者**: 
**年份**: 2026
**来源**: `18/Mu 等 - 2019 - Fast Electromagnetic Transient Simulation Model of Doubly-fed Induction Generator Based Wind Turbine.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 建立了考虑Crowbar保护投切与变换器闭锁暂态过程的受控源型变换器统一简化等效模型
- 提出了一种预测校正的调制量计算方法
- 构建了完整的双馈风电机组快速电磁暂态仿真模型并验证了其工程适用性

## 使用的方法

- [[开关函数平均化|开关函数平均化]]
- [[预测校正调制量计算|预测校正调制量计算]]
- [[受控源等效建模|受控源等效建模]]
- [[pscad-emtdc仿真验证|PSCAD/EMTDC仿真验证]]

## 涉及的模型

- [[双馈风力发电机组|双馈风力发电机组]]
- [[电力电子变换器|电力电子变换器]]
- [[crowbar保护电路|Crowbar保护电路]]
- [[chopper保护电路|Chopper保护电路]]
- [[直流母线电容|直流母线电容]]
- [[统一简化等效模型|统一简化等效模型]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[双馈风电机组|双馈风电机组]]
- [[变换器简化建模|变换器简化建模]]
- [[仿真加速技术|仿真加速技术]]
- [[保护电路暂态分析|保护电路暂态分析]]

## 主要发现

- 所提模型在保证仿真正确性的前提下显著提升了仿真步长适应性与计算速度
- 模型能够准确模拟Crowbar保护投切及变换器闭锁等关键暂态过程，有效克服了传统平均化模型的局限性

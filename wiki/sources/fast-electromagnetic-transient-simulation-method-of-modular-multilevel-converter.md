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


- 提出考虑Crowbar投切与闭锁暂态的变换器统一简化等效模型，避免导纳阵反复修改
- 设计基于线性外推与阻尼校正的调制量预测校正算法，消除PWM环节对步长的限制
- 构建完整的双馈风电机组快速电磁暂态模型，实现大仿真步长下的高精度与高效率


## 使用的方法


- [[开关函数平均化|开关函数平均化]]
- [[预测校正法|预测校正法]]
- [[线性外推插值|线性外推插值]]
- [[后退欧拉法|后退欧拉法]]
- [[受控源等效模型|受控源等效模型]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[ac-dc变换器|AC/DC变换器]]
- [[crowbar保护电路|Crowbar保护电路]]
- [[chopper保护电路|Chopper保护电路]]
- [[直流母线电容|直流母线电容]]
- [[单质量块轴系模型|单质量块轴系模型]]


## 相关主题


- [[快速电磁暂态仿真|快速电磁暂态仿真]]
- [[风电机组建模|风电机组建模]]
- [[变换器简化建模|变换器简化建模]]
- [[低电压穿越|低电压穿越]]
- [[仿真步长适应性|仿真步长适应性]]


## 主要发现


- 快速模型在50μs步长下与5μs详细模型结果高度吻合，验证了模型正确性
- 单开关切换统一模型在多次闭锁工况下无累积误差，外部特性与详细模型一致
- 消除PWM调制环节使仿真步长提升十倍，大幅缩短计算时间且保持高精度



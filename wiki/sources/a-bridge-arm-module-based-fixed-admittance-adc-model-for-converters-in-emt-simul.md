---
title: "A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;6;10.1109/TPWRD.2025.3608898"
tags: ['adc', 'fixed-admittance']
created: "2026-04-13"
sources: ["EMT_Doc/01/Cao 等 - 2025 - A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation.pdf"]
---

# A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation

**作者**: 
**年份**: 2025
**来源**: `01/Cao 等 - 2025 - A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation.pdf`

## 摘要

—Electromagnetic transient (EMT) simulation models, especially converter models, face challenges in meeting the demand for precise and fast simulation of complex dynamics in modern distribution systems. Difﬁculty in achieving both high accuracy and efﬁciency simultaneously is a key issue in converter modeling, especially in real-time simulation. To address this issue, this paper proposes a parametric ﬁxed-admittance associated discrete circuit (ADC) converter model based on bridge arm modules (BAMs), with the aim of improving simulation precision and efﬁciency. The paper ﬁrst establishes a parametric ADC model of the BAM. An optimal parameter calculation approach is introduced to ensure high ﬁdelity through analysis of steady-state and transient char- acteristics. Furthermore, to mitigate 

## 核心贡献


- 提出基于桥臂模块的参数化固定导纳ADC模型，保持导纳矩阵恒定以提升计算效率
- 设计最优参数计算方法，确保模型稳态与暂态误差快速收敛至高保真水平
- 开发交叉重初始化方法修正状态切换误差，有效降低虚拟功率损耗且不增加计算负担


## 使用的方法


- [[关联离散电路法-adc|关联离散电路法(ADC)]]
- [[固定导纳建模|固定导纳建模]]
- [[后向欧拉法|后向欧拉法]]
- [[交叉重初始化-cri|交叉重初始化(CRI)]]
- [[诺顿等效|诺顿等效]]


## 涉及的模型


- [[桥臂模块-bam|桥臂模块(BAM)]]
- [[电力电子换流器|电力电子换流器]]
- [[l-c型adc模型|L/C型ADC模型]]
- [[开关电阻模型|开关电阻模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[换流器建模|换流器建模]]
- [[虚拟功率损耗|虚拟功率损耗]]
- [[状态切换误差修正|状态切换误差修正]]


## 主要发现


- 仿真与实验验证模型兼具高精度与高效率，在多种工况下均保持良好适用性
- 交叉重初始化方法有效消除切换初始误差并显著降低虚拟损耗，未牺牲计算速度
- 模型避免重复矩阵求逆，时间复杂度显著低于传统开关电阻模型，适合大规模系统



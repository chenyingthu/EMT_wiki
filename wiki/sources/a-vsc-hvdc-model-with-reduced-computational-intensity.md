---
title: "A VSC-HVDC Model with Reduced Computational Intensity"
type: source
year: 2012
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/pesgm.2012.6345135.pdf.pdf"]
---

# A VSC-HVDC Model with Reduced Computational Intensity

**年份**: 2012
**来源**: `04/pesgm.2012.6345135.pdf.pdf`

## 摘要

The paper presents a simplified voltage-source converter (VSC) model to reduce the computational intensity of simulating a power system with embedded converters. This simplified model is based on the concept of dynamic average- value modeling and provides the ability to generate either the full spectrum or the fundamental-frequency component of the VSC voltage. The model is validated against a detailed model of a voltage-source converter based high voltage direct current (VSC- HVDC) circuit and shows accurate matching during steady state and transient operation. Simulation and validation results are obtained using an electromagnetic transient simulation program (PSCAD/EMTDC). A significant reduction in terms of central processing unit (CPU) time consumption is also achieved with the propos

## 核心贡献


- 提出基于动态平均值建模的VSC简化模型，以受控源替代详细开关器件
- 模型支持灵活输出全频谱或基频分量，兼顾仿真精度与计算效率
- 建立交直流功率平衡的受控电流源模型，准确反映直流电压动态变化


## 使用的方法


- [[动态平均值建模|动态平均值建模]]
- [[矢量控制|矢量控制]]
- [[正弦脉宽调制|正弦脉宽调制]]
- [[受控源等效建模|受控源等效建模]]
- [[开关时刻插值算法|开关时刻插值算法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[vsc-model|VSC]]
- [[三电平npc换流器|三电平NPC换流器]]
- [[直流链路电容|直流链路电容]]
- [[换流变压器|换流变压器]]


## 相关主题


- [[仿真加速|仿真加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统级建模|系统级建模]]
- [[暂态特性分析|暂态特性分析]]
- [[柔性直流输电|柔性直流输电]]


## 主要发现


- 稳态与暂态工况下，简化模型与详细开关模型的电气波形高度吻合
- 对称与非对称故障条件下，模型能准确复现系统暂态动态响应特性
- 相比详细开关模型，该简化模型显著降低CPU耗时，大幅提升仿真效率



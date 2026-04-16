---
title: "A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM"
type: source
year: 2022
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/Wu 等 - 2017 - A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM.pdf"]
---

# A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM

**年份**: 2022
**来源**: `04/Wu 等 - 2017 - A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM.pdf`

## 摘要

In order to research the inrush problems in HVDC transmission projects, a new three-phase transformer model with hysteresis characteristics of PSCAD/EMTDC was presented, which derives from ideas of the transformer model considering hysteresis characteristics in ATP-EMTP, in which it consists of Type96 and BCTRAN. This model added an excitation branch considering hysteresis characteristics based on the classical model. The hysteresis characteristics can be described effectively when using experimental data obtained. The simulation results show that the model reflects excitation characteristics well, and parameters are readily available, it’s easy for users to use it in PSCAD/EMTDC. It also studied the differences of excitation characteristics simulated by the hysteresis loop and the hystere

## 核心贡献


- 提出基于PSCAD的考虑磁滞特性三相变压器自定义电磁暂态仿真模型
- 采用可变电感法构建闭环控制逻辑实现磁滞回线工作点实时跟踪与轨迹转换
- 利用分段线性插值法拟合主次磁滞回线簇仅需最大磁滞回线数据即可建模


## 使用的方法


- [[自定义建模-ud|自定义建模(UD)]]
- [[可变电感法|可变电感法]]
- [[分段线性插值法|分段线性插值法]]
- [[延时比较法|延时比较法]]
- [[闭环控制逻辑|闭环控制逻辑]]


## 涉及的模型


- [[三相变压器|三相变压器]]
- [[换流变压器|换流变压器]]
- [[非线性电感|非线性电感]]
- [[bctran模型|BCTRAN模型]]
- [[umec模型|UMEC模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[励磁涌流|励磁涌流]]
- [[磁滞特性建模|磁滞特性建模]]
- [[高压直流输电|高压直流输电]]
- [[谐波分析|谐波分析]]


## 主要发现


- 采用磁滞中线替代完整磁滞回线模拟时励磁涌流峰值在暂态过程中保持一致
- 完整磁滞回线对涌流稳态过程及高次谐波特性具有更显著的影响
- 所提模型仅需最大磁滞回线数据即可准确反映变压器铁心非线性励磁特性



---
title: "A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien"
type: source
year: 2022
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/Wang 等 - 2019 - A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien.pdf"]
---

# A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien

**年份**: 2022
**来源**: `03/Wang 等 - 2019 - A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien.pdf`

## 摘要

Common averaging methods were studied for modeling the grid-connected converter in new energy domain to balance the accuracy and efficiency in electromagnetic transient simulation. A piecewise generalized state space averaging (P-GSSA) method was proposed for converters with the large-scale new energy connected to grid. The piecewise technique was applied to generalized state space averaging (GSSA) model of the converters in this method, which combines the time slot with similar operating characteristic together to study. And multi time scale modeling was successfully achieved in the grid-connected converter of new energy domain. An example was simulated according to the P-GSSA model proposed in this paper, and the simulation results show that the model can adapt to the efficient simulatio

## 核心贡献


- 提出分段广义状态空间平均法，融合分段技术与广义状态空间平均模型
- 设计基于幅值预测的分段策略，合并动作特性一致的开关周期实现变步长
- 构建多时间尺度变流器模型，有效兼顾电磁暂态仿真精度与计算效率


## 使用的方法


- [[广义状态空间平均法|广义状态空间平均法]]
- [[分段状态空间平均法|分段状态空间平均法]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[变步长建模|变步长建模]]
- [[多时间尺度建模|多时间尺度建模]]


## 涉及的模型


- [[并网变流器|并网变流器]]
- [[三相pwm逆变器|三相PWM逆变器]]
- [[光伏系统|光伏系统]]
- [[变流器开关详细模型|变流器开关详细模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[新能源并网|新能源并网]]
- [[变流器建模|变流器建模]]
- [[高效仿真|高效仿真]]
- [[谐波分析|谐波分析]]


## 主要发现


- 分段模型能精确反映变流器电磁暂态特性，有效计及高频分量与谐波影响
- 仿真验证表明该模型在保持高精度的同时显著提升计算效率，优于传统平均法
- 自适应分段策略成功实现多时间尺度仿真，适用于大规模新能源并网场景



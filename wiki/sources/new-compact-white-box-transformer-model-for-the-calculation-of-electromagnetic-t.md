---
title: "New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;4;10.1109/TPWRD.2021.3119272"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients.pdf"]
---

# New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients

**作者**: 
**年份**: 2022
**来源**: `27&28/New Compact White-Box Transformer Model for the Calculation of Electromagnetic Transients.pdf`

## 摘要

—In a recent work, a successful power transformer white-box model for the calculation of electromagnetic transients has been presented. Although this model gives very satisfactory results, when applied to large transformers it requires a large number of auxiliary loops to model the damping. This can be problematic as it not only requires more computational effort, but the size of the input data may even preclude its use with ATP-EMTP and perhaps with other EMTP-based software that have limitations in this regard. In this work a new reduced model which enables its use with ATP-EMTP is presented. This model requires a much smaller number of circuit components than the original model, which allows the data size and simulation time to be substantially reduced without practically affecting the 

## 核心贡献


- 提出基于奇异值分解的低秩矩阵分解方法，大幅减少变压器白盒模型辅助回路数量
- 构建紧凑型变压器白盒等效电路，显著降低输入数据规模与仿真计算时间
- 突破ATP-EMTP软件元件数量限制，实现大型变压器高频暂态的高效精确仿真


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[部分分式展开|部分分式展开]]
- [[奇异值分解|奇异值分解]]
- [[低秩矩阵分解|低秩矩阵分解]]
- [[有限元法|有限元法]]
- [[白盒等效电路建模|白盒等效电路建模]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[白盒模型|白盒模型]]
- [[频变电感模型|频变电感模型]]
- [[涡流阻尼等效回路|涡流阻尼等效回路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[模型降阶|模型降阶]]
- [[阻尼建模|阻尼建模]]
- [[atp-emtp应用|ATP-EMTP应用]]
- [[变压器谐振分析|变压器谐振分析]]


## 主要发现


- 降阶模型频率响应与原全秩模型高度一致，验证了低秩分解不损失关键电磁特性
- 辅助回路数量大幅缩减，成功突破ATP-EMTP软件对大规模电路元件的输入限制
- 仿真计算时间与数据规模显著降低，满足大型变压器高频暂态快速精确分析需求



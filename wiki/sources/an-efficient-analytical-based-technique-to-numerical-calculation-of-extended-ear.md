---
title: "An efficient analytical based technique to numerical calculation of extended earth return impedance and admittance of overhead lines"
type: source
authors: ['Z. Liu']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107330. doi:10.1016/j.epsr.2021.107330"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/j.epsr.2021.107330.pdf.pdf"]
---

# An efficient analytical based technique to numerical calculation of extended earth return impedance and admittance of overhead lines

**作者**: Z. Liu
**年份**: 2021
**来源**: `06/j.epsr.2021.107330.pdf.pdf`

## 摘要

An efficient analytical based technique to numerical calculation of extended earth return impedance and admittance of overhead lines This paper describes an efficient numerical integration technique for the extended overhead line earth return impedance and admittance formula. In-appropriate handling of the infinite integral in the formula can lead to erroneous calculated earth-return parameters at extreme frequencies, and a significant increase in computational

## 核心贡献


- 提出基于解析的数值积分技术，实现扩展输电线路方程的合理离散化
- 建立系统化的截断点与离散步长选择流程，避免递归计算并提升效率
- 将无限积分分解为消息项与包络项，明确极端频率下参数计算误差来源


## 使用的方法


- [[数值积分|数值积分]]
- [[解析离散化|解析离散化]]
- [[无限积分截断|无限积分截断]]
- [[非递归迭代|非递归迭代]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[扩展传输线模型|扩展传输线模型]]
- [[大地返回阻抗与导纳|大地返回阻抗与导纳]]


## 相关主题


- [[电磁暂态建模|电磁暂态建模]]
- [[频率相关建模|频率相关建模]]
- [[大地返回参数计算|大地返回参数计算]]
- [[宽频仿真|宽频仿真]]


## 主要发现


- 相比等距离散法，新方法在减少离散点数量的同时保持大地返回参数计算精度
- 所提解析流程有效避免递归迭代，显著降低极端频率下的计算耗时与误差



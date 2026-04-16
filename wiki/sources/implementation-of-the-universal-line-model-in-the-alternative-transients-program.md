---
title: "Implementation of the universal line model in the alternative transients program✰"
type: source
authors: ['Felipe', 'O.S.', 'Zanon']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107311. doi:10.1016/j.epsr.2021.107311"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Zanon 等 - 2021 - Implementation of the universal line model in the alternative transients program✰.pdf"]
---

# Implementation of the universal line model in the alternative transients program✰

**作者**: Felipe, O.S., Zanon
**年份**: 2021
**来源**: `23/Zanon 等 - 2021 - Implementation of the universal line model in the alternative transients program✰.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Implementation of the universal line model in the alternative Felipe O.S. Zanon a,*, Osis E.S. Leal b, Alberto De Conti c a Graduate Program of Electrical Engineering (PPGEE), UFMG, Brazil b UTFPR – Federal University of Technology – Paran´a, Pato Branco, Brazil

## 核心贡献


- 在免费ATP平台中首次实现通用线路模型，填补高精度相域线路模型空白
- 结合MATLAB拟合与C语言编程，通过type-94组件实现ULM集成
- 验证了计及频率相关土壤参数时的地回路阻抗计算精度，提升暂态仿真准确性


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[相域建模|相域建模]]
- [[递归卷积|递归卷积]]
- [[诺顿等效|诺顿等效]]
- [[外部模型接口|外部模型接口]]


## 涉及的模型


- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[架空输电线路|架空输电线路]]
- [[频率相关土壤模型|频率相关土壤模型]]
- [[marti模型|Marti模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[地回路阻抗计算|地回路阻抗计算]]
- [[仿真软件集成|仿真软件集成]]


## 主要发现


- 与EMTP-RV对比验证表明，该实现方案在ATP中具备与商业软件一致的精度
- 计及频率相关土壤参数可精确计算地回路阻抗，有效改善架空线路暂态仿真结果
- 相比传统Marti模型，该相域ULM能准确处理强不对称线路及电缆暂态过程



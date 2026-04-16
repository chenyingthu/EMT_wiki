---
title: "Optimized high-frequency white-box transformer model for implementation in ATP-EMTP."
type: source
authors: ['Enrique', 'Esteban', 'Mombello']
year: 2023
journal: "Electric Power Systems Research, 213 (2022) 108709. doi:10.1016/j.epsr.2022.108709"
tags: ['transformer', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/30/Mombello 等 - 2022 - Optimized high-frequency white-box transformer model for implementation in ATP-EMTP..pdf"]
---

# Optimized high-frequency white-box transformer model for implementation in ATP-EMTP.

**作者**: Enrique, Esteban, Mombello
**年份**: 2023
**来源**: `30/Mombello 等 - 2022 - Optimized high-frequency white-box transformer model for implementation in ATP-EMTP..pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Optimized high-frequency white-box transformer model for Enrique Esteban Mombello a,*, Guillermo Guidi Venerdini a, Guillermo Andr´es Díaz Fl´orez b a CONICET, Universidad Nacional de San Juan, Instituto de Energia Electrica, San Juan, Argentina Although several high frequency white-box transformer models have been proposed in the literature, the

## 核心贡献


- 提出针对ATP的变压器高频白盒模型降阶与磁路解耦方法，突破耦合支路限制。
- 建立RL阻抗极点初值估计与低频拟合准则，优化频率相关参数表征精度。
- 设计六种ATP适配的简化等效电路变体，实现大规模白盒模型稳定运行。


## 使用的方法


- [[模型降阶|模型降阶]]
- [[磁路解耦|磁路解耦]]
- [[rl阻抗极点拟合|RL阻抗极点拟合]]
- [[频率相关建模|频率相关建模]]
- [[等效电路法|等效电路法]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[高频白盒模型|高频白盒模型]]
- [[绕组离散模型|绕组离散模型]]
- [[频率相关rl网络|频率相关RL网络]]


## 相关主题


- [[变压器暂态过电压|变压器暂态过电压]]
- [[高频电磁暂态仿真|高频电磁暂态仿真]]
- [[模型降阶与优化|模型降阶与优化]]
- [[atp-emtp应用|ATP-EMTP应用]]
- [[频率相关参数表征|频率相关参数表征]]


## 主要发现


- 六种降阶模型在CIGRE基准算例中验证，频响特性与全阶模型高度一致。
- 磁路解耦结合ATP变量扩容，成功实现超大规模变压器模型的稳定暂态仿真。
- 优化电阻网络布局避免额外节点，有效抑制了高频暂态计算中的数值振荡。



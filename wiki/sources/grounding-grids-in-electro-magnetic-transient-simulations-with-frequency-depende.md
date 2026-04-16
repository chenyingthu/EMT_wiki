---
title: "Grounding grids in electro-magnetic transient simulations with frequency-dependent equivalent circuit"
type: source
authors: ['Alessandro Manunza']
year: 2019
journal: "Electrical Power and Energy Systems, 116 (2019) 105546. doi:10.1016/j.ijepes.2019.105546"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/j.ijepes.2019.105546.pdf.pdf"]
---

# Grounding grids in electro-magnetic transient simulations with frequency-dependent equivalent circuit

**作者**: Alessandro Manunza
**年份**: 2019
**来源**: `19、20、21/EMT_task_21/j.ijepes.2019.105546.pdf.pdf`

## 摘要

Grounding grids in electro-magnetic transient simulations with frequency- The frequency behaviour of a grounding grid cannot be neglected in insulation coordination studies. This paper proposes a new approach, which consists of calculating the frequency behaviour of a grounding grid by means of a software which implements the electromagnetic theory, building a two-port component, whose internal ad- mittances are defined as rational functions in the Laplace domain, and finally using this two-port

## 核心贡献


- 提出结合电磁场计算与有理函数拟合的混合建模方法，精确表征接地网宽频阻抗特性
- 构建π型双端口等效电路，将频变导纳直接映射为ATP-EMTP内置无源支路
- 采用纯无源网络替代MODELS语言算法，大幅降低接地网暂态仿真计算耗时


## 使用的方法


- [[混合建模方法|混合建模方法]]
- [[arma算法|ARMA算法]]
- [[频变等效电路|频变等效电路]]
- [[双端口网络法|双端口网络法]]
- [[atp-emtp时域仿真|ATP-EMTP时域仿真]]


## 涉及的模型


- [[接地网|接地网]]
- [[变压器|变压器]]
- [[避雷器|避雷器]]
- [[π型等效电路|π型等效电路]]
- [[频变导纳支路|频变导纳支路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[绝缘配合|绝缘配合]]
- [[快速暂态分析|快速暂态分析]]
- [[接地网等值|接地网等值]]


## 主要发现


- 接地网阻抗在20Hz至2MHz频段呈显著频变特性，传统工频电阻模型存在较大误差
- 所提π型无源网络在ATP-EMTP中仿真稳定，计算效率显著优于传统MODELS方法
- 模型兼容任意土壤参数与网格拓扑，能准确复现雷击下接地网电位分布与行波传播



---
title: "27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems"
type: source
authors: ['未知']
year: 2006
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems.pdf"]
---

# 27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems

**作者**: 
**年份**: 2006
**来源**: `27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems.pdf`

## 摘要

—As power electronics are increasingly used in power- electric networks, there is an interest in the creation of time-do- main simulation techniques that can model the diversity of the in- tegrative power-electric and electronic system while achieving high accuracy and computational speed. In the proposed method, gen- eration of electric network equivalents (GENE), this is supported through the nested structure of the overall simulation process. One or multiple parent simulations, in which the unknown voltages are calculated using nodal analysis, launch multiple child simulations concerned with diakoptic subdivisions of the system under study. The interfaces for information exchange between parent and child levels are designed to provide encapsulation. This makes the sub- divisions appeari

## 核心贡献



- 提出GENE嵌套父子架构，实现非迭代同步求解以提升计算效率
- 基于撕裂法与诺顿等值构建封装接口，兼容节点分析并支持多方法协同
- 结合稀疏矩阵与分段线性开关预计算，实现电力电子快速非迭代仿真


## 使用的方法



- [[节点分析法|节点分析法]]
- [[撕裂法|撕裂法]]
- [[状态空间法|状态空间法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]
- [[分段线性近似|分段线性近似]]
- [[伴随模型法|伴随模型法]]


## 涉及的模型



- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[直流输电线路|直流输电线路]]
- [[谐波滤波器|谐波滤波器]]
- [[电力电子开关|电力电子开关]]


## 相关主题



- [[实时仿真|实时仿真]]
- [[协同仿真|协同仿真]]
- [[并行计算|并行计算]]
- [[vsc-hvdc|VSC-HVDC]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络等值|网络等值]]


## 主要发现



- 在CIGRE HVDC基准模型验证，实现超实时精度的暂态仿真
- 嵌套结构实现接口封装，支持局部异构求解器且无需界面迭代补偿
- 分段线性开关模型结合预计算大幅降低开关事件计算负担



---
title: "FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent"
type: source
authors: ['Fahimeh Hajizadeh']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112400. doi:10.1016/j.epsr.2025.112400"
tags: ['fpga', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf"]
---

# FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent

**作者**: Fahimeh Hajizadeh
**年份**: 2025
**来源**: `19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf`

## 摘要

FPGA-based simulation of grid-tied converters using frequency-dependent a Dept. electrical engineering, Polytechnique Montréal, Montreal, Canada b Hydro-Québec Research Institute (IREQ), Varennes, Canada c MOTCE Laboratory, DGIGL, Polytechnique Montréal, Canada This paper introduces a real-time simulation framework for grid-tied converters, implemented on ﬁeld-

## 核心贡献


- 提出基于状态空间方程的FDNE集成方法，优化FPGA矩阵计算速度与数值稳定性
- 构建基于HLS与定制浮点算术的FPGA框架，实现计算精度与硬件资源的最优平衡
- 实现亚微秒级延迟的超实时仿真，显著降低电磁暂态仿真计算耗时


## 使用的方法


- [[频率相关网络等值|频率相关网络等值]]
- [[状态空间方程|状态空间方程]]
- [[向后欧拉法|向后欧拉法]]
- [[高层次综合|高层次综合]]
- [[定制浮点运算|定制浮点运算]]
- [[有理函数拟合|有理函数拟合]]


## 涉及的模型


- [[statcom|STATCOM]]
- [[vsc-model|VSC]]
- [[并网变流器|并网变流器]]
- [[输电线路|输电线路]]
- [[负荷|负荷]]
- [[fdne-model|FDNE]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[超实时仿真|超实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[硬件在环|硬件在环]]
- [[资源优化|资源优化]]


## 主要发现


- 仿真波形与EMTP参考模型高度吻合，验证了FDNE集成方法的高保真度
- 在Alveo U280上实现亚微秒级延迟与超实时运行，满足快速暂态分析需求
- 定制浮点算术有效降低FPGA逻辑资源占用，同时维持多精度下的计算准确性



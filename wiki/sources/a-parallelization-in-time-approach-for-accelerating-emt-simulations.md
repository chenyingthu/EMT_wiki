---
title: "A parallelization-in-time approach for accelerating EMT simulations"
type: source
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107346. doi:10.1016/j.epsr.2021.107346"
created: "2026-04-13"
sources: ["EMT_Doc/03/j.epsr.2021.107346.pdf.pdf"]
---

# A parallelization-in-time approach for accelerating EMT simulations

**年份**: 2021
**来源**: `03/j.epsr.2021.107346.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A parallelization-in-time approach for accelerating EMT simulations Ming Cai a, Jean Mahseredjian a,*, Ilhan Kocar a, Xiaopeng Fu b, Aboutaleb Haddadi a a Polytechnique Montreal, Montreal, QC H3C 3A7, Canada b Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin, China

## 核心贡献


- 提出时间并行方程分组与重排序技术，实现电磁暂态仿真加速
- 将PEGR理论从状态空间扩展至改进增广节点分析(MANA)框架
- 结合KLU稀疏求解器与OpenMP多线程，实现网络矩阵高效并行求解


## 使用的方法


- [[时间并行方程分组与重排序-pegr|时间并行方程分组与重排序(PEGR)]]
- [[改进增广节点分析-mana|改进增广节点分析(MANA)]]
- [[klu稀疏线性求解器|KLU稀疏线性求解器]]
- [[openmp多线程并行|OpenMP多线程并行]]
- [[lu分解|LU分解]]


## 涉及的模型


- [[多相π型线路模型|多相π型线路模型]]
- [[集中参数rlc元件|集中参数RLC元件]]
- [[电力系统网络|电力系统网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[时间并行计算|时间并行计算]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[离线仿真加速|离线仿真加速]]
- [[网络方程求解|网络方程求解]]


## 主要发现


- 利用PEGR技术挖掘求解过程内在独立性，显著减少前代回代计算步数
- 在电力系统基准算例中验证了该方法在保持精度的同时大幅提升仿真速度
- 算法可自动适配处理器数量，有效处理任意仿真步数与网络拓扑变化



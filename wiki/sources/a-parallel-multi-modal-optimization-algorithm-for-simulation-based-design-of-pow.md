---
title: "A Parallel Multi-Modal Optimization Algorithm for Simulation-Based Design of Power Systems"
type: source
year: 2015
journal: "IEEE Transactions on Magnetics"
created: "2026-04-13"
sources: ["EMT_Doc/03/TPWRD.2015.2410172.pdf.pdf"]
---

# A Parallel Multi-Modal Optimization Algorithm for Simulation-Based Design of Power Systems

**年份**: 2015
**来源**: `03/TPWRD.2015.2410172.pdf.pdf`

## 摘要

— This paper proposes a parallel multi-modal optimization algorithm that is combined with electromagnetic transient (EMT) simulation in a platform that unifies the set-up, test, and execution of optimal designs for power systems. The algorithm speeds up the design of power systems as its computations can be executed independently on a highly parallelized environment. Additional speed-up is achieved by using a surrogate model to estimate the objective function in regions of suspected local optima. The estimated functions can be used in the subsequent stages of post-optimization studies such as sensitivity analyses. Comparative studies in terms of computation time are conducted against sequential execution of the proposed algorithm. The optimal design of a VSC-HVDC transmission is described 

## 核心贡献


- 提出结合电磁暂态仿真的并行多模态优化算法实现电力系统黑盒目标函数高效寻优
- 引入三次样条代理模型估计局部极值区域目标函数大幅减少电磁暂态仿真调用次数
- 算法支持局部区域独立并行计算显著缩短设计周期并直接生成灵敏度分析数据


## 使用的方法


- [[并行多模态优化算法|并行多模态优化算法]]
- [[代理模型-三次样条插值|代理模型(三次样条插值)]]
- [[黑盒优化|黑盒优化]]
- [[并行计算|并行计算]]
- [[基于仿真的优化设计|基于仿真的优化设计]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[电磁暂态-emt-仿真模型|电磁暂态(EMT)仿真模型]]


## 相关主题


- [[基于仿真的优化设计|基于仿真的优化设计]]
- [[多模态优化|多模态优化]]
- [[并行计算|并行计算]]
- [[灵敏度分析|灵敏度分析]]
- [[vsc-model|VSC]]


## 主要发现


- 并行执行相比串行计算显著缩短优化耗时验证算法在大规模计算环境下的加速效果
- 三次样条代理模型能高精度逼近局部极值有效减少电磁暂态仿真调用次数
- 成功应用于VSC-HVDC设计实现快速动态响应并有效抑制直流电压纹波与功率误差



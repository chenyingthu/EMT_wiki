---
title: "Mitigation of Subsynchronous Interactions in Hybrid AC/DC Grid With Renewable Energy Using Faster-Than-Real-Time Dynamic Simulation"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Systems;2021;36;1;10.1109/TPWRS.2020.2984732"
tags: ['real-time', 'renewable']
created: "2026-04-13"
sources: ["EMT_Doc/26/Cao 等 - 2021 - Mitigation of Subsynchronous Interactions in Hybrid ACDC Grid With Renewable Energy Using Faster-Th.pdf"]
---

# Mitigation of Subsynchronous Interactions in Hybrid AC/DC Grid With Renewable Energy Using Faster-Than-Real-Time Dynamic Simulation

**作者**: 
**年份**: 2021
**来源**: `26/Cao 等 - 2021 - Mitigation of Subsynchronous Interactions in Hybrid ACDC Grid With Renewable Energy Using Faster-Th.pdf`

## 摘要

—Transmission line capacity enhancement by series compensation is commonly used in power systems, which conse- quently faces potential subsynchronous interaction (SSI). In this work, faster-than-real-time (FTRT) simulation based on the ﬁeld- programmable gate arrays is proposed to mitigate the disastrous SSI in a hybrid AC/DC grid integrated with wind farms. Dynamic simulation is applied to the AC system to gain a high speedup over real-time, and a detailed multi-mass model is speciﬁcally introduced to the synchronous generator to show the electrical- mechanical interaction. Meanwhile, the DC grid undergoes elec- tromagnetic transient simulation to reﬂect the impact of power converters’ control on the overall grid, and consequently, the EMT- dynamic co-simulation running concurrently due t

## 核心贡献


- 提出基于FPGA的超实时仿真架构，实现交直流混合电网并行加速计算
- 构建同步发电机五质量块轴系模型，精确刻画次同步相互作用机电耦合
- 设计功率电压接口实现EMT与动态仿真并发，兼顾直流控制与交流暂态


## 使用的方法


- [[超实时仿真-ftrt|超实时仿真(FTRT)]]
- [[fpga硬件并行计算|FPGA硬件并行计算]]
- [[emt-动态混合仿真|EMT-动态混合仿真]]
- [[功率-电压接口技术|功率-电压接口技术]]
- [[微分代数方程-dae-求解|微分代数方程(DAE)求解]]


## 涉及的模型


- [[同步发电机九阶模型|同步发电机九阶模型]]
- [[五质量块扭振轴系模型|五质量块扭振轴系模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[风电场|风电场]]
- [[励磁控制系统-avr-pss|励磁控制系统(AVR/PSS)]]


## 相关主题


- [[次同步相互作用-ssi-抑制|次同步相互作用(SSI)抑制]]
- [[交直流混合电网|交直流混合电网]]
- [[超实时仿真|超实时仿真]]
- [[fpga并行加速|FPGA并行加速]]
- [[机电暂态协同仿真|机电暂态协同仿真]]
- [[暂态稳定分析|暂态稳定分析]]


## 主要发现


- 超实时平台可在故障后提前生成精确潮流调整策略，有效抑制次同步振荡
- 五质量块模型成功复现轴系扭振放大现象，验证了机电交互仿真准确性
- 混合仿真结果与Matlab离线工具高度一致，且具备显著超实时加速比



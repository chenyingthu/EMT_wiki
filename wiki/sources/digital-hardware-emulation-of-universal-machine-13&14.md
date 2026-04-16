---
title: "Digital Hardware Emulation of Universal Machine"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/pesgm.2012.6343925.pdf.pdf"]
---

# Digital Hardware Emulation of Universal Machine

**作者**: 
**年份**: 2011
**来源**: `13&14/files/pesgm.2012.6343925.pdf.pdf`

## 摘要

—Real-time electromagnetic transient simulation plays an important role in the planning, design, and operation of power systems. Inclusion of accurate and complicated models, such as the universal machine (UM) model and the universal line model (ULM), requires signiﬁcant computational resources. This paper proposes a digital hardware emulation of the UM and the ULM for real-time electromagnetic transient simulation. It features ac- curate ﬂoating-point data representation, paralleled implementa- tion, and fully pipelined arithmetic processing. The hardware is based on advanced ﬁeld-programmable gate array (FPGA) using VHDL. A power system transient case study is simulated in real time to validate the design. On a 130-MHz input clock frequency to the FPGA, the achieved execution times for U

## 核心贡献


- 提出基于FPGA的通用机电与线路模型数字硬件仿真架构
- 采用全并行深度流水线与浮点运算架构大幅提升计算速度
- 运用补偿法迭代求解电机方程并集成多类元件实现完整仿真


## 使用的方法


- [[补偿法|补偿法]]
- [[全并行计算|全并行计算]]
- [[深度流水线架构|深度流水线架构]]
- [[浮点运算|浮点运算]]
- [[vhdl硬件描述|VHDL硬件描述]]


## 涉及的模型


- [[通用机电模型-um|通用机电模型(UM)]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[同步电机|同步电机]]
- [[感应电机|感应电机]]
- [[输电线路|输电线路]]
- [[地下电缆|地下电缆]]
- [[集中参数rlc|集中参数RLC]]


## 相关主题


- [[实时电磁暂态仿真|实时电磁暂态仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[fpga并行计算|FPGA并行计算]]
- [[频变线路建模|频变线路建模]]
- [[电力系统数字仿真|电力系统数字仿真]]


## 主要发现


- 130MHz时钟下UM与ULM单步执行时间仅2.5μs与1.42μs
- 实时波形与EMTP-RV离线结果高度吻合验证了硬件仿真精度



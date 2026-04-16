---
title: "Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Open Access Journal of Power and Energy;2023;10; ;10.1109/OAJPE.2022.3217601"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids.pdf"]
---

# Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids

**作者**: 
**年份**: 2023
**来源**: `19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids.pdf`

## 摘要

Enhanced environmental standards are leading to an increasing proportion of microgrids (MGs) being integrated with renewable energy resources in modern power systems, which brings new challenges to simulate such a complex system. In this work, comprehensive modeling of a grid of microgrids for faster-than-real-time (FTRT) emulation is proposed, which can be utilized in the energy control center for contingencies analysis and dynamic security assessment. Electromagnetic transient (EMT) modeling is applied to the microgrid in order to reﬂect the detailed device processes of the converter and renewable energy sources, while the AC grid utilizes the transient stability modeling to reduce the computational burden and obtain a high acceleration value over real-time execution. Consequently, a dyn

## 核心贡献


- 提出微电网EMT与主网暂态稳定混合建模架构，实现多尺度仿真共存。
- 设计动态电压注入接口策略，显著降低跨域数据通信开销与硬件资源占用。
- 基于FPGA并行计算架构实现超实时硬件仿真，系统加速比达51倍。


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[暂态稳定仿真|暂态稳定仿真]]
- [[动态电压注入接口|动态电压注入接口]]
- [[fpga并行计算|FPGA并行计算]]
- [[超实时仿真|超实时仿真]]


## 涉及的模型


- [[微电网|微电网]]
- [[光伏阵列|光伏阵列]]
- [[双馈感应发电机|双馈感应发电机]]
- [[电池储能系统|电池储能系统]]
- [[交流主网|交流主网]]
- [[电力电子变流器|电力电子变流器]]


## 相关主题


- [[超实时仿真|超实时仿真]]
- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[动态安全评估|动态安全评估]]
- [[硬件在环仿真|硬件在环仿真]]
- [[微电网群建模|微电网群建模]]


## 主要发现


- 三组案例仿真结果与Matlab/Simulink离线工具高度吻合，验证模型精度。
- FPGA平台实现51倍超实时加速，满足控制中心动态安全评估与故障分析需求。
- 动态注入接口有效隔离双仿真域，大幅降低通信延迟与硬件逻辑资源消耗。



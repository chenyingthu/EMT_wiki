---
title: "Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of Large-Scale Integrated AC/DC Grid"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Systems;2023;38;1;10.1109/TPWRS.2022.3161561"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of.pdf"]
---

# Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of Large-Scale Integrated AC/DC Grid

**作者**: 
**年份**: 2022
**来源**: `19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of.pdf`

## 摘要

—The rapid expansion of modern power systems has broughtatremendouscomputationalchallengetodynamicsecurity analysis (DSA) tools which consequently need to process extensive contingencies. In this work, hardware emulation is investigated to acceleratetheDSAsolutionofalarge-scaleAC/DCsystemdeployed on the ﬁeld-programmable gate arrays (FPGAs) faster-than-real- time (FTRT) execution. Electromagnetic transient (EMT) model- ing of the DC grid is conducted since the fast converter dynamics require a small time-step for accuracy; in contrast, the transient stability (TS) simulation is applicable to the AC grid which tolerates a much larger step size. To coordinate the 2 different types of simu- lation, an interface based on dynamic voltage injection is proposed to integrate the AC and DC grids, i

## 核心贡献


- 提出基于多FPGA的超实时硬件仿真平台用于大规模交直流电网动态安全分析
- 设计动态电压注入接口协调交直流混合仿真保持导纳矩阵恒定以降低延迟
- 采用显式RK4积分与九阶同步机模型针对FPGA并行架构优化求解效率


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[多fpga并行计算|多FPGA并行计算]]
- [[动态电压注入接口|动态电压注入接口]]
- [[显式四阶龙格库塔法|显式四阶龙格库塔法]]
- [[混合仿真|混合仿真]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[九阶同步发电机模型|九阶同步发电机模型]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[多端直流电网|多端直流电网]]
- [[换流器|换流器]]


## 相关主题


- [[动态安全分析|动态安全分析]]
- [[超实时仿真|超实时仿真]]
- [[硬件仿真|硬件仿真]]
- [[并行计算|并行计算]]
- [[交直流混合电网|交直流混合电网]]
- [[故障预想分析|故障预想分析]]


## 主要发现


- 平台实现交直流混合电网超实时加速比超208倍单系统加速比超277倍
- 成功完成超5500种故障预想分析安全指标与商业软件DSATools高度吻合
- 动态电压注入接口有效维持导纳矩阵恒定显著降低FPGA资源占用与延迟



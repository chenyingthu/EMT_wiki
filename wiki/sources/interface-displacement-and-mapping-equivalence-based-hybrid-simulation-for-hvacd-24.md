---
title: "Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3017084"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/24/Zhu 等 - 2021 - Interface Displacement and Dynamic Phasor Mapping Equivalence Based Hybrid Simulation for HVACDC Po.pdf"]
---

# Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids

**作者**: 
**年份**: 2020
**来源**: `24/Zhu 等 - 2021 - Interface Displacement and Dynamic Phasor Mapping Equivalence Based Hybrid Simulation for HVACDC Po.pdf`

## 摘要

—In the electromagnetic transient (EMT) and transient stability (TS) hybrid simulation, the entire power system is artificially split into two sub-grids, and sub-grids interact with each other via an interface. Thus interface distortions emerge, including latency and errors. The influence of interface latency is quantitated based on a demo circuit containing delayed interaction. Moreover, the principles of improving hybrid simulation interface accuracy are concluded. Inspired by the principles, a novel interface displacement (ID) and dynamic phasor mapping equivalence (DP-ME) interface scheme is proposed. The scheme makes sub-grids at opposite sides of an interface loosely coupled and avoids interface variable form conversion by applying two techniques. 1) Displacement of the partition int

## 核心贡献


- 提出接口位移技术，将分区界面移至控制回路内部，利用内置惯性实现松耦合
- 构建动态相量映射等效模型，直接计算注入功率，避免变量形式转换延迟
- 基于Lambert W函数量化接口延迟对混合仿真精度与稳定性的影响规律


## 使用的方法


- [[动态相量法|动态相量法]]
- [[接口位移技术|接口位移技术]]
- [[lambert-w函数|Lambert W函数]]
- [[混合仿真接口技术|混合仿真接口技术]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[交流系统等效电源|交流系统等效电源]]
- [[受控电流源|受控电流源]]
- [[交直流混合电网|交直流混合电网]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[接口延迟|接口延迟]]
- [[动态相量|动态相量]]
- [[交直流电网|交直流电网]]
- [[网络分区|网络分区]]


## 主要发现


- 接口位移与映射等效方案消除变量转换延迟，显著提升混合仿真接口精度
- 实际交直流电网测试表明，该方案结果与全电磁暂态仿真高度吻合
- 延迟导致系统特征根偏移，利用内置惯性松耦合可有效抑制接口误差



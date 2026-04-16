---
title: "Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3017084"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/24/TPWRD.2020.3017084.pdf.pdf"]
---

# Interface Displacement and Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids

**作者**: 
**年份**: 2020
**来源**: `24/TPWRD.2020.3017084.pdf.pdf`

## 摘要

—In the electromagnetic transient (EMT) and transient stability (TS) hybrid simulation, the entire power system is artificially split into two sub-grids, and sub-grids interact with each other via an interface. Thus interface distortions emerge, including latency and errors. The influence of interface latency is quantitated based on a demo circuit containing delayed interaction. Moreover, the principles of improving hybrid simulation interface accuracy are concluded. Inspired by the principles, a novel interface displacement (ID) and dynamic phasor mapping equivalence (DP-ME) interface scheme is proposed. The scheme makes sub-grids at opposite sides of an interface loosely coupled and avoids interface variable form conversion by applying two techniques. 1) Displacement of the partition int

## 核心贡献


- 提出接口位移技术将分区边界移至控制回路内部利用内置惯性实现松耦合
- 构建动态相量映射等效模型直接计算注入功率避免变量形式转换引入的延迟
- 基于Lambert W函数量化延迟影响机理推导提升混合仿真精度的理论原则


## 使用的方法


- [[动态相量法|动态相量法]]
- [[混合仿真|混合仿真]]
- [[接口位移技术|接口位移技术]]
- [[lambert-w函数分析|Lambert W函数分析]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[换流器|换流器]]
- [[交流系统等值模型|交流系统等值模型]]
- [[可控电流源|可控电流源]]
- [[交直流电网|交直流电网]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[接口延迟|接口延迟]]
- [[交直流电网|交直流电网]]
- [[动态相量映射|动态相量映射]]
- [[网络分区|网络分区]]


## 主要发现


- 接口位移结合动态相量映射方案有效消除转换延迟显著提升混合仿真接口精度
- 实际交直流电网测试表明该方案结果与全电磁暂态仿真高度吻合验证了有效性
- 量化分析证实接口延迟引发特征根偏移利用内置惯性可大幅降低对稳定性的影响



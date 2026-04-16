---
title: "Functional Mock-up Interface Based Approach for Parallel and Multistep Simulation of Electromagnetic Transients"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2018.2860586"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRD.2018.2860586.pdf.pdf"]
---

# Functional Mock-up Interface Based Approach for Parallel and Multistep Simulation of Electromagnetic Transients

**作者**: 
**年份**: 2018
**来源**: `19、20、21/EMT_task_20/TPWRD.2018.2860586.pdf.pdf`

## 摘要

—This paper presents a new simulation approach based on the Functional Mock-up Interface (FMI) standard for parallel and multistep simulation of electromagnetic transients (EMTs) in power grids with computationally expensive control systems. The control systems are represented by slave subsystems which are decoupled in memory from the power network and encapsulated in Functional Mock-up Units (FMUs). The simulation modes are either asynchronous or synchronous. In the asynchronous mode, the subsystems are simulated in parallel, whereas in the synchronous mode the simulation of each subsystem is executed in a sequential multistep environment. Considerable computation time gains in both modes have been observed in power system protection studies on large-scale networks with accuracy properly 

## 核心贡献


- 提出基于FMI 2.0的协同仿真架构，实现电网与控制系统内存级完全解耦
- 设计异步并行与同步多步双模式，支持多核分布式计算与子系统变步长求解
- 开发EMTP全兼容接口，利用共享内存总线与信号量机制实现主从高效同步


## 使用的方法


- [[fmi协同仿真|FMI协同仿真]]
- [[主从架构|主从架构]]
- [[异步并行计算|异步并行计算]]
- [[同步多步求解|同步多步求解]]
- [[内存解耦技术|内存解耦技术]]
- [[共享内存通信|共享内存通信]]
- [[信号量同步|信号量同步]]


## 涉及的模型


- [[控制系统模型|控制系统模型]]
- [[电力网络模型|电力网络模型]]
- [[继电保护系统|继电保护系统]]
- [[fmu封装模型|FMU封装模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[协同仿真|协同仿真]]
- [[多步长仿真|多步长仿真]]
- [[大规模电网仿真|大规模电网仿真]]
- [[离线仿真|离线仿真]]


## 主要发现


- 异步并行与同步多步模式均显著缩短计算耗时，大幅提升大规模电网仿真效率
- 在继电保护研究中验证了数值精度，仿真结果与传统全耦合方法保持高度一致
- 内存解耦架构有效消除人工干预，显著提升含复杂控制系统电网的仿真可扩展性



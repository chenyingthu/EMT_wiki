---
title: "Real-Time FPGA-RTDS Co-Simulator for Power Systems"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Access; ;PP;99;10.1109/ACCESS.2018.2862893"
tags: ['real-time', 'fpga', 'rtds']
created: "2026-04-13"
sources: ["EMT_Doc/32/ACCESS.2018.2862893.pdf.pdf"]
---

# Real-Time FPGA-RTDS Co-Simulator for Power Systems

**作者**: 
**年份**: 2018
**来源**: `32/ACCESS.2018.2862893.pdf.pdf`

## 摘要

—This paper proposes a co-simulation platform using Field-Programmable Gate Array (FPGA) and Real-Time Digital Simulator (RTDS) for the simulation of large power systems. It combines the advantages of high computational power from FPGA and better modelling flexibility from RTDS together. The FPGA therefore acts as an efficient and economical extension to RTDS especially when simulating large AC systems. One of the significant advantages of the proposed co-simulator is that it avoids the potential interface error existing in the conventional approach of interfacing Transient Stability (TS) program with Electromagnetic Transient (EMT) programs. Two key aspects of the proposed co-simulator are discussed: 1) the interface design between FPGA and RTDS and 2) the hardware implementation and expa

## 核心贡献


- 提出FPGA与RTDS纯电磁暂态联合仿真架构，避免传统机电电磁混合接口误差。
- 设计FPGA与RTDS间高效数据交互接口，实现大规模交流电网实时并行扩展。
- 在FPGA实现同步机通用模型及控制系统硬件并行化，兼顾仿真规模与精度。


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[相模变换|相模变换]]
- [[硬件并行计算|硬件并行计算]]
- [[联合仿真接口设计|联合仿真接口设计]]


## 涉及的模型


- [[同步发电机|同步发电机]]
- [[输电线路|输电线路]]
- [[励磁系统|励磁系统]]
- [[调速系统|调速系统]]
- [[无源元件|无源元件]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[联合仿真|联合仿真]]
- [[硬件加速|硬件加速]]
- [[大规模电网仿真|大规模电网仿真]]
- [[fpga实现|FPGA实现]]


## 主要发现


- 两区域四机系统仿真表明联合平台与全RTDS仿真结果高度一致，精度可靠。
- 141节点大规模电网在FPGA中成功实时运行，验证了平台的高扩展能力。
- 纯电磁暂态联合架构有效消除了传统混合仿真的接口误差，提升动态响应精度。



---
title: "Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Chen 等 - 2023 - Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen.pdf"]
---

# Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen

**作者**: CNKI
**年份**: 2023
**来源**: `19、20、21/EMT_task_19/Chen 等 - 2023 - Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen.pdf`

## 摘要

：To achieve the large-scale real-time simulation of doubly fed wind generator (DFIG), we designed a DFIG digital image intelligent property (IP) core based on field programmable gate array (FPGA), and proposed a virtual capacitance equivalent method for decoupling the “T-shaped” equivalent circuit of the stator and rotor of the asynchronous machine. Based on this, a parallel algorithm for each component in DFIG was proposed. Finally, DFIG-IP was constructed. Through pipeline optimization design, we performed the experimental verification of the calculation accuracy and speed of DFIG-IP based on FPGA under four working conditions. The research results show that the proposed method can be employed to reduce the FPGA resource required by DFIG asynchronous machine solution module about 77%. Th

## 核心贡献


- 提出虚拟电容等效法解耦异步机定转子T型电路，避免每时步矩阵求逆运算
- 设计基于FPGA的DFIG数字镜像IP核，实现内部组件级并行与流水线优化
- 开发纯Verilog编制的DFIG-IP，实现超实时仿真并大幅降低硬件资源消耗


## 使用的方法


- [[虚拟电容等效法|虚拟电容等效法]]
- [[并行计算|并行计算]]
- [[流水线优化|流水线优化]]
- [[中点积分法|中点积分法]]
- [[verilog硬件描述|Verilog硬件描述]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[异步电机|异步电机]]
- [[t型等效电路|T型等效电路]]
- [[数字镜像ip核|数字镜像IP核]]


## 相关主题


- [[超实时仿真|超实时仿真]]
- [[并行计算|并行计算]]
- [[fpga加速|FPGA加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数字孪生|数字孪生]]
- [[风电场建模|风电场建模]]


## 主要发现


- 所提方法使DFIG异步机求解模块所需FPGA资源降低约77%
- DFIG-IP在500MHz时钟下超实时加速度比达27.8，单核资源占用低于20%
- 四种工况验证表明该方法满足DFIG并网系统实时仿真的精度与速度要求



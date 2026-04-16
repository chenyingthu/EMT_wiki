---
title: "Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study"
type: source
authors: ['未知']
year: 2016
journal: "IEEE Transactions on Power Systems;2016;31;4;10.1109/TPWRS.2015.2479588"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Huang和Vittal - 2016 - Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study.pdf"]
---

# Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study

**作者**: 
**年份**: 2016
**来源**: `09/Huang和Vittal - 2016 - Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study.pdf`

## 摘要

—This paper deals with the development of a new electromagnetic transient (EMT)-transient stability (TS) hybrid simulation platform and its application to a detailed fault-induced delayed voltage recovery (FIDVR) study on the WECC system. A new EMT-TS hybrid simulation platform, which integrates PSCAD/EMTDC and the open source power system simulation software InterPSS has been developed. A combined interaction protocol with an automatic protocol switching control scheme is proposed. A multi-port three-phase Thévenin equivalent is developed for representing an external network in an EMT sim- ulator. Correspondingly, the external network is represented in three-sequence, and a three-sequence TS simulation algorithm is developed. These techniques allow simulation of unsymmetrical faults withi

## 核心贡献


- 构建基于PSCAD与InterPSS的解耦混合仿真平台，实现跨软件高效数据交互
- 设计串并联自动切换交互协议，兼顾暂态过程精度与稳态过程仿真速度
- 提出多端口三相戴维南等值与三序算法，突破边界三相平衡限制


## 使用的方法


- [[emt-ts混合仿真|EMT-TS混合仿真]]
- [[自动切换交互协议|自动切换交互协议]]
- [[多端口三相戴维南等值|多端口三相戴维南等值]]
- [[三序暂态稳定算法|三序暂态稳定算法]]
- [[socket通信框架|Socket通信框架]]


## 涉及的模型


- [[单相感应电机|单相感应电机]]
- [[空调压缩机负荷|空调压缩机负荷]]
- [[输电网络|输电网络]]
- [[ieee-9节点系统|IEEE 9节点系统]]
- [[wecc大电网模型|WECC大电网模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[故障诱发延迟电压恢复|故障诱发延迟电压恢复]]
- [[不对称故障仿真|不对称故障仿真]]
- [[电机堵转传播|电机堵转传播]]
- [[故障初相角分析|故障初相角分析]]


## 主要发现


- 单相接地故障可引发FIDVR，故障相空调电机率先堵转并向非故障相蔓延
- 在多种负荷比例组合下均观测到类似的电压延迟恢复与电机堵转传播现象
- 故障施加时刻的初相角对FIDVR事件的发生概率及严重程度具有显著影响



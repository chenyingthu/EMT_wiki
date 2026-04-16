---
title: "Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model"
type: source
authors: ['IEEE']
year: 2019
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/22/Liu 等 - 2020 - Hybrid EMT-TS Simulation Strategies to Study High Bandwidth MMC-Based HVdc Systems.pdf"]
---

# Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model

**作者**: IEEE
**年份**: 2019
**来源**: `22/Liu 等 - 2020 - Hybrid EMT-TS Simulation Strategies to Study High Bandwidth MMC-Based HVdc Systems.pdf`

## 摘要

—Modular multilevel converters (MMCs) are widely used in the design of modern high-voltage direct current (HVdc) transmission system. High-fidelity dynamic models of MMCs- based HVdc system require small simulation time step and can be accurately modeled in electro-magnetic transient (EMT) simulation programs. The EMT program exhibits slow simulation speed and limitation on the size of the model and brings certain challenges to test the high-fidelity HVdc model in system-level simulations. This paper presents the design and implementation of a hybrid simulation framework, which enables the co-simulation of the EMT model of Atlanta-Orlando HVdc line and the transient stability (TS) model of the entire Eastern Interconnection system. This paper also introduces the implementation of two high-

## 核心贡献


- 提出基于无功注入与电压灵敏度的缓冲区划分方法，精准界定EMT仿真边界
- 构建首个将高保真MMC-HVDC模型与东部互联电网全模型联合仿真的混合框架
- 实现PSCAD与PSS/E跨平台接口集成，支持微秒级与毫秒级多速率协同仿真


## 使用的方法


- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[无功注入法|无功注入法]]
- [[电压灵敏度分析|电压灵敏度分析]]
- [[动态相量接口|动态相量接口]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[东部互联电网|东部互联电网]]
- [[cdc6t直流模型|CDC6T直流模型]]


## 相关主题


- [[emt-ts混合仿真|EMT-TS混合仿真]]
- [[mmc-model|MMC]]
- [[缓冲区划分|缓冲区划分]]
- [[大规模电网仿真|大规模电网仿真]]
- [[暂态稳定分析|暂态稳定分析]]


## 主要发现


- 基于1.4%电压偏差阈值确定的缓冲区能有效平衡仿真精度与计算规模
- 混合框架成功实现近八万节点电网与微秒级MMC模型的跨平台稳定协同仿真
- 对比验证表明不同步长与缓冲区规模组合可满足系统级暂态稳定分析需求



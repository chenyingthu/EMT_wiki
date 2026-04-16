---
title: "Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Transmission and Distribution Systems"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Systems;2018;33;6;10.1109/TPWRS.2018.2834561"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans.pdf"]
---

# Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Transmission and Distribution Systems

**作者**: 
**年份**: 2018
**来源**: `06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans.pdf`

## 摘要

—Conventional electromagnetic transient (EMT) and phasor-domain hybrid simulation approaches presently exist for transmission system level studies. Their simulation efﬁciency is generally constrained by the EMT simulation. With an increasing number of distributed energy resources and nonconventional loads being installed in distribution systems, it is imperative to extend the hybrid simulation application to include distribution systems and integrated transmission and distribution systems. Meanwhile, it is equally important to improve the simulation efﬁciency as the modeling scope and complexity of the detailed system in the EMT simulation increases. To meet both requirements, this paper introduces an advanced EMT and phasor-domain hybrid simu- lation approach. This approach has two main f

## 核心贡献


- 提出适用于输配电及输配一体化系统的综合电磁暂态与相量域混合仿真框架
- 设计鲁棒的仿真模式切换机制，支持快动态平息后从混合模式平滑切回相量域
- 利用EMT捕获的离散事件协调双域模型状态，解决切换过程中的结果发散问题


## 使用的方法


- [[电磁暂态与相量域混合仿真|电磁暂态与相量域混合仿真]]
- [[仿真模式切换|仿真模式切换]]
- [[多区域戴维南等值|多区域戴维南等值]]
- [[相量域动态仿真|相量域动态仿真]]
- [[三相与序分量混合建模|三相与序分量混合建模]]


## 涉及的模型


- [[输配电网络|输配电网络]]
- [[分布式电源|分布式电源]]
- [[电力电子变换器|电力电子变换器]]
- [[单相感应电机|单相感应电机]]
- [[emt详细模型|EMT详细模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[输配电一体化|输配电一体化]]
- [[仿真模式切换|仿真模式切换]]
- [[计算效率优化|计算效率优化]]
- [[网络等值|网络等值]]


## 主要发现


- 引入模式切换机制后，总计算时间显著缩短，同时保持了较高的仿真精度
- 在输配电一体化系统测试中，快动态平息后切回相量域仿真有效提升了效率
- 协调策略成功解决了EMT与相量模型切换时的状态发散问题，验证了鲁棒性



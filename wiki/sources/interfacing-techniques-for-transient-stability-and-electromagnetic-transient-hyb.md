---
title: "Interfacing Techniques for Transient Stability and Electromagnetic Transient Hybrid Simulation"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/24/Jalili-Marandi 等 - 2009 - Interfacing Techniques for Transient Stability and Electromagnetic Transient Programs IEEE Task Forc.pdf"]
---

# Interfacing Techniques for Transient Stability and Electromagnetic Transient Hybrid Simulation

**作者**: 
**年份**: 2009
**来源**: `24/Jalili-Marandi 等 - 2009 - Interfacing Techniques for Transient Stability and Electromagnetic Transient Programs IEEE Task Forc.pdf`

## 摘要

—Transient stability (TS) and electromagnetic transient (EMT)programsarewidely usedsimulationtoolsinpower systems, with distinct applications but competing requirements. TS pro- grams are fast which makes them suitable for handling large-scale networks, however, the modeling is not sufﬁciently detailed. On the other hand, EMT simulators are highly detailed, but limited in speed; consequently, they are used to simulate only small portions of the network. Integrating these two types of simulators generates a hybrid simulator which inherits the merits of both programs. A hybrid simulator can fulﬁll the modeling requirements of a large network by providing a fast as well as a detailed simulation. Es- tablishing a connection between two different programs brings up several important issues whic

## 核心贡献


- 系统梳理TS与EMT混合仿真接口关键问题与数据交换协议
- 提出基于频移概念的机电与电磁暂态一体化自适应建模方法
- 制定混合仿真网络分割、多速率积分与步长同步的标准化规范


## 使用的方法


- [[混合仿真接口技术|混合仿真接口技术]]
- [[网络分割|网络分割]]
- [[并行计算|并行计算]]
- [[多速率积分|多速率积分]]
- [[频移法|频移法]]
- [[时间步长同步|时间步长同步]]
- [[数据交换协议|数据交换协议]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[输电线路|输电线路]]
- [[vsc-hvdc|VSC-HVDC]]
- [[facts装置|FACTS装置]]
- [[电力电子变换器|电力电子变换器]]
- [[集中参数元件|集中参数元件]]
- [[分布参数线路|分布参数线路]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[接口技术|接口技术]]
- [[并行计算|并行计算]]
- [[网络分割|网络分割]]
- [[频率自适应建模|频率自适应建模]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 混合仿真通过接口协议与步长同步，有效兼顾大电网计算速度与局部精度
- 频移技术可实现机电与电磁模型无缝集成，避免传统接口边界数值振荡
- 网络分割结合多速率积分策略显著降低数据交换延迟，提升整体求解效率



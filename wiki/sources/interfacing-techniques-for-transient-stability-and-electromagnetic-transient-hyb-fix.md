---
title: "Interfacing Techniques for Transient Stability and Electromagnetic Transient Hybrid Simulation"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/24/TPWRD.2008.2002889.pdf.pdf"]
---

# Interfacing Techniques for Transient Stability and Electromagnetic Transient Hybrid Simulation

**作者**: 
**年份**: 2009
**来源**: `24/TPWRD.2008.2002889.pdf.pdf`

## 摘要

—Transient stability (TS) and electromagnetic transient (EMT)programsarewidely usedsimulationtoolsinpower systems, with distinct applications but competing requirements. TS pro- grams are fast which makes them suitable for handling large-scale networks, however, the modeling is not sufﬁciently detailed. On the other hand, EMT simulators are highly detailed, but limited in speed; consequently, they are used to simulate only small portions of the network. Integrating these two types of simulators generates a hybrid simulator which inherits the merits of both programs. A hybrid simulator can fulﬁll the modeling requirements of a large network by providing a fast as well as a detailed simulation. Es- tablishing a connection between two different programs brings up several important issues whic

## 核心贡献


- 系统梳理并分类了暂态稳定与电磁暂态混合仿真的接口技术、通信协议与关键问题
- 探讨基于频率平移的一体化建模方法，为消除TS与EMT频带差异提供理论依据
- 统一规范混合仿真领域的术语定义与实现流程，为大规模电网仿真提供标准框架


## 使用的方法


- [[混合仿真|混合仿真]]
- [[网络分割|网络分割]]
- [[并行计算|并行计算]]
- [[多速率积分|多速率积分]]
- [[频率平移|频率平移]]
- [[数据交换协议|数据交换协议]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[输电线路|输电线路]]
- [[vsc-hvdc|VSC-HVDC]]
- [[facts装置|FACTS装置]]
- [[集中参数模型|集中参数模型]]
- [[分布参数模型|分布参数模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[暂态稳定|暂态稳定]]
- [[电磁暂态|电磁暂态]]
- [[接口技术|接口技术]]
- [[并行计算|并行计算]]
- [[网络分割|网络分割]]
- [[频率自适应建模|频率自适应建模]]
- [[多速率仿真|多速率仿真]]


## 主要发现


- 混合仿真通过合理划分网络边界与数据交互协议，可兼顾大规模电网计算速度与局部高精度
- 频率平移技术能有效桥接基频与宽频模型，实现暂态稳定与电磁暂态程序的一体化耦合
- 接口步长不匹配与通信延迟是主要误差源，需结合多速率积分与预测校正算法进行补偿



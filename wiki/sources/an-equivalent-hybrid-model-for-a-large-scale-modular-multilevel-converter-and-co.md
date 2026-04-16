---
title: "An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Access;2022;10; ;10.1109/ACCESS.2022.3176006"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations.pdf"]
---

# An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations

**作者**: 
**年份**: 2022
**来源**: `07&08/An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations.pdf`

## 摘要

Modular multilevel converter (MMC) is adopted mainly for high voltage applications with many power blocks per arm. Before commissioning a large-scale MMC application, it is vital to simulate and study internal and system-level dynamics. However, it is challenging to simulate an MMC with many SMs in EMT simulation tools due to simulation time and computation burden. Therefore, several simpliﬁed modeling techniques are proposed to reduce the challenges. Even though the existing models reasonably reduce the computation complexity and simulation time, there are still challenges as the internal dynamics of an MMC cannot be fully captured. On the other hand, the detailed equivalent models capture the internal dynamics, but the simulation complexity and the time increase. Therefore, it is still a

## 核心贡献


- 提出基于扩容控制结构的MMC混合仿真模型，将子模块分组为主从集以降低计算负担
- 主集采用详细等效模型，其余集作为受控电压源，兼顾内部动态捕捉与仿真速度
- 支持无需大幅修改模型即可灵活调整MMC容量，适用于系统级与内部动态研究


## 使用的方法


- [[混合仿真建模|混合仿真建模]]
- [[详细等效模型|详细等效模型]]
- [[扩容控制结构|扩容控制结构]]
- [[硬件在环-hil|硬件在环(HIL)]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块-hbsm|半桥子模块(HBSM)]]
- [[全桥子模块-fbsm|全桥子模块(FBSM)]]
- [[vsc-model|VSC]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[硬件在环|硬件在环]]
- [[vsc-model|VSC]]
- [[mmc-model|MMC]]


## 主要发现


- 验证表明该模型比传统详细等效EMT模型仿真速度更快，且保持相近的精度水平
- 子模块或分组数量增加时，计算负担未显著上升，具备良好的可扩展性
- 模型支持灵活调整MMC容量，可同时准确捕捉系统级响应与子模块内部动态



---
title: "Fast Voltage-Balancing Control and Fast"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/tpwrd.2014.2351397.pdf-1.pdf"]
---

# Fast Voltage-Balancing Control and Fast

**作者**: 
**年份**: 2014
**来源**: `19、20、21/EMT_task_19/tpwrd.2014.2351397.pdf-1.pdf`

## 摘要

—A methodology of fast voltage-balancing control based on average comparison and a fast numerical simulation model for the modular multilevel converter are proposed. In each control cycle, the average voltage of all the submodules (SMs) in an arm is calculated. The switching state of each SM will be determined by comparing the capacitor voltage of each SM with this average value. Little sorting of the capacitor voltages is required; therefore, the calculation burden on the controller is signiﬁcantly reduced. The previous switching state of each SM will be mostly retained. Two variables and are introduced to adjust the equivalent switching frequency of each SM. Simulation results veriﬁed the effectiveness of the proposed voltage-balancing control in normal and fault conditions. A fast numer

## 核心贡献


- 提出基于平均比较的快速电压均衡控制策略大幅减少电容电压排序计算量
- 构建保留子模块动态的快速数值仿真模型无需修改底层求解器源码
- 引入双变量调节等效开关频率开发可嵌入特定子模块细节的混合模型


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[线性化开关模型|线性化开关模型]]
- [[最近电平调制|最近电平调制]]
- [[混合仿真建模|混合仿真建模]]
- [[平均比较法|平均比较法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[详细开关模型|详细开关模型]]
- [[快速数值仿真模型|快速数值仿真模型]]
- [[混合仿真模型|混合仿真模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[电压均衡控制|电压均衡控制]]
- [[快速仿真|快速仿真]]
- [[混合仿真|混合仿真]]


## 主要发现


- 所提均衡控制在正常与故障工况下均能有效维持子模块电容电压平衡
- 快速模型仿真精度与详细开关模型一致且仿真速度提升约五千倍
- 混合模型可精准复现特定子模块开关动态兼顾全局效率与局部细节



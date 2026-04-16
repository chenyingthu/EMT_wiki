---
title: "A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC HVDC system"
type: source
authors: ['Yupeng Li']
year: 2019
journal: "Electrical Power and Energy Systems, 115 (2019) 105479. doi:10.1016/j.ijepes.2019.105479"
tags: ['lcc', 'cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Li 等 - 2020 - A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC.pdf"]
---

# A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC HVDC system

**作者**: Yupeng Li
**年份**: 2019
**来源**: `02/Li 等 - 2020 - A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC.pdf`

## 摘要

A multi-area Thevenin equivalent based multi-rate co-simulation for control Yupeng Lia, Dewu Shua,⁎, Jingwei Hua, Zheng Yana, Yun Zhoua, Haifeng Wangb a High-Performance Simulation Center, Key Lab of Control and Power Transmission and Conversion, Department of Electrical Engineering, Shanghai Jiaotong University, b State Grid Shanghai Municipal Electric Power Company, China The line commutated converter (LCC) based HVDC transmission is often adopted to transmit the large capacity

## 核心贡献


- 提出基于多区域戴维南等值的输电线路接口模型，实现交直流宽频交互精确解耦
- 构建多速率协同仿真架构，结合MATE技术大幅提升大规模电网电磁暂态仿真效率
- 提出基于虚拟阻抗的改进控制策略，有效降低换相失败概率并加快直流系统恢复


## 使用的方法


- [[多速率协同仿真|多速率协同仿真]]
- [[多区域戴维南等值-mate|多区域戴维南等值(MATE)]]
- [[输电线路模型-tlm|输电线路模型(TLM)]]
- [[网络分割技术|网络分割技术]]
- [[虚拟阻抗控制|虚拟阻抗控制]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[交直流电网|交直流电网]]
- [[输电线路|输电线路]]
- [[戴维南等效模型|戴维南等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[换相失败抑制|换相失败抑制]]
- [[网络等值|网络等值]]
- [[多速率仿真|多速率仿真]]
- [[弱交流系统|弱交流系统]]
- [[控制策略设计|控制策略设计]]


## 主要发现


- 实际交直流电网仿真验证了所提多速率协同仿真方法在精度与效率上的显著优势
- 虚拟阻抗控制策略有效降低了弱交流系统下的换相失败概率，并提升了直流电压恢复速度
- MATE-TLM接口模型在保证宽频交互精度的同时，大幅降低了大规模网络求解计算负担



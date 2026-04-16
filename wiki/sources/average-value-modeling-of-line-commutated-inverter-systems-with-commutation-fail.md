---
title: "Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;4;10.1109/TPWRD.2021.3117027"
tags: ['lcc', 'average-value']
created: "2026-04-13"
sources: ["EMT_Doc/09/Hong 等 - 2022 - Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure.pdf"]
---

# Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure

**作者**: 
**年份**: 2022
**来源**: `09/Hong 等 - 2022 - Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure.pdf`

## 摘要

—Line-commutated converters are extensively used as the interface between ac grids and classic HVDC systems. At the inverter side, commutation failure of switches is one of the most common faults that can pose threats to the system operation. Practical and reliable study of such phenomena relies on accurate and efﬁcient converter models for simulations. Recently, a para- metric average-value model (PAVM) has been presented for ac–dc rectiﬁers, which considers the internal faults of the converter. In this paper, the PAVM methodology is extended to the dc–ac inverter systems, including the commutation failure of switches. The pro- posed PAVM also augments an automatic fault detection technique to determine the faulty switches. Using comprehensive simulation studies, the developed model is ve

## 核心贡献


- 将参数化平均值模型从整流器扩展至直流交流晶闸管逆变器系统
- 提出基于电压跌落幅值与故障时刻的自动换相失败检测技术
- 采用电流源接口技术实现平均值模型与逆变器运行模式兼容


## 使用的方法


- [[参数化平均值模型|参数化平均值模型]]
- [[电流源接口技术|电流源接口技术]]
- [[自动故障检测算法|自动故障检测算法]]
- [[连续代数方程建模|连续代数方程建模]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[六脉冲晶闸管逆变器|六脉冲晶闸管逆变器]]
- [[vsc-hvdc|VSC-HVDC]]
- [[平波电抗器|平波电抗器]]
- [[输电线路|输电线路]]
- [[戴维南等效电路|戴维南等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[换相失败|换相失败]]
- [[传统高压直流输电|传统高压直流输电]]
- [[系统级仿真|系统级仿真]]
- [[交流电压跌落|交流电压跌落]]
- [[故障检测|故障检测]]


## 主要发现


- 模型能准确预测换相失败过程，波形与详细开关模型高度一致
- 仿真计算速度比详细开关模型快数个数量级，显著提升系统级效率
- 自动检测技术可依据外部电网条件精准定位故障晶闸管



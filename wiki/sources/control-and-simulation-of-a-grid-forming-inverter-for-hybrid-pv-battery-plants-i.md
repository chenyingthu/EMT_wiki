---
title: "Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start"
type: source
authors: ['Quan Nguyen']
year: 2020
journal: "2021 IEEE Power & Energy Society General Meeting (PESGM);2021; ; ;10.1109/PESGM46819.2021.9637882"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Nguyen 等 - 2021 - Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black.pdf"]
---

# Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start

**作者**: Quan Nguyen
**年份**: 2020
**来源**: `11/Nguyen 等 - 2021 - Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black.pdf`

## 摘要

—Power system restoration is an important part of system planning. Power utilities are required to maintain black start capable generators that can energize the transmission system and provide cranking power to non-blackstart capable generators. Traditionally, hydro and diesel units are used as black start capable generators. With the increased penetration of bulk size solar farms, inverter based generation can play an important role in faster and parallel black start thus en- suring system can be brought back into service without the conventional delays that can be expected with limited black start generators. Inverter-based photovoltaic (PV) power plants have advantages that are suitable for black start. This paper proposes the modeling, control, and simulation of a grid-forming inverter

## 核心贡献


- 提出构网型光储逆变器黑启动建模与控制策略，模拟同步机外特性
- 设计下垂与二次PI双层控制架构，实现并网点电压频率自主调节
- 基于PSCAD构建高保真电磁暂态模型，验证多步黑启动全过程稳定性


## 使用的方法


- [[构网型控制|构网型控制]]
- [[下垂控制|下垂控制]]
- [[dq坐标系嵌套双环控制|dq坐标系嵌套双环控制]]
- [[脉宽调制-pwm|脉宽调制(PWM)]]
- [[时域电磁暂态仿真|时域电磁暂态仿真]]
- [[pi控制|PI控制]]


## 涉及的模型


- [[构网型逆变器|构网型逆变器]]
- [[光伏阵列|光伏阵列]]
- [[电池储能系统|电池储能系统]]
- [[lc滤波器|LC滤波器]]
- [[升压变压器|升压变压器]]
- [[dc-dc变换器|DC/DC变换器]]
- [[ieee-9节点测试系统|IEEE 9节点测试系统]]


## 相关主题


- [[黑启动|黑启动]]
- [[构网型逆变器|构网型逆变器]]
- [[光储混合系统|光储混合系统]]
- [[电力系统恢复|电力系统恢复]]
- [[电压与频率稳定|电压与频率稳定]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 仿真验证多步黑启动过程中母线电压与频率保持稳定，无越限现象
- 构网型控制有效抑制变压器与线路投切引起的暂态冲击，维持额定值
- 储能优先供电配合光伏动态补充，维持直流母线电压恒定保障启动



---
title: "负荷建模 (Load Modeling)"
type: topic
tags: [load-modeling, load, power-system, dynamic, static]
created: "2026-05-02"
---

# 负荷建模 (Load Modeling)


```mermaid
graph TD
    N0[负荷建模 (Load Model…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[主要分支与机制]
    N0 --> N3
    N4[形式化表达]
    N0 --> N4
    N5[适用边界与失败模式]
    N0 --> N5
    N6[代表性来源]
    N0 --> N6
    N7[与相关页面的关系]
    N0 --> N7
    N8[开放问题]
    N0 --> N8
```


## 定义与边界

负荷建模是用静态、电磁暂态或动态模型表示负荷随电压、频率、时间和控制状态变化的过程。它不是负荷预测、用户行为分析或需求响应市场模型；这些内容只有在作为仿真场景输入时才进入 EMT 讨论。

在 EMT Wiki 中，本页关注负荷如何影响 [[emt-simulation]]、[[transient-stability-analysis]] 和 [[small-signal-stability]]。具体设备模型可阅读 [[load-model]] 和 [[induction-machine-model]]。

## EMT 中的作用

负荷模型会影响故障电流、电压恢复、暂态稳定、频率响应和保护动作。EMT 场景中尤其需要关注：

- 感应电动机失速、再加速和低电压下的无功需求。
- 电力电子负荷和恒功率负荷在电压跌落时的限流、闭锁或恢复逻辑。
- 配电网单相负荷和不平衡负荷对相域波形、零序电流和保护判据的影响。
- 聚合负荷模型与实际负荷构成、测量数据和运行点之间的误差。

## 主要分支与机制

- 静态负荷：常用 ZIP 或指数模型表示电压依赖关系，适合潮流初值和慢动态近似。
- 动态电动机负荷：用滑差、转矩和磁链状态描述电动机在故障和电压恢复中的行为。
- 电子负荷：可表示为恒功率、受限电流源或带控制器的整流/逆变接口，限流和保护逻辑是关键边界。
- 聚合负荷：把多类负荷按容量、类型或测量响应合并，应说明聚合依据和保留的动态。

## 形式化表达

常见静态负荷可写为 ZIP 形式：

$$
P=P_0\left(a_z\left(\frac{V}{V_0}\right)^2+a_i\frac{V}{V_0}+a_p\right),\qquad
Q=Q_0\left(b_z\left(\frac{V}{V_0}\right)^2+b_i\frac{V}{V_0}+b_p\right)
$$

动态电动机负荷还需要状态方程，例如：

$$
2H_m\dot{\omega}_r=T_e(V,\omega_r,x_m)-T_m
$$

其中 $V$ 是端电压，$\omega_r$ 是转速，$x_m$ 是电磁状态。若只使用静态 ZIP 模型，页面或算例不应声称已经验证电动机失速和再加速过程。

## 适用边界与失败模式

- 无来源的负荷构成比例、频率系数和典型电动机占比不应写成通用参数；应绑定地区、时段、母线和测量来源。
- 恒功率负荷在低电压时可能导致非物理电流增长，EMT 模型通常需要限流、闭锁或保护逻辑。
- 聚合负荷可能掩盖单相不平衡、局部电动机失速和电子负荷控制差异。
- 用负荷模型支撑电压稳定或频率稳定结论时，应说明模型是否覆盖电压、频率和动态响应。

## 代表性来源

- [[development-and-validation-of-a-new-detailed-emt-type-component-based-load-model]] 可作为综合负荷和电动机-发电机组建模的来源入口。
- [[modeling-a-mixed-residential-commercial-load-for-simulations-involving-large-dis]] 支撑基于中压客户响应的 EMT 负荷模型讨论。
- [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator]] 可作为高电力电子渗透率下主动负荷模型的来源入口。
- [[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati]] 可作为负荷建模综述性来源，具体参数仍需绑定场景。

## 与相关页面的关系

- [[load-model]] 是负荷模型页，承载具体模型结构。
- [[power-flow-calculation]] 使用负荷作为稳态输入；EMT 还需要动态和事件边界。
- [[transient-stability-analysis]] 与 [[small-signal-stability]] 关注负荷对稳定性的影响。
- [[renewable-energy-integration]] 和 [[pv-power-plant]] 中的逆变器型资源可能表现为发电或受控负荷，需要明确方向和控制模式。

## 开放问题

- 如何从现场测量中辨识可用于 EMT 的负荷动态，而不是只得到潮流 ZIP 系数。
- 如何在配电网不平衡、单相负荷和电子负荷快速控制之间建立可复现模型。
- 如何报告聚合负荷模型对电压恢复、保护动作和宽频振荡结论的影响。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-a-mixed-residential-commercial-load-for-simulations-involving-large-dis|Modeling A Mixed Residential-commercial Load  For Simulation]] | 2004 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[dynamic-average-modeling-of-front-end-diode-rectifier-loads-considering-13&14|Dynamic Average Modeling of Front-End Diode Rectifier Loads ]] | 2011 |
| [[development-of-data-translators-for-interfacing-13&14|Development of Data Translators for Interfacing Power-Flow P]] | 2013 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[development-and-validation-of-a-new-detailed-emt-type-component-based-load-model|Development and Validation of a New Detailed EMT-type Compon]] | 2021 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati|Modeling of inductive constant power load for electromagneti]] | 2025 |

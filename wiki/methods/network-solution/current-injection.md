---
title: "电流注入法 (Current Injection Method)"
type: method
tags: [current-injection, inverter, interfacing, emt, modeling, nodal-analysis]
created: "2026-05-02"
---

# 电流注入法 (Current Injection Method)


```mermaid
graph TD
    subgraph Ncmp[电流注入法 (Current Injection Met…]
        N0[输入: 当前或上一时间步的节点电压、器件状态、控制器输出…]
        N1[输出: 注入到节点方程右端的电流向量，必要时还包括等效导…]
        N2[网络接口: $\mathbf{Y}\mathbf{v}_…]
        N3[主要约束: 注入电流必须与端口功率、参考方向、离散化格式…]
    end
```


## 概述

电流注入法（Current Injection Method）是在 EMT 网络方程中把外部设备、受控源或离散化元件表示为节点注入电流的方法。它通常与 [[nodal-analysis]]、[[nodal-admittance-matrix]] 和 [[companion-circuit]] 一起使用：线性或等效线性部分进入导纳矩阵，随时间变化的源项、历史项和控制输出进入右端电流向量。

该页讨论的是“接口方法”，不是某一种换流器控制律。VSC、LCC、同步机、负荷或外部等值都可以在某些建模层级下形成注入电流，但每类对象的注入量、更新时刻和适用边界不同，不能把单一拓扑的控制结论外推到所有电流注入模型。

## 输入与输出

| 项目 | 内容 |
|------|------|
| 输入 | 当前或上一时间步的节点电压、器件状态、控制器输出、历史电流源、端口等效参数 |
| 输出 | 注入到节点方程右端的电流向量，必要时还包括等效导纳修正 |
| 网络接口 | $\mathbf{Y}\mathbf{v}_{n+1}=\mathbf{i}_{src,n+1}+\mathbf{i}_{hist,n+1}$ |
| 主要约束 | 注入电流必须与端口功率、参考方向、离散化格式和控制采样时刻一致 |

在伴随电路中，电感、电容和线路等动态元件经离散化后通常形成等效电导加历史电流源。例如某支路可写为：

$$i_{n+1}=G_{eq}v_{n+1}+I_{hist}$$

其中 $G_{eq}$ 进入网络导纳矩阵，$I_{hist}$ 进入注入向量。若采用不同积分公式，$G_{eq}$ 和 $I_{hist}$ 的表达会改变；因此页面不把某一组公式写成通用实现。

## 核心机制

电流注入接口的基本步骤是：

1. 明确端口方向和参考节点，确定正注入电流的符号。
2. 将可线性化或固定的端口导纳写入 $\mathbf{Y}$。
3. 将受控源、历史项、开关函数或外部子系统输出写入 $\mathbf{i}$。
4. 求解节点电压，再把端口电压、电流反馈给设备模型或控制模型。
5. 若设备为非线性或强耦合对象，按模型需要执行迭代、延迟接口或子步更新。

对受控电流源，网络通常只看到右端注入项；对带并联导纳的诺顿等效，则导纳和电流源同时更新。若使用延迟接口或松耦合算法，上一时间步量进入当前步注入项，这会减少联立求解成本，但会引入步长相关误差。

## 换流器接口中的用法

VSC 建模中，电流注入可以出现在平均值模型、受控源等值和详细开关等值中。[[a-vsc-hvdc-model-with-reduced-computational-intensity]] 将三电平 VSC 表示为交流侧受控电压源和直流侧受控电流源，用于降低系统级 EMT 仿真计算强度；该结论限于论文中的 VSC-HVDC、SPWM 和矢量控制算例。

[[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-]] 则用脉冲电压-电流源对把 VSC 开关作用移出时变导纳支路，使网络矩阵保持不变，并采用单向松耦合求解。该方法仍面向作者讨论的多 VSC 两电平开关场景；不能据此说明所有 MMC、保护闭锁或器件损耗模型都可用同一注入接口替代。

LCC 建模中的电流注入应与晶闸管阀状态、换相电压和直流电流约束一起解释。[[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] 采用电流源接口兼容线换相逆变器平均值模型，并把换相失败检测嵌入 PAVM；它支撑的是 LCC 逆变侧换相失败的平均值建模，不是 VSC 控制接口。

## 适用边界

- 适合把外部设备、控制器或离散元件接入 EMT 节点方程，尤其适合固定导纳、平均值模型、端口等值和混合仿真接口。
- 对详细开关模型，若开关状态改变导纳矩阵，电流注入不能自动消除拓扑变化；需要脉冲源对、固定导纳或拓扑分解等附加处理。
- 对强耦合换流器、电机和控制系统，单步延迟注入可能影响暂态精度，需要与详细联立模型或小步长结果对比。
- 对功率控制型注入，$I=P/V^*$ 类表达在低电压或相角快速变化时可能数值敏感，应配合限幅和保护逻辑。
- 对 LCC，换相失败、关断角和阀级状态不能只由外部注入电流决定，必须保留换相物理约束。

## 代表性证据

| 来源 | 证据用途 | 边界 |
|------|----------|------|
| [[a-vsc-hvdc-model-with-reduced-computational-intensity]] | VSC-HVDC 动态平均值模型中的受控电压源/电流源接口 | 限于论文中的三电平 VSC、SPWM 和 PSCAD/EMTDC 对比 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-]] | 多 VSC 开关事件用脉冲源对表示，避免频繁矩阵重构 | 当前证据支持机制性说明，具体误差和耗时需回原文表图 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] | LCC 逆变器 PAVM 中的电流源接口和换相失败检测 | 适用于线换相逆变器平均值模型，不适用于 VSC |

## 与相关页面的关系

- [[nodal-analysis]] 和 [[nodal-admittance-matrix]] 给出网络方程背景。
- [[companion-circuit]] 说明历史源如何由数值积分产生。
- [[fixed-admittance]] 是减少矩阵重构的一类实现策略。
- [[vsc-model]]、[[lcc-model]] 和 [[inverter-model]] 决定注入接口的设备物理含义。

## 开放问题

电流注入接口的风险主要来自跨时间步延迟、控制采样与 EMT 步长不一致、低电压下功率型电流源奇异、以及端口方向约定不统一。使用该方法时，应把注入电流、导纳修正、历史项和控制输出的来源写清楚，并用目标工况下的详细模型或实测数据校核。

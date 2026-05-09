---
title: "HVDC 控制 (HVDC Control)"
type: method
tags: [hvdc-control, lcc-hvdc, vsc-hvdc, converter-control, dc-grid]
created: "2026-05-05"
updated: "2026-05-06"
---

# HVDC 控制 (HVDC Control)


```mermaid
graph TD
    subgraph S0[HVDC 控制 (HVDC Control)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[主要分支]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[适用边界与失败模式]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

HVDC 控制是直流输电系统中围绕直流电压、直流电流、有功功率、无功支撑、换相裕度和运行方式切换建立的控制方法集合。它覆盖 LCC-HVDC、VSC-HVDC 和多端直流系统中的站级控制、极控和协调逻辑。

本页讨论的是 HVDC 运行控制结构本身，不把混合式直流断路器实时仿真建模、HIL 平台或特定硬件实现误写成 HVDC 控制方法。

## EMT 中的作用

在 EMT 仿真中，HVDC 控制主要用于：

- 表达整流侧/逆变侧的功率、电压和电流控制模式；
- 研究故障、功率指令变化和弱网条件下的动态切换；
- 评估 LCC 换相失败、VSC 限流、直流电压恢复和多站协调行为；
- 把主电路、保护和站间协调逻辑组织成可验证的控制结构。

## 主要分支

- LCC-HVDC 控制：触发角、关断角、定电流、定熄弧角、定功率等控制模式。
- VSC-HVDC 控制：直流电压外环、功率外环、电流内环、PLL 或构网控制。
- 多端直流协调：主从控制、下垂控制、电压-功率协同与站间运行方式管理。

## 关键公式

LCC 场景中常见的直流侧关系可写为：

$$
V_d = V_{d0}\cos\alpha - \frac{3\omega L_c}{\pi} I_d
$$

其中 $\alpha$ 为触发角，$I_d$ 为直流电流。对逆变侧，也常围绕关断角 $\gamma$ 组织控制和约束。

VSC 场景中，HVDC 控制通常表现为外环参考到内环电流指令的映射：

$$
\mathbf{i}_{dq}^* = f\,(V_{dc}^\*, P^\*, Q^\*, \mathbf{y}_m)
$$

该表达只说明接口关系，不意味着所有 HVDC 工程都共享同一控制器或参数。

## 与相关方法的关系

- [[thyristor-control]] 和 [[extinction-angle-calculation]]：对应 LCC 侧核心控制变量。
- [[vsc-control]] 和 [[dual-loop-pi-controller]]：对应 VSC-HVDC 常见控制骨架。
- [[multi-terminal-dc]]：对应多端直流网络中的协调背景。
- [[converter-station-inverter]]：对应站级逆变运行边界。

## 适用边界与失败模式

- LCC-HVDC 控制受交流系统强度、无功支撑和换相裕度显著影响。
- VSC-HVDC 控制受限流、直流故障、PLL 或构网模式切换影响。
- 多端系统中，局部控制稳定不等于全系统协调稳定。
- 若不显式建模保护、限幅和模式切换，EMT 结果可能高估控制能力。

## 代表性来源

- [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc]]：可用于支撑 LCC-HVDC 控制模式切换与运行特性的场景化讨论。
- [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver]]：可作为 VSC-HVDC 外环参数设计背景来源。
- [[dynamic-performance-of-embedded-hvdc-with-13&14]]：说明嵌入式 VSC-HVDC 中外环、内环与频率相关补偿的组合方式。

## 证据边界

本页只提供 HVDC 控制的上位方法框架，不新增无来源整定参数、切换阈值、控制带宽或“最优控制模式”结论。具体策略必须绑定拓扑、算例和来源。

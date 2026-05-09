---
title: "低电压穿越控制 (LVRT Control)"
type: method
tags: [lvrt-control, low-voltage-ride-through, fault-ride-through, grid-code, converter-control]
created: "2026-05-05"
updated: "2026-05-06"
---

# 低电压穿越控制 (LVRT Control)

## 定义与边界

低电压穿越控制是并网变流器、风电机组和光伏电站在交流故障或电压跌落期间维持并网、限制电流并按规范注入无功/有功支撑的控制方法。它通常包含故障检测、限流、无功优先、电流参考重构和故障后恢复逻辑。

本页讨论的是故障期间的控制策略，不把 Modelica 线性化框架、特征值扫描工具或一般小信号分析方法误写成 LVRT 控制本身。

## EMT 中的作用

在 EMT 仿真中，LVRT 控制主要用于：

- 研究故障期间电流限幅、无功支撑和直流母线动态；
- 评估故障清除后的恢复过程与控制模式切换；
- 检查弱网、PLL 动态和网规约束对并网设备可持续并网能力的影响；
- 作为风电、光伏和储能站级控制验证的重要工况。

## 主要机制

- 电压跌落检测与故障状态机；
- 电流限幅和优先级分配；
- 有功削减、无功注入或电压支撑逻辑；
- 故障后恢复与再同步。

## 关键公式

LVRT 控制没有唯一标准公式，但常用思路是按电压跌落程度重构电流参考，例如：

$$
\mathbf{i}_{dq}^\* = f(V_{pcc}, V_{dc}, I_{max}, \text{mode})
$$

其中 $V_{pcc}$ 为并网点电压，$V_{dc}$ 为直流侧电压，$I_{max}$ 为电流上限，`mode` 表示故障期间的控制优先级。不同厂商或论文的无功优先和有功降额策略可能明显不同。

## 与相关方法的关系

- [[fault-ride-through]]：更宽泛的故障穿越主题背景。
- [[pll-model]]：故障期间同步参考是否可靠，直接影响 LVRT 表现。
- [[vsc-control]] 和 [[dual-loop-pi-controller]]：故障期间电流重构常依赖这些底层控制结构。
- [[microgrid-control]]：在孤岛或弱网场景中，故障穿越逻辑可能与并网场景不同。

## 适用边界与失败模式

- 适用于需要按并网规范评估故障期间持续并网能力的变流器设备。
- 电流限流、直流过压和 PLL 失稳常是故障期间的核心限制。
- 不同网规对无功支撑和持续时间要求不同，不能在页面中泛化为统一标准。
- 单靠小信号线性化不能替代故障期间的非线性 EMT 验证。

## 代表性来源

- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]]：可作为光伏场站控制交互和故障风险背景来源，但不应替代 LVRT 时域验证。
- [[field-validated-generic-emt-type-model-of-a-full-converter-wind-turbine-based-on]]：可作为全功率变流器风机 EMT 控制与故障响应的代表性背景。
- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：说明构网型装置在电压跌落和恢复中的相关运行背景。

## 证据边界

本页不写无来源的无功支撑比例、恢复时间或网规门槛。具体 LVRT 能力必须绑定设备类型、控制结构和测试规范。

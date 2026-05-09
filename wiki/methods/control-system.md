---
title: "控制系统 (Control System)"
type: method
tags: [control-system, feedback, regulation, protection, synchronization]
created: "2026-05-06"
updated: "2026-05-06"
---

# 控制系统 (Control System)

## 定义与边界

控制系统是 EMT 模型中负责测量、比较、调节、限幅、切换和保护动作的算法与逻辑集合。它不是单一 PI 控制器，也不是任何特定拓扑的专属实现，而是对并网控制、直流控制、励磁调节、保护闭锁和模式管理等机制的总称。

## EMT 中的作用

在 EMT 仿真中，控制系统决定参考量如何生成、执行量如何受约束、故障下如何切换以及测量延迟和采样如何影响动态响应。它通常与电气主电路、网络模型和保护逻辑强耦合。

## 形式化表达

控制系统通常可抽象为测量、控制律和执行接口三部分：

$$
\mathbf{y}_m = h(\mathbf{x}, \mathbf{v}, t), \qquad
\dot{\mathbf{x}}_c = f_c(\mathbf{x}_c, \mathbf{y}_m, \mathbf{r}, t), \qquad
\mathbf{u} = g_c(\mathbf{x}_c, \mathbf{y}_m, \mathbf{r}, t)
$$

其中 $\mathbf{y}_m$ 为测量量，$\mathbf{x}_c$ 为控制器状态，$\mathbf{r}$ 为参考量，$\mathbf{u}$ 为注入主电路或保护逻辑的执行量。这个框架强调控制系统是“接口和状态组织”，而不是单一 PI 公式。

## 常见结构

- [[pi-controller-model]]：单个 PI/PID 环节的模型基础。
- [[dual-loop-pi-controller]]：电流内环与功率/电压外环的级联结构。
- [[pll-model]]：并网同步与坐标变换参考。
- [[vector-control]]：dq 坐标下的控制组织方式。
- [[thyristor-control]]：LCC 场景下的触发角与阀状态控制。
- [[distributed-control]]：多控制器协同与分布式执行。
- [[power-system-stabilizer]]：同步机侧附加阻尼控制。

## 适用边界

- 对 VSC、MMC、储能、并网逆变器和机组控制，具体结构必须绑定被控对象。
- 对 LCC-HVDC，不应把 dq 双环控制误写为通用入口。
- 对保护控制或模式切换，必须显式说明测量、延迟、限幅、闭锁和故障逻辑。

## 与相关页面的关系

- [[power-system]] 是上位系统主题。
- [[power-system-network]] 提供被控电气网络。
- [[vsc-model]]、[[mmc-model]]、[[inverter-model]] 提供典型被控对象。
- [[wide-area-monitoring-protection]] 关注更大范围的监测和执行闭环。

## 开放问题

- 数字控制延迟、采样与饱和如何在 EMT 中保持可解释性。
- 控制器、保护与主电路的分层边界如何避免重复建模。
- 同一控制逻辑在离线 EMT、平均值模型和实时平台中的一致性如何保证。

## 代表性来源

- [[improved-control-systems-simulation-in-the-emtp-through-compensation]]：说明控制方程与 EMT 网络同步求解的经典路线。
- [[dynamic-performance-of-embedded-hvdc-with-13&14]]：说明 VSC-HVDC 场景下控制系统如何与主电路和运行方式耦合。
- [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]]：说明控制器、PLL、延时和主电路必须联合分析，不能把控制系统抽空处理。

## 证据边界

本页是控制机制入口页，不给出无来源的带宽、采样周期、增益参数或“稳定有效”结论。具体控制性能必须回到对应 source、method 或 model 页面。

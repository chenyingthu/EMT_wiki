---
title: "电力系统 (Power System)"
type: topic
tags: [power-system, electric-grid, network, generation, load, operation]
created: "2026-05-06"
updated: "2026-05-06"
---

# 电力系统 (Power System)


```mermaid
graph TD
    subgraph S0[电力系统 (Power System)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[形式化表达]
        N3[关键组成]
        N4[与相关页面的关系]
        N5[开放问题]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

电力系统是由发电、输电、变电、配电、负荷以及保护控制装置构成的能量生产、传输和消费整体。在 EMT Wiki 中，它是上位主题入口，用于串联网络、设备、控制、运行和暂态现象，不替代具体方法页、模型页或测试系统页。

## EMT 中的作用

EMT 仿真把电力系统视为由网络方程、动态元件、控制器和事件逻辑共同组成的时域系统。研究对象既可以是整个系统，也可以是其中的关键子系统、接口边界或等值区域。

## 形式化表达

从系统层面看，EMT 研究通常把电力系统组织为网络方程、元件状态方程与控制方程的耦合：

$$
\mathbf{G}\mathbf{v}(t)=\mathbf{i}_{src}(t)+\mathbf{i}_{hist}(t)+\mathbf{i}_{ctrl}(t)
$$

$$
\dot{\mathbf{x}} = f(\mathbf{x}, \mathbf{v}, \mathbf{u}, t)
$$

其中 $\mathbf{v}$ 为网络节点电压，$\mathbf{x}$ 为设备和控制状态，$\mathbf{u}$ 为外部设定或离散事件输入。这个表达只用于说明“系统”在 Wiki 中的组织层次，不替代具体元件或求解方法页面。

## 关键组成

- [[power-system-network]]：网络拓扑、节点导纳、线路和等值边界。
- [[control-system]]：调节、保护、同步、限幅和模式切换逻辑。
- [[electromagnetic-transient]]：开关、故障、谐波和过电压等快速暂态现象。
- [[power-flow-calculation]]：稳态运行点与 EMT 初始化入口。
- [[steady-state-initialization]]：将稳态结果映射为时域初值。
- [[large-scale-power-system]]：系统规模扩展后的仿真复杂性。
- [[renewable-energy-integration]]：新能源接入后的系统动态变化。
- [[real-time-simulation]]：实时和硬件在环验证场景。

## 与相关页面的关系

- [[large-scale-power-system]] 关注规模扩展后的仿真与建模问题。
- [[transmission-network]] 和 [[distribution-network]] 关注不同网络层级。
- [[renewable-energy-integration]] 和 [[renewable-energy-units]] 关注新能源接入。
- [[real-time-simulation]] 和 [[hil-simulation]] 关注实时平台与闭环验证。

## 开放问题

- 如何在大规模系统中同时保留 EMT 细节和可接受计算代价。
- 如何统一系统层面的网络、控制、保护和通信建模边界。
- 如何在离线 EMT、混合仿真与实时仿真之间保持模型一致性。

## 代表性来源

- [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim]]：说明“大规模电力系统”在 EMT 语境下如何通过模型层级和接口组织来处理。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]]：说明离线大系统模型迁移到实时环境时，系统级工程边界比单一算法更关键。
- [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients]]：可用于说明系统层面相量法与 EMT 法的适用分工。

## 证据边界

本页只提供知识网络入口和概念边界。具体设备、控制器、网络模型或运行约束应回到对应页面，不在本页写成泛化的性能或能力结论。

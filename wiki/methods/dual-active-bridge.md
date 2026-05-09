---
title: "双有源桥方法 (Dual Active Bridge)"
type: method
tags: [dual-active-bridge, dab, dc-dc-converter, isolated-converter]
created: "2026-05-05"
updated: "2026-05-06"
---

# 双有源桥方法 (Dual Active Bridge)


```mermaid
graph TD
    subgraph S0[双有源桥方法 (Dual Active Bridge)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见分支]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[代表性来源]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

双有源桥（Dual Active Bridge, DAB）是带隔离高频变压器的双向 DC/DC 变换器拓扑，对应的方法问题包括其开关建模、相移控制、平均值等效和实时仿真简化。它不是乱码的实时仿真文本，也不是一般多端换流器的统称。

## EMT 中的作用

在 EMT 仿真中，DAB 方法主要用于：

- 研究高频隔离 DC/DC 接口的开关和控制动态；
- 为储能、固态变压器和多端直流接口提供设备级模型；
- 比较详细模型、聚合模型和实时等效模型的边界。

## 常见分支

- 单相移 DAB：以基础功率传输和控制分析为主；
- 多桥或三相 DAB：面向更高功率密度或多端口场景；
- 简化 EMT/平均值/小信号模型：用于系统级提速或稳定性分析。

## 关键公式

DAB 的基础功率传输关系常围绕相移角 $\phi$ 组织，例如：

$$
P \propto \frac{V_1 V_2}{\omega L} \, \phi \left(1-\frac{|\phi|}{\pi}\right)
$$

具体表达取决于调制方式和近似假设，但关键是相移控制和高频变压器漏感共同决定功率传输。

## 与相关方法的关系

- [[chb-dab]]：级联或多桥 DAB 相关背景。
- [[solid-state-transformer]]：DAB 常作为 SST 内部功率级。
- [[power-electronics-control]]：控制背景。
- [[mppt-control]]：在储能或新能源接口场景中的相关背景。
- [[dfig-offshore-wind-farm]]：新能源接口和 DC/DC 变换链路的相关背景。
- [[grid-connected-inverter]]：电力电子接口背景。

## 代表性来源

- [[high-efficiency-modeling-of-multi-layer-cascaded-dual-active-bridge-dab-units-on]]：多层级 DAB 建模背景。
- [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme]]：简化 EMT 模型背景。
- [[equivalent-modelling-method-of-single-active-network-for-fast-electromagnetic-tr]]：快速 EMT 等效背景。

## 证据边界

本页不写无来源效率、开关频率上限或最优相移结论，必须绑定具体拓扑和工况。

## 开放问题

- 当前页尚未把 DAB、MAB 和 SAB 在系统级 EMT 中的模型边界完全拆开。
- 详细模型与平均值模型的切换准则仍需回到具体 source 页确认。

---
title: "M3C 方法入口 (M3C)"
type: method
tags: [m3c, modular-multilevel-matrix-converter, lfac, converter-modeling]
created: "2026-05-05"
updated: "2026-05-06"
---

# M3C 方法入口 (M3C)


```mermaid
graph TD
    subgraph S0[M3C 方法入口 (M3C)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见关注点]
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

M3C 是 Modular Multilevel Matrix Converter 的常用缩写，常见于低频交流系统、背靠背频率变换和特殊多端交流接口场景。在 EMT Wiki 中，本页作为 M3C 建模方法入口，承接缩写型链接并说明其与普通 MMC、VSC 或机电相量模型的边界。

## EMT 中的作用

M3C 建模通常用于分析：

- 模块化多电平矩阵换流器的桥臂和端口动态；
- 不同频率系统之间的交流-交流能量交换；
- 低频交流系统中的控制和稳定性问题；
- M3C 与常规 MMC/VSC 在拓扑和控制上的差异。

## 常见关注点

- 输入/输出侧不同频率之间的能量交换；
- 桥臂储能和端口功率平衡；
- 多坐标系控制与端口约束耦合；
- 与 LFAC 或背靠背 AC/AC 接口场景的模型层级匹配。

## 关键公式

M3C 没有单一“通用公式”，但其核心仍是桥臂能量、电压和电流在输入/输出侧之间的耦合关系。实际建模通常需要结合坐标变换、桥臂约束和控制参考组织状态方程。

为了强调其多端口本质，可把端口功率平衡抽象写为：

$$
P_{in} - P_{out} = \frac{dW_{arm}}{dt} + P_{loss}
$$

其中 $W_{arm}$ 表示桥臂储能。这个表达不替代具体状态空间模型，但有助于说明 M3C 与普通两端口 VSC 的差异。

## 与相关方法的关系

- [[mmc-model]]：M3C 与普通 MMC 共享多电平桥臂思想，但端口和控制目标不同。
- [[vector-control]]：M3C 场景中常需要多坐标系或多频率控制组织。
- [[multi-terminal-dc]]：虽然应用对象不同，但可作为多端能量交换的对比背景。
- [[mbsm]]：若页面使用多桥臂统一表示思路，可与该框架关联。
- [[electromechanical-transient]]：M3C 也可能出现在比纯 EMT 更慢的混合系统研究中。
- [[power-system-network]]：M3C 与低频交流系统或换流端口网络接口紧密相关。

## 代表性来源

- [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular]]：说明 M3C 在 LFAC 系统中的建模与仿真背景。
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]：可作为多频/多端接口建模的相关背景来源。
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]：提醒多电平换流器稳定性分析不能脱离控制与主电路动态。

## 适用边界与失败模式

- 适用于研究多电平矩阵换流器及其低频交流接口问题。
- 若把 M3C 简化成普通 MMC 或 VSC，可能丢失输入/输出侧频率耦合特性。
- 机电暂态和 EMT 场景中的模型层级不同，不能把一个层级的结论直接外推到另一个层级。

## 证据边界

本页作为缩写入口，不把机电暂态、潮流算法或控制策略的细节写成通用 M3C 结论。具体模型形式应绑定系统频率、端口配置和来源。

## 开放问题

- 当前页尚未继续拆分 M3C 在 LFAC、背靠背频率变换和特殊 AC/AC 接口中的不同建模重点。
- EMT 与机电暂态层级下的 M3C 模型边界，后续仍需在相邻页面中继续细化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |

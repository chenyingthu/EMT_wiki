---
title: "锁相环方法 (Phase-Locked Loop)"
type: method
tags: [phase-locked-loop, pll, synchronization, inverter-control, grid-following]
created: "2026-05-04"
updated: "2026-05-07"
---

# 锁相环方法 (Phase-Locked Loop)


```mermaid
graph TD
    subgraph S0[锁相环方法 (Phase-Locked Loop)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见分支]
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

锁相环（Phase-Locked Loop, PLL）是在电力电子并网控制中用于估计电网相位、频率和同步坐标的基础方法。它常出现在跟网型逆变器、同步检测、电压定向控制和小信号稳定性分析场景。

本页讨论的是 PLL 作为同步机制的建模与稳定性边界，不把输电线路相域模型、同步机等效或任意频率控制策略误写成 PLL 方法本身。

## EMT 中的作用

在 EMT 仿真中，PLL 方法主要用于：

- 生成并网控制所需的相位角和频率估计；
- 分析故障、弱网和不平衡工况下的同步稳定性；
- 研究 PLL 与电流环、外环控制和网络阻抗的耦合；
- 为 GFL 逆变器的小信号与暂态响应提供同步背景。

## 常见分支

- SRF-PLL：同步旋转坐标系锁相环。
- DSOGI-PLL：通过正交信号生成改进不平衡和谐波工况下的同步能力。
- 自适应带宽 PLL：在暂态下动态调整带宽以改善响应。
- 增强型 PLL 稳定性模型：关注 PLL 与网络交互导致的失稳机制。

## 关键公式

PLL 的最小同步误差关系常围绕相位误差组织，例如：

$$
\theta_{err} = \theta_{grid} - \theta_{pll}
$$

在同步旋转坐标系实现中，PLL 通常通过误差信号和环路滤波器更新估计频率与角度。具体控制形式取决于 SRF、DSOGI 或其他结构，但关键始终是“同步误差如何反馈到角频率估计”。

## 与相关方法的关系

- [[pll-design]]：关注 PLL 参数和带宽整定问题。
- [[frequency-control]]：PLL 会影响频率测量与控制实现，但不等同于频率控制本身。
- [[grid-connected-inverter]]：GFL 并网设备的典型同步背景。
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：改进 DSOGI-PLL 的直接来源背景。
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：PLL 失稳机理的相关来源。

## 适用边界与失败模式

- 适用于需要从电网电压中提取同步角和频率的并网控制场景。
- 弱网、故障、不平衡和谐波会显著影响 PLL 动态。
- PLL 参数、带宽和滤波结构不当时，可能与网络阻抗或外环控制耦合失稳。
- 某一类 PLL 的结论不能直接外推到所有同步结构。

## 代表性来源

- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：DSOGI-PLL 暂态改进背景。
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：PLL 与网络交互失稳背景。
- [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型]]：说明 PLL 参数对交直流系统稳定性的影响背景。

## 证据边界

本页不写无来源的带宽、RMSE、SCR 临界值或统一最优 PLL 结构。具体结论必须绑定控制结构、网络强度和验证工况。

## 开放问题

- 当前页尚未继续拆分 GFL 场景中的 PLL 与其他同步机制的边界。
- PLL 的 EMT 作用与小信号作用如何统一表述，后续仍需在相邻页面中继续细化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir|Characteristic Analysis of High-frequency Resonance of Flexi]] | 2022 |

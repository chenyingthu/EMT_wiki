---
title: "同步旋转坐标系锁相环方法 (SRF-PLL)"
type: method
tags: [srf-pll, pll, synchronization, grid-following, inverter-control]
created: "2026-05-04"
updated: "2026-05-07"
---

# 同步旋转坐标系锁相环方法 (SRF-PLL)

## 定义与边界

SRF-PLL（Synchronous Reference Frame PLL）是并网变流器中经典的同步方法之一，通过将电网电压变换到同步旋转坐标系并消除 q 轴误差来估计相位和频率。

本页讨论的是 SRF-PLL 作为具体 PLL 分支的边界，不把一般 PLL 总入口、线路模型或无关惯量控制方法混写进来。

## EMT 中的作用

在 EMT 仿真中，SRF-PLL 主要用于：

- 为跟网型逆变器提供相位角和频率估计；
- 研究弱网、故障和不平衡工况下的同步性能；
- 作为 DSOGI-PLL、改进 PLL 和失稳分析的基准同步结构；
- 连接同步方法页与并网控制页。

## 常见特征

- 基于 dq 坐标系误差调节；
- 带宽和阻尼参数直接影响同步动态；
- 对谐波、不平衡和弱网阻抗较敏感；
- 常被用作更复杂 PLL 结构的对照基线。

## 关键公式

SRF-PLL 的核心误差可抽象写为：

$$
v_q \rightarrow 0
$$

即通过控制估计角速度，使同步旋转坐标系下的 q 轴电压收敛到零，从而完成对电网相位的锁定。

## 与相关页面的关系

- [[phase-locked-loop]]：PLL 总入口。
- [[pll-design]]：PLL 参数整定背景。
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：改进 DSOGI-PLL 的对照背景。
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：PLL 与网络交互失稳背景。
- [[grid-connected-inverter]]：跟网并网控制背景。

## 代表性来源

- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：SRF-PLL 与网络失稳相关背景。
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：SRF-PLL 与 DSOGI-PLL 对照背景。
- [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver]]：换流器控制参数设计中的同步环背景。

## 证据边界

本页不写无来源带宽、阻尼、RMSE 或统一 SCR 适用结论。具体结论必须绑定网络强度、故障类型和控制实现。

## 开放问题

- 当前页尚未继续细分 SRF-PLL 在弱网、谐波和不平衡工况下的改造路线。
- 与 DSOGI-PLL、观测器型同步器之间的适用边界，后续仍需在相邻页面中继续细化。

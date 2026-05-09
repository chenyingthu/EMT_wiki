---
title: "Beerten 2012 Mtdc Powerflow"
type: method
tags: [beerten-2012-mtdc-powerflow]
created: "2026-05-04"
---

# Beerten 2012 Mtdc Powerflow

## 定义与边界

`Beerten 2012 Mtdc Powerflow` 是围绕多端直流系统稳态潮流建模的来源型入口，而不是独立于 [[power-flow-calculation]] 或 [[multi-terminal-dc]] 的完整方法页。当前页面此前混入了动态相量、时域变换和通用 EMT 加速模板内容；这些内容与该标题不匹配，已收敛为受控入口。

本页只说明链接和证据边界：MTDC power flow 用于确定交直流混合系统运行点，可服务于 EMT 初始化，但本身不替代时域 EMT 求解、换流器详细控制模型或直流故障暂态分析。

## 核心机制

MTDC 稳态潮流的核心是求解交流系统和直流网络的联合功率平衡方程。对于 $N$ 节点 MTDC 网络，第 $i$ 个直流节点的功率 mismatch 可写为：

$$
\Delta P_{dc,i} = V_{dc,i} \sum_{j=1}^{N} G_{ij} V_{dc,j} - P_{dc,i}^{\text{spec}} = 0
$$

其中 $V_{dc,i}$ 为节点 $i$ 的直流电压，$G_{ij}$ 为直流网络电导矩阵元素，$P_{dc,i}^{\text{spec}}$ 为该节点换流站注入直流网络的有功功率设定值（由换流站控制方式和 AC/DC 接口方程确定）。该方程与交流系统潮流方程交替或统一求解，得到交直流混合系统的稳态运行点，作为 EMT 仿真的初始条件。

## 概念边界

- [[power-flow-calculation]]：潮流方程、PQ/PV/平衡节点和稳态相量求解的通用入口。
- [[power-flow-calculation]]：通用 Power Flow 链接锚点，用于把泛化链接导向正式潮流方法页。
- [[multi-terminal-dc]]：多端直流系统的网络、控制和保护方法边界。
- [[cigre-b4-dc-grid]]：可作为 MTDC/CIGRE B4 场景入口，而不是 Beerten 论文的替代页面。

## 链接用法

需要讨论 MTDC 稳态运行点或 AC/DC 顺序潮流算法时，可链接本页作为来源型入口；需要介绍潮流方法本身时，应链接 [[power-flow-calculation]]。需要讨论 EMT 初始化时，应链接具体初始化来源或 [[emt-simulation]]。

## 代表性来源

- [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]]：说明 MTDC EMT 初始化会依赖潮流运行点，但重点是初始化方法而非 Beerten 2012 本身。
- [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40]]：包含 CIGRE B4 多端直流测试系统与多尺度暂态建模背景。
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]：说明大型 AC 与 MMC-MTDC 系统的 EMT 协同仿真背景；不能作为稳态潮流推导的直接证据。

## 证据边界

当前本地页面没有可核验的 Beerten 2012 原文推导、算例表或算法步骤，因此不写具体 AC/DC 顺序潮流方程、收敛性结论或性能指标。后续若要扩写，应先补充对应 source 页或原文证据，再决定是否仍需要独立页面。

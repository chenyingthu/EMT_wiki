---
title: "Haileselassie 2012 Mtdc Control"
type: method
tags: [haileselassie-2012-mtdc-control]
created: "2026-05-04"
---

# Haileselassie 2012 Mtdc Control

## 定义与边界

本页是 `Haileselassie 2012 Mtdc Control` 这个来源型链接的受控入口。当前本地 Wiki 没有可核验的同名 source 页、原文摘要或算例表，因此不在这里重建具体控制律、参数或性能结论。

页面标题指向多端直流系统控制语境；它不应与构网型光储黑启动控制、通用 EMT 加速模板或储能逆变器惯量控制混写。

## 核心机制

MTDC 系统控制的核心是换流站间的功率-电压协调。以下垂控制为例，第 $i$ 个换流站的直流电压-功率特性可写为：

$$
P_i = P_{i,	ext{ref}} + K_i (V_{dc,	ext{ref}} - V_{dc,i})
$$

其中 $P_i$ 和 $V_{dc,i}$ 为实测功率和直流电压，$P_{i,	ext{ref}}$ 和 $V_{dc,	ext{ref}}$ 为参考值，$K_i$ 为下垂系数。$K_i$ 的大小决定了换流站参与直流电压调节的权重。多端系统中各站下垂系数的整定需要在动态响应速度和稳态功率分配精度之间取得平衡。

## 链接用法

需要讨论多端直流系统的控制、换流站协调或 EMT 初始化背景时，可把本页作为临时来源型入口；需要展开正式概念时优先使用：

- [[multi-terminal-dc]]：多端直流系统的网络、控制和保护边界。
- [[hvdc-control]]：HVDC 控制方法的通用入口。
- [[vsc-control]]：电压源换流器控制结构入口。
- [[mtdc-model]]：多端直流系统建模入口。
- [[emt-simulation]]：用于确认时域 EMT 语境，而不是稳态潮流本身。
- [[power-flow-calculation]]：用于区分运行点求解和控制动态验证。

## 适用边界与失败模式

- **valid_when**: VSC-MTDC 系统，各站采用电压下垂或主从控制；直流网络结构已知，站间通信延迟在可控范围内。
- **invalid_when**: LCC 主导的多端系统存在换相失败风险；弱交流系统下 VSC 注入功率受限时下垂特性可能无法保持；通信严重延迟或丢失会导致主从控制的可靠性问题。
- **assumptions**: 假设各站直流电压在额定值附近运行，下垂控制在小信号范围内近似线性（据方法推断）。
- **evidence_gaps**: Haileselassie 2012 原文的具体控制参数、算例系统和验证指标尚未在本地建立 source 页证据。

## 证据边界

- 当前页面不保留无来源的公式、仿真步长、误差、实时性或稳定性断言。
- 若后续找到 Haileselassie 2012 的正式 source 页，应先在 source 页中记录作者、题名、算例和控制结构，再决定是否把本页扩展为论文入口。
- 在证据补齐前，本页只承担断链收束和概念路由功能。

## 代表性来源

- [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems]]：说明 MTDC EMT 初始化会依赖运行点与控制状态，但不是 Haileselassie 2012 的替代证据。
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]：说明大型 AC 与 MMC-MTDC 系统的 EMT 协同仿真背景；不能作为同名控制论文的直接证据。

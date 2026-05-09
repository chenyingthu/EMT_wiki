---
title: "Ould Bachir 2019 Unified Avm"
type: method
tags: [ould-bachir-2019-unified-avm]
created: "2026-05-04"
---

# Ould Bachir 2019 Unified Avm

## 定义与边界

本页是 `Ould Bachir 2019 Unified Avm` 这个来源型链接的受控入口。当前页面原先混入了通用 EMT 模板、无来源性能指标和不完整状态空间公式；本地证据尚不足以确认同名论文的作者、题名、拓扑和验证算例。

在概念上，它应归入 [[average-value-model]] 和 MMC 平均值建模语境，而不是独立扩展为新的通用方法页。若要讨论 MMC-ES、VSC-HVDC 或 LCC-HVDC 的具体 AVM，应优先链接已有 source 页和 canonical 方法页。

## 核心机制

统一平均值模型的核心是将 MMC 桥臂的开关函数在工频周期内取平均，获得连续的状态空间表示。桥臂平均值方程可写为：

$$
rac{d}{dt} egin{bmatrix} i_{	ext{arm}} \ v_{c,	ext{avg}} \end{bmatrix} = egin{bmatrix} -R_{	ext{arm}}/L_{	ext{arm}} & -m(t)/L_{	ext{arm}} \ m(t)/C_{	ext{eq}} & 0 \end{bmatrix} egin{bmatrix} i_{	ext{arm}} \ v_{c,	ext{avg}} \end{bmatrix} + egin{bmatrix} v_{	ext{dc,arm}} / L_{	ext{arm}} \ 0 \end{bmatrix}
$$

其中 $m(t)$ 为调制信号（平均值意义下的占空比），$R_{	ext{arm}}, L_{	ext{arm}}$ 为桥臂电阻和电感，$C_{	ext{eq}}$ 为子模块等效电容。该 AVM 忽略了开关谐波和子模块电容电压纹波，但在系统级 EMT 仿真中能够以较低的代价准确复现 MMC 的端口外特性。

## 链接用法

- [[average-value-model]]：平均值模型的正式方法入口。
- [[mmc-model]]：MMC 设备和建模对象入口。
- [[mmc-modeling]]：MMC 建模路线综述入口。
- [[state-space-average-method]]：平均化状态空间推导的相邻方法页。

## 适用边界与失败模式

- **valid_when**: 系统级 EMT 仿真关注 MMC 端口的基波有功/无功交换和直流侧动态；开关频率远高于控制带宽；子模块电容电压平衡良好。
- **invalid_when**: 需要评估子模块级故障（子模块旁路、电容电压不均衡、开关管短路/开路）；MMC 工作在极端调制比（过调制）；高频谐波交互影响显著。
- **assumptions**: 假设子模块电容电压在工频周期内近似恒定，开关函数可用连续占空比代替（据方法推断）。
- **evidence_gaps**: Ould Bachir 2019 原文的 AVM 公式推导、与详细模型的误差对比和适用边界尚未在本地建立 source 页证据。

## 证据边界

- 当前页不保留原先的整流侧准稳态公式、误差百分比、实时性、步长或收敛性断言，因为它们没有与 `Ould Bachir 2019 Unified Avm` 的本地 source 证据绑定。
- 已有来源页可支撑“MMC/变流器 AVM 是一类系统级 EMT 等效方法”，但不能支撑本页标题对应的特定论文细节。
- 后续若找到正式 source 页，应先补齐论文对象、状态变量、接口方程、验证基线和失败边界，再决定是否扩写本页。

## 代表性来源

- [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage]]：代表含储能 MMC 的多阀臂级 AVM；不等同于 Ould Bachir 2019。
- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]：代表 VSC-HVDC 网格中 MMC AVM 的适用性与故障边界。
- [[dynamic-averaged-and-simplified-models-for]]：代表动态平均与简化模型路线；具体对象需回到该 source 页核查。

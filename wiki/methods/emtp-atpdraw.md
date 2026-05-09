---
title: "Emtp Atpdraw"
type: method
tags: [emtp-atpdraw]
created: "2026-05-04"
---

# Emtp Atpdraw

## 定义与边界

`emtp-atpdraw` 是 ATP/ATPDraw 相关链接的受控入口，不再作为独立方法页扩写。ATP/ATPDraw 在本 Wiki 中应主要归入 [[atp-emtp]] 工具页；若讨论商业 EMTP/EMTP-RV 生态，应转向 [[emtp]]。

本页只用于收敛旧链接和拼写变体。它不承载 ATPDraw 的安装、版本、许可或完整元件库说明，也不把“使用 ATP/ATPDraw 仿真”写成论文方法贡献。

## 概念边界

- [[atp-emtp]]：ATP/ATPDraw 的主要工具入口，适合说明 Dommel 型 EMT 求解、TACS/MODELS、线路模型和复现实验规则。
- [[emtp]]：EMTP/EMTP-RV 工具生态入口，适合承接商业 EMTP-RV 和 EMTP 家族算法背景。
- [[pscad-emtdc]]：另一个常见 EMT 工具平台，只能作为对比工具或验证环境，不应与 ATPDraw 混写成同一平台。

若来源页只说模型“在 ATP/ATPDraw 中实现”，应把 ATPDraw 视为实现和仿真环境；真正的技术对象通常是逆变器等值、线路模型、保护逻辑或控制策略。

## 核心机制

ATP/ATPDraw 的底层求解引擎与 EMTP 一致，均基于 Dommel 的伴随电路法。其梯形数值积分将储能元件离散为诺顿等效电路：

$$
\mathbf{G} \mathbf{v}(t) = \mathbf{i}(t) - \mathbf{i}_{	ext{hist}}(t - \Delta t)
$$

其中 $\mathbf{G}$ 为恒定导纳矩阵（在固定步长下只需要三角分解一次），$\mathbf{i}_{	ext{hist}}$ 为历史电流源向量，由前一时步的电压电流推算。ATPDraw 作为图形化前端，负责将元件拓扑和参数翻译为 ATP 输入文件（.atp 或 .adp），求解过程仍由 ATP 或 ATP 兼容求解器完成。

## 链接用法

优先链接 [[atp-emtp]]。只有当原文题名、摘要或模型实现明确写作 ATP/ATPDraw 时，才保留到本页的链接，作为别名入口。

推荐写法：

- “该模型在 [[atp-emtp|ATP/ATPDraw]] 中实现。”
- “ATPDraw 是图形化建模入口；模型边界见 [[atp-emtp]]。”

避免写法：

- “ATPDraw 证明该方法通用有效。”
- “ATPDraw 与所有 EMTP 工具完全兼容。”
- “使用 ATPDraw 即可得到高精度实时仿真。”

## 代表性来源

- [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]]：在 ATP/ATPDraw 中实现跟网型逆变器等效模型；可支撑“ATPDraw 作为实现环境”的说法。
- [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software]]：适合作为 ATP 软件中线路模型实现的来源入口。
- [[atp-emtp]]：工具层面的主要综述入口。

## 证据边界

本页不提供 ATPDraw 的官方功能声明、版本能力、许可结论或性能指标。需要这些信息时，应查工具官方资料；当前 Wiki 内部证据只能支持“若干来源在 ATP/ATPDraw 中实现或对比了模型”这一有限结论。

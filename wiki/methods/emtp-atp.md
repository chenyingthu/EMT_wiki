---
title: "Emtp Atp"
type: method
tags: [emtp-atp]
created: "2026-05-04"
---

# EMTP-ATP

## 定义与边界

EMTP-ATP 是 ATP 版 EMTP 的工具名/生态名入口，不是独立数值方法页。当前 Wiki 已有工具实体 [[atp-emtp]] 和 [[emtp]]；本页仅作为旧的 method 路径下的受控入口，防止 `emtp-atp` 链接扩展成与工具实体并行的完整文章。

## 概念边界

- 讨论 ATP 作为仿真平台、ATPDraw、TACS/MODELS、输入文件或复现实验时，应优先链接 [[atp-emtp]]。
- 讨论 EMTP / EMTP-RV 工具生态、Dommel 型程序或商业工具边界时，应链接 [[emtp]]。
- 讨论伴随电路、梯形积分、节点分析或输电线路模型时，应链接对应方法页，而不是把工具名当作方法贡献。
- 本页不保留旧页面中错误混入的线路模型公式、通用工程价值、泛化未来方向或无来源性能数字。

## 核心机制

EMTP-ATP 的核心求解方法是 Dommel 提出的伴随电路法（companion circuit），它将微分方程通过梯形数值积分离散化为等效电阻网络。以电感 $L$ 为例：

$$
i_L(t) = rac{\Delta t}{2L} v_L(t) + i_{	ext{hist}}(t - \Delta t), \quad i_{	ext{hist}}(t - \Delta t) = i_L(t - \Delta t) + rac{\Delta t}{2L} v_L(t - \Delta t)
$$

其中 $\Delta t$ 为仿真步长。所有储能元件的伴随电路合并到节点导纳矩阵 $\mathbf{G}$ 中，每一时步求解线性方程组 $\mathbf{G} \mathbf{v}(t) = \mathbf{i}(t)$，同时处理开关、非线性和控制系统的接口。

## 链接用法

旧页面若已有 `[[emtp-atp]]` 链接，可保留作为兼容锚点。新写页面中，工具平台应直接链接 [[atp-emtp]] 或 [[emtp]]；跨工具对比可链接 [[comparison-of-the-atp-version-of-the-emtp-and-the-netomac-program-for-simulation]]；EMTP 型算法说明应使用 [[companion-circuit]]、[[trapezoidal-rule]]、[[nodal-analysis]] 或 [[transmission-line-model]]。

## 代表性来源

- [[atp-emtp]]：ATP-EMTP 工具实体页，是本入口的 canonical target。
- [[emtp]]：EMTP / EMTP-RV 工具实体页，用于更广义的 EMTP 生态说明。
- [[comparison-of-the-atp-version-of-the-emtp-and-the-netomac-program-for-simulation]]：支撑 ATP 版 EMTP 与 NETOMAC 的 HVDC 仿真程序对比；其年份和具体数值应回源核对。
- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]]：可作为 EMTP 型电磁暂态建模传统的来源入口。
- [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation]]：可作为 EMTP-RV 图形软件使用语境的来源入口。

## 证据边界

本页不判断 ATP、EMTP-RV、NETOMAC 或其他工具的普遍优劣。工具相关结论必须说明软件版本、模型输入、步长、开关处理、控制接口和对比基线；只写“使用 ATP/EMTP 仿真”不能证明模型本身正确或可复现。

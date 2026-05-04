---
title: "变压器建模 (Transformer Modeling)"
type: topic
tags: [transformer, saturation, inrush, internal-fault, winding, white-box, black-box]
created: "2026-05-01"
---

# 变压器建模 (Transformer Modeling)

## 定义与边界

变压器建模是在 EMT 中表示绕组、电阻漏抗、磁化支路、铁芯饱和、绕组连接、分接头、频率相关效应和内部故障的建模工作。它不是单一“精确模型”问题；不同研究对象需要不同层级，例如理想变压器、饱和模型、白箱模型、黑箱频域模型或多物理场模型。

本页是 topic 页，关注变压器建模路线和证据边界。具体元件模型可阅读 [[transformer-model]]、[[multi-winding-transformer]]、[[ideal-transformer-equivalent]] 和 [[magnetic-saturation-modeling]]。

## EMT 中的作用

变压器模型影响以下 EMT 现象：

- 合闸涌流、剩磁、饱和和铁磁谐振。
- 内部故障、差动保护、励磁支路和 CT/PT 暂态。
- 雷电冲击、VFTO 和绕组电压分布等高频暂态。
- 换流变压器、移相变压器和多绕组设备与 HVDC、FACTS、MMC 的接口。

## 主要分支与机制

- 低频等值：用理想变比、漏抗和磁化支路表示工频及低频暂态，适合系统级 EMT 的基础模型。
- 饱和与磁滞：用单值磁化曲线、Jiles-Atherton、Preisach 或磁等效电路描述铁芯非线性；参数和剩磁假设决定涌流结论。
- 白箱模型：从绕组几何、材料和连接结构推导电感、电容和电阻矩阵，适合内部故障和高频电压分布。
- 黑箱/频域模型：从端口频响或测量数据拟合等值，适合系统级宽频仿真，但内部物理解释有限。
- 实时模型：为 HIL 或实时平台简化状态和矩阵结构，必须报告丢失的频带和非线性细节。

## 形式化表达

变压器 EMT 模型的基本端口关系可以写为：

$$
v = R i + \frac{d\psi(i,x_m)}{dt},\qquad
i_{\mathrm{port}}=Y_{\mathrm{eq}}v_{\mathrm{port}}+i^{\mathrm{hist}}
$$

其中 $\psi(i,x_m)$ 表示可能包含饱和、磁滞和剩磁状态的磁链，$Y_{\mathrm{eq}}$ 是离散后进入网络方程的等效导纳。白箱模型通常扩展为多绕组、多电容和多端口矩阵；黑箱模型则通过频域端口响应近似同一接口。

## 适用边界与失败模式

- 无来源的涌流倍数、误差百分比、实时步长和频率上限不应写成通用结论；它们依赖设备、剩磁、合闸角、模型和测试系统。
- 理想变压器或线性漏抗模型不能支撑饱和、涌流、内部故障和高频绕组电压结论。
- 黑箱频域模型若未检查无源性，可能在 EMT 时域中产生非物理能量。
- 内部故障和绕组电压分布需要结构参数；仅有端口模型通常不足。

## 代表性来源

- [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien]] 支撑磁滞变压器模型来源入口。
- [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t]] 可作为紧凑白箱模型来源入口。
- [[interfacing-factor-based-white-box-transformer-modeling-method]] 支撑白箱模型与系统级仿真的接口讨论。
- [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag]] 支撑基于测量的 HVDC 变压器频变模型讨论。
- [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag]] 可作为非线性磁等效电路和实时模型来源入口。

## 与相关页面的关系

- [[magnetic-saturation-modeling]] 专注铁芯饱和和非线性。
- [[frequency-dependent-modeling]] 和 [[vector-fitting]] 说明频域响应进入 EMT 的方法。
- [[differential-protection]] 和 [[protection-relay-modeling]] 需要变压器涌流、内部故障和 CT/PT 边界。
- [[finite-element-method]] 可用于白箱或局部场模型参数提取。

## 开放问题

- 如何在工程保密条件下共享足够的绕组和磁路信息以验证高频模型。
- 如何统一饱和、磁滞、剩磁和涌流的参数辨识流程。
- 如何在实时仿真中保留关键非线性而不破坏 deadline。

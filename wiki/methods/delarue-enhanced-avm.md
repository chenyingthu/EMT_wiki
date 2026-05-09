---
title: "Delarue 增强平均值模型"
type: method
tags: [delarue-enhanced-avm, mmc, average-value-model, blocking, fault]
created: "2026-05-05"
updated: "2026-05-06"
---

# Delarue 增强平均值模型

## 定义与边界

Delarue 增强平均值模型通常指围绕 MMC 闭锁、故障续流或模式切换精度进行改进的平均值建模路线。它的重点不是通用 AVM，而是在闭锁、二极管续流或桥臂电流初始化等特定工况下提升平均值模型的物理一致性。

## EMT 中的作用

在 EMT 仿真中，这类增强 AVM 主要用于：

- 保留 MMC 在故障和闭锁工况下的关键动态；
- 在系统级仿真中替代过慢的详细开关模型；
- 减少模式切换时的电流跳变和数值振荡。

## 常见增强点

- 闭锁后续流路径的更真实表示；
- 桥臂电流和内部状态的更合理初始化；
- 故障/解锁切换时的模式连续性处理；
- 在系统级 EMT 中保留关键物理约束而不过度回退到详细开关模型。

## 关键公式

增强 AVM 的核心通常是为桥臂电流或等效支路增加更合理的初始化/续流约束，例如：

$$
i_{arm}(t_0^+) = i_{fault}(t_0^-)/3
$$

具体公式取决于桥臂等效结构，但关键思想是让模式切换前后的桥臂状态更连续。

## 与相关方法的关系

- [[average-value-model]]：一般平均值模型入口。
- [[mbsm]]：统一子模块/桥臂等效背景。
- [[mmc-model]]：整机层应用背景。
- [[dc-protection]]：故障与闭锁工况背景。
- [[fbsm]]：多电平桥臂/子模块动态背景。
- [[current-injection]]：等效电流注入接口背景。

## 代表性来源

- [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep]]：增强型 AVM 的直接背景来源。
- [[enhanced-high-speed-electromagnetic-transient-simulation]]：增强高效 EMT 模型背景。

## 证据边界

本页不写无来源精度提升倍数或统一适用范围，具体效果必须绑定对比基线和故障工况。

## 开放问题

- 当前页尚未把 Delarue 路线与其他 MMC 增强 AVM 明确拆分比较。
- 闭锁、故障续流和正常运行 3 类工况下的统一精度边界仍需落到具体 source 页。

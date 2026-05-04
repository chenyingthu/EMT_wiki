---
title: "无源性保证 (Passivity Enforcement)"
type: method
tags: [passivity-enforcement, positive-real, stability, frequency-dependent]
created: "2026-05-04"
---

# 无源性保证 (Passivity Enforcement)

## 定义与边界

无源性保证是指在频变参数建模过程中，确保所得模型满足无源性条件的技术。无源系统不产生能量，仅消耗或传输能量。

## EMT中的作用

- 保证EMT仿真数值稳定性
- 确保模型物理可实现
- 无源子系统级联保持整体无源性

## 主要分支

1. 基于约束的拟合 - 在矢量拟合中直接施加无源性约束
2. 后处理修正 - 对非无源模型进行扰动修正

## 形式化表达

传递函数正实性条件：
$$Re\{H(s)\} \geq 0, \quad \forall Re\{s\} > 0$$

多端口导纳矩阵无源性：
$$\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega) \geq 0$$

## 与相关页面

- [[vector-fitting]] - 矢量拟合
- [[frequency-dependent-line-model]] - 频变线路模型

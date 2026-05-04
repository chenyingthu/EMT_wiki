---
title: "无源性保证 (Passivity Enforcement)"
type: method
tags: [passivity-enforcement, positive-real, stability, frequency-dependent, vector-fitting]
created: "2026-05-04"
---

# 无源性保证 (Passivity Enforcement)

## 定义与边界

无源性保证是指在频变参数建模过程中，确保所得模型满足无源性条件的技术。无源系统不产生能量，仅消耗或传输能量，其传递函数满足正实性条件。在EMT仿真中，无源性保证是确保频变模型（如输电线路、电缆模型）数值稳定性的关键。

**边界限定**：本方法适用于线性时不变系统的频变参数建模，非线性系统需分段线性化处理。

## EMT中的作用

- **保证EMT仿真数值稳定性**：无源模型保证仿真不会发散
- **确保模型物理可实现**：无源系统符合能量守恒定律
- **无源子系统级联保持整体无源性**：便于构建复杂系统模型
- **频变线路建模**：保证宽频模型的稳定性

## 主要分支与机制

### 1. 基于约束的拟合

在矢量拟合中直接施加无源性约束：
- 限制极点位置（左半平面）
- 约束留数保证正实性
- 优化问题带不等式约束

### 2. 后处理修正

对非无源模型进行扰动修正：
- 识别非无源频段
- 局部扰动修正
- 保持拟合精度

## 形式化表达

### 传递函数正实性条件

$$Re\{H(s)\} \geq 0, \quad \forall Re\{s\} > 0$$

### 多端口导纳矩阵无源性

$$\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega) \geq 0$$

### 频域检验条件

$$Re\{H(j\omega)\} \geq 0, \quad \forall \omega$$

## 适用边界与失败模式

### 适用条件

- 系统线性时不变
- 频响数据充分
- 原始系统本身无源

### 失效边界

- **严格非无源系统**：有源系统无法强制无源
- **数据不足**：频响数据稀疏导致无法准确判断
- **高精度要求**：强制无源可能降低拟合精度

## 与相关页面的关系

- [[vector-fitting]] - 矢量拟合方法
- [[frequency-dependent-line-model]] - 频变线路模型
- [[wideband-modeling]] - 宽频建模
- [[transmission-line-model]] - 输电线路模型
- [[cable-model]] - 电缆模型

## 代表性来源

- Gustavsen, B. and Semlyen, A., "Enforcing Passivity for Admittance Matrices Approximated by Rational Functions," *IEEE TPWRD*, 2001.
- Triverio, P., "Passivity Enforcement of Rational Models of Frequency Domain Responses," *IEEE TCPMT*, 2015.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

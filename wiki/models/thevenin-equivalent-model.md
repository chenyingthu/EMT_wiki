---
title: "戴维南等效模型 (Thevenin Equivalent Model)"
type: model
tags: [thevenin-equivalent, voltage-source, impedance, network-equivalent, linear-circuit]
created: "2026-05-04"
---

# 戴维南等效模型 (Thevenin Equivalent Model)

## 定义与边界

戴维南等效模型是将任意线性有源二端网络简化为理想电压源$V_{th}$与串联内阻抗$Z_{th}$的电路表示。该等效保持端口电压-电流关系不变，是电路分析、网络简化和多速率仿真的基础工具，与诺顿等效互为对偶。

**边界限定**：本模型仅适用于线性时不变网络，非线性网络需在工作点线性化后应用。

## EMT中的作用

戴维南等效是EMT网络简化的核心技术：

- **外部系统等值**：将复杂外部网络简化为戴维南等值
- **多速率接口**：不同步长子系统间的等效接口
- **开关分析**：简化开关状态组合分析
- **故障计算**：故障点戴维南等效简化计算
- **保护整定**：简化网络用于保护配合

## 主要分支与机制

### 1. 戴维南等效参数求解

**开路电压法**：
$$V_{th} = V_{oc}$$

将端口开路，测量开路电压。

**等效阻抗法**：
- 独立电压源短路、电流源开路
- 从端口看入的等效阻抗

$$Z_{th} = \frac{V_{oc}}{I_{sc}}$$

### 2. 与诺顿等效转换

戴维南 $\rightarrow$ 诺顿：
$$I_N = \frac{V_{th}}{Z_{th}}, \quad Y_N = \frac{1}{Z_{th}}$$

诺顿 $\rightarrow$ 戴维南：
$$V_{th} = \frac{I_N}{Y_N}, \quad Z_{th} = \frac{1}{Y_N}$$

### 3. 最大功率传输

负载获得最大功率条件：
$$Z_L = Z_{th}^*$$

共轭匹配时：
$$P_{max} = \frac{|V_{th}|^2}{4R_{th}}$$

## 形式化表达

### 戴维南定理

对于任意由线性电阻、电感、电容、受控源和独立源组成的二端网络：
$$V = V_{th} - Z_{th}I$$

### 多端口戴维南等效

$m$端口网络：
$$\mathbf{V} = \mathbf{V}_{th} - \mathbf{Z}_{th}\mathbf{I}$$

$\mathbf{Z}_{th}$为$m \times m$等效阻抗矩阵。

### EMT中的应用

开关断开时的开路电压：
$$V_{open} = V_{th}$$

开关闭合时的电流：
$$I_{close} = \frac{V_{th}}{Z_{th} + Z_{switch}}$$

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 线性性 | 网络线性时不变 | 非线性需线性化 |
| 有源性 | 含独立源 | 纯无源网络的戴维南电压为零 |
| 端口明确 | 二端或已知多端口 | 端口选择影响等效精度 |
| 可求逆 | $Z_{th}$非奇异 | 特殊情况需处理 |

### 失效边界

- **纯容性/感性网络**：等效阻抗为零或无穷
- **非线性主导**：无法线性化
- **时变网络**：参数变化快于等值更新
- **磁耦合复杂**：多绕组变压器等难以简单等值

## 代表性来源

### 经典文献

- Thévenin, L., "Extension de la loi d'Ohm aux circuits électromoteurs," *Annales Télégraphiques*, 1883.
- Desoer, C.A. and Kuh, E.S., "Basic Circuit Theory," *McGraw-Hill*, 1969.

### EMT应用

- [[thevenin-norton-equivalent]] - 戴维南-诺顿综合
- [[network-equivalent]] - 网络等值方法
- [[fdne-model]] - 频变网络等值

## 与相关页面的关系

- [[thevenin-norton-equivalent]] - 等效综合
- [[network-equivalent]] - 网络等值
- [[norton-equivalent]] - 诺顿等效
- [[multirate-method]] - 多速率接口

## 开放问题

- 时变网络的自适应等值
- 大规模网络的并行等值
- 非线性网络的分段线性等值
- 多频戴维南等值

## 参考标准

- IEEE Std. 1800 - 电磁暂态仿真导则

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

---
title: "Heidler雷电流函数 (Heidler Function)"
type: method
tags: [heidler-function, lightning, return-stroke, emt, current-waveform]
created: "2026-05-04"
---

# Heidler雷电流函数 (Heidler Function)

## 定义与边界

Heidler函数是描述雷电回击电流波形的数学解析表达式，由Heidler于1985年提出。该函数能够较好地拟合实测雷电流的波前和波尾特性，是EMT仿真中雷电暂态分析的标准雷电流源模型之一，广泛应用于输电线路防雷计算和变电站过电压分析。

**边界限定**：本函数用于描述下行负地闪的回击电流，不包括云内放电或上行闪电。

## EMT中的作用

Heidler函数是雷击暂态仿真的标准输入：

- **直击雷计算**：杆塔或导线直击雷过电压
- **感应雷计算**：附近雷击的感应过电压
- **绝缘配合**：确定绝缘水平
- **保护设计**：避雷器和接地系统

## 主要分支与机制

### 1. Heidler函数表达式

**标准形式**：
$$i(t) = \frac{I_m}{\eta} \cdot \frac{(t/\tau_1)^{10}}{1 + (t/\tau_1)^{10}} \cdot e^{-t/\tau_2}$$

其中：
- $I_m$：峰值电流（kA）
- $\tau_1$：波前时间常数（μs）
- $\tau_2$：波尾时间常数（μs）
- $\eta$：峰值修正因子

**峰值修正因子**：
$$\eta = e^{-(\tau_1/\tau_2)(10\tau_2/\tau_1)^{1/10}}$$

### 2. 参数选择

**典型参数**（IEC标准）：
- 第1分量：$I_m = 30$ kA，$\tau_1 = 0.25$ μs，$\tau_2 = 2.5$ μs
- 后续分量：$I_m = 12$ kA，$\tau_1 = 0.25$ μs，$\tau_2 = 2.5$ μs

**10/350 μs波形**：
- 用于直击雷保护等级I

### 3. 扩展形式

**双指数改进**：
结合双指数函数和Heidler函数优点。

**多场点应用**：
考虑雷电通道高度变化。

## 形式化表达

### 导数计算

电流变化率：
$$\frac{di}{dt} = \frac{I_m}{\eta} \cdot \left[ \frac{10(t/\tau_1)^9}{\tau_1(1+(t/\tau_1)^{10})} - \frac{(t/\tau_1)^{20}}{\tau_1(1+(t/\tau_1)^{10})^2} - \frac{(t/\tau_1)^{10}}{\tau_2(1+(t/\tau_1)^{10})} \right] e^{-t/\tau_2}$$

### 峰值时间

峰值出现在：
$$t_{peak} \approx \tau_1(10\tau_2/\tau_1)^{1/10}$$

## 适用边界与失败模式

### 适用条件

- 下行负地闪回击
- 首回击或后续回击
- 标准雷电防护设计

### 失效边界

- **特殊雷型**：上行闪电、云内放电
- **多回击**：复杂波形难以单函数描述
- **通道效应**：未考虑通道阻抗变化

## 与相关页面的关系

- [[lightning-transient-analysis]] - 雷击暂态分析
- [[transmission-line-model]] - 输电线路模型
- [[grounding-system-model]] - 接地系统模型
- [[surge-arrester-model]] - 避雷器模型
- [[bergeron-model]] - 贝杰龙模型
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法
- [[vector-fitting]]
- [[average-value-model]]
- [[nodal-analysis]]
## 代表性来源

- Heidler, F., "Traveling Current Source Model for LEMP Calculation," *ICLP*, 1985.
- IEC 62305 - 雷电防护
- IEEE Std. 1243 - 输电线路雷电性能

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

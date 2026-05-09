---
title: "传输线理论 (Transmission Line Theory)"
type: topic
tags: [transmission-line, distributed-parameter, wave-propagation, telegraph-equation]
created: "2026-05-04"
---

# 传输线理论 (Transmission Line Theory)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT中的作用]
    N0 --> N1
    N2[核心理论]
    N1 --> N2
    N3[形式化表达]
    N2 --> N3
    N4[适用边界与失败模式]
    N3 --> N4
    N5[与相关页面的关系]
    N4 --> N5
    N6[代表性来源]
    N5 --> N6
```


## 定义与边界

传输线理论是研究电磁波在双导体或多导体系统中传播特性的理论框架，考虑分布参数效应（单位长度电阻、电感、电容、电导），适用于高频或长线分析。与集中参数电路不同，传输线理论将线路视为连续分布的电磁系统。

**边界限定**：本页面聚焦于输电线路的分布参数理论，不包括集总参数近似或低频稳态分析。

## EMT中的作用

- **输电线路电磁暂态建模基础**：EMT仿真的核心理论
- **行波传播与反射分析**：故障定位和过电压计算
- **过电压计算**：雷击和操作过电压的传播
- **频变参数建模**：宽频范围内的线路特性
- **多导体系统分析**：多回线路的耦合效应

## 核心理论

### 1. 电报方程

时域传输线方程：
$$-\frac{\partial v}{\partial x} = L\frac{\partial i}{\partial t} + Ri$$
$$-\frac{\partial i}{\partial x} = C\frac{\partial v}{\partial t} + Gv$$

### 2. 特性阻抗与传播常数

特性阻抗：
$$Z_c = \sqrt{\frac{R + j\omega L}{G + j\omega C}}$$

传播常数：
$$\gamma = \sqrt{(R + j\omega L)(G + j\omega C)} = \alpha + j\beta$$

### 3. 行波理论

电压和电流可分解为前行波和反行波：
$$v(x,t) = v^+(x - vt) + v^-(x + vt)$$

### 4. 频变参数模型

考虑集肤效应和大地返回路径的频率依赖特性。

## 形式化表达

### 行波速度

$$v = \frac{1}{\sqrt{LC}} \approx \frac{c}{\sqrt{\varepsilon_r}}$$

架空线典型值：$v \approx 3 \times 10^8$ m/s

### 无损线简化

当$R=0, G=0$时：
$$Z_c = \sqrt{\frac{L}{C}}$$
$$\gamma = j\omega\sqrt{LC}$$

### 反射系数

在阻抗不连续点：
$$\Gamma = \frac{Z_L - Z_c}{Z_L + Z_c}$$

## 适用边界与失败模式

### 适用条件

- 线路长度大于波长（或大于几十公里）
- 关心暂态过程
- 频率足够高（>1kHz）
- 分布参数效应显著

### 失效边界

- **短线路**：可用集总参数模型简化
- **极低频**：稳态分析无需行波理论
- **非均匀线路**：需要分段建模
- **非线性效应**：如铁磁谐振需特殊处理

## 与相关页面的关系

- [[transmission-line-model]] - 输电线路模型
- [[bergeron-model]] - 贝杰龙模型
- [[frequency-dependent-line-model]] - 频变线路模型
- [[wideband-modeling]] - 宽频建模
- [[distributed-parameter-line]] - 分布参数线路
- [[electromagnetic-transient]] - 电磁暂态
- [[power-system-network]] - 电力系统网络
- [[emt-simulation]]
- [[real-time-simulation]]
- [[co-simulation]]
## 代表性来源

- Dommel, H.W., "Digital Computer Solution of Electromagnetic Transients in Single-and Multiphase Networks," *IEEE PAS*, 1969.
- Wedepohl, L.M., "Application of Matrix Methods to the Solution of Travelling-Wave Phenomena in Polyphase Systems," *Proc. IEE*, 1963.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |

---
title: "频率响应方法 (Frequency Response)"
type: method
tags: [frequency-response, impedance, transfer-function, bode, resonance]
created: "2026-05-05"
updated: "2026-05-06"
---

# 频率响应方法 (Frequency Response)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 -->|Nf1| N1
    N2[关键公式]
    N1 -->|Nf2| N2
    N3[与相关方法的关系]
    N2 -->|Nf3| N3
    N4[适用边界与失败模式]
    N3 -->|Nf4| N4
    N5[代表性来源]
    N4 -->|Nf5| N5
```


## 定义与边界

频率响应方法是通过频率变化下的增益、相位、阻抗或导纳特性来分析系统动态行为的技术路线。它常用于谐振识别、阻抗稳定性、控制器设计和模型等效验证。

本页讨论的是“频率响应”这一上位分析方法，不把矢量拟合、电压依赖负荷或其他单篇论文模型直接当成整个方法本身。

## EMT 中的作用

在 EMT 研究中，频率响应方法主要用于：

- 分析换流器、电网和控制器之间的阻抗耦合；
- 识别谐振峰、带宽和相位裕度；
- 为 [[frequency-scan]]、[[impedance-measurement]] 和 [[vector-fitting]] 提供共同分析背景；
- 检查模型等效在频域上的保真程度。

## 关键公式

频率响应最常通过传递函数或阻抗函数表示：

$$
G(j\omega)=\frac{Y(j\omega)}{U(j\omega)}, \qquad Z(j\omega)=\frac{V(j\omega)}{I(j\omega)}
$$

通过扫描 $\omega$，可获得幅频和相频特性。具体方法可能基于时域扰动、频域线性化或实验辨识。

## 与相关方法的关系

- [[frequency-scan]]：频率响应的典型获取方法。
- [[impedance-measurement]]：端口阻抗测量路线。
- [[vector-fitting]]：频率响应的有理函数等效方法。
- [[harmonic-transfer-coefficient]]：更细化的频率耦合描述。

## 适用边界与失败模式

- 适用于工作点附近的小扰动或线性化分析。
- 大扰动、故障和模式切换通常仍需回到 EMT 时域验证。
- 若系统显著时变或强非线性，单一频率响应可能不足以描述全部动态。

## 代表性来源

- [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]]：频率响应等效背景。
- [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va]]：频率响应与暂态模型对照背景。
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]]：频率特性对暂态行为影响的相关来源。

## 证据边界

本页不写具体带宽、谐振频率或稳定裕度结论，必须绑定对象和测试条件。

---
title: "滤波方法入口 (Filtering)"
type: method
tags: [filtering, signal-processing, harmonic, smoothing, measurement]
created: "2026-05-05"
updated: "2026-05-06"
---

# 滤波方法入口 (Filtering)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[关键公式]
    N1 --> N2
    N3[与相关方法的关系]
    N2 --> N3
    N4[适用边界与失败模式]
    N3 --> N4
    N5[代表性来源]
    N4 --> N5
    N6[证据边界]
    N5 --> N6
```


## 定义与边界

滤波方法是对电压、电流、功率或测量信号中的目标频段、噪声或暂态分量进行提取、抑制或平滑处理的技术集合。在 EMT Wiki 中，本页作为上位入口，承接围绕数字滤波、频谱提取和控制测量滤波展开的方法。

本页不是 LCC 不平衡平均值模型页，也不是单一谐波分析模型页。

## EMT 中的作用

滤波方法在 EMT 中常用于：

- 提取频率、相量、阻抗或谐振相关特征；
- 为保护和控制算法提供更稳定的测量量；
- 分离高频暂态、基波和谐波分量；
- 减少数值噪声和测量噪声对判据的影响。

## 关键公式

线性滤波最常抽象为卷积或传递函数：

$$
y(t)=h(t)*x(t)
$$

离散实现中也常写为差分方程或频域窗函数处理。关键区别在于滤波对象、带宽和是否允许引入额外时延。

## 与相关方法的关系

- [[fourier-filtering]]：频谱提取和滤波的更具体方法页。
- [[fft]]：频域分量提取基础。
- [[phasor-measurement-unit]]：测量链中的滤波背景。
- [[frequency-response]]：频域分析背景。
- [[signal-processing]]：更上位的信号处理入口背景。

## 适用边界与失败模式

- 适用于需要从 EMT 波形中提取较稳定特征的场景。
- 任何滤波器都会引入带宽和时延折中。
- 保护和快速控制场景下，过度平滑可能遮蔽真正暂态信息。

## 代表性来源

- [[fourier-filtering]]：当前 Wiki 中的正式频谱滤波方法页。
- [[phasor-measurement-unit]]：测量链和动态滤波背景。
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]：提醒滤波与平均化不应混同。

## 证据边界

本页不写具体滤波器阶数、带宽或最优参数，只作为上位入口。

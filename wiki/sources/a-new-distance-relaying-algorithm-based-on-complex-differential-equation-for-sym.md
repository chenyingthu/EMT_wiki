---
title: "A new distance relaying algorithm based on complex differential equation for symmetrical components"
type: source
year: 2004
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Rosołowski 等 - 1997 - A new distance relaying algorithm based on complex differential equation for symmetrical components.pdf"]
---

# A new distance relaying algorithm based on complex differential equation for symmetrical components

**年份**: 2004
**来源**: `02/Rosołowski 等 - 1997 - A new distance relaying algorithm based on complex differential equation for symmetrical components.pdf`

## 摘要

This paper presents a new digital impedance measuring technique for transmission lines that combines symmetrical components and the complex differential equation of an equivalent fault loop circuit. The phase voltages and currents at the relaying point are transformed into symmetrical components using Fourier filters of short window length. Depending on fault type, an appropriate fault loop circuit is formed, signals of which are the appropriate symmetrical components, while a parameter of which is the positive sequence impedance being a geometrical measure of the distance from the relaying point to a fault. The impedance, however, is measured very fast by on-line solving the complex differential equation originated for this fault loop circuit, Consequently, this approach combines frequenc

## 核心贡献


- 融合对称分量频域滤波与复数微分方程时域求解，实现正序阻抗快速精确测量。
- 构建通用等效故障回路模型，仅需单采样点数据即可解算故障距离参数。
- 提出平行线路高阻故障检测与选线新方法，有效克服远端故障判别难题。


## 使用的方法


- [[傅里叶滤波|傅里叶滤波]]
- [[对称分量法|对称分量法]]
- [[复数微分方程求解|复数微分方程求解]]
- [[时域阻抗估计|时域阻抗估计]]
- [[数字距离保护|数字距离保护]]


## 涉及的模型


- [[平行输电线路|平行输电线路]]
- [[等效故障回路|等效故障回路]]
- [[序网模型|序网模型]]
- [[故障阻抗模型|故障阻抗模型]]


## 相关主题


- [[距离保护|距离保护]]
- [[数字继电保护|数字继电保护]]
- [[高阻故障检测|高阻故障检测]]
- [[平行线路保护|平行线路保护]]
- [[阻抗测量|阻抗测量]]


## 主要发现


- EMTP仿真验证算法兼具滤波精度与响应速度，测距结果快速且准确。
- 方法能可靠识别平行线路远端高阻故障，并准确区分故障与非故障线路。



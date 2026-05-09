---
title: "电容式电压互感器建模方法 (CCVT)"
type: method
tags: [ccvt, cvt, voltage-transformer, ferroresonance, measurement]
created: "2026-05-05"
updated: "2026-05-06"
---

# 电容式电压互感器建模方法 (CCVT)

## 定义与边界

CCVT（Capacitive Coupling Voltage Transformer）建模方法指在 EMT 仿真中表示电容分压器、中间补偿电抗器、降压变压器、寄生电容和保护元件等组成部分的技术路线。它常用于暂态测量误差、铁磁谐振、频率响应和保护通道评估。

本页讨论的是 CCVT 作为测量装置的建模与暂态行为，不把行波保护或无关传输线公式混写成 CCVT 方法本身。

## EMT 中的作用

在 EMT 仿真中，CCVT 方法主要用于：

- 研究故障和开关操作期间的测量失真；
- 分析铁磁谐振、次谐波和高频暂态对测量通道的影响；
- 为保护、同步和故障录波模型提供更真实的电压测量输入；
- 评估寄生参数和保护元件对频率响应的影响。

## 关键公式

CCVT 的核心仍来自电容分压与补偿网络关系。最简分压关系可写为：

$$
v_s = v_p \frac{C_1}{C_1 + C_2}
$$

但 EMT 研究通常还需显式表示补偿电抗器和变压器支路，因此实际问题不止是稳态分压，而是完整暂态测量链。

## 常见分支

- 低频稳态等值：用于潮流、工频测量或简化保护输入。
- 暂态测量链模型：显式保留分压器、补偿电抗器和中间变压器动态。
- 谐振/寄生参数增强模型：用于研究铁磁谐振、高频失真和波头响应。

## 与相关方法的关系

- [[phasor-measurement-unit]]：测量链和动态相量背景。
- [[digital-distance-protection]]：保护算法对测量链失真的敏感性背景。
- [[fault-analysis]]：故障激励是 CCVT 暂态误差的主要触发场景。
- [[electromagnetic-transient]]：高频暂态和铁磁谐振背景。
- [[protection-system]]：保护系统整体背景。

## 适用边界与失败模式

- 适用于需要研究测量装置暂态行为的 EMT 场景。
- 若仅用理想电压测量替代 CCVT，可能低估保护与同步环节的误差。
- 高频暂态、铁磁饱和和寄生参数会显著改变测量结果。
- 单篇实验或装置参数不能外推到所有 CCVT 结构。

## 代表性来源

- [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo]]：CCVT 暂态行为和频率响应背景。
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]]：说明测量链与保护实现的相关背景。
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]]：提醒高速保护场景对测量装置动态十分敏感。

## 证据边界

本页不写无来源幅频误差、铁磁谐振阈值或装置参数，具体结论必须绑定装置结构和测试工况。

## 开放问题

- 何时必须从理想测量升级为暂态 CCVT 模型，仍需结合保护速度和频段要求判断。
- 当前页未细分不同制造结构和参数标定流程。

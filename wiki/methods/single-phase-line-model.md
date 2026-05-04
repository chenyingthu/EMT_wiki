---
title: "单相线路模型 (Single-Phase Line Model)"
type: method
tags: [single-phase, line-model, distribution, lumped-parameter, bergeron]
created: "2026-05-02"
---

# 单相线路模型 (Single-Phase Line Model)

## 定义与边界

单相线路模型是把一条线路简化为一个相导体及其返回路径的 EMT/电路表示。它可以是集中参数、π 型等值、常参数分布线路或 Bergeron 行波形式。其价值在于降低问题维度，适合教学、局部配电馈线、单相等效回路或经模态分解后的单一传播模态。

该模型不应被当作所有配电线路或输电线路的默认表示。三相不平衡、地线/护套回流、平行线路耦合、非换位线路和宽频电缆暂态通常需要 [[methods/mutual-impedance.md]] 和 [[methods/distributed-parameter-line.md]] 表示。

## EMT 中的作用

单相线路模型常用于：

- 构建简单的故障、开关和负荷接入算例。
- 作为 [[methods/bergeron-line-model.md]] 或 [[methods/transmission-line-theory.md]] 的入门形式。
- 表示多相系统经 [[methods/modal-transformation.md]] 后的某个独立模态。
- 在配电系统或低压网络中建立局部等效，但需明确返回导体和接地路径。

在 EMT Wiki 中，本页应帮助读者判断“何时可以简化为单相”，而不是罗列未经来源绑定的典型参数表。

## 核心机制

集中参数单相线路可写为：

$$Z_\ell(\omega)=R_\ell+j\omega L_\ell,\quad
Y_\ell(\omega)=G_\ell+j\omega C_\ell$$

π 型等值使用串联阻抗和两端并联导纳近似线路端口关系；分布参数形式则使用电报方程：

$$-\frac{dV}{dx}=Z'(\omega)I,\quad
-\frac{dI}{dx}=Y'(\omega)V$$

特性阻抗与传播常数为：

$$Z_c(\omega)=\sqrt{\frac{Z'(\omega)}{Y'(\omega)}},\quad
\gamma(\omega)=\sqrt{Z'(\omega)Y'(\omega)}$$

若采用 Bergeron 常参数行波表示，端口电流可写成当前端口电压与历史源的组合：

$$I_k(t)=\frac{V_k(t)}{Z_c}+I_{\text{hist},k}(t)$$

该式只有在返回路径、损耗处理和传播时延定义清楚时才有工程意义。

## 分类与变体

| 变体 | 输入 | 输出 | 适合场景 | 主要风险 |
|------|------|------|----------|----------|
| 集中 R-L 或 R-L-C 模型 | 线路等效参数 | 端口电压电流 | 短线、低频近似 | 忽略传播时延 |
| π 型等值 | 串联阻抗、并联导纳 | 网络等效端口 | 潮流/低频暂态近似 | 高频和长线误差 |
| 单相 Bergeron | $Z_c,\tau$ 和历史量 | 行波端口等效 | 教学、单模态、简单行波 | 频变损耗不足 |
| 频变单相模型 | $Z'(\omega),Y'(\omega)$ | 宽频端口响应 | 电缆/接地快速暂态 | 参数和拟合工作量较高 |

## 适用边界与失败模式

- 必须定义返回路径。单相二线、相-地、芯线-护套和模态回路的参数含义不同。
- 简化为单相会丢失相间互阻抗、零序耦合和不平衡传播；保护、故障定位和并行线路感应问题不能随意使用。
- 对高频暂态，简单 R-L-C 参数可能无法表示 [[methods/earth-return-impedance.md]]、集肤效应和邻近效应。
- 若单相模型来自模态变换，应说明它是“模态”等效，而不是物理单根导线。

## 代表性来源

- [[sources/frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method.md]]：说明多导体线路可分解为类似单相传播模态处理，但频变和互耦仍需在前处理阶段保留。
- [[sources/assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und.md]]：提醒短电缆快速暂态中，单相/简化 TLT 的返回路径假设需要验证。
- [[sources/a-new-tool-for-calculation-of-line-and-cable-parameters.md]]：说明单相参数不是凭经验表格给出，而应从几何、材料和介质模型计算。
- [[sources/transmission-line-model-for-variable-step-size-simulation-algorithms.md]]：可作为线路端口等值与时间步长关系的相关入口；具体算法边界需回原文确认。

## 与相关页面的关系

- [[methods/lumped-parameter-model.md]] 是单相低阶实现之一。
- [[methods/distributed-parameter-line.md]] 是保留传播效应的线路表示。
- [[methods/mutual-impedance.md]] 说明单相简化会忽略哪些耦合。
- [[models/cable-model.md]] 和 [[models/transmission-line-model.md]] 是具体设备模型页。
- [[models/frequency-dependent-line-model.md]] 处理宽频参数和时域实现。

## 修订与证据使用注意事项

本页不再保留无来源的“短线/中线/长线长度阈值”和典型参数表。若未来需要这些工程规则，应从教材、标准或明确工具手册引入，并标注它们是近似经验而非 EMT 普适规则。

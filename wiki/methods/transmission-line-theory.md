---
title: "传输线理论 (Transmission Line Theory)"
type: method
tags: [transmission-line, wave-propagation, distributed-parameter, telegrapher-equation]
created: "2026-05-02"
---

# 传输线理论 (Transmission Line Theory)

## 定义与边界

传输线理论描述电压和电流沿导体连续分布并以有限速度传播的电磁过程。它不同于把线路简化为单个集总 $RLC$ 支路的模型；当线路长度、信号上升沿或关注频带使传播时延、反射、频变损耗不可忽略时，应使用分布参数表述。

单相均匀线的电报方程为：

$$
-\frac{\partial v}{\partial x}=Ri+L\frac{\partial i}{\partial t}
$$

$$
-\frac{\partial i}{\partial x}=Gv+C\frac{\partial v}{\partial t}
$$

其中 $R,L,G,C$ 是单位长度参数。该理论本身不等同于某个 EMT 线路模型；[[bergeron-line-model]]、[[frequency-dependent-line-model]] 和 [[phase-domain-modeling]] 是不同的数值实现路线。

## EMT 中的作用

EMT 关注开关过电压、雷电波、直流线路故障、电缆暂态和频率相关网络响应时，线路不能总是视为瞬时连接。传输线理论提供三个接口量：

- 特性阻抗 $Z_c$，决定行波电压和电流比值。
- 传播常数 $\gamma=\alpha+j\beta$，决定衰减和相移。
- 传播时延 $\tau=l/v_p$，决定历史量何时作用到线路另一端。

这些量进入 [[transmission-line-model]] 的 Bergeron 等效、频变卷积模型或相域状态空间模型，并最终以历史源或端口等值方式接入 [[nodal-analysis]]。

## 核心机制

正弦稳态下，令：

$$
Z=R+j\omega L,\quad Y=G+j\omega C
$$

则传播常数和特性阻抗为：

$$
\gamma=\sqrt{ZY},\quad Z_c=\sqrt{\frac{Z}{Y}}
$$

电压和电流解可写为：

$$
V(x)=V^+e^{-\gamma x}+V^-e^{\gamma x}
$$

$$
I(x)=\frac{V^+}{Z_c}e^{-\gamma x}-\frac{V^-}{Z_c}e^{\gamma x}
$$

终端负载 $Z_L$ 的反射系数为：

$$
\Gamma_L=\frac{Z_L-Z_c}{Z_L+Z_c}
$$

无损或低损耗近似下，时域行波可按传播时延更新；有损和频变情况下，$R,L,G,C$ 随频率变化，必须通过卷积、有理函数拟合或状态空间实现。

## 分类与变体

| 线路表述 | 主要用途 | 边界 |
|----------|----------|------|
| 集总 $\pi$ 型模型 | 短线、低频或粗略网络连接 | 忽略传播时延和行波反射 |
| 无损 Bergeron 模型 | 低损耗线的行波时延 | 难以描述宽频损耗和色散 |
| 频率相关模域模型 | 架空线和电缆宽频暂态 | 需要 [[modal-transformation]] 和拟合 |
| 相域频变模型 | 非换位、不平衡或强耦合线路 | 计算和参数辨识更复杂 |
| 多导体传输线模型 | 电缆、双回线、接地回路耦合 | 参数矩阵和边界条件需明确 |

“线路长度超过某个固定公里数才需要分布参数”只是经验判断；更稳妥的边界应由关注频率、波速、上升时间和误差容忍度共同确定。

## 适用边界与失败模式

传输线理论适用于沿线参数可定义、边界条件清楚、关注传播和反射过程的线路、电缆或多导体系统。以下情况需要谨慎：

- 非均匀线路、频变土壤参数、交叉互联电缆和复杂接地会破坏简单均匀线假设。
- 模域模型在非换位线路中可能需要频率相关变换矩阵；固定实变换只是一种近似。
- 线路端接非线性避雷器、开关或变换器时，边界条件需要与外部节点方程迭代耦合。
- 参数来自几何公式、软件计算或测量拟合时，应保留来源和频率范围；不能把某个参数集外推到全部暂态频带。

## 代表性来源

- [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und]] 可作为多导体地下线路中传输线理论适用性的代表来源。
- [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp]] 支撑频变线路模型的时域实现讨论。
- [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method]] 说明 Bergeron 思路在频变多导体线路中的扩展，结论应绑定其模型假设。
- [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-]] 适合支撑土壤参数频变对波传播影响的边界提醒。
- [[耦合长线电磁暂态分析的扩展bergeron模型]] 是长线耦合暂态分析的中文来源之一。

## 与相关页面的关系

- [[transmission-line-model]] 关注线路在 EMT 软件中的模型组织；本页提供其物理和数学基础。
- [[modal-transformation]] 处理多相线路从相域到模域的解耦。
- [[distributed-parameter-model]] 与本页边界接近，但更强调建模范式。
- [[lumped-parameter-model]] 是短线或低频近似的对照。
- [[frequency-dependent-line-model]] 和 [[vector-fitting]] 负责把宽频参数转成可时域仿真的形式。

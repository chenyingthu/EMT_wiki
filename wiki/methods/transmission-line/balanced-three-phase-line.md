---
title: "平衡三相线路 (Balanced Three-Phase Line)"
type: method
tags: [three-phase, balanced, transmission-line, symmetrical, positive-sequence, single-phase-equivalent]
created: "2026-05-02"
---

# 平衡三相线路 (Balanced Three-Phase Line)


```mermaid
graph TD
    subgraph Ncmp[平衡三相线路 (Balanced Three-Phase…]
        N0[正序相量模型: 只求一相或正序网络]
        N1[常参数 Bergeron: 可用相同线模传播参数]
        N2[模态域频变线路: 简化模态变换和拟合]
        N3[相域 ULM: 可作为校验基准而非必须简化]
    end
```


## 定义与边界

平衡三相线路是一个建模假设：三相自参数相同、相间互参数相同，且外部激励和负荷也按三相对称运行。在线路参数层面，它对应循环对称矩阵；在系统分析层面，它允许只保留正序或一相等值。

本页只说明平衡线路假设如何进入 EMT 和相量分析。它不是线路设计参数表，也不负责解释换位过程；换位如何获得平均平衡参数见 [[transposed-three-phase-line]]。

## EMT 中的作用

平衡假设可显著减少模型复杂度，但在 EMT 中应作为可验证近似使用：

- 工频稳态、三相对称故障和机电暂态接口常可只保留正序。
- 常参数线路模型可用相同的线模通道表示正负序。
- 频变线路、接地故障、雷电和非对称开关暂态通常需要检查零序、地模或相域响应。

若研究问题包含不平衡故障、单相重合闸、非换位区段、平行线路互耦或电缆护套接地，仅用平衡三相线路可能遮蔽关键暂态。

## 核心机制

平衡三相线路的串联阻抗矩阵可写为：

$$
\mathbf{Z}_{abc}=
\begin{bmatrix}
Z_s & Z_m & Z_m\\
Z_m & Z_s & Z_m\\
Z_m & Z_m & Z_s
\end{bmatrix}
$$

并联导纳矩阵可类似写为：

$$
\mathbf{Y}_{abc}=
\begin{bmatrix}
Y_s & Y_m & Y_m\\
Y_m & Y_s & Y_m\\
Y_m & Y_m & Y_s
\end{bmatrix}
$$

用 Fortescue 变换：

$$
\begin{bmatrix}V_0\\V_1\\V_2\end{bmatrix}
=\frac{1}{3}
\begin{bmatrix}
1 & 1 & 1\\
1 & a & a^2\\
1 & a^2 & a
\end{bmatrix}
\begin{bmatrix}V_a\\V_b\\V_c\end{bmatrix},\quad a=e^{j2\pi/3}
$$

可得到理想序阻抗：

$$Z_0=Z_s+2Z_m,\quad Z_1=Z_2=Z_s-Z_m$$

该对角化成立的前提是参数矩阵循环对称。外部网络和边界条件若不对称，序网络仍会通过故障或连接条件耦合。

## 单相等值的使用条件

单相等值适合以下场景：

- 三相电源、负荷和线路参数均近似平衡。
- 目标只关心正序电压、电流、功率或慢速机电动态。
- 故障类型为三相对称故障，或不平衡量已由其他方法单独处理。

不适合以下场景：

- 单相接地、两相短路、断线、单相重合闸和不平衡负荷。
- 并行线路零序互感、地线耦合和土壤频变影响显著。
- 需要相域波形、行波到达时间或高频暂态细节。

## 与线路模型的关系

| 模型层次 | 平衡假设的作用 | 注意事项 |
|----------|----------------|----------|
| 正序相量模型 | 只求一相或正序网络 | 不覆盖 EMT 高频波形 |
| 常参数 Bergeron | 可用相同线模传播参数 | 零序/地模仍需独立参数 |
| 模态域频变线路 | 简化模态变换和拟合 | 频率相关土壤可能改变地模 |
| 相域 ULM | 可作为校验基准而非必须简化 | 对非平衡边界更稳健 |

## 适用边界与失败模式

- 不应把平衡三相线路写成实际线路总是平衡；它是模型假设。
- 正序等值不能推导出接地故障零序电流，除非补充零序网络和接地路径。
- 无来源的典型正序/零序参数比值、线路长度分类和电压等级参数表应删除或绑定来源。
- 在频变 EMT 中，$Z_1=Z_2$ 的低频结论不自动说明所有频点和所有传播模态相同。
- 若由换位平均得到平衡参数，应保留平均方法和未换位端部的边界说明。

## 代表性证据

- [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p]]：可作为“换位/平衡条件被用于频变线路模型构造”的来源入口。
- [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software]]：支撑完全换位三相线路中使用 Clarke 模态变换连接单相线路模型的实现路线。
- [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-]]：从反面说明不换位线路不能无条件套用平衡三相假设。

## 与相关页面的关系

- [[transposed-three-phase-line]]：说明几何换位如何产生平均平衡参数。
- [[sequence-component-method]] 和 [[symmetrical-components]]：说明序分量变换与故障网络。
- [[modal-transformation]] 和 [[modal-domain-decoupling]]：说明相域/模域转换在 EMT 线路中的使用边界。
- [[transmission-line-model]]、[[bergeron-line-model]] 和 [[universal-line-model]]：线路模型实现入口。

## 修订与证据使用注意事项

后续补充应区分“代数上可对角化”“工程上足够平衡”和“论文算例验证”。不要加入未来源绑定的线路参数表、零序倍数、长度阈值、稳定裕度或功率传输极限。

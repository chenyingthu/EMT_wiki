---
title: "等效电路法 (Equivalent Circuit Method)"
type: method
tags: [equivalent-circuit, modeling, norton, thevenin, network-reduction, circuit-theory]
created: "2026-05-02"
---

# 等效电路法 (Equivalent Circuit Method)


```mermaid
graph TD
    subgraph Ncmp[等效电路法 (Equivalent Circuit Me…]
        N0[戴维南等效: 电压源串联阻抗]
        N1[诺顿等效: 电流源并联导纳]
        N2[RLC 综合: 被动支路网络]
        N3[多端口导纳: $\mathbf{i}=\mathbf{Y…]
        N4[磁等效电路: 磁动势、磁通、磁阻]
        N5[伴随模型: 当前导纳加历史源]
    end
```


## 定义与边界

等效电路法是把复杂元件、子网络或外部系统替换为在指定端口上具有相同或近似相同电压-电流关系的电路表示。它可以是戴维南、诺顿、RLC 网络、伴随模型、磁路等效或多端口导纳矩阵。

本页关注 EMT 方法论中的端口等效。等效电路只保证其定义端口、频段、运行点和模型假设内的行为；它不保证内部节点、电磁场分布或所有非线性事件都被保留。强结论必须绑定来源、端口和验证基线。

## EMT 中的作用

在 EMT 中，等效电路法用于：

- 把电感、电容、线路、变压器和电力电子子模块离散为可进入节点方程的伴随支路。
- 把外部网络压缩为 [[thevenin-equivalent]]、[[norton-equivalent]] 或多端口动态导纳。
- 把测量或频率扫描得到的端口响应综合为 RLC 网络或状态空间模型。
- 用磁等效电路表示变压器铁芯、漏磁和局部饱和。
- 在网络分区和并行仿真中用端口源加导纳表示被消去子系统。

它的核心是端口等价，而不是“模型简化后仍保留所有物理细节”。

## 核心机制

### 端口关系

线性单端口可写成戴维南形式：

$$
v = v_{\mathrm{th}} - Z_{\mathrm{th}} i
$$

也可写成诺顿形式：

$$
i = i_{\mathrm{N}} - Y_{\mathrm{N}} v
$$

当 $Z_{\mathrm{th}}$ 可逆时：

$$
Y_{\mathrm{N}}=Z_{\mathrm{th}}^{-1},\quad i_{\mathrm{N}}=Y_{\mathrm{N}}v_{\mathrm{th}}
$$

多端口推广为矩阵：

$$
\mathbf{i}=\mathbf{i}_{\mathrm{N}}-\mathbf{Y}_{\mathrm{eq}}\mathbf{v}
$$

矩阵的非对角项表示端口间耦合，不应在没有证据时删除。

### Kron 消去

对线性网络，若保留端口集合 $R$，消去内部节点 $E$，节点方程为：

$$
\begin{bmatrix}
\mathbf{i}_R \\
\mathbf{i}_E
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{Y}_{RR} & \mathbf{Y}_{RE} \\
\mathbf{Y}_{ER} & \mathbf{Y}_{EE}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}_R \\
\mathbf{v}_E
\end{bmatrix}
$$

若内部节点无外部注入，得到端口等值导纳：

$$
\mathbf{Y}_{\mathrm{eq}}
=\mathbf{Y}_{RR}-\mathbf{Y}_{RE}\mathbf{Y}_{EE}^{-1}\mathbf{Y}_{ER}
$$

该式说明等效电路法可以严格保留线性网络端口行为，但前提是矩阵可逆、拓扑固定且模型假设成立。

### EMT 伴随电路

梯形积分把动态元件转为当前时刻导纳加历史源。例如电感支路可写成：

$$
i^{n+1}=G_{\mathrm{eq}}v^{n+1}+i_{\mathrm{hist}}^{n}
$$

电容支路也可写成类似形式。这样所有线性支路在每个时间步都可进入节点导纳矩阵，历史项作为等效源注入。

### 频率相关等效电路

若端口响应是频率相关的，可用有理函数逼近：

$$
Y(s)=D+sH+\sum_{k=1}^{r}\frac{R_k}{s-p_k}
$$

再转成 RLC 支路、状态空间或递归卷积。该路线常见于 [[detailed-equivalent-model]]、变压器高频模型和外部网络 FDNE。

## 分类与变体

| 类型 | 端口形式 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 戴维南等效 | 电压源串联阻抗 | 开路电压、故障点等值、源网络表示 | 非线性和频变需扩展 |
| 诺顿等效 | 电流源并联导纳 | 节点分析、伴随模型、电流注入接口 | 短路电流和导纳需同一端口定义 |
| RLC 综合 | 被动支路网络 | 频率响应进入 EMT | 拟合和无源性需验证 |
| 多端口导纳 | $\mathbf{i}=\mathbf{Y}\mathbf{v}$ | 外部网络、多边界系统 | 非对角耦合和矩阵条件数关键 |
| 磁等效电路 | 磁动势、磁通、磁阻 | 变压器铁芯和饱和 | 几何和材料参数要求高 |
| 伴随模型 | 当前导纳加历史源 | EMT 时间步求解 | 数值阻尼和历史项更新需检查 |

## 适用边界与失败模式

等效电路法容易出现以下问题：

- 把只在端口等价的模型用于内部状态、内部故障或局部绝缘结论。
- 在非线性元件上直接套用线性戴维南/诺顿等效，却不说明运行点和线性化范围。
- 忽略频率相关性，用工频等值分析高频暂态或谐振。
- 多端口网络只保留自导纳，删除互导纳后改变耦合路径。
- 有理拟合模型稳定但非无源，互联后在时域发散。
- 未记录端口方向、源置零规则、基准值和单位，导致等效参数不可复核。

## 代表性证据

- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]：支撑“多端口导纳矩阵可经内部节点消去和 RLC 综合进入 EMTP”的机制。其计算效率和误差结论应限定在原文网络和频率范围。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：支撑“有理函数导纳等值需要公共极点、无源性检测和参数修正”的 FDNE 工作流。
- [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions]]：支撑“端口节点导纳矩阵可以综合为变压器高频等效电路”，但该端口模型不提供内部绕组电压。
- [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based]]：支撑磁等效电路可在 EMT 型软件中表示变压器局部磁行为，但其验证边界不同于普通端口 RLC 等效。
- [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks]]：展示开关事件可通过辅助源和端口响应组织计算，适合说明等效源在暂态加速中的作用，但不能外推为通用 EMT 求解替代。

## 与相关页面的关系

- [[norton-equivalent]] 是 EMT 节点分析中最常用的端口源形式。
- [[thevenin-equivalent]] 是电压源等值形式，与诺顿等效互为转换。
- [[thevenin-norton-equivalent]] 汇总两者在 EMT 时域中的关系。
- [[detailed-equivalent-model]] 使用有理函数、状态空间或 RLC 网络保持更多端口动态。
- [[transformer-network]] 和 [[ideal-transformer-equivalent]] 是等效电路法在变压器中的典型应用。
- [[nodal-admittance-matrix]]、[[nodal-analysis]] 和 [[companion-model]] 是等效电路进入求解器的数值基础。

## 开放问题

- 对含保护动作和控制限幅的对象，线性端口等效需要多运行点或事件逻辑补充。
- 高频等效电路的无源性、离散化稳定性和拟合精度之间可能存在取舍，不能只优化其中一个指标。
- 测量型等效电路的可复现性依赖端口定义、仪器带宽、扰动幅值和数据处理流程。

## 来源论文

参见 [[index]] 获取更多等效电路法相关文献。

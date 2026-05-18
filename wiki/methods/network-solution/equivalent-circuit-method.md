---
title: "等效电路法 (Equivalent Circuit Method)"
type: method
tags: [equivalent-circuit, modeling, norton, thevenin, network-reduction, circuit-theory, kron-reduction, companion-circuit, fdne]
created: "2026-05-02"
updated: "2026-05-18"
---

# 等效电路法 (Equivalent Circuit Method)

## 定义与边界

等效电路法是把复杂元件、子网络或外部系统替换为在指定端口上具有相同或近似相同电压-电流关系的电路表示。它可以是戴维南、诺顿、RLC网络、伴随模型、磁路等效或多端口导纳矩阵。

**本文关注 EMT 方法论中的端口等效**。等效电路只保证其定义端口、频段、运行点和模型假设内的行为；它不保证内部节点、电磁场分布或所有非线性事件都被保留。强结论必须绑定来源、端口和验证基线。

等效电路法的本质是**把"网络内部结构"转化为"端口外特性"**，使外部观测者看到的端口响应与原始网络一致。根据具体实现形式，它可用于稳态分析、暂态仿真、阻抗匹配、网络降阶等多种场景。

## EMT 中的作用

在 EMT 中，等效电路法用于：

- 把电感、电容、线路、变压器和电力电子子模块离散为可进入节点方程的伴随支路。
- 把外部网络压缩为 [[thevenin-equivalent]]（电压源串联阻抗）、[[norton-equivalent]]（电流源并联导纳）或[[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|多端口动态导纳]]。
- 把测量或频率扫描得到的端口响应综合为 RLC 网络或状态空间模型。
- 用磁等效电路表示变压器铁芯、漏磁和局部饱和。
- 在网络分区和并行仿真中用端口源加导纳表示被消去子系统。
- 作为 [[companion-model|伴随模型]] 的理论基础，把动态元件转化为当前导纳加历史电流源的形式。

等效电路法的核心是**端口等价**，而不是"模型简化后仍保留所有物理细节"。

## 核心机制

### 单端口端口关系

线性单端口可写成戴维南形式：

$$
v = v_{\mathrm{th}} - Z_{\mathrm{th}} \, i \tag{1}
$$

也可写成诺顿形式：

$$
i = i_{\mathrm{N}} - Y_{\mathrm{N}} \, v \tag{2}
$$

当 $Z_{\mathrm{th}}$ 可逆时，两者可互相转换：

$$
Y_{\mathrm{N}} = Z_{\mathrm{th}}^{-1}, \quad i_{\mathrm{N}} = Y_{\mathrm{N}} \, v_{\mathrm{th}} \tag{3}
$$

### 多端口推广

多端口推广为矩阵形式：

$$
\mathbf{i} = \mathbf{i}_{\mathrm{N}} - \mathbf{Y}_{\mathrm{eq}} \, \mathbf{v} \tag{4}
$$

矩阵的非对角项表示端口间耦合，不应在没有证据时删除。

### Kron 消去（节点消去）

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
\end{bmatrix} \tag{5}
$$

若内部节点无外部注入（$\mathbf{i}_E = 0$），得到端口等值导纳（Kron 消去）：

$$
\mathbf{Y}_{\mathrm{eq}} = \mathbf{Y}_{RR} - \mathbf{Y}_{RE} \, \mathbf{Y}_{EE}^{-1} \, \mathbf{Y}_{ER} \tag{6}
$$

式(6)是等效电路法可以**严格保留线性网络端口行为**的理论基础，但前提是矩阵可逆、拓扑固定且模型假设成立 [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]。

### EMT 伴随电路（Companion Circuit）

梯形积分把动态元件转为当前时刻导纳加历史源。电感支路：

$$
i^{n+1} = G_{\mathrm{eq}} \, v^{n+1} + i_{\mathrm{hist}}^{n} \tag{7}
$$

其中 $G_{\mathrm{eq}} = \frac{\Delta t}{2L}$，历史项 $i_{\mathrm{hist}}^{n} = i^n - G_{\mathrm{eq}} v^n$。电容支路形式对称。所有线性支路在每个时间步都可进入节点导纳矩阵，历史项作为等效源注入 [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|companion-circuit]]。

### 频率相关等效电路（FDNE）

若端口响应是频率相关的，可用有理函数逼近 [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：

$$
Y(s) = D + sH + \sum_{k=1}^{r} \frac{R_k}{s - p_k} \tag{8}
$$

再转成 RLC 支路、状态空间或递归卷积。该路线常见于变压器高频模型和外部网络[[detailed-equivalent-model|FDNE]]。

### 恒定导纳接口（状态变量消去）

对于电力电子变换器，可通过状态变量消去直接生成低阶端口节点电压方程 [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]]：

$$
\mathbf{i}_s(t+\Delta t) = \mathbf{Y}_n \, \mathbf{u}_n(t+\Delta t) + \mathbf{i}_h(t) \tag{9}
$$

其中 $\mathbf{Y}_n$ 是等效端口导纳（不随开关状态切换），$\mathbf{i}_h$ 是历史电流源。外部 EMT 求解器把该变换器当作恒定导纳并联历史电流源接入全网节点方程。

## 分类与变体

| 类型 | 端口形式 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 戴维南等效 | 电压源串联阻抗 | 开路电压、故障点等值、源网络表示 | 非线性和频变需扩展 |
| 诺顿等效 | 电流源并联导纳 | 节点分析、伴随模型、电流注入接口 | 短路电流和导纳需同一端口定义 |
| RLC 综合 | 被动支路网络 | 频率响应进入 EMT | 拟合和无源性需验证 |
| 多端口导纳 | $\mathbf{i} = \mathbf{Y}\mathbf{v}$ | 外部网络、多边界系统 | 非对角耦合和矩阵条件数关键 |
| 磁等效电路 | 磁动势、磁通、磁阻 | 变压器铁芯和饱和 | 几何和材料参数要求高 |
| 伴随模型 | 当前导纳加历史源 | EMT 时间步求解 | 数值阻尼和历史项更新需检查 |
| 恒定导纳接口 | 状态消去后恒定导纳+历史源 | 大量电力电子变换器聚合 | 开关状态变化时历史源更新复杂 |

## 形式化表达

### 基本等效关系

戴维南等效：
$$
v_{\mathrm{th}} = v_{\mathrm{oc}}, \quad Z_{\mathrm{th}} = \frac{v_{\mathrm{oc}} - v_{\mathrm{sc}}}{i_{\mathrm{sc}}}
$$

诺顿等效：
$$
i_{\mathrm{N}} = \frac{v_{\mathrm{oc}}}{Z_{\mathrm{th}}}, \quad Y_{\mathrm{N}} = \frac{1}{Z_{\mathrm{th}}}
$$

### Kron 消去的矩阵形式

端口等值导纳（保留端口 $R$，消去内部节点 $E$）：
$$
\mathbf{Y}_{\mathrm{eq}} = \mathbf{Y}_{RR} - \mathbf{Y}_{RE} \mathbf{Y}_{EE}^{-1} \mathbf{Y}_{ER}
$$

该式说明等效导纳矩阵由内部网络拓扑决定，体现了"端口外特性与内部结构的关系"。

### 伴随电路的离散形式

电感（梯形积分）：
$$
i^{n+1} = \underbrace{\frac{\Delta t}{2L}}_{G_{\mathrm{eq}}} v^{n+1} + \underbrace{\left(i^n - \frac{\Delta t}{2L} v^n\right)}_{i_{\mathrm{hist}}^{n}}
$$

电容（梯形积分）：
$$
i^{n+1} = \underbrace{\frac{2C}{\Delta t}}_{G_{\mathrm{eq}}} v^{n+1} + \underbrace{\left(-i^n - \frac{2C}{\Delta t} v^n\right)}_{i_{\mathrm{hist}}^{n}}
$$

### 相域同步电机的恒定导纳形式 [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]]

把转子位置相关项从诺顿导纳中转移到受控电流源，使电机对网络呈现"恒定诺顿导纳并联受控电流源"：

$$
\mathbf{i}_{\mathrm{abcs}}^{n+1} = \mathbf{Y}_{\mathrm{c}} \mathbf{v}_{\mathrm{abcs}}^{n+1} + \mathbf{i}_{\mathrm{h}}^{n+1}
$$

其中 $\mathbf{Y}_{\mathrm{c}}$ 是常数导纳矩阵（不随转子角变化），$\mathbf{i}_{\mathrm{h}}^{n+1}$ 是包含转子角历史项的电流源。

### 多端口频变等值（FDNE） [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]

在频率点 $\omega_k$ 上计算端口导纳矩阵 $\mathbf{Y}(\omega_k)$，用有理函数拟合：

$$
\mathbf{Y}(s) = \mathbf{D} + s\mathbf{H} + \sum_{k=1}^{r} \frac{\mathbf{R}_k}{s - p_k}
$$

各端口的 RLC 支路组合后复现端口频率响应，用于替代被消去的大网络。

## 关键技术挑战

### 挑战1：非线性元件的端口等效

在非线性元件（如饱和变压器、非线性电阻）上直接套用线性戴维南/诺顿等效，必须说明运行点和线性化范围。每次迭代可能需要重新计算等效参数。

### 挑战2：频变特性与时域实现的矛盾

端口响应若具有频率相关性，用工频等值分析高频暂态或谐振会产生显著误差。频变等值需要用有理函数拟合（[[vector-fitting]]）和 RLC 支路实现，且必须进行无源性检查——非无源的拟合模型在时域仿真中会产生能量而导致数值发散 [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]。

### 挑战3：多端口网络的耦合处理

多端口网络若只保留自导纳而删除互导纳（$\mathbf{Y}_{ij}, i \neq j$），会改变耦合路径，导致间谐波和暂态响应失真。需要确保互导纳项在端口定义下有明确物理含义。

### 挑战4：状态变量消去的内-外解耦

恒定导纳接口（式(9)）需要从端口电压反演内部状态，为下一步历史源更新服务。当端口电压变化剧烈时，反演精度可能下降。[[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]]

### 挑战5：测量型等效电路的可复现性

测量得到的端口响应依赖仪器带宽、扰动幅值和数据处理流程。若端口定义不一致（如开路vs短路基准），等效参数不可直接比较。

## 量化性能边界

| 等效类型 | 计算复杂度 | 精度来源 | 典型加速比 | 适用场景 |
|----------|------------|----------|------------|----------|
| 工频戴维南/诺顿 | $O(1)$ | 单一频率 | — | 稳态短路分析 |
| Kron 消去（多端口） | $O(n^3)$ 消去内部节点 | 全频段线性 | — | 网络降阶 |
| FDNE（RLC 拟合） | 预处理 $O(f \cdot n^3)$，时域 $O(1)$ | 频率采样+有理拟合 | 10–50×（大规模网络）[[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] | 统计绝缘配合 |
| 伴随电路（恒定导纳） | 每步 $O(1)$ | 梯形积分精度 | 1.3× vs DSE（时域）[[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] | 大规模网络 EMT |
| 恒定导纳接口（状态消去） | 每步 $O(p^3)$，$p$ 为端口数 | 取决于状态变量个数 | ~30–60%（MMC 正常投切期间矩阵重构减少）[[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]] | 电力电子聚合 |
| E-PD 同步电机 | $O(p)$，恒定导纳 | 离散化误差 | 175 FLOPs/step（E-PD）vs 298（VBR）[[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]] | 多机系统加速 |

**证据说明**：上表中量化数据均来自论文原文的直接引用或页面抽取文本，原文未报告可核验数值结果时标注为"原文未报告可核验的数值结果"。

## 适用边界与选择指南

| 场景 | 推荐等效类型 | 关键依据 |
|------|-------------|----------|
| 故障点外部系统等值 | 戴维南等效 | 只需保留开路电压和等效阻抗 |
| 电力电子变换器聚合 | 恒定导纳接口 | 避免开关变化触发矩阵重构 |
| 混合仿真接口 | FDNE + 矢量拟合 | 保留宽频动态响应而非仅工频特性 |
| 同步电机接口 | E-PD 恒定导纳 | 网络导纳矩阵固定，无需随转子角更新 |
| 统计绝缘配合 | 多端口 FDNE | 大网络宽频响应可压缩为少量 RLC 支路 |
| 变压器饱和 | 磁等效电路 | 保留磁通-磁动势非线性关系 |
| 实时仿真 | 伴随电路（恒定导纳） | 每步计算量小，矩阵结构固定 |

## 相关方法与模型

- [[norton-equivalent]] 是 EMT 节点分析中最常用的端口源形式
- [[thevenin-equivalent]] 是电压源等值形式，与诺顿等效互为转换
- [[thevenin-norton-equivalent]] 汇总两者在 EMT 时域中的关系
- [[detailed-equivalent-model]] 使用有理函数、状态空间或 RLC 网络保持更多端口动态
- [[transformer-network]] 和 [[ideal-transformer-equivalent]] 是等效电路法在变压器中的典型应用
- [[nodal-admittance-matrix]] 和 [[nodal-analysis]] 是等效电路进入求解器的数值基础
- [[companion-model]] 是伴随电路（Companion Circuit）的核心——每个动态元件离散后形成当前导纳加历史源的结构
- [[vector-fitting]] 用于 FDNE 的有理函数拟合
- [[passivity-enforcement]] 用于确保频变等效电路在时域中无源稳定
- [[multi-rate-simulation]] 中网络分区后的端口等值是多速率方法的核心环节

## 来源论文

- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] — Morched/Ottevangers/Marti (1993)：多端口 FDNE 原始论文，提出预处理器生成 RLC 模块、EMTP 时步模块计算暂态响应。支撑 Kron 消去生成端口等值导纳（式6）和 RLC 支路拟合流程。

- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]] — Brandwajn 等：将 FDNE 用于 EMT-TS 混合仿真接口，通过矢量拟合形成共享极点有理函数矩阵，并结合半尺寸无源性测试矩阵检测和修正无源性违规。

- [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]] — Xia 等 (2019)：E-PD 模型，把转子位置相关项从诺顿导纳转移到历史电流源，使电机对网络呈现恒定诺顿导纳。

- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]] — 原文未完整收录：加速 MMC 详细等效模型，用欧拉形式替代梯形积分，使桥臂等效中不再出现随投切变化的电容等效电阻，正常运行时导纳矩阵保持不变。

- [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]] — Xu 等 (2024)：恒定导纳等效模型，通过状态变量消去直接生成低阶端口节点电压方程，外部网络看到恒定导纳加历史电流源。

- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — Sinkar 等 (2021)：伴随电路（CC）与描述符状态空间方程（DSE）的系统性比较，MNA 公式化，直接梯形积分，1.3×时域加速。
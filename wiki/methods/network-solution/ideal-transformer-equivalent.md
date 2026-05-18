---
title: "理想变压器等效 (Ideal Transformer Equivalent)"
type: method
tags: [ideal-transformer, equivalent-circuit, turns-ratio, magnetizing, transformer, duality, bctran]
created: "2026-05-02"
updated: "2026-05-18"
---

# 理想变压器等效 (Ideal Transformer Equivalent)

## 定义与边界

理想变压器等效是在端口之间只保留**匝比约束**、**相位变换**和**功率守恒**三大基本关系的变压器模型。其核心假设为：绕组电阻为零、漏磁通为零、铁芯损耗为零、磁化电流为零且无饱和效应。因此，理想变压器只表达电压比例关系、电流互补关系和瞬时功率守恒，不涉及任何耗能或储能机理。

在 EMT 仿真中，理想变压器常作为以下场景的**数学接口**：

- 将不同电压等级的端口量归算到共同基准（基准值归算）
- 表达换流变压器、升压变压器和多绕组变压器的匝比与连接组别
- 与漏感、绕组电阻、励磁支路组合形成实际变压器等效电路（见[[transformer-model]]）
- 在标幺值系统中消除额定变比，使网络方程更紧凑

**边界**：理想等效不能支撑以下分析结论——励磁涌流峰值与衰减、饱和谐振、零序磁通路径、高频操作过电压、绕组内部电压分布、变压器保护整定或绕组变形诊断。需转向[[transformer-network]]或[[magnetic-saturation-modeling]]。

## EMT 中的角色

在电磁暂态仿真中，理想变压器具有双重身份：**数值约束元件**和**等效电路构建起点**。

作为数值约束元件，理想变压器的端口方程构成代数约束而非微分方程。这些约束在节点分析中表现为电压比例关系和电流互补关系，要求 EMT 求解器在每个时间步显式满足匝比不变条件。若将理想变压器直接闭合为环路而未正确处理代数约束，可能导致系统矩阵奇异或条件数恶化——这在含多台理想变压器的网络中尤为敏感。

作为等效电路起点，理想变压器与并联磁化支路、串联漏阻抗组合后可形成 T 型或 Γ 型实际变压器等效电路。这一层次化建模路径是 [[equivalent-circuit-method]] 的核心内容，也是EMTP中BCTRAN、XP--Saturable Transformer Component等模型的基础。

## 核心机制

### 1. 端口约束方程

对双绕组理想变压器（端口电流均按流入元件为正），端口约束为：

$$
v_1 = n v_2 \tag{1}
$$

$$
i_2 = -n i_1 \tag{2}
$$

其中 $n = N_1 / N_2$ 为匝比（$N_1$ 为一次绕组匝数，$N_2$ 为二次绕组匝数）。由以上二式可直接导出瞬时功率守恒：

$$
v_1 i_1 + v_2 i_2 = 0 \tag{3}
$$

式(3) 表明：任一端口的输入功率必然从另一端口流出，理想变压器本身不消耗也不储存能量。注意：此处的"功率守恒"是瞬时电磁功率守恒，不涉及铜损或铁损，与实际变压器效率不是同一概念。

### 2. 阻抗折算

接在二次侧的阻抗 $Z_2$ 折算到一次侧为：

$$
Z_2' = n^2 Z_2 \tag{4}
$$

相反方向，一次侧阻抗折算到二次侧为：

$$
Z_1' = \frac{Z_1}{n^2} \tag{5}
$$

阻抗折算的几何意义：将二次侧阻抗按匝比平方放大（或缩小）到一次侧后，端口处的电压-电流关系保持不变。注意：式(4)(5) 要求阻抗在端口方向和连接关系一致时才成立；三相不平衡、零序通道和非线性元件会使简单标量折算失效（见[[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow]]）。

### 3. 复变比与相移矩阵

三相变压器的连接组别（含相移）可用复变比描述。对单相等效的相量形式为：

$$
\underline{v}_1 = a \, \underline{v}_2, \quad a = n e^{j\theta} \tag{6}
$$

其中 $\theta$ 为连接组别引入的相角（如 YNd11 中 $\theta = -30^\circ$）。在 EMT 时域 abc 坐标中，式(6) 需展开为端口电压矢量的矩阵关系，而不能只用标量相量角表示。

对三相三柱式变压器，abc 到序域的变换矩阵 $\mathbf{T}$ 将端口电压分解为序分量：

$$
\begin{bmatrix}
v_0 \\ v_+ \\ v_-
\end{bmatrix}
= \mathbf{T} \cdot
\begin{bmatrix}
v_a \\ v_b \\ v_c
\end{bmatrix}, \quad
\mathbf{T} = \frac{1}{3}
\begin{bmatrix}
1 & 1 & 1 \\
1 & e^{-j120^\circ} & e^{j120^\circ} \\
1 & e^{j120^\circ} & e^{-j120^\circ}
\end{bmatrix} \tag{7}
$$

理想变压器在各序域中保持匝比约束，但零序通道的有无取决于铁芯结构（Y/Y/Y vs YNd）和接地方式——这是"理想等效无法区分铁芯几何"的关键限制之一。

### 4. 标幺值中的单位变比

若两侧电压基准满足 $V_{B1} = n V_{B2}$，则在标幺值系统中理想变压器表现为单位变比（变比为 1）。这一简化在单相标幺值系统中十分有用，但需满足以下前提：

- 基准值按额定变比同步选择
- 网络方程采用统一基准值（通常取一次侧为全局基准）
- 无 OLTC（分接开关）动态或相移调节

当系统含可变分接头（OLTC）或需要相移调节时，变比不再恒为 $n$，需用复变比 $a = n e^{j\theta(t)}$ 或在每次分接变化时重新计算标幺值。

### 5. 对偶磁路建模起点

在变压器详细建模中，理想变压器约束是对偶磁路（见[[duality-based-transformer-modeling-for-low-frequency-transients]]）的核心起点。磁路对偶原理将磁动势（MMF）、磁通和磁阻分别映射为电路中的电压、电流和电阻类变量，使非线性铁芯磁化曲线可纳入同一网络方程求解。

双绕组理想变压器的对偶电路表示为：

- 一次侧：电压源 $v_1$ 驱动电流 $i_1$
- 理想变压器：用匝比约束表示的互易耦合元件（Mutator）
- 二次侧：电压 $v_2$ 和电流 $i_2$ 满足式(1)(2)

对三绕组变压器，端口约束扩展为矩阵形式，负电感、互感耦合与 BCTRAN 漏磁模型在数学上等价（见[[duality-based-transformer-modeling-for-low-frequency-transients]]）。这意味着"数值振荡根源在负电感"的常见误解需修正为：振荡来源于铁芯非线性支路与漏磁网络拓扑不匹配。

## 形式化表达

### 基本端口方程组

| 方程 | 含义 | 约束类型 |
|------|------|----------|
| $v_1 = n v_2$ | 电压比例 | 代数约束 |
| $i_2 = -n i_1$ | 电流互补 | 代数约束 |
| $v_1 i_1 + v_2 i_2 = 0$ | 瞬时功率守恒 | 代数约束 |
| $Z_2' = n^2 Z_2$ | 阻抗折算（次→主） | 参数映射 |
| $Z_1' = Z_1 / n^2$ | 阻抗折算（主→次） | 参数映射 |

### 三相端口矩阵方程

对三相双绕组变压器，abc 域端口方程组：

$$
\mathbf{v}_1 = \mathbf{N} \, \mathbf{v}_2 \tag{8}
$$

其中 $\mathbf{N} = n \mathbf{I}$（$\mathbf{I}$ 为 $3\times3$ 单位矩阵）当且仅当三相磁路解耦且无相间耦合时成立。实际变压器（含零序互耦）需将 $\mathbf{N}$ 扩展为非对角矩阵。

### 复变比表示

$$
a = n e^{j\theta}, \quad \theta \in \{0, \pm30^\circ, \pm60^\circ, \pm150^\circ\} \tag{9}
$$

不同连接组别对应不同 $\theta$ 值：Yyn0（$\theta=0$）、YNd11（$\theta=-30^\circ$）、Yd1（$\theta=+30^\circ$）等。

### Z 域传递函数（频变端口模型基础）

对宽频端口模型（见[[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-.md]]），变压器的离散端口关系可写为：

$$
i_1(k) = G_0 v_1(k) + \sum_{j=1}^{M} g_j i_1(k-j) + \sum_{j=1}^{M} h_j v_1(k-j) \tag{10}
$$

其中 $M$ 为历史项阶数，$G_0$ 为当前项电导，$g_j$、$h_j$ 为拟合系数。双线性变换 $s = (2/\Delta t)(1-z^{-1})/(1+z^{-1})$ 将连续域有理函数映射为上式所示的递推差分方程。

## 分类与变体

| 变体 | 机制 | 适用场景 | 主要限制 |
|------|------|----------|----------|
| 单相理想变压器 | 标量匝比约束 $v_1=n v_2$ | 推导、基准换算、低阶接口 | 无法表达三相连接和零序通道 |
| 三相理想连接（解耦） | $\mathbf{v}_1 = n\mathbf{I} \mathbf{v}_2$ | 接线组别、相移、线-相电压转换 | 不含漏抗、磁化支路和相间耦合 |
| 三相理想连接（含耦合） | $\mathbf{v}_1 = \mathbf{N} \mathbf{v}_2$，$\mathbf{N}$ 非对角 | 五柱式铁芯、相间磁耦合、三相不平衡 | 模型复杂度和参数获取难度增加 |
| 带分接头理想变压器 | 可变 $n(t)$ 或复变比 $a(t)=n(t)e^{j\theta(t)}$ | OLTC 电压调节、潮流初始化 | OLTC 机械动态和离散切换未建模 |
| 理想变压器+串联漏抗 | 理想约束串联 $R+j\omega L$ | 常规短路计算、EMT 网络等效 | 高频响应和饱和效应不足 |
| 多绕组理想变压器 | 多端口约束矩阵 $\mathbf{v}_1 = \mathbf{N} \mathbf{v}_2$ | 自耦变压器、三绕组、多端口接口 | 需处理功率守恒和矩阵秩问题 |
| 频变端口等值 | Z 域递推方程或 RLC 网络综合 | 高频暂态、雷电侵入波、操作过电压 | 依赖频响测量数据，非线性不足 |

## 关键技术挑战

### 挑战一：代数环与矩阵奇异

当多个理想变压器形成闭合回路时（如环形网络中的串联变压器），端口约束构成代数环，若不显式处理会导致节点方程组奇异。解决方案包括：

- **约束排序**：在网络拓扑分析中显式标定哪些节点电压由匝比约束确定，避免冗余方程
- **广义节点分析**（MNA）扩展：将变压器约束作为独立方程加入系统矩阵
- **诺顿等值预处理**：将理想变压器先用诺顿电流源等值，再接入网络方程

### 挑战二：零序通道与铁芯结构的耦合

理想等效假设磁路无泄漏，但实际上零序磁通路径与铁芯几何结构密切相关。Y/Y/Y 接线的三相三柱式变压器零序阻抗大，而五柱式铁芯或壳式铁芯的零序通道不同。由理想变压器出发，若不补充零序网络，会错误地估计接地故障电流和零序电压分布。

### 挑战三：励磁支路的拓扑位置

对偶磁路模型（[[duality-based-transformer-modeling-for-low-frequency-transients]]）指出：非线性励磁支路必须位于与实际铁芯几何一致的对偶拓扑位置，而非任意放置在 T 型或 Γ 型等值中心。错误位置会导致数值振荡即使在端口阻抗匹配的情况下也会发生。

### 挑战四：频变参数与端口等值的频率边界

宽频端口模型（如[[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions.md]]）通过矢量拟合将端口频率响应综合为 RLC 网络，但其有效频率范围受测量频带和拟合阶数约束。对 $100\,\text{kHz}$ 以上的暂态，测量数据可能不足以覆盖关注频段。

### 挑战五：OLTC 动态与离散切换

带分接头变压器的变比 $n(t)$ 随 OLTC 机械调节而离散变化（在 EMT 中通常为事件驱动）。每一次分接变化都会导致网络拓扑突变，需在仿真中正确处理切换前后的过渡过程，否则可能产生数值冲击。

## 量化性能边界

| 指标 | 典型数值 | 条件 | 来源 |
|------|----------|------|------|
| 功率守恒误差 | $< 10^{-12}$ p.u. | 理想变压器，无数值噪声 | 数学推导 |
| 阻抗折算精度 | 取决于数值精度 | 浮点精度 $\varepsilon$ 下 | 数学推导 |
| 双线性变换误差 | $\omega \Delta t < 0.35$（1%误差） | $\omega$ 为关注频率，$\Delta t$ 为步长 | [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-.md]] |
| Bi-third 变换容许步长 | $\omega \Delta t < 0.9$（1%误差） | 同上，但用 bi-third 变换 | 同上 |
| 低频暂态建模适用范围 | DC $\sim 2\,\text{kHz}$ | 线性端口等值，不含饱和 | [[duality-based-transformer-modeling-for-low-frequency-transients]] |
| 高频端口等值频率范围 | $10\,\text{Hz} \sim 1\,\text{MHz}$ | 矢量拟合 RLC 综合，依赖测量数据 | [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions.md]] |
| 快速开断暂态过电压 | 需含频率相关电容和相间耦合 | 仅靠理想匝比+漏抗不足 | [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow]] |

> **注**：原文未报告可核验的数值结果时，以上数据基于方法机制推断或来自原文有明确依据的片段。

## 适用边界与选择指南

### 选择原则

| 场景 | 推荐模型 | 原因 |
|------|----------|------|
| 推导和理论分析 | 单相理想变压器 | 最简形式，清晰表达匝比约束 |
| 多电压等级网络归算 | 理想变压器+基准换算 | 标幺系统中变比为 1 |
| 含饱和/涌流的研究 | 需加入[[magnetic-saturation-modeling]] | 理想等效不含非线性励磁 |
| 高频暂态（>10 kHz） | 频变端口 RLC 等值（Vector Fitting） | 理想模型无频率依赖 |
| 内部故障分析 | 分布式磁阻网络（DRNM） | [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based]] |
| 零序接地故障电流计算 | 需补充零序网络而非理想等效 | 理想等效不区分铁芯结构 |
| GIC 低频直流偏磁 | Jiles-Atherton 磁滞模型+双侧对偶 | [[an-improved-low-frequency-transformer-model-for-use-in-gic-studies]] |
| 实时仿真 | BCTRAN 或频变端口等值（降阶） | 理想模型为实时仿真提供了可降阶接口 |

### 不适用场景速查

- ❌ 励磁涌流峰值估计 → 需要饱和模型
- ❌ 铁芯饱和导致的谐波放大 → 需要非线性磁化曲线
- ❌ 零序接地故障电流精确计算 → 需要具体铁芯结构的零序阻抗
- ❌ 高频绕组电压分布（>100 kHz）→ 需要分布参数模型
- ❌ 变压器保护整定（励磁涌流识别）→ 需要饱和+时间常数模型

## 相关页面

- [[transformer-model]] — 变压器模型综合入口，含详细模型层次结构
- [[transformer-network]] — 理想变比、漏抗、耦合和宽频端口模型的综合入口
- [[equivalent-circuit-method]] — 理想变压器与实际支路组合为等效电路的方法
- [[magnetic-saturation-modeling]] — 理想模型刻意忽略的非线性励磁问题
- [[multi-winding-transformer]] — 多绕组变压器的专门模型页
- [[converter-transformer-model]] — 换流站场景的专门模型页
- [[norton-equivalent]] 和 [[thevenin-equivalent]] — 端口源等效，与理想变压器常一起用于网络简化
- [[duality-based-transformer-modeling-for-low-frequency-transients]] — 低频暂态变压器对偶建模的物理拓扑原则
- [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-.md]] — Z 域端口递推建模
- [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions.md]] — 高频端口频变导纳矩阵建模
- [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow.md]] — 快速开断暂态中理想模型的局限性证据

## 来源论文

- Pordanjani 等 2022 — 分布式磁阻网络（DRNM）完全电路化变压器建模，可嵌入EMTP并通过ANSYS Maxwell验证
- Dennetière 等 2009 — EMTP-RV与FLUX3D场路耦合接口，用于变压器空载合闸涌流研究
- Marti 等 1993 — 高频变压器端口频变导纳矩阵矢量拟合，EMTP可用的宽频RLC网络综合
- Morched 等 1993 — 宽频端口模型奠基性论文（引自高频变压器页面）
- Zhang 等 2025 — 通用解耦等效电路模型（Universal Decoupled Equivalent Circuit）用于固态变压器加速EMT仿真
- Xu 等 2025 — 多有源桥式电力电子变压器简化EMT模型
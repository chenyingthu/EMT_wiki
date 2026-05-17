---
title: "频率相关建模"
type: topic
tags: [frequency-dependent, vector-fitting, fdne, passivity, wideband, rational-approximation, fdne-model, phase-domain]
created: "2026-04-13"
updated: "2026-05-17"
---

# 频率相关建模

## 定义

频率相关建模（Frequency-Dependent Modeling）是 EMT 仿真中处理线路、电缆、变压器、接地系统、网络等值等元件参数随频率变化特性的一系列技术。核心问题是：如何在宽频精度、无源性保证、模型阶数和计算成本之间取得最优取舍。

频率相关特性广泛存在于以下场景：

- 输电线路和地下电缆的阻抗 $Z(f)$、导纳 $Y(f)$ 随频率变化（趋肤效应、大地回路、土壤参数）
- 变压器、接地网的宽频阻抗特性
- 电力电子端口的阻抗频率扫描
- 外部网络的频变等值（FDNE）

## EMT 中的角色

在 EMT 仿真体系里，频率相关建模承担三类角色：

1. **网络等值（外部网络降阶）**：将非研究区域的外部网络等效为宽频阻抗/导纳模型，大幅降低仿真规模。代表方法为 FDNE（Frequency Dependent Network Equivalent）。
2. **输电线路/电缆建模（元件级）**：在线路层面刻画频率相关的分布参数特性，替代传统的恒定参数 Bergeron / π 型等效。
3. **设备端口宽频建模**：基于测量或解析推导构建变压器、接地网、DC-DC 变换器等的宽频两端口模型。

核心挑战有三：① 宽频高精度拟合（矢量拟合等有理逼近）；② 无源性强制（保证等效网络不产生能量）；③ 时域实现效率（递归卷积、状态空间、Norton 等效）。

## EMT 建模方法

### 1. 矢量拟合（Vector Fitting）

矢量拟合是 EMT 频变建模的核心工具，由 Gustavsen 等人提出。将网络端口的频率响应（阻抗或导纳）表示为有理函数：

$$
Y(s) = \sum_{k=1}^{N} \frac{r_k}{s - p_k} + d + se
$$

其中 $r_k$ 为留数（residues），$p_k$ 为极点（poles），$d$ 和 $e$ 为常数项。拟合后得到极点-留数形式，可转换为 RLC 并联支路或状态空间实现。

**关键优势**：自动生成实数负极点（对于无源物理系统），可直接用梯形法稳定嵌入 EMT。

**主要变体**：
- **VF（Vector Fitting）**：标准矢量拟合，要求复极点成共轭对
- **CVF（Complex Vector Fitting）**：复数矢量拟合，无需共轭约束（由 Gao 等人 2024 提出）
- **Frequency Partitioning Fitting（FPF）**：频率分区拟合，针对不同频段自适应加权（Xu 等人 2015）

### 2. 频变网络等值（FDNE）

FDNE 由 Morched 等人于 2004 年提出，将外部线性网络压缩为宽频等效端口模型。核心思想是：用矢量拟合获取网络端口的频域导纳矩阵 $Y(j\omega)$，再将拟合结果实现为 RLC 网络（Norton 等效）。

**Brune-Tellegen 网络综合法（Ahmadi 等 2021）**：将拟合的频域数据直接综合为严格无源的多端口网络，无需后处理无源性校正。

典型 FDNE 构建流程：
1. 在宽频范围内对外部网络做频域扫描，获取端口导纳/阻抗频率响应 $Y_{ij}(j\omega_k)$
2. 对 $Y_{ij}$ 做矢量拟合，得到极点-留数表示
3. 用 Brune 或 Tellegen 方法将拟合结果综合为 RLC 支路网络
4. 嵌入 EMT 仿真器作为 Norton 等效：$i_{hist}(t) = \sum_k A_k e^{p_k t}$

### 3. 状态空间实现（State-Space Realization）

将有理逼近的结果转换为状态空间形式：

$$
\dot{x} = Ax + Bu,\quad y = Cx + Du
$$

**优势**：适合并行计算、模型降阶（Balanced Truncation）、实时仿真。
**挑战**：矩阵 $A$ 的特征值必须分布在左半平面（无源系统要求）。

Gustavsen（2012）的递归卷积方法将状态空间与历史电流源结合，实现无递归的状态空间矩阵：

$$
i_{hist}(t) = \sum_{k=1}^{N_r} A_k \, i(t-\tau_k)
$$

### 4. 时域递归卷积（Recursive Convolution）

矢量拟合得到的极点-留数模型可写为时域卷积形式：

$$
i(t) = G_0 v(t) + \sum_{k=1}^{N} \int_0^t h_k(t-\tau) v(\tau) d\tau
$$

其中 $h_k(t) = r_k e^{p_k t}$。离散化后变为递归形式：

$$
i_n = G_0 v_n + \sum_{k=1}^{N} A_k \, v_{n-k}
$$

每步仅需存储历史电压/电流值，计算量 $O(N_r)$，适合 GPU/FPGA 并行。

### 5. 相域频变建模（FDPD）

相域频变输电线路模型（Phase-Domain Frequency-Dependent），直接在相域实现频率相关特性，无需模态变换。

**关键公式**（Noda 等 2007）：将频变阻抗 $Z(s, \omega)$ 用矢量拟合逼近为有理函数后，在时域用梯形积分求解伴随电路。FDPD 模型中，耦合电导矩阵随频率变化：

$$
G(f) = G_0 + \sum_{k=1}^{N} \frac{G_k}{1 + jf/f_k}
$$

**FPGA 实现**（Cai 等 2021）：在 FPGA 上实现全流水线并行化 FDPD 模型，通过自定义高精度浮点格式突破实时仿真速度限制。实测 200 ns 步长（IEEE 39 节点）。

### 6. 分区拟合与直流校正（Partitioned Fitting + DC Correction）

Gustavsen（2012）提出两阶段策略解决传统单阶段拟合的数值问题：

**第一阶段（分区拟合）**：将频带分为高频区和低频区，分别拟合以避免大留数/极点比导致的数值病态：

$$
Y(s) = Y_{HF}(s) + Y_{LF}(s)
$$

**第二阶段（直流校正）**：改进有理函数形式并引入低频加权因子，强制 $Y(0)$ 精确等于直流导纳：

$$
\lim_{s\to 0} Y(s) = G_{DC}
$$

该方法有效解决了地下电缆等长线路模型的直流精度问题。

### 7. 无源性强制（Passivity Enforcement）

矢量拟合得到的模型未必无源。无源性强制通过扰动留数矩阵确保模型在整个频段内无源：

$$
\Delta R = -\frac{1}{2\pi}\int_{-\infty}^{\infty} \ln|\det(Y(j\omega))|\, d\omega
$$

**扰动方法**（Gao 等 2024）：对特征导纳的留数、极点和常数矩阵做耦合扰动，并引入精度保持度量（Frobenius 距离）以最小化对模型精度的修改。

**在线无源性强制**（De Silva 等 2018）：结合 RLS（递推最小二乘）实时辨识频变导纳，并同步进行无源性校正，无需先验参数。

## 形式化表达

### 核心模型方程

**频变阻抗**（输电线路电报方程）：

$$
\frac{\partial V(x,s)}{\partial x} = -Z(s) \, I(x,s),\quad \frac{\partial I(x,s)}{\partial x} = -Y(s) \, V(x,s)
$$

其中 $Z(s,\omega) = R(\omega) + sL(\omega)$，$Y(s,\omega) = G(\omega) + sC(\omega)$，均为频率的复函数。

**传播常数和特性阻抗**：

$$
\gamma(s) = \sqrt{Z(s)Y(s)},\quad Z_c(s) = \sqrt{Z(s)/Y(s)}
$$

**矢量拟合有理逼近**：

$$
\hat{H}(s) = \sum_{k=1}^{N} \frac{r_k}{s - p_k} + d + se
$$

**时域递归卷积（离散化）**：

$$
i_n = G_0 v_n + \sum_{k=1}^{N_r} A_k^{(j)} \, v_{n-j},\quad A_k^{(j)} = r_k \frac{e^{p_k \Delta t} - 1}{p_k}
$$

**Norton 等效**（FDNE 嵌入 EMT）：

$$
i_{port}(t) = G_{eq} \, v(t) + \sum_{k=1}^{N} I_k^{hist}(t)
$$

**FDPD 相域等效电路参数**（Noda 2007）：

$$
\Delta t \cdot G_k = \frac{2C_k}{\Delta t} + G_k,\quad \Delta t \cdot A_k = \frac{2L_k}{\Delta t} + R_k
$$

**无源性约束（Brune 综合）**：

$$
\text{对所有 } \omega \geq 0:\quad Y(j\omega) + Y^H(j\omega) \succeq 0
$$

## 关键技术挑战

### 挑战一：宽频拟合精度与阶数权衡

矢量拟合的精度直接取决于拟合阶数 $N$ 和频域采样点数量。过低的阶数无法捕捉精细的谐振峰，过高的阶数增加计算成本和实时部署难度。Gao 等人（2025）提出低阶逼近方法，通过先定位零极点再非线性优化，在保证精度的同时将模型阶数从 20+ 降至 8-12。

### 挑战二：无源性破坏与数值发散

矢量拟合的综合结果可能在某些频段呈现"主动"特性（负电阻），导致 EMT 仿真发散。解决办法包括：
- **后处理无源性强制**（Gustavsen 2012）：扰动留数使所有特征导纳实部非负
- **Brune-Tellegen 综合**（Ahmadi 2021）：在综合阶段内在保证无源，无需后处理
- **在线 RLS 校正**（De Silva 2018）：实时监测并修正无源性违规

### 挑战三：直流值精确性

频域拟合在 $f=0$ 处往往精度不足，因为低频段采样点稀疏且数值稳定性差。分区拟合 + 低频加权（Gustavsen 2012）或强制直流约束（An Enhanced Method to Achieve Exact DC Values for Frequency-Dependent Transmission Lines）可有效解决。

### 挑战四：大地回路与土壤频变

大地返回阻抗 $Z_g(\omega)$ 随频率剧烈变化（从 $10^{-2}$ 到 $10^{6}$ Hz），传统均匀土壤模型在高频（>100 kHz）严重失真。Carson（1926）-Pollaczek 公式和分层土壤格林函数矩量法（Tsiamitros 2008）是两类主流建模路径。

### 挑战五：实时仿真计算效率

FDPD/FDNE 模型的时域实现需要每步更新所有历史项，并行化（GPU/FPGA）是突破实时瓶颈的关键。Cai 等人（2021）在 FPGA 上实现 200 ns 步长；Gao 等人（2024）用 CVF 复数矢量拟合结合 C 语言并行化，相比 MATLAB 加速 15-25×。

## 量化性能边界

| 方法 | 精度 | 实时步长 | 适用场景 | 代表数据 |
|------|------|---------|---------|---------|
| 矢量拟合 + 递归卷积 | <1% vs 全波 | 50 μs | 通用频变建模 | Gustavsen 2012 |
| FDPD（相域）+ FPGA | <0.5% | 200 ns | 实时仿真 | Cai 2021 |
| FDNE + Brune 综合 | <2% vs 详细模型 | 50-100 μs | 外部网络等值 | Ahmadi 2021 |
| 分区拟合 + DC 校正 | <0.1% DC | 10-50 μs | 长电缆/直流线路 | Gustavsen 2012 |
| CVF + 并行 C 实现 | 与 VF 相当 | ~10 μs | 大规模矩阵综合 | Gao 2024 |
| 在线 RLS + 无源性 | 实时更新 | 1 μs | 动态等值 | De Silva 2018 |

**关键边界数据**：
- 地下电缆超谐波建模（2-150 kHz）：黑盒 VF 方法精度 >95%（Herath 2024）
- IEEE 39 节点系统：FDPD FPGA 实时仿真 200 ns（比实时快 50×）
- 架空线路雷电暂态（>1 MHz）：土壤频变模型使峰值误差从 25% 降至 3%（Gustavsen 2006）

## 适用边界与选择指南

| 场景 | 推荐方法 | 原因 |
|------|---------|------|
| 外部网络等值 | FDNE + Brune/ Tellegen | 自动无源保证，宽频精度 |
| 输电线路宽频（架空） | FDPD 或频变 Bergeron | 相域直接，无需模态变换 |
| 地下电缆 | 分区拟合 + DC 校正 | 精确直流响应，避免数值病态 |
| 实时硬件仿真 | FDPD + FPGA | 流水线并行，200 ns 步长 |
| 雷电/开关暂态 | 频变 JMartí + 矢量拟合 | 宽频覆盖，精度高 |
| 风电场聚合 | 黑盒 VF + 测量数据 | 参数来自实测，无需解析模型 |
| 谐波交互分析 | 动态相量 + FDNE | 同时捕捉稳态谐波和暂态过程 |

**失效边界**：当系统包含强非线性（故障电弧、饱和铁芯）时，频变等值仅在故障前/后单一网络状态下有效，需要分段建模。

## 相关方法

- [[vector-fitting|矢量拟合]] — 有理函数逼近频域响应
- [[passivity-enforcement|无源性强制]] — 保证 FDNE/FDTD 模型数值稳定
- [[state-space-method|状态空间法]] — 频变模型的矩阵实现
- [[fdne-model|频变网络等值]] — 外部网络宽频等效
- [[recursive-convolution|递归卷积]] — 频变模型的时域卷积实现
- [[model-order-reduction|模型降阶]] — 降低 FDNE 状态空间矩阵阶数

## 相关模型

- [[transmission-line-model|输电线路模型]] — 频变分布参数线路
- [[cable-model|电缆模型]] — 频变地下电缆
- [[transformer-model|变压器模型]] — 宽频变压器端口模型
- [[grounding-system-model|接地系统模型]] — 频变接地阻抗
- [[network-equivalent|网络等值]] — 系统级频变等值

## 相关主题

- [[harmonic-analysis|谐波分析]] — 宽频谐波建模
- [[real-time-simulation|实时仿真]] — 频变模型硬件加速
- [[co-simulation|混合仿真]] — EMT-TS 联合仿真中的频变接口
- [[wideband-modeling|宽频建模]] — 全频段统一建模框架

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Morched 等 - Multi-port FDNE for EMTP | 2004 | FDNE 基础工作，多端口扩展 |
| Gustavsen - Vector Fitting | 2004 | VF 标准算法，相模变换 |
| Ahmadi 等 - Guaranteed passive FDNE via Brune/Tellegen | 2021 | 自动无源保证的网络综合 |
| Cai 等 - FDPD on FPGA | 2021 | 200 ns 步长实时仿真 |
| Gao 等 - CVF parallel C implementation | 2024 | 复数 VF 并行加速 15-25× |
| Gustavsen - Partitioned Fitting + DC correction | 2012 | 直流校正两阶段方法 |
| Pereira 等 - VFDLM (Corona + FD) | 2022 | 电晕效应与频变特性耦合模型 |
| De Silva 等 - Online passivity enforced FDNE | 2018 | RLS 实时无源性校正 |
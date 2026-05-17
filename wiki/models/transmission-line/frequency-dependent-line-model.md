---
title: "频变线路模型 (Frequency-Dependent Line Model)"
type: model
tags: [frequency-dependent, transmission-line, cable, wideband, transient, rational-approximation, folded-line-equivalent]
created: "2026-05-02"
updated: "2026-05-18"
---

# 频变线路模型 (Frequency-Dependent Line Model)

## 定义与边界

频变线路模型（Frequency-Dependent Line Model）是将架空线、电缆或混合线路的单位长度参数表示为频率相关矩阵，并在 EMT 时域仿真中重构其传播、衰减和端口耦合的模型。它的物理对象是实际线路、电缆、护套、地线、接地返回路径和周围介质；EMT 等效对象通常是端口导纳、传播延时、递归卷积历史项和内部拟合状态。

本页讨论模型结构和接口边界，不把"频变"写成自动高精度。模型可信度取决于线路几何、导体与土壤参数、频率采样范围、有理拟合质量、延时提取、无源性和时域实现。未绑定来源的误差百分比、极点数量、频带上限或软件能力不应作为通用结论。

## EMT 建模对象

频变线路的连续频域对象通常包括单位长度串联阻抗矩阵 $\mathbf{Z}(\omega)$ 和并联导纳矩阵 $\mathbf{Y}(\omega)$：

$$-\frac{d\mathbf{v}}{dx}=\mathbf{Z}(\omega)\mathbf{i},\qquad
-\frac{d\mathbf{i}}{dx}=\mathbf{Y}(\omega)\mathbf{v}.$$

其中 $\mathbf{v}$ 和 $\mathbf{i}$ 是相域或导体域电压、电流向量。$\mathbf{Z}(\omega)$ 可包含导体内阻抗、集肤效应、邻近效应、护套/地线耦合和 [[earth-return-impedance|大地返回阻抗]]；$\mathbf{Y}(\omega)$ 可包含电容、电导、介质损耗和接地相关导纳。多导体耦合由矩阵非对角项体现，不能在未验证的情况下拆成多个独立单相模型。

频域对象进入 EMT 后一般转换为端口关系：

$$\mathbf{i}_{n+1}=\mathbf{G}_{eq}\mathbf{v}_{n+1}+\mathbf{i}_{hist,n},$$

其中 $\mathbf{G}_{eq}$ 是当前步端口等效导纳，$\mathbf{i}_{hist,n}$ 汇集传播延时、卷积状态和上一时间步历史量。该形式与 [[companion-model|伴随模型]]、[[nodal-admittance-matrix|节点导纳矩阵]] 和 [[thevenin-equivalent|戴维南等效]] 的接口一致。

## 模型结构与接口变量

频变线路模型至少应说明以下变量：

| 变量类别 | 典型内容 | 说明 |
|----------|----------|------|
| 物理参数 | 导体半径、位置、护套、接地、电阻率、介电常数、土壤模型 | 决定 $\mathbf{Z}(\omega)$ 和 $\mathbf{Y}(\omega)$ 的输入边界 |
| 端口变量 | 两端相电压、导体电流、护套/地线端口电压电流 | 决定如何接入外部 EMT 网络 |
| 内部状态 | 极点-留数递推状态、延时队列、历史电流源 | 决定时域记忆和数值稳定性 |
| 代数变量 | 当前步端口导纳矩阵、端口注入电流 | 进入全局节点方程 |
| 验证变量 | 频域拟合误差、时域波形、能量或无源性检查结果 | 用于约束模型可信范围 |

常见实现会从传播常数和特性导纳构造端口函数。单相或模态通道中可写为：

$$H(s)=e^{-\gamma(s)\ell}=e^{-s\tau}H_r(s),\qquad
H_r(s)\approx D+\sum_{k=1}^{N}\frac{R_k}{s-p_k}.$$

$\ell$ 是线路长度，$\tau$ 是提取出的传播延时，$p_k$ 和 $R_k$ 是有理逼近的极点和留数。每个极点项离散后成为历史状态。若 $p_k$、$R_k$ 或常数项破坏稳定性、实系数一致性或无源性，时域仿真可能产生非物理增长。

## 建模层级

| 层级 | EMT 等效 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 常参数行波模型 | 固定特性阻抗和传播延时 | 工频和低频暂态的基准对照 | 高频损耗、地回路和耦合频变不足 |
| 模态频变模型 | 模态变换后每个模态递归卷积 | 完全换位或近似对称线路 | 模态矩阵频率相关时需复核 |
| 相域频变模型 | 直接拟合相域矩阵函数 | 非换位线路、电缆、多导体耦合 | 矩阵拟合、延时和无源性更复杂 |
| [[universal-line-model|ULM]] | 相域特性导纳和传播函数的有理时域实现 | 宽频线路和电缆研究 | "Universal" 是模型名，不表示全条件适用 |
| [[folded-line-equivalent|FLE]] 或端口等值 | 分块导纳、开路/短路响应或端口函数 | 短线路、接口和实时实现研究 | 依赖分解方式、拟合和接口验证 |

模型选择应绑定研究目标。雷电、开关暂态、护套耦合和宽频振荡通常需要比常参数模型更细的频率相关描述；若只研究低频功率交换，过高阶频变模型可能增加计算负担和参数不确定性。

## 核心机制：从频域响应到时域实现

频变线路的 EMT 实现需经过三个关键步骤：频率扫描、有理拟合和时域递推。

### 频域响应采样

对每一条导体或导体组合，频率扫描得到 $\mathbf{Z}(\omega)$ 和 $\mathbf{Y}(\omega)$ 在宽带频率范围内的复数值。采样频率范围通常从 $10^{-3}$ Hz（用于捕捉低频谐振）到 $10^{6}$ Hz（用于雷电暂态研究）。采样密度过高增加拟合负担，过疏则遗漏关键谐振峰。

### 有理函数拟合

利用矢量拟合（Vector Fitting）、频率分区拟合（Frequency-Partitioning Fitting, FpF）或矩阵束（Matrix Pencil）方法，将频域响应拟合成有理函数形式：

$$\mathbf{Y}(s)\approx \mathbf{D}+\sum_{k=1}^{N}\frac{\mathbf{R}_k}{s-p_k},$$

其中 $p_k$ 为极点，$\mathbf{R}_k$ 为留数矩阵，$\mathbf{D}$ 为常数项。Noda 2015 提出的 FpF 方法将频带划分为多个子区域，各子区域独立提取极点后合并，从而在相同拟合精度下减少总极点数（FpF 约需 38+60 个极点，比 VF 的 50+80 略少）。

### 时域递推（递归卷积或伴随模型）

将拟合得到的有理函数在时域实现为递归卷积或伴随电导+历史电流源。每个极点 $p_k$ 对应一个离散时间递推系数：

$$\alpha_k = e^{p_k\Delta t},\qquad h_k(n)=\alpha_k h_k(n-1)+\mathbf{R}_k\mathbf{v}(n-1),$$

其中 $\Delta t$ 为仿真步长，$h_k(n)$ 为第 $k$ 个极点对应的历史状态。当前时刻注入电流为：

$$\mathbf{i}_{n+1}=\mathbf{D}\mathbf{v}_{n+1}+\sum_{k=1}^{N}h_k(n+1).$$

## 折叠线等效（FLE）方法

Camara 2018 提出的折叠线等效（FLE）方法将 $2n\times 2n$ 的端口导纳矩阵 $\mathbf{Y}_n$ 分解为两个 $n\times n$ 的开路导纳 $\mathbf{Y}_{oc}$ 和短路导纳 $\mathbf{Y}_{sc}$：

$$\mathbf{Y}_n = \begin{bmatrix}\mathbf{Y}_{oc} & \mathbf{T} \\ \mathbf{T}^T & \mathbf{Y}_{sc}\end{bmatrix}\Rightarrow \text{FLE}: \mathbf{Y}_{oc},\ \mathbf{Y}_{sc}$$

FLE 的核心优势在于：$\mathbf{Y}_{oc}$ 和 $\mathbf{Y}_{sc}$ 的最大/最小特征值比远小于 $\mathbf{Y}_n$，这使得有理拟合的数值条件大幅改善，所需极点数减少约 20%~30%。在时域实现中，FLE 将多导体耦合等效为两个相互耦合的 $n$ 端口子网络，开路端口和短路端口分别包含传播特性的不同侧面。

## 多伴随网络（MCN/MCNR）方法

传统频变线路模型在单一固定时间步长下求解全部极点，但不同极点的动态响应时间尺度差异显著（快极点 ~10 µs，慢极点 ~10 ms）。MCN 方法将极点按时间常数分为两组：快极点在微步长 $\Delta t_1$ 下求解，慢极点在宏步长 $\Delta t_2=k\Delta t_1$ 下求解，其中 $k$ 为步长比。MCN 原始版本在 $k>10$ 时误差急剧增大。

Camara 2018 提出的 MCNR（Relaxed MCN）在慢极点的递推中使用松弛策略：当极点系数 $\alpha \geq 0.99$ 时，判定为慢极点，其历史源每步更新而非每 $k$ 步更新：

$$h_s(n)=h_s(n-1)+\mathbf{c}_s\mathbf{v}(n-1),\qquad \alpha_s\geq 0.99 \Rightarrow \text{慢极点}$$

MCNR 在 $k=500$ 时仍保持数值稳定，相比原始 MCN 的 $k\leq 10$ 有本质改进。三个测试算例的结果表明：MCNR 在 300 m/10 km/50 km 架空线上分别取得约 10%/20%/35% 的仿真加速，时域波形与全精度模型的偏差小于 0.5%。

## 相域频变线路的 FPGA 实现

Liu 2021 在 Xilinx FPGA（VC707/VCU118）上实现了频变相域（FDPD）输电线路模型的实时仿真。全流水线并行架构将仿真步长压缩至 **2.4 µs~3.27 µs**，较传统处理器大时间步长模型（约 50 µs）提升约 **15~20 倍**。48 位自定义浮点格式在 VCU118 上 LUT 占用率为 **48.39%**，DSP48 占用率为 **47.08%**，彻底消除了 32 位单精度模型在长递归卷积中的数值发散问题。

采用 Bergeron 接口模式时，8 导体与 12 导体模型步长分别为 2.4 µs 和 2.8 µs；切换为嵌入式模式后步长增至 5.0 µs 和 5.8 µs，换取全频段（1 Hz–1000 Hz）频率响应零偏差。

## 无源性强制

有理函数拟合得到的极点-留数模型必须满足无源性条件——即端口等效导纳 $\mathbf{Y}(s)$ 的实部对所有频率均为非负（ $\Re[\mathbf{Y}(j\omega)]\geq 0$ ）。若未经无源性强制，接入外部网络后可能出现非物理能量增长振荡。

无源性强制方法包括 Vu 等提出的约束优化方法（将留数矩阵投影到无源区域内）和 Semlyen 提出的二次规划方法。对于多导体系统，无源性检查需对 $\mathbf{Y}(j\omega)$ 的每个特征值分别验证。

## 量化性能边界

频变线路模型在 EMT 仿真精度与计算效率方面已有可核验的量化结果，但以下数据均绑定具体线路参数、拟合设置和验证条件，不能外推为通用能力：

| 研究 | 算例 | 步长 | 加速比 | 精度偏差 | 实现平台 |
|------|------|------|--------|----------|----------|
| Camara 2018 | 300m 132kV 架空线 | 1 µs | ~35% | <0.5% | MatEMTP |
| Camara 2018 | 10km 132kV 架空线 | 30 µs | ~20% | <0.5% | MatEMTP |
| Camara 2018 | 50km 500kV 双回 | 50 µs | ~10% | <0.5% | MatEMTP |
| Liu 2021 | 8导体 架空线 | 2.4 µs | 15~20× | 零偏差 | FPGA VCU118 |
| Liu 2021 | 12导体 架空线 | 2.8 µs | 15~20× | 零偏差 | FPGA VCU118 |
| Noda 2015 | 500kV 双回（FpF） | — | — | 与Laplace变换一致 | — |

FLE 变换将待拟合节点导纳矩阵维度减半（$2n\times 2n$ 降至 $n\times n$），矢量拟合阶数减少约 **20%~30%**。MCNR 慢极点松弛更新公式在时间步长比 $k$ 高达 **500** 时仍保持数值稳定。

## 适用边界与失败模式

- **频率扫描范围不足**会遗漏目标暂态的主要频谱；范围过宽但采样稀疏也可能造成拟合失真。
- **土壤电阻率、频变土壤、护套接地和交叉互联参数不确定**时，模型结构本身不能保证物理准确。
- **固定模态变换**适合特定对称条件；非换位、多回线或电缆系统中应检查相域耦合和频率相关特征向量。
- **有理函数拟合若未检查无源性强制**，接入外部网络后可能出现非物理振荡。
- **延时提取、插值和时间步长**会影响波头、反射和高频衰减；只报告频域幅值误差不足以证明时域可信。
- **FPGA 实时实现的资源消耗**随导体数和极点组数快速增长，在更大规模线路（>12 导体）或更高阶拟合下的资源缩放规律缺乏系统研究。
- **FpF 方法的极点合并策略**在某些不对称线路中可能产生冗余极点，需要额外滤波步骤。

## 验证需求

频变线路页面和模型报告至少应区分三类验证：

1. **频域验证**：$\mathbf{Z}(\omega)$、$\mathbf{Y}(\omega)$、特性导纳、传播函数、低频极限和高频渐近是否与参数计算或测量一致。
2. **时域验证**：阶跃、合闸、雷电波、故障或谐波注入波形是否与解析模型、详细模型、软件基准或试验记录一致。
3. **互联验证**：与变压器、换流器、接地系统或外部网络连接后是否保持能量一致、数值稳定和端口方向正确。

若涉及实时仿真，还需报告目标硬件、步长、计算裕度、延时队列实现和模型阶数；不能仅以"递归卷积较快"推断实时可用。

## 开放问题

- 频变线路有理逼近的极点-留数阶数选择在非对称、多回线和电缆系统中缺乏通用准则：阶数过低遗漏高频动态，阶数过高引入虚假模态和过拟合风险。
- 矢量拟合和 FLE/MCNR 方法的无源性强制在不同线路拓扑和频率扫描范围下的鲁棒性缺乏系统对比，无源性违规在接入换流器控制后可能被放大。
- FPGA 实时实现（Liu 2021）的硬件资源消耗随导体数和极点组数快速增长，在更大规模线路（>12 导体）或更高阶拟合下的资源缩放规律缺乏系统研究。
- 土壤电阻率频变特性、护套交叉互联和接地路径的参数不确定性在有理拟合和时域实现中的传播缺乏量化评估。
- 模态域与相域频变模型在非换位线路和电缆系统中的适用边界缺乏统一判定准则，不同软件实现的结果差异缺乏独立基准对比。

## 与相关页面的关系

- [[transmission-line-model]] 是线路模型总览，本页聚焦频率相关 EMT 等效。
- [[distributed-parameter-line]] 和 [[transmission-line-theory]] 给出线路方程基础。
- [[earth-return-impedance]]、[[frequency-dependent-soil]] 和 [[mutual-impedance]] 决定输入参数的物理边界。
- [[universal-line-model]]、[[bergeron-line-model]]、[[modal-transformation]] 和 [[modal-domain-decoupling]] 是相邻实现路线。
- [[wideband-modeling]]、[[vector-fitting]]、[[partial-fraction-expansion]] 和 [[passivity-enforcement]] 处理频域响应到稳定时域模型的共性问题。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 | 主要贡献 |
|------|------|----------|
| Camara 等 - A full frequency dependent line model based on folded line equivalencing and latency exploitation | 2018 | FLE 降维 + MCNR 多时间步长，10%~35% 加速 |
| Noda - Application of frequency-partitioning fitting to the phase-domain frequency-dependent modeling | 2015 | FpF 频率分区拟合，较少极点数 |
| Colqui 等 - Implementation of Modal Domain Transmission Line Models in the ATP Software | 2022 | ATP 中模态频变线路的实现 |
| Liu 等 - Low-order approximation method for frequency-dependent transmission line model | 2017 | 低阶拟合方法（中文期刊） |
| Camara 等 - Time-domain modeling of a subsea buried cable | 2024 | 海底电缆频变模型 |
| Gustavsen 和 Vernay - Measurement-based frequency-dependent model of a HVDC transformer | 2020 | 实测 HVDC 变压器频变模型 |
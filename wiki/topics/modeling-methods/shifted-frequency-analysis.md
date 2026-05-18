---
title: "Shifted Frequency Analysis"
type: topic
tags: [shifted-frequency-analysis, dynamic-phasor, SFA, multirate-simulation, frequency-shifted]
created: "2026-05-04"
updated: "2026-05-19"
---

# Shifted Frequency Analysis

## 定义与边界

移频分析（Shifted Frequency Analysis, SFA）是电力系统电磁暂态仿真中的一类混合多速率方法。其核心思想是将基频附近的带通信号通过 Hilbert 变换构造成解析信号，再乘以移频因子 $e^{-j\omega_0 t}$ 将频谱搬移到零频附近，使原本以 $50/60\,\text{Hz}$ 为中心的动态分量变为低频包络（复值时间相关相量），从而允许使用更大的时间步长进行数值积分，同时保留基频附近的暂态动态精度。

与传统的准稳态相量（Quasi-Steady-State Phasor）相比，SFA 的关键区别在于它仍以时域瞬时波形为出发点和终点，仅在内部计算流程中将变量转换为复包络形式；而传统相量法则将系统方程整体化为相量域代数方程，仅保留工频稳态分量。

**边界限定**：
- 适用于包含大量电力电子设备的电网中需要同时捕捉"基频附近慢动态"和"开关级快瞬态"的场景
- 不适用于以高频谐波、开关暂态或远离工频的宽频响应为主导的研究，此时应使用全 EMT 详细建模

## EMT 中的角色

在 EMT 仿真中，SFA 承担以下关键角色：

**1. 大规模电力电子系统的实时/超实时仿真加速**
新能源和 HVDC 系统中，电力电子换流器的开关动作需要极小步长（微秒级），而网络其他部分仅需捕捉基频附近动态。SFA 使得在换流器局部保持详细 EMT 步长的同时，将交流网络部分切换为 SFA 大步长模式，从而实现数百至数千节点系统的超实时仿真。

**2. 多速率混合仿真的接口框架**
SFA 与全 EMT 的混合仿真（Hybrid SFA-EMT）允许不同子区域使用差异巨大的步长：通过 MATE（Multi-Area Thévenin Equivalent）框架下的端口戴维南等值进行耦合，慢侧 SFA 区域使用大步长，快侧 EMT 区域使用小步长，二者通过插值/抗混叠滤波交换边界量。

**3. 频率相关负荷和网络等值的集成**
在 SFA-EMT 仿真器中，频率相关负荷（如 fdLoad 模型）可以将指数型频率-功率/无功特性综合为常数 R/L/C 支路，直接接入节点导纳矩阵，使当前步网络方程隐式包含频率响应，避免传统暂态稳定程序中事后由相角差估计频率的延迟问题。

## 核心机制

### Hilbert 变换与解析信号构造

给定实值带通信号 $x(t)$，其解析信号定义为：

$$x_a(t) = x(t) + j\mathcal{H}[x(t)]$$

其中 Hilbert 变换为：

$$\mathcal{H}[x(t)] = \frac{1}{\pi}\int_{-\infty}^{+\infty}\frac{x(\tau)}{t - \tau}\,d\tau$$

对于电力系统工频信号 $x(t) = A(t)\cos(\omega_s t + \theta)$，有：

$$\mathcal{H}[A(t)\cos(\omega_s t + \theta)] = A(t)\sin(\omega_s t + \theta)$$

因此：

$$x_a(t) = A(t)\cos(\omega_s t + \theta) + jA(t)\sin(\omega_s t + \theta) = A(t)e^{j\theta}e^{j\omega_s t}$$

### 频率移位

将解析信号乘以 $e^{-j\omega_s t}$（$\omega_s = 2\pi f_s$ 为工频角速度）：

$$x_{a-\text{shifted}}(t) = x_a(t) \cdot e^{-j\omega_s t} = A(t)e^{j\theta}$$

移位后，复包络 $A(t)e^{j\theta}$ 成为缓变复值信号，其实部 $A(t)\cos\theta$ 和虚部 $A(t)\sin\theta$ 均为低频（近直流）分量，允许使用远大于 $1/(2\omega_s)$ 的时间步长进行积分。

### 时间相关相量（Time-Dependent Phasor, TDP）

移位后的复包络即为时间相关相量：

$$U(t) = u_I(t) + ju_Q(t)$$

其中：

$$u(t) = u_I(t)\cos\omega_s t - u_Q(t)\sin\omega_s t$$

$TDP$ 直接保留了信号的幅值和相位随时间变化的包络信息，而不只是在固定频率上取相量。

### SFA 数值离散格式

在 Dommel EMT 框架下，SFA 变量的离散迭代形式为：

**电压源型组件**（等效为诺顿电流源）：

$$I_n(k+1) = \mathbf{f}\big(v(k), i(k), x(k), u(k), k\big)$$

**网络方程**（修正节点分析 MNA）：

$$Y \cdot X(k+1) = b\big(v(k), i(k), I_n(k), V_n(k), k\big)$$

其中 $Y$ 为节点导纳矩阵，$X(k+1)$ 为节点电压向量，$b$ 为由历史电流源和注入电流组成的右端向量。

## SFA-EMT 混合仿真接口

### MATE 多区戴维南等值框架

在 MATE（Multi-Area Thévenin Equivalent）框架下，SFA 子系统和 EMT 子系统各自在端口处形成戴维南等效：

- **端口电压源**：$\hat{u}_i = V_i^{Thev}$
- **等效阻抗**：$\hat{Z}_i = Z_i^{Thev}$
- **连接支路电流**：由 MATE 链接方程统一求解后回写各子系统

子系统在自己的时间网格上积分并更新等效源和等效阻抗，全局 MATE 层负责在各子系统之间交换端口电压和连接支路电流。

### 双并行 EMT 跟踪复部

由于 SFA 变量是复数 $U(t) = u_I(t) + ju_Q(t)$，传统的单实值 EMT 仿真器无法直接跟踪复包络的实部和虚部。SFA-EMT 接口采用**双并行 EMT 策略**：

1. **Real-Part EMT**：跟踪 SFA 复解实部对应的接口响应
2. **Imaginary-Part EMT**：跟踪 SFA 复解虚部对应的接口响应

两个 EMT 副本与 SFA 在接口处按 MATE 交换等效量，并通过多速率同步/插值在 EMT 小步长（$\Delta t_\text{EMT}$）和 SFA 大步长（$\Delta t_\text{SFA}$）之间传递数据。

### 快慢数据交换协议

**慢→快方向（SFA → EMT）**：SFA 在相邻慢步之间提供边界量，EMT 中间小步通过线性插值获得所需等效源或端口量。

**快→慢方向（EMT → SFA）**：EMT 高采样率输出先经抗混叠滤波，再抽取（downsampled）到 SFA 时间点，避免高于 SFA 奈奎斯特频率的分量混叠（aliasing）到低频。

关键优势：$\Delta t_\text{SFA}$ 和 $\Delta t_\text{EMT}$ **不需要互为整数倍**，突破了传统多速率方法的时间步整除限制。

## 频移有理逼近（CVF + SFA）

### 复矢量拟合（Complex Vector Fitting, CVF）

传统矢量拟合（VF）要求冲激响应为实值（频谱满足 Hermitian 共轭对称 $Y(-j\omega) = Y^*(j\omega)$），适合物理实信号模型。但 SFA 移频后，目标是复频域响应，正负频率对称性不再成立。

CVF 解除 VF 的共轭对称约束，允许复极点 $p_i$ 和复留数 $R_i$ 独立出现（不必成共轭对），从而拟合只含非负频率或经频移后的复频域响应：

$$Y(s) \approx \sum_{i=1}^{N}\frac{R_i}{s - p_i} + D$$

### CVF + SFA 频移仿真流程

1. **Hilbert 变换构造解析信号**：$u_a(t) = u(t) + j\mathcal{H}[u(t)]$
2. **频移**：乘以 $e^{-j2\pi\Delta f t}$，将目标高频成分搬移到基带附近
3. **CVF 状态空间模型**：$Y(s) = C(sI - A)^{-1}B + D$
4. **梯形积分离散**：得到频移后的复电流响应
5. **逆频移 + 取实部**：恢复物理电流 $i(t) = \text{Re}\{i_{shifted}(t) \cdot e^{j2\pi\Delta f t}\}$

**量化性能边界**（Kida et al. 2026）：CVF 相对 VF 的误差最多降低 8 个数量级；加入频移后，精度最多再改善 2 个数量级；在相同目标精度下，时间步长可放大 2.33 到 5.5 倍。

## fdLoad 频率相关负荷模型

fdLoad 将指数型频率相关负荷综合为常数 R/L/C 支路网络，直接接入节点导纳矩阵：

$$P(f, V) = P_0\left(\frac{f}{f_0}\right)^{\alpha_f}\left(\frac{V}{V_0}\right)^{\alpha_v}$$

$$Q(f, V) = Q_0\left(\frac{f}{f_0}\right)^{\beta_f}\left(\frac{V}{V_0}\right)^{\beta_v}$$

$$Y(f) = \frac{P(f) - jQ(f)}{V^2}$$

通过 Vector Fitting 将 $Y(s)$ 拟合为有理函数后，映射为并联电阻、一阶极点对应 R-L 串联支路和常数电容支路。IEEE 39 节点 Bus 15 负荷（$P_0 = 306\,\text{MW}$，$Q_0 = 152\,\text{MVar}$）的综合拟合误差约 0.5%（$\alpha_f = 2.8$，$\beta_f = 1.8$）。

**优势**：当前步频率被隐式纳入网络方程求解，不存在事后相角差估计频率的延迟问题，适合处理切负荷不连续点等频率估计困难场景。

## 关键技术挑战

**1. 接口延迟与误差**
传统松耦合 SFA-EMT 接口在快慢步长交换处存在一个时间步延迟（$\Delta t_\text{EMT}$），可能引起数值不稳定和误差累积。SFA-EMT 协议通过双并行 EMT 和 MATE 链接消除了这一延迟，但增加了计算开销。

**2. 复数 TDP 与实数 EMT 的结构匹配**
SFA 的复值包络需要特殊接口处理——不能简单将复数的实部传给单个 EMT 求解器，否则会破坏解析信号结构。采用双并行实部/虚部 EMT 是当前最完整的解决方案。

**3. 步长设计（$\Delta t_\text{SFA}$ vs $\Delta t_\text{EMT}$）**
SFA 步长上限由基带包络带宽决定（需满足奈奎斯特准则），而 EMT 步长由开关动作和最高关注频率决定。二者不成整数倍时的插值/抗混叠策略增加了接口复杂度。

**4. 高频谐波和宽频暂态的保真度**
当系统响应包含远离基频的谐波或高频开关暂态时，SFA 的低频包络模型会丢失这些信息。因此 SFA 不适用于谐波分析、高频振荡研究或开关瞬态精确重现。

**5. fdLoad 的无源性约束**
频率相关负荷综合为 R/L/C 支路后，需要满足无源性约束以保证数值稳定性。CVF 框架下因不满足 Hermitian 对称性，需使用 Hamiltonian 矩阵方法进行全尺寸无源性检验，而非 VF 可用的半尺寸奇异性检验。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| IEEE 39节点系统 | faster-than-real-time（含数百至数千节点） | Zhang 2024（GPU + LB-LMC + SFA）|
| 误差（相对 VF） | CVF 误差降低最高 8 个数量级 | Kida et al. 2026 |
| 频移+CVF 精度改善 | 最高再改善 2 个数量级 | Kida et al. 2026 |
| 步长放大倍数（频移后） | 2.33–5.5 倍（相同目标精度下）| Kida et al. 2026 |
| fdLoad 拟合误差 | ~0.5%（IEEE 39 Bus 15）| Hajiakbari Fini et al. 2026 |
| SFA-EMT 接口 | 无时间步延迟、无迭代、不依赖传输线解耦 | Tarazona et al. 2026 |
| IEEE 39节点验证 | 全 EMT 可比精度 + 机电暂态捕捉 | Martí et al.（多篇）|

## 适用边界与选择指南

| 场景 | 推荐方法 |
|------|----------|
| 大规模 HVDC/新能源系统全系统仿真（关注基频附近动态）| SFA-EMT 混合仿真 |
| 需要实时/超实时能力 | SFA + GPU 加速（LB-LMC 粗粒度并行）|
| 局部详细电磁暂态 + 系统级机电动态 | SFA-EMT 多速率混合（MATE 接口）|
| 外部网络频率相关等值拟合 | CVF（解除共轭对称约束）|
| 频率相关负荷动态（低惯量电网 UFLS 分析）| fdLoad + SFA-EMT |
| 谐波分析、高频振荡、开关暂态精确重现 | 全 EMT（不用 SFA）|
| 常规暂态稳定分析（无电力电子详细模型）| 纯相量法或 TS-EMT |

## 相关方法与模型

- [[dynamic-phasor]] — 动态相量法的通用框架，SFA 是其在 EMT 加速中的具体实现形式
- [[multirate-method]] — 多速率仿真方法，SFA-EMT 是其主流实例
- [[real-time-simulation]] — 实时仿真目标，SFA 的 faster-than-real-time 能力直接服务于此
- [[average-value-model]] — 电力电子换流器的平均值建模，可与 SFA 联合使用实现混合精度仿真
- [[vector-fitting]] — 矢量拟合是 CVF/SFA 频域导纳等值的核心工具
- [[gpu-accelerated-simulation]] — GPU 并行加速是 SFA 实现超实时仿真的硬件基础
- [[hybrid-modeling]] — SFA-EMT 混合仿真是混合建模在仿真加速领域的典型应用

## 来源论文

- Zhang et al. 2024 — GPU加速SFA（LB-LMC + 数据/任务并行 + 图式线程安全）
- Tarazona et al. 2026 — SFA-EMT混合仿真接口协议（MATE + 双并行EMT）
- Kida et al. 2026 — 频移有理逼近（CVF + VF对比，2.33–5.5倍步长放大）
- Hajiakbari Fini et al. 2026 — fdLoad频率相关负荷模型（SFA-EMT集成）
- Shu et al. 2019 — 多域协同仿真（SFP模型 + HMD-TLM接口）
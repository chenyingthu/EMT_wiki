---
title: "感应电机 (Induction Machine)"
type: model
tags: [induction-machine, asynchronous-machine, motor, load, dq0, slip, squirrel-cage, wound-rotor]
created: "2026-04-29"
updated: "2026-05-19"
---

# 感应电机 (Induction Machine)

## 定义与物理概述

感应电机（又称异步电机，Induction Machine, IM）是电力系统中应用最广的旋转电机类型，通过定子三相绕组产生的旋转磁场与转子感应电流相互作用产生电磁转矩，将电能转化为机械能。其转子转速 $n_r$ 始终低于同步转速 $n_s$（转差运行），转差率定义为 $s = (n_s - n_r)/n_s$。

按转子结构分类：

| 类型 | 结构特点 | 适用场景 |
|------|----------|----------|
| **鼠笼式** | 铸铝/铜条转子，结构简单坚固 | 通用电动机、风机、泵 |
| **绕线式** | 三相绕组转子，可外接电阻调速 | 起重机、卷扬机、大型风机 |

感应电机占工业总负荷的 **60%–80%**，是电力系统电压稳定、暂态稳定和机电耦合分析的关键元件。在 EMT 仿真中，感应电机面临三个核心挑战：① 随转子位置变化的相域电感导致网络导纳矩阵时变；② dq 坐标与相域网络的接口需要坐标变换和预测/校正；③ 电磁暂态（微秒级）和机电暂态（毫秒至秒级）存在多尺度耦合。

## EMT 中的角色与建模挑战

感应电机在 EMT 仿真中承担双重角色：

1. **负荷元件**：工业配网中大量感应电机作为静态/动态负荷，其启动暂态和电压响应影响系统电压稳定性
2. **驱动系统核心**：风电场双馈发电机（DFIG）、抽水蓄能电站等以感应电机为核心部件

**核心建模挑战**：

- **转子位置相关电感**：相域下定子与转子绕组间的互感是转子角 $\theta_r$ 的函数，直接接入网络会导致导纳矩阵时变，迫使每步重新因子化
- **坐标接口不匹配**：电网用 abc 相坐标，电机内部用 dq 旋转坐标，接口处理引入数值延迟和预测误差
- **多尺度耦合**：电磁暂态（开关、故障）与机电暂态（转速、功角）在同一模型中耦合
- **磁饱和非线性**：主磁化通道饱和影响稳态电流、故障电流和电磁转矩
- **计算效率矛盾**：精确的相域耦合电路（PD）模型计算代价高；简化的 dq 模型需坐标变换且引入接口误差

## EMT 建模方法

### 方法 1：相域耦合电路模型（PD 模型）

**原理**：在 abc 相坐标下直接建立定、转子绕组电压方程和磁链方程，计及随转子位置变化的绕组互感。

定子电压方程（abc 相域）：

$$v_{abc,s} = R_s i_{abc,s} + \frac{d\psi_{abc,s}}{dt}$$

转子电压方程（转子侧短路，$v_{abc,r} = 0$）：

$$0 = R_r i_{abc,r} + \frac{d\psi_{abc,r}}{dt}$$

磁链方程：

$$\psi_{abc,s} = L_{ss}(\theta_r) i_{abc,s} + L_{sr}(\theta_r) i_{abc,r}$$
$$\psi_{abc,r} = L_{rs}(\theta_r) i_{abc,s} + L_{rr}(\theta_r) i_{abc,r}$$

**特点**：物理直观，直接接入相域网络，无需坐标变换。但 $L_{sr}(\theta_r)$ 随转子转动呈正弦变化，导致网络导纳矩阵每步更新，计算量巨大。

### 方法 2：dq 坐标变换模型（dq 模型）

**原理**：通过 Park 变换将 abc 坐标下的物理量转换到与转子同步旋转的 dq 坐标系，消去转子位置相关电感。

同步旋转坐标系下的电压方程：

$$v_{dq0,s} = R_s i_{dq0,s} + \frac{d\psi_{dq0,s}}{dt} + \omega_s \begin{bmatrix} -\psi_q \\ \psi_d \\ 0 \end{bmatrix}$$

转子坐标系（转差频率 $\omega_s - \omega_r$）下的转子方程：

$$v_{dq0,r} = R_r i_{dq0,r} + \frac{d\psi_{dq0,r}}{dt} + (\omega_s - \omega_r) \begin{bmatrix} -\psi_{qr} \\ \psi_{dr} \\ 0 \end{bmatrix} = 0$$

电磁转矩（dq 形式）：

$$T_e = \frac{3}{2} p (\psi_d i_q - \psi_q i_d)$$

机械运动方程：

$$J \frac{d\omega_r}{dt} = T_e - T_L - D\omega_r$$

**特点**：dq 坐标系下电感参数为常数，状态变量少。但需要从 abc 相坐标预测电压注入 dq 模块，再将电流解算回网络（间接接口），引入预测误差，且网络侧电导矩阵可能时变。

### 方法 3：电压后电抗模型（VBR 模型）

**原理**：将电机端口等效为"电抗/等效电导 + 内部电压源"结构，使外部网络看到类似 Norton 或 Thevenin 支路的端口特性。转子动态保留在 dq 坐标，定子端口映射到 abc 相域。

外部 abc 端口方程可整理为：

$$i_{abc,s} = G_{eq} v_{abc,s} + i_{hist}$$

其中 $G_{eq}$ 为诺顿等效电导，$i_{hist}$ 为历史电流源。VBR 的离散形式使电导矩阵不随转子位置变化（因为电导由 dq 侧结构决定，映射到 abc 端口后结构固定），避免了每步重新因子分解全网 G 矩阵。

**特点**：兼顾相域直接接口和较低计算复杂度；等效电导子矩阵在理论上可保持常数，减少网络矩阵重组。

### 方法 4：近似电压后电抗模型（AVBR 模型，Wang & Jatskevich 2010）

**原理**：在 VBR 离散接口方程中，识别含转子速度 $\omega_r$ 的系数项，将这些速度相关项近似忽略（$O(\Delta t^2)$ 量级的小量），使机器端口等效电导矩阵完全常数化。

关键机制：

$$\text{忽略项} \propto (\omega_s - \omega_r) \cdot \text{相关系数} \approx 0$$

常数电导子矩阵使 EMTP 网络导纳矩阵 **只需在初始化时完成一次稀疏 LU 分解**，每步只更新历史源，彻底消除每步重分解负担。

**精度边界**（Wang & Jatskevich 2010）：

| 指标 | AVBR 性能 |
|------|-----------|
| 单步计算耗时 | 1.9 μs（PD 模型 4.3 μs，提速 126%） |
| 近似误差上界（最严苛工况，3 HP，Δt=500 μs） | 仅 1.2% |
| 非对角/对角系数比 $|k_j/d_j|$ 衰减（Δt=500 μs） | $10^{-3}$ 量级（$O(\Delta t^2)$） |
| 验证电机容量范围 | 3 HP – 2250 HP 鼠笼式感应电机 |

### 方法 5：节点缩减模型（NR-CF / NR-CC，Vilchis-Rodriguez & Acha 2012）

**原理**：通过节点缩减消去电机内部变量（转子侧和内部支路变量），只保留定子 abc 相端口电流作为网络接口量，使机器对网络表现为 3×3 维对角阵（而非 6×6 满阵），矩阵求逆从 $O(n^3)=216$ 次乘法降至 $O(n)=3$ 次。

两种变体：

- **NR-CF**（current-flux）：定子电流 + 转子磁链作为状态，继承 VBR 的数值稳定性动机
- **NR-CC**（current-current）：仅以电流为统一输出变量，模型表示最简化

**精度边界**（Vilchis-Rodriguez & Acha 2012）：

| 指标 | NR-CC / NR-CF 性能 |
|------|-------------------|
| 导纳矩阵维度缩减 | 6×6 满阵 → 3×3 对角阵（效率提升约 98%） |
| 步长稳定性上限 | 1–5 ms（传统 PD 模型步长超过 0.5 ms 即失稳） |
| 定子电流瞬态误差 | < 0.5%（相比详细 PD 模型） |
| 稳态误差 | < 0.1% |
| 内存访问减少 | ~70%（恒定导纳矩阵只存储一次） |

### 方法 6：多尺度相域模型（解析信号 / 动态相量，Multi-scale IM）

**原理**：将电压、电流、磁链表示为解析信号（同相实部 + 正交虚部），引入可调 shift frequency $f_{ref}$：$f_{ref}=0$ 时退化为瞬时波形 EMT 模型，$f_{ref}=f_{sync}$ 时变为动态相量包络模型。同时推导对任意转子位置且不随磁化电感饱和变化的 abc 相域诺顿内导纳。

**特点**：同一组状态和接口可覆盖 EMT 瞬时波形和机电暂态包络两种工作方式；恒定诺顿内导纳减少网络导纳变化。适合同时关心故障暂态和机电振荡的多尺度仿真场景。

## 磁饱和处理

感应电机的磁饱和主要影响主磁化通道，改变 dq 轴等效电感值，进而影响转矩、电流和故障电流水平。饱和 VBR 模型（Wang & Jatskevich 2010）将非线性磁化曲线分段线性化，改写为适合 EMTP 伴随电路的形式：

$$\psi_m = f(i_\mu) \Rightarrow i_\mu = g(\psi_m) \quad \text{（分段线性近似）}$$

**交叉饱和效应**：dq 轴磁链与电流之间存在静态和动态交叉饱和，饱和的 d 轴磁链会影响 q 轴动态（在 dq 耦合项中体现）。含饱和 VBR 模型通过主磁化通道的静态饱和曲线处理这一耦合，保持 VBR 直接接口结构不变。

**适用边界**：饱和处理主要针对主磁化通道；漏磁通饱和的扩展处理在原文中指出原则上可行但未详细验证。

## EMT 启动暂态仿真

感应电机直接启动时经历强烈的电磁暂态过程：

**启动特性**：

- 启动电流：5–7 倍额定电流（持续数个工频周期）
- 启动转矩：1.5–2.5 倍额定转矩
- 启动时间：取决于惯量 $J$ 和负载转矩 $T_L$

**启动过程方程**（dq 形式）：

$$J\frac{d\omega_r}{dt} = \frac{3}{2}p(\psi_d i_q - \psi_q i_d) - T_L - D\omega_r$$

启动瞬态分析需用小步长（Δt ≤ 1 μs）捕捉电流和转矩的快速变化；稳态运行后步长可放大。

**启动方式对比**：

| 启动方式 | 特点 | EMT 建模要点 |
|----------|------|-------------|
| 直接启动 | 启动电流大，转矩高 | 需捕捉 5–7× 额定电流的暂态冲击 |
| 星-三角启动 | 启动电流降至 1/√3 | 开关模型 + 拓扑变更事件 |
| 软启动器 | 电压渐进上升 | 触发型时间序列 + 控制方程 |
| 变频器启动 | 频率/电压协同调节 | 电力电子变流器接口（[[dfig-model]]） |

## 感应电机负荷模型

感应电机负荷是系统电压稳定分析中的主要负荷类型，其电压特性建模为：

$$P = P_0\left(\frac{V}{V_0}\right)^\alpha, \quad Q = Q_0\left(\frac{V}{V_0}\right)^\beta$$

典型指数范围：$\alpha = 0.1 \sim 1.2$，$\beta = 1.5 \sim 3.0$。

**负荷转矩类型**：

- **恒转矩负载**：$T_L = const$（压缩机、输送带）
- **平方转矩负载**：$T_L \propto \omega_r^2$（风机、泵类）
- **恒功率负载**：$P = const$（加工设备）

**电压暂降估算**：

$$\Delta V \approx (X_s + X_{line}) \times I_{start}$$

典型值为额定电压的 5%–15%（大电机启动时）。

## 量化性能边界汇总

| 建模方法 | 计算耗时 | 步长稳定性 | 精度（相对 PD 模型） | 等效导纳矩阵 |
|----------|----------|-----------|---------------------|--------------|
| PD（相域耦合） | 基准（4.3 μs/步） | Δt ≤ 0.5 ms | 基准 | 时变 6×6 满阵 |
| dq 间接接口 | 较低 | 中等 | 预测误差 | 可能时变 |
| VBR | 2.2 μs/步 | 较好 | 高 | 常数 3×3 |
| **AVBR** | **1.9 μs/步** | **良好** | **误差上界 1.2%** | **常数对角** |
| **NR-CC / NR-CF** | **极低** | **Δt ≤ 1–5 ms** | **< 0.5% 瞬态 / < 0.1% 稳态** | **3×3 对角** |
| 多尺度（解析信号） | 取决于 $f_{ref}$ | 灵活 | 高 | 常数诺顿等效 |

> 表中量化数据来源：Wang & Jatskevich 2010（AVBR）、Vilchis-Rodriguez & Acha 2012（NR-CC/NR-CF）、Modelica ASM 2024（对比基准）

## 关键技术挑战

### 挑战 1：网络导纳矩阵时变问题

直接相域模型的转子位置相关电感导致网络导纳矩阵每步更新，矩阵重组/重分解计算代价高。AVBR 和节点缩减模型通过忽略速度相关项或节点缩减，将时变问题转化为常数矩阵问题。

### 挑战 2：dq 坐标与相域网络的接口延迟

dq 模型需要从 abc 相域预测电压注入 dq 模块（间接接口），预测误差随步长增大而增加。VBR/AVBR 通过在 dq 侧离散后将端口映射到 abc 相域，实现直接接口，减少预测误差。

### 挑战 3：磁饱和非线性处理

主磁化通道饱和使 dq 轴电感成为电流的非线性函数，交叉饱和进一步增加耦合复杂度。饱和 VBR 模型通过分段线性化在保持直接接口的同时纳入饱和效应。

### 挑战 4：多尺度耦合仿真

感应电机系统中同时存在微秒级电磁暂态和秒级机电过程。解析信号/多尺度模型（Multi-scale IM）通过 shift frequency 参数在同一框架下覆盖两个时间尺度，但包络带宽限制了其对高频谐波和快速开关场景的适用性。

### 挑战 5：大规模电机群等值

大量感应电机聚合建模时，单台精确模型计算代价高。NR 节点缩减模型为电机群等值提供了理论基础（内部动态封装入历史源，对外只需 3 个端口变量），但参数辨识精度和泛化能力仍需进一步验证。

## 适用边界与选择指南

| 应用场景 | 推荐建模方法 | 步长 | 精度需求 |
|----------|-------------|------|---------|
| 电机启动暂态分析 | PD / VBR | Δt ≤ 1 μs | 高精度 |
| 配网电压稳定性研究 | AVBR / NR-CC | Δt ≤ 10 μs | 中等精度 |
| 故障电流计算 | 含饱和 VBR / dq | Δt ≤ 1 μs | 高精度 |
| 长时域机电暂态 | NR-CC / dq | Δt ≤ 0.1 ms | 中等精度 |
| 多尺度 EMT-TS 协同仿真 | 多尺度解析信号 | 灵活 | 取决于场景 |
| 实时硬件在环仿真 | NR-CC / AVBR | Δt ≤ 1 μs | 中等精度 |
| FPGA 加速实时仿真 | 44 ns 并行实现（Matar 2011） | 纳秒级 | 满足实时性 |

## 相关方法

- [[state-space-method]] — 感应电机状态空间建模
- [[coordinate-transformation-model]] — Park dq0 坐标变换
- [[average-value-model]] — 机电暂态简化平均值模型
- [[numerical-integration]] — 启动暂态仿真数值积分
- [[parameter-identification]] — 电机参数辨识方法
- [[numerical-damping-optimization]] — 数值阻尼与稳定性

## 相关模型

- [[synchronous-machine-model]] — 同步电机模型（对比参考）
- [[dfig-model]] — 双馈感应发电机（DFIG，风电场核心）
- [[load-model]] — 感应电机负荷建模
- [[transformer-model]] — 机端变压器
- [[full-bridge-smb]] — 子模块建模（变流器接口参考）

## 相关主题

- [[wind-farm-modeling]] — 风电场建模（DFIG 为核心元件）
- [[real-time-simulation]] — 电机实时仿真
- [[harmonic-analysis]] — 电机谐波分析
- [[network-equivalent]] — 负荷等值
- [[electromechanical-electromagnetic-hybrid]] — 机电混合仿真

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Wang & Jatskevich — Approximate Voltage-Behind-Reactance Induction Machine Model | 2010 | 提出 AVBR 模型，忽略速度相关项实现常数电导矩阵，1.9 μs/步，1.2% 误差上界 |
| Wang & Jatskevich — Including Magnetic Saturation in Voltage-Behind-Reactance Induction Machine Model | 2010 | 将主磁化通道饱和纳入 VBR 模型，分段线性化处理交叉饱和 |
| Vilchis-Rodriguez & Acha — Nodal Reduced Induction Machine Modeling for EMTP | 2012 | 提出 NR-CF / NR-CC 节点缩减模型，3×3 对角阵，步长 1–5 ms，效率提升 98% |
| Wang et al. — Methods of Interfacing Rotating Machine Models in EMTP | 2010 | IEEE Task Force 综述，系统分类间接/直接接口技术 |
| Wang — Modeling of AC Machines using a Voltage-Behind-Reactance Formulation | 2010 | 提出 VBR 通用框架，建立同步机/感应机 EMT 离散实现 |
| Multi-scale IM in Phase Domain with Constant Inner Impedance | 2019 | 解析信号多尺度模型，shift frequency 覆盖瞬时波形与动态相量 |
| Masoom & Mahseredjian — Electromagnetic Transient Modeling of Asynchronous Machine in Modelica | 2024 | Modelica 声明式实现，DASSL 变步长，0.64%/0.77% 误差，顺序启动 112.6 s vs 198.4 s |
| Matar & Iravani — Massively Parallel Implementation of AC Machine Modeling for Real-Time Simulation | 2011 | FPGA 并行实现，44 ns/步，支持纳秒级实时仿真 |
| Mu et al. — Fast EMT Simulation Model of DFIG Based Wind Turbine | 2019 | DFIG 定转子解耦虚拟电容法，超实时仿真 |
| Li et al. — Structure Preserving Aggregation Method for DFIGs | 2022 | DFIG 聚合保持结构方法 |

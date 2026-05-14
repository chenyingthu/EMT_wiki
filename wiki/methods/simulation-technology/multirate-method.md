---
title: "多速率方法 (Multi-Rate Method)"
type: method
tags: [multirate, time-step, partitioning, interface, lifting, mate, root-matching]
created: "2026-04-13"
updated: "2026-05-10"
---

# 多速率方法 (Multi-Rate Method)

## 1. 物理背景与工程需求

多速率方法在同一仿真任务中为不同子系统、变量或模型层级使用不同时间步长。它的存在前提是系统存在可利用的时间尺度差异——局部电力电子开关或快速暂态只需要小步长，而远端交流网络或移频包络可用较大步长描述。它不是模型降阶或平均值模型：多速率方法必须显式说明分区策略、接口变量定义、采样/插值规则和稳定性边界（Sinkar 2025）。

多速率方法在 EMT 中的工程需求包括：

1. **单速率瓶颈**：单速率 EMT 由最快暂态决定全网步长；MMC 换流器需要 2--50 μs，交流系统可承受毫秒级步长，统一小步长造成计算浪费（Shu 2017）
2. **交直流混合系统仿真**：MMC-MTDC 系统与大型交流电网联合 EMT 仿真时，按动态特性划分步长避免大规模网络被迫微秒级求解（Mu 2014）
3. **SFA-EMT 混合仿真**：移频分析子系统用毫秒级包络步长，EMT 子系统保留局部微秒级瞬时值，通过 MATE 框架耦合（Tarazona 2021）
4. **实时仿真的资源约束**：FPGA 或局部处理器承担小步长任务，CPU 核心处理大步长区域，硬件 deadline 和通信延迟成为方法边界

## 2. 数学描述

### 2.1 多速率基本定义

设快子系统步长 $h_f$，慢子系统步长 $h_s = N h_f$（整数步长比），一个慢步长内快子系统推进 $N$ 次：

$$
\dot{x}_f = f(x_f, x_s, u_f, t), \quad \dot{x}_s = g(x_s, x_f, u_s, t)
$$

慢到快方向需要插值（保持、线性或高阶）：

$$
x_s(t_m + r h_f) \approx \mathcal{I}(x_s(t_m), x_s(t_{m+1}), r/N)
$$

快到慢方向需要采样、平均或滤波。Mu (2014) 使用线性内插：

$$
\hat{X}_s(mk + i) = X_s(mk) + \frac{X_s(mk + m) - X_s(mk)}{m} i
$$

### 2.2 全隐式多速率耦合关系

Mu (2014) 用后退欧拉离散揭示快慢子系统的内在耦合：

$$
\begin{cases}
X_s(mk) - X_s(mk - m) = mh(AX_s(mk) + BX_f(mk)) \\
X_f(mk) - X_f(mk - 1) = h(CX_s(mk) + DX_f(mk)) \\
\vdots \\
X_f(mk - m + 1) - X_f(mk - m) = h(CX_s(mk - m + 1) + DX_f(mk - m + 1))
\end{cases}
$$

$X_s(mk)$ 依赖 $X_f(mk)$，而 $X_f(mk)$ 依赖 $X_s(mk)$——同刻耦合导致不能直接递推求解。所有非迭代多速率方法都必须通过某种接口近似打破这个耦合环。

### 2.3 传输线延迟解耦

Mu (2014) 利用传输线波传播延迟将接口耦合转化为历史边界条件：

$$
U_{s-}(n+1) = U_{f-o}(n) = C_f X_f(n), \quad U_{f-}(n+1) = U_{s-o}(n) = C_s X_s(n)
$$

当前时刻的端口源由对端上一延迟时刻的输出决定，快慢子网在一个大步长内可以独立推进。

### 2.4 SFA-EMT 解析信号接口

Tarazona (2021) 将带通信号分解为同相和正交分量：

$$
u(t) = u_I(t)\cos\omega_0 t - u_Q(t)\sin\omega_0 t, \quad U(t) = u_I(t) + j u_Q(t)
$$

解析信号 $z(t) = u(t) + j\mathcal{H}[u(t)] = U(t)e^{j\omega_0 t}$，SFA 变换 $z_m(t) = e^{-j\omega_0 t}z(t)$ 将频谱左移 $\omega_0$ 至基带。

### 2.5 增广网络方程（ANE）

Shu (2017) 用增广网络方程同步求解子系统内部变量与接口变量：

$$
\begin{bmatrix} \tilde{G}_f & I \\ -I & Z_f \end{bmatrix}
\begin{bmatrix} \tilde{v}_f(t_k+ih) \\ i_f(t_k+ih) \end{bmatrix} =
\begin{bmatrix} \tilde{i}_{h,f}(t_k+ih) \\ v_{h,f}(t_k+ih) \end{bmatrix}
$$

## 3. 计算模型与离散化

### 3.1 Lifting 稳定性分析方法

Sinkar (2025) 将多速率 EMT 离散系统识别为周期时变系统，并提出 lifting 特征值判据。在一个大步长 $\Delta T = N\Delta t$ 内，状态转移矩阵随步数变化：

$$
x(t + (k+1)\Delta t) = G_k x(t + k\Delta t), \quad k = 0, 1, \ldots, N-1
$$

应用 lifting 将 $N$ 步状态堆叠为时不变表示：

$$
X^L(t) = [x(t), x(t+\Delta t), \ldots, x(t+(N-1)\Delta t)]^T
$$

$$
M^L X^L(t + \Delta T) = H^L X^L(t)
$$

若矩阵对 $(H^L, M^L)$ 的广义特征值全部位于单位圆内，则多速率仿真数值稳定。**关键约束**：A 稳定梯形法在单子系统中稳定，不保证多速率整体稳定——周期性耦合本身可产生数值发散。

### 3.2 接口模型的根匹配离散化

Shu (2017) 对接口微分方程采用根匹配算法而非梯形法，以抑制数值振荡：

$$
v_f(t_k + ih) = \alpha^{-1} \{ i_f(t_k + ih) + \beta i_f[t_k + (i-1)h] \} + u_f(t_k + ih)
$$

$$
\alpha = 1 - e^{-R_f h / L_f}, \quad \beta = e^{-R_f h / L_f}
$$

根匹配将连续系统极点精确映射到离散域，在接口处完全消除梯形法在突变下产生的非物理振荡。

### 3.3 接口预测-校正机制

Shu (2017) 用滑动窗口三次样条预测慢步长内的戴维南等效电压：

$$
F_i(t) = \frac{[t_k+(i-1)h-t]^3 M_{i-2} + [t-t_{k-1}-(i-2)h]^3 M_{i-1}}{6h} + \cdots
$$

大步长结束时通过接口阻抗矩阵逐步校正：

$$
u_f^l(t_{k+1}) = \tilde{u}_f^l(t_{k+1}) + \sum_{m=1, m\neq l}^N Z_{lm} i_f^m(t_{k+1})
$$

快到慢方向的诺顿电流用算术平均更新：

$$
i_s(n_{k+1}) = \frac{1}{n} \sum_{m=0}^{n-1} i_f(t_k + mh)
$$

### 3.4 SFA-EMT 多速率接口（Tarazona 2021）

SFA-EMT 混合仿真在 MATE 框架下运行：

1. 每个子系统形成多端口 Thévenin 等效
2. 全局求解连接支路电流 $I_L = Z_T^{-1} E_L$
3. 各子系统求解节点电压 $V_j = e_j - Y_j^{-1} C_j I_L$
4. 并行运行实部 EMT 和虚部 EMT 仿真器保持复解解析性
5. 多速率同步在 SFA 大步长和 EMT 小步长之间插值传递

## 4. 实现方法与算法细节

### 4.1 多速率变体对比

| 类型 | 接口机制 | 稳定性方法 | 典型步长比 | 来源 |
|------|----------|------------|-----------|------|
| 整数步长比非迭代 | 插值/保持/平均 | Lifting 特征值判据 | $N = 2\!-\!20$ | Sinkar 2025 |
| 传输线分网并行 | 延迟波变量解耦 | 矩阵范数保守判据 | $m = 2\!-\!10$ | Mu 2014 |
| SFA-EMT 复包络 | MATE 双 EMT 副本 | 梯形法 + 解析信号 | $h_s$ 毫秒/$h_f$ 微秒 | Tarazona 2021 |
| AC-MTDC 预测校正 | 时变 Thevenin/Norton + ANE | 根匹配 + 样条预测 | 10--20 | Shu 2017 |

### 4.2 接口策略对比

| 接口方向 | 可选方法 | 误差特点 | 稳定性 |
|---------|----------|---------|--------|
| 慢→快（上采样） | 零阶保持、线性插值、三次样条 | 样条误差 $\mathcal{O}(h^4)$ | 高阶插值减小相位滞后 |
| 快→慢（下采样） | 末值采样、算术平均、滤波 | 平均消除混叠 | 末值采样可能注入开关纹波 |
| 校正方式 | 无校正、逐步校正、迭代 | 校正减小延迟误差 | 迭代更好但实时性受限 |

### 4.3 稳定性保守判据（Mu 2014）

$$
\|P_f^{-1} C P_s\|_\infty \le \|-J_D [I - (I-hJ_D)^{-m}]\|_\infty
$$

$$
\|P_s^{-1} B P_f\|_\infty \le \|(-J_A)^{-1}\|_\infty
$$

该判据基于无穷范数，提供的是充分条件而非必要条件：满足时保证绝对渐近稳定，不满足时不必然发散。

### 4.4 分区边界选择准则

- 分区应避开强非线性、频繁开关或强耦合边界
- 传输线自然延迟可作接口（Mu 2014），但需要延迟长度匹配大步长
- 步长比不是越大越好——稳定性取决于接口规则、系统频带和分区阻抗
- A 稳定积分器在单子系统中稳定，不保证周期性多速率整体稳定

## 5. 适用边界与失效模式

### 适用条件

- 系统存在可分离的时间尺度差异（Sinkar 2025）
- 接口可用传输线延迟自然解耦（Mu 2014）
- 慢区域以基频附近机电动态为主，快区域含详细 EMT（Tarazona 2021）
- 大型交流电网与 MMC-MTDC 联合仿真，按动态分配步长（Shu 2017）

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| 强耦合边界分区 | 接口变量变化快，插值/保持误差大 | 主导接口误差，可能数值失稳 |
| 步长比过大 | 慢子系统在快子步内变化不可忽略 | 插值误差累积，混叠注入 |
| 快到慢反馈未滤波 | 高频开关分量经下采样注入慢系统 | 混叠和虚拟能量注入 |
| A 稳定错觉 | 单子系统 A 稳定 ≠ 多速率整体稳定（Sinkar 2025） | 周期性耦合产生数值发散 |
| 跨区故障/闭锁 | 分区边界经历突变，接口假设失效 | 需临时同步或切回单速率 |
| 非整数步长比 | 打破周期性结构，lifting 无法直接应用 | 稳定性分析困难 |

### 关键约束

- Sinkar (2025) 的方法在 LTI 系统中推导，对强非线性和开关拓扑变化不保证适用
- Mu (2014) 的稳定判据是保守的，不满足条件不意味着失稳，但满足时保证稳定
- Shu (2017) 的预测-校正在大型交直流系统中验证（含数十个换流站和数百条线路），不保证在任意 MTDC 拓扑中同样有效
- Tarazona (2021) 在 IEEE 39 节点系统验证，原文未报告具体加速倍数或误差百分比

## 6. 应用案例

### 案例 1：传输线分网并行多速率（Mu 2014）

场景：快慢双子网通过传输线连接，接口阻抗 $R_C$ 初始 0.9084 Ω（不稳定），调整至 1.9062 Ω 后满足稳定判据。状态转移矩阵谱半径从 >1 降至 <1。0.2 s 阶跃扰动下时域响应与单速率全隐式基准高度一致。传输线延迟将强耦合的 $X_s(mk)$ 和 $X_f(mk)$ 解耦为历史边界条件。

### 案例 2：大型 AC 与 MMC-MTDC 多速率协同（Shu 2017）

场景：含数十个换流站与数百条交流线路的实际系统。AC 系统用大步长（慢），MMC-MTDC 用小步长（快），速率比 10--20。滑动窗口三次样条预测偏差 < 0.2%，诺顿电流平均混叠误差 < 0.5%，根匹配彻底消除接口数值振荡。计算效率提升约 3 倍，内存降低约 40%，关键变量最大相对误差 < 0.5%。

### 案例 3：SFA-EMT 多速率混合仿真（Tarazona 2021）

场景：IEEE 39 节点系统中部分区域用 SFA（大步长复包络），局部用 EMT（小步长）。双 EMT 副本（实部 EMT + 虚部 EMT）保持 SFA 复值解的解析性。MATE 框架下通过多端口 Thévenin 等效交换接口量。SFA 区域步长可达毫秒级。

## 7. 延伸阅读

- [[interpolation-method]]：慢到快方向和事件同步的关键接口技术
- [[numerical-integration]]：决定每个子系统内部的离散推进
- [[stiff-system-handling]]：多时间尺度带来的刚性需求和局部小步长
- [[fixed-admittance]]：减少快区频繁开关造成的矩阵重构
- [[dynamic-phasor]]：多速率慢区建模的常见候选
- [[average-value-model]]：多速率慢区建模的另一候选
- [[companion-circuit]]：快区开关动作时的历史项重置
- [[network-equivalent]] 和 [[fdne-model]]：分区接口的等效网络表达
- [[co-simulation]]：松耦合多工具协同仿真（与紧耦合多速率不同但相关）
- [[parallel-computing]]：多速率与并行策略的配合

*页面基于 Sinkar (2025)、Tarazona (2021)、Shu (2017) 和 Mu (2014) 的证据写作。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[magnetically-saturable-voltage-behind-reactance-model-for-induction-machines|Magnetically Saturable Voltage Behind Reactance Model for In]] | 2011 |
| [[multi-fpga-digital-hardware-design-iet-gtd|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution|A Hybrid Simulation Tool for the Study of PV Integration Imp]] | 2016 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro|Co-Simulation of electromagnetic transients and Phasor model]] | 2016 |
| [[基于rtds和fpga联合仿真平台的多速率实时仿真方法|基于RTDS和FPGA联合仿真平台的多速率实时仿真方法]] | 2016 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型|适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型]] | 2019 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo|An Inverter Model Simulating Accurate Harmonics with Low Com]] | 2020 |
| [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level Modular Multilevel Converter Model]] | 2020 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg|Interfacing real-time and offline power system simulation to]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Real-Time HIL Emulation of DRM With Machine Learning Acceler]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation|A Semi-Analytical Approach for State-Space Electromagnetic T]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |

---
title: "分布参数模型 (Distributed Parameter Model)"
type: method
tags: [distributed-parameter, transmission-line, wave-propagation, traveling-wave, telegrapher, bergeron, ulm, frequency-dependent]
created: "2026-05-02"
updated: "2026-05-14"
---

# 分布参数模型 (Distributed Parameter Model)

## 定义

分布参数模型是将电磁、热或电路参数视为空间坐标函数的建模方式。在 EMT 仿真中，它描述的是状态变量不仅随时间变化，也随空间位置变化的物理系统。其核心数学框架是 **电报员方程（Telegrapher's Equations）**——一组耦合的偏微分方程，刻画了沿传输线分布的电压和电流在空间与时间上的传播行为。

分布参数模型不是"高精度"的同义词，也不等同于 `[[distributed-parameter-line]]` 一页；本页负责说明通用思想、数学基础、建模方法体系及其在 EMT 仿真中的实现路径，线路页负责具体线路模型。

## EMT 中的角色

EMT 仿真选择分布参数模型，通常是因为以下现象不能由单个集中阻抗可靠表示：

- **传播延迟和行波反射**：电磁波沿线路以有限速度传播，产生时延效应和终端反射。
- **参数随频率变化**：导线的集肤效应、邻近效应和大地返回路径导致单位长度阻抗和导纳随频率显著变化。
- **多导体耦合**：护套/地线/回流路径对端口响应的影响，以及平行线路间的互感耦合。
- **宽频暂态**：短电缆、架空-地下混合线路、接地系统和雷电/开关操作引起的空间分布效应。

因此，模型选择应从研究目标出发：若只关心低频稳态近似，集中参数可能足够；若研究雷电、快速开关、故障行波或高频振荡，则需要分布参数或频变模型。

## 电报员方程与传播理论

分布参数模型的基本结构是"单位长度参数 + 空间传播"。以 N 导体线路为例，定义单位长度串联阻抗矩阵 $[Z(\omega)]$ 和并联导纳矩阵 $[Y(\omega)]$，则电报员方程为：

$$-\frac{\partial v(x,\omega)}{\partial x} = [Z(\omega)] \cdot i(x,\omega)$$

$$-\frac{\partial i(x,\omega)}{\partial x} = [Y(\omega)] \cdot v(x,\omega)$$

其中 $v(x,\omega)$ 和 $i(x,\omega)$ 分别为位置 $x$ 处的电压和电流通量向量。将两式对 $x$ 求导并代入，可得二阶波动方程：

$$\frac{\partial^2 v(x,\omega)}{\partial x^2} = [Z(\omega)] \cdot [Y(\omega)] \cdot v(x,\omega) = [\gamma(\omega)]^2 \cdot v(x,\omega)$$

$$\frac{\partial^2 i(x,\omega)}{\partial x^2} = [Z(\omega)] \cdot [Y(\omega)] \cdot i(x,\omega) = [\gamma(\omega)]^2 \cdot i(x,\omega)$$

其中 $[\gamma(\omega)] = \sqrt{[Z(\omega)] \cdot [Y(\omega)]}$ 为 **传播常数矩阵**。对于均匀线路，其通解为：

$$v(x,\omega) = e^{-[\gamma(\omega)]x} \cdot v(0,\omega) + \left(1 - e^{-[\gamma(\omega)]x}\right) \cdot v_{\text{reflected}}$$

$$i(x,\omega) = e^{-[\gamma(\omega)]x} \cdot i(0,\omega) + \left(1 - e^{-[\gamma(\omega)]x}\right) \cdot i_{\text{reflected}}$$

在端口处，传播常数 $\gamma$ 和特征导纳 $Y_c = \sqrt{[Z(\omega)]/[Y(\omega)]}$ 构建了线路的端口关系。多导体系统中，$Z$ 和 $Y$ 是矩阵，需考虑 `[[mutual-impedance]]` 和并联电容耦合。

### 单位长度参数的物理组成

如 Kurokawa 2006 所系统阐述，单位长度阻抗分为三个物理部分：

1. **内部纵向阻抗**：与导体内部的电磁场相关，由 Bessel 函数描述，仅影响 $Z$ 矩阵的对角元（自阻抗）。由于集肤效应，电阻随频率增加而增大，电感随频率增加而减小。
2. **外部纵向阻抗（无损大地假设）**：与导体外部空间电磁场相关，在理想导电大地假设下为与频率无关的纯电感矩阵。
3. **大地返回阻抗（有损大地）**：考虑有限电导率时，大地返回路径引入额外的频率相关阻抗项，包含非零的对角元（自阻抗）和互阻抗元。Carson 方程和 Pollaczek 方程均可描述此项，Pollaczek 形式更通用，也适用于地下导体。

并联导纳 $Y$ 的主要假设是：在典型条件下，直到 1 MHz 频率范围内，假设理想导体和大地（无限电导率）是"相当准确"的。

## 核心建模方法体系

分布参数模型在 EMT 仿真中有多种实现路径，按方法论可分为三大类：

### 方法一：模域频率 dependent 行波模型（FD-Line / JMarti）

这是 EMT 工具中最广泛应用的线路模型。其核心思想是：在模坐标下对耦合方程进行解耦，然后对每个独立模量应用行波模型。

**原理**：通过模变换矩阵 $T$，将耦合的相域方程转化为独立的模域方程：

$$[T]^{-1} \cdot [Y] \cdot [Z] \cdot [T] = [\Lambda] = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_N)$$

其中 $[\Lambda]$ 为对角特征值矩阵。在模域中，波动方程解耦为：

$$\frac{\partial^2 v_j}{\partial x^2} = \gamma_j^2 \cdot v_j, \quad j = 1, \ldots, N$$

每个模量的传播常数和特征导纳为：

$$\gamma_j = \sqrt{\lambda_j}, \quad Z_{c,j} = \sqrt{\frac{z_j}{y_j}}$$

**频变处理**：JMarti（J. Marti 1982）模型用 Bode 渐近拟合表示每个模量的传播函数和特征阻抗的频变特性：

$$Z_{c,j}(\omega) \approx \sum_{k} A_{jk} \cdot |j\omega|^{n_{jk}}$$

$$\gamma_j(\omega) \approx \sum_{k} B_{jk} \cdot |j\omega|^{m_{jk}}$$

时域实现通过递归卷积完成：

$$i_j(t) = \frac{2}{Z_{c,j}} v_j(t) - I_{j,\text{hist}}(t-\tau_j)$$

**局限性**：JMarti 假设变换矩阵 $T$ 为实数且与频率无关。对于单回路换位线路，此假设成立；但对于平行线路、非对称多回路或强不对称结构，特征向量随频率剧烈变化，导致模域解耦失效，产生显著误差。Gustavsen 2012 通过 230 kV/115 kV 平行线路算例证明：在此类场景中，JMarti 模型与共模感应电压相比 ULM 基准的偏差可达数倍。

### 方法二：通用线路模型（ULM / 相域频变模型）

ULM（Morched, Gustavsen & Tartibi 1999）直接在相域中求解电报员方程，完全避免了模变换的频率依赖性假设。

**端口关系**：ULM 的频域端口方程为：

$$I_k - Y_c \cdot V_k = -H \cdot (I_m + Y_c \cdot V_m)$$

$$I_m - Y_c \cdot V_m = -H \cdot (I_k + Y_c \cdot V_k)$$

其中 $Y_c = \sqrt{Y^{-1}Z}$ 为特征导纳矩阵，$H = e^{\sqrt{YZ}\,\ell}$ 为传播函数矩阵，$\ell$ 为线路长度。

**时域实现**：将上述方程转换到时域，得到 Norton 等效电路：

$$i_k(t) - y_c(t) * v_k(t) = -b_k(t)$$

$$i_m(t) - y_c(t) * v_m(t) = -b_m(t)$$

其中 $*$ 表示矩阵-向量卷积运算。为高效计算卷积，$y_c(t)$ 和 $h(t)$ 需近似为指数和：

$$\tilde{Y}_c(s) = k_0 + \sum_{n=1}^{N_{pY}} \frac{k_n}{s - a_n}$$

$$\tilde{H}(s) \approx \sum_{j=1}^{N_{\text{mod}}} \left( \sum_{i=1}^{N_{pH}} \frac{c_{ij}}{s - a_i} \right) e^{-s\tau_j}$$

其中 $k_0, k_n, a_n$ 为特征导纳的 Vector Fitting 极点-留数，$\tau_j$ 为第 $j$ 模量的最小传播时延，$c_{ij}$ 为传播函数的极点-留数。时域递归卷积的递推公式为：

$$p_n = \frac{2 + a_n \Delta t}{2 - a_n \Delta t}, \quad q_n = r_n = \frac{k_n \Delta t}{2} - a_n \Delta t$$

$$j_{kn}(t) = p_n \cdot j_{kn}(t-\Delta t) + q_n \cdot v_k(t) + r_n \cdot v_k(t-\Delta t)$$

**优势**：ULM 不依赖模变换矩阵，因此对任意线路结构（包括强不对称平行线路、地下电缆系统）均保持高精度。Zanon 2021 在 ATP 中实现了 ULM，验证了其与 EMTP-RV 的 ULM 模型波形完全重合。

**计算代价**：ULM 的矩阵-向量卷积比 JMarti 的单模卷积计算量更大。Noda 2015 提出的频率分区拟合（FpF）方法通过自适应权重和频率分区策略，在保持精度的同时减少了拟合极点数量。

### 方法三：扩展 Bergeron 模型（含损耗耦合长线）

Bergeron 模型是最经典的分布参数行波模型，假设线路无损且参数为常数。徐政 1996 提出了 **扩展 Bergeron 模型**，将多相耦合线路分解为集中电阻和无损耦合线路两部分：

**核心思想**：将分布电阻等效为线路两端各 $R \cdot \ell/2$ 的集中电阻，中间段视为无损耦合线路。无损段在模坐标下通过相模变换解耦后应用 Bergeron 特征线法；集中电阻段保持在相坐标下直接处理。

**扩展 Bergeron 特征线方程**：

$$i_k(t) - \frac{1}{Z_c} u_k(t) = -\frac{1}{Z_c} u_m(t-\tau) - i_m(t-\tau)$$

其中 $\tau = \ell\sqrt{LC}$ 为传播时延，$Z_c = \sqrt{L/C}$ 为特征阻抗（模坐标下为对角阵）。

**关键创新**：传统相模变换要求电阻矩阵 $R$ 也能被同一变换矩阵对角化，即 $T^{-1}RT$ 为对角阵。但对于任意结构线路（尤其含地线的不对称结构），此前提不成立。徐政 1996 证明：平武输电线路（含地线）的 $R$ 矩阵非对角且非对角元素与对角元素同量级，传统方法失效。扩展 Bergeron 模型通过将电阻在相坐标下作为集中矩阵处理，绕开了这一限制。

**算法步骤**：
1. 输入线路参数 $R, L, C, \ell$ 及仿真步长 $\Delta t$
2. 参数集中化：两端各置 $R \cdot \ell/2$ 集中电阻，中间段为无损线路
3. 构建实数相模变换矩阵 $T$，使 $L$ 和 $C$ 对角化
4. 初始化历史电流源 $I_{\text{hist}}$ 为零
5. 时域主循环：计算无损线路历史电流源 → 模坐标求解 Bergeron 等效电路 → 逆变换回相坐标 → 求解集中电阻节点方程 → 更新历史源

**适用边界**：此方法适用于不计参数频率特性的任意结构多相耦合线路。对于频变参数，需结合 JMarti 或 ULM 的频率相关拟合。

### 方法对比

| 方法 | 坐标系 | 频变处理 | 变换矩阵 | 适用场景 | 精度 | 计算量 |
|------|--------|----------|----------|----------|------|--------|
| FD-Line (JMarti) | 模域 | Bode渐近拟合 | 实数常数 | 单回路换位线路 | 高（单回路） | 低 |
| FD-Line (JMarti) | 模域 | Bode渐近拟合 | 实数常数 | 平行线路/强不对称 | 低（互感耦合误差大） | 低 |
| ULM | 相域 | Vector Fitting + 时延 | 无 | 任意结构（含电缆） | 极高 | 中-高 |
| 扩展 Bergeron | 混合(模+相) | 无(常数参数) | 实数常数 | 任意结构含地线(常数参数) | 高(常数参数) | 低 |

## 形式化表达

### 核心公式汇总

**电报员方程（频域）**：
$$-\frac{\partial v}{\partial x} = [Z(\omega)] \cdot i, \quad -\frac{\partial i}{\partial x} = [Y(\omega)] \cdot v$$

**传播常数**：
$$[\gamma(\omega)] = \sqrt{[Z(\omega)] \cdot [Y(\omega)]}$$

**特征导纳**：
$$[Y_c(\omega)] = \sqrt{[Y(\omega)]^{-1} \cdot [Z(\omega)]}$$

**ULM 端口方程**：
$$I_k - Y_c V_k = -H(I_m + Y_c V_m), \quad H = e^{\sqrt{YZ}\,\ell}$$

**Vector Fitting 有理近似**：
$$F(s) \approx k_0 + \sum_{k=1}^{N_p} \frac{k_k}{s - a_k}$$

**递归卷积递推**：
$$p_k = \frac{2 + a_k \Delta t}{2 - a_k \Delta t}, \quad q_k = \frac{k_k \Delta t}{2} - a_k \Delta t$$

**扩展 Bergeron 特征线**：
$$i_k(t) - Z_c^{-1} u_k(t) = -Z_c^{-1} u_m(t-\tau) - i_m(t-\tau)$$

**大地返回阻抗（Carson 方程）**：
$$Z_{\text{ground}} = j\omega \frac{\mu_0}{2\pi} \left[ \ln\left(\frac{D_{ij}}{d_{ij}}\right) + \frac{1}{2} + 2s \sum_{n=1}^{\infty} K_{2n}(s) \right]$$

其中 $s = \sqrt{j\omega\mu_0\sigma_{\text{earth}}}$ 为大地传播常数，$\sigma_{\text{earth}}$ 为土壤电导率。

**模变换解耦条件**：
$$[T]^{-1} [Z] [T] = \text{diag}(z_1, \ldots, z_N), \quad [T]^{-1} [Y] [T] = \text{diag}(y_1, \ldots, y_N)$$

### 单位长度参数分解

$$Z(\omega) = Z_{\text{internal}}(\omega) + Z_{\text{external}}^{\text{lossless}} + Z_{\text{ground-return}}(\omega)$$

$$Z_{\text{internal}}(\omega) \text{ 由 Bessel 函数描述集肤效应}$$

$$Z_{\text{ground-return}}(\omega) \text{ 由 Carson 或 Nakagawa 方程描述}$$

## 关键技术挑战

### 挑战 1：频变参数的时域实现

频率相关参数从频域转换到时域是分布参数模型的核心难题。Vector Fitting 虽然能高精度拟合频响函数，但拟合阶数、频带范围和无源性直接影响数值稳定性。Gustavsen 2012 指出：当带宽从 100 kHz 扩展到 1 MHz 时，10 km 线路所需的极点数量增加约 10 倍。Noda 2015 的频率分区拟合通过自适应权重降低了这一问题。

### 挑战 2：非对称多导体的模变换频率依赖性

对于单回路换位线路，变换矩阵 $T$ 可视为常数；但对于平行线路、非对称多回路或架空-电缆混合系统，特征向量随频率剧烈变化。Gustavsen 2012 在 230 kV/115 kV 平行线路算例中证明：JMarti 模型与共模感应电压相比 ULM 基准的偏差可达数倍。Gustavsen 提出的改进方案是：每条线路用独立 FD-Line 建模，互感耦合由宽频状态空间模型表示，并通过 mode-revealing transformation 防止公共模态掩盖耦合模态。

### 挑战 3：有损大地参数的准确计算

传统 EMT 工具假设大地为良导体（$\sigma \gg \omega\epsilon$），使用 Carson 方程计算大地返回阻抗并忽略大地导纳。Duarte 2023 通过全波 FDTD 基准验证表明：在高电阻率土壤（$\rho > 500\,\Omega\cdot\text{m}$）和短电缆（50-100 m）场景中，忽略大地导纳会导致显著误差。Duarte 2023 验证了 Papadopoulos 和 Xue 的地下电缆大地返回导纳公式在快速暂态（上升时间低至 0.2 μs）中的有效性，并证明 Wise 方程简化近似在精度与效率间取得了良好平衡。

### 挑战 4：传播时延与仿真步长的匹配

ULM 中每个模量的传播时延 $\tau_j$ 不同，且通常不是仿真步长 $\Delta t$ 的整数倍。Zanon 2021 采用线性插值处理非整数倍时延，但引入了一步延迟补偿。Noda 2015 指出：FpF 方法对时间步长敏感，步长选择不当会导致拟合误差增大。

### 挑战 5：多导体系统的互耦合建模

平行线路间的互感耦合包含电容性耦合（低频主导）和电感性耦合（高频主导）。Gustavsen 2012 提出将两者分离建模：通过终端阻抗矩阵的不同边界条件（一端开路/一端短路）分别计算 $Y_{\text{open}}$ 和 $Y_{\text{short}}$，确保低频电容耦合和高频电感耦合均被准确表示。

## 量化性能边界

| 场景 | 模型 | 精度表现 | 数据来源 |
|------|------|----------|----------|
| 230 kV/115 kV 平行线路，10 km，土壤 100 Ωm | JMarti vs ULM | JMarti 与共模感应电压偏差显著，ULM 与 NLT 基准重合 | Gustavsen 2012 |
| 100 Ωm 土壤，常参数 | JMarti vs ULM | JMarti 偏差可接受（<10%），ULM 与 NLT 完全重合 | Zanon 2021 |
| 10,000 Ωm 土壤，常参数 | JMarti vs ULM | JMarti 出现明显偏差，随时间增大 | Zanon 2021 |
| 5,000 Ωm 土壤，频变参数 | JMarti* vs ULM* | JMarti* 偏差大于 ULM-RV，ULM* 与 ULM-RV 重合 | Zanon 2021 |
| 50 m/100 m 地下电缆，ρ=1000 Ωm | 传输线理论 vs FDTD | 传输线理论在正确计算大地返回参数时与 FDTD 完全一致 | Duarte 2023 |
| 平武 500 kV 线路（含地线） | 扩展 Bergeron vs 传统强制解耦 | 传统方法误差 10-20%，扩展 Bergeron 与频域精确解相当 | 徐政 1996 |
| 任意结构耦合线路 | 扩展 Bergeron vs 频域卷积 | 计算效率提升约 50-60%，内存减少约 40% | 徐政 1996 |

## 适用边界与选择指南

### 场景-方法选择指南

| 应用场景 | 推荐模型 | 原因 |
|----------|----------|------|
| 单回路换位架空线，低频暂态 | FD-Line (JMarti) | 计算效率高，精度足够 |
| 平行线路/多回路，互感耦合研究 | ULM 或 Gustavsen 改进 FD-Line | JMarti 在强不对称下误差大 |
| 地下电缆系统 | ULM | 电缆系统特征向量频变剧烈，JMarti 不适用 |
| 架空-地下混合线路 | ULM | 阻抗突变处 JMarti 误差放大 |
| 任意结构含地线，常数参数 | 扩展 Bergeron | 避免 R 矩阵对角化限制 |
| 宽频暂态（>1 MHz） | ULM + 高拟合阶数 | 需要精确的频变拟合 |
| 实时仿真/FPGA | 频域分区拟合 ULM | Noda 2015 展示 FPGA 实现可行性 |

### 失效场景

- **土壤参数不确定**：Gustavsen 2012 指出，感应电压随土壤电阻率增加而增大，但实际土壤电阻率往往未知且随深度变化，这是模型误差的主要来源之一。
- **线路弧垂变化**：弧垂导致线路几何参数沿空间变化，超出均匀线路假设。
- **频变参数 + 强不对称**：此时需结合频变拟合（FpF 或 VF）与相域模型（ULM），计算代价显著增加。

## 相关方法

- `[[distributed-parameter-line]]` — 分布参数模型在线路对象上的具体化
- `[[transmission-line-model]]` — 输电线路模型概览
- `[[frequency-dependent-line-model]]` — 频变线路模型
- `[[earth-return-impedance]]` — 大地返回阻抗计算
- `[[mutual-impedance]]` — 互阻抗
- `[[modal-transformation]]` — 模变换解耦
- `[[phase-domain-modeling]]` — 相域建模
- `[[lumped-parameter-model]]` — 集中参数模型（简化对照）
- `[[universal-line-model]]` — 通用线路模型
- `[[vector-fitting]]` — 矢量拟合（频变参数有理近似）
- `[[recursive-convolution]]` — 递归卷积（时域实现）
- `[[bergeron-model]]` — Bergeron 行波模型

## 来源论文

- **Kurokawa 2006** *"A New Procedure to Derive Transmission-Line Parameters"* — 系统阐述了单位长度参数的物理分解（内部阻抗/外部阻抗/大地返回阻抗），提出了从终端测量直接推导频变参数的方法，验证了 Carson 和 Pollaczek 方程在架空线路中的一致性。
- **Duarte 2023** *"Assessment of the Transmission Line Theory in the Modeling of Multiconductor Underground Cable Systems"* — 通过全波 FDTD 基准验证了传输线理论在短电缆快速暂态中的有效性，确认了 Papadopoulos 和 Xue 的大地返回导纳公式的准确性，以及 Wise 方程简化近似的精度-效率平衡。
- **Zanon 2021** *"Implementation of the Universal Line Model in the Alternative Transients Program"* — 在 ATP 中实现了 ULM，验证了其与 EMTP-RV 的波形一致性，展示了频变土壤参数（Nakagawa 方程 + Wise 方程 + Alipio-Visacro 因果模型）下的完整实现流程。
- **Noda 2015** *"Application of Frequency-Partitioning Fitting to the Phase-Domain Frequency-Dependent Modeling of Overhead Transmission Lines"* — 将频率分区拟合（FpF）方法应用于相域频变线路建模，在 500 kV 双回路线路算例中验证了 FpF-ULM 的精度，并与 Laplace 变换基准和现场测试进行了对比。
- **Gustavsen 2012** *"Modal Domain-Based Modeling of Parallel Transmission Lines With Emphasis on Accurate Representation of Mutual Coupling Effects"* — 提出了平行线路的改进建模方法：每条线路用独立 FD-Line 建模，互感耦合由状态空间模型表示，并通过 mode-revealing transformation 提高耦合模态的表示精度。
- **徐政 1996** *"耦合长线电磁暂态分析的扩展 Bergeron 模型"* — 提出了将多相耦合线路分解为集中电阻和无损耦合线路两部分的扩展 Bergeron 模型，解决了电阻矩阵非对角时传统相模变换失效的问题，适用于任意结构（含地线）的输电线路。

---
title: "平衡三相线路 (Balanced Three-Phase Line)"
type: method
tags: [three-phase, balanced, transmission-line, symmetrical, positive-sequence, single-phase-equivalent, modal-decoupling, clarke-transform]
created: "2026-05-02"
updated: "2026-05-14"
---

# 平衡三相线路 (Balanced Three-Phase Line)

## 定义

平衡三相线路是电力系统中一种**理想化建模假设**：三相导线的自参数完全相同（$Z_s = Z_p$, $Y_s = Y_p$），相间互参数也完全相同（$Z_m$, $Y_m$），且外部激励和负荷三相对称。在线路参数矩阵层面，它对应**循环对称矩阵**（circulant matrix）；在系统分析层面，它允许通过**模态变换**将三相耦合系统解耦为相互独立的传播模态，进而使用单相等值进行分析和仿真。

平衡三相线路的核心数学特征是：串联阻抗矩阵 $\mathbf{Z}_{abc}$ 和并联导纳矩阵 $\mathbf{Y}_{abc}$ 均为循环对称矩阵，满足

$$
\mathbf{Z}_{abc} =
\begin{bmatrix}
Z_s & Z_m & Z_m \\
Z_m & Z_s & Z_m \\
Z_m & Z_m & Z_s
\end{bmatrix}
\quad,\quad
\mathbf{Y}_{abc} =
\begin{bmatrix}
Y_s & Y_m & Y_m \\
Y_m & Y_s & Y_m \\
Y_m & Y_m & Y_s
\end{bmatrix}
$$

循环对称矩阵的一个关键性质是：**它可以被一个与频率无关的实数变换矩阵完全对角化**。对于三相线路，最常用的变换矩阵是 **Clarke 变换矩阵**（也称克拉克变换矩阵），它将三相物理量映射到 $\alpha$-$\beta$-$0$（或称为线模-地模-零模）三个独立的模态分量上。

$$
\mathbf{T}_{\text{Clarke}} =
\begin{bmatrix}
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{6}} \\
0 & \frac{\sqrt{2}}{\sqrt{3}} & -\frac{\sqrt{2}}{\sqrt{3}} \\
\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}}
\end{bmatrix}
$$

在理想换位（perfectly transposed）的三相线路上，Clarke 变换给出**精确的模态解耦**：$\alpha$ 模态和 $\beta$ 模态具有相同的传播参数（$Z_\alpha = Z_\beta = Z_s - Z_m$），零模态具有独立的传播参数（$Z_0 = Z_s + 2Z_m$）。

> **注意**：平衡三相线路是一个**建模假设**，不是实际线路的物理属性。实际线路由于几何排列、土壤频变效应、平行线路互耦等因素，通常不是严格平衡的。换位（transposition）是工程上使线路**近似**平衡的手段，详见 [[transposed-three-phase-line]]。

## EMT 中的作用

平衡三相假设在 EMT 仿真中具有三重作用：

### 1. 模态解耦：从三相耦合到独立单相

三相线路的 telegrapher 方程在相域中是耦合的偏微分方程组：

$$
\frac{\partial}{\partial x}
\begin{bmatrix}
v_a \\ v_b \\ v_c
\end{bmatrix}
= -\mathbf{Z}(\omega)
\begin{bmatrix}
i_a \\ i_b \\ i_c
\end{bmatrix}
\quad,\quad
\frac{\partial}{\partial x}
\begin{bmatrix}
i_a \\ i_b \\ i_c
\end{bmatrix}
= -\mathbf{Y}(\omega)
\begin{bmatrix}
v_a \\ v_b \\ v_c
\end{bmatrix}
$$

其中 $\mathbf{Z}(\omega)$ 和 $\mathbf{Y}(\omega)$ 是频率相关的阻抗和导纳矩阵。通过 Clarke 变换，将相域量转换为模态域量：

$$
\mathbf{v}_{m} = \mathbf{T}_{\text{Clarke}}^{-1} \mathbf{v}_{abc}
\quad,\quad
\mathbf{i}_{m} = \mathbf{T}_{\text{Clarke}}^{-1} \mathbf{i}_{abc}
$$

在模态域中，方程解耦为三个独立的单相 telegrapher 方程：

$$
\frac{\partial v_\mu}{\partial x} = -Z_\mu(\omega) \cdot i_\mu
\quad,\quad
\frac{\partial i_\mu}{\partial x} = -Y_\mu(\omega) \cdot v_\mu
\quad (\mu = \alpha, \beta, 0)
$$

每个模态可以独立地用 Bergeron 模型、JMarti 模型或折叠线等效电路表示，极大地简化了 EMT 实现。

### 2. 计算复杂度降低

对于平衡三相线路，模态解耦将 $3 \times 3$ 的矩阵运算简化为 3 个标量运算。在大规模网络仿真中，这种简化可以显著减少：

- **矩阵求逆次数**：从每步 $3 \times 3$ 求逆变为 3 次标量除法
- **状态方程维度**：频变 Bergeron 模型中，每个 RL 分支在模态域只需 3 个独立分支
- **内存占用**：特征阻抗和传播函数的拟合参数从 $3 \times 3$ 矩阵降为 3 个标量序列

Tavares 和 Pissolato (1999) 在 440 kV 线路上的验证表明，使用 Clarke 模态域模型与 EMTP 内置频变线路模型（Semlyen 方法）在暂态波形上几乎一致，但计算时间减少了约 **30-40%**（由于矩阵运算简化）。

### 3. 物理量解释

模态域提供清晰的物理图像：

- **$\alpha$ 和 $\beta$ 模态**（线模 / 行波模态）：代表相间传播的电磁波，传播速度快（接近光速），对应 EMT 仿真中感兴趣的微秒级行波暂态
- **零模态**（地模 / 共模）：代表通过大地返回的电流，传播速度较慢（受土壤电导率影响），在接地故障分析中起关键作用

De Conti 等 (2020) 在 15 kV 紧凑型配电线路上的研究表明，$\alpha$ 模态的行波速度约为 $2.98 \times 10^8$ m/s（接近真空光速），而零模态在典型土壤（$\rho = 1000\,\Omega\cdot\text{m}$）下的行波速度降至约 $1.5 \times 10^8$ m/s，速度比约为 **2:1**。

## 核心建模方法

### 方法 1：Clarke 模态域 Bergeron 模型

这是 EMT 程序（如 ATP-EMTP）中最常用的平衡三相线路实现方式。

**步骤 1：相域参数计算**

使用 Carson 公式计算频率相关的自阻抗和互阻抗：

$$
Z_{s}(\omega) = R_c + j\omega L_{ii} + j\frac{\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-(h_i+h_j)u}}{u} \, du
$$

$$
Z_{m}(\omega) = j\frac{\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-(h_i+h_j)u}}{u + \sqrt{u^2 + j\omega\mu_0\sigma_g}} \, du
$$

其中 $R_c$ 是导体直流电阻，$L_{ii}$ 是内部电感，$h_i$, $h_j$ 是导线离地高度，$\sigma_g$ 是土壤电导率。

**步骤 2：Clarke 变换对角化**

$$
\mathbf{Z}_m = \mathbf{T}_{\text{Clarke}} \mathbf{Z}_{abc} \mathbf{T}_{\text{Clarke}}^{-1} =
\begin{bmatrix}
Z_\alpha & 0 & 0 \\
0 & Z_\beta & 0 \\
0 & 0 & Z_0
\end{bmatrix}
$$

对于理想平衡线路：

$$
Z_\alpha = Z_\beta = Z_s - Z_m
\quad,\quad\quad
Z_0 = Z_s + 2Z_m
$$

同理，导纳矩阵解耦为：

$$
Y_\alpha = Y_\beta = Y_s - Y_m
\quad,\quad\quad
Y_0 = Y_s + 2Y_m
$$

**步骤 3：模态 Bergeron 模型**

每个模态用独立的 Bergeron 电路表示：

$$
i_\mu(t) = \frac{1}{Z_{0,\mu}} v_\mu(t) + I_{\mu,\text{hist}}(t - \tau_\mu)
$$

其中 $\tau_\mu = l / v_\mu$ 是模态 $\mu$ 的传播延迟，$l$ 是线路长度，$v_\mu = 1/\sqrt{L_\mu C_\mu}$ 是模态传播速度。

对于频变参数，特征阻抗 $Z_{0,\mu}(\omega)$ 和传播函数 $\gamma_\mu(\omega)$ 通过 **Vector Fitting** 技术拟合为有理函数：

$$
Z_{0,\mu}(\omega) \approx R_0 + j\omega L_0 + \sum_{i=1}^{N} \frac{j\omega R_i}{j\omega + R_i/L_i}
$$

Colqui 等 (2022) 在 ATP 中实现了一种基于理想变压器的 Clarke 变换方案：使用 8 个理想双线圈变压器（对应 Clarke 矩阵的 8 个非零元素）将相域电压/电流转换为模态域，然后每个模态可以连接任意单相等效线路模型（Bergeron、JMarti、折叠线等效等）。

### 方法 2：Clarke 模态域 JMarti 频变模型

JMarti 模型（1982）直接在频域中使用精确的 $\pi$ 等效电路和双曲函数：

$$
\mathbf{v}_m(\omega, x) = \cosh(\gamma_\mu(\omega) x) \cdot \mathbf{v}_m(\omega, 0) + Z_{0,\mu}(\omega) \sinh(\gamma_\mu(\omega) x) \cdot \mathbf{i}_m(\omega, 0)
$$

在模态域中，双曲函数参数 $Z_{0,\mu}(\omega)$ 和 $\gamma_\mu(\omega)$ 通过数值拉普拉斯逆变换（NLT）或递归卷积转换为时域递归形式。

Tavares 等 (1999) 在 EMTP 中验证了 Clarke 模态域 JMarti 模型与 Semlyen 频变模型的对比结果：在 440 kV 单回三相线路上，两种模型在操作过电压仿真中的峰值误差小于 **2%**，在频率扫描中差异小于 **5%**（10 Hz - 10 kHz 范围）。

### 方法 3：相域完整模型（不简化）

当线路不满足平衡假设时（非换位、平行线路互耦、非对称几何），必须使用相域完整模型。此时 $\mathbf{Z}_{abc}$ 和 $\mathbf{Y}_{abc}$ 不能被实数矩阵对角化，需要使用频率相关的变换矩阵（FDQ 模型）。

Gustavsen (2012) 指出，在平行线路应用中，使用恒定变换矩阵（Clarke）的频变线路模型（FD-line）可能产生显著误差。对于两条平行架空线之间的瞬态耦合，FD-line 模型的互感耦合误差可达 **20-40%**。他提出了一种改进方案：将平行线路作为独立的 FD-line 处理，用宽频状态空间模型表示互耦效应。

### 方法 4：多相扩展模态域模型

对于双回三相线（6 相）或六相线，Tavares 等 (1999) 提出先使用 **media/antimedia (m/a) 变换**将六相降为三组双相，再对每组应用 Clarke 变换：

$$
\mathbf{T}_{m/a} =
\begin{bmatrix}
1 & 0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 & 1 \\
1 & 0 & 0 & -1 & 0 & 0 \\
0 & 1 & 0 & 0 & -1 & 0 \\
0 & 0 & 1 & 0 & 0 & -1
\end{bmatrix}
$$

对于直流线路，仅需 m/a 变换即可解耦。

## 形式化表达

### 核心公式汇总

**1. 相域 telegrapher 方程**

$$
\frac{\partial \mathbf{v}_{abc}}{\partial x} = -\mathbf{Z}(\omega) \cdot \mathbf{i}_{abc}
\quad,\quad
\frac{\partial \mathbf{i}_{abc}}{\partial x} = -\mathbf{Y}(\omega) \cdot \mathbf{v}_{abc}
$$

**2. Clarke 变换矩阵**

$$
\mathbf{T}_{\text{Clarke}} =
\begin{bmatrix}
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} & \frac{1}{\sqrt{6}} \\
0 & \frac{\sqrt{2}}{\sqrt{3}} & -\frac{\sqrt{2}}{\sqrt{3}} \\
\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}}
\end{bmatrix}
$$

**3. 模态阻抗/导纳（理想平衡）**

$$
Z_\alpha = Z_\beta = Z_s - Z_m
\quad,\quad\quad
Z_0 = Z_s + 2Z_m
$$

$$
Y_\alpha = Y_\beta = Y_s - Y_m
\quad,\quad\quad
Y_0 = Y_s + 2Y_m
$$

**4. 二阶传播方程**

$$
\frac{\partial^2 \mathbf{v}_{abc}}{\partial x^2} = \mathbf{Z}(\omega)\mathbf{Y}(\omega) \cdot \mathbf{v}_{abc} = \mathbf{S}_V \cdot \mathbf{v}_{abc}
$$

$$
\frac{\partial^2 \mathbf{i}_{abc}}{\partial x^2} = \mathbf{Y}(\omega)\mathbf{Z}(\omega) \cdot \mathbf{i}_{abc} = \mathbf{S}_I \cdot \mathbf{i}_{abc}
$$

**5. Bergeron 时域递归（模态域）**

$$
i_\mu(t) = \frac{1}{Z_{0,\mu}} v_\mu(t) + I_{\mu,\text{hist}}(t - \tau_\mu)
$$

其中历史项：

$$
I_{\mu,\text{hist}}(t - \tau_\mu) = \frac{1}{Z_{0,\mu}} v_\mu(t - \tau_\mu) + i_\mu(t - \tau_\mu)
$$

**6. 频变特征阻抗的有理函数拟合**

$$
Z_{0,\mu}(\omega) \approx R_0 + j\omega L_0 + \sum_{i=1}^{N} \frac{j\omega R_i}{j\omega + R_i/L_i}
$$

**7. Carson 接地返回阻抗**

$$
Z_g(\omega) = j\frac{\omega\mu_0}{2\pi} \ln\left(\frac{1 + j\sqrt{\frac{\omega\mu_0}{4\rho}} \cdot d}{1}\right)
$$

其中 $\rho$ 是土壤电阻率，$d$ 是导线间距。

**8. 传播速度**

$$
v_\mu = \frac{1}{\sqrt{L_\mu C_\mu}}
$$

对于架空线，$\alpha$ 模态速度 $v_\alpha \approx 2.98 \times 10^8$ m/s，零模态速度 $v_0 \approx (1.5-2.5) \times 10^8$ m/s（取决于土壤参数）。

### 参数计算：Kurokawa  procedure

Kurokawa 等 (2006) 提出了两种线路参数计算方法：

**经典方法**：使用 Carson-Pollaczek 积分表示接地效应，Bessel 函数表示集肤效应：

$$
Z_{\text{self}} = R_{\text{dc}} + 4\omega \times 10^{-7} \ln\left(\frac{2h}{r}\right) + Z_g(\omega)
$$

$$
Z_{\text{mutual}} = 4\omega \times 10^{-7} \ln\left(\frac{D_{12'}}{D_{12}}\right) + Z_g(\omega)
$$

**新方法**：直接从已有线路的电压/电流测量数据反推频率相关的线路参数，适用于无法获取几何参数的已建线路。

## 单相等值的条件与限制

### 适用场景

| 场景 | 是否适用 | 说明 |
|------|----------|------|
| 三相对称工频稳态分析 | ✅ | 仅需正序网络 |
| 三相对称短路故障 | ✅ | 正序故障电流可直接计算 |
| 机电暂态仿真（swing） | ✅ | 正序等值足够 |
| 操作过电压（三相合闸） | ✅ | 线模传播主导 |
| 频率扫描（正序注入） | ✅ | 模态解耦精确 |

### 不适用场景

| 场景 | 不适用原因 | 替代方案 |
|------|------------|----------|
| 单相接地故障 | 需要零序网络 | 序分量法（正序+零序+负序） |
| 两相短路 | 正序与负序耦合 | 完整序网络 |
| 断线故障 | 边界不对称 | 相域完整模型 |
| 非换位线路段 | 参数矩阵非循环对称 | 频率相关变换矩阵（FDQ） |
| 平行线路互耦 | 相间耦合不可忽略 | Gustavsen 互耦状态空间模型 |
| 接地故障高频暂态 | 零模态与线模速度差异显著 | 模态域独立 Bergeron 模型 |
| 雷电感应电压 | 需要完整相域电场计算 | EMD 扩展模态域模型 |
| 电缆护套接地 | 多导体耦合复杂 | 多导体频变电缆模型 |

### 单相等值与模态域的关系

单相等值（single-phase equivalent）是平衡三相假设在**相量域**（phasor domain）的简化：只保留正序分量，忽略零序和负序。模态域（modal domain）是平衡三相假设在**时域**（time domain）的扩展：保留所有三个模态（$\alpha$, $\beta$, $0$），但每个模态独立求解。

- **单相等值**：适用于低频（50/60 Hz）正序分析
- **模态域 Bergeron**：适用于 EMT 全频段，包括行波暂态
- **模态域 JMarti**：适用于频变参数的 EMT 全频段分析

## 平衡假设的误差边界

### 换位线路 vs 非换位线路

Torrez Caballero 等 (2017) 系统研究了 Clarke 变换在平衡三相线路建模中的误差边界：

1. **理想换位线路**：Clarke 变换给出**精确**模态解耦，$\alpha$ 和 $\beta$ 模态完全相同，零模态独立。误差为 **0%**（数值舍入误差除外）。

2. **短距离非换位线路**（换位段长度 < $\lambda/4$）：Clarke 变换仍然给出**良好近似**。Tavares 等 (1999) 在 440 kV 线路上验证，非换位情况下的 $\alpha$-$0$ 模态耦合误差在 10 Hz - 10 kHz 范围内小于 **3%**。

3. **长距离非换位线路**：Torrez Caballero 等 (2017) 发现，当线路长度增加时，使用恒定 Clarke 变换矩阵的误差逐渐增大。在电磁暂态仿真中，峰值误差可达 **~10%**。这是因为频率相关的参数矩阵在长距离传播后，不同频率的变换矩阵差异累积。

4. **无垂直对称平面的线路**：Tavares 等 (1999) 指出，即使没有垂直对称平面，Clarke 变换仍然给出"良好近似"，但 $\alpha$ 和 $0$ 模态之间会出现额外耦合，误差取决于具体几何排列和土壤参数，"通常很小，可接受于大多数应用"。

### 频率相关参数的影响

De Conti 和 Emídio (2016) 研究了频率相关土壤参数对模态域线路模型的影响：

- 在不良导电土壤（$\rho > 1000\,\Omega\cdot\text{m}$）下，高频暂态（> 10 kHz）中，频率相关土壤参数对零模态传播的影响显著，与恒定土壤参数相比，零模态传播函数的幅值误差可达 **15-25%**。
- 对于良好导电土壤（$\rho < 100\,\Omega\cdot\text{m}$），恒定土壤参数近似足够精确。
- 线路分支的存在会最小化频率相关土壤参数的影响。

### 平行线路互耦误差

Gustavsen (2012) 对两条平行架空线（230 kV 和 115 kV）的研究表明：

- 使用恒定 Clarke 变换的频变线路模型（FD-line）在模拟线路间瞬态耦合时，由于假设变换矩阵与频率无关，可能在低频段引入 **20-40%** 的互感耦合误差。
- 改进方案：将每条线路作为独立的 FD-line 处理，用宽频状态空间模型表示互耦。该方案在 230 kV 线路对铁路信号系统的干扰仿真中，与 ULM 相域模型的误差小于 **5%**。

## 量化性能边界

| 指标 | 值 | 来源 |
|------|-----|------|
| Clarke 模态域 vs Semlyen 频变模型峰值误差 | < 2% (440 kV 线路) | Tavares 1999 |
| 频率扫描差异 | < 5% (10 Hz - 10 kHz) | Tavares 1999 |
| 计算时间减少 | 30-40% (矩阵运算简化) | Tavares 1999 |
| 非换位线路 $\alpha$-$0$ 模态耦合误差 | < 3% (短距离) | Tavares 1999 |
| 长距离非换位峰值误差 | ~10% | Torrez Caballero 2017 |
| 不良土壤零模态传播函数幅值误差 | 15-25% ($\rho > 1000\,\Omega\cdot\text{m}$) | De Conti 2016 |
| 平行线路 FD-line 互感耦合误差 | 20-40% | Gustavsen 2012 |
| 改进互耦方案 vs ULM 误差 | < 5% | Gustavsen 2012 |
| $\alpha$ 模态行波速度 | $\approx 2.98 \times 10^8$ m/s | De Conti 2020 |
| 零模态行波速度 (典型土壤) | $\approx 1.5 \times 10^8$ m/s | De Conti 2020 |
| 线模/零模速度比 | $\approx 2:1$ | De Conti 2020 |

## 适用边界与选择指南

### 方法选择决策表

| 应用场景 | 推荐模型 | 理由 |
|----------|----------|------|
| 正序工频分析 | 单相等值 | 最简单，无需模态变换 |
| 三相操作过电压 | Clarke 模态 Bergeron | 线模传播主导，计算高效 |
| 接地故障暂态 | Clarke 模态 Bergeron (全模态) | 需要零模态独立求解 |
| 频变参数精确仿真 | Clarke 模态 JMarti | 频率相关特征阻抗精确拟合 |
| 非换位线路 | 相域 ULM 或 FDQ 模型 | Clarke 变换不再精确 |
| 平行线路互耦 | Gustavsen 互耦状态空间 + FD-line | 避免恒定变换矩阵误差 |
| 雷电感应电压 | EMD 扩展模态域模型 | 需要考虑外部电磁场 |
| 紧凑型配电线路 | 模态域 JMarti + 向量拟合 |  bare+covered 导体混合 |
| 多回线路（6 相以上） | m/a + Clarke 多相扩展 | 降维后模态解耦 |

### 换位策略

工程实践中，完全换位（full transposition）是获得平衡参数的标准方法：

- **完全换位**：线路沿全长分为三段，每段导线位置轮换一次，使得每相的平均参数相等
- **短距离换位**：换位段长度 < $\lambda/4$（$\lambda$ 为感兴趣频率的波长），Clarke 变换近似有效
- **无换位**：必须使用相域完整模型或频率相关变换矩阵

## 与相关方法的关系

平衡三相线路是多个 EMT 建模方法的基础假设：

- [[transposed-three-phase-line]]：说明几何换位如何产生平均平衡参数
- [[sequence-component-method]] 和 [[symmetrical-components]]：序分量变换与故障网络分析
- [[modal-transformation]] 和 [[modal-domain-decoupling]]：相域/模域转换在 EMT 线路中的使用边界
- [[bergeron-model]]：模态域 Bergeron 模型是平衡三相线路最常用的 EMT 实现
- [[universal-line-model]]：相域 ULM 是平衡假设失效时的精确替代方案
- [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p]]：频变线路参数计算与平衡假设的结合
- [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-]]：非换位线路的频率相关变换矩阵

## 修订与证据使用注意事项

- 不要将平衡三相线路写成实际线路总是平衡——它是**模型假设**，不是物理属性
- 正序等值不能推导出接地故障零序电流，除非补充零序网络和接地路径
- 在频变 EMT 中，$Z_\alpha = Z_\beta$ 的低频结论不自动说明所有频点和所有传播模态相同
- 若由换位平均得到平衡参数，应保留平均方法和未换位端部的边界说明
- 所有量化指标均有 PDF 来源标注，未报告的数据应标注"原文未报告"

## 来源论文

- **Tavares & Pissolato 1999** (IEEE Trans. Power Delivery) — Clarke 模态域 multiphase 传输线模型，440 kV 线路验证，与 Semlyen 和 JMarti 模型对比
- **Gustavsen 2012** (IEEE Trans. Power Delivery) — 平行线路的模态域建模，恒定变换矩阵误差分析，互耦状态空间模型
- **Torrez Caballero et al. 2017** (Electric Power and Energy Systems) — Clarke 变换误差与线路长度的系统性关系，峰值误差 ~10%
- **Colqui et al. 2022** (IEEE Access) — ATP 中基于理想变压器的 Clarke 变换实现，Bergeron 和 JMarti 组合验证
- **Kurokawa et al. 2006** (IEEE Trans. Power Delivery) — 线路参数计算的经典方法与新方法，Carson-Pollaczek 公式应用
- **De Conti et al. 2020** (Electric Power Systems Research) — 15 kV 紧凑型配电线路的雷电感应电压，模态域 JMarti 模型验证
- **De Conti & Emídio 2016** (Electric Power Systems Research) — 频率相关土壤参数对模态域线路模型的影响
- **Caballero et al. 2015** (Electric Power Systems Research) — 频变多导体 Bergeron 模型，向量拟合在模态域的应用
- **Tavares et al. 1999** (Int. J. Electr. Power Energy Syst.) — 新多相模态域线路模型，media/antimedia 变换扩展

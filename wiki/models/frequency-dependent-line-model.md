---
title: "频变线路模型 (Frequency-Dependent Line Model)"
type: model
tags: [frequency-dependent, transmission-line, cable, wideband, transient]
created: "2026-05-02"
---

# 频变线路模型 (Frequency-Dependent Line Model)

## 概述

频变线路模型考虑输电线路和电缆参数随频率变化的特性，是准确分析宽频电磁暂态现象的关键。传统常参数模型在分析雷击、开关暂态等高频现象时会产生显著误差，因为高频下集肤效应、邻近效应和大地返回效应会导致线路参数发生显著变化。

频变线路模型的核心思想是在频域精确计算线路参数，然后通过有理函数逼近或数值变换方法转换到时域，从而在电磁暂态仿真中准确再现线路的宽频特性。

## 频变参数的物理基础

### 集肤效应 (Skin Effect)

集肤效应是指交流电流在导体截面上的分布不均匀，随着频率升高，电流趋于集中在导体表面薄层流动的现象。集肤深度由以下公式给出：

$$
\delta(f) = \sqrt{\frac{\rho}{\pi f \mu}}
$$

其中 $\rho$ 为导体电阻率，$\mu$ 为磁导率，$f$ 为频率。

集肤效应导致的高频电阻增加：

$$
R(f) = R_{dc} \cdot \frac{r_0}{2\delta(f)} \cdot \frac{ber(r_0/\delta) \cdot bei'(r_0/\delta) - bei(r_0/\delta) \cdot ber'(r_0/\delta)}{(ber'(r_0/\delta))^2 + (bei'(r_0/\delta))^2}
$$

式中 $ber$ 和 $bei$ 为开尔文函数，$r_0$ 为导体等效半径。

内电感随频率降低：

$$
L_{int}(f) = \frac{\mu}{2\pi} \left[ \frac{ber(r_0/\delta) \cdot bei'(r_0/\delta) - bei(r_0/\delta) \cdot ber'(r_0/\delta)}{(ber'(r_0/\delta))^2 + (bei'(r_0/\delta))^2} - \frac{2\delta}{r_0} \right]
$$

### 邻近效应 (Proximity Effect)

邻近效应是指相邻导体中电流相互作用导致电流分布进一步畸变的现象。对于多导线系统，邻近效应会显著影响导体的等效阻抗矩阵。

考虑邻近效应后的阻抗矩阵元素：

$$
Z_{ij}(f) = \begin{cases}
R_{ii}(f) + j\omega L_{ii}(f) + Z_{g,ii}(f), & i = j \\
j\omega L_{ij}(f) + Z_{g,ij}(f), & i \neq j
\end{cases}
$$

其中 $Z_g$ 为大地返回阻抗。

### 大地返回效应 (Ground Return Effect)

大地返回路径的阻抗随频率变化是频变参数的重要组成部分。Carson公式给出了大地返回阻抗的频变表达式：

$$
Z_{g,ij}(f) = \pi^2 f \cdot 10^{-7} \cdot \left[ \frac{4}{\pi} \int_0^\infty \frac{e^{-2h_i \alpha} \cos(x \cdot d_{ij})}{x + \sqrt{x^2 + j\alpha^2}} dx \right]
$$

其中 $\alpha = \sqrt{j\omega\mu_0/\rho_{earth}}$，$h_i$ 为导线对地高度，$d_{ij}$ 为导线间距。

Deri简化公式提供了工程上实用的近似：

$$
Z_{g,ij}(f) \approx \frac{j\omega\mu_0}{2\pi} \ln\frac{2}{\gamma \sqrt{(h_i + h_j)^2 + d_{ij}^2} \cdot \sqrt{\frac{j\omega\mu_0}{\rho_{earth}}}}
$$

式中 $\gamma = 1.7811...$ 为欧拉常数。

## 频变参数的数学模型

### 串联阻抗矩阵

考虑导体内部阻抗和大地返回阻抗，串联阻抗矩阵为：

$$
Z_{ser}(f) = Z_{int}(f) + Z_{ext}(f) + Z_g(f)
$$

导体内部阻抗（单位长度）：

$$
Z_{int}(f) = R_{dc} \cdot k_r(f) + j\omega L_{int}(f)
$$

外部电感（仅与几何结构有关，与频率无关）：

$$
L_{ext} = \frac{\mu_0}{2\pi} \ln\frac{D_{ij}}{r_i}, \quad i \neq j
$$

$$
L_{ext} = \frac{\mu_0}{2\pi} \ln\frac{2h_i}{r_i}, \quad i = j
$$

### 并联导纳矩阵

并联导纳主要由电容构成，在宽频范围内变化较小：

$$
Y_{sh}(f) = G(f) + j\omega C
$$

其中电导 $G(f)$ 考虑介质损耗和电晕损耗的频变特性：

$$
G(f) = G_0 + k \cdot f^n
$$

对于高压电缆，介质损耗角正切通常随频率变化：

$$
\tan\delta(f) = \tan\delta_0 \left(\frac{f}{f_0}\right)^{-\alpha}
$$

电容矩阵元素：

$$
C_{ij} = \frac{2\pi\varepsilon_0\varepsilon_r}{\ln\frac{D_{eq}}{r_{eq}}}, \quad i = j
$$

$$
C_{ij} = -\frac{2\pi\varepsilon_0\varepsilon_r}{\ln\frac{D_{ij}}{r_i}}, \quad i \neq j
$$

### 特性参数

特性阻抗和传播常数是频变线路模型的核心参数：

**特性阻抗**:

$$
Z_c(f) = \sqrt{Z(f)Y^{-1}(f)}
$$

对于多导线系统，特性阻抗矩阵为：

$$
[Z_c(f)] = \sqrt{[Z(f)][Y(f)]^{-1}}
$$

**传播常数**:

$$
\gamma(f) = \sqrt{Z(f)Y(f)}
$$

**传播速度**:

$$
v(f) = \frac{\omega}{\text{Im}(\gamma(f))}
$$

## Marti 模型

### 理论基础

Marti模型由L. Marti于1982年提出，是电磁暂态程序（EMTP）中广泛使用的频变线路模型。其核心思想是通过有理函数逼近频域中的特性阻抗和传播函数。

### 传播函数的有理函数逼近

传播函数定义为：

$$
A(f) = e^{-\gamma(f) \cdot l}
$$

其中 $l$ 为线路长度。Marti模型将传播函数分解为：

$$
A(s) = e^{-s\tau_{min}} \cdot A_{rat}(s)
$$

其中 $e^{-s\tau_{min}}$ 表示理想延迟，$A_{rat}(s)$ 为有理函数逼近：

$$
A_{rat}(s) = \frac{\sum_{k=0}^{m} b_k s^k}{\sum_{k=0}^{n} a_k s^k} = \sum_{i=1}^{n} \frac{k_i}{s - p_i}
$$

### 特性阻抗的有理函数逼近

特性阻抗的有理函数逼近：

$$
Z_c(s) = R_0 + sL_0 + \sum_{i=1}^{n_z} \frac{s k_{z,i}}{s - p_{z,i}}
$$

其中 $R_0$ 和 $L_0$ 分别表示高频电阻和电感。

### 时域状态空间实现

传播函数的时域响应通过递归卷积实现：

$$
h(t) = \mathcal{L}^{-1}\{A_{rat}(s)\} = \sum_{i=1}^{n} k_i e^{p_i t}
$$

接收端电流计算：

$$
i_r(t) = Z_c^{-1} \cdot v_r(t) - i_{hist,r}(t)
$$

历史电流源更新：

$$
i_{hist}(t) = \sum_{i=1}^{n} k_i \cdot e^{p_i \Delta t} \cdot x_i(t-\Delta t)
$$

其中 $x_i$ 为状态变量。

### Marti模型的实现步骤

1. **频率扫描**: 在宽频范围内计算 $Z(f)$、$Y(f)$、$\gamma(f)$、$Z_c(f)$
2. **最小延迟提取**: 确定最小传播时延 $\tau_{min}$
3. **有理函数拟合**: 使用[[vector-fitting]]算法拟合 $A_{rat}(s)$ 和 $Z_c(s)$
4. **无源性检查**: 确保模型满足无源性条件
5. **时域实现**: 建立状态空间方程和递归卷积

## Semlyen 模型

### 递归卷积方法

Semlyen模型由A. Semlyen于1981年提出，采用递归卷积实现频变线路的时域仿真。其核心思想是将卷积积分转化为递推形式，显著降低计算复杂度。

### 传播函数的特性

传播函数在频域表示为：

$$
A(s) = e^{-\gamma(s) \cdot l} = e^{-s\tau} \cdot H(s)
$$

其中 $H(s)$ 为衰减函数，包含有理函数形式：

$$
H(s) = \prod_{i=1}^{n} \frac{s + z_i}{s + p_i}
$$

### 递归卷积推导

卷积积分的离散形式：

$$
y(t) = \int_0^t h(t-\tau) x(\tau) d\tau
$$

对于指数形式的冲激响应 $h(t) = k \cdot e^{-\alpha t}$，卷积可递归计算：

$$
y(t_n) = e^{-\alpha \Delta t} \cdot y(t_{n-1}) + k \cdot \frac{1 - e^{-\alpha \Delta t}}{\alpha} \cdot x(t_n)
$$

对于多指数形式：

$$
h(t) = \sum_{i=1}^{n} k_i e^{-\alpha_i t}
$$

历史电流源更新公式：

$$
i_{hist}(t_n) = \sum_{i=1}^{n} k_i \cdot e^{-\alpha_i \Delta t} \cdot x_i(t_{n-1}) + \sum_{i=1}^{n} k_i \cdot \frac{1 - e^{-\alpha_i \Delta t}}{\alpha_i} \cdot v(t_n)
$$

### Semlyen模型的优势

1. **计算效率**: 递归形式避免完整的卷积计算，复杂度从 $O(n^2)$ 降至 $O(n)$
2. **内存占用**: 仅需存储上一时刻的状态变量
3. **实时仿真**: 适合硬件在环仿真和实时应用
4. **稳定性**: 递归形式天然保证数值稳定

### 极点数量选择

Semlyen模型通常使用较少的极点数量（3-5个），在精度和效率之间取得平衡：

| 极点数量 | 适用频段 | 精度 | 计算量 |
|---------|---------|------|--------|
| 3 | 低频-工频 | 中等 | 低 |
| 5 | 宽频 | 较高 | 中等 |
| 7+ | 超宽频 | 高 | 较高 |

## Noda 模型

### 相域实现方法

Noda模型由T. Noda于1996年提出，直接在相域进行建模，避免了传统模态变换方法的不对称性问题。该模型特别适合不换位输电线路的暂态分析。

### 相域传输方程

多导线系统的频域传输方程：

$$
\frac{d^2}{dx^2} \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix} = [Z(s)][Y(s)] \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix}
$$

其中 $[Z(s)]$ 和 $[Y(s)]$ 为频变阻抗和导纳矩阵。

### 分块矩阵方法

Noda模型将线路分为若干小段，每段用集中参数等效：

$$
\begin{bmatrix} V_s \\ I_s \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_r \\ I_r \end{bmatrix}
$$

其中ABCD参数为频变形式：

$$
[A] = [\cosh(\sqrt{[Z][Y]} \cdot l)]
$$

$$
[B] = [\sqrt{[Z][Y]^{-1}}] \cdot [\sinh(\sqrt{[Z][Y]} \cdot l)]
$$

### 模态变换的替代

传统方法使用模态变换：

$$
[V_{mode}] = [T_v]^{-1} [V_{phase}]
$$

Noda模型直接在相域建立有理函数逼近，避免了以下问题：

1. **模态变换矩阵的频率依赖性**: 变换矩阵 $[T_v]$ 本身随频率变化
2. **不对称性**: 不换位线路的 $[Z][Y]$ 矩阵不可对称化
3. **复数模态**: 复数特征向量导致时域实现困难

### Noda模型的有理函数逼近

相域传播函数的矩阵有理函数逼近：

$$
[A(s)] = [A_0] + s[A_1] + \sum_{k=1}^{n} \frac{[A_k]}{s - p_k}
$$

其中 $[A_k]$ 为留数矩阵，$p_k$ 为公共极点。

### 实现优势

1. **不换位线路**: 直接处理相域耦合，无需近似
2. **多相电缆**: 适合复杂电缆系统的宽频建模
3. **地线处理**: 自然包含地线的影响
4. **参数一致性**: 避免模态域与相域转换引入的误差

## Universal Line Model (ULM)

### 统一框架

Universal Line Model（通用线路模型）由Gustavsen和Semlyen于1999年提出，提供了一个统一的频变线路建模框架。ULM通过改进的矢量拟合算法实现了更宽频范围内的精确建模。

### ULM的核心改进

**1. 权重矢量拟合 (Weighting Vector Fitting)**

引入频率相关权重改善拟合质量：

$$
\min \sum_{k=1}^{N} w(f_k) \cdot |H(f_k) - \tilde{H}(f_k)|^2
$$

其中权重函数：

$$
w(f) = \frac{1}{|H(f)|}
$$

**2. 极点重定位 (Pole Relocation)**

迭代优化极点位置：

$$
\sigma(s) = 1 + \sum_{k=1}^{n} \frac{r_k}{s - \bar{p}_k}
$$

$$\sigma(s) \cdot H(s) \approx \sum_{k=1}^{n} \frac{c_k}{s - \bar{p}_k} + d + s \cdot h
$$

通过迭代求解得到最优极点位置。

**3. 公共极点策略**

ULM使用公共极点集来逼近所有模态的传播函数：

$$
H_i(s) = \sum_{k=1}^{n} \frac{r_{i,k}}{s - p_k} + d_i + s \cdot h_i
$$

这保证了实现的高效性和一致性。

### ULM的时域实现

ULM的时域伴随模型：

$$
i(t) = G_{eq} \cdot v(t) + i_{hist}(t)
$$

其中等效导纳：

$$
G_{eq} = Z_c^{-1}(\infty) + \sum_{k=1}^{n_z} k_{z,k}
$$

历史电流源：

$$
i_{hist}(t) = \sum_{k=1}^{n_a} k_{a,k} \cdot x_k(t-\Delta t) + \sum_{k=1}^{n_z} k_{z,k} \cdot y_k(t-\Delta t)
$$

### ULM的性能特点

1. **宽频精度**: 适用于从直流到数MHz的频率范围
2. **自动拟合**: 最小化用户干预的参数提取
3. **稳健性**: 对噪声数据具有良好的鲁棒性
4. **效率**: 公共极点策略降低计算复杂度

## 矢量拟合技术在频变线路中的应用

### [[vector-fitting]]算法

矢量拟合是频变线路模型参数提取的核心技术。该算法通过迭代优化将有理函数逼近问题转化为线性最小二乘问题。

### 基本算法流程

**步骤1**: 初始化极点 $\{p_k^{(0)}\}$

**步骤2**: 构建并求解线性方程组

$$
\begin{bmatrix}
\frac{1}{s_1-p_1} & \cdots & \frac{1}{s_1-p_n} & 1 & s_1 & -H(s_1)\frac{1}{s_1-p_1} & \cdots \\
\vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots \\
\frac{1}{s_m-p_1} & \cdots & \frac{1}{s_m-p_n} & 1 & s_m & -H(s_m)\frac{1}{s_m-p_1} & \cdots
\end{bmatrix}
\begin{bmatrix} c_1 \\ \vdots \\ c_n \\ d \\ h \\ \tilde{c}_1 \\ \vdots \end{bmatrix} = \begin{bmatrix} H(s_1) \\ \vdots \\ H(s_m) \end{bmatrix}
$$

**步骤3**: 从 $\sigma(s)H(s)$ 的零点获得新的极点

**步骤4**: 重复步骤2-3直至收敛

### 在频变线路中的具体应用

**传播函数拟合**:

$$
A(s) = \sum_{k=1}^{n} \frac{r_k}{s - p_k} + d
$$

**特性阻抗拟合**:

$$
Z_c(s) = R_0 + sL_0 + \sum_{k=1}^{n_z} \frac{s \cdot r_{z,k}}{s - p_{z,k}}
$$

**权重选择策略**:

对于宽频建模，采用对数均匀分布的权重：

$$
w(f) = \frac{1}{f}
$$

### 极点数量与精度

极点数量的选择取决于建模频率范围：

| 频率范围 | 建议极点数 | 相对误差 |
|---------|-----------|---------|
| 0.01Hz - 1kHz | 15-20 | < 1% |
| 0.01Hz - 10kHz | 25-30 | < 1% |
| 0.01Hz - 1MHz | 40-50 | < 2% |

## 无源性强制保证

### 无源性条件

频变线路模型必须满足无源性条件，即系统不向外提供能量。对于频变线路，无源性条件可表示为：

$$
\text{Re}\{Z_{in}(j\omega)\} \geq 0, \quad \forall \omega
$$

$$
\text{Re}\{Y_{in}(j\omega)\} \geq 0, \quad \forall \omega
$$

### 有理函数的无源性检验

对于有理函数逼近 $H(s)$，检验其在虚轴上的实部：

$$
\text{Re}\{H(j\omega)\} = \frac{H(j\omega) + H^*(-j\omega)}{2} \geq 0
$$

### 无源性强制方法

**1. 极点调整法**

将不稳定极点移至左半平面：

$$
\text{if } \text{Re}\{p_k\} > 0, \quad p_k \leftarrow -p_k
$$

**2. 留数修正法**

调整留数以满足正实条件：

$$
r_k^{new} = r_k \cdot \frac{\min_{\omega} \text{Re}\{H(j\omega)\}}{|\min_{\omega} \text{Re}\{H(j\omega)\}|}
$$

**3. 扰动法 (Perturbation Method)**

对不满足无源性的频点进行局部扰动：

$$
H_{new}(j\omega_i) = H(j\omega_i) + \delta_i, \quad \text{if } \text{Re}\{H(j\omega_i)\} < 0
$$

### [[passivity-enforcement]]的实现

在频变线路模型中，无源性强制通常在以下环节实施：

1. **拟合完成后**: 检验并修正有理函数参数
2. **时域实现前**: 确保伴随模型导纳矩阵正定
3. **仿真过程中**: 监测能量不守恒现象

## 典型应用

### 雷电过电压分析

雷电波包含丰富的频谱成分（最高达数MHz），频变线路模型对于准确分析雷电过电压传播至关重要。

**雷电波特性**:
- 波头时间：$1.2 \mu s$
- 半峰值时间：$50 \mu s$
- 等效频率范围：$10kHz - 5MHz$

**频变效应影响**:
- 高频下特性阻抗降低（约10-20%）
- 传播速度增加（接近光速）
- 衰减增大（集肤效应主导）

**应用要点**: 雷电分析需使用宽频频变模型，通常覆盖至5MHz以上频率。

### 开关暂态分析

断路器操作产生的开关暂态包含高频振荡分量，频变模型可准确捕捉以下现象：

**合闸过电压**:
- 线路分布电容充电
- 行波传播和反射
- 铁磁谐振

**模型要求**:
- 准确的高频特性阻抗
- 正确的传播速度
- 考虑电晕的非线性效应

**仿真精度**: 相比常参数模型，频变模型可将开关过电压峰值误差从15-20%降低至5%以内。

### 谐波传播分析

电力电子装置产生的谐波在频变线路上传播时，各次谐波经历不同的衰减和相移。

**谐波阻抗**:

$$
Z_{harmonic}(h) = Z_c(h \cdot f_0) \cdot \coth(\gamma(h \cdot f_0) \cdot l)
$$

其中 $h$ 为谐波次数，$f_0$ 为基波频率。

**谐振分析**: 频变模型可准确预测系统的并联和串联谐振频率，这对于滤波器设计和电能质量评估至关重要。

## 模型对比和选择指南

### 模型特性对比

| 特性 | Marti模型 | Semlyen模型 | Noda模型 | ULM |
|-----|-----------|-------------|----------|-----|
| 理论基础 | 模态变换 | 递归卷积 | 相域直接 | 改进矢量拟合 |
| 适用线路 | 换位线路 | 通用 | 不换位线路 | 通用 |
| 极点数量 | 较多(20+) | 较少(3-5) | 中等(10-15) | 中等(15-25) |
| 计算效率 | 中等 | 高 | 中等 | 中等 |
| 宽频精度 | 高 | 中等 | 高 | 很高 |
| 实现复杂度 | 中等 | 低 | 较高 | 中等 |
| 无源性保证 | 需要额外处理 | 较好 | 需要额外处理 | 较好 |

### 选择建议

**选择 Marti/ULM 当**:
- 需要宽频建模（雷击、GIS暂态）
- 对精度要求高
- 计算资源充足
- 线路参数频变显著

**选择 Semlyen 当**:
- 实时仿真应用
- 计算效率优先
- 频率范围相对有限
- 嵌入式系统实现

**选择 Noda 当**:
- 不换位多相线路
- 电缆系统建模
- 相域耦合显著
- 需要避免模态变换误差

### 工程应用建议

1. **输电线路**: 推荐使用ULM或Marti模型，极点数20-30
2. **地下电缆**: 推荐使用Noda模型或ULM
3. **实时仿真**: 使用简化Semlyen模型，极点数3-5
4. **雷电分析**: 使用ULM，频率范围至5MHz
5. **谐波分析**: 使用Marti模型，重点保证工频至2.5kHz精度

## 相关模型
- [[transmission-line-model]] - 输电线路模型
- [[cable-model]] - 电缆模型
- `untransposed-line-model` - 不换位线路模型
- `pi-section-model` - PI节段模型
- [[bergeron-model]] - Bergeron行波模型

## 相关方法
- [[vector-fitting]] - 矢量拟合算法
- [[modal-transformation]] - 模态变换
- [[phase-domain-modeling]] - 相域建模
- [[companion-circuit]] - 伴随电路
- [[passivity-enforcement]] - 无源性强制
- [[numerical-integration]] - 数值积分

## 相关主题
- [[lightning-overvoltage]] - 雷电过电压
- [[switching-transient]] - 开关暂态
- [[harmonic-analysis]] - 谐波分析
- [[frequency-dependent-modeling]] - 频变建模
- `wideband-simulation` - 宽频仿真

## 来源论文

频变线路模型的主要理论来源包括：
- J. R. Marti, "Accurate Modelling of Frequency-Dependent Transmission Lines in Electromagnetic Transient Simulations" (1982)
- A. Semlyen, "Contributions to the Theory of Frequency Dependent Transmission Lines" (1981)
- T. Noda, "A Robust and Efficient Method for Calculating Line Constants of High Frequency Transmission Lines" (1996)
- B. Gustavsen, "Computer Code for Rational Approximation of Frequency Dependent Admittance Matrices" (1998)
- B. Gustavsen and A. Semlyen, "Rational Approximation of Frequency Domain Responses by Vector Fitting" (1999)
- A. Morched, "A High Frequency Transformer Model for the EMTP" (1992)

参见 [[index.md]] 获取更多频变线路模型相关文献。

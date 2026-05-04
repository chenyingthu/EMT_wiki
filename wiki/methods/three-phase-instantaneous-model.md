---
title: "三相瞬时值模型 (Three-Phase Instantaneous Model)"
type: method
tags: [three-phase, instantaneous, abc-domain, phase-domain, electromagnetic]
created: "2026-05-02"
---

# 三相瞬时值模型 (Three-Phase Instantaneous Model)

## 概述

三相瞬时值模型(Three-Phase Instantaneous Model)是在abc三相坐标系下直接表示电压和电流瞬时值的建模方法，无需进行坐标变换(如`dq0-transformation`或[[symmetrical-components]])。该模型保留了系统固有的相间耦合特性和时变特性，能够精确捕捉不对称、谐波畸变和开关暂态等现象。作为[[enhanced-high-speed-electromagnetic-transient-simulation-17]]的基础，三相瞬时值模型适用于严重不对称工况、非正弦波形分析和电力电子装置建模，是EMTP类仿真软件的核心建模方式。

### 核心优势

- **直接性**: 无需坐标变换，直接在物理三相坐标系中建模
- **完整性**: 保留所有谐波分量和不对称信息
- **通用性**: 适用于正弦和非正弦工况
- **精确性**: 精确描述开关暂态和电力电子装置行为

## 理论基础

### 时域分析与变换域分析对比

在电力系统分析中，存在两种基本的分析方法：

**时域分析法（瞬时值法）**:
- 直接在时间域中描述电压、电流的瞬时值
- 适用于暂态过程、非线性系统和开关操作
- 能够完整保留波形信息

**变换域分析法**:
- 通过数学变换将时域信号转换到其他域
- 包括`phasor-analysis`、`dq0-transformation`、[[symmetrical-components]]等
- 适用于稳态分析和线性系统

| 分析维度 | 瞬时值模型 | 相量法 | dq0变换 | 序分量法 |
|---------|-----------|--------|---------|----------|
| 适用域 | 时域 | 频域 | 旋转坐标系 | 对称分量域 |
| 时变性 | 时变 | 时不变 | 时不变（同步旋转） | 时不变 |
| 谐波处理 | 直接 | 单频 | 需多dq框架 | 各序独立 |
| 非线性 | 直接支持 | 不适用 | 困难 | 困难 |
| 不对称 | 直接支持 | 需对称假设 | 需负序分量 | 专门处理 |
| 计算效率 | 中等 | 高 | 高 | 高 |

### 相量法与瞬时值法的关系

**相量表示**:
$$\dot{V} = V e^{j\theta} = V\cos\theta + jV\sin\theta$$

**瞬时值与相量的转换**:
$$v(t) = \text{Re}\{\sqrt{2}\dot{V}e^{j\omega t}\} = \sqrt{2}V\cos(\omega t + \theta)$$

相量法是瞬时值在单一频率正弦稳态下的简化表示，当系统存在谐波或暂态时，必须使用瞬时值模型。

## 三相变量的数学描述

### 三相电压向量

三相电压瞬时值构成三维向量：

$$\mathbf{v}_{abc}(t) = \begin{bmatrix} v_a(t) \\ v_b(t) \\ v_c(t) \end{bmatrix}$$

对于平衡正弦系统：
$$v_a(t) = \sqrt{2}V\cos(\omega t + \theta)$$
$$v_b(t) = \sqrt{2}V\cos(\omega t + \theta - 120°)$$
$$v_c(t) = \sqrt{2}V\cos(\omega t + \theta + 120°)$$

### 三相电流向量

$$\mathbf{i}_{abc}(t) = \begin{bmatrix} i_a(t) \\ i_b(t) \\ i_c(t) \end{bmatrix}$$

### 三相磁链向量

$$\mathbf{\psi}_{abc}(t) = \begin{bmatrix} \psi_a(t) \\ \psi_b(t) \\ \psi_c(t) \end{bmatrix}$$

### 复数空间矢量表示

除abc分量表示外，三相量还可用复数空间矢量表示：

$$\vec{v} = \frac{2}{3}(v_a + a v_b + a^2 v_c)$$

其中 $a = e^{j120°} = -\frac{1}{2} + j\frac{\sqrt{3}}{2}$ 为旋转算子。

逆变换：
$$\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ -\frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{1}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix} \begin{bmatrix} v_\alpha \\ v_\beta \end{bmatrix}$$

## 瞬时值表示的详细推导

### 一般形式的瞬时电压

对于任意波形，三相电压瞬时值可表示为：

$$v_k(t) = V_k(t)\cos[\omega t + \theta_k(t)] + \sum_{h=2}^{H}V_{k,h}(t)\cos[h\omega t + \theta_{k,h}(t)] + v_{k,dc}(t)$$

其中：
- $k \in \{a, b, c\}$ 表示相别
- $V_k(t)$: 基波幅值（可能时变）
- $\theta_k(t)$: 基波相位（可能时变）
- $h$: 谐波次数
- $v_{k,dc}$: 直流分量

### 幅值和相位的提取

给定瞬时值 $v(t)$，其瞬时幅值可通过希尔伯特变换求得：

$$\hat{v}(t) = \mathcal{H}\{v(t)\}$$

$$V_{inst}(t) = \sqrt{v^2(t) + \hat{v}^2(t)}$$

$$\theta_{inst}(t) = \arctan\frac{\hat{v}(t)}{v(t)}$$

### 三相瞬时对称分量

在瞬时值域中，可定义瞬时对称分量：

$$\begin{bmatrix} v_0(t) \\ v_+(t) \\ v_-(t) \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} \begin{bmatrix} v_a(t) \\ v_b(t) \\ v_c(t) \end{bmatrix}$$

其中：
- $v_0(t)$: 零序分量
- $v_+(t)$: 正序分量
- $v_-(t)$: 负序分量

这与传统的[[symmetrical-components]]不同，这里的分量仍是时间的函数。

## 三相电感模型

### 磁链方程

三相耦合电感系统的磁链方程为：

$$\mathbf{\psi}_{abc} = \mathbf{L}_{abc}\mathbf{i}_{abc}$$

展开形式：
$$\begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c \end{bmatrix} = \begin{bmatrix} L_{aa} & L_{ab} & L_{ac} \\ L_{ba} & L_{bb} & L_{bc} \\ L_{ca} & L_{cb} & L_{cc} \end{bmatrix} \begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$

### 电感矩阵结构

对于对称三相系统，电感矩阵具有特定结构：

$$\mathbf{L}_{abc} = \begin{bmatrix} L_s & L_m & L_m \\ L_m & L_s & L_m \\ L_m & L_m & L_s \end{bmatrix}$$

其中：
- $L_s$: 自感
- $L_m$: 互感（通常 $L_m < 0$）

对于输电线路，典型的电感参数为：
$$L_s = \frac{\mu_0}{2\pi}\ln\frac{D_{aa}}{r'}, \quad L_m = \frac{\mu_0}{2\pi}\ln\frac{D_{aa}}{D_{ab}}$$

### 电压方程

考虑电阻和电感的完整电压方程：

$$\mathbf{v}_{abc} = \mathbf{R}\mathbf{i}_{abc} + \frac{d\mathbf{\psi}_{abc}}{dt}$$

$$\mathbf{v}_{abc} = \mathbf{R}\mathbf{i}_{abc} + \mathbf{L}\frac{d\mathbf{i}_{abc}}{dt} + \frac{d\mathbf{L}}{dt}\mathbf{i}_{abc}$$

对于线性时不变电感：
$$\mathbf{v}_{abc} = \mathbf{R}\mathbf{i}_{abc} + \mathbf{L}\frac{d\mathbf{i}_{abc}}{dt}$$

### 耦合关系与解耦条件

三相电感间的耦合程度由互感与自感之比决定：

$$k = \frac{|L_m|}{L_s}$$

当 $k = 0.5$ 时，通过`clarke-transformation`可实现完全解耦。

## 三相电容模型

### 电荷方程

三相电容系统的电荷-电压关系：

$$\mathbf{q}_{abc} = \mathbf{C}_{abc}\mathbf{v}_{abc}$$

其中电容矩阵：
$$\mathbf{C}_{abc} = \begin{bmatrix} C_{aa} & -C_{ab} & -C_{ac} \\ -C_{ba} & C_{bb} & -C_{bc} \\ -C_{ca} & -C_{cb} & C_{cc} \end{bmatrix}$$

注意：非对角元素为负，表示相间耦合电容。

### 电流方程

电容电流是电荷的变化率：

$$\mathbf{i}_{abc} = \frac{d\mathbf{q}_{abc}}{dt} = \mathbf{C}_{abc}\frac{d\mathbf{v}_{abc}}{dt}$$

展开形式：
$$\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix} = \begin{bmatrix} C_{aa} & -C_{ab} & -C_{ac} \\ -C_{ba} & C_{bb} & -C_{bc} \\ -C_{ca} & -C_{cb} & C_{cc} \end{bmatrix} \frac{d}{dt}\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

### 对称三相电容

对于对称系统，电容矩阵简化为：

$$\mathbf{C}_{abc} = \begin{bmatrix} C_s & -C_m & -C_m \\ -C_m & C_s & -C_m \\ -C_m & -C_m & C_s \end{bmatrix}$$

其中：
- $C_s = C_{phase} + 2C_{mutual}$: 等效自电容
- $C_m = C_{mutual}$: 互电容

### 串联和并联组合

**串联连接**:
$$\mathbf{C}_{eq}^{-1} = \mathbf{C}_1^{-1} + \mathbf{C}_2^{-1}$$

**并联连接**:
$$\mathbf{C}_{eq} = \mathbf{C}_1 + \mathbf{C}_2$$

注意：由于耦合的存在，电容矩阵的逆必须整体计算。

## 三相电阻模型

### 基本欧姆定律

三相电阻网络遵循广义欧姆定律：

$$\mathbf{v}_{abc} = \mathbf{R}_{abc}\mathbf{i}_{abc}$$

### 对称电阻矩阵

对于对称三相电阻：

$$\mathbf{R}_{abc} = \begin{bmatrix} R & 0 & 0 \\ 0 & R & 0 \\ 0 & 0 & R \end{bmatrix} = R\mathbf{I}_3$$

### 不对称情况

当三相电阻不对称时（如单相负荷）：

$$\mathbf{R}_{abc} = \begin{bmatrix} R_a & 0 & 0 \\ 0 & R_b & 0 \\ 0 & 0 & R_c \end{bmatrix}$$

其中 $R_a \neq R_b \neq R_c$，导致三相电流不平衡。

### 相间耦合电阻

在某些特殊情况下（如接地电阻网络），电阻矩阵可能非对角：

$$\mathbf{R}_{abc} = \begin{bmatrix} R_{aa} & R_{ab} & R_{ac} \\ R_{ba} & R_{bb} & R_{bc} \\ R_{ca} & R_{cb} & R_{cc} \end{bmatrix}$$

### 功率损耗计算

三相电阻的总功率损耗：

$$P_{loss} = \mathbf{i}_{abc}^T \mathbf{R}_{abc} \mathbf{i}_{abc} = i_a^2 R_a + i_b^2 R_b + i_c^2 R_c$$

对于对称电阻：
$$P_{loss} = R(i_a^2 + i_b^2 + i_c^2)$$

## 网络方程

### 节点电压方程

基于[[nodal-analysis]]，三相网络的节点方程为：

$$\mathbf{Y}_{abc}\mathbf{V}_{abc} = \mathbf{I}_{abc}$$

其中：
- $\mathbf{Y}_{abc}$: $3n \times 3n$ 节点导纳矩阵（$n$为节点数）
- $\mathbf{V}_{abc}$: 节点电压向量
- $\mathbf{I}_{abc}$: 注入电流向量

### 导纳矩阵结构

三相导纳矩阵是分块矩阵：

$$\mathbf{Y}_{abc} = \begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} & \cdots & \mathbf{Y}_{1n} \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} & \cdots & \mathbf{Y}_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \mathbf{Y}_{n1} & \mathbf{Y}_{n2} & \cdots & \mathbf{Y}_{nn} \end{bmatrix}$$

每个子矩阵 $\mathbf{Y}_{ij}$ 是 $3 \times 3$ 的三相导纳块：

$$\mathbf{Y}_{ij} = \begin{bmatrix} Y_{aa} & Y_{ab} & Y_{ac} \\ Y_{ba} & Y_{bb} & Y_{bc} \\ Y_{ca} & Y_{cb} & Y_{cc} \end{bmatrix}_{ij}$$

### KCL方程的三相形式

对于节点$k$，三相KCL方程为：

$$\sum_{j \in \mathcal{N}_k} \mathbf{Y}_{kj}(\mathbf{V}_k - \mathbf{V}_j) = \mathbf{I}_k$$

其中 $\mathcal{N}_k$ 表示与节点$k$相邻的节点集合。

### 网络元件的导纳表示

**三相线路**:
$$\mathbf{Y}_{line} = \mathbf{Z}_{abc}^{-1} = (\mathbf{R} + j\omega\mathbf{L})^{-1}$$

**三相变压器**:
$$\mathbf{Y}_{trf} = \begin{bmatrix} \mathbf{Y}_{pp} & \mathbf{Y}_{ps} \\ \mathbf{Y}_{sp} & \mathbf{Y}_{ss} \end{bmatrix}$$

其中$p$表示原边，$s$表示副边。

### 不对称网络的求解

对于不对称网络，导纳矩阵不再具有对称分量的解耦特性，必须整体求解：

$$\mathbf{V}_{abc} = \mathbf{Y}_{abc}^{-1}\mathbf{I}_{abc}$$

这要求求解 $3n \times 3n$ 的复数线性方程组。

## 三相功率计算

### 瞬时有功功率

三相系统的瞬时有功功率定义为三相瞬时功率之和：

$$p(t) = v_a(t)i_a(t) + v_b(t)i_b(t) + v_c(t)i_c(t) = \mathbf{v}_{abc}^T \mathbf{i}_{abc}$$

对于正弦稳态：
$$p(t) = 3VI\cos\varphi + VI\cos(2\omega t + \theta_v + \theta_i) + \cdots$$

### 瞬时无功功率

基于`instantaneous-reactive-power-theory`，定义瞬时无功功率：

$$q(t) = v_\alpha i_\beta - v_\beta i_\alpha$$

其中 $\alpha\beta$ 分量通过`clarke-transformation`获得：

$$\begin{bmatrix} v_\alpha \\ v_\beta \end{bmatrix} = \frac{2}{3}\begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix}\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

### 瞬时有功和无功的统一表示

使用复功率表示：

$$\vec{s}(t) = p(t) + jq(t) = \vec{v}(t) \cdot \vec{i}^*(t)$$

其中 $\vec{v}$ 和 $\vec{i}$ 是复数空间矢量。

### 三相平均功率

在一个周期内的平均有功功率：

$$P = \frac{1}{T}\int_0^T p(t)dt = \frac{1}{T}\int_0^T [v_a(t)i_a(t) + v_b(t)i_b(t) + v_c(t)i_c(t)]dt$$

对于平衡系统：
$$P = 3VI\cos\varphi$$

### 视在功率和功率因数

三相视在功率：
$$S = \sqrt{P^2 + Q^2}$$

功率因数：
$$\lambda = \frac{P}{S}$$

对于非正弦系统，需使用`power-definitions-nonlinear`。

## 应用场景详解

### 不对称分析

三相瞬时值模型在不对称分析中具有独特优势：

**单相接地故障**:
故障相电压：$v_f(t) = R_f i_f(t)$
其中 $R_f$ 为接地电阻。

**两相短路**:
$$v_b(t) - v_c(t) = 0, \quad i_a(t) = 0$$

**非全相运行**:
断开相电流为零约束：
$$i_{open}(t) = 0$$

**特点**:
- 无需对称假设，直接处理不平衡
- 自动考虑相间的电磁耦合
- 适用于任意复杂的不对称工况

### 谐波分析

**非线性负荷建模**:
- 电弧炉：时变电弧电阻模型
- 变频器：开关函数表示
- 整流器：二极管/晶闸管开关模型

**谐波功率流**:
$$\mathbf{Y}^{(h)}\mathbf{V}^{(h)} = \mathbf{I}^{(h)}$$

其中上标$(h)$表示第$h$次谐波。

**特点**:
- 在时域中保留所有谐波信息
- 可分析谐波间的交叉耦合
- 频谱分析通过后处理实现

### 电力电子应用

**开关暂态分析**:
- PWM波形精确建模
- 开关损耗计算
- 谐波畸变评估

**变频器模型**:
$$v_{out}(t) = S(t) \cdot v_{dc}(t)$$

其中 $S(t)$ 为开关函数。

**优势**:
- 直接建模开关动作
- 精确捕捉开关瞬间的电压电流波形
- 与控制系统的直接接口

### 变压器暂态分析

**励磁涌流**:
$$v_{abc}(t) = R\mathbf{i}_{abc} + \frac{d}{dt}\mathbf{\psi}_{abc}(\mathbf{i}_{abc})$$

考虑磁饱和特性的非线性磁化曲线。

**内部故障**:
绕组匝间短路的不对称电流分布。

## 与变换域方法的详细对比

### 与dq0变换的对比

`dq0-transformation`将三相量转换到旋转坐标系：

$$\mathbf{v}_{dq0} = \mathbf{T}_{dq0}(\theta)\mathbf{v}_{abc}$$

**对比分析**：

| 特性 | 瞬时值模型 | dq0变换 |
|------|-----------|---------|
| 坐标系 | 静止abc | 旋转dq0 |
| 正弦信号 | 时变 | 直流（稳态） |
| 计算复杂度 | 中等 | 低（稳态） |
| 谐波处理 | 直接 | 需多参考系 |
| 不对称处理 | 直接 | 需负序分量 |
| 开关建模 | 直接 | 困难 |

**变换关系**：
$$\mathbf{T}_{dq0}(\theta) = \frac{2}{3}\begin{bmatrix} \cos\theta & \cos(\theta-120°) & \cos(\theta+120°) \\ -\sin\theta & -\sin(\theta-120°) & -\sin(\theta+120°) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix}$$

### 与序分量法的对比

[[symmetrical-components]]将不对称系统分解为正序、负序、零序：

$$\begin{bmatrix} \dot{V}_+ \\ \dot{V}_- \\ \dot{V}_0 \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 1 & a & a^2 \\ 1 & a^2 & a \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} \dot{V}_a \\ \dot{V}_b \\ \dot{V}_c \end{bmatrix}$$

**对比分析**：

| 特性 | 瞬时值模型 | 序分量法 |
|------|-----------|---------|
| 适用条件 | 通用 | 线性稳态 |
| 物理直观性 | 高 | 中等 |
| 故障分析 | 数值仿真 | 解析计算 |
| 谐波分析 | 时域FFT | 各序独立分析 |
| 暂态分析 | 直接支持 | 不适用 |

### 变换选择指南

**选择瞬时值模型的情况**：
- 电磁暂态仿真
- 电力电子开关分析
- 严重不对称工况
- 谐波畸变严重
- 需要精确波形

**选择变换域方法的情况**：
- 稳态潮流计算
- 简单故障分析
- 控制系统设计
- 快速近似计算
- 频域特性分析

## 数值实现考虑

### 时间离散化

在`electromagnetic-transient-program`类软件中，采用伴随电路法进行离散：

**电感离散**:
$$i_L(t) = i_L(t-\Delta t) + \frac{\Delta t}{2L}[v_L(t) + v_L(t-\Delta t)]$$

**电容离散**:
$$i_C(t) = -i_C(t-\Delta t) + \frac{2C}{\Delta t}[v_C(t) - v_C(t-\Delta t)]$$

### 数值稳定性

采用梯形积分法的稳定条件：
$$\Delta t < \frac{1}{\pi f_{max}}$$

其中 $f_{max}$ 为最高频率分量。

### 计算效率优化

- 稀疏矩阵技术求解网络方程
- 多速率仿真（不同元件采用不同步长）
- 并行计算（三相解耦或分区并行）

## 相关主题

- [[phase-domain-modeling]] - 相域建模
- [[coordinate-transformation]] - 坐标变换
- [[symmetrical-components]] - 对称分量法
- [[enhanced-high-speed-electromagnetic-transient-simulation-17]] - 电磁暂态仿真
- `clarke-transformation` - Clarke变换
- `dq0-transformation` - dq0变换
- [[nodal-analysis]] - 节点分析法
- `instantaneous-reactive-power-theory` - 瞬时无功功率理论
- `electromagnetic-transient-program` - 电磁暂态程序
- `phasor-analysis` - 相量分析法

## 来源论文

参见 [[index.md]] 获取更多三相瞬时值模型相关文献。

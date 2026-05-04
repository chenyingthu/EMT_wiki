---
title: "传输线理论 (Transmission Line Theory)"
type: method
tags: [transmission-line, wave-propagation, distributed-parameter, telegrapher-equation]
created: "2026-05-02"
---

# 传输线理论 (Transmission Line Theory)

## 概述

传输线理论是研究电磁波在导线上传播规律的理论基础，是电力系统电磁暂态（EMT）仿真和通信线路设计的核心理论。与集总参数电路模型不同，传输线理论考虑电气参数沿导线长度的空间分布特性，能够准确描述高频信号、快速暂态和长距离输电线路中的波过程。

### 核心物理概念

传输线理论建立在以下物理基础之上：

- **电磁波传播**：电压和电流以电磁波形式沿线传播，传播速度接近光速
- **分布参数特性**：电阻R、电感L、电导G、电容C均匀分布在整条线路上
- **波阻抗匹配**：特性阻抗决定波的能量传输效率
- **反射与折射**：阻抗不连续处产生波的反射和折射现象

### 应用场景

- [[emt-simulation]] - 电磁暂态仿真中的线路建模
- `lightning-protection` - 雷电过电压分析
- [[switching-transient]] - 开关操作过电压计算
- `power-quality` - 电能质量谐波分析
- `communication-system` - 电力线载波通信

## 物理基础

### 电磁波传播机理

当电压施加到传输线一端时，电场以光速向线路另一端传播。由于导线具有分布电感和电容，能量以电磁场形式存储和传递，而非瞬时传遍整条线路。

$$\frac{\partial^2 v}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 v}{\partial t^2}$$

其中 $c = 1/\sqrt{\mu_0\varepsilon_0} \approx 3 \times 10^8$ m/s 为真空中的光速。

### 分布参数与集总参数的区别

| 特性 | 集总参数模型 | 分布参数模型 |
|------|-------------|-------------|
| 参数位置 | 集中在电路节点 | 沿线路连续分布 |
| 适用条件 | 线路长度 $\ll$ 波长 | 线路长度与波长可比拟 |
| 时延效应 | 忽略传播时延 | 必须考虑波传播时延 |
| 波过程 | 无反射、折射现象 | 存在复杂的波过程 |
| 数学描述 | 常微分方程 | 偏微分方程 |

当信号波长 $\lambda = v/f$ 与线路长度 $l$ 满足 $l > \lambda/20$ 时，必须使用分布参数模型。

## 基本方程

### 电报方程的推导

考虑一段长度为 $\Delta x$ 的传输线微元，其等效电路包含串联的电阻 $R\Delta x$ 和电感 $L\Delta x$，以及并联的电导 $G\Delta x$ 和电容 $C\Delta x$。

#### 电压方程推导

对微元应用基尔霍夫电压定律（KVL）：

$$v(x,t) - v(x+\Delta x,t) = R\Delta x \cdot i(x,t) + L\Delta x \cdot \frac{\partial i(x,t)}{\partial t}$$

两边除以 $\Delta x$ 并取极限 $\Delta x \rightarrow 0$：

$$-\frac{\partial v}{\partial x} = Ri + L\frac{\partial i}{\partial t} \quad \text{(1)}$$

#### 电流方程推导

对微元应用基尔霍夫电流定律（KCL）：

$$i(x,t) - i(x+\Delta x,t) = G\Delta x \cdot v(x+\Delta x,t) + C\Delta x \cdot \frac{\partial v(x+\Delta x,t)}{\partial t}$$

两边除以 $\Delta x$ 并取极限：

$$-\frac{\partial i}{\partial x} = Gv + C\frac{\partial v}{\partial t} \quad \text{(2)}$$

方程(1)和(2)构成**电报方程组（Telegrapher's Equations）**，是传输线理论的基础。

### 波动方程的完整推导

#### 电压波动方程

对式(1)关于 $x$ 求偏导：

$$-\frac{\partial^2 v}{\partial x^2} = R\frac{\partial i}{\partial x} + L\frac{\partial^2 i}{\partial x \partial t}$$

将式(2)代入上式：

$$-\frac{\partial^2 v}{\partial x^2} = R\left(-Gv - C\frac{\partial v}{\partial t}\right) + L\frac{\partial}{\partial t}\left(-Gv - C\frac{\partial v}{\partial t}\right)$$

展开整理得：

$$\frac{\partial^2 v}{\partial x^2} = LC\frac{\partial^2 v}{\partial t^2} + (RC+LG)\frac{\partial v}{\partial t} + RGv \quad \text{(3)}$$

#### 电流波动方程

同理，对式(2)关于 $x$ 求偏导并代入式(1)，可得：

$$\frac{\partial^2 i}{\partial x^2} = LC\frac{\partial^2 i}{\partial t^2} + (RC+LG)\frac{\partial i}{\partial t} + RGi \quad \text{(4)}$$

方程(3)和(4)为**传输线波动方程**，是二阶线性偏微分方程。

#### 无损线简化

对于理想无损线（$R=0$, $G=0$）：

$$\frac{\partial^2 v}{\partial x^2} = LC\frac{\partial^2 v}{\partial t^2} = \frac{1}{v_p^2}\frac{\partial^2 v}{\partial t^2}$$

这就是标准的**一维波动方程**，波速 $v_p = 1/\sqrt{LC}$。

## 线路参数计算

### 单位长度参数定义

| 参数 | 符号 | 单位 | 物理意义 | 影响因素 |
|------|------|------|----------|----------|
| 电阻 | $R$ | $\Omega$/m | 导体欧姆损耗 | 材料电阻率、集肤效应 |
| 电感 | $L$ | H/m | 磁场储能能力 | 导线几何、介质磁导率 |
| 电导 | $G$ | S/m | 介质泄漏损耗 | 绝缘材料、湿度 |
| 电容 | $C$ | F/m | 电场储能能力 | 导线间距、介电常数 |

### 几何平均距离（GMD）

对于多导体系统，导体之间的互感计算需要用到几何平均距离（Geometric Mean Distance, GMD）。

#### 双导体系统的GMD

对于间距为 $D$ 的两根导体：

$$D_{eq} = D$$

#### 三相线路的GMD

对于水平排列的三相导线，间距分别为 $D_{ab}$、$D_{bc}$、$D_{ca}$：

$$D_{eq} = \sqrt[3]{D_{ab} \cdot D_{bc} \cdot D_{ca}}$$

对于对称排列（等边三角形）：

$$D_{eq} = D$$

#### 分裂导线的GMD

对于每相分裂数为 $n$ 的分裂导线，先计算自几何均距 $D_s^b$：

$$D_s^b = \sqrt[n^2]{(D_{11}D_{12}\cdots D_{1n})(D_{21}D_{22}\cdots D_{2n})\cdots(D_{n1}D_{n2}\cdots D_{nn})}$$

其中 $D_{ii}$ 为子导线自几何均距（等于子导线GMR），$D_{ij}$（$i \neq j$）为子导线间距。

`gmd` - 几何平均距离详解

### 几何平均半径（GMR）

几何平均半径（Geometric Mean Radius, GMR）用于计算导体的自感。

#### 实心圆导线的GMR

对于半径为 $r$ 的实心圆导线：

$$D_s = r \cdot e^{-1/4} \approx 0.7788r$$

推导过程：实心导线的内磁链产生的附加电感对应于半径缩小系数 $e^{-1/4}$。

#### 绞线的GMR

对于由多股绞合的导线，GMR由制造商提供，典型值约为：

$$D_s \approx 0.7 \sim 0.8r$$

其中 $r$ 为导线外半径。

#### 分裂导线的等效GMR

对于分裂间距为 $s$ 的 $n$ 分裂导线：

$$D_s^{eq} = \sqrt[n]{D_s \cdot s^{n-1}}$$

其中 $D_s$ 为单根子导线的GMR。

`gmr` - 几何平均半径详解

### 线路参数计算公式

#### 电感计算

单相线路的单位长度电感：

$$L = 2 \times 10^{-7} \ln\frac{D}{D_s} \quad \text{[H/m]}$$

三相平衡线路的正序电感：

$$L_1 = 2 \times 10^{-7} \ln\frac{D_{eq}}{D_s} \quad \text{[H/m]}$$

考虑大地回路影响的卡森（Carson）修正：

$$L = 2 \times 10^{-7} \left(\ln\frac{2h}{r} + \frac{\mu_r}{4}\right) \quad \text{[H/m]}$$

其中 $h$ 为导线对地高度。

#### 电容计算

单相线路的单位长度电容：

$$C = \frac{\pi\varepsilon_0}{\ln(D/r)} \quad \text{[F/m]}$$

三相线路的正序电容：

$$C_1 = \frac{2\pi\varepsilon_0}{\ln(D_{eq}/r)} \quad \text{[F/m]}$$

考虑大地影响的电容修正：

$$C = \frac{2\pi\varepsilon_0}{\ln(2h/r)} \quad \text{[F/m]}$$

其中 $\varepsilon_0 = 8.854 \times 10^{-12}$ F/m。

#### 电阻计算

直流电阻：

$$R_{dc} = \frac{\rho}{A} \quad [\Omega/m]$$

其中 $\rho$ 为电阻率，$A$ 为导线截面积。

交流电阻（考虑集肤效应）：

$$R_{ac} = R_{dc} \cdot k_s$$

集肤效应系数 $k_s$ 随频率增加而增大：

$$k_s \approx 1 + \frac{(r/\delta)^4}{3 + (r/\delta)^4}$$

其中 $\delta = \sqrt{\frac{2\rho}{\omega\mu}}$ 为集肤深度。

## 行波特性

### 特性阻抗的详细推导

对于正弦稳态，电报方程的相量形式为：

$$-\frac{dV}{dx} = (R+j\omega L)I = ZI$$
$$-\frac{dI}{dx} = (G+j\omega C)V = YV$$

对第一式求导并代入第二式：

$$\frac{d^2V}{dx^2} = ZYV = \gamma^2 V$$

解为：

$$V(x) = V^+ e^{-\gamma x} + V^- e^{\gamma x}$$

对应电流：

$$I(x) = \frac{V^+}{Z_c} e^{-\gamma x} - \frac{V^-}{Z_c} e^{\gamma x}$$

其中**特性阻抗**定义为：

$$Z_c = \sqrt{\frac{Z}{Y}} = \sqrt{\frac{R+j\omega L}{G+j\omega C}}$$

#### 无损线特性阻抗

当 $R=0$, $G=0$ 时：

$$Z_c = \sqrt{\frac{L}{C}}$$

对于架空线路，典型值约为 $300 \sim 400$ $\Omega$；对于电缆线路，由于电容较大，典型值约为 $30 \sim 60$ $\Omega$。

#### 特性阻抗的物理意义

特性阻抗表示传输线上行波电压与行波电流的比值，具有以下特性：

- 纯阻性（无损线情况下）
- 与线路长度无关
- 决定能量传输效率
- 决定阻抗匹配条件

`characteristic-impedance` - 特性阻抗详解

### 传播常数的完整分析

传播常数定义为：

$$\gamma = \sqrt{ZY} = \sqrt{(R+j\omega L)(G+j\omega C)} = \alpha + j\beta$$

#### 衰减常数 $\alpha$

$$\alpha = \text{Re}(\gamma) = \sqrt{\frac{1}{2}\left[\sqrt{(R^2+\omega^2L^2)(G^2+\omega^2C^2)} + (RG-\omega^2LC)\right]}$$

物理意义：表示波沿线传播时幅值的衰减程度，单位奈培/米（Np/m）。

对于无损线：$\alpha = 0$，波无衰减传播。

#### 相位常数 $\beta$

$$\beta = \text{Im}(\gamma) = \sqrt{\frac{1}{2}\left[\sqrt{(R^2+\omega^2L^2)(G^2+\omega^2C^2)} - (RG-\omega^2LC)\right]}$$

物理意义：表示波沿线传播时相位的变化率，单位弧度/米（rad/m）。

对于无损线：

$$\beta = \omega\sqrt{LC}$$

#### 传播常数的近似表达式

在工频（$\omega$ 较小）条件下，若 $R \ll \omega L$ 且 $G \ll \omega C$：

$$\alpha \approx \frac{R}{2}\sqrt{\frac{C}{L}} + \frac{G}{2}\sqrt{\frac{L}{C}}$$

$$\beta \approx \omega\sqrt{LC}\left(1 + \frac{R^2C-L^2G^2}{8\omega^2L^2C^2}\right) \approx \omega\sqrt{LC}$$

### 波速计算和物理意义

#### 相速度

$$v_p = \frac{\omega}{\beta} = \frac{\omega}{\text{Im}(\sqrt{(R+j\omega L)(G+j\omega C)})}$$

对于无损线：

$$v_p = \frac{1}{\sqrt{LC}}$$

对于架空线路：$v_p \approx 3 \times 10^8$ m/s（接近光速）

对于电缆线路：$v_p \approx 1.5 \sim 2.0 \times 10^8$ m/s（因绝缘介质介电常数较大）

#### 群速度

$$v_g = \frac{d\omega}{d\beta}$$

对于无色散线路（无损线），$v_g = v_p$。

#### 波长的计算

$$\lambda = \frac{v_p}{f} = \frac{2\pi}{\beta}$$

在工频50Hz下，架空线路波长约为6000km。

`wave-velocity` - 波速详解

## 行波解

### 达朗贝尔解

波动方程的通解（达朗贝尔解）为：

$$v(x,t) = v^+(x-v_pt) + v^-(x+v_pt)$$

$$i(x,t) = \frac{1}{Z_c}v^+(x-v_pt) - \frac{1}{Z_c}v^-(x+v_pt)$$

其中：
- $v^+(x-v_pt)$：正向行波（从源向负载传播）
- $v^-(x+v_pt)$：反向行波（从负载向源传播）

### 正向波与反向波的物理意义

#### 正向行波

$$v^+(x,t) = v^+(t - x/v_p)$$

特点：
- 波形的形状保持不变（无损线）
- 以速度 $v_p$ 向 $+x$ 方向传播
- 电压与电流比值恒为 $Z_c$
- 携带能量从源向负载传输

#### 反向行波

$$v^-(x,t) = v^-(t + x/v_p)$$

特点：
- 以速度 $v_p$ 向 $-x$ 方向传播
- 由负载端反射产生
- 电压与电流比值恒为 $-Z_c$
- 携带能量从负载向源返回

[[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]] - 行波详解

### 边界条件

#### 始端边界条件

$$v(0,t) = v_s(t) - Z_s i(0,t)$$

其中 $v_s(t)$ 为电源电压，$Z_s$ 为电源内阻。

#### 终端边界条件

$$v(l,t) = Z_L i(l,t)$$

其中 $Z_L$ 为负载阻抗，$l$ 为线路长度。

### 稳态解

对于正弦激励，稳态解为：

$$V(x) = V^+ e^{-\gamma x} + V^- e^{\gamma x}$$

由终端边界条件确定 $V^+$ 和 $V^-$：

$$\frac{V^-}{V^+} = \Gamma_L e^{-2\gamma l}$$

其中 $\Gamma_L$ 为终端反射系数。

## 反射与折射

### 反射系数的完整推导

在线路终端 $x=l$ 处：

$$V(l) = V^+ e^{-\gamma l} + V^- e^{\gamma l} = V_L$$
$$I(l) = \frac{V^+}{Z_c} e^{-\gamma l} - \frac{V^-}{Z_c} e^{\gamma l} = I_L$$

负载约束：$V_L = Z_L I_L$

解得终端电压：

$$V_L = V^+ e^{-\gamma l} (1 + \Gamma_L)$$

其中**终端反射系数**：

$$\Gamma_L = \frac{Z_L - Z_c}{Z_L + Z_c}$$

### 反射系数的物理意义

| 负载条件 | 反射系数 | 物理现象 |
|----------|----------|----------|
| 开路 ($Z_L = \infty$) | $\Gamma_L = 1$ | 全反射，电压加倍，电流为零 |
| 短路 ($Z_L = 0$) | $\Gamma_L = -1$ | 全反射，电流加倍，电压为零 |
| 匹配 ($Z_L = Z_c$) | $\Gamma_L = 0$ | 无反射，行波完全吸收 |
| 感性负载 | $|\Gamma_L| < 1$ | 部分反射，相位超前 |
| 容性负载 | $|\Gamma_L| < 1$ | 部分反射，相位滞后 |

### 折射系数（传输系数）

折射系数定义为折射波与入射波的比值：

$$\tau = 1 + \Gamma = \frac{2Z_L}{Z_L + Z_c}$$

当波从线路1（特性阻抗 $Z_{c1}$）进入线路2（特性阻抗 $Z_{c2}$）时：

$$\tau = \frac{2Z_{c2}}{Z_{c1} + Z_{c2}}$$

### 多次反射分析

对于有限长线，波在两端之间多次反射。第 $n$ 次反射后的电压：

$$v_n = v_0 \cdot \Gamma_S^{n/2} \cdot \Gamma_L^{n/2} \cdot (1 + \Gamma_L)$$

其中 $\Gamma_S$ 为始端反射系数。

`reflection-coefficient` - 反射系数详解

## 有损线分析

### 频变参数模型

实际输电线路的参数随频率变化：

#### 电阻的频率特性

由于集肤效应，交流电阻随频率增加：

$$R(f) = R_{dc} \cdot k_s(f)$$

集肤深度：

$$\delta = \sqrt{\frac{\rho}{\pi f \mu}}$$

对于圆导线：

$$k_s(f) \approx 1 + \frac{1}{3}\left(\frac{r}{\delta}\right)^2 \quad \text{（低频近似）}$$

#### 电感的频率特性

内电感受集肤效应影响：

$$L(f) = L_{ext} + L_{int}(f)$$

其中外电感 $L_{ext}$ 与频率无关，内电感 $L_{int}$ 随频率增加而减小。

`skin-effect` - 集肤效应详解

### 色散现象

由于参数随频率变化，不同频率分量以不同速度传播，导致波形畸变：

$$\beta(\omega) \approx \omega\sqrt{LC}\left(1 + \frac{R^2}{8\omega^2L^2}\right)$$

群速度色散：

$$D = \frac{d}{d\omega}\left(\frac{1}{v_g}\right) \neq 0$$

色散导致脉冲展宽，对于快速暂态分析必须考虑。

`dispersion` - 色散详解

### 频率相关线路模型

EMT仿真中的频变线路模型：

- [[frequency-dependent-line-model]] - 频变线路模型
- `jmarti-model` - J.Marti模型：基于特性阻抗和传播常数的有理函数拟合
- `noda-model` - Noda模型：相域直接建模
- [[phase-domain-modeling]] - 相域建模方法

## 多导体线路

### 多导体电报方程

对于 $n$ 相导体系统，电报方程扩展为矩阵形式：

$$-\frac{\partial [v]}{\partial x} = [R][i] + [L]\frac{\partial [i]}{\partial t}$$

$$-\frac{\partial [i]}{\partial x} = [G][v] + [C]\frac{\partial [v]}{\partial t}$$

其中 $[v]$、$[i]$ 为 $n \times 1$ 向量，$[R]$、$[L]$、$[G]$、$[C]$ 为 $n \times n$ 参数矩阵。

### 参数矩阵

#### 电阻矩阵

对角矩阵：

$$[R] = \text{diag}(R_1, R_2, \cdots, R_n)$$

#### 电感矩阵

$$L_{ii} = 2 \times 10^{-7} \ln\frac{2h_i}{r_i}$$
$$L_{ij} = 2 \times 10^{-7} \ln\frac{D_{ij}'}{D_{ij}}$$

其中 $D_{ij}'$ 为镜像间距。

#### 电容矩阵

$$[C] = 2\pi\varepsilon_0 [P]^{-1}$$

其中电位系数：

$$P_{ii} = \ln\frac{2h_i}{r_i}, \quad P_{ij} = \ln\frac{D_{ij}'}{D_{ij}}$$

### 模态分析

通过相似变换解耦：

$$[v] = [T_v][v_m], \quad [i] = [T_i][i_m]$$

模域电报方程：

$$-\frac{\partial [v_m]}{\partial x} = [R_m][i_m] + [L_m]\frac{\partial [i_m]}{\partial t}$$

其中 $[R_m] = [T_v]^{-1}[R][T_i]$，$[L_m] = [T_v]^{-1}[L][T_i]$ 为对角矩阵。

[[modal-transformation]] - 模态变换详解

### 串扰与耦合

#### 容性耦合

由线间电容引起，与频率成正比：

$$V_{coupled} = \frac{C_{12}}{C_{12} + C_{2g}} \cdot V_1$$

#### 感性耦合

由互感引起，与频率和负载阻抗有关：

$$V_{induced} = j\omega M_{12} \cdot I_1$$

`crosstalk` - 串扰详解

## 与集总参数模型的详细对比

### 模型适用范围

| 判据 | 集总参数模型 | 分布参数模型 |
|------|-------------|-------------|
| 线路长度 | $l < \lambda/20$ | $l \geq \lambda/20$ |
| 工频架空线（50Hz） | $l < 300$ km | $l \geq 300$ km |
| 工频电缆 | $l < 150$ km | $l \geq 150$ km |
| 雷电波（1MHz） | $l < 30$ m | $l \geq 30$ m |
| 开关操作（10kHz） | $l < 300$ m | $l \geq 300$ m |

### 数学模型对比

#### 集总参数模型

$$v(t) = Ri(t) + L\frac{di(t)}{dt}$$

常微分方程，瞬时响应。

#### 分布参数模型

$$\frac{\partial^2 v}{\partial x^2} = LC\frac{\partial^2 v}{\partial t^2} + (RC+LG)\frac{\partial v}{\partial t} + RGv$$

偏微分方程，需要考虑传播时延。

### 暂态响应对比

#### 集总参数模型响应

$$v(t) = V_0(1 - e^{-t/\tau})$$

指数型响应，无波过程。

#### 分布参数模型响应

$$v(t) = V_0 \cdot u(t - \tau_d) + \text{反射波叠加}$$

阶梯型响应，存在传播时延 $\tau_d = l/v_p$ 和多次反射。

[[distributed-parameter-model]] - 分布参数模型
[[lumped-parameter-model]] - 集总参数模型

## 在EMT仿真中的应用

### Bergeron模型

[[bergeron-line-model]] - Bergeron模型

基于特性阻抗和传播时延的集中参数等效：

$$i_k(t) = \frac{1}{Z_c}v_k(t) + I_k(t-\tau)$$

其中 $I_k(t-\tau)$ 为历史电流源。

适用条件：无损或低损耗线路。

### 频变模型

#### J.Marti模型

`jmarti-model` - J.Marti模型

将有理函数用于特性阻抗和传播常数的频域拟合：

$$Z_c(s) = Z_0 \frac{\prod_{i=1}^{n}(s+z_i)}{\prod_{j=1}^{n}(s+p_j)}$$

#### Noda模型

`noda-model` - Noda模型

直接在相域建立频变参数模型，使用卷积计算历史项。

### 相域建模

[[phase-domain-modeling]] - 相域建模

直接求解相域方程，考虑三相耦合：

$$\frac{d[v]}{dt} = [C]^{-1}\left(-[G][v] - \frac{\partial [i]}{\partial x}\right)$$

### 换位线路模型

`transposed-line-model` - 换位线路模型

对于完全换位线路，序阻抗矩阵为对角阵，可简化为正序、负序、零序分别计算。

## 相关方法

- [[transmission-line-model]] - 输电线路模型
- [[distributed-parameter-model]] - 分布参数模型
- [[lumped-parameter-model]] - 集总参数模型
- [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-]] - 波传播
- [[frequency-dependent-line-model]] - 频变线路模型
- [[modal-transformation]] - 模态变换
- `characteristic-impedance` - 特性阻抗
- `reflection-coefficient` - 反射系数
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]] - 行波
- `wave-velocity` - 波速

## 来源论文

参见 [[index.md]] 获取更多传输线理论相关文献。

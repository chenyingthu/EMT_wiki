---
title: "集总参数模型 (Lumped Parameter Model)"
type: method
tags: [lumped-parameter, pi-model, equivalent-circuit, short-line, medium-line, long-line, transmission-line]
created: "2026-05-02"
---

# 集总参数模型 (Lumped Parameter Model)

## 概述

集总参数模型是将分布参数的输电线路或电缆简化为集中参数的等效电路模型。当线路长度较短（相对于波长）时，集总参数模型能够准确描述线路的电气特性，同时大大降低计算复杂度，广泛应用于电力系统稳态分析和暂态仿真。

与[[distributed-parameter-model]]相比，集总参数模型将线路的电阻、电感、电导和电容视为集中在特定位置的元件，而非沿线路连续分布。这种简化在工程精度要求范围内可接受的情况下，显著提高了计算效率。

## 理论基础

### 分布参数vs集总参数

实际输电线路的电气参数（电阻$r$、电感$L$、电导$g$、电容$C$）是沿线路连续分布的。对于均匀传输线，单位长度的参数为常数，线路特性由以下偏微分方程描述：

$$\frac{\partial v}{\partial x} = -ri - L\frac{\partial i}{\partial t}$$

$$\frac{\partial i}{\partial x} = -gv - C\frac{\partial v}{\partial t}$$

这些电报方程描述了电压和电流沿线路的传播特性，其解涉及行波概念。

集总参数模型的核心思想是：当线路尺寸远小于信号波长时，可以忽略线路上的波过程，将分布参数等效为集中元件。这种近似的物理基础是准静态电磁场理论。

### 适用条件的理论推导

电磁波的传播速度在架空线中接近光速：

$$v = \frac{1}{\sqrt{LC}} \approx \frac{1}{\sqrt{\mu_0\varepsilon_0}} = c \approx 3 \times 10^8 \text{ m/s}$$

对于频率为$f$的信号，波长为：

$$\lambda = \frac{v}{f}$$

集总参数近似有效的条件是线路长度$L$满足：

$$L < \frac{\lambda}{10}$$

或等效表示为：

$$\frac{\omega L}{v} < \frac{\pi}{5} \approx 0.628$$

其中$\omega = 2\pi f$为角频率。

这个判据的物理意义是：当电磁波在线路上传播的时间$t = L/v$远小于信号周期$T = 1/f$时，可以认为电压和电流在某一时刻沿线路近似均匀分布，从而采用集总参数近似。

### 详细的长度判据和波长关系

#### 不同频率下的适用长度

| 频率 | 波长 | 适用长度（$<\lambda/10$） |
|------|------|---------------------------|
| 50 Hz | 6000 km | < 600 km |
| 60 Hz | 5000 km | < 500 km |
| 1 kHz | 300 km | < 30 km |
| 10 kHz | 30 km | < 3 km |
| 100 kHz | 3 km | < 300 m |
| 1 MHz | 300 m | < 30 m |

#### 相位变化判据

从相位角度，集总参数模型适用的条件是线路上的相位变化小于约36°：

$$\beta L < \frac{\pi}{5}$$

其中$\beta = \omega/v$为相位常数。当$\beta L = \pi/5$时，线路始端和末端的相位差约为36°，这通常被视为集总参数近似的上限。

## 模型类型与详细推导

### 短线路模型（Short-Line Model）

#### 适用条件
- 线路长度：$L < 80$ km（架空线）
- 电压等级：通常用于配电线路
- 频率：工频（50/60 Hz）

#### 模型假设
对于短线路，可以做出以下合理假设：
1. 线路电容效应可忽略（充电电流很小）
2. 电导可忽略（$g \approx 0$，绝缘良好）
3. 参数均匀分布可等效为集中参数

#### R-L串联模型的完整推导

设线路单位长度电阻为$r$（Ω/km），单位长度电感为$l$（H/km），线路总长度为$L$（km）。

总串联阻抗为：

$$Z = R + jX_L = rL + j\omega lL$$

其中：
- $R = rL$：总电阻（Ω）
- $X_L = \omega lL$：总感抗（Ω）
- $\omega = 2\pi f$：角频率（rad/s）

等效电路为简单的串联R-L电路，送端电压$\dot{V}_S$和受端电压$\dot{V}_R$的关系为：

$$\dot{V}_S = \dot{V}_R + Z\dot{I}_R$$

其中$\dot{I}_R$为受端电流。

#### 忽略电纳的条件分析

充电无功功率与传输功率的比值决定了是否可以忽略电纳：

$$\frac{Q_C}{P} = \frac{\omega C L V^2}{P}$$

对于短线路，这个比值通常小于5%，因此可以忽略电容效应。具体判据为：

$$\omega C L \cdot V_{nom}^2 < 0.05 S_{nom}$$

其中$V_{nom}$为额定电压，$S_{nom}$为额定视在功率。

### 中距离线路模型（Medium-Line Model）

#### 适用条件
- 线路长度：80 km $< L <$ 250 km（架空线）
- 电压等级：110 kV及以上输电线路
- 必须考虑电容效应

#### π型等效电路的详细推导

对于中等长度线路，电容效应不可忽略，但长线路的修正因子接近1，可以采用标准π型等效。

**串联支路：**

总串联阻抗：

$$Z = (r + j\omega l)L = R + jX_L$$

**并联支路：**

总并联电纳（容纳）：

$$Y = j\omega cL = jB_C$$

其中$c$为单位长度电容（F/km）。

在π型等效中，总电纳平分在两端：

$$\frac{Y}{2} = \frac{j\omega cL}{2} = \frac{jB_C}{2}$$

#### 参数计算与等效电路方程

π型等效的ABCD参数为：

$$\begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} 1 + \frac{YZ}{2} & Z \\ Y\left(1 + \frac{YZ}{4}\right) & 1 + \frac{YZ}{2} \end{bmatrix}$$

电压和电流的传输方程：

$$\begin{bmatrix} \dot{V}_S \\ \dot{I}_S \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} \dot{V}_R \\ \dot{I}_R \end{bmatrix}$$

### 长线路模型（Long-Line Model）

#### 适用条件
- 线路长度：$L > 250$ km（架空线）
- 电压等级：通常220 kV及以上远距离输电
- 必须采用修正参数的等效π型

#### 分布参数方程的解

均匀传输线的电压和电流分布满足：

$$\dot{V}(x) = \dot{V}_R \cosh(\gamma x) + Z_c \dot{I}_R \sinh(\gamma x)$$

$$\dot{I}(x) = \frac{\dot{V}_R}{Z_c} \sinh(\gamma x) + \dot{I}_R \cosh(\gamma x)$$

其中：
- $\gamma = \sqrt{ZY} = \alpha + j\beta$：传播常数
- $Z_c = \sqrt{Z/Y}$：特性阻抗（波阻抗）
- $x$：距受端的距离

#### 特性阻抗与传播常数

**特性阻抗（ surge impedance ）：**

$$Z_c = \sqrt{\frac{r + j\omega l}{g + j\omega c}}$$

对于无损线路（$r = 0, g = 0$）：

$$Z_c = \sqrt{\frac{l}{c}}$$

典型值：架空线约300-400 Ω，电缆约30-50 Ω。

**传播常数：**

$$\gamma = \sqrt{(r + j\omega l)(g + j\omega c)} = \alpha + j\beta$$

其中：
- $\alpha$：衰减常数（Np/km），决定幅值衰减
- $\beta$：相位常数（rad/km），决定相位变化

#### 长线路等效π型的修正参数推导

将分布参数等效为π型电路，需要修正串联阻抗和并联导纳。

**修正串联阻抗：**

$$Z' = Z_c \sinh(\gamma L) = Z \cdot \frac{\sinh(\gamma L)}{\gamma L}$$

**修正并联导纳（每侧）：**

$$\frac{Y'}{2} = \frac{1}{Z_c} \tanh\left(\frac{\gamma L}{2}\right) = \frac{Y}{2} \cdot \frac{\tanh(\gamma L/2)}{\gamma L/2}$$

**修正系数的物理意义：**

定义串联修正系数：

$$K_Z = \frac{\sinh(\gamma L)}{\gamma L}$$

定义并联修正系数：

$$K_Y = \frac{\tanh(\gamma L/2)}{\gamma L/2}$$

当$|\gamma L| < 0.1$时，$K_Z \approx 1$，$K_Y \approx 1$，即退化为中距离线路模型。

#### 等效π型的ABCD参数

长线路等效π型的传输参数为：

$$A = D = \cosh(\gamma L)$$

$$B = Z_c \sinh(\gamma L) = Z'$$

$$C = \frac{\sinh(\gamma L)}{Z_c}$$

验证：$AD - BC = \cosh^2(\gamma L) - \sinh^2(\gamma L) = 1$（满足互易条件）

## π型等效电路的参数计算公式

### 通用计算公式

对于长度为$L$的均匀传输线：

**单位长度参数：**
- $Z = r + j\omega l$：单位长度串联阻抗（Ω/km）
- $Y = g + j\omega c$：单位长度并联导纳（S/km）

**等效π型参数：**

$$Z' = \sqrt{\frac{Z}{Y}} \sinh\left(\sqrt{ZY} \cdot L\right)$$

$$\frac{Y'}{2} = \sqrt{\frac{Y}{Z}} \tanh\left(\frac{\sqrt{ZY} \cdot L}{2}\right)$$

### 简化计算条件

当$|\gamma L| < 0.1$时，可以使用泰勒展开近似：

$$\sinh(x) \approx x + \frac{x^3}{6}$$

$$\tanh(x) \approx x - \frac{x^3}{3}$$

代入后得到简化公式：

**修正串联阻抗：**

$$Z' \approx ZL\left(1 + \frac{(\gamma L)^2}{6}\right)$$

**修正并联导纳：**

$$\frac{Y'}{2} \approx \frac{YL}{2}\left(1 - \frac{(\gamma L)^2}{12}\right)$$

**进一步简化（当$|\gamma L| \ll 0.1$）：**

$$Z' \approx ZL = R + jX_L$$

$$\frac{Y'}{2} \approx \frac{YL}{2} = \frac{jB_C}{2}$$

这就是中距离线路的π型等效。

### 数值计算注意事项

1. 双曲函数计算：对于高频或大长度，$\gamma L$可能较大，需要使用精确的双曲函数计算
2. 数值稳定性：当$|\gamma L|$很小时，直接使用简化公式避免数值误差
3. 复数运算：所有参数计算涉及复数运算，注意实部和虚部的处理

## 与分布参数模型的详细对比

| 特性 | 集总参数模型 | 分布参数模型 |
|------|--------------|--------------|
| 数学描述 | 常微分方程/代数方程 | 偏微分方程（电报方程） |
| 参数特性 | 集中元件R、L、C | 单位长度参数$r$、$l$、$g$、$c$ |
| 波过程 | 无法模拟 | 准确模拟行波传播 |
| 谐振特性 | 单一谐振频率 | 多谐振点（$f_n = nv/2L$） |
| 计算复杂度 | 低（代数运算） | 高（涉及双曲函数/贝塞尔函数） |
| 暂态仿真 | 简单，大步长 | 复杂，需小步长 |
| 频率范围 | 低频/工频准确 | 全频率范围准确 |
| 过电压计算 | 无法计算行波过电压 | 准确计算操作过电压 |
| 适用长度 | 短/中等线路 | 长线路/电缆/高频 |

### 精度对比分析

**工频（50/60 Hz）下不同长度线路的模型误差：**

| 线路长度 | 短线路模型误差 | 中距离模型误差 | 长线路模型误差 |
|----------|----------------|----------------|----------------|
| < 50 km | < 1% | < 0.5% | < 0.1% |
| 50-100 km | 2-5% | < 1% | < 0.2% |
| 100-300 km | > 5% | 1-3% | < 0.5% |
| > 300 km | 不适用 | 3-8% | < 1% |

## EMT仿真中的应用

### 伴随模型（Companion Model）

在EMT仿真中，集总参数线路模型通常采用伴随模型实现。以[[trapezoidal-rule]]为例：

**R-L串联支路的伴随模型：**

离散化后的等效电导：

$$G_{eq} = \frac{\Delta t}{2L + R\Delta t}$$

历史电流源：

$$I_{history}(t) = I_{history}(t-\Delta t) + G_{eq}[v(t-\Delta t) + v(t-2\Delta t)]$$

**π型等效的伴随模型：**

每个π型支路（串联和并联）都转换为等效电导并联历史电流源的形式，便于节点分析。

### 状态空间表示

集总参数模型可以表示为状态空间形式：

$$\dot{x} = Ax + Bu$$

$$y = Cx + Du$$

对于R-L串联电路：

状态变量：$x = i$（电感电流）

$$L\frac{di}{dt} = -Ri + v$$

$$\frac{di}{dt} = -\frac{R}{L}i + \frac{1}{L}v$$

其中：$A = -R/L$，$B = 1/L$

对于π型等效，状态变量包括电感电流和电容电压，形成多阶状态方程。

### 多段π型模型（Multi-π Model）

对于长线路，可以采用多段π型串联提高精度：

**分段原则：**
- 每段长度：通常10-20 km
- 总段数：$N = L / \Delta L$
- 每段采用标准π型等效

**等效参数（每段）：**

$$Z_{segment} = \frac{Z'}{N}$$

$$\frac{Y_{segment}}{2} = \frac{Y'}{2N}$$

**精度优势：**
- 可以近似模拟行波传播
- 每段内部集总参数近似误差小
- 适合暂态过电压计算

与[[bergeron-line-model]]相比，多段π型在频率相关参数建模上更具灵活性。

## 特殊考虑

### 频率相关参数

实际线路参数具有频率相关性：

**集肤效应导致的电阻增加：**

$$r(f) = r_{DC}\sqrt{\frac{f}{f_{base}}}$$

**地回路影响的电感变化：**

$$l(f) = l_{internal} + l_{external}(f)$$

对于宽频EMT仿真，需要考虑：
- `skin-effect`模型
- [[frequency-dependent-line-model]]
- 使用[[vector-fitting]]进行频域参数辨识

### 三相模型

实际输电线路为三相系统，存在相间耦合：

**阻抗矩阵：**

$$\mathbf{Z} = \begin{bmatrix} Z_s & Z_m & Z_m \\ Z_m & Z_s & Z_m \\ Z_m & Z_m & Z_s \end{bmatrix}$$

**导纳矩阵：**

$$\mathbf{Y} = \begin{bmatrix} Y_s & Y_m & Y_m \\ Y_m & Y_s & Y_m \\ Y_m & Y_m & Y_s \end{bmatrix}$$

其中：
- $Z_s$：自阻抗
- $Z_m$：互阻抗
- 考虑`mutual-inductance`耦合

**对称分量变换：**

通过对称分量变换（Clarke/Park变换），可将耦合三相系统解耦为独立的零序、正序、负序网络。

对于`transposed-line`，三相参数对称，模型可简化。

### 变压器模型中的集总参数

[[transformer-model]]广泛采用集总参数：

**双绕组变压器等效电路：**

- **串联支路**：$R_{eq} + jX_{eq}$（归算到一侧的漏阻抗）
- **并联支路**：$R_c$（铁损等效电阻）// $jX_m$（励磁电抗）

**三绕组变压器：**

采用三绕组等效电路，每对绕组之间有独立的漏阻抗。

集总参数假设在变压器建模中非常准确，因为变压器尺寸远小于工频波长。

### 误差分析

**集总参数模型的主要误差来源：**

1. **相位误差**
   - 来源：忽略行波传播时间
   - 大小：约$\beta L / 2$弧度
   - 影响：稳态功角计算偏差

2. **幅值误差**
   - 来源：忽略分布电容的精确分布效应
   - 大小：高频时显著增大
   - 影响：过电压计算偏低

3. **谐振频率误差**
   - 来源：无法模拟多谐振点
   - 影响：谐振过电压分析失效

**误差修正方法：**

- 使用修正参数（长线路模型）
- 采用多段π型等效
- 对于关键计算，切换到[[distributed-parameter-model]]

## 工程应用指南

### 模型选择决策流程

```
线路长度？
├── < 80 km → 短线路模型（R-L串联）
├── 80-250 km → 中距离π型模型
└── > 250 km → 长线路等效π型或多段π型

频率范围？
├── 工频（50/60 Hz）→ 标准集总参数
├── 谐波（< 2 kHz）→ 集总参数（检查适用性）
└── 开关暂态（> 1 kHz）→ 考虑分布参数或多段π型

精度要求？
├── 稳态潮流计算 → 集总参数足够
├── 操作过电压 → 多段π型或分布参数
└── 雷电过电压 → 必须分布参数模型
```

### 典型参数参考值

**架空线路（单导线，50 Hz）：**

| 电压等级 | $r$ (Ω/km) | $l$ (mH/km) | $c$ (nF/km) |
|----------|------------|-------------|-------------|
| 110 kV | 0.13 | 1.35 | 8.5 |
| 220 kV | 0.08 | 1.30 | 9.0 |
| 500 kV | 0.02 | 0.85 | 13.5 |

**电缆线路（典型值）：**

| 电压等级 | $r$ (Ω/km) | $l$ (mH/km) | $c$ (nF/km) |
|----------|------------|-------------|-------------|
| 10 kV | 0.20 | 0.35 | 250 |
| 110 kV | 0.06 | 0.40 | 200 |
| 220 kV | 0.03 | 0.35 | 180 |

## 相关模型与链接

### 密切相关的模型
- [[distributed-parameter-model]] - 分布参数模型
- `pi-equivalent` - π型等效
- [[bergeron-line-model]] - Bergeron行波模型
- [[frequency-dependent-line-model]] - 频变线路模型

### 相关的数值方法
- [[companion-model]] - 伴随模型
- [[trapezoidal-rule]] - 梯形积分法则
- [[state-space-method]] - 状态空间法
- [[nodal-analysis]] - 节点分析法

### 相关的EMT主题
- [[transmission-line-model]] - 输电线路模型
- [[transformer-model]] - 变压器模型
- [[cable-model]] - 电缆模型
- `skin-effect` - 集肤效应
- `mutual-inductance` - 互感

## 来源论文

参见 [[index.md]] 获取更多中集总参数模型相关文献。

## 参考标准

- IEC 60909: 短路电流计算
- IEEE Std 738: 架空线路载流量计算
- CIGRE Technical Brochure 604: 输电线路建模指南

---

*本文档遵循 Karpathy LLM Wiki Pattern，用于电力系统EMT仿真领域知识管理*

---
title: "傅里叶级数展开 (Fourier Series Expansion)"
type: method
tags: [fourier-series, harmonic, frequency-domain, decomposition, periodic-signal, trigonometric-series]
created: "2026-05-02"
updated: "2026-05-16"
---

# 傅里叶级数展开 (Fourier Series Expansion)

## 定义

傅里叶级数展开是把周期信号表示为直流分量、基波分量和整数倍基波频率谐波分量之和的数学工具。对周期为 $T$、基波角频率 $\omega_0 = 2\pi/T$ 的信号 $x(t)$，三角形式为：

$$x(t) = a_0 + \sum_{h=1}^{H}\left[a_h\cos(h\omega_0 t) + b_h\sin(h\omega_0 t)\right]$$

其中 $H$ 是分析时保留的最高谐波阶次。复指数形式更适合与动态相量、谐波状态空间和频域网络方程衔接：

$$x(t) = \sum_{h=-H}^{H} X_h e^{jh\omega_0 t}, \quad X_h = \frac{1}{T}\int_0^T x(t)e^{-jh\omega_0 t}\,dt$$

三角形式系数与复指数形式系数的关系为：$X_0 = a_0$，当 $h>0$ 时 $X_h = (a_h - jb_h)/2$，$X_{-h} = (a_h + jb_h)/2$。

该方法适合描述周期或准周期稳态波形；若信号包含故障初始直流偏置、非周期陡波、频率漂移或明显时变包络，应转向 [[fft]]（离散频谱计算）、[[fourier-filtering]]（滤波提取）或 [[dynamic-phasor]]（时变相量）分析。

## EMT 中的角色

在 EMT 知识网络中，傅里叶级数承担三类核心角色：

1. **[[harmonic-analysis]] 的数学底座**：将电压、电流、开关函数或控制量分解为各次谐波分量，为谐波阻抗扫描和交互作用分析提供频率域表示。
2. **电力电子波形建模工具**：用少量低阶系数描述近周期 PWM 波形，支撑平均值模型（AVM）、广义状态空间平均模型（GSSA）和谐波相量模型的构建与验证。
3. **结果解释语言**：将 EMT 波形中的畸变、谐振和互调现象转化为可比较的频率分量，便于量化评估和跨仿真工具验证。

## 核心机制

### 正交积分公式

若信号在一个周期 $[0,T]$ 内可积并满足分段连续条件，系数由正交积分得到：

直流分量：
$$a_0 = \frac{1}{T}\int_0^T x(t)\,dt$$

交流分量（三角形式）：
$$a_h = \frac{2}{T}\int_0^T x(t)\cos(h\omega_0 t)\,dt, \quad b_h = \frac{2}{T}\int_0^T x(t)\sin(h\omega_0 t)\,dt$$

复指数形式系数：
$$X_h = \frac{1}{T}\int_0^T x(t)e^{-jh\omega_0 t}\,dt, \quad h = 0, \pm 1, \pm 2, \ldots$$

正交性来源于：$\int_0^T e^{j(h-k)\omega_0 t}\,dt = T\delta_{hk}$（克罗内克 delta）。

### 截断误差与帕塞瓦尔定理

保留 $H$ 阶截断时，均方误差为：
$$\varepsilon_H^2 = \frac{1}{T}\int_0^T\left|x(t) - \sum_{h=-H}^{H}X_h e^{jh\omega_0 t}\right|^2 dt = \sum_{|h|>H}|X_h|^2$$

由帕塞瓦尔定理，总功率等于各谐波分量功率之和：
$$\frac{1}{T}\int_0^T |x(t)|^2\,dt = \sum_{h=-\infty}^{\infty}|X_h|^2$$

因此，截断误差由 $|h|>H$ 的谐波功率之和界定。这说明谐波幅值 $|X_h|$ 随 $h$ 增大而衰减越快，有限阶截断的误差越小。

### 常见周期波形举例

**纯正弦波** $x(t) = A\cos(\omega_0 t + \varphi)$ 的傅里叶系数只有 $h = \pm 1$ 两项，其余为零。**对称方波**（$50\%$ 占空比）只含奇次谐波，系数为 $b_h = 0$，$a_h = 0$（$h$ 偶），$a_h = 4A/(h\pi)$（$h$ 奇）。**六脉波换流器**特征谐波为 $6k \pm 1$ 次（$k \in \mathbb{N}$），这是傅里叶级数在换相过程分析中的直接应用。

## 分类与变体

| 用法 | 输入 | 输出 | 适合场景 | 主要风险 |
|------|------|------|----------|----------|
| 稳态谐波分解 | 一个或多个周期的波形 | $a_h, b_h$ 或 $X_h$ | 周期稳态、畸变评估 | 对非整周期窗口敏感，频谱泄漏 |
| 开关函数展开 | PWM 或换流器开关函数 | 谐波系数或调制相关项 | 平均模型、GSSA、谐波相量模型 | 调制策略变化会改变系数，需要重新计算 |
| 截断重构 | 有限阶谐波系数 | 近似时域波形 | 低阶谐波保留、模型降阶 | 高频纹波和陡变可能丢失 |
| 动态相量扩展 | 滑动窗口内的时变系数 | 慢变复包络 | 多时间尺度仿真、协同仿真 | 窗长和频率参考影响结果精度 |

## 形式化表达

### DFT/FFT 的离散化关系

在 EMT 数值仿真中，连续傅里叶级数需要离散化。一个周期内等间隔采样 $N$ 点（采样周期 $\Delta t = T/N$），离散傅里叶变换（DFT）定义为：

$$X_k = \sum_{n=0}^{N-1} x_n e^{-j2\pi kn/N}, \quad k = 0, 1, \ldots, N-1$$

其中 $x_n = x(n\Delta t)$。当 $x(t)$ 是有限阶谐波合成时，DFT 的前 $H$ 个系数与连续傅里叶系数满足 $X_h = N \cdot X_h^{\text{cont}}$（离散与连续的缩放关系取决于归一化约定）。快速傅里叶变换（[[fft]]）是 DFT 的 $O(N\log N)$ 高效算法实现。

### 谐波阻抗网络

在谐波分析中，每次谐波 $h$ 对应一个独立的频域网络：
$$I_h = Y_h V_h$$

其中 $Y_h$ 是第 $h$ 次谐波的节点导纳矩阵。[[harmonic-analysis]] 基于此将系统响应分解为各次谐波的叠加。[[harmonic-interaction]] 研究不同设备之间通过耦合阻抗传递谐波分量的机制。

## 关键技术挑战

### 1. 频谱泄漏与窗函数选择

非整周期截断（信号不是正好 $T$ 的整数倍）会导致频谱从正确频率泄漏到相邻频率 bins。解决方法包括：

- **Hanning 窗**：$w_n = 0.5(1-\cos(2\pi n/N))$，旁瓣较低但主瓣加宽
- **Hamming 窗**：$w_n = 0.54 - 0.46\cos(2\pi n/N)$，比 Hanning 稍强的主瓣抑制
- **矩形窗**（不加窗）：主瓣最窄但旁瓣最高，频谱泄漏最严重

窗函数的选择是频率分辨率与泄漏抑制之间的权衡。

### 2. Gibbs 振荡现象

有限阶截断在信号不连续点附近产生过冲振荡，峰值约为跳变幅度的 $9\%$ 且不随 $H$ 增大而消除（只压缩振荡区域）。Shi 等 2021 的研究表明：时域线性中点插值等效于在频域乘余弦窗 $\cos(\pi\omega/(2\omega_{\max}))$，重复 $n$ 次插值等效于 $[G_{\cos}(\omega)]^n$，可用于抑制 Gibbs 振荡而不改变原始频域积分模块。

### 3. 时变谐波的滑动窗口跟踪

动态相量方法将时变系数理解为滑动窗口内的局部傅里叶变换：

$$X_h(t_0) = \frac{1}{T}\int_{t_0-T/2}^{t_0+T/2} x(t)w(t_0-t)e^{-jh\omega_0 t}\,dt$$

其中 $w(t)$ 是窗函数。窗长 $T$ 决定了对基波包络的跟踪速度——窗越短，时间分辨率越高但频率分辨率越低。

### 4. 非线性元件的谐波耦合

非线性元件（如饱和变压器、铁磁谐振器件）会将不同谐波相互耦合，使得 $h$ 次谐波激励产生的响应不局限于同一频率分量。处理方法包括：

- **谐波域 Norton 等值**：在工作点附近线性化，构造 $I_h = Y_h V_h$ 耦合矩阵
- **时域仿真 + 周期稳态迭代**：对非线性部分在时域仿真，用周期稳态混合方法（[[computation-of-the-periodic-steady-state-in-systems-with-nonlinear-components-us]]）求解

### 5. 谐波阻抗的网络传播

谐波分量注入网络后，通过节点导纳矩阵 $Y_h$ 传播到其他母线。[[harmonic-transfer-coefficient]] 描述指定注入点与关注点之间的谐波传递关系，是谐波滤波器设计和谐波放大评估的基础。

## 量化性能边界

| 指标 | 典型数据 | 来源 |
|------|----------|------|
| 六脉波换流器 THD | 约 $30\%$（特征谐波 $5,7,11,13$ 次为主） | 行业标准经验值 |
| PWM 逆变器 5 次谐波含量 | 约 $2\text{-}5\%$（取决于调制比 $m_a$） | IEEE 519 |
| 有限阶截断 Gibbs 过冲 | 跳变幅值的 $\approx 9\%$，不随 $H$ 增大而消除 | 理论已知 |
| 周期稳态混合方法收敛迭代次数 | 通常 $5\text{-}15$ 次（极限环外推加速） | [[computation-of-the-periodic-steady-state-in-systems-with-nonlinear-components-us]] |
| 滑动窗口动态相量 Gibbs 抑制（余弦窗，$n=2$） | 振荡过冲降低约 $50\%$ | Shi 等 2021 数值验证 |

## 适用边界与选择指南

### 何时使用傅里叶级数

- **适用**：周期或准周期稳态分析；PWM 开关函数展开；[[harmonic-analysis]]；周期稳态初始化（EMT 开机无需长时暂态积分）；电力电子平均值模型构建；[[fourier-filtering]] 的理论基础。
- **不适用**：单次故障暂态、雷电波、断路器重燃等非周期现象；频率漂移或调频过程（非整数倍基频）；需要实时处理且步长受限的场景。

### 傅里叶级数 vs [[fft]] vs [[dynamic-phasor]] vs [[fourier-filtering]]

| 特性 | 傅里叶级数 | FFT | 动态相量 | 傅里叶滤波 |
|------|-----------|-----|----------|-----------|
| 信号类型 | 连续周期 | 离散序列 | 滑动窗口时变相量 | 任意采样信号 |
| 时变系数 | 否（整周期平均） | 否 | 是 | 提取后滤波分量 |
| 计算域 | 连续积分 | 离散求和 | 滑动窗口积分 | 离散滤波 |
| 典型步长 | 不适用（分析工具） | $N\log N$ 每帧 | 窗口长度 $T$ | 每采样点 $O(1)\text{-}O(N)$ |
| 频率分辨率 | $1/T$（基频分辨） | $f_s/N$ | $1/T$（窗长决定） | 取决于滤波器设计 |
| 主要应用 | 谐波分解、波形建模 | 频谱分析、后处理 | 多速率仿真、协同仿真 | 提取/抑制指定频率 |

**选择决策**：若目标是分析已知周期波形并提取谐波幅值相位，用傅里叶级数；若目标是实时处理采样序列，用 FFT；若目标是在 EMT/TS 混合仿真中保留慢变包络，用动态相量；若目标是从采样波形中提取或抑制特定频率分量，用傅里叶滤波。

## 相关方法

- [[fft]] 是离散序列上计算频谱的算法；傅里叶级数是连续周期信号分解的理论框架，二者通过采样定理联系。
- [[fourier-filtering]] 关注从采样波形中提取或抑制目标频率分量，其滤波器设计以离散傅里叶变换为基础。
- [[harmonic-analysis]] 建立在傅里叶级数分解之上，将 EMT 响应按谐波次数组织分析。
- [[harmonic-transfer-coefficient]] 描述谐波分量在网络中的传播关系，是傅里叶系数在网络方程中的具体应用。
- [[harmonic-interaction]] 关注不同设备、网络阻抗和控制环节之间的耦合反馈，核心是谐波域的互导纳耦合矩阵。
- [[dynamic-phasor]] 可理解为时变傅里叶系数在 EMT/相量混合仿真中的扩展——滑动窗口取代整周期窗，使系数随时间慢变。
- [[average-value-model]] 利用傅里叶级数将 PWM 波形展开后取基波分量，实现逆变器的大步长等效。
- [[state-space-average-method]] 用傅里叶级数的低阶截断近似描述电力电子变换器的时域动态。

## 来源论文

- [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] — 澄清动态相量（时变傅里叶系数）在 EMT 中的有效性与局限性，指出大步长 DP 收益只对频移后分量成立
- [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy]] — 将谐波相量域（HPD）协同仿真扩展到宽频谐波交互分析，是傅里叶级数在多换流器系统中的具体应用框架
- [[computation-of-the-periodic-steady-state-in-systems-with-nonlinear-components-us]] — 用傅里叶系数描述非线性元件的周期稳态，混合频域线性网络与时域非线性仿真
- [[a-study-on-interpolation-and-weighting-function-for-numerical-fourier-transform]] — 揭示 Gibbs 振荡与频域截断窗的对应关系，时域余弦窗插值等效于频域加权抑制
- [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti]] — 将 PWM 波形分段后用傅里叶系数描述，支撑高效 EMT 变流器平均模型
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]] — 用正负序和谐波分量描述 LCC 平均值模型，说明傅里叶系数与换流器波形重构的关系
- [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte]] — 展示滑动窗口傅里叶系数在多时间尺度接口中的用法
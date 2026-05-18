---
title: "希尔伯特变换 (Hilbert Transform)"
type: method
tags: [hilbert-transform, signal-processing, analytic-signal, envelope-detection, instantaneous-frequency, shifted-frequency]
created: "2026-05-04"
updated: "2026-05-18"
---

# 希尔伯特变换 (Hilbert Transform)

## 定义与物理意义

希尔伯特变换（Hilbert Transform）是一种将实信号转换为解析信号（analytic signal）的线性时不变算子，通过引入 $90^\circ$ 相移产生信号的正交分量。对于输入实信号 $x(t)$，其希尔伯特变换记为 $\hat{x}(t)$ 或 $\mathcal{H}\{x(t)\}$。

### 时域定义

$$\hat{x}(t) = x(t) * \frac{1}{\pi t} = \frac{1}{\pi}\int_{-\infty}^{\infty}\frac{x(\tau)}{t-\tau}\,d\tau$$

其中 $\frac{1}{\pi t}$ 称为希尔伯特核（Hilbert kernel）。该核在奇点 $t=0$ 处按柯西主值（Cauchy principal value）积分定义。

### 频域定义

频域中，希尔伯特变换等价于将信号频谱的负频率分量乘以 $+1$，正频率分量乘以 $-1$：

$$\mathcal{F}\{\hat{x}(t)\} = -j\cdot\text{sgn}(\omega)\cdot X(\omega)$$

其中符号函数的定义：

$$\text{sgn}(\omega) = \begin{cases} +1, & \omega > 0 \\ 0, & \omega = 0 \\ -1, & \omega < 0 \end{cases}$$

由此可知，希尔伯特变换的幅频响应为全通（$|H(\omega)|=1$），相频响应为 $-90^\circ$（正频率）或 $+90^\circ$（负频率）。

## 解析信号构造

### 复解析信号定义

原始实信号与其希尔伯特变换构成解析信号：

$$z(t) = x(t) + j\hat{x}(t) = A(t)\,e^{j\phi(t)}$$

解析信号的瞬时特征定义为：

- **瞬时幅值**（包络）：$\displaystyle A(t) = |z(t)| = \sqrt{x^2(t) + \hat{x}^2(t)}$
- **瞬时相位**（相位）：$\displaystyle \phi(t) = \arg[z(t)] = \arctan\frac{\hat{x}(t)}{x(t)}$
- **瞬时频率**：$\displaystyle \omega(t) = \frac{d\phi(t)}{dt}$

### Bedrosian 恒等式

对于窄带信号 $x(t) = m(t)\cos\phi(t)$，若包络 $m(t)$ 与载波 $\cos\phi(t)$ 的频谱不重叠（即 $m(t)$ 的最高频率远低于 $\cos\phi(t)$ 的频率），则：

$$\mathcal{H}\{m(t)\cos\phi(t)\} = m(t)\sin\phi(t)$$

这意味着希尔伯特变换仅作用于载波分量，不影响包络。该恒等式是希尔伯特变换在包络检测中应用的理论基础。

### 解析信号的频谱特性

解析信号仅含正频率分量（单边谱），这使得采样率降至两倍（复信号采样率等于实信号采样率）：

$$Z(\omega) = \begin{cases} 2X(\omega), & \omega > 0 \\ X(0), & \omega = 0 \\ 0, & \omega < 0 \end{cases}$$

## 离散希尔伯特变换

### FIR 滤波器近似

实际计算中，有限长单位脉冲响应（FIR）滤波器对理想希尔伯特变换进行截断近似。设滤波器长度为 $N$（$N$ 为奇数），单位脉冲响应为：

$$h[n] = \frac{2}{\pi n}\sin^2\!\left(\frac{\pi n}{2}\right), \quad n \neq 0$$

$$h[0] = 0$$

对于长度 $N=2M+1$ 的滤波器，其频率响应近似为：

$$H(e^{j\omega}) \approx \begin{cases} -j, & 0 < \omega < \pi \\ j, & -\pi < \omega < 0 \end{cases}$$

### 高通移相器结构

离散希尔伯特变换也可通过离散傅里叶变换（DFT）实现：先将信号延长至 $2N$ 点，在正频率部分设置 $+j$，负频率部分设置 $-j$，再经逆变换还原。这种方法在频域滤波中应用广泛。

### 滤波器设计约束

实际 FIR 希尔伯特变换滤波器的设计约束：

| 设计参数 | 约束条件 | 影响 |
|---------|---------|------|
| 滤波器长度 $N$ | $N$ 为奇数 | 确保高通移相特性 |
| 通带宽度 | $< 0.9\pi$ | 中心频率偏移修正 |
| 阻带衰减 | $> 40$ dB | 旁瓣泄漏控制 |
| 群延迟 | $(N-1)/2$ 采样点 | 输出时间对齐 |

## EMT 中的角色

在电磁暂态（EMT）仿真中，希尔伯特变换主要用于以下场景：

### 瞬时特征提取

电力系统信号的瞬时幅值、相位和频率是故障检测、继电保护、和振荡监控的关键输入量。希尔伯特变换提供了一种无相干频带假设的瞬时参数估计方法：

$$A(t) = \sqrt{x^2(t) + \hat{x}^2(t)}, \quad \phi(t) = \arctan\frac{\hat{x}(t)}{x(t)}$$

### 移频分析（SFA, Shifted-Frequency Analysis）

移频分析方法以希尔伯特变换为基础，将工频载波从瞬时量中移除，将频谱中心从 $\omega_0$ 搬移到零频附近：

$$z_{sf}(t) = z(t) \cdot e^{-j\omega_0 t} = A(t)\,e^{j(\phi(t) - \omega_0 t)}$$

此时稳态基频正弦量被表示为慢变化包络，可使用更大的仿真步长进行计算。当 $e^{-j\omega_0 t}$ 与解析信号的乘积将正弦量变换为直流（零频）分量时，可采用大步长梯形积分，显著降低计算量。

### 包络检测与故障分析

在故障检测中，电压/电流包络的突变是故障判别的核心依据。希尔伯特变换在包络检波中的应用：

1. 对采样信号 $v[n]$ 计算希尔伯特变换 $\hat{v}[n]$
2. 构建解析信号 $z[n] = v[n] + j\hat{v}[n]$
3. 包络为 $|z[n]| = \sqrt{v^2[n] + \hat{v}^2[n]}$
4. 检测包络突变量 $\Delta |z|$ 识别故障时刻

## 形式化表达

### 希尔伯特核的奇异积分形式

$$\hat{x}(t) = \frac{1}{\pi}\lim_{\varepsilon\to 0^{+}}\left(\int_{-\infty}^{t-\varepsilon}\frac{x(\tau)}{t-\tau}d\tau + \int_{t+\varepsilon}^{\infty}\frac{x(\tau)}{t-\tau}d\tau\right)$$

### 解析信号的极坐标分解

$$z(t) = x(t) + j\hat{x}(t) = A(t)\,e^{j\phi(t)}$$

其中：

$$A(t) = \sqrt{x^2(t) + \hat{x}^2(t)}, \quad \phi(t) = \arctan\frac{\hat{x}(t)}{x(t)}$$

### 瞬时频率的直接计算形式

避免相位展开，直接由实信号和其实部希尔伯特变换计算瞬时频率：

$$\omega(t) = \frac{x(t)\,\dot{\hat{x}}(t) - \hat{x}(t)\,\dot{x}(t)}{x^2(t) + \hat{x}^2(t)}$$

### 移频相量的解析信号构造

在 EMT 移频分析中，基于希尔伯特变换的解析信号构造为：

$$z(t) = x(t) + j\mathcal{H}\{x(t)\}$$

$$\text{移频后：} \quad z_{sf}(t) = z(t)\,e^{-j\omega_0 t}$$

其中 $e^{-j\omega_0 t}$ 是移频因子，$\omega_0$ 是工频角频率（$2\pi\cdot 50$ 或 $2\pi\cdot 60$ rad/s）。

### 离散 Hilbert 变换的矩阵形式

对于长度为 $N$ 的信号向量 $\mathbf{x} = [x[0], x[1], \ldots, x[N-1]]^T$，其希尔伯特变换可写为：

$$\mathbf{\hat{x}} = \mathbf{H}\,\mathbf{x}$$

其中 $\mathbf{H}$ 是 $N\times N$ 的希尔伯特变换矩阵，元素为：

$$H_{m,n} = \frac{1}{N}\sum_{k=0}^{N-1}H[k]\,e^{j2\pi mk/N},\quad H[k] = \begin{cases} -j, & k = 1,2,\ldots,N/2-1 \\ 0, & k = 0, N/2 \\ j, & k = N/2+1,\ldots,N-1 \end{cases}$$

## EMT 建模方法

### 方法 1：直接 FIR 希尔伯特变换

**原理**：使用预设计的线性相位 FIR 滤波器直接对采样信号进行滤波，输出正交分量。

**离散化实现**：

$$h[n] = \begin{cases} \frac{2}{\pi}\frac{\sin^2(\pi n/2)}{n}, & n \neq 0 \\ 0, & n = 0 \end{cases}$$

$$\hat{x}[m] = \sum_{n=-M}^{M} h[n]\,x[m-n]$$

其中 $M = (N-1)/2$ 是滤波器半长度。

**特点**：
- 计算简单，延迟可预估
- 群延迟为 $(N-1)/2$ 采样点
- 过渡带边缘频率响应偏差需补偿

### 方法 2：DFT/FFT 频域滤波法

**原理**：将信号延拓至 $2N$ 点，在频域中对正负频率分量分别设置 $\pm j$ 的复权重，经逆变换还原。

**实现步骤**：
1. 将 $N$ 点信号延拓为 $2N$ 点：$x_e[k] = x[k]$（$k=0,1,\ldots,N-1$），$x_e[k]=0$（$k=N,\ldots,2N-1$）
2. 计算 DFT：$X_e[k] = \sum_{n=0}^{2N-1} x_e[n]\,e^{-j2\pi kn/(2N)}$
3. 频域加权：$H_e[k] = -j\cdot\text{sgn}(k - N)$（正频率加权 $-j$，负频率加权 $+j$）
4. 逆变换：$\hat{x}_e[k] = \frac{1}{2N}\sum_{k=0}^{2N-1} H_e[k]\,X_e[k]\,e^{j2\pi kn/(2N)}$
5. 取前 $N$ 点得到 $\hat{x}[k]$

**特点**：
- 精度高，频率响应理想
- 计算量 $O(N\log N)$（FFT）
- 适合离线批量处理

### 方法 3：多相 Filter Bank 法

**原理**：将信号分解为多相子带，分别在子带上实现希尔伯特变换，适用于宽频带信号的瞬时参数跟踪。

**特点**：
- 可处理宽频带信号（克服窄带假设）
- 各子带独立估计瞬时频率
- 计算复杂度高

### 方法 4：时域递归积分法

**原理**：对于实时 EMT 仿真需求，基于滑动窗口的递归积分形式逐步更新希尔伯特变换输出。

**递推形式**：

$$\hat{x}[m] = \hat{x}[m-1] + \frac{1}{\pi}\left(\frac{x[m] - x[m-1]}{m - (m-1)} + \sum_{n=m-N}^{m-1}\frac{x[n]}{m-n}\right)$$

**特点**：
- 适合实时仿真
- 延迟小（小于一个窗口长度）
- 精度低于 FIR/DFT 方法

## 关键技术挑战

### 挑战 1：窄带假设失效

希尔伯特变换的瞬时频率物理意义仅对单分量（monocomponent）信号成立。对于多频率成分叠加的电力系统信号，直接应用希尔伯特变换会导致虚假的瞬时频率分量。

**解决方向**：在使用希尔伯特变换前，先通过经验模态分解（EMD）将信号分解为若干固有模态函数（IMF），再对每个 IMF 分别应用希尔伯特变换。

### 挑战 2：边界效应（Endpoint Effect）

有限长信号的希尔伯特变换在信号两端会出现虚假振荡（Gibbs 现象），这是由于 FIR 滤波器的有限截断效应和边缘处的边界条件不确定造成的。

**解决方向**：
- 镜像延拓：在信号两端镜像延拓后再进行变换
- 线性预测：用线性外推填充边界

### 挑战 3：采样率与Nyquist准则

瞬时频率计算要求采样率满足 Nyquist 准则。对于高频振荡（ $>1$ kHz）分析，需要 $f_s > 2 f_{\max}$，这在实时 EMT 仿真中可能受限。

**解决方向**：欠采样时采用带通下变频（将信号先与 $e^{j\omega_c t}$ 相乘，中心频率搬移至低频段）后再进行分析。

### 挑战 4：噪声环境下的鲁棒性

在故障暂态期间，噪声会影响希尔伯特变换的精度，导致瞬时幅值和频率估计偏差增大。

**解决方向**：在希尔伯特变换前增加带通/陷波滤波预处理，或使用基于小波的降噪方法。

### 挑战 5：离散 Hilbert 变换的频谱泄漏

有限长 FIR 滤波器的非理想过渡带会引起频谱泄漏，导致正交分量幅值偏差和相位误差。

**解决方向**：使用 Kaiser 窗或 Dolph-Chebyshev 窗优化滤波器设计，提高阻带衰减至 $> 60$ dB。

## 量化性能边界

| 性能指标 | 数值范围 | 说明 |
|---------|---------|------|
| 幅值相对误差 | $< 2\%$（FIR-128 阶） | 理想 FIR 设计下 |
| 相位误差 | $\pm 1^\circ$（FIR-128 阶，$0.05<\omega/\pi<0.95$） | 通带内 |
| 计算复杂度（DFT法） | $O(N\log N)$ | $N$ 为信号长度 |
| 计算复杂度（FIR法） | $O(N)$ | 递推形式 |
| 群延迟 | $(N-1)/2$ 个采样点 | FIR 滤波器 |
| 阻带衰减（优化设计） | $> 50$ dB | Kaiser 窗设计 |
| 步长提升比（SFA） | $5-20\times$（移频包络 vs 全步长 EMT） | 据 Xu 等 2023 移频分析 |

**移频分析（SFA）的步长提升比**取决于仿真关注频带相对于工频的带宽比。对于慢变机电暂态（ $< 10$ Hz），步长可从 $10$ μs 提升至 $100-200$ μs，仿真效率提升 $10-20$ 倍，同时保留工频包络动态。

## 适用边界与选择指南

| 场景 | 推荐方法 | 适用条件 | 失效条件 |
|------|---------|---------|---------|
| 窄带振荡分析 | FIR 希尔伯特 + 解析信号 | 单分量、准平稳 | 多频率叠加、宽频带 |
| 故障包络检测 | 直接 FIR 包络 | 信噪比 $> 10$ dB | 高噪声、强谐波 |
| 移频大步长 EMT | SFA（希尔伯特 + 频移） | 包络变化慢于工频周期 | 快变故障、开关动作 |
| 实时仿真 | 时域递归积分 | 计算资源受限 | 精度要求高 |
| 离线频谱分析 | DFT 频域滤波 | 批量处理 | 实时性要求 |

### Hilbert 变换 vs. 其他瞬时参数估计方法

| 方法 | 精度 | 计算量 | 实时性 | 多分量 |
|------|-----|-------|-------|-------|
| Hilbert 变换 | 高 | 中 | 好 | 差（需预处理） |
| 过零检测 | 低 | 低 | 最好 | 差 |
| Prony 分析 | 高 | 高 | 差 | 好 |
| 小波变换 | 高 | 高 | 中 | 好 |

## 相关方法与相关模型

- [[fourier-series]] — 傅里叶级数展开（正交分解基础）
- [[prony-analysis]] — Prony 分析（振荡模态辨识）
- [[small-signal-analysis]] — 小信号分析（线性化分析框架）
- [[power-quality]] — 电能质量分析（谐波与间谐波检测）
- [[harmonic-analysis-methods]] — 谐波分析方法（频域分析工具）
- [[numerical-integration]] — 数值积分方法（EMT 离散化基础）
- [[state-space-method]] — 状态空间法（EMT 系统方程）
- [[vector-fitting]] — 矢量拟合（频率响应建模）
- [[average-value-model]] — 平均值模型（VSC 简化模型）
- [[nodal-analysis]] — 节点分析（EMT 网络求解）

## 来源论文

### 移频分析与希尔伯特变换

[[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a]] — 本文提出 RM-SFEMT 方法，用根匹配离散化替代常规梯形法处理移频域电磁暂态仿真中的截断误差，并结合嵌入式小步长处理突变场景。该方法证明了移频分析在故障和开关操作场景下的精度改善机制。

### 多尺度建模中的希尔伯特变换

[[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40]] — 含 VSC-HVDC 交直流系统的多尺度暂态建模研究，利用希尔伯特变换构造解析信号，结合移频因子 $e^{-j\omega_0 t}$ 将工频载波从瞬时量中移除，建立统一的移频相量模型，实现电磁暂态与机电暂态的联合仿真。

[[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe]] — 感应电机的多尺度相域建模研究，将电压、电流、磁链统一表示为解析信号，通过可调移频参考框架实现瞬时波形模型与动态相量包络模型的连续覆盖，并推导恒定的诺顿内导纳接口。

[[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析]] — MMC-MTDC 系统的电磁-机电暂态建模与实时仿真研究，将希尔伯特变换与移频分析结合用于 MMC-HVDC 系统，建立了移频相量模型以替代传统的瞬时值/相量硬接口，实现 RT-LAB 上的分区并行实时仿真。

### 经典文献

- Hilbert, D., *Grundzüge einer allgemeinen Theorie der linearen Integralgleichungen*, 1912 — 希尔伯特空间理论奠基性工作
- Bedrosian, E., "A Product Theorem for Hilbert Transforms," *Proc. IEEE*, 1963 — Bedrosian 恒等式
- Huang, N.E., et al., "The Empirical Mode Decomposition and the Hilbert Spectrum," *Proc. R. Soc. Lond. A*, 1998 — HHT 方法

### 相关信号处理方法

- 经验模态分解（EMD）与希尔伯特-黄变换（HHT）：将多分量信号分解为 IMF 后再应用希尔伯特变换，解决窄带假设失效问题
- 小波变换：时频局部化分析，适合非平稳信号的瞬时参数跟踪
- 傅里叶短时变换（STFT）：窗函数选择影响时频分辨率
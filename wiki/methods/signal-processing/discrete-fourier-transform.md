---
title: "离散傅里叶变换 (Discrete Fourier Transform)"
type: method
tags: [dft, fft, spectral-analysis, harmonic-analysis, window-function, gibbs-oscillation, emt-signal-processing]
created: "2026-05-04"
updated: "2026-05-18"
---

# 离散傅里叶变换 (Discrete Fourier Transform)

## 定义与边界

离散傅里叶变换（DFT）是将有限长离散时域序列$x[n]$（$n = 0, 1, \ldots, N-1$）映射为等长离散频域序列$X[k]$（$k = 0, 1, \ldots, N-1$）的线性变换，是连续傅里叶变换在采样、有限长序列条件下的忠实离散实现。DFT 是 EMT 后处理与信号分析的核心数学工具，快速傅里叶变换（FFT）则是其 $O(N\log_2 N)$ 高效实现。

**边界限定**：本页面聚焦于 DFT/FFT 的数值实现与 EMT 应用，涵盖窗函数设计、频谱泄漏抑制（Gibbs 振荡）、谐波分析和功率谱估计。

## EMT 中的角色

DFT 在 EMT 仿真中承担四类任务：

1. **频谱分析**：将换流器输出电流、故障电流等时域暂态波形转换为频域表示，识别特征频率分量
2. **谐波诊断**：检测电压电流中的谐波含量（THD），评估谐波畸变对设备的影响
3. **阻抗扫频**：在 EMT 频域阻抗分析中，通过 DFT 将时域响应转换为频域阻抗曲线
4. **模态参数辨识**：结合 Prony 分析或 Matrix Pencil 方法，从 DFT 频谱中提取系统振荡模态

## 核心机制

### 1. DFT/FFT 定义与算法

对于长度为 $N$ 的复序列，正变换和逆变换定义为：

$$X[k] = \sum_{n=0}^{N-1} x[n] \, e^{-j 2\pi kn/N}, \quad k = 0, 1, \ldots, N-1$$

$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \, e^{j 2\pi kn/N}, \quad n = 0, 1, \ldots, N-1$$

**Cooley-Tukey 基-2 FFT** 将 $N=2^M$ 点 DFT 分解为两个 $N/2$ 点 DFT 的递归结构，复杂度从 $O(N^2)$ 降至 $O(N\log_2 N)$。每级分解将序列按奇偶位分为两组，分别计算短 DFT 再合并。

| 算法 | 复杂度 | 长度要求 | 特点 |
|------|--------|----------|------|
| Cooley-Tukey 基-2 | $O(N\log_2 N)$ | $N = 2^M$ | 最常用，蝶形结构 |
| 基-4 FFT | $O(N\log_4 N)$ | $N = 4^M$ | 比基-2 少 $\log_2 4$ 级 |
| 混合基 FFT | $O(N\log_2 N)$ | 任意 | 支持非 2 幂次长度 |
| Chirp-Z 变换 | $O(N\log_2 N)$ | 任意 | 螺旋线等值线扫频 |

### 2. 窗函数与频谱泄漏

当信号在窗内非整周期截断时，频谱能量泄漏到相邻频点，称为**频谱泄漏**（spectral leakage）。加窗通过旁瓣抑制抑制泄漏，但会加宽主瓣、降低频率分辨率。

| 窗函数 | 旁瓣抑制 | 主瓣宽度 |适用场景 |
|--------|----------|----------|---------|
| 矩形窗 | $-13.3$ dB | 窄 | 整周期信号、快速粗测 |
| 汉宁窗 | $-31.0$ dB | 2 倍 | 一般谐波分析 |
| 汉明窗 | $-43.0$ dB | 2 倍 | 频谱泄漏要求较高 |
| 布莱克曼窗 | $-57.0$ dB | 3 倍 | 精密频谱分析 |
| 凯泽窗（$\beta=9$） | $-51.0$ dB | 可调 | 工程通用，需参数调优 |

**凯泽窗**参数 $\beta$ 控制旁瓣与主瓣宽度的权衡：$\beta$ 增大 → 旁瓣抑制增强 → 主瓣加宽。

### 3. Gibbs 振荡与抑制方法

#### 3.1 Gibbs 现象机理

当逆傅里叶积分的频率上限 $\omega_{\max}$ 被突然截断（即施加矩形窗 $G(\omega)$）时，等效于在时域与 $\mathrm{sinc}$ 函数卷积。$\mathrm{sinc}$ 函数的尾部振荡在间断点处导致过冲（overshoot），其幅度约为间断点跳变的 **9%**，且不随截断项数增加而衰减，只缩小振荡范围——这一现象由 Wilbraham（1848）发现、 Gibbs（1899）正式描述。

设 $f(t)$ 在 $t=0$ 处有跳变，则逆变换：

$$f(t) = \frac{1}{\pi}\int_{0}^{\omega_{\max}} F(\omega)\,e^{j\omega t}\,d\omega$$

施加矩形窗后，时域结果等效为 $f(t)$ 与 $\mathrm{sinc}(\omega_{\max} t)$ 的卷积，在 $t=0$ 处产生约 **0.089 × 跳变量**（即 8.95%）的过冲。

#### 3.2 Sinc 窗抑制方法（σ-approximation）

用平滑过渡的 $G_{\mathrm{sinc}}(\omega)$ 替代矩形窗以抑制 Gibbs 振荡：

$$G_{\mathrm{sinc}}(\omega) = \begin{cases} \displaystyle \frac{\sin(\pi\omega/\omega_{\max})}{\pi\omega/\omega_{\max}} = \mathrm{sinc}\!\left(\frac{\omega}{\omega_{\max}}\right), & 0 \leq \omega \leq \omega_{\max} \\[8pt] 0, & \text{otherwise} \end{cases}$$

该方法需要计算每个频率点的 $\mathrm{sinc}$ 函数值并逐点相乘，计算量较大。

#### 3.3 线性中点插值法（Shi et al. 2021）

Shi、Ametani 和 Gole（2021）提出在逆傅里叶变换计算完成后，用**线性中点插值**替代 $\mathrm{sinc}$ 窗乘法，既抑制 Gibbs 振荡，又显著降低计算复杂度。

**核心原理**：设原始频域函数为 $F(\omega)$，在相邻频点 $\omega_k$ 和 $\omega_{k+1}$ 之间进行线性中点插值，等效于在频域施加余弦窗函数 $G_{\cos}(\omega)$：

$$G_{\cos}(\omega) = \cos\!\left(\frac{\pi\omega}{2\omega_{\max}}\right), \quad 0 \leq \omega \leq \omega_{\max}$$

该余弦窗在 $\omega=0$ 和 $\omega=\omega_{\max}$ 处强制为零，实现平滑过渡，从而抑制 Gibbs 振荡。

**数值验证**（Shi et al. 2021）：当时间步长 $\Delta t \leq \frac{1}{10}\cdot\frac{1}{f_{\max}}$ 时，线性中点插值法的 Gibbs 振荡抑制效果与 $\mathrm{sinc}$ 窗方法相当，且避免了逐频点 $\mathrm{sinc}$ 计算。

### 4. 频谱参数与分辨率

**频率分辨率**：

$$\Delta f = \frac{f_s}{N} = \frac{1}{T_{\mathrm{window}}}$$

其中 $f_s$ 为采样频率，$N$ 为 DFT 点数，$T_{\mathrm{window}}$ 为分析窗长。

**奈奎斯特频率**：

$$f_{\mathrm{Nyquist}} = \frac{f_s}{2}$$

**时频不确定原理**：频率分辨率 $\Delta f$ 与时间分辨率 $\Delta t$ 满足 $\Delta f \cdot \Delta t \geq \frac{1}{2}$，加窗抑制频谱泄漏会等效加宽主瓣，实质是频率分辨率换旁瓣抑制。

### 5. 功率谱密度估计

**周期图法**（直接法）：

$$P[k] = \frac{1}{N}\bigl|X[k]\bigr|^2$$

方差较大，不适合短数据。

**Welch 法**（改进方差）：

将序列分为 $M$ 段重叠子序列，各段分别计算周期图后求平均：

$$P_{\mathrm{Welch}}[k] = \frac{1}{M}\sum_{i=1}^{M} P_i[k]$$

分段重叠率通常取 50%，使估计方差降低约 $M$ 倍，同时保持相近的频率分辨率。

### 6. 谐波分析

**总谐波畸变率**（THD）：

$$\mathrm{THD} = \frac{\sqrt{\sum_{h=2}^{H} |X[h]|^2}}{|X[1]|} \times 100\%$$

其中 $X[1]$ 为基波复振幅，$X[h]$ 为第 $h$ 次谐波（$h \geq 2$）。

**单次谐波含量**：

$$K_h = \frac{|X[h]|}{|X[1]|} \times 100\%$$

在 EMT 仿真中，常用滑动 DFT 逐时步计算谐波含量，用于换流器谐波注入评估和滤波器设计验证。

## 量化性能边界

| 工况 | 窗长 $N$ | 频率分辨率 $\Delta f$ | THD 误差 | 计算时间（1000节点）|
|------|----------|----------------------|----------|-------------------|
| 基波提取（50 Hz）| 256 | 0.39 Hz（@1 kHz采样）| <0.1% | <1 ms |
| 谐波分析（2-50 次）| 1024 | 0.10 Hz | <0.5% | <5 ms |
| 宽频振荡（10 kHz）| 2048 | 4.9 Hz | <2% | <20 ms |
| 暂态检测（突变）| 128 | 7.8 Hz | 依赖窗函数 | <0.5 ms |

Shi et al.（2021）在 ATP-EMTP 中验证：$\Delta t \leq \frac{1}{10}\cdot\frac{1}{f_{\max}}$ 时，线性中点插值法 Gibbs 振荡抑制有效，过冲幅度从 ~9% 降至 <1%；计算时间比完整 $\mathrm{sinc}$ 窗法减少约 40%。

## 适用边界与选择指南

### 窗函数选择决策

| 场景 | 推荐窗函数 | 理由 |
|------|-----------|------|
| 整周期稳态谐波 | 矩形窗 | 主瓣最窄，无额外加权失真 |
| 非整周期谐波分析 | 汉宁窗 | 旁瓣抑制-31 dB，2 倍主瓣展宽可接受 |
| 高精度阻抗扫频 | 布莱克曼窗 | -57 dB 旁瓣，抑制频谱泄漏 |
| 实时滑动 DFT | 凯泽窗 | 参数可调，精度/效率平衡 |
| EMT 故障暂态检测 | 矩形窗→汉宁窗 | 快速粗测优先，后续可加窗精细分析 |

### 失效模式

| 失效场景 | 原因 | 后果 |
|---------|------|------|
| 混叠（aliasing）| $f_s \leq 2 f_{\max}$ | 高频分量伪装成低频，谐波误诊 |
| 栅栏效应 | 离散频点未对齐信号频率 | 峰值频率估算偏差，分辨率不足 |
| 严重频谱泄漏 | 非整周期截断 + 矩形窗 | THD 高估，基波幅值偏差 |
| Gibbs 振荡 | 逆变换频率上限截断 | 跳变点附近过冲/下冲，电压/电流峰值失真 |
| 短数据方差大 | DFT 点数不足 | 谐波含量估计不稳定，需 Welch 分段 |
| 非平稳信号 | 时变频率超出窗假设 | 频谱模糊，谐波分类失效 |

## 相关方法

- [[fft]] — FFT 算法详细实现与基-2/基-4 蝶形结构
- [[fourier-filtering]] — 傅里叶域数字滤波与 FIR/IIR 设计
- [[fourier-series]] — 连续周期信号的傅里叶级数表示
- [[harmonic-analysis-methods]] — 电力系统谐波测量与分析方法
- [[prony-analysis]] — 指数拟合模态参数辨识（与 DFT 频谱互补）

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| Shi, Ametani & Gole — *A study on interpolation and weighting function for numerical Fourier transform*（Electric Power Systems Research, 2021） | 2021 | 提出线性中点插值法抑制 Gibbs 振荡，等效余弦窗，比 $\mathrm{sinc}$ 窗计算量减少 40%，在 ATP-EMTP 中验证 |
| Cooley & Tukey — *An algorithm for the machine calculation of complex Fourier series*（Math. Comp., 1965） | 1965 | 基-2 FFT 算法的奠基性工作，$O(N\log_2 N)$ 复杂度 |
| Oppenheim & Schafer — *Discrete-Time Signal Processing*（Prentice-Hall, 1989） | 1989 | DFT/FFT/窗函数/功率谱估计的理论框架 |
| Proakis & Manolakis — *Digital Signal Processing*（Prentice-Hall, 2006） | 2006 | 数字信号处理经典教材，涵盖频谱分析与谐波估计 |
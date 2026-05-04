---
title: "频域分析 (Frequency-Domain Analysis)"
type: topic
tags: [frequency-domain, analysis, harmonic, impedance, spectrum, fft, bode]
created: "2026-05-02"
---

# 频域分析 (Frequency-Domain Analysis)

## 概述

频域分析(Frequency-Domain Analysis)是研究电力系统频率响应特性的重要方法，通过分析系统在不同频率下的阻抗、导纳、传递函数和频谱特性，揭示系统的谐振特性、谐波传播行为和宽频稳定性。频域分析为滤波器设计、谐振抑制、设备建模和系统规划提供理论基础，是电磁暂态仿真和电力电子系统分析的核心技术之一。

## 基本理论

### 频域与时域关系

**拉普拉斯变换**：
$$F(s) = \mathcal{L}\{f(t)\} = \int_0^{\infty} f(t)e^{-st}dt$$

**傅里叶变换**（$s = j\omega$）：
$$F(j\omega) = \int_{-\infty}^{\infty} f(t)e^{-j\omega t}dt$$

**逆变换**：
$$f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega)e^{j\omega t}d\omega$$

### 频域特征量

| 特征量 | 符号 | 定义 | 应用 |
|-------|------|------|------|
| 阻抗 | $Z(j\omega)$ | $V/I$ | 谐振分析 |
| 导纳 | $Y(j\omega)$ | $I/V$ | 滤波器设计 |
| 传递函数 | $H(j\omega)$ | $Y/X$ | 控制分析 |
| 增益 | $|H(j\omega)|$ | 幅值比 | 频率响应 |
| 相位 | $\angle H(j\omega)$ | 相位差 | 稳定性分析 |

## 频域建模方法

### 元件频域模型

#### 电阻
$$Z_R(j\omega) = R$$

#### 电感
$$Z_L(j\omega) = j\omega L$$

#### 电容
$$Z_C(j\omega) = \frac{1}{j\omega C} = -j\frac{1}{\omega C}$$

#### RLC串联
$$Z_{RLC}(j\omega) = R + j\omega L + \frac{1}{j\omega C} = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

### 输电线路频域模型

**分布参数线路**：
$$Z_c(j\omega) = \sqrt{\frac{R(j\omega) + j\omega L(j\omega)}{G(j\omega) + j\omega C(j\omega)}}$$

$$\gamma(j\omega) = \sqrt{(R(j\omega) + j\omega L(j\omega))(G(j\omega) + j\omega C(j\omega))}$$

其中：
- $Z_c$: 特性阻抗
- $\gamma$: 传播常数
- [[frequency-dependent-line-model]] - 频变线路模型

### 频变参数处理

**大地返回阻抗**（Carson公式）：
$$Z_g(j\omega) = \frac{j\omega\mu_0}{2\pi}\ln\frac{D_{e}}{d}$$

其中$D_e = 659\sqrt{\frac{\rho}{f}}$为等效大地深度。

**皮肤效应**（简化模型）：
$$R_{ac}(f) = R_{dc}\left(1 + k\sqrt{f}\right)$$

## 频域分析技术

### 频率扫描

**单点扫描**：
$$Z(j\omega_k) = \frac{V(j\omega_k)}{I(j\omega_k)}, \quad k = 1, 2, ..., N$$

**对数扫描**：
$$\omega_k = \omega_{min} \cdot 10^{k\cdot\Delta log}, \quad \Delta log = \frac{\log_{10}(\omega_{max}/\omega_{min})}{N}$$

**应用场景**：
- 宽频带阻抗特性测量
- 谐振频率识别
- 稳定性分析

### 快速傅里叶变换(FFT)

**DFT定义**：
$$X[k] = \sum_{n=0}^{N-1} x[n]e^{-j2\pi kn/N}, \quad k = 0, 1, ..., N-1$$

**FFT复杂度**：$O(N\log N)$ vs DFT的$O(N^2)$

**采样定理**：
$$f_s \geq 2f_{max}$$

**频谱泄漏**：
- 加窗处理：Hanning、Hamming、Blackman
- 分辨率：$\Delta f = f_s/N$

[[fft]] - FFT方法详情

### 矢量拟合 (Vector Fitting)

**有理函数近似**：
$$f(s) \approx \sum_{i=1}^{N}\frac{c_i}{s-a_i} + d + se$$

**应用**：
- 频变参数建模
- 网络等值
- 时域转换

[[vector-fitting]] - 矢量拟合详情

### Prony分析

**指数函数拟合**：
$$y(t) = \sum_{i=1}^{N}A_ie^{\sigma_i t}\cos(\omega_i t + \phi_i)$$

**频率提取**：
- 阻尼系数：$\sigma_i$
- 振荡频率：$\omega_i$
- 幅值相位：$A_i, \phi_i$

[[prony-analysis]] - Prony分析详情

## 稳定性分析

### 奈奎斯特判据

**稳定性条件**：
$$Z_{source}(j\omega) + Z_{load}(j\omega) \neq 0$$

**阻抗比**：
$$L(j\omega) = \frac{Z_{source}(j\omega)}{Z_{load}(j\omega)}$$

**判据**：
- 若$L(j\omega)$的奈奎斯特图包围(-1,0)点，系统不稳定
- 距离(-1,0)点的距离表示稳定裕度

### 波德图分析

**幅频特性**：
$$20\log_{10}|H(j\omega)| \text{ [dB]}$$

**相频特性**：
$$\angle H(j\omega) \text{ [deg]}$$

**稳定裕度**：
- 增益裕度$GM$：相位=-180°时的增益余量
- 相位裕度$PM$：增益=0dB时的相位余量

### 谐振分析

**串联谐振**：
$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad Z_{min} = R$$

**并联谐振**：
$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad Z_{max} = \frac{L}{RC}$$

**品质因数**：
$$Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 CR}$$

## 设备频域建模

### 变压器

**高频模型**：
```
    ┌───R1───┬───Lσ1───┬───C1───┐
    │        │         │        │
   V1        │         │        V2
    │        │         │        │
    └───C12──┴───Lm────┴───C12──┘
```

- $R_1, R_2$: 绕组电阻
- $L_{\sigma}$: 漏感
- $L_m$: 励磁电感
- $C_1, C_2, C_{12}$: 分布电容

[[transformer-model]] - 变压器模型

### 电缆

**高频等效电路**（π型）：
$$Z_{series} = R(f) + j\omega L(f)$$
$$Y_{shunt} = G + j\omega C$$

[[cable-model]] - 电缆模型

### 电机

**等效电路**（单相）：
```
    ┌──Rs──┬──Lls──┬──────┬──Llr'──┬──Rr'/s──┐
    │      │       │      │        │         │
   Vs    Lms      Rfe    Llr'     Rr'      Ir
    │      │       │      │        │         │
    └──────┴───────┴──────┴────────┴─────────┘
```

[[synchronous-machine-model]] - 同步电机模型

## 谐波分析

### 谐波源

| 谐波源 | 特征谐波 | 幅值特性 |
|-------|---------|---------|
| 6脉波整流器 | 5, 7, 11, 13... | $I_h \approx I_1/h$ |
| 12脉波整流器 | 11, 13, 23... | 幅值更低 |
| PWM逆变器 | 载波频率附近 | 与调制比相关 |
| 电弧炉 | 2, 3, 5... | 随机性 |

### 谐波潮流

**节点方程**：
$$Y(h)V(h) = I_{source}(h)$$

其中$h$为谐波次数。

**谐波阻抗**：
$$Z(h) = \sqrt{R^2 + (hX_L - \frac{X_C}{h})^2}$$

### 谐振条件

**并联谐振**：
$$h_{res} = \sqrt{\frac{X_C}{X_L}} = \sqrt{\frac{S_{sc}}{Q_{cap}}}$$

其中：
- $S_{sc}$: 短路容量
- $Q_{cap}$: 电容无功

## 应用案例

### 滤波器设计

**单调谐滤波器**：
$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

$$Q = \frac{X_L}{R} = \frac{X_C}{R}$$

**高通滤波器**：
$$f_c = \frac{1}{2\pi RC}$$

### HVDC谐波分析

**特征谐波**：
$$h = np \pm 1$$

其中$n$为正整数，$p$为脉波数。

**非特征谐波**：由不对称、触发角偏差产生

### 风电并网宽频振荡

**次同步振荡**：10-50 Hz
**超同步振荡**：高于基波频率
**高频谐振**：与滤波器、电缆相关

[[wind-farm-modeling]] - 风电场建模

## 频域-时域转换

### 数值拉普拉斯逆变换

**Gaver-Stehfest算法**：
$$f(t) \approx \frac{\ln 2}{t}\sum_{i=1}^{N}V_i F\left(\frac{\ln 2}{t}i\right)$$

### 卷积方法

**时域响应**：
$$v(t) = \mathcal{L}^{-1}\{Z(s)I(s)\} = \int_0^t z(\tau)i(t-\tau)d\tau$$

[[numerical-laplace-transform]] - 数值拉普拉斯变换

## 相关主题
- [[time-domain-simulation]] - 时域仿真
- [[harmonic-analysis]] - 谐波分析
- [[frequency-dependent-modeling]] - 频率相关建模
- [[wideband-oscillation-stability]] - 宽频振荡稳定性

## 相关方法
- [[vector-fitting]] - 矢量拟合
- [[fft]] - 快速傅里叶变换
- [[prony-analysis]] - Prony分析
- [[modal-analysis]] - 模态分析
- [[fdne-model]] - 频变网络等值

## 来源论文

参见 [[index.md]] 获取更多频域分析相关文献。

---
title: "频率扫描法 (Frequency Scanning)"
type: method
tags: [frequency-scanning, harmonic-analysis, impedance-measurement, stability-analysis, resonance]
created: "2026-05-04"
---

# 频率扫描法 (Frequency Scanning)


```mermaid
graph TD
    subgraph Ncmp[频率扫描法 (Frequency Scanning)]
        N0[线性度: 小信号扰动]
        N1[稳态: 各频点达到稳态]
        N2[频率分辨率: $\Delta f < f_r/Q$]
        N3[动态范围: 信噪比>40dB]
    end
```


## 定义与边界

频率扫描法是一种通过向系统注入特定频率的扰动信号并测量响应，从而获取系统频域特性（阻抗、导纳、传递函数）的实验或仿真分析方法。该方法通过遍历感兴趣的频段，绘制频响特性曲线，用于识别谐振点、评估稳定性裕度。

在电力系统分析中，频率扫描法主要应用于：
- 电网阻抗频谱测量与建模
- 电力电子设备宽频阻抗特性获取
- 谐振频率识别与阻尼评估
- 并网稳定性分析与裕度计算

**边界限定**：本方法适用于线性时不变系统的频域特性获取，不适用于非线性系统的全工况特性描述。

## EMT中的作用

频率扫描法解决了复杂系统频域特性难以理论建模的问题：

- **黑箱建模**：无需设备内部参数，基于端口测量建立宽频模型
- **谐振识别**：精确定位电网与设备交互产生的谐振频率
- **稳定性裕度**：基于阻抗比的奈奎斯特图或伯德图评估稳定性
- **宽频验证**：验证电磁暂态模型的频域精度

## 主要分支与机制

### 1. 单频点扫描

在每个频点独立注入正弦扰动，稳态后测量响应：
$$Z(f_k) = \frac{V(f_k)}{I(f_k)}, \quad k = 1, 2, ..., N$$

精度高但耗时，适用于关键频段精细分析。

### 2. 多频同时扫描

注入包含多个频率分量的合成信号，通过FFT分解响应：
$$i(t) = \sum_{k=1}^{N} I_k \sin(2\pi f_k t + \phi_k)$$

效率高但可能存在频率间耦合干扰。

### 3. 线性调频扫描

注入频率连续变化的啁啾信号(chirp)：
$$f(t) = f_0 + \frac{f_1-f_0}{T}t$$

兼顾效率与精度，适用于宽频带快速扫描。

## 形式化表达

### 基本测量原理

在端口注入电流扰动 $\Delta I(f)$，测量电压响应 $\Delta V(f)$，阻抗为：

$$
Z(f) = \frac{\Delta V(f)}{\Delta I(f)} = |Z(f)|e^{j\varphi(f)}
$$

其中：
- $|Z(f)| = \frac{|\Delta V(f)|}{|\Delta I(f)|}$ 为阻抗幅值
- $\varphi(f) = \angle \Delta V(f) - \angle \Delta I(f)$ 为阻抗相角

### 谐振识别

谐振频率 $f_r$ 满足：

$$
\frac{d|Z(f)|}{df}\bigg|_{f=f_r} = 0, \quad \frac{d^2|Z(f)|}{df^2}\bigg|_{f=f_r} < 0
$$

品质因数 $Q$ 与带宽 $\Delta f$ 关系：

$$
Q = \frac{f_r}{\Delta f} = \frac{f_r}{f_2 - f_1}
$$

其中 $f_1, f_2$ 为半功率点频率。

### 稳定性裕度

基于阻抗比 $T_m(f) = Z_{grid}(f)/Z_{device}(f)$ 的稳定性判据：

**幅值裕度** (Gain Margin):
$$GM = -20\log_{10}|T_m(f_{\pi})| \quad \text{[dB]}$$

其中 $f_{\pi}$ 满足 $\angle T_m(f_{\pi}) = -180°$。

**相位裕度** (Phase Margin):
$$PM = 180° + \angle T_m(f_c) \quad \text{[°]}$$

其中 $f_c$ 满足 $|T_m(f_c)| = 1$ ($0$ dB)。

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 线性度 | 小信号扰动 | 扰动幅值<5%额定值 |
| 稳态 | 各频点达到稳态 | 需足够长的仿真时间 |
| 频率分辨率 | $\Delta f < f_r/Q$ | 分辨谐振峰 |
| 动态范围 | 信噪比>40dB | 保证测量精度 |

### 失效边界

- **非线性饱和**：大扰动导致设备非线性，小信号阻抗模型失效
- **频率耦合**：多频同时扫描时各频率分量间产生互调干扰
- **泄漏误差**：FFT分析时非整数周期截断导致频谱泄漏
- **时变特性**：控制模式切换、温度变化导致阻抗时变

### 关键假设

1. 系统在测量时间窗口内近似时不变
2. 扰动-响应关系近似线性
3. 测量端口可充分激励目标模态
4. 背景谐波与噪声可忽略或可被抑制

## 代表性来源

### 经典文献

- Rygg, A., et al., "A Modified Method for Evaluating the Impedance of Power Electronic Converters," *IEEE Trans. Power Electronics*, 2017. - 频率扫描测量方法改进
- Wang, X., et al., "Resonance Analysis in Grid-Connected Converters," *IEEE Trans. Power Electronics*, 2015. - 基于频率扫描的谐振分析
- Cespedes, M. and Sun, J., "Online Measurement of Impedance," *IEEE Trans. Power Electronics*, 2016. - 在线频率扫描技术

### 测量技术

- [[impedance-modeling]] - 阻抗建模理论
- [[harmonic-analysis-methods]] - 谐波分析方法
- [[small-signal-analysis]] - 小信号分析基础
- FFT 频谱分析

### 应用案例

- 并网逆变器阻抗测量
- [[wind-farm-modeling]] - 风电场阻抗特性
- [[pv-power-plant]] - 光伏电站频率扫描分析

## 与相关页面的关系

- [[impedance-modeling]] - 阻抗建模理论框架
- [[vector-fitting]] - 扫描数据的参数化拟合
- [[harmonic-analysis-methods]] - 谐波域分析
- [[frequency-domain-analysis]] - 频域分析方法
- [[emt-simulation-verification]] - EMT模型频域验证

## 开放问题

- 如何抑制多频扫描中的互调干扰以提高效率
- 时变系统（如光伏出力变化）的准稳态频率扫描方法
- 基于宽频功率谱密度的快速阻抗辨识
- 大规模系统的分布式并行频率扫描

## 参考标准

- IEEE Std. 1453 - 电力系统谐波测量
- IEC 61000-4-7 - 谐波和间谐波测量方法
- CIGRE TB 768 - 电力电子设备阻抗测量导则

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。如有更新或修正，请参考最新研究进展。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[application-of-emtp-in-the-research-of-uhv-ac-power-transmission|Application of EMTP in the research of UHV AC power transmis]] | 2006 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation|DQ Admittance Model Extraction for IBRs via Gaussian Pulse E]] | 2023 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
---
title: "傅里叶滤波 (Fourier Filtering)"
type: method
tags: [fourier, filtering, harmonic, signal-processing, dft, fft, relay]
created: "2026-05-02"
---

# 傅里叶滤波 (Fourier Filtering)


```mermaid
graph TD
    subgraph Ncmp[傅里叶滤波 (Fourier Filtering)]
        N0[全窗口 DFT/FFT: 固定窗口频谱]
        N1[滑动 DFT: 随时间更新的频率分量]
        N2[正交傅里叶滤波器: 基波正弦/余弦分量]
        N3[插值 DFT: 频率偏移校正后的幅值相位]
    end
```


## 定义与边界

傅里叶滤波是在频域中选择、提取或抑制特定频率分量的信号处理方法。它通常以 DFT/FFT、滑动 DFT、正弦/余弦正交滤波器或窗函数加权为实现形式，把采样波形 $x[n]$ 映射到频率分量 $X[k]$，再围绕基波、谐波、间谐波或振荡频率进行估计。

该方法是 [[harmonic-analysis]]、[[relay-protection]]、[[phasor-measurement-unit]] 和 EMT 结果后处理的常用工具，但它不是 EMT 数值求解器本身。若研究对象是网络频率响应，应连接到 [[frequency-domain-analysis]]、[[frequency-scan]] 和 [[impedance-measurement]]；若研究对象是多频率模型，应连接到 [[dynamic-phasor]]。

## EMT 中的作用

傅里叶滤波在 EMT 工作流中通常出现在四个位置：

- 波形诊断：从 EMT 输出的电压、电流中提取基波、谐波、间谐波和低频振荡分量。
- 保护算法：在距离保护、差动保护或故障检测中估计基波相量，并抑制不需要的直流偏置或谐波分量。
- 模型验证：比较详细开关模型、平均模型和频域模型在目标频段的幅值与相位。
- 接口变量提取：在 EMT 与动态相量、移频相量或混合仿真接口中生成慢变复包络。

这些用途都依赖窗口长度、采样频率、频率参考和同步策略。不能只写“使用 FFT 得到准确结果”，而应说明被提取的频率、观测窗口和误差来源。

## 核心机制

对 $N$ 点采样序列，DFT 为：

$$X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$$

第 $h$ 次基波谐波所在频点近似为：

$$k_h \approx h f_1 \frac{N}{f_s}$$

当 $k_h$ 不是整数或信号频率偏离额定值时，目标分量会泄漏到相邻频点。实际滤波通常引入窗口 $w[n]$：

$$X_w[k]=\sum_{n=0}^{N-1}w[n]x[n]e^{-j2\pi kn/N}$$

窗口选择体现分辨率与旁瓣抑制之间的权衡。矩形窗适合整周期同步采样；Hann、Hamming、Blackman 等窗可降低旁瓣，但会改变幅值标定和主瓣宽度。滑动 DFT 则通过递推更新窗口结果，适合连续监测，但对数值漂移和频率偏移更敏感。

## 分类与变体

| 方法 | 主要输出 | 适合场景 | 需要说明的前提 |
|------|----------|----------|----------------|
| 全窗口 DFT/FFT | 固定窗口频谱 | 离线 EMT 波形分析、电能质量统计 | 采样率、窗长、窗函数、频率分辨率 |
| 滑动 DFT | 随时间更新的频率分量 | 在线监测、动态相量提取 | 递推稳定性、窗口同步、频率漂移 |
| 正交傅里叶滤波器 | 基波正弦/余弦分量 | 数字保护、相量估计 | 响应时间、直流偏置、谐波抑制能力 |
| 插值 DFT | 频率偏移校正后的幅值相位 | 非同步采样、间谐波估计 | 插值假设、邻近频率干扰 |

## 适用边界与失败模式

- 傅里叶滤波默认窗口内信号接近平稳。故障初始阶段、换相失败和保护动作期间，频谱随时间变化，固定窗口结果只能解释为该窗口内的平均频率内容。
- 频率分辨率由观测时间决定，$\Delta f=f_s/N=1/T_\text{window}$。提高分辨率通常意味着更长窗口和更慢响应。
- 直流偏置、指数衰减暂态、采样不同步和频率漂移会影响基波相量估计；保护算法需要单独评估这些误差。
- 滤波结果不是物理因果证明。频谱中出现某个频率只能说明波形含有该分量，谐振来源还需结合 [[harmonic-transfer-coefficient]]、[[impedance-measurement]] 或系统拓扑分析。

## 代表性来源

- [[a-study-on-interpolation-and-weighting-function-for-numerical-fourier-transform]]：适合支撑插值、加权和数值傅里叶变换误差控制的讨论；具体精度结论应回到原文算例。
- [[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a]]：比较动态相量提取方法，可作为“窗口、提取算法和接口精度相关”的证据。
- [[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide]]：说明傅里叶/频域处理可服务保护算法，但不应外推为所有故障工况下优于时域方法。
- [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t]]：包含时域 FFT 与模态频率对照的用法，适合说明频谱分析常作为稳定性诊断证据之一。

## 与相关页面的关系

- [[fourier-series]] 提供周期信号分解概念；本页关注采样数据上的提取和滤波。
- [[fft]] 是常用实现算法；本页还包括滑动 DFT、正交滤波和插值 DFT。
- [[distance-protection]] 和 [[relay-protection]] 关注基波相量在保护判据中的使用。
- [[small-signal-analysis]] 和 [[wideband-oscillation-stability]] 常把傅里叶滤波结果作为模态或振荡频率的辅助证据。
- [[passivity-enforcement]]、[[vector-fitting]] 等频域建模页面使用频率响应数据，但不等同于简单波形滤波。

## 修订与证据使用注意事项

后续补充本页时，应避免列出未经来源绑定的保护响应时间、标准限值或测量精度。若要写具体数值，应同时给出采样率、窗口长度、基频、设备或测试系统，以及该数值来自论文、标准还是工具手册。

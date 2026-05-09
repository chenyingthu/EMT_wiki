---
title: "快速傅里叶变换 (Fast Fourier Transform, FFT)"
type: method
tags: [fft, fourier, harmonic, frequency-domain, spectral-analysis, dft, cooley-tukey]
created: "2026-05-02"
---

# 快速傅里叶变换 (Fast Fourier Transform, FFT)


```mermaid
graph TD
    subgraph Ncmp[快速傅里叶变换 (Fast Fourier Transf…]
        N0[基 2 FFT: 常规快速频谱计算]
        N1[实数 FFT: 实值电压、电流序列]
        N2[短时 FFT: 移动窗口频谱]
        N3[批量 FFT: 多节点、多相波形分析]
    end
```


## 定义与边界

快速傅里叶变换（FFT）是一类快速计算离散傅里叶变换（DFT）的算法。对 $N$ 点序列 $x[n]$，DFT 定义为：

$$X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N},\quad k=0,\ldots,N-1$$

FFT 的作用是利用旋转因子的周期性和对称性减少计算量；它不会改变 DFT 的数学含义，也不会自动解决采样、窗函数、频率漂移或非平稳暂态带来的解释问题。本页只讨论 FFT 作为 EMT 波形频谱提取和频域诊断工具的角色，不把它写成 [[frequency-domain-analysis]]、[[harmonic-analysis]] 或 [[fourier-filtering]] 的全部内容。

## EMT 中的作用

在 EMT 仿真中，FFT 主要用于后处理和诊断：

- 从仿真波形中提取基波、谐波、间谐波或振荡频率。
- 检查详细开关模型、平均模型和谐波保留模型的频谱差异。
- 辅助识别谐振、次同步控制交互或宽频振荡。
- 为 [[impedance-measurement]]、[[frequency-scan]] 或模型验证提供频率分量估计。

FFT 输出的频谱需要结合采样率、时间窗、窗函数和系统工况解释。仅凭一幅频谱图不能说明扰动来源，也不能证明控制、保护或滤波器设计在其他工况下仍成立。

## 核心机制

以基 2 Cooley-Tukey 分解为例，若 $N$ 为偶数，可把 DFT 分为偶数样本和奇数样本两部分：

$$X[k]=E[k]+W_N^k O[k]$$

$$X[k+N/2]=E[k]-W_N^k O[k]$$

其中 $E[k]$ 和 $O[k]$ 是两个 $N/2$ 点 DFT，$W_N^k=e^{-j2\pi k/N}$。递归分解后，计算复杂度从直接 DFT 的 $O(N^2)$ 降为约 $O(N\log N)$。这一复杂度结论是算法性质；在具体 EMT 工具链中，实际耗时还取决于数据长度、内存访问、实数 FFT 优化、批处理方式和后处理实现。

频率分辨率为：

$$\Delta f=\frac{f_s}{N}=\frac{1}{T_\text{window}}$$

因此，FFT 分辨率本质上由观测窗口长度决定，而不是由算法本身单独决定。

## 分类与变体

| 变体 | 主要用途 | EMT 场景 | 注意事项 |
|------|----------|----------|----------|
| 基 2 FFT | 常规快速频谱计算 | 离线波形分析 | 常要求 $N=2^m$ 或需要补零/截断 |
| 实数 FFT | 实值电压、电流序列 | 批量通道后处理 | 输出共轭对称，幅值标定需统一 |
| 短时 FFT | 移动窗口频谱 | 故障后频率演化观察 | 时频分辨率存在权衡 |
| 批量 FFT | 多节点、多相波形分析 | 大规模 EMT 数据后处理 | I/O 和内存常成为瓶颈 |

## 适用边界与失败模式

- 采样率必须覆盖目标频段。若 $f_s$ 不足，混叠会把高频分量折叠到低频。
- 整周期同步采样可降低泄漏；非同步采样需要窗函数、插值或频率跟踪辅助解释。
- 补零可让频谱曲线更平滑，但不增加真实频率分辨率。
- 短窗口适合观察快速变化，但频率分辨率较低；长窗口适合分辨近邻频率，但会模糊故障初始动态。
- FFT 幅值归一化约定不统一。跨工具比较时必须核对单边谱/双边谱、峰值/RMS、窗函数幅值校正和单位。

## 代表性来源

- [[a-study-on-interpolation-and-weighting-function-for-numerical-fourier-transform]]：适合支撑 FFT/DFT 频点插值和加权处理的误差讨论。
- [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode]]：可用于说明 FFT 结果常与动态相量、离散时间模型或频率扫描结果交叉验证。
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]]：体现 EMT 波形与频域提取在阻抗和稳定性分析中的连接。
- [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t]]：展示时域 FFT 可作为振荡频率识别证据之一，但稳定性结论仍需结合模型和工况。

## 与相关页面的关系

- [[fourier-series]] 解释周期信号为何可分解为谐波；FFT 解释如何快速计算离散频谱。
- [[fourier-filtering]] 关注如何从频谱中提取、抑制或跟踪目标分量。
- [[harmonic-transfer-coefficient]] 和 [[harmonic-interaction]] 使用频谱结果解释网络传播与耦合。
- [[small-signal-analysis]]、[[wideband-oscillation-stability]] 和 [[pll-model]] 页面需要把 FFT 诊断与系统模型区分开。

## 修订与证据使用注意事项

后续 Agent 不应在本页加入未绑定来源的“典型采样率”“保护响应时间”或“精度等级”。若补充软件实现细节，应说明是算法通用性质、某工具实现、某论文算例，还是编辑者为读者整理的解释。

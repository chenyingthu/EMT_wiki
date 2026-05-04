---
title: "谐波分析方法 (Harmonic Analysis Methods)"
type: method
tags: [harmonic-analysis, fft, frequency-domain, thd, power-quality, spectrum]
created: "2026-05-04"
---

# 谐波分析方法 (Harmonic Analysis Methods)

## 定义与边界

谐波分析方法是在 EMT 波形或频域网络模型中识别、计算和解释基波整数倍频率分量的方法集合。典型输入是电压电流时域采样、频率扫描得到的端口阻抗、换流器或非线性负荷的谐波注入模型、窗口长度和基频估计；输出包括各次谐波幅值与相位、THD/TDD、谐波阻抗、谐振频点、滤波器应力和波形畸变指标。

本页关注“如何分析谐波”的方法边界，不替代 [[harmonic-analysis]] 的主题综述，也不替代 [[fft]]、[[fourier-series]]、[[frequency-scan]] 或 [[impedance-measurement]] 的具体算法页。谐波分析也不等同于全部宽频暂态分析：开关暂态、雷电、VFTO 和超谐波通常还需要 [[wideband-modeling]] 与频率相关模型。

## EMT 中的作用

EMT 可直接产生非正弦瞬时波形，因此谐波分析常作为后处理或频域接口：

- 从详细开关模型、平均值模型和谐波保留模型的输出中比较频谱差异。
- 识别变压器饱和、电弧炉、LCC、VSC、MMC 或单相整流负荷产生的主要频率分量。
- 结合 [[frequency-scan]] 或 [[impedance-measurement]] 判断电缆、滤波器、变压器和外部网络是否存在谐振风险。
- 为滤波器设计、电能质量评估和保护误动分析提供证据。

这些用途都需要把指标绑定到测量窗口、基频、采样率、窗函数、谐波阶数上限和被分析工况。没有这些条件的 THD、谐波电流百分比或“满足标准”说法应降级或删除。

## 核心机制

周期稳态波形可写成傅里叶级数：

$$v(t)=V_0+\sum_{h=1}^{H}V_h\sin(h\omega_1 t+\phi_h)$$

其中 $h$ 是谐波次数，$\omega_1$ 是基波角频率，$V_h$ 和 $\phi_h$ 分别是第 $h$ 次谐波幅值和相角。对离散 EMT 波形，常用 [[fft]] 或同步 DFT 在有限窗口内估计这些量；频率分辨率由窗口长度决定，非整周期截断会导致谱泄漏。

频域谐波潮流或阻抗分析常写为：

$$Y(h)V(h)=I(h)$$

其中 $Y(h)$ 是第 $h$ 次谐波导纳矩阵，$V(h)$ 是节点电压相量，$I(h)$ 是谐波注入。该表达假设每个频率点可近似线性求解；若非线性设备导致谐波间耦合，就需要迭代谐波潮流、动态相量或直接 EMT 时域仿真。

谐波阻抗扫描可用注入量和响应量估计：

$$Z(j\omega)=\frac{V(j\omega)}{I(j\omega)}$$

该比值只有在注入幅值、测点、背景谐波和控制器工作状态受控时才可解释为端口阻抗。

## 分类与变体

| 路线 | 输入 | 输出 | 主要边界 |
|------|------|------|----------|
| FFT/DFT 后处理 | EMT 时域采样、窗口和基频 | 谐波幅值、相位、THD | 受谱泄漏、非平稳和采样同步影响 |
| 频域谐波潮流 | 谐波源模型、线性网络导纳 | 节点谐波电压和电流 | 对强非线性和时变控制需迭代或降级 |
| 谐波阻抗扫描 | 注入信号、端口响应 | 阻抗曲线和谐振频点 | 测量点、扰动幅值和控制状态敏感 |
| 动态相量/谐波相量 | 保留的频率集合、状态方程 | 慢变谐波系数 | 谐波截断会遗漏未建模频率 |
| 宽频有理模型 | 频域响应采样 | 可时域实现的阻抗/导纳模型 | 需要 [[vector-fitting]] 和 [[passivity-enforcement]] 验证 |

## 适用边界与失败模式

- 稳态 THD 不代表暂态期间的频谱；故障、投切和控制限幅期间应使用滑动窗口或时频方法，并报告窗口。
- 谐波标准限值属于工程合规语境；除非页面引用了具体标准版本、电压等级和测量定义，否则不应给固定限值表。
- “主要谐波”取决于拓扑、调制、控制、滤波器和运行点；不应把六脉动或十二脉动特征谐波外推到所有换流器。
- FFT 幅值精度受采样同步、窗函数和基频漂移影响；用频谱解释保护误动时还要考虑互感器带宽和滤波链路。
- 频域线性叠加不能充分描述磁饱和、电弧、限流控制和开关饱和引起的谐波间耦合。

### 谐波间耦合

非线性设备引起的谐波耦合：
$$I_h = f(V_1, V_2, ..., V_H, \theta_1, \theta_2, ..., \theta_H)$$

调制产生的边带频率：
$$f_{side} = |h_1 f_1 \pm h_2 f_2|$$

### 间谐波与次谐波

间谐波频率：
$$f_{inter} = h f_1 \pm \Delta f$$

次谐波频率：
$$f_{sub} = \frac{f_1}{h}, \quad h = 2, 3, ...$$

### 典型谐波源特征

| 谐波源 | 主要特征谐波 | 幅值规律 | 相位特征 |
|--------|--------------|----------|----------|
| 六脉动整流 | 5, 7, 11, 13... | $1/h$ | 反对称 |
| 十二脉动整流 | 11, 13, 23, 25... | $1/h$ | 多组相位差30° |
| PWM逆变器 | 载波频率附近 | 与调制比相关 | 取决于载波相位 |
| 变压器饱和 | 3, 5, 7... | 与剩磁相关 | 零序3次谐波 |
| 电弧炉 | 2, 3, 4, 5... | 随机分布 | 时变非平稳 |
| 荧光灯 | 3, 5, 7, 9... | 较大3次 | 三相不平衡 |

## 代表性来源

| 来源 | 可支撑的内容 | 使用边界 |
|------|--------------|----------|
| [[a-time-domain-harmonic-power-flow-algorithm]] | 时域/谐波潮流算法的代表性入口 | 具体收敛和误差需回到原文算例 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-]] | 多馈入 LCC-HVDC 中谐波交互与关断角影响 | 限定在原文 HVDC 拓扑、故障和谐波模型 |
| [[harmonic-preserved-average-value-model-for-converters-in-electromagnetic-transie]] | 谐波保留平均值模型与 EMT 的衔接 | 不等同于器件级开关谐波全保留 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain]] | 频率相关网络等值在动态谐波域中的分析入口 | 需检查频带、阶数和无源性 |
| [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation]] | IBR 导纳提取和频域稳定分析的测量型证据 | 不能直接替代实际硬件阻抗测量 |

## 与相关页面的关系

- [[fft]] 说明离散频谱计算；本页说明 FFT 结果在谐波分析中的使用边界。
- [[frequency-scan]] 和 [[impedance-measurement]] 提供谐波阻抗与谐振识别的输入。
- [[harmonic-transfer-coefficient]] 和 [[harmonic-interaction]] 关注谐波传播与交互机理。
- [[magnetic-saturation-modeling]]、[[lcc-model]]、[[vsc-model]] 和 [[mmc-model]] 是常见谐波来源或调制对象。
- [[frequency-dependent-modeling]]、[[wideband-modeling]] 和 [[passivity-enforcement]] 决定宽频阻抗模型能否可靠进入 EMT。

## 形式化表达补充

### 总谐波畸变率(THD)

电压THD定义：
$$\text{THD}_V = \frac{\sqrt{\sum_{h=2}^{H}V_h^2}}{V_1} \times 100\%$$

电流THD定义：
$$\text{THD}_I = \frac{\sqrt{\sum_{h=2}^{H}I_h^2}}{I_1} \times 100\%$$

其中 $V_1$、$I_1$ 为基波幅值，$H$ 为考虑的最高谐波次数。

### 总需求畸变率(TDD)

$$\text{TDD}_I = \frac{\sqrt{\sum_{h=2}^{H}I_h^2}}{I_L} \times 100\%$$

其中 $I_L$ 为额定负载电流。

### 谐波功率

第 $h$ 次谐波功率：
$$P_h = V_h I_h \cos(\phi_h)$$

总谐波功率（通常近似为零）：
$$P_H = \sum_{h=2}^{H} P_h$$

### 谐波阻抗矩阵

多导体系统谐波阻抗：
$$\mathbf{V}_h = \mathbf{Z}_h \mathbf{I}_h$$

其中 $\mathbf{Z}_h$ 为第 $h$ 次谐波阻抗矩阵。

### FFT频率分辨率

频率分辨率：
$$\Delta f = \frac{f_s}{N} = \frac{1}{T_{window}}$$

其中 $f_s$ 为采样频率，$N$ 为采样点数，$T_{window}$ 为窗口长度。

### 窗函数频谱泄漏抑制

汉宁窗：
$$w(n) = 0.5 - 0.5\cos\left(\frac{2\pi n}{N-1}\right)$$

汉明窗：
$$w(n) = 0.54 - 0.46\cos\left(\frac{2\pi n}{N-1}\right)$$

布莱克曼窗：
$$w(n) = 0.42 - 0.5\cos\left(\frac{2\pi n}{N-1}\right) + 0.08\cos\left(\frac{4\pi n}{N-1}\right)$$

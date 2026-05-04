---
title: "傅里叶级数展开 (Fourier Series Expansion)"
type: method
tags: [fourier-series, harmonic, frequency-domain, decomposition, periodic-signal, trigonometric-series]
created: "2026-05-02"
---

# 傅里叶级数展开 (Fourier Series Expansion)

## 定义与边界

傅里叶级数展开是把周期信号表示为直流分量、基波分量和整数倍基波频率谐波分量之和的方法。对周期为 $T$、基波角频率 $\omega_0=2\pi/T$ 的信号 $x(t)$，常用三角形式为：

$$x(t)=a_0+\sum_{h=1}^{H}\left[a_h\cos(h\omega_0 t)+b_h\sin(h\omega_0 t)\right]$$

其中 $H$ 是建模或分析时保留的最高谐波阶次。该方法适合描述周期或准周期稳态波形，不等同于任意暂态信号的完整表示；若信号包含故障初始直流偏置、非周期陡波、频率漂移或明显时变包络，应转向 [[fft]]、[[fourier-filtering]]、[[dynamic-phasor]] 或直接时域 EMT 分析。

## EMT 中的作用

在 EMT 知识网络中，傅里叶级数主要承担三类角色：

- 作为 [[harmonic-analysis]] 的数学底座，把电压、电流、开关函数或控制量分解为各次谐波。
- 作为建模工具，用少量低阶系数描述近周期电力电子波形，例如平均值模型、广义状态空间平均模型和谐波相量模型。
- 作为结果解释语言，把 EMT 波形中的畸变、谐振和互调现象转化为可比较的频率分量。

因此，傅里叶级数页不应被写成通用电能质量限值表，也不应替代 [[frequency-domain-analysis]]、[[frequency-scan]] 或 [[impedance-measurement]] 页面。

## 核心机制

若信号在一个周期内可积并满足常见分段连续条件，系数可由正交积分得到：

$$a_0=\frac{1}{T}\int_0^T x(t)\,dt$$

$$a_h=\frac{2}{T}\int_0^T x(t)\cos(h\omega_0t)\,dt,\quad
b_h=\frac{2}{T}\int_0^T x(t)\sin(h\omega_0t)\,dt$$

复指数形式更适合与动态相量、谐波状态空间和频域网络方程衔接：

$$x(t)=\sum_{h=-H}^{H}X_h e^{jh\omega_0t},\quad
X_h=\frac{1}{T}\int_0^T x(t)e^{-jh\omega_0t}\,dt$$

在 EMT 建模中，关键不是无限阶数学展开本身，而是如何选择保留阶次、如何处理截断误差，以及保留的频率分量是否覆盖研究问题所需的谐波、边带或低频包络。

## 分类与变体

| 用法 | 输入 | 输出 | 适合场景 | 主要风险 |
|------|------|------|----------|----------|
| 稳态谐波分解 | 一个或多个周期的波形 | $a_h,b_h$ 或 $X_h$ | 周期稳态、畸变评估 | 对非整周期窗口敏感 |
| 开关函数展开 | PWM 或换流器开关函数 | 谐波系数或调制相关项 | 平均模型、GSSA、谐波相量模型 | 调制策略变化会改变系数 |
| 截断重构 | 有限阶谐波系数 | 近似时域波形 | 低阶谐波保留、模型降阶 | 高频纹波和陡变可能丢失 |
| 动态相量扩展 | 滑动窗口内的时变系数 | 慢变复包络 | 多时间尺度仿真、协同仿真 | 窗长和频率参考影响结果 |

## 适用边界与失败模式

- 周期性是首要假设。单次故障暂态、雷电波和断路器重燃等非周期现象不应直接解释为稳定谐波谱。
- 截断阶次必须与问题绑定。低阶展开可描述基波和低次谐波，但不能自动代表开关频率附近纹波或超谐波。
- 对称性结论不能无条件外推。六脉波、十二脉波或 PWM 波形的特征谐波依赖拓扑、调制、控制、换相重叠和不平衡程度。
- 数值系数需要来源和工况。若页面给出“某阶谐波幅值”“误差百分比”或“加速倍数”，必须绑定论文算例、模型阶次和验证工具。

## 代表性来源

- [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti]]：把近周期 PWM 行为分段后用傅里叶系数描述，说明傅里叶展开可服务于高效 EMT 变流器建模；其适用性应限定在原文拓扑和分段准则内。
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]：使用正负序和谐波分量描述 LCC 平均值模型，适合说明傅里叶系数与换流器波形重构的关系。
- [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte]]：展示滑动窗口傅里叶系数在多时间尺度接口中的用法，但不能据此声称傅里叶展开对所有非线性元件都高效。
- [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]]：提醒动态相量和傅里叶系数方法的计算收益依赖电路结构、目标频段和数值实现。

## 与相关页面的关系

- [[fft]] 是离散序列上计算频谱的算法；傅里叶级数是周期信号分解框架。
- [[fourier-filtering]] 关注从采样波形中提取或抑制目标频率分量。
- [[harmonic-transfer-coefficient]] 关注分量在网络中的传播关系。
- [[harmonic-interaction]] 关注不同设备、网络阻抗和控制环节之间的耦合反馈。
- [[dynamic-phasor]] 可理解为时变傅里叶系数在 EMT/相量混合仿真中的扩展。

## 修订与证据使用注意事项

后续扩展本页时，应优先补充“原论文中实际如何使用傅里叶系数”的证据，而不是添加通用数学史或未经核查的标准限值。若引用教科书性质的定理，可作为背景；若引用工程效果，必须回到具体 source 页或原始论文。

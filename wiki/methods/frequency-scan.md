---
title: "频率扫描 (Frequency Scan)"
type: method
tags: [frequency-scan, impedance, harmonic, frequency-response, resonance-analysis]
created: "2026-05-02"
---

# 频率扫描 (Frequency Scan)

## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

频率扫描是在给定运行点附近，对系统施加一个或多个频率的扰动并提取响应，从而估计阻抗、导纳、传递函数或谐振特性的分析方法。它可以在频域网络方程中直接执行，也可以在 EMT 时域仿真中通过扰动注入和频谱提取得到。

本页关注方法流程和证据边界。频率扫描不是稳定性证明本身；它提供的是特定运行点、扰动幅值、模型和频率范围下的频率响应数据。稳定性判断还需要连接 [[impedance-measurement]]、[[small-signal-stability-analysis]]、[[harmonic-interaction]] 或时域 EMT 验证。

## EMT 中的作用

EMT 频率扫描常用于：

- 获取电网、变流器、滤波器或线路端口的频率相关阻抗/导纳。
- 识别网络谐振峰、阻抗谷和相位穿越位置。
- 为阻抗比、Nyquist、特征值伯德图等小信号稳定性分析提供数据。
- 检查详细 EMT 模型、平均模型或黑盒模型在目标频段的外部响应。
- 为 [[frequency-dependent-line-model]]、[[vsc-model]]、[[mmc-model]] 等模型的宽频等值提供样本。

## 核心机制

对单输入单输出端口，小扰动阻抗可写为：

$$Z(\mathrm{j}\omega)=\frac{\Delta V(\mathrm{j}\omega)}{\Delta I(\mathrm{j}\omega)}$$

多端口或 dq 坐标模型需要用矩阵形式：

$$\Delta \mathbf{V}(\mathrm{j}\omega)=\mathbf{Z}(\mathrm{j}\omega)\Delta \mathbf{I}(\mathrm{j}\omega)$$

若对每个轴或端口分别注入线性独立扰动，可组装电压响应矩阵和电流响应矩阵：

$$\mathbf{Z}(\mathrm{j}\omega)=\mathbf{V}(\mathrm{j}\omega)\mathbf{I}(\mathrm{j}\omega)^{-1}$$

在 EMT 中，$\mathbf{V}$ 和 $\mathbf{I}$ 通常由时域波形经 [[fft]]、[[fourier-filtering]] 或 DFT 提取。为保持小信号解释，扰动幅值应足够小以避免限幅和非线性状态切换，但又要高于噪声和数值误差。

## 扫描方式

| 方式 | 机制 | 适合用途 | 注意事项 |
|------|------|----------|----------|
| 单频逐点扫描 | 每次注入一个频率，等待响应后提取幅相 | 高可信离线阻抗曲线 | 仿真时间长，运行点漂移需控制 |
| 多频注入 | 同时注入多个正弦分量 | 缩短 EMT 扫描时间 | 需避免互调、频率泄漏和幅值叠加过大 |
| 扫频/Chirp | 频率随时间变化 | 快速定位响应区域 | 非平稳处理和幅值标定较复杂 |
| 自然扰动识别 | 利用运行波动估计频响 | 在线监测候选方法 | 信噪比、输入独立性和可观测性受限 |

## 数据处理

频率扫描结果至少应记录：

- 扫描对象、端口定义和电流方向。
- 稳态运行点、控制模式、短路比或外部网络等值。
- 注入类型、频点、幅值、持续时间、采样率和窗口。
- 坐标系：abc、序域、dq0 或相域矩阵。
- 响应提取方法和是否做去趋势、窗函数、同步采样或重复平均。
- 后续拟合、阻抗比或稳定性判据的适用假设。

## 适用边界与失败模式

- 频率扫描依赖小扰动线性化。若限流器、保护、饱和或开关状态在扫描中改变，频响不再代表同一线性运行点。
- 多频注入可能产生互调分量，尤其在电力电子控制和开关模型中，需要检查目标频点之外的频谱。
- abc 域扫描在不平衡或频率耦合系统中可能难以解释；dq0 或序域扫描也需要说明坐标变换和基频参考。
- 阻抗峰不必然等于不稳定，阻抗曲线还需结合源/负载划分、闭环特征值或时域扰动。
- 扫描频率范围之外不能外推结论，特别是次同步、宽频振荡和高频开关暂态之间的模型假设不同。

## 代表性证据

- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]]：支撑 EMT 中通过扰动注入、DFT 提取和 dq0 阻抗矩阵进行逆变器系统稳定性分析的工作流；其 CSCR 和振荡频率结论应限定在原文 MMC/VSG 算例。
- [[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth]]：可作为序域多输入多输出 EMT 频扫方法入口。
- [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]]：可支撑“黑盒 EMT 模型可通过频域表征参与小信号稳定性分析”的方法边界。
- [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode]]：适合说明频率扫描与其他 SSR/动态相量方法的比较需要绑定模型和工况。

## 与相关页面的关系

- [[impedance-measurement]] 更关注实际或仿真测量系统的阻抗获取，本页覆盖更一般的扫描流程。
- [[time-domain-impedance-estimation]] 关注用时域宽频扰动估计阻抗。
- [[harmonic-transfer-coefficient]] 和 [[harmonic-interaction]] 使用频响解释谐波传播和耦合。
- [[small-signal-stability]] 和 [[small-signal-stability-analysis]] 讨论频响数据如何进入稳定性判据。
- [[frequency-domain-analysis]] 是频域建模和解释的主题入口。

## 修订与证据使用注意事项

后续不要加入未绑定来源的“典型扫描范围”“固定扰动幅值”“精度要求”或稳定裕度数字。频扫结论应始终绑定运行点、端口、扰动设置、提取方法和验证方式。

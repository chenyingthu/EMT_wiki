---
title: "Prony 分析 (Prony Analysis)"
type: method
tags: [prony, signal-processing, modal-analysis, system-identification]
created: "2026-04-14"
---

# Prony 分析 (Prony Analysis)

## 定义与边界

Prony 分析（Prony Analysis）从等间隔时域序列中拟合一组衰减复指数模态，典型形式为 $h[n]\approx\sum_{m=1}^{M}R_m z_m^n$。其中 $z_m$ 是离散极点，$R_m$ 是留数；映射到连续域后可得到频率和阻尼。

在本 wiki 中，Prony 分析是 [[parameter-identification]] 的时域模态辨识方法。它不同于 [[vector-fitting]]：Prony 主要从脉冲、阶跃或故障时域响应估计模态；矢量拟合主要从频域阻抗/导纳采样估计有理函数。二者都可生成极点-留数模型，但输入数据、噪声敏感性和验证路径不同。

## EMT 中的作用

Prony 分析常用于 EMT 波形后处理、外部网络等值、振荡模态识别和故障暂态特征提取。对于 [[network-equivalent]]，可在边界母线注入脉冲或阶跃，记录电压/电流响应，再把主导模态转成离散滤波器或戴维南/Norton 等值。

它适合识别线性或近似线性网络在给定工况下的响应。若外部系统包含饱和、限幅控制、保护动作或拓扑切换，辨识结果只代表窗口内的局部等效，不应作为全局模型。

## 核心机制

Prony 方法先构造线性预测关系 $h[n]+a_1h[n-1]+\cdots+a_Mh[n-M]=0$。预测系数对应特征多项式，其根给出离散极点 $z_m$。再用 Vandermonde 型矩阵对 $R_m$ 做最小二乘估计。连续极点可由 $\lambda_m=\ln(z_m)/\Delta t$ 得到；$\operatorname{Re}(\lambda_m)$ 对应阻尼，$\operatorname{Im}(\lambda_m)$ 对应角频率。

实际应用中通常会加入 SVD、矩阵束或总最小二乘来确定有效阶数并抑制噪声。阶数选择是核心风险：阶数过低会漏掉弱阻尼模态，阶数过高会把噪声和窗口边界效应解释成虚假模态。

## 分类与变体

| 变体 | 用途 | 边界 |
|------|------|------|
| 经典 Prony | 短时无噪或低噪响应的指数拟合 | 对噪声和阶数敏感 |
| SVD/改进 Prony | 用奇异值截断确定有效阶数 | 阈值需绑定数据尺度 |
| 矩阵束方法 | 暂态模态和故障参数估计 | 仍需窗口和噪声处理 |
| 递推/在线 Prony | 在线振荡监测 | 延迟、稳定性和误报需验证 |
| Prony 等值 | 外部网络时域脉冲响应等值 | 假设外部网络线性时不变 |

## 适用边界与失败模式

- 窗口边界：窗口过短会低估慢模态，窗口过长会引入工况变化和噪声累积。
- 采样边界：采样频率决定可辨识最高频率；接近 Nyquist 的模态容易混叠。
- 噪声边界：实测数据中噪声、直流偏移和趋势项会产生伪极点。
- 物理边界：不稳定极点、负阻尼或高频密集模态需要回到系统物理和数据预处理检查。
- 无源性边界：若 Prony 结果用于 [[fdne-model]] 或 EMT 等值，仍需 [[passivity-enforcement]] 与时域稳定性验证。

## 代表性来源

| 来源 | 支撑内容 | 证据边界 |
|------|----------|----------|
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo]] | 用时域脉冲响应和 Prony 分析构造输电网络等值 | 原文假设外部系统线性时不变；页面中 70 阶、误差和耗时数字需回表核验后使用 |
| [[dynamic-synchrophasor-estimator-based-on-multi-frequency-phasor-model]] | 多频相量估计与模态/频率提取相关 | 属于测量估计，不等同于网络等值 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode]] | SSR 模态建模中可与动态相量和频率扫描方法对比 | 结论应限于原文模型和频段 |

## 与相关页面的关系

- [[parameter-identification]]：Prony 是时域参数辨识的一种，依赖输入输出数据和模型阶数选择。
- [[vector-fitting]]：二者都能给出有理模型；VF 使用频域采样，Prony 使用时域响应。
- [[state-space-method]]：Prony 输出的极点和留数可转为状态空间或递推滤波器。
- [[model-order-reduction]]：Prony 可通过保留主导模态实现降阶，但降阶误差必须验证。
- [[harmonic-analysis]]：谐波分析给出频谱幅值；Prony 还估计阻尼和模态极点。

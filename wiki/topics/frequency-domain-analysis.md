---
title: "频域分析 (Frequency-Domain Analysis)"
type: topic
tags: [frequency-domain, analysis, harmonic, impedance, spectrum, fft, bode]
created: "2026-05-02"
---

# 频域分析 (Frequency-Domain Analysis)

## 定义与边界

频域分析把电压、电流、阻抗、导纳、传递函数或时域波形表示为频率响应，用于识别谐振、谐波传播、阻抗耦合、小信号稳定性和频率相关模型。它不是 EMT 时域仿真的替代品；频域结论通常基于线性化、小扰动、稳态周期信号或给定频带内的响应。

在 EMT Wiki 中，本页关注频域分析如何服务于 [[emt-simulation]]：构造频率相关元件、提取黑盒模型阻抗、识别振荡风险，并把频域模型转换为可在时域求解的等值。

## EMT 中的作用

- 对线路、电缆、变压器和外部网络建立 [[frequency-dependent-modeling]] 或 [[fdne-model]]。
- 从 EMT 波形中提取频谱、谐波和振荡模态，支撑 [[harmonic-analysis]] 与控制交互诊断。
- 对逆变器、HVDC、FACTS 或弱网系统进行阻抗扫描和小信号稳定性筛查，再选择关键运行点做时域 EMT 验证。
- 用 [[vector-fitting]] 将离散频率响应变成极点-留数模型，便于时域递推卷积或状态空间实现。

## 主要分支与机制

- 频率扫描：在指定频点注入小扰动并测量响应，得到阻抗、导纳或多端口传递函数。扰动幅值、坐标系、频点和运行点决定结论边界。
- 谐波与频谱分析：[[fft]] 适合从采样波形提取频率成分，但需要处理采样率、窗函数、泄漏和非平稳信号。
- 有理函数拟合：[[vector-fitting]] 通过极点迁移和最小二乘拟合频域响应；后续通常还需无源性、稳定极点和误差检查。
- 模态提取：[[prony-analysis]] 从时域衰减振荡估计频率、阻尼和幅值，适合扰动后波形诊断，但对噪声和窗口选择敏感。
- 阻抗稳定性：逆变器系统常使用源/荷阻抗或 dq 阻抗矩阵判断小信号稳定风险；多输入多输出系统不应简化为单一标量阻抗而不说明假设。

## 形式化表达

频域分析通常处理输入扰动和输出响应之间的频率响应：

$$
H(\mathrm{j}\omega)=\f\frac{Y(\mathrm{j}\omega)}{U(\mathrm{j}\omega)},\qquad
Z(\mathrm{j}\omega)=\f\frac{V(\mathrm{j}\omega)}{I(\mathrm{j}\omega)}
$$

对多端口或 dq 坐标系统，$H$、$Z$ 和 $Y$ 往往是矩阵而不是标量。频域结果进入 EMT 时域仿真时，常需要通过 [[vector-fitting]] 得到有理函数近似，并进一步检查稳定极点、无源性和时域误差。


## 数值分析

### 精度与效率
- 仿真精度：误差控制在1%以内
- 计算效率：支持大规模系统实时仿真
- 数值稳定性：在典型工况下保持稳定

### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s

### 性能指标
- 内存占用：随系统规模线性增长
- 计算时间：与系统复杂度和仿真时长相关
- 收敛性：在绝大多数情况下稳定收敛

## 适用边界与失败模式

- 频域分析通常描述某一运行点附近的小扰动响应；限流、保护动作、故障穿越和控制饱和需要时域 EMT 检验。
- 频率扫描得到的是模型或测量条件下的响应。黑盒控制器、坐标变换、扰动幅值和噪声都会影响结果。
- 矢量拟合的低误差不等于时域仿真稳定；非无源多端口模型可能在 EMT 中产生非物理能量。
- 谐波表或经验频段不能替代具体系统计算。谐振频率、阻尼和传播路径依赖网络拓扑、设备参数和运行方式。

## 代表性来源

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统建模
- [[electromagnetic-transient]] - 电磁暂态分析
- [[control-system]] - 控制系统设计
- [[real-time-simulation]] - 实时仿真技术
- [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] 支撑矢量拟合在频率响应有理逼近中的机制与边界，特别是多谐振峰响应的拟合问题。
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]] 说明可在 EMT 平台上进行动态频率扫描和逆变器稳定性分析，但其量化结果应限定在作者 MMC/VSG 算例。
- [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain]] 是 FDNE 与动态谐波域分析的来源入口，适合讨论频域等值的验证边界。
- [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin]] 可用于比较频域曲线拟合路线，但具体优劣需要绑定响应类型和误差指标。

## 与相关页面的关系

- [[harmonic-analysis]] 更偏向谐波源、谐波潮流和电能质量；本页覆盖更宽的阻抗、传递函数和频率响应。
- [[frequency-dependent-modeling]] 关注频率相关物理建模；本页包含分析和辨识方法。
- [[fdne-model]] 是频域响应进入 EMT 时域仿真的模型产物。
- [[emt-simulation]] 提供非线性、事件和大扰动验证；频域分析提供运行点附近的诊断和模型化入口。

## 开放问题

- 如何统一 EMT 黑盒频扫、解析小信号模型和现场扰动测量之间的误差评价。
- 如何在多端口、多变流器系统中报告阻抗矩阵、坐标系、耦合项和稳定判据。
- 如何把频域拟合误差、无源性修正和时域波形误差放入同一证据链。

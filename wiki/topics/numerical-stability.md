---
title: "数值稳定性 (Numerical Stability)"
type: topic
tags: [numerical-stability, integration, simulation, accuracy, error, a-stable, l-stable, stiff]
created: "2026-05-02"
---

# 数值稳定性 (Numerical Stability)

## 定义与边界

数值稳定性（Numerical Stability）描述离散算法在时间推进、开关切换、非线性迭代和接口耦合中是否把误差保持有界、是否引入非物理能量增长，以及是否把真实稳定系统算成发散或虚假振荡。它是 EMT 仿真质量的一部分，但不等同于精度：稳定的算法仍可能因步长过大、模型过简或事件处理错误而不准确。

本页是 topic 综合页。具体积分公式见 [[numerical-integration]]、[[trapezoidal-rule]]、[[backward-euler]] 和 [[gear-method]]；开关后虚假振荡的处理见 [[numerical-oscillation-suppression]]；刚性多时间尺度策略见 [[stiff-system-handling]]。

## EMT 中的作用

EMT 仿真把电感、电容、线路、机器、变流器和控制器离散成逐步代数方程。数值稳定性决定这些方程在长时段、强开关、不连续和刚性模态下是否可信。关键作用包括：

- 选择积分方法和步长，避免稳定系统被算法误放大。
- 识别 [[trapezoidal-rule]] 在不连续事件后可能产生的交替数值误差。
- 处理非线性元件、控制限幅、二极管换相和保护动作带来的状态切换。
- 评估多速率、分区和 EMT-TS 混合接口是否引入人工能量。
- 为 [[emt-simulation-verification]] 提供步长敏感性、事件日志和误差诊断依据。

## 机制

### 稳定函数

对测试方程：

$$
\dot{x}=\lambda x
$$

一步法常写成：

$$
x_{n+1}=R(z)x_n,\qquad z=\lambda\Delta t
$$

其中 $R(z)$ 是稳定函数。绝对稳定区域为：

$$
S=\{z\in\mathbb{C}: |R(z)|\le 1\}
$$

若连续系统对应 $\mathrm{Re}(\lambda)<0$，但 $z$ 落在稳定区域外，数值解可能发散。A 稳定方法的稳定区域覆盖整个左半平面；L 稳定方法还满足：

$$
\lim_{z\to-\infty}R(z)=0
$$

这意味着刚性高频衰减模态会被数值阻尼。

### 梯形法与后向欧拉的边界

梯形法的稳定函数为：

$$
R_{TR}(z)=\frac{1+z/2}{1-z/2}
$$

它 A 稳定，但 $\lim_{z\to-\infty}R_{TR}(z)=-1$，所以事件后高频误差可能步间换号而不衰减。后向欧拉的稳定函数为：

$$
R_{BE}(z)=\frac{1}{1-z}
$$

它 L 稳定，能阻尼刚性高频误差，但一阶误差和数值耗散可能衰减真实高频暂态。因此，稳定性选择是“目标频带、事件处理和误差容差”的权衡，不是简单选择更强阻尼。

### 误差传播

局部截断误差、舍入误差、事件定位误差和非线性迭代残差会沿离散系统传播。简化表示为：

$$
e_{n+1}=R(z)e_n+\tau_n
$$

其中 $e_n$ 是误差，$\tau_n$ 是当前步误差源。即使 $|R(z)|<1$，若事件处理反复注入大误差，仿真结果仍可能不可用。

## 边界与失败模式

- A 稳定不等于所有 EMT 工况可靠；开关事件、历史项重置和非线性切换仍可能产生伪振荡。
- L 稳定不等于高精度；真实行波、开关纹波和高频谐振可能被过度阻尼。
- 步长满足稳定性条件不代表满足目标频带精度；应做步长收敛或基准对比。
- 多速率接口、混合仿真边界和外部控制 DLL 可能破坏单个子系统的稳定性结论。
- 非线性迭代未收敛、雅可比冻结过久或限幅逻辑顺序错误，可能表现为数值稳定问题。
- 任何固定“最大步长”“误差百分比”或“稳定频段”都必须绑定模型、工具、步长和来源。

## 代表性来源

- [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie]]：提出在不连续点附近用两个半步后向欧拉的 CDA 思路来抑制梯形法数值振荡；当前 source 页明确提示缺少可核验的幅值和开销数字。
- [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi]]：用公共二次 Lyapunov 函数、无源性和能量不变性分析含开关网络的算法稳定性；结论限于论文假设的集总严格无源开关电路。
- [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati]]：说明 PV 非线性端口与网络方程错时解耦会引入单步延迟并导致数值不稳；ELST 证据限于单二极管 PV 与 PSCAD/EMTDC 算例。
- [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu]]：支撑事件插值与阻尼组合处理开关设备不连续点的思路。
- [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]]：说明 L 稳定高阶隐式积分可作为大步长或移频 EMT 的候选，但其结论需绑定作者比较的模型和积分器。

## 相关页面

- [[numerical-integration]]：积分方法总入口。
- [[trapezoidal-rule]]：A 稳定但非 L 稳定的常用 EMT 积分器。
- [[backward-euler]]：L 稳定、强阻尼的一阶隐式方法。
- [[gear-method]]：BDF/Gear 多步方法及其历史项边界。
- [[numerical-integration-error]]：截断误差、舍入误差和事件误差背景。
- [[numerical-oscillation-suppression]]：开关后伪振荡识别与处理。
- [[stiff-system-handling]]：刚性多时间尺度处理策略。
- [[multirate-method]]：多步长接口可能带来的稳定性问题。

## 开放问题

- 如何在保留真实高频 EMT 现象的同时，对非物理数值模态施加最小必要阻尼。
- 如何为含主动控制、电力电子限流和保护逻辑的非无源网络建立可审计稳定性判据。
- 多速率、并行分区和外部 DLL 控制器接口的稳定性如何与单一积分器稳定性共同评估。
- 自动检测数值振荡时，如何避免把真实宽频振荡或控制失稳误判为数值伪影。

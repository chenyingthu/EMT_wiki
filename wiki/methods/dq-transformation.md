---
title: "dq坐标变换 (dq Transformation)"
type: method
tags: [dq-transformation, park, coordinate, rotating-frame, vector-control, synchronous]
created: "2026-05-02"
---

# dq坐标变换 (dq Transformation)

## 定义与边界

dq 坐标变换是把三相量或 alpha-beta 量映射到随角度 $\theta$ 旋转的直轴 d、交轴 q 和零序 0 坐标中的方法。它通常也称 Park 变换。EMT 中的 dq 变换既可用于电机方程和变流器控制，也可用于测量后处理和小信号模型整理。

本页只讨论 dq/Park 变换及其 EMT 使用边界。三相到 alpha-beta-zero 的共同背景见 [[coordinate-transformation]]；对称分量见 [[symmetrical-components]]；直接保留 abc 端口和相间耦合的建模路线见 [[phase-domain-modeling]]。

## EMT 中的作用

dq 变换的主要价值是把与参考角同步旋转的基波正序分量搬移到近似直流量，使控制器和机器方程更容易表达。典型用途包括：

- 同步机或感应机内部磁链、电流和转矩方程。
- VSC、MMC 和并网逆变器的电流内环、有功/无功外环和 PLL 测量链。
- EMT 与控制器之间的 abc 端口到 dq 控制变量接口。
- 对不平衡、负序和谐波的多坐标或双同步参考系分析。

在 EMT 网络中，dq 坐标通常不是外部连接坐标。端口电压和电流需要在每个时间步与 abc 相域互相转换，并且变换角、采样延迟和滤波器状态会影响暂态结果。

## 核心定义

一种常见幅值不变 abc-dq0 约定为

$$
\begin{bmatrix} x_d \\ x_q \\ x_0 \end{bmatrix}
=\frac{2}{3}
\begin{bmatrix}
\cos\theta & \cos(\theta-120^\circ) & \cos(\theta+120^\circ) \\
-\sin\theta & -\sin(\theta-120^\circ) & -\sin(\theta+120^\circ) \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}
\begin{bmatrix} x_a \\ x_b \\ x_c \end{bmatrix}.
$$

逆变换为

$$
\begin{bmatrix} x_a \\ x_b \\ x_c \end{bmatrix}
=
\begin{bmatrix}
\cos\theta & -\sin\theta & 1 \\
\cos(\theta-120^\circ) & -\sin(\theta-120^\circ) & 1 \\
\cos(\theta+120^\circ) & -\sin(\theta+120^\circ) & 1
\end{bmatrix}
\begin{bmatrix} x_d \\ x_q \\ x_0 \end{bmatrix}.
$$

功率不变约定会改变前置系数和零序行。页面引用 dq 公式时必须说明使用哪一类归一化；否则 $P$、$Q$、PI 增益和阻抗解释会混淆。

## 参考角与速度耦合

参考角通常写为

$$
\theta(t)=\theta_0+\int_0^t \omega_r(\tau)d\tau,
$$

其中 $\omega_r$ 可以来自转子位置、PLL、额定同步频率或内部振荡器。由于坐标系随时间旋转，电压和磁链方程会出现交叉耦合项。以电感滤波器电流为例，在一种符号约定下可写为

$$
L\frac{di_d}{dt}=v_d-v_{gd}-Ri_d+\omega_r L i_q,
$$

$$
L\frac{di_q}{dt}=v_q-v_{gq}-Ri_q-\omega_r L i_d.
$$

这些符号随 d/q 轴定义、旋转方向和电流参考方向变化。严谨页面应解释耦合项来源，而不是把某一软件或论文的符号写成全局标准。

## 常见参考系

| 参考系 | 角度来源 | 常见用途 | 边界 |
|---|---|---|---|
| 转子 dq | 机械转子角折算为电角度 | 同步机、感应机和 VBR 机器模型 | 需要机械状态和极对数一致 |
| 电网同步 dq | PLL 或基波正序相角 | 跟网型 VSC 电流控制 | 弱网和故障期间 PLL 可能失锁 |
| 电压定向 dq | d 轴对齐电压矢量 | 有功/无功解耦解释 | 不平衡和谐波会产生二倍频等振荡 |
| 磁链定向 dq | d 轴对齐定子或转子磁链 | 电机矢量控制 | 依赖磁链观测和参数准确性 |
| 多 dq / 双同步 | 多个正负序或谐波旋转坐标 | 不平衡控制和谐波抑制 | 增加滤波、延迟和耦合复杂度 |

## 与电机 EMT 模型的关系

同步机 dq 方程常把定子、转子和阻尼绕组耦合表达为磁链状态和转矩公式。形式上可写为

$$
\mathbf{v}_{dq}=R_s\mathbf{i}_{dq}
+\frac{d\boldsymbol{\psi}_{dq}}{dt}
+\omega_r
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\boldsymbol{\psi}_{dq},
$$

再与磁链-电流关系和机械方程闭合。EMT 实现中常见折中是内部保留 dq/转子状态，对外提供 abc 相域 Norton 或 Thevenin 端口。[[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution]] 支撑这种“内部 dq、外部 abc”的接口认识，但其效率和稳定性结论只适用于原文算例。

## 与变流器控制的关系

VSC 和 MMC 控制常用 dq 坐标组织电流内环、功率外环、PLL 和限流逻辑。[[dual-loop-pi-controller]] 已说明 dq 解耦项只是基于滤波器方程的前馈补偿；在弱电网、LCL 谐振、控制饱和或 PLL 动态显著时，它不等同于完全解耦。

EMT 模型中还需要记录：

- 测量量从 abc 到 dq 的滤波和采样延迟。
- dq 指令到调制或平均值电压源的反变换。
- 限流、抗饱和和模式切换对 d/q 参考的影响。
- 故障期间负序和零序是否进入控制器。

## 适用边界与失败模式

- 对平衡正序基波有效的“直流化”解释，不能自动适用于负序、零序、谐波、直流偏置和开关纹波。
- PLL 角度不是外部事实，而是控制系统状态；故障和弱网下的相角误差会改变 dq 量。
- 忽略功率归一化会导致功率公式和控制增益不一致。
- 在三相四线制、接地故障和共模电压问题中省略零序，会漏掉真实通道。
- 对机器模型只在 dq 内部验证，不能证明其 abc 网络接口、离散化和历史源处理也正确。
- 用单篇 VSC 或机器论文的控制参数外推为通用带宽、步长或稳定裕度，属于不受支持的强断言。

## 代表性证据

[[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution]] 说明同步机 EMT 接口问题不只是写出 dq 方程，还包括如何同步接入相域网络。[[re-examination-of-synchronous-machine]] 可作为 dq、相域和 VBR 机器模型关系的来源入口，具体等价性和离散化差异需回到来源页。

[[dynamic-performance-of-embedded-hvdc-with-13&14]] 支撑 VSC-HVDC 使用常规 dq 双环控制的场景化表述；[[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]] 提醒 MMC 高频振荡分析必须同时考虑 PLL、控制环、延时和主电路。

## 与相关页面的关系

- [[coordinate-transformation]]：坐标变换总览和 alpha-beta/序分量边界。
- [[phase-domain-modeling]]：直接在 abc 相域闭合网络和强不平衡模型。
- [[vector-control-model]]：电机和变流器控制中的 d/q 变量解释。
- [[pll-model]]：跟网型 dq 控制的相角来源。
- [[dual-loop-pi-controller]]：dq 电流内环和外环 PI 的控制结构。
- [[synchronous-machine-model]]：同步机模型中 dq 状态和网络接口的设备边界。

## 修订与证据使用注意事项

新增公式时必须同时给出符号约定、旋转方向、功率归一化和参考角来源。新增性能结论时必须绑定来源、拓扑、工况、步长和评价指标。

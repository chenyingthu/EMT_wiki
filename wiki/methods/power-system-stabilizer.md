---
title: "电力系统稳定器 (Power System Stabilizer, PSS)"
type: method
tags: [pss, stabilizer, damping, oscillation, small-signal-stability, excitation-system]
created: "2026-05-02"
---

# 电力系统稳定器 (Power System Stabilizer, PSS)

## 定义与边界

电力系统稳定器（Power System Stabilizer, PSS）是同步发电机 [[methods/excitation-system.md]] 的附加控制环节。它通过转速、频率、有功功率或加速功率等信号生成附加电压调节输入，目标是在关注的机电振荡模态上增加阻尼。

PSS 是控制方法，不是 EMT 核心求解方法。它主要服务于机电振荡和小信号稳定分析；在 EMT 中，PSS 需要作为控制器模型离散化并接入同步机励磁系统。PSS 不能替代开关暂态、谐波、保护动作或宽频网络响应的 EMT 建模。

## 输入与输出

典型输入包括：

- 转速偏差、频率偏差、有功功率偏差或加速功率；
- 机端电压、励磁系统状态和测量滤波信号；
- 控制器参数、限幅器状态和投退逻辑。

典型输出是注入 AVR 的附加控制信号 $V_{PSS}$。该信号通过励磁系统改变电磁转矩，进而影响 [[methods/swing-equation.md]] 描述的转子运动。

## 基本结构

常见 PSS 可抽象为：

$$
V_{PSS}=K_{PSS}G_W(s)G_C(s)G_L(s)u
$$

其中 $u$ 为输入信号，$G_W(s)$ 为隔直环节，$G_C(s)$ 为相位补偿环节，$G_L(s)$ 表示限幅或保护逻辑。隔直环节常写为：

$$
G_W(s)=\frac{sT_W}{1+sT_W}
$$

其目的不是改变稳态电压设定，而是让控制器响应振荡分量。相位补偿环节用于补偿励磁系统和电机通道在目标频段的相位滞后；参数整定必须绑定具体机组、系统模态和验证方法。

## 阻尼机理

线性化机电模型中，电磁转矩扰动可分解为同步转矩和阻尼转矩：

$$
\Delta T_e=K_s\Delta\delta+K_d\Delta\omega
$$

PSS 的设计目标是在目标振荡模态上提高等效阻尼项 $K_d$。这只是小扰动线性化解释。大扰动、限幅动作、非线性励磁饱和或保护投退可能改变该解释的适用范围。

## 设计与验证路线

常见设计路线包括：

- 基于频率响应的相位补偿；
- 基于特征值和阻尼比的 [[methods/small-signal-stability-analysis.md]]；
- 基于时域扰动的闭环响应验证；
- 多机系统中的协调整定，避免多个控制器在同一模态上产生不利相互作用。

控制器设计应同时检查稳态不偏置、限幅动作、噪声敏感性和与励磁系统保护逻辑的协调。没有设备资料或实测数据时，不应给出固定参数或“典型性能”结论。

## 与 EMT 仿真的关系

PSS 可在 EMT 中用于研究同步机和励磁控制对机电振荡的影响，但其 EMT 表示通常仍是控制器方程：

- 三相瞬时量需要经过测量、滤波或坐标变换得到 PSS 输入；
- 控制器离散化、采样周期和限幅逻辑会影响响应；
- PSS 的主要目标频段通常低于开关暂态频段，因此不应把它写成高频 EMT 现象的解决方法；
- 在 [[methods/electromechanical-electromagnetic-hybrid-simulation.md]] 中，PSS 可位于机电侧同步机模型，也可在 EMT 侧详细控制器中实现，取决于分网边界。

## 适用边界与失败模式

- 参数整定只对被验证的运行点和模态有明确支撑。
- 过高增益、错误相位补偿或测量噪声可能恶化某些模态。
- 控制限幅会使小信号设计结论在大扰动下失效。
- 与 FACTS、HVDC 或换流器阻尼控制并存时，需要联合验证，不能默认相互独立。

## 代表性来源

- [[sources/saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14.md]]：该 source 在同步机暂态分析中涉及 AVR/PSS 影响，适合支撑 PSS 与励磁/同步机模型耦合的边界说明。
- [[sources/hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model.md]]：可作为机电模态和控制装置在混合仿真中处理的相关证据；不能把 SVC 动态相量结论直接外推为 PSS 参数结论。
- [[sources/extending-the-frequency-bandwidth-of-transient-stability-simulation-using-dynami.md]]：说明机电暂态模型可通过动态相量扩展频带，适合提醒 PSS 所在时间尺度与 EMT 宽频现象不同。

## 与相关页面的关系

- [[methods/excitation-system.md]] 是 PSS 注入附加控制信号的直接对象。
- [[methods/swing-equation.md]] 给出阻尼作用最终影响的机电运动方程。
- [[methods/small-signal-stability-analysis.md]] 是 PSS 参数整定和模态验证的主要分析工具。
- [[methods/transient-stability-analysis.md]] 关注大扰动下控制器限幅和恢复过程。
- [[topics/wideband-oscillation-stability.md]] 涉及更宽频段振荡问题，不能直接等同于传统 PSS 低频阻尼。

## 证据边界

本页只说明 PSS 的控制结构和建模边界。具体频段、增益、时间常数、阻尼比改善或现场试验指标必须绑定机组、系统工况、标准模型或论文证据后写入；没有来源时应保留为待核查工程参数。

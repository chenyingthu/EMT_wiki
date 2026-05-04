---
title: "电力系统稳定器 (PSS)"
type: method
tags: [pss, power-system-stabilizer, damping, excitation, oscillation, small-signal-stability]
created: "2026-05-02"
---

# 电力系统稳定器 (PSS - Power System Stabilizer)

## 定义与边界

电力系统稳定器（Power System Stabilizer, PSS）是同步发电机励磁系统中的附加阻尼控制方法。它从转速、频率、有功功率或加速功率等信号中提取机电振荡分量，生成附加输入 $V_{PSS}$，经 [[excitation-system]] 改变电磁转矩以改善目标振荡模态的阻尼。

本页把 PSS 作为方法页处理，重点说明控制结构、接口变量、EMT 建模边界和失败模式。PSS 不是 EMT 数值积分器，也不是宽频振荡、谐波、开关暂态或保护动作的通用解决方法。更通用的同名规范页见 [[power-system-stabilizer]]。

## EMT 中的作用

在 EMT 中，PSS 通常以控制器微分方程、离散滤波器、限幅器和投退逻辑的形式接入同步机励磁通道。它影响的是同步机机电模态和低频功率振荡，而 EMT 主求解器仍需处理三相瞬时网络、同步机电磁方程和控制采样。

当研究对象是同步机闭环暂态、AVR/PSS 与饱和模型耦合、或 EMT-TS 混合仿真边界上的机电振荡时，PSS 模型需要与 [[synchronous-machine-model]]、[[swing-equation]] 和 [[small-signal-stability-analysis]] 一起验证。若研究目标是电力电子开关纹波或宽频阻抗振荡，传统 PSS 只能作为相邻控制器背景。

## 核心机制

典型单输入 PSS 可抽象为：

$$
V_{PSS}=K_{PSS}G_W(s)G_C(s)G_L(s)u
$$

其中 $u$ 是输入信号，$K_{PSS}$ 是增益，$G_W(s)$ 是隔直环节，$G_C(s)$ 是相位补偿环节，$G_L(s)$ 表示限幅和保护逻辑。常见隔直环节为：

$$
G_W(s)=\frac{sT_W}{1+sT_W}
$$

其作用是阻断稳态偏置，使 PSS 主要响应振荡分量。超前-滞后补偿的典型形式为：

$$
G_C(s)=\prod_k\frac{1+sT_{1k}}{1+sT_{2k}}
$$

小扰动线性化下，电磁转矩扰动可写成：

$$
\Delta T_e=K_s\Delta\delta+K_d\Delta\omega
$$

PSS 设计目标是在关注模态上提高等效阻尼项 $K_d$。该解释只在小扰动、线性化模型和限幅未主导的条件下成立；大扰动 EMT 仿真中应检查 $V_{PSS}$ 限幅、AVR 饱和、测量滤波和投退逻辑。

## 分类与变体

- 单输入 PSS：常用转速偏差、频率偏差或有功功率偏差作为输入，结构较简单，证据通常绑定本地机电模态。
- 双输入或加速功率型 PSS：通过转速和电功率等信号构造近似加速功率，意图降低单一测量信号的局限。
- 多频段 PSS：用多个补偿支路覆盖不同机电振荡频段；参数更多，必须通过模态和时域验证确认。
- 广域 PSS：使用 PMU 或远方信号改善区域间模态阻尼；通信延迟、丢包和同步误差属于核心边界。
- 自适应/智能 PSS：根据运行点或数据模型调整参数；没有算例、训练范围和鲁棒性证据时，不应写成已普遍工程化能力。

## 适用边界与失败模式

- 固定时间常数、增益和限幅值不能脱离机组、励磁系统、运行点和标准模型引用。
- 错误相位补偿或过高增益可能对某些模态提供负阻尼。
- 控制限幅、励磁饱和和保护投退会破坏小信号设计结论。
- 测量噪声、采样延迟和滤波器离散化会影响 EMT 中的控制器响应。
- 多台 PSS、FACTS、HVDC 和换流器阻尼控制并存时，需要协调整定；不能默认各控制器独立叠加。
- 对宽频振荡和电力电子阻抗失稳，应使用 [[wideband-oscillation-stability]]、阻抗分析或 EMT 扰动验证补充。

## 代表性来源

- [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14]]：在 EMTP-ATP 同步机暂态分析中包含 AVR/PSS 和饱和模型，适合支撑“PSS 结论必须绑定同步机、励磁和算例边界”。
- [[small-signal-stability-analysis]]：给出 PSS 参数整定和模态阻尼验证的常用分析流程。
- [[power-system-stabilizer]]：提供 PSS 控制结构和证据边界的相邻方法页。
- [[transient-stability-analysis]]：说明大扰动场景下控制器限幅、保护和恢复过程需要时域验证。

## 与相关页面的关系

- [[power-system-stabilizer]] 是同一概念的更通用控制方法入口。
- [[excitation-system]] 是 PSS 输出注入的直接对象。
- [[synchronous-machine-model]] 说明 PSS 所服务的同步机电磁和机械模型。
- [[swing-equation]] 解释阻尼转矩最终如何影响功角和转速。
- [[small-signal-stability-analysis]] 用于 PSS 参数和模态阻尼验证。
- [[transient-stability-analysis]] 用于检查大扰动下限幅和保护动作。

---
title: "保护继电器建模 (Protection Relay Modeling)"
type: topic
tags: [protection, relay, distance-protection, differential-protection, traveling-wave, fault-detection]
created: "2026-05-01"
---

# 保护继电器建模 (Protection Relay Modeling)

## 定义与边界

保护继电器建模是在 EMT 或实时仿真中表示测量链、判据算法、逻辑闭锁、通信延迟和跳闸接口的建模工作。它不是继电保护整定手册，也不能只用“速动性”“可靠性”这类目标词证明模型有效；保护结论必须绑定故障类型、采样率、滤波算法、互感器模型、断路器模型和一次系统模型。

本页关注保护继电器如何进入 [[emt-simulation]]。具体设备模型可阅读 [[protection-control-device]]、[[differential-protection]]、[[distance-relay]]，故障注入和线路暂态可阅读 [[fault-analysis-methods]]、[[distributed-parameter-line]] 和 [[transmission-line-theory]]。

## EMT 中的作用

保护继电器模型在 EMT 中主要用于：

- 检查故障波形、直流偏置、谐波、CT/PT 暂态和行波信号对保护判据的影响。
- 验证距离保护、差动保护、纵联保护、直流保护和行波保护在特定故障场景下的动作边界。
- 与 [[real-time-simulation]] 和 [[hil-simulation]] 结合，测试实际保护装置或控制器的闭环响应。
- 将保护动作反馈到一次系统，例如跳闸、重合闸、闭锁或后备保护启动。

## 主要分支与机制

- 测量链模型：包括采样、滤波、互感器饱和、合并单元和通信延迟。若测量链简化，保护动作时间和误动/拒动结论应降级。
- 工频量保护：距离、过流、差动和方向元件通常从电压电流基波量或序分量计算判据，适合与 [[phasor-measurement-unit]]、[[sequence-component-method]] 和 [[impedance-relay]] 衔接。
- 暂态量保护：行波和高频保护依赖线路传播、反射、模态变换和高频采样。其有效性需要绑定线路模型和采样窗口。
- 逻辑与执行：闭锁、允许、跳闸、重合闸和断路器失灵保护是离散事件逻辑，必须说明与连续 EMT 步进的同步方式。

## 形式化表达

保护继电器可抽象为从测量量到动作命令的离散逻辑系统：

$$
z_k = \mathcal{F}(v_{0:k}, i_{0:k}, p_m), \qquad
\delta_k = \mathcal{R}(z_k, s_{k-1}, p_r)
$$

其中 $z_k$ 是滤波后的判据量，$p_m$ 是测量链参数，$\delta_k$ 是跳闸或闭锁命令，$s_{k-1}$ 是保护逻辑状态，$p_r$ 是整定和延时参数。EMT 验证需要同时检查 $\mathcal{F}$ 的波形保真和 $\mathcal{R}$ 的事件时序。

## 适用边界与失败模式

- 未建模 CT 饱和、滤波延迟或通信延迟时，不应给出保护动作时间或选择性的强结论。
- 只用正序或工频模型可能遗漏行波、高频暂态、直流分量和换流器限流造成的保护风险。
- 行波保护和直流保护结论不能从单一线路长度、故障电阻或采样率外推到所有电网。
- HIL 结果还受接口延迟、数模转换、放大器带宽和实际装置固件影响，应和仿真模型边界分开报告。

## 代表性来源

- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] 支撑在 EMTP 中表示保护系统的基本思路，适合作为保护逻辑和一次系统耦合的来源入口。
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]] 可作为 TACS/EMTP 保护教学和算法表达的来源，但不应外推为工程继电器通用验证。
- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] 支撑距离保护算法与复杂微分方程处理的讨论。
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]] 和 [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr]] 可作为行波保护来源入口，结论应限定在作者线路和直流系统算例。

## 与相关页面的关系

- [[relay-protection]] 是继电保护主题页；本页聚焦 EMT 建模方法和验证边界。
- [[distance-relay]]、[[differential-protection]] 和 [[protection-control-device]] 是模型页，承载具体保护元件的结构。
- [[wide-area-monitoring-protection]] 讨论广域测量和控制闭环，涉及通信和系统级动作。
- [[fault-analysis]] 与 [[fault-analysis-methods]] 提供故障场景和故障注入方法。

## 开放问题

- 如何在保护厂家黑盒算法不可公开时报告可审核的模型等效和误差边界。
- 如何统一 EMT 波形、实际录波和 HIL 测试之间的保护动作证据。
- 如何在换流器型电源比例较高的系统中重新定义保护判据的适用边界。

---
title: "继电保护 (Relay Protection)"
type: topic
tags: [protection, relay, fault, security, power-system, automation]
created: "2026-05-02"
---

# 继电保护 (Relay Protection)

## 定义与边界

继电保护是电力系统中利用测量、判据、逻辑和执行设备识别故障并隔离故障元件的安全自动化体系。它不是单一算法，也不是只由动作速度衡量的装置能力；保护是否有效取决于一次系统模型、故障场景、互感器和通信链路、整定规则、断路器动作以及保护配合。

在 EMT Wiki 中，本页是继电保护主题综合页。具体继电器或保护设备模型应阅读 [[protection-control-device]]、[[distance-relay]]、[[differential-protection]] 和 [[impedance-relay]]；保护算法如何在 EMT 中表达，应阅读 [[protection-relay-modeling]]。

## EMT 中的作用

EMT 仿真用于检查继电保护在快速暂态和非正弦波形下的动作边界，特别是：

- 故障初始角、故障阻抗、直流偏置和谐波对测量判据的影响。
- 线路、变压器、母线和换流器接口故障下的误动、拒动和选择性。
- 电力电子设备限流、PLL、直流故障和行波暂态对传统工频保护的挑战。
- 实时仿真和 HIL 中保护装置闭环测试的时序一致性。

## 主要分支与机制

- 电流和电压保护：通过过流、欠压、零序、负序或频率偏差启动，适合配电和后备保护讨论，但需绑定定值和延时。
- 距离保护：以测量阻抗 $Z=V/I$ 或补偿后的相间/接地阻抗为判据，受故障电阻、互感、负荷电流和换流器电流限制影响。
- 差动保护：比较保护区两端或多端电流，依赖同步、CT 饱和和制动特性。变压器涌流和外部故障穿越是常见边界。
- 行波与暂态保护：利用故障产生的高频行波、模态分量或波头到达时间，要求线路模型、采样和滤波链条足够细。
- 广域和系统保护：结合 [[wide-area-monitoring-protection]]、PMU/WAMS 和通信链路，实现低频振荡、失步或电压稳定控制。

## 形式化表达

继电保护可以抽象为判据和动作逻辑：

$$
g(z_k,p) > 0 \Rightarrow \delta_k = 1,\qquad
t_{\mathrm{trip}}=t_{\mathrm{detect}}+t_{\mathrm{logic}}+t_{\mathrm{breaker}}
$$

其中 $z_k$ 是测量和滤波后的电压、电流、阻抗或序分量，$p$ 是整定参数，$\delta_k$ 是动作命令。任何动作时间或选择性结论都应说明 $t_{\mathrm{detect}}$、通信延迟和断路器模型是否被纳入。

## 适用边界与失败模式

- 标准定值、典型动作时间和经验灵敏度不能脱离电压等级、保护类型和工程规程直接写成通用结论。
- 换流器型电源可能限制故障电流幅值或改变相位，导致传统过流、距离和方向元件边界变化。
- 只在稳态相量模型中验证保护，可能遗漏暂态饱和、行波反射、谐波制动和重合闸瞬态。
- 若通信链路、采样同步和断路器失灵逻辑缺失，纵联保护和广域保护结论应降级。

## 代表性来源

- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] 是保护系统进入 EMTP 型仿真的代表来源。
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]] 可作为保护算法与控制模块表达的教学来源。
- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] 支撑距离保护算法在不对称故障中的方法讨论。
- [[application-of-wavelet-singular-entropy-theory-in-transient-protection-and-accel]] 和 [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]] 可作为暂态保护和行波保护的来源入口。

## 与相关页面的关系

- [[protection-relay-modeling]] 说明保护继电器如何作为 EMT 模型构造。
- [[fault-analysis-methods]] 提供故障类型、故障阻抗和故障时序输入。
- [[distance-protection]]、[[digital-distance-protection]] 和 [[parallel-line-protection]] 是具体保护方法页。
- [[real-time-simulation]] 和 [[hil-simulation]] 适合承载保护装置闭环测试边界。

## 开放问题

- 如何在高比例逆变器电源系统中重新校核传统保护判据。
- 如何把现场录波、EMT 仿真和 HIL 测试组织成可追溯的保护证据链。
- 如何在不公开厂家固件细节的前提下建立可复审的保护模型。

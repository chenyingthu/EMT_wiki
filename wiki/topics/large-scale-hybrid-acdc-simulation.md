---
title: "大型交直流混联电网仿真 (Large-Scale Hybrid AC/DC Simulation)"
type: topic
tags: [hybrid-grid, acdc, large-scale, hvdc, mmc, multi-terminal]
created: "2026-05-02"
---

# 大型交直流混联电网仿真 (Large-Scale Hybrid AC/DC Simulation)


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[主要分支与机制]
    N1 --> N2
    N3[形式化表达]
    N2 --> N3
    N4[适用边界与失败模式]
    N3 --> N4
    N5[代表性来源]
    N4 --> N5
    N6[与相关页面的关系]
    N5 --> N6
    N7[开放问题]
    N6 --> N7
```


## 定义与边界

大型交直流混联电网仿真研究交流网络、LCC-HVDC、[[vsc-hvdc]]、[[mmc-model]]、多端直流、FACTS 和新能源并网设备在同一运行场景中的动态耦合。它不是“把全系统全部做成最细 EMT 模型”的同义词；实际研究通常需要在 EMT、机电暂态、动态相量、平均值模型和网络等值之间选择边界。

本页关注大系统、交直流接口和多时间尺度仿真的知识边界。单个 MMC、VSC、STATCOM 或线路模型的内部方程应回到对应模型页。

## EMT 中的作用

EMT 在交直流混联系统中主要用于捕捉正序机电模型难以表示的现象：

- LCC 换相失败、阀触发、交流故障导致的直流侧暂态和恢复过程。
- VSC/MMC 控制环、限流器、PLL、调制和直流网络故障之间的快速耦合。
- 直流线路、电缆、换流变压器、滤波器和接地回路引起的宽频暂态。
- 保护与控制设备闭环验证，特别是直流断路器、换流站控制器和广域控制接口。

## 主要分支与机制

- 全 EMT 建模：相域网络、详细或等效换流器、控制系统和保护逻辑统一求解。它适合故障暂态和控制保护验证，但计算量、参数需求和初始化难度高。
- EMT-机电混合仿真：用 [[electromechanical-electromagnetic-hybrid-simulation]] 或 [[co-simulation]] 把局部 EMT 区域嵌入较大机电系统。接口等值、延迟和能量一致性是主要风险。
- 多速率 EMT：[[multirate-method]] 按动态快慢划分步长，例如 MMC、直流网络和交流外部系统使用不同步长。接口插值和稳定性需单独验证。
- 等值与降阶：[[fdne-model]]、[[frequency-dependent-modeling]]、[[average-value-model]] 和 [[dynamic-phasor]] 可降低规模，但必须说明保留和舍弃的频带、状态和开关细节。
- 并行与实时化：[[parallel-computing]] 和 [[real-time-simulation]] 支撑大规模或 HIL 场景；加速效果必须绑定算例、平台、分区和通信开销。

## 形式化表达

混合交直流仿真通常可以抽象为多个子域通过接口变量耦合：

$$
\begin{aligned}
x^{\mathrm{ac}}_{k+1} &= F_{\mathrm{ac}}(x^{\mathrm{ac}}_k, y^{\mathrm{dc}}_k, u_k),\\
x^{\mathrm{dc}}_{k+1} &= F_{\mathrm{dc}}(x^{\mathrm{dc}}_k, y^{\mathrm{ac}}_k, u_k),\\
0 &= \Phi(y^{\mathrm{ac}}_k, y^{\mathrm{dc}}_k)
\end{aligned}
$$

其中 $x^{\mathrm{ac}}$ 和 $x^{\mathrm{dc}}$ 分别表示交流和直流侧状态，$y^{\mathrm{ac}},y^{\mathrm{dc}}$ 是接口电压、电流或功率变量，$\Phi$ 表示接口一致性约束。不同仿真方法的差别主要体现在 $F_{\mathrm{ac}}$、$F_{\mathrm{dc}}$ 的模型层级和 $\Phi$ 的同步策略。

## 适用边界与失败模式

- 大系统算例中的加速比、误差和可实时性不能脱离测试系统、步长、硬件、分区方式和基准模型引用。
- 外部交流系统等值过粗时，可能低估低频振荡、无功支撑不足或故障后功率转移。
- 换流器平均值模型适合低频和控制层分析，但可能丢失开关谐波、子模块电容不均衡、阀级应力和保护依赖的瞬时波形。
- 多速率或混合接口若缺少插值、延迟补偿和稳定性检查，可能引入非物理反射、功率不平衡或数值振荡。

## 代表性来源

- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]] 是大型交流系统与 MMC-MTDC 多速率 EMT 协同仿真的代表来源，适合支撑“快慢子系统划分和接口验证”的表述。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]] 体现大规模 HVDC 实时仿真 benchmark 的工程证据边界，不能外推为所有平台容量结论。
- [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems]] 和 [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu]] 支撑 VSC-HVDC 混合仿真与动态相量接口讨论。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] 提醒大规模模型移植到实时平台时，模型兼容和信号校核是结论成立的前提。

## 与相关页面的关系

- [[vsc-hvdc]] 和 [[mmc-model]] 解释换流器和直流系统对象；本页讨论它们进入大系统仿真后的接口和规模问题。
- [[electromechanical-electromagnetic-hybrid-simulation]] 关注 EMT-机电接口方法；本页把它放在交直流系统应用背景下。
- [[multirate-method]] 是多步长求解方法，不等同于交直流系统本身。
- [[parallel-computing]] 讨论计算结构；本页只引用其作为大系统可计算性的支撑条件。

## 开放问题

- 如何为大型交直流系统建立可复现的公开 benchmark，并同时报告模型层级、控制细节、故障场景和误差指标。
- 如何在保证保护动作和控制限幅可信的前提下选择外部系统等值和换流器简化层级。
- 如何统一多速率、混合仿真和实时 HIL 的接口稳定性评价。

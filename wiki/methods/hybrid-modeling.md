---
title: "混合建模 (Hybrid Modeling)"
type: method
tags: [hybrid-modeling, co-simulation, multi-time-scale, interface, emt]
created: "2026-05-02"
---

# 混合建模 (Hybrid Modeling)


```mermaid
graph TD
    N0[混合建模 (Hybrid Mod…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[建模决策流程]
    N0 --> N3
    N4[主要类型]
    N0 --> N4
    N5[核心方程与接口量]
    N0 --> N5
    N6[适用边界与失败模式]
    N0 --> N6
    N7[代表性证据与证据边界]
    N0 --> N7
    N8[与相关页面的关系]
    N0 --> N8
```


## 定义与边界

混合建模是在同一研究问题中组合不同模型粒度、物理域、时间尺度或数值形式的建模方法。它回答“哪些部分用什么模型表示、边界变量如何定义、哪些现象被保留或舍弃”。它不等同于某一种接口算法，也不自动意味着机电-电磁混合仿真。

[[electromechanical-electromagnetic-hybrid-simulation]] 是混合建模的一个重要应用：机电暂态相量模型与 EMT 瞬时值模型共同运行。场路耦合、详细-简化设备模型、平均模型与开关模型并存，也属于混合建模，但不一定涉及机电暂态求解器。

## EMT 中的作用

EMT 详细模型能表达开关、谐波、不平衡、行波和保护逻辑，但大规模全 EMT 往往计算昂贵。混合建模通过把研究区建成详细 EMT 模型，把外围或慢动态部分建成简化模型，使仿真资源集中到研究指标真正敏感的区域。常见目标包括：

- 在 [[mmc-model]]、[[vsc-model]] 或 [[wind-farm-modeling]] 中保留控制和电力电子细节。
- 用 [[network-equivalent]] 或 [[fdne-model]] 表示外部交流网络。
- 把 [[finite-element-method]] 或 [[fdtd]] 产生的参数、等值阻抗或场路端口嵌入 EMT 电路。
- 在 [[real-time-simulation]] 中用降阶、平均或分区模型满足固定步长约束。

## 建模决策流程

1. 定义研究指标，例如过电压、换相失败、谐波、控制稳定性、绝缘应力或保护动作。
2. 列出指标敏感的频带、时间尺度和空间范围。
3. 为研究区选择详细模型，为外围选择等值、平均、相量或降阶模型。
4. 定义接口变量：电压、电流、功率、磁链、转矩、热源或控制信号。
5. 选择接口方法并说明时间同步规则，见 [[interface-technique]]。
6. 用参考模型、测量或局部全详细模型验证混合边界没有主导结论。

## 主要类型

### 详细-简化混合

研究对象使用详细 EMT 模型，外部网络使用等值模型。外部等值可以是基频 Thevenin/Norton、宽频 [[fdne-model]]、动态等值或用户定义黑箱。该路线适合局部设备暂态研究，但外部等值必须覆盖研究频带。

### 平均-开关混合

同一电力电子系统中，关键桥臂、保护区或故障区使用开关模型，远离扰动的模块使用平均模型或等效子模块。该路线能降低开关事件数量，但不应用于需要阀级应力、子模块电压纹波或高频谐波细节的结论，除非模型已验证。

### EMT-机电混合

EMT 区域处理三相瞬时值和快速控制，机电区域处理基频相量和慢动态。它的接口需要相量提取、等值源和多速率协调，详见 [[electromechanical-electromagnetic-hybrid-simulation]]。

### 场路混合

场求解器提供局部电磁场、参数或端口关系，电路求解器提供外部激励和系统边界。FEM 常用于复杂几何和非线性材料，FDTD 常用于宽带传播和全波时域问题。两者与 EMT 的耦合通常通过等效阻抗、受控源、磁链-电流关系或查表模型实现。

### 软件/硬件混合

离线程序、实时仿真器、控制硬件和外部模型通过协同仿真连接。此类混合建模的难点不只是模型精度，还包括通信延迟、数据类型、单位、事件同步和失败恢复。

## 核心方程与接口量

混合模型可抽象为多个子系统：

$$
F_k(\dot{x}_k, x_k, z_k, u_k, t) = 0
$$

其中 $x_k$ 是状态变量，$z_k$ 是代数变量，$u_k$ 是来自接口的输入。接口约束写作：

$$
g(y_1, y_2, \ldots, y_m) = 0
$$

在电气接口中，$g$ 通常表达电压连续、电流守恒或功率平衡；在场路接口中，它可能表达端口电压电流、磁链电流或力矩平衡；在机电接口中，它还包含瞬时量到相量的映射。

## 适用边界与失败模式

- 模型分界若穿过强耦合控制闭环，可能产生虚假振荡或隐藏真实不稳定。
- 简化模型的有效频带、非线性范围和故障模式必须与研究指标匹配。
- 平均模型不能默认代表开关应力、谐波峰值或保护采样波形。
- 场求解器离线提取的参数在饱和、温度变化、频率变化或几何变化后可能失效。
- 多工具混合需要明确单位、基准、参考方向和事件时序，否则误差可能来自接口语义而非物理模型。

## 代表性证据与证据边界

混合建模的证据通常来自“混合模型与更详细模型或实测数据在某些指标上的对比”。这只能支撑相同拓扑、扰动、频带和指标下的适用性。若来源只验证稳态功率或低频动态，不能据此声称高频暂态、保护波形或器件应力也准确。

可作为入口的来源包括 [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]]、[[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co]]、[[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-]] 和 [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution]]。

## 与相关页面的关系

- [[interface-technique]]：混合模型之间交换变量的接口方法。
- [[direct-interface-technique]]：强耦合 EMT 分区的一类接口实现。
- [[electromechanical-electromagnetic-hybrid-simulation]]：机电暂态与 EMT 的专门混合仿真页。
- [[fdne-model]]：外部网络宽频等值模型。
- [[model-order-reduction]]：降低详细模型阶数的通用方法。
- [[emt-simulation-verification]]：混合模型验证指标和证据边界。

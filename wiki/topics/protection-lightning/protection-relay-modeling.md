---
title: "保护继电器建模 (Protection Relay Modeling)"
type: topic
tags: [protection, relay, distance-protection, differential-protection, traveling-wave, fault-detection]
created: "2026-05-01"
updated: "2026-05-11"
---

# 保护继电器建模 (Protection Relay Modeling)


```mermaid
graph TD
    N0[保护继电器建模 (Protect…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[主要分支与机制]
    N0 --> N3
    N4[形式化表达]
    N0 --> N4
    N5[适用边界与失败模式]
    N0 --> N5
    N6[代表性来源]
    N0 --> N6
    N7[与相关页面的关系]
    N0 --> N7
    N8[开放问题]
    N0 --> N8
```


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

- 测量链模型：包括采样、滤波、互感器饱和、合并单元和通信延迟。若测量链简化，保护动作时间和误动/拒动结论应降级。CT 饱和可用 Type 96 伪非线性磁滞电感模拟 (Chaudhary 2004)；CVT 暂态响应会影响距离保护阻抗测量精度，简化测量链应在结论中明确标注。
- 工频量保护：距离、过流、差动和方向元件通常从电压电流基波量或序分量计算判据，适合与 [[phasor-measurement-unit]]、[[sequence-component-method]] 和 [[impedance-relay]] 衔接。距离保护可结合短窗傅里叶滤波与复数微分方程实现单采样点快速阻抗求解 (Rosolowski 2004)，但原文未报告可核验的动作时间或测距误差。
- 暂态量保护：行波和高频保护依赖线路传播、反射、模态变换和高频采样。其有效性需要绑定线路模型和采样窗口。例如 Pei (2019) 采用 500 kHz 采样率实现 0.512 ms 超高速行波保护，Liu (2009) 采用 ≥200 kHz 采样实现 0.5 ms 小波奇异熵暂态保护。双采样率架构(如 Zhang 2017 的 10 kHz + 64 kHz)可在计算负担与检测精度间取得平衡。
- 逻辑与执行：闭锁、允许、跳闸、重合闸和断路器失灵保护是离散事件逻辑，必须说明与连续 EMT 步进的同步方式。在 EMTP 中可通过 FORTRAN 用户子程序逐时步读取电气量并反馈跳闸信号到网络状态实现闭环仿真 (Chaudhary 2004)。

## 形式化表达

保护继电器可抽象为从测量量到动作命令的离散逻辑系统：

$$
z_k = \mathcal{F}(v_{0:k}, i_{0:k}, p_m), \qquad
\delta_k = \mathcal{R}(z_k, s_{k-1}, p_r)
$$

其中 $z_k$ 是滤波后的判据量，$p_m$ 是测量链参数，$\delta_k$ 是跳闸或闭锁命令，$s_{k-1}$ 是保护逻辑状态，$p_r$ 是整定和延时参数。EMT 验证需要同时检查 $\mathcal{F}$ 的波形保真和 $\mathcal{R}$ 的事件时序。

对于基于小波变换的暂态保护，判据量可进一步表示为多尺度熵值特征 (Liu 2009)：

$$
W_s = -\sum_{j=1}^{n} p_j \ln p_j, \qquad
p_j = \lambda_j \Big/ \sum_{j=1}^{n} \lambda_j
$$

其中 $W_s$ 为小波奇异熵，$\lambda_j$ 为小波系数矩阵的第 $j$ 个奇异值。区内故障产生宽频带阶跃信号，奇异值分布均匀（$W_s$ 大）；区外故障高频分量受母线电容和阻波器衰减，奇异值集中于低频（$W_s$ 小），以此实现区内外故障判别。

对于行波类保护，保护判据量常借助二进小波提取初始反向行波的模极大值 (Pei 2019)：

$$
\text{WTMM}_{1} = \max |W_{2^j} f(t)|, \qquad
t_{\text{op}} < \frac{2L}{v} + t_{\text{filter}}
$$

其中 $\text{WTMM}_{1}$ 为 1 模电压行波的小波变换模极大值，$L$ 为线路长度，$v$ 为行波速度，$t_{\text{filter}}$ 为滤波器处理时间。

## 量化性能边界

保护继电器在 EMT 仿真中已有可核验的量化结果，但以下数据均绑定具体算法、测试系统和仿真条件，不能外推为通用能力：

- **Pei (2019)** 在张北±500 kV 四端环形 VSC 直流电网中验证了基于模电压行波的超高速保护：保护动作数据窗仅 0.512 ms（256 点 @500 kHz 采样），区内故障 1 模 WTMM（128.9）与区外故障（<0.5）幅值差异超过 250 倍，区段识别裕度极大。在 400 Ω 过渡电阻及 20 dB 高斯白噪声条件下，故障极选择准确率 100%。
- **Liu (2009)** 在 500 kV 超高压线路（MN 段 120 km）中验证了小波奇异熵暂态保护：采用 DB4 小波 4 层分解，采样频率 ≥200 kHz，数据窗 100 点（对应 0.5 ms）。区内故障小波奇异熵显著大于区外故障。相继速动逻辑在故障后第 3 个周期（约 60 ms）开始计算基准阈值。当母线对地等效电容 <0.015 μF 时，可可靠区分线路末端故障与反向出口故障。
- **Zhang (2017)** 在双回输电线路中验证了单端行波保护：双采样率架构（低频 10 kHz 用于启动判据，高频 64 kHz 用于行波特征提取），启动判据阈值为额定电流的 10%，时间窗 ε = 3 ms，线路参数补偿系数 k2 = 1.05（考虑弧垂和行波速度最大 5% 误差）。
- **Chaudhary (2004)** 在 EPRI/DCG EMTP Version 2.0 中集成了 CT/CVT 暂态模型和 FORTRAN 用户子程序接口，实现了 EMTP 闭环保护仿真，原文未报告可核验的动作时间或误差指标。

这些量化数据不构成对所涉保护方法的全面性能评价，只说明在特定 EMT 测试条件下可获得的能力边界。

## 适用边界与失败模式

- 未建模 CT 饱和、滤波延迟或通信延迟时，不应给出保护动作时间或选择性的强结论。
- 只用正序或工频模型可能遗漏行波、高频暂态、直流分量和换流器限流造成的保护风险。
- 行波保护和直流保护结论不能从单一线路长度、故障电阻或采样率外推到所有电网。
- HIL 结果还受接口延迟、数模转换、放大器带宽和实际装置固件影响，应和仿真模型边界分开报告。

## 代表性来源

- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] 支撑在 EMTP 中表示保护系统的基本思路（CT/CVT 暂态模型、FORTRAN 接口、断路器闭环反馈），适合作为保护逻辑和一次系统耦合的来源入口。原文未提供可核验的动作时间或误差指标。
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]] 可作为 TACS/EMTP 保护教学和算法表达的来源，但不应外推为工程继电器通用验证。
- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] 支撑距离保护算法与复数微分方程处理的讨论（短窗傅里叶滤波 + 单采样点阻抗求解）。原文未报告可核验的数值结果。
- [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr]] 为 VSC 直流电网行波保护来源：0.512 ms 动作数据窗、250 倍区内/区外 WTMM 差异、400 Ω 高阻故障 100% 准确率 (Pei 2019)。结论限于张北四端环网和 PSCAD 离线 EMT 仿真。
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]] 为双回线路单端行波保护来源：10 kHz + 64 kHz 双采样率、3 ms 时间窗、阈值 10% 额定电流 (Zhang 2017)。
- [[application-of-wavelet-singular-entropy-theory-in-transient-protection-and-accel]] 为小波奇异熵暂态保护来源：200 kHz 采样、0.5 ms 数据窗、DB4 小波 4 层分解 (Liu 2009)。

## 与相关页面的关系

- [[relay-protection]] 是继电保护主题页；本页聚焦 EMT 建模方法和验证边界。
- [[distance-relay]]、[[differential-protection]] 和 [[protection-control-device]] 是模型页，承载具体保护元件的结构。
- [[wide-area-monitoring-protection]] 讨论广域测量和控制闭环，涉及通信和系统级动作。
- [[fault-analysis]] 与 [[fault-analysis-methods]] 提供故障场景和故障注入方法。

## 开放问题

- 如何在保护厂家黑盒算法不可公开时报告可审核的模型等效和误差边界。
- 如何统一 EMT 波形、实际录波和 HIL 测试之间的保护动作证据。
- 如何在换流器型电源比例较高的系统中重新定义保护判据的适用边界。

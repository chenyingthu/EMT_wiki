---
title: "硬件在环仿真 (HIL Simulation)"
type: topic
tags: [hil, real-time, simulation, hardware, testing, controller-validation]
created: "2026-05-02"
---

# 硬件在环仿真 (HIL Simulation)


```mermaid
graph LR
    N0[技术背景]
    N1[定义与边界]
    N0 -->|Nf1| N1
    N2[EMT 中的作用]
    N1 -->|Nf2| N2
    N3[主要分支与机制]
    N2 -->|Nf3| N3
    N4[适用边界与失败模式]
    N3 -->|Nf4| N4
    N5[代表性来源]
    N4 -->|Nf5| N5
```


## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

硬件在环仿真 (Hardware-in-the-Loop, HIL) 是把真实控制器、保护装置、功率设备或通信设备接入实时仿真闭环的测试方法。仿真器提供被控电力系统或设备模型，硬件通过模拟量、数字量、通信或功率接口交换信号。

本页关注 EMT 语境下 HIL 的模型、接口和证据边界。它不同于纯软件 [[co-simulation]]，也不同于只追求离线加速的快速仿真。HIL 的核心约束是闭环可实时、接口语义一致、被测硬件看到的信号可信。

## EMT 中的作用

HIL 让控制保护硬件在投运前经历可重复、可注入故障且风险可控的 EMT 场景，常见用途包括：

- HVDC、FACTS、MMC、VSC 和新能源控制保护系统的动态性能测试。
- 继电保护装置在交流故障、直流故障、互感器饱和或通信条件变化下的闭环验证。
- [[wide-area-monitoring-protection]]、通信仿真器和真实 IED 的联合测试。
- 大型离线 EMT 模型迁移到 [[real-time-simulation]] 平台后的信号、波形和 deadline 校核。

## 主要分支与机制

### 控制器 HIL

控制器 HIL 中真实硬件只处理测量、控制和保护逻辑，功率系统由实时 EMT 或 RMS-EMT 模型表示。基本闭环可写成

$$
y_k = H(x_k)+\eta_k,\qquad u_k=C_{\mathrm{hw}}(y_{k-d}),\qquad x_{k+1}=F(x_k,u_k),
$$

其中 $x_k$ 是仿真模型状态，$y_k$ 是传给硬件的测量量，$u_k$ 是硬件输出控制量，$d$ 表示采样、转换、通信和处理形成的等效延迟。证据应说明 $d$、量程、采样率、滤波和信号方向，而不能只说“接入真实控制器”。

### 功率 HIL

功率 HIL 让实际功率设备通过功率放大器或变流器接入仿真环境。接口稳定性通常比控制器 HIL 更敏感，因为功率放大器带宽、延迟、输出阻抗和被测设备动态共同进入闭环。最低限度应检查接口注入功率、阻抗匹配、延迟补偿和故障时饱和/限流行为。

### RMS-EMT 与多域实时 HIL

保护 HIL 或广域控制场景常把被测区域保留 EMT，把外部大系统放在 RMS、相量或动态相量域。[[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective]] 代表了利用传输线接口连接 OPAL-RT ePhasorSim 与 RTDS，并将实际保护继电器接入 HIL 的路线。该类方法的关键不是“两个工具能通信”，而是相量和瞬时波形的转换延迟、频率估计和接口线路假设。

### 大型系统混合实时 HIL

大型 HVDC 或 WAMPAC 平台往往同时包含软件化旧控制、真实新控制硬件和详细 AC/DC 网络。[[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]] 说明 Nelson River 多馈入 HVDC benchmark 中，模块化建模、逐级集成、控制逻辑重构和硬件副本接入是主要工程内容；其结论应限定在原文系统、RTDS 模型和现场投运验证范围内。

## 适用边界与失败模式

- 实时性必须以最坏步长时间和抖动判断：

$$
T_{\mathrm{solve}}+T_{\mathrm{io}}+T_{\mathrm{comm}}+T_{\mathrm{hw}}\le \Delta t,
$$

其中 $\Delta t$ 是实时步长，$T_{\mathrm{hw}}$ 是硬件响应或控制处理进入闭环的等效时间。

- I/O 量程、采样保持、抗混叠滤波和通信协议可能改变保护或控制动作，必须作为模型边界说明。
- 为满足 deadline 而采用平均值模型、等效电压源或降阶阀组时，应说明哪些开关谐波、子模块状态或保护瞬时量被舍弃。
- 功率 HIL 若功放带宽不足、延迟补偿不当或接口阻抗选择不当，可能出现非物理振荡甚至损坏设备。
- HIL 测试通过不等于现场投运保证；未覆盖的故障、通信异常、固件版本和硬件配置仍是残余风险。


### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s
- 电压等级：10kV ~ 500kV
- 功率范围：1MW ~ 1000MW
- 频率范围：50Hz / 60Hz

## 代表性来源

- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]]：支撑混合 SVC-VSC 工程中小步长 EMT 与常规步长 EMT 两类 HIL 建模路径；步长和接口结论限于该项目和平台。
- [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective]]：支撑实时 RMS-EMT 多域接口和保护继电器 HIL；不能外推为所有继电保护或所有接口精度最优。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：支撑大规模 HVDC 混合实时 HIL 的模块化建模和硬件副本闭环。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]]：支撑离线大系统向实时 HIL 迁移时，模型兼容层、信号校核和波形比较是工程证据的一部分。
- [[emt-simulation-verification]] 提供 HIL 波形、接口和 deadline 证据的验证框架。

## 与相关页面的关系

- [[real-time-simulation]] 讨论固定步长和 deadline；HIL 在此基础上增加真实硬件、I/O 和安全约束。
- [[interface-technique]] 解释电压、电流、功率、相量和多端口接口；HIL 需要把这些接口落实到物理或通信通道。
- [[offline-to-realtime-porting]] 关注离线模型迁移；HIL 是迁移后的闭环使用场景之一。
- [[protection-control-device]] 和 [[distance-relay]] 解释被测保护控制对象的模型边界。
- [[large-scale-grid-simulation]] 与 [[large-scale-hybrid-acdc-simulation]] 提供 HIL 常见系统背景。

## 开放问题

- 如何为 HIL 报告统一的接口延迟、抖动、量化误差、波形误差和硬件版本信息。
- 如何在满足实时 deadline 的同时保留保护动作所需的瞬时量和高频分量。
- 如何把通信网络、真实 IED、功率接口和 EMT 数值稳定性纳入同一验证报告。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[29tpwrd20162518676-2|29/TPWRD.2016.2518676]] | 2016 |
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|An automated FPGA real-time simulator for power electronics ]] | 2016 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation|Use of efficient task allocation algorithm for parallel real]] | 2020 |
| [[compensation-method-for-parallel-real-time-emt-studies|Compensation method for parallel real-time EMT studies✰]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[flexible-time-stepping-dynamic-emulation-of-acdc-grid-for-faster-than-scada-appl|Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for F]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co|An Equivalent Hybrid Model for a Large-Scale Modular Multile]] | 2022 |
| [[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co|An Equivalent Hybrid Model for a Large-Scale Modular Multile]] | 2022 |
| [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix|Analysis and Prospect of Development of China]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop ]] | 2023 |
| [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Lessons learned in porting offline large-scale power system ]] | 2023 |
| [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Real-Time HIL Emulation of DRM With Machine Learning Acceler]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul|Sparse solver application for parallel real-time electromagn]] | 2023 |
| [[key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation|Key Technologies and Prospects for Electromagnetic Transient]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
---
title: "暂态稳定分析 (Transient Stability Analysis)"
type: method
tags: [transient-stability, rotor-angle, swing-equation, equal-area, stability-margin]
created: "2026-05-02"
---

# 暂态稳定分析 (Transient Stability Analysis)


```mermaid
graph TD
    N0[暂态稳定分析 (Transien…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[分析流程]
    N0 --> N3
    N4[时域仿真法]
    N0 --> N4
    N5[等面积与直接法]
    N0 --> N5
    N6[CCT 与裕度搜索]
    N0 --> N6
    N7[EMT/混合仿真分析要点]
    N0 --> N7
    N8[适用边界与失败模式]
    N0 --> N8
```


## 定义与边界

暂态稳定分析是评估电力系统在指定大扰动后能否保持同步、失稳模式为何、稳定裕度有多大以及控制/保护措施是否有效的方法集合。它把 [[transient-stability]] 的概念转化为可执行的建模、仿真、判据和证据流程。

本页讨论分析方法。它不重写 [[swing-equation]] 的方程推导，也不替代 [[electromechanical-simulation]] 的数值推进细节。与 [[small-signal-stability-analysis]] 相比，本页关注大扰动非线性轨迹；小信号特征值只可作为补充证据。

## EMT 中的作用

EMT 或 EMT-TS 混合仿真在暂态稳定分析中用于处理机电模型难以可信近似的环节，例如不平衡故障、单相负荷堵转、换相失败、变流器限流、保护动作和波形级控制逻辑。分析流程应说明：哪些区域使用 EMT，哪些区域使用机电相量模型，边界数据如何交换，稳定判据在哪一侧计算。

若分析目标只是大系统同步保持，机电仿真可能足够；若局部 EMT 细节会显著改变电磁功率或无功支撑，则应通过混合或全 EMT 复核关键案例。

## 分析流程

1. 定义研究问题：首摆、多摆、CCT、控制措施、机群分裂或电压-功角耦合。
2. 确定模型边界：同步机、励磁、PSS、负荷、HVDC/IBR、保护和网络表示。
3. 初始化运行点：记录潮流、机组出力、控制参考和限制状态。
4. 定义扰动集：故障类型、位置、阻抗、施加时刻、切除时间和切除后拓扑。
5. 运行时域或混合仿真：保存功角、转速、电压、功率、限幅和保护动作。
6. 应用判据：识别失步机群、最大角差、转速衰减、滑极、CCT 或能量裕度。
7. 做敏感性检查：改变清除时间、运行点、负荷模型、控制参数、步长和接口设置。
8. 给出证据边界：说明结论只对哪些场景、模型和判据成立。

## 时域仿真法

时域法直接求解机电或混合 DAE：

$$
\dot{x}=f(x,y,\sigma,t), \qquad 0=g(x,y,\sigma,t)
$$

扰动通过 $\sigma$ 改变网络拓扑和控制/保护状态。稳定性判断通常基于相对功角、相对转速、机群分离和轨迹是否进入可接受动态范围。

优点是模型范围广，可处理复杂控制、限幅、保护和非线性负荷；缺点是计算成本较高，且每个结论都绑定具体扰动和观察时窗。时域法不能自动给出全局稳定域，CCT 和裕度通常需要重复仿真或搜索。

## 等面积与直接法

等面积准则用于单机无穷大或等效两机场景。基本思想是在无阻尼近似下比较故障期间加速面积和故障后可用减速面积：

$$
A_{\mathrm{acc}}=\int_{\delta_0}^{\delta_c}(P_m-P_e^{fault})\,d\delta
$$

$$
A_{\mathrm{dec}}=\int_{\delta_c}^{\delta_{\max}}(P_e^{post}-P_m)\,d\delta
$$

临界条件是两者相等。该方法物理解释清楚，但对多机、励磁限制、动态负荷、电压崩溃和电力电子限流的适用性有限。扩展等面积、SIME 和能量函数法试图把多机系统映射到等效机群或能量裕度，但临界机群识别和模型假设需要单独验证。

## CCT 与裕度搜索

临界切除时间通常通过二分或逐步搜索得到：

1. 固定故障类型、位置和切除后拓扑。
2. 选择稳定/失稳判据和观察时窗。
3. 在切除时间区间内重复仿真。
4. 找到稳定与失稳边界，并报告搜索容差。

CCT 必须与场景绑定。不能把某次 CCT 当作系统常数，也不能在未说明判据时报告“稳定裕度”。时间裕度、角度裕度、能量裕度和功率裕度之间不可直接互换。

## EMT/混合仿真分析要点

- 边界位置应远离强非线性和严重畸变区域，或采用三相/三序等值。
- 相量提取窗口会影响故障初期和清除后若干步的边界量。
- 串行交互更稳但耗时较大；并行交互可能在突变时产生滞后误差。
- 对 FIDVR、换相失败和控制限流，应保存相别电压、电流、状态切换和保护动作，而不仅是正序量。
- 混合仿真结论应至少用局部全 EMT、步长/接口敏感性或文献基线做交叉检查。

## 适用边界与失败模式

- 判据不清会导致不可复核结论，例如只说“功角没有超过某值”但未说明参考机、时窗和机群。
- 直接法适合解释机制和快速筛查，但不能替代复杂模型的时域验证。
- 单次仿真稳定不代表全部运行方式稳定；需要对关键运行点和扰动集做覆盖。
- 控制器限幅、保护动作和负荷恢复若未建模，可能把真实失稳误判为稳定。
- 机电-EMT 混合接口误差可能恰好改变临界案例，应对 CCT 附近场景做额外复核。

## 代表性证据

- [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t]]：支持在不平衡 FIDVR 场景中使用 EMT-TS 混合分析，并提醒串/并行协议和三序等值属于证据边界。
- [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model]]：支持动态相量 HVDC 模型接入暂态稳定仿真的方法思想，但页面证据不足以提供通用误差或加速比。
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]]：展示 FACTS 局部动态相量模型与机电暂态子系统耦合的路线。
- [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie]]：说明低频振荡指标可比较机电模型与机电-电磁混合模型，但不能外推到所有暂态稳定问题。

## 与相关页面的关系

- [[transient-stability]]：定义分析对象和稳定性概念。
- [[electromechanical-simulation]]：提供主要时域轨迹生成方法。
- [[electromechanical-modeling]]：说明模型层级和状态变量来源。
- [[swing-equation]]：提供功率不平衡与转子运动的核心关系。
- [[small-signal-stability-analysis]]：可作为阻尼和控制参数的补充分析，不替代大扰动分析。
- [[emt-simulation-verification]]：用于组织混合或 EMT 结果的验证证据。

## 证据边界

本页不列固定裕度等级、固定保护要求或无来源 CCT 数值。所有分析结果必须报告模型、扰动、判据、搜索容差、观察时窗和验证方式。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient|Comparison and Selection of Grid-Tied Inverter Models for Ac]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl|Electromechanical transient-electromagnetic transient hybrid]] | 2022 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
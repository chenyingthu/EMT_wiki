---
title: "等面积法则 (Equal Area Criterion)"
type: method
tags: [equal-area, stability, transient, swing-equation, direct-method, single-machine, power-angle]
created: "2026-05-02"
---

# 等面积法则 (Equal Area Criterion)


```mermaid
graph TD
    N0[等面积法则 (Equal Are…]
    N1[经典单机无穷大 EAC：适合教材…]
    N0 --> N1
    N2[两机等效 EAC：把两台机或两个…]
    N0 --> N2
    N3[多机扩展路线：eeac 和 SI…]
    N0 --> N3
    N4[能量函数联系：energy-fu…]
    N0 --> N4
```


## 定义与边界

等面积法则（Equal Area Criterion, EAC）是用于单机无穷大系统或可严格化为等效两机系统的暂态功角稳定直接判据。它把 [[swing-equation]] 中的功率不平衡积分解释为转子动能变化，通过比较故障期间的加速面积和故障切除后的可用减速面积判断首摆稳定边界。

本页讨论方法本身，不把 EAC 写成通用多机稳定算法。复杂多机系统、励磁限幅、动态负荷、电力电子限流、保护动作和电压稳定问题需要通过 [[transient-stability-analysis]]、[[time-domain-simulation]] 或 [[eeac]] 等扩展/验证流程处理。

## EMT 中的作用

EAC 在 EMT 研究中的主要价值是提供功角稳定的机制解释和低维校核，而不是替代 EMT 波形仿真。EMT 或 EMT-TS 混合仿真可给出故障期间的电磁功率、切除角、限幅状态和保护动作；EAC 可用于解释这些结果中“加速能量是否能被切除后网络吸收”。

若 EMT 细节显著改变 $P_e(\delta)$，例如换流器限流改变电磁功率表达、故障不平衡导致正序等效不充分，EAC 只能作为解释框架，不能作为独立判据。

## 核心机制

单机无穷大系统的经典摇摆方程可写为：

$$
M\frac{d^2\delta}{dt^2}=P_m-P_e(\delta)
$$

其中 $M$ 是等效惯性，$\delta$ 是功角，$P_m$ 是机械输入功率，$P_e$ 是电磁输出功率。令 $\omega=d\delta/dt$，两边乘以 $\omega$ 并积分，得到：

$$
\frac{1}{2}M(\omega^2-\omega_0^2)
=\int_{\delta_0}^{\delta}(P_m-P_e(\alpha))\,d\alpha
$$

因此，故障期间的加速面积为：

$$
A_{\mathrm{acc}}
=\int_{\delta_0}^{\delta_c}
\left(P_m-P_e^{fault}(\delta)\right)\,d\delta
$$

切除后的最大减速面积为：

$$
A_{\mathrm{dec,max}}
=\int_{\delta_c}^{\delta_u}
\left(P_e^{post}(\delta)-P_m\right)\,d\delta
$$

其中 $\delta_0$ 是故障前稳态功角，$\delta_c$ 是故障切除角，$\delta_u$ 是切除后功率曲线上的不稳定平衡角。首摆稳定的理想判据是：

$$
A_{\mathrm{acc}}<A_{\mathrm{dec,max}}
$$

临界切除角满足 $A_{\mathrm{acc}}=A_{\mathrm{dec,max}}$。若采用经典正弦功率角关系：

$$
P_e=P_{\max}\sin\delta
$$

则不稳定平衡角常写为：

$$
\delta_u=\pi-\arcsin\left(\frac{P_m}{P_{\max}^{post}}\right)
$$

该表达依赖恒定内电势、等效电抗、无阻尼或弱阻尼、机械功率短时近似恒定等假设。

## 分类与变体

- 经典单机无穷大 EAC：适合教材级故障前、故障中、故障后三条功率角曲线分析。
- 两机等效 EAC：把两台机或两个等效机群的相对运动写成等效单自由度问题。
- 临界切除角/时间计算：先用面积相等求 $\delta_{cr}$，再由故障期间轨迹 $\delta(t)$ 反求临界切除时间；时间结果必须绑定故障、模型和数值积分设置。
- 多机扩展路线：[[eeac]] 和 SIME 类方法通过机群识别构造 OMIB 等效，再在等效系统上使用面积判据。
- 能量函数联系：[[energy-function]] 从更一般的能量裕度角度处理稳定边界，EAC 可视为单自由度无阻尼情形下的图形化能量判据。

## 适用边界与失败模式

- 只适用于首摆主导且等效功率角曲线可定义的场景；多摆失稳或机群重组需要额外验证。
- 阻尼、调速、励磁、PSS 和限幅若显著改变 $P_e$ 或 $P_m$，面积解释需降级为近似。
- 单相故障、不平衡网络、动态负荷和电力电子控制可能破坏简单正弦功率角关系。
- CCT 不是系统常数；必须绑定故障位置、故障类型、切除拓扑、判据和观察时窗。
- “面积大于/小于”只说明该低维模型的能量关系，不自动证明完整 EMT 模型稳定。

## 代表性来源

- [[transient-stability-analysis]]：给出暂态稳定分析中直接法、CCT 搜索和 EMT/混合仿真证据边界。
- [[swing-equation]]：支撑 EAC 的功率不平衡和转子动能积分关系。
- [[electromechanical-transient]]：提供 EAC 所在机电暂态时间尺度的上下文。
- [[dynamic-performance-of-embedded-hvdc-with-13&14]]：报告特定 PSCAD 算例中频率控制对 CCT 的影响；其数值只可作为该论文工况的结果，不能外推为 EAC 通用性能。

## 与相关页面的关系

- [[swing-equation]] 是 EAC 的基础动力学方程。
- [[transient-stability]] 定义功角暂态稳定概念。
- [[transient-stability-analysis]] 说明 EAC 与时域法、CCT 搜索和混合仿真的关系。
- [[energy-function]] 是更一般的直接法框架。
- [[eeac]] 把 EAC 扩展到机群等效后的多机问题。
- [[time-domain-simulation]] 用于生成 EAC 无法覆盖的完整非线性轨迹。

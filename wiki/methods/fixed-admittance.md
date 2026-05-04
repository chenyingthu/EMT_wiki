---
title: "恒导纳模型 (Fixed Admittance / ADC Model)"
type: method
tags: [fixed-admittance, adc, real-time, companion-circuit]
created: "2026-04-13"
---

# 恒导纳模型 (Fixed Admittance / ADC Model)

## 定义与边界

恒导纳模型是把开关器件、桥臂模块或局部子网络表示为导纳矩阵在开关状态变化时保持不变的 EMT 等效方法。它常与关联离散电路（Associated Discrete Circuit, ADC）和伴随电路历史源结合使用：开关状态变化主要进入右端注入项、历史源或内部状态，而不是每次都改变主网络导纳矩阵。

本页讨论数值建模方法，不把恒导纳写成器件物理模型、控制模型或无条件实时加速技术。具体收益必须绑定拓扑、步长、平台、矩阵规模和误差指标。

## EMT 中的作用

在含大量电力电子开关的 EMT 仿真中，传统 RON/ROFF 或详细开关模型可能频繁改变网络拓扑并触发矩阵重组、重排序或重分解。恒导纳模型的作用是：

- 让 [[nodal-analysis]] 中的主导纳矩阵可重复使用。
- 减少开关频繁动作对稀疏矩阵分解的影响。
- 为实时仿真和 FPGA/CPU 异构实现提供确定性计算结构。
- 通过模块级等效减少 MMC、VSC 或桥臂内部开关对外部网络的耦合维度。

## 核心机制

恒导纳模型的统一形式可写为

$$
i_k=Y_{\mathrm{fix}}v_k+i_{\mathrm{hist}}(s_k,x_{k-1},u_k),
$$

其中 $Y_{\mathrm{fix}}$ 在开关状态 $s_k$ 改变时保持不变，$i_{\mathrm{hist}}$ 包含历史电压电流、内部状态、控制量和开关逻辑。关键不是让物理导纳真的不变，而是通过等效电路、历史源参数化、状态消元或模块聚合，把拓扑变化从左端矩阵转移到右端项和局部更新。

这种方法依赖 [[discretization-methods]] 和 [[numerical-integration]]：积分公式决定电感、电容和内部状态的等效导纳；状态切换时还需要与 [[interpolation-method]] 或重初始化策略配合，避免虚拟损耗和初值误差。

## 分类与变体

| 类型 | 机制 | 边界 |
|------|------|------|
| 单开关 ADC | 为开关状态构造固定等效导纳和历史源 | 容易受步长和虚拟损耗影响 |
| 桥臂或模块级 ADC | 把上下开关、桥臂电感、电容等合成模块 | 适用拓扑由模块假设决定 |
| 状态变量消元等效 | 消去内部状态形成外部恒导纳接口 | 需检查可观测状态和历史源恢复 |
| MMC 聚合恒导纳 | 对子模块或桥臂做 Thevenin/Norton 聚合 | 可能丢失阀级细节或故障内部行为 |
| FPGA 实时恒导纳 | 固定矩阵适合流水线和确定性调度 | 受数值精度、资源和通信延迟约束 |

## 适用边界与失败模式

- 适合矩阵分解成本显著、开关动作频繁、外部只需端口行为的 EMT 场景。
- 若研究目标是器件级损耗、极短时标过电压、EMI 或保护临界时刻，恒导纳等效可能过粗。
- 固定矩阵不等于无误差；历史源设计可能引入虚拟功率损耗、谐波尖峰或状态切换初值误差。
- 状态依赖参数、强非线性元件和非互补开关状态可能需要局部迭代、降级模型或重新判定。
- 与实时仿真相关的“可实时”结论必须绑定硬件平台、步长、节点规模和实现细节。

## 代表性来源

| 来源 | 支撑内容 | 证据边界 |
|------|----------|----------|
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul]] | 提出桥臂模块级参数化固定导纳 ADC，并用历史源参数和切换重初始化处理误差 | 当前页面证据不支持固定加速倍数或所有拓扑适用 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]] | 状态变量消元可用于构造 EMTP 型恒定导纳等效 | 需按原文对象确认哪些状态可消去 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-]] | MMC 高速等效中使用恒定矩阵和模块聚合思想 | 不等同于保留所有子模块内部细节 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear]] | FPGA 微秒级 EMT 场景使用固定导纳以支持确定性计算 | 平台、资源、步长和非线性处理需回查原文 |
| [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-]] | 半桥腿 ADC 解析建模说明固定导纳可在桥臂层级构造 | 结论限于原文半桥建模假设 |

## 与相关页面的关系

- [[nodal-analysis]] 是恒导纳模型复用矩阵的求解框架。
- [[discretization-methods]] 和 [[numerical-integration]] 决定等效导纳和历史源。
- [[interpolation-method]] 用于修正开关时刻和接口状态。
- [[stiff-system-handling]] 说明固定导纳不能单独解决刚性和事件后振荡。
- [[sparse-matrix-solver]] 解释固定矩阵为何可能降低分解开销。
- [[mmc-model]]、[[vsc-model]] 和 [[switch-modeling]] 是恒导纳方法常见但需要限定的应用对象。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报|中  国  电  机  工  程  学  报]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等 | A fixed-admittance algorithm for the FPGA-based micro]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[中-国-电-机-工-程-学-报-37|中  国  电  机  工  程  学  报]] | 2025 |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability|RMS&#x002B;: Augmenting the Traditional Circuit Model to Cap]] | 2026 |

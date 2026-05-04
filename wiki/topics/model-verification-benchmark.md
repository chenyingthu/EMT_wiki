---
title: "模型验证与基准测试 (Model Verification and Benchmarking)"
type: topic
tags: [verification, benchmark, validation, cigre, ieee, standard, emt]
created: "2026-05-01"
book-chapter: "20"
---

# 模型验证与基准测试 (Model Verification and Benchmarking)

## 定义与边界

模型验证与基准测试用于回答 EMT 模型和工具结果是否可信、是否可复现、是否可与其他模型比较。验证关注某个模型在给定假设下是否正确；基准测试关注多个模型、工具或算法在同一系统和扰动下是否可比。

本页不是标准条文汇编，也不提供通用误差阈值。误差准则必须绑定模型类型、测试系统、采样窗口、参考解、工具设置和研究目的。测试系统条目可阅读 [[ieee-118-bus-system]]、[[ieee-39-bus-system]] 和 [[test-systems/cigre-hvdc-benchmark]]。

## EMT 中的作用

EMT 验证和 benchmark 通常用于：

- 检查元件模型、控制模型和网络接口是否按预期产生波形。
- 比较 [[numerical-integration]]、[[nodal-admittance-matrix]]、[[frequency-dependent-line-model]] 或 [[transformer-model]] 的实现差异。
- 为论文或工程报告提供可追溯的测试系统、故障场景和误差指标。
- 支撑实时仿真和 HIL 模型移植，避免只报告“能运行”而不报告误差和边界。

## 主要分支与机制

- 单元验证：对 RLC、开关、变压器、线路或控制器单独测试，优先与解析解、频响或已知稳态对比。
- 子系统验证：对换流器、线路段、保护链路或电机-控制组合测试，关注接口变量和事件时序。
- 系统 benchmark：在 IEEE、CIGRE 或工程系统中设置统一扰动，对比波形、特征量、收敛性和计算成本。
- 跨工具对比：不同工具之间必须统一拓扑、参数、初值、步长、插值和输出采样，否则差异不能直接归因于算法。

## 形式化表达

常见误差指标可写为：

$$
\epsilon_{\mathrm{rms}}=
\sqrt{\frac{\sum_k (y_k-y_k^{\mathrm{ref}})^2}{\sum_k (y_k^{\mathrm{ref}})^2}},
\qquad
\epsilon_F=\frac{|F-F^{\mathrm{ref}}|}{|F^{\mathrm{ref}}|}
$$

其中 $y_k$ 是波形采样，$F$ 是峰值、到达时间、频率或动作时间等特征量。报告这些指标时应同时说明参考解来源、采样窗口、滤波处理和归一化方式。

## 适用边界与失败模式

- 单个 benchmark 只能证明模型在该系统和扰动下表现合理，不能证明通用正确。
- 只比较峰值可能遗漏相位、波前、频率和保护动作时序差异。
- 跨工具结果一致不等于真实系统准确；多个工具可能共享同一简化假设。
- 实时 benchmark 必须报告 deadline、overrun、I/O 延迟和模型简化，否则不能支撑 HIL 有效性。

## 代表性来源

- [[benchmark-high-fidelity-emt-models-for-power]] 可作为高保真 EMT benchmark 模型来源入口。
- [[inverter-based-resources-model-verification-using-electromagnetic-transient-play]] 支撑逆变器资源模型验证和 playback 方法讨论。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]] 体现大规模 HVDC 实时仿真 benchmark 的证据边界。
- [[validation-of-frequency-dependent]] 可作为频率相关模型验证来源入口，具体结论应回到原文表图核查。

## 与相关页面的关系

- [[simulation-practice-guide]] 更偏向工程仿真流程和常见问题诊断。
- [[model-order-reduction]]、[[vector-fitting]] 和 [[passivity-enforcement]] 需要 benchmark 支撑简化误差。
- [[real-time-simulation]] 和 [[hil-simulation]] 需要额外验证实时约束。
- [[ieee-118-bus-system]] 是系统级测试对象，不等同于 EMT 模型验证流程本身。

## 开放问题

- 如何为黑盒变流器和保护装置建立可公开复验的 benchmark。
- 如何同时报告波形误差、特征量误差、计算代价和模型边界。
- 如何把现场录波、实验平台和多工具仿真组织成一致证据链。

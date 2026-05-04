---
title: "数字仿真器 (Digital Simulator)"
type: topic
tags: [digital-simulator, real-time, hardware, emulation, power-system]
created: "2026-05-02"
---

# 数字仿真器 (Digital Simulator)

## 定义与边界

数字仿真器是用数字计算平台求解电力系统模型的仿真环境。它可以是离线软件、实时硬件平台、FPGA/MPSoC 专用仿真器，也可以是与物理控制器连接的 HIL 系统。它不是某一种固定求解算法，也不自动保证“高精度”或“实时”；精度、实时性和可接入硬件的能力都取决于模型层级、时间步长、接口延迟、数值方法和硬件资源。

在 EMT Wiki 中，本页关注数字仿真器作为 [[emt-simulation]] 和 [[real-time-simulation]] 的执行平台。具体线路、变压器、换流器和控制器模型应分别回到 [[transmission-line-model]]、[[frequency-dependent-line-model]]、[[mmc-model]]、[[inverter-model]] 等模型页讨论。

## EMT 中的作用

数字仿真器在 EMT 中承担三类任务：

- 离线研究：用较细模型和可接受的运行时间分析 [[electromagnetic-transient]]、[[switching-transient]]、[[lightning-overvoltage]]、换流器控制交互和参数敏感性。
- 实时闭环：在固定步长内完成求解，并通过 I/O、通信或功率接口连接保护装置、控制器或功率硬件，对应 [[hil-simulation]]。
- 模型迁移与工程验证：把离线 EMT 模型移植到实时平台时，需要重新检查元件等价、控制代数环、初始化、数值阻尼和实时 deadline，而不是简单更换软件。

## 主要分支与机制

- 离线 EMT 仿真器通常围绕 [[nodal-admittance-matrix]]、[[state-space-method]]、[[numerical-integration]] 和事件处理组织模型。它们更适合详细波形研究、参数扫描和模型开发，但运行速度可能慢于真实时间。
- 实时 EMT 仿真器必须满足每步计算时间小于仿真步长这一硬约束。常见手段包括 [[parallel-computing]]、网络分区、固定导纳等值、模型降阶和专用硬件流水线。
- FPGA 或异构硬件仿真器把部分网络、开关器件或电力电子模块映射为并行硬件逻辑。其优势需要绑定具体模型、字长、资源占用和接口方案说明，不能泛化为所有场景更准确。
- 协同仿真器通过 [[co-simulation]] 或 [[electromechanical-electromagnetic-hybrid-simulation]] 连接不同时间尺度或不同软件环境。接口变量、同步策略和延迟补偿决定了可用边界。

## 形式化表达

数字仿真器的核心约束可写成离散步进和实时 deadline 的组合：

$$
x_{k+1}=F_h(x_k,u_k,p), \qquad t_{\mathrm{solve},k}+t_{\mathrm{io},k}+t_{\mathrm{comm},k}\le h
$$

其中 $x_k$ 是离散状态，$u_k$ 是控制或扰动输入，$p$ 是模型参数，$h$ 是仿真步长。离线仿真主要关心 $F_h$ 的数值误差和模型边界；实时仿真还必须证明每一步求解、I/O 和通信延迟都不超过 deadline。

## 适用边界与失败模式

- 实时平台的关键风险是 overrun：若某步计算、通信或 I/O 超过 deadline，闭环测试的时间一致性会被破坏。
- 离线模型移植到实时平台时，等价元件缺失、控制模块差异、初始化技巧和数值阻尼设置都可能改变波形。
- 为满足实时性而使用平均值模型、固定导纳模型或网络等值时，应说明丢失的开关纹波、高频行波、饱和、谐波或保护判据。
- 数字仿真器输出不能直接替代现场测量。它支撑的是在给定模型和算例下的可重复验证，外推到实际工程前仍需模型校核、参数核验和现场证据。

## 代表性来源

- [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss]] 以输电线路实时数字模型为例，说明 Bergeron 行波、相模变换和并行硬件如何服务于线路 EMT 实时化；其证据主要限于作者线路合闸算例和硬件条件。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] 讨论离线大规模 EMT 模型向实时平台移植的工程问题，适合作为模型兼容、信号校核和实时约束的边界证据。
- [[real-time-fpga-rtds-co-simulator-for-power-systems]] 和 [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]] 支撑“实时仿真需要硬件结构、任务分配和接口设计共同成立”的综合判断。

## 与相关页面的关系

- [[real-time-simulation]] 讨论固定步长实时执行和 HIL 场景；本页更强调平台类型与证据使用规则。
- [[hil-simulation]] 关注硬件闭环接口、时延和测试对象；数字仿真器只是 HIL 的仿真侧。
- [[emt-software-history]] 适合承载工具演化和软件生态；本页不列工具市场清单。
- [[parallel-computing]]、[[multirate-method]] 和固定导纳方法是实现大规模或实时仿真的方法，不等同于仿真器本身。

## 开放问题

- 如何在不暴露厂家黑盒控制细节的情况下完成可审核的 EMT 模型验证。
- 如何为实时仿真报告统一的 deadline、overrun、接口延迟、模型误差和硬件资源证据。
- 如何在数字孪生、超实时仿真和传统 HIL 之间建立清晰的验证边界。

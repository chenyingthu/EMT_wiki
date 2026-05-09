---
title: "仿真实践与工程指南 (Simulation Practice and Engineering Guide)"
type: topic
tags: [simulation-practice, engineering-guide, best-practice, troubleshooting, emt]
created: "2026-05-01"
book-chapter: "26"
---

# 仿真实践与工程指南 (Simulation Practice and Engineering Guide)


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

仿真实践与工程指南关注 EMT 模型从问题定义、参数整理、初始化、扰动设置、运行、诊断到结果报告的工作流程。它不是固定步长表、工具使用手册或“最佳实践”口号集合；任何步长、误差或性能建议都应绑定模型、工具、硬件和研究目标。

本页面向工程流程层面。具体数值方法应阅读 [[numerical-integration]]、[[stiff-system-handling]] 和 [[numerical-stability]]；模型验证应阅读 [[model-verification-benchmark]]。

## EMT 中的作用

良好的仿真实践用于降低以下风险：

- 初始潮流、控制器积分状态和 EMT 初始状态不一致导致的伪暂态。
- 开关事件、刚性元件或非线性器件引发的数值振荡和不收敛。
- 模型层级、步长和输出采样不匹配，导致结果看似精细但证据不足。
- 报告中缺少参数来源、版本、工具设置、误差指标和适用边界。

## 主要分支与机制

- 问题界定：先定义研究对象、频带、扰动、关注指标和可接受模型层级，再选择详细开关、平均值、等值或混合仿真。
- 初始化：用 [[power-flow-calculation]] 或稳态求解生成电压、电流和控制初值，并检查功率平衡和状态一致性。
- 步长与积分：根据关注频率、控制采样、开关事件和数值稳定性选择步长与积分方法，不使用无来源通用经验表。
- 诊断与修复：对不收敛、数值振荡、能量异常和保护误动作分别检查模型参数、事件时序、积分公式和输出采样。
- 报告与复现：记录工具版本、模型层级、参数来源、扰动脚本、输出采样和误差指标。

## 形式化表达

一次可复验的 EMT 仿真可抽象为：

$$
\mathcal{R}=S(\mathcal{M},p,x_0,\mathcal{D},h,\theta_{\mathrm{solver}})
$$

其中 $\mathcal{M}$ 是模型结构，$p$ 是参数，$x_0$ 是初值，$\mathcal{D}$ 是扰动集合，$h$ 是步长，$\theta_{\mathrm{solver}}$ 是求解器设置。若报告缺少其中任一项，结果的可复现性和外推能力都应降低。

## 适用边界与失败模式

- 步长减小后结果变化较小，只能说明该指标在该设置下收敛，不能证明模型物理正确。
- 为加速而使用等值、平均值或并行分区时，应报告丢失的频带、状态和事件。
- 数值阻尼可以抑制振荡，也可能掩盖真实高频响应，必须说明使用场景。
- 实时仿真还需要检查 deadline、I/O 延迟和 overrun；离线仿真流程不能直接替代实时验证。

## 代表性来源

- [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms]] 支撑 EMT 算法精度评价需要绑定测试系统和指标。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] 说明离线模型迁移到实时平台时需要重新检查模型兼容和信号校核。
- [[benchmark-high-fidelity-emt-models-for-power]] 可作为高保真模型 benchmark 的来源入口。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] 可用于比较伴随电路实现的数值差异。

## 与相关页面的关系

- [[emt-simulation]] 定义仿真范式；本页定义工程执行流程。
- [[model-verification-benchmark]] 关注验证和 benchmark 证据。
- [[numerical-stability]] 解释数值振荡、刚性和稳定域。
- [[real-time-simulation]] 关注固定步长和实时执行约束。

## 开放问题

- 如何用统一模板报告 EMT 仿真的模型层级、参数来源、误差和可复现脚本。
- 如何在保护、控制和电力电子模型存在黑盒时仍保持证据可审核。
- 如何把仿真失败案例、数值问题和修复策略纳入知识网络，而不是只保留成功算例。

---
title: "锁相环参数设计方法 (PLL Design)"
type: method
tags: [pll-design, pll, parameter-tuning, synchronization, inverter-control]
created: "2026-05-04"
updated: "2026-05-07"
---

# 锁相环参数设计方法 (PLL Design)

## 定义与边界

PLL 设计方法指围绕锁相环带宽、阻尼、滤波结构和暂态整定规则建立的参数设计路线。它关注的是“如何设计和整定 PLL”，而不是把任意惯量控制或线路模型残片误写成 PLL 设计页。

本页讨论的是 PLL 的参数与结构整定边界，不替代 [[phase-locked-loop]] 作为总入口。

## EMT 中的作用

在 EMT 仿真中，PLL 设计方法主要用于：

- 选择 PLL 带宽、阻尼和滤波结构；
- 评估暂态下的相位误差、频率估计和同步恢复速度；
- 研究 PLL 参数与弱网、故障和控制外环之间的耦合；
- 为 GFL 逆变器、HVDC 换流器和混合系统的小信号整定提供背景。

## 常见设计目标

- 提高同步速度；
- 控制超调和相位误差；
- 降低谐波、不平衡和噪声影响；
- 避免 PLL 与网络阻抗或外环控制耦合失稳。

## 关键公式

PLL 设计常围绕带宽和环路参数之间的关系展开。最小抽象可写为：

$$
G_{pll}(s)=\frac{K_p s + K_i}{s}
$$

其中 $K_p$ 和 $K_i$ 分别为比例与积分参数。具体设计时，还需要结合同步结构、滤波器和网络模型，把带宽、阻尼和暂态检测策略一并考虑。

## 与相关方法的关系

- [[phase-locked-loop]]：PLL 作为同步方法的总入口。
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：自适应带宽 PLL 设计的直接背景。
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：PLL 参数与网络交互失稳的背景。
- [[frequency-control]]：频率控制会依赖 PLL 测量，但 PLL 设计不等同于频率控制设计。
- [[grid-connected-inverter]]：并网逆变器中的 PLL 设计应用背景。

## 适用边界与失败模式

- 适用于需要整定并网同步环的场景。
- 单独优化 PLL 带宽，不一定能保证整个控制系统稳定。
- 弱网、谐波、不平衡和限流都会改变“看起来合理”的 PLL 参数区间。
- 单篇论文中的最优参数结论不能直接外推到其他控制器、拓扑或 SCR 条件。

## 代表性来源

- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]：DSOGI-PLL 带宽与暂态整定背景。
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：PLL 参数与同步失稳背景。
- [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver]]：说明换流器外环参数设计与 PLL 设计的相关背景。

## 证据边界

本页不写无来源的最优带宽、最优阻尼或统一 SCR 适用范围。具体参数必须绑定同步结构、网络强度和验证工况。

## 开放问题

- 当前页尚未继续拆分 SRF-PLL、DSOGI-PLL 和其他增强型 PLL 的参数整定差异。
- PLL 参数如何与限流、外环和弱网稳定性联合整定，后续仍需回到具体 source 页细化。

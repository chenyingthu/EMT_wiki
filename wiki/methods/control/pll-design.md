---
title: "锁相环参数设计方法 (PLL Design)"
type: method
tags: [pll-design, pll, parameter-tuning, synchronization, inverter-control]
created: "2026-05-04"
updated: "2026-05-10"
---

# 锁相环参数设计方法 (PLL Design)


```mermaid
graph TD
    subgraph S0[锁相环参数设计方法 (PLL Design)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见设计目标]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[适用边界与失败模式]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

PLL 设计方法指围绕锁相环带宽、阻尼、滤波结构和暂态整定规则建立的参数设计路线。它关注"如何设计与整定 PLL"，而非 PLL 作为同步机制的原理本身。本页讨论 PLL 的参数与结构整定边界，不替代 [[phase-locked-loop]] 作为总入口。

PLL 参数设计需同时考虑三个层面:
- **稳态性能**: 谐波/不平衡下的相位精度、频率跟踪精度
- **暂态性能**: 故障/相位跳变下的同步恢复速度、超调控制
- **稳定边界**: PLL 与网络阻抗、电流内环、外环控制的交互稳定性

## EMT 中的作用

在 EMT 仿真中，PLL 设计方法主要用于:

- 选择 PLL 带宽、PI 增益和滤波结构参数
- 评估故障、弱网和不平衡工况下的相位误差与同步恢复时间
- 分析 PLL 参数与短路比(SCR)、外环带宽、电流内环带宽之间的联合稳定性
- 设计自适应带宽策略，在不同工况下切换 PLL 动态特性
- 验证 PLL 参数是否落入跨临界分岔或 Hopf 分岔的不稳定区域

## 常见设计目标

### 带宽选择策略

PLL 带宽是设计的核心参数。高带宽加速同步但放大谐波，低带宽抑制噪声但暂态响应慢。

- **固定带宽设计**: 在稳态滤波和暂态响应间折中。
- **自适应带宽设计**[Ranasinghe 2024]: 稳态保持低带宽(62 rad/s)，暂态放大至 5 倍，配合频率冻结防止噪声放大。

### PI 参数整定

SRF-PLL 的 PI 参数(Kp, Ki)决定闭环动态: Kp 控制同步速度，Ki 消除稳态频率偏差。

- **特征方程匹配法**[Ranasinghe 2024]: 根据目标阻尼比 $ξ=0.7$ 和穿越频率 $ω_c$ 联立求解 Kp, Ki
- **稳定边界约束法**[Carreño 2026]: 确保 Kp < 1/(i_P L) 避免跨临界分岔，Ki/Kp < √(V^2-(i_P X)^2)/(i_P L) 避免 Hopf 分岔

### 时间尺度分离要求

电感时间常数 $τ_L = L/R$ 与 PLL 时间常数 $τ_PLL = 1/K_p$ 的比值决定建模精度:
- $τ_L/τ_PLL < 0.1$: PLL 与网络动态可近似解耦，误差 < 2%
- $τ_L/τ_PLL > 0.3$: 需高阶修正，网络电感 di/dt 效应不可忽略

## 关键公式

### SRF-PLL 闭环传递函数

$$
G_{pll}(s)=\frac{K_p s + K_i}{s}
$$

其中 $K_p$ 为比例增益，$K_i$ 为积分增益。

### 自适应 PI 参数整定方程组 [Ranasinghe 2024]

$$
\omega_p = 2\xi\omega_n + A,\quad A\omega_n^2 = K_i \omega_p,\quad \omega_n^2 + 2\xi\omega_n A = \omega_p K_p
$$

给定目标阻尼比 $ξ$ 和自然频率 $ω_n$，联立求解 Kp, Ki。

### Hopf 分岔稳定判据 [Carreño 2026]

$$
K_p\sqrt{V^2 - (i_P X)^2} - K_i i_P L > 0
$$

当不等式不成立时，PLL 与电网电感交互导致持续振荡失稳。

### 跨临界分岔条件 [Carreño 2026]

$$
K_p < \frac{1}{i_P L}
$$

PLL 比例增益越过此边界时系统发生鞍结型失稳。

### 耦合强度系数

$$
\kappa = \frac{K_p \cdot i_P \cdot L}{\omega_n}
$$

当 $κ > 0.05$ 时系统进入弱阻尼区域(阻尼比 $ζ < 0.1$)。

## 与相关方法的关系

- [[phase-locked-loop]]: PLL 作为同步机制的总入口
- [[dsogi-pll]]: 基于正交信号生成的 PLL 结构，DSOGI-PLL 参数涉及 SOGI 谐振频率和阻尼系数
- [[srf-pll]]: 同步坐标系 PLL，参数设计以带宽和 PI 增益为核心
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]: 自适应带宽 DSOGI-PLL 的设计依据
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]: PLL 参数与网络交互失稳边界
- [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver]]: 外环参数与 PLL 参数的联合整定
- [[frequency-control]]: PLL 影响频率测量，但不等同于频率控制

## 适用边界与失败模式

### 适用条件

- 需要整定并网同步环的 SRF-PLL、DSOGI-PLL 或类似结构
- 弱电网(SCR < 3) 下 PLL 参数需协同网络阻抗和外环控制联合设计
- 自适应带宽策略适用于变工况(故障、相位跳变、频率斜坡)并网场景

### 失效边界

- **参数独立假设不成立**: 单独优化 PLL 带宽不保证整体系统稳定，必须校核与外环、内环的交互
- **弱网下常规经验失效**: 强网经验"高带宽好"在弱网(SCR<2)下可能触发失稳，降低参数反而有利
- **频率冻结依赖暂态检测**: 若暂态检测阈值不当(如 Ranasinghe 2024 取 $ε=0.1$ rad)，可能误触发或漏触发
- **单篇论文结论不可外推**: Ranasinghe 2024 的参数(62 rad/s, Kp=57.1)适用于其特定 DSOGI 结构，不适用于 SRF-PLL 或其他拓扑
- **忽略 PCC 电容效应**: Li 2024 表明 PCC 并联等效电容(0.15pu)显著改变稳定边界，忽略电容的参数设计在高无功工况下可能失稳

### 关键假设

- PLL 参数设计通常采用小信号线性化模型，假设扰动在平衡点附近
- 自适应策略假设暂态检测可靠、带宽切换速度足够快
- RMS+ 失稳边界(Carreño 2026)基于时间尺度分离假设($τ_L/τ_PLL < 0.1$)

## 代表性来源

- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]: DSOGI-PLL 自适应带宽参数设计，提供标称带宽 62 rad/s、PI 参数 Kp=57.1/Ki=1660.1、暂态放大 5 倍等具体设计值
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]: PLL 参数与网络交互失稳边界，提供跨临界分岔和 Hopf 分岔解析条件
- [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver]]: 外环-PLL 参数联合整定，阐明 PLL 带宽接近外环带宽不必然引起谐振失稳

## 数值证据汇总

| 参数 | 值 | 来源 |
|------|-----|------|
| 标称穿越频率 | 62 rad/s | Ranasinghe 2024 |
| 暂态带宽放大倍数 | 5 倍 | Ranasinghe 2024 |
| PI 增益(Kp, Ki) | 57.1, 1660.1 | Ranasinghe 2024 |
| 目标阻尼比 | 0.7 | Ranasinghe 2024 |
| 相位误差阈值 | 0.1 rad | Ranasinghe 2024 |
| 频率冻结时间 | 0.1 s | Ranasinghe 2024 |
| Kp 临界值(跨临界分岔) | 1/(i_P L) | Carreño 2026 |
| 耦合强度系数阈值 | κ > 0.05 进入弱阻尼 | Carreño 2026 |
| 主导极点(外环+PLL) | -19.6±j3.9 | Li 2024 |
| PLL 相关谐振频率 | 70.3 Hz | Li 2024 |

## 开放问题

- 自适应带宽的频率冻结时间与系统惯性之间缺乏通用整定规则
- PLL 参数如何与限流、VSG 虚拟惯量和弱网稳定性联合整定仍需进一步研究
- 多机并联场景下各 PLL 参数之间的交互耦合机制尚不明确

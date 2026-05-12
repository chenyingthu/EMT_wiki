---
title: "同步旋转坐标系锁相环方法 (SRF-PLL)"
type: method
tags: [srf-pll, pll, synchronization, grid-following, inverter-control]
created: "2026-05-04"
updated: "2026-05-10"
---

# 同步旋转坐标系锁相环方法 (SRF-PLL)

## 1. 定义与边界

同步旋转坐标系锁相环（Synchronous Reference Frame PLL, SRF-PLL）是最经典、应用最广泛的并网变流器同步方法。其基本原理是：将三相电网电压经 Park 变换（abc→dq）投影到同步旋转坐标系后，通过闭环调节使 q 轴电压 $v_q$ 收敛至零，从而估计电网电压的相位角和频率。

SRF-PLL 是众多高级 PLL 结构（如 DSOGI-PLL、解耦双同步参考坐标系 PLL 等）的数学基础和性能基线 [Ranasinghe 2024]。本页聚焦 SRF-PLL 的 EMT 仿真建模、参数设计与弱网失稳机理。不讨论具体拓扑变体（如 DSOGI、增强型 PLL）或与其无关的惯量控制方法。

## 2. EMT 仿真中的作用

在 EMT 仿真中，SRF-PLL 的关键作用包括：

1. **同步信号生成**: 为跟网型逆变器提供电网电压相位角 $	heta$ 和频率 $$，支撑 dq 坐标变换和电流/功率控制。
2. **弱网稳定性分析**: SRF-PLL 与电网阻抗的交互是 GFL-VSC 小信号失稳的主要机制，涉及跨临界分岔和 Hopf 分岔两种模式 [Carreño 2026]。
3. **控制性能基线**: 作为衡量更复杂 PLL 结构（DSOGI-PLL、自适应带宽 PLL 等）性能改进的对照参考。
4. **初始化关键环节**: SRF-PLL 的状态变量（PI 输出、角度积分器）需要在 EMT 启动时精确初始化，否则会导致仿真从零初值经历数百毫秒的非物理暂态过程 [Guilherme 2023]。

## 3. 关键原理与算法

### 3.1 基本结构

SRF-PLL 由三个环节组成：
1. **Park 变换**: 将三相电压 $v_{abc}$ 变换到 dq 坐标系
2. **环路滤波器（PI 控制器）**: 调节 $v_q$ 至零，输出频率偏差 $$ 或 $$ 
3. **压控振荡器（积分器）**: 对频率积分得到估计相位 $	heta$

### 3.2 小信号模型与失稳机理

Carreño 2026 基于慢快系统理论推导了 SRF-PLL 在弱电网条件下的完整失稳边界。核心物理机制是电感 $di/dt$ 效应通过 PLL 闭环反馈影响同步稳定性。

**跨临界分岔条件**（单调失稳）：

$$1 - K_p i_P L > 0$$

当 PLL 比例增益 $K_p$ 与有功电流 $i_P$ 和电网电感 $L$ 的乘积超过 1 时，系统发生跨临界分岔。传统 RMS 模型由于忽略 $di/dt$，会错误地预测系统在所有参数下稳定（误差 100%）[Carreño 2026]。

**Hopf 分岔条件**（振荡失稳）：

$$K_p 	{V^2 - (i_P X)^2} - K_i i_P L > 0$$

当该不等式被违反时，系统出现持续的低频振荡（0.5-2 Hz）。

### 3.3 参数设计与带宽

SRF-PLL 的 PI 参数通过开环传递函数设计 [Ranasinghe 2024]：

$$G_{ol} = t(K_p s + K_i}{s}
t) 	{1}{s}$$

闭环特征方程对应二阶系统，自然频率 $$ 和阻尼比 $	$ 与 PI 参数的关系为：

$$ = 	{K_i}, 	{K_p}{2	{K_i}}$$

**典型参数范围**:
| 应用场景 | ωc (rad/s) | Kp | Ki | ξ | 来源 |
|---------|-----------|----|----|----|------|
| 60Hz 跟网逆变器 | 62 | 57.1 | 1660.1 | 0.7 | [Ranasinghe 2024] |
| ATP 等效模型 | - | 0.8 | 61.69 | - | [Luchini 2023] |

### 3.4 与 SCR 的耦合关系

短路比（SCR）与 SRF-PLL 失稳风险呈强相关性 [Carreño 2026]：
- SCR < 2.0 时，Hopf 分岔临界功率从 0.9 pu 降至 0.55 pu（下降 40%）
- 耦合强度系数 $	 = K_p 	 i_P 	 L / $ 是评估失稳风险的综合指标
- 当 $	 > 0.05$ 时系统进入弱阻尼区域（阻尼比 $	 < 0.1$）

### 3.5 初始化

SRF-PLL 的稳态初始化精度直接影响 EMT 仿真启动质量 [Guilherme 2023]：
- 角度积分器初值：$	 = 	 + 	 H(j)}$，其中 $H(j) = 1/(1+j	)$ 为 LPF 传递函数
- PI 控制器输出初值设为 0（稳态频率偏差为零）
- 若不初始化，PLL 角度与电网电压相位不一致会导致 300 ms 以上的数值振荡

## 4. 关键公式

| 公式 | 含义 | 来源 |
|------|------|------|
| $v_q 	 0$ | SRF-PLL 控制目标（锁相条件） | 基本定义 |
| $1 - K_p i_P L > 0$ | 跨临界分岔稳定条件 | [Carreño 2026] |
| $K_p	{V^2-(i_P X)^2} - K_i i_P L > 0$ | Hopf 分岔稳定条件 | [Carreño 2026] |
| $	 = K_p 	 i_P 	 L / $ | PLL-电网耦合强度系数 | [Carreño 2026] |
| $	 = 	 + 	 H(j)$ | PLL 角度初始化公式 | [Guilherme 2023] |
| $ = 	{K_i}$ | SRF-PLL 自然频率 | [Ranasinghe 2024] |
| $i_d = 2P/(3v_d), i_q = -2Q/(3v_d)$ | 电网电压定向电流反解 | [Luchini 2023] |

## 5. 与相关方法的关系

- **[[phase-locked-loop]]**: PLL 总入口，SRF-PLL 是最基础的结构分支。
- **[[dsogi-pll]]**: DSOGI-PLL 在 SRF-PLL 前增加正交信号发生器，在电网畸变/不平衡时精度优于 SRF-PLL [Ranasinghe 2024]。
- **[[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]**: 在 DSOGI-PLL 基础上增加暂态冻结和自适应带宽，SCR 极限从 2.3 扩展至 1.0 [Ranasinghe 2024]。
- **[[grid-connected-inverter]]**: SRF-PLL 是跟网型变流器（GFL）的默认同步策略。
- **[[pll-design]]**: SRF-PLL 的参数整定（带宽、阻尼比）是该页面的核心内容。
- **[[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]**: RMS+ 模型揭示 SRF-PLL 与电网电感耦合的失稳机理 [Carreño 2026]。
- **[[grid-forming-converters-sufficient-conditions-for-rms-modeling]]**: GFM 控制与 GFL+SRF-PLL 的同步机制对比。

## 6. 适用边界与失效模式

### 适用条件
- 电网强度较好（SCR ≥ 2）的跟网型逆变器并网场景
- 三相电压对称、谐波含量较低的工况
- 需要快速实现标准 dq 解耦控制的系统级 EMT 仿真

### 失效边界
- **弱电网（SCR < 2）**: SRF-PLL 在弱电网中存在跨临界分岔和 Hopf 分岔两种失稳模式 [Carreño 2026]
- **严重不平衡/畸变电压**: SRF-PLL 仅跟踪基波正序，负序和零序分量会在 dq 坐标系中产生 100 Hz 脉动，导致相位估计误差
- **电压幅值骤降**: 幅值波动通过 PI 环路耦合影响带宽，造成同步动态退化 [Ranasinghe 2024]
- **单相故障**: 不对称故障期间 SRF-PLL 的相位估计误差显著增大，可能触发逆变器保护脱网
- **高频谐波**: SRF-PLL 不含预滤波器，对 PWM 谐波和背景谐波敏感，需要额外 LPF 或陷波器

### 关键假设
- 电网电压频率在标称值附近缓慢变化，不适用于频率剧烈波动的孤岛或黑启动场景
- PI 参数设计时假设电网阻抗为理想或已知常数，实际中电网阻抗变化可能使预设参数不再最优

## 7. 代表性来源与数值证据

### 数值证据汇总

| 来源 | 关键数值 | 方法核心 |
|------|---------|---------|
| [Carreño 2026] | Kp·iP·L > 1 时跨临界分岔, SCR<2 时临界功率降 40%, κ>0.05 时 ζ<0.1, 状态数降 75% | RMS+ 模型精确捕捉 SRF-PLL 失稳 |
| [Ranasinghe 2024] | 60Hz 系统 ωc=62 rad/s, Kp=57.1, Ki=1660.1; 改进 PLL 使 SCR 从 2.3→1.0 | DSOGI-PLL 以 SRF-PLL 为基线 |
| [Luchini 2023] | Kp=0.8, Ki=61.69; 误差 2.33%, 速度提升 70% | SRF-PLL 用于 ATP 等效模型同步 |
| [Guilherme 2023] | 未初始化 → 300ms+ 暂态; 初始化公式 θ̂=θ+∠H(jω) | SRF-PLL 稳态初始化流程 |

### 代表论文

- **[[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]**: Carreño 2026, RMS+ 模型揭示 SRF-PLL 与网络电感交互的双模失稳机理
- **[[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]**: Ranasinghe 2024, 以 SRF-PLL 为基线的 DSOGI-PLL 改进，暂态检测+自适应带宽
- **[[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]]**: Luchini 2023, 采用 SRF-PLL 的跟网型 IBR 等效模型
- **[[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in]]**: Guilherme 2023, 含 SRF-PLL 的 VSC 稳态初始化三阶段流程

## 来源论文

| 论文 | 年份 | 关注点 |
|------|------|--------|
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability|RMS+: PLL Instability"]] | 2026 | SRF-PLL 失稳机理 |
| [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of|Advanced DSOGI PLL"]] | 2024 | DSOGI-PLL vs SRF-PLL 基线 |
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati|GF-IBR Model"]] | 2023 | SRF-PLL 在 ATP 中的应用 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|VSC Steady-State Initialization"]] | 2023 | SRF-PLL 初始化 |
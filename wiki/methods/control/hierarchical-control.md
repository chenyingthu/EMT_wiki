---
title: "分层控制 (Hierarchical Control)"
type: method
tags: [hierarchical-control, primary-control, secondary-control, tertiary-control, coordination, droop-control, time-scale-separation, bandwidth-separation]
created: "2026-05-05"
updated: "2026-05-14"
---

# 分层控制 (Hierarchical Control)

## 定义

分层控制是把控制任务按**时间尺度**和**职责边界**逐级分解为一次（Primary）、二次（Secondary）、三次（Tertiary）乃至更高层级的组织方法。其核心思想是**快慢解耦**：每一层负责一个特定的动态时间尺度，层内闭环带宽远大于层间耦合速率，从而避免跨层交互导致的失稳。

分层控制在 EMT 仿真中的独特价值在于：EMT 的亚微秒~毫秒级步长能够**直接解析**各层控制器的暂态交互——这是机电暂态仿真无法做到的。Nguyen (2021) 在 PSCAD/EMTDC 中用 ~10 μs 步长完整仿真了 GFM 逆变器一次下垂环（~1 ms 时间常数）与二次 PI 恢复环（~100 ms 时间常数）的耦合过程；Liu (2014) 在 EMTDC 中用 ~50 μs 步长仿真了 LCC-HVDC 整流/逆变侧三层控制（阀控→极控→主控）的阶跃响应。

## EMT 中的角色

分层控制在 EMT 仿真中承担以下关键角色：

1. **时间尺度分离验证**：EMT 能够直接观测一次、二次、三次控制之间由于带宽重叠导致的交互振荡。例如，当二次控制积分时间常数与一次下垂环时间常数之比 < 10 时，EMT 仿真中会出现明显的频率超调叠加（Nguyen 2021）。
2. **通信延迟传播分析**：二次/三次控制的分布式一致性协议依赖通信网络，EMT 可量化通信延迟（通常 10~100 ms）对控制稳定性的影响。Rault (2020) 在 HIL 平台中验证了 DCCB 控制器与换流器控制器之间的通信延迟导致故障切除时间增加 0.5~2 ms。
3. **模式切换暂态**：分层控制在故障穿越、黑启动、并网/离网切换等工况下的模式切换逻辑需要在 EMT 中验证——这些切换涉及控制参数的实时重初始化（Allabadi 2024）。
4. **跨层参数整定**：EMT 仿真可帮助确定各层控制器的增益、积分时间常数和限幅参数，确保层间带宽分离充分。

## 层级分解与数学描述

### 一次控制层（Primary Control）

一次控制是**最快**的控制层，响应时间在 **微秒~毫秒级**，通常部署在逆变器/变流器的本地控制器中，无需通信。其核心是**下垂控制（Droop Control）**和**虚拟同步机（VSG）**。

**有功-频率下垂（P-f droop）**：

$$
\omega_i(t) = \omega_0 - m_{p,i} \cdot \left( P_i(t) - P_i^{\star} \right)
$$

**无功-电压下垂（Q-V droop）**：

$$
V_i(t) = V_0 - n_{q,i} \cdot \left( Q_i(t) - Q_i^{\star} \right)
$$

其中 $\omega_0 = 2\pi f_0$ 为额定角频率，$V_0$ 为额定电压幅值，$m_{p,i}$、$n_{q,i}$ 为第 $i$ 台设备的下垂系数。下垂系数决定了功率分配的稳态精度：当 $n$ 台设备并联运行时，稳态功率分配满足

$$
m_{p,1} P_1^{\text{ss}} = m_{p,2} P_2^{\text{ss}} = \cdots = m_{p,n} P_n^{\text{ss}}
$$

即各设备有功输出与下垂系数倒数成正比。

**虚拟同步机（VSG）扩展**：在 P-f 下垂基础上增加虚拟惯量 $J_i$ 和阻尼 $D_i$，模拟同步机转子运动方程：

$$
J_i \frac{d\omega_i}{dt} = \frac{P_i^{\star} - P_i(t)}{\omega_0} - D_i \cdot (\omega_i(t) - \omega_0)
$$

$$
V_i(t) = V_0 - n_{q,i} \cdot \left( Q_i(t) - Q_i^{\star} \right)
$$

VSG 的惯量时间常数 $\tau_{J,i} = J_i / \omega_0$ 决定了频率变化的初始响应速率。Nguyen (2021) 的黑启动模型中，一次下垂环的时间常数约为 10~50 ms。

**下垂系数的工程取值范围**：

|| 设备类型 | $m_p$ (Hz/kW 或 p.u./p.u.) | $n_q$ (V/kvar 或 p.u./p.u.) | 典型下垂百分比 |
|----------|-----------------------------|-----------------------------|-------------------|
| 并网 GFM 逆变器 | 0.001~0.01 (Hz/kW) | 0.0005~0.005 (V/kvar) | 2~5% |
| 微电网 DG | 0.002~0.02 (Hz/kW) | 0.001~0.01 (V/kvar) | 3~10% |
| LCC-HVDC 极控 | 0.05~0.2 (p.u./p.u.) | N/A | 5~20% |

### 二次控制层（Secondary Control）

二次控制以**较慢时间尺度**（**100 ms ~ 数秒**）运行，负责**消除一次控制的稳态偏差**。其核心是**PI 补偿**和**分布式一致性协议**。

**集中式二次恢复（PI）**：

$$
f_i^{\text{ref}}(t) = f_i^{\text{primary}}(t) + K_{pf,i} \cdot e_f(t) + K_{if,i} \int_0^t e_f(\tau) d\tau
$$

$$
V_i^{\text{ref}}(t) = V_i^{\text{primary}}(t) + K_{pv,i} \cdot e_v(t) + K_{iv,i} \int_0^t e_v(\tau) d\tau
$$

其中 $e_f = f_0 - f_i$、$e_v = V_0 - V_i$ 分别为频率和电压偏差，$K_{pf}, K_{if}, K_{pv}, K_{iv}$ 为 PI 增益。

Nguyen (2021) 在黑启动模型中采用集中式 PI 二次恢复，PI 积分时间常数约为 50~200 ms，使黑启动完成后频率精确收敛至 60 Hz。二次控制的时间尺度比一次慢一个数量级，避免两个层级相互干扰。

**分布式一致性二次控制**：各设备仅与邻居通信，通过一致性协议使频率和电压恢复至额定值。对于网络拓扑为图 $G = (V, E)$ 的系统，一致性更新律为：

$$
\dot{x}_i(t) = \sum_{j \in \mathcal{N}_i} a_{ij} \cdot \left( x_j(t) - x_i(t) \right)
$$

其中 $x_i$ 为频率或电压偏差，$a_{ij}$ 为邻接矩阵元素，$\mathcal{N}_i$ 为节点 $i$ 的邻居集合。林继灿 (2023) 将此方法应用于多 VSG 并联系统的有功振荡抑制，通过互阻尼补偿实现分布式二次协调。

**二次控制的带宽约束**：二次 PI 控制器的带宽应低于一次下垂环带宽的 1/10，但高于三次控制带宽的 10 倍。若二次带宽与一次带宽之比 > 0.1，EMT 仿真中会出现明显的层间振荡。

### 三次控制层（Tertiary Control）

三次控制负责**功率调度、经济运行和能量管理**，时间尺度通常在**秒~分钟级**，一般不在 EMT 仿真中直接体现。但在 EMT 中，三次控制输出的**参考值变化**（如经济调度指令的阶跃）会作为二次控制的输入，其影响可通过 EMT 仿真量化。

**经济调度参考更新**：

$$
P_i^{\star}(t_k) = \arg\min_{P} \sum_{i=1}^{n} C_i(P_i) \quad \text{s.t.} \quad \sum_{i=1}^{n} P_i = P_{\text{load}}, \quad P_i^{\min} \leq P_i \leq P_i^{\max}
$$

其中 $C_i(P_i)$ 为第 $i$ 台设备的成本函数，$t_k$ 为调度周期（通常 5~15 分钟）。

**LCC-HVDC 的三层控制架构**（Liu 2014）：

Liu (2014) 在 EMTDC 中仿真了云广 ±800 kV UHVDC 的三层控制架构：

1. **阀控层（Valve Control）**：触发角生成，响应时间 ~0.1 ms
2. **极控层（Pole Control）**：定电流/定功率控制，响应时间 ~10 ms
3. **主控层（Master Control）**：功率/频率设定，响应时间 ~100 ms

整流侧采用定电流/定功率两种控制模式，逆变侧采用定关断角 + 定电流 + VDCOL 协调控制。定功率模式暂态变化率较定电流模式降低 20~30%。故障电流峰值 1.5~1.6 p.u.，恢复时间 0.2~0.4 s。

### 控制层级时间尺度总览

|| 层级 | 响应时间 | 主要控制方法 | EMT 步长要求 | 典型带宽 |
|------|--------|-----------|-------------|------------|----------|
| 一次 | 10 μs ~ 50 ms | 下垂、VSG、限流 | ≤ 10 μs | 10 ~ 1000 Hz |
| 二次 | 50 ms ~ 5 s | PI 恢复、一致性 | ≤ 100 μs | 0.2 ~ 20 Hz |
| 三次 | 5 s ~ 15 min | 经济调度、能量管理 | ≤ 1 ms | 0.001 ~ 0.2 Hz |

## EMT 实现细节

### 离散化与时间步长

分层控制在 EMT 仿真中的离散化需要特别注意**多速率问题**：一次控制可能需要 ~1 μs 步长（开关级），而二次控制可用 ~100 μs 步长。Wang (2026) 指出，传统 EMT 仿真中功率系统和控制系统分开求解会导致**外部时延**（一个时间步长的信息传递延迟），在高频控制交互场景下可能引起数值不稳定。

**同时求解方法**（Wang 2026）：利用变换器仿真中状态空间矩阵的三角块结构，将功率系统和控制系统方程合并为统一的状态空间矩阵，通过指数积分器（Exponential Integrator）同时求解，消除外部时延。核心数学思路是将非对角块的矩阵指数求解问题转化为 Sylvester 方程：

$$
e^{\mathbf{A}h} = \begin{bmatrix} e^{\mathbf{A}_{pp}h} & \mathbf{X} \\ 0 & e^{\mathbf{A}_{cc}h} \end{bmatrix}
$$

其中 $\mathbf{X}$ 满足 Sylvester 方程：

$$
\mathbf{A}_{cc} \mathbf{X} - \mathbf{X} \mathbf{A}_{pp} = \mathbf{A}_{cp} \cdot \frac{e^{\mathbf{A}_{pp}h} - I}{\mathbf{A}_{pp}} \cdot \mathbf{A}_{pc}
$$

这种方法使功率和控制变量在同一时间步内同步更新，提高了换流器仿真的精度。

### 通信延迟建模

二次和三次控制依赖通信网络，通信延迟 $\tau_{\text{comm}}$ 在 EMT 中需要显式建模。对于分布式一致性控制，延迟会导致一致性协议的不稳定：

$$
\dot{x}_i(t) = \sum_{j \in \mathcal{N}_i} a_{ij} \cdot \left( x_j(t - \tau_{\text{comm}}) - x_i(t - \tau_{\text{comm}}) \right)
$$

Rault (2020) 在 HIL 平台中实测 DCCB 控制器与换流器控制器之间的通信延迟为 0.5~2 ms，导致故障切除时间增加。当通信延迟超过控制周期的一半时，一致性协议可能发散。

### 模式切换与抗饱和

分层控制在故障穿越、黑启动等工况下需要模式切换。模式切换涉及**控制参数的实时重初始化**：

- **黑启动**：GFM 逆变器从 PQ 模式切换到 V/f 模式，下垂系数从零逐步增加到设定值（Allabadi 2024）
- **故障穿越**：下垂控制被限流/保护逻辑覆盖，故障清除后需要平滑恢复下垂关系
- **并网/离网切换**：GFM 逆变器的 PLL 从锁相模式切换到自建频率模式

Allabadi (2024) 提出的 CISS（Control Initialization in Steady State）方法通过稳态分析初始化 GVSC 的外层控制系统，将 MTDC 系统初始化时间减少 6.9 倍。

## 形式化表达

### 分层控制统一框架

分层控制可抽象为多时间尺度系统的级联更新：

$$
\begin{aligned}
\text{一次层（快）:} \quad & \dot{\mathbf{x}}_1 = \mathbf{f}_1(\mathbf{x}_1, \mathbf{u}_1) \\
\text{二次层（中）:} \quad & \dot{\mathbf{x}}_2 = \frac{1}{\varepsilon_2} \mathbf{f}_2(\mathbf{x}_1, \mathbf{x}_2, \bar{\mathbf{y}}) \\
\text{三次层（慢）:} \quad & \dot{\mathbf{x}}_3 = \frac{1}{\varepsilon_3} \mathbf{f}_3(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, \mathcal{O}, \mathcal{C})
\end{aligned}
$$

其中 $\varepsilon_2 \ll 1$、$\varepsilon_3 \ll \varepsilon_2$ 为时间尺度分离参数。$\bar{\mathbf{y}}$ 为邻居协调信息，$\mathcal{O}$、$\mathcal{C}$ 为运行目标和约束。

### 层间带宽分离条件

为确保各层解耦，需满足：

$$
\frac{\omega_{\text{primary}}}{\omega_{\text{secondary}}} \geq 10, \qquad \frac{\omega_{\text{secondary}}}{\omega_{\text{tertiary}}} \geq 10
$$

其中 $\omega_{\text{primary}}$、$\omega_{\text{secondary}}$、$\omega_{\text{tertiary}}$ 分别为各层的闭环带宽。

### 下垂-恢复耦合的稳态误差

一次下垂 + 二次 PI 控制的稳态频率误差为：

$$
e_f^{\text{ss}} = \frac{1}{1 + K_{if}/(s \cdot m_p)} \bigg|_{s \to 0} = 0 \quad (\text{PI 积分消除稳态误差})
$$

但若二次 PI 积分饱和（抗饱和未启用），稳态误差可能不为零。

## 关键技术挑战

### 挑战 1：层间带宽重叠导致的交互振荡

当一次和二次控制的带宽分离不充分时（比值 < 10），EMT 仿真中会出现明显的频率超调叠加。Nguyen (2021) 观察到，当二次 PI 积分时间常数 < 50 ms 时，黑启动过程中的负荷阶跃会引发频率二次振荡。

### 挑战 2：通信延迟与拓扑变化的稳定性

分布式一致性二次控制在非理想通信条件下的稳定性缺乏系统验证。通信延迟 > 100 ms 或拓扑频繁变化时，一致性协议可能发散。现有文献多基于理想通信假设，实际 HIL 平台中实测延迟为 0.5~2 ms（Rault 2020），但分布式一致性协议的通信延迟容忍度通常在 50~200 ms 范围。

### 挑战 3：模式切换的平滑过渡

黑启动、故障穿越、并网/离网切换等工况涉及控制模式的实时切换。切换瞬间的控制参数重初始化可能引发暂态冲击。Allabadi (2024) 的 CISS 方法通过稳态分析减少切换冲击，但切换过程中的动态响应仍需 EMT 验证。

### 挑战 4：限幅与抗饱和

当下垂环生成的 PQ 参考点超出设备额定约束时，需启用限流或抗饱和机制。Nurunnabi (2025) 指出，基础下垂控制（FDR）在限幅时丢失电压支撑能力，而增强型电压调节（EVR）在限幅时保留电压支撑能力。限幅激活后下垂关系的恢复特性缺乏标准测试方法。

### 挑战 5：EMT 多速率仿真的计算效率

一次控制需要 ~1 μs 步长，二次控制可用 ~100 μs 步长。多速率仿真需要处理不同时间步长之间的数据插值和状态传递。Wang (2026) 提出的同时求解方法消除了外部时延，但增加了矩阵运算复杂度。

## 量化性能边界

**Nguyen 2021 GFM 黑启动一次+二次分层控制（改进 IEEE 9 节点，PSCAD/EMTDC）**：
- 一次下垂（P-f/Q-V）提供快速本地电压/频率支撑，二次 PI 补偿稳态偏差
- 黑启动全过程 18 s 含 7 个切换步，频率精确收敛至 60 Hz
- 稳态电压误差 < 1%（与数值优化解对比），负荷阶跃最大 120.2 MW + 42.3 Mvar
- 验证平台：PSCAD/EMTDC 高保真模型，光储混合电站
- 数据缺口：下垂系数 $m_p$、$n_q$ 的取值依据和灵敏度未系统报告

**Nurunnabi 2025 GFM 逆变器 PQ 能力与增强型电压调节（EVR）**：
- 对比基础下垂（FDR）与增强型电压调节（EVR）两层控制
- EVR 在限幅时保留电压支撑能力，电压偏差 < 2.9%，频率偏差 < 0.37%
- SVPWM 输出能力达 1.53 p.u. vs SPWM 1.33 p.u.
- 含 L、LC、LCL 三种滤波器拓扑 PQ 运行域对比，满足 IEEE 1547 标准
- 验证方式：EMT 仿真 + 实时 HIL
- 数据缺口：EVR 策略的控制参数整定方法未系统报告

**Liu 2014 云广 ±800 kV UHVDC 分层控制模式分析（EMTDC）**：
- LCC-HVDC 三层控制架构：主控层（功率/频率）→ 极控层（电流）→ 阀控层（触发）
- 整流侧：定电流/定功率两种模式；逆变侧：定关断角 + 定电流 + VDCOL 协调
- 定功率模式暂态变化率较定电流模式降低 20~30%
- 故障电流峰值 1.5~1.6 p.u.，恢复时间 0.2~0.4 s
- 整流侧定电流 PI 控制：比例增益 1.0989，积分时间常数 0.01092 s
- 逆变侧定电流 PI 控制：比例增益 0.63，积分时间常数 0.01524 s
- 定关断角控制：比例增益 0.7506，积分时间常数 0.0544 s
- VDCOL 特性：当 $0.4 < U_{\text{dc,pu}} < 0.9$ 时，$I_{\text{dc,pu}}$ 与 $U_{\text{dc,pu}}$ 呈 0.9 倍比例关系
- 数据缺口：仅分析云广工程特定参数，通用性待验证

**Allabadi 2024 GFM VSC 初始化（CIGRE BM4 基准，EMTP）**：
- CISS 方法通过稳态分析初始化 GVSC 外层控制系统
- 与现有潮流初始化方法相比，系统初始化时间减少 6.9 倍
- 适用于黑盒 GVSC 模型（Decoupling Interface 方法）
- 数据缺口：初始化方法对控制参数摄动的鲁棒性未系统评估

**Rault 2020 DCCB 控制器实时仿真（三端直流电网，HIL）**：
- DCCB 控制器与换流器控制器之间的通信延迟实测 0.5~2 ms
- 通信延迟导致故障切除时间增加
- 12 个 DCCB 物理控制器 + 1 个 MMC 换流器站
- 验证平台：HIL 实时仿真平台，ABB DCCB 和换流器物理控制器
- 数据缺口：通信延迟对一致性协议稳定性的定量影响未系统分析

## 适用边界与选择指南

### 适用场景

|| 场景 | 推荐层级 | EMT 仿真必要性 |
|------|------|----------|---------------|
| 微电网黑启动 | 一次+二次 | 必须（验证电压/频率建立） |
| 多逆变器并联功率共享 | 一次 | 可选（稳态功率分配可用解析法） |
| LCC-HVDC 故障恢复 | 一次+二次+三次 | 必须（换相失败分析需要详细控制模型） |
| MTDC 系统初始化 | 一次+二次 | 推荐（CISS 方法验证） |
| 分布式一致性协调 | 二次 | 推荐（通信延迟影响需 EMT 量化） |

### 不适用场景

- **仅关注单台逆变器的本地控制**：应使用 [[droop-control]] 或 [[grid-forming-control]]
- **大型输电系统的一次调频**：惯性和一次调频机制与逆变器下垂控制不同，应使用机电暂态仿真
- **器件级热/损耗模型**：与分层控制无关，应使用 [[switch-modeling]] 或 [[igbt-model]]

### 层间带宽设计准则

|| 设计参数 | 推荐范围 | 依据 |
|----------|----------|--------|------|
| 一次/二次带宽比 | ≥ 10 | Nguyen 2021 | 避免层间振荡 |
| 二次/三次带宽比 | ≥ 10 | 通用准则 | 避免调度指令干扰 |
| 二次 PI 积分时间常数 | 50~200 ms | Nguyen 2021 | 黑启动稳定 |
| 通信延迟容忍度 | < 50 ms | Rault 2020 | 一致性协议稳定 |
| 下垂百分比 | 2~10% | 通用准则 | IEEE 1547 |

## 方法体系架构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg">
  <!-- 标题 -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">分层控制架构：时间尺度与职责分解</text>

  <!-- 一次控制层（蓝） -->
  <rect x="80" y="50" width="740" height="100" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#2563eb">一次控制层 (Primary) · 10 μs ~ 50 ms · 10 ~ 1000 Hz</text>

  <!-- 一次控制方法卡片 -->
  <rect x="100" y="88" width="170" height="50" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="185" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">P-f / Q-V 下垂</text>
  <text x="185" y="120" text-anchor="middle" font-size="9" fill="#666">ω = ω₀ - mₚ(P-P*)</text>

  <rect x="290" y="88" width="170" height="50" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="375" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">VSG 虚拟惯量</text>
  <text x="375" y="120" text-anchor="middle" font-size="9" fill="#666">J·dω/dt = (P*-P)/ω₀ - D·Δω</text>

  <rect x="480" y="88" width="170" height="50" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="565" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">限流/保护</text>
  <text x="565" y="120" text-anchor="middle" font-size="9" fill="#666">RIC + PWM 饱和约束</text>

  <rect x="670" y="88" width="130" height="50" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="735" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">内环 dq 控制</text>
  <text x="735" y="120" text-anchor="middle" font-size="9" fill="#666">电流环 + 电压环</text>

  <!-- 箭头向下 -->
  <line x1="450" y1="150" x2="450" y2="180" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- 二次控制层（绿） -->
  <rect x="80" y="185" width="740" height="100" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="210" text-anchor="middle" font-size="14" font-weight="bold" fill="#16a34a">二次控制层 (Secondary) · 50 ms ~ 5 s · 0.2 ~ 20 Hz</text>

  <rect x="130" y="223" width="200" height="50" rx="4" fill="#ffffff" stroke="#16a34a" stroke-width="1"/>
  <text x="230" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#16a34a">集中式 PI 恢复</text>
  <text x="230" y="255" text-anchor="middle" font-size="9" fill="#666">f_ref = f_pri + Kp·e + Ki∫e</text>

  <rect x="350" y="223" width="200" height="50" rx="4" fill="#ffffff" stroke="#16a34a" stroke-width="1"/>
  <text x="450" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#16a34a">分布式一致性</text>
  <text x="450" y="255" text-anchor="middle" font-size="9" fill="#666">ẋᵢ = Σaᵢⱼ(xⱼ(t-τ) - xᵢ(t-τ))</text>

  <rect x="570" y="223" width="200" height="50" rx="4" fill="#ffffff" stroke="#16a34a" stroke-width="1"/>
  <text x="670" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#16a34a">VDCOL 低压限流</text>
  <text x="670" y="255" text-anchor="middle" font-size="9" fill="#666">I_dc = 0.9 · U_dc (U_dc,pu ∈ [0.4,0.9])</text>

  <!-- 箭头向下 -->
  <line x1="450" y1="285" x2="450" y2="315" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- 三次控制层（黄） -->
  <rect x="80" y="320" width="740" height="100" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="345" text-anchor="middle" font-size="14" font-weight="bold" fill="#d97706">三次控制层 (Tertiary) · 5 s ~ 15 min · 0.001 ~ 0.2 Hz</text>

  <rect x="160" y="358" width="180" height="50" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="250" y="375" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">经济调度</text>
  <text x="250" y="390" text-anchor="middle" font-size="9" fill="#666">min ΣCᵢ(Pᵢ) s.t. ΣPᵢ = P_load</text>

  <rect x="360" y="358" width="180" height="50" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="450" y="375" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">能量管理</text>
  <text x="450" y="390" text-anchor="middle" font-size="9" fill="#666">储能SOC管理/功率分配</text>

  <rect x="560" y="358" width="180" height="50" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="650" y="375" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">调度指令更新</text>
  <text x="650" y="390" text-anchor="middle" font-size="9" fill="#666">P* 周期更新 (5~15 min)</text>

  <!-- 箭头 -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>

  <!-- 底部图例 -->
  <rect x="100" y="440" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="118" y="450" font-size="10" fill="#666">一次控制</text>
  <rect x="200" y="440" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="218" y="450" font-size="10" fill="#666">二次控制</text>
  <rect x="300" y="440" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="318" y="450" font-size="10" fill="#666">三次控制</text>
  <text x="420" y="450" font-size="10" fill="#666">核心原则：层间带宽比 ≥ 10，通信延迟 < 50 ms</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 分层控制架构：时间尺度与职责分解</p>

## 相关方法

- [[droop-control]]：一次控制层的核心方法，下垂方程、PQ 能力边界、限流机制
- [[grid-forming-control]]：GFM 逆变器控制，构网型下垂与 VSG 的详细实现
- [[distributed-control]]：分布式一致性协议，二次控制的通信拓扑和收敛性
- [[microgrid-control]]：微电网场景中的分层控制组合，黑启动、孤岛运行
- [[vsc-control]]：VSC-HVDC 控制架构，与分层控制的交叉
- [[economic-dispatch]]：三次控制的经济调度方法，参考值生成
- [[adaptive-droop]]：下垂系数的在线调整，一次控制的参数自适应
- [[inertia-control]]：虚拟惯量注入，一次控制的惯量增强
- [[hierarchical-control]]：（自引用）分层控制的整体框架

## 来源论文

- **Nguyen 2021** — 光储 GFM 黑启动控制，一次下垂 + 二次 PI 恢复，18 s/7 步黑启动流程，稳态电压误差 < 1%，频率精确收敛至 60 Hz。提供了 GFM 逆变器分层控制在 EMT 中的完整实现范例。
- **Liu 2014** — 云广 ±800 kV UHVDC 三层控制架构（主控→极控→阀控），定电流/定功率模式对比，VDCOL 特性参数，故障恢复量化数据。提供了 HVDC 场景下分层控制的详细参数。
- **Nurunnabi 2025** — GFM 逆变器 PQ 能力边界，EVR 增强型电压调节在限幅时的电压支撑能力，电压偏差 < 2.9%，频率偏差 < 0.37%。提供了下垂控制与限流机制的交互分析。
- **Allabadi 2024** — GFM VSC 初始化方法（CISS + DI），系统初始化时间减少 6.9 倍。提供了分层控制在 MTDC 系统初始化中的应用。
- **Rault 2020** — DCCB 控制器 HIL 实时仿真，通信延迟实测 0.5~2 ms，故障切除时间影响。提供了分层控制在保护协调中的实际应用。
- **Wang 2026** — 功率与控制方程的同时求解方法，消除 EMT 外部时延，Sylvester 方程转换。提供了分层控制在 EMT 数值实现中的前沿方法。
- **林继灿 2023** — 多 VSG 并联互阻尼一致性算法，分布式二次协调，Lyapunov 稳定性证明。提供了分布式一致性二次控制的理论分析。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

---
title: "构网型变流器 (Grid-Forming Inverter, GFM)"
type: model
tags: [grid-forming, gfm, droop, vsm, virtual-synchronous-machine, weak-grid, inertia, vsg, psm, grid-forming-converter]
created: "2026-04-30"
updated: "2026-05-17"
---

# 构网型变流器 (Grid-Forming Inverter, GFM)

## 定义

构网型变流器（Grid-Forming Inverter, GFM）是新型电力系统中实现 100% 电力电子化电网的关键装备。与传统跟网型变流器（Grid-Following, GFL）依赖锁相环（PLL）追踪电网相位不同，GFM 变流器通过模拟同步发电机的转子运动方程和励磁系统特性，自主生成电压相位和频率，因而不需要外部电网作为相位参考。GFM 的核心功能是建立和维持交流电压系统，为弱电网、孤岛电网和新能源高渗透率电网提供惯量支撑和频率阻尼。在 EMT 仿真中，GFM 变流器既是待研究的物理对象（新能源场站储能接口、换流器控制策略），又是构建无源网络时域模型的核心元件。

## EMT 中的角色

在 EMT 仿真中，构网型变流器承担以下角色：

1. **新能源场站接口模型**：光伏/风电场站经储能电池配合 GFM 变流器接入电网时，GFM 作为黑启动电源建立交流电压，需要建立从直流侧 PV/储能功率到交流侧电压频率的完整动态模型
2. **虚拟电压源**：GFM 在 EMT 中表现为受控电压源，其输出电压幅值和频率由内部状态变量（下垂参考、积分器状态）决定，而非由外部网络强加
3. **惯量响应元件**：虚拟同步机（VSM）控制使得 GFM 能够像同步发电机一样响应系统频率变化，提供等效转动惯量 $J$ 和阻尼系数 $D$
4. **初始化挑战对象**：MTDC 系统含 V/f 控制 GVSC 时，传统潮流初始化因辅助电压源与控制器积分器初值不匹配，会导致启动暂态延长；CISS 和 DI 方法是解决这一问题的重要接口技术
5. **PQ 运行域约束**：GFM 的 PWM 饱和约束和额定电流约束决定了 PCC 点可实现的 P/Q 工作域，该边界与滤波器拓扑和直流母线电压强相关

## EMT 建模方法

GFM 变流器的 EMT 建模方法根据控制策略和等效电路结构分为以下六类：

### 方法 1：下垂控制（Droop Control）

下垂控制是最基础的 GFM 控制策略，通过有功-频率（P-f）和无功-电压（Q-V）下垂关系实现功率分配和频率电压支撑。

**P-f 下垂方程**：
$$
f = f_0 - k_p (P - P_0) \tag{1}
$$

**Q-V 下垂方程**：
$$
V = V_0 - k_q (Q - Q_0) \tag{2}
$$

其中 $k_p$（Hz/MW）和 $k_q$（pu/kV）为下垂系数，$f_0$、$V_0$ 为额定频率和电压，$P_0$、$Q_0$ 为额定有功和无功。

**EMT 实现要点**：下垂控制的 EMT 模型将频率参考转换为相角积分 $\theta = \int \omega dt$，再由 PWM 调制生成逆变器输出电压。该方法计算简单，适合微电网和多机并联场景，但无法提供惯量响应。

### 方法 2：虚拟同步机（Virtual Synchronous Machine, VSM）

VSM 在下垂控制基础上引入同步发电机的转子运动方程和励磁系统，使 GFM 具备惯性响应能力。

**转子运动方程**（式 (3)）：
$$
J \frac{d\omega}{dt} = P_{ref} - P - D(\omega - \omega_0) \tag{3}
$$

**相角方程**（式 (4)）：
$$
frac{d\theta}{dt} = \omega \tag{4}
$$

**励磁系统方程**（式 (5)）：
$$
\tau_f \frac{dE}{dt} = V_{ref} + k_q(Q_{ref} - Q) - E \tag{5}
$$

其中 $J$ 为虚拟转动惯量（H·s），$D$ 为阻尼系数（pu/rad/s），$\omega_0$ 为额定角速度（pu），$\tau_f$ 为励磁时间常数，$E$ 为内电势幅值。

**EMT 实现要点**：VSM 在 EMT 中的状态空间模型为 $mathbf{x} = [theta, omega, E]^T$，包含三个状态变量。数值积分通常采用隐式方法（如梯形法或 Gear 法）以保证数值稳定性。惯量 $J$ 的选取影响 VSM 对频率扰动的响应速度：$J$ 越大，频率变化率 $d\omega/dt$ 越小，系统越稳定但响应越慢。

### 方法 3：功率同步环（Power Synchronization Loop, PSL）

PSL 直接将功率偏差映射为频率/相角变化，绕过 dq 坐标系下的电压环设计，适用于对功率控制精度要求高的场景。

**PSL 基本方程**：
$$
\frac{d\theta}{dt} = \omega_0 + k_{\omega}(P_{ref} - P) \tag{6}
$$

其中 $k_{\omega}$ 为功率-频率增益，$P_{ref}$ 为有功功率参考。

**传递函数框架**：PSL 的核心是把"有功—频率/相角—线路电流—有功"的闭环路径显式化，通过传递函数分析得到控制参数的稳定边界。该方法是 Misyris (2021) 讨论 RMS 建模充分条件的对象，其结论指出：当 PSL 外环增益满足时间尺度分离充分条件且 SCR ∈ [1, 3] 时，RMS 模型与 EMT 的相对误差小于 3%。

### 方法 4：匹配控制（Matching Control）

匹配控制基于非线性控制理论的反馈线性化方法，将 GFM 的非线性动态精确线性化，实现精确的电压/频率跟踪。

**匹配条件**：通过精确输入-输出反馈线性化，使得闭环系统动态与参考模型一致。

**特点**：理论严谨，但参数整定复杂，在 EMT 仿真中通常需要对控制器进行离散化处理。

### 方法 5：虚拟振荡器控制（Virtual Oscillator Control, VOC）

VOC 基于 Hopf 分岔理论，利用非线性振荡器（如 Van der Pol 振荡器）的自激振荡特性实现 GFM 功能，无需 PLL 即可实现多机自同步。

**Van der Pol 振荡器方程**：
$$
\frac{d^2 v}{dt^2} - \mu (1 - v^2) \frac{dv}{dt} + v = 0 \tag{7}
$$

其中 $\mu$ 为非线性阻尼系数，控制振荡器的幅度和衰减特性。

**EMT 实现要点**：VOC 在 EMT 中的优势在于多机并联时自然实现功率均分，无需通信链路。但非线性振荡器的参数设计（$\mu$、振荡频率）需要针对具体应用场景优化。

### 方法 6：CISS 接口初始化方法

CISS（Current Injection State Initialization）不是 GFM 控制策略本身，而是 GFM 变流器接入 MTDC 系统时的初始化接口方法。当 GFM 变流器作为黑盒模型（无法访问内部 PI 参数）接入大型交直流混合 EMT 系统时，CISS 利用潮流相量和已知换流器参数解析计算外环积分器初值，使 EMT 仿真从稳态开始而非从零初始暂态开始。

**CISS 原理**：
1. 输入：潮流计算的 PCC 电压相量 $V_{PCC}$、交流电流相量 $I_{ac}$、直流电压 $V_{dc}$、变压器阻抗 $Z_t$、桥臂电抗 $Z_a$、PI 增益 $(k_p, k_i)$、电压设定值 $V^*$
2. 从 PCC 向换流器内部反推参考电压：$V_{ref} = V_{PCC} - I_{ac}(Z_t + Z_a)$
3. 由 d 轴电压环关系反解 PI 积分状态 $h = f(V_{ref}, V_{dc}, k_p, k_i)$
4. 用解析得到的 $[h, V_{ref}]$ 作为 EMT 初始状态，启动仿真

**DI（Direct Initialization）接口方法**：面向无法读取内部参数的黑盒 GFM，在 PCC 插入接口辅助源（Interface Auxiliary Source, IAS）将 GVSC 与交流孤岛临时解耦，两个子系统分别独立时域收敛后再断开 IAS 并联。CISS 使初始化时间缩短为传统潮流初始化的 1/6.9（Allabadi 2024）。

## 形式化表达

### GFM 基本方程组

**三相 dq 坐标系下的输出功率**（式 (8)-(9)）：
$$
P = \frac{3}{2}(v_d i_d + v_q i_q) \tag{8}
$$
$$
Q = \frac{3}{2}(v_q i_d - v_d i_q) \tag{9}
$$

**dq 旋转坐标系与abc坐标系的变换矩阵**：
$$
mathbf{T}_{dq0}^{abc} = \frac{2}{3} \begin{bmatrix} \cos\theta & \cos(\theta - 2\pi/3) & \cos(\theta + 2\pi/3) \\ -\sin\theta & -\sin(\theta - 2\pi/3) & -\sin(\theta + 2\pi/3) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix} \tag{10}
$$

**dq 坐标系下的电压电流关系**（滤波器方程）：
$$
v_d = L \frac{di_d}{dt} + Ri_d - \omega L i_q + e_d \tag{11}
$$
$$
v_q = L \frac{di_q}{dt} + Ri_q + \omega L i_d + e_q \tag{12}
$$

其中 $e_{dq}$ 为 GFM 内电势在 dq 轴的分量，$R$、$L$ 为滤波器电阻和电感，$\omega$ 为角速度。

### 状态空间表示

GFM 变流器的状态空间模型可表示为：
$$
\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u} \tag{13}
$$

其中状态向量 $\mathbf{x} = [\theta, \omega, E, i_d, i_q]^T$（VSM 模式），输入向量 $\mathbf{u} = [P_{ref}, Q_{ref}, V_{dc}]^T$。

### PQ 运行域约束

GFM 变流器的 PQ 运行域由两类硬约束决定（Nurunnabi 2025）：

**额定电流约束**（式 (14)）：
$$
\sqrt{i_d^2 + i_q^2} \leq I_{rated} \tag{14}
$$

**PWM 饱和约束**（式 (15)）：
$$
\sqrt{e_d^2 + e_q^2} \leq \frac{V_{dc}}{\sqrt{3}} \cdot m_{max} \tag{15}
$$

其中 $m_{max}$ 为最大调制比（通常 $m_{max} \leq 1$），$V_{dc}$ 为直流母线电压。

## 关键技术挑战

### 挑战 1：惯量与响应速度的矛盾

虚拟惯量 $J$ 的选取存在矛盾：$J$ 越大，频率稳定性越好，但 VSM 对功率指令的动态响应越慢。在新能源高渗透率系统中，需要在惯量支撑和快速功率调节之间取得平衡。

### 挑战 2：故障电流限幅非线性

GFM 变流器在故障期间内电势与 PCC 电压之间的差值增大，导致电流急剧上升。PWM 限幅和电流环饱和使得 GFM 在故障期间表现出强非线性，线性小信号模型在此时失效，需要在 EMT 中使用详细开关模型验证。

### 挑战 3：多机并联同步稳定性

多台 GFM 并联时，下垂控制或 VSM 之间的交互可能导致低频振荡（1-5 Hz）。振荡的机制是各 GFM 变流器之间的功率同步环交互与网络阻抗的耦合，其稳定性分析与同步发电机惯量支撑系统类似，但控制带宽更大。

### 挑战 4：GFM/GFL 混联系统交互

在同一 PCC 下 GFM 和 GFL 并联运行时，GFL 的 PLL 与 GFM 的自主相位生成之间存在交互。GFM 提供的电压支撑可能影响 GFL 的锁相环同步过程，导致系统稳定性改变。

### 挑战 5：初始化与稳态建立

GFM 变流器接入大型 EMT 系统时，控制器初值与网络潮流工况不匹配会导致长时间的启动暂态（可达数百毫秒到数秒），CISS 和 DI 方法是解决此问题的专用接口技术。

## 量化性能边界

| 性能指标 | 数值 | 来源 |
|---------|------|------|
| 黑启动完成时间 | 18 s 内完成 7 步黑启动 | Nguyen 2021 |
| 稳态电压误差 | < 1% | Nguyen 2021 |
| 负荷切换后电压恢复时间 | < 0.2 s | Nguyen 2021 |
| 多 GFM 协同功角偏差 | 降低约 15-20° | Wu 2025（据方法推断） |
| RMS 建模相对误差（SCR ∈ [1,3]，满足充分条件） | < 3% | Misyris 2021 |
| RMS 建模失效时错误率（违背充分条件） | 100% | Misyris 2021 |
| 计及电压下垂后相位裕度提升 | 约 14-16° | Misyris 2021 |
| 短路比 CSCR 临界值 | ≈ 3.7 | Jiang 2025 |
| 振荡频率（对应 CSCR≈3.7） | 1.15 Hz | Jiang 2025 |
| CISS/DI 初始化加速比 | 6.9 倍 | Allabadi 2024 |
| VSG 实时仿真 FPGA 步长 | 1 μs（FPGA）+ 100 μs（CPU） | Wu 2023 |
| PWM 饱和约束与电流约束交集 PQ 运行域 | 动态边界（与 PCC 电压、$V_{dc}$、滤波器拓扑相关） | Nurunnabi 2025 |

**数据缺口声明**：GFM 变流器的详细开关模型与平均值模型在故障穿越、限幅非线性、多机并联等方面缺乏统一的量化对比基准。不同 GFM 控制策略（下垂、VSM、匹配控制、VOC）在同一测试条件下的性能比较数据不足。

## 适用边界与选择指南

| 应用场景 | 推荐 GFM 方法 | 原因 |
|---------|-------------|------|
| 微电网多机并联 | 下垂控制 | 计算简单，自然实现功率均分，无需通信 |
| 高惯量需求（弱网/孤岛） | VSM | 提供惯量响应，$J$ 和 $D$ 可调 |
| 精确功率跟踪 | PSL | 功率同步环直接映射，响应快 |
| 理论严谨性要求高 | 匹配控制 | 反馈线性化精确控制 |
| 孤岛微电网自同步 | VOC | 多机无需通信自然同步 |
| MTDC 大系统初始化 | CISS（参数可读）/ DI（黑盒） | CISS 6.9× 加速，DI 适合供应商模型 |
| PQ 运行域计算 | Nurunnabi 2025 框架 | 动态边界同时考虑 PWM 饱和和电流约束 |

### GFM vs GFL 选型决策

| 判断维度 | GFM | GFL |
|---------|-----|-----|
| 电网强度 | 弱网（SCR < 3）/ 孤岛 | 强网（SCR > 3） |
| 惯量需求 | 需要惯量支撑 | 不需要 |
| 黑启动需求 | 支持（可作 BS 单元） | 不支持 |
| 控制复杂度 | 较高（需 VSM/下垂设计） | 较低（PLL 追踪） |
| 故障电流特性 | 有限流（受 PWM 饱和约束） | 受 IGBT 定额限制 |
| 多机并联 | 自然同步（下垂/VSM） | 需要通信协调 |
| 适用接口 | V/f 控制端口 | PQ 控制端口 |

## 相关方法

- [[state-space-method|状态空间法]] — GFM 状态空间建模与数值求解
- [[droop-control-model|下垂控制]] — GFM 下垂控制策略
- [[average-value-model|平均值模型]] — GFM 平均值简化模型
- [[numerical-integration|数值积分]] — VSM 惯量响应仿真中的数值积分方法
- [[multirate-method|多速率方法]] — 多 GFM 并行仿真
- 功率同步环（Power Synchronization Loop, PSL）— 直接将功率偏差映射为频率/相角变化的控制策略，适用于精确功率跟踪场景

## 相关模型

- [[gfl-inverter-model|跟网型变流器]] — GFL 与 GFM 对比分析
- [[vsc-model|VSC 模型]] — 换流器主电路通用结构
- [[pll-model|锁相环]] — 对比 GFM 无 PLL 的自主相位生成
- [[bess-model|电池储能]] — 储能系统作为 GFM 直流侧能量源
- [[mtdc-model|MTDC 模型]] — 多端直流系统中 GFM 初始化接口

## 相关主题

- [[vsc-hvdc]] — 柔性直流输电中的 GFM 应用
- [[droop-control-model|下垂控制]] — 功率均分与频率调节策略
- [[real-time-simulation]] — GFM 实时仿真（CPU-FPGA 异构平台）
- [[wind-farm-modeling]] — 风电场 GFM 建模
- [[network-equivalent]] — 含高渗透率 GFM 的电网等值方法

## 来源论文

- Nguyen 等 2021 — PV-电池混合电站构网型逆变器黑启动控制与 PSCAD 仿真
- Nurunnabi 等 2025 — 构网型逆变器 PQ 能力边界与 EVR/CPID 控制策略
- Misyris 等 2021 — 构网型变流器 RMS 建模充分条件（PSL 和 VSG）
- Allabadi 等 2024 — MTDC 系统中 GVSC 的 CISS 和 DI 初始化方法
- Jiang 等 2025 — 电压源型 VSG 的临界短路比（CSCR）分析
- Wu 等 2023 — CPU-FPGA 异构平台上 VSG 并网逆变器实时仿真
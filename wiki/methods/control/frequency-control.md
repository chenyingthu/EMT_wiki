---
title: "频率控制 (Frequency Control)"
type: method
tags: [frequency-control, primary-frequency-control, secondary-frequency-control, grid-forming, droop-control, inertia-control, virtual-synchronous-generator, vsg, emt-simulation, power-electronics-control]
created: "2026-05-05"
updated: "2026-05-15"
---

# 频率控制 (Frequency Control)

## 定义

频率控制是维持电力系统频率在扰动后可接受范围内，并在不同时间尺度上恢复频率偏差的控制方法总称。在电磁暂态（EMT）仿真中，频率控制涵盖两个层面的含义：对于同步机主导的传统电网，频率控制以调速器为核心的机械功率调节；对于逆变器主导系统（IBR高渗透率电网），频率控制以构网型（Grid-Forming, GFM）逆变器的有功-频率下垂、虚拟惯量补偿和虚拟同步机（Virtual Synchronous Generator, VSG）控制为核心。

从 EMT 建模视角，频率控制是连接控制层与网络方程的关键接口：它将系统频率偏差 $\Delta\omega$ 映射为有功功率指令 $\Delta P$，再通过逆变器或同步机的电磁功率通道注入网络，参与节点方程求解。

## EMT 中的角色

在 EMT 仿真中，频率控制承担以下任务：

1. **扰动响应分析**：分析负荷突变、故障切除、发电机脱网和孤岛切换后的频率动态，评估最大频率偏差（Frequency Deviation, FD）和频率变化率（Rate of Change of Frequency, RoCoF）；
2. **惯量支撑评估**：评估同步机惯性、虚拟惯量和储能协同支撑对 RoCoF 的抑制效果，分析惯量不足时的频率稳定性；
3. **协调控制研究**：研究一次控制（快速下垂）、二次控制（PI恢复）和三次控制（经济调度）之间的耦合与时序配合；
4. **并网逆变器稳定性**：评估 PLL 跟网策略与构网策略在频率支撑中的差异，验证限流、饱和和同步逻辑对频率支撑的影响；
5. **黑启动与网络恢复**：在系统全域停电后的重建阶段，评估构网型逆变器作为黑启动电源建立电压和频率的能力。

## 核心机制

### 1. 同步机式频率控制

同步机的频率控制基于转子运动方程和调速器控制。转子运动方程描述机械功率与电磁功率不平衡时的频率暂态过程：

$$J\frac{d\omega}{dt} = \frac{P_m - P_e}{\omega_0} - D(\omega - \omega_0)$$

其中 $J$ 为转子惯性常数，$P_m$ 为机械输入功率，$P_e$ 为电磁输出功率，$D$ 为阻尼系数，$\omega_0$ 为额定角频率。

调速器（Governor）根据频率偏差调节机械功率输入，实现一次调频：

$$P_m = P_{ref} + K_g(\omega_0 - \omega)$$

其中 $K_g$ 为调速器增益。一次调频为无通信的分布式控制，响应时间通常在 $0.1$–$1$ 秒量级。

### 2. 逆变器式频率控制

逆变器式频率控制旨在模拟或替代同步机的频率支撑功能，按控制策略分为以下几类：

#### 2.1 有功-频率下垂控制（P-f Droop）

有功-频率下垂控制模拟同步机的调速器特性，将频率偏差映射为有功功率调整：

$$f = f_{set} + m_p(P_{ref} - P)$$

其中 $m_p$ 为有功-频率下垂系数（单位：Hz/p.u.），$f_{set}$ 为额定频率，$P_{ref}$ 为有功参考，$P$ 为实测有功。该控制通过测量 PCC 点有功功率与参考的偏差，自主调节逆变器输出频率，实现无通信的频率支撑。

下垂控制的 EMT 实现需要实时计算 $f$ 并将其转换为相角积分 $\theta = \int 2\pi f dt$，再注入 PWM 调制环节。在 EMT 仿真中，下垂控制与内环电流/电压控制形成嵌套双环结构：

- **外环**：有功-频率下垂，产生频率参考 $f$
- **内环**：电压环（产生 $E$）和电流环（产生调制电压），经 PWM 生成开关指令

典型参数：$m_p$ 通常设为 $1\%$–$4\%$，即额定频率偏差 $0.01$–$0.04$ p.u. 对应额定有功变化。

#### 2.2 虚拟同步机控制（VSG）

虚拟同步机控制通过在逆变器控制中嵌入同步机转子运动方程，使逆变器表现类同步机特性。核心方程：

$$J\frac{d\omega}{dt} = \frac{P_m - P_e}{\omega_0} - D(\omega - \omega_0)$$

$$P_m = P_{ref} + k_{\omega}(\omega_0 - \omega)$$

其中 $J$ 为虚拟惯量（可调），$D$ 为虚拟阻尼，$k_\omega$ 为一次调频系数。与同步机调速器不同的是，$J$ 和 $D$ 是软件定义的参数，不受物理机械限制，因此可以在很宽的范围内调节（$J$ 可从接近零调到数十秒等效惯性时间常数）。

无功-电压控制模拟同步机励磁特性：

$$E = \frac{1}{K_q s}[Q_{ref} - Q + D_q(U_{ref} - U)]$$

其中 $K_q$ 为积分系数，$D_q$ 为无功-电压下垂系数，$E$ 为内电势幅值参考。

并联 VSC-ESS 的频率响应传递函数为二阶系统：

$$\frac{\Delta\omega_i(s)}{\Delta\omega_{bus}(s)} = \frac{K_i}{J_i\omega_0 s^2 + (D_i\omega_0 + k_{\omega i})s + K_i}$$

其中 $K_i = \frac{3U_{ci}U_g}{2X_i}$ 为同步功率系数。多台并联时，总负荷扰动与母线频率的关系为：

$$\frac{\Delta P_L(s)}{\Delta\omega_{bus}(s)} = -\sum_{i=1}^{n}\frac{K_i(J_i\omega_0 s + D_i\omega_0 + k_{\omega i})}{J_i\omega_0 s^2 + (D_i\omega_0 + k_{\omega i})s + K_i}$$

#### 2.3 自适应惯量控制

传统 VSG 中 $J$ 为固定参数，在频率扰动初期提供惯性支撑，但可能在恢复阶段拖慢响应速度。自适应惯量控制使 $J$ 随频率偏差和 RoCoF 动态调整：

$$J(t) = J_{min} + \alpha(\Delta\omega, RoCoF)\cdot (J_{max} - J_{min})$$

在扰动初期（$|\Delta\omega|$ 大或 $|RoCoF|$ 大），$J$ 自动增大以抑制 RoCoF；在恢复阶段，$J$ 减小以加快频率恢复。自适应系数 $\alpha$ 的设计需兼顾稳定性与响应速度。

暂态电磁功率补偿用于抑制并联 VSC 之间的有功功率振荡和超调。不同并联单元因虚拟惯量、阻尼和下垂系数不同，导致角加速度差异，进而放大功率-频率振荡。补偿策略在频率响应暂态期间修正电磁功率通道，抵消导致超调和振荡的暂态功率分量。

### 3. 构网型控制与跟网型控制的频率特性对比

| 特性 | 构网型（GFM） | 跟网型（GFL） |
|------|--------------|--------------|
| 频率建立 | 自主建立频率/相角参考，无需外部锁相 | 依赖 PLL 跟踪电网相角 |
| 频率支撑 | 可主动注入惯量，支撑系统频率 | 跟随电网频率，被动响应 |
| 黑启动能力 | 可作为黑启动电源独立建压建频 | 需外部电网支撑，无法独立启动 |
| 故障响应 | 内电势支撑，短路容量有限 | 受 PLL 带宽限制 |
| 适用场景 | 弱网/孤岛/微网 | 并网型新能源场站 |

### 4. 构网型逆变器的 PQ 能力边界

GFM 逆变器的实际有功-无功运行域由以下约束共同决定：

**额定电流约束**：

$$|\vec{I}_{PCC}| \le I_{rated}$$

**PWM 饱和约束**（取决于调制策略和直流电压）：

$$|\vec{E}_{inv}| \le E_{max}$$

其中 SVPWM 的 $E_{max} \approx 1.53$ p.u.，SPWM 的 $E_{max} \approx 1.33$ p.u.（据 Nurunnabi 2025）。

PCC 点有功和无功传输近似方程：

$$P_{PCC} \approx V_{PCC}\frac{E_{inv}}{X_F}\delta_{inv}, \quad Q_{PCC} \approx V_{PCC}\frac{E_{inv} - V_{PCC}}{X_F}$$

GFM 逆变器的 PQ 能力边界不是固定能力曲线，而是由 PCC 电压、直流母线电压、滤波器压降和调制电压裕度共同决定的动态可行域。

## EMT 建模方法

### 等效电路模型

同步机频率控制的 EMT 等效电路通常保留转子运动方程作为状态方程，与网络方程联立求解。同步机的电磁暂态过程通过 $d$/$q$ 轴电压方程描述：

$$u_d = R_s i_d + L_d \frac{di_d}{dt} - \omega_e L_q i_q$$
$$u_q = R_s i_q + L_q \frac{di_q}{dt} + \omega_e L_d i_d + \omega_e \psi_f$$

与频率控制相关的状态变量包括转子角 $\delta$、角频率 $\omega$ 和机械功率 $P_m$。

逆变器式频率控制的 EMT 等效电路包含：
- **LC/ LCL 滤波器**：连接逆变器输出与 PCC
- **内环电流/电压控制**：PI 控制，产生调制电压 $v^*$
- **PWM 调制**：将调制电压转化为开关指令
- **外环下垂或 VSG 控制**：产生频率/电压参考

### 初始化方法

大规模交直流混合系统 EMT 仿真中，构网型 VSC 的初始化质量直接影响启动暂态时长。传统潮流初始化依赖辅助电压源强制节点电压，导致外环 PI 积分器初值错误，引发长时间振荡。

**控制积分器初值求解法（CISS）**：基于潮流相量和已知控制参数，解析计算外环积分器初值：

$$h = \frac{1}{K_i}\left\{\frac{2}{V_{dc}}\left[\vec{V}_{PCC}^{LF} - \vec{I}_{ac}(\vec{Z}_{tr} + j\frac{X_{Larm}}{2})\right] - |V_{ac}^{set}|\right\}$$

该方法可将系统初始化时间缩短 $6.9$ 倍（据 Allabadi 2024，基于 CIGRE BM4 基准）。

**解耦接口法（DI）**：在并网点插入接口辅助源，将孤岛电网子系统与 GVSC 电气解耦，两个子系统分别独立初始化至稳态后再重耦合。该方法无需访问内部控制参数，适用于黑盒供应商模型。

## 形式化表达

### 同步机频率控制核心方程

| 方程 | 含义 | 参数 |
|------|------|------|
| $J\frac{d\omega}{dt} = \frac{P_m - P_e}{\omega_0} - D(\omega - \omega_0)$ | 转子运动方程 | $J$: 惯性常数，$D$: 阻尼 |
| $P_m = P_{ref} + K_g(\omega_0 - \omega)$ | 调速器一次调频 | $K_g$: 调速器增益 |
| $\Delta P = -K_f \Delta\omega$ | 简化一次频率支撑 | $K_f = 1/m_p$ |

### 逆变器式频率控制核心方程

| 方程 | 含义 | 参数 |
|------|------|------|
| $f = f_{set} + m_p(P_{ref} - P)$ | P-f 下垂控制 | $m_p$: 下垂系数 |
| $J\frac{d\omega}{dt} = \frac{P_m - P_e}{\omega_0} - D(\omega - \omega_0)$ | VSG 转子方程 | $J$: 虚拟惯量 |
| $E = \frac{1}{K_q s}[Q_{ref} - Q + D_q(U_{ref} - U)]$ | 无功-电压控制 | $K_q$: 积分系数 |
| $\frac{\Delta\omega_i(s)}{\Delta\omega_{bus}(s)} = \frac{K_i}{J_i\omega_0 s^2 + (D_i\omega_0 + k_{\omega i})s + K_i}$ | 并联 VSC 频率响应 | $K_i$: 同步功率系数 |
| $f_g = f_{rated} - m_p(P_{ac} - P_{ref})$ | GFM 一次下垂（ Nguyen 2021） | — |
| $\Delta f_g = K_{p,f}(f_{ref} - f_g) + K_{i,f}\int(f_{ref} - f_g)dt$ | GFM 二次 PI 补偿（ Nguyen 2021） | — |
| $P_{PCC} \approx V_{PCC}\frac{E_{inv}}{X_F}\delta_{inv}$ | PCC 有功传输近似（Nurunnabi 2025） | $X_F$: 滤波器电抗 |
| $\|I_{PCC}\| \le I_{rated}$ 且 $\|E_{inv}\| \le E_{max}$ | GFM PQ 双重约束（Nurunnabi 2025） | — |

## 关键技术挑战

### 挑战 1：惯量估计与测量

同步机系统的惯量可直接从机组参数获得，但逆变器主导系统的等效惯量 $J$ 是软件定义的参数，不同逆变器的等效惯量可能因控制策略、DC/DC 变换器和储能 SOC 状态而异。在 EMT 仿真中如何准确建模多逆变器的聚合等效惯量，是分析 RoCoF 时的核心挑战。

### 挑战 2：并联逆变器之间的耦合振荡

多台并联 VSC 因虚拟惯量、阻尼、调频系数和线路同步功率系数不同，会导致角加速度差异。该差异通过公共母线耦合，诱发有功功率振荡和超调。单纯增大阻尼可能牺牲一次调频性能，需要引入暂态电磁功率补偿与自适应惯量联合抑制。

### 挑战 3：构网型控制的参数整定

GFM 逆变器的虚拟惯量 $J$、阻尼 $D$ 和下垂系数 $m_p$ 相互耦合，整定时需在惯量支撑能力、响应速度和稳定性之间取得平衡。参数整定缺乏统一准则，往往依赖经验或时域扫描。

### 挑战 4：EMT 与 RMS 模型的适用边界

低惯量电网中，控制动态与线路电磁动态的时间尺度分离可能不成立，RMS/相量模型会误判稳定性。GFM 外环控制增益需满足传递函数分析推导的充分条件（相角裕度 PM≥45°，幅值裕度 GM≥6dB）才能保证 RMS 近似有效（据 George & Misyris 2021）。

### 挑战 5：黑启动场景下的直流侧协调

在黑启动场景中，构网型逆变器作为独立电压源建压建频时，光伏阵列和储能之间的 DC/DC 协调控制、直流母线电压稳定和交流负荷阶跃暂态之间存在强耦合。如何设计直流侧控制器以支撑多步网络充电过程，是黑启动 EMT 仿真的关键。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| P-f 下垂系数典型范围 | $1\%$–$4\%$（Hz/p.u.） | 行业惯例 |
| Q-V 下垂系数典型范围 | $3\%$–$6\%$（p.u./p.u.） | 行业惯例 |
| SVPWM 最大调制电压 | $1.53$ p.u.（vs SPWM $1.33$ p.u.） | Nurunnabi 2025 |
| EVR 策略动态负载电压偏差 | $< 2.9\%$ | Nurunnabi 2025 |
| EVR 策略动态负载频率偏差 | $< 0.37\%$ | Nurunnabi 2025 |
| CISS 初始化加速比 | $6.9\times$ vs 传统潮流初始化 | Allabadi 2024 |
| RMS vs EMT 模型误差（满足充分条件时） | $< 3\%$ | George & Misyris 2021 |
| 黑启动恢复时间（IEEE 9-bus 算例） | $< 0.2$ 秒/次负荷投切 | Nguyen 2021 |
| 稳态电压精度（vs 数值优化解） | 误差 $< 1\%$ | Nguyen 2021 |

## 适用边界与选择指南

| 应用场景 | 推荐控制方法 | 说明 |
|---------|------------|------|
| 强同步机主导电网 | 同步机调速器 + 一次/二次频率控制 | 惯量充足，关注故障后频率恢复 |
| IBR 高渗透率弱网 | GFM 下垂 + VSG 惯量控制 | 需要主动频率支撑，抑制 RoCoF |
| 并联储能系统 | 自适应惯量 + 暂态功率补偿 | 协调多台并联 VSC 的频率响应 |
| 孤岛/微网黑启动 | GFM V/f 控制 + 二次 PI 恢复 | 构网逆变器独立建压建频 |
| 大规模 EMT 参数扫描 | RMS + EMT 混合仿真 | 满足时间尺度分离条件时用 RMS 加速 |
| 黑盒供应商模型初始化 | 解耦接口法（DI） | 无需访问内部参数 |
| 低惯量系统稳定性评估 | GFM 小信号建模 + 传递函数分析 | 用于判断 RMS 模型的适用性 |

## 相关方法与模型

- [[droop-control]]：有功-频率下垂控制，是最基础的逆变器式频率控制方法
- [[inertia-control]]：惯量控制，通过虚拟惯量抑制 RoCoF
- [[adaptive-droop]]：自适应下垂，根据运行状态在线调整频率支撑系数
- [[virtual-synchronous-generator]]：虚拟同步机，嵌入同步机转子方程的逆变器控制
- [[hierarchical-control]]：分层控制，一次/二次/三次频率控制在层级架构中的组织
- [[grid-forming-control]]：构网型控制，逆变器自主建立电压和频率参考的控制策略
- [[pll-design]]：锁相环设计，跟网型逆变器的同步环节
- [[energy-storage-system]]：储能系统，为频率控制提供快速功率支撑
- [[power-electronics-control]]：电力电子控制，逆变器控制的一般性框架
- [[small-signal-analysis]]：小信号分析，用于频率控制参数稳定性分析
- [[emt-simulation]]：电磁暂态仿真，频率控制 EMT 建模与验证的平台

## 来源论文

- **Nurunnabi 等 2025** — Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis（IEEE Access 2025）：提出 GFM 逆变器 PQ 能力边界建模方法，含 P-f/Q-V 下垂控制方程和 PWM 饱和约束，EVR 策略将电压偏差限制在 $2.9\%$ 以内、频率偏差 $0.37\%$ 以内
- **Hu 等 2025** — Transient Electromagnetic Power Compensation-Based Adaptive Inertia Control Strategy for Parallel Energy Storage VSC（IET GTD 2025）：提出并联 VSC-ESS 自适应惯量控制，虚拟惯量随频率偏差和 RoCoF 动态调整，含 VSG 小信号传递函数
- **George & Misyris 2021** — Grid-forming converters: Sufficient conditions for RMS modeling（Electric Power Systems Research）：推导 GFM 外环控制时间尺度分离的充分条件，相角裕度 PM≥45°、幅值裕度 GM≥6dB，RMS 与 EMT 误差 $< 3\%$
- **Allabadi 2024** — Initializing EMT models of grid forming VSCs in MTDC systems（Electric Power Systems Research）：提出 CISS 和 DI 两种 GFM EMT 初始化方法，初始化加速比 $6.9\times$，适用于 CIGRE BM4 基准
- **Nguyen 等 2021** — Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start（IEEE PES GM）：提出 PV-电池混合电站 GFM 黑启动控制，一次下垂+二次 PI 恢复，IEEE 9-bus 算例 18 秒内完成 7 步黑启动
---
title: "H∞ 鲁棒控制 (H-Infinity Control)"
type: method
tags: [robust-control, h-infinity, optimization, controller-design, mimo, sensitivity, mixed-sensitivity, mu-synthesis]
created: "2026-05-02"
updated: "2026-05-18"
---

# H∞ 鲁棒控制 (H-Infinity Control)

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 340" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1: Generalized Plant P(s) input -->
  <rect x="20" y="30" width="140" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="52" text-anchor="middle" font-size="13" font-family="Arial">扰动 w</text>
  <text x="90" y="68" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">外部输入</text>

  <rect x="20" y="130" width="140" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="152" text-anchor="middle" font-size="13" font-family="Arial">不确定性 Δ</text>
  <text x="90" y="168" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">模型不确定性</text>

  <rect x="20" y="230" width="140" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="252" text-anchor="middle" font-size="13" font-family="Arial">控制 u</text>
  <text x="90" y="268" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">控制输入</text>

  <!-- Layer 2: Generalized Plant P(s) -->
  <rect x="220" y="90" width="160" height="120" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="300" y="130" text-anchor="middle" font-size="14" font-family="Arial" font-weight="bold">广义对象</text>
  <text x="300" y="148" text-anchor="middle" font-size="12" font-family="Arial">P(s)</text>
  <text x="300" y="168" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">加权性能 z</text>
  <text x="300" y="184" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">测量输出 y</text>

  <!-- Layer 3: Controller K(s) -->
  <rect x="440" y="120" width="130" height="60" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="505" y="148" text-anchor="middle" font-size="14" font-family="Arial" font-weight="bold">控制器</text>
  <text x="505" y="166" text-anchor="middle" font-size="12" font-family="Arial">K(s)</text>

  <!-- Layer 4: Closed-loop transfer Tzw -->
  <rect x="640" y="110" width="160" height="80" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="720" y="138" text-anchor="middle" font-size="14" font-family="Arial" font-weight="bold">闭环传递</text>
  <text x="720" y="158" text-anchor="middle" font-size="12" font-family="Arial">T</text>
  <text x="732" y="158" text-anchor="middle" font-size="9" font-family="Arial" font-style="italic">zw</text>
  <text x="720" y="174" text-anchor="middle" font-size="11" font-family="Arial">(s)</text>

  <!-- Arrows -->
  <line x1="160" y1="55" x2="220" y2="130" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="160" y1="155" x2="220" y2="160" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="160" y1="255" x2="220" y2="190" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="380" y1="150" x2="440" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="505" y1="180" x2="640" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="570" y1="140" x2="640" y2="140" stroke="#333" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrow)"/>

  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>

  <!-- H∞ Norm box -->
  <rect x="700" y="230" width="120" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="760" y="252" text-anchor="middle" font-size="12" font-family="Arial">‖T</text>
  <text x="771" y="252" text-anchor="middle" font-size="9" font-family="Arial" font-style="italic">zw</text>
  <text x="778" y="252" text-anchor="middle" font-size="12" font-family="Arial">‖</text>
  <text x="760" y="270" text-anchor="middle" font-size="12" font-family="Arial">∞</text>
  <line x1="720" y1="190" x2="760" y2="230" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- Legend -->
  <rect x="20" y="290" width="14" height="14" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="40" y="302" font-size="11" font-family="Arial">外部输入/扰动</text>
  <rect x="140" y="290" width="14" height="14" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="160" y="302" font-size="11" font-family="Arial">广义对象 P(s)</text>
  <rect x="270" y="290" width="14" height="14" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="290" y="302" font-size="11" font-family="Arial">H∞ 控制器 K(s)</text>
  <rect x="400" y="290" width="14" height="14" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="420" y="302" font-size="11" font-family="Arial">闭环性能 / H∞ 范数</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · H∞ 鲁棒控制的标准框架：扰动 w → 广义对象 P(s) → 控制器 K(s) → 性能输出 Tzw(s) → H∞ 范数最小化</p>

## 定义与边界

H∞ 鲁棒控制是一类以最坏情形增益为性能指标的线性控制综合方法。它通过构造广义对象，把扰动、测量噪声、控制量、模型不确定性和性能输出放入同一闭环传递矩阵，并寻找控制器 $K(s)$ 使从外部输入到性能输出的 H∞ 范数满足给定界限。

对稳定传递矩阵 $G(s)$，H∞ 范数定义为：

$$\|G\|_\infty = \sup_{\omega} \bar{\sigma}(G(j\omega))$$

其中 $\bar{\sigma}$ 是最大奇异值。它表示频域中最坏方向的小信号增益上界，而不是时域所有非线性故障的保证。

本页讨论鲁棒控制框架本身。[[mixed-sensitivity-optimization]] 是 H∞ 控制中常见的 S/KS/T 加权设计问题；[[power-system-stabilizer]] 是同步机励磁通道中的具体阻尼控制器；[[small-signal-stability-analysis]] 是验证线性化闭环模态的常用分析方法。不要把 H∞ 综合结果直接写成大扰动暂态稳定保证。

## EMT 中的作用

在 EMT/hybrid simulation 场景中，H∞ 控制通常不是直接在开关级非线性模型上求解，而是基于某个运行点附近的线性化、阻抗模型、频率扫描识别模型或动态相量模型设计控制器。设计完成后，需要回到 EMT 时域验证控制器在限幅、采样、延时、非线性负荷、故障和保护动作下的表现。

典型用途包括：

- 为 VSC/MMC、FACTS、HVDC 或阻尼控制器设计多输入多输出补偿器；
- 在模型不确定性下约束扰动到电压、电流、功率或模态输出的最坏增益；
- 将 EMT 频率扫描得到的阻抗/导纳模型作为设计或验证对象；
- 在 EMT-TS 混合仿真中验证控制器对低频机电模态和局部电磁动态的共同影响。

## 基本数学形式

广义对象可写为：

$$\begin{bmatrix} z \\ y \end{bmatrix} = P(s) \begin{bmatrix} w \\ u \end{bmatrix}$$

其中 $w$ 是扰动、参考或不确定性输入，$u$ 是控制输入，$z$ 是加权性能输出，$y$ 是测量输出。控制器 $u = K(s) y$ 闭合后得到从 $w$ 到 $z$ 的闭环传递 $T_{zw}(s)$。H∞ 综合目标通常写成：

$$\min_K \|T_{zw}(s)\|_\infty$$

## 设计路线

1. 选择运行点和模型来源：解析线性化、EMT 频扫识别、动态相量或状态空间降阶。
2. 定义输入输出：扰动、测量、控制量、性能变量和不确定性通道。
3. 选择权重：把低频跟踪、中频阻尼、高频噪声、控制量和执行器限制转化为频率权重。
4. 构造广义对象 $P(s)$ 并检查可镇定、可检测、正则性和维度一致性。
5. 用 Riccati、LMI、$\gamma$ 迭代或固定结构优化求控制器。
6. 做阶次降低、离散化、采样延时和限幅处理。
7. 在频域、线性时域、EMT 时域和多工况扰动下验证。

## 方法变体

| 变体 | 机制 | 适用场景 | 主要风险 |
|------|------|----------|----------|
| 标准 H∞ 综合 | 最小化 $T_{zw}$ 的最大奇异值 | MIMO 线性控制器设计 | 控制器阶次高、权重解释困难 |
| 混合灵敏度 | 加权 $S, KS, T$ | 跟踪/扰动/噪声/控制量折中 | 权重选择可能导致保守或不可实现 |
| 固定结构 H∞ | 优化给定控制器结构 | 工程控制器参数整定 | 非凸，可能停在局部解 |
| $\mu$ 综合 | 处理结构化不确定性 | 参数和动态不确定性明确时 | D-K 迭代不保证全局最优 |
| 基于阻抗的鲁棒整形 | 针对端口阻抗/导纳设计 | IBR、HVDC、弱网振荡 | 依赖线性频域模型质量 |

## EMT 建模方法

在 EMT 仿真中嵌入 H∞ 控制器涉及以下核心建模环节：

### 阻抗/导纳接口法

将 EMT 频域扫描得到的端口阻抗 $Z(j\omega)$ 或导纳 $Y(j\omega)$ 作为 H∞ 设计对象。把换流器等效为多端口网络后，可直接用阻抗矩阵实施鲁棒控制综合。参见 [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]] 的 dq0 坐标系扫描方法（Chen Jiang 2025）。

### 伴随电路-特征值接口法

利用 EMT 程序的伴随电路节点导纳矩阵 $G$ 及其 LU 分解因子，直接提取系统线性化模型做特征值分析。如 [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-.md]] 所述，复用 EMT 内部离散化信息可将开关非线性系统的状态转移矩阵 $\Phi_T$ 映射为可做特征值分析的形式（Chindu & Kulkarni 2023）。

### MIMO 阻抗模型法

针对多端级联混合 HVDC 系统（送端双12脉动 LCC + 受端 MMC 阵列），分别建立 LCC 和 MMC 的多输入多输出端口阻抗矩阵，再通过灵敏度分析指导阻抗重塑。参见 [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy.md]]（Xu 等 2025）。

### 慢快系统降阶法（RMS+）

将 EMT 网络中的电磁暂态（快动态）与 PLL 动态（慢动态）在时间尺度上分离，用 Tikhonov-Fenichel 理论构造降阶混合代数-微分方程模型。保留影响 PLL 同步稳定性的网络动态成分，同时消除冗余高频状态。参见 rms+ 源页（Carreño 等 2026）。

### 非线性迭代求解法

在 EMT 每步积分求解非线性电路时，采用标准 NR → 双轴 NR → Katzenelson 算法三级递进框架，保证强非线性（铁芯饱和、MOA 等）条件下的数值鲁棒性。参见 a-robust-and-efficient-iterative-scheme 源页（Noda & Kikuma 2011）。

### 无源性强制法

在传输线/电缆的矢量拟合模型上，先用改进函数形式降低无源性违规概率，再用频率扫描定位剩余违规区，最后用线性约束最小二乘对特征导纳和传播矩阵元素施加小扰动以强制无源。参见 robust-passivity-enforcement-scheme 源页（De Silva 等 2010）。

## 形式化表达

### 标准 H∞ 综合

广义对象状态空间实现：

$$\begin{aligned} \dot{x} &= A x + B_1 w + B_2 u \\ z &= C_1 x + D_{11} w + D_{12} u \\ y &= C_2 x + D_{21} w + D_{22} u \end{aligned}$$

闭环传递函数：

$$T_{zw}(s) = C_1 (sI - A - B_2 K)(I + D_{22} K))^{-1} B_1 + D_{11}$$

H∞ 综合求解（Riccati 形式）：存在正定解 $X > 0$ 满足代数 Riccati 方程，当 $\gamma > \gamma_{\min}$ 时控制器可求得。

### 混合灵敏度加权

灵敏度函数 $S = (I + GK)^{-1}$，补灵敏度 $T = I - S$。混合灵敏度综合的加权优化目标：

$$\min_K \| W_p S \|_\infty \quad \text{s.t.} \quad \| W_u KS \|_\infty < 1, \ \| W_t T \|_\infty < 1$$

其中 $W_p$、$W_u$、$W_t$ 分别为性能权、控制量权、鲁棒性权。

### dq0 阻抗扫描

在三相 abc 坐标系注入多频正弦扰动后，通过 Park 变换转换到 dq0 坐标系：

$$\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix} = T_{abc \to dq0} \begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}, \quad T = \frac{2}{3} \begin{bmatrix} \cos\theta & \cos(\theta-2\pi/3) & \cos(\theta+2\pi/3) \\ -\sin\theta & -\sin(\theta-2\pi/3) & -\sin(\theta+2\pi/3) \\ 1/2 & 1/2 & 1/2 \end{bmatrix}$$

dq0 坐标系下的阻抗矩阵（消除频率耦合）：

$$Z_{dq0}(\omega) = V_{dq0}(\omega) \cdot I_{dq0}(\omega)^{-1}$$

### 特征值稳定性判据（Floquet 理论）

周期 $T$ 内状态转移矩阵 $\Phi_T = A_{N-1} A_{N-2} \cdots A_0$ 的特征值满足 $|\lambda_i| < 1$ 则小信号稳定。双线性变换映射到连续域：

$$\lambda_c = \frac{2}{h} \frac{\lambda_d - 1}{\lambda_d + 1}$$

其中 $\lambda_d$ 为离散特征值，$\lambda_c$ 为连续域特征值，$h$ 为 EMT 仿真步长。伪特征值（由数值离散引入）可通过判据 $\lambda_d = -1$ 识别并剔除。

## 关键技术挑战

### 1. 权重选择与解释

H∞ 综合中频率权重的选择依赖于设计者的工程经验，而权重参数直接影响控制器的性能和保守性。激进的权重可能导致控制量过大、执行器饱和或噪声放大；保守的权重则可能使系统动态过于迟缓。需要在 EMT 时域中反复调整权重参数并验证闭环表现，尚无系统性自动整定方法。

### 2. 控制器阶次与离散化

H∞ 综合得到的控制器通常阶次较高（与广义对象状态维度相同），而 EMT 仿真采用固定步长显式或隐式积分。控制器降阶（平衡截断、Hankel 范数优化）和离散化（Tustin 变换、双线性变换）会引入额外相位偏移和延时，在高频段影响尤为显著。

### 3. 模型不确定性描述

实际 EMT 模型中的参数不确定性和未建模动态难以用精确数学形式描述。$\mu$ 综合虽可处理结构化不确定性，但 D-K 迭代计算复杂度高且不保证全局最优；当不确定性描述过保守时，综合出的控制器同样保守。

### 4. 限幅与饱和处理

H∞ 设计的控制器假设线性系统，但 EMT 中的限幅器（电流限幅、直流电压限幅）和调制饱和在故障期间频繁动作。限幅器一旦饱和，控制器的线性假设失效，H∞ 范数最小化结论不再适用。需要额外在 EMT 时域中验证饱和恢复特性和保护动作下的系统表现。

### 5. 多速率接口与延时

H∞ 设计基于连续时间模型，而 EMT 中控制器与网络方程通过采样接口耦合。PLL 同步延时、控制计算延时（通常 0.5~1 个步长）和通信延时在鲁棒控制设计中难以精确建模，导致实际闭环性能与 H∞ 综合结果存在偏差。

## 量化性能边界

| 指标 | 典型数值 | 来源 |
|------|----------|------|
| 电压源型 VSG 临界短路比（CSCR） | ≈ 3.7 | Chen Jiang 2025（频率扫描工具） |
| 失稳振荡频率 | ≈ 1.05~1.15 Hz | Chen Jiang 2025 |
| 电流源型 VSG 稳定 SCR 上限 | ≥ 100（强交流系统） | Chen Jiang 2025 |
| 双线性变换特征值匹配误差 | 0%（精确匹配，不受步长影响） | Chindu & Kulkarni 2023 |
| EMT-伴随电路小信号模型状态变量 | 等于纯电感割集 + 纯电容回路数 | Chindu & Kulkarni 2023 |

## 适用边界与选择指南

H∞ 控制适合处理小信号、线性化和频域鲁棒性能问题。对于 EMT 中常见的大扰动问题，应注意：

- 故障穿越、限流、保护闭锁、调制饱和和模式切换会破坏线性假设；
- 控制器离散化、计算延时、PWM 或采样保持会改变高频相位；
- 频率扫描模型只在扰动幅值、频段和运行点附近有效；
- 权重越激进，越可能导致控制量过大、噪声放大或执行器饱和；
- 控制器阶次降低后必须重新验证鲁棒稳定性和 EMT 时域表现。

因此，本页允许写"用于设计、筛查或验证鲁棒阻尼/跟踪性能"，不应写"保证所有 EMT 故障稳定"。

| 场景 | 推荐方法 |
|------|----------|
| 并网变流器小信号振荡分析与阻尼设计 | 阻抗扫描 + H∞ 整形 |
| 多端 HVDC 系统振荡传播路径识别 | MIMO 阻抗 + 灵敏度分析 |
| PLL 同步稳定性与网络动态耦合 | RMS+ 慢快降阶 + 特征值分析 |
| 强非线性设备 EMT 求解鲁棒性 | 双轴 NR → Katzenelson 三级迭代 |
| 输电线路频变参数无源性保证 | 改进函数形式 + 频率扫描 + 约束最小二乘 |

## 相关方法 / 相关模型 / 相关主题

- [[mixed-sensitivity-optimization]]：详细说明 H∞ 设计中常用的 S/KS/T 加权问题。
- [[frequency-scan]] 和 [[impedance-measurement]]：可为控制设计和验证提供频域模型。
- [[small-signal-stability-analysis]]：验证线性化闭环模态和阻尼。
- [[power-system-stabilizer]]：是同步机励磁通道的具体阻尼控制页面，不等同于一般 H∞ 控制。
- [[transient-stability-analysis]]：用于检验控制器在大扰动场景中的实际效果。
- [[emt-simulation-verification]]：用于组织 EMT 时域验证证据。
- [[pll-model]] / [[srf-pll]]：PLL 同步控制是 H∞ 设计中常见的扰动通道和测量噪声源。
- [[vector-control]] / [[vsc-control]]：VSC 控制结构是 H∞ 控制器实现的具体载体。
- [[droop-control]] / [[adaptive-droop]]：下垂控制与 H∞ 鲁棒控制在多换流器协调中可互补使用。
- [[modal-analysis]]：用于解释 H∞ 控制器改变哪些模态、输入输出通道和参与因子。

## 来源论文

- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]：MMC-HVDC 高频振荡抑制策略，含阻抗扫描和阻尼设计方法。
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]]：基于 EMT 的动态频率扫描工具，支持 dq0 阻抗提取和 CSCR 预测。
- [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-.md]]：EMT 伴随电路自动化小信号稳定性分析，复用 TDS 内部矩阵构建 Floquet 特征值模型。
- [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy.md]]：多端级联混合 HVDC 的 MIMO 阻抗建模与振荡传播分析。
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]]：RMS+ 慢快系统降阶建模，保留电感 di/dt 效应对 PLL 稳定性的影响。
- [[robust-passivity-enforcement-scheme-for]]：传输线/电缆矢量拟合模型的无源性强制算法。
- [[a-robust-and-efficient-iterative-scheme-for-the-emt-simulations-of-nonlinear-cir-fix]]：EMT 非线性电路的双轴 NR 三级递进迭代求解框架。
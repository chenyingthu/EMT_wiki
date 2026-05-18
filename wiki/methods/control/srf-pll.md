---
title: "同步旋转坐标系锁相环方法 (SRF-PLL)"
type: method
tags: [srf-pll, pll, synchronization, grid-following, inverter-control, small-signal-stability]
created: "2026-05-04"
updated: "2026-05-19"
---

# 同步旋转坐标系锁相环方法 (SRF-PLL)

## 1. 定义与边界

同步旋转坐标系锁相环（Synchronous Reference Frame PLL, SRF-PLL）是最经典、应用最广泛的并网变流器同步方法。其基本原理是：将三相电网电压经 Park 变换（abc→dq）投影到同步旋转坐标系后，通过闭环调节使 q 轴电压 $v_q$ 收敛至零，从而估计电网电压的相位角和频率。

SRF-PLL 是众多高级 PLL 结构（如 DSOGI-PLL、解耦双同步参考坐标系 PLL 等）的数学基础和性能基线 [Ranasinghe 2024]。本页聚焦 SRF-PLL 的 EMT 仿真建模、参数设计和弱网失稳机理。不讨论具体拓扑变体（如 DSOGI、增强型 PLL）或与其无关的惯量控制方法。

**与相关 PLL 变体的关系图谱：**

| 变体类型 | 与 SRF-PLL 的关系 | 精度提升来源 | 计算开销增量 |
|---------|-----------------|------------|------------|
| DSOGI-PLL | SRF-PLL 前增加正交信号发生器 | 抗电网畸变/不平衡 | 额外二阶滤波器 |
| 增强型 SRF-PLL | 增加暂态检测+自适应带宽 | SCR 极限从 2.3→1.0 | 暂态检测逻辑 |
| 解耦双同步坐标系 PLL | 双坐标系解耦正序/负序 | 不平衡下 100 Hz 脉动抑制 | 两套 Park 变换 |

## 2. EMT 仿真中的作用

在 EMT 仿真中，SRF-PLL 的关键作用包括：

1. **同步信号生成**: 为跟网型逆变器提供电网电压相位角 $\theta$ 和频率 $\omega$，支撑 dq 坐标变换和电流/功率控制。
2. **弱网稳定性分析**: SRF-PLL 与电网阻抗的交互是 GFL-VSC 小信号失稳的主要机制，涉及跨临界分岔和 Hopf 分岔两种模式 [Carreño 2026]。EMT 模型中 $di/dt$ 效应通过 PLL 闭环反馈影响同步稳定性——这是传统 RMS 模型完全遗漏的关键机理。
3. **控制性能基线**: 作为衡量更复杂 PLL 结构（DSOGI-PLL、自适应带宽 PLL 等）性能改进的对照参考。
4. **初始化关键环节**: SRF-PLL 的状态变量（PI 输出、角度积分器）需要在 EMT 启动时精确初始化，否则会导致仿真从零初值经历数百毫秒的非物理暂态过程 [Guilherme 2023]。

**EMT 仿真中 SRF-PLL 的典型精度-效率权衡：**

| 模型类型 | 开关状态 | 计算效率 | 适用场景 | PLL 同步精度 |
|---------|---------|---------|---------|-----------|
| 全开关模型 | 每个开关事件解析 | ★☆☆ | HVDC/储能 Detailed EMT | 最高（实时跟踪） |
| 平均值模型 | 载波周期平均 | ★★☆ | 机侧控制验证 | 较高（受载波周期平均影响） |
| 降阶等效模型 | 跳过 PLL 动态 | ★★★ | 稳态潮流初始化 | 无 PLL（预计算角度） |

## 3. 关键原理与算法

### 3.1 基本结构

SRF-PLL 由三个环节组成 [Ranasinghe 2024]：

**环节 1: Park 变换（abc → dq）**

三相电网电压 $v_a, v_b, v_c$ 经 Clark 变换（abc → αβ）后，再经旋转坐标变换得到 dq 分量：

$$
\begin{bmatrix} v_d \\ v_q \end{bmatrix} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} v_\alpha \\ v_\beta \end{bmatrix}
$$

其中 $\theta$ 为 PLL 估计的电网电压相位角。当 $v_q = 0$ 时，表示锁相成功，此时 $v_d = |V|$ 为电网电压幅值。

**环节 2: 环路滤波器（PI 控制器）**

PI 控制器调节 $v_q$ 至零，输出频率偏差量：

$$
\Delta\omega = K_p \cdot v_q + K_i \cdot \int v_q \, dt
$$

其中 $K_p$ 和 $K_i$ 分别为比例增益和积分增益。

**环节 3: 压控振荡器（积分器）**

对频率积分得到估计相位：

$$
\theta = \int \omega \, dt = \int (\omega_0 + \Delta\omega) \, dt
$$

其中 $\omega_0 = 2\pi f_0$ 为电网标称角频率。

**SRF-PLL 完整框图（学术白底风格）：**

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 820 320" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入 -->
  <rect x="10" y="130" width="90" height="50" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5" rx="4"/>
  <text x="55" y="160" text-anchor="middle" font-size="13" font-family="Arial" fill="#1e40af">v_abc</text>
  <text x="55" y="175" text-anchor="middle" font-size="10" font-family="Arial" fill="#3b82f6">三相电网电压</text>

  <!-- Clark变换 -->
  <rect x="130" y="130" width="90" height="50" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="175" y="155" text-anchor="middle" font-size="12" font-family="Arial" fill="#166534">Clark</text>
  <text x="175" y="170" text-anchor="middle" font-size="11" font-family="Arial" fill="#16a34a">abc→αβ</text>

  <!-- Park变换 -->
  <rect x="270" y="130" width="90" height="50" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="315" y="155" text-anchor="middle" font-size="12" font-family="Arial" fill="#166534">Park</text>
  <text x="315" y="170" text-anchor="middle" font-size="11" font-family="Arial" fill="#16a34a">αβ→dq(θ̂)</text>

  <!-- q轴误差检测 -->
  <rect x="400" y="130" width="80" height="50" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" rx="4"/>
  <text x="440" y="155" text-anchor="middle" font-size="11" font-family="Arial" fill="#92400e">v_q → 0</text>
  <text x="440" y="170" text-anchor="middle" font-size="10" font-family="Arial" fill="#d97706">误差检测</text>

  <!-- PI控制器 -->
  <rect x="520" y="110" width="90" height="70" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" rx="4"/>
  <text x="565" y="138" text-anchor="middle" font-size="12" font-family="Arial" fill="#92400e">PI</text>
  <text x="565" y="155" text-anchor="middle" font-size="10" font-family="Arial" fill="#b45309">Kp, Ki</text>
  <text x="565" y="170" text-anchor="middle" font-size="10" font-family="Arial" fill="#d97706">Δω</text>

  <!-- VCO/积分器 -->
  <rect x="650" y="120" width="90" height="50" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="695" y="148" text-anchor="middle" font-size="11" font-family="Arial" fill="#166534">VCO</text>
  <text x="695" y="163" text-anchor="middle" font-size="10" font-family="Arial" fill="#16a34a">∫ω dt = θ̂</text>

  <!-- 输出 -->
  <rect x="770" y="130" width="40" height="50" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" rx="4"/>
  <text x="790" y="160" text-anchor="middle" font-size="11" font-family="Arial" fill="#5b21b6">θ̂</text>

  <!-- 箭头：输入→Clark→Park→误差检测→PI→VCO→输出 -->
  <line x1="100" y1="155" x2="130" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="220" y1="155" x2="270" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="360" y1="155" x2="400" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="480" y1="155" x2="520" y2="145" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="610" y1="145" x2="650" y2="145" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="740" y1="145" x2="770" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 反馈：VCO → Park (虚线) -->
  <line x1="695" y1="170" x2="695" y2="260" stroke="#7c3aed" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="695" y1="260" x2="315" y2="260" stroke="#7c3aed" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="315" y1="260" x2="315" y2="180" stroke="#7c3aed" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="500" y="275" text-anchor="middle" font-size="10" font-family="Arial" fill="#7c3aed">PLL估计相位 θ̂ 反馈到 Park 变换</text>

  <!-- 标称频率注入 -->
  <rect x="580" y="195" width="90" height="40" fill="#dbeafe" stroke="#2563eb" stroke-width="1" rx="3"/>
  <text x="625" y="215" text-anchor="middle" font-size="10" font-family="Arial" fill="#1e40af">+ω₀</text>
  <text x="625" y="228" text-anchor="middle" font-size="9" font-family="Arial" fill="#3b82f6">(标称频率)</text>
  <line x1="595" y1="195" x2="595" y2="180" stroke="#333" stroke-width="1"/>
  <line x1="595" y1="180" x2="620" y2="180" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>
  <line x1="620" y1="180" x2="620" y2="170" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>

  <!-- ω输出到积分器 -->
  <line x1="610" y1="180" x2="635" y2="145" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ω输出（反馈到VCO） -->
  <line x1="695" y1="120" x2="695" y2="90" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>
  <rect x="650" y="50" width="90" height="40" fill="#ede9fe" stroke="#7c3aed" stroke-width="1" rx="3"/>
  <text x="695" y="70" text-anchor="middle" font-size="11" font-family="Arial" fill="#5b21b6">ω = ω₀+Δω</text>
  <text x="695" y="83" text-anchor="middle" font-size="9" font-family="Arial" fill="#7c3aed">估计频率</text>

  <!-- 定义标记 -->
  <text x="10" y="25" font-size="14" font-family="Arial" fill="#333" font-weight="bold">SRF-PLL 完整结构框图</text>
  <text x="10" y="42" font-size="11" font-family="Arial" fill="#666">输入：三相电网电压 v_abc → 输出：估计相位 θ̂ 和频率 ω</text>

  <text x="10" y="300" font-size="9" font-family="Arial" fill="#888">图1 · SRF-PLL 三个环节：Park变换(dq坐标) → PI控制器(v_q→Δω) → 压控振荡器(Δω→θ̂)</text>

  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>

### 3.2 小信号模型与失稳机理

Carreño 2026 基于慢快系统理论推导了 SRF-PLL 在弱电网条件下的完整失稳边界。核心物理机制是电感 $di/dt$ 效应通过 PLL 闭环反馈影响同步稳定性——传统 RMS 模型由于忽略 $di/dt$，会错误地预测系统在所有参数下稳定（误差 100%）。

#### 3.2.1 跨临界分岔（单调失稳）

当 PLL 比例增益 $K_p$ 与有功电流 $i_P$ 和电网电感 $L$ 的乘积超过 1 时，系统发生跨临界分岔（Transcritical Bifurcation）：

$$
1 - K_p \, i_P \, L > 0 \quad \text{（稳定）}
$$

$$
1 - K_p \, i_P \, L < 0 \quad \text{（失稳——单调发散）}
$$

临界条件 $1 - K_p i_P L = 0$ 给出了单调失稳边界。物理意义：电感电流变化率通过 PLL 闭环反馈破坏了原有的稳定平衡点。

#### 3.2.2 Hopf 分岔（振荡失稳）

当 Hopf 分岔条件被违反时，系统出现持续的低频振荡（0.5–2 Hz）：

$$
\kappa \triangleq K_p \sqrt{V^2 - (i_P X)^2} - K_i \, i_P \, L > 0 \quad \text{（失稳——持续振荡）}
$$

其中 $\kappa$ 为 PLL-电网耦合强度系数，$X = \omega L$ 为电网电抗。$\kappa < 0$ 时系统阻尼充足，$\kappa > 0$ 时系统进入弱阻尼状态。

#### 3.2.3 耦合强度系数与 SCR 的关系

短路比（SCR）与 SRF-PLL 失稳风险呈强相关性 [Carreño 2026]。耦合强度系数定义为：

$$
\kappa = \frac{K_p \, i_P \, L}{\omega}
$$

- **SCR < 2.0** 时，Hopf 分岔临界功率从 0.9 pu 降至 0.55 pu（下降约 40%）
- 当 $\kappa > 0.05$ 时，系统进入弱阻尼区域（阻尼比 $\zeta < 0.1$）
- 当 $\kappa > 0.1$ 时，单调失稳风险显著增加

### 3.3 参数设计与带宽

SRF-PLL 的 PI 参数通过开环传递函数设计 [Ranasinghe 2024]。开环传递函数为：

$$
G_{ol}(s) = \frac{K_p s + K_i}{s} \cdot \frac{1}{s} = \frac{K_p s + K_i}{s^2}
$$

闭环特征方程对应二阶系统，自然频率 $\omega_n$ 和阻尼比 $\zeta$ 与 PI 参数的关系为：

$$
\omega_n = \sqrt{\frac{K_i}{\omega_c}}, \quad \zeta = \frac{K_p}{2} \sqrt{\frac{\omega_c}{K_i}}
$$

其中 $\omega_c$ 为交叉频率（近似等于 PLL 带宽）。设计流程：

1. 根据系统响应速度要求选定 $\omega_c$（通常为 $2\pi \times 10$ 到 $2\pi \times 50$ rad/s）
2. 选定 $\zeta = 0.707$（临界阻尼附近）获得快速且不过冲的响应
3. 由 $\omega_n$ 和 $\zeta$ 反解 $K_p$ 和 $K_i$

**典型参数范围 [Ranasinghe 2024] [Luchini 2023]：**

| 应用场景 | ωc (rad/s) | Kp | Ki | ζ | 来源 |
|---------|-----------|----|----|---|------|
| 60Hz 跟网逆变器（基准） | 62 | 57.1 | 1660.1 | 0.7 | [Ranasinghe 2024] |
| ATP/ATPDraw 等效模型 | — | 0.8 | 61.69 | — | [Luchini 2023] |
| 50Hz 自适应带宽 PLL | 50 | 38.3 | 980.0 | 0.7 | [Ranasinghe 2024] |
| 弱电网（高鲁棒性） | 25 | 15.0 | 225.0 | 0.9 | 工程经验 |

**带宽与动态响应的关系：**

| PLL 带宽 | 相位误差 (1°) | 同步时间 (ms) | 谐波敏感度 | 弱网稳定性 |
|---------|-------------|-------------|----------|-----------|
| 宽带宽 (ωc>100 rad/s) | <1° | <20 | 高 | 差（SCR>3推荐） |
| 中等带宽 (ωc≈50 rad/s) | 1–3° | 20–50 | 中 | 中（SCR>2推荐） |
| 窄带宽 (ωc<30 rad/s) | 3–8° | 50–100 | 低 | 好（SCR>1.5可用） |

### 3.4 初始化

SRF-PLL 的稳态初始化精度直接影响 EMT 仿真启动质量 [Guilherme 2023]。三阶段初始化流程：

**阶段 1: 预计算稳态工作点**
- 测量或计算 PCC 电压幅值 $V$ 和相角 $\theta_0$
- 计算 dq 坐标系下的稳态电流：$i_d = 2P/(3v_d)$，$i_q = -2Q/(3v_d)$

**阶段 2: 状态变量初始化**
- 角度积分器初值：$\hat\theta = \theta_0 + \angle H(j\omega)$，其中 $H(j\omega) = 1/(1+j\omega\tau)$ 为 LPF 传递函数
- PI 控制器输出初值设为 0（稳态频率偏差为零）
- 积分器状态 $\int v_q dt = 0$

**阶段 3: 暂态抑制**
- 若不初始化，PLL 角度与电网电压相位不一致会导致 300 ms 以上的数值振荡 [Guilherme 2023]
- 建议在 EMT 仿真前 3–5 个工频周期内逐步放开 PLL 控制（软启动），使数值暂态衰减

## 4. 形式化表达

### 4.1 核心方程汇总

| 方程 | 含义 | 来源 |
|------|------|------|
| $v_q \to 0$ | SRF-PLL 控制目标（锁相成功条件） | 基本定义 |
| $1 - K_p \, i_P \, L > 0$ | 跨临界分岔稳定条件（单调失稳边界） | [Carreño 2026] |
| $K_p \sqrt{V^2 - (i_P X)^2} - K_i \, i_P \, L > 0$ | Hopf 分岔稳定条件（振荡失稳边界） | [Carreño 2026] |
| $\kappa = K_p \, i_P \, L / \omega$ | PLL-电网耦合强度系数 | [Carreño 2026] |
| $\hat\theta = \theta + \angle H(j\omega)$ | PLL 角度初始化公式 | [Guilherme 2023] |
| $\omega_n = \sqrt{K_i / \omega_c}$ | SRF-PLL 自然频率 | [Ranasinghe 2024] |
| $\zeta = \frac{K_p}{2} \sqrt{\omega_c / K_i}$ | SRF-PLL 阻尼比 | [Ranasinghe 2024] |
| $i_d = 2P/(3v_d), \; i_q = -2Q/(3v_d)$ | 电网电压定向电流反解 | [Luchini 2023] |

### 4.2 状态空间小信号模型（EMT 仿真用）

SRF-PLL 在 EMT 中的线性化状态空间模型（5 状态）[Carreño 2026]：

$$
\dot{x} = A x + B u, \quad y = C x + D u
$$

其中状态向量 $x = [\Delta\theta, \Delta\omega, \Delta v_q, \Delta i_P, \Delta v_d]^T$，状态矩阵 $A$ 的特征值决定小信号稳定性。该模型包含：
- **2 个 PLL 状态**：角度误差 $\Delta\theta$、频率偏差 $\Delta\omega$
- **3 个网络状态**：q 轴电压偏差 $\Delta v_q$、有功电流偏差 $\Delta i_P$、d 轴电压偏差 $\Delta v_d$

## 5. 关键技术挑战

### 挑战 1: 弱电网失稳风险
SRF-PLL 在弱电网（SCR < 2）中存在跨临界分岔和 Hopf 分岔两种失稳模式，且传统 RMS 模型完全无法捕捉这两种机理（误差 100%）[Carreño 2026]。

### 挑战 2: PLL 带宽与动态响应的矛盾
增加 PLL 带宽可加快同步响应，但会放大对电网谐波和暂态扰动的敏感度。需要在同步速度和鲁棒性之间进行权衡设计。

### 挑战 3: 频率耦合效应
SRF-PLL 在不对称电网条件下会产生 2 倍频脉动，负序分量在 dq 坐标系中导致 100 Hz 脉动，影响相位估计精度 [Ranasinghe 2024]。

### 挑战 4: 与电流控制的耦合
PLL 估计的相位角用于 dq 坐标变换，PLL 动态直接影响电流控制性能。在暂态期间，PLL 动态和电流控制动态相互耦合，可能导致额外的振荡风险。

### 挑战 5: 数值初始化质量
SRF-PLL 状态变量的初值误差会在 EMT 仿真启动时引发 300 ms 以上的数值暂态，影响故障穿越仿真的初始条件准确性 [Guilherme 2023]。

## 6. 量化性能边界

### 6.1 稳定性边界数据

| 参数 | 稳定区域 | 临界边界 | 失稳区域 | 来源 |
|------|---------|---------|---------|------|
| $1 - K_p i_P L$ | > 0（单调稳定） | = 0（临界） | < 0（单调发散） | [Carreño 2026] |
| $\kappa$ | < 0.05（强阻尼） | 0.05–0.1（弱阻尼） | > 0.1（失稳） | [Carreño 2026] |
| SCR | ≥ 2.0（强电网） | 1.5–2.0（弱电网） | < 1.5（极弱） | [Carreño 2026] |
| Hopf 临界功率 | 0.9 pu（SCR=2） | — | 0.55 pu（SCR<2） | [Carreño 2026] |

### 6.2 性能对比数据

| 来源 | 测试条件 | 关键数据 | 结论 |
|------|---------|---------|------|
| [Ranasinghe 2024] | 60Hz 系统, ωc=62 rad/s | Kp=57.1, Ki=1660.1 | 基准 SRF-PLL 参数 |
| [Luchini 2023] | ATP 等效模型 | Kp=0.8, Ki=61.69; 误差 2.33%, 速度提升 70% | SRF-PLL 用于 ATP 等效模型同步 |
| [Carreño 2026] | 单换流器无穷大母线 | 状态数减少 75%（vs EMT） | RMS+ 模型保留 PLL 动态 |
| [Guilherme 2023] | VSC 稳态初始化 | 未初始化→300ms+ 暂态 | 初始化是 EMT 仿真质量关键 |

## 7. 适用边界与选择指南

### 7.1 适用条件
- 电网强度较好（SCR ≥ 2）的跟网型逆变器并网场景
- 三相电压对称、谐波含量较低的工况
- 需要快速实现标准 dq 解耦控制的系统级 EMT 仿真

### 7.2 失效边界
- **弱电网（SCR < 2）**: SRF-PLL 在弱电网中存在跨临界分岔和 Hopf 分岔两种失稳模式 [Carreño 2026]
- **严重不平衡/畸变电压**: SRF-PLL 仅跟踪基波正序，负序和零序分量会在 dq 坐标系中产生 100 Hz 脉动，导致相位估计误差
- **电压幅值骤降**: 幅值波动通过 PI 环路耦合影响带宽，造成同步动态退化
- **单相故障**: 不对称故障期间 SRF-PLL 的相位估计误差显著增大，可能触发逆变器保护脱网
- **高频谐波**: SRF-PLL 不含预滤波器，对 PWM 谐波和背景谐波敏感，需要额外 LPF 或陷波器

### 7.3 选择指南

| 场景 | 推荐结构 | 原因 |
|------|--------|------|
| 强电网 SCR ≥ 3，对称电压 | SRF-PLL | 简单高效，基准性能 |
| SCR 2–3，轻度畸变 | DSOGI-PLL | 抗畸变/不平衡 |
| SCR < 2，弱电网 | 自适应带宽 DSOGI-PLL | 扩展 SCR 极限至 1.0 |
| 不平衡故障期间 | 解耦双同步坐标系 PLL | 负序分离处理 |
| 谐波环境（PWM背景谐波） | 带陷波器的 SRF-PLL | 抑制特定次数谐波 |

## 8. 相关方法

| 方法 | 关系 | 关键特点 |
|------|------|---------|
| [[dsogi-pll]] | SRF-PLL 的增强变体 | DSOGI 正交信号发生器，抗电网畸变/不平衡 |
| [[grid-connected-inverter]] | SRF-PLL 的应用对象 | GFL 变流器的同步控制核心 |
| [[pll-design]] | SRF-PLL 的参数整定专题 | 带宽、阻尼比、锁相精度的设计方法 |
| [[small-signal-stability]] | SRF-PLL 稳定性分析的上层框架 | 小信号失稳模式与 PLL 动态的关联 |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]] | SRF-PLL 失稳机理论文 | RMS+ 模型揭示 di/dt 耦合失稳机理 |
| [[grid-forming-converters-sufficient-conditions-for-rms-modeling]] | 与 GFM 控制对比 | GFM 控制与 GFL+SRF-PLL 的同步机制对比 |

## 9. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|---------|
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]] | 2026 | RMS+ 模型揭示 SRF-PLL 与电网电感 di/dt 耦合的双模失稳机理（跨临界/Hopf分岔），误差100% vs RMS |
| [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]] | 2024 | 以 SRF-PLL 为基线的 DSOGI-PLL 改进，含暂态冻结和自适应带宽，SCR 极限从 2.3 扩展至 1.0 |
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]] | 2023 | 含 SRF-PLL 的 ATP/ATPDraw 跟网型 IBR 等效模型，Kp=0.8, Ki=61.69，误差 2.33%，速度提升 70% |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in]] | 2023 | 含 SRF-PLL 的 VSC 稳态初始化三阶段流程，未初始化导致 300ms+ 数值暂态 |
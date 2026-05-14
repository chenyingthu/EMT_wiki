---
title: "变步长求解器 (Variable Time Step Solver)"
type: method
tags: [variable-time-step, adaptive, error-control, stiff-system, emt-simulation, runge-kutta, bdf, exponential-integrator]
created: "2026-05-04"
updated: "2026-05-13"
---

# 变步长求解器 (Variable Time Step Solver)

## 定义

变步长求解器（Variable Time Step Solver）是一类在数值积分过程中根据解的局部特性（如局部截断误差估计、系统刚性程度、开关事件临近程度）动态调整积分步长的数值算法。其核心思想是：在解变化平缓的稳态阶段采用大步长以降低计算量，在暂态突变（如开关动作、故障发生）阶段自动缩小步长以保证精度和稳定性。

与固定步长方法（如固定步长梯形法、固定步长向后欧拉法）相比，变步长方法在相同精度约束下通常可显著减少积分步数，但其实现复杂度更高——需要在每一步进行误差估计、步长预测/校正、事件检测与定位、以及可能的步长拒绝与重试。

**核心公式 · 步长更新律**：

$$\Delta t_{n+1} = \Delta t_n \left( \frac{\epsilon}{e_n} \right)^{1/p} \left( \frac{e_{n-1}}{e_n} \right)^{k_1} \left( \frac{e_{n-1} e_{n-2}}{e_n^2} \right)^{k_2}$$

其中 $\epsilon$ 为用户设定的误差容限，$e_n$ 为当前步的局部截断误差估计值，$p$ 为积分方法的阶数，后两项为 PID 型历史误差修正因子（$k_1, k_2$ 为增益系数）。该公式在 Hairer & Wanner (1996) 和 Shampine et al. (1993) 的 ODE 求解理论中有严格推导。

**边界限定**：本方法主要适用于**离线仿真**场景。实时仿真（如 RTDS、OPAL-RT）因对确定性时序有严格要求，通常采用固定步长或预定义的变步长序列。

## EMT中的角色

在电力系统电磁暂态（EMT）仿真中，变步长求解器承担以下关键角色：

1. **暂态-稳态自适应**：电力系统运行通常在稳态（变化缓慢）与暂态（开关、故障导致快速变化）之间切换。变步长求解器在稳态阶段可将步长提升至毫秒级（如 100 μs ~ 1 ms），在暂态阶段自动缩小至微秒级（1 μs ~ 10 μs），实现数量级的计算效率提升。

2. **开关事件精确定位**：电力电子变换器、晶闸管换流器、断路器等的开关动作时刻通常不与仿真步长对齐。变步长求解器结合事件定位算法（interpolation / root-finding），可将开关时刻定位到亚步长精度，避免固定步长方法因"错过"开关时刻而引入的低次谐波和数值振荡。

3. **局部截断误差可控**：通过每步的误差估计，求解器确保全局误差满足用户指定的容限（通常为 0.1% ~ 1%），在精度和效率之间实现最优折中。

4. **刚性系统处理**：当系统包含小时间常数元件（如大容量电容、高频滤波器）时，系统呈现刚性。变步长求解器可自动切换到适合刚性系统的积分方法（如 BDF 法），并在刚性缓解后切换回高效方法。

**EMT仿真中的核心挑战**：
- 开关事件时刻与积分步长的非对齐性
- 刚性与非刚性区域的自动识别与切换
- 误差估计的可靠性（尤其在高频谐振点）
- 步长调整带来的数值不连续性处理

## 核心机制

### 1. 局部截断误差估计

局部截断误差（Local Truncation Error, LTE）是变步长求解器的核心反馈信号。不同方法采用不同的误差估计策略：

**嵌入式 Runge-Kutta 法（如 RK45 / Dormand-Prince）**：在同一计算步中使用两个不同阶数的公式（如 4 阶和 5 阶）同时推进，两者的差值即为 LTE 估计：

$$e_n = \| y_{n+1}^{(5)} - y_{n+1}^{(4)} \|$$

其中 $y_{n+1}^{(5)}$ 和 $y_{n+1}^{(4)}$ 分别为 5 阶和 4 阶公式计算的下一步状态。由于两个公式共享中间阶段（stage）计算，额外开销仅为一次状态向量范数计算。

**多步法（如 Adams-Bashforth-Moulton）**：使用预测器-校正器（PECE）格式，预测值与校正值之差作为误差估计：

$$e_n = \| y_{n+1}^{\text{corrected}} - y_{n+1}^{\text{predicted}} \|$$

**BDF 法（Gear 法）**：利用阶数变化时的公式差异估计误差，或使用嵌入的低一阶 BDF 公式。

**指数积分器（Exponential Integrator）**：通过 $\phi$ 函数展开的截断项估计 LTE：

$$e_n \approx \phi_{p+1}(A_k h) h^{p+1} B_k \frac{d^{(p)} u_n}{dt^{(p)}}$$

其中 $p$ 为 $\phi$ 函数展开项数，$A_k, B_k$ 为当前开关拓扑下的状态空间矩阵（Paull et al., 2025）。

### 2. 步长选择策略

步长选择是变步长求解器的核心决策环节，通常包含三个子步骤：

**（1）理想步长计算**：基于当前 LTE 估计和目标容限，计算满足精度要求的理想步长：

$$\Delta t_{\text{ideal}} = \Delta t_{\text{current}} \left( \frac{\epsilon}{e_n} \right)^{1/(p+1)}$$

其中 $p$ 为当前积分方法的阶数。该公式确保新步长下的 LTE 接近 $\epsilon$。

**（2）安全系数缩放**：为避免误差估计偏差导致频繁拒绝步长，引入安全因子 $\sigma \in (0.85, 0.95)$：

$$\Delta t_{\text{safe}} = \sigma \cdot \Delta t_{\text{ideal}}$$

**（3）变化率限制**：为防止步长在相邻步间剧烈震荡，限制步长变化率（通常每步变化不超过 2~5 倍）：

$$\Delta t_{n+1} = \min(\Delta t_{\text{safe}}, \beta_{\max} \cdot \Delta t_n)$$
$$\Delta t_{n+1} = \max(\Delta t_{\min}, \beta_{\min} \cdot \Delta t_{n+1})$$

其中 $\beta_{\max} \approx 3 \sim 5$，$\beta_{\min} \approx 0.1 \sim 0.3$。

**PID 型步长控制器**：为进一步提升步长控制的平滑性，引入历史误差信息的 PID 控制器：

$$\Delta t_{n+1} = \Delta t_n \cdot K_p \cdot \left( \frac{\epsilon}{e_n} \right) + K_i \cdot e_{n-1} + K_d \cdot (e_{n-1} - e_{n-2})$$

Carbone et al. (2002) 在分析 EMTP 截断误差时指出，步长选择策略对谐振电路的仿真精度有显著影响——不当的步长会放大谐振频率处的建模误差。

### 3. 事件检测与定位（Event Location）

电力电子电路的开关事件是变步长求解器面临的最重要事件类型。事件定位的核心问题是：开关动作发生在两个仿真步之间，如何精确确定其发生时刻？

**（1）符号检测法（Sign Change Detection）**：

定义事件函数 $g(t)$（如开关电流方向、电压阈值），当 $g(t_n)$ 与 $g(t_{n+1})$ 异号时，判定开关事件发生在 $[t_n, t_{n+1}]$ 区间内。

**（2）插值定位（Interpolation-based Localization）**：

在检测到事件跨越步长后，利用步内密集输出点（dense output）进行高阶插值，求解 $g(t_d) = 0$ 的根 $t_d$：

- **线性插值**：最简方案，定位精度为 $O(h^2)$，PSCAD/EMTP 默认采用
- **二次插值**：利用密集输出点提供步内中间状态，定位精度为 $O(h^3)$（Li et al., 2020）
- **三次 Hermite 插值**：同时利用状态值和导数值，定位精度为 $O(h^4)$

**（3）步长分割**：

定位到开关时刻 $t_d$ 后，将原步长分割为两段：$[t_n, t_d]$ 和 $[t_d, t_{n+1}]$，分别用对应拓扑的积分公式推进。

**密集输出公式（Dense Output Formula）**：

矩阵指数积分器的独特优势在于其缩放平方算法天然产生密集输出点（Li et al., 2020; Paull et al., 2025）：

$$x\left(t_0 + \frac{h}{2^{s-i}}\right) = [I_n \quad 0] \cdot e^{\frac{h}{2^{s-i}}\mathbf{A}} \cdot x_0, \quad i = 0, 1, \dots, s-1$$

这些密集输出点无需额外计算成本，直接复用矩阵指数缩放平方过程中的中间结果，为高阶插值提供精确的步内状态快照。

### 4. 积分方法选择与切换

变步长求解器通常支持多种积分方法，并根据系统特性自动切换：

| 方法 | 稳定性 | 阶数 | 适用场景 | 典型步长范围 |
|------|--------|------|----------|-------------|
| 梯形法 (TR) | A-稳定 | 2阶局部 | 非刚性系统通用 | 1 μs ~ 100 μs |
| 向后欧拉 (BE) | L-稳定 | 1阶局部 | 强刚性系统 | 0.1 μs ~ 10 μs |
| RK45 (Dormand-Prince) | 条件稳定 | 4/5阶局部 | 非刚性、高精度 | 1 μs ~ 1 ms |
| BDF (Gear) | L-稳定 | 1~6阶可变 | 刚性系统 | 0.1 μs ~ 100 μs |
| 指数积分器 (MEXP) | L-稳定 | 1~5阶可变 | 电力电子开关电路 | 0.06 μs ~ 50 μs |
| 紧凑格式 (CS) | A-稳定 | 2~3阶局部 | 高精度需求 | 0.5 μs ~ 20 μs |

**指数积分器方法**：

对于状态空间方程 $\dot{x}(t) = A_k x(t) + B_k u(t)$，指数积分器的一步更新为：

$$x_{n+1} = e^{A_k h} x_n + \int_{t_n}^{t_n+h} e^{A_k(t_n+h-\tau)} B_k u(\tau) d\tau$$

将强迫函数项展开为 $\phi$ 函数级数：

$$x_{n+1} = e^{A_k h} x_n + \sum_{j=1}^{\infty} \phi_j(A_k h) h^j B_k \frac{d^{(j-1)} u_n}{dt^{(j-1)}}$$

其中 $\phi$ 函数定义为：

$$\phi_j(z) = \frac{1}{(j-1)!} \int_0^1 e^{(1-\theta)z} \theta^{j-1} d\theta, \quad j \geq 1$$

矩阵指数 $e^{A_k h}$ 通过 Padé 逼近计算，如 $(3,3)$ 阶 Padé：

$$e^{A_k h} \approx \frac{I + \frac{1}{2}A_k h + \frac{1}{10}(A_k h)^2 + \frac{1}{120}(A_k h)^3}{I - \frac{1}{2}A_k h + \frac{1}{10}(A_k h)^2 - \frac{1}{120}(A_k h)^3}$$

指数积分器的 L 稳定性确保其在刚性系统中不会产生数值振荡（Paull et al., 2025; Li et al., 2020）。

**紧凑格式（Compact Scheme, CS）**：

紧凑格式在积分中额外考虑了状态变量的导数值，从而获得高于传统方法的精度（Tanaka & Baba, 2023; Matehkolaei et al., 2026）。对于一般微分方程 $\dot{x} = f(x,t)$，CS 格式为：

$$x_{k+1} = x_k + \frac{\Delta t}{6}(f_{k+1} + 4f_{k+\frac{1}{2}} + f_k)$$

其中 $f_{k+\frac{1}{2}} = f\left(\frac{x_k + x_{k+1}}{2}, t_k + \frac{\Delta t}{2}\right)$。该格式利用中点导数信息，在相同步长下比梯形法具有更高的精度阶数。

**不连续性处理**：Matehkolaei et al. (2026) 指出 CS 在开关不连续点会产生异常结果，因此建议在不连续点切换到 CS_BE 混合格式（CS + 向后欧拉），以兼顾精度和稳定性。

### 5. 变步长与电力电子仿真的协同

在电力电子变换器仿真中，变步长求解器与离散状态事件驱动（Discrete-State Event-Driven, DSED）框架深度协同（Paull et al., 2025）：

**DSED 框架**：利用电力电子变换器的数字控制信号（如 PWM 调制波）精确预测开关事件时刻，将积分步长与开关事件对齐。DSED 的步长由控制器信号决定，而非由误差估计决定，因此具有确定性和可预测性。

**AGEI（自适应粒度指数积分器）**：在 DSED 框架基础上，AGEI 算法提出自适应粒度预计算策略：
- 将连续步长范围按数量级划分（如 0.1 μs, 1 μs, 10 μs）
- 仅预计算 1~9 倍缩放因子对应的矩阵指数 $e^{A_k h}$ 和 $\phi_j(A_k h)$
- 仿真时将事件间总步长拆解为粗、中、细粒度子步长顺序积分
- 基于 LTE 动态调整 $\phi$ 函数展开项数以满足误差阈值

**混合数值积分**：对于 MMC 等多电平变换器，采用中点法与梯形法的混合积分（Hybrid Numerical Integration），将 MMC 模型离散化为 Norton 等效电路，等效电导矩阵保持恒定，减少节点方程维度（Zhang et al., 2023）。

## 形式化表达

### 变步长求解器通用算法流程

```
输入: 初始状态 x₀, 初始步长 Δt₀, 误差容限 ε, 积分方法 M
输出: 时间序列 {tₙ, xₙ}

n ← 0
t ← t₀, x ← x₀
while t < t_end do
    // 1. 误差估计
    x_high ← M_high(x, t, Δt)        // 高阶公式推进
    x_low ← M_low(x, t, Δt)          // 低阶公式推进
    e ← ||x_high - x_low||            // LTE 估计
    
    // 2. 步长接受/拒绝
    if e ≤ ε then
        接受步长: t ← t + Δt, x ← x_high, n ← n + 1
    else
        拒绝步长: Δt ← 0.5·Δt, 重试
        if 重试次数 > 5 then 报错: 步长过小
        
    // 3. 步长调整
    Δt_new ← Δt · σ · (ε/e)^(1/(p+1))
    Δt_new ← clamp(Δt_new, Δt_min, Δt_max, β_min·Δt, β_max·Δt)
    Δt ← Δt_new
    
    // 4. 事件检测
    if event_detected(t, t+Δt) then
        t_d ← locate_event(t, t+Δt)    // 插值定位
        将步长分割为 [t, t_d] 和 [t_d, t+Δt]
        更新系统拓扑 A_k, B_k
end while
```

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <marker id="arrow-red" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333" font-family="sans-serif">变步长求解器架构与工作流程</text>
  
  <!-- Input block (blue) -->
  <rect x="30" y="55" width="160" height="60" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="78" text-anchor="middle" font-size="13" fill="#1e3a5f" font-family="sans-serif" font-weight="bold">系统状态方程</text>
  <text x="110" y="96" text-anchor="middle" font-size="11" fill="#1e3a5f" font-family="sans-serif">ẋ = A(t)x + B(t)u(t)</text>
  
  <!-- Error Estimation block (yellow) -->
  <rect x="270" y="55" width="170" height="60" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="355" y="78" text-anchor="middle" font-size="13" fill="#5c3d1e" font-family="sans-serif" font-weight="bold">局部截断误差估计</text>
  <text x="355" y="96" text-anchor="middle" font-size="11" fill="#5c3d1e" font-family="sans-serif">eₙ = ‖y⁽⁵⁾ − y⁽⁴⁾‖</text>
  
  <!-- Step Size Selection block (green) -->
  <rect x="520" y="55" width="170" height="60" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="605" y="78" text-anchor="middle" font-size="13" fill="#14532d" font-family="sans-serif" font-weight="bold">步长选择策略</text>
  <text x="605" y="96" text-anchor="middle" font-size="11" fill="#14532d" font-family="sans-serif">Δtₙ₊₁ = f(eₙ, ε, p)</text>
  
  <!-- Integration block (yellow) -->
  <rect x="270" y="180" width="170" height="60" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="355" y="203" text-anchor="middle" font-size="13" fill="#5c3d1e" font-family="sans-serif" font-weight="bold">数值积分推进</text>
  <text x="355" y="221" text-anchor="middle" font-size="11" fill="#5c3d1e" font-family="sans-serif">TR / RK45 / BDF / ExpInt</text>
  
  <!-- Event Detection block (red) -->
  <rect x="520" y="180" width="170" height="60" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="605" y="203" text-anchor="middle" font-size="13" fill="#7f1d1d" font-family="sans-serif" font-weight="bold">事件检测与定位</text>
  <text x="605" y="221" text-anchor="middle" font-size="11" fill="#7f1d1d" font-family="sans-serif">g(t) = 0, 插值定位 t_d</text>
  
  <!-- Output block (purple) -->
  <rect x="520" y="340" width="170" height="60" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="605" y="363" text-anchor="middle" font-size="13" fill="#3b0764" font-family="sans-serif" font-weight="bold">状态更新输出</text>
  <text x="605" y="381" text-anchor="middle" font-size="11" fill="#3b0764" font-family="sans-serif">xₙ₊₁, tₙ₊₁ → 下一时刻</text>
  
  <!-- Accept/Reject decision (green) -->
  <rect x="270" y="340" width="170" height="60" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="355" y="363" text-anchor="middle" font-size="13" fill="#14532d" font-family="sans-serif" font-weight="bold">接受/拒绝决策</text>
  <text x="355" y="381" text-anchor="middle" font-size="11" fill="#14532d" font-family="sans-serif">eₙ ≤ ε ? 接受 ✓ / 拒绝 ✗</text>
  
  <!-- Arrow: Input → Error Estimation -->
  <line x1="190" y1="85" x2="265" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow: Error Estimation → Step Size -->
  <line x1="440" y1="85" x2="515" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow: Step Size → Integration (down) -->
  <line x1="605" y1="115" x2="355" y2="175" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow: Integration → Event Detection (right) -->
  <line x1="440" y1="210" x2="515" y2="210" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow: Event Detection → Output (down) -->
  <line x1="605" y1="240" x2="605" y2="335" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow: Integration → Accept/Reject (down) -->
  <line x1="355" y1="240" x2="355" y2="335" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow: Accept → Output (right) -->
  <line x1="440" y1="370" x2="515" y2="370" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Reject arrow (red dashed) -->
  <path d="M 270 370 L 200 370 L 200 140 L 265 140" stroke="#dc2626" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arrow-red)" fill="none"/>
  <text x="185" y="260" text-anchor="middle" font-size="11" fill="#dc2626" font-family="sans-serif" font-weight="bold">拒绝: Δt ← 0.5Δt</text>
  
  <!-- Feedback loop: Output → Input (curved) -->
  <path d="M 520 370 L 430 370 L 430 130 L 30 130 L 30 110" stroke="#333" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow)" fill="none"/>
  <text x="230" y="125" text-anchor="middle" font-size="11" fill="#333" font-family="sans-serif">闭环反馈: 新状态 → 误差估计</text>
  
  <!-- Method selection box (bottom) -->
  <rect x="100" y="440" width="700" height="65" rx="8" fill="#f0f4f8" stroke="#64748b" stroke-width="1.5"/>
  <text x="450" y="462" text-anchor="middle" font-size="13" font-weight="bold" fill="#333" font-family="sans-serif">积分方法选择指南</text>
  <text x="140" y="482" text-anchor="middle" font-size="11" fill="#1e3a5f" font-family="sans-serif">梯形法 (TR)</text>
  <text x="140" y="496" text-anchor="middle" font-size="10" fill="#64748b" font-family="sans-serif">A-稳定, 2阶</text>
  
  <text x="300" y="482" text-anchor="middle" font-size="11" fill="#5c3d1e" font-family="sans-serif">RK45</text>
  <text x="300" y="496" text-anchor="middle" font-size="10" fill="#64748b" font-family="sans-serif">4/5阶, 非刚性</text>
  
  <text x="460" y="482" text-anchor="middle" font-size="11" fill="#14532d" font-family="sans-serif">BDF (Gear)</text>
  <text x="460" y="496" text-anchor="middle" font-size="10" fill="#64748b" font-family="sans-serif">L-稳定, 1~6阶</text>
  
  <text x="620" y="482" text-anchor="middle" font-size="11" fill="#7c3aed" font-family="sans-serif">指数积分器</text>
  <text x="620" y="496" text-anchor="middle" font-size="10" fill="#64748b" font-family="sans-serif">L-稳定, 电力电子</text>
  
  <!-- Connecting lines from selection box -->
  <line x1="140" y1="440" x2="140" y2="420" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="300" y1="440" x2="300" y2="420" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="460" y1="440" x2="460" y2="420" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="620" y1="440" x2="620" y2="420" stroke="#64748b" stroke-width="1" stroke-dasharray="3,3"/>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 变步长求解器架构与工作流程</p>

### 关键数学关系汇总

**梯形法截断误差**（Carbone et al., 2002）：

对于电感元件，梯形法的视在电抗为：

$$X_{L}^{\text{APP}} = X_L \cdot \frac{1 + j}{1 - j}, \quad j = \tan\left(\frac{\omega \Delta t}{2}\right) / \left(\frac{\omega \Delta t}{2}\right)$$

相对误差为：

$$\hat{\epsilon}_X(\omega) = |j|$$

对于谐振电路，误差在谐振频率处被品质因数 $Q$ 放大：

$$\hat{\epsilon}_Z(\omega) = jQ \sqrt{\left(1 - \frac{\omega^2}{\omega_0^2}\right)^2 + \frac{1}{Q^2}\frac{\omega^2}{\omega_0^2}}$$

**指数积分器 LTE 估计**（Paull et al., 2025）：

$$\epsilon \approx \phi_{p+1}(A_k h) h^{p+1} B_k \frac{d^{(p)} u_n}{dt^{(p)}}$$

**Padé 逼近误差**（Li et al., 2020）：

$$e^{hA} - r_{k,m}(hA) = O(h^{k+m+1})$$

其中 $r_{k,m}$ 为 $(k,m)$ 阶 Padé 有理函数逼近。

**紧凑格式精度**（Tanaka & Baba, 2023）：

| 积分-插值组合 | 无开关步精度 | 开关步精度 | 稳定性 |
|-------------|------------|----------|--------|
| ExP01-L (BE + 线性插值) | $O(h^2)$ | $O(h)$ | L-稳定 |
| ExP12-Q (TR + 二次插值) | $O(h^3)$ | $O(h^2)$ | L-稳定 |
| 梯形法 + 线性插值 | $O(h^2)$ | $O(h)$ | A-稳定 |

## 关键技术挑战

### 1. 数值振荡抑制

A-稳定方法（如梯形法）在开关不连续点会产生数值振荡（fictitious oscillations），这是因为数值方法对阶跃输入的响应与真实物理响应不同——真实电感在电流突变时产生 Dirac 脉冲电压，而数值方法只能产生有限幅值的电压跳变。

**抑制策略**：
- **半步向后欧拉切换**（TR_BE / CDA）：在开关发生后的一到两步切换到向后欧拉法，提供 L 稳定性以阻尼振荡（Carbone et al., 2002）
- **插值平滑**：在开关事件处使用高阶插值替代线性插值，减少插值引入的误差（Li et al., 2020）
- **指数积分器**：利用矩阵指数的解析性质，天然抑制数值振荡（Paull et al., 2025）

### 2. 刚性系统处理

电力系统中的刚性来源于时间常数的巨大差异：电力电子开关的时间常数在纳秒级，而电网惯性时间常数在秒级。刚性比（Stiffness Ratio）定义为：

$$\sigma_{\text{stiff}} = \frac{|\lambda_{\max}|}{|\lambda_{\min}|}$$

其中 $\lambda_{\max}$ 和 $\lambda_{\min}$ 分别为系统 Jacobi 矩阵的最大和最小特征值绝对值。

当 $\sigma_{\text{stiff}} > 10^3$ 时，系统被视为刚性。刚性系统中，显式方法（如 RK45）的稳定区域有限，需要极小步长才能保持稳定，而隐式方法（如 BDF、向后欧拉）无条件稳定，可使用更大步长。

**自动刚性检测**：通过监测系统 Jacobi 矩阵的特征值分布或连续步长的误差变化率，自动判断系统刚性程度并切换积分方法。

### 3. 开关事件定位精度

开关事件定位精度直接影响仿真结果的谐波含量。定位误差 $\Delta t_d$ 导致的状态误差为：

$$\Delta x \approx \left| \frac{dx}{dt} \right| \cdot \Delta t_d$$

对于高频开关电路（如 PWM 频率 10 kHz），$\frac{dx}{dt}$ 可达 $10^6$ A/s 量级，即使 1 μs 的定位误差也会产生 1 A 的状态误差。

**高精度定位策略**：
- 利用密集输出公式提供步内多状态点（Li et al., 2020）
- 采用二次或三次 Hermite 插值替代线性插值
- 结合 DSED 框架，利用控制信号精确预测开关时刻（Paull et al., 2025）

### 4. 步长拒绝与重试开销

当 LTE 估计超出容限时，求解器需要拒绝当前步并缩小步长重试。频繁的步长拒绝会显著降低效率。

**减少拒绝的策略**：
- 更精确的误差估计（嵌入式公式 vs 单公式估计）
- 历史误差 PID 控制，避免步长震荡
- 步长变化率限制，平滑步长调整

## 量化性能边界

### 效率提升数据

| 对比方案 | 场景 | 加速比 | 来源 |
|---------|------|--------|------|
| AGEI vs Simulink (ode8, 0.1 μs) | 非刚性直流变换器 | > 8× | Paull et al., 2025 |
| AGEI vs PLECS (DOPRI) | 刚性交直流混合系统 | > 3× | Paull et al., 2025 |
| ExP12-Q vs PSCAD/EMTP | TCR 电路, 50 μs 步长 | 全局误差低 6 个数量级 | Tanaka & Baba, 2023 |
| ExP12-Q vs MEXP-L | VSC-HVDC, 20 μs 步长 | 精度相当，计算量降低 | Tanaka & Baba, 2023 |

### 精度数据

| 方法 | 阶数 | 无开关步全局误差 | 开关步全局误差 | 稳定性 |
|------|------|-----------------|---------------|--------|
| 梯形法 + 线性插值 | 2阶 | $O(h^2)$ | $O(h)$ | A-稳定 |
| 梯形法 + 二次插值 | 2阶 | $O(h^2)$ | $O(h^2)$ | A-稳定 |
| ExP01-L (BE+线性) | 1阶 | $O(h^2)$ | $O(h)$ | L-稳定 |
| ExP12-Q (TR+二次) | 3阶 | $O(h^3)$ | $O(h^2)$ | L-稳定 |
| RK45 (Dormand-Prince) | 4/5阶 | $O(h^4)$ | $O(h^4)$ | 条件稳定 |
| BDF (Gear) | 1~6阶 | $O(h^p)$ | $O(h^p)$ | L-稳定 |

### 预计算优化

| 指标 | 全步长预计算 | AGEI 自适应粒度 | 优化幅度 |
|------|------------|----------------|---------|
| 矩阵指数项数 | 99,900 | 2,700 | 降低 92% |
| 典型步长分解 | 单一固定步长 | 5.56 μs → 5 μs + 0.5 μs + 60 ns | 自适应粒度 |
| 直流输入场景 | 需多阶 $\phi$ 函数 | 项数恒为 1，LTE = 0 | 精确解析 |

（数据来源：Paull et al., 2025）

## 适用边界与选择指南

### 场景-方法推荐表

| 应用场景 | 推荐求解器 | 理由 |
|---------|-----------|------|
| 纯电力电子变换器仿真（PWM 开关） | 指数积分器 (AGEI/MEXP) | L 稳定，密集输出支持高精度事件定位，开关处精度达 3 阶 |
| 含电力电子的大规模电网仿真 | 变步长 RK45 + TR_BE 事件处理 | 非刚性区域高效，开关处阻尼振荡 |
| 刚性系统（小时间常数元件多） | BDF (Gear) 变阶 | L 稳定，自动阶数切换 |
| 高精度谐波分析 | 紧凑格式 CS (ExP12-Q) | 全局误差 $O(h^3)$，显著低于梯形法 |
| 实时仿真 | 固定步长（不适用变步长） | 变步长无法保证确定性时序 |
| 仅含直流源的变换器 | 指数积分器 (AGEI) | 强迫函数项数恒为 1，LTE = 0，精确解析 |

### 适用条件

- **离线仿真**：变步长求解器依赖误差估计和步长调整，要求计算时序可变
- **开关事件可检测**：系统需提供事件函数 $g(t)$ 或控制信号以触发事件检测
- **误差容限可定义**：用户需指定相对/绝对误差容限（通常相对容限 $10^{-3} \sim 10^{-6}$）
- **系统分段光滑**：每个开关拓扑区间内系统方程为光滑函数（线性或弱非线性）

### 失效边界

- **实时仿真**：RTDS、OPAL-RT 等实时平台要求固定步长（通常 10 ~ 100 μs），变步长无法满足确定性时序要求
- **频繁开关场景**：当开关频率极高（> 100 kHz）且占空比变化频繁时，步长调整开销可能超过收益
- **强非线性器件**：如饱和磁芯、电弧模型，其不连续特性可能导致误差估计失效
- **多时间尺度极端分离**：当刚性比 > $10^6$ 时，可能需要混合仿真（EMT + 机电暂态）而非单一变步长求解器

## 相关方法 / 相关模型 / 相关主题

- [[numerical-integration]] - 数值积分方法（变步长求解的基础）
- [[stiff-system-handling]] - 刚性系统处理（变步长求解器的关键挑战）
- [[switch-modeling]] - 开关建模（事件检测与定位的对象）
- [[trapezoidal-rule]] - 梯形积分法（最常用的固定步长方法，变步长的对比基准）
- [[interpolation-method]] - 插值方法（开关事件定位的核心技术）
- [[state-space-method]] - 状态空间法（指数积分器的输入形式）
- [[backward-euler]] - 向后欧拉法（L-稳定方法，常用于事件后阻尼振荡）
- [[runge-kutta-in-emt]] - Runge-Kutta 法在 EMT 中的应用（RK45 是经典变步长方法）
- [[dae-solvers]] - 微分代数方程求解器（电力系统 EMT 的 DAE 形式）
- [[numerical-stability]] - 数值稳定性（A-稳定、L-稳定的理论基础）
- [[compact-scheme]] - 紧凑格式（高精度积分方法，Matehkolaei et al. 2026）
- [[exponential-integrator]] - 指数积分器（状态空间 EMT 的高效求解器）
- [[variable-time-step-solver]] - 变步长求解器（本页面）
- [[adaptive-grained-exponential-integrator]] - AGEI 算法（Paull et al. 2025）

## 来源论文

- **Carbone et al., 2002** — "Analysis and estimation of truncation errors in modeling complex resonant circuits with the EMTP" (*Electrical Power and Energy Systems*, 24(3):295-304)。系统分析了 EMTP 梯形积分在谐振电路中的截断误差，建立了步长-频率-品质因数的误差解析模型，为变步长策略提供了理论依据。

- **Paull et al., 2025** — "Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter Systems" (*IEEE Transactions on Power Delivery*, 40(2):1114-1127)。提出 AGEI 算法，将指数积分器与 DSED 框架结合，通过自适应粒度预计算和变步长高阶积分，在电力电子变换器仿真中实现 > 8× 加速。

- **Li et al., 2020** — "Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs" (*Electric Power Systems Research*, 189:106714)。提出基于矩阵指数积分和密集输出公式的高阶插值方法，设计了两种 L-稳定求解器（1 阶高效型和 3 阶高精度型），解决了开关事件定位精度问题。

- **Tanaka & Baba, 2023** — "Study of a numerical integration method using the compact scheme for electromagnetic transient simulation" (*Electric Power Systems Research*, 222:109477)。研究紧凑格式（CS）在 EMT 仿真中的应用，提出积分-插值匹配策略（ExP01-L 和 ExP12-Q），在 TCR 和 VSC-HVDC 算例中验证了 3 阶全局精度。

- **Matehkolaei et al., 2026** — "Compact scheme challenges in EMT-Type simulations" (*Electric Power Systems Research*, 252:112403)。分析紧凑格式在开关不连续点的异常行为，提出 CS_BE 混合格式解决不连续性问题，在 MANA 框架下推导了 CS 的网路方程离散化。

- **Hairer, E. & Wanner, G.** — "Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems" (*Springer*, 1996)。变步长 ODE 求解的经典理论著作，系统阐述了嵌入式 Runge-Kutta 法、BDF 法、误差控制和步长选择策略。

- **Shampine, L. F. & Reichelt, M. W.** — "The MATLAB ODE Suite" (*SIAM Journal on Scientific Computing*, 18(1):1-22, 1997)。介绍了 ode45 (Dormand-Prince RK45) 和 ode15s (变阶 BDF) 的实现细节，是变步长求解器工程实现的重要参考。

- **Zhang et al., 2023** — "An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration" (*IEEE Transactions on Power Delivery*)。提出 MMC 的混合数值积分建模方法，结合中点法和梯形法，将 MMC 离散化为恒定电导的 Norton 等效电路。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy--16|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[huang-等-a-heterogeneous-multiscale-method-for-efficient-simulation-of-power-syst|Huang 等 | A Heterogeneous Multiscale Method for Efficient Si]] | 2025 |

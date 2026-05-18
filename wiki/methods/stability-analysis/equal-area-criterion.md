---
title: "等面积法则 (Equal Area Criterion)"
type: method
tags: [equal-area, stability, transient, swing-equation, direct-method, single-machine, power-angle, cct, critical-clearing]
created: "2026-05-02"
updated: "2026-05-18"
---

# 等面积法则 (Equal Area Criterion)

## 定义与边界

等面积法则（Equal Area Criterion, EAC）是用于单机无穷大系统或可严格化为等效两机系统的暂态功角稳定直接判据。它把 [[swing-equation]] 中的功率不平衡积分解释为转子动能变化，通过比较故障期间的**加速面积**（$A_{\mathrm{acc}}$）和故障切除后的**可用减速面积**（$A_{\mathrm{dec,max}}$）判断首摆稳定边界。当 $A_{\mathrm{acc}} < A_{\mathrm{dec,max}}$ 时系统首摆稳定，临界状态下 $A_{\mathrm{acc}} = A_{\mathrm{dec,max}}$。

本页讨论方法本身，不把 EAC 写成通用多机稳定算法。复杂多机系统、励磁限幅、动态负荷、电力电子限流、保护动作和电压稳定问题需要通过 [[transient-stability-analysis]]、[time-domain-simulation] 或 [[eeac]] 等扩展/验证流程处理。

EAC 的核心假设：**单机无穷大总线束、恒定内电势、简化正弦功率角关系、故障期间机械功率短时恒定**。这些假设在经典电力系统教材和首摆稳定性快速评估中是合理的，但现代电力电子并网场景下可能不再成立。

## EMT 中的作用

EAC 在 EMT 研究中的主要价值是提供功角稳定的**机制解释**和**低维校核**，而不是替代 EMT 波形仿真。EMT 或 EMT-TS 混合仿真可给出故障期间的电磁功率、切除角、限幅状态和保护动作；EAC 可用于解释这些结果中"加速能量是否能被切除后网络吸收"。

EMT 仿真与 EAC 的互补关系：

| EMT 仿真提供 | EAC 提供 |
|-------------|----------|
| 逐点电磁功率轨迹 $P_e(\delta,t)$ | 面积积分的解析/数值结果 |
| 故障切除时间 $t_c$（精确） | 临界切除时间 CCT 的估算 |
| 限流、HVDC 控制、饱和动态 | 能量裕度的定性判断 |
| 多摆失稳轨迹 | 首摆稳定边界的快速判据 |

若 EMT 细节显著改变 $P_e(\delta)$，例如换流器限流改变电磁功率表达、故障不平衡导致正序等效不充分，EAC 只能作为**解释框架**，不能作为独立判据。

## 核心机制

### 基础摇摆方程

单机无穷大系统的经典摇摆方程可写为：

$$M\frac{d^2\delta}{dt^2} = P_m - P_e(\delta) \tag{1}$$

其中 $M$ 是等效惯性时间常数（标幺制下 $M = 2H/\omega_0$），$\delta$ 是功角（转子 q 轴与无穷大总线电压的夹角），$P_m$ 是机械输入功率（pu），$P_e$ 是电磁输出功率。令 $\omega = d\delta/dt$，两边乘以 $\omega$ 并积分，得到能量形式的积分关系：

$$\frac{1}{2}M(\omega^2 - \omega_0^2) = \int_{\delta_0}^{\delta}(P_m - P_e(\alpha))\,d\alpha \tag{2}$$

式 (2) 的物理含义：**转子动能变化等于功率不平衡对功角的积分**。这正是 EAC 的数学起点。

### 面积法则的图形推导

将故障期间和故障切除后的功率-功角 $(P-\delta)$ 曲线画在同一坐标系中，图上两块面积对应能量关系：

**故障期间的加速面积**：

$$A_{\mathrm{acc}} = \int_{\delta_0}^{\delta_c}(P_m - P_e^{\mathrm{fault}}(\delta))\,d\delta \tag{3}$$

**故障切除后的最大减速面积**：

$$A_{\mathrm{dec,max}} = \int_{\delta_c}^{\delta_u}(P_e^{\mathrm{post}}(\delta) - P_m)\,d\delta \tag{4}$$

其中各角度的物理含义：

| 符号 | 名称 | 物理含义 |
|------|------|----------|
| $\delta_0$ | 故障前功角 | 故障前稳态运行点，满足 $P_m = P_e(\delta_0)$ |
| $\delta_c$ | 故障切除角 | 故障被切除瞬间的转子角度 |
| $\delta_u$ | 不稳定平衡角 | 故障后功率曲线与 $P=P_m$ 的不稳定交点，满足 $P_e^{\mathrm{post}}(\delta_u) = P_m$ 且 $\frac{dP_e^{\mathrm{post}}}{d\delta}\bigg|_{\delta_u} > 0$ |

首摆稳定的**理想判据**：

$$A_{\mathrm{acc}} < A_{\mathrm{dec,max}} \tag{5}$$

临界状态下面积相等：

$$A_{\mathrm{acc}} = A_{\mathrm{dec,max}} \tag{5'}$$

### 经典正弦功率角关系下的解析解

若采用经典正弦功率角关系：

$$P_e = P_{\max}\sin\delta \tag{6}$$

则不稳定平衡角有解析表达式：

$$\delta_u = \pi - \arcsin\!\left(\frac{P_m}{P_{\max}^{\mathrm{post}}}\right) \tag{7}$$

临界切除角的解析形式（故障期间功率曲线与故障后曲线不同时需数值积分，但 $\delta_u$ 可解析求得）。在简单三段线性功率曲线（故障前/故障中/故障后）下，加速面积和减速面积可分别化为三角函数组合，$\delta_{cr}$ 可通过数值求解超越方程获得。

**临界切除时间（CCT）**：先由面积相等求出 $\delta_{cr}$，再由故障期间轨迹 $\delta(t)$ 反求临界切除时间 $t_{cr}$。注意 CCT 不是系统常数——它绑定于故障位置、故障类型、切除拓扑、 EMT 模型和数值积分设置。

### 关键假设汇总

EAC 解析推导依赖以下强假设，任何一条不成立时面积解释需降级为近似或失效：

$$P_e(\delta) = P_{\max}\sin\delta \quad \text{（恒定内电势、简化电抗、无饱和）}$$

$$P_m = \text{const} \quad \text{（故障期间机械功率短时不变）}$$

$$E = \text{const} \quad \text{（故障期间内电势恒定）}$$

$$\omega \approx \omega_0 \quad \text{（积分时近似同步速）}$$

$$\text{阻尼} \approx 0 \quad \text{（弱阻尼假设）}$$

## 分类与变体

### 经典单机无穷大 EAC

适用于教材级故障前、故障中、故障后三条功率角曲线分析。是 EAC 的原始形式，也是所有扩展变体的理论基础。典型场景：三相短路故障叠加于单机无穷大总线，研究故障清除时间与稳定裕度的关系。

### 两机等效 EAC

把两台机或两个等效机群的相对运动写成等效单自由度问题。本质上与单机无穷大 EAC 相同，但参数通过两机等效变换得到。适用范围：两群失稳模式主导的多机系统，其中一群可合并为等效机。

### 临界切除角/时间计算

先用面积相等求 $\delta_{cr}$，再由故障期间轨迹 $\delta(t)$ 反求临界切除时间 $t_{cr}$：

$$t_{cr} = t(\delta_{cr}); \quad \delta(t) \text{ 由数值积分 (1) 求得} \tag{8}$$

注意：时间结果必须绑定故障、模型和数值积分设置；同一系统在 EMT 中用详细开关模型与用平均值模型得到的 $\delta(t)$ 不同，CCT 也会不同。

### 多机扩展路线

[[eeac]] 和 SIME 类方法通过机群识别构造 OMIB（等效单机无穷大）等效，再在等效系统上使用面积判据。具体见 [[eeac]] 页面详细推导。

### 能量函数联系

[[energy-function]] 从更一般的能量裕度角度处理稳定边界，EAC 可视为单自由度无阻尼情形下的图形化能量判据。EAC 的面积裕度 $\Delta A = A_{\mathrm{dec,max}} - A_{\mathrm{acc}}$ 与能量函数法的能量裕度 $\Delta V = V_{cr} - V_{cl}$ 在数学上同构。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 720 480" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="720" height="480" fill="#ffffff"/>
  
  <!-- Grid lines -->
  <line x1="80" y1="400" x2="680" y2="400" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="80" y1="100" x2="80" y2="400" stroke="#e0e0e0" stroke-width="1"/>
  
  <!-- Title -->
  <text x="360" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="15" font-weight="bold" fill="#333">图1 · EAC 面积法则示意图（单机无穷大系统）</text>
  
  <!-- Axes -->
  <line x1="80" y1="400" x2="680" y2="400" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="80" y1="420" x2="80" y2="80" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="690" y="390" font-family="Arial,sans-serif" font-size="13" fill="#333">δ (rad)</text>
  <text x="60" y="75" font-family="Arial,sans-serif" font-size="13" fill="#333">P</text>
  <text x="90" y="415" font-family="Arial,sans-serif" font-size="11" fill="#666">0</text>
  <text x="335" y="415" font-family="Arial,sans-serif" font-size="11" fill="#666">π/2</text>
  <text x="580" y="415" font-family="Arial,sans-serif" font-size="11" fill="#666">π</text>
  
  <!-- Arrow marker def -->
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#333"/></marker></defs>
  
  <!-- Fault-before curve: P = Pmax * sin(delta) -->
  <!-- delta_0 at arcsin(Pm/Pmax), which is ~0.4 rad for Pm=0.8, Pmax=1.0 -->
  <!-- Pmax = 1.0 pu, Pm = 0.8 pu, so delta_0 = arcsin(0.8) ≈ 0.927 rad -->
  <!-- delta_c = 1.4 rad (fault clearing angle) -->
  <!-- delta_u = π - arcsin(0.8) ≈ 2.214 rad -->
  <!-- Fault curve: higher Pmax = 1.2, post curve: Pmax = 1.0 -->
  
  <!-- Fault-after curve: P_post = 1.0 * sin(delta) -->
  <path d="M 80,400 Q 200,150 376,240 Q 480,300 590,350 Q 640,375 665,385" fill="none" stroke="#2563eb" stroke-width="2.5"/>
  
  <!-- Fault-during curve: higher Pmax = 1.4 -->
  <path d="M 80,400 Q 200,80 376,180 Q 480,240 590,310 Q 640,340 665,360" fill="none" stroke="#dc2626" stroke-width="2.5"/>
  
  <!-- Horizontal line P = Pm = 0.8 -->
  <line x1="80" y1="300" x2="665" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="5,3"/>
  
  <!-- Area fills -->
  <!-- A_acc = integral from delta_0 to delta_c of (Pm - P_fault) -->
  <!-- This is the area between P_fault curve and Pm horizontal line, from delta_0 to delta_c -->
  <!-- P_fault at delta_0=0.927: 1.4*sin(0.927)=1.4*0.801=1.12, above Pm=0.8 -->
  <!-- P_fault at delta_c=1.4: 1.4*sin(1.4)=1.4*0.985=1.38, above Pm=0.8 -->
  <!-- Shade A_acc (red) -->
  <path d="M 376,300 Q 200,80 376,180 Q 480,240 510,255 L 510,300 L 376,300 Z" fill="#fee2e2" fill-opacity="0.7" stroke="none"/>
  
  <!-- A_dec = integral from delta_c to delta_u of (P_post - Pm) -->
  <!-- P_post at delta_c=1.4: 1.0*sin(1.4)=0.985, above Pm=0.8 -->
  <!-- P_post at delta_u=2.214: 1.0*sin(2.214)=0.8 (=Pm, at the intersection) -->
  <!-- Shade A_dec (green) -->
  <path d="M 510,255 L 560,295 Q 580,302 595,308 L 590,300 L 510,300 Z" fill="#dcfce7" fill-opacity="0.7" stroke="none"/>
  
  <!-- Vertical lines for key angles -->
  <line x1="376" y1="400" x2="376" y2="290" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="376" y="430" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">δ₀</text>
  
  <line x1="510" y1="400" x2="510" y2="290" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="510" y="430" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">δc</text>
  
  <line x1="595" y1="400" x2="595" y2="295" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="595" y="430" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">δu</text>
  
  <!-- Labels for curves -->
  <text x="600" y="170" font-family="Arial,sans-serif" font-size="12" fill="#dc2626" font-weight="bold">故障中 P_e^fault</text>
  <text x="600" y="230" font-family="Arial,sans-serif" font-size="12" fill="#2563eb" font-weight="bold">故障后 P_e^post</text>
  <text x="660" y="295" font-family="Arial,sans-serif" font-size="12" fill="#333">P_m</text>
  
  <!-- Area labels -->
  <text x="440" y="270" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#dc2626">A_acc</text>
  <text x="555" y="270" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#16a34a">A_dec</text>
  
  <!-- Legend box -->
  <rect x="480" y="80" width="180" height="90" rx="4" fill="#f9f9f9" stroke="#ccc" stroke-width="1"/>
  <text x="570" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#333">图例</text>
  <rect x="495" y="108" width="20" height="10" fill="#fee2e2"/>
  <text x="522" y="117" font-family="Arial,sans-serif" font-size="10" fill="#333">加速面积 A_acc</text>
  <rect x="495" y="125" width="20" height="10" fill="#dcfce7"/>
  <text x="522" y="134" font-family="Arial,sans-serif" font-size="10" fill="#333">减速面积 A_dec</text>
  <line x1="495" y1="148" x2="515" y2="148" stroke="#dc2626" stroke-width="2"/>
  <text x="522" y="152" font-family="Arial,sans-serif" font-size="10" fill="#333">故障中功率曲线</text>
  <line x1="495" y1="162" x2="515" y2="162" stroke="#2563eb" stroke-width="2"/>
  <text x="522" y="166" font-family="Arial,sans-serif" font-size="10" fill="#333">故障后功率曲线</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EAC面积法则示意图（经典正弦功率角模型）</p>

## 形式化表达

### 核心判据汇总

**摇摆方程**（以惯性常数 $H$ 表示）：

$$\frac{2H}{\omega_0}\frac{d^2\delta}{dt^2} = P_m - P_e(\delta) \tag{1'}$$

**能量积分形式**：

$$\frac{1}{2}M\omega^2 = \int_{\delta_0}^{\delta}(P_m - P_e(\alpha))\,d\alpha + C \tag{2'}$$

**面积稳定判据**：

$$A_{\mathrm{acc}} < A_{\mathrm{dec,max}} \tag{5}$$

**临界切除角（经典正弦模型）**：

$$\delta_{cr} = \arcsin\!\left(\frac{P_m}{P_{\max}^{\mathrm{post}}}\right) + \frac{P_{\max}^{\mathrm{post}} - P_{\max}^{\mathrm{fault}}}{P_{\max}^{\mathrm{post}}}\cos(\delta_0) \cdot (\cdots) \quad \text{（需数值求解）} \tag{9}$$

### 两机等效变换

临界群 $C$ 与非临界群 $N$ 的相对运动可写为等效 OMIB 方程：

$$M_{eq}\frac{d^2\delta_{eq}}{dt^2} = P_{m,eq} - P_{e,eq}(\delta_{eq}) \tag{10}$$

其中：

$$M_{eq} = \frac{M_C M_N}{M_C + M_N}, \quad \delta_{eq} = \delta_C - \delta_N \tag{11}$$

$$P_{m,eq} = P_m^C - P_m^N, \quad P_{e,eq} = \frac{M_N P_e^C - M_C P_e^N}{M_C + M_N} \tag{12}$$

### 稳定裕度

面积裕度（等价于能量函数法的 $\Delta V$）：

$$\eta = \frac{A_{\mathrm{dec,max}} - A_{\mathrm{acc}}}{A_{\mathrm{dec,max}} \tag{13}$$

$\eta > 0$ 表示稳定，$\eta = 0$ 对应临界稳定，$\eta < 0$ 表示失稳。

## 关键技术挑战

### 挑战一：恒定内电势假设失效

当同步机励磁系统有强励动作、或故障期间机端电压大幅跌落时，内电势 $E$ 不再恒定，$P_e = \frac{EV}{X}\sin\delta$ 中的 $E$ 是时变的。此时 EAC 面积解释给出的是"假设 $E$ 恒定下的判据"，与实际 EMT 轨迹可能存在显著偏差。

**应对方向**：在 EMT 仿真后处理中使用实际 $P_e(t)$ 轨迹做面积积分，不假设正弦形式。这是联结 EAC 和 EMT 的最直接方式。

### 挑战二：多摆失稳与机群重组

EAC 面积判据只判定首摆稳定性。若故障切除后系统在第二摆或后续摆次失稳（多摆失稳），或故障期间机群结构发生变化（机群重组），EAC 无法预判。EMT 详细仿真或 [[transient-stability-analysis]] 中的时域轨迹是唯一可靠手段。

**应对方向**：在 [[transient-stability-analysis]] 框架下，用时域仿真的多摆轨迹补充 EAC 的首摆判据。[[eeac]] 的动态分群变体可部分处理机群重组。

### 挑战三：阻尼与调速的面积修正

阻尼转矩 $D\frac{d\delta}{dt}$ 在 EAC 推导中被忽略。当系统阻尼较强时，实际减速面积 $A_{\mathrm{dec}}$ 小于理想值（阻尼消耗部分势能），EAC 可能高估稳定裕度。

**应对方向**：在 EMT 混合仿真中，[[swing-equation]] 页面给出了含阻尼的摇摆方程。修正方法之一是在面积积分中加入等效阻尼能量耗散项：

$$\Delta E_D = \int_{\delta_c}^{\delta} D\omega(\alpha)\,d\alpha \tag{14}$$

### 挑战四：电力电子并网的功率曲线畸变

对于含 VSC-HVDC 或 Grid-Forming Inverter 的系统，电磁功率 $P_e(\delta)$ 不再是简单正弦形式。变流器限流、PQ 控制外环响应、虚拟同步控制等因素使 $P_e(\delta)$ 曲线出现饱和、折线或不唯一对应等复杂特征，面积法则的"加速/减速面积"图形可能无法定义。

**应对方向**：这类场景下 EAC 退化为定性解释工具，[[time-domain-simulation]] 是定量分析的唯一手段。

### 挑战五：CCT 对模型和数值设置的敏感性

临界切除时间 CCT 不能作为系统常数报告。同一个网络拓扑，用 EMT 详细开关模型与用平均值等效模型得到的 CCT 可能相差 20%~50%，因为两种模型下的 $P_e(\delta,t)$ 轨迹不同。

**应对方向**：报告 CCT 时必须同时说明：故障类型、切除拓扑、所用 EMT 模型、积分步长、数值阻尼设置。不同研究之间比较 CCT 时需在相同条件下进行。

## 量化性能边界

EAC 作为直接法，其**精度**主要由以下因素决定：

| 因素 | 对 EAC 精度的影响 |
|------|-------------------|
| 经典单机模型（无阻尼、恒 $E$、恒 $P_m$） | 理论精确（与时域数值积分等价） |
| 含阻尼/调速 | 近似；误差随阻尼强度增大而增加 |
| 励磁系统饱和（$E$ 变化） | 近似；需用实际 $E(t)$ 修正面积 |
| 多机等效（OMIB 变换） | 近似；误差随机群识别精度变化 |
| 电力电子并网（$P_e$ 曲线畸变） | 面积概念可能失效 |
| 故障切除后网络结构变化 | 需分区段定义面积 |

**典型 CCT 范围**（以经典单机系统三相短路为例，数值参考典型电力系统参数）：

- $P_m = 0.8~\mathrm{pu}$，$P_{\max}^{\mathrm{post}} = 1.0~\mathrm{pu}$ 时，临界 $\delta_{cr} \approx 70^\circ \sim 90^\circ$
- 对应 CCT 约为几个周波（50Hz 系统下 $0.1\sim 0.3~\mathrm{s}$），具体数值与 $H$ 和 $P_{\max}$ 成正比
- **原文未报告可核验的数值结果**：上述数值为典型参数下的估算值，非特定论文的实验数据

## 适用边界与选择指南

### EAC 适用场景

- 单机无穷大系统的首摆功角稳定快速评估
- 经典电力系统教材中的教学演示（故障前三段功率曲线分析）
- 与时域仿真联合使用（EMT 提供轨迹，EAC 提供解释）
- 作为 [[eeac]] 和 [[energy-function]] 的理论基础

### EAC 不适用/受限场景

- 多机系统（需 OMIB 等效变体，误差不可忽略）
- 强阻尼系统（阻尼能量耗散使面积法高估裕度）
- 励磁/调速/PSS 显著改变 $P_e(\delta)$ 动态
- 换流器限流、HVDC 控制、Grid-Forming 并网场景
- 多摆失稳和机群重组过程
- 不平衡故障（序网耦合使 $P_e(\delta)$ 复杂化）

### 方法选择对照

| 场景 | 推荐方法 |
|------|----------|
| 单机/等效两机首摆稳定快速评估 | EAC（经典） |
| 多机系统首摆稳定 | [[eeac]]（静态/动态分群） |
| 多摆稳定、详细 EMT 轨迹 | [[transient-stability-analysis]]（时域仿真） |
| 任意扰动类型下的稳定裕度 | [[energy-function]]（PEBS/UEP/BCU） |
| 电力电子并网系统 | [[time-domain-simulation]]（EMT 详细仿真） |
| 需要 CCT 精确值 | EMT 时域仿真 + CCT 搜索算法 |

## 相关方法与相关模型

- [[swing-equation]]：EAC 的基础动力学方程，提供转子运动方程和状态空间形式
- [[transient-stability]]：定义功角暂态稳定概念
- [[transient-stability-analysis]]：说明 EAC 与时域法、CCT 搜索和混合仿真的关系
- [[energy-function]]：更一般的直接法框架，包含 PEBS、UEP、BCU 等临界能量计算方法
- [[eeac]]：把 EAC 扩展到机群等效后的多机问题，含静态/动态分群变体和稳定裕度计算
- [[time-domain-simulation]]：用于生成 EAC 无法覆盖的完整非线性轨迹（多摆、高频、 EMT 细节）
- [[electromechanical-transient]]：提供 EAC 所在机电暂态时间尺度的上下文
- [[power-flow-calculation]]：EAC 初始化所需的稳态运行点（$\delta_0$，$P_m$）由潮流计算给出
---
title: "旋转电机建模 (Rotating Machine Modeling)"
type: topic
tags: [rotating-machine, synchronous-machine, induction-machine, dfig, pmsm, park-transform, vbr, phase-domain]
created: "2026-05-01"
book-chapter: "6"
---

# 旋转电机建模 (Rotating Machine Modeling)

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1: Physical Input (Blue) -->
  <rect x="10" y="10" width="880" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="20" y="35" font-family="Arial" font-size="14" font-weight="bold" fill="#1e40af">第一层：物理系统（输入层）</text>
  <rect x="20" y="45" width="130" height="35" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="30" y="67" font-family="Arial" font-size="12" fill="#1e40af">同步电机</text>
  <rect x="165" y="45" width="160" height="35" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="175" y="67" font-family="Arial" font-size="12" fill="#1e40af">感应电机 (IM)</text>
  <rect x="340" y="45" width="160" height="35" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="350" y="67" font-family="Arial" font-size="12" fill="#1e40af">双馈感应发电机 DFIG</text>
  <rect x="515" y="45" width="160" height="35" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="525" y="67" font-family="Arial" font-size="12" fill="#1e40af">永磁同步电机 PMSM</text>
  <rect x="690" y="45" width="180" height="35" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="700" y="67" font-family="Arial" font-size="12" fill="#1e40af">其他特殊电机</text>

  <!-- Arrow 1→2 -->
  <line x1="450" y1="90" x2="450" y2="120" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333"/></marker></defs>

  <!-- Layer 2: Coordinate Systems (Green) -->
  <rect x="10" y="120" width="880" height="90" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="20" y="145" font-family="Arial" font-size="14" font-weight="bold" fill="#166534">第二层：坐标变换与建模框架</text>
  <rect x="20" y="155" width="260" height="45" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="30" y="175" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">dq0 旋转坐标系</text>
  <text x="30" y="190" font-family="Arial" font-size="11" fill="#166534">Park变换 · 时变电感→常数</text>
  <rect x="295" y="155" width="260" height="45" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="305" y="175" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">abc 相域 (Phase-Domain)</text>
  <text x="305" y="190" font-family="Arial" font-size="11" fill="#166534">直接三相 · 无坐标变换 · 不对称</text>
  <rect x="570" y="155" width="310" height="45" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="580" y="175" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">dq/abc 混合坐标 (VBR)</text>
  <text x="580" y="190" font-family="Arial" font-size="11" fill="#166534">abc接口定子 · dq转子动态</text>

  <!-- Arrow 2→3 -->
  <line x1="450" y1="210" x2="450" y2="240" stroke="#333" stroke-width="2" marker-end="url(#arrow2)"/>
  <defs><marker id="arrow2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333"/></marker></defs>

  <!-- Layer 3: EMT Modeling Methods (Yellow) -->
  <rect x="10" y="240" width="880" height="110" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="20" y="265" font-family="Arial" font-size="14" font-weight="bold" fill="#92400e">第三层：EMT 建模方法</text>
  <rect x="20" y="275" width="200" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="30" y="295" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">dq0 模型 (EMTP Type-59)</text>
  <text x="30" y="310" font-family="Arial" font-size="10" fill="#78350f">节点分析·梯形积分</text>
  <text x="30" y="325" font-family="Arial" font-size="10" fill="#78350f">恒导纳接口·计算效率高</text>
  <rect x="235" y="275" width="200" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="245" y="295" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">相域模型 (PD)</text>
  <text x="245" y="310" font-family="Arial" font-size="10" fill="#78350f">恒定等效导纳·无需阻尼绕组</text>
  <text x="245" y="325" font-family="Arial" font-size="10" fill="#78350f">E-PD模型 (Wang 2019)</text>
  <rect x="450" y="275" width="200" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="460" y="295" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">VBR 模型</text>
  <text x="460" y="310" font-family="Arial" font-size="10" fill="#78350f">电压源+电抗·数值稳定</text>
  <text x="460" y="325" font-family="Arial" font-size="10" fill="#78350f">非迭代同步接口</text>
  <rect x="665" y="275" width="205" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="675" y="295" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">磁路等效模型</text>
  <text x="675" y="310" font-family="Arial" font-size="10" fill="#78350f">dq/dq分解·磁动势映射</text>
  <text x="675" y="325" font-family="Arial" font-size="10" fill="#78350f">Yonezawa 2023</text>

  <!-- Arrow 3→4 -->
  <line x1="450" y1="350" x2="450" y2="380" stroke="#333" stroke-width="2" marker-end="url(#arrow3)"/>
  <defs><marker id="arrow3" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333"/></marker></defs>

  <!-- Layer 4: EMT Analysis (Purple) -->
  <rect x="10" y="380" width="880" height="60" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="20" y="405" font-family="Arial" font-size="14" font-weight="bold" fill="#5b21b6">第四层：EMT 分析场景与接口</text>
  <rect x="20" y="415" width="170" height="18" rx="3" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="30" y="428" font-family="Arial" font-size="11" fill="#5b21b6">故障分析（短路电流）</text>
  <rect x="205" y="415" width="170" height="18" rx="3" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="215" y="428" font-family="Arial" font-size="11" fill="#5b21b6">新能源并网暂态</text>
  <rect x="390" y="415" width="170" height="18" rx="3" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="400" y="428" font-family="Arial" font-size="11" fill="#5b21b6">机电混合仿真</text>
  <rect x="575" y="415" width="170" height="18" rx="3" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="585" y="428" font-family="Arial" font-size="11" fill="#5b21b6">谐波与不对称分析</text>
  <rect x="760" y="415" width="120" height="18" rx="3" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="770" y="428" font-family="Arial" font-size="11" fill="#5b21b6">实时仿真</text>

  <!-- Arrow 4→5 -->
  <line x1="450" y1="440" x2="450" y2="465" stroke="#333" stroke-width="2" marker-end="url(#arrow4)"/>
  <defs><marker id="arrow4" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333"/></marker></defs>

  <!-- Layer 5: Output (Red) -->
  <rect x="10" y="465" width="880" height="45" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="20" y="490" font-family="Arial" font-size="14" font-weight="bold" fill="#991b1b">量化性能边界</text>
  <rect x="180" y="475" width="200" height="28" rx="4" fill="#fecaca" stroke="#dc2626" stroke-width="1"/>
  <text x="190" y="490" font-family="Arial" font-size="11" fill="#991b1b">dq0模型：步长 50μs / 误差 &lt;0.1%</text>
  <rect x="395" y="475" width="200" height="28" rx="4" fill="#fecaca" stroke="#dc2626" stroke-width="1"/>
  <text x="405" y="490" font-family="Arial" font-size="11" fill="#991b1b">VBR模型：步长 500μs / 效率↑660%</text>
  <rect x="610" y="475" width="265" height="28" rx="4" fill="#fecaca" stroke="#dc2626" stroke-width="1"/>
  <text x="620" y="490" font-family="Arial" font-size="11" fill="#991b1b">E-PD模型：无需人工阻尼绕组 / 效率与dq0相当</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 旋转电机 EMT 建模五层架构：物理输入 → 坐标变换 → 建模方法 → 分析场景 → 量化输出</p>

## 概述

旋转电机是电力系统中最核心的机电能量转换设备，包括同步电机（发电机）、感应电机（电动机/负荷）、永磁同步电机（PMSM）、双馈感应发电机（DFIG）等类型。在EMT仿真中，旋转电机建模面临独特挑战：需要同时处理电磁暂态（微秒级）和机电暂态（毫秒至秒级）的时间尺度差异，处理转子运动方程与电磁方程的耦合，以及准确表征磁路饱和、阻尼效应等非线性特性。

EMT语境下的旋转电机建模与机电暂态仿真（TS）有本质区别：EMT需要显式建模定子绕组暂态（忽略定子暂态是TS的典型简化），处理dq0坐标变换带来的时变电感，解决数值稳定性问题（VBR方法），以及实现与电力电子变流器的准确接口（新能源并网场景）。

## 作用机制

### 6.1 同步电机EMTP型建模

**坐标系选择与变换**

同步电机EMT建模的核心是Park变换，将三相abc坐标系转换到与转子同步旋转的dq0坐标系：

$$\begin{bmatrix} i_d \\ i_q \\ i_0 \end{bmatrix} = \frac{2}{3}\begin{bmatrix} \cos\theta & \cos(\theta-120^\circ) & \cos(\theta+120^\circ) \\ -\sin\theta & -\sin(\theta-120^\circ) & -\sin(\theta+120^\circ) \\ 1/2 & 1/2 & 1/2 \end{bmatrix}\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$

**电压方程**

定子电压方程（dq0坐标系）：

$$\begin{aligned} v_d &= -R_s i_d - \omega\psi_q + \frac{d\psi_d}{dt} \\ v_q &= -R_s i_q + \omega\psi_d + \frac{d\psi_q}{dt} \\ v_0 &= -R_s i_0 + \frac{d\psi_0}{dt} \end{aligned}$$

转子绕组电压方程：

$$\begin{aligned} v_{fd} &= R_{fd} i_{fd} + \frac{d\psi_{fd}}{dt} \\ 0 &= R_{kd} i_{kd} + \frac{d\psi_{kd}}{dt} \\ 0 &= R_{kq} i_{kq} + \frac{d\psi_{kq}}{dt} \end{aligned}$$

**磁链方程**

$$\begin{bmatrix} \psi_d \\ \psi_q \\ \psi_{fd} \\ \psi_{kd} \\ \psi_{kq} \end{bmatrix} = \begin{bmatrix} L_d & 0 & L_{ad} & L_{ad} & 0 \\ 0 & L_q & 0 & 0 & L_{aq} \\ L_{ad} & 0 & L_{fd} & L_{ad} & 0 \\ L_{ad} & 0 & L_{ad} & L_{kd} & 0 \\ 0 & L_{aq} & 0 & 0 & L_{kq} \end{bmatrix}\begin{bmatrix} i_d \\ i_q \\ i_{fd} \\ i_{kd} \\ i_{kq} \end{bmatrix}$$

**转子运动方程**

$$J\frac{d\omega_r}{dt} = T_m - T_e - D\omega_r, \quad \frac{d\delta}{dt} = \omega_r - \omega_s$$

### 6.2 相域模型：直接abc坐标建模

**核心思想**

直接在abc三相坐标系下建模，无需Park变换，避免时变电感问题。

**电压方程**

$$v_{abc} = R_s i_{abc} + \frac{d\psi_{abc}}{dt}$$

**磁链方程**

$$\psi_{abc} = L_{abc}(\theta)i_{abc} + \psi_{abc,r}$$

其中电感矩阵 $L_{abc}(\theta)$ 是转子位置角 $\theta$ 的函数。

**恒定等效导纳技术（E-PD模型，Wang 2019）**

为保持EMTP节点导纳矩阵恒定，采用方程重构：

$$Y_{eq}v_{abc} = i_{inj} - i_{hist}$$

其中等效导纳 $Y_{eq}$ 不随转子位置变化。E-PD模型通过把转子位置相关项从诺顿导纳中转移到受控电流源/历史项，使电机对网络呈现"恒定诺顿导纳并联受控电流源"，同时减少电机内部每步计算量。

**相域模型优势**

| 特性 | dq0模型 | 相域模型 |
|------|---------|---------|
| 坐标变换 | 需要 | 不需要 |
| 时变电感 | 无 | 需要特殊处理 |
| 不对称工况 | 受限 | 适合 |
| 谐波分析 | 受限 | 准确 |
| 计算效率 | 高 | 中 |

### 6.3 电压Behind-Reactance(VBR)模型

**核心思想**

通过电路等效变换，将电机表示为电压源串联电抗的形式，提高数值稳定性。

**等效电路**

$$v_{abc} = e''_{abc} - X''_d i_{abc}$$

其中 $e''_{abc}$ 为次暂态电势，$X''_d$ 为次暂态电抗。

**VBR模型优势**

- 恒导纳矩阵：等效导纳不随转子位置变化
- 数值稳定性：避免dq模型在EMT中的数值问题
- 接口友好：易于与外部网络直接连接

**dq/abc混合坐标离散化**

1. 内部状态变量使用dq坐标（简化方程）
2. 网络接口使用abc坐标（直接连接）
3. 通过变换矩阵实时转换

VBR-EMTP形式把"对网络友好的abc端口"和"对机器动态友好的dq转子状态"结合起来，在同一节点分析步内求解网络变量与机器电气变量，而不是用上一时步电压或反复预测校正来闭合接口（Wang 2010）。

### 6.4 异步电机（感应电机）建模

**双笼转子模型**

$$\begin{bmatrix} v_{ds} \\ v_{qs} \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} R_s & 0 & 0 & 0 & 0 & 0 \\ 0 & R_s & 0 & 0 & 0 & 0 \\ 0 & 0 & R_{r1} & 0 & 0 & 0 \\ 0 & 0 & 0 & R_{r1} & 0 & 0 \\ 0 & 0 & 0 & 0 & R_{r2} & 0 \\ 0 & 0 & 0 & 0 & 0 & R_{r2} \end{bmatrix}\begin{bmatrix} i_{ds} \\ i_{qs} \\ i_{dr1} \\ i_{qr1} \\ i_{dr2} \\ i_{qr2} \end{bmatrix} + \frac{d}{dt}\begin{bmatrix} \psi_{ds} \\ \psi_{qs} \\ \psi_{dr1} \\ \psi_{qr1} \\ \psi_{dr2} \\ \psi_{qr2} \end{bmatrix} + \begin{bmatrix} -\omega\psi_{qs} \\ \omega\psi_{ds} \\ -(\omega-\omega_r)\psi_{qr1} \\ (\omega-\omega_r)\psi_{dr1} \\ -(\omega-\omega_r)\psi_{qr2} \\ (\omega-\omega_r)\psi_{dr2} \end{bmatrix}$$

**深槽效应（Deep Bar Effect）**

考虑转子导条集肤效应，转子电阻和漏感随转差率变化：

$$R_r(s) = R_{r0}K_R(s), \quad L_{lr}(s) = L_{lr0}K_L(s)$$

**转矩方程**

$$T_e = \frac{3}{2}p(\psi_{ds}i_{qs} - \psi_{qs}i_{ds}) = \frac{3}{2}pL_m(i_{qs}i_{dr} - i_{ds}i_{qr})$$

**节点缩减感应电机模型（NR模型，Nodal Reduced）**

NR-CF（current-flux）和NR-CC（current-current）通过节点缩减消去内部变量，只保留定子端口对外，外部网络看到的是一个与普通三相元件类似的端口模型。

### 6.5 通用电机建模范式

**统一建模框架**

各类旋转电机可采用统一的EMT建模框架：

1. **电气方程**：电磁感应定律 + 电路约束
2. **机械方程**：牛顿运动定律
3. **接口方程**：网络连接条件

**状态空间形式**

$$\dot{x} = Ax + Bu$$

其中状态变量 $x$ 包括：定子电流/磁链、转子电流/磁链、转子转速、转子位置角。

### 6.6 旋转电机的接口方法

**与EMTP网络的接口**

| 接口类型 | 实现方式 | 特点 |
|---------|---------|------|
| 电流源接口 | 向网络注入电流 | 简单，但需迭代 |
| 诺顿等效 | 导纳+电流源 | 标准EMTP形式 |
| VBR接口 | 电压源+电抗 | 数值稳定 |
| 直接嵌入 | 方程联立求解 | 精度高，复杂 |

**多时间尺度接口**

- 电磁暂态（μs-ms）：定子绕组暂态
- 机电暂态（ms-s）：转子运动
- 控制器（ms）：励磁/调速系统

**接口技术的数值延迟问题**

间接接口法因变量预测机制必然引入1个仿真步长（$\Delta t$）的数值延迟，可能激发界面高频振荡。采用电阻平均法处理凸极效应后，电机等效电导子矩阵保持恒定，避免全网导纳矩阵的重复LU分解，计算效率提升约60%~70%。

## 量化性能边界

### 模型精度与步长

| 模型类型 | 可用步长 | 相对误差 <0.25% | 计算效率提升 | 适用场景 |
|---------|---------|-----------------|-------------|---------|
| dq0模型（传统） | 10 μs | 基准 | 1×（基准） | 对称短路故障分析 |
| dq0模型（VBR优化） | 500 μs | 是 | ~50× | 大规模系统实时仿真 |
| 相域模型（PD） | 150 μs | 是 | ~6.6× | 不对称故障、谐波分析 |
| E-PD模型（恒定导纳） | 50~100 μs | 是 | 与dq0相当 | 无需人工阻尼绕组 |
| NR-CC（节点缩减） | 大步长 | 是 | 优 | EMTP大规模网络接口 |

*数据来源：Wang 2010 (VBR EMTP), Wang 2019 (E-PD), Nodal Reduced IM (NR模型)*

### 接口方法量化对比

| 接口方法 | 数值延迟 | 计算量 | 精度 | 矩阵复用 |
|---------|---------|--------|------|---------|
| 间接接口（预测） | 1步长 | 低 | 中 | 是（恒导纳） |
| 间接接口（电阻平均） | 最小化 | 中 | 中高 | 是 |
| 直接接口（联立求解） | 无 | 高（200%~300%↑） | 高 | 否 |
| VBR接口（非迭代） | 无 | 中 | 高 | 是 |

*数据来源：Wang 2010 Methods of Interfacing*

### 三类同步电机模型等价性

| 特性 | dq0模型 | 相域模型（PD） | VBR模型 |
|------|---------|--------------|---------|
| 连续时间域数学等价 | 是 | 是 | 是 |
| 不平衡运行适用性 | 受限（需假设） | 适用 | 适用 |
| 离散后数值表现 | 不同 | 不同 | 不同 |
| 网络接口形式 | 诺顿等效 | 端口导纳 | 电压源+电抗 |
| EMT建模复杂度 | 中 | 高 | 中 |

*数据来源：Re-examination of Synchronous Machine (2007)*

## 适用边界与选择指南

- dq0模型适合对称工况，相域模型适合不对称和谐波分析
- VBR模型数值稳定性好，但计算量略大
- 双笼模型适合需要精确表示启动特性的场景
- 磁路饱和模型计算复杂，仅在饱和严重时必需
- 实时仿真需采用简化模型或并行计算
- E-PD模型无需人工阻尼绕组，适合大规模网络聚合
- NR-CC节点缩减模型适合大步长EMT仿真

## 相关方法
- [[state-space-method]] - 旋转电机状态空间建模
- [[nodal-analysis]] - 电机与网络联立求解
- [[coordinate-transformation-model]] - Park/dq0变换
- [[numerical-integration]] - 电机暂态积分方法
- [[synchronous-machine-model]] - 电压Behind-Reactance方法

## 相关模型
- [[synchronous-machine-model]] - 发电机详细模型
- [[induction-machine-model]] - 电动机/负荷模型
- [[dfig-model]] - 双馈感应发电机
- [[pmsm-model]] - 新能源发电
- [[transformer-model]] - 机端变压器

## 相关主题
- [[emt-mathematical-foundation]] - 电机建模数学基础
- [[wind-farm-modeling]] - 风力发电机群
- [[real-time-simulation]] - 电机模型实时化
- [[network-equivalent]] - 电机群等值聚合
- [[co-simulation]] - 机电混合仿真

## 来源论文

[[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution]] - Wang 等 2006, VBR模型非迭代同步接口技术，50μs步长误差<0.1%，500μs步长VBR仍稳定（传统模型发散），效率提升~50倍

[[re-examination-of-synchronous-machine]] - 2007, 证明dq/PD/VBR三类模型在连续域数学等价，不平衡运行适用性无本质差别

[[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]] - Wang 2019, E-PD恒定等效导纳，无需人工阻尼绕组，计算效率与dq0相当

[[methods-of-interfacing-rotating-machine-models-in-emtp]] - Wang 等 2010, IEEE Task Force综述，间接/直接接口技术系统分类，间接法计算速度提升2~3倍但暂态峰值误差增加1.5%~3.0%

[[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-]] - Yonezawa 2023, 磁路等效相域模型，绕组电流映射为磁动势，支持空间谐波和三相不平衡

[[nodal-reduced-induction-machine-modeling-for]] - 感应电机NR-CF/NR-CC节点缩减模型，以电流为统一输出变量，适合EMTP大规模网络接口

[[synchronous-machine-exciter-circuit-model-in-a]] - 2013, MANA公式相域同步机励磁绕组直接电气连接，SM1/SM2两条接口路线

[[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio]] - 2016, 实时仿真感应电机数值优化模型，固定步长保证数值稳定性
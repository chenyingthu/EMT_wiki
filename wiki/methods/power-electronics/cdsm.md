---
title: "双钳位子模块方法 (CDSM)"
type: method
tags: [cdsm, clamp-double-submodule, mmc, fault-tolerant, electrothermal, dc-fault-limiting]
created: "2026-05-05"
updated: "2026-05-13"
---

# 双钳位子模块方法 (CDSM)

## 定义

双钳位子模块（Clamp Double Submodule, CDSM）是模块化多电平换流器（MMC）中的一种故障容错型子模块拓扑，由半桥子模块（HBSM）衍生而来。其核心结构包含 **5 组 IGBT（T1~T5）**、**5 个反并联二极管（D1~D5）**、**2 个独立钳位二极管（D6、D7）** 以及 **2 个独立串联电容（C1、C2）**，如图 1 所示。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="900" height="420" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">图1 · CDSM 拓扑结构与电路模型</text>
  
  <!-- Submodule box -->
  <rect x="200" y="50" width="500" height="300" rx="10" fill="#f8f9fa" stroke="#333" stroke-width="2"/>
  <text x="450" y="75" text-anchor="middle" font-size="13" fill="#666">CDSM 子模块内部拓扑</text>
  
  <!-- Left arm: T1-D1 branch -->
  <line x1="320" y1="100" x2="320" y2="180" stroke="#333" stroke-width="2"/>
  <rect x="305" y="110" width="30" height="50" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="320" y="140" text-anchor="middle" font-size="11" fill="#2563eb">T1</text>
  <line x1="320" y1="160" x2="320" y2="180" stroke="#333" stroke-width="2"/>
  <rect x="305" y="180" width="30" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="320" y="200" text-anchor="middle" font-size="10" fill="#dc2626">D1</text>
  <line x1="320" y1="210" x2="320" y2="230" stroke="#333" stroke-width="2"/>
  
  <!-- Right arm: T2-D2 branch -->
  <line x1="320" y1="230" x2="320" y2="250" stroke="#333" stroke-width="2"/>
  <rect x="305" y="250" width="30" height="50" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="320" y="280" text-anchor="middle" font-size="11" fill="#2563eb">T2</text>
  <line x1="320" y1="300" x2="320" y2="320" stroke="#333" stroke-width="2"/>
  <rect x="305" y="320" width="30" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="320" y="340" text-anchor="middle" font-size="10" fill="#dc2626">D2</text>
  
  <!-- Capacitor C1 -->
  <line x1="320" y1="350" x2="320" y2="370" stroke="#333" stroke-width="2"/>
  <line x1="305" y1="370" x2="335" y2="370" stroke="#333" stroke-width="2"/>
  <line x1="305" y1="378" x2="335" y2="378" stroke="#333" stroke-width="2"/>
  <line x1="320" y1="378" x2="320" y2="395" stroke="#333" stroke-width="2"/>
  <text x="290" y="378" text-anchor="end" font-size="11" fill="#333">C1</text>
  
  <!-- Top bus -->
  <line x1="200" y1="100" x2="320" y2="100" stroke="#333" stroke-width="2"/>
  <text x="195" y="95" text-anchor="end" font-size="12" fill="#333" font-weight="bold">+ U_SM</text>
  
  <!-- Bottom bus -->
  <line x1="200" y1="395" x2="320" y2="395" stroke="#333" stroke-width="2"/>
  <text x="195" y="400" text-anchor="end" font-size="12" fill="#333" font-weight="bold">- U_SM</text>
  
  <!-- Middle section: T5-D5 + D6/D7 -->
  <!-- T3-D3 branch (right of C1) -->
  <line x1="420" y1="100" x2="420" y2="180" stroke="#333" stroke-width="2"/>
  <rect x="405" y="110" width="30" height="50" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="420" y="140" text-anchor="middle" font-size="11" fill="#2563eb">T3</text>
  <line x1="420" y1="160" x2="420" y2="180" stroke="#333" stroke-width="2"/>
  <rect x="405" y="180" width="30" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="420" y="200" text-anchor="middle" font-size="10" fill="#dc2626">D3</text>
  <line x1="420" y1="210" x2="420" y2="230" stroke="#333" stroke-width="2"/>
  
  <!-- T4-D4 branch -->
  <line x1="420" y1="230" x2="420" y2="250" stroke="#333" stroke-width="2"/>
  <rect x="405" y="250" width="30" height="50" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="420" y="280" text-anchor="middle" font-size="11" fill="#2563eb">T4</text>
  <line x1="420" y1="300" x2="420" y2="320" stroke="#333" stroke-width="2"/>
  <rect x="405" y="320" width="30" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="420" y="340" text-anchor="middle" font-size="10" fill="#dc2626">D4</text>
  
  <!-- Capacitor C2 -->
  <line x1="420" y1="350" x2="420" y2="370" stroke="#333" stroke-width="2"/>
  <line x1="405" y1="370" x2="435" y2="370" stroke="#333" stroke-width="2"/>
  <line x1="405" y1="378" x2="435" y2="378" stroke="#333" stroke-width="2"/>
  <line x1="420" y1="378" x2="420" y2="395" stroke="#333" stroke-width="2"/>
  <text x="390" y="378" text-anchor="end" font-size="11" fill="#333">C2</text>
  
  <!-- Connection between left and right arms -->
  <line x1="320" y1="230" x2="420" y2="230" stroke="#333" stroke-width="2"/>
  
  <!-- T5 + D5 middle branch (clamping) -->
  <line x1="520" y1="100" x2="520" y2="140" stroke="#333" stroke-width="2"/>
  <rect x="505" y="140" width="30" height="50" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="520" y="170" text-anchor="middle" font-size="11" fill="#d97706">T5</text>
  <line x1="520" y1="190" x2="520" y2="210" stroke="#333" stroke-width="2"/>
  <rect x="505" y="210" width="30" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="520" y="230" text-anchor="middle" font-size="10" fill="#dc2626">D5</text>
  <line x1="520" y1="240" x2="520" y2="370" stroke="#333" stroke-width="2"/>
  
  <!-- Horizontal connections -->
  <line x1="420" y1="230" x2="520" y2="230" stroke="#333" stroke-width="2"/>
  <line x1="520" y1="395" x2="700" y2="395" stroke="#333" stroke-width="2"/>
  <line x1="320" y1="395" x2="520" y2="395" stroke="#333" stroke-width="2"/>
  
  <!-- Clamp diodes D6 and D7 -->
  <rect x="560" y="150" width="30" height="30" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="575" y="170" text-anchor="middle" font-size="10" fill="#7c3aed">D6</text>
  <line x1="520" y1="170" x2="560" y2="165" stroke="#333" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <rect x="560" y="280" width="30" height="30" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="575" y="300" text-anchor="middle" font-size="10" fill="#7c3aed">D7</text>
  <line x1="520" y1="300" x2="560" y2="295" stroke="#333" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Current arrow -->
  <line x1="700" y1="395" x2="750" y2="395" stroke="#333" stroke-width="2"/>
  <polygon points="750,395 745,390 745,400" fill="#333"/>
  <text x="760" y="400" font-size="12" fill="#333" font-weight="bold">i_SM</text>
  
  <!-- Labels -->
  <text x="450" y="415" text-anchor="middle" font-size="10" fill="#999">5 IGBTs + 7 Diodes + 2 Capacitors</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · CDSM 拓扑结构与器件组成（左臂：T1-D1-C1，右臂：T3-D3-C2，钳位支路：T5-D5，钳位二极管：D6、D7）</p>

CDSM 的核心特征是 **直流故障自清除能力**：当直流侧发生短路故障时，通过特定的开关序列将子模块电容插入故障路径，利用电容电压的反向充电过程限制故障电流上升率（di/dt）。与 HBSM 相比，CDSM 增加了钳位支路（T5-D5）和钳位二极管（D6、D7），使得子模块在故障状态下能够从"投入"模式切换到"钳位"模式，在故障电流过零后实现自清除。

CDSM 的等效电路可用 **二值电阻模型** 描述：每个 IGBT 及其反并联二极管被等效为导通电阻 $R_{on}$（毫欧级）或关断电阻 $R_{off}$（兆欧级），共 7 个二值电阻 $R_1 \sim R_7$ 对应 T1~T5、D1~D5、D6、D7。正常工作状态下，桥臂电阻满足约束关系：

$$
\begin{cases}
R_1 + R_2 = R_3 + R_4 = R_{sum} \\
R_1 \times R_2 = R_3 \times R_4 = R_{mul}
\end{cases}
$$

其中 $R_{sum} = R_{on} + R_{off}$，$R_{mul} = R_{on} \times R_{off}$。

## EMT 中的角色

在 EMT 仿真中，CDSM 方法主要解决以下问题：

1. **直流故障限流仿真**：CDSM 具备直流故障穿越能力，其故障清除过程涉及子模块从正常投入→钳位→反向充电→高阻态的完整状态转换序列，需要在 EMT 中精确刻画各阶段的电气动态。

2. **器件级电热耦合**：CDSM 的结构复杂度高于 HBSM/FBSM，故障清除期间各 IGBT 承受剧烈的开关瞬态应力，需要同时求解电磁暂态和热网络，评估单个器件的结温变化。

3. **大规模 MMC 的高效仿真**：CDSM 内部含 2 个独立电容和 5 个开关器件，其详细模型会导致 EMT 求解的线性方程组阶数显著升高。如何在不损失精度的前提下实现快速仿真，是 CDSM-MMC 工程应用的关键瓶颈。

4. **容错控制策略验证**：CDSM 的故障容错能力依赖于精确的子模块排序、均压控制和闭锁逻辑，EMT 仿真需要支持从系统级到器件级的分层建模，以验证控制策略的有效性。

## 核心建模方法

CDSM 的 EMT 建模方法可分为三大体系：**详细开关模型**、**等效电路解耦模型** 和 **器件级电热模型**。

### 方法一：详细开关模型（Detailed Switch Model）

直接对 CDSM 内部的 5 个 IGBT 和 7 个二极管进行逐器件级建模，采用 Norton/Companion 等效电路将每个开关器件离散化为电流源与并联电阻的组合。

**原理**：在每个仿真步长 $\Delta t$ 内，根据门极信号 $g_1 \sim g_5$ 和电流方向判定各器件导通/关断状态，更新二值电阻 $R_1 \sim R_7$，组装子模块的节点导纳矩阵和等效电流源。

**状态空间方程**（刘晋 2022）：

$$
\begin{bmatrix}
C\frac{dU_{C1}}{dt} \\
C\frac{dU_{C2}}{dt} \\
L_{SM}\frac{di_{SM}}{dt}
\end{bmatrix} =
\begin{bmatrix}
G_{11} & G_{12} & K_{i1} \\
G_{21} & G_{22} & K_{i2} \\
K_{u1} & K_{u2} & -R_{eq}
\end{bmatrix}
\begin{bmatrix}
U_{C1} \\
U_{C2} \\
i_{SM}
\end{bmatrix} +
\begin{bmatrix}
0 \\
0 \\
U_i
\end{bmatrix}
$$

其中等效电导参数由二值电阻计算：

$$
\begin{aligned}
G_{11} &= -\frac{1}{R_1+R_2} - \frac{R_5+R_7}{R_5R_6+R_5R_7+R_6R_7} \\
G_{12} = G_{21} &= \frac{R_5}{R_5R_6+R_5R_7+R_6R_7} \\
G_{22} &= -\frac{1}{R_3+R_4} - \frac{R_5+R_6}{R_5R_6+R_5R_7+R_6R_7} \\
R_{eq} &= \frac{R_1R_2}{R_1+R_2} + \frac{R_3R_4}{R_3+R_4} + \frac{R_5R_6R_7}{R_5R_6+R_5R_7+R_6R_7} \\
K_{i1} = -K_{u1} &= \frac{R_2}{R_1+R_2} - \frac{R_5R_7}{R_5R_6+R_5R_7+R_6R_7} \\
K_{i2} = -K_{u2} &= \frac{R_4}{R_3+R_4} - \frac{R_5R_6}{R_5R_6+R_5R_7+R_6R_7}
\end{aligned}
$$

**特点**：
- 精度最高，可精确刻画每个开关器件的瞬态波形
- 计算量最大，每个 CDSM 子模块引入 3 个状态变量（$U_{C1}$、$U_{C2}$、$i_{SM}$）
- 开关动作导致导纳矩阵频繁重构，易引发数值振荡

**适用场景**：小规模系统验证、器件级应力分析、控制策略原型验证。

### 方法二：半隐式延迟解耦模型（Semi-Implicit Late Decoupling Model）

针对详细开关模型计算量大的问题，刘晋等（2022）提出基于半隐式延迟解耦法的 CDSM 高效仿真方法。

**原理**：将系统矩阵分裂为自项/阻尼项和耦合项，利用中心积分（用于电容电压）与梯形积分（用于电感电流）在半个时间步上的变量错位特性，实现状态变量的时间延迟解耦。具体而言，电容电压按 $n$ 时刻更新，电感电流按 $n+\frac{1}{2}$ 时刻更新，使电容侧和端口电流侧在计算上延迟解耦。

**半隐式差分方程**：

$$
\begin{aligned}
C(U_{C1}^{n+1}-U_{C1}^n) &= \frac{\Delta t}{2} K_{i1} U_{C1}^{n+\frac{1}{2}} + \cdots \\
C(U_{C2}^{n+1}-U_{C2}^n) &= \frac{\Delta t}{2} K_{i2} U_{C2}^{n+\frac{1}{2}} + \cdots \\
L_{SM}(i_{SM}^{n+\frac{1}{2}}-i_{SM}^{n-\frac{1}{2}}) &= -\frac{\Delta t}{2} R_{eq} i_{SM}^{n+\frac{1}{2}} + \frac{\Delta t}{2} U_i^{n+\frac{1}{2}}
\end{aligned}
$$

**闭锁状态分类**：CDSM 闭锁后存在 3 种子状态（刘晋 2022）：

| 子状态 | 开关条件 | $R_{eq}$ | $K_{i1}=K_{i2}$ | 物理含义 |
|--------|----------|----------|-----------------|----------|
| 正向充电 | $i_{arm} > 0$ | $2.5R_{on}$ | $-K_{u1}=-K_{u2} \approx \frac{1}{6}$ | 电容通过导通器件充电 |
| 反向充电 | $i_{arm} < 0$ | $2.5R_{on}$ | $K_{i1}=K_{i2} \approx \frac{1}{6}$ | 电容反向充电 |
| 高阻态 | $i_{arm} = 0$ | $\infty$ | $K_{i1}=K_{i2} \approx -\frac{1}{6}$ | 电容隔离，等效开路 |

**特点**：
- 导纳矩阵恒定，无需在开关动作时重构
- 子模块交直流侧解耦，支持并行计算
- 避免了开关动作引发的状态变量突变和数值振荡
- 计及并联电容过渡过程，闭锁波形与详细模型吻合

**量化性能**（刘晋 2022）：在 41 电平 CDSM-MMC 系统中，解耦模型串行计算相较于详细模型加速显著，且随着电平数增加加速效果更明显。

**适用场景**：大规模 CDSM-MMC 系统 EMT 仿真、含数百个子模块的柔性直流工程。

### 方法三：器件级电热模型（Device-Level Electrothermal Model）

Shen 和 Dinavahi（2019）提出 CDSM 的器件级电热耦合模型，用于实时 EMT 仿真中的器件应力评估。

**原理**：采用分层混合建模（Hierarchical Hybrid Modeling），将系统级等效电路模型（ECM）与 CDSM 器件级电热模型（DLEM）相结合。电磁部分求解 IGBT 的瞬时电压电流和损耗，热模型以损耗为输入更新结温，结温再反馈修正器件电气特性，形成电磁—热双向耦合。

**IGBT 损耗模型**：

$$
P_{loss}(t) = P_{cond}(t) + P_{sw}(t) = V_{ce}(T_j) \cdot I_c(t) + \frac{E_{on}(I_c,V_{dc},T_j) + E_{off}(I_c,V_{dc},T_j)}{T_{sw}}
$$

**热网络模型**（Foster 网络）：

$$
C_{th}\frac{dT_j}{dt} + \frac{T_j - T_c}{R_{th}} = P_{loss}(t), \quad T_c = T_a + P_{total} \cdot R_{heatsink}
$$

**温度依赖的导通压降**：

$$
V_{ce}(T_j) = V_{ce0}[1 + \alpha_V(T_j - T_{ref})] + r_{ce}[1 + \alpha_r(T_j - T_{ref})] \cdot I_c
$$

**特点**：
- 实现电磁暂态与热网络的动态双向耦合
- 支持多时间尺度仿真：电磁步长 $\Delta t$（微秒级）与热更新周期（毫秒级）
- 可在 MPSoC 等硬件平台上实现实时仿真
- 提供单个 IGBT 的开关瞬态波形、损耗峰值和结温动态

**量化性能**（Shen & Dinavahi 2019）：在三端 MTDC 系统验证中，实时硬件输出波形与 PSCAD/EMTDC 系统级波形偏差小于 2%；器件级开关瞬态与 SaberRD 参考模型偏差小于 5%；结温计算误差小于 1-2%。

**适用场景**：故障清除过程中的器件应力评估、HIL 实时验证、保护控制策略的硬件在环测试。

### 方法四：广义 Norton 等效建模（Generalized Norton Equivalent）

Xu 等（2018）提出基于 Schur 补技术的多端口子模块通用建模方法，可适用于包括 CDSM 在内的任意多端口子模块结构。

**原理**：利用 Schur 补技术递归消除子模块内部的中间节点，将多端口子模块简化为一个连接到外部网络的多端口 Norton 等效电路。最终由 EMT 求解器看到的导纳矩阵维度比未约简结构小几个数量级。

**特点**：
- 通用性强，适用于 HBSM、FBSM、CDSM 等各类子模块
- 所有内部信息（如子模块电容电压）均可保留并输出
- 加速比达 2~3 个数量级

**适用场景**：含任意多端口子模块结构的大规模 MMC 高效 EMT 仿真。

### 建模方法对比

| 方法 | 精度 | 计算效率 | 导纳矩阵 | 并行性 | 适用规模 |
|------|------|----------|----------|--------|----------|
| 详细开关模型 | 最高 | 最低 | 开关时重构 | 困难 | < 11 电平 |
| 半隐式延迟解耦 | 近似详细 | 高（加速显著） | 恒定 | 支持 | 41+ 电平 |
| 器件级电热模型 | 器件级 | 中等（硬件加速） | — | PL/PS 分离 | 实时 HIL |
| 广义 Norton 等效 | 高 | 极高（加速 100-1000x） | 恒定 | 支持 | 大规模 MMC |

## 形式化表达

### CDSM 状态空间方程（基础动态）

$$
\dot{\mathbf{x}} = \mathbf{A}(\sigma) \mathbf{x} + \mathbf{B} U_i
$$

其中 $\mathbf{x} = [U_{C1}, U_{C2}, i_{SM}]^T$，$\mathbf{A}(\sigma)$ 为依赖于开关状态 $\sigma$ 的系统矩阵，$U_i$ 为子模块端口电压。

### 半隐式离散化（解耦形式）

$$
\mathbf{G} \mathbf{x}^{n+1} = \mathbf{H} \mathbf{x}^{n+\frac{1}{2}} + \mathbf{f}^{n+\frac{1}{2}}
$$

其中 $\mathbf{G}$ 为常数导纳矩阵（不随开关状态变化），$\mathbf{H}$ 为耦合矩阵，$\mathbf{f}$ 为已知源项向量。

### 热阻抗瞬态响应

$$
T_j(t) = T_a + Z_{th}(t) * P_{loss}(t) = T_a + \int_0^t P_{loss}(\tau) \cdot z_{th}(t-\tau) d\tau
$$

其中 $Z_{th}(t) = \sum_{i=1}^n R_{th,i}(1 - e^{-t/\tau_{th,i}})$ 为 Foster 网络的热阻抗瞬态曲线。

### 子模块端口电流

$$
I_{cdsm}(t) = C_{sm}\frac{dV_{sm}}{dt} + \sum_{k=1}^{5} S_k(t) \cdot I_{sw,k}(V_{ce,k}, T_{j,k})
$$

其中 $S_k$ 为第 $k$ 个 IGBT 的开关函数（0 或 1）。

## 关键技术挑战

### 1. 闭锁状态下的电容过渡过程

CDSM 闭锁后，子模块从正常工作状态进入高阻态的过程中，两个并联电容 $C_1$、$C_2$ 经历正向充电→反向充电→高阻态的过渡过程。传统等值模型往往忽略这一过渡过程，导致闭锁初期的电容电压波形与详细模型存在显著偏差。半隐式延迟解耦模型通过分裂系统矩阵，在解耦形式中保留了电容过渡过程，使闭锁波形与详细模型吻合。

### 2. 导纳矩阵恒定与开关动作的矛盾

CDSM 有 5 个开关器件，每个器件有 2 种状态，理论上存在 $2^5 = 32$ 种开关组合。传统方法在每次开关动作时都需要重构导纳矩阵，计算开销大且易引发数值振荡。半隐式延迟解耦和广义 Norton 等效方法通过矩阵分裂和 Schur 补约简，实现了导纳矩阵恒定，从根本上解决了这一矛盾。

### 3. 电热耦合的多时间尺度问题

IGBT 的开关瞬态（微秒级）与结温变化（毫秒至秒级）存在 3~6 个数量级的时间尺度差异。直接采用统一步长仿真会导致热计算资源浪费或电磁精度不足。Shen 和 Dinavahi（2019）采用多速率仿真策略：每 $N$ 个电磁步长（如 $N=1000$）求解一次热网络微分方程，在精度和效率之间取得平衡。

### 4. 大规模 CDSM-MMC 的并行计算

CDSM 内部含有 2 个独立电容和 5 个开关器件，子模块数量庞大时，详细模型的线性方程组阶数可达数千甚至数万。解耦模型通过子模块间的相互解耦，将全局网络求解与子模块内部更新分离，各子模块的计算任务可分配至不同计算核心并行执行，显著提升计算效率。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 详细模型 vs 解耦模型加速比 | 随电平数增加，41 电平时显著加速 | 刘晋 2022 |
| 广义 Norton 等效加速比 | 2~3 个数量级（100-1000x） | Xu 2018 |
| 系统级波形偏差（vs PSCAD） | < 2% | Shen & Dinavahi 2019 |
| 器件级开关瞬态偏差（vs SaberRD） | < 5% | Shen & Dinavahi 2019 |
| 结温计算误差（vs 理论热模型） | < 1-2% | Shen & Dinavahi 2019 |
| 温度分辨率 | 0.1°C | Shen & Dinavahi 2019 |
| CDSM 故障电流限制 | di/dt < 0.5-1 kA/ms，峰值降低 60-70% | Shen & Dinavahi 2019 |
| 实时仿真步长 | 1-10 $\mu$s（电磁），100 $\mu$s-1 ms（热） | Shen & Dinavahi 2019 |
| 正常状态开关组合数 | 4 种（投入/旁路等） | 刘晋 2022 |
| 闭锁状态子状态数 | 3 种（正向充电/反向充电/高阻态） | 刘晋 2022 |

## 适用边界与选择指南

### 场景-方法推荐表

| 应用场景 | 推荐建模方法 | 理由 |
|----------|-------------|------|
| 小规模系统验证（< 11 电平） | 详细开关模型 | 精度最高，计算量可接受 |
| 大规模工程仿真（41+ 电平） | 半隐式延迟解耦 / 广义 Norton 等效 | 导纳矩阵恒定，加速比高 |
| 器件应力与结温评估 | 器件级电热模型 | 提供单个 IGBT 的损耗和温度动态 |
| 实时 HIL 测试 | 分层混合建模（ECM + DLEM） | 硬件加速，满足硬实时约束 |
| 直流故障清除过程分析 | 半隐式延迟解耦 + 闭锁状态分类 | 精确刻画正向充电→高阻态过渡 |
| 含任意子模块的通用仿真 | 广义 Norton 等效 | 通用性强，支持 HBSM/FBSM/CDSM |

### 失效边界

- **不适用于平均值模型场景**：CDSM 建模关注子模块级内部动态，若仅需系统级端口等效，应采用桥臂等值模型或动态相量模型。
- **闭锁状态外推受限**：刘晋（2022）的闭锁状态分类仅针对 CDSM 的双电容结构，不应直接外推到半桥、全桥或其他混合子模块。
- **电热模型硬件依赖**：Shen 和 Dinavahi（2019）的实时电热模型在 MPSoC 硬件上验证，软件仿真中的多速率耦合参数需重新标定。
- **未验证稳定性分析**：刘晋（2022）未对所提解耦模型的数值稳定性进行理论分析，实际应用中需注意步长选择对稳定性的影响。

## 相关方法

- [[half-bridge-submodule]] — 半桥子模块，CDSM 的基线对比拓扑
- [[fbsm]] — 全桥子模块，具备故障阻断能力但器件利用率低
- [[mmc-model]] — MMC 整机层建模，CDSM 的应用载体
- [[mbsm]] — 统一子模块表示框架，CDSM 可作为其特例
- [[switch-modeling]] — 开关器件级建模基础
- [[state-space-method]] — 状态空间建模方法，CDSM 解耦模型的基础
- [[numerical-integration]] — 数值积分方法，半隐式延迟解耦的核心
- [[fixed-admittance]] — 恒定导纳矩阵方法，解耦模型的关键特征
- [[parallel-computing]] — 并行计算，解耦模型支持的任务级并行
- [[real-time-simulation]] — 实时仿真，CDSM 电热模型的硬件实现平台
- [[dc-fault-blocking]] — 直流故障闭锁，CDSM 的核心应用场景
- [[igbt-model]] — IGBT 器件模型，CDSM 电热耦合的基础

## 来源论文

- **刘晋 等 (2022)**《计及电容过渡过程的双钳位型 MMC 电磁暂态高效仿真方法》— 提出基于半隐式延迟解耦法的 CDSM 高效仿真方法，建立计及并联电容过渡过程的解耦模型，覆盖正常状态和闭锁状态（正向充电/反向充电/高阻态），实现导纳矩阵恒定和并行计算。发表于《中国电机工程学报》，46(24)。
- **Shen & Dinavahi (2019)**《Real-Time MPSoC-Based Electrothermal Transient Simulation of Fault Tolerant MMC Topology》— 提出 CDSM 器件级电热耦合模型，采用分层混合建模（ECM + DLEM），在 Xilinx Zynq UltraScale+ ZCU102 MPSoC 平台上实现实时仿真，精确刻画 IGBT 开关瞬态、损耗和结温动态。IEEE PESGM。
- **Xu 等 (2018)**《High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents》— 提出基于 Schur 补的多端口子模块通用建模方法，适用于包括 CDSM 在内的各类子模块，加速比达 2~3 个数量级。IEEE Transactions on Power Delivery, 33(3)。

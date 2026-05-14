---
title: "光伏电站 (PV Power Plant)"
type: topic
tags: [pv, solar, photovoltaic, power-plant, inverter, mppt, emt-modeling, co-simulation, ssci, benchmark]
created: "2026-05-02"
updated: "2026-05-14"
---

# 光伏电站 (PV Power Plant)

## 定义

光伏电站是由光伏阵列（PV Array）、直流汇集网络、直流-交流逆变器（DC-AC Inverter）、升压变压器、集电线路（Collector Lines）、控制保护系统和并网接口组成的集中式电源系统。EMT 语境中的光伏电站不是组件成本、运维或市场收益页面；本页关注其作为逆变器型电源（IBR）进入电网后，如何建模、验证控制响应和界定并网暂态风险。

光伏电站的核心物理过程包括：

- **光伏效应与直流侧建模**：光生电流、二极管暗电流、串联/并联电阻构成单二极管或双二极管模型，给出 $I$-$V$ 特性曲线和最大功率点（MPP）。
- **直流-交流变换**：DC-DC Boost 或 Buck 变换器实现 MPPT，DC-AC 三相逆变器（两电平/三电平）实现并网，含 LCL 或 L 滤波器。
- **并网控制**：GFL（Grid-Following）依赖 PLL 同步 + d/q 电流内环 + 外环功率/电压控制；GFM（Grid-Forming）采用下垂、VSG 或虚拟阻抗机制自主建立电压幅值和相角。
- **电站级聚合**：多逆变器、箱变、集电线路合并为等效机组时，需说明聚合依据（容量权重、拓扑分区、辐照度分布、阻抗等效）。

$$
I_{PV} = I_{ph} - I_0 \left[ \exp\left( \frac{V_{PV} + I_{PV} R_s}{a N_s V_{th}} \right) - 1 \right] - \frac{V_{PV} + I_{PV} R_s}{R_p}
$$

其中 $I_{ph}$ 为光生电流，$I_0$ 为反向饱和电流，$R_s$ 和 $R_p$ 分别为串联和并联电阻，$a$ 为二极管理想因子，$N_s$ 为串联电池数，$V_{th} = kT/q$ 为热电压。该隐式方程是 EMT 中所有 PV 模型的起点。

## EMT 中的作用

光伏电站在 EMT 中用于研究以下核心问题：

- **并网暂态响应**：逆变器的电流控制、PLL 动态、限流逻辑、LVRT/FRT 和故障后恢复。电网故障导致 PCC 电压跌落时，逆变器需在 0.02-0.15 s 内注入无功以支撑电压（依据 NERC PRC-024 标准）。
- **宽频振荡与阻抗耦合**：大规模 PV 接入后，逆变器控制环路（PLL、电流环、功率外环）与电网阻抗（尤其是长线路感抗）形成负阻尼交互，引发次同步控制交互（SSCI）。当短路比（SCR）降至 1.8-3.0 时，11-20 Hz 模态可能失稳。
- **谐波与电能质量**：PWM 开关频率（通常 10-20 kHz）产生的开关谐波、LCL 滤波器谐振峰、以及逆变器控制与电网阻抗交互引起的谐波放大效应。
- **多时间尺度仿真**：从微秒级开关动态到分钟级辐照度变化，光伏电站涉及跨越 5-6 个数量级的时间尺度，需要多速率、混合仿真或频域平均方法。
- **聚合等值与精度权衡**：详细开关模型、平均值模型（AVM）、受控电流源模型之间的精度-效率映射，是电站级 EMT 仿真的核心挑战。

## 核心建模方法

### 1. 光伏阵列模型

光伏阵列是电站的能源输入端，其建模精度直接影响直流侧动态和交流侧响应的准确性。

**单二极管模型**是最常用的 EMT 级 PV 阵列模型。由单个 PV 模块参数扩展到由 $N_p$ 个并联支路、每支路 $N_s$ 个串联模块组成的 PV 发电机时，参数换算为：

$$
a_{gen} = a,\quad I_{g,gen} = N_p I_g,\quad I_{o,gen} = N_p I_o,\quad R_{s,gen} = \frac{N_s}{N_p}R_s,\quad R_{p,gen} = \frac{N_s}{N_p}R_p,\quad \beta_{gen} = \frac{\beta}{N_s}
$$

其中 $\beta = q/(M_s k T)$ 为反热电压。光生电流 $I_g$ 和反向饱和电流 $I_o$ 随辐照度 $G$ 和结温 $T$ 变化：

$$
I_g = \left[ I_{sc,ref} + K_i (T - T_{ref}) \right] \frac{G}{G_{ref}},\quad I_o = I_{o,ref} \left( \frac{T}{T_{ref}} \right)^3 \exp\left( \frac{E_g}{k N_s} \left( \frac{1}{T_{ref}} - \frac{1}{T} \right) \right)
$$

MPPT 条件由 $\frac{d(P_{PV})}{dV_{PV}} = I_{PV} + V_{PV}\frac{dI_{PV}}{dV_{PV}} = 0$ 确定。

**双二极管模型**在低辐照度下更精确，增加了一个额外的二极管支路来描述晶界复合电流，适用于局部遮阴场景。

**等效电流源模型**将 PV 阵列简化为受控电流源，仅在研究交流侧控制时使用，忽略直流侧动态。

### 2. 逆变器建模层级

逆变器是 EMT 建模的核心，其精度-效率映射遵循五类模型框架：

| 模型层级 | 描述 | 典型步长 | 加速比 | 精度 | 适用场景 | 失效场景 |
|---------|------|---------|-------|------|---------|---------|
| 开关级 (SW) | 详细 IGBT/二极管开关模型，含死区效应 | 0.5-5 μs | 1× | 最高 | 开关谐波、EMI、保护动作细节 | 系统级大规模仿真 |
| 电压源级 (VI) | 两电平/三电平 VSI 平均模型，保留 PWM 调制 | 5-50 μs | 10-50× | 高 | LCL 谐振、PLL 动态、故障穿越 | 器件级损耗、高频 EMI |
| 平均值模型 (AV) | 忽略 PWM 开关，仅保留基波等效 | 50-500 μs | 50-200× | 中 | 控制环路验证、系统级稳定性 | 开关谐波、死区效应 |
| 受控电流源 (CCI) | 恒定导纳 + 受控电流源，忽略滤波器 | 1-10 ms | 200-1000× | 低 | 大规模场站聚合、机电暂态 | 任何高频动态 |
| 标量幅值模型 (SCI) | 仅保留有功/无功幅值 | 10-100 ms | 1000-5000× | 最低 | 准稳态时间序列 (QSTS) | 任何暂态分析 |

**开关级模型**使用理想开关（零导通电阻、无穷大关断电阻、零开关时间）或实际器件模型（含 $R_{on}$、$C_{oss}$、开关延迟）。SPWM 调制时刻通过解析交点避免逐时间步比较：

$$
t_{down} = t_n + \frac{T_s}{4V_c}(V_m + V_c),\quad t_{up} = t_n + T_s - t_{down}
$$

**电压源级模型**将逆变器等效为受控电压源，通过梯形积分离散化 LCL 滤波器：

$$
i_i(t) = i_i(t-\delta t) + \frac{\delta t}{2L_{f1}}[v_i(t) + v_i(t-\delta t) - v_f(t) - v_f(t-\delta t)]
$$

### 3. 数值积分与数值稳定性

PV 模型引入的非线性方程与线性网络方程的耦合方式，直接影响 EMT 仿真的数值稳定性。

**基本线性系统技术 (BLST)** 将 PV 非线性方程与电力系统线性方程分离求解，第 $k$ 步用第 $k-1$ 步端电压代入 PV 方程：

$$
I^{(k)}_{BLST} = f\left(V^{(k-1)}\right)
$$

这种一步延迟在端电压快速变化（如局部遮阴、电气故障、多电平逆变器多直流端口）时，会放大物理非线性为数值振荡甚至不收敛。

**扩展线性系统技术 (ELST)** 在上一工作点附近对 PV 的 $I$-$V$ 曲线作局部线性化，将其写成 Norton 等效形式：

$$
I(V) \approx I_0 + \left.\frac{dI}{dV}\right|_0 (V - V_0) = I_{eq} - G_{eq} V
$$

其中等效电导来自 PV 电流对端电压的斜率：

$$
\frac{dI}{dV} = -\frac{\frac{\beta I_o}{a}e^{\beta(V+R_s I)/a} + \frac{1}{R_p}}{1 + \frac{\beta R_s I_o}{a}e^{\beta(V+R_s I)/a} + \frac{R_s}{R_p}}
$$

等效电导并入 EMT 节点导纳矩阵，等效电流源并入注入向量，从而消除 BLST 的单步延迟误差，同时避免每步全系统非线性迭代。

### 4. 频域开关平均方法 (FD-AVM)

Agudelo 2023 提出基于数值拉普拉斯变换 (NLT) 的开关平均频域仿真方法。核心创新：

1. **分时窗策略**：将总仿真时间 $T$ 划分为若干时间窗 $T_k$，每个窗独立设置采样点数（快动态区密集采样，慢动态区稀疏采样）。
2. **开关函数平均**：对 PWM 开关函数进行频域平均，将高频开关动态等效为低频平均特性。
3. **样本重叠**：在时间窗接口处保留 $M=5-20$ 个重叠样本，抑制逆 NLT 半值收敛产生的上升时间数值振荡。

动态相量/开关平均系数公式：

$$
\langle x \rangle_k(t) = \frac{1}{P} \int_0^P x(t-P+r) e^{-jk\omega_s(t-P+r)} dr
$$

频域平均状态方程：

$$
\frac{d}{dt}\langle x \rangle_k = -jk\omega_s \langle x \rangle_k + \langle f(x,u) \rangle_k
$$

开关-电压卷积公式（Toeplitz 矩阵形式）：

$$
\langle s \cdot v \rangle_k = \sum_i \langle s \rangle_{k-i} \langle v \rangle_i
$$

### 5. 多速率 EMT-TS 混合仿真

Cao, Lin & Dinavahi 2021 提出基于 FPGA 的超实时 (FTRT) EMT-TS 混合仿真架构，用于预测并抑制弱电网下大型光伏电站的次同步控制交互 (SSCI)：

- **EMT 域**：光伏阵列与 VSC 采用 EMT 详细建模（200 μs 步长），捕捉高频开关与控制动态。
- **TS 域**：交流主网采用 TS 模型（5 ms 步长），用四阶 Runge-Kutta 求解同步发电机微分方程。
- **功率-电压接口**：EMT 侧每 200 μs 计算一次 P+jQ，TS 侧每 5 ms 计算一次；EMT 在单个 TS 步长内并行迭代 25 次。

TS 域积分公式：

$$
x_{n+1} = x_n + \frac{1}{6}(RK_1 + 2RK_2 + 2RK_3 + RK_4)
$$

光伏单元诺顿等效电导（适配 FPGA 并行计算）：

$$
G_{pv} = \frac{G_d + G_{sh}}{G_d R_s + R_s G_{sh} + 1}
$$

### 6. 基于 Modelica 的自动线性化与特征值分析

Masoom 2025 提出基于 Modelica 方程建模的 PV 场站控制交互风险快速评估框架：

1. 使用 MSEMT 库构建包含 PV 阵列、DC-AC 变流器、集电线路、变压器及 FRT 控制器的完整 EMT 详细模型。
2. Modelica 编译器自动将分层物理模型展平为微分代数方程组 $F(t, \dot{x}, x, y, z) = 0$。
3. 在目标运行点 $t_l$ 处进行泰勒级数线性化，直接提取显式状态空间矩阵：

$$
\delta\dot{x} = A\delta x + B\delta u,\quad \delta y = C\delta x + D\delta u
$$

4. 对矩阵 $A$ 进行特征值分解，复特征值实部 $>0$ 指示负阻尼风险。

## 形式化表达

电站级 PV EMT 模型可概括为以下耦合关系：

$$
\begin{aligned}
I_{PV}(V_{PV}, G, T) &= I_{ph}(G, T) - I_0(T) \left[ \exp\left( \frac{V_{PV} + I_{PV} R_s}{a N_s V_{th}} \right) - 1 \right] - \frac{V_{PV} + I_{PV} R_s}{R_p} \\
I^{(k)}_{BLST} &= f\left(V^{(k-1)}\right) \\
I(V) &\approx I_0 + \left.\frac{dI}{dV}\right|_0 (V - V_0) = I_{eq} - G_{eq} V \\
\langle x \rangle_k(t) &= \frac{1}{P} \int_0^P x(t-P+r) e^{-jk\omega_s(t-P+r)} dr \\
\delta\dot{x} &= A\delta x + B\delta u \\
SCR &= \frac{U_N^2}{Z_g \cdot S_N} \\
x_{n+1} &= x_n + \frac{1}{6}(RK_1 + 2RK_2 + 2RK_3 + RK_4)
\end{aligned}
$$

其中 $G$ 和 $T$ 表示辐照度和温度，$C(\cdot)$ 表示逆变器控制与限流逻辑，$v_{\mathrm{pcc}}$ 是并网点电压，$SCR$ 为短路比。若聚合多个逆变器，应说明哪些状态和控制差异被保留，哪些被等值。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 620" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="620" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">光伏电站 EMT 建模体系架构</text>
  
  <!-- Layer 1: 物理系统输入 (Blue) -->
  <rect x="50" y="50" width="120" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="72" text-anchor="middle" font-size="12" fill="#1e40af">光伏阵列</text>
  <text x="110" y="90" text-anchor="middle" font-size="10" fill="#3b82f6">单二极管模型</text>
  
  <rect x="180" y="50" width="120" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="240" y="72" text-anchor="middle" font-size="12" fill="#1e40af">DC-DC 变换器</text>
  <text x="240" y="90" text-anchor="middle" font-size="10" fill="#3b82f6">MPPT 控制</text>
  
  <rect x="310" y="50" width="120" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="370" y="72" text-anchor="middle" font-size="12" fill="#1e40af">DC-AC 逆变器</text>
  <text x="370" y="90" text-anchor="middle" font-size="10" fill="#3b82f6">VSI/LCL 滤波器</text>
  
  <line x1="370" y1="100" x2="370" y2="130" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 2: 控制架构 (Green) -->
  <rect x="50" y="130" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="110" y="152" text-anchor="middle" font-size="12" fill="#15803d">GFL 控制</text>
  <text x="110" y="170" text-anchor="middle" font-size="10" fill="#22c55e">PLL + d/q 电流环</text>
  
  <rect x="180" y="130" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="240" y="152" text-anchor="middle" font-size="12" fill="#15803d">GFM 控制</text>
  <text x="240" y="170" text-anchor="middle" font-size="10" fill="#22c55e">下垂 / VSG</text>
  
  <rect x="310" y="130" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="152" text-anchor="middle" font-size="12" fill="#15803d">PPC 电站控制</text>
  <text x="370" y="170" text-anchor="middle" font-size="10" fill="#22c55e">功率分配 / 无功</text>
  
  <line x1="370" y1="180" x2="370" y2="210" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 3: 逆变器建模层级 (Yellow) -->
  <rect x="50" y="210" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="130" y="232" text-anchor="middle" font-size="12" fill="#92400e">开关级 (SW)</text>
  <text x="130" y="250" text-anchor="middle" font-size="10" fill="#f59e0b">0.5-5 μs / 1× / 最高精度</text>
  
  <rect x="220" y="210" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="300" y="232" text-anchor="middle" font-size="12" fill="#92400e">电压源级 (VI)</text>
  <text x="300" y="250" text-anchor="middle" font-size="10" fill="#f59e0b">5-50 μs / 10-50× / 高精度</text>
  
  <rect x="390" y="210" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="470" y="232" text-anchor="middle" font-size="12" fill="#92400e">平均值模型 (AV)</text>
  <text x="470" y="250" text-anchor="middle" font-size="10" fill="#f59e0b">50-500 μs / 50-200× / 中精度</text>
  
  <line x1="470" y1="260" x2="470" y2="290" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 4: EMT 分析方法 (Purple) -->
  <rect x="50" y="290" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="130" y="312" text-anchor="middle" font-size="12" fill="#5b21b6">BLST / ELST</text>
  <text x="130" y="330" text-anchor="middle" font-size="10" fill="#7c3aed">数值稳定性方法</text>
  
  <rect x="220" y="290" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="300" y="312" text-anchor="middle" font-size="12" fill="#5b21b6">FD-AVM</text>
  <text x="300" y="330" text-anchor="middle" font-size="10" fill="#7c3aed">频域开关平均</text>
  
  <rect x="390" y="290" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="470" y="312" text-anchor="middle" font-size="12" fill="#5b21b6">EMT-TS 混合</text>
  <text x="470" y="330" text-anchor="middle" font-size="10" fill="#7c3aed">FPGA 超实时</text>
  
  <rect x="560" y="290" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="640" y="312" text-anchor="middle" font-size="12" fill="#5b21b6">Modelica 线性化</text>
  <text x="640" y="330" text-anchor="middle" font-size="10" fill="#7c3aed">特征值分析</text>
  
  <line x1="640" y1="340" x2="640" y2="370" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 5: 分析场景 (Amber) -->
  <rect x="50" y="370" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="130" y="392" text-anchor="middle" font-size="12" fill="#92400e">并网暂态响应</text>
  <text x="130" y="410" text-anchor="middle" font-size="10" fill="#f59e0b">LVRT / 故障穿越</text>
  
  <rect x="220" y="370" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="300" y="392" text-anchor="middle" font-size="12" fill="#92400e">SSCI 分析</text>
  <text x="300" y="410" text-anchor="middle" font-size="10" fill="#f59e0b">弱网 / 11-20 Hz</text>
  
  <rect x="390" y="370" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="470" y="392" text-anchor="middle" font-size="12" fill="#92400e">谐波与电能质量</text>
  <text x="470" y="410" text-anchor="middle" font-size="10" fill="#f59e0b">PWM / LCL 谐振</text>
  
  <rect x="560" y="370" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="640" y="392" text-anchor="middle" font-size="12" fill="#92400e">聚合等值验证</text>
  <text x="640" y="410" text-anchor="middle" font-size="10" fill="#f59e0b">精度-效率权衡</text>
  
  <line x1="370" y1="420" x2="370" y2="450" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 6: 量化性能 (Bottom summary) -->
  <rect x="50" y="450" width="160" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="130" y="472" text-anchor="middle" font-size="12" fill="#991b1b">FD-AVM 加速 100-1000×</text>
  <text x="130" y="490" text-anchor="middle" font-size="10" fill="#ef4444">RMS误差 &lt;2%</text>
  
  <rect x="220" y="450" width="160" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="300" y="472" text-anchor="middle" font-size="12" fill="#991b1b">FTRT 加速 122×</text>
  <text x="300" y="490" text-anchor="middle" font-size="10" fill="#ef4444">SSCI 0.09s 响应</text>
  
  <rect x="390" y="450" width="160" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="470" y="472" text-anchor="middle" font-size="12" fill="#991b1b">ELST 消除一步延迟</text>
  <text x="470" y="490" text-anchor="middle" font-size="10" fill="#ef4444">IEEE 配电验证</text>
  
  <rect x="560" y="450" width="160" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="640" y="472" text-anchor="middle" font-size="12" fill="#991b1b">134台逆变器基准</text>
  <text x="640" y="490" text-anchor="middle" font-size="10" fill="#ef4444">ORNL IEEE 39节点</text>
  
  <!-- Legend -->
  <text x="450" y="540" text-anchor="middle" font-size="13" font-weight="bold" fill="#333">图例</text>
  <rect x="100" y="550" width="30" height="15" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="140" y="563" font-size="11" fill="#333">物理系统输入</text>
  <rect x="260" y="550" width="30" height="15" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="300" y="563" font-size="11" fill="#333">控制架构</text>
  <rect x="390" y="550" width="30" height="15" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="430" y="563" font-size="11" fill="#333">建模层级</text>
  <rect x="530" y="550" width="30" height="15" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="570" y="563" font-size="11" fill="#333">EMT方法</text>
  <rect x="670" y="550" width="30" height="15" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="710" y="563" font-size="11" fill="#333">量化性能</text>
  
  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 光伏电站 EMT 建模体系架构（六层：物理输入→控制架构→建模层级→EMT方法→分析场景→量化性能）</p>

## 关键技术挑战

### 挑战 1：数值稳定性与非线性耦合

PV 单二极管模型的隐式 $I$-$V$ 方程在 EMT 线性网络求解中引入数值不稳定性。BLST 的一步延迟在局部遮阴、多阵列、多电平逆变器接口等场景下会放大为数值振荡。ELST 通过局部线性化将等效电导并入导纳矩阵，但仅适用于外部网络为线性的场景，对含大量非线性电力电子元件的系统需重新验证。

### 挑战 2：多时间尺度仿真

光伏电站涉及从微秒级开关动态到分钟级辐照度变化的跨越。传统 EMT 仿真需使用 0.5-5 μs 步长，导致大规模场站仿真时间过长。FD-AVM 通过开关平均将步长提升至 0.1-1 ms（100-1000 倍加速），但牺牲了高频开关纹波和器件级损耗细节。多速率混合仿真（如 EMT-TS 协同）通过功率-电压接口实现多速率同步，但接口处的数据交换精度影响全局稳定性。

### 挑战 3：次同步控制交互 (SSCI)

大型 PV 经长距离线路接入弱电网时，逆变器控制（PLL、电流环）与线路阻抗形成负阻尼交互。Cao 2021 在 IEEE 39 节点系统 + 400 MW PV 场景中，特征值分析得到 11.8207 Hz 模态，FFT 时域分析约 12 Hz，SCR 降至 1.8 时特征值进入右半平面。SSCI 的频率范围通常在 2-100 Hz，取决于控制参数和电网强度。

### 挑战 4：聚合等值与精度损失

将数百个逆变器合并为等效机组时，单机等值可能掩盖集电线路谐振、分散逆变器控制差异和局部辐照度不一致。Marthi 2024 的 ORNL 基准模型包含三个 PV 厂站（125 MW + 125 MW + 250 MW），共 134 台逆变器（1 MW 和 2.5 MW 混合配置），采用 5 条辐射状集电线路，展示了详细聚合与等值之间的精度权衡。

### 挑战 5：控制交互风险快速筛查

传统特征值分析需手动推导状态空间方程，拓扑变化时需重写。Masoom 2025 的 Modelica 自动线性化流程消除了这一断点，但线性化特征值分析仅反映选定运行点附近的小扰动动态，对限幅、保护切换、故障穿越过程中的强非线性和离散事件不能直接给出全局结论。

## 量化性能边界

| 指标 | 数值 | 来源 | 场景 |
|------|------|------|------|
| BLST→ELST 数值稳定性改善 | 消除单步延迟误差 | Di Fazio 2012 | IEEE 配电系统局部遮阴/故障 |
| FD-AVM 步长加速比 | 100-1000× (μs→ms) | Agudelo 2023 | 单相/三相光伏逆变器 |
| FD-AVM 状态变量 RMS 误差 | <2% | Agudelo 2023 | IEEE 39 节点含 PV |
| FD-AVM 峰值误差 | <5% | Agudelo 2023 | 电网电压跌落故障穿越 |
| FD-AVM 计算时间减少 | 60-80% | Agudelo 2023 | 三相光伏并网系统 |
| FD-AVM 内存减少 | ~85% | Agudelo 2023 | IEEE 39 节点含 PV |
| EMT-TS 混合仿真加速比 | 122× (FTRT) | Cao 2021 | IEEE 39 + 400 MW PV + 4端HVDC |
| SSCI 振荡频率 | 11.82 Hz (特征值) / ~12 Hz (FFT) | Cao 2021 | SCR=1.8 弱电网 |
| SSCI 控制响应时间 | 0.09 s | Cao 2021 | t=1.0s 扰动, t=1.09s 补偿 |
| SSCI 失稳临界 SCR | 1.8 | Cao 2021 | λ5, λ6 进入右半平面 |
| 全 EMT 仿真加速 | 1小时物理→4小时计算 | Hariri 2017 | 佛罗里达实际配电馈线 |
| QSTS 仿真加速 | 1周数据(15min间隔)→30分钟 | Hariri 2017 | 配电网电压调节 |
| 混合仿真 EMT 步长 | 2 μs | Hariri 2017 | 开关动态、LCL 谐振 |
| 混合仿真 QSTS 步长 | 15 分钟 | Hariri 2017 | 准稳态潮流 |
| Marthi 基准 PV 厂站容量 | 125 + 125 + 250 MW | Marthi 2024 | IEEE 39 节点系统 |
| Marthi 基准逆变器数量 | 134 台 (1MW+2.5MW) | Marthi 2024 | 5 条辐射状集电线路 |
| Marthi 基准 SCR (原始) | 25, 27.5, 15 | Marthi 2024 | IBR-1, IBR-2, IBR-3 接入点 |
| Marthi 基准 SCR (弱化) | 10, 9, 8 | Marthi 2024 | 降低线路强度模拟弱网 |
| Modelica 自动线性化 | 消除手动推导断点 | Masoom 2025 | 任意拓扑变更直接提取 A/B/C/D |

## 适用边界与选择指南

### 建模层级选择决策表

| 应用场景 | 推荐模型 | 步长 | 原因 |
|---------|---------|------|------|
| 开关谐波与 EMI 分析 | 开关级 (SW) | 0.5-5 μs | 需精确再现 IGBT 开关瞬态 |
| PLL 动态与故障穿越 | 电压源级 (VI) | 5-50 μs | 保留 PWM 调制和 LCL 谐振 |
| 系统级控制验证 | 平均值模型 (AV) | 50-500 μs | 精度-效率平衡 |
| 大规模场站聚合 | 受控电流源 (CCI) | 1-10 ms | 计算效率优先 |
| 频域暂态分析 | FD-AVM | 0.1-1 ms | 保留网络频率特性，平均开关 |
| 弱网 SSCI 预测 | EMT-TS 混合 (FPGA) | EMT: 200 μs, TS: 5 ms | 超实时推演 |
| 控制交互快速筛查 | Modelica 特征值 | 线性化 | 自动提取 A/B/C/D 矩阵 |
| 配电网 QSTS 研究 | EMT-相量混合 | EMT: μs, QSTS: min | 多速率解耦 |

### 失效边界

- **平均值模型**无法反映 PWM 谐波、死区效应、直流侧纹波和保护动作所需的瞬时电流。
- **单机等值**可能掩盖集电线路谐振、分散逆变器控制差异和局部辐照度不一致。
- **弱网稳定结论**必须绑定短路比、控制参数、扰动幅值、运行点和模型层级；不能从一个 PV 算例外推到所有逆变器型电源。
- **ELST 方法**仅适用于外部电力系统可表示为线性网络、非线性主要来自 PV 发电机单二极管模型的场景。
- **FD-AVM**不适合要求精确再现器件级 PWM 纹波、开关损耗、EMI 或保护中高频瞬态细节的研究。
- **特征值分析**仅反映选定运行点附近的小扰动动态，对大扰动、保护切换、限幅饱和不能直接给出全局结论。

## 与相关页面的关系

- [[pv-system-model]] 解释光伏系统等效模型；本页组织电站级对象和应用边界。
- [[inverter-model]]、[[gfl-inverter-model]]、[[gfm-inverter-model]] 讨论逆变器控制和接口；本页不重复控制器内部方程。
- [[renewable-energy-integration]] 关注新能源并网总体问题；本页聚焦光伏电站。
- [[frequency-domain-analysis]] 和 [[harmonic-analysis]] 可用于识别阻抗耦合和谐波风险，但不能替代大扰动 EMT 验证。
- [[co-simulation]] 和 [[multirate-method]] 是解决光伏电站多时间尺度仿真的核心方法。
- [[eigenvalue-analysis]] 和 [[small-signal-analysis]] 是控制交互风险筛查的工具。
- [[average-value-model]] 是逆变器建模层级的关键方法。
- [[parallel-in-time]] 和 [[gpu-parallel-acceleration]] 是加速大规模 PV 仿真的计算技术。
- [[ieee-39-bus-system]] 是 PV 基准模型验证的标准测试系统。
- [[power-quality]] 是评估 PV 并网电能质量的主题。

## 开放问题

- 如何在不泄露厂家控制器细节的情况下建立可信的光伏电站 EMT 等值。
- 如何统一光伏场站的聚合误差、弱网稳定裕度、谐波风险和故障穿越验证指标。
- 如何把储能和构网控制纳入电站级模型，同时避免把单个控制器算例外推为通用能力。
- 如何在 FD-AVM 中定量刻画开关平均对谐波传播和 EMI 分析的边界影响。
- 如何建立标准化的 PV 场站 EMT 基准模型库（参考 Marthi 2024 的 ORNL 工作），覆盖不同逆变器拓扑、集电网络拓扑和控制策略。

## 来源论文

- **Di Fazio & Russo 2012** — 提出扩展线性系统技术 (ELST)，解决 PV 单二极管模型在 EMT 线性网络中的数值不稳定性问题，通过局部线性化消除 BLST 的单步延迟误差。
- **Agudelo 2023** — 提出基于 NLT 的开关平均频域仿真方法 (FD-AVM)，通过分时窗、开关函数平均和样本重叠技术，将步长从 μs 提升至 ms 级（100-1000 倍加速），RMS 误差 <2%。
- **Cao, Lin & Dinavahi 2021** — 提出 FPGA 超实时 EMT-TS 混合仿真架构，实现 122× 加速比，用于预测和抑制弱电网下大型 PV 的 SSCI（11.82 Hz 模态，SCR=1.8 失稳）。
- **Masoom 2025** — 提出基于 Modelica 方程建模的 PV 场站控制交互风险快速评估框架，通过自动 DAE 展平和泰勒线性化直接提取状态空间矩阵，消除手动推导断点。
- **Hariri & Faruque 2017** — 提出 EMT-相量域混合仿真架构，EMT 侧（微秒级）求解 PV 和逆变器动态，OpenDSS 侧（分钟级）执行 QSTS 潮流，实现配电网 PV 接入影响的多速率协同分析。
- **Marthi, Debnath & Choi 2024** — 提出 ORNL 基准高保真 EMT 模型，包含 IEEE 39 节点系统 + 三个 PV 厂站（125+125+250 MW，134 台逆变器，5 条辐射状集电线路），用于测试不同故障条件和 SCR 下的 PV 并网动态。

---
title: "GaN HEMT 建模方法"
type: method
tags: [gan-hemt, wide-bandgap, device-modeling, realtime, electrothermal, pfnn, wbg]
created: "2026-05-05"
updated: "2026-05-13"
---

# GaN HEMT 建模方法

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 460" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="460" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">GaN HEMT 建模方法体系架构</text>
  
  <!-- Row 1: 建模复杂度层级 -->
  <text x="450" y="60" text-anchor="middle" font-size="12" fill="#666">按建模复杂度递进</text>
  
  <!-- Level 1: 理想开关 -->
  <rect x="30" y="75" width="190" height="70" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="125" y="98" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">理想开关模型</text>
  <text x="125" y="116" text-anchor="middle" font-size="10" fill="#555">两态电阻 (R_on/R_off)</text>
  <text x="125" y="132" text-anchor="middle" font-size="10" fill="#555">L/C 伴随电路等价</text>
  
  <!-- Arrow down -->
  <line x1="125" y1="145" x2="125" y2="165" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Level 2: 稳态特性 -->
  <rect x="250" y="170" width="190" height="70" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="345" y="193" text-anchor="middle" font-size="12" font-weight="bold" fill="#16a34a">稳态特性模型</text>
  <text x="345" y="211" text-anchor="middle" font-size="10" fill="#555">u_th + r_on 串联</text>
  <text x="345" y="227" text-anchor="middle" font-size="10" fill="#555">多项式拟合输出特性</text>
  
  <!-- Arrow down -->
  <line x1="345" y1="240" x2="345" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Level 3: 开关瞬态 -->
  <rect x="470" y="265" width="190" height="70" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="565" y="288" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">开关瞬态模型</text>
  <text x="565" y="306" text-anchor="middle" font-size="10" fill="#555">线性化/查表法波形</text>
  <text x="565" y="322" text-anchor="middle" font-size="10" fill="#555">分段折线 / 指数函数</text>
  
  <!-- Arrow down -->
  <line x1="565" y1="335" x2="565" y2="355" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Level 4: 物理/行为模型 -->
  <rect x="690" y="360" width="190" height="70" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="785" y="383" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">物理/行为模型</text>
  <text x="785" y="401" text-anchor="middle" font-size="10" fill="#555">Hefner 等效电路</text>
  <text x="785" y="417" text-anchor="middle" font-size="10" fill="#555">非线性阻抗 + 受控源</text>
  
  <!-- Bottom section: ML 加速模型 -->
  <rect x="30" y="445" width="855" height="60" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="468" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c3aed">机器学习加速模型（PFNN / FTPNN）— 变量时步，可低至 1 ns，FPGA 实时 HIL 加速</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · GaN HEMT 建模方法体系架构</p>

## 定义

GaN HEMT（Gallium Nitride High Electron Mobility Transistor，氮化镓高电子迁移率晶体管）建模方法是指在电磁暂态（EMT）仿真中，对 GaN HEMT 的开关瞬态特性、导通/关断动态、寄生参数效应、损耗机制及电热耦合行为进行精确数值表征的技术体系。

GaN HEMT 作为宽禁带（Wide Bandgap, WBG）半导体器件的代表，其开关速度可达数十纳秒量级（关断过程约 10 ns），开关频率可达数百 kHz 至 MHz 级别，远高于传统 Si IGBT（微秒级）和 SiC MOSFET。这一高速特性使得 GaN HEMT 在 EMT 仿真中面临独特的建模挑战：仿真步长需达纳秒级才能保证数值精度，而器件内部非理想特性（寄生电容 $C_{gd}$、$C_{ds}$、米勒平台效应、di/dt 和 dv/dt 振荡）对系统暂态有显著影响。

GaN HEMT 建模的核心目标是在计算精度与仿真效率之间取得平衡，根据研究场景选择从理想开关到物理模型的合适粒度。

## EMT 中的角色

GaN HEMT 在 EMT 仿真中承担三个关键角色：

**1. 高频电力电子接口器件**：在高频 DC/DC 变换器、固态变压器（SST）、微型电网（如 DC Railway Microgrid, DRM）中，GaN HEMT 作为核心开关器件，其开关瞬态直接影响系统级电磁暂态波形。精确的 GaN HEMT 模型可反映开关过冲、振铃、米勒电容耦合等高频现象。

**2. 硬件在环（HIL）实时仿真对象**：GaN HEMT 的超快瞬态过程（约 10 ns）要求实时仿真平台使用纳秒级步长。Zhang 等（2023）在 Xilinx Ultrascale+ FPGA 上实现了 GaN HEMT 的 PFNN 模型，变量时步可低至 1 ns，实现了设备级瞬态的实时硬件在环仿真。

**3. 损耗评估与热管理分析基础**：GaN HEMT 的开关损耗（开通 $E_{on}$、关断 $E_{off}$）和导通损耗 $P_{cond} = V_{on} \cdot I_{ds}$ 是热设计的关键输入。EMT 仿真中需精确量化各工况下的损耗，Sinkar 等（2025）提出了 MMC 臂级半导体损耗的快速估计方法，可应用于 GaN HEMT 系统。

## EMT 建模方法

### 方法一：理想开关模型

最简单的 GaN HEMT 建模将器件视为两态电阻：

$$R_{\text{GaN}} = \begin{cases} R_{\text{on}}, & \text{导通 (V}_{\text{gs}} > V_{\text{th}}) \\ R_{\text{off}}, & \text{关断 (V}_{\text{gs}} \leq V_{\text{th}}) \end{cases}$$

其中 $R_{\text{on}}$ 为毫欧级通态电阻（GaN HEMT 的典型 $R_{\text{ds(on)}}$ 为 10-100 m$\Omega$），$R_{\text{off}}$ 为 G$\Omega$ 级阻断电阻。

在实时仿真中，为避免导纳矩阵因开关状态变化而频繁求解逆矩阵，常采用 L/C 伴随电路模型。在导通时表现为电感元件，关断时表现为电阻与电容元件串联。电感 $L$、电容 $C$ 及电阻 $R$ 的取值由仿真步长 $\Delta T$ 和阻尼系数 $d$ 确定：

$$L = \frac{\Delta T}{2F}, \quad C = \frac{\Delta T \cdot F}{2}, \quad R = \frac{1}{F}$$

其中 $F = \frac{1}{2(\sqrt{d^2+1}-d)}$，$d$ 为阻尼系数，$V$ 为关断时稳态电压，$I$ 为导通时稳态电流。

**适用场景**：系统级初步分析、控制策略验证、大系统机电-电磁混合仿真。
**局限性**：无法反映导通压降、开关瞬态波形、寄生参数效应、开关损耗。

### 方法二：稳态特性模型

稳态特性模型采用电压源与电阻串联的方式表示 GaN HEMT 的导通状态：

$$V_{\text{ds}} = u_{\text{th}} + i_{\text{ds}} \cdot r_{\text{on}}$$

其中 $u_{\text{th}}$ 为器件导通截止电压（GaN HEMT 的典型阈值电压 $V_{\text{th}} \approx 1.5-3.0$ V），$r_{\text{on}}$ 为一定范围内的斜率电阻。

采用多项式拟合输出特性时，$u_{\text{th}}$ 和 $r_{\text{on}}$ 的表达式为：

$$u_{\text{th}}(i) = \sum_{k=0}^{n} a_k i^k$$

$$r_{\text{on}}(i) = \frac{d u_{\text{th}}}{d i} = \sum_{k=1}^{n} k \cdot a_k \cdot i^{k-1}$$

其中 $a_k$ 为多项式第 $k$ 阶拟合系数，由器件数据手册或实验测试获得。

**适用场景**：稳态损耗计算、器件应力评估、中等精度系统仿真。
**优势**：比理想开关模型更精确地反映导通压降的非线性，计算开销小。

### 方法三：线性化/查表法开关瞬态模型

开关瞬态是指 GaN HEMT 在导通和关断瞬间器件电压电流的变化过程。由于 GaN HEMT 开关过程通常在数百纳秒内完成，需采用极小的仿真步长。

通过数据手册或测试实验获取 GaN HEMT 电压电流通断瞬间波形数据，包括：
- 电流上升时间 $t_r$
- 电流下降时间 $t_f$
- 电压上升时间 $t_{v\_rise}$
- 电压下降时间 $t_{v\_fall}$
- 开通损耗 $E_{\text{on}}$
- 关断损耗 $E_{\text{off}}$

电压上升时间和下降时间可由式估算：

$$t_{v\_rise} = \frac{t_r}{I_{\text{off}}} \cdot V_{\text{on}}$$

$$t_{v\_fall} = \frac{t_f}{I_{\text{on}}} \cdot V_{\text{off}}$$

其中 $V_{\text{on}}$、$I_{\text{on}}$ 为导通稳态值，$V_{\text{off}}$、$I_{\text{off}}$ 为关断稳态值。

在单个仿真步长内，电压电流变化量为：

$$\Delta V = \frac{V_{\text{off}} - V_{\text{on}}}{t_{v\_rise}} \cdot \Delta t, \quad \Delta I = \frac{I_{\text{on}} - I_{\text{off}}}{t_r} \cdot \Delta t$$

该模型可在 FPGA 的单个系统时钟内完成单步长计算，实现极小步长实时仿真。

**适用场景**：FPGA 实时 HIL 仿真、开关瞬态波形分析、di/dt 和 dv/dt 研究。
**优势**：计算步骤简单，可在单个时钟周期内完成，适合纳秒级步长。
**局限性**：基于线性化假设，对不同稳态电压/电流值的泛化能力有限。

### 方法四：分段折线模型

分段折线模型基于对器件开关瞬态行为过程的分析，建立多个时序分段的折线模型。以导通瞬态为例，模型包含以下关键分段点：

- $I_{\text{ds1}}$：器件导通状态下集电极稳态电流
- $V_{\text{gs1}}$：导通状态时栅极与源极间稳态电压
- $V_{\text{ds2}}$：关断状态时集电极与源极间稳态电压

对每个分段过程，通过已知的稳态电压、电流及栅极状态信息，计算该时间分段下电流、电压变化率及分段时长。该模型需考虑器件的非线性电阻及电容特性（$C_{\text{gd}}$、$C_{\text{gs}}$、$C_{\text{ds}}$），数学模型计算量比线性化开关模型显著增大。

**适用场景**：开关瞬态波形精确复现、米勒平台效应分析、驱动电路影响研究。
**优势**：波形更准确地随电路稳态数值及器件状态变化。
**难点**：与系统电路的耦合方式——采用受控源时需保证电压或电流波形之一准确。

### 方法五：物理模型与行为模型

物理模型通过对 GaN HEMT 的二维电子气（2DET）沟道、势垒层、衬底结构建立数学解析表达式，采用非线性阻抗及受控电流源构建等效电路。GaN HEMT 的物理模型通常包含：

- 沟道电流模型：$I_{\text{ds}} = f(V_{\text{gs}}, V_{\text{ds}}, T)$，考虑 2DET 载流子浓度
- 寄生电容模型：$C_{\text{gd}}(V_{\text{gd}})$、$C_{\text{gs}}(V_{\text{gs}})$、$C_{\text{ds}}(V_{\text{ds}})$，非线性电压依赖
- 热阻-热容网络：$R_{\text{th}}-C_{\text{th}}$ 耦合电热效应

物理模型通常需要详细的器件制造参数（沟道长度、掺杂浓度、材料参数），获取难度较大。行为模型则通过实验获得的电压/电流波形进行参数拟合，不依赖器件内部结构。

**适用场景**：器件级设计优化、寄生参数敏感性分析、高频振荡研究。
**局限性**：计算复杂度最高，牛顿法迭代求解，在大规模系统中应用受限。

### 方法六：机器学习加速模型（PFNN / FTPNN）

针对 GaN HEMT 超快瞬态过程（约 10 ns）的实时仿真需求，Zhang 等（2023）提出了两种基于机器学习的建模方法：

**固定时步点神经网络（FTPNN）**：使用全连接神经网络（FNN）或门控循环单元（GRU）在固定时间步长下预测 GaN HEMT 的电压/电流波形。例如，使用 50 个数据点以 20 ns 固定步长模拟 1 $\mu$s 波形，或使用 20 个数据点以 50 ns 步长模拟。

**物理特征神经网络（PFNN）**：PFNN 是 Zhang 等（2023）提出的创新方法，将机器学习算法与物理建模相结合。PFNN 不输出所有时间步长的数据点，而是仅输出关键物理特征点（波形拐点、峰值和谷值点），基于这些物理特征（PF）进行变量时步预测。输出数据点不仅包含电压值，还包含对应的时间值：

$$\{(t_1, v_1), (t_2, v_2), \ldots, (t_n, v_n)\}$$

通过减少无关信息的输出，PFNN 大幅降低了硬件资源消耗。对于波形变化不大的时段，输出点数显著减少。在获得数据点后，采用分段线性化方法按所需时间步长插入中间数据点，可实现 10 ns 甚至 1 ns 的等效输出步长。

PFNN 的输入为器件的电压-时间-电流三维数据集，训练过程包括：
1. 从 EMT 仿真获取原始 3D 数据（电压-电流-时间）
2. 压缩为 3D 电压-时间波形
3. 提取物理特征点作为训练集
4. 训练 GRU/FNN 网络

**适用场景**：FPGA 实时 HIL 仿真、超快瞬态设备级建模。
**优势**：变量时步（可低至 1 ns），FPGA 并行加速，显著降低硬件资源消耗。
**来源**：Zhang 等（2023）在 Xilinx Ultrascale+ FPGA 上验证，与 PSCAD/EMTDC 离线仿真和 SaberRD 设备级瞬态对比验证。

## 形式化表达

### GaN HEMT 关键参数

| 参数 | 符号 | 典型值/范围 | 说明 |
|------|------|------------|------|
| 导通电阻 | $R_{\text{ds(on)}}$ | 10-100 m$\Omega$ | 2DET 沟道电阻 |
| 阈值电压 | $V_{\text{th}}$ | 1.5-3.0 V | 沟道开启电压 |
| 栅-漏电容 | $C_{\text{gd}}$ | 0.1-1 pF | 米勒电容，影响开关瞬态 |
| 栅-源电容 | $C_{\text{gs}}$ | 0.5-5 pF | 输入电容 |
| 漏-源电容 | $C_{\text{ds}}$ | 0.1-2 pF | 输出电容 |
| 开通损耗 | $E_{\text{on}}$ | 数-数十 mJ | 与 $V_{\text{ds}}$、$I_{\text{ds}}$、$R_g$ 相关 |
| 关断损耗 | $E_{\text{off}}$ | 数-数十 mJ | 与 $V_{\text{ds}}$、$I_{\text{ds}}$、$R_g$ 相关 |
| 开关时间 | $t_{\text{sw}}$ | 5-50 ns | GaN HEMT 典型开关时间 |

### 半导体功率损耗分解

GaN HEMT 的总功率损耗可分解为三部分（Sinkar 等 2025）：

**导通损耗**：
$$P_{\text{cond}} = V_{\text{on}} \cdot I_{\text{ds}} = I_{\text{ds}}^2 \cdot R_{\text{on}}(T_j)$$

其中 $R_{\text{on}}(T_j)$ 为结温相关的导通电阻，GaN HEMT 的 $R_{\text{on}}$ 具有正温度系数。

**阻断损耗**：
$$P_{\text{block}} = V_{\text{off}} \cdot I_{\text{leakage}}$$

其中 $I_{\text{leakage}}$ 为关断漏电流，通常极小可忽略。

**开关损耗**：
$$P_{\text{sw}} = f_{\text{sw}} \cdot (E_{\text{on}} + E_{\text{off}})$$

其中 $f_{\text{sw}}$ 为开关频率，$E_{\text{on}}$ 和 $E_{\text{off}}$ 分别为单次开通/关断能量损耗，由器件数据手册或实验测量获得。

### PFNN 模型时间步长灵活性

FTPNN 与 PFNN 的核心区别在于输出策略：

$$\text{FTPNN: } \{(t_0, v_0), (t_1, v_1), \ldots, (t_N, v_N)\}, \quad t_{n+1} - t_n = \Delta t_{\text{fixed}}$$

$$\text{PFNN: } \{(t_1, v_1), (t_2, v_2), \ldots, (t_n, v_n)\}, \quad t_{i+1} - t_i \text{ 自适应}$$

PFNN 输出点数 $n \ll N$，通过分段线性化插入中间点，等效步长可达 1-10 ns。

## 关键技术挑战

### 1. 纳秒级开关瞬态的精确建模

GaN HEMT 的开关过程通常在 10-50 ns 内完成，其中 dv/dt 可达数十 kV/$\mu$s，di/dt 可达数十 A/ns。在 EMT 仿真中，如果步长 $\Delta t$ 与开关时间相当或更大，将导致开关瞬态被过度平滑，无法准确反映电压电流的过冲、振铃和米勒平台效应。Zhang 等（2023）指出，传统 EMT 点-to-point 计算方法在 10 $\mu$s 步长下无法捕捉 GaN HEMT 的 10 ns 瞬态。

### 2. 寄生参数与高频振荡

GaN HEMT 的寄生电容（尤其是 $C_{\text{gd}}$ 米勒电容）和封装寄生电感会在开关瞬态引发高频振荡。这些振荡的频率可达数十 MHz，对电磁兼容性（EMC）和器件应力有重要影响。精确建模需考虑：
- 封装寄生电感 $L_{\text{source}}$、$L_{\text{drain}}$、$L_{\text{gate}}$
- 非线性寄生电容 $C_{\text{gd}}(V_{\text{gd}})$、$C_{\text{gs}}(V_{\text{gs}})$、$C_{\text{ds}}(V_{\text{ds}})$
- 栅极驱动电阻 $R_g$ 对开关速度的影响

### 3. 实时仿真的计算效率

GaN HEMT 的详细模型在 FPGA 上实现时面临计算资源约束。Zhang 等（2023）的 PFNN 方法在 Xilinx Ultrascale+ FPGA 上实现了 GaN HEMT 的实时 HIL 仿真，相比 FTPNN 方法显著降低了硬件资源消耗。然而，PFNN 的训练数据获取、特征点提取算法、以及神经网络在 FPGA 上的定点量化实现仍是开放问题。

### 4. 电热耦合效应

GaN HEMT 的导通电阻 $R_{\text{on}}$ 具有正温度系数，开关损耗随结温升高而增加。在长时间仿真或高功率应用中，电热耦合效应不可忽略。物理模型需包含热阻-热容网络：

$$C_{\text{th}} \frac{dT_j}{dt} = P_{\text{loss}} - \frac{T_j - T_a}{R_{\text{th}}}$$

其中 $T_j$ 为结温，$T_a$ 为环境温度，$P_{\text{loss}}$ 为总损耗功率。

## 量化性能边界

**开关速度**：GaN HEMT 的典型开关时间为 5-50 ns（Zhang 等 2023），开关频率可达数百 kHz 至 MHz。相比之下，Si IGBT 的开关时间为 1-10 $\mu$s，SiC MOSFET 为 50-200 ns。

**PFNN 等效步长**：Zhang 等（2023）的 PFNN 方法在 FPGA 上实现了变量时步仿真，等效输出步长可低至 1 ns。通过分段线性化插入中间数据点，在保持精度的同时大幅降低计算量。

**HIL 验证精度**：Zhang 等（2023）将 PFNN 的 FPGA 实时仿真结果与 PSCAD/EMTDC 离线仿真和 SaberRD 设备级瞬态仿真对比，验证了 PFNN 方法在 GaN HEMT 开关瞬态波形复现上的高精度。

**损耗估计效率**：Sinkar 等（2025）提出的 MMC 臂级半导体损耗估计方法，在 EMT 仿真中将损耗计算从单个开关器件级别提升到整个 MMC 臂级别，在保持精度的同时显著加速了仿真。

**FPGA 资源消耗**：Zhang 等（2023）的 PFNN 方法相比 FTPNN 方法，在 Xilinx Ultrascale+ FPGA 上显著降低了 LUT（Look-Up Table）和 DSP 资源消耗，主要得益于 PFNN 的稀疏输出策略。

## 适用边界与选择指南

### GaN HEMT 建模方法选择指南

| 应用场景 | 推荐模型 | 原因 |
|---------|---------|------|
| 系统级初步分析 | 理想开关模型 | 计算效率高，反映通断逻辑即可 |
| 稳态损耗与应力评估 | 稳态特性模型 | 多项式拟合输出特性，精度与效率平衡 |
| 开关瞬态波形分析 | 线性化/查表法 | 纳秒级步长，FPGA 单时钟周期计算 |
| 米勒平台/驱动电路研究 | 分段折线模型 | 精确反映开关瞬态各阶段波形 |
| 寄生参数敏感性分析 | 物理/行为模型 | 包含非线性电容和受控源 |
| FPGA 实时 HIL 仿真 | PFNN | 变量时步 1 ns，FPGA 并行加速 |
| MMC 臂级损耗评估 | 臂级损耗估计（Sinkar 2025） | 避免逐个开关建模，大幅加速 |

### 不适用的场景

- **低频系统仿真（<10 kHz）**：GaN HEMT 的超快开关特性在低频系统中影响较小，理想开关模型即可满足需求
- **纯系统级机电仿真**：机电暂态仿真步长为毫秒级，GaN HEMT 的纳秒级开关过程被完全平均化
- **器件物理设计**：GaN HEMT 的能带结构、2DET 载流子动力学等需使用 TCAD 工具（如 SILVACO、COMSOL），非 EMT 仿真范畴

## 相关方法 / 相关模型 / 相关主题

- [[models/converter/switching-model.md]] — 开关器件建模，GaN HEMT 的物理基础
- [[methods/control/power-electronics-control.md]] — 电力电子器件建模总论
- [[topics/simulation/fpga-real-time-simulation.md]] — GaN HEMT 常出现在硬件加速和 HIL 场景
- [[models/transformer/solid-state-transformer.md]] — 宽禁带器件在高频电力电子装备中的应用
- [[models/converter/grid-connected-inverter.md]] — 宽禁带器件在并网电力电子中的背景
- [[methods/transmission-line/wideband-modeling.md]] — 宽禁带器件与高频动态背景
- [[methods/power-electronics/half-bridge-submodule.md]] — 半桥子模块中的 GaN HEMT 应用
- [[methods/power-electronics/commutation-failure.md]] — 与 GaN HEMT 快速开关相关的换相过程
- [[methods/power-electronics/switching-function-method.md]] — 开关函数建模，GaN HEMT 简化建模方法

## 来源论文

| 论文 | 年份 | 说明 |
|------|------|------|
| [[sources/real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode.md|Zhang 等 2023]] | 2023 | PFNN/FTPNN 机器学习加速 WBG 器件建模，Xilinx Ultrascale+ FPGA 实时 HIL，变量时步可低至 1 ns |
| [[sources/analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-.md]] | 2026 | ADC 关联离散电路 GaN 半桥解析建模，统一导纳框架下 ZVS/inc-ZVS/硬开关无缝切换 |
| Sinkar 等 2025 | 2025 | MMC 臂级半导体损耗快速估计方法（原文未报告可核验数值结果） |

> 注：Sinkar 2025 论文尚未收录至 wiki/sources/，此处引用为方法论引用。
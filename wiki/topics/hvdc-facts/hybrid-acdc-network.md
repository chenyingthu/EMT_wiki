---
title: "混合交直流电网 (Hybrid AC/DC Network)"
type: topic
tags: [hybrid, acdc, network, hvdc, converter, mtdc, power-electronics]
created: "2026-05-02"
updated: "2026-05-18"
---

# 混合交直流电网 (Hybrid AC/DC Network)

## 定义与边界

混合交直流电网（Hybrid AC/DC Network）是指同时包含交流（AC）输电网和直流（DC）输电网的现代电力系统架构，其中直流侧可包括常规直流（LCC-HVDC）、柔性直流（VSC-HVDC）和多端直流（MTDC）等多种形态。这一架构在 EMT 仿真中的核心挑战在于**同时处理多时间尺度动态**——从微秒级开关换相到秒级机电暂态——而全系统按统一EMT步长仿真的计算代价难以承受。

混合交直流电网的 EMT 研究边界包括：
- 大规模 AC 电网 + VSC-MTDC 系统的协同仿真
- 含 MTDC 的异步电网互联（50Hz/60Hz）
- 新能源经 DC 汇集的外送系统
- 城市直流配电网与 AC 主网的互联

## 在EMT中的作用

混合交直流电网在 EMT 仿真中承担双重角色：

**（1）系统级研究平台**
混合仿真将系统划分为外部系统（ES，交流大电网，采用机电暂态或暂态稳定仿真）和详细系统（DS，含 VSC-MTDC，采用电磁暂态仿真），在接口处传递等效电气量，从而兼顾仿真精度与计算效率。典型接口位置在 VSC 换流器的公共连接点（PCC）。

**（2）换流器接口问题的研究对象**
混合交直流电网中，换流站附近的交流母线必须纳入 EMT 区域（buffer area sizing），以避免接口边界误差导致误导性结论。接口设计的核心问题包括：等效源更新频率、交互协议设计、故障期间相量提取精度。

[[topics/simulation/co-simulation]] - 协同仿真方法

## 网络架构

### 典型拓扑结构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg">
  <!-- AC Grids -->
  <rect x="20" y="30" width="120" height="60" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5" rx="4"/>
  <text x="80" y="55" text-anchor="middle" font-size="11" fill="#1e40af" font-family="sans-serif">AC Grid A</text>
  <text x="80" y="72" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">（交流电网）</text>
  <rect x="660" y="30" width="120" height="60" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5" rx="4"/>
  <text x="720" y="55" text-anchor="middle" font-size="11" fill="#1e40af" font-family="sans-serif">AC Grid B</text>
  <text x="720" y="72" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">（交流电网）</text>
  <!-- AC lines -->
  <line x1="140" y1="60" x2="240" y2="60" stroke="#333" stroke-width="1.5"/>
  <line x1="560" y1="60" x2="660" y2="60" stroke="#333" stroke-width="1.5"/>
  <line x1="240" y1="60" x2="560" y2="60" stroke="#333" stroke-width="1.5"/>
  <text x="400" y="50" text-anchor="middle" font-size="9" fill="#666" font-family="sans-serif">AC Transmission</text>
  <!-- Converter boxes -->
  <rect x="240" y="30" width="80" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="280" y="52" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">Conv. 1</text>
  <text x="280" y="65" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">(Rect.)</text>
  <text x="280" y="78" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">LCC</text>
  <rect x="360" y="30" width="80" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="400" y="52" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">Conv. 2</text>
  <text x="400" y="65" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">(Inv.)</text>
  <text x="400" y="78" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">VSC/MMC</text>
  <rect x="480" y="30" width="80" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="520" y="52" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">Conv. 3</text>
  <text x="520" y="65" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">(Inv.)</text>
  <text x="520" y="78" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">VSC/MMC</text>
  <!-- Vertical connections to DC bus -->
  <line x1="280" y1="90" x2="280" y2="150" stroke="#333" stroke-width="1.5"/>
  <line x1="400" y1="90" x2="400" y2="150" stroke="#333" stroke-width="1.5"/>
  <line x1="520" y1="90" x2="520" y2="150" stroke="#333" stroke-width="1.5"/>
  <!-- DC Bus -->
  <rect x="200" y="150" width="400" height="80" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" rx="4"/>
  <text x="400" y="175" text-anchor="middle" font-size="12" fill="#92400e" font-family="sans-serif">DC Transmission Network</text>
  <text x="400" y="195" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">Bipolar / Monopolar / Multi-terminal</text>
  <text x="400" y="215" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">线路阻抗 + 直流电抗器</text>
  <!-- DC line to renewable -->
  <line x1="400" y1="230" x2="400" y2="290" stroke="#333" stroke-width="1.5"/>
  <!-- Renewable converter -->
  <rect x="360" y="290" width="80" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="400" y="312" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">Conv. 4</text>
  <text x="400" y="325" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">(VSC)</text>
  <text x="400" y="338" text-anchor="middle" font-size="9" fill="#166534" font-family="sans-serif">新能源汇集</text>
  <line x1="400" y1="350" x2="400" y2="380" stroke="#333" stroke-width="1.5"/>
  <!-- Wind/PV -->
  <rect x="360" y="380" width="80" height="30" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5" rx="4"/>
  <text x="400" y="398" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">Wind/PV</text>
  <!-- Legend -->
  <rect x="620" y="180" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="640" y="191" font-size="9" fill="#333" font-family="sans-serif">AC系统</text>
  <rect x="620" y="200" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="640" y="211" font-size="9" fill="#333" font-family="sans-serif">换流站</text>
  <rect x="620" y="220" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="640" y="231" font-size="9" fill="#333" font-family="sans-serif">直流网络</text>
  <line x1="620" y1="248" x2="634" y2="248" stroke="#333" stroke-width="1.5"/>
  <text x="640" y="251" font-size="9" fill="#333" font-family="sans-serif">功率传输</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 混合交直流电网典型拓扑结构（LCC + VSC/MMC 多端直流）</p>

### 直流系统类型

| 类型 | 技术 | 容量 | 换相方式 | 典型应用 |
|------|------|------|---------|---------|
| LCC-HVDC | 晶闸管 | 1000–10000 MW | 电网换相 | 远距离大容量输电 |
| VSC-HVDC | IGBT/IGBT | 50–2000 MW | 自换相 | 弱电网互联、海上风电 |
| MTDC | VSC/MMC | 可变 | 自换相 | 区域电网互联、新能源汇集 |
| DC Grid | VSC/MMC | 可变 | 自换相 | 未来超级电网、广域调度 |

## 换流技术

### 线路换相换流器（LCC）

LCC 采用晶闸管作为开关器件，依赖交流系统电压进行换相。其 EMT 模型需要反映以下关键动态：

**换相过程**：换相电抗 $X_c$ 导致重叠角 $\mu$，换相失败风险随短路比（SCR）降低而增加。

**功率传输方程**：
$$P_{dc} = V_d \cdot I_d$$

$$V_d = \frac{3\sqrt{2}}{\pi} V_{LL} \cos\alpha - \frac{3}{\pi} X_c I_d$$

其中：
- $V_{LL}$：交流线电压有效值
- $\alpha$：触发滞后角
- $X_c$：换相电抗
- $\mu$：重叠角，$\cos\alpha - \cos(\alpha+\mu) = \frac{2X_c I_d}{\sqrt{2}V_{LL}}$

**故障穿越特性**：LCC-HVDC 需要交流系统提供无功支撑，SCR 降低时换相失败概率急剧上升，需要串联电抗器或静止无功补偿（SVC）辅助。

**EMT 建模要点**：LCC 的 EMT 模型需包含阀级开关模型（晶闸管导通/关断逻辑）、换相电抗耦合效应、以及换相失败期间的电流不均衡特性。

[[models/converter/lcc-model]] - LCC 换流器模型

### 电压源换流器（VSC）

VSC 采用 IGBT 自换相，不依赖交流系统电压，支持有功/无功独立控制。

**拓扑结构**：两电平、三电平、模块化多电平（MMC）。MMC 通过子模块（SM）串联实现高电压等级，输出电平数可达数百级。

**功率控制方程**：
$$P = \frac{V_s V_c}{X} \sin\delta$$
$$Q = \frac{V_s(V_s - V_c \cos\delta)}{X}$$

其中：
- $\delta$：换流器电压相对于交流系统电压的相角差
- $V_s$、$V_c$：交流系统电压和换流器电压幅值
- $X$：连接电抗

**控制器结构**（矢量控制）：
- 内环：$d$ 轴控制有功电流 $i_d$，$q$ 轴控制无功电流 $i_q$
- 外环：$V_{dc}$ 控制有功功率，$V_{ac}$（或 $Q$）控制无功功率
- PLL（锁相环）：提供 $dq$ 坐标系参考角度

[[models/converter/vsc-model]] - VSC 换流器模型

### 模块化多电平换流器（MMC）

MMC 是 VSC-HVDC 和 MTDC 的主流拓扑，由 $N$ 个子模块（SM）串联构成，每个子模块含电容和开关器件。

**输出电压**：
$$V_{out} = \sum_{k=1}^{N} S_k \cdot V_{cap,k}$$

其中 $S_k \in \{0,1\}$ 为第 $k$ 个子模块的开关状态，$V_{cap,k}$ 为其电容电压。

**桥臂动态方程**（每相上下桥臂）：
$$L_{arm} \frac{di_{arm}}{dt} = \frac{V_{dc}}{2} - R_{arm} i_{arm} - v_{arm}$$

**环流抑制**：MMC 三相桥臂间存在环流（$i_{circ}$），通过环流抑制控制器（CCC）消除：
$$v_{circ}^* = -K_p \cdot i_{circ} - K_i \int i_{circ} dt$$

[[models/converter/mmc-model]] - MMC 模型

## 混合仿真接口方法

混合仿真是同时运行 EMT 和暂态稳定（TS）仿真并通过接口交换数据的协同仿真方法。

### 系统分区

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 750 320" xmlns="http://www.w3.org/2000/svg">
  <!-- ES box -->
  <rect x="20" y="40" width="300" height="240" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="5"/>
  <text x="170" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af" font-family="sans-serif">外部系统（ES）</text>
  <text x="170" y="82" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">暂态稳定仿真 · 步长 1–20 ms</text>
  <!-- ES internal -->
  <rect x="40" y="95" width="260" height="40" fill="white" stroke="#93c5fd" stroke-width="1" rx="3"/>
  <text x="170" y="115" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">同步发电机 + 潮流 + 负荷</text>
  <rect x="40" y="145" width="260" height="40" fill="white" stroke="#93c5fd" stroke-width="1" rx="3"/>
  <text x="170" y="165" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">网络方程（电流注入牛顿法）</text>
  <rect x="40" y="195" width="260" height="40" fill="white" stroke="#93c5fd" stroke-width="1" rx="3"/>
  <text x="170" y="215" text-anchor="middle" font-size="10" fill="#1e40af" font-family="sans-serif">VSC 慢侧控制器</text>
  <!-- Interface node -->
  <rect x="320" y="145" width="110" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>
  <text x="375" y="168" text-anchor="middle" font-size="10" font-weight="bold" fill="#92400e" font-family="sans-serif">接口节点</text>
  <text x="375" y="183" text-anchor="middle" font-size="9" fill="#92400e" font-family="sans-serif">PCC</text>
  <text x="375" y="196" text-anchor="middle" font-size="9" fill="#92400e" font-family="sans-serif">（公共连接点）</text>
  <!-- Arrow ES → Interface -->
  <line x1="170" y1="235" x2="170" y2="290" stroke="#333" stroke-width="1.5"/>
  <line x1="170" y1="290" x2="320" y2="175" stroke="#333" stroke-width="1.5"/>
  <polygon points="316,172 326,175 316,178" fill="#333"/>
  <!-- Arrow Interface → ES -->
  <line x1="320" y1="175" x2="280" y2="175" stroke="#333" stroke-width="1.5"/>
  <polygon points="284,172 274,175 284,178" fill="#333"/>
  <text x="295" y="165" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">$\tilde{V}_{th}$</text>
  <text x="248" y="188" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">$\tilde{I}_{Norton}$</text>
  <!-- DS box -->
  <rect x="430" y="40" width="300" height="240" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>
  <text x="580" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534" font-family="sans-serif">详细系统（DS）</text>
  <text x="580" y="82" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">EMT仿真 · 步长 μs 级</text>
  <!-- DS internal -->
  <rect x="450" y="95" width="260" height="40" fill="white" stroke="#86efac" stroke-width="1" rx="3"/>
  <text x="580" y="115" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">MMC/VSC 换流器详细模型</text>
  <rect x="450" y="145" width="260" height="40" fill="white" stroke="#86efac" stroke-width="1" rx="3"/>
  <text x="580" y="165" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">DC 网络 + 线路/电缆模型</text>
  <rect x="450" y="195" width="260" height="40" fill="white" stroke="#86efac" stroke-width="1" rx="3"/>
  <text x="580" y="215" text-anchor="middle" font-size="10" fill="#166534" font-family="sans-serif">VSC 快侧控制器 + PLL</text>
  <!-- Arrow Interface → DS -->
  <line x1="375" y1="175" x2="430" y2="175" stroke="#333" stroke-width="1.5"/>
  <polygon points="426,172 436,175 426,178" fill="#333"/>
  <text x="400" y="165" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">$\tilde{V}_{th}$</text>
  <!-- DS → Interface -->
  <line x1="450" y1="175" x2="375" y2="175" stroke="#333" stroke-width="1.5"/>
  <polygon points="379,172 369,175 379,178" fill="#333"/>
  <text x="415" y="188" text-anchor="middle" font-size="8" fill="#666" font-family="sans-serif">$I_{ph}$</text>
  <!-- IP Protocol box -->
  <rect x="300" y="300" width="150" height="20" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" rx="3"/>
  <text x="375" y="313" text-anchor="middle" font-size="9" fill="#5b21b6" font-family="sans-serif">交互协议（IP）</text>
  <!-- Legend -->
  <text x="50" y="305" font-size="9" fill="#1e40af" font-family="sans-serif">蓝色：交流系统</text>
  <text x="450" y="305" font-size="9" fill="#166534" font-family="sans-serif">绿色：直流详细系统</text>
  <text x="280" y="330" font-size="9" fill="#92400e" font-family="sans-serif">黄色：接口界面</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图2 · 混合仿真系统分区与接口架构</p>

### 接口类型

#### Thevenin 等效接口（EMT 侧）

在 EMT 详细系统中，外部交流系统用时变 Thevenin 等效表示：
$$Z_{th} = \frac{V_{th}}{I_{sc}}$$
$$\tilde{v}_{th}(t) = \sqrt{2} |V_{th}| \cos(\omega_0 t + \angle V_{th})$$

Thevenin 阻抗可通过断路/短路测试或节点阻抗矩阵求得。阻抗更新需要网络方程矩阵的部分重新分解（re-factorization）。

**更新策略**：零阶保持（ZOH）直接使用上一个 TS 步长的值；一阶保持（FOH）通过线性外推近似 $Z_{th}$ 和 $V_{th}$ 在 EMT 步长内的变化：
$$\tilde{v}_{th}(t) = v_{th}[n] + \frac{t - t_n}{T_{es}} \left( v_{th}[n+1] - v_{th}[n] \right)$$

#### Norton 等效接口（TS 侧）

在 TS 外部系统中，详细系统用时变 Norton 电流源等效：
$$\tilde{I}_{Norton} = \frac{\tilde{V}_{ph}}{Z_{th}}$$

其中 $\tilde{V}_{ph}$ 通过 DFT 或曲线拟合从 EMT 瞬时量提取基频正序相量：
$$V_{ph} = \frac{1}{W} \sum_{k=0}^{W-1} v(k) \cdot e^{-j\omega_0 k \Delta t}$$

#### 接口位移原则

传统接口位于换流器 PCC 母线。van der Meer 等（2015）提出将接口从强电气耦合的 PCC 移到 EMT 子网内部控制环节或内部节点，利用控制与滤波惯性削弱分区延迟影响。

van der Meer 等（2015）提出将接口从强电气耦合的 PCC 移到 EMT 子网内部控制环节或内部节点，利用控制与滤波惯性削弱分区延迟影响。

### 交互协议（Interaction Protocol, IP）

交互协议定义 ES 和 DS 之间的计算顺序和数据交换时机：

| 协议 | ES→DS 数据 | DS→ES 数据 | 适用场景 |
|------|-----------|-----------|---------|
| IP1（EMT 优先）| TS 步长初的 $V_{th}$ | EMT 步长末的相量 | 正常稳态运行 |
| IP2（TS 优先）| TS 步长末的 $V_{th}$ | TS 步长内的相量序列 | DS 动态影响显著 |
| IP3（ZOH 故障处理）| 故障前后 ZOH | 故障期间连续相量 | 故障穿越期间 |
| IP4（自适应）| 可变窗口 + 自适应 $T_{es}$ | 逐步校正 | 复杂故障序列 |

**故障期间相量提取**（IP3/IP4）：交流故障后电压波形含谐波，直接 DFT 会产生误差。通过缩小窗口长度 $W$ 并在故障期间用插值外推代替常规相量计算，可提高精度。

van der Meer 等（2015）混合仿真接口技术

## AC/DC 接口稳定性

### 短路比（SCR）分析

SCR 是衡量弱电网接入能力的核心指标：
$$SCR = \frac{S_{sc}}{P_{dc}} = \frac{V_{ac}^2 / Z_{ac}}{P_{dc}}$$

| SCR 范围 | 系统类型 | EMT 建模要求 |
|---------|---------|------------|
| SCR > 3 | 强系统 | 可采用平均值模型 |
| 2 < SCR < 3 | 弱系统 | 需要详细开关模型 |
| SCR < 2 | 极弱系统 | 需 VSC 提供电压支撑 |

### 多馈入交互因子（MIIF）

多端直流系统中，换流站之间的交互强度用多馈入交互因子衡量：
$$MIIF_{ij} = \frac{\Delta V_i / V_i}{\Delta P_j / P_j}$$

其中 $\Delta V_i$ 为换流站 $j$ 功率扰动引起的换流站 $i$ 电压变化。MIIF 用于确定哪些交流母线必须纳入 EMT 区域（buffer area sizing）。

### 低电压穿越（FRT）特性

VSC-HVDC 的 FRT 保护包括：
- **交流侧过电流限制**：$|i_{ac}| \leq I_{max}$
- **无功电流升压**：故障期间注入 $Q_{fault} \geq 0.5 p.u.$
- **调制指数限幅**：$m \leq m_{max}$（防止直流电压过升）

FRT 状态机：Normal → FRT → post-FRT，状态转换由 PCC 电压幅值触发。

[[methods/protection-fault/dc-protection]] - 直流保护

## 直流保护

### 直流故障特性

直流故障电流特性（非限流情况）：
$$i_{fault}(t) = \frac{V_{dc}}{R_{dc}} \left(1 - e^{-t/\tau_{dc}}\right) + I_0 e^{-t/\tau_{dc}}$$

其中 $\tau_{dc} = L_{dc}/R_{dc}$ 为直流侧时间常数。

**故障电流上升率**：MMC 子模块电容放电导致故障电流在数毫秒内达到数十 kA，需要快速直流断路器（< 5 ms）。

### 保护策略

| 故障类型 | 检测方法 | 动作 | 限流措施 |
|---------|---------|------|---------|
| 直流线路接地 | $dV_{dc}/dt$ + 电压突降 | 直流断路器跳闸 + 再起动 | 平波电抗器 |
| 换相失败 | 电压畸变 + 电流不均衡 | 控制调节 + 闭锁 | 吸收电路 |
| 交流故障 | PCC 电压跌落 | 低压限流（UVCL） | STATCOM 支撑 |
| 阀故障 | 桥臂电流不平衡 | 阀闭锁 | 快速熔丝 |

### 直流断路器技术

| 类型 | 开断时间 | 额定电流 | 技术路线 |
|------|---------|---------|---------|
| 机械式 | 10–30 ms | 5–10 kA | 预充电电容换流 |
| 固态式 | < 1 ms | 1–5 kA | IGBT/SiC 串联 |
| 混合式 | 2–5 ms | 10–20 kA | 机械转移 + 固态限流 |

## 应用场景

### 远距离大容量输电

**典型工程案例**：

| 工程 | 电压 | 容量 | 拓扑 |
|------|------|------|------|
| 向家坝—上海 | ±800 kV | 6400 MW | LCC-HVDC |
| 锦屏—苏南 | ±800 kV | 7200 MW | LCC-HVDC |
| 鲁西背靠背 | ±350 kV | 1000 MW | VSC-MTDC |
| 舟山五端直流 | ±200 kV | 1000 MW | VSC-MTDC |

**效率优势**：直流输电损耗 $P_{loss} = I^2 R$，同等功率下直流电流小于交流，且无交流线路的充电功率问题。

[[topics/renewable-storage/renewable-energy-integration]] - 新能源并网

### 海上风电汇集

海上风电通过 VSC-HVDC 接入陆上交流系统：
- 交流电缆充电电流限制（> 50 km 交流电缆需做无功补偿）
- 直流输电无距离限制（100 km+ 海底电缆）
- VSC 可向海上平台提供电压支撑

**典型配置**：风电场 AC 汇集 → VSC 整流 → DC 海底电缆 → 陆上 VSC 逆变 → AC 电网。

### 城市电网升级

柔性直流配电网（Soft Open Point，SOP）替代传统联络开关：
- 实时功率控制（0–100% 双向潮流）
- 故障隔离（< 1 ms 换流）
- 储能/光伏即插即用接入

## 发展趋势

### 直流电网（DC Grid）

欧洲超级电网（SuperGrid）和全球能源互联网的愿景推动 DC Grid 发展：
- **多端双向功率流**：多个 VSC-MTDC 互联构成直流电网
- **直流潮流控制**：DC/DC 变换器调节直流电压分布
- **故障隔离与清除**：DC 断路器 + 故障自清除换流器（full-bridge MMC）

### 新型换流技术

**碳化硅（SiC）器件**：更高开关频率（> 10 kHz）、更低损耗（< 1%/电平）、更小体积，推动 DC/DC 变换器和直流断路器发展。

**器件级直流变压器**：SiC JFET + 矩阵变换器实现 AC/DC/AC 固态变压器，频率提升至 20–50 kHz，变压器体积减小 5–10 倍。

[[models/submodule/full-bridge-smb]] - 全桥子模块

### 多速率协同仿真框架

van der Meer 等（2015）多速率协同仿真框架（12.8× 加速比）

多速率协同仿真将含 MMC 的 MTDC 作为快子系统（μs 步长）、交流系统作为慢子系统（ms 步长），通过以下技术维持精度与稳定性：
- **时变 Thevenin/Norton 接口模型**
- **移动窗口预测 + 逐步校正**
- **接口振荡抑制离散化**

加速比相对于全 EMT 仿真可达 **12.8×**（van der Meer 2015）或更高（取决于接口效率）。

## 相关主题

- [[topics/simulation/co-simulation]] - 协同仿真
- [[topics/renewable-storage/electromechanical-electromagnetic-hybrid]] - 机电暂态混合仿真
- [[topics/modeling-methods/multirate-and-network-partitioning]] - 多速率方法与网络分區
- [[models/converter/vsc-model]] - VSC 模型
- [[models/converter/mmc-model]] - MMC 模型
- [[models/converter/lcc-model]] - LCC 模型
- [[methods/power-electronics/average-value-model]] - 平均值模型
- [[topics/simulation/time-domain-simulation]] - 时域仿真

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| van der Meer 等：Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems | 2015 | VSC-MTDC 混合仿真接口技术（Thevenin更新/FOH/IP3-IP4故障协议） |
| Li 等：Fault Area Discrimination Method for Parallel Multi-terminal Hybrid HVDC Line | 2019 | 多端混合 HVDC 故障区域判别 |
| Liu 等：The Averaged-value Model of a Flexible Power Electronics Based Substation in Hybrid ACDC Distribution | 2022 | 灵活电力电子变电站平均值模型 |
| Cao 等：Mitigation of Subsynchronous Interactions in Hybrid ACDC Grid With Renewable Energy | 2021 | 新能源并网混合系统 SSRI 抑制 |
| 叶华等：含VSC-HVDC交直流系统多尺度暂态建模与仿真研究 | 2017 | 含 VSC-HVDC 多尺度混合仿真 |
| Chen 等：A hybrid parallel computation algorithm and its application to multi-phase hybrid ACDC power system | 2010 | 多相混合 AC/DC 系统并行计算 |
| Rashidirad 等：Unified MANA-based load-flow for multi-frequency hybrid ACDC multi-microgrids | 2023 | 多频率混合 AC/DC 微电网统一 MANA 潮流 |
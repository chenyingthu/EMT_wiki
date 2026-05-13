---
title: "晶闸管旁路开关方法 (Thyristor Bypass Switch, TBS)"
type: method
tags: [tbs, thyristor-bypass-switch, bypass-protection, mmc-upfc, fast-bypass, fault-isolation, hybrid-mmc, protection-coordination]
created: "2026-05-04"
updated: "2026-05-13"
---

# 晶闸管旁路开关方法 (Thyristor Bypass Switch, TBS)

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="420" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">TBS 动作时序与保护协调流程</text>
  
  <!-- Phase 1: Normal operation -->
  <rect x="30" y="55" width="180" height="80" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="120" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#2563eb">正常运行态</text>
  <text x="120" y="100" text-anchor="middle" font-size="11" fill="#555">TBS 关断，主换流器导通</text>
  <text x="120" y="118" text-anchor="middle" font-size="11" fill="#555">电流经 MMC 桥臂流通</text>
  
  <!-- Arrow 1 -->
  <line x1="210" y1="95" x2="260" y2="95" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Phase 2: Fault detection -->
  <rect x="265" y="55" width="180" height="80" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="355" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#d97706">故障检测</text>
  <text x="355" y="100" text-anchor="middle" font-size="11" fill="#555">过流/欠压判据触发</text>
  <text x="355" y="118" text-anchor="middle" font-size="11" fill="#555">动作延迟 &lt; 0.5 ms</text>
  
  <!-- Arrow 2 -->
  <line x1="445" y1="95" x2="495" y2="95" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Phase 3: TBS firing -->
  <rect x="500" y="55" width="180" height="80" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="590" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#dc2626">TBS 触发导通</text>
  <text x="590" y="100" text-anchor="middle" font-size="11" fill="#555">晶闸管门极脉冲触发</text>
  <text x="590" y="118" text-anchor="middle" font-size="11" fill="#555">主电流转移至旁路 &lt; 2 ms</text>
  
  <!-- Arrow 3 -->
  <line x1="680" y1="95" x2="730" y2="95" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Phase 4: Mechanical bypass -->
  <rect x="735" y="55" width="150" height="80" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="810" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#16a34a">机械旁路合闸</text>
  <text x="810" y="100" text-anchor="middle" font-size="11" fill="#555">机械开关闭合</text>
  <text x="810" y="118" text-anchor="middle" font-size="11" fill="#555">TBS 关断，长时隔离</text>
  
  <!-- Bottom section: Key characteristics -->
  <rect x="30" y="160" width="855" height="100" rx="6" fill="#f0f9ff" stroke="#93c5fd" stroke-width="1"/>
  <text x="450" y="185" text-anchor="middle" font-size="13" font-weight="bold" fill="#2563eb">TBS 关键技术特征</text>
  
  <rect x="40" y="195" width="200" height="55" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="140" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">动作时间 &lt; 2 ms</text>
  <text x="140" y="233" text-anchor="middle" font-size="10" fill="#555">快于机械开关(10-50ms)</text>
  
  <rect x="260" y="195" width="200" height="55" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="360" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">电流转移比</text>
  <text x="360" y="233" text-anchor="middle" font-size="10" fill="#555">i_main → i_bypass</text>
  
  <rect x="480" y="195" width="200" height="55" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="580" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">跨接变压器绕组</text>
  <text x="580" y="233" text-anchor="middle" font-size="10" fill="#555">三相公共端接中性点</text>
  
  <rect x="700" y="195" width="175" height="55" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="787" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="#16a34a">与 DCCB 协同</text>
  <text x="787" y="233" text-anchor="middle" font-size="10" fill="#555">短时隔离 → 长时隔离</text>
  
  <!-- Application scenarios -->
  <rect x="30" y="280" width="420" height="120" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="240" y="305" text-anchor="middle" font-size="13" font-weight="bold" fill="#2563eb">MMC-UPFC 串联侧保护</text>
  <text x="45" y="325" font-size="10" fill="#333">• 苏州 500 kV UPFC：串联侧 2 个换流器各配 1 个 TBS</text>
  <text x="45" y="343" font-size="10" fill="#333">• 南京 220 kV UPFC：2 个串联换流变 + 1 个并联换流变</text>
  <text x="45" y="361" font-size="10" fill="#333">• 并联侧故障（Bus-21）：三相短路时 TBS 动作，单相不</text>
  <text x="45" y="379" font-size="10" fill="#333">• 动作时序：闭锁 MMC → 触发 TBS → 机械旁路合闸</text>
  
  <rect x="470" y="280" width="415" height="120" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="677" y="305" text-anchor="middle" font-size="13" font-weight="bold" fill="#d97706">混合型 MMC 子模块旁路</text>
  <text x="485" y="325" font-size="10" fill="#333">• HB-SM 闭锁：正向充电/反向旁路/截止 3 种状态</text>
  <text x="485" y="343" font-size="10" fill="#333">• FB-SM 闭锁：正向充电/反向充电/截止 3 种状态</text>
  <text x="485" y="361" font-size="10" fill="#333">• 二极管阈值导通：正向电压超过阈值时自动旁路</text>
  <text x="485" y="379" font-size="10" fill="#333">• 多样性 SM 统一外特性模型：开关函数 + 电容动态</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · TBS 动作时序与保护协调流程</p>

## 定义

晶闸管旁路开关（Thyristor Bypass Switch, TBS）是一种基于晶闸管（或 IGBT）的快速半导体开关装置，用于在故障或异常工况下将主换流器支路的电流快速转移至旁路支路，从而保护主功率器件免受过大电流或过电压应力的电磁暂态建模方法。

在 EMT 仿真中，TBS 的核心动作目标可形式化表示为：

$$i_{\text{main}}(t) \rightarrow i_{\text{bypass}}(t)$$

即在满足触发条件后，将主支路电流尽可能快地转移到旁路支路。这一电流转移过程必须在数毫秒内完成，远快于机械旁路开关的动作时间（通常 10-50 ms），因此 TBS 充当了"短时隔离"的桥梁角色。

TBS 在工程中的典型部署方式是：每一相 TBS 阀跨接在串联变压器绕组两端，三相 TBS 的公共端与串联变压器中性点连接（叶小晖 2019）。这种拓扑结构使得 TBS 能够在故障时提供低阻抗旁路通道，将故障电流从昂贵的电力电子换流阀中"分流"出去。

## EMT 中的角色

TBS 在电磁暂态仿真中承担三个关键角色：

**1. 换流阀快速保护**：在 MMC-UPFC、MMC-STATCOM 等柔性装置中，串联侧换流器直接承受线路故障电流。TBS 动作时间小于 2 ms（叶小晖 2019），可以在变压器机械旁路开关合闸前完成瞬时旁路，防止 IGBT/二极管因过电流而损坏。

**2. 故障电流转移路径**：TBS 为故障电流提供一条可控的半导体通路。在混合型 MMC 中，闭锁模式下子模块通过二极管实现自然旁路（连攀杰 2021），而在有控 TBS 场景中，通过门极触发实现主动电流转移，两者的暂态特性差异需要在 EMT 中精确刻画。

**3. 保护协调桥梁**：TBS 与 DCCB（直流断路器）、机械旁路开关、站级保护控制构成多级保护体系。Rault (2020) 描述了完整的动作链：故障检测 → TBS/DCCB 半导体换流 → 能量吸收（MOV）→ 机械隔离。EMT 仿真需要精确建模这一时间尺度跨越微秒到毫秒的协调过程。

## 核心建模方法

### 方法一：理想开关模型（理想导通/关断）

最简单的 TBS 建模将晶闸管视为理想开关：导通时电阻为零，关断时电阻为无穷大。该模型适用于初步的概念分析和保护逻辑验证。

$$R_{\text{TBS}} = \begin{cases} 0, & \text{导通 (fired)} \\ \infty, & \text{关断 (blocking)} \end{cases}$$

$$V_{\text{TBS}} = \begin{cases} 0, & \text{导通} \\ V_{\text{applied}}, & \text{关断且正向电压} \end{cases}$$

**适用场景**：保护逻辑开发、控制策略验证、大系统级仿真。
**局限性**：无法反映导通压降、换流过程暂态、反向恢复特性。

### 方法二：导通电阻 + 触发延迟模型（工程实用模型）

工程上最常用的 TBS 模型在理想开关基础上引入导通电阻 $R_{\text{on}}$ 和门极触发延迟 $t_{\text{delay}}$：

$$R_{\text{TBS}} = \begin{cases} R_{\text{on}}, & \text{导通} \\ R_{\text{off}}, & \text{关断} \end{cases}$$

其中 $R_{\text{on}}$ 通常为毫欧级（晶闸管通态电阻），$R_{\text{off}}$ 为兆欧级。触发延迟 $t_{\text{delay}}$ 从门极脉冲施加到主电流开始转移的时间，典型值为 0.5-2 ms。

该模型的电流转移过程可描述为：

$$i_{\text{bypass}}(t) = i_{\text{main}}(t) \cdot \left(1 - e^{-\frac{t - t_{\text{fire}}}{\tau}}\right) \cdot u(t - t_{\text{fire}})$$

其中 $t_{\text{fire}}$ 为触发时刻，$\tau = L_{\text{loop}} / (R_{\text{main}} + R_{\text{on}})$ 为电流转移时间常数，$L_{\text{loop}}$ 为旁路回路电感。

**适用场景**：MMC-UPFC 工程仿真（叶小晖 2019 采用的戴维南等效模型即基于此原理）、保护协调研究。
**优势**：计算效率高，能反映导通压降和转移时间。

### 方法三：戴维南/诺顿等效模型（高效 EMT 模型）

在大规模 EMT 仿真中，TBS 可与 MMC 桥臂一起纳入戴维南等效框架。叶小晖 (2019) 采用戴维南等效模型对 MMC 子模块进行等效，其中单个子模块的等效电阻和电压为：

$$R_{\text{SMEQ}} = \begin{cases} R_{\text{ON}} + R_C, & \text{投入} \\ R_{\text{ON}}, & \text{切除} \end{cases}$$

$$V_{\text{SMEQ}} = \begin{cases} V_C(t - \Delta t), & \text{投入} \\ 0, & \text{切除} \end{cases}$$

$$V_{\text{SM}} = I_{\text{SM}} R_{\text{SMEQ}} + V_{\text{SMEQ}}$$

其中 $R_C = \Delta t / C$ 为电容的后退欧拉等效电阻，$\Delta t$ 为仿真步长。当 TBS 导通时，等效电路中的相应支路电阻从 $R_{\text{ON}} + R_C$ 突变为 $R_{\text{ON}}$，实现电流的快速重新分配。

**适用场景**：大规模电力系统 EMT 仿真、含 UPFC 的机电-电磁混合仿真。
**优势**：与 EMT 程序的伴随模型（companion model）框架兼容，保持节点导纳矩阵稀疏性。

### 方法四：混合型 MMC 闭锁二极管模型

在混合型 MMC（连攀杰 2021；李亚楼 2020）中，TBS 的概念延伸到子模块级别的"自然旁路"机制。闭锁模式下，IGBT 全部关断，子模块通过二极管实现自动旁路：

**半桥子模块（HB-SM）闭锁状态**：
- 正向充电：$i_{\text{arm}} > 0$，二极管导通，电容接入电路
- 反向旁路：$i_{\text{arm}} < 0$，二极管导通，电容被短接（旁路）
- 截止：反向电压超过二极管阈值，关断

**全桥子模块（FB-SM）闭锁状态**：
- 正向充电：$i_{\text{arm}} > 0$，特定二极管组合导通，电容接入
- 反向充电：$i_{\text{arm}} < 0$，另一组二极管导通，电容反向接入
- 截止：所有二极管关断

李亚楼 (2020) 提出基于开关函数的统一动态平均化等值方法，将多样性子模块的串联结构统一建模：

$$u_{\text{scp}}(t) = \sum_{i=1}^{k} u_{\text{co},i}(t) = \sum_{i=1}^{k} S_i(t) u_{\text{ci}}(t) = \sum_{i=1}^{k} S_i(t) \left( \frac{1}{C_i} \int_{t_0}^{t} S_i(t) i_{\text{sc}}(t) \mathrm{d}t + u_{\text{ci}}(t_0) \right)$$

其中 $S_i(t)$ 为第 $i$ 个子模块的开关函数（投切状态），$u_{\text{ci}}(t)$ 为电容电压。该模型在不改变电路结构的情况下，通过开关函数参数化实现不同类型子模块的统一仿真。

**适用场景**：混合型 MMC 全状态仿真、多样性子模块选型对比。
**优势**：统一模型具有良好的可移植性，通过参数定义子模块类型即可切换。

## TBS 动作时序与保护协调

TBS 在工程中的典型动作时序（叶小晖 2019；Rault 2020）如下：

**第一阶段：故障检测（0-0.5 ms）**
过流/欠压判据触发保护动作。在 MMC-UPFC 并联侧故障场景中，Bus-21 三相短路故障在 4.0 s 触发，保护系统在 <0.5 ms 内检测到故障特征。

**第二阶段：TBS 触发导通（0.5-2 ms）**
触发 TBS 晶闸管门极脉冲，主电流开始向旁路转移。苏州 500 kV UPFC 工程中，TBS 动作时间小于 2 ms，在变压器机械旁路开关合闸前完成短时隔离。

**第三阶段：机械旁路合闸（2-50 ms）**
机械旁路开关闭合，TBS 关断，故障电流由机械开关承担，实现长时隔离。这一阶段 TBS 退出运行，由机械开关承担持续导通任务。

与 DCCB 的协调（Rault 2020）：
- **半导体换流阶段**：混合 DCCB 的主分支（MB）由 n 个半导体单元串联组成，每个单元 rated voltage 80 kV，通过换流将直流电流转移到并联 MOV 支路
- **UFD 动作阶段**：超快速隔离开关（Ultra-Fast Disconnector, UFD）在电流中断期间承受直流电压绝缘
- **LCS 换流阶段**：负载换流开关（Load Commutation Switch, LCS）使电流转移到辅助支路
- **MOV 能量吸收**：非线性压敏电阻分段线性化建模，吸收故障能量 $W_{\text{abs}} = \int v_{\text{MOV}}(t) \cdot i(t) \, dt$

## 形式化表达

### TBS 等效电路参数

| 参数 | 符号 | 典型值/范围 | 说明 |
|------|------|------------|------|
| 导通电阻 | $R_{\text{on}}$ | 0.01-0.1 Ω | 晶闸管通态电阻 |
| 关断电阻 | $R_{\text{off}}$ | 10⁶-10⁹ Ω | 晶闸管阻断电阻 |
| 触发延迟 | $t_{\text{delay}}$ | 0.5-2 ms | 门极脉冲到导通 |
| 旁路回路电感 | $L_{\text{loop}}$ | 0.1-10 mH | 旁路路径寄生电感 |
| 转移时间常数 | $\tau$ | $L_{\text{loop}}/(R_{\text{main}}+R_{\text{on}})$ | 电流转移速度 |

### 戴维南等效模型关键公式

电容后退欧拉离散化：
$$V_C(t) = V_C(t - \Delta t) + I_C \frac{\Delta t}{C} = V_C(t - \Delta t) + I_C R_C$$

其中 $R_C = \Delta t / C$ 为戴维南等效电阻，$\Delta t$ 为仿真步长。

子模块端口电压：
$$V_{\text{SM}} = I_{\text{SM}} R_{\text{SMEQ}} + V_{\text{SMEQ}}$$

桥臂等效电压和电阻（连攀杰 2021）：
$$u_{\text{arm,eq}}(t) = u_{\text{all\_sm,eq}}^{\text{HB}}(t) + u_{\text{all\_sm,eq}}^{\text{FB}}(t) + u_L(t)$$

$$R_{\text{arm,eq}}(t) = R_{\text{all\_sm,eq}}^{\text{HB}}(t) + R_{\text{all\_sm,eq}}^{\text{FB}}(t)$$

### 开关函数统一模型

多样性子模块串联结构的统一动态平均化模型（李亚楼 2020）：
$$u_{\text{scp}}(t) = \sum_{i=1}^{k} S_i(t) \left( \frac{1}{C_i} \int_{t_0}^{t} S_i(t) i_{\text{sc}}(t) \mathrm{d}t + u_{\text{ci}}(t_0) \right)$$

## 关键技术挑战

### 1. 电流转移暂态的精确建模

TBS 导通瞬间，主支路和旁路支路之间的电流转移涉及寄生电感和分布参数的动态过程。转移时间常数 $\tau = L_{\text{loop}} / (R_{\text{main}} + R_{\text{on}})$ 决定了电流重新分配的速度。在 EMT 仿真中，如果步长 $\Delta t$ 与 $\tau$ 相当或更大，将导致转移过程被过度平滑，无法准确反映换流瞬态的过冲和振荡。

### 2. 闭锁模式下的二极管自然旁路

混合型 MMC 在闭锁模式下，子模块通过二极管实现自动旁路。连攀杰 (2021) 指出，部分 MMC 等效模型在闭锁模式下仍在进行不必要的电容电压排序，影响了计算效率。正确区分 HB-SM 和 FB-SM 在闭锁模式下的不同工作状态（正向充电/反向旁路/截止）是精确建模的关键。

### 3. 多级保护协调的时间尺度跨越

TBS 动作涉及从微秒级（门极触发）到毫秒级（机械开关合闸）的宽时间尺度。Rault (2020) 的 HIL 仿真表明，需要同时处理半导体开关的纳秒级动态（寄生电容/电感）和机械开关的毫秒级运动。这种多时间尺度的统一仿真对 EMT 程序的步长策略提出了挑战。

### 4. 多样性子模块的统一建模

李亚楼 (2020) 指出，混合型 MMC 可采用半桥、全桥、钳位双子模块、五电平交叉等多种子模块拓扑，每种拓扑的闭锁特性和等效模型不同。传统戴维南等值算法需要进行硬编码，降低了模型的工程移植性。统一外特性模型通过开关函数参数化解决了这一问题。

## 量化性能边界

**动作时间**：苏州 500 kV UPFC 工程中，TBS 动作时间小于 2 ms（叶小晖 2019）。这一速度远快于机械旁路开关（10-50 ms），但慢于纯半导体 DCCB 的换流时间（<5 ms，Rault 2020）。

**保护选择性**：在 MMC-UPFC 并联侧故障仿真中（叶小晖 2019），Bus-21 三相短路故障（4.0 s 触发，持续 0.1 s）导致所有接口方案中的 TBS 均发生动作；而单相短路故障下，TBS 未动作。这表明 TBS 对故障类型具有选择性响应。

**仿真效率**：连攀杰 (2021) 的混合型 MMC 全状态高效仿真方法在闭锁模式下通过将二极管等效替换为固定电阻，将内部节点数量从 6 个（单桥臂）降低到 1-2 个，仿真效率提升显著。李亚楼 (2020) 的统一外特性模型在 ADPSS 中验证，与分立元件详细模型对比，稳态误差 <1%，暂态误差 <3%，仿真速度提升 10-50 倍。

**MOV 能量吸收**：Rault (2020) 将 MOV 建模为 V/I 分段线性曲线（5-10 段），在 EMTP-RV 中验证了能量吸收的精确性。混合 DCCB 的半导体单元额定电压 80 kV，70 mH 限流电感。

## 适用边界与选择指南

### TBS  vs 其他保护方法的适用场景对比

| 应用场景 | 推荐方法 | 原因 |
|---------|---------|------|
| MMC-UPFC 串联侧故障保护 | TBS + 机械旁路 | 苏州 500 kV UPFC 工程验证，2 ms 级动作足以保护换流阀 |
| 混合型 MMC 闭锁保护 | 二极管自然旁路 + 统一外特性模型 | 无需额外硬件，利用子模块固有二极管特性 |
| 多端直流电网故障隔离 | DCCB（混合/全半导体） | 需要主动切断直流电流，TBS 无法开断持续电流 |
| 大规模系统机电-电磁混合仿真 | 戴维南等效 TBS 模型 | 保持节点导纳矩阵稀疏性，与 PSD-PS Model 兼容 |
| 子模块选型对比研究 | 开关函数统一模型 | 通过参数切换子模块类型，无需重新建模 |

### 不适用的场景

- **持续直流电流开断**：TBS 是半导体开关，导通后无法主动关断直流电流（晶闸管需自然过零），因此不能替代 DCCB 执行故障隔离功能
- **高频开关应用**：TBS 的触发延迟（0.5-2 ms）不适合 PWM 级别的开关频率需求，此时应使用 IGBT 或 SiC MOSFET
- **超高速保护（<1 ms）**：对于行波保护要求的 <1 ms 动作时间（Verrax 2022），TBS 的触发延迟可能不足，需配合更快的半导体开关

## 相关方法 / 相关模型 / 相关主题

- [[dccb]] — 直流断路器建模，与 TBS 构成多级保护体系
- [[dc-protection]] — 直流故障保护判据与动作逻辑
- [[thyristor-control]] — 晶闸管触发控制策略
- [[mmc-model]] — MMC 换流器建模，TBS 的主要部署对象
- [[mmc-hvdc]] — MMC-HVDC 系统级建模
- [[submodule]] — 子模块拓扑，TBS 在子模块级别的延伸
- [[half-bridge-submodule]] — 半桥子模块，闭锁时通过二极管自然旁路
- [[full-bridge-smb]] — 全桥子模块，闭锁时具有更灵活的旁路状态
- [[commutation-failure]] — 换相失败，与 TBS 电流转移过程相关
- [[switching-model]] — 开关器件建模，TBS 的物理基础
- [[circuit-breaker-model]] — 断路器建模，TBS 与机械开关的协调
- [[statcom-model]] — STATCOM 装置，TBS 同样适用于 STATCOM 保护
- [[hybrid-converter]] — 混合型换流器，TBS 在混合拓扑中的应用
- [[power-electronics-control]] — 电力电子装置控制，TBS 触发逻辑的上位控制
- [[upfc-model]] — UPFC 装置模型，TBS 在 UPFC 串联侧的直接应用
- [[protection-system]] — 保护系统框架，TBS 的保护协调背景
- [[switching-transient]] — 开关瞬态分析，TBS 动作引发的暂态过程
- [[mmc-upfc电磁-机电混合仿真技术研究]] — MMC-UPFC 电磁-机电混合仿真，TBS 工程应用的直接来源

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| 叶小晖 等 - MMC-UPFC电磁-机电混合仿真技术研究 | 2019 | TBS 在 MMC-UPFC 串联侧的工程部署、动作时序（<2 ms）、戴维南等效建模、并联侧故障仿真验证 |
| 连攀杰 等 - 混合型MMC全状态高效电磁暂态仿真方法研究 | 2021 | 混合型 MMC 闭锁模式下子模块二极管自然旁路特性、HB-SM/FB-SM 三种闭锁状态、等效模型优化 |
| 李亚楼 等 - 多样性子模块混合型MMC统一外特性高效电磁暂态模型 | 2020 | 基于开关函数的统一动态平均化等值、多样性子模块（半桥/全桥/钳位双子模块/五电平交叉）统一建模 |
| Rault 等 - Real-time simulation with an industrial DCCB controller in a HVDC grid | 2020 | 混合 DCCB 半导体换流与 TBS 的协调、MOV 分段线性化建模、HIL 仿真验证 |
| Le-Huy & Tremblay - Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation | 2023 | 混合型 SVC 中晶闸管开关（TSC/TCR）的 HIL 建模方法，TBS 建模思路的延伸参考 |

---
title: "故障穿越 (Fault Ride-Through)"
type: topic
tags: [fault-ride-through, low-voltage-ride-through, grid-code, inverter, renewable-energy, lvrt, fvrt, zvrt, grid-support]
created: "2026-05-04"
updated: "2026-05-17"
---

# 故障穿越 (Fault Ride-Through)

## 定义与边界

故障穿越（Fault Ride-Through, FRT）是指电网发生故障导致电压跌落（或升高）时，并网设备维持并网运行、支撑电网恢复的能力要求。低电压穿越（Low Voltage Ride-Through, LVRT）是 FRT 的主要形式，要求设备在电压跌落期间不脱网，并按需提供无功电流支撑。

**边界限定**：本页面聚焦于并网准则对 FRT 的要求及 EMT 仿真中的验证方法，不替代具体设备控制设计或电网保护整定。

FRT 与以下概念的区别：
- **脱网（Trip-off）**：设备因故障而主动断开，是 FRT 的对立面
- **低电压穿越（LVRT）**：FRT 的子集，专门针对电压跌落场景
- **高电压穿越（HVRT）**：FRT 的子集，针对电压升高场景

## EMT 中的作用

FRT 是新能源并网研究的核心议题，在 EMT 仿真中承担以下关键角色：

| 目标 | 场景 | 关键技术 |
|------|------|----------|
| 并网准则验证 | 验证设备是否满足电网公司 FRT 要求 | 三相短路、两相短路、单相接地测试用例 |
| 设备应力评估 | 分析故障期间设备承受的过电流、过电压 | 撬棒电路、斩波电阻、IGBT 限流 |
| 系统稳定性 | 评估大规模新能源 FRT 行为对系统暂态稳定的影响 | 多机协调、机电-电磁混合仿真 |
| 保护配合 | 分析 FRT 与线路保护、脱网保护的动作配合 | 保护时序、恢复曲线 |

## 主要分支与机制

### 1. 低电压穿越 (LVRT)

电压跌落期间保持并网，是 FRT 研究的核心：

**电压-时间耐受曲线**：定义可接受的电压跌落深度和持续时间。中国风电场标准（GB/T 19963）的典型要求：
- 电压跌至 20% 额定值时，至少维持 625 ms 不脱网
- 电压在 2 s 内恢复至 90%，持续并网运行

**无功电流注入**：电压跌落时按比例注入无功电流支撑电压恢复（Q式）：

$$I_q^* = K_q \cdot (0.9 - V_{pu}) \cdot I_N, \quad V_{pu} < 0.9$$

其中 $K_q$ 为无功支撑系数（通常 1.5~2.0），$I_N$ 为额定电流。

**有功功率恢复**：故障清除后快速恢复有功输出，恢复斜率通常限定为 30%~50% 额定功率/秒。

### 2. 高电压穿越 (HVRT)

电压升高期间保持并网：
- **感性无功吸收**：通过升压变压器吸收多余无功
- **过电压耐受**：设备需承受 1.1~1.3 p.u. 电压而不脱网
- **典型场景**：无功过剩、负荷突降导致电压升高

### 3. 零电压穿越 (ZVRT)

极端故障下（如三相短路导致电压完全丧失）的并网保持：
- 对同步电机和换流器的极限考验
- 部分地区电网的特殊要求
- 需要设备在 0~5% 额定电压下维持控制能力

### 4. 构网型设备的 FRT 特性

构网型（Grid-Forming, GFM）设备的 FRT 特性与跟网型不同：
- **主动电压支撑**：GFM 设备在故障期间主动建压，而非跟随电网
- **故障电流能力**：GFM 设备可提供 1.5~2.0 p.u. 短路电流
- **无缝模式切换**：GFM 可在并网模式和离网模式间无缝切换

## 形式化表达

### LVRT 电压-时间耐受边界

$$T_{\text{ride-through}}(V_{pu}) = \begin{cases}
t_1 & V_{pu} \geq V_1 \text{ (持续)} \\
t_2 & V_2 \leq V_{pu} < V_1 \\
t_3 & V_3 \leq V_{pu} < V_2 \\
\text{脱网} & V_{pu} < V_3
\end{cases}$$

典型参数（中国 GB/T 19963.1-2021）：
- $V_1 = 0.90$ p.u.，$t_1 = \infty$（持续运行）
- $V_2 = 0.20$ p.u.，$t_2 = 625$ ms（最低耐受时间）
- $V_3 = 0.05$ p.u.，可能触发脱网保护

### 直流母线电压动态

故障期间直流侧功率不平衡导致电压抬升：

$$\frac{1}{2}C_{dc}\frac{dV_{dc}^2}{dt} = P_{in} - P_{out}$$

其中 $P_{in}$ 为发电机侧功率，$P_{out}$ 为电网侧功率。故障期间 $P_{out}$ 受限，需通过撬棒（crowbar）或斩波电阻耗散多余功率：

$$P_{\text{chopper}} = \frac{V_{dc}^2}{R_{\text{chopper}}}$$

### FRT 期间电流应力

过电流限制通常采用$I^2t$ 准则：

$$I_{\text{max}}(t) = \sqrt{\frac{1}{t}\int_0^t i^2(\tau)d\tau} \leq I_{\text{thermal}}$$

对于 IGBT 模块，典型热极限为 $2 \times I_{\text{rated}}$ 持续 1 s。

### 无功支撑容量

无功电流注入比例需满足：

$$\frac{I_q}{I_N} \geq K_{\text{grid}} \cdot (1 - V_{pu}), \quad K_{\text{grid}} \geq 1.5$$

各国电网代码要求的最小无功支撑系数：
| 电网代码 | $K_{\text{grid}}$ 最小值 | 参考电压 |
|---------|------------------------|---------|
| IEEE 1547-2018 | 1.0 | 0.9 p.u. |
| GB/T 19963 | 1.5 | 0.9 p.u. |
| ENTSO-E | 2.0 | 0.85 p.u. |
| BDEW | 2.5 | 0.8 p.u. |

## 关键技术挑战

### 挑战 1：撬棒保护与恢复特性

撬棒电路（Crowbar）在故障时短接 IGBT 以旁路故障电流，但切除后会引入恢复暂态：
- 撬棒电阻 $R_{cb}$ 通常取 0.1~0.5 p.u.
- 撬棒持续时间：5~20 ms
- 恢复时直流电压可能出现二次抬升

### 挑战 2：锁相环（PLL）暂态失锁

深度电压跌落会导致 PLL 跟踪失败，引起有功/无功振荡：
- 带宽自适应 PLL 可在故障期间降低带宽
- DSOGI-PLL 在序分量域提取正序电压，受不平衡影响小

### 挑战 3：多机协调与系统稳定性

大规模新能源场站中多台设备同时 FRT 可能引发：
- 无功电压调控过冲（多台设备同时注入无功）
- 有功功率恢复时域重叠（恢复斜率叠加导致频率扰动）

### 挑战 4：构网型设备的主动支撑

GFM 设备在 FRT 期间面临：
- 电流限制与电压建立的矛盾（内环饱和）
- 模式切换瞬态（并网→离网→并网）的平滑过渡

## 量化性能边界

**中国 GB/T 19963.1-2021 风电场 LVRT 要求**：
- 电压跌至 0.20 p.u.：最低维持 625 ms 不脱网
- 电压恢复至 0.90 p.u. 时间：≤ 2 s
- 无功电流支撑系数：≥ 1.5（电压 < 0.9 p.u. 时）
- 有功功率恢复斜率：≥ 10% 额定功率/s

**双馈风机（Type-3 DFIG）典型 FRT 性能**：
- 撬棒电阻激活阈值：0.75 p.u.（部分文献）
- 撬棒持续时间：5~15 ms
- 故障清除后有功恢复时间：0.5~2 s

**全功率变换器风机（Type-4 PMSG）典型 FRT 性能**：
- 直流 Chopper 激活阈值：1.05~1.10 p.u.（直流电压）
- 无功电流响应时间：< 5 ms
- 故障清除后无缝恢复

## 适用边界与选择指南

| 应用场景 | 推荐模型 | 原因 |
|---------|---------|------|
| LVRT 并网准则验证 | 三相短路 EMT 测试 | 标准测试用例，验证脱网边界 |
| 不平衡故障 FRT | 两相短路、单相接地 EMT | 评估序分量交互 |
| 新能源场站聚合 | 平均值模型 + 等效阻抗 | 大规模系统实时性要求 |
| GFM 设备 FRT | 详细开关模型 + GFM 控制 | 主动电压建立需详细模型 |
| 撬棒电路设计 | 详细开关模型 + thermal coupling | IGBT 过流保护设计 |

### 失效边界

- **深度电压跌落**：超出设备设计耐受极限（< 0.15 p.u. 持续 > 1 s）
- **长时间故障**：超过故障穿越时间边界（如 > 2 s）
- **连锁故障**：多点故障导致电压无法恢复
- **设备过流/过压**：FRT 期间保护装置动作导致提前脱网
- **频率失稳**：大规模脱网导致频率崩溃

### 关键假设

1. 电网故障可检测且设备能及时响应（响应时间 < 5 ms）
2. 故障清除后电压可恢复至 0.9 p.u. 以上
3. 设备功率器件能承受故障期间过电流（< 2×额定值）
4. 多台设备 FRT 行为不会恶化系统稳定性

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">故障穿越（FRT）EMT 仿真决策流程</text>
  
  <!-- Input -->
  <rect x="350" y="48" width="200" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">设备 + 电网模型</text>
  <text x="450" y="82" text-anchor="middle" font-size="10" fill="#666">风电/光伏/储能+系统</text>
  
  <!-- Arrow -->
  <line x1="450" y1="88" x2="450" y2="115" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- FRT Type Decision -->
  <polygon points="450,120 600,170 450,220 300,170" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="160" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">FRT 类型？</text>
  <text x="450" y="175" text-anchor="middle" font-size="10" fill="#d97706">LVRT/HVRT/ZVRT</text>
  
  <!-- Three paths -->
  <!-- LVRT -->
  <line x1="600" y1="170" x2="700" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="700" y="180" width="150" height="40" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="775" y="200" text-anchor="middle" font-size="11" font-weight="bold" fill="#16a34a">LVRT</text>
  <text x="775" y="214" text-anchor="middle" font-size="9" fill="#666">无功支撑 I_q*</text>
  
  <!-- ZVRT -->
  <line x1="450" y1="220" x2="450" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="375" y="260" width="150" height="40" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="280" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">ZVRT</text>
  <text x="450" y="294" text-anchor="middle" font-size="9" fill="#666">零电压/GFM建压</text>
  
  <!-- HVRT -->
  <line x1="300" y1="170" x2="200" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="50" y="180" width="150" height="40" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="125" y="200" text-anchor="middle" font-size="11" font-weight="bold" fill="#dc2626">HVRT</text>
  <text x="125" y="214" text-anchor="middle" font-size="9" fill="#666">过电压/感性吸收</text>
  
  <!-- Key checks -->
  <!-- Crowbar check -->
  <rect x="650" y="260" width="200" height="40" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="750" y="280" text-anchor="middle" font-size="10" font-weight="bold" fill="#dc2626">撬棒/Chopper 激活？</text>
  
  <!-- PLL check -->
  <rect x="375" y="320" width="150" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="340" text-anchor="middle" font-size="10" font-weight="bold" fill="#d97706">PLL 跟踪？</text>
  
  <!-- Output -->
  <rect x="350" y="320" width="200" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="340" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">FRT 验证结果</text>
  
  <!-- Connect to output -->
  <line x1="750" y1="300" x2="750" y2="340" stroke="#333" stroke-width="1.5"/>
  <line x1="750" y1="340" x2="550" y2="340" stroke="#333" stroke-width="1.5"/>
  <line x1="550" y1="340" x2="550" y2="320" stroke="#333" stroke-width="1.5"/>
  <line x1="550" y1="320" x2="450" y2="320" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Legend -->
  <rect x="50" y="370" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="68" y="380" font-size="9" fill="#666">输入/输出</text>
  <rect x="130" y="370" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="148" y="380" font-size="9" fill="#666">判断</text>
  <rect x="190" y="370" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="208" y="380" font-size="9" fill="#666">LVRT</text>
  <rect x="240" y="370" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="258" y="380" font-size="9" fill="#666">ZVRT/GFM</text>
  <rect x="310" y="370" width="12" height="12" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="328" y="380" font-size="9" fill="#666">HVRT/保护</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 故障穿越（FRT）EMT 仿真决策流程</p>

## 与相关页面的关系

- [[gfl-inverter-model]] — 跟网型逆变器及 FRT 控制
- [[gfm-inverter-model]] — 构网型逆变器故障特性
- [[dfig-model]] — 双馈风机 FRT 与保护
- [[pmsm-model]] — 直驱风机 FRT 特性
- [[fault-analysis-methods]] — 故障分析方法
- [[renewable-energy-integration]] — 可再生能源并网
- [[electromagnetic-transient]] — 电磁暂态
- [[power-system-network]] — 电力系统网络

## 来源论文

- **GB/T 19963.1-2021** — 风电场接入电力系统技术规定，中国风电场 LVRT 要求（电压跌至 20% 额定值时维持 625 ms 不脱网）
- **IEEE Std. 1547-2018** — 分布式资源并网标准，北美 FRT 要求（无功支撑系数 ≥ 1.0）
- **ENTSO-E Grid Code** — 欧洲电网并网准则，HVRT 要求（1.05~1.10 p.u. 持续时间）

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献和标准。*
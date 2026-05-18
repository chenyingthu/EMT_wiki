---
title: "微电网与配电网 (Microgrid and Distribution Network)"
type: topic
tags: [microgrid, distribution-network, dg, islanding, protection, emt, droop-control, grid-forming]
created: "2026-05-01"
book-chapter: "23"
updated: "2026-05-18"
---

# 微电网与配电网 (Microgrid and Distribution Network)

## 定义与边界

微电网是由分布式电源（DG）、储能、负荷和控制系统组成的低压配电系统，可运行于**并网模式**（PCC闭合，与大电网交换功率）或**孤岛模式**（PCC断开，本地自治供能）。配电网是连接输电网与终端用户的电力网络，正经历从传统单向供电向双向潮流、高比例分布式能源接入的转型。

**边界定义**：微电网强调自治性（并离网切换能力），配电网强调拓扑结构（辐射状或环网）与电压等级（10kV/0.4kV配电变压器）。两者在分布式电源渗透率>30%时面临共性挑战——双向潮流、保护失效、稳定性劣化。

## EMT中的作用

EMT仿真在微电网与配电网领域的核心应用：

1. **并离网切换暂态分析**：PCC断开/闭合瞬间的电压/频率恢复过程，需捕捉变流器控制模式切换
2. **电能质量评估**：DG谐波注入、电压波动、闪变分析，需开关级精度
3. **保护配合校核**：DG故障电流受逆变器限流影响（通常1.1–1.5 p.u.）后，传统过流保护的整定失效
4. **稳定性分析**：低惯量微电网中下垂控制/VSM控制与弱电网的交互稳定性
5. **多微网交互**：多ACMG/DCMG通过互联变流器（IC）互连时的谐波交互与功率分配

## 微电网拓扑结构

### 交流微电网（ACMG）

典型结构包括分布式电源（光伏、风电、微型燃气轮机）、储能（电池、超级电容）、敏感/可控负荷与静态转移开关（STS）。控制层次上，设备级采用P/Q控制或下垂控制，系统级采用微网能量管理（EMS），上级由配电网调度协调。

### 直流微电网（DCMG）

优势在于无频率/相位问题、减少AC/DC变换环节，更适合数据中心与EV充电站。电压等级通常为380V/750V/1500V。DC bus通过双向AC/DC变换器与交流母线互联。

### 混合交直流微电网（Hybrid ACMG/DCMG）

交流母线与直流母线并存，不同类型DG和负荷按接入端口分区管理，通过双向AC/DC变流器（Interlinking Converter, IC）实现功率互济。各ACMG可运行于不同频率（孤岛ACMG频率作为潮流变量），这是混合微电网与纯AC微电网的本质区别。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- 颜色方案: 蓝=输入/源, 绿=处理/控制, 黄=算法/方法, 紫=输出/性能 -->
  <!-- 第一层: 物理系统输入 -->
  <rect x="10" y="10" width="880" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">物理系统输入（能量来源与负荷）</text>
  <text x="130" y="52" text-anchor="middle" font-size="11" fill="#1e3a8a">光伏阵列</text>
  <text x="130" y="70" text-anchor="middle" font-size="10" fill="#3b82f6">DC/DC-MPPT</text>
  <text x="300" y="52" text-anchor="middle" font-size="11" fill="#1e3a8a">风电 PMSG</text>
  <text x="300" y="70" text-anchor="middle" font-size="10" fill="#3b82f6">DC/DC</text>
  <text x="470" y="52" text-anchor="middle" font-size="11" fill="#1e3a8a">储能 BESS</text>
  <text x="470" y="70" text-anchor="middle" font-size="10" fill="#3b82f6">双向 DC/DC</text>
  <text x="630" y="52" text-anchor="middle" font-size="11" fill="#1e3a8a">交流负荷</text>
  <text x="630" y="70" text-anchor="middle" font-size="10" fill="#3b82f6">居民/商业/工业</text>
  <text x="790" y="52" text-anchor="middle" font-size="11" fill="#1e3a8a">配电网</text>
  <text x="790" y="70" text-anchor="middle" font-size="10" fill="#3b82f6">SCR ≥ 3 或 <3</text>

  <!-- 箭头 1→2 -->
  <line x1="450" y1="90" x2="450" y2="125" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333"/></marker></defs>

  <!-- 第二层: 微电网控制架构 -->
  <rect x="10" y="130" width="880" height="100" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="150" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">微电网控制架构（分层控制体系）</text>
  <!-- 一次控制 -->
  <rect x="30" y="165" width="170" height="55" rx="6" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="115" y="182" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">一次控制（设备级）</text>
  <text x="115" y="198" text-anchor="middle" font-size="10" fill="#15803d">P/Q 控制 / 下垂控制</text>
  <text x="115" y="212" text-anchor="middle" font-size="10" fill="#15803d">VSM 虚拟同步机</text>
  <!-- 二次控制 -->
  <rect x="220" y="165" width="170" height="55" rx="6" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="305" y="182" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">二次控制（系统级）</text>
  <text x="305" y="198" text-anchor="middle" font-size="10" fill="#15803d">频率/电压恢复</text>
  <text x="305" y="212" text-anchor="middle" font-size="10" fill="#15803d">SOC 均衡管理</text>
  <!-- 三次控制 -->
  <rect x="410" y="165" width="170" height="55" rx="6" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="495" y="182" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">三次控制（优化）</text>
  <text x="495" y="198" text-anchor="middle" font-size="10" fill="#15803d">经济调度 / 需求响应</text>
  <text x="495" y="212" text-anchor="middle" font-size="10" fill="#15803d">多微网功率互济</text>
  <!-- IC互联 -->
  <rect x="600" y="165" width="130" height="55" rx="6" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="665" y="182" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">互联变流器 IC</text>
  <text x="665" y="198" text-anchor="middle" font-size="10" fill="#15803d">AC/DC 功率互济</text>
  <text x="665" y="212" text-anchor="middle" font-size="10" fill="#15803d">频率解耦</text>
  <!-- PCC/STS -->
  <rect x="750" y="165" width="120" height="55" rx="6" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="810" y="182" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">并网点 PCC</text>
  <text x="810" y="198" text-anchor="middle" font-size="10" fill="#15803d">STS 静态开关</text>
  <text x="810" y="212" text-anchor="middle" font-size="10" fill="#15803d">同步检测</text>

  <!-- 箭头 2→3 -->
  <line x1="450" y1="230" x2="450" y2="265" stroke="#333" stroke-width="2"/>
  <polygon points="445,260 455,260 450,270" fill="#333"/>

  <!-- 第三层: 变流器建模层级（EMT核心） -->
  <rect x="10" y="275" width="880" height="80" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">变流器 EMT 建模层级（五类模型精度-效率映射）</text>
  <rect x="30" y="310" width="140" height="35" rx="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="100" y="326" text-anchor="middle" font-size="10" fill="#92400e">SW 详细开关</text>
  <text x="100" y="340" text-anchor="middle" font-size="9" fill="#b45309">Δt ≤ 1 μs</text>
  <rect x="190" y="310" width="140" height="35" rx="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="260" y="326" text-anchor="middle" font-size="10" fill="#92400e">VI 电压源等效</text>
  <text x="260" y="340" text-anchor="middle" font-size="9" fill="#b45309">Δt ≤ 10 μs</text>
  <rect x="350" y="310" width="140" height="35" rx="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="420" y="326" text-anchor="middle" font-size="10" fill="#92400e">AV 平均值</text>
  <text x="420" y="340" text-anchor="middle" font-size="9" fill="#b45309">Δt ≤ 50 μs</text>
  <rect x="510" y="310" width="140" height="35" rx="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="580" y="326" text-anchor="middle" font-size="10" fill="#92400e">CCI 斩波简化</text>
  <text x="580" y="340" text-anchor="middle" font-size="9" fill="#b45309">Δt ≤ 100 μs</text>
  <rect x="670" y="310" width="140" height="35" rx="5" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="740" y="326" text-anchor="middle" font-size="10" fill="#92400e">SCI 标幺谐波</text>
  <text x="740" y="340" text-anchor="middle" font-size="9" fill="#b45309">Δt ≤ 500 μs</text>

  <!-- 箭头 3→4 -->
  <line x1="450" y1="355" x2="450" y2="390" stroke="#333" stroke-width="2"/>
  <polygon points="445,385 455,385 450,395" fill="#333"/>

  <!-- 第四层: EMT分析场景 -->
  <rect x="10" y="400" width="880" height="80" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="420" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">EMT 分析场景与多微网交互</text>
  <rect x="30" y="435" width="155" height="35" rx="5" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="107" y="451" text-anchor="middle" font-size="10" fill="#5b21b6">并离网切换</text>
  <text x="107" y="465" text-anchor="middle" font-size="9" fill="#7c3aed">无缝切换 < 100 ms</text>
  <rect x="205" y="435" width="155" height="35" rx="5" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="282" y="451" text-anchor="middle" font-size="10" fill="#5b21b6">谐波/电能质量</text>
  <text x="282" y="465" text-anchor="middle" font-size="9" fill="#7c3aed">THD < 5% (GB)</text>
  <rect x="380" y="435" width="155" height="35" rx="5" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="457" y="451" text-anchor="middle" font-size="10" fill="#5b21b6">故障暂态</text>
  <text x="457" y="465" text-anchor="middle" font-size="9" fill="#7c3aed">DC bus 跌落/恢复</text>
  <rect x="555" y="435" width="155" height="35" rx="5" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="632" y="451" text-anchor="middle" font-size="10" fill="#5b21b6">多微网交互</text>
  <text x="632" y="465" text-anchor="middle" font-size="9" fill="#7c3aed">多频率 ACMG</text>
  <rect x="730" y="435" width="140" height="35" rx="5" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="800" y="451" text-anchor="middle" font-size="10" fill="#5b21b6">保护配合</text>
  <text x="800" y="465" text-anchor="middle" font-size="9" fill="#7c3aed">自适应整定</text>

  <!-- 图例 -->
  <rect x="30" y="490" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="50" y="502" font-size="10" fill="#333">输入/源</text>
  <rect x="120" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="140" y="502" font-size="10" fill="#333">控制架构</text>
  <rect x="230" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="250" y="502" font-size="10" fill="#333">变流器建模</text>
  <rect x="370" width="14" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="390" y="502" font-size="10" fill="#333">EMT分析场景</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 微电网EMT仿真五层架构：物理系统输入 → 分层控制 → 变流器建模层级 → EMT分析场景</p>

## 微电网控制策略

### 下垂控制（Droop Control）

下垂控制模拟同步发电机的频率-有功、电压-无功特性，通过本地测量实现多DG的功率分配，无需通信。

**有功-频率下垂（P-f）**：
$$f = f_0 - m_p(P - P_0)$$

**无功-电压下垂（Q-V）**：
$$V = V_0 - n_q(Q - Q_0)$$

其中 $m_p$ 和 $n_q$ 为下垂系数，决定功率分配精度与响应速度的权衡。典型设计准则：功率分配误差 < 5%，频率偏差 < 0.2 Hz（分层控制后）。

### 虚拟同步机（VSM）

VSM在控制环中引入惯性模拟，使逆变器具有同步机的转动惯量特性：
$$J\frac{d\omega}{dt} = T_m - T_e - D(\omega - \omega_0)$$

其中 $J$ 为虚拟惯量，$T_m$ 为机械功率参考，$T_e$ 为电磁功率，$D$ 为阻尼系数。VSM控制可使微电网等效惯量增加3–5倍，显著提升抗扰动能力。

### 分层控制体系

| 层次 | 控制内容 | 时间尺度 | 实现方式 |
|------|---------|---------|---------|
| 一次控制 | 本地下垂/VSM | 毫秒级 | 本地PI/离散控制 |
| 二次控制 | 频率/电压恢复 | 秒级 | 集中通信或分布式 |
| 三次控制 | 经济优化调度 | 分钟级 | 能量管理系统EMS |

## 构网型变流器的EMT建模

### 初始化方法（CISS/DI）

大型微电网EMT仿真的首要问题是正确初始化工作点。两种主流方法：

**电流注入接口法（CISS）**：利用潮流相量和换流器参数解析计算外环PI积分器初值。具体步骤：① 从PCC电压相量反推换流器内部参考电压（KVL）；② 由直流电压标幺化关系转d轴量；③ 由电压环关系反解PI积分状态$h$。适用于可读取控制器参数的白盒模型。

**直接接口法（DI）**：通过接口辅助源将GVSC与交流孤岛临时电气解耦，使黑盒模型也能独立进入稳态后再重耦合。适用于黑盒变流器（参数不可得）的初始化。

### PQ运行域约束

构网型逆变器（GFM）的P/Q指令受两类硬约束限制：

1. **额定电流约束**：PCC电流幅值不能超过额定值，$|I_{PCC}| \leq I_{rated}$
2. **PWM饱和约束**：逆变器可合成的交流电压幅值受直流母线和调制方式限制，$|V_{inv}| \leq M \cdot V_{dc}/2$（其中$M$为调制比）

GFM的PQ能力边界与滤波器拓扑（L/LC/LCL）、PCC电压、直流母线电压密切相关，需在EMT模型中显式建模以评估给定工况下的可运行区域。

### 构网型与跟网型并联稳定性

构网型（GFM）与跟网型（GFL）逆变器并联时，存在控制交互稳定性问题。RMS模型可能将实际不稳定情形误判为稳定——因为控制环与网络特征频率可能不再满足时间尺度分离假设。EMT仿真是评估此类交互风险的必要手段。

## 多微网与互联变流器

### 多频率孤岛ACMG的MANA潮流

多ACMG互联时，每个ACMG可运行于不同频率（孤岛AC子网频率作为潮流变量之一）。Rashidirad 2023将多频MMG写成统一MANA（改进增广节点分析）潮流问题，Jacobian矩阵中非对角块表达IC与AC/DC侧的耦合：

$$J_{MMG} \cdot \Delta X_{MMG} = -f_{MMG}$$

未知量包括各ACMG变量（节点电压、频率）、DCMG变量（直流电压、节点电流）和IC接口量，在统一Jacobian中同时求解电压、电流、内部电压、频率和IC接口量。

### FPGA亚微秒实时仿真

微电网含大量电力电子开关（20 kHz量级开关频率，要求步长≤500 ns）。Xu 2020提出网络解耦算法：变流器用固定导纳开关模型（开关状态变化不改变主导纳矩阵结构，通过等效历史源/支路量更新），配电线路/电缆用π型等效电路经LIM分布式求解，各DG子系统通过线路接口解耦并行计算，将微电网级亚微秒实时仿真推进到单块Kintex-7 410T FPGA。

### MMC-BESS储能系统

含嵌入式BESS的模块化多电平换流器（MMC-BESS）需保留开关级暂态行为。IDEM（改进详细等效模型）在DEM框架内专门处理"双开关同时关断"情形：闭锁用PSCAD辅助开关和内置插值处理过零，电池断开用补充判据决定二极管等效状态，并加入加速计算以减少开关网络求解负担。

## 配电网建模方法

### 配电线路模型选择

| 应用场景 | 推荐模型 | 关键考量 |
|---------|---------|---------|
| 稳态潮流 | 集总参数π型 | 收敛性优先 |
| 短路计算 | 等效电压源 | 精度优先 |
| 谐波分析 | 频域模型 | 谐波阻抗 |
| 暂态过电压 | EMT详细 | 波过程 |
| 保护整定 | EMT详细 | 故障电流 |
| 电能质量 | 时域仿真 | 波形畸变 |

短线路（<10 km）用集总参数π型等值；中等线路（10–50 km）考虑电容效应或Bergeron模型；长线路（>50 km）用频变参数模型或ULM通用线路模型。

### 配电变压器模型

配电变压器建模需关注：① 饱和特性（励磁电流非线性）；② 有载调压（OLTC，±10%范围）；③ 组别连接（Yyn0，Dyn11等）。配电网中柱上变压器（10kV/0.4kV）通常用非线性饱和模型以捕捉暂态过电压。

### 负荷模型

| 负荷类型 | 特性 | EMT建模要点 |
|---------|------|------------|
| 居民负荷 | 时变性（日负荷曲线）、多样性 | 静态ZIP模型 + 随机扰动 |
| 商业负荷 | 空调、照明为主，谐波源 | 谐波阻抗模型 |
| 工业负荷 | 大电机启动、冲击负荷 | 动态等效电路 + 启动电流 |

## 微电网保护策略

### 保护挑战

微电网双向潮流使传统过流保护面临严峻挑战：DG故障电流受逆变器限流（约1.1–1.5 p.u.），远低于同步机短路电流（3–5 p.u.），导致保护正确动作率下降。据测算，高比例DG接入使传统过流保护误动率增加20–40%。

### 自适应保护方案

**方向过流保护**：利用方向元件判断故障电流方向，区分上游（配电网侧）和下游（微电网侧）故障。自适应定值根据DG出力和运行模式动态调整保护阈值。

**差动保护**：适用于微电网内部母线、变压器和重要馈线的保护，需要通信通道。

**孤岛检测**：被动式（过/欠频、过/欠压）存在检测盲区（Non-Detection Zone, NDZ）；主动式（阻抗检测、频率偏移）可缩小检测盲区至<2%额定功率不匹配，但会引入小扰动。

### 保护定值

| 保护类型 | 定值设置 | 动作延时 |
|---------|---------|---------|
| 过电流 | 1.5–2倍额定 | 0.1–0.5 s |
| 速断 | 5–10倍额定 | 0 s |
| 零序过流 | 0.2–0.5倍额定 | 0.1–0.3 s |
| 过/欠频 | ±0.5–1 Hz | 0.1–0.5 s |
| 过/欠压 | ±10%额定 | 0.1–0.5 s |

## 并离网切换

### 切换过程

**并网转孤岛**：① 检测电网故障（被动/主动）；② 断开并网开关（STS）；③ DG由电流控制模式转为电压控制模式（V/f控制）；④ 负荷频率/电压恢复。

**孤岛转并网**：① 检测电网恢复（同步检测）；② PCC处频率、相位、电压同步（预同步）；③ 闭合并网开关；④ DG由电压控制模式转为电流控制模式（P/Q控制）。

### 无缝切换条件

$$\text{电压匹配}: |V_{micro} - V_{grid}| < 5\%$$
$$\text{频率匹配}: |f_{micro} - f_{grid}| < 0.1 \text{ Hz}$$
$$\text{相位匹配}: |\theta_{micro} - \theta_{grid}| < 10°$$

实测数据：预同步控制使切换冲击电流 < 1.5倍额定，储能缓冲使切换过程频率跌落 < 0.5 Hz。

## 关键技术挑战

1. **弱电网稳定性（SCR < 3）**：下垂控制在弱电网下可能不稳定，需增加虚拟阻抗（Virtual Impedance）以改善阻尼
2. **多频率ACMG潮流初始化**：多孤岛ACMG以不同频率运行，每个ACMG频率作为Jacobian变量，MANA统一求解是当前最优方法
3. **谐波交互**：LCL滤波器谐振与DG控制环交互可能导致1–5 kHz频段振荡，EMT开关模型是唯一可信的分析手段
4. **故障电流受限**：逆变器限流导致DG故障电流仅1.1–1.5 p.u.，传统保护整定失效，需自适应保护
5. **黑启动能力**：大规模光伏-储能电站作为黑启动电源时，变压器励磁、线路充电和负荷阶跃暂态强耦合，EMT详细模型是必选

## 量化性能边界

| 指标 | 典型值 | 数据来源 |
|------|--------|---------|
| 下垂控制功率分配误差 | < 5% | 工程设计准则 |
| VSM等效惯量提升 | 3–5倍 | Wang 2018 |
| 分层控制频率偏差 | < 0.2 Hz | 分层控制标准 |
| 分层控制电压偏差 | < 3% | 分层控制标准 |
| DG故障电流限幅 | 1.1–1.5 p.u. | IEEE 1547 |
| 保护误动率（高DG） | +20–40% | 工程统计 |
| 自适应保护正确率 | ≥ 95% | Liu 2019 |
| 无缝切换相位差 | < 10° | Xu 2017 |
| 切换冲击电流 | < 1.5倍额定 | Zhang 2020 |
| 切换频率跌落 | < 0.5 Hz | Cao 2023 |
| 孤岛检测盲区 | < 2%功率不匹配 | Zheng 2022 |
| FPGA实时步长 | ≤ 500 ns | Xu 2020 |

## 适用边界与选择指南

| 场景 | 推荐方案 | 原因 |
|------|---------|------|
| 微电网并网稳态分析 | 下垂控制 + AV模型 | 步长50 μs，精度足够 |
| 孤岛暂态切换 | 下垂/VSM + SW模型 | Δt≤1 μs捕捉快动态 |
| 谐波振荡分析 | LCL/LC滤波器 + SW模型 | 开关精度必要 |
| 故障电流计算 | 详细开关模型 + 自适应保护 | 故障电流精度关键 |
| 实时硬件在环 | CISS初始化 + VI模型 | 平衡精度与速度 |
| 多微网交互研究 | MANA潮流 + EMT混合仿真 | 多频率初始化基础 |
| FPGA亚微秒仿真 | 网络解耦 + VI模型 | 并行计算优势 |

## 相关方法

- [[models/control/droop-control-model.md]] — 分布式电源有功-频率/无功-电压下垂控制
- [[models/converter/grid-forming-inverter.md]] — 构网型变流器（VSM/PSL控制）
- [[methods/power-electronics/average-value-model.md]] — 逆变器快速仿真平均值模型
- [[methods/numerical-methods/numerical-integration.md]] — 微电网暂态数值积分方法
- [[topics/simulation/co-simulation.md]] — EMT与机电暂态混合仿真

## 相关模型

- [[models/renewable-storage/pv-system-model.md]] — 分布式光伏EMT建模
- [[models/rotating-machine/dfig-model.md]] — 分布式风电EMT建模
- [[models/renewable-storage/bess-model.md]] — 电池储能系统EMT建模
- [[models/basic-component/load-model.md]] — 配电网负荷模型
- [[models/converter/vsc-model.md]] — 电压源换流器通用模型

## 相关主题

- [[topics/component-modeling/load-and-dg-modeling.md]] — 分布式电源详细建模
- [[topics/protection-lightning/protection-relay-modeling.md]] — 配电网保护配合
- [[topics/hvdc-facts/vsc-hvdc.md]] — 电压源换流器HVDC技术
- [[topics/simulation/co-simulation.md]] — 多时间尺度混合仿真
- [[methods/control/frequency-control.md]] — 微电网频率控制

## 技术演进脉络

### 2000s–2010s：微电网概念兴起
- **CERTS微电网**：美国提出微电网概念，下垂控制成为多DG协调控制基础
- **示范工程**：欧洲、日本微电网示范（希腊Kythros岛、德国Rabble等）
- **储能集成**：Battery Energy Storage System（BESS）提升微网灵活性

### 2010s–2020s：高比例DG接入
- **主动配电网**：从被动到主动管理，需求响应参与调度
- **虚拟同步机**：构网型控制技术，惯量支撑与阻尼特性
- **数字孪生**：微网在线监测与优化运维

### 2020s–2026：多微网与能源互联网
- **微电网集群**：多微网协调运行，功率互济与电压支撑
- **能源互联网**：微网作为节点参与大系统优化
- **数字孪生**：实时数字孪生与AI驱动的能量管理

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
---
title: "交直流混合系统 (Hybrid AC/DC System)"
type: topic
tags: [hybrid-acdc, vsc-hvdc, lcc-hvdc, mtdc, co-simulation, multirate, emt-simulation]
created: "2026-05-04"
updated: "2026-05-14"
---

# 交直流混合系统 (Hybrid AC/DC System)

## 定义

交直流混合系统（Hybrid AC/DC System）是指由交流电网与高压直流输电系统（HVDC）互联构成的电力系统，通过换流站实现交流电与直流电的相互转换。这类系统中，交流侧通常采用相量模型（phasor-domain）描述低频动态过程，而直流侧（尤其是基于电力电子换流器的 VSC-HVDC 或 LCC-HVDC）需要采用电磁暂态（EMT）模型捕捉毫秒至微秒级的快速暂态过程。

**核心特征**：交直流混合系统的本质挑战在于**多时间尺度耦合**——交流系统的机电暂态时间常数在秒至百毫秒量级，而直流换流器的电磁暂态过程在微秒至毫秒量级。二者通过换流站接口紧密耦合，导致仿真时面临"步长矛盾"：若统一采用 EMT 小步长（1~50 μs），则大规模交流系统的仿真计算量呈指数增长；若采用机电暂态大步长（0.01~1 s），则无法捕捉换相失败、直流故障等快速暂态过程。

**边界限定**：本页面聚焦于高压直流输电与交流电网互联的系统级建模与仿真方法，涵盖 LCC-HVDC、VSC-HVDC、MMC-MTDC 等主流拓扑，不包括纯交流或纯直流系统。

## EMT中的角色

交直流混合系统在 EMT 仿真中的核心角色可归纳为四类关键任务：

1. **多直流多馈入稳定性分析**：评估交流系统故障引发的多回直流同时换相失败（LCC-HVDC）或闭锁（VSC-HVDC），以及由此引发的连锁故障。实际系统中已多次发生交流故障导致多回直流同时换相失败的事故 [Chen 2020]。

2. **换相失败与直流暂态过程**：LCC-HVDC 特有的换相失败过程、直流线路故障、直流功率调制对交流系统的动态影响。换相失败涉及毫秒级的换流阀关断角动态，必须使用 EMT 模型才能准确捕捉 [Xiong 2020]。

3. **新能源并网动态评估**：大规模风电/光伏通过 HVDC 外送时，交流侧低频振荡与直流侧快速控制的交互作用。Lin 等 [2021] 在 IEEE 39 母线系统 + CIGRE B4 直流网格的仿真中，展示了 DFIG 风电场通过 MMC-HVDC 接入时对交流电压稳定性的影响。

4. **机电-电磁混合仿真**：在大规模交直流电网中，将直流输电及其周边区域采用 EMT 建模、其余交流电网采用机电暂态建模，以兼顾仿真精度和规模。这是国网和南网运行方式计算的重要工具 [Chen 2020]。

**关键挑战**：
- **接口稳定性**：不同时间尺度的子系统通过等效模型耦合时，接口模型（Thevenin/Norton 等效）的更新频率和数值离散方式直接影响整体仿真稳定性
- **多时间尺度协调**：交流侧大步长与直流侧小步长之间的同步机制（重同步、波形松弛、多速率迭代）
- **控制交互**：VSC 的 PLL、电流内环、功率外环与 LCC 的触发角控制、VDCOL 在混合系统中的交互行为

## 四层次仿真方法体系

交直流混合系统的 EMT 仿真方法可按"建模粒度→仿真架构→数值方法→计算加速"四个层次组织。

### 第一层：全电磁暂态（Full EMT）建模

全 EMT 方法对交直流混合系统的所有元件（交流线路、变压器、换流器、直流线路、负荷）均采用电磁暂态建模，使用统一的小时间步长（通常 1~50 μs）。

**核心建模方法**：

1. **交流系统 EMT 建模**：采用节点导纳矩阵法，将每条线路建模为 π 型等效电路或行波模型（Bergeron 模型、JMarti 频变模型）。同步发电机采用六阶或更高阶暂态模型，包含转子运动方程 [Lin 2021]：

$$\frac{d\omega_r(t)}{dt} = -\frac{F}{J}\omega_r(t) + \frac{P}{J}(T_e(t) - T_m(t))$$

其中 $P$ 为极对数，$J$ 为转动惯量，$F$ 为阻尼系数，$T_e$ 为电磁转矩，$T_m$ 为机械转矩。电磁转矩的计算为：

$$T_e = \frac{3}{2}P(x_{d}\lambda_{q} - x_{q}\lambda_{d})$$

2. **LCC-HVDC EMT 建模**：采用 12 脉波换流阀（双桥六脉冲）建模，换流器通过换流变压器与交流系统相连。直流电压算式为 [Chen 2020]：

$$V_0 = \frac{3BX_C}{\pi}I_d \cdot \frac{\cos\alpha + \cos(\alpha+\mu)}{2}$$

其中 $B$ 为六脉冲换流器个数，$X_C$ 为换相电抗（取换流变漏抗 $X_T$），$\alpha$ 为触发角，$\mu$ 为换相角。换相角由下式确定：

$$\mu = \arccos(\cos\alpha - \frac{2nX_T I_d}{U_s}) - \alpha$$

逆变侧关断角 $\gamma = \mu - \beta$，正常运行时 $\gamma$ 稳态值约为 17° [Xiong 2020]。

3. **VSC-HVDC EMT 建模**：采用平均值模型（AVM）或详细开关模型。AVM 将 VSC 等效为时变电压源，功率平衡方程为 [van der Meer 2015]：

$$P_{ac} = P_{dc} = V_{dc} \cdot I_{dc}$$

VSC 的 d-q 坐标系下矢量控制方程为：

$$\vec{E}_{abc} = E_d^{ref} + j\frac{E_q^{ref}}{2}$$

其中 $E_d^{ref} = V_{dc}^{ref}$，$E_q^{ref} = 0$（无功为零时）。通过 KVL 可得 PCC 电压关系 [Allabadi 2024]：

$$\vec{V}_{PCC}^{LF} - \vec{I}_{ac}(Z_{tr} + j\frac{X_{Larm}}{2}) = \vec{E}_{abc}^{ref}$$

4. **MMC-HVDC EMT 建模**：MMC 由上下两个桥臂组成，每个桥臂包含 $N$ 个子模块（SM）。SM 电容电压动态为 [Lin 2021]：

$$v_{SM}(t) = i_{SM}r_{on} + \frac{1}{C}\int i_{SM}(t)dt + (g_1 - \text{sgn}(i_{SM}))^2V_f + (g_1 + \text{sgn}(i_{SM}) - 1)V_j$$

桥臂电压方程为：

$$v_{arm}^{m}(t) = (Z_{Lu/d} + R_{Lu/d})i_{arm}(t) + \frac{1}{N}\sum v_{SM}(t-\Delta) + 2v_L^{(i)}(t)$$

### 第二层：机电-电磁混合仿真（EM-EMT Hybrid）

机电-电磁混合仿真的核心思想是：将需要高精度仿真的区域（直流输电及其周边交流区域）采用 EMT 建模，其余大规模交流电网采用机电暂态（TS）建模，通过接口等效模型实现耦合。

**接口等效方法**：

混合仿真通过戴维南/诺顿等效在机电侧与电磁侧之间建立接口 [Xiong 2020]。接口等效示意图如图 1 所示。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect x="0" y="0" width="900" height="420" fill="#fafafa" stroke="#e0e0e0" stroke-width="1"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#333" font-weight="bold">图1 · 机电-电磁混合仿真接口架构</text>
  
  <!-- EMT Region (right) -->
  <rect x="480" y="55" width="380" height="140" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="670" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#92400e" font-weight="bold">电磁暂态子网 (EMT)</text>
  
  <!-- EMT components -->
  <rect x="510" y="95" width="80" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="550" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">换流站1</text>
  
  <rect x="600" y="95" width="80" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="640" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">换流站2</text>
  
  <rect x="690" y="95" width="80" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="730" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">直流线路</text>
  
  <rect x="510" y="135" width="80" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="550" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">换流变压器</text>
  
  <rect x="600" y="135" width="80" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="640" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">滤波器组</text>
  
  <rect x="690" y="135" width="80" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="730" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">控制系统</text>
  
  <rect x="510" y="175" width="260" height="15" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="640" y="187" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">步长: 1~50 μs | 详细拓扑建模</text>
  
  <!-- TS Region (left) -->
  <rect x="40" y="55" width="420" height="140" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="250" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#1e40af" font-weight="bold">机电暂态子网 (TS)</text>
  
  <!-- TS components -->
  <rect x="70" y="95" width="90" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="115" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">同步发电机</text>
  
  <rect x="170" y="95" width="90" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="215" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">交流网络</text>
  
  <rect x="270" y="95" width="90" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="315" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">负荷模型</text>
  
  <rect x="370" y="95" width="70" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="405" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">励磁系统</text>
  
  <rect x="70" y="135" width="90" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="115" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">输电线路</text>
  
  <rect x="170" y="135" width="90" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="215" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">变压器</text>
  
  <rect x="270" y="135" width="90" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="315" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">无功补偿</text>
  
  <rect x="370" y="135" width="70" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="405" y="155" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">PSS</text>
  
  <rect x="70" y="175" width="370" height="15" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="255" y="187" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">步长: 0.01~0.1 s | 相量模型 (DAE)</text>
  
  <!-- Interface (center) -->
  <rect x="430" y="70" width="60" height="110" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="460" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b" font-weight="bold">接口</text>
  <text x="460" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">戴维南</text>
  <text x="460" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">/诺顿</text>
  <text x="460" y="146" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">等效</text>
  <text x="460" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">模型</text>
  
  <!-- Arrows -->
  <line x1="430" y1="125" x2="428" y2="125" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="470" y1="125" x2="480" y2="125" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Data flow labels -->
  <text x="395" y="120" font-family="Arial,sans-serif" font-size="8" fill="#666">电压相量</text>
  <text x="485" y="120" font-family="Arial,sans-serif" font-size="8" fill="#666">注入电流</text>
  
  <!-- Bottom: Application scenarios -->
  <rect x="40" y="230" width="820" height="170" rx="8" fill="#f0f9ff" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="450" y="258" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#1e40af" font-weight="bold">混合仿真应用场景</text>
  
  <!-- Scenario 1 -->
  <rect x="60" y="275" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="160" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af" font-weight="bold">特高压分层直流接入</text>
  <text x="160" y="313" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#3b82f6">±800 kV 雅中-江西工程</text>
  
  <!-- Scenario 2 -->
  <rect x="280" y="275" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="380" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af" font-weight="bold">VSC-MTDC 暂态稳定</text>
  <text x="380" y="313" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#3b82f6">海上风电并网评估</text>
  
  <!-- Scenario 3 -->
  <rect x="500" y="275" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="600" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af" font-weight="bold">多直流多馈入系统</text>
  <text x="600" y="313" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#3b82f6">受端电网换相失败分析</text>
  
  <!-- Scenario 4 -->
  <rect x="720" y="275" width="140" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="790" y="295" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af" font-weight="bold">大规模电网</text>
  <text x="790" y="313" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#3b82f6">批量方式计算校核</text>
  
  <!-- Bottom: Key advantages -->
  <rect x="40" y="340" width="820" height="50" rx="6" fill="#ecfdf5" stroke="#16a34a" stroke-width="1.5"/>
  <text x="450" y="360" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#166534">
    核心优势：兼顾 EMT 精度与 TS 规模 | 接口采用戴维南/诺顿等效 | 分网边界为换流变压器连接母线
  </text>
  <text x="450" y="378" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#16a34a">
    计算效率提升 23% | 0.6 s 内达到稳态 | 支持含大量电磁直流模型的批量仿真
  </text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 机电-电磁混合仿真接口架构</p>

**接口等效原理**：在混合仿真计算时，对方模型进行戴维南/诺顿等值处理 [Xiong 2020]。机电侧向电磁侧提供等值阻抗和注入电流，电磁侧向机电侧提供节点电压和等效电流源。分网边界通常选取换流变压器连接的交流侧母线 [Xiong 2020]。

**混合仿真流程** [Chen 2020]：
1. 面向实际直流工程分别建立电磁直流标准化模型作为模型库
2. 根据混合仿真分网预案确定电磁暂态仿真的直流工程范围，从模型库中调取仿真模型，实现数据拼接
3. 程序自动定义机电-电磁暂态混合仿真接口，自动添加接口平稳启动的临时箝位电源
4. 采用基于潮流数据的初始化方法，对电磁直流模型进行运行状态的自动初始化
5. 混合仿真启动，达到稳态后切除箝位电源，保存运行点，套用预设故障集进行批量仿真

**直流电磁模型自动初始化** [Chen 2020]：

直流输电工程内部潮流与电磁模型状态的映射关系如表 1 所示。

**表 1 · 直流内部潮流与电磁模型状态映射**

| 内部潮流信息 | 电磁直流模型状态 |
|------------|----------------|
| 单/双极运行 | 六脉冲换流器闭锁状态 |
| 全压/半压运行 | 六脉冲换流器闭锁及旁通开关状态 |
| 金属/大地回线 | 回线状态切换开关状态 |
| 直流传输功率 | 直流电流参考值 |
| 直流电压 | 直流电压参考值 |
| 换流变变比 | 换流变抽头位置 |
| 换流站无功消耗 | 交流滤波器投切开关状态 |
| 逆变侧关断角 | 逆变侧关断角参考值 |

**自动初始化公式** [Chen 2020]：

直流电压和电流初始化：

$$I_d = \frac{P_s}{N \cdot U_{dr}}$$

$$U_{di} = U_{dr} - I_d \cdot R_d$$

其中 $N$ 为当前直流运行极数，$R_d$ 为直流线路电阻。

换流变变比计算：

$$n = \frac{\sqrt{3} \cdot B \cdot U_s}{\pi \cdot V_0}$$

其中 $V_0 = (U_d + \frac{3BX_C}{\pi}I_d) / \cos\alpha$，$U_s$ 为交流侧相电压。

换相角计算：

$$\mu = \arccos(\cos\alpha - \frac{2nX_T I_d}{U_s}) - \alpha$$

**仿真启动方法**：在接口位置加钳位电源（临时电压源）支持直流逐步加入稳态。采用该方法可使混合仿真在 0.6 s 的仿真过程内达到稳态 [Chen 2020]。

### 第三层：多速率协同仿真（Multirate Co-Simulation）

多速率方法的核心思想是：将整个系统划分为交流子系统和直流子系统，各子系统根据自身精度需求采用不同的时间步长进行仿真。MTDC 子系统使用较小的积分步长（如 50 μs），而交流子系统使用较大的积分步长（如 100~500 μs）。

**核心方法**：

1. **多速率 Thevenin/Norton 等效接口** [Shu 2018]：

接口模型采用时变 Thevenin 和 Norton 等效，通过增广网络方程（ANE）同时计算各子系统内部变量和接口变量。Shu 等 [2018] 提出的方法中，接口模型参数的推导采用移动窗口预测、逐步校正和平均化技术，以消除混叠误差和时延误差。

网络划分方法如图 2 所示。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 300" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="900" height="300" fill="#fafafa" stroke="#e0e0e0" stroke-width="1"/>
  <text x="450" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" fill="#333" font-weight="bold">图2 · 多速率协同仿真网络划分架构</text>
  
  <!-- MTDC subsystems -->
  <rect x="50" y="50" width="350" height="200" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="225" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#92400e" font-weight="bold">MTDC 子系统 (快速率)</text>
  <text x="225" y="96" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#d97706">步长: 5~50 μs</text>
  
  <rect x="80" y="110" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="140" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">MMC 换流站 1</text>
  
  <rect x="250" y="110" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="310" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">MMC 换流站 2</text>
  
  <rect x="80" y="155" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="140" y="177" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">MMC 换流站 N</text>
  
  <rect x="250" y="155" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="310" y="177" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">直流线路</text>
  
  <rect x="165" y="200" width="120" height="30" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="225" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">详细开关模型 / AVM</text>
  
  <!-- AC subsystem -->
  <rect x="500" y="50" width="350" height="200" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="675" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" fill="#1e40af" font-weight="bold">交流子系统 (慢速率)</text>
  <text x="675" y="96" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2563eb">步长: 100~500 μs</text>
  
  <rect x="530" y="110" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="590" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">同步发电机群</text>
  
  <rect x="700" y="110" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="760" y="132" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">交流网络</text>
  
  <rect x="530" y="155" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="590" y="177" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">负荷与变压器</text>
  
  <rect x="700" y="155" width="120" height="35" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="760" y="177" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">无功补偿装置</text>
  
  <rect x="610" y="200" width="130" height="30" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="675" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">DAE 相量模型</text>
  
  <!-- Interface -->
  <rect x="420" y="80" width="70" height="140" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="455" y="115" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b" font-weight="bold">接口模型</text>
  <text x="455" y="133" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">时变</text>
  <text x="455" y="147" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">Thevenin</text>
  <text x="455" y="161" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">/ Norton</text>
  <text x="455" y="185" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">移动窗口</text>
  <text x="455" y="199" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#991b1b">预测+校正</text>
  
  <!-- Arrows -->
  <line x1="420" y1="150" x2="418" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrow2)"/>
  <line x1="490" y1="150" x2="500" y2="150" stroke="#333" stroke-width="2" marker-end="url(#arrow2)"/>
  
  <defs>
    <marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Rate ratio info -->
  <text x="455" y="255" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">速率比: 交流步长 / 直流步长 = 2~10</text>
  <text x="455" y="275" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#666">基于 EMT 仿真精度准则确定速率比</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图2 · 多速率协同仿真网络划分架构</p>

**增广网络方程（ANE）方法** [Shu 2018]：

传统多速率方法（如波形松弛 WR、多区域 Thevenin 等效 MATE）存在混叠误差和时延误差。Shu 等 [2018] 提出的一层方法中，各子系统内部变量及接口变量由增广网络方程同时计算：

$$\mathbf{y}_s = \mathbf{Y}_s \mathbf{v}_s + \mathbf{I}_s^{his}(t-\Delta t)$$

其中 $\mathbf{Y}_s$ 为子系统等效导纳矩阵，$\mathbf{I}_s^{his}$ 为递归历史电流。接口处的数值振荡通过根匹配算法（root-matching algorithm）抑制。

2. **EMT-DS 混合仿真** [Lin 2021]：

Lin 等 [2021] 提出将风电场和直流网格采用 EMT 详细建模，交流系统采用动态仿真（DS）的方法。交流系统基于微分-代数方程（DAE）：

$$\dot{x}(t) = f(x(t), u(t))$$

$$g(x(t), u(t)) = 0$$

其中 $x$ 为同步发电机状态向量（转子角、转速、磁链等），$u$ 为输入量。通过零阻抗线（ZIL）实现 EMT 与 DS 的接口耦合。

3. **多速率实时仿真** [Zhou 2021]：

针对 Nelson River 多馈入 HVDC 系统的实际工程应用，Zhou 等 [2021] 采用多速率实时仿真架构，在 RT-LAB 平台上实现不同子系统使用不同步长的并行仿真。

### 第四层：异构计算加速（Heterogeneous Computing）

交直流混合系统的仿真计算量随系统规模呈非线性增长，异构计算（CPU+GPU）是关键的加速手段。

**CPU-GPU 异构架构** [Lin 2021]：

Lin 等 [2021] 提出的自适应异构串行-并行处理架构中：
- **CPU** 处理交流/直流混合系统中重复性不足的部分（如不同类型的换流器、非均匀的网络拓扑）
- **GPU** 负责具有大规模同质性的组件（如成百上千个 DFIG 风力发电机）

DFIG 的风机拓扑重配置（topological reconfiguration）通过内部解耦将 5 阶状态空间方程离散化 [Lin 2021]：

$$\nu(t) = \left(I - \frac{A\Delta t}{2}\right)^{-1} \left(I + \frac{A\Delta t}{2}\right)\nu(t-\Delta t) + \left(I - \frac{A\Delta t}{2}\right)^{-1} \frac{B\Delta t}{2}(u(t) + u(t-\Delta t))$$

**并行计算效率** [Chen 2020]：

在含大量电磁直流模型的混合仿真中，Chen 等 [2020] 的并行计算平台（基于 ADPSS）实现了：
- 混合仿真模型与纯 EMT 模型在关断角指令阶跃过程中拟合程度很好
- PSCAD 电磁暂态仿真耗时约 170 s，ADPSS 混合仿真耗时约 138 s，计算效率提升约 23%
- 混合仿真可在 0.6 s 内达到稳态，支持大批量方式计算校核

**GPU 并行加速** [Allabadi 2024]：

Allabadi 等 [2024] 在 CIGRE BM4 基准测试上，提出的解耦接口（Decoupling Interface, DI）初始化方法将完整系统初始化时间减少了 6.9 倍。

## 形式化表达

### 直流功率传输基本公式

直流侧功率：

$$P_{dc} = V_{dc} \cdot I_{dc}$$

LCC 换流器有功功率（整流侧）：

$$P_{ac} = \frac{3\sqrt{2}}{\pi} V_{LL} I_{dc} \cos\alpha$$

其中 $V_{LL}$ 为交流线电压有效值，$\alpha$ 为触发角。

### VSC 功率平衡

VSC 交流侧与直流侧功率平衡：

$$P_{ac} = P_{dc} = V_{dc} \cdot I_{dc}$$

VSC 在 d-q 坐标系下的功率：

$$P = \frac{3}{2}(v_d i_d + v_q i_q)$$

$$Q = \frac{3}{2}(v_q i_d - v_d i_q)$$

### 换相角与关断角

LCC 换相角：

$$\mu = \arccos(\cos\alpha - \frac{2X_C I_d}{V_0}) - \alpha$$

关断角：

$$\gamma = \mu - \beta = \mu - (\pi - \alpha)$$

正常运行时 $\gamma \approx 17^\circ$，当 $\gamma < \gamma_{min}$（通常 15°~17°）时发生换相失败。

### 接口等效模型

戴维南等效：

$$\mathbf{v}(t) = \mathbf{E}_{th}(t) - \mathbf{Z}_{th}(t) \cdot \mathbf{i}(t)$$

诺顿等效：

$$\mathbf{i}(t) = \mathbf{Y}_{no}(t) \cdot \mathbf{v}(t) + \mathbf{I}_{no}^{his}(t-\Delta t)$$

### 多速率时间步长关系

设交流子步长为 $\Delta t_{ac}$，直流子步长为 $\Delta t_{dc}$，速率比 $R$ 为：

$$R = \frac{\Delta t_{ac}}{\Delta t_{dc}}$$

重同步周期为 $\Delta t_{ac}$，在每个重同步点更新接口等效参数。

## 关键技术挑战

### 1. 换相失败与多直流交互

LCC-HVDC 的换相失败是最核心的 EMT 挑战。当交流系统发生故障导致换流母线电压下降时，换相角减小，若低于临界值则发生换相失败。在多直流多馈入系统中，一回直流的换相失败可能引发相邻直流的连锁换相失败，形成恶性循环 [Chen 2020]。

**换相失败三阶段**：
- **触发阶段**：交流故障导致换相电压降低，换相角减小
- **失败阶段**：换相角低于临界值，换流阀未能成功换相
- **恢复阶段**：故障清除后，换相角逐渐恢复，直流功率重建

**量化数据** [Xiong 2020]：在 ±800 kV 雅中-江西工程中，500 kV 换流母线处发生三相接地故障（持续 0.1 s）后，高端逆变器关断角降至 0，发生换相失败，直流功率骤降。

### 2. 接口数值稳定性

多速率协同仿真中，接口模型的离散化方式直接影响整体数值稳定性。Shu 等 [2018] 指出，波形松弛（WR）方法在 EMT 仿真中会产生混叠误差，而多区域 Thevenin 等效（MATE）在大扰动下的性能尚未充分验证。根匹配算法结合梯形积分可抑制数值振荡，但会引入额外的数值阻尼。

**量化数据** [Shu 2018]：在 IEEE 39 母线 + MMC-MTDC 测试系统上，多速率方法相比全 EMT 方法，计算效率提升约 3~5 倍，同时保持误差在 2% 以内。

### 3. 大规模混合仿真初始化

Chen 等 [2020] 指出，含大量电磁直流模型的混合仿真在数据建立、运行方式调整和平稳启动方面存在困难。传统方法需要仿真人员人工建立各回直流的电磁暂态模型，再人工定义混合仿真接口，存在大量人工干预。

**量化数据** [Chen 2020]：采用标准化建模和自动初始化方法后，混合仿真可在 0.6 s 内达到稳态，而传统方法需要数分钟的初始化时间。

### 4. 控制交互与稳定性

VSC-HVDC 的 PLL、电流内环与 LCC-HVDC 的触发角控制在混合系统中的交互行为复杂。van der Meer 等 [2015] 指出，VSC 在故障期间的非线性行为（过流限制、无功电流注入、调制指数限幅、故障穿越）使得传统的线性化方法失效。

**量化数据** [van der Meer 2015]：改进的 Thevenin 阻抗重构和故障期间交互协议使 VSC-MTDC 的暂态稳定性评估精度提升约 15%。

### 5. 多时间尺度耦合

Lin 等 [2021] 指出，DFIG 风电场的机电暂态（转子运动，秒级）与电力电子换流器的电磁暂态（开关过程，微秒级）之间存在 5~6 个数量级的时间尺度差异。自适应计算边界（adaptive computing boundary）的确定是混合仿真的关键。

## 量化性能边界

### 仿真效率对比

**表 2 · 交直流混合系统仿真方法性能对比**

| 方法 | 适用场景 | 计算加速比 | 精度误差 | 验证系统 | 来源 |
|------|---------|-----------|---------|---------|------|
| 全 EMT | 小规模系统 | 1×（基准） | < 1% | CIGRE B4 | Lin 2021 |
| 多速率 EMT | 大规模 AC+MTDC | 3~5× | < 2% | IEEE 39+MTDC | Shu 2018 |
| EM-EMT 混合 | 含大量直流模型 | 2~3× | < 2% | ±800 kV 雅中-江西 | Xiong 2020 |
| EM-EMT 混合（批量） | 大规模电网 | 计算效率提升 23% | < 1.5% | 国调电网 | Chen 2020 |
| EMT-DS 混合 | 风电场+HVDC | 10~50× | < 3% | IEEE 39+CIGRE B4 | Lin 2021 |
| DI 初始化 | MTDC 系统 | 初始化时间减少 6.9× | < 1% | CIGRE BM4 | Allabadi 2024 |

### 典型参数范围

- **时间步长**：EMT 侧 1~50 μs，机电侧 0.01~1 s
- **系统规模**：10~1000 节点（EMT 侧），100~10000 节点（机电侧）
- **仿真时长**：0.1~10 s（暂态分析），0.1~300 s（稳定性评估）
- **速率比**：2~10（交流步长/直流步长）

### 工程应用案例

**雅中-江西 ±800 kV 分层直流工程** [Xiong 2020]：
- 输送功率：10,000 MW
- 额定直流电流：6.25 kA
- 额定直流电压：±800 kV
- 江西电网总负荷：约 2,500 万 kW
- 高压阀组接入 500 kV 系统，低压阀组接入 1000 kV 系统
- 500 kV 交流系统短路比：4.53
- 1000 kV 交流系统短路比：6.10

**Nelson River 多馈入 HVDC 系统** [Zhou 2021]：
- 大规模混合实时仿真基准
- 在 RT-LAB 平台上实现多速率实时仿真

**CIGRE BM4 五端 MTDC 基准** [Allabadi 2024]：
- 包含三个互联 HVDC 系统
- 第一系统：单极点对点（Cm-D1, Cm-D2）
- 第二系统：五端双极 MTDC（Cb-D3, Cb-D4, Cb-D6, Cb-D7, Cb-D9）
- 第三系统：四端单极 MTDC（Cm-D5, Cm-D10, Cm-D12, Cm-D13）
- 仿真步长：10 μs

## 适用边界与选择指南

### 方法选择决策表

**表 3 · 交直流混合系统仿真方法选择指南**

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|------|
| 小规模 AC+MTDC 系统（<50 节点） | 全 EMT | 无需简化，精度最高 |
| 大规模 AC+MTDC 系统（>100 节点） | 多速率 EMT 协同仿真 | 兼顾精度与效率 |
| 含多条直流的受端电网 | EM-EMT 混合仿真 | 直流 EMT + 交流 TS |
| 风电场通过 HVDC 外送 | EMT-DS 混合 | 风电 EMT + 交流 DS |
| MTDC 系统初始化 | DI 方法 / CISS | 减少初始化时间 |
| 实时仿真 / HIL | 多速率实时仿真 | 硬件约束下的最优选择 |
| 批量方式计算校核 | EM-EMT 混合（标准化建模） | 自动化建模提高效率 |

### 失效边界

- **全 EMT 方法**：不适用于大规模交流系统（>500 节点），计算时间过长
- **多速率方法**：速率比过大（>10）时可能导致数值不稳定；要求子系统之间通过传输线（>15~30 km）自然隔离
- **EM-EMT 混合**：接口等效模型的准确性依赖于分网边界的选取；分网边界为换流变压器连接母线时效果最佳
- **EMT-DS 混合**：要求交流/直流接口处使用零阻抗线（ZIL）耦合；不适用于强耦合的近距离交流/直流互联
- **DI 初始化方法**：仅适用于 GVSC 控制的 VSC 系统；对 LCC-HVDC 不适用

## 相关方法

- [[vsc-hvdc]] — VSC-HVDC 系统建模与控制
- [[lcc-model]] — LCC 换流器 EMT 建模
- [[mmc-model]] — MMC 换流器详细模型
- [[mt-hvdc-test-system]] — 多端直流测试系统
- [[co-simulation]] — 协同仿真技术
- [[multirate-method]] — 多速率方法
- [[electromechanical-electromagnetic-hybrid-simulation]] — 机电电磁混合仿真
- [[hybrid-acdc-network]] — 交直流混合电网拓扑
- [[frequency-domain-analysis]] — 频域分析
- [[parallel-computing]] — 并行计算

## 来源论文

- **Shu et al. 2018** — "A Multirate EMT Co-simulation of Large AC and MMC-based MTDC Systems"，IEEE Trans. on Power Systems。提出多速率 EMT 协同仿真方法，采用时变 Thevenin/Norton 等效接口和增广网络方程（ANE），通过根匹配算法抑制数值振荡。在 IEEE 39+MTDC 系统上验证，计算效率提升 3~5 倍。

- **Lin et al. 2021** — "Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive AC/DC Grids"，IEEE Trans. on Energy Conversion。提出 EMT-DS 混合仿真框架，将风电场和直流网格采用 EMT 详细建模，交流系统采用动态仿真。提出 CPU-GPU 异构并行架构，DFIG 拓扑重配置实现 GPU 并行加速。

- **van der Meer et al. 2015** — "Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems"，IEEE Trans. on Power Delivery。提出 VSC-MTDC 系统的混合仿真建模方法，包括改进的 Thevenin 阻抗重构、故障期间交互协议和故障穿越（FRT）状态机。

- **Xiong et al. 2020** — "含分层接入特高压直流的交直流混联电网机电—电磁暂态混合仿真研究"，电力系统保护与控制。基于 ADPSS 平台，建立 ±800 kV 雅中-江西分层直流系统的 EM-EMT 混合仿真模型，验证了混合仿真的准确性和效率提升（23%）。

- **Chen et al. 2020** — "含大量电磁直流模型的机电–电磁暂态混合仿真技术研究"，电网技术。提出含大量电磁直流模型的混合仿真自动化技术框架，包括标准化建模、数据映射拼接、自动初始化和箝位电源平稳启动方法。

- **Allabadi et al. 2024** — "Initializing EMT models of grid forming VSCs in MTDC systems"，Electric Power Systems Research。提出控制初始化（CISS）和解耦接口（DI）两种 GVSC 初始化方法，在 CIGRE BM4 基准上将初始化时间减少 6.9 倍。

- **Zhou et al. 2021** — "Large-scale hybrid real time simulation modeling and benchmark for Nelson River multi-infeed HVdc system"，Electric Power Systems Research。基于 RT-LAB 平台的大规模混合实时仿真工程应用，验证了多速率实时仿真在 Nelson River 多馈入 HVDC 系统中的可行性。

- **Liu et al. 2014** — "Electro-mechanical transient modeling of MMC based multi-terminal HVDC system"，Electrical Power and Energy Systems。提出 MMC-MTDC 系统的机电暂态建模方法，为混合仿真中的直流侧等值提供了基础。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Comparison between electromechanical transient model and ele]] | 2013 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |

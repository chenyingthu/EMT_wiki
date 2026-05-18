---
title: "开关暂态 (Switching Transient)"
type: topic
tags: [switching, circuit-breaker, transient, trapped-charge, re-strike, pre-insertion]
created: "2026-05-01"
updated: "2026-05-18"
---

# 开关暂态 (Switching Transient)

## 定义与边界

开关暂态（Switching Transient）是断路器、隔离开关、负荷开关、电力电子器件或直流断路器改变网络连接状态时产生的电压电流暂态。它包括合闸过电压、分闸过电压、预击穿、重燃、截流、暂态恢复电压和残余电荷释放等现象。

开关事件的物理本质是**网络中储能元件（电感、电容）之间的能量重新分配**。断路器操作前，线路电容残存电荷或电感储能的磁场能量处于稳定态；操作后，网络拓扑突变，储能重新分布激励高频振荡，通过波过程传播到整个网络。

本页讨论由开关事件触发的 EMT 现象。它不等同于全部 [[electromagnetic-transient]]，也不替代 [[circuit-breaker-model]] 或 [[detailed-switch-model]] 的设备模型细节。若开关只被表示为预定时刻的理想拓扑变化，页面结论应限于网络波形，不应外推为真实断路器灭弧能力或寿命结论。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#222">图1 · 开关暂态分类体系与 EMT 建模方法</text>
  <!-- Legend -->
  <rect x="680" y="42" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="700" y="53" font-size="11" fill="#333">合闸类</text>
  <rect x="680" y="62" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="700" y="73" font-size="11" fill="#333">分闸类</text>
  <rect x="680" y="82" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="700" y="93" font-size="11" fill="#333">重燃/预击穿</text>
  <rect x="680" y="102" width="14" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="700" y="113" font-size="11" fill="#333">直流开断</text>
  <!-- Level 1: Input category -->
  <rect x="30" y="65" width="180" height="80" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="120" y="85" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">合闸暂态</text>
  <text x="120" y="102" text-anchor="middle" font-size="10" fill="#333">空载线路合闸</text>
  <text x="120" y="117" text-anchor="middle" font-size="10" fill="#333">电容器组投切</text>
  <text x="120" y="132" text-anchor="middle" font-size="10" fill="#333">变压器合闸</text>
  <rect x="30" y="175" width="180" height="80" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="120" y="195" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">分闸暂态</text>
  <text x="120" y="212" text-anchor="middle" font-size="10" fill="#333">感性负载开断</text>
  <text x="120" y="227" text-anchor="middle" font-size="10" fill="#333">并联电抗器投切</text>
  <text x="120" y="242" text-anchor="middle" font-size="10" fill="#333">截流过电压</text>
  <rect x="30" y="285" width="180" height="65" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="120" y="305" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">重燃/预击穿</text>
  <text x="120" y="322" text-anchor="middle" font-size="10" fill="#333">介质恢复电压竞争</text>
  <text x="120" y="337" text-anchor="middle" font-size="10" fill="#333">多次重燃抑制</text>
  <rect x="30" y="370" width="180" height="65" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="120" y="390" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">直流开断</text>
  <text x="120" y="407" text-anchor="middle" font-size="10" fill="#333">混合式/谐振式拓扑</text>
  <text x="120" y="422" text-anchor="middle" font-size="10" fill="#333">电流转移与能量吸收</text>
  <!-- Arrow down from each category -->
  <line x1="120" y1="145" x2="120" y2="175" stroke="#555" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="120" y1="255" x2="120" y2="285" stroke="#555" stroke-width="1.5"/>
  <line x1="120" y1="350" x2="120" y2="370" stroke="#555" stroke-width="1.5"/>
  <!-- Level 2: EMT modeling methods (center column) -->
  <rect x="280" y="80" width="220" height="340" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="390" y="100" text-anchor="middle" font-size="12" font-weight="bold" fill="#475569">EMT 建模方法</text>
  <!-- Method cards -->
  <rect x="290" y="115" width="200" height="42" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="390" y="130" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e40af">理想开关</text>
  <text x="390" y="145" text-anchor="middle" font-size="9" fill="#334">拓扑事件 · s_n∈{0,1}</text>
  <rect x="290" y="163" width="200" height="42" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="390" y="178" text-anchor="middle" font-size="10" font-weight="bold" fill="#92400e">动态电弧模型</text>
  <text x="390" y="193" text-anchor="middle" font-size="9" fill="#334">Mayr · Cassie · Avdonin</text>
  <rect x="290" y="211" width="200" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="390" y="226" text-anchor="middle" font-size="10" font-weight="bold" fill="#166534">残余电荷源</text>
  <text x="390" y="241" text-anchor="middle" font-size="9" fill="#334">TCS · PTCS (2025)</text>
  <rect x="290" y="259" width="200" height="42" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="390" y="274" text-anchor="middle" font-size="10" font-weight="bold" fill="#5b21b6">插值方法</text>
  <text x="390" y="289" text-anchor="middle" font-size="9" fill="#334">[[interpolation-method]]</text>
  <rect x="290" y="307" width="200" height="42" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="390" y="322" text-anchor="middle" font-size="10" font-weight="bold" fill="#991b1b">直流断路器</text>
  <text x="390" y="337" text-anchor="middle" font-size="9" fill="#334">VSC辅助谐振电流</text>
  <!-- Arrows from methods to output -->
  <line x1="390" y1="349" x2="390" y2="375" stroke="#555" stroke-width="1.5"/>
  <!-- Level 3: Output -->
  <rect x="560" y="180" width="160" height="110" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
  <text x="640" y="200" text-anchor="middle" font-size="12" font-weight="bold" fill="#334">输出指标</text>
  <text x="640" y="220" text-anchor="middle" font-size="10" fill="#475569">过电压倍数 (pu)</text>
  <text x="640" y="235" text-anchor="middle" font-size="10" fill="#475569">TRV 上升率 (RRRV)</text>
  <text x="640" y="250" text-anchor="middle" font-size="10" fill="#475569">截流电流 I_chop</text>
  <text x="640" y="265" text-anchor="middle" font-size="10" fill="#475569">重燃概率</text>
  <text x="640" y="280" text-anchor="middle" font-size="10" fill="#475569">开断能量 (DC)</text>
  <!-- Level 4: Application scenarios -->
  <rect x="560" y="315" width="160" height="90" rx="6" fill="#fafafa" stroke="#64748b" stroke-width="1.5"/>
  <text x="640" y="335" text-anchor="middle" font-size="12" font-weight="bold" fill="#334">典型场景</text>
  <text x="640" y="352" text-anchor="middle" font-size="10" fill="#475569">绝缘配合</text>
  <text x="640" y="367" text-anchor="middle" font-size="10" fill="#475569">断路器应力分析</text>
  <text x="640" y="382" text-anchor="middle" font-size="10" fill="#475569">长电缆合分闸</text>
  <text x="640" y="397" text-anchor="middle" font-size="10" fill="#475569">HVDC 故障开断</text>
  <!-- Connecting arrows -->
  <line x1="210" y1="105" x2="290" y2="136" stroke="#555" stroke-width="1.2"/>
  <line x1="210" y1="215" x2="290" y2="184" stroke="#555" stroke-width="1.2"/>
  <line x1="210" y1="310" x2="290" y2="267" stroke="#555" stroke-width="1.2"/>
  <line x1="210" y1="400" x2="290" y2="328" stroke="#555" stroke-width="1.2"/>
  <line x1="490" y1="235" x2="560" y2="220" stroke="#555" stroke-width="1.2"/>
  <line x1="640" y1="290" x2="640" y2="315" stroke="#555" stroke-width="1.2"/>
  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#555"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 开关暂态分类体系与 EMT 建模方法</p>

## EMT 中的角色

开关暂态是 EMT 仿真的经典入口，因为事件时刻会直接改变节点导纳矩阵、历史源和元件状态。它常用于绝缘配合、断路器应力、并联电抗器和电容器投切、长电缆合分闸、直流故障开断、电力电子开关波形和控制保护验证。

对第 $n$ 个时步，可把开关状态写为 $s_n \in \{0,1\}$，网络方程写成

$$\mathbf{Y}(s_n)\mathbf{v}_n = \mathbf{i}^{\mathrm{hist}}_n + \mathbf{i}^{\mathrm{src}}_n$$

其中 $\mathbf{Y}(s_n)$ 是开关状态决定的节点导纳矩阵，$\mathbf{i}^{\mathrm{hist}}_n$ 是历史电流源，$\mathbf{i}^{\mathrm{src}}_n$ 是当前时刻注入电流。拓扑切换（$s_n$ 从 0 变为 1 或反之）使 $\mathbf{Y}$ 产生不连续跳变。

若需要表示电弧或重燃，开关不再只是 $s_n$，而是带状态的非线性端口 $i_{\mathrm{arc}} = f(v_{\mathrm{arc}}, x_{\mathrm{arc}}, t)$。这一区分决定了模型能否讨论开断失败、热击穿和介质恢复。

## 主要分支与机制

### 1. 合闸暂态

合闸相角、残余电荷、线路或电缆端接阻抗决定入射波和反射波，常与 [[transmission-line-model]]、`cable-model` 衔接。空载线路合闸时，电源电压通过线路波阻抗给沿线的对地电容充电，电压波以光速传播到线路末端，经反射后形成叠加过电压。

残余电荷在单相接地故障后的重合闸中最危险——线路上残存的 $-1.0$ pu 电荷与电源正峰值叠加，可使合闸过电压达到 $2.0$~$3.0$ pu。Akafi-Mobarakeh 等（2025）提出的 PTCS（Proposing trapped charge source）模型通过有源滤波器概念，在有并联电抗器的线路中消除了传统 TCS 模型的电压振荡问题，并在 400 kV 南方伊朗电网中与现场测量验证一致。

### 2. 分闸暂态

电感或电容储能在电流过零附近释放，可能形成暂态恢复电压（TRV）和高频振荡。分闸时，断路器触头分离产生电弧，电弧在电流过零时熄灭。若触头间介质强度恢复速度慢于恢复电压上升速度，将发生重燃。

暂态恢复电压上升率（RRRV）是衡量开断难度的关键指标：

$$\text{RRRV} = \left.\frac{dv}{dt}\right|_{t=t_0} = \omega I_0 \sqrt{\frac{L}{C}}$$

其中 $I_0$ 为开断电流，$L$ 为系统电感，$C$ 为等效电容。

### 3. 重燃与预击穿

触头间介质强度和恢复电压相互竞争，简单理想开关无法给出可信失败机理。Phaniraj & Phadke（1988）在 EMTP 中实现了三个动态电弧方程（Avdonin / Urbanek / Kopplin），使仿真热击穿和介质击穿成为可能。

Urbanek 模型能模拟热击穿、介质击穿、截流和重燃，是三者中最全面的：

$$\frac{d}{dt}\left(\frac{1}{g}\right) = \frac{1}{\tau}\left(\frac{1}{G_{eq}} - \frac{1}{g}\right) + \frac{u^2}{P_0}$$

其中 $g$ 是电弧电导，$\tau$ 是时间常数，$G_{eq}$ 是平衡电导，$P_0$ 是电弧散热功率。

### 4. 截流和电弧

小感性电流开断、并联电抗器投切和真空/SF₆ 断路器研究需要动态电弧或经验开断模型。截流过电压的幅值由截流电流 $I_{chop}$ 决定：

$$V_{max} = I_{chop}\sqrt{\frac{L}{C}}$$

感性负载截流时，磁场能量 $\frac{1}{2}LI_{chop}^2$ 转换为电场能量 $\frac{1}{2}CV_{max}^2$，由此导出上式。

### 5. 直流开断

直流电流没有自然过零，混合式、谐振式或限流式拓扑需要同时表示电流转移、能量吸收和控制时序。Mirhosseini 等（2020）提出 VSC 辅助谐振式 DC 断路器，通过预充电电容与电感谐振产生电流过零点实现开断。Phaniraj & Phadke（1988）在 UBC-EMTP 中用 Kopplin 模型验证了多馈入 HVDC 系统负荷电流开断，发现存在最小并联电容和最大/最小并联电感要求——电感越小所需电容越大才能产生电流过零。

### 6. 数值事件处理

开关事件通常落在离散步之间，[[interpolation-method]] 和 [[voltage-interpolation]] 决定事件时刻误差和数值振荡风险。对于精确事件时刻定位，常用方法包括二分搜索、线性插值和多级校正。

## 形式化表达

### 合闸过电压

空载线路合闸过电压幅值（入射波 + 反射波叠加）：

$$V_{max} = V_m \frac{2Z_0}{Z_0 + Z_s} \cdot k_{af}$$

其中 $V_m$ 为电源电压峰值，$Z_0$ 为线路波阻抗，$Z_s$ 为系统阻抗，$k_{af}$ 为振幅系数（考虑残余电荷和相位）。对于无限大系统（$Z_s \approx 0$），$V_{max} \approx 2V_m$。

考虑合闸相位角 $\phi$ 和残余电荷 $V_{res}$（三相对应不同期的最严重情况）：

$$V_{max} = V_m \sin\phi - V_{res}$$

统计过电压（$2\%$ 概率统计值）：

$$V_{2\%} = k_a \cdot k_{st} \cdot V_{max}$$

其中 $k_a = 1.2$~$1.4$ 为三相不同期系数，$k_{st}$ 为统计系数。

### 分闸暂态恢复电压

恢复电压上升率（RRRV）：

$$\text{RRRV} = \omega I_0 \sqrt{\frac{L}{C}}$$

TRV 的峰值电压：

$$U_{TRV} = \frac{I_0}{C} \cdot t_{characteristics}$$

其中 $t_{characteristics}$ 是断路器的特征开断时间。

### 电弧模型

**Mayr 电弧模型**（1948）：

$$\frac{dg}{dt} = \frac{1}{\tau}\left(G_{eq} - g\right)$$

线性化后电导变化与功率平衡相关。适用于电流过零附近的弧柱冷却阶段。

**Cassie 电弧模型**（1939）：

$$\frac{d}{dt}\left(\frac{1}{g}\right) = \frac{1}{\tau}\left(\frac{1}{G_{eq}} - \frac{1}{g}\right) + \frac{u^2}{P_0}$$

适用于大电流电弧阶段，假设电弧温度恒定、热游离平衡。

**Avdonin 模型**（Phaniraj & Phadke 1988 引用）：

$$\frac{dr}{dt} = \frac{1}{A \cdot r^a - B \cdot r^p}$$

由 Mayr 模型派生，时间常数 $\tau = A \cdot r^a$，功率常数 $P = B \cdot r^p$。在 Hydro-Quebec 经过测试验证。

**Kopplin 模型**：

$$r(g) = k_r \cdot (g + 0.0005)^{0.25}, \quad P(g) = k_p \cdot (g + 0.0005)^{0.6}$$

比 Avdonin 可用更大时间步长，适用于 DC 断路器和长持续时间仿真。

### 截流过电压

感性负载截流过电压（磁场能量→电场能量转换）：

$$V_{max} = I_{chop}\sqrt{\frac{L}{C}}$$

并联电抗器开断时的截流过电压倍数可达 $3.0$~$4.5$ pu（是所有开关操作中最高的），因为电抗器储能大且开断电流相对较小。

### 重燃条件

介质恢复强度（指数恢复）：

$$U_{die}(t) = U_0(1 - e^{-t/\tau_{rec}})$$

恢复电压（工频振荡）：

$$U_{trv}(t) = U_m(1 - \cos\omega t)$$

重燃条件（恢复电压超过介质强度）：

$$U_{trv}(t) > U_{die}(t)$$

### 残余电荷源模型

传统 TCS（ATP 默认模型）：三相直流电压源串联阻抗，残余电荷电压为 $1.0$、$-1.0$、$1.0$ pu 提供最严重相间感应电压。

PTCS（有源滤波器型，Akafi-Mobarakeh 2025）：根据线路固有频率注入适当频率分量，消除电压振荡。在有并联电抗器时消除了传统 TCS 的错误谐振过电压，与 400 kV 现场测量一致。

### 直流断路器开断等效电路

VSC 辅助谐振 DC 断路器等效电路的核心是电流转移阶段：

$$L \frac{dI_{断路器}}{dt} + I_{断路器} \cdot R + V_{电容}(t) = V_{系统}$$

电容放电产生反向电流与原 DC 电流叠加形成过零点。最小并联电容要求由系统电感和断路器参数共同决定（Phaniraj & Phadke 1988）。

## 典型过电压倍数

| 操作类型 | 典型过电压倍数 (pu) | 主要影响因素 |
|----------|---------------------|--------------|
| 空载线路合闸 | 2.0~3.0 | 残余电荷、合闸相位 |
| 电容器组投切 | 2.0~2.5 | 合闸相位、涌流限制 |
| 并联电抗器开断 | 3.0~4.5 | 截流水平、重燃概率 |
| 变压器合闸 | 1.5~2.0 | 剩磁、合闸相位 |
| 电缆合闸 | 1.8~2.5 | 电缆长度、接地方式 |
| 直流断路器开断 | 1.5~2.0 | 能量吸收、开断速度 |

并联电抗器开断的过电压倍数最高（$3.0$~$4.5$ pu），因为感性储能大且截流电流无法自然过零释放。

## 过电压限制措施

| 措施 | 原理 | 适用场景 |
|------|------|----------|
| 合闸电阻 | 投入串联电阻限制电流 | 空载线路、变压器 |
| 同步合闸 | 在电压过零附近合闸 | 电容器组、线路 |
| 避雷器 | 限制过电压幅值 | 各种操作 |
| 铁磁谐振抑制 | 避免参数谐振条件 | 电压互感器回路 |
| 阻尼回路 | 消耗振荡能量 | 变压器合闸 |

## 关键技术挑战

### 挑战 1：电弧参数的获取与验证

动态电弧模型（Mayr / Cassie / Avdonin / Kopplin）的参数（A、B、a、p、$\tau$、$P_0$）通常来自开断实验数据。Phaniraj & Phadke（1988）开发了最小二乘参数估计程序，从 30 个样本（间隔 0.5 μs，覆盖电流过零前后各 20 μs）估计 Avdonin 模型参数，但测量噪声仅 1% 就会显著扭曲估计结果或导致不收敛。没有实测数据时只能用默认值，不能判断真实开断成功率。

### 挑战 2：重燃与数值振荡的区分

物理重燃（介质击穿）、数值振荡（事件时刻插值误差）和插值误差在波形中表现相似，难以自动区分。解决方案：多重插值精度对比 + 频谱分析。开关插值方法若只在某个电力电子算例中验证，应写为"作者在该算例中报告"，不能写成所有开关暂态都消除数值振荡。

### 挑战 3：残余电荷的分布特性

残余电荷在故障清除后的线路上不是均匀分布的——故障相残留电荷通过接地故障点泄放，非故障相通过相对地电容维持。传统 ATP-TCS 模型使用集总 DC 电压源无法反映这种分布不均。Akafi-Mobarakeh 2025 的 PTCS 模型在分布特性上做了改进，但对无并联电抗器线路仍需进一步验证。

### 挑战 4：直流断路器的跨拓扑验证基准

直流断路器论文中的开断时间、电流和能量结果通常是特定拓扑和测试系统结论，不能泛化为所有 HVDC 开断。Phaniraj & Phadke（1988）发现：存在最小并联电容要求和最大/最小并联电感范围——L 从 0.25 mH 增到 0.5 mH 即可成功开断，L 到 20 mH 则完全不产生电流过零。这些边界数据在同一拓扑内有参考价值，跨拓扑时应注明适用范围。

### 挑战 5：多次重燃的累积效应

一次重燃后，线路状态（电荷分布、频率特性）已改变，后续重燃概率受前一次触发电弧影响。Urbanek 模型理论上支持多次重燃仿真，但参数估计难度和计算收敛性使其在实际应用中受限。

## 适用边界与失败模式

| 建模方法 | 适用场景 | 失效场景 |
|----------|----------|----------|
| 理想开关 | 拓扑事件初筛、控制逻辑验证 | 电弧能量、热失败、介质击穿 |
| Mayr 电弧 | 小电流开断、热击穿 | 介质击穿、多次重燃 |
| Cassie 电弧 | 大电流电弧阶段 | 小电流过零 |
| Avdonin 电弧 | 电流过零前后、热击穿 | 介质击穿（无显式 $u_{breakdown}$ 项） |
| Urbanek 电弧 | 热+介质击穿、截流、重燃 | 参数估计复杂 |
| Kopplin 电弧 | DC 断路器、长持续仿真 | 小电流精度 |
| 传统 TCS | 无并联电抗器的线路合闸 | 有并联电抗器的谐振 |
| PTCS | 有并联电抗器线路合闸（2025） | 无并联电抗器（待验证） |

- 合闸电阻、同步合闸、重燃概率和过电压倍数必须绑定电压等级、线路长度、负荷状态、残余电荷、断路器模型和统计口径。
- 动态断路器模型需要实测或厂家参数。没有电弧参数时，只能讨论建模方法，不能判断真实开断成功率。
- 理想开关适合拓扑事件和控制逻辑初筛，不适合研究电弧能量、热失败、介质击穿或多次重燃。
- 直流断路器论文中的开断时间、电流和能量结果通常是特定拓扑和测试系统结论，不能泛化为所有 HVDC 开断。
- 开关插值方法若只在某个电力电子算例中验证，应写为"作者在该算例中报告"，不能写成所有开关暂态都消除数值振荡。

## 与相关页面的关系

- [[electromagnetic-transient]] 给出暂态现象总边界；本页聚焦开关事件。
- [[ideal-switch-model]]、`detailed-switch-model` 和 [[circuit-breaker-model]] 分别承载开关模型层级。
- [[state-space-method]] 和 [[nodal-admittance-matrix]] 解释拓扑切换后网络方程如何求解。
- [[interpolation-method]] 与 `voltage-interpolation` 处理离散步长内的事件时刻。
- [[vsc-hvdc]]、`mmc-model` 和 [[power-electronics]] 涉及高频器件开关，但器件调制问题不等同于高压断路器开断。

## 开放问题

- 如何在公开 EMT 模型中记录断路器电弧参数、介质恢复和厂家数据的证据等级。
- 如何把开关统计分散性、残余电荷和保护动作组织成可复现的绝缘配合算例。
- 如何为直流断路器建立跨拓扑、跨平台且不过度外推的验证基准。
- 如何区分物理重燃、数值振荡和插值误差在波形中的表现。

## 来源论文

Akafi-Mobarakeh 等 2025 提出了有源滤波器型 PTCS 模型，在有并联电抗器的 400 kV 线路中消除了传统 TCS 的电压振荡，与现场测量验证一致，为残余电荷源建模的重要进展。

Phaniraj & Phadke 1988 在 EMTP 中实现了 Avdonin、Urbanek 和 Kopplin 三个动态电弧模型，并通过多馈入 HVDC 系统负荷电流开断算例验证了 Kopplin 模型的适用性，发现直流开断存在最小并联电容和电感边界。

Mirhosseini 等 2020 提出了 VSC 辅助谐振式 DC 断路器拓扑，通过预充电电容与系统电感谐振产生电流过零点，为直流故障开断提供了可实时仿真的等效电路模型。

Morales 等 2021（建模架空线路残余电荷放电速率）从线路频率相关模型出发，详细分析了残余电荷通过线路对地电容和并联电抗器的放电过程，为 TCS 模型的高频特性分析提供了理论基础。
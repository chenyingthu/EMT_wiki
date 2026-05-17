---
title: "铁磁谐振 (Ferroresonance)"
type: topic
tags: [ferroresonance, transformer, nonlinear, resonance, transient]
created: "2026-04-14"
updated: "2026-05-17"
---

# 铁磁谐振 (Ferroresonance)

## 定义

铁磁谐振是电力系统中由于变压器铁芯非线性磁化特性与系统电容（线路对地电容、CCVT电容、串联补偿电容等）相互作用产生的非线性谐振现象。其本质是磁芯饱和电感与电容构成的分岔（bifurcation）系统，在特定参数条件下在多个稳态之间跳跃或进入混沌状态。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景 -->
  <rect width="900" height="480" fill="#fafafa"/>
  
  <!-- 标题 -->
  <text x="450" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#1a1a1a">图1 · 铁磁谐振机理与抑制路径</text>
  
  <!-- 输入层：激发条件 -->
  <rect x="30" y="50" width="200" height="70" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="73" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e40af">激发条件</text>
  <text x="130" y="92" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">变压器铁芯饱和（非线性励磁）</text>
  <text x="130" y="107" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">系统电容（线路对地、CCVT等）</text>
  
  <!-- 箭头1 -->
  <line x1="130" y1="120" x2="130" y2="145" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- 过程层：谐振类型 -->
  <rect x="30" y="150" width="200" height="130" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="130" y="173" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#92400e">谐振类型与特征</text>
  <text x="130" y="193" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">基频谐振（50Hz）</text>
  <text x="130" y="208" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">次谐波谐振（1/2、1/3频）</text>
  <text x="130" y="223" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">超谐波谐振（2、3倍频）</text>
  <text x="130" y="238" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">混沌特性（不可预测）</text>
  <text x="130" y="253" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">多稳态跳跃</text>
  <text x="130" y="268" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">电压波形严重畸变</text>
  
  <!-- 箭头2 -->
  <line x1="130" y1="280" x2="130" y2="305" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- 输出层：过压过流危害 -->
  <rect x="30" y="310" width="200" height="80" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="130" y="333" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#991b1b">危害</text>
  <text x="130" y="353" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">过电压（可达2.4 p.u.）</text>
  <text x="130" y="368" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">过电流</text>
  <text x="130" y="383" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">设备热应力与老化</text>
  
  <!-- 抑制路径（右侧） -->
  <rect x="300" y="150" width="250" height="240" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="425" y="173" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#166534">抑制方法</text>
  
  <text x="320" y="198" font-family="Arial,sans-serif" font-size="10" fill="#166534">1. 阻尼电阻法</text>
  <text x="320" y="213" font-family="Arial,sans-serif" font-size="9" fill="#166534">   二次侧并联5Ω电阻</text>
  <text x="320" y="228" font-family="Arial,sans-serif" font-size="9" fill="#166534">   临界阻尼电阻R_crit≈3.4Ω</text>
  
  <text x="320" y="253" font-family="Arial,sans-serif" font-size="10" fill="#166534">2. 消谐装置</text>
  <text x="320" y="268" font-family="Arial,sans-serif" font-size="9" fill="#166534">   MOV限压装置</text>
  <text x="320" y="283" font-family="Arial,sans-serif" font-size="9" fill="#166534">   2个工频周期内耗散能量</text>
  
  <text x="320" y="308" font-family="Arial,sans-serif" font-size="10" fill="#166534">3. 参数优化</text>
  <text x="320" y="323" font-family="Arial,sans-serif" font-size="9" fill="#166534">   限制操作过电压</text>
  <text x="320" y="338" font-family="Arial,sans-serif" font-size="9" fill="#166534">   优化电容/电感参数设计</text>
  
  <text x="320" y="363" font-family="Arial,sans-serif" font-size="10" fill="#166534">4. 逐次切除策略</text>
  <text x="320" y="378" font-family="Arial,sans-serif" font-size="9" fill="#166534">   单次切除R≥9Ω</text>
  <text x="320" y="393" font-family="Arial,sans-serif" font-size="9" fill="#166534">   间隔5个周波（100ms）</text>
  
  <!-- J-A模型卡片（右侧） -->
  <rect x="580" y="150" width="290" height="240" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="725" y="173" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#5b21b6">Jiles-Atherton磁滞模型</text>
  
  <text x="600" y="198" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">核心方程：</text>
  <text x="600" y="215" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">M = M_rev + M_irr</text>
  <text x="600" y="230" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">M_rev = c(M_an - M_irr)</text>
  <text x="600" y="245" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">dM_irr/dH = (M_an - M_irr) /</text>
  <text x="600" y="258" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">            (kδ - α(M_an - M_irr))</text>
  
  <text x="600" y="283" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">五参数：</text>
  <text x="600" y="298" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">M_s（饱和磁化强度）</text>
  <text x="600" y="313" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">a, α, k, c（形状/耦合/阻塞/可逆系数）</text>
  
  <text x="600" y="338" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">数值稳定性：</text>
  <text x="600" y="353" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">Δt < 100μs</text>
  <text x="600" y="368" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">13.956kHz振荡→步长≤0.7μs</text>
  
  <text x="600" y="393" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">精度：</text>
  <text x="600" y="408" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">电流波形误差<5%</text>
  <text x="600" y="423" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">识别2-3个额外谐振工作点</text>
  
  <!-- CCVT谐振频率标注 -->
  <rect x="300" y="410" width="570" height="50" rx="4" fill="#fef9c3" stroke="#ca8a04" stroke-width="1"/>
  <text x="585" y="433" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#854d0e">CCVT高频谐振频率</text>
  <text x="585" y="452" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#854d0e">f₀ = 1/(2π√((C₁+C₂)L_d)) ≈ 13.956 kHz（近端接地故障激发）</text>
  
  <!-- 箭头定义 -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- 图例 -->
  <rect x="30" y="420" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="48" y="430" font-family="Arial,sans-serif" font-size="9" fill="#333">输入</text>
  <rect x="90" y="420" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="108" y="430" font-family="Arial,sans-serif" font-size="9" fill="#333">过程</text>
  <rect x="145" y="420" width="12" height="12" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="163" y="430" font-family="Arial,sans-serif" font-size="9" fill="#333">危害</text>
  <rect x="195" y="420" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="213" y="430" font-family="Arial,sans-serif" font-size="9" fill="#333">抑制</text>
  <rect x="250" y="420" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="268" y="430" font-family="Arial,sans-serif" font-size="9" fill="#333">J-A模型</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 铁磁谐振机理与抑制路径（Jiles-Atherton磁滞模型核心方程）</p>

## 概述

铁磁谐振是电力系统中由于变压器铁芯非线性磁化特性与系统电容相互作用产生的非线性谐振现象。铁磁谐振会导致过电压、过电流，威胁设备安全，是EMT仿真研究的重要课题。

## 产生条件

- 变压器铁芯饱和（非线性励磁）
- 系统电容（线路对地电容、CCVT电容等）
- 系统扰动（开关操作、单相接地故障等）
- 低阻尼系统

## 主要特征

- 非线性、多稳态特性
- 可能出现基频、次谐波、超谐波谐振
- 电压波形畸变严重
- 难以预测，具有混沌特性
- 持续时间可能很长

## EMT建模方法

### 1. 变压器磁滞模型

**Jiles-Atherton（J-A）动态磁滞模型**是当前EMT仿真中描述铁磁谐振的核心方法。其磁化强度分解为可逆分量与不可逆分量：

$$M = M_{rev} + M_{irr}$$

其中可逆磁化分量由修正系数$c$表征：

$$M_{rev} = c(M_{an} - M_{irr})$$

不可逆磁化分量的微分方程控制磁滞回线的路径：

$$\frac{dM_{irr}}{dH} = \frac{M_{an} - M_{irr}}{k\delta - \alpha(M_{an} - M_{irr})}$$

其中无磁滞磁化强度$M_{an}$可采用修正的AMC（Adaptive Moving Average Correction）公式描述：

$$M_{an} = M_s \cdot \mathcal{L}\left(\frac{H_e}{a}\right)$$

有效磁场$H_e = H + \alpha M$耦合了磁化强度对磁滞特性的影响。参数$\delta$由磁场变化率的方向决定，使模型能够区分增磁与退磁过程，从而形成主磁滞回线和次磁滞回线。

**Preisach磁滞模型**基于算子叠加理论，通过大量滞后算子的加权积分描述磁滞特性。其优势在于能够精确捕捉次磁滞回线，但计算成本较高。

### 2. 电容模型

铁磁谐振中的电容元件包括：

- **线路对地电容**：长输电线路分布电容的集总等效
- **CCVT耦合电容**：电容式电压互感器中$C_1$、$C_2$分压电容
- **串联补偿电容**：串联电容补偿装置中的电容

在CCVT中，高频谐振回路的自然频率由电容$C_1$、$C_2$与泄放线圈电感$L_d$共同决定：

$$f_0 = \frac{1}{2\pi\sqrt{(C_1 + C_2)L_d}} \approx 13.956 \text{ kHz}$$

### 3. 仿真求解

- 需要小时间步长捕捉非线性动态（$\Delta t < 100\,\mu\text{s}$）
- 数值积分方法影响稳定性
- EMTP/EMTP-RV是主要仿真工具

## 抑制措施

### 临界阻尼电阻

对于中性点接地变电站的PT（电压互感器）系统，折算至二次侧的临界阻尼电阻约为：

$$R_{crit} \approx 3.4\,\Omega$$

工程整定时，通过EMTP试错整定，星形二次侧并联**5Ω**电阻可将铁磁谐振过电压从1.5~2.4 p.u.压制至0.8~1.04 p.u.。

### 逐次切除策略

电阻切除需采用逐次切除策略，关键参数为：
- 单次切除电阻值必须 $\geq 9\,\Omega$
- 相邻切除操作需间隔 **5个工频周波（100ms）**，以避免电压突变重新激发谐振

## 仿真平台对比

| 仿真平台 | 建模能力 | 时间步长要求 | 适用场景 | 性能特点 |
|---------|---------|-------------|---------|---------|
| **EMTP/ATP** | 支持Type-94元件实现J-A动态模型 | $\Delta t < 100\,\mu\text{s}$ | 大规模电网铁磁谐振分析 | 仿真速度比实时快50-100倍，数值稳定性强 |
| **EMTP-RV** | 详细变压器饱和模型与杂散电容 | 自适应步长 | CCVT暂态特性研究 | 支持复杂保护装置（MOV）建模 |
| **PSCAD/EMTDC** | 自定义磁滞模型接口 | 固定小步长 | 教学与快速原型验证 | 图形化建模友好，但磁滞模型精度依赖用户自定义 |
| **RTDS** | 简化磁滞模型 | 50 $\mu\text{s}$ 级 | 硬件在环测试 | 受限于实时性，通常采用等效饱和电感近似 |

## 关键技术挑战

### 1. 数值稳定性要求

采用J-A动态模型时，需满足$\Delta t < 100\,\mu\text{s}$以保证数值稳定性。对于13.956 kHz的高频振荡成分，建议步长不超过振荡周期的1/100（约0.7 $\mu\text{s}$）。

### 2. 宽频带建模

铁磁谐振涉及从工频到数百kHz的宽频振荡，需建立包含杂散参数的多物理场模型：

- **降压变压器一次侧杂散电容 $C_t$**：在频率高于100Hz时对频响特性产生不可忽略的影响
- **串联电抗器杂散电容 $C_c$**：从0 pF增至1500 pF时，可使频响曲线首个陷波频率从基频附近偏移至约640 Hz
- **泄放线圈电感 $L_d$**：显著主导600Hz以上频段的幅频响应，其Q因子直接决定高频振荡的阻尼速率

### 3. 动态损耗耦合

通过引入Type-94元件实现电压驱动的动态磁链-电流（$\psi-i$）关系，将静态J-A模型扩展为动态模型。动态损耗建模显示，当磁通密度变化率$dB/dt$增加时，等效铁损电阻呈非线性下降，在150Hz时较50Hz降低约40%。

### 4. 多稳态与混沌预测

铁磁谐振具有典型的多稳态和混沌特性，现有确定性仿真难以完全预测其发生边界。

### 5. 实时仿真约束

当前RTDS等实时平台多采用简化饱和模型，磁滞损耗精度受限。

## 量化性能边界

| 应用场景 | 核心设备 | 关键参数 | 仿真/试验结果 | 技术要点 |
|---------|---------|---------|--------------|---------|
| **CCVT暂态** | CCVT主电容$C_1$/$C_2$，降压变压器，泄放线圈$L_d$ | $L_d$ Q因子，$C_t$杂散电容，负载功率因数 | 近端接地故障激发13.956 kHz高频振荡；MOV可在2个工频周期内耗散谐振能量 | 杂散电容在>100Hz频段不可忽略；负载容量（200-1200VA）对频响影响微弱 |
| **饱和电抗器铁磁谐振** | 环形铁芯饱和电抗器 | $M_s, a, \alpha, k, c$（J-A五参数） | 动态模型在50/150Hz验证中电流波形相对误差<5%，识别出2-3个传统模型无法预测的谐振工作点 | Type-94元件实现电压驱动动态损耗；修正AMC公式提升拟合精度15-20% |
| **中性点接地变电站PT谐振抑制** | 电磁式电压互感器 (PT) | 二次侧并联电阻$R=5\,\Omega$，切除步长$\geq 9\,\Omega$ | 31次现场开关操作试验成功率100%，过电压从2.4 p.u.降至1.04 p.u.以下 | 星形侧并联方案效率100%；逐次切除需间隔5个周波防止重激 |

## 适用边界与选择指南

| 场景 | 推荐模型 | 步长要求 | 抑制策略 |
|------|---------|---------|---------|
| 大规模电网铁磁谐振分析 | EMTP/ATP + J-A动态模型 | $\Delta t < 100\,\mu\text{s}$ | 5Ω二次侧并联电阻 |
| CCVT暂态特性研究 | EMTP-RV + 详细杂散电容 | 自适应步长 | MOV + 逐次切除 |
| 饱和电抗器设计验证 | J-A + Type-94动态损耗 | $\Delta t < 1\,\mu\text{s}$ | 阻尼电阻优化 |
| 硬件在环测试 | RTDS + 简化饱和模型 | 50 $\mu\text{s}$ 级 | 等效饱和电感近似 |
| GIS/VFTO宽频分析 | J-A扩展至MHz频段 | $\Delta t < 0.1\,\mu\text{s}$ | 多物理场耦合 |

## 相关模型

- [[transformer-model]] — 变压器模型
- [[cable-model]] — 电缆模型
- [[transmission-line-model]] — 输电线路模型

## 相关方法

- [[numerical-integration]] — 数值积分方法
- [[nodal-analysis]] — 节点分析方法

## 相关主题

- [[frequency-dependent-modeling]] — 频率相关建模
- [[real-time-simulation]] — 实时仿真

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror]] | 2018 | 提出电压驱动的动态ψ-i J-A磁滞电抗器模型，50/150Hz测试验证误差<5% |
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo]] | 2004 | 建立CCVT全电路时域模型，识别13.956 kHz高频谐振模式 |
| [[accurate-simulation-model-for-a-three-phase-ferroresonant-circuit-in-emtpatp]] | 2018 | 三相铁磁谐振电路精确建模方法 |
| [[duality-based-transformer-modeling-for-low-frequency-transients]] | 2016 | 基于对偶性的变压器低频暂态建模 |
| [[dual-reversible-transformer-model-for-the-13&14]] | 2013 | 双可逆变压器模型 |
| [[determination-of-the-saturation-curve-of-power-transformers-by-processing-transi]] | 2021 | 通过暂态处理确定变压器饱和曲线 |
| [[application-of-emtp-in-the-research-of-uhv-ac-power-transmission]] | 2006 | EMTP在超高压输电研究中的应用 |
| [[analysing-a-power-transformers-internal-response-to-system-transients-using-a-hy]] | 2015 | 混合建模分析变压器对系统暂态的响应 |

## 技术演进脉络

### 1990-2000年：现象识别与机理研究

- **铁磁谐振现象系统描述** (1990s)
  - 建立铁磁谐振的基本理论框架，识别参数谐振、基频谐振、分频谐振等类型
- **磁化特性建模** (1995-1999)
  - 提出分段线性磁化曲线和多项式近似方法，用于EMT仿真

### 2001-2010年：磁滞模型贡献

- **Preisach磁滞模型** (2001-2005)
  - 引入Preisach理论描述铁芯磁滞特性，提升谐振预测精度
- **Jiles-Atherton动态模型** (2006-2010)
  - 建立基于物理的J-A动态磁滞模型，能够模拟剩磁、磁滞损耗和频率效应

### 2011-2015年：工程应用与验证

- **CCVT暂态分析** (2011-2013)
  - 系统研究电容式电压互感器的铁磁谐振特性，识别13.956 kHz高频振荡模式
- **饱和电抗器建模** (2014-2015)
  - J-A模型在饱和电抗器中验证，电流波形误差<5%，识别传统模型遗漏的谐振点

### 2016-2026年：实时仿真与多物理场

- **实时平台简化模型** (2016-2020)
  - RTDS等实时仿真器采用简化饱和模型，步长50μs级，权衡精度与实时性
- **多物理场耦合** (2021-2026)
  - 研究铁芯振动、温度效应与电磁谐振的耦合机制，扩展至GIS/VFTO宽频领域

## 研究趋势与开放问题

### 多稳态与混沌特性预测

铁磁谐振具有典型的多稳态和混沌特性，现有确定性仿真难以完全预测其发生边界。当前研究趋势包括：

- **分岔分析**：结合数值延拓算法与EMT仿真，构建参数空间中的谐振域边界
- **概率性评估**：考虑参数不确定性（如剩磁、开关时刻）的蒙特卡洛仿真方法
- **吸引域刻画**：基于能量函数的暂态稳定域分析，识别避免铁磁谐振的安全操作区域

### 宽频带电磁暂态建模

随着电力电子装置和GIS（气体绝缘开关设备）的广泛应用，铁磁谐振与高频振荡（VFTO）的耦合机制成为新挑战：

- **频率相关磁导率**：现有J-A模型主要针对工频至千赫兹频段，需扩展至MHz级以涵盖GIS中的快速暂态
- **集肤效应建模**：高频条件下铁芯集肤效应对磁滞回线的影响机制尚不明确
- **多物理场耦合**：铁芯振动（磁致伸缩）与电气谐振的机电耦合建模

### 智能电网环境下的新风险

- **分布式电源接入**：逆变器控制策略与铁磁谐振的相互作用，特别是低短路比（SCR）条件下的谐振风险
- **直流偏磁影响**：高压直流（HVDC）接地极电流导致的变压器直流偏磁，改变铁芯工作点，可能引发或抑制铁磁谐振
- **数据驱动建模**：利用实测运行数据训练代理模型（Surrogate Model），弥补物理模型在复杂工况下的精度不足

### 实时仿真与数字孪生

- **实时磁滞模型简化**：当前RTDS等实时平台多采用简化饱和模型，如何在保持实时性的同时集成J-A动态模型是技术瓶颈
- **数字孪生应用**：构建包含铁磁谐振风险的变电站数字孪生体，实现在线风险评估与抑制策略优化

### 开放性问题

1. **长期稳定性**：铁磁谐振可能持续数分钟至数小时，现有短时仿真难以评估热积累对磁化特性的影响
2. **剩磁测量与估计**：系统初始条件（变压器剩磁）难以实时获取，导致谐振预测存在不确定性
3. **多变压器交互**：大型变电站多组变压器并联运行时的集群铁磁谐振机理尚缺乏系统性研究
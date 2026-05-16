---
title: "接地系统建模 (Grounding System Modeling)"
type: method
tags: [grounding, earth electrode, gpr, earth-return, soil ionization, tower-footing, counterpoise, soil frequency-dependence]
created: "2026-05-02"
updated: "2026-05-16"
---

# 接地系统建模 (Grounding System Modeling)

## 定义

接地系统建模是在 EMT 中表示接地网、接地极、杆塔接地、风电场互联接地、设备接地引线和土壤返回路径的方法。其输出通常是接地点电位（Ground Potential Rise, GPR）、注入电流、地电位升、冲击阻抗、端口阻抗/导纳或与线路/电缆模型耦合的接地边界条件。

在雷电暂态仿真中，接地系统的准确建模至关重要。简单的工频接地电阻无法反映高频雷电电流下地电位升的实际分布——高频电流倾向于集中在注入点附近，而非沿接地导体均匀扩散。

本页关注接地系统作为电磁暂态网络元件的建模。它不替代安全标准中的接触电压/跨步电压计算，也不把工频接地电阻等同于雷电冲击响应。接触电压、跨步电压和安全限值应以具体标准、现场参数和工程校核为准。

## EMT 中的作用

接地模型在 EMT 中主要用于：

- 雷电直击或反击下的 [[ground-potential-rise]] 和设备端口过电压
- 接地故障、零序电流和多接地点分流
- 电缆护套、杆塔、避雷器和变压器中性点的接地边界
- 风电场、变电站或配电网中多点接地网络的相互耦合
- [[lightning-transient-analysis]] 和 [[insulation-coordination]] 中的保护装置应力与绝缘裕度计算
- 特高压直流换流站阀塔接地和直流偏磁电流分析

若把所有接地点设为理想零电位，可能低估设备端口电压、护套电压、控制电缆干扰和人员安全相关电位差。在 500 kV 及以上电压等级的线路雷电屏蔽分析中，接地冲击阻抗对反击跳闸率的定量影响尤为显著（Alipio et al. 2023）。

## 核心机制

低频近似中，接地系统常被表示为电阻或 R-L 支路：

$$v_g(t) = R_g i_g(t) + L_g \frac{di_g(t)}{dt}$$

宽频 EMT 中，更一般的关系是端口阻抗/导纳矩阵：

$$\mathbf{v}_g(\omega) = \mathbf{Z}_g(\omega) \mathbf{i}_g(\omega), \quad \mathbf{i}_g(\omega) = \mathbf{Y}_g(\omega) \mathbf{v}_g(\omega)$$

其中 $\mathbf{Z}_g$ 可由电路分段、场积分、传输线、矩量法、多端口宽带模型或测量识别得到。进入时域时，频域函数通常需被拟合为稳定有理函数：

$$\hat{Z}_g(s) = D + \sum_{r=1}^{N} \frac{R_r}{s - p_r}$$

并转换成 EMT 步进中的历史项或状态空间模型。

### 土壤频变特性

对土壤介质，频率相关电导率和介电常数通过复电导率进入模型：

$$\sigma^*(\omega) = \sigma(\omega) + j\omega\varepsilon(\omega)$$

常用的频变土壤模型有 Visacro-Alipio（VA）公式（基于巴西现场测量数据）（Araujo et al. 2021）：

$$\rho(f) = \rho_0 \left[1 + 1.2 \times 10^{-6} (\rho_0)^{0.73} (f - 100)^{0.65}\right]^{-1}$$

$$\varepsilon_r(f) = \begin{cases} 192 & f < 10 \text{ kHz} \\ 7.6 \times 10^3 f^{-0.4} + 1.30 & f \geqslant 10 \text{ kHz} \end{cases}$$

其中 $\rho_0$ 为 100 Hz 测得的直流电阻率。Scott 模型给出了含水率对频变特性的影响：

$$\log_{10}\sigma = -0.604 + 1.640W_1 - 0.062f_1 + 0.062W_1^2 - 0.070W_1 f_1 + 0.021f_1^2$$

$$\log_{10}\varepsilon_r = 4.905 + 1.308W_1 - 0.971f_1 + 0.111W_1^2 - 0.168W_1 f_1 + 0.059f_1^2$$

其中 $W_1 = \log_{10}$（体积含水率百分比），$f_1 = \log_{10}$（频率 Hz）。研究表明：高频下土壤电阻率下降、容性效应增强，尤其在 $\rho > 600\ \Omega\text{m}$ 的高电阻率土壤中表现显著（Salarieh et al. 2020）。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>
    </filter>
  </defs>

  <!-- Title -->
  <text x="450" y="28" fill="#1a1a2e" font-size="16" font-weight="bold" text-anchor="middle">接地系统建模方法分类体系</text>

  <!-- Top-level: 输入节点 -->
  <rect x="360" y="48" width="180" height="44" rx="5" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="450" y="68" fill="#1e3a5f" font-size="13" font-weight="bold" text-anchor="middle">系统端口参数</text>
  <text x="450" y="84" fill="#4b6b8f" font-size="10" text-anchor="middle">注入电流 I(ω), 土壤参数 ρ, 几何布置</text>

  <!-- Arrow down -->
  <line x1="450" y1="92" x2="450" y2="108" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- 5 method cards in 2 rows -->
  <!-- Row 1: Lumped, Transmission Line -->
  <rect x="30" y="118" width="180" height="80" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="120" y="140" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">① 集总 R/RL/RC</text>
  <text x="120" y="158" fill="#92400e" font-size="10" text-anchor="middle">尺寸 ≪ 波长</text>
  <text x="120" y="173" fill="#92400e" font-size="10" text-anchor="middle">工频/保护筛选</text>
  <text x="120" y="188" fill="#a16207" font-size="9" text-anchor="middle">R = ρ/2πl (垂直接地极)</text>

  <rect x="245" y="118" width="180" height="80" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="335" y="140" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">② 传输线模型</text>
  <text x="335" y="158" fill="#166534" font-size="10" text-anchor="middle">电报方程 + Marti 模型</text>
  <text x="335" y="173" fill="#166534" font-size="10" text-anchor="middle">杆塔接地/引下线</text>
  <text x="335" y="188" fill="#15803d" font-size="9" text-anchor="middle">Alipio 2023 (误差 &lt; 5%)</text>

  <rect x="460" y="118" width="180" height="80" rx="5" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="550" y="140" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">③ 多端口 FDNE</text>
  <text x="550" y="158" fill="#4c1d95" font-size="10" text-anchor="middle">矢量拟合 + 无源性强制</text>
  <text x="550" y="173" fill="#4c1d95" font-size="10" text-anchor="middle">变电站/复杂接地网</text>
  <text x="550" y="188" fill="#5b21b6" font-size="9" text-anchor="middle">Lima 2026 (有效长度约束)</text>

  <rect x="675" y="118" width="195" height="80" rx="5" fill="#f3f4f6" stroke="#6b7280" stroke-width="2" filter="url(#shadow)"/>
  <text x="772" y="140" fill="#374151" font-size="12" font-weight="bold" text-anchor="middle">④ 场模型 MoM/FEM/FDTD</text>
  <text x="772" y="158" fill="#4b5563" font-size="10" text-anchor="middle">Maxwell 方程直接求解</text>
  <text x="772" y="173" fill="#4b5563" font-size="10" text-anchor="middle">研究级校核/复杂几何</text>
  <text x="772" y="188" fill="#6b7280" font-size="9" text-anchor="middle">Araujo 2021 (MoM + 分层 Green)</text>

  <!-- Row 2: Soil ionization centered -->
  <rect x="340" y="218" width="220" height="70" rx="5" fill="#fee2e2" stroke="#dc2626" stroke-width="2" filter="url(#shadow)"/>
  <text x="450" y="240" fill="#7f1d1d" font-size="12" font-weight="bold" text-anchor="middle">⑤ 非线性土壤电离模型</text>
  <text x="450" y="258" fill="#991b1b" font-size="10" text-anchor="middle">大雷电流 (I &gt; 10 kA)</text>
  <text x="450" y="273" fill="#991b1b" font-size="10" text-anchor="middle">R(t) = R₀ / √(1 + i_g/I_c)</text>
  <text x="450" y="285" fill="#b91c1c" font-size="9" text-anchor="middle">I_c ≈ 1–10 kA (临界电离电流)</text>

  <!-- Output layer -->
  <line x1="450" y1="198" x2="450" y2="215" stroke="#333" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="120" y1="198" x2="120" y2="215" stroke="#333" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="335" y1="198" x2="335" y2="215" stroke="#333" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="550" y1="198" x2="550" y2="215" stroke="#333" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="772" y1="198" x2="772" y2="215" stroke="#333" stroke-width="1" stroke-dasharray="3,3"/>

  <rect x="320" y="305" width="260" height="55" rx="5" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <text x="450" y="325" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">EMT 仿真输出</text>
  <text x="450" y="343" fill="#166534" font-size="10" text-anchor="middle">GPR(ω), 端口阻抗 Z(ω), 接地冲击阻抗, 护套电压</text>

  <!-- Legend -->
  <text x="30" y="385" fill="#333" font-size="11" font-weight="bold">图例：</text>
  <rect x="30" y="392" width="14" height="9" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="50" y="400" fill="#555" font-size="9">输入/源</text>
  <rect x="105" y="392" width="14" height="9" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="125" y="400" fill="#555" font-size="9">算法/解析</text>
  <rect x="195" y="392" width="14" height="9" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="215" y="400" fill="#555" font-size="9">传输线法</text>
  <rect x="290" y="392" width="14" height="9" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="310" y="400" fill="#555" font-size="9">FDNE 法</text>
  <rect x="375" y="392" width="14" height="9" rx="2" fill="#f3f4f6" stroke="#6b7280" stroke-width="1"/>
  <text x="395" y="400" fill="#555" font-size="9">场模型法</text>
  <rect x="465" y="392" width="14" height="9" rx="2" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="485" y="400" fill="#555" font-size="9">非线性电离</text>

  <text x="700" y="400" fill="#888" font-size="9" text-anchor="middle">实线：直接路径 | 虚线：分层方法</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 接地系统 EMT 建模方法分类体系（5 类方法 → EMT 输出）</p>

## 形式化表达

### 传输线法（杆塔接地）

将接地导体视为埋地传输线，是精度与计算效率平衡的建模方法（Alipio et al. 2023）。四根水平引下线的每一对可用等效均匀传输线表示，其电报方程为：

$$\frac{d\mathbf{V}}{dx} = -\mathbf{Z}_i - j\omega\mathbf{L}\mathbf{I}$$

$$\frac{d\mathbf{I}}{dx} = -(\mathbf{G} + j\omega\mathbf{C})\mathbf{V}$$

其中 $\mathbf{Z}_i$ 和 $\mathbf{L}$ 分别为 $2 \times 2$ 内部阻抗矩阵和外电感矩阵，$\mathbf{G}$ 和 $\mathbf{C}$ 分别为并联电导和电容矩阵。

Sunde 接地电阻公式（埋地裸导线平行于地面）：

$$R_S = \frac{1}{\pi\sigma_g} \left[\ln\frac{2l}{\sqrt{2hr}} - 1\right]$$

其中 $l$ 为导线总长，$h = 0.8\ \text{m}$ 为埋深，$r = 4.7625\ \text{mm}$ 为导线半径。

互阻抗（相邻导线间）：

$$R_M = \frac{e^{-\gamma_g d}}{\pi\sigma_g} \left[\ln\frac{2l}{\sqrt{2hd}} - 1\right]$$

其中 $\gamma_g = j\omega\mu_0(\sigma_g + j\omega\varepsilon_g)$ 为土壤固有传播常数，$d$ 为线间距离。

### 多端口有理函数等值（FDNE）

将宽频端口阻抗矩阵 $\mathbf{Z}_g(\omega)$ 用矢量拟合（Vector Fitting）逼近似有理函数：

$$\hat{Z}_{ij}(s) = D_{ij} + \sum_{r=1}^{N} \frac{R_{r,ij}}{s - p_r}$$

Lima et al.（2026）指出：FDNE 的鲁棒性取决于"有效长度"——超过有效长度的导体部分对高频阻抗贡献可忽略。有效长度的合理选择是 FDNE 最小阶实现的关键。

### 非线性土壤电离模型

大雷电流下，土壤电离导致接地电阻非线性下降。常用指数模型：

$$g(E) = \sigma_0 + a E^b \quad \text{（电离区域）}$$

或等效为时变电阻：

$$R(t) = \frac{R_0}{\sqrt{1 + i_g(t)/I_c}}$$

其中 $I_c$ 为临界电离电流（通常 1–10 kA 量级），$R_0$ 为静态接地电阻。

## 关键技术挑战

### 挑战 1：频率依赖与分层土壤的参数获取

频变土壤参数（$\rho(f)$、$\varepsilon_r(f)$）通常依赖现场测量或经验公式。土壤的非均匀性和分层结构（深层低电阻率层）显著改变高频响应，但精确参数难以获取。Araujo et al.（2021）表明：对于垂直电极，分层土壤的影响比交叉电极更显著。

### 挑战 2：接地极有效长度的确定

超过有效长度后，继续延长接地导体不再显著降低高频阻抗。Alipio et al.（2023）给出不同土壤电阻率下典型接地导体长度参考值：

| $\rho_g$（$\Omega$m） | 250 | 500 | 1000 | 2500 | 5000 |
|---|---|---|---|---|---|
| $l$（m） | 15 | 25 | 40 | 55 | 80 |

### 挑战 3：无源性约束与稳定性

宽带有理拟合若非无源，连接避雷器或电缆后可能出现非物理振荡。需在矢量拟合后执行无源性强制（Passivity Enforcement），确保 $\text{Re}\{Z_{ij}(j\omega)\} \geqslant 0$ 对所有频率成立（Lima et al. 2026）。

### 挑战 4：土壤电离非线性与 EMT 步进耦合

土壤电离的非线性特性与 EMT 时域步进之间的耦合需要迭代处理：大电流注入时接地电阻随时间变化，需在每个步进中更新电导矩阵。

### 挑战 5：多端口模型与网络方程的接口

复杂接地网（如变电站网格）的多端口模型与系统网络方程的接口需处理端口定义一致性问题——端口电压参考电位选取影响等效阻抗的数值。

## 量化性能边界

### GPR 峰值对比（传输线模型 vs HEM 模型）

Alipio et al.（2023）对 138 kV 线路杆塔接地（4 根水平引下线）进行了验证：

| 土壤电阻率 $\rho_g$（$\Omega$m） | $V_p$（Marti TL 模型）（kV） | $V_p$（HEM 模型）（kV） | 误差（%） |
|---|---|---|---|
| 250 | 212 | 223 | 4.9 |
| 500 | 288 | 293 | 1.7 |
| 1000 | 390 | 387 | 0.8 |
| 2500 | 691 | 688 | 0.4 |
| 5000 | 906 | 911 | 0.5 |

传输线模型对高土壤电阻率的精度反而更好（误差 < 1%），适合工程应用。

### 频变土壤对 GPR 的影响

Salarieh et al.（2020）研究显示：考虑频变特性后，GPR 峰值显著降低（vs 常参数土壤），降低幅度随土壤电阻率和含水率增加而增大。对 $\rho = 1000\ \Omega\text{m}$ 的垂直电极，考虑频变特性后 GPR 峰值较常参数模型降低约 30%–50%（具体数值依电极长度和注入电流波形而定）。

### 土壤分层对 GPR 的影响

Araujo et al.（2021）研究表明：在 100 Hz – 10 MHz 频域内，分层土壤对垂直电极 GPR 的影响比对交叉电极更显著。对于垂直电极，深层低电阻率层可降低高频阻抗约 20%–40%（vs 均匀土壤模型）。

## 建模方法分类总览

| 方法 | 核心原理 | 适合用途 | 主要边界 |
|---|---|---|---|
| 集总 R/RL/RC | 尺寸 $\ll$ 波长 | 工频、初步 EMT、保护筛选 | 不能描述空间分布和高频传播 |
| 传输线模型 | 埋地导体电报方程 | 杆塔接地、引下线、互联接地线 | 参数需校核，波长效应在高估时需分段 |
| 多端口 FDNE | 频域有理函数拟合 | 风电场、变电站、复杂接地网 | 有理拟合阶数、有效长度、无源性 |
| 场模型 MoM/FEM/FDTD | 直接求解 Maxwell 方程 | 研究级校核、复杂土壤/几何 | 数据需求高、计算量大、与 EMT 接口复杂 |
| 非线性土壤电离 | 时变电导/电阻 | 大雷电流接地冲击 | 参数可得性和实验验证有限 |

## 适用边界与选择指南

| 场景 | 推荐方法 | 说明 |
|---|---|---|
| 工频接地电阻估算 | 集总 R 模型 | 简单查表或 Sunde 公式即可 |
| 雷电反击分析（杆塔接地） | 传输线模型（Marti） | Alipio 2023 验证误差 < 5%，优先选此 |
| 变电站接地网宽频建模 | 多端口 FDNE + VF | 需场计算工具获取 $Z(\omega)$，后用 VF 拟合 |
| 大雷电流（> 10 kA）冲击 | 非线性电离模型 | 需与传输线模型或 FDNE 叠加 |
| 含分层土壤的精确分析 | MoM/FEM + 分层 Green 函数 | Araujo 2021 方法，需专业工具 |
| 多导体耦合接地网 | 传输线矩阵方程 | 考虑互感、互容耦合，精度最高 |

## 相关方法与模型

- [[ground-potential-rise]]：接地电流导致电位升的主题页
- [[lightning-transient-analysis]]：雷电暂态分析使用接地模型计算直击雷、反击和侵入波
- [[insulation-coordination]]：绝缘配合使用接地模型结果检查设备和保护器应力
- [[earth-return-impedance]]：大地返回阻抗与线路/电缆参数耦合的边界
- [[frequency-dependent-soil]]：土壤参数频变特性，提供土壤电阻率/介电常数的频变模型
- [[underground-cable-modeling]] 和 [[cross-bonded-cable]]：需要接地点阻抗作为护套边界
- [[high-frequency-transient-analysis]]：讨论接地系统在宽频暂态中的数值与物理边界
- [[heidler-function]]：雷电流波形建模（接地电流注入的激励源）
- [[vector-fitting]]：宽频阻抗/导纳的有理函数拟合方法
- [[transmission-line-modeling]]：传输线模型的理论基础

## 来源论文

- Alipio et al. 2023 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model（传输线法杆塔接地，GPR对比数据）
- Lima et al. 2026 - Realization of rational models for tower-footing grounding systems（FDNE阶数与有效长度关系）
- Salarieh et al. 2020 - Electromagnetic transient modeling of grounding electrodes buried in frequency dependent soil with variable water content（频变土壤四模型对比，土壤含水率影响）
- Araujo et al. 2021 - Computation of ground potential rise and grounding impedance of simple arrangement of electrodes buried in frequency-dependent stratified soil（分层土壤MoM分析，VA公式）
- Manunza - Grounding grids in electro-magnetic transient simulations with frequency-dependent equivalent circuit（PI型两端口接地网等值，ATP-EMTP实现）
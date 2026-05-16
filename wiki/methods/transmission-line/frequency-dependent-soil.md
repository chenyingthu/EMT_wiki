---
title: "频率相关土壤特性 (Frequency-Dependent Soil Properties)"
type: method
tags: [soil, frequency-dependent, grounding, wideband, lightning, transient, carson, pollaczek, vector-fitting]
created: "2026-05-02"
updated: "2026-05-16"
---

# 频率相关土壤特性 (Frequency-Dependent Soil Properties)

## 定义与边界

频率相关土壤特性指土壤电导率 $\sigma$、电阻率 $\rho$ 和介电常数 $\varepsilon$ 随频率变化，并通过复数介质参数影响大地返回电流、接地阻抗和线路传播特性的建模问题。它是 EMT 中的参数与方法问题，不等同于单一接地电阻测量，也不等同于土壤电离或击穿模型。

土壤可用复数电导率表示：

$$\sigma^*(\omega) = \sigma(\omega) + \mathrm{j}\omega\varepsilon(\omega) \quad (1)$$

对应复电阻率：

$$\rho^*(\omega) = \frac{1}{\sigma^*(\omega)} \quad (2)$$

本页关注土壤频变参数如何进入 [[earth-return-impedance]]（Carson/Pollaczek 类表达式）、[[grounding-system-model]]（接地网频变阻抗）、[[frequency-dependent-line-model]] 和 [[universal-line-model]]（频变线路参数）。土壤分层、含水率、温度、季节和测量布置都会影响参数可信度。

## EMT 中的作用

在 EMT 中，频率相关土壤特性主要影响：

- **架空线路和地下电缆的大地返回阻抗**：Carson（架空线）和 Pollaczek（地下电缆）大地返回阻抗公式中的 $\sigma(\omega)$ 和 $\varepsilon(\omega)$ 替代常数项
- **接地网、杆塔接地和电极暂态响应**：地电位升（GPR）和接地冲击阻抗的宽频特性
- **雷电、开关陡波和宽频过电压中的地模传播**：数百 kHz 至 MHz 量级频段的地模衰减和相位
- **护套、铠装、接地线和土壤之间的耦合**：护套接地和交叉互联电缆的频变耦合
- **频域参数计算到时域线路模型的转换**：通过 [[vector-fitting]] 等有理拟合方法实现频域到时域的转换

若频段内位移电流项 $\mathrm{j}\omega\varepsilon$ 与传导项 $\sigma$ 不再相对可忽略，则把土壤写成频率无关纯电阻介质可能改变 EMT 结果。例如在雷电频段（数百 kHz 以上），$\mathrm{j}\omega\varepsilon$ 可与 $\sigma$ 同量级。

## 核心机制

### 复数土壤参数模型

土壤电导率和相对介电常数均随频率变化。根据实验室测量数据（Portela 2007, Alipio & Visacro 2015），在 100 Hz 至 2 MHz 范围内：

**Alipio-Visacro 模型**（基于实测验证，推荐使用）：

$$\sigma(\omega) = \sigma_0 \left[1 + \left(\frac{\mathrm{j}\omega}{\omega_0}\right)^n\right] \quad (3)$$

$$\varepsilon_r(\omega) = \varepsilon_r^\infty + \frac{\sigma_0}{\omega_0 \varepsilon_0} \left(\frac{\omega_0}{\mathrm{j}\omega}\right)^n \quad (4)$$

其中 $\sigma_0$ 为低频（100 Hz）电导率，$\varepsilon_r^\infty$ 为高频极限相对介电常数，$\omega_0 = 2\pi \times 100$ rad/s，指数 $n \approx 0.45$（统计平均值）。

**Portela 模型**（更适用于高频）：

Portela 在巴西多个地点进行的大量土壤样本测量（覆盖不同土壤类型和地质结构，100 Hz 至 2 MHz）表明，频变土壤参数可用一阶模型综合：

$$\sigma(\omega) = \sigma_0 \left[1 + \alpha \ln\left(\frac{\omega}{\omega_0}\right) + \mathrm{j}\beta \ln\left(\frac{\omega}{\omega_0}\right)\right] \quad (5)$$

该模型只需三个统计独立参数：低频电导率 $\sigma_0$、频率依赖系数 $\alpha$ 和 $\beta$。这些参数可通过最小二乘曲线拟合测量数据获得。

### 大地返回阻抗中的土壤参数

在电磁场方程或线路参数公式中，土壤参数通过 $\sigma^*$ 进入大地返回阻抗积分。Carson 类表达式（架空线）和 Pollaczek 类表达式（地下电缆）都需要在每个频点使用一致的土壤参数：

对于均匀半无限土壤，大地返回阻抗的积分形式为：

$$Z_g(\omega) = \frac{\mathrm{j}\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-2ha}}{a + \sqrt{a^2 + \mathrm{j}\omega\mu_0 \sigma^*}} \, \mathrm{d}a \quad (6)$$

其中 $h$ 是导线对地高度，$\mu_0$ 是真空磁导率。当 $\sigma^* \to \infty$（理想导体大地）时简化为经典 Carson 公式。

### 频变土壤参数的 EMT 接口

常见经验模型把 $\sigma(\omega)$、$\varepsilon(\omega)$ 或 $\rho^*(\omega)$ 写成少量弛豫项、有理函数或幂律函数。用于 EMT 时，这些频域函数需要通过 [[vector-fitting]] 转成可递推的时域模型：

1. **频域计算**：在 $N$ 个频率采样点计算大地返回阻抗 $Z_g(\omega_k)$
2. **有理拟合**：使用 Vector Fitting 得到极-留数表示 $Z(s) = \sum_{i=1}^N \frac{r_i}{s - p_i}$
3. **时域递推**：将极点 $p_i$ 转换为时域递推关系，嵌入 EMT 网络方程

## 分类与变体

| 类别 | 核心输入 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 常数土壤参数 | 单一电阻率或电导率 | 工频接地、低频近似 | 宽频和高阻土壤需复核；雷电频段可能严重失真 |
| 频变均匀土壤（Alipio-Visacro） | $\sigma(\omega)$、$\varepsilon(\omega)$、指数 $n$ | 架空线/电缆宽频参数，Lightning EMT | 需要低频测量数据；公式基于实证模型 |
| 频变均匀土壤（Portela） | $\sigma_0$、$\alpha$、$\beta$ | 高频（> 1 MHz）接地和雷电分析 | 参数获取需要复杂拟合；高频行为更激进 |
| 分层土壤模型 | 各层厚度和复参数 | 接地网、地下电缆、地质分层 | 参数获取和积分计算复杂；多层土壤需递归等效 |
| 非线性电离模型 | 电场、临界条件、动态电导 | 雷电大电流接地 | 不属于线性小信号频变模型；需要非线性迭代 |

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入层：土壤测量数据 -->
  <rect x="20" y="30" width="180" height="70" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="55" font-family="Arial" font-size="13" fill="#1e40af" text-anchor="middle" font-weight="bold">输入：土壤测量数据</text>
  <text x="110" y="75" font-family="Arial" font-size="11" fill="#3b82f6" text-anchor="middle">σ₀, εᵣ(ω), 频率范围</text>
  <text x="110" y="93" font-family="Arial" font-size="11" fill="#3b82f6" text-anchor="middle">含水率, 温度, 土壤类型</text>

  <!-- 箭头 -->
  <path d="M200 65 L260 65" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- 处理层：频变土壤模型 -->
  <rect x="260" y="20" width="200" height="90" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="360" y="42" font-family="Arial" font-size="13" fill="#166534" text-anchor="middle" font-weight="bold">频变土壤模型 (5类)</text>
  <text x="290" y="62" font-family="Arial" font-size="10" fill="#15803d" text-anchor="left">① 常数土壤参数</text>
  <text x="290" y="76" font-family="Arial" font-size="10" fill="#15803d" text-anchor="left">② Alipio-Visacro 模型</text>
  <text x="290" y="90" font-family="Arial" font-size="10" fill="#15803d" text-anchor="left">③ Portela 模型</text>
  <text x="430" y="62" font-family="Arial" font-size="10" fill="#15803d" text-anchor="left">④ 分层土壤</text>
  <text x="430" y="76" font-family="Arial" font-size="10" fill="#15803d" text-anchor="left">⑤ 非线性电离</text>
  <text x="430" y="90" font-family="Arial" font-size="10" fill="#15803d" text-anchor="left">(不纳入频变分析)</text>

  <!-- 箭头 -->
  <path d="M460 65 L520 65" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- 算法层：Vector Fitting -->
  <rect x="520" y="20" width="160" height="90" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="600" y="42" font-family="Arial" font-size="13" fill="#92400e" text-anchor="middle" font-weight="bold">Vector Fitting</text>
  <text x="600" y="62" font-family="Arial" font-size="11" fill="#b45309" text-anchor="middle">极-留数有理拟合</text>
  <text x="600" y="80" font-family="Arial" font-size="11" fill="#b45309" text-anchor="middle">Σ rᵢ / (s - pᵢ)</text>

  <!-- 箭头 -->
  <path d="M680 65 L740 65" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- 输出层：EMT接口 -->
  <rect x="740" y="20" width="140" height="90" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="810" y="42" font-family="Arial" font-size="13" fill="#5b21b6" text-anchor="middle" font-weight="bold">EMT 输出</text>
  <text x="810" y="62" font-family="Arial" font-size="11" fill="#6d28d9" text-anchor="middle">接地阻抗 Z(s)</text>
  <text x="810" y="80" font-family="Arial" font-size="11" fill="#6d28d9" text-anchor="middle">线路参数矩阵</text>

  <!-- 下方：典型应用场景 -->
  <rect x="20" y="140" width="860" height="70" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="450" y="158" font-family="Arial" font-size="12" fill="#475569" text-anchor="middle" font-weight="bold">典型应用场景</text>

  <text x="50" y="180" font-family="Arial" font-size="11" fill="#64748b">① 架空线路大地返回</text>
  <text x="260" y="180" font-family="Arial" font-size="11" fill="#64748b">② 地下电缆传播</text>
  <text x="460" y="180" font-family="Arial" font-size="11" fill="#64748b">③ 杆塔接地GPR</text>
  <text x="650" y="180" font-family="Arial" font-size="11" fill="#64748b">④ 雷电过电压分析</text>
  <text x="810" y="180" font-family="Arial" font-size="11" fill="#64748b">⑤ EMC评估</text>

  <!-- 下方：量化性能数据 -->
  <rect x="20" y="230" width="860" height="150" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="450" y="248" font-family="Arial" font-size="12" fill="#475569" text-anchor="middle" font-weight="bold">量化性能边界（来源：Schroeder 2018, Alipio 2023）</text>

  <text x="40" y="272" font-family="Arial" font-size="10" fill="#475569" font-weight="bold">GPR 降低幅度：</text>
  <text x="40" y="288" font-family="Arial" font-size="10" fill="#64748b">• ρ₀ = 300 Ωm → 降低 45.0%</text>
  <text x="40" y="302" font-family="Arial" font-size="10" fill="#64748b">• ρ₀ = 1000 Ωm → 降低 58.3%</text>
  <text x="40" y="316" font-family="Arial" font-size="10" fill="#64748b">• ρ₀ = 2500 Ωm → 降低 66.3%</text>
  <text x="40" y="330" font-family="Arial" font-size="10" fill="#64748b">• ρ₀ = 4000 Ωm → 降低最高达 70%+</text>

  <text x="300" y="272" font-family="Arial" font-size="10" fill="#475569" font-weight="bold">绝缘子过电压降低：</text>
  <text x="300" y="288" font-family="Arial" font-size="10" fill="#64748b">• 首次雷击：最大降低 27.1%</text>
  <text x="300" y="302" font-family="Arial" font-size="10" fill="#64748b">• 后续雷击：约 0.4%</text>
  <text x="300" y="316" font-family="Arial" font-size="10" fill="#64748b">• 高土壤电阻率时更显著</text>

  <text x="560" y="272" font-family="Arial" font-size="10" fill="#475569" font-weight="bold">接地阻抗精度：</text>
  <text x="560" y="288" font-family="Arial" font-size="10" fill="#64748b">• ATP-Marti 模型 vs HEM：< 3%</text>
  <text x="560" y="302" font-family="Arial" font-size="10" fill="#64748b">• 有效频率范围：10 MHz (低阻)</text>
  <text x="560" y="316" font-family="Arial" font-size="10" fill="#64748b">• 限制到 1 MHz (2500 Ωm) 精度</text>

  <text x="300" y="350" font-family="Arial" font-size="9" fill="#94a3b8" font-style="italic">数据来源：Schroeder et al. 2018 (Electric Power Systems Research 159)</text>
  <text x="560" y="365" font-family="Arial" font-size="9" fill="#94a3b8" font-style="italic">Alipio et al. 2023 (EPSR 223)</text>

  <!-- 图例 -->
  <rect x="20" y="395" width="15" height="15" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="40" y="407" font-family="Arial" font-size="10" fill="#475569">输入</text>
  <rect x="80" width="15" height="15" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="100" y="407" font-family="Arial" font-size="10" fill="#475569">处理/模型</text>
  <rect x="170" width="15" height="15" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="190" y="407" font-family="Arial" font-size="10" fill="#475569">算法</text>
  <rect x="250" width="15" height="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="270" y="407" font-family="Arial" font-size="10" fill="#475569">输出</text>

  <!-- 定义箭头标记 -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 频率相关土壤特性的 EMT 建模流程与性能边界</p>

## 形式化表达

### 核心公式汇总

**复数电导率**：

$$\sigma^*(\omega) = \sigma(\omega) + \mathrm{j}\omega\varepsilon(\omega) = \sigma(\omega) + \mathrm{j}\omega\varepsilon_0\varepsilon_r(\omega) \quad (1)$$

**大地返回阻抗积分形式**：

$$Z_g(\omega) = \frac{\mathrm{j}\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-2ha}}{a + \sqrt{a^2 + \mathrm{j}\omega\mu_0\sigma^*}} \, \mathrm{d}a \quad (6)$$

**Alipio-Visacro 频变模型**：

$$\sigma(\omega) = \sigma_0 \left[1 + \left(\frac{\mathrm{j}\omega}{2\pi \times 100}\right)^{0.45}\right] \quad \text{[S/m]} \quad (3)$$

$$\varepsilon_r(\omega) = \varepsilon_r^\infty + \frac{\sigma_0}{2\pi \times 100 \cdot \varepsilon_0} \left(\frac{2\pi \times 100}{\mathrm{j}\omega}\right)^{0.45} \quad (4)$$

**Portela 一阶频变模型**：

$$\sigma(\omega) = \sigma_0 [1 + \alpha \ln(\omega/\omega_0) + \mathrm{j}\beta \ln(\omega/\omega_0)] \quad (5)$$

**分层土壤等效电导率（递归算法）**：

对 $N$ 层水平分层土壤，从最底层向上递归等效：

$$\sigma_{eq,k}^{-1} = \sigma_k^{-1} \cdot \frac{\int_0^\infty \frac{\lambda^2}{p_k + \lambda} \prod_{i=1}^{k-1} \frac{\lambda}{p_i + \lambda} \mathrm{d}\lambda}{\int_0^\infty \frac{\lambda}{p_k + \lambda} \prod_{i=1}^{k-1} \frac{\lambda}{p_i + \lambda} \mathrm{d}\lambda} \quad (7)$$

其中 $p_k = \sqrt{\mathrm{j}\omega\mu_0\sigma_k}$ 为第 $k$ 层的电流穿透系数。

**Vector Fitting 有理逼近**：

$$Z_g(s) = \sum_{i=1}^{N_r} \frac{r_i}{s - p_i} + d + s h \quad (8)$$

其中 $r_i$ 为留数，$p_i$ 为极点，$d$ 和 $h$ 为常数项。

## 量化性能边界

| 场景 | 土壤电阻率 | 频变土壤 vs 常数土壤 | 数据来源 |
|------|-----------|---------------------|----------|
| 地电位升（GPR）| 300 Ωm | GPR 降低 45.0% | Schroeder 2018 |
| 地电位升（GPR）| 1000 Ωm | GPR 降低 58.3% | Schroeder 2018 |
| 地电位升（GPR）| 2500 Ωm | GPR 降低 66.3% | Schroeder 2018 |
| 地电位升（GPR）| 4000 Ωm | GPR 降低最高达 70%+ | Schroeder 2018 |
| 绝缘子过电压 | 任意 | 首次雷击最大降低 27.1% | Schroeder 2018 |
| 绝缘子过电压 | 任意 | 后续雷击约 0.4% | Schroeder 2018 |
| 接地冲击阻抗 | 250 Ωm | ATP-Marti vs HEM < 3% | Alipio 2023 |
| 接地冲击阻抗 | 2500 Ωm | 限制到 1 MHz 精度 | Alipio 2023 |

**关键发现**（Schroeder 2018）：
- 频变土壤对 GPR 的影响远大于对绝缘子过电压的影响
- 高土壤电阻率时，频变效应更显著
- 将杆塔接地简化为工频接地电阻可能导致严重的 GPR 高估（低估雷电性能）
- 绝缘子过电压对土壤常数 vs 频变的敏感性较低（差异 < 3%）

## 测量与参数识别

土壤参数可来自现场电阻率测试、实验室样品、频域阻抗谱或文献参数。用于 EMT 页面时，应至少说明：

- **测量对象**：表观电阻率、复电阻率、接地阻抗还是线路端口响应
- **频率范围**：低频（100 Hz）、工频（50/60 Hz）、雷电频段（100 kHz - 2 MHz）
- **含水率、温度、样品或现场布置**
- **是否假设均匀半无限土壤、水平分层土壤或局部三维结构**
- **参数是否直接用于线路/接地模型，还是先经过拟合和有理化**

没有这些信息时，只能写"参数不确定性会影响结果"，不应给出固定安全裕度或误差保证。

### 参数获取方法

| 方法 | 适用场景 | 参数输出 | 精度 |
|------|---------|---------|------|
| Wenner 四极法 | 现场低频电阻率 | $\rho_0$ | ±10% |
| 频域阻抗谱 | 实验室样品 | $\sigma(\omega)$、$\varepsilon_r(\omega)$ | ±5% |
| 时域反射（TDR）| 原位快速测量 | $\rho_0$ 和大致分层 | 粗略 |
| 曲线拟合 | Portela/AV 模型参数 | $\alpha$、$\beta$、$n$ | 依赖数据质量 |

## 关键技术挑战

1. **参数获取困难**：土壤参数空间变化很强，单点测量不一定能代表整条线路走廊或接地网范围；高频测量技术复杂，需要专业设备

2. **无穷积分的计算**：Carson/Pollaczek 阻抗公式含无穷积分，Gauss 求积数值计算开销大；在多频率点评估时成为计算瓶颈

3. **模型选择不确定性**：Alipio-Visacro、Portela、Longmire-Smith 等多种模型并存，高电阻率土壤下各模型行为差异显著（可达数十个百分点）

4. **因果性和稳定性**：频域土壤模型直接用于时域 EMT 时，需要检查有理逼近的因果性（极点实部 < 0）和无源性（留数符号正确）

5. **非线性电离的耦合**：雷电大电流下土壤电离效应与频变特性耦合，需要迭代处理非线性，增加了建模复杂度

## 适用边界与失败模式

| 场景 | 适用性 | 原因 |
|------|-------|------|
| 工频接地计算 | ★★★★★ | 常数电阻率近似足够 |
| 雷电暂态分析（低阻土壤）| ★★★★★ | 频变效应显著，Alipio-Visacro 验证良好 |
| 雷电暂态分析（高阻土壤）| ★★★★☆ | 频变效应更显著，但模型差异大 |
| 开关操作暂态 | ★★★☆☆ | 频率介于工频和雷电之间，视具体系统 |
| 地下电缆传播 | ★★★★☆ | 地模衰减和色散受频变土壤影响 |
| 非线性土壤电离 | ★★☆☆☆ | 需要单独的非线性模型 |
| 复杂三维地质结构 | ★★☆☆☆ | 需要场模型或测量校核 |
| 实时仿真 | ★★★☆☆ | Vector Fitting 阶数影响计算效率 |

**失败模式**：

- **常数土壤假设**：在数百 kHz 以上频段低估接地阻抗，导致 GPR 计算偏低
- **模型不匹配**：Portela 模型在高频段行为较 Alipio-Visacro 更激进，混用会导致结果差异
- **Vector Fitting 阶数不足**：低阶逼近会在高频端出现振荡；过阶则增加计算成本
- **忽略有效长度**：接地极超过有效长度后，远端电流辐射到土壤，高频阻抗趋于纯电阻

## 相关页面关系

- [[frequency-dependent-soil-model]] 更偏向具体模型族和参数表达，本页强调方法边界和 EMT 接口
- [[earth-return-impedance]] 使用土壤参数计算线路大地返回阻抗（Carson/Pollaczek 类表达式）
- [[grounding-system-modeling]] 和 [[grounding-system-model]] 处理接地网与电极的系统模型
- [[cable-model]] 和 [[underground-cable-modeling]] 是频变土壤影响地下电缆传播的主要应用
- [[transmission-line-model]] 是频变土壤进入线路参数体系的总入口
- [[vector-fitting]] 是频域土壤参数到时域 EMT 模型转换的核心算法
- [[universal-line-model]] 使用频变参数进行行波建模
- [[grounding-lightning-overvoltage]] 关注频变土壤在雷电过电压问题中的后果

## 来源论文

- [[inclusion-of-frequency-dependent-soil-parameters-in|de Lima & Portela 2007]] — 提出一阶模型综合频变土壤参数，扩展 Carson/Pollaczek 公式，包含 Gauss 求积数值计算无穷积分
- [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Schroeder et al. 2018]] — 系统比较 Alipio-Visacro/Portela/Longmire-Smith 模型对 GPR 和绝缘子过电压的影响，提供量化边界数据
- [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Alipio et al. 2023]] — 将杆塔接地建模为传输线，ATP-Marti 模型实现，验证精度 < 3%
- [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient|Azevedo et al. 2024]] — 评估土壤物理因素（湿度、孔隙率、温度）对风机接地暂态的影响，比较六种土壤模型
- [[multi-layer-earth-structure-approximation-by-a-homogeneous-conductivity-soil-for|Lima et al. 2026]] — N 层水平分层土壤递归等效为均匀电导率土壤，扩展 Carson 公式可用
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o|Li et al. 2016]] — 分析土壤参数频率特性对地返回线路参数的影响
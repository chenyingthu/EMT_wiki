---
title: "气体绝缘开关设备建模方法 (GIS)"
type: method
tags: [gis, gas-insulated-switchgear, switching-transient, lightning, vfto, vft, enclosure, control-cable, coaxial-mode, fdt]
created: "2026-05-05"
updated: "2026-05-13"
---

# 气体绝缘开关设备建模方法 (GIS)

## 定义

气体绝缘开关设备（Gas-Insulated Switchgear, GIS）建模方法指在电磁暂态（EMT）仿真中对 GIS 内部导体-外壳-接地系统的**高频波传播行为**进行数值表征的技术体系。GIS 的核心结构是同轴式传输线：中心导体（母线）被 SF₆ 气体绝缘，外围为金属接地外壳（pipe/duct/tank），二者之间形成 TEM 模传播通道。

GIS 建模关注的是 **VFT/VFTO（极快暂态 Very Fast Transient / Very Fast Transient Overvoltage）** 范围内的波过程，频率范围从 1 MHz 至 140 MHz 以上，对应波长从数百米到数毫米量级。其核心挑战在于：

- 同轴模式（coaxial mode）的传播参数（传播函数 $h(\omega)$、特征导纳 $Y_C(\omega)$）随频率的精确表征
- 外壳接地方式（单端接地、双端接地、经电阻接地）对波反射和外壳电压的强烈影响
- 分支母线（branch GIB）、断路器（CB）、隔离开关（DS）、电压/电流互感器（VT/CT）的等效建模
- 控制电缆与 GIS 母线之间的互感耦合导致的感应过电压

GIS 建模是操作过电压、绝缘配合、电磁干扰（EMD）和控制回路抗扰度评估的基础。

## EMT 中的角色

在 EMT 仿真中，GIS 建模主要用于以下场景：

1. **VFTO 过电压评估**：隔离开关操作产生的极快暂态过电压可达 1.2–3.0 pu（UHV 系统中更高），对 GIS 主绝缘和控制回路绝缘构成威胁
2. **电磁干扰（EMD）分析**：VFT 的高频分量（1–140 MHz）通过互感耦合到控制电缆，引起继电器误动、电子设备故障
3. **绝缘配合设计**：确定 GIS 内各部件的绝缘裕度，特别是 UHV GIS 相对较低的绝缘水平
4. **外壳暂态电压分析**：外壳感应电压（0.1–0.7 pu）对维护人员安全和外壳绝缘的影响
5. **与外部设备耦合**：GIS 通过套管（bushing）与外部架空线、电缆、变压器连接，波过程在接口处发生反射和透射

### 核心挑战

- **频率范围极宽**：从 50 Hz 工频到 140 MHz 极高频，单一模型难以覆盖
- **几何结构敏感**：导体半径、外壳半径、SF₆ 相对介电常数（εᵣ ≈ 1.0–1.1）、支撑绝缘子等效介电常数（εᵣ ≈ 2.3–6.0）对传播参数影响显著
- **接地方式多样性**：双端接地、单端接地、经电阻接地、交叉互联等，每种方式对应不同的波反射边界
- **测量设备建模**：VT、CT 在高频下的等效参数（集中电容 vs. 详细模型）影响 VFT 波形

## EMT 建模方法

GIS 在 EMT 软件（EMTP-ATP、EMTRV、PSCAD 等）中的建模基于**传输线理论**，将 GIS 视为同轴传输线系统。根据频率范围和精度需求，可分为以下方法：

### 方法一：常参数（CP）传输线模型

**原理**：使用固定频率下的传播参数和特征导纳，适用于特定频带（如 1–20 MHz）的快速仿真。

GIS 同轴模式的传播参数可由几何尺寸解析计算：

$$Z_0 = \frac{1}{2\pi} \sqrt{\frac{\mu_0}{\varepsilon_0 \varepsilon_r}} \ln\left(\frac{r_p}{r_c}\right) \quad [\Omega] \tag{1}$$

$$v = \frac{1}{\sqrt{L'C'}} = \frac{1}{\sqrt{\mu_0 \varepsilon_0 \varepsilon_r}} \quad [\text{m/s}] \tag{2}$$

$$h(\omega) = e^{-\gamma l} = e^{-(\alpha + j\beta)l} \tag{3}$$

其中 $r_p$ 为外壳内半径，$r_c$ 为中心导体半径，$\varepsilon_r$ 为 SF₆ 气体相对介电常数（≈ 1.0–1.1），$l$ 为 GIS 段长度。

**特点**：
- 计算效率高，每个 GIS 段仅需数个 pi 节
- 频率范围有限，通常覆盖 1–20 MHz
- 对分支母线和接地回路的建模需要额外等效

**适用场景**：VFT 波形定性分析、绝缘配合初步评估、多节点 GIS 系统快速仿真

### 方法二：宽频（WB）传输线模型

**原理**：使用频率相关的传播参数，通过矢量拟合（Vector Fitting）将复频域响应 $h(\omega)$ 和 $Y_C(\omega)$ 拟合为有理函数：

$$\tilde{h}(\omega) \approx \sum_{g=1}^{G} \left( \mathbf{G}_g + \sum_{i=1}^{N_g} \frac{\mathbf{R}_{g,i}}{j\omega - a_{g,i}} \right) e^{-j\omega \tau_g} \tag{4}$$

$$\tilde{Y}_C(\omega) \approx \mathbf{R}_0 + \sum_{i=1}^{N_Y} \frac{\mathbf{R}_i}{j\omega - a_i} \tag{5}$$

**特点**：
- 覆盖宽频范围（1 Hz – 100+ MHz）
- 自动包含导体集肤效应和介质损耗
- 计算量较大，但精度显著优于 CP 模型

**适用场景**：VFT 定量分析、控制电缆感应电压精确计算、FDTD 验证基准

### 方法三：有限截面（Finite Sections）模型

**原理**：将导体截面沿径向离散为多层薄壳，每层用 pi 节表示，同时模拟**轴向**和**径向**电磁波传播。对同轴 GIS，核心导体和外壳分别被离散为多层同心圆柱壳：

$$R_{\text{layer}} = \rho \frac{2\pi l}{2\pi r \Delta r} = \frac{\rho l}{r \Delta r} \quad [\Omega] \tag{6}$$

$$L_{\text{layer}} = \mu_0 \mu_r \frac{l \ln(r_2/r_1)}{2\pi} \quad [\text{H}] \tag{7}$$

其中 $r_1, r_2$ 为当前层的内外半径，$\Delta r = r_2 - r_1$ 为层厚，$\rho$ 为材料电阻率。

**特点**：
- 物理意义明确，直接模拟电磁波在导体内部的传播
- 可精确表征外壳厚度方向的集肤效应（典型 3.5 mm 铅护套需 6–7 层）
- 节点数多（典型 GIS 段约 1300 节点、2850 支路），计算量大

**适用场景**：外壳暂态电压空间分布、导体内部涡流效应、高频损耗精确计算

### 方法四：FDTD 三维场路耦合模型

**原理**：使用有限时域差分（FDTD）方法对 GIS 三维结构进行全电磁场求解，再通过端口提取等效电路参数嵌入 EMTP：

$$\frac{\partial \mathbf{E}}{\partial t} = \frac{1}{\varepsilon} \nabla \times \mathbf{H} - \frac{\sigma}{\varepsilon} \mathbf{E} \tag{8}$$

$$\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu} \nabla \times \mathbf{E} \tag{9}$$

**特点**：
- 完整三维电磁场，自动包含辐射损耗
- 可精确建模分支结构、支撑绝缘子、套管等复杂几何
- 内存和 CPU 消耗巨大（典型 12 m GIB 需大量网格）

**适用场景**：GIS 局部放电仿真、极端高频 VFT 波形、辐射干扰评估

### 方法对比

| 方法 | 频带范围 | 节点数/段 | 精度 | 计算速度 | 推荐场景 |
|------|---------|----------|------|---------|---------|
| CP 线模型 | 1–20 MHz | 2–5 pi 节 | 中等 | 快 | 快速初步分析 |
| WB 线模型 | 1 Hz–100+ MHz | 8–20 极点 | 高 | 中等 | VFT 定量分析 |
| 有限截面 | DC–100+ MHz | 1000–3000 | 极高 | 慢 | 外壳涡流、损耗 |
| FDTD | DC–140+ MHz | 10⁴–10⁵ | 极高 | 极慢 | 三维场、辐射 |

## 形式化表达

### 同轴模式传播方程

GIS 中心导体与外壳之间的 TEM 波传播由 Telegrapher 方程描述：

$$\frac{\partial v(x,t)}{\partial x} = -L' \frac{\partial i(x,t)}{\partial t} - R' i(x,t) \tag{10}$$

$$\frac{\partial i(x,t)}{\partial x} = -C' \frac{\partial v(x,t)}{\partial t} - G' v(x,t) \tag{11}$$

其中 $L', C', R', G'$ 为单位长度分布参数。在频域中，传播函数和特征导纳为：

$$\gamma(\omega) = \sqrt{(R' + j\omega L')(G' + j\omega C')} = \alpha(\omega) + j\beta(\omega) \tag{12}$$

$$Z_C(\omega) = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}} \tag{13}$$

### 分支母线的等效电容

分支母线（branch GIB）在高频下等效为集中电容 [Ametani 2018, Eq.(1)]：

$$C_b = \frac{1}{z_{\text{oc}} \cdot c} \quad [\text{F/m}] \tag{14}$$

其中 $z_{\text{oc}}$ 为同轴模式开路阻抗，$c$ 为波速。对于典型 500 kV GIS（$r_c = 13.5$ cm, $r_p = 76$ cm, εᵣ = 1.05），$C_b \approx 81$ pF/m。

### 引线波阻抗

连接电源与 GIS 母线的引线（lead wire）在 VFT 频率下必须作为分布参数线建模。垂直引线的波阻抗近似为 [Ametani 2018, Eq.(2)]：

$$Z_{\text{ov}} = 60 \ln\left(\frac{2h}{r}\right) - 1 \quad [\Omega] \tag{15}$$

其中 $h$ 为引线高度（长度），$r$ 为引线半径。

### 多导体电缆合并模型

对于含外壳接地和外部耦合的 GIS 系统，Gustavsen [2023] 提出将测量得到的同轴传播特性与经典多导体模型合并：

$$\tilde{\mathbf{H}} = \mathbf{LP}(\omega) \cdot \mathbf{H} + \mathbf{HP}(\omega) \cdot \mathbf{T}_I \text{diag}(\mathbf{h}_{\text{coax}}^T \mathbf{h}) \mathbf{T}_I^{-1} \tag{16}$$

$$\tilde{\mathbf{Y}}_C = \mathbf{LP}(\omega) \cdot \mathbf{Y}_C + \mathbf{HP}(\omega) \cdot \mathbf{Y}_{C,\text{merged}} \tag{17}$$

其中低通/高通滤波器由截止频率 $\omega_0$ 定义：

$$\text{LP}(\omega) = \frac{\omega_0}{j\omega + \omega_0}, \quad \text{HP}(\omega) = 1 - \text{LP}(\omega) = \frac{j\omega}{j\omega + \omega_0} \tag{18}$$

该合并方法确保低频段保留经典模型精度，高频段采用测量/精确计算的同轴模式数据。

## 关键技术挑战

### 1. 外壳接地方式的精确建模

GIS 外壳电压强烈依赖于接地方式 [Ametani 2018]。双端接地时，外壳在高频下形成完整屏蔽层， earth 电阻率影响极小；单端接地时，外壳产生显著暂态电压（可达 0.1–0.7 pu）；经电阻接地时，电阻值（典型 2–10 Ω）显著改变波反射系数。外壳接地电阻在 EMT 中必须显式建模为集中参数或与分布参数线串联。

### 2. 分支母线的等效与谐振

分支母线引起高频振荡，使 VFT 波形高度振荡 [Ametani 2018]。实测波形受示波器采样频率限制（1970 年代设备最高仅数十 MHz），仿真中需使用足够高的频率分辨率。分支可用等效电容 $C_b$ 近似，但更精确的建模需将分支段作为独立传输线段处理。

### 3. 控制电缆感应电压

控制电缆沿 GIS 母线敷设时，通过互感耦合感应 VFT 过电压 [Ametani 2018]。实测数据显示：

- CT 二次回路：45–55 MHz，20–600 V（峰值）
- VT 二次回路：8–20 MHz，20–120 V（峰值）
- 控制回路：8–55 MHz，10–100 V（峰值）
- 1000 kV GIS VT：40–80 MHz，60–450 V（峰值）

感应电压与控制电缆平行于 GIS 母线的长度近似成正比，频率分量在 2–20 MHz 范围。仿真时必须详细建模 VT/CT 高频等效电路和控制电缆的分布参数。

### 4. FDTD 与 EMTP 的交叉验证

FDTD 三维场计算与 EMTP 电路仿真在 VFT 问题上显示出合理的一致性 [Ametani 2018]，但 FDTD 结果通常振荡性较低，原因是 FDTD 自动包含了辐射损耗（radiation losses），而 EMTP 电路模型无法直接表征辐射。这一差异在评估 EMI 时尤为重要。

## 量化性能边界

### VFT 过电压实测数据汇总

根据 Ametani et al. [2018] 汇总的 24 篇文献实测结果：

| 电压等级 | 频率范围 | 过电压幅值 | 数据来源 |
|---------|---------|-----------|---------|
| 500/550 kV | 1–140 MHz | 1.2–3.0 pu | [5,6,13] |
| 550 kV | 10–50 MHz | 2.7 pu | [10] |
| UHV | 1–5 MHz | 2.4–3.0 pu | [7] |
| 1100 kV | 2–31 MHz | 1.35 pu | [19] |
| 1100 kV | 0.25–2 MHz | 1.05–1.62 pu | [20] |
| 1100 kV | 8–118 MHz | 1.82–2.19 pu | [21] |

### 外壳电压

| 电压等级 | 频率范围 | 外壳电压 | 数据来源 |
|---------|---------|---------|---------|
| 500 kV | 2.5–10 MHz | 0.1 pu | [5] |
| 550 kV | 2–50 MHz | 0.1–0.7 pu | [10] |

### 控制回路 EMD

13 个 GIS 站、58 个测试案例 [16] 显示：

| 回路类型 | 频率范围 | 峰峰值电压 |
|---------|---------|-----------|
| CT 二次 | 5–70 MHz | 80–700 V |
| VT 二次 | 10–80 MHz | 10–600 V |
| 控制回路 | 1–70 MHz | 10–450 V |

### 模型精度验证

Ametani et al. [2018] 对比了 CP 模型、WB 模型和单模 CP 模型在原型 GIB 测试中的表现：

- **核心电压波形**：三种模型结果几乎一致，与实测波形吻合
- **外壳电压**：WB 模型在外壳开路工况下显示比 CP 模型更高的振荡性，与实测趋势一致
- **分支母线等效**：使用 $C_b = 81$ pF/m 等效时，仿真波形与实测波形吻合最佳

Gustavsen [2023] 对合并模型的验证：

- 高频段（> 300 kHz）：合并模型与测量数据的同轴模式传播特性误差 < 5%
- 低频段（50 Hz–10 kHz）：合并模型与经典模型的正/零序短路阻抗偏差 < 2%
- 波前阻尼：合并模型能准确复现测量中的波前衰减，经典模型阻尼明显不足

## 适用边界与选择指南

### 建模方法选择

| 应用场景 | 推荐模型 | 频率要求 | 说明 |
|---------|---------|---------|------|
| VFT 过电压定性评估 | CP 线模型 | 1–20 MHz | 快速多节点仿真 |
| VFT 定量分析 | WB 线模型 | 1 Hz–100+ MHz | EMT 软件标准方法 |
| 外壳涡流/损耗分析 | 有限截面模型 | DC–100+ MHz | 需详细几何参数 |
| 三维场/辐射分析 | FDTD | DC–140+ MHz | 研究用途 |
| 控制电缆 EMD 分析 | WB + VT/CT 详细模型 | 1 Hz–80 MHz | 需互感耦合建模 |

### 关键建模注意事项

1. **接地假设**：VFT 高频区域（> 1 MHz）， earth 可视为理想导体（σ → ∞）或铝板，earth 电阻率对 VFT 影响极小 [Ametani 2018, 结论(1)]
2. **外壳接地必须精确**：外壳电压波形强烈依赖于接地方式，核心电压受影响较小 [Ametani 2018, 结论(2)]
3. **分支母线等效**：分支可用集中电容 $C_b$ 近似 [Ametani 2018, 结论(3)]，但需注意示波器带宽限制
4. **直流偏置处理**：带电 GIS 包含直流电压分量，EMTP 无法直接处理，需用低频交流电压替代 [Ametani 2018, 结论(4)]
5. **引线必须分布参数建模**：连接电源与 GIS 母线的引线长度在 VFT 频率下不可忽略，必须作为 CP 线建模 [Ametani 2018, 结论(5)]
6. **互感耦合不可忽略**：控制电缆沿 GIS 敷设时，接地网格电压不能假设为零 [Ametani 2018, 结论(7)]

### 失效边界

- **低频集总参数模型**：无法解释 GIS 内部的快速波过程，不适用于 VFT 分析
- **忽略外壳的导体单模模型**：在双端接地以外的接地方式下误差显著
- **未考虑分支母线的模型**：遗漏高频振荡源，波形失真
- **未考虑接地电阻的模型**：外壳电压计算严重偏差
- **FDTD 网格不足**：140 MHz 对应波长仅 2.1 m，网格尺寸需 < λ/20 ≈ 10 cm，对大型 GIS 不切实际

## GIS 同轴传输线建模流程

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>
    </filter>
  </defs>

  <!-- Title -->
  <text x="450" y="30" fill="#1a1a2e" font-size="16" font-weight="bold" text-anchor="middle">GIS 同轴传输线 EMT 建模流程</text>

  <!-- Step 1: 几何参数输入 -->
  <rect x="30" y="60" width="160" height="60" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="110" y="83" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">几何参数输入</text>
  <text x="110" y="100" fill="#4b6b8f" font-size="10" text-anchor="middle">r_c, r_p, ε_r, l, 接地方式</text>

  <!-- Step 2: 分布参数计算 -->
  <rect x="250" y="60" width="160" height="60" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="330" y="83" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">分布参数计算</text>
  <text x="330" y="100" fill="#3a7a5a" font-size="10" text-anchor="middle">Z(ω), Y(ω), h(ω), Y_C(ω)</text>

  <!-- Step 3: 模型选择 -->
  <rect x="470" y="60" width="160" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="550" y="83" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">模型选择</text>
  <text x="550" y="100" fill="#a16207" font-size="10" text-anchor="middle">CP / WB / 有限截面 / FDTD</text>

  <!-- Step 4: 元件等效 -->
  <rect x="30" y="200" width="160" height="60" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="110" y="223" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">元件等效建模</text>
  <text x="110" y="240" fill="#3a7a5a" font-size="10" text-anchor="middle">DS, CB, VT, CT, 分支C_b</text>

  <!-- Step 5: 互感耦合 -->
  <rect x="250" y="200" width="160" height="60" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="330" y="223" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">互感耦合建模</text>
  <text x="330" y="240" fill="#3a7a5a" font-size="10" text-anchor="middle">控制电缆平行耦合</text>

  <!-- Step 6: 边界条件 -->
  <rect x="470" y="200" width="160" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="550" y="223" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">接地边界条件</text>
  <text x="550" y="240" fill="#a16207" font-size="10" text-anchor="middle">双端接地/单端/电阻接地</text>

  <!-- Step 7: 仿真验证 -->
  <rect x="340" y="340" width="220" height="60" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="450" y="363" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">VFT 仿真与验证</text>
  <text x="450" y="380" fill="#6b21a8" font-size="10" text-anchor="middle">对比实测波形 / FDTD 交叉验证</text>

  <!-- Arrows -->
  <line x1="190" y1="90" x2="248" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="410" y1="90" x2="468" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="550" y1="120" x2="550" y2="198" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="190" y1="230" x2="248" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="410" y1="230" x2="468" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="380" y1="260" x2="380" y2="338" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="500" y1="260" x2="500" y2="338" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Legend -->
  <text x="30" y="415" fill="#333" font-size="10" font-weight="bold">输入/源</text>
  <rect x="80" y="405" width="12" height="10" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="100" y="414" fill="#555" font-size="10">处理/模型</text>
  <rect x="160" y="405" width="12" height="10" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="240" y="414" fill="#555" font-size="10">算法/方法</text>
  <rect x="320" y="405" width="12" height="10" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="400" y="414" fill="#555" font-size="10">输出/结果</text>
  <rect x="480" y="405" width="12" height="10" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · GIS 同轴传输线 EMT 建模流程（基于 Ametani 2018, Gustavsen 2023, Meredith 1997）</p>

## GIS 截面几何与传播参数

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>
    </filter>
  </defs>

  <text x="350" y="25" fill="#1a1a2e" font-size="15" font-weight="bold" text-anchor="middle">GIS 同轴截面几何结构</text>

  <!-- Outer pipe (grounded enclosure) -->
  <circle cx="250" cy="200" r="120" fill="none" stroke="#2563eb" stroke-width="3"/>
  <circle cx="250" cy="200" r="115" fill="#dbeafe" stroke="#2563eb" stroke-width="1" opacity="0.5"/>
  <text x="115" y="95" fill="#2563eb" font-size="11" font-weight="bold">外壳 (Pipe)</text>
  <text x="115" y="108" fill="#4b6b8f" font-size="10">接地, 内半径 r_p</text>

  <!-- SF6 insulating gas region -->
  <circle cx="250" cy="200" r="80" fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="340" y="140" fill="#16a34a" font-size="10">SF₆ 气体</text>
  <text x="340" y="153" fill="#3a7a5a" font-size="9">ε_r ≈ 1.0–1.1</text>

  <!-- Spacer (insulating support) -->
  <ellipse cx="250" cy="120" rx="15" ry="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="270" y="115" fill="#d97706" font-size="9">支撑绝缘子</text>
  <text x="270" y="126" fill="#a16207" font-size="8">ε_r ≈ 2.3–6.0</text>

  <!-- Inner conductor -->
  <circle cx="250" cy="200" r="35" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="250" y="197" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle">中心导体</text>
  <text x="250" y="210" fill="#a16207" font-size="9" text-anchor="middle">半径 r_c</text>

  <!-- Dimension arrows and labels -->
  <!-- r_p arrow -->
  <line x1="250" y1="200" x2="370" y2="200" stroke="#dc2626" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="315" y="195" fill="#dc2626" font-size="11" font-weight="bold">r_p</text>

  <!-- r_c arrow -->
  <line x1="250" y1="200" x2="285" y2="200" stroke="#7c3aed" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="267" y="195" fill="#7c3aed" font-size="11" font-weight="bold">r_c</text>

  <!-- 500kV example dimensions -->
  <rect x="440" y="60" width="230" height="130" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="555" y="82" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">典型 500 kV GIS 参数</text>
  <text x="455" y="102" fill="#333" font-size="10">r_c = 13.5 cm</text>
  <text x="455" y="118" fill="#333" font-size="10">r_p = 76.0 cm</text>
  <text x="455" y="134" fill="#333" font-size="10">ε_r(SF₆) = 1.05</text>
  <text x="455" y="150" fill="#333" font-size="10">Z₀ ≈ 70 Ω</text>
  <text x="455" y="166" fill="#333" font-size="10">v ≈ 2.7 × 10⁸ m/s</text>

  <!-- 1100kV example -->
  <rect x="440" y="210" width="230" height="100" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="2" filter="url(#shadow)"/>
  <text x="555" y="232" fill="#7f1d1d" font-size="12" font-weight="bold" text-anchor="middle">典型 1100 kV UHV GIS 参数</text>
  <text x="455" y="252" fill="#333" font-size="10">r_c = 13.5 cm</text>
  <text x="455" y="268" fill="#333" font-size="10">r_p = 77.0 cm</text>
  <text x="455" y="284" fill="#333" font-size="10">ε_r(SF₆) = 1.05</text>
  <text x="455" y="300" fill="#333" font-size="10">ρ_c = 1.8×10⁻⁸ Ω·m</text>
  <text x="455" y="316" fill="#333" font-size="10">ρ_p = 1.5×10⁻⁷ Ω·m</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图2 · GIS 同轴截面几何结构及典型参数（Ametani 2018, Fig. 1, Fig. 10）</p>

## 相关方法

- [[switching-transient]] — 操作过电压与极快暂态的宏观现象
- [[lightning-overvoltage]] — 雷击暂态与 GIS 接口耦合
- [[grounding-system]] — GIS 外壳与接地回路的耦合建模
- [[transmission-line-theory]] — 高频传播建模的传输线理论基础
- [[electromagnetic-transient]] — EMT 仿真的上位概念
- [[frequency-dependent-modeling]] — 频率相关传输线模型（WB/ULM）
- [[vector-fitting]] — 有理函数拟合方法，用于传播参数离散化
- [[bergeron-line-model]] — 行波线模型在 GIS 中的适用性
- [[switching-transient]] — GIS 电磁干扰（EMD）分析的暂态背景

## 来源论文

- **Ametani et al. 2018** — "Electromagnetic disturbances in gas-insulated substations and VFT calculations"（Electric Power Systems Research 160, 2018）：系统总结了 GIS 中 VFT 的实测数据（频率 1–140 MHz，过电压 1.2–3.0 pu），详细说明了 EMTP 中 GIS 元件的建模方法（CP/WB 线模型、分支等效、引线建模、VT/CT 高频等效），并对比了 FDTD 与 EMTP 的三维仿真结果。是 GIS VFT 建模的权威综述。
- **Meredith 1997** — "EMTP Modeling of Electromagnetic Transients in Multi-Mode Coaxial Cables by Finite Sections"（IEEE Trans. Power Delivery, 1997）：提出有限截面法（finite sections）建模同轴电缆，同时模拟轴向和径向电磁波传播，可精确表征导体集肤效应和多层结构。为 GIS 外壳涡流和厚度方向高频效应提供了精确建模方法。
- **Gustavsen 2023** — "Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics"（IEEE Trans. Power Delivery, 2023）：提出将测量得到的同轴传播特性与经典多导体传输线模型合并的方法，通过低通/高通滤波器在中间频率平滑过渡，确保低频保留经典模型精度、高频采用精确同轴模式数据。适用于 GIS 外壳接地方式变化时的精确仿真。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[expanding-the-measuring-range-via-s-parameters-in-a-ehv-voltage-transformer-mode|Expanding the measuring range via S-parameters in a EHV volt]] | 2021 |

---
title: "电缆模型 (Cable Model)"
type: model
tags: [cable, underground, submarine, frequency-dependent, multi-core, coaxial, crossbonded, armor, ULM]
created: "2026-04-13"
updated: "2026-05-14"
---

# 电缆模型 (Cable Model)

## 定义

电力电缆（地下电缆、海底电缆）的电磁暂态（EMT）建模是电力系统仿真中最为复杂的环节之一。与架空线路不同，电缆具有多层同轴几何结构（导体→半导体层→绝缘层→金属护套→铠装层→外部介质），导致**集肤效应、邻近效应、螺线管效应**和**护套接地方式**对阻抗特性产生决定性影响。电缆的电磁耦合强度比架空线路高 1–2 个数量级，频率相关特性更为显著，宽频带（0.001 Hz–1 MHz）建模成为必需。

电缆模型的核心输入是**每单位长度（p.u.l.）串联阻抗矩阵 $\mathbf{Z}(\omega)$** 和**并联导纳矩阵 $\mathbf{Y}(\omega)$**，它们通过telegrapher方程（1）–（2）描述沿电缆长度的电压和电流变化：

$$
-\frac{d\mathbf{v}(\omega)}{dx} = \mathbf{Z}(\omega)\mathbf{i}(\omega) \quad (1)
$$

$$
-\frac{d\mathbf{i}(\omega)}{dx} = \mathbf{Y}(\omega)\mathbf{v}(\omega) \quad (2)
$$

由（1）和（2）导出的telegrapher波动方程为：

$$
\frac{d^2\mathbf{v}}{dx^2} = \mathbf{ZY}\mathbf{v} \quad (3a)
$$

$$
\frac{d^2\mathbf{i}}{dx^2} = \mathbf{YZ}\mathbf{i} \quad (3b)
$$

求解（3a）和（3b）需要边界条件。在电缆两端（节点1和2），终端行为由（4a）和（4b）定义：

$$
\mathbf{i}_1 - \mathbf{Y}_C\mathbf{v}_1 = -\mathbf{H}(\mathbf{i}_2 + \mathbf{Y}_C\mathbf{v}_2) \quad (4a)
$$

$$
\mathbf{i}_2 - \mathbf{Y}_C\mathbf{v}_2 = -\mathbf{H}(\mathbf{i}_1 + \mathbf{Y}_C\mathbf{v}_1) \quad (4b)
$$

其中 $\mathbf{H}$ 为传播函数矩阵，$\mathbf{Y}_C$ 为特征导纳矩阵。对于长度为 $l$ 的电缆，它们与 $\mathbf{Z}$ 和 $\mathbf{Y}$ 的关系为：

$$
\mathbf{H} = e^{-\sqrt{\mathbf{ZY}}\,l} \quad (5)
$$

$$
\mathbf{Y}_C = \mathbf{Z}^{-1}\sqrt{\mathbf{ZY}} = \sqrt{\mathbf{Z}\mathbf{Y}^{-1}} \quad (6)
$$

## EMT中的角色

电缆模型在EMT仿真中承担以下关键角色：

1. **高频暂态分析**：预测变压器和电机绕组上的电压应力，计算陡波前脉冲在馈电电缆上的传播效应。传统电缆模型在极高频率（>100 kHz）下可能产生过弱的阻尼，导致电压波前失真。
2. **HVDC海底电缆系统**：海上风电场（如TenneT埋设深度超5 m的海底电缆）和长距离海底输电（>3700 km概念）的EMT仿真，要求同时考虑两层损耗介质（海水/海床土壤+电缆绝缘）的电磁场衰减。
3. **交叉互联接地系统**：高压电缆护套交叉互联（crossbonding）配置下的暂态过电压分析，涉及相间模态耦合和护套环流。
4. **混合架空线-电缆线路**：城网中架空线过渡到地下电缆的混合线路，行波在阻抗不连续点的反射与折射。
5. **雷电冲击与开关操作**：截断电荷（trapped charge）放电、操作过电压、雷电波传播等暂态过程的精确模拟。

**核心挑战**：电缆的多层同轴结构导致（1）阻抗矩阵在宽频带上呈现强烈的频率依赖性；（2）高维多导体系统（96导体以上）的向量拟合数值不稳定；（3）直流到雷电冲击的宽频带（0.001 Hz–1 MHz）覆盖需求；（4）螺线管效应（三芯铠装电缆的3D螺旋结构）和铠装层涡流效应难以精确建模。

## 核心建模方法

### 方法一：传输线理论 + ULM（通用线路模型）

**原理**：基于telegrapher方程（1）–（3b），通过模态分解将多导体系统解耦。$\mathbf{YZ}$ 矩阵由频率相关的特征向量矩阵 $\mathbf{T}_I$ 对角化：

$$
\mathbf{YZ} = \mathbf{T}_I \,\text{diag}(\gamma_1^2, \gamma_2^2, \cdots, \gamma_n^2)\, \mathbf{T}_I^{-1} \quad (7)
$$

其中 $\gamma_1^2, \gamma_2^2, \cdots, \gamma_n^2$ 为 $\mathbf{YZ}$ 的特征值。传播函数矩阵 $\mathbf{H}$ 可表示为：

$$
\mathbf{H} = \mathbf{T}_I \,\text{diag}(e^{-\gamma_1 l}, e^{-\gamma_2 l}, \cdots, e^{-\gamma_n l})\, \mathbf{T}_I^{-1} \quad (8)
$$

ULM模型将 $\mathbf{H}$ 和 $\mathbf{Y}_C$ 拟合为低阶延迟有理函数（9）和（10）：

$$
\mathbf{H} \approx \sum_{g=1}^{N_g} \frac{\mathbf{G}_g}{s - p_g} e^{-j\omega\tau_g} \quad (9)
$$

$$
\mathbf{Y}_C \approx \mathbf{D} + \sum_{i=1}^{N_Y} \frac{\mathbf{R}_{Y,i}}{s - a_i} \quad (10)
$$

**特点**：
- 适用于任意长度的电缆（短电缆到长距离海底电缆）
- 频率相关参数通过向量拟合（vector-fitting）实现
- 递归卷积（recursive-convolution）进行时域计算
- 对于高维多导体系统（>50导体）可能出现数值不稳定

**适用场景**：通用EMT仿真，特别是长距离电缆、HVDC海底电缆、混合架空线-电缆线路。

**局限性**：对于极短电缆（<100 m）和高维多芯电缆系统，大残差/极点比（residue/pole ratio）可能导致时域仿真不稳定。

### 方法二：频变电缆模型（FDCM）

**原理**：FDCM（Frequency-Dependent Cable Model）通过将传播函数 $\mathbf{H}$ 分解为分组模态贡献（grouped modal contributions），在相域直接拟合传播函数，而非模态传播函数。模态贡献组是频率的平滑函数，避免了传统ULM中不同模态延迟混合导致的拟合问题：

$$
\mathbf{H}_{\text{grouped}} = \mathbf{T}_{\text{group}} \,\text{diag}(H_{g1}, H_{g2}, \cdots)\, \mathbf{T}_{\text{group}}^{-1} \quad (11)
$$

其中 $H_{gk}$ 为第 $k$ 个模态组的传播函数，在相域直接进行有理逼近。

**特点**：
- 通过模态分组降低残差/极点比，改善数值稳定性
- 适用于特征值可合并和平滑的电缆系统
- 对架空线效果有限（特征值特性不同）
- 需要确定最优的模态分组策略

**适用场景**：多芯电缆、特征值重复或相似的系统（如同类型电缆并联）。

**局限性**：不适用于所有架空线配置，模态分组策略缺乏通用性准则。

### 方法三：分频段拟合 + 直流校正（FDM/DC）

**原理**：Cervantes 等（2020）提出的两阶段拟合方法。第一阶段在高频带进行拟合（排除接近DC的频率样本），第二阶段为被排除的低频样本寻找校正函数：

$$
\mathbf{H}(s) \approx \mathbf{H}_{\text{HF}}(s) + \mathbf{H}_{\text{LF,corr}}(s) \quad (12)
$$

其中 $\mathbf{H}_{\text{HF}}(s)$ 为高频主模型（1 Hz–1 MHz，阶数20–50），$\mathbf{H}_{\text{LF,corr}}(s)$ 为低频校正项（低阶有理函数，阶数2–4）。约束线性最小二乘法控制残差/极点比 < 10³。

**特点**：
- 精确捕获直流响应，避免传统ULM在DC拟合不良导致的不正确稳态解
- 显著降低残差/极点比，改善时域数值稳定性
- 宽频覆盖范围 0.001 Hz – 1 MHz
- 适用于HVDC输电线路的EMT仿真

**适用场景**：HVDC海底电缆、直流输电线路、需要精确DC响应的仿真。

**局限性**：需要额外的优化步骤来减少高频误差；对于交流系统，DC校正的必要性较低。

### 方法四：宽频自适应模式分组（Advanced Wideband）

**原理**：Ramirez 等（2024）提出三项改进：

1. **最优时延计算**：基于最小相位基础寻找时延，使模态传播函数尽可能接近最小相位函数：

$$
H_{m,i} = e^{-(\alpha_i + j\beta_{\min,i})l} \cdot e^{-j\omega\tau_i} \quad (13)
$$

2. **自适应模态分组**：基于时延接近度的简单有效分组策略，大幅降低大残差/极点比：

$$
\text{Group}_k = \{i \mid |\tau_i - \tau_{\text{group},k}| < \epsilon\} \quad (14)
$$

3. **快速衰减模式截断**：当模态幅度低于阈值时限制最大拟合频率：

$$
|H(j\omega)| < 10^{-3} \implies \omega_{\text{max}} = \omega_{\text{threshold}} \quad (15)
$$

**量化结果**（Ramirez 2024，96导体电缆系统）：
- 传播模式分组数从36组降至8组（>75% 压缩率）
- 双回架空线从10组降至4组
- 快速衰减模式截断抑制高频相位振荡（>90% 振荡抑制）
- 矢量拟合容差 0.5%，RMS拟合误差 < 0.1%
- 在现有ULM失败的案例中仍能稳定运行

**适用场景**：超大导体数量电缆系统（96导体以上）、现有ULM数值不稳定的场景。

**局限性**：分组策略需要针对具体电缆结构调参；对于模态速度差异小的系统效果有限。

### 方法五：测量融合 coaxial 模态模型

**原理**：Gustavsen（2023）提出将实测 coaxial 模态传播特性与多导体传输线模型融合的方法。对于单芯电缆，coaxial 模态特征为：

$$
z_{\text{coax}}(\omega) = R(\omega) + j\omega L_{\text{coax}}(\omega) \quad (16)
$$

$$
y_{\text{coax}}(\omega) = G_{\text{dielectric}} + j\omega C_{\text{coax}}(\omega) \quad (17)
$$

由此得到 coaxial 传播函数和特征导纳：

$$
h_{\text{coax}} = e^{-\sqrt{y_{\text{coax}} z_{\text{coax}}}\,l} \quad (18)
$$

$$
y_{C,\text{coax}} = \sqrt{\frac{y_{\text{coax}}}{z_{\text{coax}}}} \quad (19)
$$

通过低通/高通滤波器（11a）和（11b）在高频段融合测量数据与计算模型：

$$
\tilde{\mathbf{H}} = \mathbf{H}_{\text{calc}} \cdot F_{\text{LP}}(\omega) + \mathbf{H}_{\text{coax}} \cdot F_{\text{HP}}(\omega) \quad (11a)
$$

$$
\tilde{\mathbf{Y}}_C = \mathbf{Y}_{C,\text{calc}} \cdot F_{\text{LP}}(\omega) + \mathbf{Y}_{C,\text{coax}} \cdot F_{\text{HP}}(\omega) \quad (11b)
$$

**特点**：
- 在高频段（>100 kHz）利用实测数据修正绞线效应、绝缘层损耗和半导体层损耗
- 在低频段保留经典几何计算模型的准确性
- 滤波器截止频率 $\omega_0$ 可选择在中间频率，确保平滑过渡
- 适用于护套单端接地或交叉互联的电缆系统

**量化结果**（Gustavsen 2023）：
- 高频同轴模态衰减修正：绞线效应+半导电层损耗在1 MHz处提供 40–60% 增量修正
- 实测融合截止频率 500 kHz，高于此频率时传统几何模型误差显著
- 同轴模态时延精度：实测值 ±5%（vs 纯解析计算的 10–20% 误差）
- 阻抗计算误差 < 2%（MoM-SO方法，考虑邻近效应和螺线管效应）

**适用场景**：需要极高频率精度的变压器绕组电压应力分析、VFT（极快暂态）仿真。

**局限性**：需要电缆端部可访问的S参数测量（on-drum测量）；修正系数 $\delta_{sk}, \delta_{sc}$ 的通用性在不同电缆截面/材料下验证不足。

### 方法六：导纳矩阵幂等分解（Idempotent Decomposition）

**原理**：Camara 等（2023）提出基于节点导纳矩阵 $\mathbf{Y}_n$ 幂等分解的电缆建模方法。节点导纳矩阵在频域表征终端电压与电流关系：

$$
\mathbf{Y}_n(s) \approx \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D} \quad (20)
$$

其中 $p_m$ 为公共极点（实数或复共轭），$\mathbf{R}_m$ 为留数矩阵，$\mathbf{D}$ 为 $\mathbf{Y}_n$ 在无限频率处的实部。

幂等分解将 $\mathbf{Y}_n$ 分解为幂等矩阵之和（$\mathbf{E}_i^2 = \mathbf{E}_i$）：

$$
\mathbf{Y}_n = \sum_{i=1}^{k} \lambda_i \mathbf{E}_i \quad (21)
$$

对幂等矩阵而非节点导纳矩阵本身进行有理拟合，克服了最小特征值在低频段可观测性差的问题。

**特点**：
- 与特征法（MoC）不同，产生完全耦合的导纳矩阵
- 适用于短电缆和长电缆场景（无长度约束）
- 保留频率相关参数
- 无需小时间步长

**适用场景**：短电缆系统（<100 m）、需要避免小时间步长的实时仿真。

**局限性**：幂等分解的计算复杂度较高；对于频率相关变换矩阵，需要逐频率计算。

### 方法七：海底埋设电缆 quasi-TEM 模型

**原理**：Camara 等（2024）针对海底埋设电缆（两层均为损耗介质）提出 quasi-TEM 近似的全波公式。传统EMT程序假设一个介质为无损，不适用于海底电缆。quasi-TEM 近似下，外部介质阻抗和导纳表达式为：

$$
Z_{\text{ext}} = \frac{\gamma_{\text{seabed}}}{2\pi\sigma_{\text{seabed}}} \cdot K_0(\gamma_{\text{seabed}} r) \quad (22)
$$

$$
Y_{\text{ext}} = j\omega \frac{2\pi\epsilon_{\text{seabed}}}{\ln(r_{\text{outer}}/r_{\text{inner}})} \quad (23)
$$

其中 $\gamma_{\text{seabed}} = \sqrt{j\omega\mu_{\text{seabed}}/(\sigma_{\text{seabed}} + j\omega\epsilon_{\text{seabed}})}$ 为海床传播常数。

时间域实现采用两种方法：
1. **基于ULM的MoC方法**：利用EMT程序中Universal Line Model的实现结构
2. **Folded Line Equivalent (FLE) 方法**：对电缆节点导纳矩阵进行有理拟合

两种方法的结果与数值拉普拉斯变换（NLT）验证结果高度一致。

**适用场景**：海上风电场海底电缆（HVDC/HVAC）、埋设深度>1 m的海底电缆系统。

**局限性**：quasi-TEM 近似在极高频率下精度下降；有限元方法（FEM）对绞线效应的建模更精确但计算量大。

## 形式化表达

### 电缆参数计算的核心公式

**同轴导体系统的串联阻抗**（考虑集肤效应）：

$$
z_{ij}(\omega) = z_{\text{earth}}(\omega) + \delta_{ij} \cdot z_{\text{cond},i}(\omega) \quad (24)
$$

其中 $z_{\text{earth}}(\omega)$ 为大地返回阻抗（参见 [[earth-return-impedance]]），$z_{\text{cond},i}(\omega)$ 为导体 $i$ 的内部阻抗（Bessel函数描述集肤效应）：

$$
z_{\text{cond},i}(\omega) = \frac{j\omega\mu_0}{2\pi a_i} \cdot \frac{J_0(u_i a_i)}{J_1(u_i a_i)} \quad (25)
$$

其中 $u_i = \sqrt{j\omega\mu_0/(\rho_i + j\omega\mu_0\mu_{r,i})}$，$J_0$ 和 $J_1$ 为零阶和一阶Bessel函数，$a_i$ 为导体半径，$\rho_i$ 为导体电阻率。

**并联导纳**（考虑绝缘层电容和介质损耗）：

$$
y_{ij}(\omega) = j\omega c_{ij} + g_{ij}(\omega) \quad (26)
$$

其中 $c_{ij}$ 为几何电容，$g_{ij}(\omega)$ 为介质电导（与绝缘层损耗角正切相关）。

**大地返回导纳**（位移电流效应）：

Magalhães 等（2021）指出，传统方法忽略大地返回导纳（位移电流），但在短段交叉互联电缆系统中，大地返回导纳对暂态过电压有显著影响。包含大地返回导纳后，阻尼增加，传统方法可能导致保守估计。

### 螺线管效应（Solenoid Effect）公式

Chrysochos 等（2023）针对三芯铠装海底电缆，通过3D FEM建模发现螺线管效应对串联阻抗有显著影响。螺线管效应源于铠装层螺旋绞合产生的纵向磁场分量：

$$
Z_{\text{solenoid}} = j\omega L_{\text{solenoid}} = j\omega \frac{\mu_0 N^2 A}{l_{\text{lay}}} \cdot f(\theta_{\text{armor}}, \mu_r) \quad (27)
$$

其中 $N$ 为绞合匝数，$A$ 为截面积，$l_{\text{lay}}$ 为绞合节距，$\theta_{\text{armor}}$ 为铠装层绞合角，$\mu_r$ 为磁导率。

**量化影响**：对于磁性铠装（magnetic armor）三芯电缆，螺线管效应使功率频率下的串联阻抗增加 5–15%，对模态传播特性产生可测量的影响。

### 全通函数时延估计

Loaiza-Elejalde 等（2026）提出基于全通滤波器迭代的因果性强制方法，用于ULM传播函数时延估计：

$$
H_{m,i} = e^{-(\alpha_i + j\beta_{\min,i})l} \cdot e^{-j\omega\tau_i} \quad (28)
$$

迭代过程确保 $v < c$（传播速度小于光速），消除非物理前驱波。迭代收敛容差 $10^{-8}$（NLT参考值），最大迭代 20–50 次。

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
  <text x="450" y="22" fill="#1a1a2e" font-size="14" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">电缆EMT建模方法体系架构</text>

  <!-- Layer 1: Input (Blue) -->
  <rect x="340" y="40" width="220" height="36" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="450" y="58" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">电缆几何参数</text>
  <text x="450" y="72" fill="#4b6b8f" font-size="9" text-anchor="middle">Z(ω), Y(ω) → H, Y<sub>C</sub></text>

  <!-- Arrow down -->
  <line x1="450" y1="76" x2="450" y2="96" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 2: Core Modeling Methods (Green - 7 methods in 2 rows) -->
  <!-- Row 1: Methods 1-4 -->
  <rect x="30" y="96" width="200" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="130" y="111" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">ULM (通用线路模型)</text>
  <text x="130" y="126" fill="#3a7a5a" font-size="9" text-anchor="middle">向量拟合 + 递归卷积</text>

  <rect x="240" y="96" width="200" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="340" y="111" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">FDCM (频变电缆模型)</text>
  <text x="340" y="126" fill="#3a7a5a" font-size="9" text-anchor="middle">模态分组 + 相域拟合</text>

  <rect x="450" y="96" width="200" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="550" y="111" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">FDM/DC (分频段+DC校正)</text>
  <text x="550" y="126" fill="#3a7a5a" font-size="9" text-anchor="middle">两阶段拟合 + 低频校正</text>

  <rect x="660" y="96" width="210" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="765" y="111" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">自适应模式分组</text>
  <text x="765" y="126" fill="#3a7a5a" font-size="9" text-anchor="middle">时延分组 + 衰减截断</text>

  <!-- Row 2: Methods 5-7 -->
  <rect x="30" y="142" width="200" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="130" y="157" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">测量融合 Coaxial 模态</text>
  <text x="130" y="172" fill="#3a7a5a" font-size="9" text-anchor="middle">实测S参数 + 高频修正</text>

  <rect x="240" y="142" width="200" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="340" y="157" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">幂等分解导纳矩阵</text>
  <text x="340" y="172" fill="#3a7a5a" font-size="9" text-anchor="middle">E<sub>i</sub><sup>2</sup> = E<sub>i</sub> 分解</text>

  <rect x="450" y="142" width="200" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="550" y="157" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">海底 quasi-TEM 模型</text>
  <text x="550" y="172" fill="#3a7a5a" font-size="9" text-anchor="middle">双层损耗介质 + MoC/FLE</text>

  <rect x="660" y="142" width="210" height="34" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="765" y="157" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">全通函数时延估计</text>
  <text x="765" y="172" fill="#3a7a5a" font-size="9" text-anchor="middle">因果性强制 + 最小相位</text>

  <!-- Arrows from all methods to output -->
  <line x1="130" y1="176" x2="130" y2="210" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="340" y1="176" x2="340" y2="210" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="550" y1="176" x2="550" y2="210" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="765" y1="176" x2="765" y2="210" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>

  <!-- Layer 3: Output (Purple) -->
  <rect x="300" y="210" width="300" height="36" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="450" y="225" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">时域电缆模型</text>
  <text x="450" y="240" fill="#6b21a8" font-size="9" text-anchor="middle">ULM / FLE / NLT 等效电路</text>

  <!-- Arrow from methods to output -->
  <line x1="450" y1="246" x2="450" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 4: Applications (Amber) -->
  <rect x="30" y="270" width="250" height="34" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="155" y="285" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle">HVDC海底电缆</text>
  <text x="155" y="300" fill="#a16207" font-size="9" text-anchor="middle">海上风电场 / 长距离输电</text>

  <rect x="290" y="270" width="250" height="34" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="415" y="285" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle">VFT / 变压器绕组应力</text>
  <text x="415" y="300" fill="#a16207" font-size="9" text-anchor="middle">陡波前 / 雷电冲击</text>

  <rect x="570" y="270" width="250" height="34" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="695" y="285" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle">交叉互联系统</text>
  <text x="695" y="300" fill="#a16207" font-size="9" text-anchor="middle">护套环流 / 相间耦合</text>

  <!-- Arrows to applications -->
  <line x1="450" y1="306" x2="155" y2="306" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="450" y1="306" x2="415" y2="306" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="450" y1="306" x2="695" y2="306" stroke="#333" stroke-width="1" stroke-dasharray="4,3"/>

  <!-- Legend -->
  <text x="30" y="340" fill="#333" font-size="11" font-weight="bold">图例</text>
  <rect x="30" y="348" width="14" height="10" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="50" y="357" fill="#555" font-size="9">输入/源参数</text>
  <rect x="150" y="348" width="14" height="10" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="170" y="357" fill="#555" font-size="9">建模方法</text>
  <rect x="270" y="348" width="14" height="10" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="290" y="357" fill="#555" font-size="9">等效模型</text>
  <rect x="390" y="348" width="14" height="10" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="410" y="357" fill="#555" font-size="9">应用场景</text>
  <line x1="530" y1="353" x2="546" y2="353" stroke="#333" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="552" y="357" fill="#555" font-size="9">数据流</text>

  <!-- Caption -->
  <text x="450" y="395" fill="#888" font-size="10" text-anchor="middle">图1 · 电缆EMT建模方法体系架构（七种核心方法 → 时域等效模型 → 应用场景）</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 电缆EMT建模方法体系架构（七种核心方法 → 时域等效模型 → 应用场景）</p>


## 关键技术挑战

### 1. 宽频带数值稳定性

电缆模型需要在 0.001 Hz – 1 MHz 的超宽频带上保持有理拟合的数值稳定性。大残差/极点比（>10³）和被动性违反（passivity violation）是主要问题。Ramirez 等（2024）和 Gustavsen 等（2023）均指出，对于高维多导体系统，数值不稳定是ULM应用的主要障碍。

### 2. 3D螺旋效应建模

三芯铠装海底电缆的绞线效应（ twisting）和螺线管效应（solenoid effect）是三维电磁问题。2.5D FEM方法计算速度快但忽略螺线管效应，3D FEM方法更精确但计算量大。Chrysochos 等（2023）表明，对于磁性铠装电缆，螺线管效应对阻抗的影响不可忽略（5–15%阻抗增加）。

### 3. 双层损耗介质

海底埋设电缆的电缆绝缘层和海床土壤均为损耗介质，传统EMT程序假设一个介质为无损的算法不适用。Camara 等（2024）通过quasi-TEM近似解决了这一问题，但quasi-TEM在极高频率下精度下降。

### 4. 交叉互联接地系统

高压电缆护套交叉互联（crossbonding）配置下，护套环流和相间耦合使建模复杂度大幅增加。短段交叉互联（<500 m）中，大地返回导纳的影响显著。

### 5. 测量数据融合

Gustavsen（2023）提出的测量融合方法需要电缆端部的S参数测量，这对于已敷设的电缆不可行。对于设计阶段的电缆，只能依赖几何计算模型，无法利用实测数据修正高频损耗。

## 量化性能边界

**分频段拟合 + 直流校正（FDM/DC, Cervantes 2020）**：
- 高频主模型在 1 Hz–1 MHz 拟合（阶数20–50），低频校正项使用低阶有理函数（阶数2–4）
- 约束线性最小二乘法控制残差/极点比 < 10³
- 宽频覆盖范围 0.001 Hz – 1 MHz
- 适用：HVDC输电线路，需要精确DC响应的仿真

**宽频自适应模式分组（Ramirez 2024）**：
- 96导体电缆系统：传播模式分组数从36组降至8组（>75% 压缩率）
- 快速衰减模式截断阈值 $|H(j\omega)| < 10^{-3}$，有效抑制高频相位振荡（>90% 振荡抑制）
- 矢量拟合容差 0.5%，RMS拟合误差 < 0.1%
- 适用：超大导体数量电缆系统，现有ULM数值不稳定的场景

**测量融合coaxial模态模型（Gustavsen 2023）**：
- 高频同轴模态衰减修正：绞线效应+半导电层损耗在1 MHz处提供 40–60% 增量修正
- 实测融合截止频率 500 kHz，高于此频率时传统几何模型误差显著
- 同轴模态时延精度：实测值 ±5%（vs 纯解析计算的 10–20% 误差）
- 阻抗计算误差 < 2%（MoM-SO方法）
- 适用：变压器绕组电压应力分析、VFT仿真

**螺线管效应3D FEM建模（Chrysochos 2023）**：
- 磁性铠装三芯电缆：螺线管效应使功率频率串联阻抗增加 5–15%
- 对模态传播特性产生可测量影响
- 适用：海上风电场三芯 submarine 电缆设计

**海底埋设电缆quasi-TEM模型（Camara 2024）**：
- 解决双层损耗介质问题，MoC和FLE两种时域实现均与NLT验证结果高度一致
- 适用：海上风电场海底电缆（HVDC/HVAC）

**导纳矩阵幂等分解（Camara 2023）**：
- 适用于短电缆和长电缆场景，无需小时间步长
- 克服最小特征值在低频段可观测性差的问题
- 适用：短电缆系统（<100 m）、实时仿真

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|------|
| 长距离HVDC海底电缆 | ULM + FDM/DC | 宽频带覆盖+精确DC响应 |
| 超大导体数量电缆（>50导体） | ULM + 自适应模式分组 | 降低残差/极点比，改善稳定性 |
| 变压器绕组VFT分析 | 测量融合coaxial模态 | 高频精度最高（实测数据修正） |
| 短电缆系统（<100 m） | 导纳矩阵幂等分解 / FLE | 避免小时间步长，无长度约束 |
| 三芯铠装海底电缆 | 3D FEM阻抗计算 + ULM | 考虑螺线管效应和3D螺旋效应 |
| 交叉互联高压电缆 | ULM + 大地返回导纳 | 准确模拟护套环流和相间耦合 |
| 城网混合线路（架空线+电缆） | ULM / FDCM | 通用EMT仿真，兼容性良好 |
| 实时仿真（HIL） | FLE / 幂等分解 | 无需小时间步长，计算效率高 |

## 相关方法

- [[universal-line-model]] - 通用线路模型，电缆EMT仿真的核心框架
- [[frequency-dependent-line-model]] - 频变线路模型
- [[vector-fitting]] - 有理逼近算法，电缆模型拟合的核心工具
- [[passivity-enforcement]] - 无源性强制，确保电缆模型数值稳定
- [[modal-domain-decoupling]] - 模域解耦，多导体电缆分析的基础
- [[modal-transformation]] - 模态变换矩阵
- [[characteristic-method]] - 特征法，基于MoC的电缆模型实现
- [[folded-line-equivalent]] - 折叠线等效，导纳矩阵拟合方法
- [[underground-cable-modeling]] - 地下电缆建模综述
- [[earth-return-impedance]] - 大地返回阻抗，电缆参数计算的关键输入
- [[distributed-parameter-line]] - 分布参数线路模型
- [[recursive-convolution]] - 递归卷积，时域实现方法
- [[cross-bonded-cable]] - 交叉互联电缆模型

## 来源论文

- **Gustavsen 2023** — "Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics" (IEEE TPWRD) — 提出测量融合coaxial模态模型，解决高频阻尼不足问题
- **Ramirez 2024** — "Advanced Wideband Line/Cable Modeling for Transient Studies" — 三项改进：最优时延计算、自适应模态分组、快速衰减模式截断
- **Cervantes 2020** — "Partitioned Fitting and DC Correction in Transmission Line/Cable Models for Wideband EMT Studies" — 分频段拟合+直流校正（FDM/DC），解决ULM的DC拟合不良问题
- **Camara 2023** — "Admittance-based Modelling of Cables and Overhead Lines by Idempotent Decomposition" — 导纳矩阵幂等分解方法，适用于任意长度电缆
- **Camara 2024** — "Time-domain Modeling of a Subsea Buried Cable" — 海底埋设电缆quasi-TEM模型，解决双层损耗介质问题
- **Chrysochos 2023** — "Impact of Solenoid Effects on Series Impedance of Three-core Armoured Cables" — 三芯铠装电缆螺线管效应的3D FEM建模
- **Magalhães 2021** — "Earth Return Admittance Impact on Crossbonded Underground Cables" — 交叉互联电缆中大地返回导纳的影响
- **Loaiza-Elejalde 2026** — "Time-delay Estimation through All-pass Functions for ULM Line and Cable Models" — 基于全通滤波器的因果性强制时延估计
- **Meredith 1997** — "EMTP Modeling of Electromagnetic Transients in Multi-mode Coaxial Cables by Finite Sections" — 有限段方法建模同轴电缆电磁传播

## 来源论文

| 论文 | 年份 |
|------|------|
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on|EMTP Modeling Of Electromagnetic Transients - Power Delivery]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[parametric-study-of-transient-electromagnetic-fields|Parametric Study of Transient Electromagnetic Fields]] | 2011 |
| [[multi-fpga-digital-hardware-design-iet-gtd|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[high-performance-computing-engines-for-the-fpga-based-simulation-of-the-ulm|High performance computing engines for the FPGA-based simula]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[extension-of-vances-closed-form-approximation-to-calculate-the-ground-admittance|Extension of Vance]] | 2021 |
| [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable|Modal propagation characteristics and transient analysis of ]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[algorithm-for-fast-calculating-the-energization-overvoltages-along-a-power-cable|Algorithm for fast calculating the energization overvoltages]] | 2022 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va|Frequency and transient responses of A 275 kV pressure oil-f]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |

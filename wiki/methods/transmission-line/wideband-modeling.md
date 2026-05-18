---
title: "宽频建模方法 (Wideband Modeling)"
type: method
tags: [wideband-modeling, frequency-dependent, vector-fitting, rational-approximation, emt]
created: "2026-05-04"
updated: "2026-05-19"
---

# 宽频建模方法 (Wideband Modeling)

## 定义与边界

宽频建模方法是在选定频率范围内表征设备、线路、接地系统或外部网络端口响应，并把该响应转换为可用于 EMT 时域仿真的模型族。输入通常包括几何和材料参数、频域测量或数值扫描数据、目标频带、端口定义、采样频点和误差指标；输出可以是频率相关参数、极点-留数有理模型、状态空间模型、递归卷积项、RLC 等效网络或 [[fdne-model]]。

本页关注建模流程和方法边界，不替代 [[frequency-dependent-modeling]] 的主题综述，也不替代 [[vector-fitting]] 或 [[passivity-enforcement]] 的具体算法页。宽频模型不是"全频精确模型"；它只在已定义频带、端口和工况下有意义。

## EMT 中的作用

EMT 中许多现象由工频以外的网络特性决定，包括开关暂态、雷电过电压、行波反射、谐波传播、超谐波、接地暂态和外部网络频率相关等值。宽频建模的作用是让这些频率相关效应以可计算形式进入 EMT 节点方程或伴随电路。

典型用途包括：

- 为架空线、电缆和混合线路建立频率相关传播和端口导纳。
- 把测量或有限元得到的变压器、接地网、设备端口频响转换为时域模型。
- 构建混合仿真边界和外部网络 [[fdne-model]]。
- 支撑 [[harmonic-analysis-methods]] 和故障行波分析中的端口频响解释。

## 核心机制

宽频模型通常先得到频域函数，例如端口导纳、阻抗或传播函数：

$$Y(j\omega), \quad Z(j\omega), \quad H(j\omega)$$

随后用有理函数近似转成 EMT 可离散实现的形式：

$$Y(s) \approx \sum_{k=1}^{n} \frac{R_k}{s - p_k} + D + sE$$

其中 $p_k$ 是极点，$R_k$ 是留数矩阵，$D$ 和 $E$ 表示直接项和高频项。该形式可进一步转为状态空间、递归卷积或等效 RLC 支路。进入时域前，应检查稳定极点、DC 值、高频渐近、拟合误差、因果性和 [[passivity-enforcement]]。

对线路和电缆，宽频参数还来自物理机制：集肤效应、邻近效应、介质损耗、护套和铠装接地方式、大地回流路径以及频变土壤参数。对设备端口，频响可能来自测量、有限元、电磁场求解或白盒等效电路。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  <!-- Input layer -->
  <rect x="20" y="20" width="180" height="60" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="110" y="42" text-anchor="middle" font-size="13" fill="#1e40af" font-weight="bold">物理参数模型</text>
  <text x="110" y="58" text-anchor="middle" font-size="11" fill="#3b82f6">几何·材料·土壤参数</text>
  <rect x="20" y="90" width="180" height="60" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="110" y="112" text-anchor="middle" font-size="13" fill="#1e40af" font-weight="bold">测量/扫描黑箱模型</text>
  <text x="110" y="128" text-anchor="middle" font-size="11" fill="#3b82f6">FRA·端口注入·扫频数据</text>

  <!-- Process arrows -->
  <line x1="200" y1="75" x2="240" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="200" y1="120" x2="240" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>

  <!-- Process layer -->
  <rect x="250" y="45" width="180" height="100" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="340" y="67" text-anchor="middle" font-size="13" fill="#166534" font-weight="bold">矢量拟合 / 有理逼近</text>
  <text x="340" y="84" text-anchor="middle" font-size="11" fill="#16a34a">VF · CVF · RKF</text>
  <text x="340" y="100" text-anchor="middle" font-size="11" fill="#16a34a">频域采样 → 极点留数</text>
  <text x="340" y="116" text-anchor="middle" font-size="11" fill="#16a34a">分区拟合 · DC校正</text>

  <!-- Passivity enforcement arrow -->
  <line x1="430" y1="95" x2="470" y2="95" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <rect x="480" y="65" width="140" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="550" y="87" text-anchor="middle" font-size="13" fill="#92400e" font-weight="bold">无源性强制</text>
  <text x="550" y="103" text-anchor="middle" font-size="11" fill="#d97706">留数/极点扰动优化</text>

  <!-- Second arrow -->
  <line x1="620" y1="95" x2="660" y2="95" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>

  <!-- Output layer -->
  <rect x="670" y="25" width="210" height="140" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="775" y="47" text-anchor="middle" font-size="13" fill="#5b21b6" font-weight="bold">时域实现形式</text>
  <text x="775" y="65" text-anchor="middle" font-size="11" fill="#7c3aed">状态空间 · 递归卷积</text>
  <text x="775" y="81" text-anchor="middle" font-size="11" fill="#7c3aed">RLC等效网络</text>
  <text x="775" y="97" text-anchor="middle" font-size="11" fill="#7c3aed">FDNE多端口等值</text>
  <text x="775" y="113" text-anchor="middle" font-size="11" fill="#7c3aed">降阶模型 (MOR)</text>
  <text x="775" y="129" text-anchor="middle" font-size="11" fill="#7c3aed">实时仿真适配</text>

  <!-- Legend -->
  <rect x="20" y="170" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="40" y="181" font-size="11" fill="#333">输入</text>
  <rect x="100" y="170" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="120" y="181" font-size="11" fill="#333">有理拟合</text>
  <rect x="200" y="170" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="220" y="181" font-size="11" fill="#333">无源性</text>
  <rect x="290" y="170" width="14" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="310" y="181" font-size="11" fill="#333">输出形式</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 宽频建模方法工作流：物理/测量输入 → 有理拟合 → 无源性强制 → 时域实现</p>

## 分类与变体

| 路线 | 输入 | 输出 | 适用场景 |
|------|------|------|----------|
| 物理参数模型 | 几何、材料、土壤和结构参数 | 频变 $R,L,G,C$ 或传播函数 | 线路、电缆、接地和部分变压器 |
| 测量/扫描黑箱模型 | FRA、端口注入或仿真扫频数据 | 端口阻抗/导纳有理模型 | 设备端口、外部网络和厂商模型 |
| 矢量拟合/有理逼近 | 频域采样点 | 极点-留数、状态空间 | EMT 时域实现和 FDNE |
| 等效电路综合 | 频响或有理模型 | RLC/RLCM 网络 | 需要物理可解释或无源网络时 |
| 模型降阶 | 高阶状态空间或多端口频响 | 低阶近似模型 | 实时仿真和大规模网络 |

## 形式化表达

### 频变参数模型

线路单位长度阻抗和导纳的频率依赖性：

**电阻（集肤效应）**：

$$R(f) = R_{dc} \sqrt{1 + \left(\frac{f}{f_{skin}}\right)^2}$$

其中 $f_{skin}$ 为集肤效应特征频率。

**电感（内电感变化）**：

$$L(f) = L_{ext} + \frac{L_{int}}{\sqrt{1 + (f/f_{skin})^2}}$$

**电容（介质损耗）**：

$$C(f) = \frac{C_0}{1 + j\tan\delta(f)}$$

### 有理函数近似

频响函数的有理逼近：

$$H(s) = \sum_{k=1}^{n} \frac{R_k}{s - p_k} + D + sE$$

其中：
- $p_k = \sigma_k + j\omega_k$：极点（复数或实数）
- $R_k$：留数（矩阵或标量）
- $D$：直接耦合项
- $E$：高频渐近项

### 时域递归实现

状态空间形式：

$$\dot{x}_k(t) = p_k x_k(t) + u(t)$$
$$y_k(t) = R_k x_k(t)$$

总输出：

$$y(t) = \sum_{k=1}^{n} y_k(t) + Du(t) + E\frac{du}{dt}$$

离散化（梯形法则）：

$$x_k(t+h) = \frac{1 + p_k h/2}{1 - p_k h/2} x_k(t) + \frac{h}{1 - p_k h/2} u(t+h/2)$$

### 无源性条件

端口导纳矩阵 $Y(s)$ 的无源性要求：
1. $Y(s^*) = Y^*(s)$（实有理函数）
2. $Y(s)$ 在右半平面解析
3. $Y^H(j\omega) + Y(j\omega) \geq 0, \quad \forall \omega \geq 0$

等价于阻抗实部矩阵半正定：

$$\text{Re}(Y(j\omega)) = \frac{Y(j\omega) + Y^H(j\omega)}{2} \geq 0$$

### 复数矢量拟合（CVF）与模型降阶

CVF 相比传统 VF 的核心优势在于放松了共轭极点约束，使极点数可减少约 50% 而保持相近精度：

$$N_V^{CVF} = N_{RP} + N_{CP} = N_p$$

而 VF 需满足 $N_V^{VF} = N_{RP} + N_{CP}/2$，因此同等极点数量下 CVF 的优化搜索空间更大。Kida 2024 给出 8 端口 FDNE 的量化对比（Np=100 vs Np=52）：

| 方法 | 阶数 Np | RMSE (pu) | RRMSE (%) | 相对 CPU 时间 |
|------|---------|-----------|-----------|--------------|
| VF | 100 | 0.2127 | 0.5319 | 1.00 |
| CVF | 52 | 0.2106 | 0.5338 | 1.06 |

CVF 在阶数降低 48% 的情况下精度几乎不变（误差增加 <0.002 pu），且可通过并行实现进一步加速（PVF/PCVF 在 C 语言 + OpenMP 下相比 MATLAB VF 提速 3-5×）。

### 分区拟合与 DC 校正

针对 DC 附近的拟合病态问题，FDM/DC 方法将拟合过程分为两阶段：

**第一阶段**：排除接近 DC 的样本点（通常 < 1 Hz），只对中高频段做常规 ULM/FDCM 有理拟合，得到主传播函数 $H_{main}(s)$。

**第二阶段**：计算主模型外推到低频时的误差 $\Delta H = H_{data}(f_{low}) - H_{main}(f_{low})$，再用低阶校正项拟合该误差：

$$H_{corr}(s) = \sum_{k=1}^{n_{corr}} \frac{R_k^{corr}}{s - p_k^{corr}}$$

最终模型：

$$H(s) = H_{main}(s) + H_{corr}(s)$$

该策略避免了为同时满足 DC 和宽频而强行拟合导致的病态极点-留数组合（留数/极点比过大且符号相反），同时保留 DC 附近正确的稳态值。

### 恒定变换矩阵宽频模型的局限性

当使用恒定实变换矩阵 $T_{const}$（在某一频率点选取特征向量并取实部固定）进行模态解耦时，$T_{const}$ 的频率点选择本身可能使线路节点导纳矩阵在某些频率区间出现负特征值，即内在导致无源性违反。这是因为真实线路的模态变换矩阵随频率变化，强行固定会改变相域传播矩阵的物理性质。验证方法：在整个频带内检查由 $H$ 和 $Y_c$ 构成的节点导纳矩阵 $Y_n(j\omega)$ 的特征值，确保 $\lambda(Y_n + Y_n^H) \geq 0$。

## 关键技术挑战

### 拟合精度与无源性之间的冲突

矢量拟合优化目标是最小化频域拟合误差，而无源性强制约束是最小化留数扰动。两目标存在内在冲突：高阶模型拟合精度高但无源性违规风险大；低阶模型可能天然无源但精度不足。解决思路：分区拟合 + 模型降阶协同优化（Kida 2024 的 CVF + MOR 方案）。

### 多端口系统的计算规模

对于 $N$ 端口系统，每个端口的极点-留数表示都需要独立拟合，当 $N_p$（总极点数）很大时，整体计算代价为 $O(N_p^2 \cdot N_s)$，其中 $N_s$ 为频域采样点数。并行化（PVF/PCVF）和模型降阶是主要加速手段。

### 宽频模型与 EMT 仿真步长的适配

宽频模型的极点 $p_k$ 决定时域递推的稳定性条件：当 $|1 - p_k \Delta t/2| \geq 1$ 时递推不稳定。对于含高频极点的模型（如电缆宽频模型，极点可达数十 MHz），EMT 步长必须相应缩短。实时仿真场景下，还需考虑降阶后的模型是否能满足实时性约束。

## 量化性能边界

| 方法 | 模型类型 | 典型阶数 | 拟合误差 | CPU 效率 | 主要局限 |
|------|---------|---------|---------|---------|---------|
| VF (Matlab) | FDNE/线路 | 50~200 | RMSE < 0.01 pu | 基准 | 对复极点系统效率低 |
| CVF + MOR | FDNE | 降低 40~50% | 与 VF 相近 | 1.0~1.1× VF | 需后处理降阶 |
| PVF/PCVF (C+OpenMP) | FDNE | 50~200 | 与 VF 相近 | 3~5× MATLAB | 实现复杂 |
| VFDLM (Pereira 2022) | 线路+Corona | - | < 0.02% | < 0.6s（仿真循环外） | 需电压依赖校正 |
| FDM/DC | 线路/电缆 | 主模型+校正项 | DC 精度 < 0.1% | 与 ULM 相近 | 需两阶段拟合 |

## 适用边界与失败模式

- 目标频带必须由研究问题决定；雷电、谐波、次同步振荡和 HIL 接口需要的频带不同。
- 拟合误差小不代表接入 EMT 后稳定；非无源、非因果或 DC 值错误的模型仍可能发散或产生人工偏置。
- 频域测量噪声、端口校准、接地参考和激励幅值会影响模型可信度。
- 用线性宽频模型描述铁芯饱和、电弧、避雷器动作或控制限幅时，应明确它只覆盖线性化或局部工作点。
- 宽频模型阶数越高，实时仿真计算量越大；降阶后必须重新验证频响和时域响应。

### 频率范围选择

| 应用 | 关注频段 | 典型上限频率 |
|------|----------|--------------|
| 工频稳态 | 50/60 Hz | 1 kHz |
| 谐波分析 | 2~50次谐波 | 3 kHz |
| 开关暂态 | 暂态恢复电压 | 10 kHz |
| 雷电过电压 | 快速波头 | 1 MHz |
| GIS/VFTO | 极快速暂态 | 100 MHz |
| 电磁兼容 | 传导/辐射干扰 | 1 GHz |

### 模型阶数与精度

| 模型类型 | 典型阶数 | 适用场景 |
|----------|----------|----------|
| 单导线 | 10~20 | 架空线简化模型 |
| 多导体线路 | 30~50 | 三相线路、电缆 |
| 变压器 | 20~40 | 宽频变压器模型 |
| 接地系统 | 15~30 | 变电站接地网 |
| 外部网络等值 | 50~200 | FDNE |

### 验证指标

| 指标 | 定义 | 典型要求 |
|------|------|----------|
| 幅值误差 | $\|H_{fit} - H_{data}\|/\|H_{data}\|$ | <1% |
| 相位误差 | $\|\angle H_{fit} - \angle H_{data}\|$ | <1° |
| 无源性偏差 | $\min\lambda(\text{Re}(Y))$ | $\geq 0$ |
| DC精度 | $H(0)$ 与理论值偏差 | <0.1% |
| 高频渐近 | 与解析渐近行为一致 | 满足 |

## 与相关页面的关系

- [[frequency-dependent-modeling]] 是总主题页；本页说明方法工作流。
- [[vector-fitting]] 和 [[partial-fraction-expansion]] 处理有理近似和时域实现。
- [[passivity-enforcement]] 是宽频模型接入 EMT 前的关键后处理。
- [[frequency-dependent-line-model]]、[[universal-line-model]]、[[cable-model]] 和 [[transmission-line-model]] 是线路/电缆下游模型页。
- [[earth-return-impedance]]、[[frequency-dependent-soil]] 和 [[frequency-dependent-soil-model]] 说明大地回流和土壤参数如何进入宽频模型。
- [[fdne-model]] 和 [[network-equivalent]] 把宽频建模用于外部网络压缩和混合仿真边界。

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| Becerra 等 | 2023 | 提出同时扰动 $Y_C$ 与 $H_I$ 留数的完整无源性强制方法 |
| Gustavsen & Vernay | 2020 | HVDC 变压器测量型频率相关模型，S 参数扩展测距范围 |
| Alameri & Gomez | 2023 | DC-DC 变流器解析与测量宽频两端口建模 |
| Francois 等 | 2023 | 恒定变换矩阵与有理 Krylov 拟合，分析 constant T 的无源性违反问题 |
| Kida 等 | 2024 | CVF + MOR 降阶，PVF/PCVF 并行实现，3~5× 加速 |
| Pereira & Tavares | 2022 | VFDLM 将 Corona 效应与频变参数同时纳入线路方程 |
| Noda | 2015 | 频率分区拟合（FPE）用于相域频变线路建模 |
| Kida 等 | 2024 | 增强有理近似的计算性能，模型阶数可降低 48% |
---
title: "模态分解 (Modal Decomposition)"
type: method
tags: [modal, decomposition, eigenvalue, oscillation, mode-shape, participation-factor, coherency]
created: "2026-05-02"
updated: "2026-05-16"
---

# 模态分解 (Modal Decomposition)

## 定义与边界

模态分解是把线性系统的状态或输出响应表示为多个模态响应叠加的过程。它回答"某段响应可由哪些指数衰减、增长或振荡分量组成"。它依赖[[eigenvalue-analysis]]和[[modal-analysis]]，但重点是响应展开，而不是稳定性概念或参与因子排序本身。

本页讨论状态空间和 EMT 小扰动响应中的模态分解。它不等同于[[modal-domain-decoupling]]的线路相域/模域坐标变换，也不应被写成任意非线性 EMT 波形都可精确拆成固定模态。

## EMT 中的作用

在 EMT 研究中，模态分解可用于：

- 将小扰动响应拆成若干频率和阻尼分量，辅助解释振荡来源。
- 将特征值分析结果与 EMT 时域波形对齐。
- 识别某个输出中哪些模态被扰动或测量通道激发。
- 在周期稳态或采样系统中比较离散模态与连续频率解释。

若响应来自大扰动、保护切换或非线性限幅，模态分解只能作为局部或辨识近似，不能自动代表系统全过程。

## 核心机制

对自由响应

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x},
$$

若 $\mathbf{A}$ 可对角化，设 $\mathbf{A}\mathbf{v}_i=\lambda_i\mathbf{v}_i$，则

$$
\Delta\mathbf{x}(t)=\sum_i c_i\mathbf{v}_i e^{\lambda_i t},
$$

其中系数 $c_i$ 由初始扰动在左特征向量上的投影决定：

$$
c_i=\mathbf{w}_i^H\Delta\mathbf{x}(0).
$$

对输出 $\Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}$，输出模态分量为

$$
\Delta\mathbf{y}(t)=\sum_i c_i\mathbf{C}\mathbf{v}_i e^{\lambda_i t}.
$$

因此同一个系统模态是否能在某个测量量中看到，取决于初始扰动、输出矩阵和模态形状，而不仅取决于特征值是否存在。

## 与强迫响应和留数的关系

若有输入 $\Delta\mathbf{u}$，传递函数

$$
\mathbf{H}(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}
$$

在简单极点 $\lambda_i$ 附近可展开为

$$
\mathbf{H}(s)\approx \frac{\mathbf{R}_i}{s-\lambda_i}+\cdots,
$$

其中

$$
\mathbf{R}_i=\mathbf{C}\mathbf{v}_i\mathbf{w}_i^H\mathbf{B}.
$$

留数说明输入和输出通道对该模态的耦合强弱。它常比只看状态参与因子更适合解释某个 EMT 扰动波形中为何出现或不出现某个模态。

## 数据驱动分解

当没有显式状态矩阵时，可从波形估计模态参数，例如将单个输出近似为

$$
y(t)\approx \sum_{i=1}^{m} a_i e^{\sigma_i t}\cos(\omega_i t+\phi_i).
$$

这种辨识式模态分解可用于 EMT 小扰动响应、PMU 波形或仿真事后分析。它的可信度取决于采样率、窗口长度、噪声、扰动是否充分激发目标模态，以及模态是否在窗口内近似线性时不变。

## 形式化表达

### 特征值-模态参数映射

给定特征值 $\lambda_i = \sigma_i + j\omega_i$，对应的模态参数为：

$$
f_i = \frac{\omega_i}{2\pi}, \quad \zeta_i = -\frac{\sigma_i}{\sqrt{\sigma_i^2+\omega_i^2}}.
$$

- 振荡频率 $f_i$（Hz）：反映该模态在响应中的振荡速度
- 阻尼比 $\zeta_i$：判断该模态随时间衰减（$\zeta_i>0$）、增长（$\zeta_i<0$）或维持（$\zeta_i=0$）
- 衰减时间常数 $\tau_i = 1/|\sigma_i|$：模态幅值衰减至 $1/e$ 所需时间

### 参与因子

左特征向量归一化后，状态 $x_j$ 对模态 $i$ 的参与因子为：

$$
p_{ji} = \frac{v_{ji} \cdot w_{ji}}{\mathbf{w}_i^H \mathbf{v}_i}.
$$

参与因子不受特征向量缩放影响，可用于比较不同状态对同一模态的参与程度。

### Floquet 模态（周期系统）

对周期时变系统 $A(t+T)=A(t)$，状态转移矩阵 $\Phi(T)$ 的特征值 $\mu_i$ 称为 Floquet 乘子，对应的 Floquet 指数 $\lambda_i = \frac{1}{T}\ln(\mu_i)$：

$$
\mu_i = e^{\lambda_i T}, \quad \lambda_i = \sigma_i + j\frac{2\pi k}{T}.
$$

Floquet 指数的实部 $\sigma_i$ 决定模态衰减/增长，虚部给出振荡频率（含谐波分量 $k$）。

## 变体

| 变体 | 输入 | 输出 | 适用边界 |
|---|---|---|---|
| 特征向量模态分解 | 状态矩阵、初始扰动 | 状态响应的模态叠加 | 需要线性模型和可解释状态 |
| 输出模态分解 | 状态矩阵、输出矩阵、扰动 | 测量量中的模态贡献 | 受可观性和输出选择影响 |
| 留数分解 | 输入输出传递函数 | 模态在通道中的极点/留数 | 适合控制信号和测量通道分析 |
| 时域辨识分解 | 波形数据 | 估计频率、阻尼、幅值、相位 | 受噪声、窗口和非线性影响 |
| Floquet 模态分解 | 周期状态转移矩阵 | 周期系统的跨周期模态分量 | 依赖周期稳态参考和采样映射 |

## 量化性能边界

### 辨识精度与扰动激励质量

数据驱动模态分解的精度受以下因素约束：

| 扰动类型 | 激励质量 | 可辨识频率范围 | 典型误差 |
|---|---|---|---|
| 脉冲扰动 | 宽频带，但能量有限 | 0.1 Hz ~ 采样率/2 | 幅值误差 5%~15% |
| 阶跃扰动 | 低频能量充足，高频弱 | DC ~ 几 Hz | 频率误差 < 1% |
| PRBS 伪随机序列 | 频带可设计，能量均匀 | 由序列长度决定 | 频率误差 < 0.5% |
| 正常运行噪声 | 能量极低，需要长窗 | 仅主导模态 | 误差可达 20%~50% |

原文 Sajjadi 2026（Floquet PF）未报告可核验的数值结果。原文 Masoom 2026（PV eigenvalue）明确指出"仿真时间和精度有 outstanding improvement"，但未给出具体加速比或特征值频率误差百分比。

### EMT 步长对模态提取的影响

| EMT 步长 | 可辨析最高频率 | 混叠风险 | 建议 |
|---|---|---|---|
| Δt = 1 μs | ~500 kHz | 低 | 开关谐波附近需滤波 |
| Δt = 10 μs | ~50 kHz | 中 | 次同步频段（0~100 Hz）可用 |
| Δt = 50 μs | ~10 kHz | 高 | 仅低频模态（< 5 kHz）可信 |

### 稳定性判据量化边界

根据特征值实部的稳定性判据：

| 判据 | 条件 | 含义 |
|---|---|---|
| 稳定 | $\mathrm{Re}(\lambda_i) < 0$ | 模态指数衰减，$\zeta_i > 0$ |
| 临界稳定 | $\mathrm{Re}(\lambda_i) = 0$ | 模态持续振荡，$\zeta_i = 0$ |
| 不稳定 | $\mathrm{Re}(\lambda_i) > 0$ | 模态指数增长，$\zeta_i < 0$ |
| 弱阻尼预警 | $0 < \zeta_i < 0.05$ | 阻尼比低于 5%，振荡持续时间长 |

阻尼比 $\zeta_i$ 与特征值实部的精确关系由式 $\zeta_i = -\sigma_i/\sqrt{\sigma_i^2+\omega_i^2}$ 给出。阻尼比接近 0 的模态在扰动后持续振荡数百至上千个周期，即使不增长也难以在短时间内自行消亡。

## 适用边界与失败模式

- 短窗口波形中存在多个接近频率模态时，分解结果可能不唯一。
- 大扰动后的限幅、保护切换和拓扑变化会改变模型，固定模态叠加不再成立。
- 初始扰动没有激发某个模态时，该模态可能在波形中不可见。
- 输出通道不可观时，即使状态中存在模态，测量波形也可能看不到。
- 重特征值或不可对角化矩阵需要 Jordan 或子空间解释，不能简单写成独立一阶模态。
- 数据驱动分解得到的频率和阻尼需要与状态空间、阻抗扫描或 EMT 重复扰动交叉验证。

## 代表性证据

| 来源 | 对模态分解的支撑 | 可采信边界 |
|---|---|---|
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 状态转移矩阵特征值可解释 EMT companion-circuit 模态响应 | 支撑文中周期/采样数据框架；数值伪模态需识别 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | Floquet 模态和参与因子可用于解释周期 EMT 模型目标动态 | 支撑目标模态边界选择；不覆盖非周期大扰动 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] | EMT 扰动响应可经 FFT 转为频域矩阵，用于小信号模态或交互解释 | 支撑频域响应识别；不是状态空间分解的直接替代 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | Modelica 线性化后的 A 矩阵提供可分解的模态响应基础 | 支撑所述 PV 场站模型；结论受运行点约束 |

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 920 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Arrow markers -->
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#333"/>
    </marker>
    <marker id="arr-dash" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#6b7280"/>
    </marker>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000022"/>
    </filter>
  </defs>

  <!-- Title -->
  <text x="460" y="25" fill="#1a1a2e" font-size="14" font-weight="bold" text-anchor="middle">图1 · 模态分解方法体系架构</text>

  <!-- ===== INPUT LAYER ===== -->
  <rect x="20" y="50" width="130" height="55" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="85" y="73" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">状态矩阵 A</text>
  <text x="85" y="90" fill="#4b6b8f" font-size="10" text-anchor="middle">线性系统 · 可对角化</text>

  <rect x="20" y="120" width="130" height="55" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="85" y="143" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">初始扰动 Δx(0)</text>
  <text x="85" y="160" fill="#4b6b8f" font-size="10" text-anchor="middle">时域波形数据</text>

  <rect x="20" y="190" width="130" height="55" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="85" y="213" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">传递函数 H(s)</text>
  <text x="85" y="230" fill="#4b6b8f" font-size="10" text-anchor="middle">B · C · D 矩阵</text>

  <!-- Arrows from input to decomposition layer -->
  <line x1="150" y1="77" x2="195" y2="77" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="150" y1="147" x2="195" y2="147" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="150" y1="217" x2="195" y2="217" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- ===== FIVE DECOMPOSITION METHODS ===== -->
  <rect x="210" y="50" width="150" height="65" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="285" y="72" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">特征向量模态分解</text>
  <text x="285" y="88" fill="#3a7a5a" font-size="9" text-anchor="middle">A · v_i = λ_i · v_i</text>
  <text x="285" y="102" fill="#3a7a5a" font-size="9" text-anchor="middle">Δx(t) = Σ c_i v_i e^{λ_i t}</text>

  <rect x="210" y="125" width="150" height="65" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="285" y="147" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">输出模态分解</text>
  <text x="285" y="163" fill="#3a7a5a" font-size="9" text-anchor="middle">Δy(t) = Σ c_i C v_i e^{λ_i t}</text>
  <text x="285" y="177" fill="#3a7a5a" font-size="9" text-anchor="middle">含输出矩阵 C</text>

  <rect x="210" y="200" width="150" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="285" y="222" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle">留数分解</text>
  <text x="285" y="238" fill="#a16207" font-size="9" text-anchor="middle">H(s) ≈ R_i / (s - λ_i)</text>
  <text x="285" y="252" fill="#a16207" font-size="9" text-anchor="middle">R_i = C v_i w_i^H B</text>

  <rect x="450" y="50" width="150" height="65" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="525" y="72" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle">时域辨识分解</text>
  <text x="525" y="88" fill="#a16207" font-size="9" text-anchor="middle">y(t) ≈ Σ a_i e^{σ_i t}</text>
  <text x="525" y="102" fill="#a16207" font-size="9" text-anchor="middle">cos(ω_i t + φ_i)</text>

  <rect x="450" y="125" width="150" height="65" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="525" y="147" fill="#3b0764" font-size="11" font-weight="bold" text-anchor="middle">Floquet 模态分解</text>
  <text x="525" y="163" fill="#6b21a8" font-size="9" text-anchor="middle">Φ(T) 状态转移矩阵</text>
  <text x="525" y="177" fill="#6b21a8" font-size="9" text-anchor="middle">Floquet 乘子 → 指数</text>

  <!-- Arrows from methods to output -->
  <line x1="360" y1="82" x2="448" y2="82" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="360" y1="157" x2="448" y2="157" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="360" y1="232" x2="448" y2="232" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- ===== OUTPUT LAYER ===== -->
  <rect x="620" y="50" width="130" height="55" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="685" y="73" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">模态参数</text>
  <text x="685" y="90" fill="#6b21a8" font-size="10" text-anchor="middle">频率 f_i · 阻尼 ζ_i</text>

  <rect x="620" y="120" width="130" height="55" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="685" y="143" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">参与因子</text>
  <text x="685" y="160" fill="#6b21a8" font-size="10" text-anchor="middle">w_i^H · Δx(0)</text>

  <rect x="620" y="190" width="130" height="55" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="685" y="213" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">模态贡献</text>
  <text x="685" y="230" fill="#6b21a8" font-size="10" text-anchor="middle">幅值 · 相位 · 衰减率</text>

  <!-- Arrows to output -->
  <line x1="600" y1="82" x2="618" y2="82" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="600" y1="147" x2="618" y2="147" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="600" y1="217" x2="618" y2="217" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>

  <!-- ===== STABILITY ASSESSMENT BOX ===== -->
  <rect x="780" y="50" width="120" height="195" rx="4" fill="#f3f4f6" stroke="#6b7280" stroke-width="2" stroke-dasharray="5,3" filter="url(#shadow)"/>
  <text x="840" y="72" fill="#374151" font-size="11" font-weight="bold" text-anchor="middle">稳定性判据</text>
  <text x="840" y="92" fill="#6b7280" font-size="9" text-anchor="middle">Re(λ_i) &lt; 0</text>
  <text x="840" y="110" fill="#6b7280" font-size="9" text-anchor="middle">→ 阻尼振荡</text>
  <text x="840" y="132" fill="#6b7280" font-size="9" text-anchor="middle">Re(λ_i) = 0</text>
  <text x="840" y="150" fill="#6b7280" font-size="9" text-anchor="middle">→ 临界稳定</text>
  <text x="840" y="172" fill="#dc2626" font-size="9" text-anchor="middle">Re(λ_i) &gt; 0</text>
  <text x="840" y="190" fill="#dc2626" font-size="9" text-anchor="middle">→ 不稳定</text>

  <!-- Dashed arrow to stability box -->
  <line x1="750" y1="147" x2="778" y2="147" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arr-dash)"/>

  <!-- ===== APPLIED SCENARIOS ===== -->
  <rect x="210" y="300" width="480" height="60" rx="4" fill="#f3f4f6" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="450" y="320" fill="#374151" font-size="11" font-weight="bold" text-anchor="middle">典型应用场景</text>
  <text x="240" y="340" fill="#6b7280" font-size="9" text-anchor="middle">IBR并网 · SSO筛查</text>
  <text x="370" y="340" fill="#6b7280" font-size="9" text-anchor="middle">次同步振荡定位</text>
  <text x="490" y="340" fill="#6b7280" font-size="9" text-anchor="middle">控制器参数整定</text>
  <text x="610" y="340" fill="#6b7280" font-size="9" text-anchor="middle">弱网稳定性评估</text>

  <!-- Legend -->
  <text x="20" y="385" fill="#333" font-size="10" font-weight="bold">图例</text>
  <rect x="20" y="393" width="14" height="8" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="40" y="401" fill="#555" font-size="9">输入</text>
  <rect x="75" y="393" width="14" height="8" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="95" y="401" fill="#555" font-size="9">特征向量/输出分解</text>
  <rect x="210" y="393" width="14" height="8" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="230" y="401" fill="#555" font-size="9">留数/时域辨识</text>
  <rect x="310" y="393" width="14" height="8" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="330" y="401" fill="#555" font-size="9">Floquet/输出参数</text>
  <rect x="420" y="393" width="14" height="8" rx="2" fill="#f3f4f6" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="440" y="401" fill="#555" font-size="9">稳定性判据/应用场景</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 模态分解方法体系架构：输入数据 → 五类模态分解方法 → 模态参数/参与因子/稳定性判据</p>

## 与相关页面的关系

- [[modal-analysis]]：解释模态形状、参与因子和灵敏度。
- [[eigenvalue-analysis]]：提供模态分解所需的特征值和特征向量。
- [[small-signal-stability-analysis]]：把模态分解用于稳定性分析验证。
- [[generalized-eigenvalue-method]]：处理矩阵束下的模态展开问题。
- [[frequency-scan]]和[[impedance-measurement]]：提供无显式状态矩阵时的频域响应证据。

## 来源论文

- [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] — 自动生成 EMT 伴随电路采样数据模型的特征值分析方法，支撑 Floquet 模态与特征向量分解的理论基础
- [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] — Floquet 参与因子用于 EMT 模型边界选择，可识别对目标振荡模态高度参与的网络元件
- [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] — Z-Tool 开源工具通过 EMT 频域识别获得导纳矩阵，用于小信号稳定分析和次同步振荡筛查
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] — Modelica 自动线性化生成 PV 场站状态矩阵，支持模态参数提取和控制交互风险评估
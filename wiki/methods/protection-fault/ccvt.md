---
title: "电容式电压互感器建模方法 (CCVT)"
type: method
tags: [ccvt, cvt, voltage-transformer, ferroresonance, measurement, transients, s-parameter, rational-model]
created: "2026-05-05"
updated: "2026-05-13"
---

# 电容式电压互感器建模方法 (CCVT)

## 定义

电容式电压互感器（Capacitive Coupling Voltage Transformer，CCVT）是一种基于电容分压原理的高压测量装置，用于将输电线路的高压按固定比例变换为低压信号，供继电保护装置、同步设备和故障录波系统使用。在电磁暂态（EMT）仿真中，CCVT 建模方法指在时域和频域中精确表示其内部所有电气元件及其非线性动态行为的数值技术路线。

CCVT 的核心结构由以下部分组成：

- **电容分压器**：高压臂电容 $C_1$ 与低压臂电容 $C_2$ 串联构成主分压网络
- **排流线圈**（阻尼线圈）$L_d$：串联在分压节点与中间变压器之间，用于限制故障电流并调谐至系统基频谐振
- **串联电抗器** $L_c$：进一步调谐分压网络，补偿电容分压器的容性电抗
- **降压变压器**（中间变压器 SDT）：将中间电压降至标准二次侧电压（通常为 100 V 或 100/√3 V）
- **谐波抑制滤波器**：并联在二次侧，抑制高频谐振过电压
- **集中杂散电容** $C_m$、$C_t$、$C_c$：分别表示排流线圈对地、降压变压器对地和串联电抗器对地的寄生电容
- **保护装置**：MOV（金属氧化物避雷器）、火花隙（spark-gap）、晶闸管（triac）等，用于限制内部过电压

最简稳态分压关系为：

$$
\frac{V_{out}}{V_{in}} = \frac{C_1}{C_1 + C_2}
$$

但 EMT 仿真中必须考虑完整的暂态测量链，因为 CCVT 不是线性固定变比元件——其二次侧波形失真来自分压网络、调谐电感、铁芯饱和、杂散电容、负载和保护器件的耦合效应。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="420" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">CCVT 等效电路拓扑与信号流向</text>
  
  <!-- Primary side input -->
  <rect x="20" y="60" width="120" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="80" y="82" text-anchor="middle" font-size="11" fill="#1e3a5f">一次侧输入</text>
  <text x="80" y="98" text-anchor="middle" font-size="10" fill="#1e3a5f">V_in (高压侧)</text>
  
  <!-- C1 capacitor -->
  <rect x="160" y="55" width="100" height="60" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="210" y="78" text-anchor="middle" font-size="11" fill="#14532d">C₁ 高压臂电容</text>
  <text x="210" y="96" text-anchor="middle" font-size="10" fill="#14532d">14611 pF</text>
  
  <!-- C2 capacitor -->
  <rect x="280" y="55" width="100" height="60" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="330" y="78" text-anchor="middle" font-size="11" fill="#14532d">C₂ 低压臂电容</text>
  <text x="330" y="96" text-anchor="middle" font-size="10" fill="#14532d">118400 pF</text>
  
  <!-- Arrow C1 to C2 -->
  <line x1="260" y1="85" x2="280" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Ld reactor -->
  <rect x="400" y="55" width="100" height="60" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="78" text-anchor="middle" font-size="11" fill="#14532d">Ld 排流线圈</text>
  <text x="450" y="96" text-anchor="middle" font-size="10" fill="#14532d">10 mH</text>
  
  <!-- Arrow C2 to Ld -->
  <line x1="380" y1="85" x2="400" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Lc reactor -->
  <rect x="520" y="55" width="100" height="60" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="570" y="78" text-anchor="middle" font-size="11" fill="#14532d">Lc 串联电抗器</text>
  <text x="570" y="96" text-anchor="middle" font-size="10" fill="#14532d">42 H</text>
  
  <!-- Arrow Ld to Lc -->
  <line x1="500" y1="85" x2="520" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- SDT transformer -->
  <rect x="640" y="50" width="110" height="70" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="695" y="73" text-anchor="middle" font-size="11" fill="#78350f">SDT 降压变压器</text>
  <text x="695" y="91" text-anchor="middle" font-size="10" fill="#78350f">非线性饱和特性</text>
  <text x="695" y="105" text-anchor="middle" font-size="9" fill="#78350f">多分接头切换</text>
  
  <!-- Arrow Lc to SDT -->
  <line x1="620" y1="85" x2="640" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Stray capacitances (bottom) -->
  <rect x="180" y="160" width="80" height="40" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="220" y="178" text-anchor="middle" font-size="9" fill="#991b1b">Cc 杂散电容</text>
  <text x="220" y="192" text-anchor="middle" font-size="9" fill="#991b1b">242 pF</text>
  
  <rect x="290" y="160" width="80" height="40" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="330" y="178" text-anchor="middle" font-size="9" fill="#991b1b">Ct 杂散电容</text>
  <text x="330" y="192" text-anchor="middle" font-size="9" fill="#991b1b">变压器对地</text>
  
  <rect x="400" y="160" width="80" height="40" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="440" y="178" text-anchor="middle" font-size="9" fill="#991b1b">Cm 杂散电容</text>
  <text x="440" y="192" text-anchor="middle" font-size="9" fill="#991b1b">排流线圈对地</text>
  
  <!-- Dashed lines for stray caps -->
  <line x1="220" y1="115" x2="220" y2="158" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="330" y1="115" x2="330" y2="158" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="440" y1="115" x2="440" y2="158" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  
  <!-- Protection devices -->
  <rect x="540" y="155" width="100" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="590" y="175" text-anchor="middle" font-size="10" fill="#991b1b">MOV / 火花隙</text>
  <text x="590" y="190" text-anchor="middle" font-size="9" fill="#991b1b">triac 保护器件</text>
  
  <line x1="695" y1="120" x2="590" y2="153" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,3"/>
  
  <!-- Filter -->
  <rect x="760" y="155" width="100" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="810" y="175" text-anchor="middle" font-size="10" fill="#78350f">谐波抑制</text>
  <text x="810" y="190" text-anchor="middle" font-size="9" fill="#78350f">滤波器 75 Ω</text>
  
  <!-- Arrow SDT to output -->
  <line x1="695" y1="120" x2="695" y2="140" stroke="#333" stroke-width="2"/>
  <line x1="695" y1="140" x2="810" y2="140" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="810" y1="140" x2="810" y2="153" stroke="#333" stroke-width="2"/>
  
  <!-- Output -->
  <rect x="740" y="230" width="140" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="810" y="252" text-anchor="middle" font-size="11" fill="#4c1d95">二次侧输出</text>
  <text x="810" y="268" text-anchor="middle" font-size="10" fill="#4c1d95">V_out (100 V)</text>
  
  <!-- Load -->
  <rect x="740" y="310" width="140" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="810" y="332" text-anchor="middle" font-size="11" fill="#4c1d95">负载</text>
  <text x="810" y="348" text-anchor="middle" font-size="10" fill="#4c1d95">400 VA, pf=0.8滞后</text>
  
  <line x1="810" y1="280" x2="810" y2="308" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Natural frequency annotation -->
  <rect x="20" y="280" width="200" height="80" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="120" y="303" text-anchor="middle" font-size="11" font-weight="bold" fill="#78350f">关键频率参数</text>
  <text x="120" y="320" text-anchor="middle" font-size="10" fill="#78350f">f_n = 1 / (2π√(Ld·C_eq))</text>
  <text x="120" y="336" text-anchor="middle" font-size="10" fill="#78350f">= 13.956 kHz</text>
  <text x="120" y="350" text-anchor="middle" font-size="9" fill="#92400e">主导高频暂态响应</text>
  
  <!-- Arrow from main line to freq box -->
  <line x1="330" y1="115" x2="220" y2="280" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4,3"/>
  
  <!-- Ferroresonance warning -->
  <rect x="20" y="380" width="200" height="30" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="120" y="399" text-anchor="middle" font-size="10" fill="#991b1b">⚠ 铁磁谐振起振条件: pf &lt; 0.6滞后</text>
  
  <!-- Arrow markers -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · CCVT 等效电路拓扑与信号流向（基于 Haefely-Trench TEHMP161A 参数）</p>

## EMT 中的角色

CCVT 在 EMT 仿真中承担着连接一次侧高压系统与被测二次侧保护设备的桥梁作用。其重要性体现在以下方面：

**测量失真评估**：故障和开关操作期间，CCVT 内部非线性元件（铁芯饱和、MOV 导通）和寄生参数会显著改变二次侧输出电压波形。若用理想电压测量替代 CCVT 模型，将严重低估继电保护与同步环节（如 PLL）的误差。

**铁磁谐振分析**：CCVT 的电容分压器与系统电感在特定工况下可能形成谐振回路，激发次谐波振荡。这种铁磁谐振不仅影响测量精度，还可能造成内部器件热应力累积和绝缘老化。

**保护通道真实性**：距离保护、方向保护等算法依赖 CCVT 提供的电压测量值。CCVT 的暂态响应特性（高频振荡、衰减包络、相位偏移）直接影响保护判据的动作时间和选择性。

**VFTO 传播研究**：在气体绝缘变电站（GIS）中，隔离开关操作和故障产生的极快瞬态过电压（VFTO，频率范围 100 kHz ~ 50 MHz）会通过 CCVT 的一次-二次耦合传播到二次回路，威胁二次设备安全。

**核心挑战**：CCVT 不是单一元件，而是由十余个电气参数耦合而成的多端口非线性系统。其暂态响应取决于：
- 电容分压比 $C_1/C_2$
- 调谐回路 $L_d$、$L_c$ 与等效电容的谐振频率
- 降压变压器饱和磁化曲线
- 杂散电容 $C_m$、$C_t$、$C_c$ 的分布
- 负载容量和功率因数
- 保护器件（MOV、火花隙）的伏安特性

## EMT 建模方法

根据精度需求和应用场景，CCVT 建模可分为四个层次：

### 方法一：纯电容分压模型（最简化）

仅保留 $C_1$ 和 $C_2$ 的稳态分压关系：

$$
\frac{V_{out}}{V_{in}} = \frac{C_1}{C_1 + C_2}
$$

**特点**：计算量极小，适用于工频潮流和稳态分析。

**局限性**：完全忽略调谐回路、变压器动态和寄生参数，无法捕捉任何暂态过程。在故障暂态下，二次侧输出仅为一次侧的线性缩放，不反映真实 CCVT 的高频振荡和铁磁谐振现象。

**适用场景**：仅用于不包含保护暂态评估的粗粒度仿真。

### 方法二：线性调谐等效电路（中等精度）

在电容分压基础上，显式包含排流线圈 $L_d$、串联电抗器 $L_c$ 和二次侧负载，将所有元件视为线性参数。该模型可捕捉基频调谐和若干低频谐振模态。

**自然振荡频率**由分压电容与排流线圈构成的 LC 回路决定：

$$
f_n = \frac{1}{2\pi\sqrt{L_d \cdot C_{eq}}} = \frac{1}{2\pi\sqrt{L_d \cdot \frac{C_1 C_2}{C_1 + C_2}}}
$$

其中 $C_{eq} = \frac{C_1 C_2}{C_1 + C_2}$ 为串联等效电容。

对于 Haefely-Trench TEHMP161A 型 CCVT（$C_1 = 14611 \text{ pF}$，$C_2 = 118400 \text{ pF}$，$L_d = 10 \text{ mH}$）：

$$
C_{eq} = \frac{14611 \times 118400}{14611 + 118400} \approx 13257 \text{ pF}
$$

$$
f_n = \frac{1}{2\pi\sqrt{10 \times 10^{-3} \times 13257 \times 10^{-12}}} \approx 13956 \text{ Hz}
$$

该 13.956 kHz 模态主导了近端接地故障下的高频暂态响应。

**特点**：可复现调谐回路的主谐振频率和若干低频谐振峰，计算量适中。

**局限性**：无法预测铁磁谐振（需要变压器非线性饱和特性）、无法反映杂散电容对频响的影响（$C_c$ 从 0 增至 1500 pF 时，频响曲线第一谷点频率偏移至约 640 Hz），也无法模拟保护器件的动作。

**适用场景**：工频及近工频（< 1 kHz）的暂态评估，不包含铁磁谐振风险的保护方案校核。

### 方法三：全元件级非线性时域模型（高保真）

基于 Iravani & Wang (2004) 的 EMTP 建模框架，将 CCVT 的所有内部组件按实际拓扑组网，纳入非线性磁化曲线、保护器件伏安特性和多分接头切换逻辑。

**模型组成**：

| 组件 | 参数 | 物理意义 |
|------|------|----------|
| $C_1$ | 14611 pF | 高压臂电容 |
| $C_2$ | 118400 pF | 低压臂电容 |
| $L_d$ | 10 mH | 排流线圈（阻尼线圈） |
| $L_c$ | 42 H | 串联电抗器 |
| SDT 一次电阻 $R_1$ | 284.5 Ω | 降压变压器一次绕组直流电阻 |
| SDT 一次电感 $L_1$ | 7.37 H | 降压变压器一次绕组电感 |
| SDT 励磁电阻 $R_m$ | 4.96 MΩ | 铁芯损耗等效电阻 |
| $C_c$ | 242 pF | 串联电抗器杂散电容 |
| 谐波抑制滤波器 | 75 Ω（线性支路） | 二次侧阻尼滤波 |
| 典型负载 | 400 VA, pf=0.8 滞后 | 二次侧测量负载 |

**频域幅频响应传递函数**用于评估不同频率下的电压传递衰减特性：

$$
H(f) = 20 \log_{10}\left(\frac{V_{out}(f)}{V_{in}(f)}\right)
$$

**铁芯磁链与饱和特性**的积分关系用于构建非线性磁化曲线：

$$
\Psi = \int V_{sec}(t) \cdot i_{mag}(t) \, dt
$$

**求解流程**（基于 EMTP 梯形积分法与补偿法）：

1. **拓扑建模与参数初始化**：在 EMTP 中搭建 CCVT 完整电路拓扑，录入各元件基准参数，配置 SDT 多分接头切换逻辑与杂散电容集中等效节点。
2. **频域灵敏度扫描**：将非线性元件线性化，施加扫频电压源，计算幅频曲线，遍历 $L_d$、$L_c$、$C_c$、$C_t$ 及负载 VA/pf 等变量，识别对 > 300 Hz 及 < 60 Hz 频段敏感的关键寄生参数。
3. **时域暂态激励注入**：设置开关模拟系统近端接地故障与二次侧短路，在电压峰值或过零点触发操作，生成阶跃与短路电流冲击波形。
4. **非线性暂态求解**：启用 EMTP 梯形积分算法，结合 SDT 分段线性磁化曲线与 MOV 非线性电阻模型，采用补偿法迭代求解网络节点电压与支路电流。
5. **保护装置效能评估**：对比无保护、火花隙限压与 MOV 吸收三种工况下的过电压峰值与能量积分，量化铁磁谐振抑制效果与热应力分布。
6. **试验数据交叉验证**：将仿真输出与实验室实测波形进行时域对齐，调整 $L_d$ 品质因数（Q 值）与滤波器饱和阈值，直至振荡频率、衰减时间常数及谐振起振点误差收敛至工程允许范围。

**特点**：可精确预测铁磁谐振起振、次谐波振荡、高频衰减过程及保护器件动作行为。

**局限性**：建模复杂度高，需要实测磁化曲线、抽头配置、保护器件伏安特性和负载数据；计算量大，不适用于大规模系统实时仿真。

**适用场景**：继电保护暂态性能评估、CCVT 保护/铁磁谐振抑制装置设计、故障和投切事件下的测量链路建模。

### 方法四：多端口黑盒有理模型（超宽带）

针对 GIS 中 VFTO（极快瞬态过电压，频率范围 100 kHz ~ 50 MHz）研究，Oliveira 等 (2022) 提出了基于 S 参数的多端口黑盒有理模型方法。传统方法使用 Y 参数或纯电容元件建模 VT，但无法复现特征谐振频率，也无法预测瞬态如何传播到 VT 二次绕组。

**S 参数到 Y 参数的转换**：

线性多端口网络在频域中的基本关系：

$$
I(s) = Y(s)V(s)
$$

其中 $Y(s)$ 为导纳矩阵。当使用 S 参数（散射参数）进行测量时，优化问题为：

$$
\minimize_{\tilde{S}} \sum_{k=1}^{K} \left\| S(j\omega_k) - \tilde{S}(j\omega_k) \right\|_2^2
$$

通过 S 参数到 Y 参数的转换，可将测量频率范围扩展至 50 MHz，从而准确捕获 GIS 设施中 VFTO 现象的全部动力学特性。

**电压传递函数**（从一次侧高压端子到二次侧低压端子）：

$$
\frac{V_1(j\omega)}{V_2(j\omega)} = \frac{Y_{13}(j\omega)Y_{33}(j\omega) - Y_{12}(j\omega)}{Y_{11}(j\omega) - \frac{Y_{13}(j\omega)Y_{31}(j\omega)}{Y_{33}(j\omega)}}
$$

**有理逼近与状态空间实现**：

通过向量拟合（Vector Fitting）方法，将频域测量数据拟合为有理函数，并转化为状态空间实现：

$$
\begin{cases}
\dot{x}(t) = A x(t) + B u(t) \\
y(t) = C x(t) + D u(t)
\end{cases}
$$

其中 $\{A, B, C, D\}$ 为状态空间矩阵，可直接嵌入 EMT 仿真器（如 EMTP-RV、PSCAD）进行高效时域仿真，CPU 时间随仿真长度线性缩放。

**特点**：覆盖 100 kHz ~ 50 MHz 超宽带频率范围，无需知道内部拓扑结构（黑盒方法），计算效率高。

**局限性**：需要精确的频域测量数据（S 参数），测量设备在 MHz 范围的性能限制模型精度；不提供内部物理量的可解释性。

**适用场景**：GIS 中 VFTO 传播研究、二次回路过电压风险评估、超宽带 VT 建模。

### 方法对比总览

| 方法 | 精度 | 频率范围 | 非线性 | 计算量 | 适用场景 |
|------|------|----------|--------|--------|----------|
| 纯电容分压 | 低 | 工频 | 否 | 极小 | 稳态潮流 |
| 线性调谐等效 | 中 | < 1 kHz | 否 | 低 | 保护方案校核 |
| 全元件非线性时域 | 高 | < 50 kHz | 是 | 高 | 继电保护评估 |
| 多端口黑盒有理模型 | 高 | 50 MHz | 线性 | 中 | GIS VFTO 研究 |

## 形式化表达

### 核心公式汇总

**电容分压比**：

$$
k = \frac{C_1}{C_1 + C_2}
$$

**LC 回路自然谐振频率**：

$$
f_n = \frac{1}{2\pi\sqrt{L_d \cdot \frac{C_1 C_2}{C_1 + C_2}}}
$$

**频域幅频响应**：

$$
H(f) = 20 \log_{10}\left(\frac{V_{out}(f)}{V_{in}(f)}\right) \quad [\text{dB}]
$$

**铁芯磁链积分关系**：

$$
\Psi(t) = \int_0^t V_{sec}(\tau) \cdot i_{mag}(\tau) \, d\tau
$$

**S 参数优化拟合目标**：

$$
\minimize \sum_{k=1}^{K} \left\| S(j\omega_k) - \tilde{S}(j\omega_k) \right\|_2^2
$$

**电压传递函数（三端口网络）**：

$$
\frac{V_1}{V_2} = \frac{Y_{13}Y_{33} - Y_{12}}{Y_{11} - \frac{Y_{13}Y_{31}}{Y_{33}}}
$$

**状态空间 EMT 实现**：

$$
\dot{x} = Ax + Bu, \quad y = Cx + Du
$$

## 关键技术挑战

### 铁磁谐振起振与次谐波振荡

CCVT 的铁磁谐振是 EMT 仿真中最具挑战性的非线性现象之一。当负载功率因数低于 0.6 滞后时，电容分压器与降压变压器励磁电感可能形成谐振回路，激发次谐波振荡。Iravani & Wang (2004) 通过 EMTP 仿真复现了这一现象：在二次侧短路后断开（S2 在电压峰值闭合后 10 周期断开）的测试中，SDT 铁芯饱和引发次谐波铁磁谐振，MOV 投入后有效吸收谐振能量，抑制电压畸变。

### 杂散电容对频响的决定性影响

串联电抗器杂散电容 $C_c$ 对低频段谐振特性具有决定性影响。当 $C_c$ 从 0 pF 增至 1500 pF 时，频响曲线第一谷点频率偏移至约 640 Hz。$C_c = 242 \text{ pF}$（TEHMP161A 实测值）是精确预测低频谐振特性的关键参数。

### 排流线圈 Q 值对高频振荡衰减的调控

排流线圈 $L_d$ 的品质因数（Q 值）直接决定 13.956 kHz 振荡模态的衰减速率。准确表征 $L_d$ 损耗是抑制高频过电压仿真的关键。Iravani & Wang (2004) 通过迭代优化 Q 值，使仿真与实测波形在振荡频率、衰减时间常数及谐振起振点上高度吻合。

### 超宽带测量与建模的仪器限制

Oliveira 等 (2022) 指出，Y 参数测量在 MHz 频率范围受到固有寄生电容耦合的限制，且需要电流互感器，不可避免地引入插入阻抗。S 参数测量无需短路条件，不要求电流互感器，可自然扩展测量频率至 50 MHz。但 S 参数测量本身在超高频段也面临仪器带宽和校准精度的限制。

## 量化性能边界

以下数据来自 Iravani & Wang (2004) 的实验验证和灵敏度分析：

| 指标 | 数值 | 来源 |
|------|------|------|
| 自然振荡频率 | 13.956 kHz | Iravani & Wang 2004 |
| Cc 从 0→1500 pF 时谷点频率偏移 | 至约 640 Hz | Iravani & Wang 2004 |
| 负载 pf=0.4 滞后时 > 300 Hz 频段幅频衰减 | 较 pf=1.0 增大逾 15 dB | Iravani & Wang 2004 |
| 全参数模型 vs 简化模型高频振荡幅值误差 | < 3% | Iravani & Wang 2004 |
| 仿真与实测波形相位偏差 | < 2% | Iravani & Wang 2004 |
| 起振时刻误差 | < 0.5 ms | Iravani & Wang 2004 |
| 60 Hz 电压传递误差 | -73 dB 精确捕获 | Oliveira 等 2022 |
| 超宽带测量频率范围 | 100 kHz ~ 50 MHz | Oliveira 等 2022 |
| 负载功率因数影响阈值 | pf < 0.6 滞后时频响显著变化 | Iravani & Wang 2004 |

## 适用边界与选择指南

### 模型选择决策树

```
是否需要保护暂态评估？
├─ 否 → 纯电容分压模型（仅稳态）
└─ 是 → 是否需要铁磁谐振分析？
    ├─ 否 → 线性调谐等效电路
    └─ 是 → 频率范围？
        ├─ < 50 kHz → 全元件非线性时域模型（EMTP）
        └─ > 100 kHz → 多端口黑盒有理模型（S 参数 + Vector Fitting）
```

### 具体适用场景

| 应用场景 | 推荐模型 | 关键参数需求 |
|----------|----------|--------------|
| 工频潮流与稳态电压测量 | 纯电容分压 | $C_1$、$C_2$ |
| 故障暂态保护动作时间评估 | 线性调谐等效 | $C_1$、$C_2$、$L_d$、$L_c$、负载 |
| 铁磁谐振风险评估 | 全元件非线性时域 | 全部参数 + SDT 磁化曲线 + MOV 特性 |
| GIS VFTO 传播研究 | 多端口黑盒有理模型 | S 参数测量数据（100 kHz ~ 50 MHz） |
| 距离保护高频响应评估 | 全元件非线性时域 | 全部参数 + 负载 pf 范围 |

### 失效边界

- **不应外推**到原文未覆盖的拓扑结构（如分裂电容、多抽头设计）、不同额定电压等级（110 kV ~ 1000 kV 参数差异显著）、实时仿真步长限制（> 1 μs 会丢失 13.956 kHz 模态）。
- **不应忽略**杂散电容 $C_m$、$C_t$、$C_c$ 的影响——这些寄生参数对低频段谐振特性具有决定性作用。
- **不应假设**所有 CCVT 型号的 Q 值、磁化曲线和保护器件参数相同——不同制造商（Haefely-Trench、Končar 等）的参数差异显著。

## 相关方法 / 相关模型 / 相关主题

- [[ferroresonance]] - 铁磁谐振机理与仿真方法
- [[gis]] - 气体绝缘变电站中的 VFTO 现象
- [[lightning-overvoltage]] - 过电压分析（含 VFTO 相关内容）
- [[phasor-measurement-unit]] - 测量链和动态相量背景
- [[digital-distance-protection]] - 保护算法对测量链失真的敏感性
- [[fault-analysis]] - 故障激励是 CCVT 暂态误差的主要触发场景
- [[electromagnetic-transient]] - 高频暂态和铁磁谐振背景
- [[protection-system]] - 保护系统整体背景
- [[vector-fitting]] - 有理逼近与黑盒建模
- [[frequency-dependent-modeling]] - 频率相关建模方法
- [[transformer-model]] - 变压器建模方法（SDT 非线性饱和建模的基础）
- [[impedance-measurement]] - 频域阻抗测量方法
## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Iravani & Wang, "Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Voltage Transformer", IEEE Trans. Power Delivery | 2004 | 建立 Haefely-Trench TEHMP161A CCVT 全元件级 EMTP 时域模型，涵盖电容分压器、排流线圈、非线性 SDT、串联电抗器、杂散电容和保护装置；通过实验室测试验证，量化了自然振荡频率（13.956 kHz）、杂散电容影响、负载功率因数影响和 Q 值调控作用 |
| Oliveira 等, "Expanding the measuring range via S-parameters in a EHV voltage transformer modelling for reliable GIS VFT simulations", Electric Power Systems Research | 2022 | 提出基于 S 参数的多端口黑盒有理模型方法，将 VT 测量频率范围扩展至 50 MHz，解决传统 Y 参数方法在 MHz 频段的测量局限，适用于 GIS 中 VFTO 传播研究 |
| Trkulja 等, "Lightning impulse voltage distribution over voltage transformer windings — Simulation and measurement", Electric Power Systems Research | 2017 | 提出基于边界元法（BEM）的电压互感器绕组集总参数快速精确计算方法，包括电容矩阵、电感矩阵和电阻矩阵的解析求解，建立了等效电路的时域求解框架 |

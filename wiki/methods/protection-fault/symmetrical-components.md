---
title: "对称分量法 (Symmetrical Components)"
type: method
tags: [symmetrical-components, sequence, unbalanced, fault-analysis, fortescue, fortescue-transform, sequence-network, zero-sequence, positive-sequence, negative-sequence]
created: "2026-05-02"
updated: "2026-05-16"
---

# 对称分量法 (Symmetrical Components)

## 定义与边界

对称分量法（Symmetrical Components）是 Fortescue 于 1918 年提出的线性代数分解方法，将任意一组三相复相量唯一分解为零序、正序和负序三组对称相量。三相相量 $[X_a, X_b, X_c]^T$ 经 Fortescue 变换后得到序相量 $[X_0, X_1, X_2]^T$，三者各自满足特定的对称性约束：

| 分量 | 相序关系 | 对称性 |
|------|----------|--------|
| 零序 $X_0$ | 三相同相（$0^\circ$ 相移） | $[1, 1, 1]$ 基底 |
| 正序 $X_1$ | a-b-c 正相序（$120^\circ$ 顺时针） | $[1, a, a^2]$ 基底 |
| 负序 $X_2$ | a-c-b 反相序（$120^\circ$ 逆时针） | $[1, a^2, a]$ 基底 |

其中复算子 $a = e^{j120^\circ} = -\frac{1}{2} + j\frac{\sqrt{3}}{2}$，满足 $a^3 = 1$ 和 $1 + a + a^2 = 0$。

**重要边界**：对称分量法是一种数学工具，不是完整的故障模型。它本身不自动给出设备参数、保护动作或 EMT 暂态波形。序阻抗 $Z_0$、$Z_1$、$Z_2$ 需由具体设备和网络模型提供。

本页负责数学定义和物理解释。使用流程见 [[sequence-component-method]]；序网构建见 [[sequence-network-model]]；直接相域建模见 [[phase-domain-modeling]]。

## 数学定义

### Fortescue 变换

令 $a = e^{j120^\circ}$，相量到序量的正变换为：

$$\begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix} \begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix}$$

反变换（逆 Fortescue 变换）为：

$$\begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix}$$

由矩阵乘法展开得各相分量表达式：

$$X_a = X_0 + X_1 + X_2$$

$$X_b = X_0 + a^2 X_1 + a X_2$$

$$X_c = X_0 + a X_1 + a^2 X_2$$

### 零序、正序、负序分量的物理含义

| 分量 | 相序关系 | 常见物理解释 | 边界条件 |
|------|----------|-------------|---------|
| 零序 $X_0$ | 三相同相 | 接地通道、中性点位移、共模分量 | 是否流通取决于回路——零序网络必须存在低阻抗闭合路径 |
| 正序 $X_1$ | a-b-c 正相序 | 正常基波运行和正向旋转磁场 | 不代表全部暂态能量；谐波和直流分量不在正序中 |
| 负序 $X_2$ | a-c-b 反相序 | 不平衡、反向旋转磁场、负序保护量 | 对旋转电机可能引起额外转子发热和振荡转矩 |

对称分量的"正序""负序"是**相量基底定义**，而非时域波形的直接分解。若研究瞬时波形中的正负序能量，需要明确从 EMT 数据中提取基频相量的方法（如短窗傅里叶滤波）。

## 与功率和阻抗的关系

### 序功率分解

在相量稳态且共轭约定一致的前提下，三相复功率可分解为各序贡献之和：

$$S = 3\left(V_0 I_0^* + V_1 I_1^* + V_2 I_2^*\right)$$

该式的成立依赖：电压和电流使用相同的序分量约定，且均为基频相量。

**工程注意**：保护、设备发热和稳定性分析不应只看这个代数式，还需考虑时间积分、负序热容量、控制限流和故障持续时间等外部条件。

### 序阻抗的非自动性

序阻抗 $Z_0$、$Z_1$、$Z_2$ 不是由变换矩阵自动给出的——它们来自设备和网络模型：

- **正序阻抗** $Z_1$：与普通相域阻抗等价，由线路电阻 $R$、感抗 $X_L$ 决定
- **负序阻抗** $Z_2$：对静止设备（如线路、变压器、电缆）通常 $Z_2 \approx Z_1$；对旋转电机则不同
- **零序阻抗** $Z_0$：受接地方式、变压器连接组别、中性点电抗等影响，通常 $Z_0 \neq Z_1$

## EMT 中的建模方法

对称分量在 EMT 建模中的核心作用是**将三相耦合系统解耦为三个独立的序网**，从而将不对称故障分析从联立方程求解转化为序网叠加。EMT 仿真中对称分量的应用主要有以下四类场景：

### 场景一：相量域故障计算（静态）

将 EMT 仿真的稳态结果或故障前后潮流解投影到序域，用序阻抗网络计算故障电流。适用于：保护整定验证、短路容量评估、不平衡度计算。此场景的核心是**序网方程**：

$$\begin{bmatrix} V_0 \\ V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} Z_0 & 0 & 0 \\ 0 & Z_1 & 0 \\ 0 & 0 & Z_2 \end{bmatrix} \begin{bmatrix} I_0 \\ I_1 \\ I_2 \end{bmatrix}$$

对角序阻抗矩阵体现了对称分量法对三相耦合系统的对角化解耦能力。

### 场景二：序域阻抗测量（动态相量）

从 EMT 时域仿真结果中提取基频对称分量，构建序域阻抗/导纳矩阵，用于稳定性分析。[[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth|Meng 等 2023]] 提出耦合序域扫描（CSD-scan）：直接在静止坐标系注入三相平衡电压扰动，利用 DFT 同步提取正、负序电流响应，构建计及镜像频率效应的 MIMO 导纳矩阵。相比传统 dq 域方法，计算负担降低 50%，且能区分物理谐振频率与数学镜像频率。

### 场景三：dq-序动态相量建模

[[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Mao 等 2025]] 提出 dq-序动态相量（dq-SDP），将对称分量分解与 dq 旋转坐标结合：

1. 对三相时域信号进行瞬时对称分量分解（ISCD），得到正序（PS）、负序（NS）和零序（ZS）分量
2. 对正序分量应用 Park 变换 $[\theta]$，对负序应用 $[-\theta]$，零序单独保留
3. 在 dq 序坐标中取时变傅里叶系数作为 dq-SDP

dq-SDP 补足了已有序动态相量缺少的**乘法性质**，使含多频分量变量乘积（如 MMC 调制量 $\times$ 电流）的运算得以在序域完成，避免将控制方程转回 abc 坐标系的复杂推导。

### 场景四：序域距离保护算法

[[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym|Rosołowski 等 1997]] 将对称分量与复数微分方程结合用于数字距离保护。算法流程：

- **输入**：保护点三相电压、电流采样
- **滤波**：半周期非递归傅里叶滤波器提取对称分量
- **建模**：根据故障类型选择序分量组合，构建复数形式等效故障回路
- **求解**：将复数微分方程拆分为实部/虚部，单采样时刻直接解算出正序电阻 $R_1$ 和电抗 $X_1$

该方法在 400 kV/50 Hz 双回线路（线路 A 长 208 km，线路 B 长 180 km）上验证，故障测距响应时间稳定在半个周波（10 ms）以内，高阻故障（$R_f = 50\ \Omega$）检测时间近端 2 ms、远端 7 ms，采样率 1 kHz 下计算延迟低于 1 ms。

## 形式化表达

### 故障类型与序分量组合

对称分量法将不对称故障分解为各种基本故障类型的序分量组合：

| 故障类型 | $I_0$ | $I_1$ | $I_2$ | 边界条件 |
|----------|-------|-------|-------|----------|
| 单相接地（a-g） | $I_0 = I_1 = I_2$ | $= I_f / 3$ | $= I_f / 3$ | $V_1 = V_2 = V_0$ at fault |
| 两相接地（bc-g） | $I_0 = -I_2$ | $= I_1$ | $< 0$ | $V_1 = V_2$ at fault |
| 两相短路（bc） | $I_0 = 0$ | $= -I_2$ | $< 0$ | $V_1 = V_2$, $I_0 = 0$ |
| 三相短路（abc） | $I_0 = 0$ | $= V_1 / Z_1$ | $= 0$ | 纯正序 |

其中 $I_f$ 为故障点总故障电流。

### 序网等效电路

不对称故障通过序网叠加求解。正序网、负序网和零序网各自独立，仅在故障点通过故障类型边界条件耦合：

- **正序网**：与普通潮流计算网络相同，电压源为故障前 pre-fault 电压
- **负序网**：网络拓扑与正序相同，所有电源置零，等值阻抗 $Z_2$
- **零序网**：取决于系统接地方式，可能与正序/负序拓扑不同

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="400" fill="#ffffff"/>
  
  <!-- Input: Three-phase quantities -->
  <rect x="20" y="140" width="120" height="120" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="80" y="170" font-family="Arial" font-size="13" fill="#1e40af" text-anchor="middle" font-weight="bold">三相相量</text>
  <text x="80" y="192" font-family="Arial" font-size="11" fill="#3b82f6" text-anchor="middle">$X_a, X_b, X_c$</text>
  <text x="80" y="214" font-family="Arial" font-size="10" fill="#6b7280" text-anchor="middle">任意不对称量</text>
  <text x="80" y="236" font-family="Arial" font-size="10" fill="#6b7280" text-anchor="middle">三相 abc 坐标系</text>

  <!-- Arrow to Fortescue transform -->
  <line x1="140" y1="200" x2="195" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="168" y="190" font-family="Arial" font-size="10" fill="#374151" text-anchor="middle">Fortescue</text>
  <text x="168" y="203" font-family="Arial" font-size="10" fill="#374151" text-anchor="middle">变换</text>

  <!-- Fortescue Transform Box -->
  <rect x="200" y="145" width="150" height="110" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="275" y="173" font-family="Arial" font-size="13" fill="#92400e" text-anchor="middle" font-weight="bold">Fortescue 变换</text>
  <text x="275" y="196" font-family="Arial" font-size="10" fill="#92400e" text-anchor="middle">$a = e^{j120^\circ}$</text>
  <text x="275" y="215" font-family="Arial" font-size="10" fill="#92400e" text-anchor="middle">$a^3 = 1$, $1+a+a^2=0$</text>
  <text x="275" y="234" font-family="Arial" font-size="9" fill="#b45309" text-anchor="middle">$\frac{1}{3}\begin{bmatrix}1&amp;1&amp;1\\1&amp;a&amp;a^2\\1&amp;a^2&amp;a\end{bmatrix}$</text>

  <!-- Arrows to three sequence outputs -->
  <line x1="350" y1="175" x2="405" y2="110" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="350" y1="200" x2="405" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="350" y1="225" x2="405" y2="290" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>

  <!-- Zero-sequence component -->
  <rect x="410" y="65" width="140" height="90" rx="6" fill="#fecaca" stroke="#dc2626" stroke-width="2"/>
  <text x="480" y="93" font-family="Arial" font-size="13" fill="#991b1b" text-anchor="middle" font-weight="bold">零序 $X_0$</text>
  <text x="480" y="116" font-family="Arial" font-size="11" fill="#dc2626" text-anchor="middle">三相同相</text>
  <text x="480" y="133" font-family="Arial" font-size="10" fill="#7f1d1d" text-anchor="middle">$[1, 1, 1]$ 基底</text>
  <text x="480" y="148" font-family="Arial" font-size="9" fill="#b91c1c" text-anchor="middle">接地回路决定流通性</text>

  <!-- Positive-sequence component -->
  <rect x="410" y="155" width="140" height="90" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="480" y="183" font-family="Arial" font-size="13" fill="#166534" text-anchor="middle" font-weight="bold">正序 $X_1$</text>
  <text x="480" y="206" font-family="Arial" font-size="11" fill="#16a34a" text-anchor="middle">a-b-c 正相序</text>
  <text x="480" y="223" font-family="Arial" font-size="10" fill="#15803d" text-anchor="middle">$[1, a, a^2]$ 基底</text>
  <text x="480" y="238" font-family="Arial" font-size="9" fill="#166534" text-anchor="middle">正常基波运行</text>

  <!-- Negative-sequence component -->
  <rect x="410" y="245" width="140" height="90" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="480" y="273" font-family="Arial" font-size="13" fill="#5b21b6" text-anchor="middle" font-weight="bold">负序 $X_2$</text>
  <text x="480" y="296" font-family="Arial" font-size="11" fill="#7c3aed" text-anchor="middle">a-c-b 反相序</text>
  <text x="480" y="313" font-family="Arial" font-size="10" fill="#6d28d9" text-anchor="middle">$[1, a^2, a]$ 基底</text>
  <text x="480" y="328" font-family="Arial" font-size="9" fill="#5b21b6" text-anchor="middle">不平衡/反向旋转</text>

  <!-- Arrow to output: Fault analysis -->
  <line x1="550" y1="200" x2="610" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <text x="580" y="190" font-family="Arial" font-size="10" fill="#374151" text-anchor="middle">序网叠加</text>

  <!-- Output: Sequence network -->
  <rect x="615" y="125" width="155" height="150" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
  <text x="692" y="153" font-family="Arial" font-size="13" fill="#075985" text-anchor="middle" font-weight="bold">序网等效电路</text>
  <text x="692" y="178" font-family="Arial" font-size="10" fill="#0369a1" text-anchor="middle">正序网: $Z_1$, 电压源</text>
  <text x="692" y="198" font-family="Arial" font-size="10" fill="#0369a1" text-anchor="middle">负序网: $Z_2 \approx Z_1$</text>
  <text x="692" y="218" font-family="Arial" font-size="10" fill="#0369a1" text-anchor="middle">零序网: $Z_0$ (接地决定)</text>
  <text x="692" y="243" font-family="Arial" font-size="10" fill="#0c4a6e" text-anchor="middle">对角序阻抗矩阵</text>
  <text x="692" y="260" font-family="Arial" font-size="9" fill="#164e63" text-anchor="middle">$V = Z \cdot I$ (三序解耦)</text>

  <!-- Arrow to fault results -->
  <line x1="770" y1="200" x2="825" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>

  <!-- Fault results -->
  <rect x="830" y="160" width="60" height="80" rx="6" fill="#f9fafb" stroke="#374151" stroke-width="1.5"/>
  <text x="860" y="185" font-family="Arial" font-size="11" fill="#1f2937" text-anchor="middle" font-weight="bold">故障</text>
  <text x="860" y="203" font-family="Arial" font-size="11" fill="#1f2937" text-anchor="middle">电流</text>
  <text x="860" y="221" font-family="Arial" font-size="11" fill="#1f2937" text-anchor="middle">电压</text>

  <!-- Legend at bottom -->
  <rect x="20" y="365" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="38" y="376" font-family="Arial" font-size="10" fill="#374151">输入/源</text>
  <rect x="100" y="365" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="118" y="376" font-family="Arial" font-size="10" fill="#374151">变换核</text>
  <rect x="180" y="365" width="12" height="12" fill="#fecaca" stroke="#dc2626" stroke-width="1"/>
  <text x="198" y="376" font-family="Arial" font-size="10" fill="#374151">零序</text>
  <rect x="250" y="365" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="268" y="376" font-family="Arial" font-size="10" fill="#374151">正序</text>
  <rect x="320" y="365" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="338" y="376" font-family="Arial" font-size="10" fill="#374151">负序</text>
  <rect x="390" y="365" width="12" height="12" fill="#f0f9ff" stroke="#0284c7" stroke-width="1"/>
  <text x="408" y="376" font-family="Arial" font-size="10" fill="#374151">序网输出</text>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · Fortescue 变换将不对称三相相量分解为零序、正序、负序三个独立对称分量，经序网叠加后求得故障电流和电压</p>

## 关键技术挑战

### 挑战一：零序网络的建模完整性

零序电流是否能够流通，**不取决于 $X_0$ 是否为零**，而取决于系统中是否存在零序电流的低阻抗闭合路径。具体地：

- 变压器 Yn 接法提供零序电流通路，Y 接法阻断零序电流
- 架空地线、单相接地故障点、中性点接地电抗共同决定零序回路
- EMT 仿真中若零序网络拓扑不完整，$X_0$ 计算会失真

### 挑战二：旋转电机负序效应的设备依赖性

负序电流对旋转电机的危害（转子发热、振荡转矩）**不是负序相量本身能够评估的**，而需要发电机转子模型提供负序电流-热容量耦合关系。仅用负序相量大小直接推断热风险会遗漏保护时机。

### 挑战三：暂态波形中序分量的时变提取

EMT 仿真输出的瞬时波形中包含衰减直流分量、高频谐波、开关纹波和行波成分。从这些混合信号中提取基频序分量，需要：

- **滤波**：半周期或全周期傅里叶滤波器（如 Rosołowski 1997 所用）
- **窗长权衡**：短窗（10 ms）响应快但抗频偏能力弱；长窗精度高但动作速度慢
- **频偏鲁棒性**：频率偏离额定值时，算子 $a = e^{j120^\circ}$ 的相位基准发生偏移，导致序分量估计误差

### 挑战四：序域与 EMT 时域的语义边界

"基频相量序分量"（phasor-domain symmetrical components）和"瞬时序分量"（instantaneous symmetrical components）是两个不同的概念：

- **相量域**：稳态/准稳态分析，频率固定为基频，结果是复数幅值-相位
- **瞬时域**：每时步计算，频率随信号变化，结果是时变复数

混用两者会导致 EMT 稳定分析中的虚假收敛或在保护算法中引入非物理振荡。

### 挑战五：非线性工况下的序分量失效

对称分量法的线性叠加性质在以下工况中失效：

- **非线性饱和**：变压器饱和导致零序电流中含有高次谐波，不能简单用 $X_0$ 解释
- **电弧故障**：电弧的电压-电流特性高度非线性，序分量分解无法捕捉电弧暂态
- **电力电子限流**：MMC、SVG 等设备在限流模式下序阻抗随控制状态变化，静态序网模型不再适用
- **断续接触故障**：接触电阻的随机跳变使序阻抗成为时变量

## 量化性能边界

### 序阻抗典型值

| 设备类型 | $Z_1$ (pu) | $Z_2/Z_1$ | $Z_0/Z_1$ | 数据来源 |
|----------|-----------|-----------|-----------|---------|
| 架空线路（每千米） | $R + jX_L$ | $\approx 1.0$ | $1.5-3.0$（大地回路影响） | 取决于线路几何参数 |
| 变压器（每台） | 取决于容量 | $\approx 1.0$（静止设备） | 接地方式决定 | IEEE C37.010 |
| 同步发电机 | $X_d''$ ~ $0.2$ pu | $0.1-0.5$ pu | $0.05-0.2$ pu（转子构造） | IEEE 421 |
| 接地电抗器 | — | — | $0.01-0.5$ pu | 系统接地设计 |

### 保护算法性能

| 方法 | 适用场景 | 精度 | 速度 | 数据来源 |
|------|---------|------|------|---------|
| 短窗傅里叶 + 复数微分方程 | 相量域阻抗测量 | 幅值误差 < 2% | < 1 ms 计算延迟 | [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym\|Rosołowski 1997]] |
| CSD-scan（耦合序域 MIMO） | IBR 阻抗稳定性分析 | 相位裕度偏差 0.4°（vs dq-scan） | 单次扫描降低 50% 计算量 | [[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth\|Meng 2023]] |
| 双端零序互感补偿法 | 平行线路接地故障测距 | 参数准确时误差 ~0 英里 | 4 次迭代收敛 | [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel\|Dase 2025]] |

### dq-SDP 建模性能（Mao 2025）

dq-序动态相量方法避免了控制方程从 dq 坐标系向 abc 坐标系的转换，显著降低了非对称工况下状态空间建模的推导复杂度。模型维度相比传统三相动态相量方法有所降低，适用于两端 MMC-HVDC 系统的非对称交流故障分析。

## 适用边界与选择指南

### 何时优先使用对称分量法

| 场景 | 推荐方法 | 说明 |
|------|---------|------|
| 不平衡电流/电压计算 | 序分量分解 | 快速将不对称三相量解耦为独立序分量 |
| 保护整定验证 | 序网故障计算 | 用 $Z_0, Z_1, Z_2$ 计算各故障类型的保护量 |
| 不平衡度评估 | $I_2/I_1$ 比值 | 衡量系统不平衡程度（GB/T 15531） |
| IBR 阻抗稳定性分析 | 耦合序域扫描（CSD-scan） | 计及镜像频率效应，比 dq-scan 效率更高 |
| 电力电子设备非对称建模 | dq-序动态相量（dq-SDP） | 避免 abc 坐标回代，保持 dq 控制接口 |

### 何时不适合使用对称分量法

| 场景 | 替代方法 |
|------|---------|
| 子模块开关暂态细节 | [[mmc-model]] 详细开关模型 |
| 故障后高频行波 | 行波故障测距 |
| 电弧非线性动态 | 电弧电阻时变模型 |
| 大扰动故障穿越 | [[electromagnetic-transient]] 全 EMT 时域仿真 |
| 电力电子设备内部谐波耦合 | [[harmonic-interaction]] 多谐波域建模 |

## 与相关页面的关系

- [[sequence-component-method]]：把本页 Fortescue 变换用于不平衡分析的步骤流程
- [[sequence-network-model]]：把序阻抗组织成故障计算网络，含故障回路方程推导
- [[coordinate-transformation]]：坐标变换总览（含 Clarke 变换、Park 变换等）
- [[dq-transformation]]：同步旋转坐标，与序分量可组合但不属于同一分解
- [[phase-domain-modeling]]：不通过序分解而直接求解 abc 耦合网络
- [[unbalanced-fault-analysis]]：不对称故障应用场景，含各类故障的序分量组合详解
- [[fault-analysis]]：不平衡故障中对称分量的上位方法入口
- [[dynamic-phasor]]：序分量、旋转坐标和包络变量的结合框架
- [[complex-differential-equation-solving]]：复数微分方程在序域阻抗测量中的应用

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] | 1997 | 短窗傅里叶 + 复数微分方程的序域距离保护算法；400 kV/50 Hz 双回线路验证；10 ms 内完成故障测距 |
| [[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth]] | 2023 | 耦合序域 MIMO 频扫（CSD-scan）；单次扫描覆盖全频段；计算负担降低 50% |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond]] | 2025 | dq-序动态相量（dq-SDP）；保持 dq 控制接口同时处理非对称工况；避免控制方程回代 abc 坐标系 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri]] | 2011 | 对称与不对称线路的时域建模；修正 Clarke 矩阵用于非换位线路模态解耦；50-100 μs 步长实现宽频暂态仿真 |
| [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel]] | 2025 | 零序互感补偿双端测距；无需测量平行线电流；自适应平均 4 次迭代收敛 |
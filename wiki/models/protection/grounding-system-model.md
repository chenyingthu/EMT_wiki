---
title: "接地系统 (Grounding System)"
type: model
tags: [grounding, earthing, soil, frequency-dependent, step-voltage, touch-voltage, GPR, tower-footing, soil-ionization, FDNE]
created: "2026-04-29"
updated: "2026-05-17"
---

# 接地系统 (Grounding System)

## 定义

接地系统是电力系统安全运行的重要基础设施，为故障电流提供低阻抗消散路径、限制雷电和操作过电压、保障人身和设备安全。在EMT仿真中，接地系统建模面临两大核心挑战：①接地阻抗随频率剧烈变化（从直流到雷电流频段，阻抗可变化2~10倍）；②土壤电离效应在冲击电流下导致接地电阻非线性变化。准确建模对于雷电暂态分析、变电站地电位升高（GPR）评估和绝缘配合设计至关重要。

## EMT中的作用

接地系统在EMT仿真中承担以下角色：

- **建模对象**：描述接地电极（垂直接地棒、水平接地极、接地网）的宽频电气特性
- **仿真场景**：适用于雷电过电压分析、故障电流分布、工频接地电阻计算、地电位升高评估
- **模型接口**：提供接地端口的频变阻抗/导纳边界条件，与输电线路、杆塔、变压器模型联解
- **验证基准**：GPR峰值、冲击阻抗、时域波形可作为接地模型正确性的验证基准

## EMT建模方法

### 方法1：集总电阻模型（简化模型）

最简化的接地模型，将接地系统等效为工频测得或计算的单一电阻 $R_0$。适用于工频接地电阻估算和稳态分析，但无法反映雷电高频暂态下的接地阻抗变化。

**接地电阻计算公式**：

均匀土壤中，垂直接地极的接地电阻为：

$$R_v = \frac{\rho}{2\pi L}\ln\frac{4L}{d}$$

水平接地极的接地电阻为：

$$R_h = \frac{\rho}{2\pi L}\ln\frac{L^2}{hd}$$

接地网的综合接地电阻近似为：

$$R_g = \frac{\rho}{4}\sqrt{\frac{\pi}{A}} + \frac{\rho}{L_{total}}$$

其中 $\rho$ 为土壤电阻率（Ω·m），$L$ 为接地极长度，$d$ 为等效直径，$h$ 为埋深，$A$ 为接地网面积，$L_{total}$ 为接地导体总长度。

### 方法2：传输线理论模型（Alipio 2023）

将接地电极建模为埋地传输线，采用Marti频变线路模型描述接地极的宽频特性。这是目前最准确的单根接地极EMT建模方法。

**电报方程**（2×2耦合系统）：

$$\frac{d\mathbf{V}}{dx} = -\mathbf{Z}_i\mathbf{I} - j\omega\mathbf{L}\mathbf{I}$$

$$\frac{d\mathbf{I}}{dx} = -(\mathbf{G} + j\omega\mathbf{C})\mathbf{V}$$

其中 $\mathbf{V}$ 和 $\mathbf{I}$ 为2×1电压电流向量，$\mathbf{Z}_i$ 和 $\mathbf{L}$ 为2×2内阻抗和电感矩阵，$\mathbf{G}$ 和 $\mathbf{C}$ 为2×2导纳和电容矩阵。

**接地网等效**：四根水平接地极（水平段长度 $l_2$，倾斜段长度 $l_1$，总长 $l=l_1+l_2$）从杆塔腿以45°角延伸。通过等效均匀传输线表征耦合特性，利用FDLine模型或Marti模型在ATP/EMTP中实现。

**有效长度约束**：接地极存在"有效长度"——超过该长度后继续延伸对降低接地电阻的贡献急剧减小。有效长度与土壤电阻率 $\rho$ 和注入电流波形相关（Alipio 2023: ρ=250 Ωm时有效长度约17m，ρ=2500 Ωm时约40m）。

### 方法3：频变网络等值FDNE（Lima 2026）

将接地系统建模为多端口频变网络等值（Frequency-Dependent Network Equivalent），通过有理函数逼近接地端口导纳 $Y_g(\omega)$ 或阻抗 $Z_g(\omega)$。

**节点导纳方程**：

$$\mathbf{Y}_n \cdot \mathbf{V} = \mathbf{I}_n$$

其中 $\mathbf{Y}_n$ 为等效节点导纳矩阵，$\mathbf{V}$ 为节点电压向量，$\mathbf{I}_n$ 为注入电流向量（注入点为1/4，其余为0）。

**接地阻抗计算**：

$$Z_g(\omega) = \frac{V_A(\omega)}{I_n(\omega)}$$

其中 $V_A$ 为地电位升高（GPR），$I_n$ 为注入电流。

**矢量拟合有理函数**：

$$Z_g(s) = R_0 + \sum_{k=1}^{N}\frac{R_k}{s - p_k}$$

或等效的导纳形式：

$$Y_g(s) = G_0 + \sum_{k=1}^{N}\frac{G_k}{s - p_k}$$

其中 $R_k$、$G_k$ 为留数，$p_k$ 为极点，$N$ 为逼近阶数。

**拓扑选择**：Lima 2026证明，直接拟合谐波导纳与将接地系统作为FDNE多端口网络两类拓扑相比，在满足有效长度约束时，FDNE实现略更鲁棒；所需最小阶数通常为4~8阶（误差<2%）。

### 方法4：动态土壤电离模型（Meyberg 2026）

实际冲击电流下，土壤电阻率随局部电场变化（电离效应），接地电阻不再是常数。Meyberg等将动态土壤电离模型通过DLL接入EMTP，无需细网格FDTD即可实现变电阻率接地。

**等位面壳层法**：将接地极周围土壤划分为若干等位面壳层，而非FDTD空间网格。EMTP在每个时间步将瞬态电流 $i(t)$、土壤初始电阻率 $\rho_0$、临界电场 $E_c$ 等参数传递给DLL，DLL逐壳层计算电场分布并更新各壳层电阻率，从而得到时变接地电阻 $R(t)$。

**电离模型**（Lowe & Sargent模型）：

$$\rho(E) = \frac{\rho_0}{1 + E/E_c}$$

其中 $E_c$ 为土壤临界电离场强（约300~400 kV/m取决于土壤类型），$\rho(E)$ 为电场 $E$ 下的等效电阻率。

**EMTP接口**：DLL以当前时间步接地电流 $i(t)$、土壤初始电阻率 $\rho_0$、临界电场 $E_c$、接地极几何参数为输入，返回更新后的接地电阻向量，实现与EMTP网络方程的耦合迭代。

### 方法5：分层土壤频变模型

实际土壤往往呈分层结构（表层高电阻率土+深层低电阻率土），需采用分层土壤模型。

**二层土壤等效**：表层厚度 $h$、电阻率 $\rho_1$；下层电阻率 $\rho_2$。通过镜像法或数值积分计算等效接地电阻：

$$R = \frac{\rho_1}{2\pi L}\ln\frac{2L}{d} + f(\rho_1, \rho_2, h, L)$$

其中 $f(\cdot)$ 为与分层结构相关的修正项（De Araújo 2021）。

**频变土壤参数**：土壤电导率 $\sigma(f)$ 和介电常数 $\varepsilon_r(f)$ 均随频率变化，导致高频下大地不再是理想良导体。考虑土壤频变特性后，接地阻抗在 f>1 MHz 时幅值显著降低（Alipio 2020）。

## 形式化表达

### 跨步电压与接触电压

**跨步电压**（两脚间距离 s=1m）：

$$E_{step} = \frac{\rho I}{2\pi}\left(\frac{1}{x} - \frac{1}{x+s}\right)$$

**接触电压**（手脚间）：

$$E_{touch} = \frac{\rho I}{2\pi}\left(\frac{1}{2x} + \frac{1}{D}\right)$$

其中 $D$ 为接地网等效直径，$x$ 为距接地中心距离。

**安全限值**（IEEE Std 80，50/60 Hz）：

$$E_{step}^{limit} = \frac{116 + 0.7\rho_s}{\sqrt{t}}$$

$$E_{touch}^{limit} = \frac{116 + 1.5\rho_s}{\sqrt{t}}$$

其中 $\rho_s$ 为表层土壤电阻率（Ω·m），$t$ 为故障持续时间（s）。

### 杆塔塔脚接地系统等效电路

四根水平接地极构成2×2耦合传输线系统，等效为一个二端口网络：

$$\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} Z_{11} & Z_{12} \\ Z_{21} & Z_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

端口1对地导纳 $Y_1 = 1/Z_{11}$，端口2对地导纳 $Y_2 = 1/Z_{22}$，转移导纳 $Y_{12} = -Z_{12}/(Z_{11}Z_{22}-Z_{12}^2)$。

### 雷电流波形（Heidler函数叠加）

雷电暂态仿真的注入电流通常用Heidler函数叠加表征：

$$i(t) = \sum_{k=1}^{n} \frac{I_{pk}}{k_p}\frac{(t/\tau_1)^{k_p}}{1+(t/\tau_1)^{k_p}}\exp(-t/\tau_2)$$

典型参数（Alipio 2023）：峰值 $I_p=31$ kA，前沿时间 $\tau_1=3.8$ μs（30%~90%峰值除以0.6），半峰值时间 $\tau_2=75$ μs。

## 关键技术挑战

**挑战1：接地阻抗频变耦合** — 从直流到雷电流频段（10 kHz~1 MHz），接地阻抗变化2~10倍，集肤效应和土壤频变特性需同时考虑。集肤深度 $\delta = \sqrt{2/(\omega\mu\sigma)}$ 在高频下急剧减小，等效导电截面积降低。

**挑战2：土壤电离非均匀性** — 大注入电流下，接地极周围电场超过土壤临界电离场强 $E_c$（300~400 kV/m），局部土壤电阻率降低，形成非均匀电离区。电离前锋推进过程难以用简单解析式描述，是冲击接地仿真中的核心难题（Meyberg 2026）。

**挑战3：有效长度与高频振荡** — 接地极超过有效长度后，导体末端产生高频反射振荡，与土壤参数频变耦合，导致宽频阻抗出现谐振峰值。Alipio 2023指出：在ρ=2500 Ωm土壤中，有效长度约40m；超长接地极的高频振荡可能使GPR峰值增加30%~50%。

**挑战4：分层土壤参数的获取与验证** — 分层土壤参数（$\rho_1$、$\rho_2$、$h$）通常通过温纳四极法现场测量获得，但测量频段有限（通常<1 kHz），外推至雷电频段（>100 kHz）的可靠性缺乏系统验证。

**挑战5：多接地极互耦与大型接地网等值** — 变电站接地网含数十至数百根导体，导体间互感耦合形成复杂频变网络。直接建模计算量巨大，需进行端口等值缩减。如何保证等值端口的频率依赖特性在宽频段内一致是尚未完全解决的问题。

## 量化性能边界

**接地电阻典型范围**（IEEE 80，均匀土壤）：

| 场景 | 电阻范围 | 典型条件 |
|------|---------|---------|
| 变电站接地网 | 0.1~5 Ω | ρ=10~500 Ω·m，A=100×100 m² |
| 输电线路杆塔 | 10~50 Ω | ρ=100~1000 Ω·m，L=30~50 m放射线 |
| 垂直接地极（L=2.5m） | 0.3ρ~0.4ρ Ω | d=20mm，h=0.8m |
| 水平接地极（L=30m） | 0.05ρ~0.1ρ Ω | h=0.8m |

**雷电流频率特性**（Alipio 2023，138kV线路，4根counterpoise，ρ=250~2500 Ω·m）：

- 工频（50/60 Hz）：$Z_g \approx R_0$，感性分量可忽略
- 雷电流频率（10 kHz~1 MHz）：$Z_g$ 可升至直流电阻的 2~10 倍
- 有效长度：ρ=250 Ωm时约17m；ρ=2500 Ωm时约40m
- GPR峰值：31 kA雷电流在ρ=1000 Ω·m土壤中典型值为30~80 kV（与接地极长度强相关）

**FDNE有理逼近精度**（Lima 2026）：

| 逼近阶数N | 最大误差 | 备注 |
|---------|---------|------|
| 2 | 15%~25% | 低频简化，100 kHz以下 |
| 4 | 5%~8% | 常规工程精度 |
| 6 | 2%~4% | 推荐工程精度 |
| 8 | <2% | 高精度需求场景 |

**矢量拟合阶数与误差**（Alipio 2020）：N=4~8 可实现误差<2%的宽频接地阻抗拟合（10 Hz~10 MHz）。

**土壤电离效应**（Meyberg 2026）：冲击电流峰值100 kA时，动态土壤电离模型下的接地电阻比恒电阻模型低30%~60%（取决于土壤电阻率和接地极长度）。

**安全电压限值**（IEEE Std 80）：允许跨步电压200~2000 V（t=0.5 s，ρ_s=100~5000 Ω·m）；允许接触电压相应更低（系数从0.7变为1.5）。

**EMT仿真步长选择**：

| 分析类型 | 推荐步长 | 原因 |
|---------|---------|------|
| 工频接地分析 | 50~100 μs | 准稳态，精度要求低 |
| 雷电暂态接地 | 0.01~0.1 μs | 波过程，步长需<<波头时间 |
| FDNE频变等效 | 1~10 μs | 矢量拟合有理函数变换允许较大步长 |

## 适用边界与选择指南

| 方法 | 适用场景 | 不适用场景 | 精度 | 计算效率 |
|------|---------|-----------|------|---------|
| 集总电阻 | 工频接地估算、初步设计 | 雷电暂态、高频分析 | 低 | 最高 |
| 传输线模型（FDLine/Marti） | 单根/少数接地极雷电分析 | 多接地极互耦、大型接地网 | 高 | 中 |
| FDNE有理逼近 | 需与EMTP联解的多端口接地 | 未知拓扑或非线性电离 | 高 | 中~高 |
| 动态电离模型 | 大注入电流冲击接地 | 小电流、工频分析 | 最高 | 低 |
| 分层土壤模型 | 分层土壤现场评估 | 均匀土壤、参数未知 | 中~高 | 中 |

**方法选择决策**：

1. **工频接地电阻计算** → 集总电阻模型（IEEE 80经验公式）
2. **杆塔雷电暂态分析（单杆塔）** → 传输线模型（Alipio 2023 FDLine/Marti）
3. **变电站接地网宽频等值** → FDNE矢量拟合（Lima 2026）
4. **大冲击电流接地（>10 kA）** → 动态土壤电离模型（Meyberg 2026 DLL）
5. **分层土壤现场数据** → 分层土壤频变模型（De Araújo 2021）

## 相关方法
- [[vector-fitting]] — 接地阻抗频变拟合（FDNE矢量拟合实现）
- [[nodal-analysis]] — 接地网节点分析（端口导纳矩阵组装）
- [[state-space-method]] — 频变接地状态空间实现
- [[frequency-dependent-modeling]] — 宽频接地建模总论
- [[numerical-integration]] — 雷电响应时域积分
- [[earth-return-impedance]] — 大地回路阻抗（ Carson/Pollaczek公式）
- [[mutual-impedance]] — 接地极间互感耦合

## 相关模型
- [[cable-model]] — 电缆金属护套接地
- [[transformer-model]] — 变压器中性点接地
- [[transmission-line-model]] — 杆塔接地与输电线路模型
- [[surge-arrester-model]] — 防雷接地（避雷器接地点）
- [[tower-model]] — 杆塔波阻抗模型

## 相关主题
- [[frequency-dependent-modeling]] — 频变接地建模
- [[harmonic-analysis]] — 接地谐波阻抗分析
- [[real-time-simulation]] — 接地系统实时仿真
- [[network-equivalent]] — 接地网等值
- [[lightning-transient-analysis]] — 雷电暂态分析
- [[insulation-coordination]] — 绝缘配合（接地系统设计依据）

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Alipio等 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model | 2023 | 传输线理论+Marti模型接地极建模，138kV线路案例，FDLine ATP实现 |
| Lima等 - Realization of rational models for tower-footing grounding systems | 2026 | FDNE有理逼近拓扑比较，有效长度对最小阶实现的影响 |
| De Araújo等 - Computation of ground potential rise and grounding impedance of simple arrangement of electrodes buried in frequency-dependent stratified soil | 2021 | 分层土壤GPR计算，频变土壤参数对接地阻抗的影响 |
| Meyberg等 - Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistance | 2026 | 动态土壤电离DLL实现，等位面壳层法嵌入EMTP |
| De Conti & Lima - Inclusion of Frequency-Dependent Soil Parameters in Transmission-Line Modeling | 2006 | 频变土壤参数对线路模型的影响（大地回路阻抗扩展） |
| Alipio等 - Influence of a lossy ground on the lightning performance of overhead transmission lines | 2023 | 有损大地对输电线路雷电性能的影响 |
---
title: "频变土壤模型 (Frequency-Dependent Soil Model)"
type: method
tags: [soil, grounding, frequency-dependent, resistivity, corrosion, polarization, alipio-visacro, carson, pollaczek, rational-model]
created: "2026-05-02"
updated: "2026-05-18"
---

# 频变土壤模型 (Frequency-Dependent Soil Model)

## 定义与边界

频变土壤模型是把土壤电导率 $\sigma$、电阻率 $\rho$ 或介电常数 $\varepsilon$ 写成频率相关函数，并将其作为线路大地返回、接地电极或电缆外部介质参数输入 EMT 的模型族。它更偏向"具体参数表达和实现形式"；频变土壤在 EMT 中的总边界已由保护页 [[frequency-dependent-soil]] 说明。

本页不处理土壤电离、击穿、热效应或接地网几何建模本身。若模型没有显式非线性机制，不能把它用于强雷电电流下的土壤电离结论。

## EMT 中的作用

频变土壤模型通常向下游模型提供：

- 复电导率 $\sigma^*(\omega) = \sigma(\omega) + j\omega\varepsilon(\omega)$ 或复电阻率 $\rho^*(\omega) = 1/\sigma^*(\omega)$；
- 大地返回阻抗计算所需的复穿透深度 $p(\omega)$ 或复介质参数；
- 接地电极、杆塔接地、电缆护套和线路地模传播的频域参数；
- 若进入时域 EMT，则提供有理函数、状态空间或递归卷积表示。

频变土壤的可信度取决于测量条件、拟合模型、频率范围、土壤空间均匀性和低频/高频极限是否合理。

## 核心数学表达

### 复电导率与复电阻率

频变土壤的核心入口是复电导率：

$$\sigma^*(\omega) = \sigma(\omega) + j\omega\varepsilon(\omega)$$

复电阻率为：

$$\rho^*(\omega) = \frac{1}{\sigma^*(\omega)}$$

在复返回平面或 Carson/Pollaczek 类地回路计算中，土壤参数会进入复穿透深度表达式：

$$p(\omega) = \frac{1}{\sqrt{j\omega\mu\left[\sigma(\omega) + j\omega\varepsilon(\omega)\right]}}$$

### 一阶幂律模型（de Lima & Portela 2007）

针对实测土壤样本，三参数一阶模型能以统计独立参数拟合宽频数据：

$$\sigma(\omega) = \sigma_0 + \alpha\omega^\beta$$

其中 $\sigma_0$ 为低频电导率，$\alpha$、$\beta$ 为频变系数。对巴西 8 个不同地质结构实测土壤样本的拟合优度 $R^2 > 0.98$（据 de Lima & Portela 2007）。

### Longmire/Smith 模型（LS 模型，Xue et al. 2020）

LS 模型通过 13 项弛豫型表达式拟合 100 Hz 至 4 MHz 频段土壤频变特性：

$$\sigma(f) = \sigma_{DC} + 2\pi\varepsilon_0\sum_{n=1}^{13} a_n F_n \frac{f^2}{1 + (f/F_n)^2}$$

$$\varepsilon_r(f) = \varepsilon_\infty + \sum_{n=1}^{13} \frac{a_n}{1 + (f/F_n)^2}$$

该模型与独立实测土壤数据吻合度最佳（Xue et al. 2020）。

### Alipio-Visacro 模型（Visacro & Alipio 2009）

针对雷电频段（10 kHz 至 10 MHz）的宽频土壤电导率模型：

$$\sigma(f) = \left[\sigma_0 + 1.26\sigma_0^{0.27}\left(\frac{f}{10^6}\right)^\gamma\right] \times 10^{-3} \quad \text{(S/m)}$$

$$\varepsilon_r(f) = \varepsilon_{r\infty} + \frac{1.26\times10^{-3}\tan\left(\frac{\pi\gamma}{2}\right)\sigma_0^{0.27}}{2\pi\varepsilon_0\cdot 10^6\gamma_{\text{av}}-1} \cdot \frac{1}{f^{0.73}}$$

其中 $\gamma_{\text{av}} = 0.54$ p.u.，$\varepsilon_{r\infty} = 12$（Xue et al. 2020 给出 AV 模型形式化表达）。

### Archie 模型（Azevedo et al. 2024）

考虑孔隙率和含水率的广义土壤电导率模型：

$$\sigma(W, \phi) = \sigma_{\text{dry}} + \left(\frac{\sigma_{\text{sat}} - \sigma_{\text{dry}}}{\phi^2} - \eta\right)W^2 + \eta\phi W$$

其中 $W$ 为含水率，$\phi$ 为孔隙率，$\eta$ 为经验系数。用于考察物理组成对土壤导电性的影响（Azevedo et al. 2024）。

### 时域等效：向量拟合与状态空间

若要在时域 EMT 中使用频变函数，常将频域响应拟合成有理函数：

$$F(s) \approx D + sE + \sum_{r=1}^{N}\frac{R_r}{s - p_r}$$

随后每个极点-留数项离散为状态变量或递归卷积项。此步骤需要检查稳定极点、因果性和 [[passivity-enforcement]]（de Lima & Portela 2007）。

## 模型类型对比

| 类型 | 表达对象 | 数学形式 | 适合用途 | 主要边界 |
|------|----------|----------|----------|----------|
| 常数土壤模型 | 单一 $\rho$ 或 $\sigma$ | $\sigma(\omega) = \sigma_0$ | 工频近似、初步参数扫描 | 宽频暂态可能严重低估阻抗高频衰减 |
| 幂律/一阶经验模型 | $\sigma(\omega)$ | $\sigma_0 + \alpha\omega^\beta$ | 少参数拟合和线路参数扫描 | 参数需由测量或文献约束 |
| Longmire/Smith (LS) | $\sigma(f)$、$\varepsilon_r(f)$ | 13 项弛豫和 | 地下电缆宽频传播、护套过电压 | 多参数辨识需实测数据 |
| Alipio-Visacro (AV) | $\sigma(f)$、$\varepsilon_r(f)$ | 雷电频段专用幂律 | 雷电暂态接地系统分析 | 仅验证于 10 kHz 至 10 MHz |
| Archie 孔隙模型 | $\sigma(W,\phi)$ | 含水率-孔隙率联立 | 高阻土壤、干燥沙土条件 | 不适用于饱和土壤或高频色散 |
| 分层土壤模型 | 各层厚度和复参数 | 积分方程或传递矩阵 | 接地网、地下电缆、地质分层 | 反演和积分计算复杂 |
| 有理函数模型 | 频域响应的时域实现 | 极点-留数展开 | EMT 状态空间/卷积接口 | 需稳定性和无源性验证 |

## EMT 建模方法

### 方法 1：复穿透深度 + 准模态法（Li et al. 2016）

**原理**：基于 Maxwell 方程完整推导的复穿透深度公式，将频变土壤参数代入复返回平面法，计算架空线路地回路自阻抗与互阻抗。

**自阻抗公式**：

$$Z_{ii} = j\omega\frac{\mu_0}{2\pi}\ln\frac{2(h_i + p)}{r}$$

**互阻抗公式**：

$$Z_{ij} = j\omega\frac{\mu_0}{2\pi}\ln\frac{\sqrt{(h_i + h_j + 2p)^2 + d_{ij}^2}}{\sqrt{(h_i - h_j)^2 + d_{ij}^2}}$$

其中 $p = 1/\sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$。

**关键发现**（Li et al. 2016）：
- 频变土壤与恒定参数模型的自阻差异主要集中于 **1 kHz 以上**频段
- 自感差异在 **1 MHz 以下**频段显著
- 50 Hz 恒定参数模型在全频段误差最大，**1 MHz 恒定参数**最逼近全频变计算结果

### 方法 2：扩展大地返回阻抗公式（de Lima & Portela 2007）

**原理**：将土壤复电导率 $\sigma + j\omega\varepsilon$ 整体替换 Carson（架空线）和 Pollaczek（电缆）大地返回阻抗公式中的 $\sigma$，并用 Gauss-Kronrod 数值积分求解无穷积分。

**扩展 Carson 型自阻抗**：

$$Z_{ii} = \frac{j\omega\mu_0}{2\pi}\ln\left(\frac{2h_i}{r_i}\right) + \frac{j\omega\mu_0}{\pi}\int_0^\infty \frac{e^{-2h_i\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0[\sigma(\omega) + j\omega\varepsilon(\omega)]}}\,d\lambda$$

**关键量化**（de Lima & Portela 2007）：
- 传统复平面近似法在高阻土壤（$\rho > 1000\;\Omega\cdot\text{m}$）下最大误差超过 **10%**
- Gauss-Kronrod 数值积分法将全频段（DC 至 2 MHz）阻抗计算误差控制在 **1.5% 以内**
- 地模传播常数在 100 kHz 至 1 MHz 频段实部增加约 **12.5%**，波速衰减显著

### 方法 3：塔脚传输线模型（Alipio et al. 2023）

**原理**：将杆塔接地系统（四根水平 Counterpoise 导线）等效为传输线，基于电报方程和 Marti 模型求解接地冲击阻抗时域响应。

**每单位长度参数方程**：

$$\frac{dV}{dx} = -Z_i - j\omega L I$$
$$\frac{dI}{dx} = -(G + j\omega C)V$$

其中 $Z_i$ 和 $L$ 分别为内阻抗和外部电感矩阵，$G$ 和 $C$ 为并联电导和电容矩阵。

**Sunde 接地电阻公式**（用于构建 $G$ 矩阵对角元）：

$$R_S = \frac{1}{\pi\sigma_g}\ln\frac{2l^2}{2hr} - 1$$

其中 $l$ 为总 Counterpoise 长度，$\sigma_g$ 为大地电导率，$h = 0.8\;\text{m}$ 为埋深，$r = 4.76\;\text{mm}$ 为导线半径。

**关键发现**：频变接地阻抗在雷电暂态中显著影响地电位升（GPR）幅值和波形，恒定电阻模型会低估接地系统的高频电位抬升。

### 方法 4：扩展传输线法（Xue et al. 2020）

**原理**：将 LS 频变土壤模型同时代入电缆串联阻抗矩阵 $Z$ 和并联导纳矩阵 $Y$（含大地返回导纳），通过模态分解得到传播常数。

**传播常数**：

$$\gamma = \sqrt{Z(\omega)Y(\omega)} = \alpha + j\beta$$

其中 $\alpha$ 为衰减常数，$\beta$ 为相位常数。

**量化边界**（Xue et al. 2020）：
- 在 $\rho_0 = 5000\;\Omega\cdot\text{m}$ 高阻土壤下，LS 模型与 CS（恒定土壤）模型的护套电压峰值偏差 $\delta$ 最大达 **11.1%**
- 电缆排列方式影响显著：水平排列偏差最大（11.1%），垂直排列次之（9.1%），三角形排列在极高阻下最小（4.7%）
- 短电缆（0.263 km）因富含高频分量，受频变土壤影响显著大于长电缆（1 km）
- 传统 Cable Constants 方法因忽略大地返回导纳，在高阻土壤下存在系统性偏差

### 方法 5：全波-EMT 联合仿真接口（Azevedo et al. 2024）

**原理**：利用矩量法（MoM）在 FEKO 中计算 100 Hz 至 10 MHz 频段接地谐波阻抗 $Z_h(j\omega)$，通过冲击阻抗 $Z_p = V_p/I_p$ 转换为 ATP 集中参数等效电路。

**地电位升计算**：

$$\text{GPR} = \mathcal{F}^{-1}\{I(j\omega) \times Z_h(j\omega)\}$$

**冲击阻抗**：

$$Z_p = \frac{\max[\text{GPR}]}{\max[i(t)]}$$

**关键量化**（Azevedo et al. 2024）：
- 高阻土壤（$\rho_0 = 5000\;\Omega\cdot\text{m}$）下 Portela 模型预测的 GPR 峰值较 FC 恒定土壤模型下降幅度最大
- SRS（后续回击）雷电流因波头更陡（$T_{10} = 0.50\;\mu\text{s}$），其 GPR 峰值约为 FRS（首次回击）的 **2 倍**
- 含水率 $W$ 从 1% 增至 25% 时，暂态电压峰值下降幅度可达 **30% 以上**
- 孔隙率 $\phi$ 每增加 10%，低频接地电阻 $R_{\text{LF}}$ 呈非线性上升

## 关键技术挑战

### 挑战 1：无穷积分的数值稳定性

Carson/Pollaczek 型大地返回阻抗公式含 $\int_0^\infty (\cdots)\,d\lambda$ 无穷积分。传统复平面近似法将 $\sigma + j\omega\varepsilon$ 近似为纯实部或仅保留一阶项，在高阻土壤（$\rho > 1000\;\Omega\cdot\text{m}$）下误差可达 10% 以上（de Lima & Portela 2007）。Gauss-Kronrod 数值积分可稳定求解，但计算量随频率点数增加。

### 挑战 2：多模态传播中的频变耦合

地下电缆中土壤参数同时进入串联阻抗矩阵 $Z$ 和并联导纳矩阵 $Y$。传统 Cable Constants 方法常忽略大地返回导纳中的 $\omega\varepsilon$ 项，导致模态衰减常数系统性低估。扩展传输线法通过完整 $Z$、$Y$ 矩阵解决了这一问题，但计算复杂度增加（Xue et al. 2020）。

### 挑战 3：土壤频变参数实测难度

土壤电导率和介电常数的宽频测量需要专用介电谱仪，且受温度（20°C 至 40°C）、湿度（1% 至 25%）和粒径等物理因素影响。不同土壤样本的频变曲线差异显著，难以建立通用参数库（Li et al. 2016）。

### 挑战 4：时域等效的稳定性与无源性

将有理函数模型或递归卷积嵌入 EMT 时域仿真时，若拟合极点位于右半平面或违反因果性，会导致数值发散。必须结合 [[passivity-enforcement]] 检查，确保等效电路在所有频率上无源。

### 挑战 5：分层土壤与各向异性

工程中土壤常存在水平分层或各向异性（深层高电阻率土壤 vs 浅层低电阻率土壤）。现有频变模型大多基于均匀半空间假设，分层土壤需要积分方程或传递矩阵方法，计算成本显著增加。

## 量化性能边界

| 场景 | 参数条件 | 关键指标 | 数值 |
|------|----------|----------|------|
| 高阻土壤阻抗计算精度 | $\rho_0 > 1000\;\Omega\cdot\text{m}$，DC~2 MHz | 数值积分法 vs 复平面近似误差 | 误差从 >10% 降至 <1.5% |
| 幂律模型拟合优度 | 8 个不同地质样本 | 三参数模型拟合 $R^2$ | $> 0.98$ |
| 地模传播常数偏移 | 100 kHz~1 MHz | 地模实部增加比例 | 约 12.5% |
| 地回路阻抗相位偏移 | 500 kHz，双回垂直线路 | 零序阻抗相位偏移 | 约 15° |
| 地下电缆护套电压偏差 | $\rho_0 = 5000\;\Omega\cdot\text{m}$，水平排列 | LS vs CS 峰值偏差 $\delta$ | 最大 11.1% |
| 接地阻抗降幅（雷电高频） | $\rho_0 = 5000\;\Omega\cdot\text{m}$，VP 模型 | 高频接地阻抗相对 FC 基准下降 | 约 13% |
| 雷电流 GPR 峰值倍率 | SRS vs FRS，$\rho_0 = 5000\;\Omega\cdot\text{m}$ | SRS GPR / FRS GPR | 约 2 倍 |
| 含水率对电压的影响 | $W: 1\% \to 25\%$ | 暂态电压峰值下降 | > 30% |

## 适用边界与选择指南

**选择恒定土壤模型**当：工频参数扫描、初步可行性评估、实时仿真步长约束严格。

**选择幂律模型（$\sigma_0 + \alpha\omega^\beta$）**当：需要宽频特性但参数来源有限，雷电和开关混合暂态分析，且有 3 个实测点可拟合。

**选择 LS 模型**当：地下电缆宽频传播分析、高阻土壤（$\rho_0 > 1000\;\Omega\cdot\text{m}$）、需要同时保留 $Z$ 和 $Y$ 矩阵完整性的场景。

**选择 AV 模型**当：专注于雷电高频（10 kHz 至 10 MHz）接地系统分析，已有 Visacro/Alipio 团队实测数据支持。

**选择 Archie 模型**当：分析含水率/孔隙率变化对干燥沙土接地特性的影响，或需要考察物理参数不确定性的敏感性分析。

**禁止将频变线性模型用于**：强雷电电流下的土壤电离（需要非线性电离模型）、分层土壤解析（需要积分方程或全波仿真）、热效应暂态分析（需要热耦合模型）。

## 相关页面

| 关联类型 | 页面 | 说明 |
|----------|------|------|
| 上游概念 | [[frequency-dependent-soil]] | 频变土壤保护页，总边界和 EMT 接口 |
| 大地返回阻抗 | [[earth-return-impedance]] | 使用土壤参数计算线路大地返回阻抗 |
| 传输线模型 | [[frequency-dependent-line-model]] | 频变参数进入线路模型的下游位置 |
| 通用线模型 | [[universal-line-model]] | ULM 行波模型中的土壤参数处理 |
| 接地系统 | [[grounding-system-modeling]] | 接地系统 EMT 建模方法 |
| 电缆建模 | [[cable-model]] | 电缆护套接地和外部介质应用 |
| 电缆埋设 | [[underground-cable-modeling]] | 地下电缆敷设条件下的土壤影响 |
| 向量拟合 | [[vector-fitting]] | 频域响应时域等效的核心工具 |
| 无源性强制 | [[passivity-enforcement]] | 有理函数模型的稳定性保障 |
| 传输线理论 | [[transmission-line-model]] | 线路建模整体框架 |

## 来源论文

- de Lima & Portela (2007) — 将频变 $\sigma$ 和 $\varepsilon$ 纳入 Carson/Pollaczek 公式，三参数幂律模型拟合 $R^2 > 0.98$，Gauss-Kronrod 数值积分法精度提升至 1.5% 以内
- Li et al. (2016) — 复穿透深度准模态法量化土壤频变对 500 kV 线路地回路参数的影响，50 Hz 恒定模型误差最大，1 MHz 恒定模型最逼近全频变结果
- Xue et al. (2020) — LS 模型与扩展传输线法结合，$\rho_0 = 5000\;\Omega\cdot\text{m}$ 时护套电压峰值偏差达 11.1%，电缆排列方式显著调制频变耦合效应
- Azevedo et al. (2024) — 全波 MoM + ATP 联合仿真，Portela 模型预测电压降幅最大，含水率 1%→25% 时暂态电压下降 >30%，SRS 雷击 GPR 峰值约为 FRS 的 2 倍
- Alipio et al. (2023) — 塔脚接地传输线模型 + Marti 模型，138 kV 线路算例验证，雷电暂态下地电位升和绝缘子串过电压受频变阻抗显著调制
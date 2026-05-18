---
title: "频率扫描 (Frequency Scan)"
type: method
tags: [frequency-scan, impedance, impedance-scan, dq-scan, csd-scan, gaussian-pulse, z-tool, small-signal]
created: "2026-05-02"
updated: "2026-05-11"
---

# 频率扫描 (Frequency Scan)

## 定义与边界

频率扫描是在给定运行点附近，对系统施加一个或多个频率的小幅扰动并提取响应，从而估计阻抗、导纳、传递函数或谐振特性的分析方法。在EMT仿真语境中，频率扫描的核心问题是：**如何用最少的仿真实验获取目标频段内足够精确的频率响应模型**。已形成至少四条不同方法论路线，在坐标系、注入信号、响应提取方式和输出形式上各有取舍：

1. **逐频点正弦注入+DFT提取**（传统方法，Jiang 2025, Meng 2023, Cifuentes 2025均基于此）：最直接，频点独立可调，但实验次数正比于频点数。
2. **多频正弦叠加注入**（Jiang 2025, Cifuentes 2025）：一次仿真覆盖多个频点，但需避免互调和幅值叠加过大。
3. **宽频脉冲激励+系统辨识**（Fan 2023）：用高斯脉冲替代逐频扫描，直接输出参数化传递函数模型，实验次数降为O(端口数)而非O(频点数)。
4. **自然扰动/运行波动识别**：利用系统固有波动估计频响，信噪比和可观测性受限。

本页关注方法流程和证据边界。频率扫描提供的是特定运行点、扰动幅值、模型和频率范围下的频响数据，稳定性判断还需结合阻抗比、Nyquist判据或时域EMT验证。

## EMT中的作用

EMT频率扫描常用于：

- **稳定性边界预测**：Jiang 2025通过dq0频扫预测电压源型VSG的CSCR=3.7、失稳振荡频率1.15 Hz，经EMT时域仿真和根轨迹交叉验证。
- **镜像频率效应识别**：Meng 2023在弱电网场景（SCR=1.02）中通过CSD-scan识别108 Hz主谐振和12 Hz镜像振荡，p-scan因忽略耦合误判为临界稳定（相位裕度1.7° vs 实际-0.5°）。
- **黑盒模型频域表征**：Cifuentes 2025的Z-tool支持多端AC/DC混合系统（含3×3导纳矩阵的HVDC换流器）的自动化扫描，无需打开控制器内部方程。
- **参数化小信号模型提取**：Fan 2023的高斯脉冲法从时域响应直接提取连续传递函数Ydq(s)，适用于后续仿真和稳定性分析。

## 常见分支

### 1. dq0坐标系多频正弦扫描（Jiang 2025 为代表）

在PSCAD/EMTDC中集成自动化频扫工具，在PCC注入多频正弦扰动（最多30个频点，幅值0.5%额定值），通过DFT提取响应并组装dq0阻抗矩阵。计算开环增益矩阵Z_MMC·Y_ac的特征值伯德图，由相位180°穿越点推导CSCR。

- **量化结果**：VSG型GFM的CSCR=3.7（根轨迹验证3.7-3.8），振荡频率1.15 Hz；CS-VSG在SCR≤100.0保持稳定
- **验证**：PSCAD/EMTDC，MMC（270 MVA, ±150 kV, 20 SMs/arm），根轨迹+EMT时域双层验证
- **局限**：仅限两类GFM控制，未覆盖多变流器网络和大扰动场景

### 2. 耦合序域MIMO扫描（CSD-scan, Meng 2023 为代表）

在静止坐标系中直接注入平衡三相正弦电压扰动（0.01 p.u.），通过DFT同步提取扰动频率f_i和镜像频率|f_i-2f_b|处的正负序电流响应，构建计及镜像频率效应的2×2 MIMO导纳矩阵。利用正负序导纳的频域共轭对称关系减少重复扫描。

- **量化结果**：CSD与dq-scan谐振频率一致（108 Hz），相位裕度偏差0.4°；p-scan高估2.2°误判稳定性；计算量较双扰动CSD法降低50%
- **参数**：扰动0.01 p.u.，DFT窗长1s，1-119 Hz步长1Hz，收敛容差1%
- **验证**：FSC风电场，SCR=1.02失稳场景；EMT时域复现108 Hz+12 Hz振荡
- **局限**：已验证弱电网FSC场景；依赖小扰动线性化，DFT窗长和扫频步长影响精度

### 3. 高斯脉冲激励+系统辨识（Fan 2023 为代表）

向IBR的d轴和q轴电压端口注入高斯脉冲（σ=0.01s, 0.05 p.u.），记录dq电流响应，使用MATLAB系统辨识工具箱的tfest函数（工具变量法）直接拟合为传递函数形式的2×2 dq导纳矩阵。

- **量化结果**：传统逐频扫频200次实验（1-100 Hz）→高斯脉冲法仅需2次轴向激励；σ=0.01s覆盖0.1-30 Hz；幅值超0.05 p.u.→验证匹配度降至8%
- **验证**：MATLAB/Simscape，Type-4风电机组；Chirp信号独立验证，频域响应与扫频高度一致
- **输出**：连续参数化传递函数Ydd(s), Ydq(s), Yqd(s), Yqq(s)，可直接用于稳定性分析和时域仿真
- **局限**：Type-4风机案例；30 Hz以上频段激励能量不足

### 4. 多端混合系统频域识别（Cifuentes 2025 Z-tool 为代表）

开源Python工具，以EMT仿真为数据源，对多端AC、DC及混合AC/DC系统进行频域识别。通过并联理想电压源解耦子系统，在多端端口处注入正弦扰动，FFT提取响应后按Y(jω)=ΔI·ΔV⁻¹构造导纳矩阵。

- **关键特征**：支持3×3 AC/DC导纳矩阵（HVDC换流器）；多频激励+对称性利用减少仿真次数；稳态快照减少重复启动成本
- **参数**：推荐扰动0.02%-2%额定值（电压控制模式<0.5%）；dq对称性可减少50%扰动次数
- **验证**：PSCAD/EMTDC，VSC串补线路（次同步振荡）、MMC-HVDC、基础元件
- **局限**：识别误差具有步长依赖性；扰动幅值和频段需用户根据目标系统调整

## 形式化表达

### 端口阻抗/导纳定义（单输入单输出）

$$$Z(\mathrm{j}\omega)=\frac{\Delta V(\mathrm{j}\omega)}{\Delta I(\mathrm{j}\omega)}, \quad Y(\mathrm{j}\omega) = Z(\mathrm{j}\omega)^{-1}$$$

### 多端口dq0阻抗矩阵（Jiang 2025）

通过三次独立d/q/0轴扰动组装响应矩阵求逆：

$$$\mathbf{Z}(\mathrm{j}\omega)=\mathbf{V}(\mathrm{j}\omega)\mathbf{I}(\mathrm{j}\omega)^{-1}$$$

闭环传递函数：

$$$\frac{\Delta V_{PCC}}{\Delta I_{Dis}} = \frac{Z_{MMC}}{1 + Z_{MMC} \cdot Y_{ac}}$$$

### CSCR推算（Jiang 2025）

$$$CSCR = \frac{SCR_{initial}}{|\lambda|_{180^\circ}}$$$

### CSD导纳矩阵（Meng 2023）

$$$Y_{IBR}^{CSD}(f_i) = \begin{bmatrix} Y_{IBR}^{p,p}(f_i) & Y_{IBR}^{p,n}(f_i) \\ Y_{IBR}^{n,p}(f_i) & Y_{IBR}^{n,n}(f_i) \end{bmatrix}$$$

频域共轭对称关系（减少扫描次数）：

$$$Y_{IBR}^{p,n}(f_i) = Y_{IBR}^{n,p*}(2f_b-f_i), \quad Y_{IBR}^{n,n}(f_i) = Y_{IBR}^{p,p*}(2f_b-f_i)$$$

### dq导纳传递函数模型（Fan 2023）

$$$\begin{bmatrix} i_d(s) \\ i_q(s) \end{bmatrix} = \begin{bmatrix} Y_{dd}(s) & Y_{dq}(s) \\ Y_{qd}(s) & Y_{qq}(s) \end{bmatrix} \begin{bmatrix} v_d(s) \\ v_q(s) \end{bmatrix}$$$

高斯脉冲激励：

$$$g(t) = \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{t^2}{2\sigma^2}}, \quad G(f) = e^{-\frac{1}{2}(2\pi\sigma f)^2}$$$

### 多端口导纳矩阵构造（Cifuentes 2025）

$$$Y(\mathrm{j}\omega) = \Delta I \cdot \Delta V^{-1}$$$

支持AC-d, AC-q, DC通道的混合多端口形式（如HVDC换流器的3×3导纳）。

## 与相关页面的关系

- [[impedance-measurement]]：更关注阻抗获取的具体测量系统实现，本页覆盖更一般的扫描策略和坐标选择。
- [[time-domain-impedance-estimation]]：Fan 2023的高斯脉冲法是其典型应用，用时域宽频扰动估计参数化阻抗模型。
- [[small-signal-stability]] 和 [[small-signal-stability-analysis]]：频扫数据进入稳定性判据的入口。Jiang 2025和Meng 2023分别展示了特征值伯德图和GNC的完整流程。
- [[harmonic-interaction]] 和 [[harmonic-transfer-coefficient]]：Meng 2023的镜像频率效应是频率耦合的典型案例。
- [[frequency-domain-analysis]]：频域建模和解释的主题入口。
- [[parameter-identification]]：Fan 2023的高斯脉冲+tfest方法将频扫问题转化为系统辨识问题。

## 代表性来源

| 来源 | 年份 | 方法类型 | 关键数值 | 验证方式 |
|------|------|----------|----------|----------|
| [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-|Jiang 2025]] | 2025 | dq0多频正弦+DFT+特征值伯德图 | CSCR=3.7, 1.15 Hz, 30频点, 0.5%幅值 | PSCAD+根轨迹+EMT时域 |
| [[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth|Meng 2023]] | 2023 | CSD-MIMO单频注入+镜像频率DFT | 108 Hz谐振, 0.4°相裕偏差, 50%计算节省 | EMT仿真+GNC+时域验证 |
| [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation|Fan 2023]] | 2023 | 高斯脉冲+系统辨识→参数化Ydq(s) | 200→2次实验, σ=0.01s覆盖30Hz, <0.05p.u. | MATLAB/Simscape+Chirp验证 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit|Cifuentes 2025]] | 2025 | 多端多频+FFT+导纳矩阵求逆 | 3×3 AC/DC导纳, 50%扰动减少(dq对称) | PSCAD+Python开源 |

## 证据边界

- **已验证系统**：MMC单机并网（Jiang 2025, 270 MVA）、FSC风电场弱电网（Meng 2023, SCR=1.02）、Type-4风电机组（Fan 2023）、VSC串补线路和MMC-HVDC（Cifuentes 2025）
- **已验证工具**：PSCAD/EMTDC（Jiang 2025, Cifuentes 2025）、MATLAB/Simscape（Fan 2023）
- **已验证频段**：0.1-30 Hz（Fan 2023）、1-119 Hz（Meng 2023）；其他方法频段取决于用户设置
- **未经验证**：多变流器网络交互、故障暂态、保护限流动作、不平衡工况、实时硬件平台、大扰动非线性稳定
- **量化谨慎**：CSCR=3.7和1.15 Hz来自Jiang 2025原文图表可核验部分；108 Hz谐振来自Meng 2023的弱电网算例；200→2次实验来自Fan 2023的方法对比；3×3导纳来自Cifuentes 2025的HVDC案例描述

## 开放问题

1. 四种方法路线（dq0多频、CSD、高斯脉冲+辨识、多端混合）在不同场景下的精度-效率对比缺乏系统研究。
2. 高斯脉冲法（Fan 2023）和Z-tool（Cifuentes 2025）的连续参数化输出能否统一到同一稳定性分析框架？
3. 镜像频率效应（Meng 2023）在多变流器系统中的传播和叠加效应尚待理论化。
4. 所有方法基于小扰动线性化假设；大扰动暂态过程中频扫的适用性和误差边界未有系统量化。
5. 频扫结果的不确定性量化（受DFT窗长、扰动幅值、步长、收敛判据影响）仍缺少标准方法。

## 量化性能边界

**Jiang 2025 dq0多频正弦扫描（PSCAD/EMTDC，MMC并网）**:
- 集成自动化频扫工具，PCC注入多频正弦扰动（最多30个频点，0.5%额定值）
- DFT提取响应并组装dq0阻抗矩阵，计算开环增益矩阵特征值伯德图
- 预测VSG型GFM的CSCR=3.7，振荡频率1.15 Hz
- 根轨迹验证CSCR范围3.7-3.8，EMT时域复现失稳振荡
- CS-VSG在SCR≤100.0保持稳定（无右半平面特征值）
- 验证平台：PSCAD/EMTDC，MMC 270 MVA/±150 kV/20 SMs
- 数据缺口：仅覆盖两类GFM控制，未验证多变流器网络和大扰动场景

**Meng 2023 CSD-MIMO序域频率扫描（FSC风电场弱电网）**:
- 静止坐标系注入平衡三相正弦扰动（0.01 p.u.），DFT提取扰动频率和镜像频率响应
- CSD与dq-scan谐振频率一致（108 Hz），相位裕度偏差仅0.4°
- p-scan忽略镜像频率耦合，相位裕度高估2.2°（1.7° vs 实际-0.5°），误判为临界稳定
- 计算量较双扰动CSD法降低50%（利用频域共轭对称关系）
- DFT窗长1s，1-119 Hz步长1Hz，收敛容差1%
- 验证：FSC风电场SCR=1.02失稳场景，EMT时域复现108 Hz+12 Hz振荡
- 数据缺口：已验证弱电网FSC场景；DFT窗长和扫频步长对精度的影响未系统量化

**Fan 2023 高斯脉冲激励+系统辨识（Type-4风电机组）**:
- 向IBR的d/q轴电压端口注入高斯脉冲（σ=0.01s, 0.05 p.u.），用tfest拟合传递函数
- 传统逐频扫频200次实验（1-100 Hz）→高斯脉冲法仅需2次轴向激励
- σ=0.01s覆盖0.1-30 Hz；幅值超0.05 p.u.时验证匹配度降至8%
- 输出连续参数化传递函数Ydd(s)/Ydq(s)/Yqd(s)/Yqq(s)
- Chirp信号独立验证，频域响应与逐频扫频高度一致
- 验证平台：MATLAB/Simscape
- 数据缺口：仅验证Type-4风机案例；30 Hz以上频段激励能量不足

**Cifuentes 2025 Z-tool多端混合系统频域识别（Python开源）**:
- 开源Python工具，以EMT仿真为数据源，支持多端AC/DC混合系统频域识别
- 多频正弦注入+FFT提取+Y(jω)=ΔI·ΔV⁻¹构造导纳矩阵
- 支持3×3 AC/DC导纳矩阵（HVDC换流器）；多频激励+对称性利用减少仿真次数
- 推荐扰动0.02%-2%额定值（电压控制模式<0.5%）；dq对称性减少50%扰动次数
- 稳态快照减少重复启动成本
- 验证：PSCAD/EMTDC，VSC串补线路（次同步振荡）、MMC-HVDC、基础元件
- 数据缺口：识别误差具有步长依赖性；扰动幅值和频段需用户根据目标系统调整；未支持实时硬件平台

**数据缺口声明**：四种频率扫描方法（dq0多频、CSD、高斯脉冲、多端混合）在不同场景下的精度-效率对比缺乏统一基准测试。所有方法基于小扰动线性化假设，大扰动暂态过程中频扫的适用性和误差边界未有系统量化。频扫结果的不确定性（受DFT窗长、扰动幅值、步长、收敛判据影响）仍缺少标准评估方法。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters W]] | 2021 |
| [[electromagnetic-transient-modeling-and-surge-analysis-of-overhead-power-lines-ab|Electromagnetic transient modeling and surge analysis of ove]] | 2025 |

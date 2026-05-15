---
title: "阻抗测量 (Impedance Measurement)"
type: method
tags: [impedance, measurement, frequency-scan, frequency-response, wideband, stability, black-box, passivity]
created: "2026-05-02"
updated: "2026-05-15"
---

# 阻抗测量 (Impedance Measurement)

## 定义

阻抗测量是通过端口电压和电流响应估计系统、设备或等效网络频率相关外部特性的过程。其核心定义是小扰动阻抗：

$$Z(j\omega)=\frac{\Delta V(j\omega)}{\Delta I(j\omega)}$$

对于两端口或多端口设备，更适合写成导纳矩阵形式：

$$
\begin{bmatrix}
\Delta I_1 \\
\Delta I_2
\end{bmatrix}
=
\begin{bmatrix}
Y_{11} & Y_{12} \\
Y_{21} & Y_{22}
\end{bmatrix}
\begin{bmatrix}
\Delta V_1 \\
\Delta V_2
\end{bmatrix}
$$

阻抗测量可以发生在多种环境中：现场测试、实验室测试、硬件在环（HIL/RTDS）测试，或 EMT 仿真中的虚拟扰动测量。本页关注测量方法、输入输出和失败边界，不等同于 [[frequency-scan]]——频率扫描是一种获取阻抗曲线的流程，阻抗测量还包括传感器、注入源、同步、噪声、端口定义、数据处理和黑盒设备识别等更广泛的问题。

## EMT 中的作用

阻抗测量在 EMT 知识体系中承担以下关键角色：

- 从详细开关模型、封装控制模型或现场数据中获取外部端口阻抗/导纳，实现**黑盒设备**的频域表征。
- 验证 [[vsc-model]]、[[mmc-model]]、[[lcc-model]]、[[frequency-dependent-line-model]] 等模型的频域行为是否与理论预期一致。
- 为阻抗比、Nyquist、特征值伯德图和谐振分析提供输入，支撑 [[small-signal-stability-analysis]]。
- 比较解析模型、平均模型、黑盒模型和测量重构模型之间的差异，评估建模误差。
- 为 [[vector-fitting]] 或宽频等值模型提供频率样本，确保拟合数据的测量精度和一致性。

## 核心机制

### 单端口阻抗定义

单端口小扰动阻抗的基本定义为端口电压扰动与电流扰动之比：

$$Z_{single}(j\omega) = \frac{\Delta V(j\omega)}{\Delta I(j\omega)}$$

其中 $\Delta V$ 和 $\Delta I$ 为稳态工作点附近的小扰动分量，需在注入频率处通过 DFT 或数值拉普拉斯变换从时域波形中提取。

### 多端口 MIMO 阻抗矩阵

对于多端口设备（如双绕组变压器、多端 DC-DC 变换器、三相并网变流器），阻抗/导纳矩阵的完整估计需要足够独立的端口激励：

$$\mathbf{I}(j\omega) = \mathbf{Y}(j\omega) \cdot \mathbf{V}(j\omega)$$

对 $M$ 端口系统，导纳矩阵为 $M \times M$，包含 $M^2$ 个独立元素。单次扰动通常只能提供部分方程——必须设计多次线性独立的注入，或用多频/多轴扰动构造可逆的响应矩阵。对于三相系统，需分别对 d、q、0 轴（或正/负/零序）施加扰动，形成完整的响应矩阵：

$$
\mathbf{Z}_{dq0} = \mathbf{V}_{dq0} \cdot \mathbf{I}_{dq0}^{-1}
$$

### 闭环稳定性判据

阻抗测量常用于源-荷阻抗比或闭环特征值分析。开环传递函数矩阵为：

$$\mathbf{L}(j\omega) = \mathbf{Z}_\text{source}(j\omega) \cdot \mathbf{Y}_\text{load}(j\omega)$$

系统稳定性由 $\mathbf{L}(j\omega)$ 的特征值轨迹判断。对于 $m$ 输入 $m$ 输出系统，有 $m$ 个特征值曲线。稳定性边界出现在特征值幅值为 1.0 且相位为 $180^\circ$ 处。增益裕度定义为：在特征值相位达到 $180^\circ$ 的频率处，幅值与 1.0 的比值。临界短路比（CSCR）由下式确定：

$$\text{CSCR} = \text{SCR}_\text{initial} \times \frac{1}{|\lambda_\text{max}|}$$

其中 $|\lambda_\text{max}|$ 为最接近单位圆的特征值幅值。

## 测量方法体系

### 方法一：单频注入法（Single-Frequency Injection）

**原理**：在稳态工作点注入单一频率正弦扰动（电压或电流），测量响应后通过 DFT 提取该频率点的阻抗幅相。

**流程**：
1. 系统运行至稳态
2. 注入单频扰动 $\Delta V = V_\text{inj} \sin(\omega t)$，典型幅值为额定值的 0.5%–1.0%
3. 等待瞬态衰减后，记录端口电压和电流波形
4. 应用 DFT 提取注入频率处的幅值和相位
5. 计算 $Z(j\omega) = \Delta V / \Delta I$

**特点**：实现简单，适合离线标定和仿真扫频。但逐频扫描时间长，运行点需保持稳定。

**公式**：
$$Z(j\omega_k) = \frac{|V(\omega_k)| \angle \theta_V}{|I(\omega_k)| \angle \theta_I} = \frac{|V(\omega_k)|}{|I(\omega_k)|} \angle (\theta_V - \theta_I)$$

### 方法二：多频注入法（Multi-Frequency Injection）

**原理**：在一次注入中叠加多个正弦频率成分（多正弦信号）、伪随机二进制序列（PRBS）或 Chirp 信号，通过单次 EMT 仿真同时获取宽频响应。

**多正弦注入**：
$$\Delta V(t) = \sum_{k=1}^{N} A_k \sin(\omega_k t + \phi_k)$$

其中 $N$ 为频点数，$A_k$ 为各频点幅值，$\phi_k$ 为随机相位以避免谐波对齐。典型 IBR 系统使用最多 30 个频点。

**PRBS 注入**：伪随机二进制序列具有白噪声频谱特性，可在宽频范围内均匀激发系统响应，适合在线候选方法。

**Chirp 注入**：频率随时间线性或非线性扫频的信号，适合快速获取宽频响应。

**特点**：一次注入覆盖宽频，效率高。但需检查互调失真、频谱泄漏和信噪比。

**数据处理**：对多频响应应用 DFT 后，在各注入频率处独立提取幅相，避免频谱泄漏需使用整周期窗函数（如 Hann 窗）：

$$W(\omega) = 0.5 \left(1 - \cos\frac{2\pi\omega}{\omega_s}\right)$$

### 方法三：耦合序域扫描法（CSD-Scan）

**原理**：在静止坐标系中直接注入平衡三相正弦扰动，通过 DFT 提取正序和负序镜像频率耦合响应，形成计及镜像频率效应（MFE）的 MIMO 阻抗模型。

**背景**：IBR 因 PLL 和 dq 轴控制不对称会产生镜像频率效应——正序频率扰动 $\omega$ 会在负序镜像频率 $2\omega_b - \omega$ 处产生响应。传统 p-scan（单序 SISO）忽略此耦合，可能误判稳定裕度；dq-scan 能计及耦合但需坐标变换且混合了谐振频率与镜像频率。

**CSD 导纳矩阵**：
$$
\mathbf{Y}_\text{CSD} =
\begin{bmatrix}
Y_\text{IBR}^{p,p} & Y_\text{IBR}^{p,n} \\
Y_\text{IBR}^{n,p} & Y_\text{IBR}^{n,n}
\end{bmatrix}
$$

其中对角线元素为同序自导纳，非对角线元素为镜像频率互导纳。各元素由下式计算：

$$Y_\text{IBR}^{p,p}(\omega_i) = \frac{|I^p(\omega_i)|}{|V^p(\omega_i)|} \angle (\angle I^p(\omega_i) - \angle V^p(\omega_i))$$

$$Y_\text{IBR}^{p,n}(\omega_i) = \frac{|I^n(\omega_i - 2\omega_b)|}{|V^p(\omega_i)|} \angle (\angle I^n(\omega_i - 2\omega_b) - \angle V^p(\omega_i))$$

**收敛判据**：
$$\left|\frac{\Delta Y_\text{IBR}^{j,k}(\omega_i)}{Y_\text{IBR}^{j,k}(\omega_i)}\right| < \text{tol} \quad \& \quad \left|\frac{\Delta \angle Y_\text{IBR}^{j,k}(\omega_i)}{\angle Y_\text{IBR}^{j,k}(\omega_i)}\right| < \text{tol}$$

其中 $j, k \in \{p, n\}$，tol 为收敛容差。

**优势**：
- 直接在三相相域操作，无需坐标变换
- 区分谐振频率与镜像频率
- 利用正负序导纳关于 $2\omega_b$ 的共轭对称关系减少扫描次数
- 计算负担约为 dq-scan 的一半（在 1 Hz 至两倍基频范围内）

**验证案例**：60 Hz 基频、833.5 MVA 基准、500 kV 系统，FSC 风电场弱网工况。CSD-scan 识别 108 Hz 谐振和 12 Hz 镜像振荡，与 dq-scan 一致；p-scan 因忽略 MFE 给出偏乐观相位裕度。

### 方法四：测量重构法（Measurement-Based Reconstruction）

**原理**：不假设内部拓扑已知，仅依赖端口测量数据重构宽频导纳矩阵。适用于黑盒设备。

**数值拉普拉斯变换**：
$$V_i^M(s) = \text{NLT}[v_i^M(t)], \quad I_i^M(s) = \text{NLT}[i_i^M(t)]$$

**两端口导纳重构**：对同一设备进行若干组不同源和负载条件下的端口测试，每次测试提供两条方程，组合多次测试后形成超定线性方程组，用最小范数最小二乘求解各频点处的导纳元素 $y_{11}, y_{12}, y_{21}, y_{22}$：

$$
\begin{bmatrix}
I_{i1}^M & 0 \\
0 & I_{o1}^M \\
I_{i2}^M & 0 \\
0 & I_{o2}^M
\end{bmatrix}
=
\begin{bmatrix}
V_{i1}^M & V_{o1}^M \\
V_{i1}^M & V_{o1}^M \\
V_{i2}^M & V_{o2}^M \\
V_{i2}^M & V_{o2}^M
\end{bmatrix}
\begin{bmatrix}
y_{11} \\ y_{12}
\end{bmatrix}
$$

**验证案例**：Buck 和 Boost DC-DC 变换器，测量重构模型相对 EMTP 基准开关仿真的误差低于约 1.4%，解析模型误差最高约 3%。

### 方法五：VNA 端口扫频法（Vector Network Analyzer）

**原理**：使用专用矢量网络分析仪（VNA）在变压器等设备端子上进行导纳频率扫描，获取宽频多端口导纳数据。

**测量流程**：
1. 在连接盒上施加电压于终端 $j$，其余终端接地
2. 测量终端 $i$ 的电流：$Y_{ij} = I_i / V_j$
3. 对每个端口重复，构建完整 $Y$ 矩阵
4. 对称化：$\mathbf{Y} \rightarrow \frac{1}{2}(\mathbf{Y} + \mathbf{Y}^T)$

**共模测量**：对于含未接地绕组的设备（如 HVDC 变压器），需额外进行共模测量以捕捉低频对地高阻抗耦合。将两个未接地绕组端子短接，形成三端子组件进行测量：

$$\mathbf{Y}_{3\times3} = f(\omega)$$

**特征值缩放**：小信号测量会给出非现实的 50 Hz 励磁电流。通过特征值缩放调整低频模态：
1. 对导纳矩阵进行特征值分解
2. 识别导致励磁电流过大的低频模态
3. 调整该模态大小，使端口等效励磁支路回到合理水平

**模态揭示变换**：在拟合前将大小相差很大的模态分量显式分离，避免与对地高阻抗耦合相关的小特征值被数值拟合误认为无关误差而丢失。

**验证案例**：法国—英国 IFA2000 HVDC 互联中的单相 HVDC 变压器（206 MVA, 400/√3 kV），五端口导纳模型，频率覆盖至数百 kHz。

### 方法六：离散阻抗建模法（Discretized Impedance-Based Modeling）

**原理**：将含滤波器和控制的 VSC 子系统写成拉普拉斯域导纳模型，再离散化为恒定阻抗矩阵加历史电压源，嵌入 SV 型 EMT 仿真器。

**梯形积分离散化**：
$$s \approx \frac{2}{\Delta t} \frac{z-1}{z+1}$$

**诺顿形式**：
$$i(t) = \mathbf{G} \cdot v(t) + \mathbf{h}(t)$$

其中 $\mathbf{G}$ 为恒定导纳矩阵，$\mathbf{h}(t)$ 汇集历史电压、电流、控制参考等贡献。

**戴维南形式**：
$$v(t) = \mathbf{Z} \cdot i(t) + \mathbf{e}(t), \quad \mathbf{Z} = \mathbf{G}^{-1}, \quad \mathbf{e}(t) = -\mathbf{G}^{-1}\mathbf{h}(t)$$

**验证案例**：七母线 VSC 互联系统（20 台 VSC），状态数从 271 降至 43；传统 AVM 最大稳定步长约 80 µs，DIBM 可运行至 1 ms；在 200 µs 步长下相对 1 µs 参考解误差小于 0.5%；实时单步计算性能最高约 4 倍提升。

## 不同坐标域中的扫描

阻抗扫描可在不同坐标域中实施：相域（abc）、序域（±/0 序）或 dq0 域。

### abc 相域

在相域中，阻抗矩阵 $\mathbf{Z}_{abc}$ 通常是非对角满阵。为捕获完整数据，需在三个不同相（a、b、c）分别施加独立注入：

$$
\mathbf{Z}_{abc} = \mathbf{V}_{abc} \cdot \mathbf{I}_{abc}^{-1}
$$

### dq0 域

在 dq0 域中，对 d、q、0 轴分别施加扰动。通常零序路径不存在或不受关注，可仅做两次注入：

$$
\mathbf{Z}_{dq0} = \mathbf{V}_{dq0} \cdot \mathbf{I}_{dq0}^{-1}
$$

EMT 仿真在相域执行，因此扰动需在 abc 域施加，测量后通过逆 Park 变换（$\mathbf{T}_{dq0}^{-1}$）或逆序变换（$\mathbf{T}_{+-0}^{-1}$）转换到 dq0 或序域进行 DFT 和阻抗计算。

### 频率耦合问题

功率电子系统的频率耦合是指：在一个频率的扰动会激发其他频率的响应。在 dq0 域中，平衡系统的扰动通常不会激发其他频率（频率耦合效应较弱），因此 dq0 扫描被广泛用于 IBR 系统。但在低阶谐波、不平衡或单相系统中，频率耦合显著，需使用相域或耦合序域方法。

## 数据处理与校核

测量得到的时域波形需要以下处理步骤：

1. **时间对齐**：对齐电压、电流通道时间戳和端口方向
2. **扰动分量提取**：去除稳态偏置或提取小扰动分量
3. **频域转换**：用 [[fft]]、[[fourier-filtering]]、数值拉普拉斯变换或相关法得到频域响应
4. **信噪比检查**：检查注入频点处的信噪比和非注入频点的互调分量
5. **矩阵条件数**：对矩阵阻抗检查条件数、非物理跳变和重复测试一致性
6. **无源性检查**：在用于 EMT 等值前检查有理拟合、稳定性和 [[passivity-enforcement]]

### 收敛判据

对于迭代式频扫，各导纳分量的幅值和相位变化需满足：

$$\left|\frac{\Delta |Y(\omega_i)|}{|Y(\omega_i)|}\right| < \text{tol}_\text{mag} \quad \& \quad \left|\frac{\Delta \angle Y(\omega_i)}{\angle Y(\omega_i)}\right| < \text{tol}_\text{phase}$$

典型容差设置为 $10^{-3}$（幅值）和 $10^{-2}$ rad（相位）。

## 稳定性分析中的使用边界

阻抗测量常服务于源-荷阻抗比或闭环特征值分析。开环传递函数：

$$\mathbf{L}(j\omega) = \mathbf{Z}_\text{source}(j\omega) \cdot \mathbf{Y}_\text{load}(j\omega)$$

之后可对 $\mathbf{L}$ 的特征值轨迹、Nyquist 包围或增益/相位裕度进行分析。该过程需要明确源/荷划分、坐标系、参考方向和运行点。

**关键边界**：
- 若系统存在强非线性、限流、保护动作或大扰动故障，阻抗测量只能解释小扰动邻域，不能替代 EMT 时域验证
- 阻抗依赖运行点、控制模式和外部网络，不能把一次测量曲线当作所有条件下的设备模型
- 扰动幅值过小会被噪声淹没，过大会触发非线性或控制限幅

## 关键技术挑战

### 挑战一：镜像频率效应（MFE）

IBR 因控制器不对称（PLL、dq 轴控制差异）会产生镜像频率耦合。正序频率 $\omega$ 的扰动会在负序镜像频率 $2\omega_b - \omega$ 处产生响应。忽略 MFE 的 p-scan 方法可能给出偏乐观的稳定裕度估计。

### 挑战二：未接地绕组与高阻抗耦合

含未接地绕组的设备（如 HVDC 变压器）在低频下对地呈现高阻抗，小特征模态容易被测量噪声和拟合过程淹没。需要共模测量和特征值缩放技术来正确表征低频行为。

### 挑战三：测量干扰

现场测量受邻近高压线路电磁干扰、传感器带宽限制、CT/VT 饱和、抗混叠滤波和同步误差影响。Gustavsen 2020 的 HVDC 变压器测量中，邻近 400 kV 交流线路的干扰导致低频数据噪声显著，需在 300 Hz 以下用理论电容性趋势替代实测数据。

### 挑战四：无源性保证

由测量数据拟合出的等效模型可能非无源，连接到 EMT 网络前应检查能量一致性。David Becerra 2023 提出同时对特征阻抗和传播函数残差施加扰动的方法，在相位域中实现最小扰动无源性保证。

### 挑战五：运行点依赖性

阻抗测量结果强烈依赖于稳态运行点。任何运行点变化（如功率指令变化、电网强度变化、控制模式切换）都需要重新扫描。Jiang 2026 通过 CSCR 分析量化了不同短路比下的稳定性边界变化。

## 量化性能边界

| 方法 | 频率范围 | 精度 | 计算效率 | 验证平台 | 数据来源 |
|------|----------|------|----------|----------|----------|
| CSD-scan | 1 Hz–2$f_b$ | 与 dq-scan 一致识别 108 Hz 谐振 | 比 dq-scan 快约 2 倍 | PSCAD/EMTDC | Meng 2023 |
| 多频注入 EMT | 宽频（≤30 频点） | 与根轨迹分析一致（CSCR 3.7 vs 3.7-3.8） | 自动化流程减少手动工作 | PSCAD/EMTDC | Jiang 2026 |
| 测量重构（DC-DC） | 宽频 | 相对 EMTP 基准误差 < 1.4% | 最小二乘求解约 1 分钟 | EMTP + MATLAB | Alameri 2023 |
| VNA 端口扫频 | DC–数百 kHz | 与白盒模型接近 | 测量约 5 天，拟合约 1 分钟 | VNA + 连接盒 | Gustavsen 2020 |
| DIBM（离散阻抗） | 固定步长 | 200 µs 步长误差 < 0.5% | 步长从 80 µs 提升至 1 ms，单步性能提升 4× | OPAL-RT | Vahabzadeh 2025 |
| DQ 阻抗（频变线路） | 宽频 | 与 OPAL-RT/ARTEMiS 和 PSCAD 结果一致 | 避免重复 EMT 仿真和 FFT | OPAL-RT + PSCAD | Hernández-Ramírez 2024 |

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 原因 |
|----------|----------|------|
| 黑盒 IBR 模型阻抗辨识 | CSD-scan 或 dq-scan | 无需内部控制器参数，静止坐标系实现简单 |
| 宽频 DC-DC 变换器建模 | 测量重构法 | 两端口导纳可直接与其他导纳型网络互联 |
| HVDC 变压器宽频建模 | VNA 端口扫频 + 特征值缩放 | 处理未接地绕组和高阻抗耦合 |
| SV 型 EMT 实时仿真 | DIBM（离散阻抗） | 恒定阻抗矩阵替代动态状态，步长提升 12.5 倍 |
| 含频变线路的 DQ 阻抗 | 谐波平衡 + Park 频移 | 避免集总参数近似，保留线路传播特性 |
| 弱电网稳定性筛查 | 多频注入 EMT + CSCR 分析 | 自动化流程，直接给出稳定裕度 |
| 在线监测 | 自然扰动法 | 利用背景波动，无需主动注入 |

## 相关方法 / 相关模型 / 相关主题

- [[frequency-scan]] 是阻抗测量的常见获取流程
- [[time-domain-impedance-estimation]] 关注用时域扰动和估计算法获得阻抗
- [[harmonic-interaction]] 使用阻抗结果解释谐波和控制网络耦合
- [[small-signal-stability-analysis]] 使用阻抗矩阵进行稳定性判断
- [[frequency-domain-analysis]] 提供频域解释框架
- [[vector-fitting]] 用于将离散频率响应拟合为有理函数模型
- [[passivity-enforcement]] 确保拟合模型的无源性
- [[fft]] 和 [[fourier-filtering]] 用于频域信号提取

## 来源论文

- **Jiang et al. 2026** "An EMT based dynamic frequency scanning tool for stability analysis of inverter based systems" — 提出 EMT 中通过扰动注入测量变流器/电网阻抗矩阵并用于稳定性分析的自动化工具，比较电压源型/电流源型 VSG 在不同 SCR 下的稳定性边界（CSCR 约 3.7，失稳频率约 1.15 Hz）。
- **Meng et al. 2023** "A new sequence domain EMT-level multi-input multi-output frequency scanning method for inverter based resources" — 提出静止坐标系 CSD-MIMO 频扫方法，计及镜像频率效应，区分谐振频率与镜像频率，计算负担比 dq-scan 减半。
- **Alameri & Gomez 2023** "Analytical and measurement-based wideband two-port modeling of DC-DC converters for electromagnetic transient studies" — 提出拉普拉斯域两端口导纳建模方法，测量重构法通过数值拉普拉斯变换从端口数据获得宽频模型，误差低于 1.4%。
- **Hernández-Ramírez et al. 2024** "Comprehensive DQ impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines" — 提出时频混合解析法，通过谐波平衡求精确稳态，直接获取含频变分布参数线路的 DQ 阻抗模型。
- **Gustavsen & Vernay 2020** "Measurement-based frequency-dependent model of a HVDC transformer for electromagnetic transient studies" — 首次将 VNA 端口测量黑盒建模用于 HVDC 变压器，提出共模测量、特征值缩放和模态揭示变换处理未接地绕组。
- **Vahabzadeh et al. 2025** "Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Simulators" — 提出离散阻抗接口方法，将 VSC 导纳模型离散化为恒定阻抗矩阵加历史电压源，状态数从 271 降至 43，步长从 80 µs 提升至 1 ms。

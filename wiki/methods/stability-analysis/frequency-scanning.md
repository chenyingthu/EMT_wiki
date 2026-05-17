---
title: "频率扫描法 (Frequency Scanning)"
type: method
tags: [frequency-scanning, harmonic-analysis, impedance-measurement, stability-analysis, resonance, small-signal, dq0-impedance]
created: "2026-05-04"
updated: "2026-05-17"
---

# 频率扫描法 (Frequency Scanning)

## 定义

频率扫描法（Frequency Scanning）是一种通过向电力系统注入特定频率的小信号扰动，并测量系统响应以获取其频域阻抗/导纳特性的实验或仿真分析方法。该方法的核心原理是：在系统稳态运行点上叠加频率可控的试探信号，通过测量端口电压与电流的幅值和相位关系，直接计算得到系统的宽频阻抗/导纳矩阵。

在 EMT 仿真环境中，频率扫描法通过在公共连接点（PCC）注入多频正弦扰动，利用离散傅里叶变换（DFT）提取各频率点下的阻抗响应。该方法可在不打开控制器黑盒的前提下，获取变流器或电网的宽频阻抗特性，广泛用于并网稳定性分析、谐振识别和阻尼评估。

## EMT中的角色

频率扫描法在 EMT 建模与分析体系中承担以下关键角色：

- **黑盒阻抗建模**：无需设备内部参数，基于端口测量建立宽频模型，特别适用于封装控制器或商业模型的等值
- **谐振频率识别**：精确定位电网与电力电子设备交互产生的谐振点，评估阻尼特性
- **稳定性裕度计算**：基于阻抗比的奈奎斯特或伯德图分析，预测系统的增益裕度和相位裕度
- **EMT模型频域验证**：将 EMT 时域仿真结果与频域阻抗测量对比，验证模型的宽频精度
- **临界短路比（CSCR）评估**：通过阻抗扫描特征值分析，预测IBR接入系统的临界短路比

### 核心挑战

1. **频率耦合效应**：电力电子装置在 abc 坐标系下存在正负序频率耦合，直接扫描得到的阻抗矩阵维度高且非对角元素显著
2. **非线性饱和**：大扰动导致设备进入非线性区域，小信号阻抗模型失效
3. **时变系统**：控制模式切换、温度漂移等导致阻抗随时变化

## 频率扫描方法体系

### 1. 单频点独立扫描

在每个频点独立注入单一频率正弦扰动，待系统达到稳态后测量响应：

$$Z(f_k) = \frac{V(f_k)}{I(f_k)}, \quad k = 1, 2, \ldots, N$$

**特点**：精度高，每次测量相互独立，无频率间耦合干扰；**缺点**：耗时长，N个频点需要N次独立仿真。

适用于关键频段的精细分析，或作为其他扫描方法的精度基准。

### 2. 多频同时扫描（PRBS伪随机）

注入包含多个频率分量的合成信号，通过 DFT 并行分解响应：

$$i(t) = \sum_{k=1}^{N} I_k \sin(2\pi f_k t + \phi_k)$$

或采用二进制伪随机序列（PRBS）激励，其自相关函数接近δ函数，频谱接近均匀分布：

$$u_{PRBS}(t) = \sum_{k=0}^{N-1} a_k \cdot u(t - k\tau), \quad a_k \in \{-1, +1\}$$

**特点**：效率高，一次仿真获取多频响应；**缺点**：频率间互调干扰可能导致测量误差。

### 3. 线性调频扫描（Chirp）

注入频率连续变化的啁啾信号：

$$f(t) = f_0 + \frac{f_1 - f_0}{T}t$$

**特点**：宽频带快速扫描，连续频谱无离散间隔；**缺点**：短时截断导致频谱泄漏，需加窗函数抑制旁瓣。

### 4. dq0坐标系扫描

为消除 abc 域频率耦合效应，在 dq0 旋转坐标系下进行扫描。通过 Park 变换将三相电压电流变换到 dq0 域：

$$\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix} = \frac{2}{3} \begin{bmatrix} \cos\theta & \cos(\theta-120^\circ) & \cos(\theta+120^\circ) \\ -\sin\theta & -\sin(\theta-120^\circ) & -\sin(\theta+120^\circ) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix} \begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

分别在 d 轴、q 轴、0 轴注入扰动，构建电压响应矩阵和电流响应矩阵，通过矩阵运算获取阻抗矩阵：

$$Z_{MMC}^{dq0}(f) = V_{PCC}^{dq0}(f) \cdot [I_{MMC}^{dq0}(f)]^{-1}$$

dq0 域扫描可使阻抗矩阵非对角元素（如 $Z_{d0}$、$Z_{q0}$）幅值极小，近似解耦为对角占优结构。

### 5. 序列域频率扫描

在正序/负序/零序坐标系下分别进行扫描，适用于不对称故障分析和多端直流系统：

$$Z_{seq}(f) = \frac{\Delta V_{seq}(f)}{\Delta I_{seq}(f)}$$

## 形式化表达

### 基本测量原理

在端口注入电流扰动 $\Delta I(f)$，测量电压响应 $\Delta V(f)$，阻抗定义为：

$$Z(f) = \frac{\Delta V(f)}{\Delta I(f)} = |Z(f)|e^{j\varphi(f)}$$

其中：
- $|Z(f)| = \frac{|\Delta V(f)|}{|\Delta I(f)|}$ 为阻抗幅值
- $\varphi(f) = \angle \Delta V(f) - \angle \Delta I(f)$ 为阻抗相角

### 谐振识别

谐振频率 $f_r$ 满足一阶导数为零、二阶导数小于零的条件：

$$\left.\frac{d|Z(f)|}{df}\right|_{f=f_r} = 0, \quad \left.\frac{d^2|Z(f)|}{df^2}\right|_{f=f_r} < 0$$

品质因数 $Q$ 与带宽 $\Delta f$ 的关系：

$$Q = \frac{f_r}{\Delta f} = \frac{f_r}{f_2 - f_1}$$

其中 $f_1, f_2$ 为半功率点频率（对应 $|Z(f)| = |Z(f_r)|/\sqrt{2}$）。

### 闭环系统传递函数

基于扫描得到的 MMC 阻抗与电网导纳，构建闭环系统传递函数：

$$\frac{\Delta V_{PCC}}{\Delta I_{Dis}} = \frac{Z_{MMC}}{1 + Z_{MMC} \cdot Y_{ac}}$$

计算开环增益矩阵 $Z_{MMC} Y_{ac}$ 的特征值 $\lambda_i(f)$，将多输入多输出稳定性问题转为各特征值轨迹的增益/相位裕度判断。

### 稳定性裕度

基于阻抗比 $T_m(f) = Z_{grid}(f) / Z_{device}(f)$ 的稳定性判据：

**幅值裕度**（Gain Margin）：

$$GM = -20\log_{10}|T_m(f_{\pi})| \quad \text{[dB]}$$

其中 $f_{\pi}$ 满足 $\angle T_m(f_{\pi}) = -180^\circ$。

**相位裕度**（Phase Margin）：

$$PM = 180^\circ + \angle T_m(f_c) \quad \text{[\circ]}$$

其中 $f_c$ 满足 $|T_m(f_c)| = 1$（0 dB）。

### 临界短路比（CSCR）

通过伯德图中特征值相位穿越 $180^\circ$ 时的幅值反推临界短路比：

$$CSCR = \frac{SCR_{initial}}{|\lambda|_{180^\circ}}$$

当 $|\lambda|_{180^\circ} = 1$ 时，系统处于失稳边界。

## 关键技术挑战

### 挑战1：频率耦合效应

电力电子装置在 abc 坐标系下存在固有的频率耦合——注入某一频率的扰动会在其他频率产生响应（尤其在 dq 坐标变换后表现为阻抗矩阵非对角元素）。**解决方案**：采用 dq0 坐标系扫描，通过坐标变换消除频率耦合影响，使阻抗矩阵近似解耦。对于高度耦合系统，可采用 MIMO 阻抗矩阵测量方法（分别注入 d、q、0 轴扰动）。

### 挑战2：频谱泄漏与频率分辨率

Chirp 信号的短时截断和非整数周期采样会导致频谱泄漏，使谐振峰估值偏差。**解决方案**：加汉宁窗或汉明窗抑制旁瓣；选择足够长的观测窗口 $T_{obs} \gg 1/\Delta f$ 以提高频率分辨率。

### 挑战3：非线性饱和与互调干扰

多频同时注入时，各频率分量间会产生互调干扰（Intermodulation），特别在大扰动幅值时更显著。**解决方案**：扰动幅值控制在额定值的 0.5% 以内保证线性度；采用 PRBS 代替多频叠加信号，利用其低互调特性。

### 挑战4：时变系统阻抗跟踪

IBR 控制模式切换（如 LVRT）、温度变化和太阳辐照波动导致阻抗随时变化，单次扫描结果不能代表全工况。**解决方案**：研发实时/准实时阻抗跟踪算法，结合递推最小二乘法（RLS）或卡尔曼滤波在线更新阻抗模型。

### 挑战5：大规模系统分布式扫描

大规模多端直流系统中，集中在单一 PCC 端口的扫描无法覆盖全网模态。**解决方案**：基于区域分解的分布式并行频率扫描——各子区域独立注入扰动，通过接口等值模型拼接全局阻抗矩阵。

## 量化性能边界

| 指标 | 典型数值 | 数据来源 |
|------|---------|---------|
| 电压源型 VSG 临界短路比（CSCR） | 3.7 | Jiang 2025（PSCAD/EMTDC+MMC 270MVA） |
| 电压源型 VSG 失稳振荡频率 | 1.15 Hz | Jiang 2025（根轨迹法对比） |
| 电流源型 VSG 稳定 SCR 上限 | ≥100（强网） | Jiang 2025 |
| 频率扫描点数（多频注入） | 最多30点 | Jiang 2025 |
| 扰动幅值（线性度要求） | <0.5%额定值 | Jiang 2025 |
| 阻抗测量信噪比要求 | >40 dB | 工程经验 |
| 频率分辨率要求 | $\Delta f < f_r/Q$ | 工程经验 |

## 适用边界与选择指南

| 扫描方法 | 适用场景 | 优点 | 缺点 |
|---------|---------|------|------|
| 单频点扫描 | 关键频段精细分析、基准验证 | 精度高、无互调 | 耗时长 |
| 多频同时扫描 | 宽频快速扫描、在线监测 | 效率高 | 频率耦合 |
| Chirp 扫描 | 宽频带快速扫描 | 连续频谱 | 频谱泄漏 |
| dq0 扫描 | 并网变流器阻抗提取 | 消除耦合 | 需坐标变换 |
| 序列域扫描 | 不对称故障、多端DC系统 | 解耦正负序 | 设备复杂 |

## 来源论文

- Jiang 等 - 2025 - An EMT based dynamic frequency scanning tool for stability analysis of inverter based systems（Electric Power Systems Research）
- Dey 等 - 2021 - Comparison of dynamic phasor, discrete-time and frequency scanning based SSR models of a TCSC（IEEE TPWRD）
- Meng 等 - 2023 - A new sequence domain EMT-level multi-input multi-output frequency scanning method for inverter base（IEEE TPEL）
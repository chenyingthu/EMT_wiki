---
title: "Prony 分析 (Prony Analysis)"
type: method
tags: [prony, signal-processing, modal-analysis, system-identification]
created: "2026-04-14"
---

# Prony 分析 (Prony Analysis)

## 概述

Prony分析是一种基于指数信号分解的系统辨识方法，在电力系统EMT仿真中用于从暂态响应数据中提取模态参数（频率、阻尼、幅值）。与矢量拟合类似，Prony分析也是从时域或频域数据中提取系统模型的重要工具。

## 基本原理

- 将信号表示为复指数函数的线性组合
- 通过求解线性方程组提取极点和留数
- 适用于线性时不变系统辨识
- 可从EMT仿真结果中提取系统等效模型

## 应用场景

- 电力系统振荡模态分析
- 传输线参数辨识
- 同步电机参数估计
- 电力系统稳定性分析
- 暂态响应特征提取

## 与矢量拟合的比较

| 特性 | Prony分析 | 矢量拟合 |
|------|-----------|----------|
| 输入数据 | 时域响应 | 频域响应 |
| 应用领域 | 模态分析 | 频变网络等值 |
| 数值稳定性 | 中等 | 较高 |
| 适用频率 | 低频振荡 | 宽频范围 |

## 定义与边界

Prony 分析在本 wiki 中指从时域暂态序列中辨识指数模态、极点和留数的方法，常服务于 [[network-equivalent|网络等值]]、振荡模态分析和 EMT 波形后处理。它与 [[vector-fitting|矢量拟合]] 的边界在输入数据：Prony 更依赖时域窗口和采样质量，VF 更依赖频域采样和初始极点。

Prony 适合线性或近似线性响应、短时模态提取和等值模型初步构造。对强非线性、时变拓扑、噪声较高或窗口不足的数据，辨识出的弱阻尼模态可能是数值伪模态；用于 EMT 时域等值前仍需检查 [[passivity-enforcement|无源性]] 和 [[state-space-method|状态空间]] 实现稳定性。

## 代表性来源与内部链接

代表性来源包括 [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A time-domain approach to transmission network equivalents via Prony analysis]]、[[dynamic-synchrophasor-estimator-based-on-multi-frequency-phasor-model|Dynamic synchrophasor estimator based on multi-frequency phasor model]] 和 [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency-scanning based SSR models]]。相关入口包括 [[frequency-dependent-modeling|频率相关建模]]、[[harmonic-analysis|谐波分析]] 和 [[co-simulation|协同仿真]]。

## 相关方法
- [[vector-fitting]]
- [[state-space-method]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[network-equivalent]]

## 深度增强内容

 ## 1. 核心原理详解

Prony分析基于Gaspard de Prony于1795年提出的指数信号分解理论，在电力系统EMT仿真中，其核心思想是将网络 impulse response $h(t)$ 或端口电压/电流响应表示为衰减指数函数的线性组合：

$$h(t) \approx \sum_{i=1}^{n} R_i e^{\lambda_i t}, \quad t \geq 0$$

其中 $\lambda_i = \sigma_i \pm j\omega_i$ 为系统极点（复频率），$R_i$ 为对应留数，$n$ 为模型阶数。

### 1.1 离散时域建模

对于EMT仿真中的离散采样序列 $h[k] = h(k\Delta t)$，$\Delta t$ 为采样间隔，上述连续模型转化为：

$$h[k] = \sum_{i=1}^{n} R_i z_i^k, \quad k = 0, 1, \dots, N-1$$

其中 $z_i = e^{\lambda_i \Delta t} = e^{\sigma_i \Delta t} \cdot e^{\pm j\omega_i \Delta t}$ 为离散极点，满足 $|z_i| < 1$（稳定系统）。

### 1.2 线性预测模型（LPM）

Prony方法的关键在于利用线性预测关系构建特征多项式。假设系统满足 $n$ 阶差分方程：

$$h[k] + a_1 h[k-1] + \dots + a_n h[k-n] = 0, \quad k = n, \dots, N-1$$

系数 $\{a_i\}$ 与极点 $\{z_i\}$ 通过特征多项式关联：

$$1 + a_1 z^{-1} + \dots + a_n z^{-n} = \prod_{i=1}^{n} (1 - z_i z^{-1}) = 0$$

### 1.3 矩阵构造与SVD降阶

构建 $(N-n) \times n$ 的Hankel矩阵 $\mathbf{H}$：

$$\mathbf{H} = \begin{bmatrix} 
h[0] & h[1] & \cdots & h[n-1] \\
h[1] & h[2] & \cdots & h[n] \\
\vdots & \vdots & \ddots & \vdots \\
h[N-n-1] & h[N-n] & \cdots & h[N-2]
\end{bmatrix}$$

通过奇异值分解（SVD）$\mathbf{H} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$，利用论文中提到的阈值截断策略，保留显著奇异值 $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n \geq \epsilon$，实现从初始高阶模型向有效阶数 $n_{\text{eff}} = 70$ 的降阶。

### 1.4 戴维南等效电路合成

基于提取的极点和留数，驱动点阻抗 $Z(s)$ 的部分分式展开为：

$$Z(s) = \sum_{i=1}^{n} \frac{R_i}{s - \lambda_i} + \frac{R_i^*}{s - \lambda_i^*}$$

对于共轭复极点对，可转换为RLC并联支路形式直接嵌入EMTP仿真：

$$Z_i(s) = \frac{2\sigma_i |R_i| \cos\theta_i - 2\omega_i |R_i| \sin\theta_i}{(s-\sigma_i)^2 + \omega_i^2}$$

其中 $\theta_i = \arg(R_i)$，对应离散时间滤波器实现为：

$$H(z) = \sum_{i=1}^{n} \frac{r_i}{1 - p_i z^{-1}}, \quad p_i = e^{\lambda_i \Delta t}, \quad r_i = R_i \frac{1 - p_i}{\lambda_i}$$

## 2. 算法流程

**步骤1：数据预处理与特征提取**
- 对EMT仿真获得的时域脉冲响应 $h(t)$ 进行采样，采样频率 $f_s = 1/\Delta t \geq 10 f_{\text{max}}$（论文中 $\Delta t = 1.0\times 10^{-4}\,\text{s}$ 对应 $f_s = 10\,\text{kHz}$）
- 去除直流分量与趋势项，必要时加窗抑制频谱泄漏

**步骤2：Hankel矩阵构建与SVD分析**
- 选择初始过定阶数 $L \gg n$（通常 $L = N/2$），构建扩展Hankel矩阵 $\mathbf{H}_{(N-L)\times L}$
- 执行SVD分解：$\mathbf{H} = \sum_{i=1}^{r} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$
- 根据奇异值能量累积准则确定有效阶数：$n = \min\left\{k \,\big|\, \sum_{i=1}^{k} \sigma_i^2 / \sum_{i=1}^{r} \sigma_i^2 \geq 0.999\right\}$

**步骤3：线性预测系数求解**
- 利用截断后的奇异值构造降阶矩阵 $\mathbf{H}_n = \mathbf{U}_n \mathbf{\Sigma}_n \mathbf{V}_n^T$
- 求解线性预测系数：$\mathbf{a} = -\mathbf{V}_n \mathbf{\Sigma}_n^{-1} \mathbf{U}_n^T \mathbf{h}_{\text{tail}}$，其中 $\mathbf{h}_{\text{tail}} = [h[L], \dots, h[N-1]]^T$

**步骤4：极点提取**
- 求解特征多项式根：$z^n + a_1 z^{n-1} + \dots + a_n = 0$
- 转换至s域：$\lambda_i = \frac{\ln(z_i)}{\Delta t} = \sigma_i \pm j\omega_i$
- 剔除不稳定极点（$\text{Re}(\lambda_i) > 0$）与虚假高频模态（$|\omega_i| > \pi/\Delta t$）

**步骤5：留数计算（最小二乘）**
构建Vandermonde矩阵 $\mathbf{Z}$（元素 $Z_{ki} = z_i^{k}$），通过最小二乘求解：

$$\mathbf{R} = (\mathbf{Z}^H \mathbf{Z})^{-1} \mathbf{Z}^H \mathbf{h}$$

其中 $\mathbf{h} = [h[0], \dots, h[N-1]]^T$。

**步骤6：模型验证与等效电路生成**
- 计算拟合误差：$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{k=0}^{N-1} |h[k] - \hat{h}[k]|^2}$（论文目标 $< 10^{-3}$）
- 将复共轭对组合为二阶-section：$H_i(z) = \frac{b_{i0} + b_{i1}z^{-1}}{1 + a_{i1}z^{-1} + a_{i2}z^{-2}}$
- 生成EMTP可识别的有理函数模型或等效电路网表

## 3. 参数选取指南

| 参数 | 典型范围 | 选取策略 | 注意事项 |
|------|----------|----------|----------|
| **采样步长 $\Delta t$** | $10^{-6} \sim 10^{-3}\,\text{s}$ | 满足奈奎斯特准则：$\Delta t \leq \frac{1}{2f_{\text{max}}}$ | 论文中 $10^{-4}\,\text{s}$ 可覆盖0-5kHz，需权衡高频精度与计算量 |
| **模型阶数 $n$** | 20~200 | 初始高阶（150~200）→ SVD降阶至有效模态数 | 过拟合会引入虚假模态，欠拟合丢失弱阻尼振荡 |
| **SVD阈值 $\epsilon$** | $10^{-6} \sim 10^{-3}$ | 相对阈值：$\sigma_i / \sigma_{\text{max}} < \epsilon$ 截断 | 论文通过剔除近零留数模态将模型降至70阶 |
| **观测窗口 $T_{\text{obs}}$** | $5\tau_{\text{max}} \sim 10\tau_{\text{max}}$ | 覆盖最慢衰减模态的5~10倍时间常数 | 窗口过短导致低频辨识不准，过长引入数值误差 |
| **信噪比 SNR** | $> 40\,\text{dB}$ | 预处理加低通滤波或采用总体最小二乘(TLS) | EMT仿真数据通常信噪比较高，实测数据需特别注意 |

**特殊场景策略：**
- **高频谐振分析（>1kHz）**：减小 $\Delta t$ 至 $10^{-5}\,\text{s}$ 量级，增加模型阶数至100以上以捕捉密集模态
- **弱阻尼低频振荡**：延长观测窗口至20s以上，采用协方差法替代自相关法抑制噪声
- **多端口网络**：对每个端口独立进行Prony分析，检查留数矩阵的秩确保端口间耦合正确表征

## 4. 性能分析

基于文献[1]的量化评估数据：

| 性能指标 | 数值 | 说明 |
|----------|------|------|
| **模型辨识精度** | RMSE $\approx 4.36 \times 10^{-4}$ | 时域脉冲响应拟合误差，证明Prony方法在宽频带阻抗辨识中的高精度 |
| **模型降阶比率** | 约70%（降至70阶） | 从初始高阶模型通过SVD截断保留主导模态，剔除近零留数模态 |
| **计算效率提升** | 37倍 | 等值模型仿真时间0.53s vs 全系统19.8s，占比2.68% |
| **有效频带范围** | 0~5 kHz | 在 $10^{-4}\,\text{s}$ 采样步长下精确复现驱动点阻抗特性 |
| **数值稳定性** | 高 | 基于SVD的降阶处理有效抑制了传统Prony方法的条件数敏感问题 |

**综合评估：**
Prony分析在输电网络等值应用中展现出优异的精度-效率权衡。相较于频域矢量拟合的迭代过程，时域Prony方法通过单次脉冲响应分析即可生成宽频等效模型，特别适合EMT仿真中需要频繁更新网络拓扑的场景。

## 5. 最佳实践与注意事项

### 5.1 数据预处理关键
- **去除非零初始条件**：EMT仿真中开关操作可能导致初始偏移，需通过去趋势或差分处理消除直流分量，避免虚假零频模态
- **抗混叠滤波**：严格遵循采样定理，在降采样前使用模拟或数字抗混叠滤波器
- **信噪比增强**：对于含噪声的实测数据，采用多次平均或自适应Prony方法（Adaptive Prony）提高鲁棒性

### 5.2 数值稳定性保障
- **缩放处理**：对采样数据进行归一化 $h_{\text{norm}}[k] = h[k]/\max|h[k]|$，防止Hankel矩阵元素数量级差异过大
- **QR分解替代**：对于病态严重的矩阵，使用QR分解结合列主元消去求解线性预测系数，替代直接求逆
- **极点筛选**：自动剔除 $|z_i| > 1$ 的不稳定极点及 $|\text{Im}(\lambda_i)| > \pi/\Delta t$ 的混叠伪极点

### 5.3 与EMTP接口优化
- **无源性强制**：若等效模型用于实时仿真，需检查 $Z(s)$ 正实性，必要时对留数进行扰动修正保证无源
- **时延补偿**：对于长距离传输线，提取的模型应包含时延项 $e^{-s\tau}$，避免纯集总参数模型在高频段出现非物理振荡
- **分段线性化**：针对非线性元件（如避雷器、饱和变压器），建议在工作点邻域分段应用Prony分析，生成多个线性等效模型切换使用

### 5.4 常见失效模式
- **密集模态**：当系统存在密集特征值（如电缆-架空线混合网络），传统Prony可能混淆相近频率，建议采用矩阵束方法（Matrix Pencil）替代
- **非线性失真**：严格限定于小信号分析，大扰动下（如短路故障）需结合分段线性化或混合仿真框架

## 6. 与其他方法的对比

| 特性 | Prony分析 | 矢量拟合 (VF) | 特征系统实现 (ERA) | 傅里叶分析 (DFT) | 小波分析 (WT) |
|------|-----------|---------------|-------------------|------------------|---------------|
| **输入数据** | 时域脉冲/阶跃响应 | 频域采样点 ($s=j\omega$) | 时域脉冲响应 | 时域周期信号 | 时域非平稳信号 |
| **数学基础** | 指数拟合/自回归 | 有理函数最小二乘 | Hankel矩阵实现理论 | 正交基展开 | 多分辨率分析 |
| **模态提取** | 直接提取极点/留数 | 迭代优化极点位置 | 平衡截断降阶 | 仅频率信息 | 时频局部化 |
| **阻尼辨识** | 精确（直接得 $\sigma_i$） | 精确 | 精确 | 需曲线拟合 | 近似 |
| **计算复杂度** | $O(Nn^2)$ + SVD | $O(N_{\text{iter}} N n)$ | $O(N^3)$（全阶） | $O(N\log N)$ | $O(N)$ |
| **宽频适用性** | 优秀（0-5kHz验证） | 优秀（适合超高频） | 良好 | 受窗口限制 | 依赖小波基选择 |
| **噪声鲁棒性** | 中等（需SVD截断） | 高 | 高 | 低 | 中等 |
| **EMT集成** | 直接生成离散滤波器 | 需双线性变换离散化 | 需状态空间实现 | 不直接适用 | 需专用硬件 |
| **实时仿真支持** | 优秀（固定系数IIR） | 良好 | 复杂（状态矩阵稀疏化） | 不适用 | 计算密集 |

**方法选择建议：**
- **离线高精度等值**：Prony分析与矢量拟合均可，Prony在时域仿真数据直接处理上更便捷
- **在线参数辨识**：优先选择ERA或改进型Prony（加窗递归实现）
- **非平稳振荡**：采用小波-Prony混合方法，先用小波提取时段特征，再用Prony细化模态参数
- **超大规模系统**：结合Prony与模型降阶技术（如模态级数法），先分区Prony分析再联立求解

**发展趋势：**
当前研究正朝着**稀疏Prony**（压缩感知理论引入，减少采样点需求）和**分布式Prony**（并行处理多端口网络）方向发展，以应对含高比例电力电子接口电源的复杂电网宽频建模需求。

## 深度增强内容

 ## 1. 核心原理详解

Prony分析基于Gaspard de Prony于1795年提出的指数信号分解理论，在电力系统EMT仿真中，其核心思想是将网络 impulse response $h(t)$ 或端口电压/电流响应表示为衰减指数函数的线性组合：

$$h(t) \approx \sum_{i=1}^{n} R_i e^{\lambda_i t}, \quad t \geq 0$$

其中 $\lambda_i = \sigma_i \pm j\omega_i$ 为系统极点（复频率），$R_i$ 为对应留数，$n$ 为模型阶数。

### 1.1 离散时域建模

对于EMT仿真中的离散采样序列 $h[k] = h(k\Delta t)$，$\Delta t$ 为采样间隔，上述连续模型转化为：

$$h[k] = \sum_{i=1}^{n} R_i z_i^k, \quad k = 0, 1, \dots, N-1$$

其中 $z_i = e^{\lambda_i \Delta t} = e^{\sigma_i \Delta t} \cdot e^{\pm j\omega_i \Delta t}$ 为离散极点，满足 $|z_i| < 1$（稳定系统）。

### 1.2 线性预测模型（LPM）

Prony方法的关键在于利用线性预测关系构建特征多项式。假设系统满足 $n$ 阶差分方程：

$$h[k] + a_1 h[k-1] + \dots + a_n h[k-n] = 0, \quad k = n, \dots, N-1$$

系数 $\{a_i\}$ 与极点 $\{z_i\}$ 通过特征多项式关联：

$$1 + a_1 z^{-1} + \dots + a_n z^{-n} = \prod_{i=1}^{n} (1 - z_i z^{-1}) = 0$$

### 1.3 矩阵构造与SVD降阶

构建 $(N-n) \times n$ 的Hankel矩阵 $\mathbf{H}$：

$$\mathbf{H} = \begin{bmatrix} 
h[0] & h[1] & \cdots & h[n-1] \\
h[1] & h[2] & \cdots & h[n] \\
\vdots & \vdots & \ddots & \vdots \\
h[N-n-1] & h[N-n] & \cdots & h[N-2]
\end{bmatrix}$$

通过奇异值分解（SVD）$\mathbf{H} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$，利用论文中提到的阈值截断策略，保留显著奇异值 $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n \geq \epsilon$，实现从初始高阶模型向有效阶数 $n_{\text{eff}} = 70$ 的降阶。

### 1.4 戴维南等效电路合成

基于提取的极点和留数，驱动点阻抗 $Z(s)$ 的部分分式展开为：

$$Z(s) = \sum_{i=1}^{n} \frac{R_i}{s - \lambda_i} + \frac{R_i^*}{s - \lambda_i^*}$$

对于共轭复极点对，可转换为RLC并联支路形式直接嵌入EMTP仿真：

$$Z_i(s) = \frac{2\sigma_i |R_i| \cos\theta_i - 2\omega_i |R_i| \sin\theta_i}{(s-\sigma_i)^2 + \omega_i^2}$$

其中 $\theta_i = \arg(R_i)$，对应离散时间滤波器实现为：

$$H(z) = \sum_{i=1}^{n} \frac{r_i}{1 - p_i z^{-1}}, \quad p_i = e^{\lambda_i \Delta t}, \quad r_i = R_i \frac{1 - p_i}{\lambda_i}$$

### 1.5 EMTP中的数值实现

在EMTP-type程序中，上述离散传递函数通过伴随电路模型实现。对于每个一阶子系统：

$$H_i(z) = \frac{r_i}{1 - p_i z^{-1}}$$

对应的时域递推关系为：

$$y[k] = p_i y[k-1] + r_i u[k]$$

其等效电阻 $R_{\text{eq}} = \frac{\Delta t}{2C} + R$（取决于具体电路拓扑），历史电流源 $I_{\text{hist}}[k] = f(y[k-1])$ 在每一步EMT仿真中更新，确保宽频等值网络与外部系统的接口兼容性。

## 2. 算法流程

**步骤1：数据预处理与特征提取**
- 对EMT仿真获得的时域脉冲响应 $h(t)$ 进行采样，采样频率 $f_s = 1/\Delta t \geq 10 f_{\text{max}}$（论文中 $\Delta t = 1.0\times 10^{-4}\,\text{s}$ 对应 $f_s = 10\,\text{kHz}$）
- 去除直流分量与趋势项，必要时加窗抑制频谱泄漏（推荐使用Hamming或Kaiser窗）
- 对含噪声信号进行低通滤波，截止频率设置为 $f_{\text{max}} = 5\,\text{kHz}$

**步骤2：Hankel矩阵构建与SVD分析**
- 选择初始过定阶数 $L \gg n$（通常 $L = N/2$），构建扩展Hankel矩阵 $\mathbf{H}_{(N-L)\times L}$
- 执行SVD分解：$\mathbf{H} = \sum_{i=1}^{r} \sigma_i \mathbf{u}_i \mathbf{v}_i^T$
- 根据奇异值能量累积准则确定有效阶数：$n = \min\left\{k \,\big|\, \sum_{i=1}^{k} \sigma_i^2 / \sum_{i=1}^{r} \sigma_i^2 \geq 0.999\right\}$，论文中最终确定为70阶

**步骤3：线性预测系数求解**
- 利用截断后的奇异值构造降阶矩阵 $\mathbf{H}_{\text{red}} = \mathbf{U}_n \mathbf{\Sigma}_n \mathbf{V}_n^T$
- 通过最小二乘求解预测系数向量 $\mathbf{a} = [a_1, \dots, a_n]^T$：
  $$\mathbf{a} = -\mathbf{H}_{\text{red}}^{\dagger} \mathbf{h}_{\text{tail}}$$
  其中 $\mathbf{h}_{\text{tail}} = [h[n], h[n+1], \dots, h[N-1]]^T$，$\dagger$ 表示伪逆

**步骤4：极点提取**
- 求解特征多项式根：$z^n + a_1 z^{n-1} + \dots + a_n = 0$
- 将离散极点映射至连续域：$\lambda_i = \frac{1}{\Delta t} \ln(z_i)$
- 稳定性检查：剔除 $\text{Re}(\lambda_i) > 0$ 的不稳定极点（物理系统应满足 $\text{Re}(\lambda_i) < 0$）

**步骤5：留数计算**
- 构建Vandermonde矩阵 $\mathbf{V}$，元素 $V_{ki} = z_i^{k-1}$，$k=1,\dots,N$，$i=1,\dots,n$
- 求解超定线性方程组 $\mathbf{h} = \mathbf{V} \mathbf{R}$ 得留数向量 $\mathbf{R} = [R_1, \dots, R_n]^T$
- 幅值阈值筛选：剔除 $|R_i| < \epsilon_{\text{res}}$ 的弱贡献模态（论文中通过此步骤实现从过定阶数到70阶的精简）

**步骤6：模型验证与降阶**
- 重构脉冲响应：$\hat{h}[k] = \sum_{i=1}^{n} R_i z_i^k$
- 计算归一化均方根误差（NRMSE）：
  $$\text{NRMSE} = \frac{\sqrt{\frac{1}{N}\sum_{k=0}^{N-1} |h[k] - \hat{h}[k]|^2}}{\max(|h|)}$$
  论文中达到 $4.36\times 10^{-4}$ 的精度指标
- 若误差超限，返回步骤2调整阶数或检查数据质量

**步骤7：EMTP电路合成**
- 将共轭极点对分组，转换为RLC并联支路参数：
  $$L_i = \frac{1}{2|R_i|\cos\theta_i}, \quad R_i = -\frac{\sigma_i}{|R_i|\cos\theta_i}, \quad C_i = \frac{2|R_i|\cos\theta_i}{\sigma_i^2 + \omega_i^2}$$
- 对实数极点实现RC支路：$R = -\frac{1}{R_i}$，$C = \frac{R_i}{\lambda_i}$
- 在EMTP中构建戴维南等效电路，通过端口阻抗测试验证0-5kHz频带匹配度

## 3. 参数选取指南

| 参数类别 | 低频振荡分析(<5Hz) | 宽频网络等值(0-5kHz) | 高频EMI分析(>10kHz) |
|---------|-------------------|---------------------|-------------------|
| **采样步长 $\Delta t$** | $0.01\,\text{s} - 0.1\,\text{s}$ | $1.0\times 10^{-4}\,\text{s}$ (论文值) | $1.0\times 10^{-6}\,\text{s} - 1.0\times 10^{-5}\,\text{s}$ |
| **采样点数 $N$** | $10^3 - 10^4$ | $2\times 10^4 - 5\times 10^4$ | $>10^5$ |
| **Hankel矩阵行数** | $N/2$ | $N/2$ 或固定为500 | 固定为1000-2000 |
| **初始阶数估计** | $2\times$ 预期模态数 | $100-200$ (过定) | $200-500$ |
| **SVD截断阈值** | $10^{-3} \sim 10^{-4}$ | $10^{-4}$ (论文经验值) | $10^{-5}$ |
| **留数幅值阈值** | $10^{-3} \max(|R|)$ | $10^{-4} \max(|R|)$ | $10^{-6} \max(|R|)$ |
| **数据窗类型** | 指数窗（抑制尾部振荡） | Hamming窗 | Kaiser窗 ($\beta=6$) |

### 关键参数调优策略

**采样频率选择**：根据奈奎斯特准则，$f_s$ 应至少为关注最高频率的2倍，但考虑Prony方法对噪声敏感，建议 $f_s \geq 10 f_{\text{max}}$。论文中 $f_s = 10\,\text{kHz}$ 对应有效分析带宽5kHz。

**阶数过定与降阶**：初始设置较高阶数（如200阶）以捕获所有潜在模态，通过SVD分析观察奇异值"拐点"，通常在前70个奇异值后出现显著跌落（如论文所示），此时截断可有效抑制虚假模态。

**数值稳定性增强**：当Hankel矩阵条件数 $\kappa(\mathbf{H}) > 10^{12}$ 时，采用Tikhonov正则化：
$$\mathbf{a} = -(\mathbf{H}^T\mathbf{H} + \lambda \mathbf{I})^{-1}\mathbf{H}^T\mathbf{h}_{\text{tail}}$$
正则化参数 $\lambda$ 通常取 $10^{-6} \sim 10^{-8}$。

## 4. 性能分析

基于2004年IEEE Transactions论文的量化评估数据：

| 性能指标 | 全系统仿真 | Prony等值模型 | 改善倍数/数值 |
|---------|-----------|--------------|--------------|
| **计算时间** | $19.8\,\text{s}$ | $0.53\,\text{s}$ | $37\times$ (2.68%耗时) |
| **辨识精度(NRMSE)** | - | $4.36\times 10^{-4}$ | 高精度拟合 |
| **模型阶数** | 原系统数千节点 | 70阶 | 降阶比 >50:1 |
| **有效频带** | DC-5kHz | DC-5kHz | 全频段复现 |
| **暂态响应误差** | 基准 | <1% (峰值误差) | 工程可接受 |
| **内存占用** | 完整网络矩阵 | 70组RLC参数 | 显著降低 |

### 不同场景下的计算效率对比

| 应用场景 | 网络规模 | 全系统耗时 | Prony等值耗时 | 加速比 |
|---------|---------|-----------|--------------|--------|
| 输电线路等值 | 500节点 | 15-25s | 0.4-0.6s | 30-40× |
| 变电站母线阻抗 | 1000+节点 | 40-60s | 1.0-1.5s | 35-50× |
| 风电场集电系统 | 200节点 | 8-12s | 0.2-0.3s | 25-35× |

## 5. 最佳实践与注意事项

### 5.1 数据质量与预处理

**脉冲响应获取**：优先使用电流源注入法获取驱动点阻抗，避免电压源注入导致的数值振荡。注入波形推荐采用半正弦或梯形波，上升沿 $t_r \leq 1/(2f_{\text{max}})$ 以确保足够频谱内容。

**趋势项消除**：EMT仿真结果常含直流偏移，采用多项式拟合或经验模态分解（EMD）去除趋势，避免Prony将其误判为低频模态。

**信噪比控制**：当SNR < 40dB时，先进行小波去噪或SVD滤波，否则虚假模态数量将显著增加。

### 5.2 虚假模态识别与剔除

**能量准则**：定义模态能量 $E_i = |R_i|^2 / (2|\sigma_i|)$，剔除 $E_i < 0.01\% E_{\text{total}}$ 的弱模态。

**物理可行性检查**：
- 频率合理性：$\omega_i$ 应在预期物理范围内（如工频50/60Hz及其谐波附近）
- 阻尼合理性：阻尼比 $\xi_i = -\sigma_i / \sqrt{\sigma_i^2 + \omega_i^2}$ 应在 $0.001 \sim 0.3$ 之间，异常高阻尼常提示数值噪声

**留数-极点比检验**：若 $|R_i| / |\lambda_i| \ll \min(|h|)$，该模态可能为计算伪迹。

### 5.3 数值稳定性保障

**条件数控制**：构建Hankel矩阵时采用位移结构（Displacement Structure）或快速算法，避免显式构造大型矩阵。

**重根处理**：当系统存在重极点时（如理想LC谐振），标准Prony方法失效，需采用扩展Prony方法（Extended Prony Method）引入多项式乘子 $t^m e^{\lambda t}$。

**直流分量处理**：对于含非零直流偏移的阻抗 $Z(0) \neq 0$，增加一个实极点 $\lambda_0 = 0$（或极小负实数 $-10^{-6}$）对应留数 $R_0 = Z(0)$。

### 5.4 EMT接口兼容性

**插值误差**：Prony提取的离散模型需在EMTP中以 $\Delta t_{\text{EMTP}}$ 步长运行，若 $\Delta t_{\text{EMTP}} \neq \Delta t_{\text{Prony}}$，需通过Tustin变换或零阶保持器离散化重新映射极点。

**因果性验证**：确保所有留数-极点组合满足Hilbert变换关系，避免出现非因果响应。

## 6. 与其他方法的对比

| 对比维度 | Prony分析 | Vector Fitting (VF) | ERA (特征系统实现算法) | HT (Hilbert变换) |
|---------|-----------|-------------------|---------------------|----------------|
| **输入数据** | 时域脉冲响应 | 频域采样数据 | 时域脉冲/阶跃响应 | 时域响应（解析信号） |
| **数学基础** | 指数拟合/线性预测 | 有理函数最小二乘 | 奇异值分解+状态空间 | 解析信号瞬时参数 |
| **模态提取** | 直接得极点留数 | 迭代优化极点位置 | 需额外转换得留数 | 仅得瞬时频率/幅值 |
| **非线性处理** | 弱（需分段线性化） | 中等（可处理弱非线性） | 弱 | 强（适用于非平稳信号） |
| **计算复杂度** | $O(Nn^2)$，单次计算 | $O(Nn^2)$，多次迭代 | $O(N^3)$（SVD主导） | $O(N \log N)$（FFT辅助） |
| **宽频适用性** | 中-低频优（<5kHz） | 宽频优（DC-GHz） | 全频段 | 低频优 |
| **EMT集成** | 直接合成RLC电路 | 需转换为状态空间 | 需模型降阶 | 难以直接电路综合 |
| **抗噪性** | 中等（需预处理） | 强（最小二乘平滑） | 强（SVD截断） | 弱（对端点效应敏感） |
| **时变系统** | 不适用 | 不适用 | 分段适用 | 适用（HHT方法） |

### 方法选择决策树

1. **数据可用性优先**：
   - 若仅有频域网络函数（如阻抗扫描结果）→ 选择 **Vector Fitting**
   - 若仅有EMT仿真时域波形 → 选择 **Prony分析**

2. **频段特性**：
   - 低频机电振荡（0.1-2Hz）→ **Prony分析** 或 **HT**
   - 高频电磁暂态（>10kHz）→ **Vector Fitting**（Prony受限于采样长度）

3. **实时性要求**：
   - 在线辨识 → **HT**（计算最快）或 **改进Prony**（递归实现）
   - 离线高精度等值 → **Prony分析**（物理意义明确，直接电路综合）

4. **多端口网络**：
   - 单端口驱动点阻抗 → **Prony分析**（简单高效）
   - 多端口耦合网络 → **Vector Fitting**（矩阵拟合成熟）

### 混合策略建议

对于超大规模系统（>1000节点），建议采用**两阶段方法**：
1. 使用 **Prony分析** 在时域提取主导模态（如前70阶），获得初始极点估计；
2. 将这些极点作为 **Vector Fitting** 的初始极点，在频域进行精修，以同时保证计算效率和宽频精度。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS V]] | 2004 |

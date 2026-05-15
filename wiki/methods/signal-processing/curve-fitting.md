---
title: "曲线拟合 (Curve Fitting)"
type: method
tags: [curve-fitting, parameter-estimation, optimization, least-squares, nonlinear-fitting, rational-approximation, vector-fitting]
created: "2026-05-04"
updated: "2026-05-15"
---

# 曲线拟合 (Curve Fitting)

## 定义

曲线拟合是通过数学函数近似描述离散数据点间关系的方法，目标是找到最佳参数使拟合函数与实测数据之间的误差最小。在EMT仿真中，曲线拟合用于从测量数据提取设备参数、频率响应的有理函数逼近、以及实验数据的数学建模。

从数学上讲，曲线拟合问题可表述为：给定$N$个观测点$\{(x_i, y_i)\}_{i=1}^{N}$，寻求参数向量$\mathbf{\theta}$使得目标函数最小化：

$$\min_{\mathbf{\theta}} \sum_{i=1}^{N} w_i \left( y_i - f(x_i, \mathbf{\theta}) \right)^2$$

其中$f(x_i, \mathbf{\theta})$为拟合函数，$w_i$为权重。不同拟合方法的核心差异在于$f$的形式（线性/非线性）、优化算法、以及正则化策略。

**边界限定**：本页面聚焦于曲线拟合的数值方法，不包括统计回归分析的推断理论。

## EMT中的作用

曲线拟合是参数辨识和模型构建的核心工具，在EMT仿真中有四类主要应用场景：

### 频变参数拟合
从频率扫描数据提取有理函数模型（如矢量拟合），用于传输线路、网络等值的宽频建模。Gustavsen 2004指出，矢量拟合（VF）已成为EMT中频变参数逼近的标准方法，在0-100kHz频带内可实现机器精度拟合（RMS误差<10⁻¹¹）。

### 饱和特性拟合
变压器磁化曲线的数学表示。Canal 2021提出从现场投切暂态测量数据中分离励磁电流，通过积分重构磁链-电流关系，对深饱和区采用最小二乘法拟合线性段斜率获取饱和电感。该方法使96 MVA变压器饱和电感辨识误差降至0.6%。

### 电弧特性拟合
断路器电弧的V-I特性建模需要根据实验数据拟合电弧电导的时变模型。

### 实验数据处理
测量数据的平滑和插值，如现场录波数据的去噪和特征提取。

## 形式化表达

### 有理函数逼近基本形式

EMT中频域曲线拟合的核心是有理函数逼近，即将频域响应$F(j\omega)$表示为：

$$F(s) = \sum_{n=1}^{N} \frac{R_n}{s - a_n} + D + sE$$

其中$a_n$为极点，$R_n$为留数，$D$和$E$为常数项。该形式可直接用于递归卷积计算，实现时域高效仿真。

### 线性最小二乘

当拟合函数关于参数线性时（如多项式拟合），正规方程为：

$$\mathbf{A}^T\mathbf{W}\mathbf{A}\mathbf{\theta} = \mathbf{A}^T\mathbf{W}\mathbf{y}$$

其中$\mathbf{A}$为设计矩阵，$\mathbf{W}$为权重对角矩阵，$\mathbf{y}$为观测向量。求解采用QR分解以保证数值稳定性。

### 非线性最小二乘

当拟合函数关于参数非线性时（如指数函数、有理函数），采用迭代优化：

$$\mathbf{\theta}_{k+1} = \mathbf{\theta}_k + \left( \mathbf{J}_k^T\mathbf{J}_k \right)^{-1} \mathbf{J}_k^T \mathbf{r}_k$$

其中$\mathbf{J}_k = \partial \mathbf{r}(\mathbf{\theta}_k) / \partial \mathbf{\theta}$为雅可比矩阵，$\mathbf{r}_k = \mathbf{y} - f(\mathbf{x}, \mathbf{\theta}_k)$为残差向量。

## EMT专用拟合方法

### 1. 矢量拟合（Vector Fitting, VF）

矢量拟合是EMT中应用最广的有理函数逼近方法，由Gustavsen 2004提出。其核心思想是通过极点迁移将非线性优化问题转化为两个线性最小二乘问题。

**两阶段算法**：

第一阶段（极点识别）：给定初始极点集$\{\bar{a}_n\}$，构建增广系统同时拟合$\sigma(s)$和$\sigma(s)f(s)$：

$$\sigma_{fit}(s) = 1 + \sum_{n=1}^{N} \frac{\tilde{c}_n}{s - \bar{a}_n}$$
$$(\sigma f)_{fit}(s) = \sum_{n=1}^{N} \frac{c_n}{s - \bar{a}_n} + d + sh$$

通过求解线性最小二乘获得$\sigma_{fit}(s)$的零点$z_n$，这些零点成为改进后的极点$a_n^{new}$。

第二阶段（留数识别）：固定新极点，重新拟合原始函数$f(s)$获得留数$c_n$、$d$、$h$。

**复数起始极点策略**：对于含多谐振峰的响应，使用复数共轭起始极点$\bar{a}_n = -\alpha + j\beta$（其中$\alpha = \beta/100$），可完全消除病态条件问题。

**量化性能**（Gustavsen 2004）：
- 20阶VF拟合18阶测试函数：RMS误差3.8×10⁻¹²
- 40阶VF拟合18阶测试函数：RMS误差1.6×10⁻¹²
- 极点估计相对误差：约10⁻⁷
- 留数估计相对误差：约10⁻⁷
- 收敛性：通常1-3次迭代即可达到机器精度

### 2. 频率分区拟合（Frequency-partitioning Fitting, FpF）

Noda 2015提出，将宽频率范围划分为多个分区，各分区独立进行有理函数拟合，以避免大留极比（large residue/pole ratios）问题。

**算法步骤**：
1. 将频率范围划分为高频段（HF, 如1 Hz至1 MHz）和低频段（LF, 如0.001 Hz至1 Hz）
2. 对高频段使用标准VF或FDCM拟合
3. 计算低频段拟合误差$\Delta H_{low} = H_{low} - H_{high}(s_{low})$
4. 对误差函数独立进行有理逼近作为校正项
5. 最终模型：$H \approx H_{high} + \Delta H_{low}$

### 3. 分区拟合与直流校正（Partitioned Fitting with DC Correction）

Cervantes et al. 2018在FpF基础上增加直流校正，专门处理HVDC线路/电缆的直流稳态响应。

**高频传播函数拟合**：
$$H_{high} \cong \sum_{i=1}^{N_{gr}} \left( \sum_{j=1}^{M_i} \frac{R_{i,j}}{s - p_{i,j}} e^{-s\tau_i} \right)$$

其中$N_{gr}$为模态传播组数，$M_i$为第$i$组逼近阶数，$\tau_i$为第$i$模态组时延。

**低频误差校正**：
$$\Delta H_{low} = H_{low} - H_{high}(s_{low})$$
$$\Delta H_{low} \cong \sum_{j=1}^{M_{low}} \frac{R_{low,j}}{s - p_{low,j}} e^{-s\tau_1}$$

**量化性能**（Cervantes et al. 2018）：
- 两端HVDC系统测试（27km架空线+44km电缆+97km架空线）：
  - FDM/DC稳态电压V₂=0.8659 p.u.（误差<0.1%）
  - FDM/DC稳态电流I₄=0.3084 p.u.（误差<0.1%）
  - 传统ULM（fmin=0.1 Hz）：V₂误差10.1%，I₄误差27.6%
  - 传统ULM（fmin=0.001 Hz）：I₄误差5.1%且时域持续振荡
- 拟合参数：12极点/模态组（HF），8极点（LF校正），10 μs仿真步长

### 4. 复矢量拟合（Complex Vector Fitting, CVF）

Kida 2025提出，CVF在VF基础上解除共轭对称约束，允许极点和留数独立存在，从而构建非厄米对称的有理逼近模型。

**基本形式**：
$$\mathbf{Y}(s) \approx \sum_{i=1}^{N_p} \frac{\mathbf{R}_i}{s - p_i} + \mathbf{D}$$

其中$\mathbf{Y}(s)$为N端口导纳矩阵，$p_i$和$\mathbf{R}_i$可为任意复数（不要求共轭成对）。

**解析信号与频移**：
$$u_A(t) = u(t) + j\mathcal{H}\{u(t)\}$$
$$u_{A,sh}(t) = \exp(-j2\pi\Delta f t) u_A(t)$$

通过希尔伯特变换构造解析信号消除负频率镜像，再经频移将高频成分下变频至基带。

**量化性能**（Kida 2025）：
- CVF拟合误差较传统VF降低最高达8个数量级（10⁸倍）
- 频移技术使CVF框架精度再提升最高达2个数量级（10²倍）
- 在相同目标精度下，EMT仿真步长可扩大2.33至5.5倍
- 测试系统：132 kV三相输电线路（12 km）

### 5. 低阶有理函数拟合

Liu et al.提出针对传输线路频变参数的低阶拟合方法，避免Bode渐近线法产生冗余零极点。

**方法**：
1. 对特征阻抗和传播系数进行低阶零极点初始定位
2. 用非线性最小二乘法提高拟合精度
3. 保证拟合精度的同时降低拟合阶数

### 6. 非线性饱和曲线拟合

Canal 2021提出从现场投切暂态数据中辨识变压器饱和曲线。

**算法步骤**：
1. 采集三相电压、电流瞬时值（采样率5 kHz）
2. 从线电流中分离三角形绕组环流：$I_{mag,i} = J_i - I_{delta}$
3. 计算励磁支路电压：$V_{mag,i}(t) = V_{HV,i}(t) - L_{HV} \frac{dJ_i}{dt} - R_{HV} J_i(t)$
4. 积分重构磁链：$\phi_i(t) = -\int V_{mag,i}(t) dt + C_i$
5. 筛选饱和区数据点，采用最小二乘法拟合饱和电感

**量化性能**（Canal 2021）：
- 96 MVA变压器（Ynd11, 410/6.8 kV）：饱和电感均值0.833 H，标准差0.053 H
- 95%预测区间：±6.3%
- 制造商估算值0.959 H较实测均值高估约15.1%
- 饱和电感每高估10%，导致投切过电压约束低估约30%
- 算法提取励磁电流与EMTP理论计算值总误差仅0.6%

## 数值分析

### 精度与效率对比

| 方法 | 拟合精度 | 计算效率 | 适用场景 |
|------|---------|---------|---------|
| 线性多项式拟合 | 中等（取决于阶数） | 高 | 光滑函数、数据平滑 |
| Levenberg-Marquardt | 高 | 中等（依赖初值） | 非线性函数、饱和特性 |
| 矢量拟合（VF） | 极高（机器精度） | 高（共享极点） | 频域响应、网络等值 |
| 频率分区拟合（FpF） | 高 | 中等 | 宽频带响应、HVDC |
| 复矢量拟合（CVF） | 极高 | 高 | 非对称频谱、频移仿真 |

### 典型参数范围

| 参数 | 典型范围 |
|------|---------|
| 拟合阶数 | 4-40阶 |
| 频率范围 | 0.001 Hz - 1 MHz |
| 仿真步长 | 1 μs - 100 μs |
| 系统规模 | 1-100端口 |

### 性能指标

- **拟合精度**：VF可达机器精度（RMS误差<10⁻¹²），FpF/CVF可降低误差2-8个数量级
- **计算效率**：共享极点策略使多端口系统卷积计算速度提高约2倍
- **数值稳定性**：分区拟合策略可彻底消除大留极比导致的数值振荡

## 关键技术挑战

### 挑战1：病态条件问题

宽频带拟合时，设计矩阵的列存在尺度差异，导致正规方程条件数过大。VF通过复数起始极点和两阶段极点迁移策略有效缓解此问题。

### 挑战2：过拟合与欠拟合

拟合阶数选择是核心问题。阶数过低导致欠拟合（误差大），阶数过高导致过拟合（数值振荡、稳定性差）。通常通过交叉验证或误差准则（如AIC、BIC）选择阶数。

### 挑战3：局部极小

非线性最小二乘优化问题可能收敛到局部极小而非全局最优。信赖域方法和全局搜索策略（如遗传算法）可缓解此问题。

### 挑战4：直流稳态精确性

传统ULM在拟合频带包含直流附近频率时，大留极比导致时域数值振荡。分区拟合与直流校正（FDM/DC）策略可有效解决。

### 挑战5：无源性保持

有理函数模型必须满足无源性以保证时域仿真稳定性。VF模型可通过半尺寸奇异性测试检验无源性；CVF模型因非厄米特性需采用全尺寸哈密顿矩阵奇异值测试。

## 量化性能边界

| 方法 | 精度范围 | 加速比 | 误差指标 |
|------|---------|--------|---------|
| VF（Gustavsen 2004） | RMS<10⁻¹² | 2x（多端口卷积） | 极点相对误差~10⁻⁷ |
| FpF（Noda 2015） | 满足工程精度 | - | 与VF相当 |
| FDM/DC（Cervantes 2018） | DC误差<0.1% | - | 消除数值振荡 |
| CVF+频移（Kida 2025） | 较VF降低8数量级 | 步长扩大2.33-5.5x | RRMSE优化 |
| 饱和曲线辨识（Canal 2021） | 0.6% | - | 饱和电感标准差6.3% |

## 适用边界与选择指南

### 方法选择决策表

| 应用场景 | 推荐方法 | 关键参数 |
|---------|---------|---------|
| 输电线路频变参数 | VF + FDM/DC | 12极点/模态组，10 μs步长 |
| 网络等值宽频建模 | VF（复数起始极点） | 20-40阶，0-100kHz |
| HVDC直流稳态 | FDM/DC | 高频1Hz-1MHz，低频0.001-1Hz |
| 非对称频谱 | CVF + 频移 | Δf匹配激励频率 |
| 变压器饱和曲线 | 现场暂态测量+最小二乘 | 5kHz采样，饱和区线性拟合 |
| 低频暂态研究 | 低阶有理拟合 | 非线性最小二乘优化 |

### 失效边界

- **过拟合**：模型过于复杂导致数值不稳定
- **欠拟合**：模型过于简单导致关键动态丢失
- **病态问题**：参数高度相关导致求解不准确
- **局部极小**：非凸优化问题收敛到次优解
- **数据噪声**：测量噪声导致拟合参数偏差

## 相关页面

- [[vector-fitting]] - 矢量拟合（有理函数拟合的核心方法）
- [[parameter-identification]] - 参数辨识方法
- [[transmission-line-model]] - 输电线路模型（频变参数拟合应用）
- [[transformer-model]] - 变压器模型（饱和特性拟合应用）
- [[least-squares-method]] - 最小二乘法
- [[frequency-dependent-modeling]] - 频变建模
- [[network-equivalent]] - 网络等值
- [[wideband-modeling]] - 宽频建模
- [[state-space-method]] - 状态空间法
- [[prony-analysis]] - Prony分析
- [[dynamic-phasor]] - 动态相量法

## 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|---------|
| Gustavsen - Rational approximation of frequency domain responses by vector fitting | 2004 | VF两阶段极点迁移算法，复数起始极点策略，机器精度拟合 |
| Noda - Application of frequency-partitioning fitting to phase-domain frequency-dependent modeling | 2015 | FpF频率分区策略，改善数值条件 |
| Cervantes et al. - Partitioned Fitting and DC Correction for the Simulation of EMT in Transmission Lines/Cables | 2018 | FDM/DC两阶段分区拟合，直流校正，消除数值振荡 |
| Kida - Improving EMT simulations using frequency-shifted rational approximations | 2025 | CVF非厄米逼近，解析信号频移，步长扩大2.33-5.5倍 |
| Canal - Determination of the saturation curve of power transformers by processing transient measurements | 2021 | 现场暂态测量+最小二乘，饱和电感辨识误差0.6% |
| Liu et al. - Low-order approximation method for frequency-dependent transmission line model | 2016 | 低阶零极点定位，非线性最小二乘优化 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
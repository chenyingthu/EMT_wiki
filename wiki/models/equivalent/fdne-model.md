---
title: "频变网络等值 (FDNE)"
type: model
tags: [fdne, frequency-dependent, network-equivalent, multi-port, passivity]
created: "2026-04-13"
updated: "2026-05-18"
---

# 频变网络等值 (FDNE)

## 定义

频变网络等值（Frequency-Dependent Network Equivalent, FDNE）是将大规模电力系统的外部网络等效为多端口频率相关阻抗/导纳模型的技术。通过频域响应数据拟合有理函数或直接综合物理元件，将宽频网络特性压缩为有限阶状态空间或RLCM电路，同时大幅减少EMT仿真规模并保留外部网络在直流至数MHz频段的宽频动态响应。

核心数学形式为多端口导纳矩阵的有理函数逼近：

$$\mathbf{Y}(s) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}$$

其中 $N_p$ 为端口数，$N$ 为模型阶数，$\mathbf{R}_k \in \mathbb{C}^{N_p \times N_p}$ 为留数矩阵，$p_k$ 为系统极点，$\mathbf{D}, \mathbf{E} \in \mathbb{R}^{N_p \times N_p}$ 为常数项和微分项矩阵。

## EMT中的角色

FDNE在EMT仿真中承担外部网络等值接口的核心角色，解决三类关键问题：

**大规模电网简化**：全EMT仿真全部线路和变压器计算量大，FDNE将外部网络（接口以内）用频变N端口等值替代，减少50%-90%的网络节点数，同时保留宽频响应特性。

**混合仿真接口**：在TS-EMT混合仿真中，机电侧用相量模型，电磁侧用EMT详细模型，两者之间通过FDNE接口实现频率解耦——FDNE捕捉交流电网高频动态（>10 Hz），而机电侧等值提供低频动态。

**换流器宽频相互作用**：MMC-HVDC、风电等电力电子装置的开关谐波（Hz~数kHz）与外部网络的阻抗频率响应重叠，FDNE能复现这种宽频耦合，避免固定阻抗等值带来的交互失真。

## 建模方法

### 方法1：矢量拟合法（VF）

矢量拟合（Vector Fitting）是FDNE建模最成熟的方法，通过迭代将频域响应数据拟合为有理函数：

$$\mathbf{Y}(s) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}$$

**算法步骤**：
1. 选择初始极点集合（通常对数分布，$p_{k+1} = p_k^*$ 保证共轭成对）
2. 构造右插值问题：$[\sum_k \frac{R_k}{s_i-p_k}] \cdot v_i = w_i$，求解留数
3. 提取新极点（$R_k$ 矩阵的奇异值分解）
4. 迭代直至收敛（通常3-5次）
5. 无源性检查与强制（若需要）

**特点**：精度高、工业成熟；但依赖初始极点选择、迭代可能不收敛、需要单独处理无源性。

### 方法2：Loewner矩阵法（非迭代）

Loewner矩阵法从切向插值数据直接构造状态空间模型，无需迭代：

**核心公式（Loewner矩阵差商构造）**：

$$\mathbb{L}_{ij} = \frac{v_j r_i - l_j w_i}{\mu_j - \lambda_i}$$

其中 $\{\lambda_i\}$ 为右插值频点，$\{\mu_j\}$ 为左插值频点，$r_i, l_j$ 为切向方向向量。

**SVD降阶**：

$$[\mathbf{E}, \mathbf{A}, \mathbf{B}, \mathbf{C}] = f(\mathbf{L}, \mathbf{L}_\sigma, \mathbf{R}, \mathbf{L})$$

通过奇异值分解 $\mathbf{L} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^H$ 保留前 $n$ 个主奇异值对应的子空间，自动确定模型阶数。

**特点**：非迭代、无需初始极点、自动确定阶数；但需要合理的频域数据划分策略。

### 方法3：复数矢量拟合法（CVF）

CVF解除传统VF的共轭极点约束，允许独立拟合复极点：

$$\mathbf{Y}(s) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - (\sigma_k + j\omega_k)} + \mathbf{D} + s\mathbf{E}$$

适用于非对称系统或基带频响拟合场景。

### 方法4：网络综合法（Brune-Tellegen）

网络综合法直接面向频域阻抗表格数据综合物理RLCM网络，从拓扑层面保证无源性：

**四步递归算法**：
1. **移除虚轴极点**：$s=0$（串联电容）、$s=\infty$（串联电感）、$\omega_{jp}$（LC谐振）对应留数矩阵提取
2. **移除虚轴零点**：对剩余阻抗求逆，提取并联元件
3. **提取最小实部电阻**：$\Lambda(\omega) = |\Re\{Z_2(j\omega)\}| / \Delta_{11}(\omega)$，使实部在 $\omega_0$ 处秩亏
4. **Tellegen-Brune循环**：构造串联电感 $L_1$、并联LC $L_2/C_2$、耦合电感 $L_3$

最终得到80个RLCM模块的三端口等值网络，**无源性由物理拓扑内禀保证**，无需后处理。

### 方法5：双层FDNE等值

双层FDNE将外部网络分为详细层和等值层，分别捕捉不同频段动态：

$$\mathbf{Y}_{T-FDNE}(s) = \mathbf{Y}_{detailed}(s) + \mathbf{Y}_{equivalent}(s) + \mathbf{Y}_{comp}(s)$$

- **详细层**：端口宽频扰动测试 + 矢量拟合，捕捉高频电磁动态（>10 Hz）
- **等值层**：基于网络拓扑参数解析推导，捕捉低频机电动态
- **局部无源性补偿**：仅在破坏频段添加辅助有理函数，避免全局优化

## 关键技术挑战

### 挑战1：无源性保持

FDNE接入含开关和非线性元件的EMT网络后，若模型非无源，可能产生数值不稳定。

**判定条件**：$\lambda_{\min}(\Re[\mathbf{Y}(j\omega)]) \geq 0, \forall \omega$

**解决方案**：残差摄动法、局部无源性补偿（0.1-0.2秒构建时间 vs 全局优化的数十秒）、网络综合法（内禀保证）。

### 挑战2：端口数与计算复杂度

多端口系统中，状态空间矩阵维度为 $N \cdot N_p \times N \cdot N_p$（其中 $N$ 为每端口极点数，$N_p$ 为端口数），当 $N_p > 8$ 时计算成本显著增加——三端口网络80个RLCM模块意味着240个状态变量。

**解决方案**：SVD压缩留数矩阵（当秩 $r < (N+1)/2$ 时降计算量50%以上）、并行QR分解（占VF算法95%以上时间）、FPGA硬件加速实现亚微秒级步长。

### 挑战3：实时仿真步长约束

实时仿真要求单步计算时间严格小于仿真步长，FDNE的递归卷积或状态更新成为实时性瓶颈——尤其当端口数多、模型阶数高时，单步计算可能超过数毫秒。

**解决方案**：状态空间实现替代递归卷积、极点-留数转A/B/C/D矩阵、定点化（注意数值精度损失，CuFP定制浮点算术可降低30-40%资源占用）。

### 挑战4：模型验证与误差控制

FDNE精度需在全频段（DC~10MHz）与原始网络拟合误差严格校验，尤其在谐振峰附近若采样不足会导致严重偏差。

**验证方法**：频域阻抗曲线对比（对角与非对角元素）、时域阶跃响应仿真、全频段无源性特征值验证（$\lambda_{\min}(\Re[Y]) > 0$）、与详细模型交叉校验。

## 量化性能边界

| 性能指标 | 数值 | 来源 |
|---------|------|------|
| 计算加速比 | 3.3倍（网络综合法，640ms→194ms） | Ahmadi 2021 |
| 计算加速比 | 218倍（风电场等值，18480s→110s） | 2012 |
| 计算加速比 | 6.5倍（双层FDNE，1420s→218s） | Shu 2019 |
| 建模效率提升 | >200倍（局部补偿 vs 全局优化） | Shu 2019 |
| 幅值拟合误差 | <0.8%（Loewner矩阵法） | Gurrala 2015 |
| 相位偏差 | <0.5°（Loewner矩阵法） | Gurrala 2015 |
| 时域偏差 | <0.5%（风电机组故障暂态） | 2024 |
| 仿真发散率降低 | 18.7%→0%（局部无源性补偿后） | Shu 2019 |
| 模型阶数 | 40-50个极点（10kHz-10MHz杆塔模型） | 2021 |
| 模型阶数 | 80个RLCM模块（三端口网络） | Ahmadi 2021 |
| 实时成功率 | 100%（11个子模块划分，Y10案例） | 2020 |

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 关键参数 |
|---------|---------|---------|
| 实时仿真/硬件加速 | 网络综合法 + FPGA状态空间 | 步长 <1 µs，80个RLCM模块 |
| 风电场/新能源并网 | 双层FDNE或离散z域模型 | 频率0-50 kHz，17台等效替代66台 |
| 多端口大规模网络 | Loewner矩阵法或并行CVF | $N_p \geq 10$，SVD自适应阶数 |
| 严格无源性要求 | 网络综合法或局部补偿 | 发散率18.7%→0% |
| MMC-HVDC混合仿真 | 双层FDNE + 局部补偿 | 高频>10 Hz，建模0.1-0.2秒 |

## 相关方法

- [[vector-fitting]] — 矢量拟合：最成熟的频域响应拟合方法
- [[passivity-enforcement]] — 无源性强制：确保FDNE时域稳定
- [[prony-analysis]] — Prony分析：参数辨识与模态分析
- [[state-space-method]] — 状态空间法：FDNE的离散化实现
- [[network-equivalent]] — 网络等值：FDNE所属的上位概念

## 相关模型

- [[transmission-line-model]] — 输电线路模型：FDNE端口边界模型
- [[transformer-model]] — 变压器模型：变压器宽频等值
- [[vsc-model]] — VSC模型：换流器外部系统简化
- [[wind-farm-modeling]] — 风电场模型：风电场宽频聚合
- [[mmc-model]] — MMC模型：MMC外部网络等值

## 来源论文

| 论文 | 年份 |
|------|------|
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs]] | 2015 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port FDNE]] | 2021 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|Two-layer network equivalent with local passivity compensation]] | 2019 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Online passivity enforced wide-band multi-port FDNE]] | 2018 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient implementation of multi-port FDNEs]] | 2022 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic transient analysis using FDNE]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation using FDNE]] | 2025 |
| [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o|Enhanced K-means two-step clustering for dynamic equivalent]] | 2025 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of FDNEs in dynamic harmonic domain]] | 2021 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation for FDNE]] | 2024 |
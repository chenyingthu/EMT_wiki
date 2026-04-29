---
title: "矢量拟合"
type: method
tags: []
created: "2026-04-13"
---

# 矢量拟合

## 论文方法分析
> 基于 6 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 并行计算技术 | 2 | Enhancing computation performance of rational approximation for freque |
| C语言底层线性代数实现 | 2 | Enhancing computation performance of rational approximation for freque |
| 有理函数逼近 | 2 | Rational approximation of frequency domain responses by vector fitting |
| 复数向量拟合(CVF) | 1 | Enhancing computation performance of rational approximation for freque |
| 向量拟合(VF) | 1 | Enhancing computation performance of rational approximation for freque |
| 有理逼近建模 | 1 | Enhancing computation performance of rational approximation for freque |
| 复数向量拟合 (CVF) | 1 | Enhancing computation performance of rational approximation for freque |
| 向量拟合 (VF) | 1 | Enhancing computation performance of rational approximation for freque |
| 有理逼近与频域实现 | 1 | Enhancing computation performance of rational approximation for freque |
| 模态矢量拟合(MVF) | 1 | Fast Realization of the Modal Vector Fitting |
| 带逆幅值加权的常规矢量拟合 | 1 | Fast Realization of the Modal Vector Fitting |
| 稀疏矩阵结构优化求解 | 1 | Fast Realization of the Modal Vector Fitting |
| 逐行对称留数识别 | 1 | Fast Realization of the Modal Vector Fitting |
| 有理函数/极点-留数建模 | 1 | Fast Realization of the Modal Vector Fitting |
| 向量拟合(Vector Fitting) | 1 | Rational approximation of frequency domain responses by vector fitting |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 频率相关网络等值(FDNE) | 1 |
| 8端口网络模型 | 1 |
| 导纳/阻抗矩阵模型 | 1 |
| 频率相关网络等值 (FDNE) | 1 |
| 8端口网络等值模型 | 1 |
| 有理模型 (Rational Models) | 1 |
| 频率相关网络等效(FDNE) | 1 |
| 多端口导纳矩阵 | 1 |
| 极点-留数模型 | 1 |
| 状态空间模型 | 1 |
| 变压器 | 1 |
| 网络等值模型 | 1 |
| 频变电力系统组件 | 1 |
| Frequency-dependent network equivalents (FDNE) | 1 |
| High-frequency transformers | 1 |
### 验证方式分布
- **仿真/对比**: 2 篇
- **仿真与计算性能对比**: 1 篇
- **仿真**: 1 篇
- **仿真/实验**: 1 篇
- **仿真对比**: 1 篇
## 技术演进脉络
### 2004年 (1篇)
- **Rational approximation of frequency domain responses by vector fitting - Power D**
  - 💡 通过在向量拟合中引入复数起始极点，实现了对含密集谐振峰频域响应的高精度、通用有理函数逼近。
  - 提出了一种通用的频域响应有理函数逼近框架
  - 将向量拟合算法扩展至复数起始极点，解决了多谐振峰拟合难题
### 2009年 (1篇)
- **Fast Realization of the Modal Vector Fitting**
  - 💡 通过预计算初始极点、利用稀疏矩阵求解极点及逐行对称求解留数三步策略，实现了模态矢量拟合方法的高效计算，解决了高阻抗终端下小特征值建模误差放大与计算资源消耗大的问题。
  - 提出通过带逆幅值加权的常规矢量拟合预计算初始极点集，显著减少MVF迭代次数。
  - 利用稀疏矩阵结构仅求解关键未知数，实现极点识别步骤的高效计算。
### 2021年 (1篇)
- **Review and comparison of frequency-domain curve-fitting techniques: Vector fitti**
  - 💡 首次将四种主流频域曲线拟合技术与模型降阶方法结合进行系统性横向对比，为EMT仿真中宽频带等效建模提供了明确的方法选型与降阶指导。
  - 系统梳理并对比了VF、FpF、MPM和LM四种主流频域曲线拟合技术的基本理论与算法特性。
  - 通过三个典型算例定量评估了各方法在拟合精度与模型阶数方面的性能差异。
### 2022年 (1篇)
- **Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining **
  - 💡 将矢量拟合技术与考虑频变土壤参数的Nakagawa模型相结合，有效提升了ATP工具中多相架空线路雷击暂态仿真的计算精度。
  - 系统对比了Bode法与矢量拟合技术在JMarti模型中逼近特征阻抗和传播矩阵的精度与性能。
  - 深入分析了Nakagawa方法与Carson方法在考虑频变土壤参数时对线路暂态响应的影响差异。
### 2024年 (2篇)
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 首次将CVF引入FDNE矩阵综合并结合并行C语言底层实现，在保持高精度的同时大幅提升了计算效率与软件独立性。
  - 首次将复数向量拟合(CVF)应用于FDNE导纳/阻抗矩阵综合，突破了传统算法必须满足复共轭极点配对的限制。
  - 开发了基于C语言与底层线性代数库的并行化VF/CVF算法实现，彻底摆脱了对MATLAB等商业软件的依赖。
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 将复数向量拟合引入FDNE导纳矩阵综合，并结合并行化C语言底层实现，构建了无商业软件依赖的高性能有理逼近计算框架。
  - 首次将复数向量拟合（CVF）应用于导纳/阻抗矩阵综合，消除了传统VF对复共轭极点的强制约束。
  - 开发了基于C语言和底层线性代数库的VF与CVF并行化实现，彻底摆脱了对MATLAB等商业软件的依赖。
## 关键发现汇总
- [2004] **Rational approximation of frequency domain responses by vect**: 复数起始极点策略成功克服了原实数极点方法在多谐振峰场景下的失效问题
- [2004] **Rational approximation of frequency domain responses by vect**: 在人工构造数据、实测变压器频响及网络等值模型中均实现了高精度拟合
- [2004] **Rational approximation of frequency domain responses by vect**: 将频域响应转化为低阶有理函数，大幅提升了时域EMT仿真的计算效率
- [2009] **Fast Realization of the Modal Vector Fitting**: 所提快速实现方法在保证小特征值精确表示的同时，大幅降低了计算时间和内存消耗。
- [2009] **Fast Realization of the Modal Vector Fitting**: 在频率相关网络等效（FDNE）建模算例中验证了该方法的高效性与准确性。
- [2021] **Review and comparison of frequency-domain curve-fitting tech**: VF及其改进算法在多数宽频带场景下拟合精度最优，但为满足误差指标常需较高的模型阶数。
- [2021] **Review and comparison of frequency-domain curve-fitting tech**: MPM和LM作为非迭代方法避免了初始极点选择难题，但在复杂频段拟合中易产生冗余阶数。
- [2021] **Review and comparison of frequency-domain curve-fitting tech**: 结合MOR技术可在几乎不损失精度的前提下显著压缩状态空间模型阶数，有效提升EMT仿真计算速度。
- [2022] **Transient Analysis on Multiphase Transmission Line Above Los**: 矢量拟合技术在逼近特征阻抗和传播矩阵时的精度显著优于传统Bode法。
- [2022] **Transient Analysis on Multiphase Transmission Line Above Los**: 采用Nakagawa方法计算的暂态电压峰值较Carson方法明显降低，且在高电阻率土壤中差异更为显著。
- [2024] **Enhancing computation performance of rational approximation **: 并行化C语言实现显著加速了有理逼近过程，有效处理了具有大量峰谷特征的复杂频率响应。
- [2024] **Enhancing computation performance of rational approximation **: CVF算法在取消共轭极点约束的情况下仍能保证FDNE建模的精度与数值稳定性。
- [2024] **Enhancing computation performance of rational approximation **: 所提算法的计算性能随模型阶数、端口数和频率样本量的变化表现出良好的可扩展性与效率优势。
- [2024] **Enhancing computation performance of rational approximation **: 并行化C语言实现显著提升了有理逼近的计算效率，大幅缩短了大规模FDNE的拟合耗时。
- [2024] **Enhancing computation performance of rational approximation **: CVF方法成功处理了具有大量频域峰谷的8端口FDNE，且无需进行复共轭极点配对。
- [2024] **Enhancing computation performance of rational approximation **: 算法计算性能随模型阶数、端口数及频率样本量的变化表现出良好的可扩展性与稳定性。

## 定义与边界

矢量拟合是把频域采样响应转换为稳定有理函数的系统辨识方法，常用于 [[fdne-model|频率相关网络等值]]、[[transmission-line-model|输电线路模型]]、[[cable-model|电缆模型]] 和 [[transformer-model|变压器模型]] 的宽频 EMT 实现。它解决的是“如何拟合端口响应”的问题，不直接保证模型接入网络后的能量一致性；用于时域仿真前通常还要配合 [[passivity-enforcement|无源性强制]]、[[state-space-method|状态空间实现]] 和模型阶数检查。

该方法适用于线性或线性化端口频响、测量阻抗/导纳曲线和频率相关参数表。若对象包含强饱和、开关限幅或控制器非线性，VF 只能描述选定工作点附近的小信号行为；若频段、采样密度或初始极点选择不足，拟合曲线看似平滑也可能在时域卷积中产生虚假振荡。

## 代表性来源与内部链接

代表性来源包括 [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vector fitting]]、[[fast-realization-of-the-modal-vector-fitting|Fast Realization of the Modal Vector Fitting]]、[[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting techniques]]、[[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Lossy Ground]] 和 [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation for frequency-dependent network equivalents]]。阅读顺序可从 [[frequency-dependent-modeling|频率相关建模]] 进入，再连接到 [[network-equivalent|网络等值]]、[[prony-analysis|Prony 分析]]、[[passivity-enforcement|无源性强制]] 和 [[rtds|RTDS]] 实时实现约束。

## 深度增强内容

### 矢量拟合（Vector Fitting, VF）

## 1. 核心原理详解

矢量拟合是一种鲁棒的有理函数逼近技术，用于将频域响应数据 $H(s)$ 拟合为极点-留数形式的有理函数模型。该方法通过迭代线性化技术将非线性最小二乘问题转化为两步线性最小二乘求解，避免了直接非线性优化的数值困难。

### 1.1 有理函数逼近形式

对于单端口系统，目标函数为：
$$H(s) \approx \sum_{n=1}^{N} \frac{c_n}{s-a_n} + d + se$$

其中 $a_n$ 为极点（$s$-平面），$c_n$ 为留数，$d$ 为直接耦合项，$e$ 为高频渐近项。对于多端口 $N_p \times N_p$ 导纳矩阵 $\mathbf{Y}(s)$，采用**公共极点策略**（Common-Pole Strategy）：
$$\mathbf{Y}(s) \approx \sum_{n=1}^{N} \frac{\mathbf{R}_n}{s-a_n} + \mathbf{D} + s\mathbf{E}$$

其中 $\mathbf{R}_n \in \mathbb{C}^{N_p \times N_p}$ 为留数矩阵，所有矩阵元素共享相同极点集 $\{a_n\}$，这使得时域实现可通过共享状态变量显著降低计算量。

### 1.2 两阶段线性化算法

**第一阶段：极点迁移（Pole Relocation）**

引入辅助函数 $\sigma(s)$，将非线性问题转化为关于扩展参数的线性问题：
$$\left(\sum_{n=1}^{N} \frac{\bar{c}_n}{s-\bar{a}_n} + 1\right) H(s) \approx \sum_{n=1}^{N} \frac{c_n}{s-\bar{a}_n} + d + se$$

通过采样频点 $s_k = j\omega_k$ 构建超定线性方程组 $\mathbf{A}\mathbf{x} = \mathbf{b}$，利用 QR 分解求解 $\bar{c}_n$ 和 $c_n$。新极点通过 $\sigma(s)$ 的零点获得：
$$\text{zeros}(\sigma(s)) = \text{eig}(\mathbf{A} - \mathbf{b}\mathbf{c}^T)$$

其中 $\mathbf{A} = \text{diag}(\bar{a}_n)$，$\mathbf{b} = [1, \cdots, 1]^T$。

**第二阶段：留数辨识（Residue Identification）**

固定收敛后的极点 $\{a_n\}$，重新求解线性最小二乘问题获得最优留数 $\mathbf{R}_n$、$\mathbf{D}$ 和 $\mathbf{E}$。

### 1.3 复数矢量拟合（Complex Vector Fitting, CVF）

传统 VF 强制极点为实数或共轭复数对（$a_{n+1} = a_n^*$），适用于实值冲激响应系统。CVF 解除该约束，允许独立复极点：
$$H(s) \approx \sum_{n=1}^{N} \frac{c_n}{s-a_n} + \text{c.c.} \quad \Rightarrow \quad H(s) \approx \sum_{n=1}^{N} \frac{c_n}{s-a_n}$$

其中 $a_n \in \mathbb{C}$ 独立优化。CVF 特别适用于：
- 非对称频响（如含旋转机械的系统等效）
- 基带频移系统（如电力电子变换器阻抗）
- 复数变换域模型（如 Clarke/Park 变换后的域）

### 1.4 模态矢量拟合（Modal Vector Fitting, MVF）

针对多导体传输线，MVF 在模态域进行拟合：
$$\mathbf{Y}(s) = \mathbf{T}(s)\mathbf{Y}_m(s)\mathbf{T}^{-1}(s)$$

通过特征值分解将矩阵拟合转化为独立标量拟合：
$$y_{m,i}(s) \approx \sum_{n=1}^{N_i} \frac{r_{i,n}}{s-p_{i,n}} + d_i$$

利用稀疏矩阵结构仅求解关键未知数，计算复杂度从 $O(N^3)$ 降至 $O(N)$。

## 2. 算法流程

### 2.1 标准 VF 算法步骤

**输入**：频域采样数据 $\{s_k, H(s_k)\}_{k=1}^{K}$，初始极点数 $N$
**输出**：极点 $\{a_n\}$，留数 $\{c_n\}$，直流项 $d$，高频项 $e$

1. **初始化**  
   选择起始极点 $\{\bar{a}_n\}$，对数分布于拟合频段 $[\omega_{\min}, \omega_{\max}]$：
   $$\bar{a}_n = -\alpha_n + j\beta_n, \quad \alpha_n = \beta_n/100$$
   其中 $\beta_n$ 对数均匀分布。

2. **构建线性系统**  
   对每个采样点 $s_k$ 构造行：
   $$\frac{1}{s_k-\bar{a}_1}, \cdots, \frac{1}{s_k-\bar{a}_N}, 1, s_k, \frac{-H(s_k)}{s_k-\bar{a}_1}, \cdots, \frac{-H(s_k)}{s_k-\bar{a}_N}$$

3. **QR 分解求解**  
   求解 $\mathbf{A}\mathbf{x} = \mathbf{b}$，提取 $\bar{c}_n$ 构建 $\sigma(s)$。

4. **极点更新**  
   计算 $\sigma(s)$ 零点作为新极点 $\{a_n^{\text{new}}\}$。

5. **收敛判断**  
   若 $\|\mathbf{a}^{\text{new}} - \mathbf{a}^{\text{old}}\| < \varepsilon$（通常 $\varepsilon = 10^{-3}$），进入步骤 6；否则返回步骤 2。

6. **留数计算**  
   固定极点，重新求解留数 $c_n, d, e$。

7. **稳定性强制**  
   对 $\text{Re}(a_n) > 0$ 的极点取负：$a_n^{\text{stable}} = -\text{Re}(a_n) + j\text{Im}(a_n)$。

### 2.2 快速 MVF 优化流程

针对大规模多端口系统（$N_p > 10$）：

1. **预计算初始极点**  
   采用带逆幅值加权的常规 VF 对模态响应预拟合，获得高质量初始极点集，将迭代次数从 10-15 次降至 3-5 次。

2. **稀疏 QR 分解**  
   利用块对角结构，极点识别阶段仅求解 $N_p \times N$ 个关键未知数，避免构建完整的 $KN_p \times N(N_p+2)$ 矩阵。

3. **逐行对称求解**  
   残差识别阶段利用导纳矩阵对称性 $\mathbf{Y}_{ij} = \mathbf{Y}_{ji}$，内存分配降低 85%，支持端口数 $>30$ 的系统。

## 3. 参数选取指南

| 应用场景 | 极点数量 $N$ | 频率采样策略 | 起始极点设置 | 特殊处理 |
|---------|-------------|-------------|-------------|---------|
| **电力电缆 FDNE** | 20-40 个极点 | 0.01 Hz – 2 MHz，对数均匀，每 decade 20-50 点 | $\alpha = \beta/100$ | 考虑 FLE（折叠线等效）分解改善低频条件数 |
| **架空输电线路** | 30-60 个极点 | 0.1 Hz – 10 MHz，需覆盖地模与线模特征频率 | 复数共轭对，虚部对应传播常数特征频率 | 结合全通函数提取频变时延 |
| **变压器宽频模型** | 10-30 个极点 | 1 Hz – 1 MHz，关注谐振峰密集区 | 在谐振峰附近密集布置初始极点 | 强制无源性：Hamiltonian 矩阵检测虚轴特征值 |
| **多端口网络等值** ($N_p=8$) | 40-80 个极点（公共极点） | 1 Hz – 2 kHz（含 HVDC 特征谐波） | 对数分布，实部为虚部 1/100 | 采用 CVF 解除共轭约束，提升非对称响应拟合精度 |
| **电力电子阻抗** | 10-20 个极点 | 基波附近 ±1 kHz，关注非对称特性 | CVF 允许独立复极点 | 状态空间实现时注意开关动作引起的代数环 |

**关键经验公式**：
- **极点密度**：每 decade 频率范围至少 2-3 个极点，每个谐振峰需 2-4 个极点描述。
- **起始极点实部**：$\alpha = \beta/100$ 可有效避免宽频带拟合中的病态条件问题（条件数 $< 10^{10}$）。
- **迭代收敛**：通常 1-3 次迭代（标准 VF）或 3-5 次（Fast MVF）即可达到机器精度（RMS 误差 $< 10^{-10}$）。

## 4. 性能分析

基于 18 篇相关论文的实测数据汇总：

| 算法变体 | 实现平台 | 模型规模 | 精度指标 | 计算效率 | 内存占用 |
|---------|---------|---------|---------|---------|---------|
| **标准 VF (2004)** | MATLAB | 单端口，20 阶 | RMS 误差 $3.8\times10^{-12}$，极点相对误差 $10^{-7}$ | 1-3 次迭代收敛 | 标准稠密矩阵存储 |
| **Fast MVF (2009)** | MATLAB/C | 多端口，30 端口 | 小特征值误差 $<0.1\%$ | 总时间降低 20-25 倍，QR 步骤加速 92% | 降低 85%（稀疏存储） |
| **并行 CVF (2024)** | C + Intel MKL | 8 端口 FDNE | 宽频带拟合偏差 $<1\%$ | QR 分解占 95% 时间，并行效率 $>80\%$ | $O(N^2)$ 复杂度，状态矩阵维度 $N \cdot N_p \times N \cdot N_p$ |
| **RKF (2023)** | MATLAB | 三导体线路 | 与 VF 同精度 | 模型阶数降低 30-40% | 中等 |
| **Bode 法** | 商业软件 | 单端口 | 高频段误差大（$>10\%$） | 计算快但精度低 | 低 |

**计算瓶颈分析**：
- **QR 分解**：占 VF/CVF 总执行时间 95% 以上，是并行化核心目标。
- **状态空间矩阵**：维度随端口数平方增长 $(N \cdot N_p)^2$，大规模系统需采用分块并行策略。
- **无源性校正**：Hamiltonian 矩阵特征值计算增加 10-20% 开销，但避免时域仿真发散。

## 5. 最佳实践与注意事项

### 5.1 数据预处理
- **归一化**：将频响数据归一化至单位量级（如 $|H(s)|_{\max} = 1$），改善数值条件。
- **去噪**：对测量数据采用 Savitzky-Golay 滤波或加权最小二乘（WLS），降低高频噪声影响。
- **频率范围**：确保采样覆盖 DC（或极低频）至最高关注频率，避免外推误差。

### 5.2 无源性强制（Passivity Enforcement）
无源性破坏会导致时域仿真发散（能量非物理增长）。推荐流程：
1. **检测**：构造 Hamiltonian 矩阵 $\mathbf{M}$，检测纯虚数特征值 $\lambda = j\omega$。
2. **校正**：采用线性约束最小二乘（LC-LS）扰动传播矩阵对角元素，最小化参数修改量：
   $$\min \|\Delta \mathbf{H}\|_F \quad \text{s.t.} \quad \mathbf{H}_{\text{pert}}(j\omega) > 0, \forall \omega$$
3. **验证**：强制后重新检查特征值，确保无源性在整个频带内满足。

### 5.3 时延处理（ULM 模型）
对于长线路，直接拟合传播矩阵 $H(s)$ 需要高阶有理函数。建议：
- **时延提取**：先通过全通函数或 Bode 积分提取模态时延 $\tau_i$，拟合 $H(s)e^{s\tau_i}$ 的低通部分。
- **因果性保证**：确保拟合结果满足最小相位条件，传播速度不超过光速。

### 5.4 混合仿真接口
在电磁-机电暂态混合仿真中：
- **伴随仿真**：FDNE 切换时采用伴随仿真（热备用）初始化状态变量，可抑制虚假暂态，增加计算量约 14%。
- **临界电气距离**：建立电气距离 $D$ 与频率响应变化量 $\Delta E_{FR}$ 的关系，当 $D > D_{cr}$ 时无需更新 FDNE，可减少 60% 以上 FDNE 重计算。

## 6. 与其他方法的对比

| 方法 | 数学基础 | 优势 | 局限性 | 适用场景 |
|------|---------|------|--------|----------|
| **矢量拟合 (VF)** | 极点-留数迭代最小二乘 | 鲁棒性强，公共极点策略适合多端口，宽频带精度高 | 模型阶数可能偏高，需无源性后处理 | 电力系统 FDNE、电缆/线路建模 |
| **频域分区拟合 (FpF)** | 分段有理逼近 | 各频段可独立优化，适合强谐振系统 | 分段边界连续性需额外处理 | 谐振密集型网络（如谐波滤波器组） |
| **矩阵束法 (MPM)** | 奇异值分解 (SVD) | 无需迭代，计算速度快，适合实时应用 | 对噪声敏感，需预设模型阶数 | 在线监测、快速暂态识别 |
| **Loewner 矩阵 (LM)** | 数据驱动插值 | 自动模型降阶，适合大规模系统 | 可能产生非最小相位或不稳定极点 | 黑箱系统辨识、模型降阶 |
| **有理 Krylov 拟合 (RKF)** | 矩匹配/Krylov 子空间 | 模型阶数显著低于 VF，保持精度 | 恒定变换矩阵可能破坏无源性 | 输电线路宽频模型、大规模网络降阶 |
| **Bode 渐近法** | 渐近线近似 | 计算简单，物理意义明确 | 高频误差大（$>10\%$），难以处理密集谐振 | 早期 EMT 工具、教学演示 |

**选型建议**：
- **高精度离线仿真**：首选 VF 或 RKF，配合无源性强制。
- **实时仿真（RTDS）**：采用 Fast MVF 或 MPM，平衡精度与速度。
- **黑箱建模（无物理参数）**：Loewner 矩阵法，直接由测量数据构建。
- **超大规模系统（$N_p > 50$）**：分区 VF 结合并行计算（OpenMP/MPI）。

## 深度增强内容

### 矢量拟合 (Vector Fitting)

## 1. 核心原理详解

矢量拟合（Vector Fitting, VF）是一种鲁棒的频域有理函数逼近技术，通过迭代重定位极点将非线性优化问题转化为线性最小二乘（LS）问题。其核心思想是引入辅助函数 $\sigma(s)$ 将待拟合函数 $f(s)$ 的加权形式转化为线性形式。

### 1.1 标准矢量拟合（Standard VF）

对于单端口系统，标量传递函数 $f(s)$ 的有理逼近形式为：

$$f(s) \approx \sum_{n=1}^{N} \frac{r_n}{s - p_n} + d + s \cdot e$$

其中 $p_n$ 为极点，$r_n$ 为留数，$d$ 为直接耦合项，$e$ 为微分项。

VF通过引入辅助函数 $\sigma(s)$ 构造两个线性问题：

$$\sigma(s) f(s) \approx \sum_{n=1}^{N} \frac{\tilde{r}_n}{s - \tilde{p}_n} + \tilde{d}$$

$$\sigma(s) \approx 1 + \sum_{n=1}^{N} \frac{\tilde{r}_n'}{s - \tilde{p}_n}$$

通过求解 $\sigma(s) = 0$ 的零点获得更新后的极点 $p_n^{\text{new}}$，实现极点的重定位。

### 1.2 复数矢量拟合（Complex VF, CVF）

传统VF强制实数系统极点满足共轭对称（$p_{n+1} = p_n^*$），限制了非对称频响的拟合灵活性。CVF解除该约束，允许独立拟合复极点：

$$[Y(s)] \approx \sum_{m=1}^{M} \frac{R_m}{s - p_m} + D + sE$$

其中 $p_m$ 可为任意复数（无需共轭对），特别适用于基带频响或非对称系统。

### 1.3 模态矢量拟合（Modal VF, MVF）

针对多端口系统 $Y(s) \in \mathbb{C}^{N \times N}$，MVF先进行模态分解：

$$Y(s) = T \cdot \text{diag}(h_1(s), \dots, h_N(s)) \cdot T^{-1}$$

对每个模态 $h_i(s)$ 独立进行VF拟合，再利用稀疏矩阵结构求解：

- **极点识别**：利用块对角稀疏结构，计算复杂度从 $O(N^3)$ 降至 $O(N)$
- **留数识别**：逐行对称求解，利用矩阵对称性减少内存分配约85%

### 1.4 状态空间实现

拟合结果可转换为状态空间形式用于EMT仿真：

$$\dot{x} = Ax + Bu$$
$$y = Cx + Du$$

其中系统矩阵维度为 $(N \cdot N_p) \times (N \cdot N_p)$，$N$ 为端口数，$N_p$ 为每端口极点数。

## 2. 算法流程

### 阶段一：极点重定位（Pole Relocation）

1. **初始极点设置**  
   选择起始极点 $\tilde{p}_n$（建议：复数极点实部为虚部的 $1/100$，即 $\alpha = \beta/100$）：
   - 低频段：线性分布
   - 高频段：对数分布

2. **构建线性方程组**  
   在采样频率点 $s_k$ 处构建超定方程组：
   
   $$\begin{bmatrix} 
   \frac{1}{s_k-\tilde{p}_1} & \cdots & \frac{1}{s_k-\tilde{p}_N} & 1 & s_k & \frac{-f(s_k)}{s_k-\tilde{p}_1} & \cdots & \frac{-f(s_k)}{s_k-\tilde{p}_N}
   \end{bmatrix} 
   \begin{bmatrix} \tilde{r}_1 \\ \vdots \\ \tilde{r}_N \\ \tilde{d} \\ \tilde{e} \\ \tilde{r}_1' \\ \vdots \\ \tilde{r}_N' \end{bmatrix} 
   \approx 
   \begin{bmatrix} f(s_k) \end{bmatrix}$$

3. **QR分解求解**  
   通过QR分解求解最小二乘问题（此步骤占总计算时间95%以上）。

4. **极点更新**  
   求解 $\sigma(s) = 0$ 的特征值，实部为正则取负稳定化：
   $$p_n^{\text{stable}} = -\text{Re}(p_n) + j\text{Im}(p_n)$$

### 阶段二：留数识别（Residue Identification）

5. **固定极点求解留数**  
   将更新后的极点 $p_n^{\text{new}}$ 代入，求解线性方程组获得 $r_n, d, e$。

6. **收敛判断**  
   计算均方根误差（RMS）：
   $$\text{RMS} = \sqrt{\frac{1}{K} \sum_{k=1}^{K} |f(s_k) - \hat{f}(s_k)|^2}$$
   
   若相邻两次迭代误差变化小于阈值（如 $<10^{-6}$）或达到最大迭代次数，停止迭代；否则返回步骤1。

### 阶段三：无源性校正（Passivity Enforcement）

7. **无源性检验**  
   通过Hamiltonian矩阵纯虚数特征值或频率扫描检验无源性违规。

8. **扰动修正**  
   采用约束最小二乘或摄动法调整留数矩阵，确保所有频率点特征值为正。

## 3. 参数选取指南

| 应用场景 | 初始极点策略 | 模型阶数 | 特殊处理 |
|---------|-------------|---------|---------|
| **宽频带架空线** | 复数极点，$\alpha = \beta/100$，对数分布 | 20-40阶/模态 | 需处理传播时延，建议结合ULM |
| **海底电缆** | 低频密集分布（<1 Hz），高频稀疏 | 30-50阶 | 分离充电电流模态（小特征值） |
| **变压器建模** | 谐振峰附近密集布点 | 根据谐振峰数量×2 | 考虑铁芯非线性时需分段拟合 |
| **多端口FDNE** | 逆幅值加权预计算（MVF） | 公共极点策略 | 利用端口间耦合对称性 |
| **高频变压器** | 10 kHz-10 MHz覆盖 | 40-50阶 | 确保无源性，避免虚假振荡 |
| **机电-电磁混合仿真** | 1-2 kHz范围重点覆盖 | 足够覆盖12脉波谐波（11,13次） | 伴随仿真初始化状态变量 |

**关键参数建议：**

- **频率扫描范围**：至少覆盖10 MHz以确保捕获高频无源性违规，即使实际仿真带宽仅1 MHz
- **采样点数**：通常500-1000点，在谐振峰处需加密
- **迭代次数**：标准VF通常3-4次收敛；MVF通过预计算初始极点可降至3-5次（传统10-15次）
- **稳定性处理**：对正实部极点强制取负，确保 $\text{Re}(p_n) < 0$

## 4. 性能分析

| 性能指标 | 标准VF (2004) | MVF (2009) | CVF (2024) | 备注 |
|---------|--------------|-----------|-----------|------|
| **拟合精度 (RMS)** | $3.8\times10^{-12}$ (20阶)<br>$1.6\times10^{-12}$ (40阶) | <0.1% (小特征值) | 与VF相当 | 双精度机器精度量级 |
| **极点/留数精度** | 相对误差 $\sim 10^{-7}$ | - | - | - |
| **计算复杂度** | $O(N^3)$ | $O(N)$ (稀疏优化后) | $O(N^2)$ | $N$为端口数 |
| **迭代次数** | 1-3次 | 3-5次 (预计算后) | 3-5次 | MVF预计算减少约3倍迭代 |
| **计算加速比** | 基准 | 20-25倍 | 依赖并行核数 | MVF通过稀疏结构优化 |
| **内存优化** | 标准 | 降低85% | - | MVF逐行对称求解 |
| **QR分解占比** | >95% | >95% | >95% | 并行化关键瓶颈 |
| **状态空间维度** | $N\cdot N_p$ | $N\cdot N_p$ | $N\cdot N_p$ | 多端口系统维度爆炸问题 |

**多端口扩展性能：**

- **8端口FDNE**：CVF在解除共轭约束后保持宽频带高精度，状态空间矩阵维度为 $8N_p \times 8N_p$
- **30+端口系统**：MVF稀疏优化支持大规模系统，传统VF面临维度灾难

## 5. 最佳实践与注意事项

### 5.1 无源性保证
- **问题识别**：有理拟合可能在40 Hz附近产生深度约-40的负特征值，导致时域仿真发散
- **解决方案**：
  - 低频段（<1 Hz）拟合不良是主因，需增加低频采样点
  - 采用鲁棒无源性强制算法，仅扰动传播矩阵对角元素最小化精度损失
  - 使用Hamiltonian矩阵法精确识别无源性违规频段，避免频率扫描漏检

### 5.2 数值稳定性
- **初始极点选择**：避免实数初始极点，采用复数极点（实部为虚部1/100）可完全消除宽频带病态条件
- **小特征值处理**：高阻抗终端下，充电电流模态（小特征值）易被数值误差淹没，建议采用FLE（折叠线等效）分解分别拟合 $Y_{oc}$ 和 $Y_{sc}$

### 5.3 时延处理
- **长时延系统**：标准VF对长传输线（大时延）拟合困难，建议：
  - 使用ULM（Universal Line Model）分离模态时延
  - 采用全通函数迭代估计时延，确保因果性（传播速度不超过光速）
  - 避免Bode积分法在截止频率选取上的局限性

### 5.4 实现优化
- **并行计算**：QR分解占总时间95%，应优先使用Intel MKL等多线程库并行化
- **语言选择**：C语言+底层线性代数库（如MKL）实现较MATLAB可提升10倍以上性能
- **公共极点策略**：多端口系统共享极点可使时域卷积计算速度提高约2倍

### 5.5 模型降阶
- 在保证精度前提下，通过Rational Krylov Fitting (RKF) 或频域分区拟合（FpF）降低模型阶数
- 避免恒定变换矩阵（$T_{const}$）导致的无源性破坏（特定频率选择下）

## 6. 与其他方法的对比

| 特性 | 矢量拟合 (VF) | 矩阵束法 (MPM) | Loewner矩阵 (LM) | 有理Krylov (RKF) | Bode拟合 |
|------|--------------|---------------|-----------------|-----------------|---------|
| **数学基础** | 最小二乘迭代 | 奇异值分解 | 有理插值 | Krylov子空间 | 渐近逼近 |
| **非线性处理** | 迭代线性化 | 直接求解 | 直接求解 | 投影降阶 | 分段线性 |
| **模型阶数** | 中等 | 较低 | 较低 | **最低** | 较高 |
| **宽频带精度** | 高 | 中等 | 中等 | 高 | 低（高频差） |
| **无源性控制** | 需后处理 | 需后处理 | 需后处理 | 需后处理 | 难保证 |
| **多端口扩展** | 优秀（MVF） | 复杂 | 复杂 | 良好 | 差 |
| **计算效率** | 中等（QR主导） | 快 | 快 | 快 | 最快 |
| **初始参数敏感** | 是（极点初值） | 否 | 否 | 否 | 否 |
| **适用场景** | 通用EMT建模 | 模态参数识别 | 大规模数据驱动 | 严格降阶需求 | 教学/粗略估计 |

**方法选择建议：**

- **高精度EMT仿真**：首选VF或其变体（CVF/MVF），配合无源性强制
- **超大规模系统（端口>100）**：考虑LM或RKF降低计算负担
- **实时仿真需求**：RKF生成更低阶模型，或采用VF+模型降阶（MOR）
- **在线参数识别**：MPM无需迭代，适合实时监测
- **雷电/EMI分析**：必须采用VF类方法确保宽频带（0.01 Hz-10 MHz）精度，Bode法在相域误差显著

**混合策略**：现代FDNE工具常结合VF与优化算法（如遗传算法）自动确定最优阶数，或采用VF+FpF分段处理宽频带响应。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |

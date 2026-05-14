---
title: "电流轨迹相似性方法 (Current Trajectory Similarity)"
type: method
tags: [current-trajectory-similarity, pattern-recognition, protection, waveform, coherency-clustering, feature-extraction]
created: "2026-05-05"
updated: "2026-05-13"
---

# 电流轨迹相似性方法 (Current Trajectory Similarity)

## 定义

电流轨迹相似性方法是一类通过比较故障或运行过程中电流波形（或其变换后的特征表示）的几何形状、演化轨迹或统计特征来进行识别、分类或判据构造的技术路线。其核心思想是：**不同故障类型、不同故障位置、不同机组或不同工况所产生的电流暂态响应，在时域中会形成不同的"轨迹"；通过量化这些轨迹之间的相似性或距离，可以实现故障判别、机组分群、模型验证等目标。**

在 EMT 仿真语境中，电流轨迹通常定义为在故障时段 $[0,T]$ 内采样得到的电流向量序列 $\mathbf{i}(t_k)$，$k=1,2,\ldots,N$。轨迹相似性度量可以是时域波形直接比较、变换域特征比较、或基于动态时间规整的非刚性对齐比较。

核心相似性度量公式为归一化余弦相似度：

$$
S(\mathbf{i}_1, \mathbf{i}_2) = \frac{\mathbf{i}_1^\top \mathbf{i}_2}{\|\mathbf{i}_1\| \, \|\mathbf{i}_2\|}
$$

其中 $\mathbf{i}_1, \mathbf{i}_2$ 为两段归一化后的电流采样向量。$S \in [-1, 1]$，值越接近 1 表示两段轨迹方向越一致。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <filter id="shadow" x="-2" y="-2" width="12" height="12">
      <feDropShadow dx="1" dy="1" stdDeviation="2" flood-opacity="0.1"/>
    </filter>
  </defs>
  
  <rect width="900" height="520" fill="#ffffff" rx="8"/>
  
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a1a" font-family="sans-serif">电流轨迹相似性方法体系架构</text>
  
  <!-- Layer 1: Input (Blue) -->
  <rect x="50" y="55" width="180" height="60" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="140" y="78" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af" font-family="sans-serif">原始电流信号</text>
  <text x="140" y="96" text-anchor="middle" font-size="11" fill="#3b82f6" font-family="sans-serif">i(t) 采样序列</text>
  
  <line x1="230" y1="85" x2="290" y2="85" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 2: Preprocessing (Light Blue) -->
  <rect x="290" y="55" width="180" height="60" rx="8" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)"/>
  <text x="380" y="78" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d4ed8" font-family="sans-serif">预处理</text>
  <text x="380" y="96" text-anchor="middle" font-size="11" fill="#60a5fa" font-family="sans-serif">滤波 / 同步 / 窗口截取</text>
  
  <line x1="470" y1="85" x2="530" y2="85" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 3: Feature Extraction (Green) -->
  <rect x="530" y="55" width="180" height="60" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="620" y="78" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803d" font-family="sans-serif">特征提取</text>
  <text x="620" y="96" text-anchor="middle" font-size="11" fill="#22c55e" font-family="sans-serif">包络线 / 小波 / 暂态特征</text>
  
  <line x1="620" y1="115" x2="620" y2="150" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 4: Similarity Metrics (Yellow) -->
  <rect x="60" y="150" width="220" height="70" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="170" y="175" text-anchor="middle" font-size="13" font-weight="bold" fill="#b45309" font-family="sans-serif">时域直接度量</text>
  <text x="170" y="195" text-anchor="middle" font-size="11" fill="#f59e0b" font-family="sans-serif">余弦相似度 / 欧氏距离</text>
  <text x="170" y="210" text-anchor="middle" font-size="10" fill="#d97706" font-family="sans-serif">Minkowski 距离</text>
  
  <rect x="310" y="150" width="220" height="70" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="420" y="175" text-anchor="middle" font-size="13" font-weight="bold" fill="#b45309" font-family="sans-serif">动态时间规整</text>
  <text x="420" y="195" text-anchor="middle" font-size="11" fill="#f59e0b" font-family="sans-serif">DTW 最优对齐路径</text>
  <text x="420" y="210" text-anchor="middle" font-size="10" fill="#d97706" font-family="sans-serif">非刚性时间偏移鲁棒</text>
  
  <rect x="560" y="150" width="220" height="70" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="670" y="175" text-anchor="middle" font-size="13" font-weight="bold" fill="#b45309" font-family="sans-serif">变换域特征度量</text>
  <text x="670" y="195" text-anchor="middle" font-size="11" fill="#f59e0b" font-family="sans-serif">小波能量 / FFT 频谱</text>
  <text x="670" y="210" text-anchor="middle" font-size="10" fill="#d97706" font-family="sans-serif">包络线结构相似度 STS</text>
  
  <line x1="450" y1="220" x2="450" y2="255" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 5: Distance Matrix (Light Purple) -->
  <rect x="280" y="255" width="340" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="450" y="278" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6" font-family="sans-serif">距离矩阵 D<sub>mn</sub> = d(f<sub>m</sub>, f<sub>n</sub>)</text>
  <text x="450" y="296" text-anchor="middle" font-size="11" fill="#8b5cf6" font-family="sans-serif">M×M 相似性矩阵 (M = 机组数)</text>
  
  <line x1="450" y1="310" x2="450" y2="345" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 6: Clustering (Orange) -->
  <rect x="60" y="345" width="220" height="70" rx="8" fill="#ffedd5" stroke="#ea580c" stroke-width="2" filter="url(#shadow)"/>
  <text x="170" y="370" text-anchor="middle" font-size="13" font-weight="bold" fill="#c2410c" font-family="sans-serif">K-means 聚类</text>
  <text x="170" y="390" text-anchor="middle" font-size="11" fill="#f97316" font-family="sans-serif">WCSS 目标函数优化</text>
  <text x="170" y="405" text-anchor="middle" font-size="10" fill="#ea580c" font-family="sans-serif">K-Means++ / KD树加速</text>
  
  <rect x="310" y="345" width="220" height="70" rx="8" fill="#ffedd5" stroke="#ea580c" stroke-width="2" filter="url(#shadow)"/>
  <text x="420" y="370" text-anchor="middle" font-size="13" font-weight="bold" fill="#c2410c" font-family="sans-serif">谱聚类</text>
  <text x="420" y="390" text-anchor="middle" font-size="11" fill="#f97316" font-family="sans-serif">拉普拉斯矩阵特征分解</text>
  <text x="420" y="405" text-anchor="middle" font-size="10" fill="#ea580c" font-family="sans-serif">DBI 自动确定 K 值</text>
  
  <rect x="560" y="345" width="220" height="70" rx="8" fill="#ffedd5" stroke="#ea580c" stroke-width="2" filter="url(#shadow)"/>
  <text x="670" y="370" text-anchor="middle" font-size="13" font-weight="bold" fill="#c2410c" font-family="sans-serif">层次聚类</text>
  <text x="670" y="390" text-anchor="middle" font-size="11" fill="#f97316" font-family="sans-serif">凝聚 / 分裂策略</text>
  <text x="670" y="405" text-anchor="middle" font-size="10" fill="#ea580c" font-family="sans-serif">树状图可视化</text>
  
  <line x1="450" y1="415" x2="450" y2="450" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 7: Output (Purple) -->
  <rect x="200" y="450" width="500" height="55" rx="8" fill="#e9d5ff" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="450" y="473" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6" font-family="sans-serif">同调机群划分 → 参数聚合 → 等值模型</text>
  <text x="450" y="492" text-anchor="middle" font-size="11" fill="#8b5cf6" font-family="sans-serif">仿真效率提升 ~90% | 动态响应精度 > 98%</text>
  
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 电流轨迹相似性方法体系架构：从原始电流信号到同调机群分群的完整流程</p>

## EMT 中的角色

在 EMT 仿真与分析中，电流轨迹相似性方法承担三类核心角色：

1. **保护判据设计**：利用故障电流波形的轨迹特征（如波头形状、上升速率、包络线形态）构造故障检测与类型识别判据。在直流故障中，故障电流的上升速率和包络线形状是区分金属性短路和高阻抗故障的关键特征。
2. **机群同调分群**：在大规模风电场或机组群的 EMT 分析中，利用各机组故障电流轨迹的相似性进行聚类分群，将暂态响应相似的机组合并为等值机，实现模型降阶。
3. **模型验证与比对**：比较不同模型（详细模型 vs 等值模型、不同参数设置、不同控制策略）产生的电流轨迹，量化模型保真度。

## 核心机制

### 1. 时域波形直接相似度

最直接的轨迹相似性度量是在时域中对原始电流波形进行比较。

**余弦相似度（Cosine Similarity）**：

$$
S_{\cos}(\mathbf{i}_a, \mathbf{i}_b) = \frac{\sum_{k=1}^{N} i_{a,k} \cdot i_{b,k}}{\sqrt{\sum_{k=1}^{N} i_{a,k}^2} \cdot \sqrt{\sum_{k=1}^{N} i_{b,k}^2}}
$$

物理含义：衡量两段电流轨迹在 $N$ 维采样空间中的夹角余弦。对幅值缩放不变，适用于比较波形形状而非绝对幅值。

**欧氏距离（Euclidean Distance）**：

$$
d_{\text{Euc}}(\mathbf{i}_a, \mathbf{i}_b) = \sqrt{\sum_{k=1}^{N} (i_{a,k} - i_{b,k})^2}
$$

物理含义：两段电流轨迹在采样空间中的直线距离。对幅值和相位偏移均敏感，适用于需要同时考虑波形形状和幅值差异的场景。

**闵可夫斯基距离（Minkowski Distance）**（欧氏距离的广义形式）：

$$
d_p(\mathbf{i}_a, \mathbf{i}_b) = \left( \sum_{k=1}^{N} |i_{a,k} - i_{b,k}|^p \right)^{1/p}
$$

当 $p=2$ 时退化为欧氏距离，$p=1$ 时为曼哈顿距离。参数 $p$ 控制对异常点的敏感度——$p$ 越大，距离受大偏差采样点的影响越显著。

**连续时间形式**（适用于连续信号）：

$$
d_p(\mathbf{i}_a, \mathbf{i}_b) = \left( \int_0^T \| \mathbf{i}_a(t) - \mathbf{i}_b(t) \|^p \, dt \right)^{1/p}
$$

### 2. 动态时间规整（Dynamic Time Warping, DTW）

当两段电流轨迹在时间轴上存在非刚性偏移（如故障检测延迟不同、采样起始时刻不一致）时，欧氏距离和余弦相似度会给出误导性结果。DTW 通过寻找最优对齐路径来克服这一问题。

**DTW 距离定义**：

给定两条轨迹 $\mathbf{A} = (a_1, \ldots, a_N)$ 和 $\mathbf{B} = (b_1, \ldots, b_M)$，构建 $N \times M$ 的成本矩阵 $D$，其中 $D_{i,j} = |a_i - b_j|$。DTW 距离为从 $(1,1)$ 到 $(N,M)$ 的最小累积路径成本：

$$
\text{DTW}(\mathbf{A}, \mathbf{B}) = \min_{\pi} \sqrt{\sum_{(i,j) \in \pi} D_{i,j}^2}
$$

其中 $\pi$ 为满足单调性和连续性约束的对齐路径。

**物理意义**：DTW 允许将一段轨迹的某个时间点"拉伸"或"压缩"以匹配另一段轨迹的对应点，从而在存在时间偏移的情况下仍能正确评估波形相似性。在故障电流轨迹比较中，DTW 对检测延迟和保护动作时序差异具有鲁棒性。

### 3. 包络线轨迹相似度

在 Ouyang 等（2017）提出的 DFIG 风电机群同调分群方法中，核心创新是**提取短路电流包络线作为轨迹特征**，而非直接使用原始瞬时电流值。

**包络线提取**：对故障电流 $i(t)$，其包络线 $\hat{i}(t)$ 可通过以下方式获得：
- 包络检波：取局部极大值的平滑插值
- Hilbert 变换：$\hat{i}(t) = | \mathcal{H}\{i(t)\} |$，其中 $\mathcal{H}$ 为 Hilbert 变换算子
- 滑动窗口最大值：$\hat{i}(t) = \max_{\tau \in [t-W, t]} |i(\tau)|$

**包络线轨迹结构相似度**：定义两条包络线轨迹 $\hat{i}_a(t)$ 和 $\hat{i}_b(t)$ 的结构相似度为：

$$
\text{STS}(\hat{i}_a, \hat{i}_b) = \alpha \cdot S_{\cos}(\hat{i}_a, \hat{i}_b) + (1-\alpha) \cdot \left(1 - \frac{d_{\text{Euc}}(\hat{i}_a, \hat{i}_b)}{\max(\|\hat{i}_a\|, \|\hat{i}_b\|)}\right)
$$

其中 $\alpha \in [0,1]$ 为形状权重系数，用于平衡形状相似性和幅值相似性的贡献。

**物理洞察**：包络线滤除了工频振荡成分，突出故障电流的直流分量和衰减趋势——这正是决定机组间暂态行为差异的关键特征。Ouyang 等（2017）证明，基于包络线轨迹的相似度能够有效区分 DFIG 机组在故障期间的不同响应行为（如转子保护动作 vs 未动作、不同故障前有功出力水平等）。

### 4. 变换域特征相似度

在噪声较强或高频振荡干扰显著的场景中，直接在时域比较原始电流波形效果有限。变换域方法先将电流投影到另一个表征空间，再比较特征向量。

**小波变换特征**：对电流 $i(t)$ 进行离散小波变换（DWT），提取各尺度的细节系数 $d_j[k]$ 和近似系数 $a_j[k]$，构造特征向量：

$$
\mathbf{f}_{\text{wavelet}} = \left[ E_1, E_2, \ldots, E_J, \|a_J\|_2 \right]
$$

其中 $E_j = \sum_k |d_j[k]|^2$ 为第 $j$ 层细节系数的能量，$J$ 为分解层数。 Liu 等（2009）将小波奇异熵理论应用于暂态保护，证明小波变换能够有效提取故障特征并在噪声环境下保持判别力。

**傅里叶变换特征**：对故障电流窗口进行 FFT，提取频谱幅值和相位特征：

$$
\mathbf{f}_{\text{FFT}} = \left[ |I(f_1)|, |I(f_2)|, \ldots, |I(f_K)|, \angle I(f_1), \ldots, \angle I(f_K) \right]
$$

适用于稳态谐波特征比较和频域保护判据。

**暂态特征提取**：从电流波形中提取物理可解释的特征量，如：
- 波头到达时间 $t_{\text{head}}$
- 峰值电流 $I_{\text{peak}}$
- 峰值时刻 $t_{\text{peak}}$
- 上升速率 $\frac{di}{dt}|_{\max}$
- 过零时刻 $t_{\text{zero}}$
- 波形因子 $k_f = \frac{I_{\text{rms}}}{I_{\text{avg}}}$

## 形式化表达

### 相似性度量体系总览

| 度量方法 | 公式 | 不变性 | 适用场景 |
|---------|------|--------|---------|
| 余弦相似度 | $\frac{\mathbf{i}_a^\top \mathbf{i}_b}{\|\mathbf{i}_a\|\|\mathbf{i}_b\|}$ | 幅值缩放不变 | 波形形状比较 |
| 欧氏距离 | $\sqrt{\sum (i_{a,k}-i_{b,k})^2}$ | 无 | 幅值+形状综合比较 |
| DTW 距离 | $\min_{\pi}\sqrt{\sum D_{i,j}^2}$ | 时间偏移鲁棒 | 非刚性对齐比较 |
| 包络线 STS | $\alpha S_{\cos} + (1-\alpha)(1-d_{\max})$ | 幅值+形状加权 | 机组分群、故障判别 |
| 小波能量比 | $\sum |d_j|^2 / \sum |i_k|^2$ | 噪声鲁棒 | 噪声环境特征提取 |

### 聚类分群框架

对于 $M$ 台机组的电流轨迹集合 $\{\mathbf{i}_1, \mathbf{i}_2, \ldots, \mathbf{i}_M\}$，聚类分群流程为：

1. **特征提取**：对每台机组 $m$，提取轨迹特征向量 $\mathbf{f}_m$（包络线、小波特征或暂态特征）
2. **距离矩阵计算**：计算所有机组对之间的相似性/距离矩阵 $D_{mn} = d(\mathbf{f}_m, \mathbf{f}_n)$
3. **聚类算法**：应用 K-means、谱聚类或层次聚类进行分群
4. **参数聚合**：对同一群内的机组，按容量加权或等比例聚合控制参数和电气参数

Xu 等（2026）提出的增强型 K-means 两步聚类法在特征提取后增加了 K-Means++ 概率初始化、KD 树加速搜索和 Davies-Bouldin 指数自动确定最优聚类数 $K$，其 WCSS 目标函数为：

$$
\text{WCSS} = \sum_{j=1}^{K} \sum_{\mathbf{x} \in C_j} \|\mathbf{x} - \boldsymbol{\mu}_j\|^2
$$

其中 $\boldsymbol{\mu}_j$ 为第 $j$ 类的聚类中心。

## 关键技术挑战

### 1. 采样同步与对齐

电流轨迹比较的前提是各轨迹在时间上严格对齐。在实际保护系统中，故障检测时刻、采样启动时刻和保护动作时序的差异会导致时间偏移。DTW 可以部分缓解这一问题，但会引入计算复杂度。对于实时保护应用，通常采用固定时间窗口对齐或事件触发对齐策略。

### 2. 噪声与高频振荡抑制

EMT 仿真中的数值振荡和实际测量中的传感器噪声会显著影响波形相似度度量。Liu 等（2009）证明小波奇异熵在噪声环境下仍保持较好的特征判别能力。实际应用中，通常在相似度计算前对电流信号进行滤波预处理（如 [[filtering]] 所述）。

### 3. 特征选择与维度灾难

高维特征向量（如全波形采样点）可能引发维度灾难，导致距离度量失效。Xu 等（2026）通过 KD 树将高维最近邻搜索的时间复杂度从 $O(a \cdot K \cdot D)$ 降至 $O(a \cdot \log(a) \cdot D)$，其中 $a$ 为样本数，$K$ 为聚类数，$D$ 为特征维度。

### 4. 工况泛化能力

基于特定工况（如三相短路）训练的轨迹相似度判据，在不对称故障、高阻抗故障或不同电网强度下可能失效。Ouyang 等（2017）的算例验证了该方法在 DFIG 风电机群中的有效性，但未覆盖不对称故障、不同风速分布和不同控制策略的交叉验证。

## 量化性能边界

| 指标 | 数值 | 来源 | 条件 |
|------|------|------|------|
| 包络线 STS 区分 DFIG 机组暂态差异 | 有效 | Ouyang 等 2017 | 三相短路故障，DFIG 风电场 |
| 增强 K-means 聚类搜索加速比 | 约 75%（降至 25.1%） | Xu 等 2026 | KD 树加速，20 台 DFIG |
| 等值模型仿真时间缩减 | 约 90% | Xu 等 2026 | 20 台 DFIG 聚合为等值机 |
| 等值模型动态响应精度 | > 98% | Xu 等 2026 | RMSE < 2%，PCC 三相电压跌落 0.2 p.u. |
| DBI 自动确定最优聚类数 | K=2 | Xu 等 2026 | Davies-Bouldin 指数最小化 |
| 小波奇异熵噪声鲁棒性 | 有效 | Liu 等 2009 | 暂态保护加速跳闸场景 |

> 注：以上量化数据来自各论文的算例验证，实际应用中需根据具体系统参数和故障场景重新评估。

## 适用边界与选择指南

### 方法选择指南

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|------|
| 机组同调分群（风电场/机群等值） | 包络线 STS + K-means | Ouyang 等 2017 验证有效，物理可解释性强 |
| 实时故障检测与分类 | 暂态特征 + 阈值判据 | 计算量低，适合实时保护 |
| 噪声环境下的特征提取 | 小波变换 + 奇异熵 | Liu 等 2009 证明噪声鲁棒性 |
| 时间偏移鲁棒的波形比较 | DTW | 对检测延迟和采样偏移不敏感 |
| 频域保护判据 | FFT 频谱特征 | 适用于稳态谐波分析和阻抗相关判据 |
| 模型保真度验证 | 余弦相似度 + 欧氏距离 | 直接量化波形差异 |

### 适用条件

- 采样率足够高以捕捉关键暂态特征（通常 ≥ 10 kHz）
- 电流波形具有可区分的形状特征（故障类型、位置或机组响应差异明显）
- 轨迹窗口覆盖完整的暂态过程（通常从故障发生到保护动作或稳态恢复）

### 失效边界

- 故障电流幅值差异极小且波形形状高度相似时，相似度判据区分力不足
- 采样同步误差超过 DTW 允许的对齐窗口时，可能产生错误对齐
- 强电磁干扰或传感器饱和导致波形严重失真时，所有基于波形的相似度度量均失效
- 未经验证的新故障类型（如新型直流故障）可能不在参考轨迹库覆盖范围内

## 相关方法

- [[coherency-clustering]] — 同调聚类：基于暂态响应相似性进行机组分群的上位概念
- [[dc-protection]] — 直流保护：波形相似性可用于故障判据设计
- [[digital-distance-protection]] — 数字距离保护：电流/电压轨迹特征可服务保护算法
- [[distance-protection]] — 距离保护：阻抗轨迹与电流轨迹的关联
- [[filtering]] — 信号滤波：轨迹特征提取前的预处理步骤
- [[fault-analysis]] — 故障分析：故障工况是轨迹相似性方法的典型激励背景
- [[impedance-relay]] — 阻抗继电器：阻抗轨迹与电流轨迹的互补关系
- [[protection-system]] — 保护系统：保护算法与判据设计的上位背景
- [[signal-processing]] — 信号处理：波形变换和特征提取的基础方法

## 来源论文

- **Ouyang 等 (2017)** — "基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法"，中国电机工程学报，37(10):2896-2904。提出基于短路电流包络线轨迹结构相似度的 DFIG 风电机群电磁暂态同调分群方法，是电流轨迹相似性在 EMT 机群等值中的奠基性工作。
- **Xu 等 (2026)** — "An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on LVRT characteristics"，Electric Power Systems Research。提出基于 LVRT 特性的增强型 K-means 两步聚类法，融合 K-Means++ 初始化、KD 树加速和 DBI 自动确定聚类数，等值精度 > 98%，仿真时间减少 90%。
- **Liu 等 (2009)** — "Application of wavelet singular entropy theory in transient protection and accelerated trip of transmission line"。将小波奇异熵理论应用于线路暂态保护，证明小波变换在噪声环境下仍保持特征判别能力。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |

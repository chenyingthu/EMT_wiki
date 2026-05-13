---
title: "Coherency Clustering"
type: method
tags: [coherency-clustering, dynamic-equivalent, wind-farm, clustering, k-means, aggregation, model-reduction]
created: "2026-05-04"
updated: "2026-05-13"
---

# Coherency Clustering

## 定义

同调聚类（Coherency Clustering）指根据设备或机组在电磁暂态（EMT）过程中的动态响应相似性，将多台设备划分为若干"同调群"（coherent group），每个群可用一台等值机组表示。其核心思想是：在故障暂态期间，若多台机组的暂态响应（如短路电流包络线、有功功率跌落-恢复轨迹、转子角偏差等）在给定时间窗内高度相似，则它们在电磁暂态意义上是"同调"的，可以合并为一个等值单元。

在 EMT 仿真中，同调聚类是模型降阶（model order reduction）和动态等值（dynamic equivalent modeling）的关键前置步骤。大型风电场、光伏场或同步机群包含数十至数百台机组，逐台详细建模会导致节点数量爆炸（"维数灾难"），同调聚类通过识别响应相似机组实现模型降阶，在保持关键动态特性的同时大幅降低计算负担。

核心相似性度量公式：对任意两台机组 $i, j$，其响应向量 $\mathbf{x}_i(t), \mathbf{x}_j(t)$ 在故障时段 $[0, T]$ 内的距离为：

$$
d_{ij} = \left( \int_0^T \|\mathbf{x}_i(t) - \mathbf{x}_j(t)\|^p \, dt \right)^{1/p}
$$

当 $d_{ij} < \varepsilon_{\text{cluster}}$（聚类阈值）时，两机组归入同一同调群。实际应用中 $\mathbf{x}_i$ 可选为故障电流包络线、LVRT 响应曲线、转子角轨迹或有功-无功联合特征；阈值 $\varepsilon_{\text{cluster}}$ 和范数阶次 $p$ 由具体聚类算法和验证工况决定。

## EMT 中的角色

### 为什么需要同调聚类

大规模新能源场站（风电场、光伏场）接入电网后，EMT 仿真面临两大挑战：

1. **计算复杂度**：逐台详细建模导致节点数与机组数成正比，矩阵求逆复杂度 $O(n^3)$ 迅速增长
2. **实时性**：RTDS 等实时仿真器硬件资源有限，无法容纳数百台详细机组模型

同调聚类通过将响应相似的机组合并为等值机组，将原始 $N$ 台机组降阶为 $K$ 台等值机组（$K \ll N$），从而：
- 减少网络节点数和导纳矩阵维度
- 降低单步计算量和总仿真时间
- 保留场站关键动态特性（故障响应、保护动作、电压恢复）

### 核心挑战

- **特征量选择**：稳态参数（如风速、容量）不足以反映暂态同调性，需选取能同时捕捉控制动态和保护动作的特征量
- **阈值确定**：聚类阈值和簇数 $K$ 需有客观依据，而非主观指定
- **场景通用性**：不同故障类型、不同运行工况下分群结果可能不同，在线分析需频繁重分群
- **等值精度**：降阶后等值模型与详细模型的误差需控制在可接受范围内

## 核心机制

### 方法一：基于电流轨迹结构相似度的分群（Ouyang 2017）

**原理**：欧阳金鑫等（2017）提出基于短路电流包络线轨迹结构相似度的 DFIG 风电机群同调分群方法。该方法的核心输入是故障后各台 DFIG 的短路电流时域波形，核心特征量是由三相电流或 $\alpha\beta$ 坐标电流得到的电流包络线轨迹。

其思想不是直接比较某一时刻的电流峰值，而是比较一个暂态时间窗内整条电流轨迹的结构形态：若两台机组电流包络线在故障初期衰减、振荡、控制保护动作后的变化趋势相近，则认为它们在电磁暂态意义下同调。

**实现流程**：
1. 对每台 DFIG 获取故障电流时域波形
2. 提取反映暂态强度与变化趋势的包络线
3. 对任意两台机组计算轨迹相似度或差异度
4. 形成相似度矩阵
5. 依据相似度评价规则进行机群划分
6. 对每个群构建等值机

**特点**：分群变量直接取自故障电流响应，能够同时反映风速差异、电气距离差异、控制器暂态响应和保护动作（如 Crowbar 投切）差异，比仅按容量或拓扑位置划分更贴近 EMT 等值需求。

**验证**：在双馈风电场并网系统 EMT 仿真算例中验证了该方法能有效辨别 DFIG 暂态过程差别。

### 方法二：增强 K-means 两阶段聚类（Xu 2026）

**原理**：Xu 等（2026）针对 DFIG 风电场 LVRT 特性提出增强 K-means 两阶段聚类方法，解决传统 K-means 依赖主观参数（初始中心、簇数）的问题。

**第一阶段——按有功功率输出预分类**：

根据机组实时有功功率输出 $P$ 和 LVRT 响应特征，将全部机组分为两类：具有聚类特性的机组和不具有聚类特性的机组。基于 LVRT 动态响应分析，功率阈值划分为四个运行区（见公式 18）：

$$
V(X) = V_0 \left(1 - \frac{C_T}{2} \frac{\partial X}{r_0^2} \right)^{1/2}
$$

其中 $V_0$ 为原始风速（3–13 m/s），$C_T$ 为推力系数（0.8），$\partial$ 为尾流衰减系数（0.075），$r_0$ 为叶片半径（38 m）。

- 启动区（A–B）：$P < 0.072$ p.u.
- MPPT 区（B–C）：$0.072 \leq P < 0.91$ p.u.
- 恒速区（C–D）：$0.91 \leq P < 1.0$ p.u.
- 恒功率区（D–E）：$P = 1.0$ p.u.

A–B、C–D、D–E 区内机组响应曲线形状、跌落深度和恢复轨迹高度相似，归为"有聚类特性"类；MPPT 区（B–C）机组因转速调节跟踪 $C_p$ 导致有功波动较大，归为"无聚类特性"类，进入第二阶段二次聚类。

**第二阶段——增强 K-means 聚类**：

对 MPPT 区机组应用增强 K-means 算法，包含三项改进：

**(1) K-means++ 初始中心选择**：

首先从数据集中随机选择一个数据点 $c_1$ 作为第一个中心。对每个未选为中心的点 $x$，计算其到已有中心的最小欧氏距离：

$$
D(x) = \sqrt{\sum_{d=1}^{D} (x_d - c_{i_d})^2}
$$

基于最小距离计算被选为下一个中心的概率：

$$
P(x) = \frac{D^2(x)}{\sum_{y \in T \setminus t} D^2(y)}
$$

**(2) KD-tree 加速搜索**：

对数据集 $T$ 构建 KD-tree 索引（维度 $D=3$，特征为 $P, V_w, C_p$）。递归构建过程：

计算各维度方差：

$$
\text{Var}(X_d) = \frac{1}{a-1} \sum_{i=1}^{a} (v_{di} - \mu_d)^2
$$

选择方差最大维度 $d^* = \arg\max_d \text{Var}(X_d)$ 作为分割轴，取中位数作为当前节点，较小值归左子树，较大值归右子树，交替选择分割维度。

传统 K-means 分配阶段复杂度为 $O(a \cdot K \cdot D)$，KD-tree 加速后降至 $O(a \cdot \log a \cdot D)$。测试表明该方法每次迭代仅消耗传统方法 25.1% 的运行时间，数据搜索时间减少约 75%。

**(3) Davies-Bouldin Index (DBI) 自动确定簇数**：

对候选簇数 $K \in \{2, 3, \cdots, a\}$，计算 DBI 并取最小值对应的 $K$ 为最优簇数：

$$
S_i = \frac{1}{|C_i|} \sum_{x \in C_i} \|x - \mu_i\|
$$

$$
DBI = \frac{1}{K} \max_{i \neq j} \frac{S_i + S_j}{\|\mu_i - \mu_j\|}
$$

其中 $S_i$ 和 $S_j$ 分别为第 $i$ 和第 $j$ 簇的簇内离散度，$\|\mu_i - \mu_j\|$ 为簇心间距离。DBI 最小化等价于最大化簇内紧密度与簇间分离度的比值。

**等值参数计算**：

对聚类结果，等值机组参数采用倒数平均（并联等效）：

$$
S_{eq} = \sum_{i=1}^{N} S_i = N_S, \quad P_{eq} = \sum_{i=1}^{N} P_i = N_P, \quad Q_{eq} = \sum_{i=1}^{N} Q_i = N_Q
$$

$$
X_{m,eq} = \frac{X_m}{N}, \quad X_{s,eq} = \frac{X_s}{N}, \quad X_{r,eq} = \frac{X_r}{N}
$$

$$
R_{s,eq} = \frac{R_s}{N}, \quad R_{r,eq} = \frac{R_r}{N}, \quad C_{eq} = N C, \quad Z_{T,eq} = \frac{Z_T}{N}
$$

集电系统等值阻抗采用线损等效模型：

$$
Z_{equ} = \frac{\sum_{i=1}^{n} I_i^2 Z_i}{\left(\sum_{i=1}^{n} I_i\right)^2}
$$

**验证结果**：

在 20 台 2.25 MW DFIG 风电场（PSCAD/EMTDC 验证）中：
- 等值模型在故障期间与详细模型精度 > 98%
- 仿真时间减少约 90%
- RMSE 误差公式：

$$
E = \sqrt{\frac{1}{m} \sum_{i=1}^{m} \left(\frac{A_i - A_{eqi}}{A_i}\right)^2}
$$

其中 $m$ 为采样点数，$A_i$ 和 $A_{eqi}$ 分别为详细模型和等值模型的电气量。

### 方法三：基于动态行为相似性的通用等值模型（Li 2025）

**原理**：Li 等（2025）针对永磁直驱风电场（PMSG）提出基于单机模型扩展的通用等值模型构建方法。与传统机理等值不同，该方法通过神经网络学习单台 PMSG 的暂态响应特性，再通过输入参数等效计算将单机模型扩展至风电场，无需在不同工况下重新分群。

**神经网络通用模型结构**：

$$
\hat{i}_{t+1} = f(i_{t-k:t}, u_{t-k:t}, s)
$$

其中 $i_{t-k:t}$ 为历史电流序列，$u_{t-k:t}$ 为历史电压序列，$s$ 为静态参数（风速、拓扑阻抗等），$f(\cdot)$ 为神经网络预测模型。

网络结构包含：
- **时序参数输入模块**：多层卷积层提取电压/电流时序特征（8×21 维度输入）
- **风速输入模块**：风速作为静态参数，在暂态短时间内视为恒定
- **准稳态参考值输入模块**：基于故障稳态模型的电流参考值

故障稳态电流输出特性：

$$
\begin{cases}
\hat{i}_{+d} = \min\{\hat{i}_{+d,\text{ref},1}, \hat{i}_{+d,\text{max}}\} \\
\hat{i}_{+q} = -K_+(0.9 - u_+)I_N \\
\hat{i}_{-d} = -K_- u_- I_N \\
\hat{i}_{-q} = -K_- u_- I_N
\end{cases}
$$

其中 $K_+, K_-$ 为正/负序无功电流比例系数，$u_+$ 为机端正序电压标幺值，$I_N$ 为额定电流。

**风电场扩展——输入参数等效**：

通过 PCC 处量测电压对各 PMSG 机端电压进行估计（前推-回代法），计算平均正/负序电压相量：

$$
\dot{U}_{\text{avg}}^+ = \frac{1}{N'} \sum_{i=1}^{N'} \dot{U}_{t,i}^+
$$

等效旋转轴与 PCC 同步旋转轴夹角：

$$
\Delta\theta_{\text{PLL}} = \arctan\left(\frac{u_{+q,\text{pcc}}}{u_{+d,\text{pcc}}}\right)
$$

等效负序旋转轴夹角：

$$
\Delta\phi_{\text{avg}} = \phi_{u,\text{avg}}^+ - \Delta\theta_{\text{PLL}}
$$

等值风速计算公式：

$$
V_{w,\text{eq}} = f_v^{-1}\left(\frac{1}{N'} \sum_{i=1}^{N'} f_v(V_{w,i})\right)
$$

**验证**：在基于江苏如东某风电场的 CloudPSS 平台验证中，该通用等值模型在各类运行工况下均无须改变分群，准确度高于单机等值模型但低于四机等值模型，更适合在线分析场景。训练集包含 200 个不同运行场景的仿真结果，测试集 50 个。

### 方法四：延迟解耦与多级嵌套快速同时求解（Liu 2025）

**原理**：Liu 等（2025）提出基于延迟解耦（latency decoupling）和多级嵌套快速同时求解（M-NFSS）的 DFIG 风电场实时仿真模型，在减少节点数的同时保留内部细节。

**DFIG 延迟解耦建模**：

DFIG 数学模型包含电压方程、磁链方程和转子机械方程：

$$
\mathbf{U}_{abcs} = R_s \mathbf{I}_{abcs} + \frac{d\boldsymbol{\psi}_{abcs}}{dt}
$$

$$
\mathbf{U}_{abcr} = R_r \mathbf{I}_{abcr} + \frac{d\boldsymbol{\psi}_{abcr}}{dt}
$$

$$
\boldsymbol{\psi}_{abcs} = (L_{ls} + L_m)\mathbf{I}_{abcs} + n_1 L_m \mathbf{I}_{abcr} e^{j\theta_r}
$$

$$
\boldsymbol{\psi}_{abcr} = (L_{lr} + n_1^2 L_m)\mathbf{I}_{abcr} + n_1 L_m \mathbf{I}_{abcs} e^{-j\theta_r}
$$

$$
J\frac{d\omega_r}{dt} = T_e - T_m - K_D\omega_r
$$

通过隐式欧拉法离散化并采用延迟解耦，将定子与转子之间的互导纳延迟至上一时刻，使节点导纳矩阵简化：

$$
\mathbf{I}_{abcs}(t) = \begin{bmatrix} G_{11} & G_{12} \end{bmatrix} \mathbf{U}_{abcs}(t-\Delta t) + \hat{\mathbf{I}}_s(t-\Delta t)
$$

$$
\mathbf{I}_{abcr}(t) = \begin{bmatrix} G_{21} & G_{22} \end{bmatrix} \mathbf{U}_{abcr}(t-\Delta t) + \hat{\mathbf{I}}_r(t-\Delta t)
$$

将 DFIG 完整模型的节点数从 24 降至 3（仅连接外部电路的节点）。

**M-NFSS 集电线等值**：

对于由 $m$ 台机组和 $m$ 条线路组成的串（string），采用多级嵌套快速同时求解：

$$
\begin{bmatrix} A & B \\ B^T & C \end{bmatrix} \begin{bmatrix} \mathbf{U}_{\text{EX}} \\ \mathbf{U}_{\text{IN}} \end{bmatrix} = \begin{bmatrix} \mathbf{J}_{\text{EX}} \\ \mathbf{J}_{\text{IN}} \end{bmatrix}
$$

消去内部节点：

$$
(A - BC^{-1}B^T)\mathbf{U}_{\text{EX}} = \mathbf{J}_{\text{EX}} + \mathbf{J}_{\text{IN}} - BC^{-1}\mathbf{J}_{\text{IN}}
$$

M-NFSS 采用"多次低阶"而非"一次高阶"策略，每一步仅考虑七节点模型，将 $3m$ 个内部节点逐步消去，每步仅需求解 3 阶矩阵逆，最终获得四节点等值模型。

**验证**：在 RTDS 实时数字仿真器上验证，所提模型仅使用传统详细模型 33.3% 的硬件资源，阻抗特性和时域波形高度准确。故障期间平均相对误差 < 3%。

## 形式化表达

### 核心公式汇总

**相似性距离度量**：

$$
d_{ij} = \left( \int_0^T \|\mathbf{x}_i(t) - \mathbf{x}_j(t)\|^p \, dt \right)^{1/p}
$$

**WCSS（簇内平方和）**：

$$
\text{WCSS} = \sum_{i=1}^{K} \sum_{x \in C_i} \|x - \mu_i\|^2
$$

**DBI（Davies-Bouldin Index）**：

$$
DBI = \frac{1}{K} \max_{i \neq j} \frac{S_i + S_j}{\|\mu_i - \mu_j\|}
$$

**等值参数倒数平均**：

$$
X_{\text{eq}} = \frac{X}{N}, \quad Z_{\text{eq}} = \frac{Z}{N}, \quad C_{\text{eq}} = NC
$$

**RMSE 误差**：

$$
E = \sqrt{\frac{1}{m} \sum_{i=1}^{m} \left(\frac{A_i - A_{eqi}}{A_i}\right)^2}
$$

**尾流风速修正**：

$$
V(X) = V_0 \left(1 - \frac{C_T}{2} \frac{\partial X}{r_0^2} \right)^{1/2}
$$


<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Background -->
  <rect width="900" height="420" fill="#fff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333" font-family="sans-serif">同调聚类方法体系架构</text>
  
  <!-- Layer 1: Input -->
  <rect x="50" y="55" width="160" height="70" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#2563eb" font-family="sans-serif">输入：故障暂态响应</text>
  <text x="130" y="100" text-anchor="middle" font-size="11" fill="#666" font-family="sans-serif">电流包络线 / 功率曲线</text>
  
  <!-- Layer 2: Feature Extraction -->
  <rect x="290" y="55" width="160" height="70" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="370" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#d97706" font-family="sans-serif">特征提取</text>
  <text x="370" y="100" text-anchor="middle" font-size="11" fill="#666" font-family="sans-serif">相似度矩阵 / DBI</text>
  
  <!-- Layer 3: Clustering Algorithm -->
  <rect x="530" y="55" width="160" height="70" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="610" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#d97706" font-family="sans-serif">聚类算法</text>
  <text x="610" y="100" text-anchor="middle" font-size="11" fill="#666" font-family="sans-serif">K-means / 轨迹相似度</text>
  
  <!-- Layer 4: Grouping -->
  <rect x="770" y="55" width="100" height="70" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="820" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#16a34a" font-family="sans-serif">同调群</text>
  <text x="820" y="100" text-anchor="middle" font-size="11" fill="#666" font-family="sans-serif">K 台等值机组</text>
  
  <!-- Arrows -->
  <line x1="210" y1="90" x2="285" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="450" y1="90" x2="525" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="690" y1="90" x2="765" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  
  <!-- Specific Methods Row -->
  <text x="450" y="160" text-anchor="middle" font-size="14" font-weight="bold" fill="#333" font-family="sans-serif">四大核心方法</text>
  
  <!-- Method 1: Current Trajectory -->
  <rect x="20" y="180" width="200" height="90" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="120" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c3aed" font-family="sans-serif">① 电流轨迹相似度</text>
  <text x="120" y="225" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">Ouyang 2017</text>
  <text x="120" y="242" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">包络线结构相似性</text>
  <text x="120" y="258" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">故障电流响应</text>
  
  <!-- Method 2: Enhanced K-means -->
  <rect x="240" y="180" width="200" height="90" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="340" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c3aed" font-family="sans-serif">② 增强K-means两阶段</text>
  <text x="340" y="225" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">Xu 2026</text>
  <text x="340" y="242" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">K-means++ / KD-tree / DBI</text>
  <text x="340" y="258" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">LVRT特性驱动</text>
  
  <!-- Method 3: Neural Network -->
  <rect x="460" y="180" width="200" height="90" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="560" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c3aed" font-family="sans-serif">③ 神经网络通用等值</text>
  <text x="560" y="225" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">Li 2025</text>
  <text x="560" y="242" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">CNN时序预测</text>
  <text x="560" y="258" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">一次训练处处可用</text>
  
  <!-- Method 4: M-NFSS -->
  <rect x="680" y="180" width="200" height="90" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="780" y="205" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c3aed" font-family="sans-serif">④ 延迟解耦+M-NFSS</text>
  <text x="780" y="225" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">Liu 2025</text>
  <text x="780" y="242" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">延迟解耦节点降阶</text>
  <text x="780" y="258" text-anchor="middle" font-size="10" fill="#666" font-family="sans-serif">RTDS实时仿真</text>
  
  <!-- Output Row -->
  <rect x="250" y="310" width="400" height="70" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="335" text-anchor="middle" font-size="13" font-weight="bold" fill="#16a34a" font-family="sans-serif">输出：风电场 EMT 等值模型</text>
  <text x="450" y="355" text-anchor="middle" font-size="11" fill="#666" font-family="sans-serif">精度 &gt;98% · 加速比 3–10x · 硬件资源降至 33%</text>
  
  <!-- Arrow to output -->
  <line x1="120" y1="270" x2="120" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="340" y1="270" x2="340" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="560" y1="270" x2="560" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="780" y1="270" x2="780" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="120" y1="300" x2="450" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="340" y1="300" x2="450" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="560" y1="300" x2="450" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="780" y1="300" x2="450" y2="300" stroke="#333" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="450" y1="310" x2="450" y2="308" stroke="#333" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  
  <!-- Legend -->
  <rect x="50" y="395" width="12" height="12" fill="#dbeafe" stroke="#2563eb"/>
  <text x="68" y="405" font-size="10" fill="#666" font-family="sans-serif">输入</text>
  <rect x="100" y="395" width="12" height="12" fill="#fef3c7" stroke="#d97706"/>
  <text x="118" y="405" font-size="10" fill="#666" font-family="sans-serif">算法</text>
  <rect x="160" y="395" width="12" height="12" fill="#dcfce7" stroke="#16a34a"/>
  <text x="178" y="405" font-size="10" fill="#666" font-family="sans-serif">输出</text>
  <rect x="220" y="395" width="12" height="12" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="238" y="405" font-size="10" fill="#666" font-family="sans-serif">方法</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 同调聚类方法体系架构</p>

## 关键技术挑战

### 特征量选择的多目标性

同调聚类的特征量需同时反映：
- **风速空间异质性**：实际风场内不同位置风速不同
- **电气距离差异**：距故障点的电气距离影响短路电流幅值
- **控制策略差异**：LVRT 控制参数、PLL 动态、Crowbar 阈值
- **保护动作差异**：Crowbar 投切时刻、变流器电流限幅

单一特征（如仅风速或仅容量）无法全面刻画暂态同调性。Xu 2026 采用三维特征 $(P, V_w, C_p)$，Ouyang 2017 采用电流包络线轨迹，Li 2025 采用电压/电流时序 + 准稳态参考值，不同方法在特征选择上各有侧重。

### 聚类数量的客观确定

传统 K-means 需人工指定簇数 $K$，主观性强。Xu 2026 通过 DBI 自动确定最优 $K$，在 20 台 DFIG 风电场中确定 $K=2$ 为最优（WCSS 曲线在 $K=2$ 处斜率明显变缓，DBI 也在 $K=2$ 处取得最小值）。但 DBI 仅适用于欧氏距离聚类，对于基于轨迹相似度的分群（如 Ouyang 2017），需另寻客观定簇方法。

### 场景通用性 vs 在线适应性

Li 2025 的神经网络通用等值模型通过单机训练 + 输入参数等效实现"一次训练、处处可用"，无需在不同工况下重新分群。但其优势在于适用于预想故障分析（故障未实际发生，等值线路参数难以求解的场景）。对于需要精确反映场站内部细节的 EMT 暂态分析，机理等值（如 Xu 2026 的两阶段聚类）仍具有不可替代的精度优势。

## 量化性能边界

| 方法 | 验证系统 | 降阶比 | 精度 | 加速比 | 数据来源 |
|------|----------|--------|------|--------|----------|
| Xu 2026 (增强K-means) | 20台×2.25MW DFIG, PSCAD | 20→3台 | >98% | ~10x (仿真时间减少90%) | Xu et al. 2026, EPSR |
| Liu 2025 (M-NFSS) | RTDS 实时仿真 | 详细→4节点/string | 平均相对误差<3% | 硬件资源降至33.3% | Liu et al. 2025, IEEE TPEL |
| Li 2025 (神经网络通用) | 16台PMSG, CloudPSS | 16→1台(通用) | 高于单机等值,低于四机等值 | 无需重分群 | Li et al. 2025, AEPS |
| Ouyang 2017 (电流轨迹) | 双馈风电场, EMT仿真 | 多→少(未报告具体数字) | 定性有效,未报告定量误差 | 未报告 | Ouyang et al. 2017, 中国电机工程学报 |

## 适用边界与选择指南

### 方法选择指南

| 应用场景 | 推荐方法 | 理由 |
|----------|----------|------|
| 故障暂态精确分析 | 电流轨迹相似度 (Ouyang 2017) | 直接基于故障电流响应，最贴近 EMT 需求 |
| 大规模风电场在线等值 | 增强K-means两阶段 (Xu 2026) | 自动定簇、KD-tree加速、仿真加速10倍 |
| 预想故障分析/在线安全评估 | 神经网络通用等值 (Li 2025) | 一次训练处处可用，无需重分群 |
| RTDS 实时仿真 | 延迟解耦+M-NFSS (Liu 2025) | 硬件资源降至33.3%，阻抗特性高度准确 |
| 全风速范围覆盖 | 增强K-means两阶段 (Xu 2026) | 第一阶段区分运行区，第二阶段处理MPPT区 |

### 不适用场景

- **非风电场景**：上述方法主要针对 DFIG/PMSG 风电场，对同步机群同调分析需采用基于转子角/频率的判据（如 IEEE 标准方法）
- **极高精度需求**：当需保留每台机组的 Crowbar 动作、变流器内部状态等细节时，等值模型无法替代详细模型
- **不平衡故障**：多数聚类方法基于对称故障假设，三相不平衡故障下的同调性需额外验证
- **含储能场站**：若风电场集成 BESS，储能系统的动态响应可能破坏机组间的同调性

## 相关方法

- [[current-trajectory-similarity]] — 基于电流轨迹相似度的具体分群方法
- [[network-equivalent]] — 网络等值方法，同调聚类常用于等值前的分群
- [[wind-farm-modeling]] — 风电场建模，聚类等值是重要手段
- [[modal-analysis]] — 模态分析，关注线性化模态，不同于时域轨迹聚类
- [[model-order-reduction]] — 模型降阶，同调聚类是其中一种物理意义明确的降阶途径
- [[equivalent-modeling]] — 动态等值建模方法，同调聚类是核心前置步骤

## 来源论文

- **Ouyang 等 2017**《基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法》，中国电机工程学报, 37(10): 2896–2904. — 提出基于短路电流包络线轨迹结构相似度的 DFIG 风电机群同调分群方法，是 EMT 领域风电场同调聚类的重要奠基性工作。
- **Xu 等 2026**《An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on LVRT characteristics》，Electric Power Systems Research 252 (2026) 112367. — 提出增强 K-means 两阶段聚类方法，集成 K-means++ 初始化、KD-tree 加速和 DBI 自动定簇，仿真加速 10 倍、精度 > 98%。
- **Li 等 2025**《基于单机模型扩展的直驱风电场通用等值模型构建方法》，中国电机工程学报, 49(8). — 提出基于神经网络通用模型的直驱风电场等值方法，通过输入参数等效实现"一次训练、处处可用"。
- **Liu 等 2025**《Modeling Method for DFIG-Based Wind Farm in High-Efficiency Real-Time Electromagnetic Transient (EMT) Simulations》，IEEE Trans. Power Electron., vol. 40, no. 9, pp. 13632–13646, Sep. 2025. — 提出基于延迟解耦和 M-NFSS 的 DFIG 风电场实时仿真模型，硬件资源降至 33.3%。
- **Yang 等 2011**《An aggregation method of permanent magnet synchronous generators wind farm model for electromagnetic transient studies》，IEEE/PES. — 针对永磁直驱风电场的聚合等值方法，为 PMSG 场站同调聚类提供参考。
- **Li 等 2022**《Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion》，IEEE Trans. on Sustainable Energy. — 保持结构的 DFIG 聚合方法，在保持系统物理结构的前提下实现模型降阶。
- **Guo 等 2025**《Electromagnetic transient aggregation of large-scale doubly-fed induction wind farm based on analytical criteria》. — 基于解析判据的大规模 DFIG 风电场电磁暂态聚合方法。

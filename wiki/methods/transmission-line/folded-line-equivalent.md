---
title: "折叠线等效 (Folded Line Equivalent)"
type: method
tags: [folded-line, equivalent, bergeron, transmission-line, delay, travel-time, frequency-dependent, vector-fitting]
created: "2026-05-02"
updated: "2026-05-16"
---

# 折叠线等效 (Folded Line Equivalent)

## 定义

折叠线等效（Folded Line Equivalent, FLE）是将传输线两端口节点导纳矩阵 $\mathbf{Y}_n(s)$ 通过线性变换分解为**开路导纳** $Y_{oc}(s)$ 和**短路导纳** $Y_{sc}(s)$ 两个独立子块的线路等效方法。FLE 源自 Gustavsen 和 Semlyen（1999）的研究，其核心动机是解决直接对 $2n\times 2n$ 节点导纳矩阵进行矢量拟合时，**低频小特征值难以准确逼近**导致时域响应失真的问题。

设单相两端口线路的频域端口关系为：

$$
\begin{bmatrix} I_k \\ I_m \end{bmatrix} = \mathbf{Y}_n(s) \begin{bmatrix} V_k \\ V_m \end{bmatrix} \tag{1}
$$

FLE 的关键是用变换矩阵 $\mathbf{L}$ 将端口变量映射到"同相"（开路贡献）和"反相"（短路贡献）组合：

$$
\begin{bmatrix} V_{oc} \\ V_{sc} \end{bmatrix} = \mathbf{L} \begin{bmatrix} V_k \\ V_m \end{bmatrix}, \quad \mathbf{L} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \tag{2}
$$

经相似变换后，导纳矩阵解耦为对角块：

$$
\mathbf{Y}_{fle}(s) = \mathbf{L}^{-1} \mathbf{Y}_n(s) \mathbf{L} = \begin{bmatrix} Y_{oc}(s) & 0 \\ 0 & Y_{sc}(s) \end{bmatrix} \tag{3}
$$

对角块的维度仅为原矩阵的一半（$n \times n$ 而非 $2n \times 2n$），且最大/最小特征值比值显著降低，从而改善矢量拟合的收束性和拟合精度。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 380" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入层：频域节点导纳 -->
  <rect x="20" y="150" width="140" height="80" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="185" text-anchor="middle" font-size="13" fill="#1e40af" font-weight="bold">频域节点导纳</text>
  <text x="90" y="205" text-anchor="middle" font-size="11" fill="#1e40af">Y_n(s) (2n×2n)</text>
  <text x="90" y="220" text-anchor="middle" font-size="10" fill="#3b82f6">传输线参数</text>

  <!-- 箭头1 -->
  <line x1="160" y1="190" x2="225" y2="190" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="192" y="183" text-anchor="middle" font-size="10" fill="#666">FLE变换矩阵L</text>

  <!-- 处理层：开路/短路分解 -->
  <rect x="230" y="70" width="120" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="290" y="95" text-anchor="middle" font-size="12" fill="#166534" font-weight="bold">开路导纳</text>
  <text x="290" y="112" text-anchor="middle" font-size="10" fill="#15803d">Y_oc(s) (n×n)</text>

  <rect x="230" y="255" width="120" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="290" y="280" text-anchor="middle" font-size="12" fill="#166534" font-weight="bold">短路导纳</text>
  <text x="290" y="297" text-anchor="middle" font-size="10" fill="#15803d">Y_sc(s) (n×n)</text>

  <!-- 虚线框 -->
  <rect x="225" y="65" width="130" height="250" rx="4" fill="none" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="290" y="58" text-anchor="middle" font-size="10" fill="#16a34a">FLE解耦层</text>

  <!-- 箭头2: Y_oc -->
  <line x1="350" y1="97" x2="415" y2="97" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="382" y="90" text-anchor="middle" font-size="10" fill="#666">矢量拟合</text>

  <!-- 箭头2: Y_sc -->
  <line x1="350" y1="282" x2="415" y2="282" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="382" y="275" text-anchor="middle" font-size="10" fill="#666">矢量拟合</text>

  <!-- 算法层：RLC综合 -->
  <rect x="420" y="70" width="130" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="485" y="93" text-anchor="middle" font-size="12" fill="#92400e" font-weight="bold">RLC等效电路</text>
  <text x="485" y="110" text-anchor="middle" font-size="10" fill="#b45309">G_oc(s) ≈ ∑ r/(s+p)</text>

  <rect x="420" y="255" width="130" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="485" y="278" text-anchor="middle" font-size="12" fill="#92400e" font-weight="bold">RLC等效电路</text>
  <text x="485" y="295" text-anchor="middle" font-size="10" fill="#b45309">G_sc(s) ≈ ∑ r/(s+p)</text>

  <!-- 箭头3: 无源性 -->
  <line x1="550" y1="97" x2="615" y2="97" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="582" y="90" text-anchor="middle" font-size="10" fill="#666">无源性强制</text>

  <line x1="550" y1="282" x2="615" y2="282" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="582" y="275" text-anchor="middle" font-size="10" fill="#666">无源性强制</text>

  <!-- 输出层：诺顿等效 -->
  <rect x="620" y="115" width="140" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="690" y="140" text-anchor="middle" font-size="12" fill="#5b21b6" font-weight="bold">诺顿等效</text>
  <text x="690" y="157" text-anchor="middle" font-size="10" fill="#6d28d9">G + I_hist</text>

  <rect x="620" y="215" width="140" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="690" y="240" text-anchor="middle" font-size="12" fill="#5b21b6" font-weight="bold">诺顿等效</text>
  <text x="690" y="257" text-anchor="middle" font-size="10" fill="#6d28d9">G + I_hist</text>

  <!-- 箭头4: 逆变换 -->
  <line x1="760" y1="140" x2="830" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="760" y1="240" x2="830" y2="240" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="795" y="178" text-anchor="middle" font-size="10" fill="#666">L⁻¹逆变换</text>

  <!-- 输出: 端口 -->
  <rect x="835" y="115" width="55" height="150" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="862" y="155" text-anchor="middle" font-size="11" fill="#991b1b" font-weight="bold">端口</text>
  <text x="862" y="172" text-anchor="middle" font-size="10" fill="#b91c1c">V_k, I_k</text>
  <text x="862" y="200" text-anchor="middle" font-size="10" fill="#b91c1c">V_m, I_m</text>
  <text x="862" y="250" text-anchor="middle" font-size="11" fill="#991b1b" font-weight="bold">时域EMT</text>

  <!-- 图例 -->
  <rect x="20" y="340" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="37" y="350" font-size="10" fill="#333">输入/源</text>
  <rect x="90" y="340" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="107" y="350" font-size="10" fill="#333">处理/分解</text>
  <rect x="175" y="340" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="192" y="350" font-size="10" fill="#333">算法/拟合</text>
  <rect x="270" y="340" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="287" y="350" font-size="10" fill="#333">输出/等效</text>
  <rect x="360" y="340" width="12" height="12" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="377" y="350" font-size="10" fill="#333">最终端口</text>

  <!-- Marker definition -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 折叠线等效（FLE）建模流程：频域节点导纳经FLE解耦为开路/短路导纳，分别矢量拟合、无源性强制后综合为诺顿等效，最终逆变换回端口时域EMT方程</p>

## EMT中的作用

FLE 在 EMT 仿真中主要解决两类问题：

**问题一：频变线路特征值跨度大**。当线路节点导纳矩阵 $\mathbf{Y}_n(s)$ 的特征值跨越数个数量级（如低频小特征值与高频大特征值并存），直接对该矩阵进行矢量拟合（Vector Fitting）时，小特征值对应的低频响应难以精确拟合，导致时域波形失真。FLE 将 $\mathbf{Y}_n(s)$ 分解为 $Y_{oc}(s)$ 和 $Y_{sc}(s)$ 后，每个子矩阵的特征值跨度显著收窄（Gustavsen 1999 原文明确指出），从而降低拟合难度。

**问题二：短线路步长瓶颈**。基于特征线法（Method of Characteristics）的线路模型（如 JMarti、ULM）要求仿真步长 $\Delta t$ 小于线路传播延时 $\tau$。在含大量短线路的复杂网络中，最短线路的 $\tau$ 迫使全系统采用极小步长，严重拖累仿真效率。FLE 不依赖特征线法的延时队列，而是通过频域导纳的电路综合实现时域积分，**允许 $\Delta t > \tau$**，从而突破短线路步长瓶颈。

其外部接口仍是线路两端端口电压和注入电流；内部实现则可能是有理导纳、RLC 综合电路、Norton 历史源或多伴随网络。

## 核心机制

### 1. FLE 变换的数学基础

FLE 变换的核心是**相似变换**而非特征线法。对于单模态或单相两端口线路，频域端口关系（式1）经变换矩阵 $\mathbf{L}$（式2）映射后得到对角化解耦形式（式3）。

关键性质：
- $\mathbf{L}$ 是**正交矩阵**（$\mathbf{L}^{-1} = \mathbf{L}^T$），保持向量模长不变，便于电路实现
- 分解后 $Y_{oc}$ 和 $Y_{sc}$ 的最大/最小特征值比远小于 $\mathbf{Y}_n(s)$ 的对应比值
- $Y_{oc}$ 和 $Y_{sc}$ 均为 $n \times n$ 矩阵（而非 $2n \times 2n$），**拟合维度减半**

### 2. 矢量拟合与无源性强制

对分解后的开路/短路导纳进行极点-留数有理逼近：

$$
Y(s) \approx G(s) = \sum_{k=1}^{N_p} \frac{r_k}{s + p_k} + d + e s \tag{4}
$$

式中 $N_p$ 为共轭复极点对数，$r_k$ 为留数，$p_k$ 为极点，$d$ 为常数项，$e$ 为高频渐近项系数。矢量拟合（Vector Fitting）通过迭代求解线性最小二乘问题确定参数。

无源性强制是保证时域稳定性的关键步骤。FLE 拟合后需通过**留数扰动法**（Residue Perturbation）确保 $G(j\omega)$ 在全频段满足 $\text{Re}[G(j\omega)] \geq 0$，防止时域积分出现能量生成。

### 3. 时域电路实现

拟合得到的有理函数可综合为 RLC 等效电路（串联或并联支路），或表示为诺顿等效形式：

$$
I = G V + I_{hist} \tag{5}
$$

其中 $I_{hist}$ 包含所有极点的历史电流卷积贡献。在每步 EMT 积分中，只需更新 $I_{hist}$ 而保持电导矩阵 $G$ 恒定。

### 4. 延迟利用与多速率更新（Camara 2017 扩展）

Camara 等（2017）将 FLE 与延迟利用（Latency Exploitation）结合，提出改进的多伴随网络（MCNR）方法。其核心思想是利用极点时间尺度的差异：快极点（时间常数小）用小步长 $\Delta t$ 更新，慢极点（时间常数大）允许用大时间步 $\Delta t_s = k \cdot \Delta t$（$k$ 可达数百）松弛更新。

慢极点判定阈值 $\alpha \geq 0.99$（强耦合线路需收紧至 $\alpha \geq 0.9999$）。慢极点的松弛更新公式为：

$$
h_s(t) = h_s(t - \Delta t) + c \cdot v(t - \Delta t) \tag{6}
$$

该公式在 $k$ 高达 500 时仍保持数值稳定，克服了原始 MCN 方法在 $k > 10$ 时误差急剧增大的缺陷。

## 实现路线

| 路线 | 机制 | 适合用途 | 风险点 |
|------|------|----------|--------|
| 频域导纳 FLE | 对 $\mathbf{Y}_n(s)$ 分解后拟合 $Y_{oc}$、$Y_{sc}$ | 频变线路和短线路等效 | 拟合阶数、无源性、频带选择 |
| 电路化 FLE | 把导纳有理函数综合为 RLC 或 Norton 支路 | ATP/EMTP 类节点求解器 | 电路元件数量和数值条件 |
| FLE + 延迟利用 | 区分快慢极点，降低慢动态更新频度 | 多时间尺度频变线路 | 快慢阈值和强耦合线路响应需验证 |
| 模态 FLE | 先相域到模态域，再对每个模态折叠 | 三相近似可解耦线路 | 频率相关变换矩阵会影响准确性 |

## 形式化表达

### FLE 变换矩阵

**原始正交矩阵**（Gustavsen & Semlyen 1999）：

$$
\mathbf{L} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \tag{7}
$$

**改进正交矩阵**（Colqui 等 2022，用理想变压器电路实现）：

$$
\mathbf{L}_{mod} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \cdot \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \tag{8}
$$

两种矩阵本质等价，区别在于改进版便于 ATP 中用双绕组理想变压器（变比 $1:\sqrt{2}$）直接电路实现。

### 节点导纳矩阵分解

$$
\mathbf{Y}_{fle}(s) = \mathbf{L}^{-1} \mathbf{Y}_n(s) \mathbf{L} = \begin{bmatrix} \mathbf{Y}_{oc}(s) & 0 \\ 0 & \mathbf{Y}_{sc}(s) \end{bmatrix} \tag{9}
$$

其中开路导纳和短路导纳分别对应端口变量在开路和短路边界条件下的驱动点导纳。

### Camara 2017 的 MCNR 慢极点松弛更新

$$
h_s(t) = h_s(t - \Delta t) + c \cdot v(t - \Delta t) \tag{10}
$$

$$
h_f(t) = \alpha_f \cdot h_f(t - \Delta t) + c_f \cdot v(t - \Delta t) \tag{11}
$$

式（10）为慢极点松弛更新，忽略衰减系数 $\alpha_s \approx 1$ 的项；式（11）为快极点标准递归卷积，保留 $\alpha_f < 0.99$ 的衰减项。

### Colqui 2022 的 NRMSD 误差评估

$$
\text{NRMSD} = \frac{\sqrt{\frac{1}{N}\sum_{i=1}^N (y_{\text{MFLE},i} - y_{\text{ULM}})^2}}{\max\{y_{\text{ULM}}\} - \min\{y_{\text{ULM}}\}} \tag{12}
$$

用于量化 MFLE 模型与 ULM 基准之间的波形偏差。

## 量化性能边界

### Colqui 2022（MFLE in ATP）性能数据

| 参数 | 数值 |
|------|------|
| 测试线路 | 300m 架空三相输电线路（含地线，Kron 降阶） |
| 传播延时 | 约 1 μs |
| 拟合极点对数 | 20 对（共轭复极点） |
| 仿真步长测试 | 0.1 μs（10%）、1 μs（100%）、2 μs（200%）、4 μs（400%） |
| **NRMSD 范围** | **0.1%~0.8%**（步长 0.1~4 μs） |
| 步长扩大倍数 | 4×（4 μs vs 1 μs 传播延时） |
| 正交矩阵实现误差 | 0（理想变压器精确实现） |
| 电路拓扑复杂度 | 较传统相似矩阵降低约 30% |

**关键结论**：在开路合闸、负载投切、单相接地故障三种工况下，MFLE 在步长扩大至传播延时 400%（4 μs）时 NRMSD 仍控制在 0.8% 以内，有效突破短线路对全网步长的限制。

### Camara 2017（MCNR 延迟利用）性能数据

| 测试案例 | 线路规格 | 仿真步长 | Yoc/Ysc 极点数 | 慢极点数 | 计算加速 | 精度损失 |
|---------|---------|---------|--------------|---------|---------|---------|
| Case 1 | 300m 132kV 单回架空线 | 1 μs | 16/20 | 10/20 | ~35% | <0.1% |
| Case 2 | 10km 132kV 单回架空线 | 30 μs | 38/50 | 9/50 | >30% | 可忽略 |
| Case 3 | 50km 500kV 双回强耦合线 | 10 μs | 38/60 | 10/60 | 10%~15% | <0.5% |

**关键结论**：FLE 变换使待拟合矩阵维度减半（$2n \times 2n \to n \times n$），矢量拟合阶数减少约 20%~30%。MCNR 方法在三个测试案例中均实现 10%~35% 的仿真加速，且时域波形最大幅值偏差均小于 0.5%。

## 关键技术挑战

**挑战一：拟合阶数与无源性的权衡**。FLE 分解后 $Y_{oc}$ 和 $Y_{sc}$ 的极点数量取决于原始线路参数的频变特性。增加拟合阶数 $N_p$ 可提高拟合精度，但也会增加时域电路的元件数量和计算负担。无源性强制（留数扰动）可能进一步改变留数矩阵，需要在精度和稳定性之间权衡。

**挑战二：模态解耦的准确性假设**。模态 FLE 路线假设三相线路可经 Clarke 变换或类似矩阵解耦为独立模态。这一假设对**理想换位线路**成立，对**非换位不对称多回线路**，频率相关变换矩阵会破坏解耦条件，导致 FLE 分解不准确。

**挑战三：快慢极点的分类阈值设定**。Camara 2017 的 $\alpha \geq 0.99$ 阈值是经验设定，适用于一般线路；但对强耦合线路（如 500kV 双回线），该阈值需收紧至 $\alpha \geq 0.9999$。阈值的自适应选择尚无通用方法，需结合线路参数和仿真精度要求人工调整。

**挑战四：多速率界面与 EMT 主回路同步**。MCNR 的慢极点用大时间步更新，但其输出需与 EMT 主回路的小步长节点方程同步。这一同步过程若处理不当，可能引入相位误差或数值振荡，尤其在故障暂态初期（所有极点的历史源均未充分建立）更为敏感。

**挑战五：非换位线路和多回强耦合线路**。FLE 的开路/短路分解假设线路端口可独立设置边界条件。对非换位线路、多回强耦合线路、地下电缆和含接地护套系统，模态解耦假设不再成立，开路/短路块的条件数可能显著增大，影响矢量拟合收敛性。

## 适用边界与选择指南

| 场景 | 推荐路线 | 说明 |
|------|---------|------|
| 短线路大步长仿真（$\Delta t > \tau$） | 频域导纳 FLE + 电路化 | Colqui 2022 验证 4τ 步长仍保持 <0.8% NRMSD |
| 多时间尺度频变线路网络 | FLE + 延迟利用（MCNR） | Camara 2017 验证 10%~35% 加速，<0.5% 精度损失 |
| ATP/EMTP 平台实现 | 电路化 FLE（RLC 综合） | 理想变压器实现 Clarke 和正交矩阵 L |
| 频变线路与 ULM/JMarti 对比验证 | 频域导纳 FLE | 可直接比较端口外特性 |
| 非换位不对称多回线路 | 模态 FLE（需谨慎） | 频率相关变换矩阵影响准确性 |
| 地下电缆和含护套系统 | 不推荐 FLE | 土壤回流和护套耦合破坏开路/短路假设 |

FLE 不改变线路端口物理本身。若原始线路参数或土壤模型不可靠，FLE 不会修复物理输入。开路/短路块是否易于拟合取决于线路结构、频带和矩阵条件数，不能把单篇算例中的拟合阶数或加速比写成一般规律。

## 相关方法 / 相关模型 / 相关主题

- [[bergeron-line-model]] — 延时历史源表示特征线传播；FLE 偏向节点导纳分解和有理导纳实现，两者原理不同
- [[universal-line-model]] — 直接拟合相域特征导纳和传播矩阵，常作为频变线路对比基准
- [[vector-fitting]] — 把 $Y_{oc}$、$Y_{sc}$ 转为有理函数的工具，FLE 的前置步骤
- [[passivity-enforcement]] — 检查和修正有理导纳模型的无源性，FLE 拟合后的必要验证
- [[frequency-dependent-line-model]] — 频变线路模型的统称，JMarti 和 ULM 均属此类
- [[modal-transformation]] — 模态域解耦变换，三相 FLE 的前置步骤
- [[large-timestep-simulation]] — 大时间步仿真方法论，FLE 是其实现手段之一
- [[multirate-method]] — 多速率仿真方法，Camara 2017 的 MCNR 属于此类

## 来源论文

- [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-]] — Colqui 等 2022，**改进 FLE 正交矩阵的 ATP 电路实现**，三相 Clarke 变换解耦 + 理想变压器电路化 + 4τ 步长验证，NRMSD 0.1%~0.8%
- [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat]] — Camara 等 2017，**FLE + 延迟利用 MCNR 方法**，快慢极点分离 + 松弛更新，10%~35% 加速，<0.5% 偏差
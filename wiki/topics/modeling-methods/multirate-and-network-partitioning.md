---
title: "多速率与分网方法 (Multirate and Network Partitioning Methods)"
type: topic
tags: [multirate, partitioning, mate, network-decomposition, emt]
created: "2026-05-01"
book-chapter: "12"
---

# 多速率与分网方法 (Multirate and Network Partitioning Methods)

## 定义

多速率仿真（Multirate EMT Simulation）和分网方法（Network Partitioning）是解决大规模电力系统电磁暂态（EMT）仿真中**"规模-速度-精度"三角矛盾**的核心技术组合：

- **多速率仿真**：允许不同子系统采用不同时间步长，以快子系统步长$h_f$为基准，慢子系统步长$h_s = n \cdot h_f$（$n$为步长比）
- **分网方法**：将大规模系统分解为可并行或独立求解的子系统，通过接口模型耦合
- **两者协同**：分网提供并行性，多速率提供差异化步长，两者结合实现高效大规模EMT仿真

核心挑战：时间尺度差异（μs级电力电子 vs s级机电）、接口稳定性、计算效率。

## EMT中的角色

### 规模-速度-精度三角矛盾

| 矛盾维度 | 传统单速率EMT问题 | 多速率+分网解决方案 |
|---------|------------------|-------------------|
| 规模 | MMC使节点数激增，$O(N^3)$求逆成本 | 分网将大矩阵拆分为多个小矩阵 |
| 速度 | 全系统μs步长，计算量巨大 | 快系统用μs步长，慢系统用ms步长 |
| 精度 | 简化等值模型损失非线性动态 | 保留详细模型，仅在接口处等值 |

### 为什么需要多速率+分网

1. **MMC-HVDC系统**：换流器子模块级（1-10 μs）与外接AC系统（1-10 ms）时间常数比达$10^3$:$1$
2. **接口稳定性**：子系统间数据交换引入数值振荡风险
3. **实时约束**：实时仿真器（RTDS）需要在严格时间窗口内完成计算

## 核心机制

### 1. 网络分网策略

#### 1.1 自然解耦（传输线分网）

利用Bergeron线路模型的波传播延迟特性，在线路末端自然解耦：

$$V_m(t) = Z_c I_m(t-2\tau) + V_{other}(t-\tau)$$

**优势**：无条件稳定，无近似误差。**局限**：依赖线路长度$\geq 15-30$ km（对应50-100 μs延迟）。

#### 1.2 人工解耦（补偿法/Latency Insertion）

在接口处注入虚拟延迟，人为创造解耦条件：

$$I_{comp} = Y_{eq} V_{interface} + J_{hist}$$

**优势**：任意拓扑均可分网。**局限**：虚拟元件可能影响精度。

#### 1.3 基于图论的分网

利用谱聚类或Metis算法最优化网络划分：
- 最小化割边权重（子网络间连接最小化）
- 平衡各分区计算负载
- 考虑电气耦合强度作为边权重

### 2. 多导纳技术（MATE）

MATE（Multi-Area Thevenin Equivalent）将网络划分为多个子网络，通过链接支路耦合。系统方程写成块结构：

$$\begin{bmatrix} Y_{sub1} & 0 & B_1 \\ 0 & Y_{sub2} & B_2 \\ B_1^T & B_2^T & Y_{link} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \\ V_{link} \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \\ I_{link} \end{bmatrix}$$

**求解流程**：
1. 各子网络独立求解（可并行）
2. 构建链接点简化方程
3. 求解链接点电压
4. 回代求子网络内部电压

**核心优势**：子网络导纳矩阵可预分解（LU分解一次，多次调用）；拓扑变化仅影响局部子网络；天然适合并行计算。

### 3. 接口模型更新

#### 3.1 诺顿等值（用于慢子系统对快子系统的接口）

慢子系统端口用诺顿等值表示：

$$I_{port} = Y_{eq} V_{port} + J_{eq}$$

**诺顿电流更新**（移动窗口平均）：

$$i_s(nk+1) = \frac{1}{n} \sum_{m=0}^{n-1} i_f(tk + mh)$$

该技术防止单一瞬时值带来的准随机性抖动。

#### 3.2 戴维南等值（用于快子系统对慢子系统的接口）

快子系统端口用时变戴维南等值表示：

$$V_{port} = Z_{eq} I_{port} + E_{eq}$$

**时变戴维南参数更新**（移动窗口预测 + 分步校正）：

1. **移动窗口预测**：记录最近$m$个历史电压值，三次样条插值计算预测电压$\tilde{u}_f(t_k + ih)$，4阶精度
2. **分步校正**：端点校正考虑多接口间交互

$$\Delta u_l^f(t_{k+1}) = \sum_{m=1, m \neq l}^{N} Z_{lm} i_m^f(t_{k+1})$$

校正后电压：
$$u_l^f(t_{k+1}) = \tilde{u}_l^f(t_{k+1}) + \Delta u_l^f(t_{k+1})$$

### 4. 接口模型离散化

#### 4.1 梯形法（TR）的数值振荡问题

梯形法在剧烈扰动后产生不良数值振荡。EMT程序通常嵌入插值方法抑制振荡，但接口模型缺乏此类机制。

#### 4.2 根匹配算法（RM）

选择根匹配算法离散接口模型，因其在抑制数值振荡方面优于向后欧拉法，且精度更高。

以RL支路为例，MTDC子系统中的阻抗比：

$$Z_{dc} = \frac{\hat{u}}{\hat{\imath}} = \frac{\frac{L}{h}(z^n - 1) + \frac{R}{2}(1 + z^n) + R \sum_{m=1}^{n-1} z^m}{\frac{1}{z} + \frac{n}{2}(1 + z) + \sum_{m=1}^{n-1} z^m}$$

阻抗比$\zeta(n, \omega) = Z_{ac}/Z_{dc}$用于衡量两个子系统仿真精度的一致性。$R \to 0$时：

$$\lim_{R \to 0} \zeta(n, \omega) = \frac{(1 + z^n) + 2\sum_{m=1}^{n-1} z^m}{n \cdot (1 + z^n)}$$

其中$z = e^{j\omega h}$。

### 5. 最优步长比选择

步长比$n = h_{ac}/h_{dc}$的选择需满足两个约束：

**约束1（稳定性）**：$n \leq h_{ac,max}/h$（$h_{ac,max}$是AC子系统的最大稳定步长）

**约束2（精度一致性）**：

$$0.9 \leq |\zeta(n, \omega)| \leq 1.1, \quad \omega \in [0, 0.2 f_{Ny}]$$

**Shu 2018案例**：MTDC步长$h = 50 \mu s$，AC步长上限$h_{ac,max} = 500 \mu s$，故$n \leq 10$。结合精度约束，$n=2-6$均可满足，但最优步长比为**$n=6$**（最大加速比）。

## 关键技术挑战

### 挑战1：混叠误差与时间延迟误差

慢子系统向快子系统提供数据时，仅在同步时刻更新，产生采样混叠和时间延迟误差。

**解法**：移动窗口预测+三次样条插值（4阶精度）消除时间延迟；分步校正消除多接口间交互。

### 挑战2：数值振荡

梯形法在接口处引发数值振荡，导致结果失真。

**解法**：根匹配算法替代梯形法离散接口模型。

### 挑战3：步长比边界

步长比>6时误差急剧增大，超出精度一致性范围。

**解法**：通过阻抗比判据约束$n \leq 6$（Shu 2018实证）。

### 挑战4：接口线路长度限制

传输线自然解耦要求线路长度≥15-30 km，短接口线路无法使用。

**解法**：补偿法或MATE人工解耦替代自然解耦。

### 挑战5：计算负载均衡

各子网络计算量差异导致并行效率下降。

**解法**：基于图论划分时将计算负载作为权重因素。

## 量化性能边界

### 分网加速性能

| 分网方法 | 适用场景 | 加速比 | 精度影响 |
|---------|---------|-------|---------|
| 自然解耦（Bergeron） | 长线路系统（≥15 km） | 3-5× | 无近似误差 |
| 补偿法（Latency） | 任意拓扑 | 2-4× | 误差<1% |
| MATE | 大规模系统并行 | 3-6× | 无显著影响 |
| 图划分+并行 | 任意拓扑 | 取决于CPU核数 | 无 |

### 多速率性能（Shu 2018，四端MMC-MTDC系统）

| 步长比$n$ | DC步长$h$ | AC步长$h_{ac}$ | 最大误差（短线路） | 最大误差（长线路） |
|---------|---------|--------------|-------------------|--------------------|
| n=2 | 50 μs | 100 μs | ~0.02 pu | ~0.01 pu |
| n=4 | 50 μs | 200 μs | ~0.04 pu | ~0.02 pu |
| **n=6** | **50 μs** | **300 μs** | **0.0523 pu** | **0.0315 pu** |
| n=7 | 50 μs | 350 μs | 不可接受 | — |

### 接口精度对比（Shu 2018，三相接地故障）

| 接口更新方法 | 离散化方法 | 最大误差（pu） | 数值振荡 |
|------------|-----------|-------------|---------|
| 线性预测（LP） | 梯形法 | 0.2677 | 有 |
| 移动窗口预测+分步校正 | 梯形法 | 0.0523 | 有 |
| 移动窗口预测+分步校正 | **根匹配法** | **<0.01** | **无** |

**结论**：所提方法（移动窗口预测+分步校正+根匹配离散）精度比传统方法高约5倍，并完全抑制数值振荡。

## 适用边界与选择指南

| 场景 | 推荐分网策略 | 推荐接口更新 | 步长比上限 |
|------|------------|------------|----------|
| 含长输电线路（≥15 km） | 自然解耦 | 传输线延迟模型 | n≤10 |
| 任意拓扑，精度优先 | MATE | 时变Thevenin/Norton | n≤6 |
| 任意拓扑，速度优先 | 补偿法 | 诺顿等值平均更新 | n≤4 |
| 短接口线路 | MATE/补偿法 | 移动窗口预测+根匹配 | n≤6 |
| 宽频暂态分析 | 频域分区 | FDNE端口等值 | n≤3 |

**多速率接口稳定性判据**：
- 延迟稳定性：$\omega_{max} \cdot \Delta t_{delay} < \pi/4$
- 插值误差传播：$\varepsilon_{interp} \propto (h_s/\tau_{interface})^2$

## 多速率EMT协同仿真框架

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="520" fill="#fafafa"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">多速率EMT协同仿真框架</text>
  
  <!-- Layer 1: Input -->
  <rect x="20" y="45" width="160" height="90" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="100" y="62" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e3a8a">系统输入</text>
  <text x="100" y="78" text-anchor="middle" font-size="9" fill="#3b82f6">36节点AC系统</text>
  <text x="100" y="91" text-anchor="middle" font-size="9" fill="#3b82f6">4端MMC-MTDC</text>
  <text x="100" y="104" text-anchor="middle" font-size="9" fill="#3b82f6">250子模块/桥臂</text>
  <text x="100" y="117" text-anchor="middle" font-size="9" fill="#3b82f6">400kV额定电压</text>
  
  <!-- Layer 2: Partition -->
  <rect x="20" y="150" width="160" height="100" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="100" y="167" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">网络分网</text>
  <text x="100" y="183" text-anchor="middle" font-size="9" fill="#b45309">MATE多导纳技术</text>
  <text x="100" y="196" text-anchor="middle" font-size="9" fill="#b45309">自然解耦（长线路）</text>
  <text x="100" y="209" text-anchor="middle" font-size="9" fill="#b45309">补偿法（短线路）</text>
  <text x="100" y="222" text-anchor="middle" font-size="9" fill="#b45309">图论Metis划分</text>
  <text x="100" y="235" text-anchor="middle" font-size="9" fill="#b45309">并行子网络独立求解</text>
  
  <!-- Layer 3: Multirate Co-simulation -->
  <rect x="240" y="45" width="200" height="205" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="340" y="62" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">多速率协同仿真</text>
  
  <rect x="250" y="75" width="85" height="80" rx="4" fill="#bbf7d0" stroke="#15803d" stroke-width="1"/>
  <text x="292" y="90" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">AC子系统</text>
  <text x="292" y="104" text-anchor="middle" font-size="8" fill="#22c55e">h_ac = n×50μs</text>
  <text x="292" y="116" text-anchor="middle" font-size="8" fill="#22c55e">n=6（最优）</text>
  <text x="292" y="128" text-anchor="middle" font-size="8" fill="#22c55e">hac_max=500μs</text>
  <text x="292" y="140" text-anchor="middle" font-size="8" fill="#22c55e">TR离散化</text>
  <text x="292" y="152" text-anchor="middle" font-size="8" fill="#22c55e">诺顿等值接口</text>
  
  <rect x="345" y="75" width="85" height="80" rx="4" fill="#bbf7d0" stroke="#15803d" stroke-width="1"/>
  <text x="387" y="90" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">MTDC子系统</text>
  <text x="387" y="104" text-anchor="middle" font-size="8" fill="#22c55e">h=50μs</text>
  <text x="387" y="116" text-anchor="middle" font-size="8" fill="#22c55e">250子模块/桥臂</text>
  <text x="387" y="128" text-anchor="middle" font-size="8" fill="#22c55e">RM离散化</text>
  <text x="387" y="140" text-anchor="middle" font-size="8" fill="#22c55e">戴维南等值接口</text>
  <text x="387" y="152" text-anchor="middle" font-size="8" fill="#22c55e">移动窗口预测</text>
  
  <rect x="262" y="165" width="155" height="70" rx="4" fill="#d1fae5" stroke="#059669" stroke-width="1"/>
  <text x="340" y="180" text-anchor="middle" font-size="9" font-weight="bold" fill="#065f46">协调器（Coordinator）</text>
  <text x="340" y="194" text-anchor="middle" font-size="8" fill="#059669">接口参数计算</text>
  <text x="340" y="206" text-anchor="middle" font-size="8" fill="#059669">网络等值计算</text>
  <text x="340" y="218" text-anchor="middle" font-size="8" fill="#059669">信号交换与校正</text>
  <text x="340" y="230" text-anchor="middle" font-size="8" fill="#059669">Socket/共享内存通信</text>
  
  <line x1="180" y1="200" x2="250" y2="180" stroke="#6b7280" stroke-width="1.5"/>
  <line x1="180" y1="200" x2="250" y2="120" stroke="#6b7280" stroke-width="1.5"/>
  <line x1="335" y1="120" x2="345" y2="120" stroke="#6b7280" stroke-width="1.5"/>
  <line x1="335" y1="180" x2="345" y2="180" stroke="#6b7280" stroke-width="1.5"/>
  
  <!-- Layer 4: Accuracy criteria -->
  <rect x="460" y="95" width="160" height="130" rx="6" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="540" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">精度一致性判据</text>
  <text x="540" y="130" text-anchor="middle" font-size="9" fill="#7c3aed">阻抗比约束：</text>
  <text x="540" y="145" text-anchor="middle" font-size="9" fill="#6d28d9">0.9 ≤ |ζ(n,ω)| ≤ 1.1</text>
  <text x="540" y="160" text-anchor="middle" font-size="9" fill="#7c3aed">ω ∈ [0, 0.2f_Ny]</text>
  <text x="540" y="178" text-anchor="middle" font-size="9" fill="#6d28d9">n=2~6满足精度</text>
  <text x="540" y="193" text-anchor="middle" font-size="9" fill="#6d28d9">n=6为最优步长比</text>
  <text x="540" y="208" text-anchor="middle" font-size="9" fill="#6d28d9">|ζ(n,ω)|越接近1</text>
  <text x="540" y="220" text-anchor="middle" font-size="9" fill="#6d28d9">AC/MTDC精度越一致</text>
  
  <!-- Layer 5: Output results -->
  <rect x="640" y="95" width="160" height="130" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="720" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#991b1b">量化性能</text>
  <text x="720" y="130" text-anchor="middle" font-size="9" fill="#dc2626">误差（短线路）：</text>
  <text x="720" y="145" text-anchor="middle" font-size="9" fill="#b91c1c">Proposed: 0.0523 pu</text>
  <text x="720" y="158" text-anchor="middle" font-size="9" fill="#b91c1c">TLM: 0.2677 pu</text>
  <text x="720" y="175" text-anchor="middle" font-size="9" fill="#dc2626">误差（长线路）：</text>
  <text x="720" y="190" text-anchor="middle" font-size="9" fill="#b91c1c">Proposed: 0.0315 pu</text>
  <text x="720" y="203" text-anchor="middle" font-size="9" fill="#b91c1c">TLM: 0.1981 pu</text>
  <text x="720" y="218" text-anchor="middle" font-size="9" fill="#dc2626">数值振荡：完全抑制</text>
  
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#6b7280"/>
    </marker>
  </defs>
  
  <line x1="180" y1="95" x2="240" y2="95" stroke="#6b7280" stroke-width="1.5"/>
  <line x1="440" y1="160" x2="460" y2="160" stroke="#6b7280" stroke-width="1.5"/>
  <line x1="620" y1="160" x2="640" y2="160" stroke="#6b7280" stroke-width="1.5"/>
  
  <rect x="20" y="480" width="12" height="12" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="38" y="490" font-size="9" fill="#374151">输入层</text>
  <rect x="90" y="480" width="12" height="12" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="108" y="490" font-size="9" fill="#374151">分网策略</text>
  <rect x="175" y="480" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="193" y="490" font-size="9" fill="#374151">多速率仿真</text>
  <rect x="290" y="480" width="12" height="12" rx="2" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="308" y="490" font-size="9" fill="#374151">精度判据</text>
  <rect x="385" y="480" width="12" height="12" rx="2" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="403" y="490" font-size="9" fill="#374151">性能输出</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 多速率EMT协同仿真框架：系统分网→多速率求解→精度判据→量化性能</p>

## 相关方法

- [[multirate-method]] — 时间尺度分离的数学框架与多速率积分算法
- [[interpolation-method]] — 接口数据同步的插值策略（零阶保持、线性插值、多项式外推）
- [[thevenin-norton-equivalent]] — 端口等值理论基础（诺顿/戴维南等值变换）
- [[fixed-admittance]] — 固定导纳矩阵并行求解技术（MATE的核心）
- [[numerical-integration]] — EMT数值积分方法（TR/RM/BE等）
- [[parallel-computing]] — 分网并行加速的硬件实现

## 相关模型

- [[fdne-model]] — 宽频端口等值（FDNE），用于宽频暂态仿真的频变接口等值
- [[mmc-model]] — 多速率仿真的典型应用场景（MMC换流器μs级与AC系统ms级协同）
- [[transmission-line-model]] — 自然解耦的基础（Bergerton模型延迟特性）

## 相关主题

- [[electromechanical-electromagnetic-hybrid]] — 多速率接口的典型应用场景
- [[parallel-computing]] — 分网并行加速的支撑技术
- [[co-simulation]] — 多求解器分网协同仿真的框架
- [[real-time-simulation]] — 实时多速率仿真的时间约束

## 来源论文

- **Shu 2018** — A Multirate EMT Co-simulation of Large AC and MMC-based MTDC Systems（IEEE TPWRS 2017/2018）— 提出移动窗口预测+分步校正+根匹配的多速率协同仿真框架，四端MMC-MTDC系统验证，n=6时精度损失<5%，计算效率提升6倍
- **MATE原始文献** — 多导纳技术的基础理论（见[[fixed-admittance]]页面详细引用）

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第三篇第12章"多速率与分网方法"*
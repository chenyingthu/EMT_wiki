---
title: "节点分析法 (Nodal Analysis)"
type: method
tags: [nodal-analysis, companion-circuit, emtp, network-solution, kcl]
created: "2026-04-13"
updated: "2026-05-10"
---

# 节点分析法 (Nodal Analysis)

## 1. 物理背景与工程需求

### 为什么要有节点分析？

求解一个电路网络，本质上是在解一个方程组。这个方程组来源于两条最基本的物理定律：

- **KCL**（基尔霍夫电流定律）：流入任意节点的电流之和为零
- **KVL**（基尔霍夫电压定律）：沿任意闭合回路的电压降之和为零

如果直接用这两条定律列方程，得到的是混合的微分-代数方程组——既有节点电压，又有支路电流，还有电感、电容的状态变量。对于一个几百个节点的电网，这种混合方程的求解规模非常大。

节点分析的**核心思想**是：把每个元件都表示为等效电流源（诺顿等效），使得列出来的方程只含节点电压一个未知量。这样就把一个庞大的混合问题简化成了纯粹的线性代数问题。

```text
元件特性 + 拓扑连接 → KCL方程组 → 只有节点电压是未知数
```

### 在 EMT 仿真中的角色

电磁暂态仿真是**时域步进**的——从 $t=0$ 开始，每步算一个时刻，每步都要解一次电路方程。如果每次解一个巨大的混合方程组，仿真会非常慢。

节点分析在 EMT 中相当于**装配线**：它让各个元件（电阻、电感、电容、线路、开关）在每一时步都转化成标准接口（诺顿等效导纳 + 历史电流源），然后统一求解。


<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 840 320" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#333"/>
    </marker>
  </defs>
  <!-- Component layer boxes -->
  <rect x="10" y="40" width="100" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="60" y="69" text-anchor="middle" font-size="14" font-family="Arial">电感 L</text>
  <rect x="10" y="100" width="100" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="60" y="129" text-anchor="middle" font-size="14" font-family="Arial">电容 C</text>
  <rect x="10" y="160" width="100" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="60" y="189" text-anchor="middle" font-size="14" font-family="Arial">电阻 R</text>
  <rect x="10" y="220" width="100" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="60" y="249" text-anchor="middle" font-size="14" font-family="Arial">输电线路</text>
  <text x="60" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af" font-family="Arial">元件层</text>
  <!-- Arrows L1→L2 -->
  <line x1="110" y1="65" x2="200" y2="65" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="110" y1="125" x2="200" y2="125" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="110" y1="185" x2="200" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="110" y1="245" x2="200" y2="245" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <!-- Interface layer boxes -->
  <rect x="200" y="40" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="280" y="60" text-anchor="middle" font-size="12" font-family="Arial">等效导纳 + 历史源</text>
  <text x="280" y="76" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">G_eq + I_hist</text>
  <rect x="200" y="100" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="280" y="120" text-anchor="middle" font-size="12" font-family="Arial">等效导纳 + 历史源</text>
  <text x="280" y="136" text-anchor="middle" font-size="11" font-family="Arial" fill="#555">G_eq + I_hist</text>
  <rect x="200" y="160" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="280" y="189" text-anchor="middle" font-size="14" font-family="Arial">电导 g</text>
  <rect x="200" y="220" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="280" y="240" text-anchor="middle" font-size="12" font-family="Arial">多端口等效导纳</text>
  <text x="280" y="256" text-anchor="middle" font-size="12" font-family="Arial">矩阵</text>
  <text x="280" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534" font-family="Arial">接口层（诺顿等效）</text>
  <!-- Arrows L2→L3 converging -->
  <line x1="360" y1="65" x2="450" y2="110" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="360" y1="125" x2="450" y2="110" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="360" y1="185" x2="450" y2="110" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="360" y1="245" x2="450" y2="110" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <!-- Network solution layer -->
  <rect x="450" y="55" width="170" height="110" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2.5"/>
  <text x="535" y="85" text-anchor="middle" font-size="14" font-weight="bold" font-family="Arial">组装 Y_n</text>
  <text x="535" y="105" text-anchor="middle" font-size="12" font-family="Arial">节点导纳矩阵</text>
  <line x1="465" y1="115" x2="605" y2="115" stroke="#d97706" stroke-width="0.8"/>
  <text x="535" y="135" text-anchor="middle" font-size="14" font-weight="bold" font-family="Arial">求解 Y_n · v = i</text>
  <text x="535" y="153" text-anchor="middle" font-size="12" font-family="Arial">→ 节点电压 v</text>
  <text x="535" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="Arial">网络求解层</text>
  <!-- Legend -->
  <rect x="650" y="10" width="180" height="280" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="740" y="32" text-anchor="middle" font-size="12" font-weight="bold" fill="#333" font-family="Arial">图例</text>
  <rect x="665" y="45" width="40" height="20" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="715" y="59" text-anchor="start" font-size="12" fill="#333" font-family="Arial">输入源</text>
  <rect x="665" y="75" width="40" height="20" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="715" y="89" text-anchor="start" font-size="12" fill="#333" font-family="Arial">处理/模型</text>
  <rect x="665" y="105" width="40" height="20" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="715" y="119" text-anchor="start" font-size="12" fill="#333" font-family="Arial">算法/输出</text>
  <line x1="665" y1="140" x2="705" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  <text x="715" y="144" text-anchor="start" font-size="12" fill="#333" font-family="Arial">信号流</text>
  <line x1="665" y1="168" x2="705" y2="168" stroke="#333" stroke-width="1.5"/>
  <text x="715" y="172" text-anchor="start" font-size="12" fill="#333" font-family="Arial">汇聚连接</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 节点分析法"元件-接口-求解"三层架构</p>

这种"元件-接口-求解"三层分离架构，使得 EMT 仿真程序具有良好的可扩展性——新元件只需要实现自己的伴随电路接口，不需要修改网络求解器。

---

## 2. 数学描述

### 从 KCL 到矩阵方程

考虑一个 $N$ 个节点的电路。对节点 $k$，KCL 给出：

$$
\sum_{j} i_{kj} = 0
$$

其中 $i_{kj}$ 是从节点 $k$ 流向节点 $j$ 的电流。如果支路 $(k,j)$ 是一个电导 $g_{kj}$，则：

$$
i_{kj} = g_{kj}(v_k - v_j)
$$

代入 KCL 并整理：

$$
(\sum_j g_{kj}) v_k - \sum_{j \neq k} g_{kj} v_j = 0
$$

对所有节点写出上述方程，就得到了节点方程的矩阵形式：

$$
\mathbf{Y}_n \mathbf{v} = \mathbf{i}
$$

其中：

- $\mathbf{Y}_n \in \mathbb{R}^{N \times N}$：节点导纳矩阵
  - 对角线元素 $Y_{kk} = \sum_j g_{kj}$（与节点 $k$ 相连的所有支路电导之和）
  - 非对角线元素 $Y_{kj} = -g_{kj}$（支路电导取负）
- $\mathbf{v} \in \mathbb{R}^{N}$：节点电压向量（待求解）
- $\mathbf{i} \in \mathbb{R}^{N}$：注入电流向量（独立电流源 + 历史电流源）

### 方程的物理含义

这个方程的每一行都是在说一件事：**节点 $k$ 上的净注入电流等于从该节点流向所有相邻节点的电流之和**。换句话说，它就是 KCL 的代数形式。

把方程展开来看更清楚。对于节点 $k$：

$$
g_{k1}(v_k - v_1) + g_{k2}(v_k - v_2) + \cdots + g_{kN}(v_k - v_N) = i_k
$$

左边每一项 $g_{kj}(v_k - v_j)$ 都是从节点 $k$ 流向节点 $j$ 的电流。如果某一对节点之间没有直接连接，对应的 $g_{kj} = 0$。

### 节点导纳矩阵的装配规则

对一个连接在节点 $p$ 和 $q$ 之间的支路电导 $g$，它对矩阵的贡献非常直观：

$$
Y_{pp} \mathrel{+}= g, \quad Y_{qq} \mathrel{+}= g, \quad Y_{pq} \mathrel{-}= g, \quad Y_{qp} \mathrel{-}= g
$$

这种装配方式是**叠加的**——每个元件独立贡献，最终矩阵是所有元件贡献的叠加。这给编程实现带来了极大的便利：遍历所有元件，把每个元件的导纳贡献累加到对应位置即可。

### 参考节点的处理

节点方程中有一个自由度是冗余的——整个系统的电压基准需要指定。通常选取大地（或某一节点）作为参考节点（地节点），其电压固定为零，不参与方程求解。这样，矩阵 $

tbf{Y}_n$ 是 $(N-1) \times (N-1)$ 的（若总共有 $N$ 个节点，其中一个为地）。

---

## 3. 计算模型与离散化

### 动态元件的伴随电路转化

这是节点分析在 EMT 中发挥作用的关键一步。一个动态元件（电感、电容）在连续时域中是由微分方程描述的，但在数字计算机上，我们只能处理代数方程。**数值积分把微分方程离散化，而伴随电路把离散后的方程表现为等效电路。**

#### 电容

电容的特性方程：

$$
i_C(t) = C \frac{dv_C(t)}{dt}
$$

用梯形法在 $t_k$ 时刻离散：

$$
i_C(t_k) = \frac{2C}{\Delta t} v_C(t_k) - \left[ \frac{2C}{\Delta t} v_C(t_{k-1}) + i_C(t_{k-1}) \right]
$$

记 $G_{eq} = 2C/\Delta t$，$I_{hist} = -[G_{eq} v_C(t_{k-1}) + i_C(t_{k-1})]$，则：

$$
i_C(t_k) = G_{eq} v_C(t_k) + I_{hist}
$$

这就是一个电导 $G_{eq}$ 与电流源 $I_{hist}$ 并联的**诺顿等效电路**。

#### 电感

电感的特性方程：

$$
v_L(t) = L \frac{di_L(t)}{dt}
$$

同理离散：

$$
i_L(t_k) = \frac{\Delta t}{2L} v_L(t_k) + \left[ i_L(t_{k-1}) + \frac{\Delta t}{2L} v_L(t_{k-1}) \right]
$$

记 $G_{eq} = \Delta t/(2L)$，$I_{hist} = i_L(t_{k-1}) + G_{eq} v_L(t_{k-1})$，则：

$$
i_L(t_k) = G_{eq} v_L(t_k) + I_{hist}
$$

同样是一个诺顿等效电路。


<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#333"/>
    </marker>
  </defs>
  <!-- Continuous time domain -->
  <rect x="10" y="50" width="160" height="70" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af" font-family="Arial">连续时域</text>
  <text x="90" y="100" text-anchor="middle" font-size="11" fill="#333" font-family="Arial">电容: i = C·dv/dt</text>
  <text x="90" y="116" text-anchor="middle" font-size="11" fill="#333" font-family="Arial">电感: v = L·di/dt</text>
  <!-- Trapezoidal discretization -->
  <rect x="250" y="50" width="160" height="70" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="330" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="Arial">梯形法离散</text>
  <text x="330" y="100" text-anchor="middle" font-size="11" fill="#333" font-family="Arial">i_k = 2C/Δt · v_k + I_hist</text>
  <text x="330" y="116" text-anchor="middle" font-size="11" fill="#333" font-family="Arial">i_k = Δt/2L · v_k + I_hist</text>
  <!-- Companion circuit -->
  <rect x="490" y="50" width="160" height="70" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="570" y="78" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534" font-family="Arial">伴随电路</text>
  <text x="570" y="96" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">G_eq=2C/Δt, I_hist含v_{k-1}</text>
  <text x="570" y="110" text-anchor="middle" font-size="10" fill="#333" font-family="Arial">G_eq=Δt/2L, I_hist含i_{k-1}</text>
  <!-- Nodal equation assembly -->
  <rect x="690" y="50" width="160" height="70" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="770" y="80" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6" font-family="Arial">节点方程</text>
  <text x="770" y="100" text-anchor="middle" font-size="12" fill="#333" font-family="Arial">装配到 Y_n 矩阵</text>
  <text x="770" y="116" text-anchor="middle" font-size="12" fill="#333" font-family="Arial">Y_n · v = i</text>
  <!-- Arrows -->
  <line x1="170" y1="85" x2="245" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arr2)"/>
  <line x1="410" y1="85" x2="485" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arr2)"/>
  <line x1="650" y1="85" x2="685" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arr2)"/>
  <!-- Labels above arrows -->
  <text x="207" y="70" text-anchor="middle" font-size="11" fill="#666" font-family="Arial">梯形积分</text>
  <text x="447" y="70" text-anchor="middle" font-size="11" fill="#666" font-family="Arial">诺顿等效</text>
  <text x="667" y="70" text-anchor="middle" font-size="11" fill="#666" font-family="Arial">组装</text>
  <!-- Legend -->
  <rect x="10" y="160" width="840" height="120" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1"/>
  <text x="430" y="182" text-anchor="middle" font-size="12" font-weight="bold" fill="#333" font-family="Arial">关键离散化公式汇总</text>
  <line x1="30" y1="190" x2="830" y2="190" stroke="#e2e8f0" stroke-width="0.8"/>
  <!-- Formula box 1: Capacitor -->
  <rect x="30" y="200" width="390" height="65" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="225" y="220" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af" font-family="Arial">电容梯形法离散</text>
  <text x="225" y="240" text-anchor="middle" font-size="12" font-family="Arial">i_C(t_k) = (2C/Δt)·v_C(t_k) + I_hist</text>
  <text x="225" y="258" text-anchor="middle" font-size="11" fill="#555" font-family="Arial">I_hist = −(2C/Δt)·v_C(t_{k−1}) − i_C(t_{k−1})</text>
  <!-- Formula box 2: Inductor -->
  <rect x="440" y="200" width="390" height="65" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="635" y="220" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534" font-family="Arial">电感梯形法离散</text>
  <text x="635" y="240" text-anchor="middle" font-size="12" font-family="Arial">i_L(t_k) = (Δt/2L)·v_L(t_k) + I_hist</text>
  <text x="635" y="258" text-anchor="middle" font-size="11" fill="#555" font-family="Arial">I_hist = i_L(t_{k−1}) + (Δt/2L)·v_L(t_{k−1})</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图2 · 伴随电路离散化：从连续时域到节点方程的三阶段映射</p>

### 关键洞察

上表中隐含了一个非常重要的结论：**等效电导 $G_{eq}$ 只取决于元件参数 $C$（或 $L$）和步长 $\Delta t$，与历史状态无关。** 这意味着：

1. 如果步长不变，等效电导在仿真过程中保持不变
2. 矩阵 $\mathbf{Y}_n$ 只需在步长变化或开关动作时才需要重新分解
3. 每个时步的计算量主要是：装配右端项 $\mathbf{i}$ + 一次前代回代

这是 EMTP 类程序能够高效运行的根本原因。

### 其他积分公式的影响

上面的推导用了梯形法。如果改用其他积分公式，等效电导的形式会不同：

| 积分方法 | 电容等效电导 $G_{eq}$ | 特性 |
|----------|----------------------|------|
| 后向欧拉 | $C/\Delta t$ | L-稳定，无数值振荡 |
| 梯形法 | $2C/\Delta t$ | A-稳定，可能有数值振荡 |
| Gear-2 | $3C/(2\Delta t)$ | L-稳定，精度较低 |
| 2S-DIRK | 取决于具体格式 | L-稳定，高阶精度 |

这就是"节点分析本身不保证数值特性，数值特性取决于积分公式"的含义。

---

## 4. 实现方法与算法细节

### 一个完整时步的计算流程

在 EMT 中，每一时步的节点分析流程如下：

```text
输入: 本时步的电压/电流历史值, 步长 Δt

1. 更新所有元件的诺顿等效
   - 对每类元件, 计算其历史电流源 I_hist
   - 注意: 若步长未变且无开关动作, G_eq 不需重算

2. 装配右端电流向量 i
   - 将所有元件的 I_hist 和独立电流源叠加到对应节点

3. 求解节点方程
   - 若 Y_n 不变: 前代回代 (O(n²) 稀疏求解)
   - 若 Y_n 变化: 重新 LU 分解 + 前代回代

4. 更新支路量
   - 从节点电压回代计算各支路电流
   - 更新元件的状态变量 (电容电压、电感电流等)

输出: 本时步的节点电压和所有支路量
```

### 矩阵复用与重新分解

$

tbf{Y}_n$ 的 LU 分解是整个仿真中计算量最大的步骤之一。实际程序中会用以下策略减少分解次数：

- **恒导纳模型**：开关动作时不改变矩阵，通过补偿法或插值来模拟开关效果
- **部分重分解**：只更新矩阵中受开关影响的几个元素，对 LU 因子做局部修正
- **符号分解 + 数值分解分离**：矩阵稀疏模式不变时，只用重做数值分解

### 与稀疏矩阵求解器的配合

实际电网的节点导纳矩阵是高度稀疏的（每个节点只与少数几个节点相连）。因此节点方程不会用稠密高斯消去法求解，而是使用专门的稀疏矩阵技术：

- **KLU 求解器**：EMTP 类程序中最常用的稀疏求解器
- **AMD 重排序**：减少 LU 分解中的填充元
- **BTF 预处理**：将矩阵分解为块三角形式，每个块独立求解

---

## 5. 适用边界与失效模式

### 什么条件下好用？

- 网络拓扑清晰，大部分元件可用导纳或诺顿等效表示
- 电网规模大但连接稀疏（稀疏性使得求解效率高）
- 步长相对于系统最快暂态足够小

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 数值振荡 | 开关动作后电压/电流出现非物理振荡 | 梯形法在突变时无法快速衰减高频分量 | 切换为后向欧拉、CDA 算法、或插值法 |
| 矩阵病态 | 求解结果精度丧失 | 断路支路使用过小导纳、闭合支路使用过大导纳 | 合理选择开关电导比值（通常 $10^{4}\sim10^{6}$） |
| 奇异回路 | 节点方程无解 | 理想开关形成仅含电压源的回路 | 增加寄生电阻或使用增广节点法 |
| 接口延迟 | 分网仿真精度下降 | 子网间信息交换滞后一时步 | 使用迭代接口或预测-校正方法 |
| 非线性迭代发散 | 牛顿法不收敛 | 雅可比矩阵更新不及时或初始猜测不好 | 减小步长、使用阻尼牛顿法 |

### 工程经验值

- 开关电导比（开态/关态）推荐 $10^{5}$ 左右，太大或太小都会恶化矩阵条件数
- 梯形法 + CDA 的组合是 EMTP 中最成熟的工程方案
- 恒导纳模型需要配合延迟和插值，不能仅靠矩阵不变就声称"精确"

---

## 6. 一个简单的数值算例

考虑一个 RC 串联电路：电阻 $R=100\Omega$，电容 $C=10\mu\text{F}$，电压源 $V_s = 100\text{V}$（阶跃输入）。求电容电压 $v_C(t)$ 的响应。

**步骤 1：节点方程**

电路中只有两个节点（地 + 节点1），节点方程为：

$$
\left(\frac{1}{R} + \frac{2C}{\Delta t}\right) v_1(t_k) = \frac{V_s}{R} + \left[\frac{2C}{\Delta t} v_1(t_{k-1}) + i_C(t_{k-1})\right]
$$

**步骤 2：节点方程的迭代求解**（取 $\Delta t = 50\mu\text{s}$）

该电路时间常数 $\tau = RC = 1$ms，解析解 $v_C(t) = V_s(1 - e^{-t/RC})$。

每步先根据上一时步的状态计算历史电流源，然后求解节点方程得到新的 $v_1$，再从 $v_1$ 回代电流 $i_C$ 供下一步使用。读者可代入参数自行验证：梯形法伴随电路的数值解会以二阶精度收敛到解析解。

如果把步长增大到 $500\mu\text{s}$ 并在 $t = \tau$ 处突然切除电容（开关动作），梯形法就会出现明显的数值振荡，需要切换到后向欧拉来阻尼。


---

## 来源论文

节点分析法的奠基性参考文献如下，按发表年份组织：

| 论文 | 年份 |
|------|------|
| Dommel H.W., "Digital Computer Solution of Electromagnetic Transients in Single- and Multi-Phase Networks," *IEEE Transactions on Power Apparatus and Systems*, PAS-88(4), 1969 | 1969 |
| Dommel H.W., "Nonlinear and Time-Varying Elements in the EMTP — A New Preprocessor," *IEEE PAS-TPS*, 1986 | 1986 |
| Sae-Long W., Ji-祁, "A Nodal Approach for Electromagnetic Transient Simulation," *IEEJ Transactions on Electrical Engineering*, 2003 | 2003 |
| Chiu H.C., "State Space Nodal Analysis for Transient Stability and EMT Simulation," *IEEE PES GM*, 2011 | 2011 |


---
title: "递归卷积 (Recursive Convolution)"
type: method
tags: [recursive-convolution, frequency-dependent, transmission-line, transient-analysis, ulm, model-order-reduction]
created: "2026-05-04"
updated: "2026-05-19"
---

# 递归卷积 (Recursive Convolution)

## 定义与边界

递归卷积（Recursive Convolution，RC）是一种用于电磁暂态（EMT）仿真中计算频变参数元件历史项的数值方法。其核心思想是将时域卷积运算转换为递推形式，避免每步存储完整历史数据，从而将存储需求从 $O(N)$ 降至 $O(1)$，计算复杂度从每步 $O(N)$ 降至 $O(1)$（$N$ 为时间步数）。

在 EMT 仿真中，递归卷积主要应用于：
- 频变参数输电线路模型的时域实现（如 ULM、JMarti 模型）
- 频变阻抗元件的暂态响应计算
- 多导体传输线模域模型的历史项更新
- 电缆系统的分布参数建模

**边界限定**：本方法不适用于非线性元件、时变参数系统或需要完整历史信息的频域分析。

## EMT中的作用

递归卷积解决了频变模型在时域仿真中的关键计算瓶颈：

- **存储效率**：将 $O(N)$ 存储需求降为 $O(1)$，其中 $N$ 为时间步数
- **计算效率**：每步计算复杂度从 $O(N)$ 降至 $O(1)$
- **数值稳定性**：通过适当的极点-留数分解保证递推稳定性
- **精度保持**：在保持频变特性精度的同时实现实时或近实时仿真

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 920 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1: Frequency domain fitting -->
  <rect x="10" y="20" width="200" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="45" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">频域有理函数拟合</text>
  <text x="110" y="62" text-anchor="middle" font-size="11" fill="#1e40af">矢量拟合 → 极点/留数</text>
  <text x="110" y="78" text-anchor="middle" font-size="11" fill="#1e40af">$Y_C(s), H(s)$</text>

  <!-- Arrow 1->2 -->
  <line x1="210" y1="60" x2="255" y2="60" stroke="#333" stroke-width="2"/>
  <polygon points="255,60 247,55 247,65" fill="#333"/>

  <!-- Layer 2: Modal decomposition -->
  <rect x="260" y="20" width="200" height="80" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="360" y="45" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">模态域分解</text>
  <text x="360" y="62" text-anchor="middle" font-size="11" fill="#92400e">特征值分解 $T_I$</text>
  <text x="360" y="78" text-anchor="middle" font-size="11" fill="#92400e">$e^{-\lambda_j\ell}$ 指数和</text>

  <!-- Arrow 2->3 -->
  <line x1="460" y1="60" x2="505" y2="60" stroke="#333" stroke-width="2"/>
  <polygon points="505,60 497,55 497,65" fill="#333"/>

  <!-- Layer 3: RC state update -->
  <rect x="510" y="20" width="200" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="610" y="45" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">递归卷积状态更新</text>
  <text x="610" y="62" text-anchor="middle" font-size="11" fill="#166534">历史电流递推</text>
  <text x="610" y="78" text-anchor="middle" font-size="11" fill="#166534">$j_{kn}(t+\Delta t)$</text>

  <!-- Arrow 3->4 -->
  <line x1="710" y1="60" x2="755" y2="60" stroke="#333" stroke-width="2"/>
  <polygon points="755,60 747,55 747,65" fill="#333"/>

  <!-- Layer 4: Norton equivalent -->
  <rect x="760" y="20" width="150" height="80" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="835" y="45" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">诺顿等效电路</text>
  <text x="835" y="62" text-anchor="middle" font-size="11" fill="#5b21b6">$G = k_0 + \sum q_n$</text>
  <text x="835" y="78" text-anchor="middle" font-size="11" fill="#5b21b6">$i_{k,hist}(t)$</text>

  <!-- Bottom flow: each time step -->
  <rect x="260" y="140" width="400" height="60" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="460" y="165" text-anchor="middle" font-size="13" font-weight="bold" fill="#475569">每个仿真时间步 $\Delta t$（$O(1)$ 计算）</text>
  <text x="460" y="183" text-anchor="middle" font-size="11" fill="#475569">① 读取端电压 $v_k(t)$ → ② 更新历史电流 $j_{kn}$ → ③ 注入诺顿电流 → ④ 返回主求解器</text>

  <!-- Connection to bottom -->
  <line x1="360" y1="100" x2="360" y2="140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="460" y1="100" x2="460" y2="140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="610" y1="100" x2="610" y2="140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="710" y1="100" x2="710" y2="140" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,2"/>

  <!-- Quantitative box -->
  <rect x="10" y="240" width="900" height="180" rx="8" fill="#fafafa" stroke="#e2e8f0" stroke-width="1.5"/>
  <text x="460" y="265" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">量化性能边界</text>

  <text x="30" y="290" font-size="12" font-weight="bold" fill="#1e293b">存储效率：</text>
  <text x="30" y="308" font-size="11" fill="#334155">传统卷积：$O(N)$ · RC：$O(1)$（存储当前和前一时刻值）</text>

  <text x="30" y="332" font-size="12" font-weight="bold" fill="#1e293b">计算效率：</text>
  <text x="30" y="350" font-size="11" fill="#334155">每步计算：$O(1)$（与时间步数无关）· 内存占用 $\propto N_C^2$（导体数）</text>
  <text x="30" y="368" font-size="11" fill="#334155">实时仿真：$N_C=6$ 时单步 < 0.1 ms（Zanon 2021）</text>

  <text x="460" y="290" font-size="12" font-weight="bold" fill="#1e293b">拟合精度：</text>
  <text x="460" y="308" font-size="11" fill="#334155">$Y_C$ 拟合 RMSE < 1×10⁻⁴</text>
  <text x="460" y="326" font-size="11" fill="#334155">$H$ 拟合误差 < 0.5%（1 Hz ~ 1 MHz）</text>
  <text x="460" y="344" font-size="11" fill="#334155">优化时延使高频拟合误差较无损假设降低约 60%</text>

  <text x="460" y="368" font-size="12" font-weight="bold" fill="#1e293b">全局误差：</text>
  <text x="460" y="386" font-size="11" fill="#334155">历史电流补偿后系统全局误差 < 0.1%（Zanon 2021）</text>

  <text x="30" y="400" font-size="12" font-weight="bold" fill="#1e293b">模型降阶加速（De Silva 2025）：</text>
  <text x="30" y="418" font-size="11" fill="#334155">模态截断（MT）剔除小留数极点，传播矩阵阶数从 18 阶降至 3~5 阶</text>
  <text x="30" y="436" font-size="11" fill="#334155">平衡截断（BT）数学保证渐近稳定性，提供先验误差界</text>

  <!-- Legend -->
  <rect x="760" y="240" width="150" height="30" rx="5" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="775" y="258" font-size="10" fill="#64748b">■ 输入/频域拟合</text>
  <text x="835" y="258" font-size="10" fill="#64748b">■ 算法</text>

  <rect x="760" y="275" width="150" height="30" rx="5" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
  <text x="775" y="293" font-size="10" fill="#64748b">■ 等效电路</text>
  <text x="835" y="293" font-size="10" fill="#64748b">■ 时域执行</text>

  <!-- Key formulas box -->
  <text x="460" y="470" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">核心公式（Zanon 2021）</text>
  <text x="460" y="490" text-anchor="middle" font-size="11" fill="#334155">$j_{kn}(t) = p_n j_{kn}(t-\Delta t) + q_n v_k(t) + r_n v_k(t-\Delta t)$（历史电流递推）</text>
  <text x="460" y="508" text-anchor="middle" font-size="11" fill="#334155">$G = k_0 + \sum_{n=1}^{N_{pY}} q_n$（诺顿等效电导）</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 递归卷积在频变线路模型中的工作流程：频域有理函数拟合 → 模态分解 → 递归状态更新 → 诺顿等效电路注入 EMT 网络方程</p>

## 主要分支与机制

### 1. 基于指数函数的递归卷积

适用于具有有理函数频变特性的元件，通过极点-留数展开：

$$Y(s) = \sum_{i=1}^{n} \frac{k_i}{s-p_i}$$

时域核函数表示为指数和：

$$h(t) = \sum_{i=1}^{n} k_i e^{p_i t}$$

通过部分分式展开，每个指数项可在时域中独立递推。

### 2. 基于特性阻抗的递归卷积

用于传输线模型，将特性阻抗的历史项表示为：

$$h(t) = \sum_{i=1}^{m} A_i e^{-\alpha_i t}$$

其中 $A_i$ 为留数，$\alpha_i = -p_i$ 为衰减常数。

### 3. 模态域递归卷积

在多导体线路分析中，对各模态分别应用递归卷积。模态传播函数经特征值分解后：

$$e^{-\lambda_j \ell} = \sum_{i=1}^{N_j} \frac{c_{ij}}{s - a_i} e^{-s\tau_j}$$

时域实现中，端口电流表达式为：

$$i_k(t) = \sum_{j=1}^{n} Y_{kj}(0) v_j(t) + \sum_{j=1}^{n} h_{kj}(t)$$

### 4. 模型降阶增强（MT/BT）

De Silva 2025 在标准递归卷积流程中引入两类模型降阶（MOR）技术：

**模态截断（MT）**：按 $\|c_k\|/|a_k| > \text{tol}$ 判据剔除非主导极点项，将传播矩阵阶数从最高 18 阶压缩至 3~5 阶，使递归卷积状态数显著减少。

**平衡截断（BT）**：将频域有理函数转为状态空间实现 $(A,B,C)$，通过 Lyapunov 方程计算能控/能观 Gramian，截断弱能控能观状态，严格保证降阶后模型的渐近稳定性并提供先验误差界：

$$A = S^{-1}AS, \quad B = S^{-1}B, \quad C = CS$$

## 形式化表达

### 基本递推公式

对于具有指数衰减特性的核函数，递归卷积的历史项可表示为：

$$h(t) = \sum_{i=1}^{n} h_i(t)$$

其中各分量满足递推关系：

$$h_i(t) = k_i x(t) + e^{-\Delta t/\tau_i} h_i(t-\Delta t)$$

式中：
- $k_i$ 为第 $i$ 个留数
- $\tau_i$ 为第 $i$ 个时间常数
- $\Delta t$ 为仿真时间步长
- $x(t)$ 为当前输入量

### 频变导纳的时域实现

对于频变导纳 $Y(s)$，端口电流可表示为：

$$i(t) = Y_0 v(t) + \sum_{k=1}^{K} i_k(t)$$

其中历史电流分量满足：

$$i_k(t+\Delta t) = \alpha_k i_k(t) + \beta_k [v(t+\Delta t) + v(t)]$$

系数由极点 $p_k$ 和留数 $r_k$ 决定：

$$\alpha_k = e^{p_k \Delta t}, \quad \beta_k = \frac{r_k}{p_k \Delta t}(1-\alpha_k)$$

### ULM 递归卷积完整递推（Zanon 2021）

特征导纳矩阵 $Y_C$ 的时域递推（式 19）：

$$j_{kn}(t) = p_n j_{kn}(t-\Delta t) + q_n v_k(t) + r_n v_k(t-\Delta t)$$

诺顿等效电导（式 16）：

$$G = k_0 + \sum_{n=1}^{N_{pY}} q_n$$

历史电流源更新（式 17）：

$$i_{k,hist}(t) = -j_{kh}(t-\Delta t) + b_k(t)$$

其中 $b_k(t)$ 由传播矩阵 $H$ 的历史卷积贡献决定。

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 |
|------|------|
| 频域特性 | 可用有理函数近似或有指数衰减形式 |
| 时间步长 | $\Delta t \ll \min(\tau_i)$ 以保证数值稳定性 |
| 线性时不变 | 仅适用于线性时不变元件 |
| 精度要求 | 需验证有理近似的频域精度 |

### 失效边界

- **极点位置**：当极点实部接近零（长时程）或虚部很大（高频振荡）时，递推可能不稳定
- **刚性系统**：时间常数跨度很大（$\tau_{\max}/\tau_{\min} > 10^6$）时，可能产生数值误差
- **非线性效应**：不适用于饱和、电弧等非线性现象
- **多端口耦合**：强耦合多导体系统需要特殊处理交叉模态

### 关键假设

1. 频变特性可用有限阶有理函数充分近似
2. 仿真时间步长足够小以满足稳定性条件
3. 系统在工作点附近可线性化

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 特征导纳拟合 RMSE | < 1×10⁻⁴ | Zanon 2021 |
| 传播矩阵拟合误差 | < 0.5%（1 Hz ~ 1 MHz） | Zanon 2021 |
| 全局误差（补偿后） | < 0.1% | Zanon 2021 |
| 实时单步计算时间 | < 0.1 ms（$N_C=6$） | Zanon 2021 |
| 高频拟合改善 | 较无损延迟假设降低约 60% | Zanon 2021 |
| 地回路阻抗误差（土壤频变） | 从 >15% 降至 <2%（10 kHz~1 MHz） | Zanon 2021 |
| 传播矩阵初始阶数 | 最高 18 阶 | De Silva 2025 |
| MT 降阶后阶数 | 3~5 阶（剔除冗余极点） | De Silva 2025 |
| BT 先验误差界 | 严格保证（Lyapunov 稳定性） | De Silva 2025 |

## 相关方法

- [[frequency-dependent-modeling]] - 频变建模的综述
- [[transmission-line-model]] - 输电线路模型
- [[vector-fitting]] - 频变特性有理近似方法
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间实现替代方案
- [[modal-transformation]] - 模态变换与递归卷积的结合
- [[finite-element-method]] - 有限元方法在频变建模中的应用
- [[passivity-enforcement]] - 无源性强制（解决过拟合导致的无源性破坏）

## 来源论文

- Zanon 2021 — 在 ATP 中实现通用线路模型（ULM），提出两阶段混合架构（MATLAB 拟合 + C 语言递归卷积），给出诺顿等效电路递推公式和量化精度数据
- De Silva 2025 — 针对频变线路传播矩阵阶数过高问题，提出模态截断（MT）与平衡截断（BT）两类模型降阶技术，量化降阶前后阶数和拟合误差
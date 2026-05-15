---
title: "矢量拟合"
type: method
tags: [rational-approximation, pole-residue-model, frequency-dependent-modeling, fdne, state-space]
created: "2026-04-13"
updated: "2026-05-15"
---

# 矢量拟合

## 定义与边界

矢量拟合（Vector Fitting, VF）是一种频域有理函数逼近方法，通过迭代极点重定位把离散频率响应拟合为极点-留数模型。其核心目标形式为：

$$f(s) = \sum_{n=1}^{N} \frac{c_n}{s - a_n} + d + s h \tag{1}$$

其中 $a_n$ 为极点（实数或复数共轭对），$c_n$ 为留数，$d$ 为常数项，$h$ 为高频渐近斜率项。对多端口系统的导纳矩阵有：

$$\mathbf{Y}(s) \approx \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D} + s\mathbf{E} \tag{2}$$

VF 解决的是"由频域采样得到可时域实现的有理模型"这一核心问题。它不直接保证模型接入 EMT 后无源、稳定或实时可运行——这些需要 [[passivity-enforcement]]、离散化和时域验证。它也不负责给出物理材料参数，除非拟合模型与物理参数之间有额外映射。

VF 的价值在于把宽频响应压缩为有限阶模型。模型阶数、频率范围、采样密度、权重和初始极点决定拟合结果；离开这些条件谈"高精度""最优"或"实时"都不够严谨。

## EMT 中的作用

VF 是 [[frequency-dependent-modeling]] 和 [[fdne-model]] 的关键工具。线路、电缆、变压器、外部网络和黑箱设备的阻抗/导纳频率响应经过 VF 后，可转为递推卷积、状态空间模型或等效 RLC 网络，从而进入 EMT 时间步进。

VF 的核心价值在于把频域响应转换为时域可计算的有理模型。Gustavsen 1999 证明，当频率响应 $H(j\omega)$ 在 $N$ 个频点被采样后，可用式 (1) 的有理函数逼近，从而使时域卷积变为状态空间递推：

$$i(t) = \sum_{m=1}^{M} R_m e^{p_m t} \otimes v(t) + D \cdot v(t) + E \cdot \frac{dv(t)}{dt} \tag{3}$$

VF 的应用场景包括：
- **线路宽频建模**：将频率相关线路参数 $Z(\omega)$ 拟合为有理函数，实现时域递推卷积
- **变压器高频模型**：拟合绕组谐振阻抗，控制铁芯涡流损耗效应
- **FDNE 等值**：外部网络在关注频段内的等效导纳矩阵（多端口有理逼近）
- **黑箱设备接口**：直流换流站、FACTS 设备的宽频阻抗特性

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <!-- 标题 -->
  <text x="450" y="25" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">图1 · 矢量拟合 VF 两阶段算法流程</text>
  
  <!-- 阶段1: 初始设置 -->
  <rect x="20" y="45" width="200" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="120" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">初始设置</text>
  <text x="120" y="88" text-anchor="middle" font-size="11" fill="#333">频域采样点</text>
  <text x="120" y="104" text-anchor="middle" font-size="11" fill="#333">$H(s_j), j=1,...,N$</text>
  <text x="120" y="120" text-anchor="middle" font-size="11" fill="#333">设置起始极点 $\bar{p}_m$</text>

  <!-- 箭头 A->B -->
  <line x1="220" y1="85" x2="260" y2="85" stroke="#333" stroke-width="2"/>
  <polygon points="260,85 252,80 252,90" fill="#333"/>

  <!-- 阶段2: 迭代求解 -->
  <rect x="270" y="45" width="200" height="150" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="370" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">迭代重定位极点</text>
  <text x="370" y="88" text-anchor="middle" font-size="11" fill="#333">Step 1: 求解线性 LS</text>
  <text x="370" y="104" text-anchor="middle" font-size="11" fill="#333">$[\mathbf{A}]\mathbf{x} = \mathbf{b}$</text>
  <text x="370" y="120" text-anchor="middle" font-size="11" fill="#333">提取 $\sigma(s)$ 零点</text>
  <text x="370" y="136" text-anchor="middle" font-size="11" fill="#333">作为新极点 $\bar{p}_m$</text>
  <text x="370" y="152" text-anchor="middle" font-size="11" fill="#333">返回 Step 1 迭代</text>
  <text x="370" y="168" text-anchor="middle" font-size="11" fill="#333">判断收敛条件</text>

  <!-- 收敛判断 -->
  <text x="370" y="188" text-anchor="middle" font-size="11" fill="#333">收敛?</text>
  <line x1="370" y1="195" x2="370" y2="210" stroke="#333" stroke-width="1.5"/>
  <text x="370" y="222" text-anchor="middle" font-size="10" fill="#666">否 → 返回 Step 1</text>
  <line x1="370" y1="195" x2="370" y2="210" stroke="#333" stroke-width="1.5"/>
  <text x="370" y="238" text-anchor="middle" font-size="10" fill="#666" font-weight="bold">是 → 进入 Step 2</text>

  <!-- 箭头 B->C -->
  <line x1="470" y1="85" x2="510" y2="85" stroke="#333" stroke-width="2"/>
  <polygon points="510,85 502,80 502,90" fill="#333"/>

  <!-- 阶段3: 最终求解 -->
  <rect x="520" y="45" width="200" height="100" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="620" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">固定极点求留数</text>
  <text x="620" y="88" text-anchor="middle" font-size="11" fill="#333">Step 2: 固定极点 $p_m$</text>
  <text x="620" y="104" text-anchor="middle" font-size="11" fill="#333">重新求解留数 $c_n$</text>
  <text x="620" y="120" text-anchor="middle" font-size="11" fill="#333">求得常数项 $d$ 和 $h$</text>

  <!-- 箭头 C->D -->
  <line x1="720" y1="95" x2="760" y2="95" stroke="#333" stroke-width="2"/>
  <polygon points="760,95 752,90 752,100" fill="#333"/>

  <!-- 阶段4: 输出 -->
  <rect x="770" y="45" width="110" height="100" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="825" y="68" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">输出模型</text>
  <text x="825" y="88" text-anchor="middle" font-size="11" fill="#333">有理函数模型</text>
  <text x="825" y="104" text-anchor="middle" font-size="11" fill="#333">状态空间/FDNE</text>
  <text x="825" y="120" text-anchor="middle" font-size="11" fill="#333">/ 等效 RLC 网络</text>

  <!-- 无源性检查 -->
  <rect x="520" y="165" width="200" height="60" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="620" y="188" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b">无源性检查</text>
  <text x="620" y="208" text-anchor="middle" font-size="11" fill="#333">检验 $\mathbf{Y}(j\omega)$ 正实性</text>
  <text x="620" y="220" text-anchor="middle" font-size="10" fill="#666">(必要时施加无源性修正)</text>

  <!-- 连接无源性检查 -->
  <line x1="720" y1="145" x2="720" y2="175" stroke="#333" stroke-width="1.5" stroke-dasharray="4"/>
  <line x1="720" y1="175" x2="620" y2="175" stroke="#333" stroke-width="1.5" stroke-dasharray="4"/>
  <polygon points="620,175 615,167 625,167" fill="#333"/>

  <!-- 图例 -->
  <rect x="20" y="280" width="18" height="18" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="45" y="293" font-size="12" fill="#333">输入/采样</text>
  
  <rect x="150" y="280" width="18" height="18" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="175" y="293" font-size="12" fill="#333">迭代算法</text>
  
  <rect x="280" y="280" width="18" height="18" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="305" y="293" font-size="12" fill="#333">最终求解</text>
  
  <rect x="410" y="280" width="18" height="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="435" y="293" font-size="12" fill="#333">输出模型</text>
  
  <rect x="540" y="280" width="18" height="18" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="565" y="293" font-size="12" fill="#333">无源修正</text>

  <!-- 底部注释 -->
  <text x="450" y="320" text-anchor="middle" font-size="11" fill="#666">VF 两阶段算法：阶段1通过辅助函数 $\sigma(s)$ 迭代重定位极点；阶段2固定极点求留数</text>
  <text x="450" y="340" text-anchor="middle" font-size="10" fill="#888">基于 Gustavsen 1999 "Rational Approximation of Frequency Domain Responses by Vector Fitting"</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 矢量拟合 VF 两阶段算法流程</p>

## 核心机制

标准 VF 通过辅助函数 $\sigma(s)$ 把同时优化极点和留数的非线性问题拆成线性最小二乘问题。给定起始极点 $\bar{p}_m$，算法执行两个阶段：

**阶段 1（极点重定位）**：拟合 $\sigma(s)H(s)$ 与 $\sigma(s)$，其中辅助函数取相同极点形式：

$$\sigma(s) = \sum_{m=1}^{M} \frac{1}{s - \bar{p}_m} \tag{4}$$

通过线性最小二乘求解可得 $a_m$（$\sigma$ 的分子系数），进而求得 $\sigma(s)$ 的根作为更新后的极点：

$$a(s) = \prod_{m=1}^{M}(s - \bar{p}_m) = \sum_{m=0}^{M} a_m s^m \tag{5}$$

**阶段 2（留数识别）**：固定收敛后的极点 $p_m$，重新求解留数 $c_n$、常数项 $d$ 和高频项 $h$：

$$\begin{bmatrix} \frac{1}{s_1-p_1} & \cdots & \frac{1}{s_1-p_M} & 1 & s_1 \\ \vdots & \ddots & \vdots & \vdots & \vdots \\ \frac{1}{s_N-p_1} & \cdots & \frac{1}{s_N-p_M} & 1 & s_N \end{bmatrix} \begin{bmatrix} c_1 \\ \vdots \\ c_M \\ d \\ h \end{bmatrix} = \begin{bmatrix} H(s_1) \\ \vdots \\ H(s_N) \end{bmatrix} \tag{6}$$

对多端口系统，常采用公共极点策略：所有矩阵元素共享同一组极点，但留数为矩阵。这样有利于统一状态空间实现，却可能增加阶数。若导纳矩阵小特征值很重要，普通元素级误差可能不足以控制高阻抗端接下的响应误差，需要模态加权或模态 VF。

## 分类与变体

| 变体 | 机制 | EMT 用途 | 边界 |
|------|------|----------|------|
| 标准 VF | 两阶段极点重定位和留数识别 | 单端口或矩阵元素频响拟合 | 对初始极点、权重和频段敏感 |
| 复数 VF (CVF) | 允许独立复极点或复数域响应 | 基带、非对称或变换域模型 | 实值时域实现需额外处理 |
| 模态 VF (MVF) | 在模态分量上加权拟合（逆特征值加权） | 多端口 FDNE、小特征值保护 | 依赖模态变换和矩阵对称性 |
| 快速/并行 VF | 利用稀疏结构、QR 和底层线性代数 | 大规模端口或高采样数拟合 | 加速量绑定实现平台 |
| VF + 降阶 | 拟合后截断弱状态或做 MOR | 实时仿真和 HIL | 降状后需重新检查误差和无源性 |

### 模态 VF (MVF) 的加权策略

Gustavsen 2009 指出，直接拟合多端口导纳矩阵 $\mathbf{Y}$ 时，元素级误差在高阻抗端接下会被放大。模态 VF 通过模态分解解决此问题：

$$\mathbf{Y}(s) = \mathbf{T}^{-1} \mathbf{Y}_\text{modal}(s) \mathbf{T} \tag{7}$$

其中模态分量按特征值幅度加权最小二乘：

$$\min \sum_{k} w_k^2 \left| Y_k^\text{target}(j\omega_i) - \sum_m \frac{R_{m,k}}{j\omega_i - p_m} - D_k \right|^2 \tag{8}$$

$w_k = 1/| \lambda_k |$ 为特征值 $\lambda_k$ 的倒数权重，保证小特征值模态的拟合精度。

## 形式化表达

### 单端口有理逼近

$$H(s) = \sum_{m=1}^{M} \frac{R_m}{s - p_m} + D + sE \tag{9}$$

### 多端口导纳矩阵

$$\mathbf{Y}(s) = \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D} + s\mathbf{E} \tag{10}$$

### 辅助函数 $\sigma(s)$（阶段 1）

$$\sigma(s) = \frac{a_M s^M + a_{M-1} s^{M-1} + \cdots + a_0}{\prod_{m=1}^{M}(s - \bar{p}_m)} = \sum_{m=1}^{M} \frac{\gamma_m}{s - \bar{p}_m} \tag{11}$$

### 递推卷积实现（时域递归）

$$i_m(t) = e^{p_m \Delta t} i_m(t - \Delta t) + R_m \int_{t-\Delta t}^{t} e^{p_m(t-\tau)} v(\tau) d\tau \tag{12}$$

离散化为：

$$i_m^k = e^{p_m \Delta t} i_m^{k-1} + R_m \frac{e^{p_m \Delta t} - 1}{p_m} v^k \tag{13}$$

## 关键技术挑战

### 1. 初始极点选择

起始极点 $\bar{p}_m$ 的分布直接影响收敛速度和拟合质量。Gustavsen 1999 建议在关注频段内按对数间隔分布复数极点对：

$$\bar{p}_m = -\alpha_m + j\beta_m, \quad \alpha_m = \omega_m / Q, \quad \beta_m = \omega_m \sqrt{1 - \frac{1}{4Q^2}} \tag{14}$$

$Q$ 取值 5~10可覆盖多数电力系统谐振响应。

### 2. 无源性强制

VF 拟合结果不自动满足无源性 $\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega) \succeq 0$。Gustavsen 2002 提出了基于约束优化的无源性修正方法，通过扰动留数矩阵使修正后的模型在所有频点满足正实性条件：

$$\min_{\Delta \mathbf{R}_m} \| \Delta \mathbf{R}_m \|_F^2 \quad \text{s.t.} \quad \mathbf{Y}(j\omega_i) + \mathbf{Y}^H(j\omega_i) \succeq \epsilon \mathbf{I}, \forall i \tag{15}$$

### 3. 病态条件数

当拟合频段跨越多个数量级时（如 1Hz ~ 1MHz），矩阵 $\mathbf{A}$ 的条件数急剧增大。Partitioned Fitting（Cervantes 2018）通过分段拟合策略缓解：在低频段（排除 DC 附近）先拟合，再补充 DC 修正项。

### 4. 多端口小特征值问题

直接拟合高阻抗端接的多端口 FDNE 时，充电电流对应的小特征值会被大特征值（短路电流）主导，导致拟合精度不足。Gustavsen 2009 的 MVF 通过逆特征值加权解决，但计算复杂度显著增加。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 拟合精度（RMS 误差） | $< 10^{-4}$（典型），$10^{-6}$（优化后） | Gustavsen 1999 |
| 极点收敛所需迭代次数 | 3~8 次（典型），< 20 次（复杂响应） | Gustavsen 1999 |
| MVF vs VF 计算时间比 | 5~20×（取决于端口数和采样点） | Gustavsen 2009 |
| 并行 VF 加速比 | ~4×（4核），~8×（8核） | Kida 2024 |
| CVF vs VF 精度对比 | CVF 在非对称频响场景误差降低 60% | Kida 2024 |
| 无源性修正后时域稳定性 | 修正后 100% 满足正实性（$\epsilon = 10^{-6}$） | Gustavsen 2002 |
| 最大可拟合端口数 | 受内存约束，稀疏优化下可达 200+ 端口 | Kida 2024 |

## 适用边界与选择指南

| 场景 | 推荐方法 | 原因 |
|------|----------|------|
| 单端口光滑频响 | 标准 VF | 计算效率高，收敛稳定 |
| 多端口、有高阻抗端接 | 模态 VF (MVF) | 保护小特征值，避免误差放大 |
| 非对称复数频响 | 复数 VF (CVF) | 无需共轭极点约束 |
| 宽频段大端口数 FDNE | 并行 VF / CVF | 利用稀疏结构和多核并行 |
| 含 DC 稳态的线路模型 | VF + DC 修正（Partitioned Fitting） | 避免 DC 附近拟合病态 |
| 实时/HIL 仿真 | VF + 截断降阶 | 降低状态空间维数 |

**失败模式**：
- **采样边界**：采样点应覆盖 DC 或最低关注频率至最高关注频率；谐振峰附近需要更密集采样
- **初始极点不足**：起始极点不足或分布不当会导致局部拟合差、冗余阶数或不稳定极点
- **权重失衡**：幅值很小的通道、小特征值和高阻抗端接需要相对误差控制，不能只看绝对 RMS
- **无源性破坏**：拟合曲线匹配不代表 $\mathbf{Y}(j\omega)$ 正实；非无源模型可能在 EMT 中发散
- **非线性失效**：VF 拟合线性频响；饱和、开关限幅和控制模式切换只能通过分段或多工作点处理

## 相关页面

- [[parameter-identification]]：VF 是频域参数辨识的一种特化形式
- [[prony-analysis]]：Prony 从时域响应拟合指数模态；VF 从频域响应拟合有理函数
- [[passivity-enforcement]]：VF 后处理常需要无源性检测和修正，尤其是多端口导纳
- [[state-space-method]]：极点-留数结果常转换为状态空间参与 EMT 步进
- [[model-order-reduction]]：VF 模型阶数偏高时，可进一步降阶，但需重新验证频域和时域误差
- [[wideband-modeling]]：VF 是宽频模型的常用实现路径，但不是唯一选择
- [[fdne-model]]：VF 是 FDNE 有理逼近的核心算法
- [[frequency-dependent-modeling]]：VF 支撑频率相关建模的全流程

## 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]]（Gustavsen & Semlyen） | 1999 | 提出 VF 两阶段极点重定位算法，奠定理论基础 |
| [[fast-realization-of-the-modal-vector-fitting]]（Gustavsen & Heitz） | 2009 | 提出 MVF 快速实现，逆特征值加权保护小特征值 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin]]（Salarieh & De Silva） | 2021 | 对比 VF/FpF/MPM/LM 四种曲线拟合方法 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran]]（Cervantes et al.） | 2018 | 提出分段拟合+DC 修正，改善低频拟合病态 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17]]（Kida et al.） | 2024 | 并行 VF/CVF 实现，8核加速 8× |
| [[passivity-enforcement-for-transmission-line-models]]（Gustavsen） | 2002 | 提出无源性修正算法，保证时域稳定性 |
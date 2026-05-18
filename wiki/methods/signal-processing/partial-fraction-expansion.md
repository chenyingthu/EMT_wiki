---
title: "部分分式展开 (Partial Fraction Expansion)"
type: method
tags: [partial-fraction, residue, laplace-transform, transfer-function, rational-function]
created: "2026-05-02"
updated: "2026-05-19"
---

# 部分分式展开 (Partial Fraction Expansion)

## 定义与边界

部分分式展开把有理函数表示为极点、留数和直接项的和。对 EMT 而言，它是频域有理模型进入时域递推、状态空间实现和模态解释的桥梁。

设 $F(s) = N(s)/D(s)$ 为复频率域有理函数，部分分式形式为：

$$F(s) = \sum_{i=1}^{n}\frac{k_i}{s-p_i} + d + se$$

其中 $p_i$ 为极点，$k_i$ 为留数，$d$ 和 $e$ 分别为直接项和高频比例项。当 $p_i$ 互异时，留数由下式给出：

$$k_i = \lim_{s\to p_i}(s-p_i)F(s) = \frac{N(p_i)}{D'(p_i)}$$

本页讨论极点-留数表示的实现边界。它不是频域曲线拟合算法本身，也不自动保证拟合模型无源、稳定或适合实时仿真。

## EMT 中的角色

频率相关线路、变压器、接地网络和外部网络等值常以采样频率响应给出。若将端口响应拟合为有理函数，部分分式形式可把卷积核写为指数项，使 EMT 时域实现避免每步全历史卷积。

典型用途包括：

- 将导纳、阻抗或传播函数写为极点-留数模型
- 从传递函数提取时域指数响应和振荡模式
- 将有理函数转换为状态空间模型或递归卷积
- 在 [[modal-analysis]] 中解释输入输出通道对某个模态的留数

## 核心形式

### 互异单极点

若分母 $D(s)$ 有互异单极点 $p_i$，可写为：

$$F(s) = d + se + \sum_{i=1}^{n}\frac{k_i}{s-p_i}$$

留数计算式：

$$k_i = \frac{N(p_i)}{D'(p_i)}$$

### 重极点处理

若 $p$ 是 $m$ 阶重极点，部分分式形式为：

$$F(s) = \sum_{j=1}^{m}\frac{k_j}{(s-p)^j} + R(s)$$

其中留数需通过导数公式或线性方程组求解：

$$k_j = \frac{1}{(m-j)!}\lim_{s\to p}\frac{d^{m-j}}{ds^{m-j}}\left[(s-p)^m F(s)\right]$$

工程实现中应谨慎处理近重根——数值上"相近极点"和"精确重极点"的行为不同。

### 多端口公共极点

多端口导纳/阻抗矩阵的所有元素可共享同一组极点，留数为矩阵：

$$\mathbf{Y}(s) \approx \sum_{n=1}^{N_p}\frac{\mathbf{R}_n}{s-p_n} + \mathbf{D} + s\mathbf{E}$$

其中 $\mathbf{R}_n\in\mathbb{C}^{N\times N}$ 为留数矩阵，$\mathbf{D},\mathbf{E}\in\mathbb{R}^{N\times N}$ 为常数矩阵。多端口形式要求留数矩阵满足对称性和互易性约束。

## 时域解释

### 拉普拉斯逆变换对应关系

基本对应关系为：

$$\mathcal{L}^{-1}\left\{\frac{k}{s-p}\right\} = ke^{pt}$$

若 $p = \sigma + j\omega$ 且实值系统存在共轭项，则一对复极点 $p, p^*$ 在时域形成衰减振荡（$\sigma<0$）或增长振荡（$\sigma>0$）。但端口模型是否可接入网络还需检查无源性、因果性和数值离散化。

### EMT 递归卷积实现

对 EMT 递归卷积，连续指数核在步长 $\Delta t$ 下转化为递推系数：

$$z_{i,k} = a_i z_{i,k-1} + b_i u_k, \quad a_i \approx e^{p_i\Delta t}$$

其中 $b_i$ 取决于积分规则和输入保持假设。[[companion-model]] 章节给出了 companion 形式离散化的详细推导。

### 状态空间实现

极点-留数参数可直接转换为状态空间形式：

$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t),\quad \mathbf{y}(t) = \mathbf{C}^T\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t) + \mathbf{E}\dot{\mathbf{u}}(t)$$

其中 $\mathbf{A} = \mathrm{diag}(p_1, p_2, \ldots, p_{N_p})$ 为极点对角阵，$\mathbf{B}$ 为选择矩阵。该形式便于与 EMT 网络方程联解。

## 工作流

1. **获得有理函数**：来自解析传递函数、 [[vector-fitting]] 拟合、频域扫描或网络等值
2. **分离直接项**：若分子阶次不低于分母阶次，先做多项式除法
3. **求极点**：计算 $D(s)$ 的根或读取拟合算法输出的极点
4. **求留数**：对单极点用留数公式，对多端口或近重极点用线性最小二乘（参见 [[least-squares-method]]）
5. **组合共轭项**：实值时域模型应保持共轭对一致
6. **生成时域实现**：转换为状态空间、递归卷积或 companion-like 历史项
7. **验证**：检查频域拟合误差、时域波形、稳定极点、无源性和步长敏感性

## 变体与实现形式

| 变体 | 机制 | 适用场景 | 风险 |
|---|---|---|---|
| 标量部分分式 | 单输入单输出有理函数 | 传递函数、单端口阻抗 | 高阶多项式根可能病态 |
| 多端口公共极点 | 多个矩阵元素共享极点，留数为矩阵 | FDNE、宽频线路和变压器 | 留数矩阵需满足对称性和无源性 |
| 状态空间实现 | 把极点-留数转换为一阶状态方程 | EMT 时域求解 | 状态缩放影响条件数 |
| 递归卷积实现 | 把指数核转为历史递推 | 频变线路和网络等值 | 步长和积分规则影响误差 |
| 模态展开 | 按特征模式或极点解释响应 | 振荡模式识别 | 留数小不代表状态不重要 |

## 关键技术挑战

### 频率畸变（Frequency Warping）

使用梯形规则离散化时，模拟频率 $\omega_a$ 与离散频率 $\omega$ 之间存在双线性映射：

$$\omega_a = \frac{2}{h}\tan\frac{\omega h}{2}$$

该映射导致频变元件（电感、电容）在离散域呈现频率依赖的等效值：

$$L_{\mathrm{DT}}(\omega) = \Psi(\omega)L, \quad C_{\mathrm{DT}}(\omega) = \Psi(\omega)C$$

其中 $\Psi(\omega) = \frac{2}{h}\cot\frac{\omega h}{2}$。Kida 2026 证明该误差在 10 倍最大感兴趣频率以下仍可能显著。预畸变（pre-warping）策略可在拟合阶段补偿此效应：

$$L' = \frac{\omega' h/2}{\tan(\omega' h/2)}L_{\mathrm{DT}}, \quad C' = \frac{\omega' h/2}{\tan(\omega' h/2)}C_{\mathrm{DT}}$$

### 留数病态与条件数

相近极点会导致留数数量级急剧增大并互相抵消，时域实现对舍入误差极其敏感。Gustavsen 2004 指出，使用复数起始极点（实部为虚部的 $1/100$）可有效消除宽频带拟合中的病态条件问题，使最小二乘求解获得准确解。

### 无源性保持

拟合误差在频域可接受，不代表接入网络后无源或稳定。多端口模型的每个矩阵元素单独拟合可能破坏对称性和互易性。Kida 2024 提出用 Hamiltonian 矩阵检测无源性破坏：

$$\mathbf{H} = \begin{bmatrix} \mathbf{A}-\mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & \mathbf{B}(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \\ -\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{C} & -\mathbf{A}^H+\mathbf{C}^H(\mathbf{D}+\mathbf{D}^H)^{-1}\mathbf{B}^H \end{bmatrix}$$

若 $\mathbf{H}$ 存在纯虚数特征值，则在对应频率处发生无源性破坏。

### 不稳定极点的处理

不稳定极点若来自物理负阻尼、拟合噪声或数值伪影，需要分别解释。简单处理方法：将正实部取负得到稳定极点 $p_n^{\mathrm{stable}} = -\mathrm{Re}(p_n) + j\mathrm{Im}(p_n)$，但这可能改变物理含义。

## 量化性能边界

| 指标 | 数值 | 来源 |
|---|---|---|
| VF 拟合 RMS 误差（18 阶系统，20 极点） | $3.8\times 10^{-12}$ | Gustavsen 2004 |
| VF 拟合 RMS 误差（18 阶系统，40 极点） | $1.6\times 10^{-12}$ | Gustavsen 2004 |
| 极点估计相对误差 | $\approx 10^{-7}$ | Gustavsen 2004 |
| 留数估计相对误差 | $\approx 10^{-7}$ | Gustavsen 2004 |
| 算法收敛迭代次数 | 通常 1–3 次 | Gustavsen 2004 |
| PRFWC 精度提升幅度 | 约 2 个数量级 | Kida 2026 |
| QR 分解占 VF 计算时间比例 | $>95\%$ | Kida 2024 |
| 步长上界建议 | $h \leq 1/(10f_{\max})$ | Marti & Lin |

## 适用边界与失败模式

- **相近极点**：留数很大且互相抵消，时域实现对舍入误差敏感
- **拟合误差 ≠ 无源性**：频域可接受的拟合，接入网络后可能不稳定
- **不稳定极点的物理判断**：负阻尼、拟合噪声、数值伪影需要分别解释，不能简单删除
- **多端口对称性破坏**：矩阵元素单独拟合可能破坏互易性
- **步长敏感性**：当 $h$ 接近或超过 $1/(10f_{\max})$ 时，频率畸变误差显著（Kida 2026）

## 相关方法

- [[vector-fitting]]：最常用的极点-留数识别方法，本身也是一种部分分式展开的实现框架
- [[least-squares-method]]：多端口留数识别和重极点留数求解的数学工具
- [[passivity-enforcement]]：部分分式模型接入网络前的无源性检查与修正
- [[frequency-dependent-line-model]]：使用有理近似实现频变线路的工程实例
- [[companion-model]]：EMT 中将极点-留数模型转化为离散时域接口的历史项形式
- [[numerical-laplace-transform]]：频域与时域转换的另一类数值路线，与部分分式展开互补

## 来源论文

- **Gustavsen & Semlyen 2004** — Rational Approximation of Frequency Domain Responses by Vector Fitting (IEEE Trans Power Delivery). 首次系统提出两阶段极点迁移矢量拟合，允许复数起始极点处理多谐振峰响应，18 阶测试函数 RMS 误差达机器精度（$10^{-12}$ 量级）
- **Kida et al. 2024** — Enhancing Computation Performance of Rational Approximation for Frequency-Dependent Network Equivalents with Parallelism and Complex Vector Fitting (Elec Power Syst Res). 将复数矢量拟合（CVF）引入 FDNE 导纳矩阵综合，用 C 语言 + Intel MKL 并行实现，QR 分解步骤占总计算时间 $>95\%$
- **Kida et al. 2026** — High-Accuracy EMT Simulations Through Pole-Residue Compensation (Elec Power Syst Res). 提出极点-留数频率畸变补偿（PRFWC）算法，补偿后精度提升约两个数量级，同时阐明了预畸变电感/电容的解析修正公式
---
title: "特征线法 (Characteristic Method)"
type: method
tags: [characteristic, method, bergeron, transmission-line, wave, distributed-parameter, moc]
created: "2026-05-02"
updated: "2026-05-18"
---

# 特征线法 (Characteristic Method)

## 定义与边界

特征线法（Method of Characteristics, MoC）是一类将双曲型偏微分方程沿特征方向转化为常微分方程的数学方法。在 EMT 线路建模中，它通过构造电压、电流波变量的特征线，将分布参数线路的偏微分方程化为沿特征线传播的常微分方程，从而得到行波变量、传播延时和端口历史项。

本页讨论的是特征线法本身——从电报方程得到沿线传播关系的数学框架。它不同于 [[bergeron-line-model]] 和 [[bergeron-model]]（关注 EMT 端口等效电路的具体实现），也不同于 [[universal-line-model]]（处理相域频变矩阵拟合与时域递归卷积）。本页聚焦于特征线法的核心数学机制：如何从相域或模域线路方程推导出传播关系，以及该方法在频变条件下向 Bergeron 类、ULM 类模型的演化路径。

## EMT 中的角色

特征线法在 EMT 仿真中承担三重角色：

1. **数学框架**：将分布参数线路的电压、电流偏微分方程转化为沿特征线传播的行波方程
2. **数值离散入口**：通过特征线关系把 PDE 化为 ODE，使时域步进求解成为可能
3. **等效电路构造基础**：Bergeron 类端口历史源、延时队列、递归卷积项均源于特征线关系

其输出不是单一软件模块，而是一组可离散化的端口关系。常参数模型可得到简单延时历史源；频变模型通常需要将特征导纳、传播函数或损耗项进一步拟合成时域可递推形式。

## 核心数学机制

### 1. 无损单相线路的特征线方程

无损单相线路的电报方程为：

$$-\frac{\partial v(x,t)}{\partial x}=L\frac{\partial i(x,t)}{\partial t},\quad -\frac{\partial i(x,t)}{\partial x}=C\frac{\partial v(x,t)}{\partial t}$$

定义特征阻抗 $Z_c=\sqrt{L/C}$ 和光速 $u=1/\sqrt{LC}$，可构造**特征变量**（Riemann 不变量）：

$$w^+(x,t)=v(x,t)+Z_c i(x,t),\quad w^-(x,t)=v(x,t)-Z_c i(x,t)$$

它们沿两组特征线传播：

$$\frac{\partial w^+}{\partial t}+u\frac{\partial w^+}{\partial x}=0,\quad \frac{\partial w^-}{\partial t}-u\frac{\partial w^-}{\partial x}=0$$

$w^+$ 与 $w^-$ 分别表示向 $+x$ 和 $-x$ 方向传播的行波变量。在长度 $\ell$ 的线路两端评价，有：

$$v(0,t)-\frac{Z_c}{u}i(0,t) = w^+(0,t),\quad v(\ell,t)+\frac{Z_c}{u}i(\ell,t) = w^-(0,t-\tau)$$

其中 $\tau=\ell/u$ 为传播时延。消去中间点变量，得到 Bergeron 类端口历史源：

$$i_k = \frac{1}{Z_c}\left[w^+\left(0,t_k\right)-w^-\left(\ell,t_k-\tau\right)\right]$$

### 2. 频变线路的扩展特征线方程

有损或频变线路的频域方程为：

$$-\frac{d\mathbf{V}(x,\omega)}{dx}=\mathbf{Z}(\omega)\mathbf{I},\quad -\frac{d\mathbf{I}(x,\omega)}{dx}=\mathbf{Y}(\omega)\mathbf{V}$$

其中 $\mathbf{Z}(\omega)=\mathbf{R}(\omega)+j\omega\mathbf{L}(\omega)$，$\mathbf{Y}(\omega)=\mathbf{G}(\omega)+j\omega\mathbf{C}$。

此时"沿特征线保持常数"的简单结论不再严格成立。Kauffmann 等 (2018) 的分析表明，需要通过**变量替换和线性化近似**建立端点关系：

**步骤 1：串联阻抗有理函数拟合**

对串联阻抗矩阵 $\mathbf{Z}(s)$ 采用部分分式展开（Vector Fitting）：

$$\mathbf{Z}(s) \sim \mathbf{R}_{dc} + s\mathbf{D} + \sum_{i=1}^{N}\frac{\mathbf{K}_i}{s-p_i}$$

其中 $\mathbf{R}_{dc}$ 为直流电阻矩阵，$\mathbf{D}$ 为高频电感常数矩阵，$\mathbf{K}_i$ 和 $p_i$ 为极点—留数对。

**步骤 2：拉普拉斯反变换得到时域卷积**

经拉普拉斯反变换后，频变部分变成由指数核表示的卷积：

$$\mathbf{h}(t)=\sum_{i=1}^{N}e^{p_i t}\mathbf{K}_i$$

时域方程中的卷积项为：

$$\mathbf{\psi}(x,t)=\int_0^t \mathbf{h}(t-\tau)\mathbf{i}(x,\tau)d\tau$$

**步骤 3：模态变换与特征线构造**

定义变换矩阵 $\mathbf{T}_v$ 和 $\mathbf{T}_i$ 使 $\mathbf{Z}\mathbf{Y}$ 近似对角化：

$$\mathbf{V}_m=\mathbf{T}_v^{-1}\mathbf{V},\quad \mathbf{I}_m=\mathbf{T}_i^{-1}\mathbf{I}$$

各模态的传播速度为：

$$\mathbf{\Lambda}=\mathrm{diag}(\lambda_1,\ldots,\lambda_n)=\mathrm{diag}\left(\frac{1}{\sqrt{D_{kk}C_{kk}}}\right)$$

沿特征线，将 PDE 化为 ODE 后，用梯形法在时间上离散，得到端点代数关系。

### 3. 无空间离散 MoC 的可行性分析

Kauffmann 等 (2018) 深入分析了"取消空间离散化"的 MoC 变体。对于均匀线路，可利用模态传播延迟建立端点直接关系：

$$w^+(0,t)=w^-(\ell,t-\tau),\quad w^-(\ell,t)=w^+(0,t-\tau)$$

理论上每端只需**一个卷积**（vs 行波模型的两个卷积），且串联阻抗元素比传播函数 $H$ 和特征导纳 $Y_c$ 更平滑，拟合更易处理。但关键问题是：为建立端点关系而对 ODE 线性化会引入**近似误差**，且积分步长受整段模态延迟约束可能过大，导致精度损失和数值不稳定。结论是：**均匀线路仍需分段**才能恢复精度和稳定性。

## 多导体扩展

多导体线路的频域方程可写为：

$$-\frac{d\mathbf{V}}{dx}=\mathbf{Z}(\omega)\mathbf{I},\quad -\frac{d\mathbf{I}}{dx}=\mathbf{Y}(\omega)\mathbf{V}$$

若存在变换矩阵 $\mathbf{T}$ 使 $\mathbf{Z}\mathbf{Y}$ 近似对角化，则每个模态可单独应用特征线关系。对平衡或完全换位三相线路，固定序分量或 Clarke/Karrenbauer 类变换可能足够；对非换位、平行线路和电缆，变换矩阵可能随频率变化，需参考 [[modal-transformation]] 与 [[modal-domain-decoupling]] 的边界。

Torres Caballero 等 (2019) 采用**固定频率实模态变换矩阵**的工程近似：取某一参考频率 $\omega_0$ 处的 $\mathbf{T}_v$ 和 $\mathbf{T}_i$ 实部作为时域变换矩阵，避免频率相关模变换在时域中的复杂卷积运算。

## EMT 建模方法体系

### 常参数 Bergeron 模型

对常参数无损或低频近似线路，特征线法退化为经典的 Bergeron 等效电路：

$$i_k = \frac{2}{Z_c}v_k + I_{hist,k-1},\quad I_{hist,k-1}=\frac{2}{Z_c}v_{k-\tau}+i_{k-\tau}$$

其中 $Z_c=\sqrt{L/C}$，$\tau=\ell\sqrt{LC}$。该方法计算量小，与时变元件耦合方便，是 EMTP 的核心算法之一。

### 频变 Bergeron 模型（纵向参数拟合）

Torres Caballero 等 (2014) 将频率相关纵向阻抗 $Z(\omega)$ 拟合为有理函数后，嵌入 Bergeron 等效电路：

1. 对 $Z(\omega)$ 做 Vector Fitting 得到 $R_{fit}(\omega)$ 和 $L_{fit}(\omega)$
2. 将拟合结果映射为频率无关的 RLC 等效电路拓扑（梯形网络）
3. 将等效电路嵌入 Bergeron 特征线传播关系

优势是保留 Bergeron 方法与时变元件耦合方便的特点，同时引入宽频频率效应。

### 扩展 Bergeron 模型（混合坐标）

徐政 (1996) 针对多相耦合长线提出：把电阻损耗从分布参数波动方程中剥离，等效为集中电阻部分；剩余无损耦合线在模坐标下用 Bergeron 思想处理：

- **无损传播部分**：模坐标处理，通过 Bergeron 特征线关系处理行波传播
- **损耗部分**：相坐标处理，允许电阻矩阵 $\mathbf{R}$ 保持非对角形式

这一方法避免了"要求 $\mathbf{R}$ 也能被同一相模变换对角化"的传统限制，更适合含地线的非对称线路。

### 加速频变特征线法（稀疏化实现）

Torres Caballero 等 (2019) 提出的加速实现方法：

1. **电路拓扑约简**：利用级联电路结构减少状态方程数量（从 $bm$ 降至约 $(b+1)m$ 量级）
2. **稀疏矩阵分组**：将状态空间矩阵组装为全局稀疏形式，用稀疏求解器加速 ODE 步进
3. **历史源索引化**：预定义内存索引，将历史源更新从"逐分散地址访问"转为"固定偏移写入"
4. **传播时间校正**：对 $\tau$ 不是步长整数倍的情况进行校正，减少时间离散截断误差

### 多导体模态 FD-MoC

多导体频变特征线法的一般流程：

1. **建立相域参数**：$\mathbf{Z}(\omega)$、$\mathbf{Y}(\omega)$ 由几何参数和大地返回模型计算
2. **模态解耦**：用固定频率模变换矩阵将相域方程化为模态域独立方程
3. **频变纵向参数拟合**：每个模态的 $Z_m(\omega)$ 用 Vector Fitting 拟合为极点—留数形式
4. **模态 Bergeron 等效电路**：对每个模态建立含频变阻抗的 Bergeron 等效电路
5. **端口关系组装**：将各模态结果变换回相域，得到多导体端口电压、电流

## 形式化表达

**无损单相线路特征变量**：

$$w^+ = v + Z_c i,\quad w^- = v - Z_c i, \quad Z_c = \sqrt{\frac{L}{C}}$$

**传播时延**：

$$\tau = \ell\sqrt{LC} = \frac{\ell}{u},\quad u = \frac{1}{\sqrt{LC}}$$

**频变串联阻抗有理函数拟合**：

$$\mathbf{Z}(s) \sim \mathbf{R}_{dc} + s\mathbf{D} + \sum_{i=1}^{N}\frac{\mathbf{K}_i}{s-p_i}$$

**时域卷积核**：

$$\mathbf{h}(t) = \sum_{i=1}^{N}e^{p_i t}\mathbf{K}_i$$

**多导体模态传播速度**：

$$\lambda_m = \frac{1}{\sqrt{D_{mm}C_{mm}}}$$

**频变 Bergeron 端口历史源**：

$$i_k = \frac{1}{Z_c}\left[v_k - v_{k-\tau} + Z_c i_{k-\tau} + \psi_k\right]$$

其中 $\psi_k$ 为卷积历史项。

**加速实现的离散状态更新**：

$$\mathbf{x}_{n+1} = \mathbf{A}_H\mathbf{x}_n + \mathbf{B}_H(\mathbf{u}_n + \mathbf{u}_{n+1})$$

## 量化性能边界

| 建模方法 | 适用场景 | 计算效率 | 精度 | 代表数据 |
|---------|---------|---------|------|---------|
| 常参数 Bergeron | 窄频/低频近似 | 最高（无卷积） | 低 | 时延整数倍步长时无插值误差 |
| 频变 Bergeron（纵向拟合） | 架空线宽频暂态 | 中等（每端1个卷积） | 高 | 拟合频带内精度取决于阶数 |
| 扩展 Bergeron（混合坐标） | 含地线非对称多相线路 | 中等 | 高 | 无需 R 矩阵对角化假设 |
| 加速 FD-MoC（稀疏化） | 大规模多导体线路 | 高（稀疏求解+索引化） | 高 | 状态方程数降低约 $bm\to(b+1)m$ |
| 无空间离散 MoC | 理论分析 | 最高（无空间离散） | 低 | 精度受限，需线路分段 |

**Kauffmann 等 (2018) 关键发现**：
- 无空间离散 MoC 的误差源：线性化近似误差 + 受模态延迟约束的大积分步长
- 线路分段可恢复精度，但会削弱原本的计算效率优势
- 串联阻抗元素比传播函数 $H$ 和特征导纳 $Y_c$ 更平滑，拟合更稳定

**Torres Caballero 等 (2019) 算例**：
- 2 km 三相架空线路（高斯脉冲激励）：10 段和 25 段模型波形接近数值拉普拉斯变换 (NLT) 基准，耗时低于级联频变 $\pi$ 型电路
- 100 km 三相线路（接非线性负载）：算法层面状态方程数由传统级联形式降低约 $bm$ 量级

## 关键技术挑战

1. **模态变换频率依赖**：$\mathbf{T}_v$ 和 $\mathbf{T}_i$ 随频率变化，严格时域实现需要频率相关模变换的卷积处理；固定频率近似可能在电缆或强不对称条件下失效

2. **频变参数的有理函数拟合**：Vector Fitting 的阶数选择影响精度和稳定性；极点若位于右半平面会导致时域不稳定，需进行[[passivity-enforcement]]

3. **传播时间非整数倍步长**：$\tau/\Delta t$ 不为整数时需插值处理；插值方式影响高频相位精度

4. **无空间离散 MoC 的数值稳定性**：线性化误差和大积分步长的组合可能导致数值振荡或发散；线路分段虽可改善但降低效率优势

5. **多导体解耦的近似误差**：对非换位线路，固定频率实模态变换矩阵可能引入不可忽略的解耦误差；需参考 [[modal-domain-decoupling]] 的误差估计方法

## 适用边界与选择指南

**选择常参数 Bergeron** 当：仿真频带窄（如工频暂态）、线路参数近似常数、计算资源有限

**选择频变 Bergeron（纵向拟合）** 当：需要宽频精度、时域与其他非线性元件耦合、拟合阶数可接受

**选择扩展 Bergeron（混合坐标）** 当：线路含地线或非对称结构、R 矩阵不满足对角化条件、多相耦合显著

**选择加速 FD-MoC** 当：大规模多导体线路、计算效率关键、需要保留频变精度

**避免无空间离散 MoC** 单独使用：其精度受限问题在 Kauffmann 等 (2018) 中已系统论证；如需极高效率建议采用 [[universal-line-model]]

## 相关页面

- [[bergeron-model]]：从特征线关系落到端口 Norton 等效的具体实现
- [[bergeron-line-model]]：常参数线路模型的门户页面
- [[distributed-parameter-line]]：线路偏微分方程的背景与电报方程推导
- [[modal-transformation]] 和 [[modal-domain-decoupling]]：说明多相线路解耦的坐标变换条件
- [[frequency-dependent-line-model]] 和 [[universal-line-model]]：处理频率相关传播和相域实现的行波类模型
- [[vector-fitting]]：频变参数有理函数拟合的核心技术
- [[passivity-enforcement]]：保证拟合模型无源性和因果性的后处理步骤
- [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-]]：加速 FD-MoC 的稀疏化实现方法

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| Kauffmann, Kocar 等 | 2018 | 系统分析无空间离散 MoC 的可行性与局限性，证明线性化误差和大积分步长是主要误差源 |
| Torres Caballero, Kurokawa, Kordi | 2019 | 提出加速 FD-MoC 的稀疏化实现，状态方程数约降低 $bm\to(b+1)m$ |
| Torres Caballero 等 | 2014 | 将 Vector Fitting 频变纵向参数嵌入 Bergeron 等效电路，扩展宽频适用范围 |
| 徐政 | 1996 | 提出扩展 Bergeron 模型（混合坐标），解决含地线非对称多相线路的建模问题 |
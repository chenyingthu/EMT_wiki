---
title: "通用线路模型 (Universal Line Model, ULM)"
type: method
tags: [universal-line, frequency-dependent, marti, transmission-line, vector-fitting]
created: "2026-05-02"
updated: "2026-05-19"
---

# 通用线路模型 (Universal Line Model, ULM)

## 定义与边界

通用线路模型（Universal Line Model, ULM）是 EMT 中直接在相域处理多导体线路频率相关响应的一类方法。ULM 由 Marti 于 1988 年提出（Marti, 1988），其核心贡献是避免固定模态变换，直接在相域中拟合特征导纳矩阵 $\mathbf{Y}_c(\omega)$ 和传播矩阵 $\mathbf{H}(\omega)$，使其适用于非换位线路、地下电缆和宽频暂态仿真。

ULM 的可信度取决于：线路参数精度、频率采样范围、拟合质量、延时提取精度、无源性约束和时域接口实现。ULM 不是万能模型——其边界在于：对强频率相关变换矩阵的线路（如不对称架空线），常数模态变换的 JMarti 模型可能失效，而 ULM 是更高保真度的替代方案。

## EMT 中的角色

在 EMT 仿真中，线路模型是将系统电气特性转化为节点导纳方程的关键环节。ULM 面向以下典型场景：

- **非换位或强不对称线路**：常数模态变换无法准确描述频率相关耦合特性时，需要相域处理。
- **地下电缆与架空-电缆混合段**：土壤返回路径和护套阻抗的频率相关性在宽频暂态中影响显著。
- **宽频阻抗建模**：需要将线路频域响应（从 0.1 Hz 到数 MHz）转换为节点导纳方程中的固定导纳和历史电流源。
- **基准对比研究**：为不同 EMT 工具中的线路模型提供方法级精度的对比基准。

## 核心机制

### 频域线路方程

多导体传输线路的频域方程为：

$$-\frac{d\mathbf{V}}{dx}=\mathbf{Z}(\omega)\mathbf{I},\quad -\frac{d\mathbf{I}}{dx}=\mathbf{Y}(\omega)\mathbf{V}$$

其中 $\mathbf{Z}(\omega)$ 和 $\mathbf{Y}(\omega)$ 分别是单位长度串联阻抗矩阵和并联导纳矩阵。

由此导出两个核心频率相关矩阵——特征导纳和传播函数：

$$\mathbf{Y}_c(\omega)=\mathbf{Y}(\omega)^{-1}\sqrt{\mathbf{Y}(\omega)\mathbf{Z}(\omega)}$$

$$\mathbf{H}(\omega)=e^{-\ell\sqrt{\mathbf{Z}(\omega)\mathbf{Y}(\omega)}}$$

$\mathbf{Y}_c$ 决定端口特征导纳，$\mathbf{H}$ 描述跨端传播、衰减和相间耦合。

### 时域等效方程

在时域中，两端电压电流关系为（Zanon et al., 2021）：

$$\mathbf{i}_k(t)-\mathbf{y}_c(t)*\mathbf{v}_k(t)=-\mathbf{b}_k(t)$$

$$\mathbf{i}_m(t)-\mathbf{y}_c(t)*\mathbf{v}_m(t)=-\mathbf{b}_m(t)$$

其中 $\mathbf{b}_k$ 和 $\mathbf{b}_m$ 是卷积历史项：

$$\mathbf{b}_k(t)=\mathbf{h}(t)*[\mathbf{i}_m(t)+\mathbf{y}_c(t)*\mathbf{v}_m(t)]$$

$$\mathbf{b}_m(t)=\mathbf{h}(t)*[\mathbf{i}_k(t)+\mathbf{y}_c(t)*\mathbf{v}_k(t)]$$

符号 $*$ 表示卷积运算。

### Norton 等效电路

将 $\mathbf{y}_c(t)$ 和 $\mathbf{h}(t)$ 拟合成指数和：

$$\tilde{\mathbf{Y}}_C(s)=\mathbf{K}_0+\sum_{r=1}^{N_{pY}}\frac{\mathbf{R}_r}{s-p_r}$$

$$\tilde{\mathbf{H}}(s)\approx\sum_{j=1}^{N_{mod}}\mathbf{D}_j e^{-\tau_j s}\left(\sum_{i=1}^{N_{pH}}\frac{\mathbf{C}_{ij}}{s-a_i}\right)$$

每个极点-留数项可离散为递归卷积历史变量，形成 Norton 等效：

$$\mathbf{i}(t)=\mathbf{G}\mathbf{v}(t)+\mathbf{i}_{hist}(t)$$

其中 $\mathbf{G}=\mathbf{K}_0+\sum q_n$（电导矩阵），$\mathbf{i}_{hist}$ 是由历史卷积项合成的历史电流源。

### 时域递归实现

时域步进中的历史项递推公式为（Zanon et al., 2021）：

$$p_n=\frac{2+a_n\Delta t}{2-a_n\Delta t},\quad q_n=r_n=\frac{k_n\Delta t}{2}-a_n\Delta t$$

$$\mathbf{j}_{kn}(t)=p_n\cdot\mathbf{j}_{kn}(t-\Delta t)+q_n\mathbf{v}_k(t)+r_n\mathbf{v}_k(t-\Delta t)$$

$$\mathbf{i}_{k,hist}(t)=-\mathbf{j}_{kh}(t-\Delta t)+\mathbf{b}_k(t)$$

Zanon 2021 在 ATP 中的实现采用两步流程：第一步在 MATLAB 中进行参数计算和有理拟合，第二步将拟合结果（电导矩阵元、极点、留数、时间延时）写入文本文件作为接口。

## 变体与相邻模型

| 方法 | 核心处理 | 适合用途 | 边界 |
|------|----------|----------|------|
| 相域 ULM | 直接拟合 $\mathbf{Y}_c$ 和 $\mathbf{H}$，无模态变换 | 非对称线路、地下电缆、宽频暂态 | 矩阵拟合实现复杂，计算量大 |
| JMarti 类模型 | 使用近似常数模态变换矩阵 + 频变传播函数 | 常见架空线暂态 | 频率相关特征向量强变化时需复核 |
| Noda 相域模型 | 分频区拟合（Frequency-Partitioning Fitting, FpF）替代 VF | 避免固定模态假设，提高拟合效率 | 对时间步和拟合设置敏感性需验证 |
| FLE 频变实现 | 分解节点导纳为开路/短路贡献块 | 短线路和导纳拟合问题 | 依赖分解质量、无源性处理 |

## 关键技术挑战

### 拟合方法与极点稳定性

有理拟合是 ULM 的核心环节。主要方法包括：
- **矢量拟合（Vector Fitting, VF）**：Gustavsen & Semlyen (1999) 提出，是 EMT 中的标准工具。优点是鲁棒性好，缺点是对延时处理不直接。
- **分频区拟合（Frequency-Partitioning Fitting, FpF）**：Noda (2015) 提出，将频谱分段后分别拟合再合并极点，减少极点数量（FpF: 33 极点 vs VF: 59 极点 for Kaga-Reinan 500 kV 双回线，同等精度）。
- **延时估计**：Loaiza-Elejalde et al. (2025) 提出基于全通滤波器的延时估计方法，保证因果性和最小相位特性，避免 Bode 积分法因最小均方误差延时导致的超光速违反。

### 无源性约束

有理模型若非无源，连接到其他网络元件后可能产生非物理振荡。Noda (2015) 验证：通过对 $\mathbf{Y}_c$ 实施奇异值分解（SVD）滤波，可保证所有特征导纳矩阵元的特征值在足够宽的频带内为正实部，从而满足无源性。实验表明：不加滤波时，10 μs 大步长会导致数值发散；加入滤波后可稳定。

### 延时项与延时不匹配

传播函数 $\mathbf{H}$ 中的延时项 $e^{-\tau_j s}$ 是区分 ULM 与普通有理逼近的关键。当估计的延时与实际不符时，会产生因果性违反。Loaiza-Elejalde (2025) 的 All-Pass Filter (APF) 方法通过迭代调整保证因果性。

### 数值稳定性与步长约束

时域递归卷积的数值稳定性要求：时间步 $\Delta t$ 需小于最小模态延时（Kaga-Reinan 线路：14.2 μs）。Noda (2015) 指出：即使加了滤波，大于传播延时差异的步长仍会导致数值放大。

## 量化性能边界

### Noda 2015 — 500 kV 双回线 Kaga-Reinan 测试结果

| 指标 | 数值 | 说明 |
|------|------|------|
| 时间步 | 0.5 μs | 仿真步长 |
| 最大拟合频率 | $10^8$ Hz | 拟合上限 |
| FpF 极点数量 | 33–51 poles | 可调参数 $\varepsilon$ 控制 |
| VF 极点数量 | 59 poles | 相似精度时 VF 需更多极点 |
| 最大拟合偏差 | $<10^{-3}$ | FpF 加权算法后 |
| 步长 2 μs 验证 | 通过 | 小于模态延时 14.2 μs |
| 步长 10 μs | 数值放大 | 需进一步滤波稳定 |

### Loaiza-Elejalde 2025 — 延时估计对比

| 方法 | 因果性保证 | 迭代次数 | 适用性 |
|------|-----------|----------|--------|
| Bode 积分法 | 否 | 1次 | 可能违反因果性 |
| GS 方法 | 部分 | 多 | 精度可但迭代多 |
| APF 方法（本文） | 是 | 少 | 推荐使用 |

### Colqui 2022 — FLE vs JMarti

| 指标 | FLE | JMarti |
|------|-----|-------|
| 步长容忍度 | $> \tau$（传播延时） | $<\tau$ |
| 仿真速度 | 快（大步长） | 较慢 |
| 适用范围 | 短线路/复杂地形 | 一般架空线 |

## 形式化表达

### 核心方程汇总

**频域线路关系**（Zanon et al., 2021, Eq. 1-4）：

$$\mathbf{I}_k-\mathbf{Y}_c\mathbf{V}_k=-\mathbf{H}(\mathbf{I}_m+\mathbf{Y}_c\mathbf{V}_m)$$

$$\mathbf{I}_m-\mathbf{Y}_c\mathbf{V}_m=-\mathbf{H}(\mathbf{I}_k+\mathbf{Y}_c\mathbf{V}_k)$$

$$\mathbf{Y}_c=\mathbf{Y}^{-1}\sqrt{\mathbf{Y}\mathbf{Z}},\quad \mathbf{H}=e^{-\ell\sqrt{\mathbf{Z}\mathbf{Y}}}$$

**时域卷积形式**（Zanon et al., 2021, Eq. 7-10）：

$$\mathbf{i}_k(t)-\mathbf{y}_c(t)*\mathbf{v}_k(t)=-\mathbf{b}_k(t)$$

$$\mathbf{b}_k(t)=\mathbf{h}(t)*[\mathbf{i}_m(t)+\mathbf{y}_c(t)*\mathbf{v}_m(t)]$$

**Norton 等效参数**（Zanon et al., 2021, Eq. 16-21）：

$$\mathbf{G}=\mathbf{K}_0+\sum_{n=1}^{N_{pY}}q_n$$

$$p_n=\frac{2+a_n\Delta t}{2-a_n\Delta t},\quad q_n=r_n=\frac{k_n\Delta t}{2}-a_n\Delta t$$

### FpF 极点拟合（模态分解形式，Noda 2015）

$$\mathbf{H}\approx\sum_{j=1}^{N_{mod}}\mathbf{D}_j e^{-\lambda_j\ell}\left(\sum_{i=1}^{N_p}\frac{\mathbf{C}_{ij}}{s-a_i}\right)$$

其中 $\lambda_j$ 是 $\mathbf{ZY}$ 的特征值（模态传播常数），$a_i$ 是分频区拟合得到的极点，$\mathbf{C}_{ij}$ 是留数矩阵。

## 适用边界与选择指南

**选择 ULM 的条件**：
- 线路不对称性强（无法用常数模态变换近似）
- 宽频暂态仿真（从工频到数 MHz）
- 需要最高精度作为基准对比

**选择 JMarti 的条件**：
- 线路较对称（常数模态近似可接受）
- 步长可取较小值
- 需要较高计算效率

**选择 FLE 的条件**：
- 短线路或需要较大步长
- 已有现成的 FLE 实现
- 对无源性有特殊要求

**ULM 的失效场景**：
- 拟合频率范围不足（高频端截断过快）
- 无源性处理不当导致网络振荡
- 时间步远大于模态延时差异时数值不稳定
- 频率相关土壤参数的不确定性无法通过 ULM 结构本身消除

## 相关页面

- [[distributed-parameter-line]] — 线路方程总框架，ULM 的理论根基
- [[bergeron-model]] — 常参数行波时域实现的入口
- [[folded-line-equivalent]] — 频变线路节点导纳分解的相邻实现路线
- [[vector-fitting]] — ULM 中拟合 $\mathbf{Y}_c$ 和 $\mathbf{H}$ 的标准工具
- [[passivity-enforcement]] — 保证 ULM 有理模型无源性的关键步骤
- [[frequency-dependent-soil]] — 土壤参数频率相关性影响 ULM 输入
- [[earth-return-impedance]] — 大地返回阻抗的频率相关特性
- [[mutual-impedance]] — 互感阻抗的频率相关建模
- [[frequency-dependent-modeling]] — 宽频参数转时域的共性问题

## 来源论文

- [[zanon-2021-implementation-of-ulm]] — Zanon et al. 2021，ULM 在 ATP 中的完整实现，含 Norton 等效递推公式
- [[noda-2015-frequency-partitioning]] — Noda 2015，FpF 分频区拟合方法，500 kV 双回线基准测试
- [[colqui-2022-modified-fle]] — Colqui et al. 2022，FLE 改进实现，与 JMarti 对比
- [[loaiza-2025-delay-estimation-ulm]] — Loaiza-Elejalde et al. 2025，延时估计与 APF 方法
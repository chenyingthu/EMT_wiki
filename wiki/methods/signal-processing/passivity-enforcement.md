---
title: "无源性保证 (Passivity Enforcement)"
type: method
tags: [passivity-enforcement, positive-real, stability, frequency-dependent, vector-fitting]
created: "2026-05-04"
updated: "2026-05-15"
---

# 无源性保证 (Passivity Enforcement)

## 定义

无源性（Passivity）是物理系统能量特性的基本约束。设系统传递函数为 $H(s)$，若对任意正实频率 $\omega$ 满足

$$\Re\{H(j\omega)\} \geq 0$$

则该系统为无源的——即系统不产生净能量，仅消耗或传输能量。在 EMT 仿真中，输电线路、电缆、变压器等无源网络元件的有理函数模型若违反无源性条件，即使频域拟合精度看似良好，时域递归卷积仿真中也可能因非物理能量注入而数值发散。

多端口系统的无源性由导纳矩阵 $Y(j\omega)$ 的 Hermitian 部分正定性判定：

$$\lambda_i\left(\frac{Y(j\omega) + Y^H(j\omega)}{2}\right) \geq 0, \quad \forall \omega$$

其中 $\lambda_i(\cdot)$ 表示矩阵特征值，$Y^H$ 为共轭转置。所有特征值非负是模型无源性的充要条件。

**边界限定**：本方法仅适用于线性时不变系统的频变参数建模，非线性系统需分段线性化处理；且模型在拟合阶段本身应接近无源，严重非无源的模型（如强有源性系统）无法通过无源性强制修正。

## EMT 中的角色

电磁暂态（EMT）仿真对稳定性有严格要求。时域求解采用梯形积分法或隐式 Gear 法等数值积分，步长通常在微秒级（$1$–$100\ \mu\text{s}$）。在此精度要求下，频变线路模型的宽频特性必须以有理函数形式拟合，并通过递归卷积注入时域递推。

无源性在 EMT 中的核心价值体现在三个方面：

1. **数值稳定性保证**：有源模型会在仿真中引入非物理能量，导致状态发散，即使拟合误差在目标频带内很小
2. **多子系统级联保持整体无源性**：各元件模型独立满足无源性后，级联组成的网络整体保持稳定
3. **物理可实现性约束**：无源系统必定满足能量守恒定律，其有理函数模型的极点必位于复平面左半部

实际工程中，Universal Line Model（ULM）和 Frequency Dependent Cable Model（FDCM）是 EMT 领域最常用的频变线路模型。这类模型通过矢量拟合将频域阻抗 $Z(\omega)$ 和导纳 $Y(\omega)$ 拟合成有理函数形式，其传递函数 $H(s)$ 和特征导纳 $Y_C(s)$ 的极点位置直接决定时域递推卷积的稳定性。拟合过程仅优化目标频带内的频率响应，不自动保证正实性/无源性——这是无源性保证方法存在的根本原因。

## 形式化表达

### 传递函数正实性条件

$$H(s) \text{ 正实} \iff \Re\{H(j\omega)\} \geq 0, \quad \forall \omega \in \mathbb{R}$$

这要求 $H(s)$ 的极点全部位于左半平面，且分子多项式次数不超过分母次数（相对阶非负）。

### 多端口导纳矩阵无源性

$$\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega) \geq 0$$

矩阵所有特征值非负。等价于检查 Hermitian 矩阵 $\Theta(\omega) = Y(j\omega) + Y^H(j\omega)$ 的最小特征值：

$$\lambda_{\min}(\Theta(\omega)) \geq 0, \quad \forall \omega$$

### 特征导纳与传播函数

ULM 模型中，特征导纳 $Y_C(s)$ 和传播函数 $H_I(s)$ 分别为：

$$Y_C(s) = \sum_{i=1}^{n} \frac{R_i}{s - p_i} + D + sE$$

$$H_I(s) = \sum_{g=1}^{G} e^{-s\tau_g} \sum_{i=1}^{n_g} \frac{\hat{R}_{i,g}}{s - \hat{p}_{i,g}}$$

其中 $R_i$ 为留数矩阵，$p_i$ 为极点，$D$ 和 $E$ 为常数矩阵，$\tau_g$ 为模态时延。节点导纳矩阵由二者组装：

$$Y_n = \begin{bmatrix} (I-H_I^2)^{-1}(I+H_I^2)Y_C & -2(I-H_I^2)^{-1}H_I Y_C \\ -2(I-H_I^2)^{-1}H_I Y_C & (I-H_I^2)^{-1}(I+H_I^2)Y_C \end{bmatrix}$$

### 节点导纳矩阵无源性检查

$$Y_{nodal} = Y_c(I+H)^{-1}(I-H)$$

无源性判定：

$$\lambda(\text{real}(Y_{nodal} + Y_{nodal}^H)) \geq 0$$

## 核心机制

无源性保证方法按机制分为两大类：约束拟合（在拟合阶段直接施加无源性约束）和后处理修正（拟合后检测并修正非无源频段）。

### 方法一：约束拟合

在矢量拟合（Vector Fitting）过程中直接施加无源性约束，将优化问题表述为：

$$\min_{\{R_i, p_i\}} \sum_k |Y(j\omega_k) - \sum_i \frac{R_i}{j\omega_k - p_i}|^2 \quad \text{s.t.} \quad \lambda_{\min}(\Theta(\omega)) \geq 0, \forall \omega$$

约束条件要求所有频率采样点的 Hermitian 矩阵特征值非负。这需要将非线性特征值约束线性化为一组线性不等式约束，通过凸优化求解。

**优点**：从源头避免无源性违规，修正量最小
**缺点**：优化问题规模大、非线性约束需线性化近似、求解耗时

### 方法二：后处理修正

拟合完成后再检测非无源频段，通过扰动已有点/留数/常数项消除违规。根据扰动对象进一步分为三种：

#### 2.1 留数扰动法（R 方案）

仅扰动特征导纳的留数矩阵 $R_i$：

$$\min_{\Delta R} \|\Delta R\|_F \quad \text{s.t.} \quad \lambda_{\min}(\Theta(\omega)) \geq 0, \forall \omega$$

**优点**：变量维度小，计算效率高
**缺点**：修正压力集中于留数，可能导致拟合精度下降

#### 2.2 留数-极点联合扰动法（RP 方案）

同时扰动留数 $R_i$ 和极点 $p_i$：

$$\min_{\Delta R, \Delta p} \left\| \begin{bmatrix} \Delta R \\ \Delta p \end{bmatrix} \right\|_2 \quad \text{s.t.} \quad \lambda_{\min}(\Theta(\omega)) \geq 0, \forall \omega$$

**优点**：修正自由度更高，分散修正压力，Frobenius 距离减少约 $30$–$50\%$
**缺点**：优化变量增加，收敛性需关注

#### 2.3 留数-极点-常数联合扰动法（RPC 方案）

在 RP 基础上增加常数矩阵 $D$ 的扰动自由度：

$$\min_{\Delta R, \Delta p, \Delta D} \left\| \begin{bmatrix} \Delta R \\ \Delta p \\ \Delta D \end{bmatrix} \right\|_2 \quad \text{s.t.} \quad \lambda_{\min}(\Theta(\omega)) \geq 0, \forall \omega$$

**优点**：对近直流大幅违规（深度达 $-40$ 量级）特别有效，避免低频失真
**缺点**：变量维度最高，需 DC 校正预处理以保证算法收敛

### 方法三：并联无源滤波器法（De Silva 2021）

在线路端口节点上并联物理可实现的 RLC/RC/RL 无源滤波器，补偿特定频段的负特征值：

$$F(\omega) = \frac{K\lambda_0}{1 + jQ\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)}$$

其中 $\lambda_0$ 为违规中心频率的最大负特征值，$\omega_0$ 为中心角频率，$Q$ 为品质因数。滤波器 RLC 参数由下式计算：

$$R = \frac{1}{K\lambda_0}, \quad L = \frac{QR}{\omega_0}, \quad C = \frac{1}{RQ\omega_0}$$

改进的品质因数估算避免过/欠补偿：

$$Q = \min\left( \frac{\sqrt{2}-1}{\frac{\omega_U}{\omega_0} - \frac{\omega_0}{\omega_U}}, \frac{\sqrt{2}-1}{\frac{\omega_0}{\omega_L} - \frac{\omega_L}{\omega_0}} \right)$$

其中 $\omega_L, \omega_U$ 为违规频段下、上边界频率。

**优点**：非迭代、局部修正、无需矩阵线性化或特征值灵敏度计算、保持线路自然解耦结构
**缺点**：需要多次频域扫描定位违规频段，滤波器参数需精细调校

### 方法四：双层局部补偿（Shu 2019）

针对大规模交直流混合仿真中的外部网络等值，提出双层频变网络等值（T-FDNE）：

$$Y_{T-FDNE}(s) = Y_{detailed}(s) + Y_{equivalent}(s) + Y_{comp}(s)$$

局部无源性补偿辅助函数：

$$Y_{comp}(s) = \sum_{m=1}^{M} \frac{\Delta R_m}{s - \Delta p_m}$$

仅在检测到的无源性破坏频段内添加微小补偿项，无需全局参数重优化。

**优点**：建模效率提升超 $200$ 倍，发散率从 $18.7\%$ 降至 $0\%$
**缺点**：需要两层建模（详细层 + 等值层），算法复杂度较高

### 方法五：三层防御策略（Gustavsen 2008）

针对 ULM 的三层无源性防御策略：

1. **低频段**：对并联导纳矩阵对角线添加人工并联电导 $G_{add} = C/\tau$，消除直流附近无源性违规，确保特性导纳在直流处非零。时间常数 $\tau = 1\text{s}$ 对应零点频率 $f_0 = 0.159\text{Hz}$
2. **高频段**：引入二阶低通滤波器 $F_{lp}(s) = 1/(1+s/\omega_1)(1+s/\omega_2)$ 引入人工衰减，强制执行特性导纳的高频渐近无源性条件
3. **带内校正**：对残余无源性违规，采用基于模态分解的二阶校正项 $\Delta Y(s) = R_1/(s-a_1) + R_2/(s-a_2)$ 进行端口补偿

**优点**：针对不同频段分类处理，覆盖 dc–高频全频带
**缺点**：参数预设（时间常数 $1\text{s}$、滤波器截止频率 $10\text{MHz}$）需根据具体系统调整

## 量化性能边界

| 测试场景 | 方法 | 无源性违规消除 | 精度保持 | 计算效率 |
|---------|------|---------------|---------|---------|
| 145kV 电缆, 1000m, Gustavsen 2008 | 三层防御 | 原始 $-40$ 负特征值 → 全正 | 目标频带精度未降低 | 少量迭代 |
| 2km 三相地下电缆, De Silva 2021 | 并联 RLC 滤波器（5个） | 全部消除 | 导纳误差 $\sim 6\times 10^{-7}$ | 无需迭代，局部修正 |
| 10km 双回电缆, De Silva 2021 | 并联 RLC 滤波器（2个） | 全部消除 | VF RMS 误差 $Y_c$: 0.0954%, $H$: 0.0731% | 即时收敛 |
| IEEE 39 + MMC, Shu 2019 | 双层局部补偿 | 发散率 $18.7\% \to 0\%$ | 动态误差 $<1.2\%$ | 建模时间 $0.1$–$0.2\text{s}$，效率提升 $>200\times$ |
| 100km HVDC 电缆, De Silva 2010 | 两阶段鲁棒法 | 约 $40\text{Hz}$ 处 $-40$ 负特征值 → 正 | 低频拟合误差降低一个数量级以上 | 线性约束最小二乘，收敛可靠 |
| 地下电缆, Becerra 2020 | RPC 联合扰动 | 全频段 $\lambda_i \geq 0$ | Frobenius 距离偏差降低 $30$–$50\%$ | $21$ 次迭代上限内收敛 |
| IEEE 39/68, Thakallapelli 2018 | 在线 RLS + 无源性 | 高频误差 $29.98\%$–$35.89\% \to <1\%$ | 误差 $<1\%$ | 建模时间缩短 $>90\%$ |

## 关键技术挑战

### 挑战一：近直流频段大幅违规

低频段（$<1\text{Hz}$）拟合误差通常最大，导致深度可达 $-40$ 的负特征值。大幅违规使特征值约束的线性化近似失效，需先进行 DC 校正预处理（如 Gustavsen 2008 的人工电导注入、Becerra 2020 的 DC 校正预处理）才能保证后续优化收敛。

### 挑战二：高频渐近无源性

当 $\omega \to \infty$ 时，有理函数逼近的行为需满足物理约束：

$$D = |Y_c(j\omega_{high})|, \quad \omega_{high} \gg \omega_{\max}$$

即特性导纳的高频极限必须为非负实数。若拟合时未约束该行为，高频段可能出现非物理增益。

### 挑战三：多端口系统的计算复杂度

无源性检查需计算 $n\times n$ 导纳矩阵的 Hermitian 部分特征值。当端口数 $n > 10$ 时，半尺寸测试矩阵方法可降低计算量，但仍需 $O(n^3)$ 量级的特征值分解运算。

### 挑战四：精度保持与无源性修正的权衡

修正无源性必然引入参数扰动。评估指标包括：

- 频率响应相对偏差：$\|\Delta Y|/Y$
- 状态空间 Frobenius 距离：$\|\Delta [A,B,C,D]\|_F / \|[A,B,C,D]\|_F$
- 收敛迭代次数与计算时间

联合扰动方法（RP、RPC）在精度保持上优于单一留数扰动，但代价是优化变量维度增加。

### 挑战五：在线递推辨识场景的无源性强制

当外部网络参数未知、需在线构造 FDNE 时（如 Thakallapelli 2018），无源性强制需嵌入递推最小二乘（RLS）框架中，实时监测极点分布（稳定性）和特征值符号（无源性），在线修正。

## 适用边界与选择指南

| 场景 | 推荐方法 | 原因 |
|------|---------|------|
| 离线批量处理，有充足计算时间 | Gustavsen 2008 三层防御或 Becerra 2020 RPC | 参数预设明确，修正量小，精度保持好 |
| 实时/在线场景，微秒级步长 | De Silva 2021 并联滤波器或 Shu 2019 双层补偿 | 非迭代或局部迭代，计算效率高，满足实时约束 |
| 严重近直流大幅违规（$<-20$） | Becerra 2020 RPC + DC 预处理 | 极点参与修正，分散修正压力，预处理保证收敛 |
| 端口数多（$>10$），计算资源有限 | De Silva 2010 线性约束最小二乘 | 线性约束，易于求解，半尺寸测试矩阵降低复杂度 |
| 外部网络参数未知，需在线等值 | Thakallapelli 2018 在线 RLS | 无需预知宽频导纳数据，z 域直接实现 |

## 相关方法

- [[vector-fitting]] - 矢量拟合是有理函数逼近的核心方法，无源性强制通常作为 VF 的后处理步骤
- [[frequency-dependent-line-model]] - 频变线路模型是最主要的应用对象
- [[wideband-modeling]] - 宽频建模覆盖 DC 至 MHz 频段，无源性是数值稳定性的前提
- [[transmission-line-model]] - 输电线路模型的 EMT 时域实现依赖无源性保证
- [[cable-model]] - 电缆模型的宽频特性更显著，无源性违规问题更突出
- [[numerical-integration]] - 数值积分方法的稳定性与模型无源性直接相关
- [[state-space-method]] - 状态空间模型的无源性判定和修正
- [[characteristic-method]] - 特征线法是 ULM 的基础
- [[fdne-model]] - 频变网络等值的无源性强制是接口稳定性的关键
- [[nodal-analysis]] - 节点分析中导纳矩阵的无源性检查
- [[frequency-scanning]] - 频率扫描是定位无源性违规频段的基础手段
- [[eigenvalue-analysis]] - 特征值分析用于无源性判定

## 来源论文

- [[passivity-enforcement-for-transmission-line-models|Gustavsen 2008]] - 三层防御策略，低频电导/高频滤波/端口二阶校正，145kV/1000m 电缆验证，负特征值 $-40 \to$ 全正
- [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|De Silva 2021]] - 并联 RLC 非迭代算法，2km/10km 地下电缆验证，导纳误差 $6\times10^{-7}$，VF RMS 误差 0.0954%/0.0731%
- [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Becerra 2023]] - 全相域混合扰动，RPC 联合扰动，21 次迭代上限内收敛，多数案例 $<5$ 次迭代
- [[robust-passivity-enforcement-scheme-for|De Silva 2010]] - 两阶段鲁棒法，100km HVDC 电缆，线性约束最小二乘，40Hz 处 $-40$ 负特征值消除
- [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|Shu 2019]] - 双层 T-FDNE 局部补偿，建模时间 $0.1$–$0.2\text{s}$，发散率 $18.7\% \to 0\%$，IEEE 39 + 中国实际系统验证
- [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Thakallapelli 2018]] - 在线 RLS z 域辨识，高频误差 $35.89\% \to <1\%$，建模时间缩短 $90\%$，IEEE 39/68 节点验证
- [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Becerra 2020]] - 留数-极点联合扰动，RPC 方案，Frobenius 距离偏差降低 $30$–$50\%$，5 种电缆配置验证
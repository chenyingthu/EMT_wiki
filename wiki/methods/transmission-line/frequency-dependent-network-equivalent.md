---
title: "频变网络等值 (Frequency-Dependent Network Equivalent)"
type: method
tags: [frequency-dependent, network-equivalent, fdne, wideband, rational-approximation, vector-fitting, loewner-matrix, passivity, emtp]
created: "2026-05-04"
updated: "2026-05-16"
---

# 频变网络等值 (Frequency-Dependent Network Equivalent)

## 定义

频变网络等值（FDNE, Frequency-Dependent Network Equivalent）是一种将大规模外部电力系统在宽频范围内保留频率响应特性的网络简化方法。其核心思想是：通过有理函数逼近从边界端口观测到的外部系统频域导纳/阻抗矩阵，将数千节点外部系统降阶为数十个频变RLC元件，在保证计算效率的同时维持从直流到数kHz的暂态精度。

与工频短路阻抗等值（仅保留低频特性）和静态等值（无频率依赖）不同，FDNE通过保留端口导纳矩阵的宽频响应，使外部网络在开关暂态、故障清除、雷击过电压、HVDC/FACTS谐波交互等场景下的边界条件与全详细模型一致。

## EMT中的作用

FDNE是连接大规模系统与详细EMT仿真的关键技术：

- **计算效率**：将数千节点外部系统降阶为数十个等值元件，计算量降低一个数量级
- **频带覆盖**：保留从直流到数kHz的关键谐振特性，适用于开关暂态、谐波、雷击分析
- **暂态保真**：准确复现外部系统对内部扰动的宽频响应，避免固定阻抗等值导致的波形失真
- **多场景复用**：同一FDNE可支撑不同内部故障工况的多次EMT仿真，避免重复建模
- **工程实用**：以EMTP可直接使用的RLC支路或诺顿等效形式输出，无需修改仿真器内核

### 核心挑战

1. **无源性保证**：有理函数逼近后的模型在全频段必须保持无源（$\text{Re}(Y(j\omega)) \geq 0$），否则接入含开关/非线性元件的EMT网络后可能激发数值不稳定
2. **模型阶数权衡**：阶数过高增加历史项递推负担，阶数过低丢失关键谐振动态
3. **多端口耦合**：端口间耦合导纳的非对角元素必须准确拟合，不能分解为独立单端口等值
4. **频率扫描效率**：大规模系统高频扫描计算量大，扫描点不足导致插值误差

## 建模方法

### 方法1：矢量拟合（Vector Fitting）FDNE

矢量拟合是FDNE的主流方法，通过有理函数逼近频率响应数据。

**单端口情形**：

$$Y_{\text{eq}}(s) = \sum_{k=1}^{n}\frac{r_k}{s - p_k} + d + se$$

其中 $p_k$ 为极点（必须位于左半平面 $\text{Re}(p_k) < 0$ 保证稳定性），$r_k$ 为留数，$d$ 为常数项，$e$ 为微分项（反映高频渐近行为）。

**多端口情形**：导纳矩阵的有理逼近为：

$$\mathbf{Y}_{\text{eq}}(s) = \sum_{k=1}^{n}\frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}$$

其中 $\mathbf{R}_k$ 为留数矩阵（$m \times m$，$m$ 为端口数），$\mathbf{D}$ 和 $\mathbf{E}$ 分别为常数矩阵和微分矩阵。

**时域实现**：每个极点-留数分式转换为伴随网络的历史项递推。实极点 $p_k$ 产生一阶RC/RL支路；复共轭极点 $\{p_k, p_k^*\}$ 合并为二阶RLC谐振支路；直接项 $d$ 产生恒电导 $G = d$ 并入节点方程。

### 方法2：Loewner矩阵（Loewner Matrix）FDNE

Loewner矩阵方法将VLSI多端口建模中的切向插值框架引入FDNE，无需迭代初始极点。

**算法流程**：

1. **切向采样**：在复频点 $s_1, s_2, \ldots, s_N$ 处施加方向向量 $\mathbf{v}_k$（右采样）和 $\mathbf{w}_k$（左采样），测量对应的频率响应 $\mathbf{R}_k$
2. **Loewner矩阵构造**：由左右切向数据和差商构造Loewner矩阵 $\mathbf{L}$ 和移位Loewner矩阵 $\mathbf{L}_\sigma$
3. **矩阵铅笔建立**：$\mathbf{L}_\sigma - \sigma \mathbf{L}$ 隐含满足切向插值条件的描述符系统结构
4. **SVD阶数指示**：对Loewner矩阵做奇异值分解，保留主要奇异子空间确定模型阶数
5. **状态空间描述符输出**：

$$\mathbf{E}\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \quad \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

频域上对应 $\mathbf{Y}(s) = \mathbf{C}(s\mathbf{E} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$

**优势**：非迭代方法，不依赖初始极点选择；SVD提供模型阶数的客观指示。精度、稳定性和无源性与矢量拟合相当（Gustavsen 2019）。

### 方法3：Brune/Tellegen网络综合FDNE

该方法从网络综合角度直接构造物理无源网络，保证无源性不是"事后修正"而是"拓扑内在属性"。

**算法流程**：

1. **虚轴极点移除**：$s=0$ 处极点 → 串联电容；$s=\infty$ 处极点 → 串联电感；有限谐振频率处极点 → LC谐振支路，留数矩阵决定元件值和变比
2. **导纳域零点移除**：对剩余阻抗求逆，移除导纳虚轴零点，对应并联元件
3. **最小电阻提取**：计算实部矩阵最小可提取电阻 $\mathbf{R}_{\min}$，使剩余阻抗在某频率处出现秩亏
4. **Brune循环入口**：通过零空间向量和秩一矩阵构造串联电感、并联LC支路及耦合电感/理想变压器
5. **Tellegen多端口扩展**：零空间向量构造耦合电感/理想变压器关系，每次扣除部分由物理无源网络实现
6. **循环终止**：剩余项退化为常数电阻矩阵 $\mathbf{R}_{\infty}$

**输出**：80个RLCM模块（230kV三相输电网络三端口等值案例），时域EMT接入方式为节点方程诺顿等效。

### 方法4：低阶有理函数拟合FDNE

针对频变输电线路中特征阻抗 $Z_C(\omega)$ 和传播系数 $A(\omega)$ 的拟合优化。

**算法流程**：

1. **低阶初始定位**：不按Bode渐近线法的折线拐点机械配置，而是用较少数量的初始零极点（通常3-5对）
2. **非线性最小二乘修正**：在初始结构上调整零极点和增益，使离散频点处的拟合误差 $\epsilon$ 最小化

$$\epsilon = \sum_{k=1}^{N} w_k \left| F_{\text{orig}}(j\omega_k) - F_{\text{fit}}(j\omega_k) \right|^2$$

其中 $w_k$ 为频率权重，可强调关键频段。

**核心价值**：零极点数量越少，时域递归卷积的历史项越少——每个指数项 $r_k/(s-p_k)$ 在时域对应 $e^{p_k t}$ 的卷积，历史项维护和递推计算量直接与阶数成正比。

### 方法5：多端口π型综合FDNE

将多端口导纳矩阵综合为可解释的π型网络结构。

**算法流程**：

1. **频率扫描**：在边界端口施加正弦源，通过相量解得到 $m \times m$ 端口导纳矩阵 $\mathbf{Y}(\omega_k)$
2. **导纳矩阵分解**：对角项 $Y_{ii}$ 为端口自导纳；非对角项 $Y_{ij}$ 为端口间耦合导纳
3. **π型转换**：端口间支路导纳 $Y_{ij}^{\text{branch}} = -Y_{ij}$；对地支路 $Y_i^{\text{shunt}} = \sum_{j=1}^{m} Y_{ij}$
4. **极点-留数拟合**：每个支路导纳元素拟合为极点-留数分式
5. **诺顿等效**：梯形积分离散化后，每个分式在当前步表现为 $I(t) = G \cdot V(t) + I_{\text{hist}}(t - \Delta t)$

**量化数据**：Saldaña & Calzolari 2022 给出500kV系统案例，5–5000 Hz范围内导纳矩阵最大绝对拟合误差为 $8.805 \times 10^{-5}$ mho；Type-69实现耗时为完整系统的29%，外部子模型实现为45.7%。

## 形式化表达

### 频率扫描基础

在边界端口施加扫频电压源或电流源，测量驱动点阻抗和转移阻抗：

$$Z_{ij}(j\omega_k) = \frac{V_i(j\omega_k)}{I_j(j\omega_k)}\bigg|_{I_{m \neq j} = 0}$$

其中 $\omega_k$ 覆盖关心的最高暂态频率（通常10 Hz – 10 kHz）。

### 有理逼近误差度量

$$ \epsilon_{\text{fit}} = \sum_{k=1}^{N} w_k \left\| \mathbf{Y}_{\text{orig}}(j\omega_k) - \mathbf{Y}_{\text{fit}}(j\omega_k) \right\|_F^2 $$

其中 $\|\cdot\|_F$ 为Frobenius范数，权重 $w_k$ 可用于强调关键频段。

### 稳定性与无源性约束

- **稳定性**：所有极点位于左半平面 $\text{Re}(p_k) < 0$
- **无源性**：对于所有频率 $\omega$，$\text{Re}(\mathbf{Y}(j\omega))$ 为对称正定矩阵

无源性强制（[[passivity-enforcement]]）是VF等方法的必要后处理步骤。

### 多端口导纳矩阵结构

$$\mathbf{Y}_{\text{eq}}(s) = \begin{bmatrix} Y_{11} & Y_{12} & \cdots & Y_{1m} \\ Y_{21} & Y_{22} & \cdots & Y_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ Y_{m1} & Y_{m2} & \cdots & Y_{mm} \end{bmatrix}$$

其中非对角元素 $Y_{ij}$（$i \neq j$）描述端口间耦合，是FDNE区别于多个独立单端口等值的关键。

## 关键技术挑战

### 挑战1：无源性破坏

矢量拟合等方法逼近得到的模型可能在某些频段呈现负阻特性（$\text{Re}(Y) < 0$），当接入含开关和非线性元件的EMT网络时产生数值不稳定。

**解决路径**：Brune/Tellegen网络综合从拓扑层面保证无源性；或采用后处理无源性强制（[[passivity-enforcement]]）修正非无源部分。

### 挑战2：模型阶数选择

阶数选择是FDNE的核心超参数：阶数过高增加计算负担，阶数过低丢失谐振动态。

- 凭经验选择可能导致拟合精度不足或过度拟合
- Loewner方法的SVD提供了客观的阶数指示
- 低阶拟合法通过初始零极点定位+最小二乘修正将阶数选择与精度优化分离

### 挑战3：多端口耦合导纳拟合

多端口FDNE必须保留端口间耦合 $Y_{ij}$（$i \neq j$），而非分解为独立单端口等值。

**要求**：导纳矩阵拟合需保证对称性 $\mathbf{Y} = \mathbf{Y}^T$ 和正实性 $\text{Re}(\mathbf{Y}(j\omega)) > 0$。

### 挑战4：非线性外部系统

FDNE的理论基础是线性时不变系统假设。当外部系统含HVDC换流器、STATCOM、风电变流器等电力电子设备时，频域扫描结果可能受控制策略主导。

**应对策略**：对电力电子设备用其等效阻抗或平均值模型替代扫描；或在控制模式切换时触发FDNE在线更新。

### 挑战5：频率扫描效率

大规模系统的频率扫描涉及复频域求解，计算量随系统规模和端口数增加。

**优化方向**：稀疏矩阵技术、模型降阶预处理的扫描、多端口并行扫描。

## 量化性能边界

### 拟合精度

| 来源 | 频率范围 | 最大拟合误差 | 拟合方法 |
|------|---------|-------------|---------|
| Saldaña & Calzolari 2022 | 5–5000 Hz | $8.805 \times 10^{-5}$ mho | 极点-留数拟合 |
| Gustavsen & Semlyen 1999 | 0.1 Hz – 10 kHz | $< 1\%$ 相对误差 | 矢量拟合 |
| Morched et al. 1992 | 10 Hz – 5 kHz | $< 2\%$ 幅值误差 | 频率扫描+有理逼近 |

### 计算效率

| 来源 | 系统规模 | 等值后规模 | 加速比 | 实现方式 |
|------|---------|-----------|--------|---------|
| Saldaña & Calzolari 2022 | 500 kV大型网络 | 多端口FDNE | Type-69: 29%耗时；外部子模型: 45.7%耗时 | EMTP-ATP TACS/MODELS |
| Saldaña & Calzolari 2022 | 230 kV三相网络 | 80个RLCM模块 | **3.3×**（640 ms→194 ms） | Brune/Tellegen综合 |
| Morched et al. 1992 | Ontario Hydro大型网络 | 多端口FDNE | 大幅降低计算时间 | 单端口→多端口扩展 |

*注：原文均未报告完整误差分布、置信区间或实时硬件验证数据，以上量化数据仅来自原文表格/图注，应在正式引用时回查原文。*

## 适用边界与选择指南

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 线性假设 | 外部系统近似线性 | 饱和、开关动作需特殊处理 |
| 时不变性 | 外部拓扑恒定 | 快速拓扑变化需在线更新 |
| 频率范围 | 明确上下限 | 决定扫描和拟合参数 |
| 端口选择 | 边界清晰 | 端口位置影响等值精度 |

### 方法选择决策表

| 场景 | 推荐方法 | 理由 |
|------|---------|------|
| 高阶多端口、一般EMT精度 | 矢量拟合FDNE | 成熟稳健，EMTP工具链完善 |
| 需自动阶数指示 | Loewner矩阵方法 | SVD提供阶数指示，非迭代 |
| 强无源性要求（故障暂态） | Brune/Tellegen综合 | 拓扑层面保证无源性，数值稳定 |
| 大规模线路模型降阶 | 低阶有理函数拟合 | 减少递归卷积历史项，加速EMT |
| 需EMTP兼容输出 | 多端口π型综合 | 直接输出RLC支路，无需修改仿真器 |

### 失效边界

- **非线性主导**：外部系统含大量电力电子换流器
- **拓扑时变**：频繁开关操作改变外部系统结构
- **端口效应**：端口选择不当导致内部响应失真
- **谐振遗漏**：极点阶数不足或扫描范围不当
- **长时漂移**：FDNE参数不能反映外部系统慢变特性

## 相关方法

- [[vector-fitting]] - 有理函数逼近核心算法
- [[passivity-enforcement]] - 无源性强制后处理
- [[frequency-domain-analysis]] - 频域分析基础
- [[network-equivalent]] - 网络等值一般方法
- [[electromechanical-electromagnetic-hybrid-simulation]] - 混合仿真接口
- [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems]] - Loewner矩阵FDNE（切向插值框架）
- [[folded-line-equivalent]] - 折叠线等值与FDNE结合

## 来源论文

- [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems]] - Loewner矩阵切向插值FDNE（非迭代、SVD阶数指示）
- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] - 多端口FDNE预处理器与EMTP RLC模块（Ontario Hydro 500kV案例）
- [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent]] - Brune/Tellegen网络综合保证无源性（230kV 80模块 3.3×加速）
- [[low-order-approximation-method-for-frequency-dependent-network-equivalent]] - 低阶零极点定位+非线性最小二乘（减少递归卷积历史项）
- [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f]] - 高阶FDNE诺顿等效实现（5-5000Hz误差8.805×10⁻⁵ mho，Type-69 29%耗时）
- Gustavsen, B. and Semlyen, A., "Rational Approximation of Frequency Domain Responses," *IEEE TD*, 1999. - 矢量拟合奠基性工作
- Morched, A., et al., "A Multipurpose Frequency Scanning Technique," *IEEE PAS*, 1992. - 频率扫描技术开创者
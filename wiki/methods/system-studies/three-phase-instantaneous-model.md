---
title: "三相瞬时值模型 (Three-Phase Instantaneous Model)"
type: method
tags: [three-phase, instantaneous, abc-domain, phase-domain, electromagnetic]
created: "2026-05-02"
updated: "2026-05-16"
---

# 三相瞬时值模型 (Three-Phase Instantaneous Model)

## 定义与边界

三相瞬时值模型在 $abc$ 相域直接表示电压、电流、磁链和控制注入的时间函数：

$$\mathbf{v}_{abc}(t)=\begin{bmatrix}v_a(t)\\ v_b(t)\\ v_c(t)\end{bmatrix},\qquad \mathbf{i}_{abc}(t)=\begin{bmatrix}i_a(t)\\ i_b(t)\\ i_c(t)\end{bmatrix}.$$

它是 EMT 时域建模的基本形式之一。与 [[phasor-model]] 不同，瞬时值模型不要求波形是单频正弦；与 [[average-value-model]] 不同，它可以保留开关纹波、暂态偏置和相间不平衡；与 [[dq-transformation]] 不同，它不依赖同步旋转坐标系。

相域模型的核心特征是**保留三相各自独立的时间函数**，因此天然适合处理：
- 不对称故障（单相接地、两相短路、断相）
- 开关暂态（电力电子器件的快速开断）
- 非正弦稳态（谐波、间谐波、次谐波）
- 饱和与非线性（磁链与电流的非线性关系）

## EMT 中的角色

三相瞬时值模型在 EMT 仿真中承担以下任务：

1. **网络方程的基础变量**：在 [[nodal-analysis]] 中，三相节点电压 $\mathbf{v}_{abc}$ 构成待求解向量
2. **不对称故障的建模入口**：相间互感和接地导纳必须用相域矩阵显式表达
3. **电力电子开关的瞬间状态**：开关函数 $s_a, s_b, s_c$ 直接作用于瞬时电压和电流
4. **饱和非线性的表达载体**：电感矩阵 $\mathbf{L}_{abc}(\mathbf{i})$ 随电流或磁链变化

它通常需要比相量或平均模型更细的时间离散和更完整的网络状态，建模代价最高但信息最完整。

## 核心方程

### 线性三相支路方程

线性三相支路的电压—电流关系为：

$$\mathbf{v}_{abc}=\mathbf{R}_{abc}\mathbf{i}_{abc}+\frac{d\boldsymbol{\psi}_{abc}}{dt},\qquad \boldsymbol{\psi}_{abc}=\mathbf{L}_{abc}\mathbf{i}_{abc}.$$

若电感矩阵随时间或饱和状态变化：

$$\mathbf{v}_{abc}=\mathbf{R}_{abc}\mathbf{i}_{abc}+\mathbf{L}_{abc}\frac{d\mathbf{i}_{abc}}{dt}+\frac{d\mathbf{L}_{abc}}{dt}\mathbf{i}_{abc}.$$

### 电容支路方程

电容支路写为：

$$\mathbf{i}_{abc}=\frac{d\mathbf{q}_{abc}}{dt},\qquad \mathbf{q}_{abc}=\mathbf{C}_{abc}\mathbf{v}_{abc}.$$

### 节点导纳方程

离散化后的相域网络形成分块导纳方程：

$$\mathbf{Y}_{abc}\mathbf{V}_{abc}=\mathbf{I}_{abc}.$$

其中每个物理节点可包含三相电压未知量，也可根据接线方式包含零序和接地支路。

### 瞬时功率

瞬时有功功率直接由相量乘积求和：

$$p(t)=\mathbf{v}_{abc}^{T}(t)\mathbf{i}_{abc}(t)=v_a i_a+v_b i_b+v_c i_c.$$

瞬时无功功率在 $abc$ 相域中同样可以直接计算，无需坐标变换。

### 相域耦合矩阵

考虑相间互感时，三相电感矩阵包含自感和互感：

$$\mathbf{L}_{abc}=\begin{bmatrix}L_{aa} & M_{ab} & M_{ac}\\ M_{ba} & L_{bb} & M_{bc}\\ M_{ca} & M_{cb} & L_{cc}\end{bmatrix}.$$

对于平衡三相线路，有 $L_{aa}=L_{bb}=L_{cc}=L$，$M_{ab}=M_{bc}=M_{ca}=M$，且 $M=-L/2$（当三相耦合均匀时）。

### 相域互阻抗

三相耦合阻抗矩阵为：

$$\mathbf{Z}_{abc}=\mathbf{R}_{abc}+s\mathbf{L}_{abc}.$$

在频域中，耦合阻抗的频率依赖性（集肤效应、邻近效应）使 $\mathbf{R}_{abc}(s)$ 和 $\mathbf{L}_{abc}(s)$ 成为复频域矩阵。

### 开关函数模型

对于三相 VSC/MMC 换流器，开关函数驱动模型将开关状态映射为瞬时电压：

$$v_{a,b,c}=s_{a,b,c}\cdot V_{dc}/2.$$

若考虑动作死区和非理想特性，开关函数需加入重叠时间 $\Delta t_{ol}$：

$$s_k^{eff}(t)=\frac{1}{\Delta t_{ol}}\int_{t-\Delta t_{ol}}^{t}s_k(\tau)d\tau,\qquad k\in\{a,b,c\}.$$

## EMT建模方法

### 方法1：纯$abc$相域模型（直接解法）

直接对三相电压和电流瞬时值建模，每个时间步求解 $3n\times 3n$ 维节点方程，其中 $n$ 为三相节点数。

**特点**：建模最直接，但计算量与相数成正比，适合不对称故障和开关暂态研究。

### 方法2：相域耦合矩阵模型（互感支路法）

将相间互感、互容和接地耦合显式写入矩阵 $\mathbf{L}_{abc}$ 和 $\mathbf{C}_{abc}$：

- 输电线路：建立 $6\times 6$ 耦合矩阵（每相含正序和零序分量）
- 变压器：建立 $3\times 3$ 或 $3\times 3n$ 耦合矩阵（考虑绕组连接）
- 电缆：建立 $3\times 3$ 导体对地导纳矩阵

代表论文：[[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow]]（Papadias 2004）系统比较了五种三相变压器模型在快速暂态中的精度差异，发现零序与正序电感比 $\sigma=L_0/L_1$ 对过电压峰值有显著影响。

### 方法3：开关函数驱动模型（VSC/MMC专用）

在三相换流器中，开关函数 $s_a, s_b, s_c$ 直接驱动瞬时电压和电流计算：

$$v_{phase}=s_k\cdot V_{dc}/2,\qquad i_{dc}=s_k\cdot i_k,\qquad k\in\{a,b,c\}.$$

该方法需要与 PWM 调制模块耦合，适合分析开关纹波和谐波含量。

### 方法4：$\alpha\beta$空间矢量模型（坐标降维）

通过 Clarke 变换将 $abc$ 变换为 $\alpha\beta$ 分量：

$$\begin{bmatrix}v_\alpha\\ v_\beta\\ v_0\end{bmatrix}=T_c\begin{bmatrix}v_a\\ v_b\\ v_c\end{bmatrix},\qquad T_c=\frac{2}{3}\begin{bmatrix}1 & -\frac{1}{2} & -\frac{1}{2}\\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}\\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{bmatrix}.$$

零序分量 $v_0$ 反映接地或不平衡程度，$\alpha\beta$ 分量保留主能量。

代表论文：Yonezawa 2023 将同步机相域方程改写为磁路网络形式，利用受控源映射随转子角 $\theta$ 变化的时变电感矩阵 $\mathbf{L}_{abc}(\theta)$，避免dq0变换。

### 方法5：多速率相域模型（子系统细化）

不同子系统使用不同时间步长，在接口处进行信息交换：

- 电力电子部分：$\Delta t_{pe}=1-10\ \mu\text{s}$
- 网络其他部分：$\Delta t_{net}=10-100\ \mu\text{s}$
- 机电暂态部分：$\Delta t_{mech}=1-10\ \text{ms}$

接口处的相量映射需满足功率守恒和频率一致性条件。

## 形式化表达

三相瞬时值模型的核心数学表达汇总如下：

**电压—电流关系（时域）**：

$$\mathbf{v}_{abc}=\mathbf{R}_{abc}\mathbf{i}_{abc}+\mathbf{L}_{abc}\frac{d\mathbf{i}_{abc}}{dt}+\frac{d\mathbf{L}_{abc}}{dt}\mathbf{i}_{abc}.$$

**节点导纳方程（离散后）**：

$$\mathbf{Y}_{abc}\mathbf{V}_{abc}=\mathbf{I}_{abc}.$$

**瞬时有功功率**：

$$p(t)=\mathbf{v}_{abc}^{T}\mathbf{i}_{abc}=\sum_{k=a,b,c}v_k i_k.$$

**Clarke 变换（$abc\to\alpha\beta 0$）**：

$$\mathbf{v}_{\alpha\beta 0}=T_c\mathbf{v}_{abc},\qquad T_c=\frac{2}{3}\begin{bmatrix}1 & -\frac{1}{2} & -\frac{1}{2}\\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}\\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2}\end{bmatrix}.$$

**逆 Clarke 变换（$\alpha\beta 0\to abc$）**：

$$\mathbf{v}_{abc}=T_c^{-1}\mathbf{v}_{\alpha\beta 0}=T_c^{T}\mathbf{v}_{\alpha\beta 0}.$$

**开关函数驱动电压（VSC）**：

$$v_{phase}=s_k\cdot\frac{V_{dc}}{2},\qquad k\in\{a,b,c\}.$$

## 关键技术挑战

### 挑战1：相间耦合的不对称建模

三相参数不对称（不平衡线路、不平衡故障、接地不对称）使得耦合矩阵 $\mathbf{L}_{abc}$ 无法对角化，必须完整保留 $3\times 3$ 耦合结构。

**影响**：计算量是不平衡度的函数，单相接地故障时另外两相仍参与耦合计算。

### 挑战2：高频开关暂态的数值稳定性

开关沿的高频分量（$dV/dt$ 达到数千kV/μs）要求仿真步长足够小以捕捉暂态细节，但步长过小会显著增加计算时间。

**常用策略**：变步长（开关动作时自动缩小步长）、开关事件检测、插值PWM。

### 挑战3：时变电感矩阵的处理

同步机转子旋转时，定子自感和定转子互感随转子角 $\theta$ 周期变化：

$$\mathbf{L}_{abc}(\theta)=\mathbf{L}_0+\sum_{n=1,3,5,\ldots}L_n\cos(n\theta).$$

**处理方法**：受控源映射（Yonezawa 2023）、查表插值、在线更新雅可比矩阵。

### 挑战4：相域与dq/序域的坐标混用

$abc$、$\alpha\beta$、$dq$ 和相量变量必须标明参考系，避免把平均量和瞬时量相加。

**常见错误**：将 $dq$ 坐标系的直流控制量与 $abc$ 瞬时值直接叠加。

### 挑战5：饱和非线性的迭代收敛

饱和使电感矩阵 $\mathbf{L}_{abc}(\mathbf{i})$ 成为电流的非线性函数，牛顿迭代可能出现不收敛或振荡。

**解决思路**：主子矩阵分区（线性部分用直接求解，非线性部分用迭代）、雅可比预conditioning。

## 量化性能边界

| 建模方法 | 适用场景 | 步长范围 | 计算效率 | 精度 |
|---------|---------|---------|---------|------|
| 纯 $abc$ 直接解 | 不平衡故障 | 1-50 μs | 低（3n×3n规模） | 最高 |
| 相域耦合矩阵 | 线路/变压器耦合 | 10-100 μs | 中 | 高 |
| 开关函数驱动 | VSC/MMC换流器 | 1-10 μs | 中 | 取决于开关模型 |
| $\alpha\beta$ 空间矢量 | 平衡系统谐波分析 | 10-100 μs | 高（降1维） | 中等（忽略零序） |
| 多速率相域 | 大系统混合仿真 | 1 μs-10 ms | 高（分区） | 取决于接口精度 |

**来源**：Noda 2015 指出相域频变建模的关键挑战在于宽频矩阵拟合；Yonezawa 2023 在100 μs步长下验证了相域同步机模型的波形精度；Papadias 2004 发现零序电感比 $\sigma$ 对三相变压器开断过电压有显著影响。

## 适用边界与选择指南

| 场景 | 推荐模型 | 原因 |
|------|---------|------|
| 不对称故障分析 | 纯 $abc$ 相域模型 | 必须保留相间耦合不对称性 |
| 电力电子开关暂态 | 开关函数驱动模型 | 直接捕捉开关沿和高频纹波 |
| 平衡系统谐波分析 | $\alpha\beta$ 空间矢量模型 | 降维计算效率高 |
| 多速率大规模系统 | 多速率相域模型 | 按子系统选择步长 |
| 同步机详细模型 | 相域耦合矩阵+磁路等效 | 保留空间谐波和不平衡绕组 |
| 长线路频变特性 | 相域频变矩阵模型 | 避免模态变换矩阵的近似 |

## 与相关页面的关系

- [[phasor-model]]：三相瞬时值在正弦稳态、单频假设下可压缩为相量
- [[dq-transformation]]：提供从相域到同步旋转坐标系的变换工具
- [[coordinate-transformation]]：提供从相域到 $\alpha\beta$ 坐标系的 Clarke 变换
- [[symmetrical-components]]：提供从相域到序分量的对称分量变换
- [[nodal-analysis]]：提供相域网络方程组装基础
- [[switching-function-method]]：把开关状态映射为瞬时相电压或线电压
- [[switch-modeling]]：决定开关事件和器件非理想性的表示层级
- [[phase-domain-modeling]]：提供相域建模的通用框架

## 来源论文

- **Yonezawa 2023** — 相域同步机磁路等效建模（Yonezawa，Electric Power Systems Research）：将同步机时变电感矩阵用受控源映射为磁路网络，在100 μs步长下与常规Park模型验证等效
- **Noda 2015** — 频域分区拟合的相域频变线路建模（IEEE TPWRD）：将FpF方法引入ULM相域线路建模，最大拟合偏差降至 $1.2\times 10^{-3}$
- **Papadias 2004** — 三相变压器快速EMT暂态建模（IEEE TPWRD）：系统比较五种三相变压器模型在400/120/21 kV自耦变压器开断过电压中的性能差异，发现 $\sigma=L_0/L_1=0.96$ 对低磁阻铁心结构有显著影响
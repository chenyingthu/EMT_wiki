---
title: "多桥子模块统一表示方法 (MBSM)"
type: method
tags: [mbsm, multi-bridge-submodule, mmc, unified-modeling, average-value-model, generalized-norton, detailed-equivalent-model]
created: "2026-05-05"
updated: "2026-05-14"
---

# 多桥子模块统一表示方法 (MBSM)

## 定义

多桥子模块统一表示方法（Multi-Bridge Submodule Unified Representation，简称 MBSM）是一类面向模块化多电平换流器（MMC）中多种子模块拓扑的统一建模框架。其核心思想是：用一套统一的桥臂状态变量、插入指数和等效接口，将半桥（HBSM）、全桥（FBSM）、钳位双子模块（CDSM）、五电平交叉子模块等多种拓扑映射到同一数学表示中，从而避免为每种子模块分别编写建模代码。

MBSM 方法不是单一算法，而是包含三个层面的统一：

- **拓扑统一**：不同子模块结构映射到同一关联矩阵 / 支路导纳矩阵表示
- **等效统一**：统一采用诺顿 / 戴维南等效接口与外部网络耦合
- **模型切换统一**：在详细等效模型（DEM）与开关函数平均值模型（SFB-AVM）之间平滑切换

本页讨论的是统一表示框架本身，不是具体的 MMC 整机模型或通用线路公式。

## EMT 中的角色

在 EMT 仿真中，MBSM 方法主要解决以下问题：

1. **多拓扑建模重复性**：当研究不同子模块选型（HBSM/FBSM/CDSM 混合）时，传统方法需要为每种拓扑重新推导伴随电路和符号解析解，MBSM 通过矩阵参数化实现一次建模、多次复用。
2. **DEM 与 AVM 的互补性**：DEM 精度高但计算量大，AVM 速度快但丢失电容电压纹波细节；MBSM 框架支持两者之间的平滑切换。
3. **系统级直流电网仿真**：在含多个换流器的 MTDC 系统中，MBSM 可将每个 MMC 桥臂等效为仅含 2m 个外部接口节点的小维诺顿等效电路，大幅降低系统导纳矩阵规模。
4. **闭锁 / 故障工况一致性**：统一方程在解锁、闭锁、整流三种运行状态下均保持有效，无需为故障工况单独建模。

## 核心建模方法

MBSM 方法体系包含四种核心方法，按统一程度由低到高排列。

### 方法一：拓扑参数化统一（关联矩阵法）

**代表论文**：Xu 等 2019, "Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary Multi-type Submodule Structures"

**原理**：将任意端口子模块的伴随电路用图论方法参数化。设子模块伴随电路含 $n$ 个节点、$b$ 条支路，构造：

- **关联矩阵** $A_a$（$n \times b$ 阶）：描述节点与支路的连接关系
- **支路导纳矩阵** $Y_b$（$b \times b$ 阶对角矩阵）：各支路导纳值
- **支路电流源列向量** $I_S$（$b \times 1$ 阶）：诺顿等效电流源

节点电压方程为：

$$Y = A_a Y_b A_a^T \tag{1}$$

$$J = A_a I_S \tag{2}$$

$$YV = J + I \tag{3}$$

将节点分为外部节点（EX，下标 $1 \sim 2m$）和内部节点（IN），式 (3) 可写为分块形式：

$$\begin{bmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{bmatrix} \begin{bmatrix} V_{EX} \\ V_{IN} \end{bmatrix} = \begin{bmatrix} J_{EX} \\ J_{IN} \end{bmatrix} + \begin{bmatrix} I_{EX} \\ I_{IN} \end{bmatrix} \tag{4}$$

通过高斯消元消去内部节点：

$$V_{IN} = Y_{22}^{-1} (J_{IN} + I_{IN} - Y_{21} V_{EX}) \tag{5}$$

代入第一行得到外部节点的诺顿等效：

$$Y_{eq} V_{EX} = J_{eq} + I_{EX} \tag{6}$$

其中 $Y_{eq} = Y_{11} - Y_{12} Y_{22}^{-1} Y_{21}$，$J_{eq} = J_{EX} - Y_{12} Y_{22}^{-1} (J_{IN} + I_{IN})$。

**特点**：
- 用户只需输入关联矩阵、导纳矩阵和电流源向量，无需手工推导符号解析解
- 适用于单端口（$m=1$）和双端口（$m=2$）子模块
- 代码高度可复用，更换拓扑仅需修改输入矩阵

**局限**：
- 需要矩阵求逆 $Y_{22}^{-1}$，当子模块内部节点较多时计算开销增大
- 针对对称双端口子模块推导，对非对称多端口需额外处理

### 方法二：舒尔补递归诺顿等效（广义诺顿法）

**代表论文**：Xu 等 2018, "High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents"

**原理**：采用舒尔补（Schur's complement）技术递归消除级联子模块的内部节点。对第 $k$ 个子模块，其伴随电路的节点导纳方程为：

$$Y_{SM}^{(k)} V_{SM}^{(k)} = J_{SM}^{(k)} + I_{SM}^{(k)} \tag{7}$$

将 $Y_{SM}$ 分块为外部接口节点（$m \times m$）和内部节点（$(n-m) \times (n-m)$）：

$$\begin{bmatrix} Y_{PP} & Y_{PQ} \\ Y_{QP} & Y_{QQ} \end{bmatrix} \begin{bmatrix} V_P \\ V_Q \end{bmatrix} = \begin{bmatrix} I_P \\ I_Q \end{bmatrix} \tag{8}$$

通过舒尔补消去内部节点 $V_Q$：

$$Y_{PP}^{(k)} V_P^{(k)} = I_P^{(k)} - Y_{PQ} Y_{QQ}^{-1} I_Q^{(k)} \tag{9}$$

令 $Y_{eq}^{(k)} = Y_{PP}^{(k)} - Y_{PQ}^{(k)} (Y_{QQ}^{(k)})^{-1} Y_{QP}^{(k)}$，$I_{eq}^{(k)} = I_P^{(k)} - Y_{PQ}^{(k)} (Y_{QQ}^{(k)})^{-1} I_Q^{(k)}$，得到第 $k$ 个子模块的诺顿等效。

**递归合并**：将第 $k$ 个子模块的等效与第 $k+1$ 个子模块串联合并：

$$\begin{bmatrix} Y_{ALL} & Y_{ALR} \\ Y_{ARL} & Y_{ARR} \end{bmatrix} \begin{bmatrix} X_L \\ X_R \end{bmatrix} = \begin{bmatrix} X_L \\ X_R \end{bmatrix} \tag{10}$$

递归执行 $N$ 次后，整个桥臂（$N$ 个子模块级联）被等效为仅含 $2m$ 个外部接口节点的诺顿等效电路。

**特点**：
- 计算复杂度随子模块数 $N$ 近似线性增长：$CT = 0.15N + 1.8$（秒）
- 详细模型（DSM）的计算复杂度为多项式增长：$CT = 0.053N^{2.3} + 80$
- 最终导纳矩阵维度比未简化结构小 2~3 个数量级
- 所有内部节点信息（各子模块电容电压）可精确反解

**量化结果**（Xu 等 2018，PSCAD/EMTDC 验证）：

| 子模块数 | 详细模型 CPU (s) | 广义诺顿等效 CPU (s) | 加速比 |
|---------|-----------------|---------------------|--------|
| 8 | 基准 | 基准 | 1x |
| 40 | ~12x | ~3x | ~4x |
| 200 | ~80x | ~30x | ~2.7x |
| 500 | ~500x | ~75x | ~6.7x |

相对误差小于 0.2%，可忽略不计。

**局限**：
- 需要处理电流过零点的插值问题，避免数值振荡
- 对多端口子模块（$m>1$）的接口矩阵维度高

### 方法三：动态平均化统一模型（DAUM）

**代表论文**：李亚楼 等 2020, "多样性子模块混合型 MMC 统一外特性高效电磁暂态模型"

**原理**：基于开关函数定义与电容器件动态特性，对多样性子模块串联结构进行统一的动态平均化等值。动态平均化等值原理为：借助串联结构中电容电压与电流的循环耦合关系，将电路拓扑变化转化为不变的等效电路与变化的开关函数的组合。

以 FBSM 串联结构为例，解锁模式下，$k$ 个子模块串联在任意 $t$ 时刻的实际电压为：

$$u_{scp}(t) = \sum_{i=1}^{k} S_i(t) \left( \frac{1}{C_i} \int_{t_0}^{t} S_i(t) i_{sc}(t) \mathrm{d}t + u_{ci}(t_0) \right) \tag{11}$$

基于动态平均化等值原理，假设同一桥臂中所有子模块的开关函数相等，即 $S_i(t) = S_{run}(t)$，则：

$$u_{sc}(t) = S_{run}(t) \left( \frac{1}{C_{sc}} \int_{t_0}^{t} S_{run}(t) i_{sc}(t) \mathrm{d}t + u_c(t_0) \right) \tag{12}$$

其中 $S_{run}(t)$ 为桥臂运行状态开关函数：

$$S_{run}(t) = \begin{cases} \frac{1 - e_j}{2} & \text{上桥臂} \\ \frac{1 + e_j}{2} & \text{下桥臂} \end{cases} \tag{13}$$

式中 $e_j$（$j=a,b,c$）为三相交流电压的调制参考波。

**子模块类型参数化**：引入类型参数 $d_{type1} \sim d_{type4}$，不同子模块类型的参数值如表 1 所示。

**表 1 · 多样性子模块串联结构的等效电压源类型参数**

| 子模块类型 | $d_{type1}$ | $d_{type2}$ | $d_{type3}$ | $d_{type4}$ |
|-----------|------------|------------|------------|------------|
| 全桥 (FBSM) | 1 | 1 | 1.0 | 1.0 |
| 半桥 (HBSM) | 1 | 1 | 0 | 0 |
| 单极全桥 | 1 | 1 | 1.0 | 1.0 |
| 钳位双子模块 (CDSM) | 2 | 1 | 0.5 | 0.5 |
| 五电平交叉 | 2 | 1 | 1.0 | 1.0 |

统一模型的等效电压源表达式为：

$$u_{sc}(t) = \begin{cases} d_{type1} \int \frac{1}{C_{sc}} (i_{sc1}(t) + i_{sc2}(t)) \mathrm{d}t + d_{type2} u_c(t_1) & \text{类型1} \\ d_{type4} u_{sc1}(t) & \text{类型2} \\ d_{type1} \int \frac{1}{C_{sc}} (i_{sc3}(t)) \mathrm{d}t + d_{type2} u_c(t_2) & \text{类型3} \end{cases} \tag{14}$$

**特点**：
- 通过类型参数 $d_{type}$ 实现不同子模块的统一表示，无需修改电路结构
- 考虑了 MMC 桥臂中电容的充放电动态过程，保证稳态仿真精度
- 满足闭锁、环流抑制、交直流故障清除和恢复时的仿真精度
- 具有良好可移植性，基于 ADPSS 仿真软件验证

**局限**：
- 本质上是平均化建模，丢失了单个子模块的电容电压纹波细节
- 在子模块选型对比分析中，不同类型子模块的差异化动态（如 FBSM 与 HBSM 电容电压的发散行为）可能无法精确捕捉

### 方法四：GSFB-AVM 与 DEM 组合模型（CM）

**代表论文**：Meng 等 2020, "Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation of MMCs"

**原理**：在 MBSM 框架内，将广义开关函数平均值模型（GSFB-AVM）与详细等效模型（DEM）组合，形成组合模型（Combined Model, CM）。两种模型共享相同的桥臂等效电路（统一臂模块 UAM），仅在电压源计算块中切换。

**GSFB-AVM 的桥臂等效**：

$$u_{arm}(t) = m(t) \cdot v_c^{avg}(t) \tag{15}$$

其中 $m(t)$ 为等效插入指数，$v_c^{avg}(t)$ 为平均电容电压。GSFB-AVM 用两个等效电容器（上桥臂和下桥臂各一个）代替 $N$ 个子模块，大幅降低计算量。

**DEM 的桥臂等效**：每个子模块用戴维南等效电路表示，$N$ 个子模块串联：

$$u_{arm}(t) = \sum_{i=1}^{N} (v_{th,i}(t) - R_{th,i}(t) \cdot i_{arm}(t)) \tag{16}$$

**组合模型切换**：

$$GSFB\text{-}AVM \rightarrow DEM: \quad v_{ci}(t) = \frac{1}{N} \sum_{i=1}^{N} v_{ci}(t) \tag{17}$$

$$DEM \rightarrow GSFB\text{-}AVM: \quad v_c^{avg}(t) = \frac{1}{N} \sum_{i=1}^{N} v_{ci}(t) \tag{18}$$

**特点**：
- GSFB-AVM 的 CPU 时间为 9.45 µs/步（480 个子模块的 MMC 站），DEM 为 51.59 µs/步，加速比约 5.5x
- 在实时硬件在环（RT-LAB）仿真中，GSFB-AVM 加速比达 24.45x（24.45 µs vs DEM）
- 相对误差小于 0.3%~0.4%（与 DEM 对比）
- 可平滑切换：正常运行时用 GSFB-AVM 提速，电容电压均衡控制或故障工况时切换到 DEM

**局限**：
- GSFB-AVM 无法精确模拟 FBSM 与 HBSM 电容电压的发散行为（故障后），此时必须切换到 DEM
- 半导体损耗模型在 GSFB-AVM 中采用解析法而非瞬态法，精度略低

## 形式化表达

MBSM 方法的核心数学框架可归纳如下：

**统一接口表示**：

$$Y_{eq} V_{EX} = J_{eq} + I_{EX} \tag{19}$$

其中 $Y_{eq}$ 为等效导纳矩阵（$2m \times 2m$），$V_{EX}$ 为外部接口电压向量，$J_{eq}$ 为历史电流源向量，$I_{EX}$ 为外部注入电流。

**递归合并公式**（舒尔补法）：

$$Y_{combined} = Y_A + Y_A (Y_B^{-1}) Y_A^T \tag{20}$$

**动态平均化等效电压**：

$$u_{sc}(t) = S_{run}(t) \left( \frac{1}{C_{sc}} \int_{t_0}^{t} S_{run}(t) i_{sc}(t) \mathrm{d}t + u_c(t_0) \right) \tag{21}$$

**类型参数映射**（DAUM 法）：

$$d_{type} \in \{ \text{FBSM: }(1,1,1,1), \text{ HBSM: }(1,1,0,0), \text{ CDSM: }(2,1,0.5,0.5) \} \tag{22}$$

## 关键技术挑战

### 1. 多端口子模块的接口矩阵维数爆炸

当子模块外部端口数 $m > 1$ 时，接口矩阵维度为 $2m \times 2m$。对于五电平交叉子模块（$m=2$）或更复杂的多端口拓扑，递归合并过程中的矩阵运算量显著增加。Xu 等 2018 采用舒尔补逐步消元，将最终导纳矩阵维数控制在 2m 维，但中间过程的 $Y_{QQ}^{-1}$ 求逆仍是计算瓶颈。

### 2. 闭锁 / 故障工况的一致性

不同子模块在闭锁状态下的行为差异显著：HBSM 电容电压通过二极管自然放电，FBSM 可通过 IGBT 主动钳位。MBSM 的统一方程在闭锁工况下需要重新推导开关函数 $S_{run}(t)$ 的表达式。李亚楼 等 2020 通过引入三种运行状态（解锁、闭锁、整流）分别推导等效模型，但增加了模型复杂度。

### 3. DEM 与 AVM 切换的数据一致性

组合模型（CM）在 DEM 和 GSFB-AVM 之间切换时，需要保证电容电压数据的平滑传递。式 (17) 和 (18) 的映射是简单的算术平均，忽略了子模块间的电压不均衡。当子模块电容电压差异较大时，简单平均会导致切换瞬态的数值振荡。Meng 等 2020 通过限制切换频率（在稳态工况下切换）来缓解此问题。

### 4. 拓扑自动识别的编程实现

Xu 等 2019 提出的拓扑自动识别方法要求用户输入关联矩阵 $A_a$、支路导纳矩阵 $Y_b$ 和电流源向量 $I_S$。虽然理论上适用于任意拓扑，但实际工程中用户需要手动构建这些矩阵，对非专业用户的编程能力要求较高。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 广义诺顿等效 vs 详细模型加速比 | 2~7x（随子模块数增加） | Xu 等 2018 |
| 计算复杂度（等效法） | $CT = 0.15N + 1.8$ | Xu 等 2018 |
| 计算复杂度（详细模型） | $CT = 0.053N^{2.3} + 80$ | Xu 等 2018 |
| 相对误差（广义诺顿等效） | < 0.2% | Xu 等 2018 |
| GSFB-AVM vs DEM CPU 时间 | 9.45 µs vs 51.59 µs | Meng 等 2020 |
| GSFB-AVM 实时仿真加速比 | 24.45x | Meng 等 2020 |
| 组合模型相对误差 | < 0.4% | Meng 等 2020 |
| Parvari 加速 DEM vs 传统 DEM | HBSM: 30% 提升, FBSM: 60% 提升 | Parvari 等 2023 |
| 归一化 MAE（DEM vs TDM） | ~1% | Beddard 等 2015 |
| 归一化 MAE（AM vs TDM） | ~2.5% | Beddard 等 2015 |

## 适用边界与选择指南

**表 2 · MBSM 方法选择指南**

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|------|
| 单端口 MMC（HBSM/FBSM）系统级仿真 | 方法二（广义诺顿） | 计算复杂度最低，加速比最高 |
| 多端口子模块（双端口/五电平） | 方法二（广义诺顿） | 递归舒尔补天然支持多端口 |
| 多样性子模块混合型 MMC 选型对比 | 方法三（DAUM） | 类型参数化支持快速切换拓扑 |
| 需要精确电容电压纹波 | 方法一（拓扑参数化）或 DEM | 平均化方法丢失纹波细节 |
| 实时硬件在环仿真 | 方法四（GSFB-AVM/CM） | 24x 加速比满足实时性要求 |
| 闭锁/故障工况精确分析 | 方法四（CM 切换到 DEM） | GSFB-AVM 在故障工况下精度不足 |
| 新拓扑快速验证 | 方法一（拓扑参数化） | 无需推导符号解析解 |
| 含多个换流器的 MTDC 系统 | 方法二 + 方法三组合 | 诺顿等效降低网络矩阵规模 + 类型参数化 |

**不适用场景**：
- 需要精确模拟半导体开关瞬态损耗的研究（DEM 和 AVM 均不覆盖开关级细节）
- 子模块内部拓扑极度复杂（节点数 $n > 20$）且需要实时仿真的场景（矩阵求逆开销过大）
- 研究子模块间电容电压不均衡对系统级特性的影响（统一表示抹平了个体差异）

## 相关方法 / 相关模型

- [[half-bridge-submodule]] — 半桥子模块，MBSM 覆盖的最基本拓扑
- [[fbsm]] — 全桥子模块，MBSM 中通过类型参数 $d_{type} = (1,1,1,1)$ 统一表示
- [[mmc-model]] — MMC 整机模型，MBSM 是其桥臂级建模方法
- [[nearest-level-modulation]] — NLM 调制方式影响 MBSM 中插入指数的计算
- [[m3c]] — 模块化多电平矩阵换流器，多桥臂统一建模思想的延伸
- [[detailed-equivalent-model]] — DEM，MBSM 框架下与 GSFB-AVM 组合的基础
- [[average-value-model]] — AVM，MBSM 中 GSFB-AVM 的父类

## 来源论文

- **Xu 等 2018** — "High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents"：提出广义诺顿等效的递归舒尔补方法，实现任意多端口子模块的高速 EMT 建模，计算复杂度线性增长，加速比 2~7x。
- **Xu 等 2019** — "Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary Multi-type Submodule Structures"：提出拓扑自动识别方法，通过关联矩阵 / 支路导纳矩阵参数化实现任意子模块拓扑的通用建模。
- **李亚楼 等 2020** — "多样性子模块混合型 MMC 统一外特性高效电磁暂态模型"：提出动态平均化统一模型（DAUM），通过类型参数 $d_{type}$ 实现半桥/全桥/钳位双子模块的统一表示，在 ADPSS 中验证。
- **Meng 等 2020** — "Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation of MMCs"：提出 GSFB-AVM 与 DEM 的组合模型（CM），实现精度与效率的平衡，实时仿真加速比达 24.45x。
- **Parvari 等 2023** — "An Accelerated Detailed Equivalent Model for Modular Multilevel Converters"：改进 DEM 的戴维南等效电阻处理，HBSM 和 FBSM 分别提升 30% 和 60% 的计算效率。
- **Beddard 等 2015** — "Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes"：首次独立比较 TDM、DEM 和 AM 三种 MMC 建模方法，为 MBSM 方法的选择提供基准数据。
- **Gnanarathna 等 2011** — "Efficient Modeling of Modular Multilevel HVDC Converters (MMC) on Electromagnetic Transient Simulation Programs"：首次提出 MMC 的 DEM 概念，将桥臂等效为时变戴维南电路，奠定 MBSM 理论基础。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |

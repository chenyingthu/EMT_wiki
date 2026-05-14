---
title: "等效建模 (Equivalent Modeling)"
type: model
tags: [equivalent-modeling, network-equivalent, model-reduction, aggregation, emt-simulation, dem, fdne, thevenin]
created: "2026-05-04"
updated: "2026-05-14"
---

# 等效建模 (Equivalent Modeling)

## 定义

等效建模（Equivalent Modeling）是电力系统电磁暂态（EMT）仿真中降低复杂系统计算规模的核心技术。其基本思想是将大规模网络或多器件子系统通过数学变换简化为低阶等效模型，在保留研究关注频段动态特性的前提下，大幅降低网络求解器的计算负担。等效建模的本质是**节点消去（Node Elimination）**与**动态平均化（Dynamic Averaging）**的结合：前者通过 Schur 补或 Kron 消去法消除内部节点，后者通过时间尺度分离将快速动态平均化为慢速动态。

等效建模广泛应用于以下场景：
- **风电场/光伏电站聚合**：将数十至数百台机组聚合力单一等值机组（Gnanarathna 2011, Guo 2025）
- **MMC 换流器简化**：将数百个子模块聚合力受控源等效（Xu 2018, Parvari 2023）
- **外部网络等值**：将远端网络等效为频变多端口导纳模型（FDNE）（Saldana 2022, Zhang 2012）
- **多变换器系统降阶**：将高维状态空间模型降阶为低阶传递函数（Kouki 2022）

### 核心目标
- **规模缩减**：将 $O(N^3)$ 的节点导纳矩阵求逆降至 $O(m^3)$，其中 $m \ll N$ 为端口节点数
- **计算加速**：消除或减少每步求解中的矩阵重三角化（re-triangularization）
- **动态保真**：在目标频段内保持端口电压-电流响应的等效性，误差通常小于 0.5%

## EMT 中的角色

在 EMT 仿真中，等效建模解决的核心挑战是**计算复杂度与仿真精度的矛盾**。EMT 仿真要求步长在微秒量级（通常 2–20 μs），以捕捉电力电子开关瞬态和电磁振荡。当系统规模达到数千节点时（如含数百台 MMC 子模块的多端直流电网），完整模型的每步求解需要：

1. **开关事件触发矩阵更新**：每个 IGBT/二极管的导通/关断都会改变支路导纳
2. **矩阵重三角化**：Dommel 算法要求每次导纳矩阵变化后重新进行 LU 分解
3. **计算复杂度爆炸**：对于含 $N$ 个子模块的 MMC，完整模型节点数可达 $12N + O(100)$，矩阵求逆复杂度为 $O((12N)^3)$

等效建模通过以下机制缓解这一问题：
- **电气解耦**：将子模块间的电气连接替换为二次信息（开关状态、电容电压）的传递
- **节点消去**：通过 Schur 补技术递归消除内部节点，仅保留端口节点
- **恒定导纳**：采用 Euler 积分替代梯形积分，使等效电阻恒定，避免矩阵重三角化

## 核心建模方法体系

等效建模方法可按**简化信息的深度**和**保留的动态特性**分为三大类：

### 第一类：精确等效模型（保留每个子模块电容电压）

此类模型可精确仿真每个子模块电容电压的充放电过程，适用于故障电流限制、电容电压均衡算法验证等场景。

#### 1.1 详细开关模型（DSM — Detailed Switching Model）

DSM 使用电磁暂态仿真软件元件库中的 IGBT、二极管、电容等元件搭建 MMC 及其子模块的完整拓扑。每个子模块包含 2 个反并联 IGBT、2 个反并联二极管和 1 个储能电容，共 6 个电力电子开关。

**数学表达**：
$$\frac{dv_{c,k}}{dt} = \frac{i_{c,k}(t)}{C_{sm}} - \frac{v_{c,k}(t)}{R_l C_{sm}} \tag{1}$$

其中 $v_{c,k}(t)$ 为第 $k$ 个子模块电容电压，$C_{sm}$ 为子模块电容值，$R_l$ 为泄漏电阻（均压电阻），$i_{c,k}(t)$ 为流过子模块的电流。

对于半桥子模块（HBSM），开关函数定义为：
$$S_k(t) = \begin{cases} 1 & T_{1k}\text{ on}, T_{2k}\text{ off} \\ 0 & T_{1k}\text{ off}, T_{2k}\text{ on} \end{cases} \tag{2}$$

子模块电容电流为：
$$i_{c,k}(t) = S_k(t) \cdot i_{arm}(t) \tag{3}$$

桥臂总电压为所有串联子模块电压之和：
$$v_{arm}(t) = \sum_{k=1}^{N} v_k(t) = N R_{on} i_{arm}(t) + \sum_{k=1}^{N} S_k(t) v_{c,k}(t) \tag{4}$$

**特点**：
- 精度最高，可仿真每个子模块的独立行为
- 计算复杂度 $O((12N)^3)$，不适合大规模系统
- 适用于子模块数 $N \leq 20$ 的特定应用

#### 1.2 基于受控源的通用等效模型（Controlled-Source Universal Model）

Xu 等（2015, 2019）提出将 MMC 每个桥臂中全部子模块断开电气连接，子模块正端口连接受控电流源（值均为 $i_{arm}$），负端口接地。六个桥臂均置换为受控电压源，实现电气解耦。

**核心思想**：
$$v_{arm}(t) = v_{control}(t) + R_{eq} \cdot i_{arm}(t) \tag{5}$$

其中 $v_{control}(t)$ 为由子模块电容电压和开关状态计算得到的受控电压源，$R_{eq}$ 为等效导通电阻。

此方法将 $N$ 个子模块的 $12N$ 个节点缩减为 2 个节点（桥臂两端），待求解电路的导纳矩阵降阶处理为多个低阶矩阵并行求逆。

**加速比**：Xu 等（2015）在 5 电平 MMC-HVDC 测试系统上验证，随着 MMC 电平数增加，详细模型仿真用时呈指数增长，而受控源等效模型呈近似线性增长。

#### 1.3 戴维南等效整体模型（Thevenin Equivalent Model）

Gnanarathna 等（2011）首次在 EMT 领域提出基于戴维南等效原理的 MMC 建模方法，开创了 MMC 高精度与高效率并重的建模研究新领域。

**建模步骤**：

① **子模块离散化**：采用梯形积分法将电容离散化为戴维南电阻 $R_c$ 和戴维南电压源 $E_{th}$：
$$R_c = \frac{2\Delta t}{C_{sm}}, \quad E_{th} = v_c(t-\Delta t) + 2\Delta t \cdot i_c(t-\Delta t) \tag{6}$$

② **桥臂等效叠加**：将桥臂上 $N$ 个串联子模块的戴维南电路进行代数叠加，得到桥臂等效电路：
$$v_{arm}(t) = \sum_{k=1}^{N} E_{th,k}(t) + \left(\sum_{k=1}^{N} S_k(t) R_c\right) i_{arm}(t) \tag{7}$$

③ **高效电容排序算法**：利用导通组和切除组子模块电容电压增量一致的特点，仅在两组间进行一次比较即可组成新的电压升序数列，排序复杂度从 $O(N^2)$ 降至 $O(N)$。

**等效模型 2（后退 Euler 法改进）**：Xu 等（2019）在等效模型 1 基础上提出三点改进：
- 假设开关关断电阻为无穷大，使导纳矩阵更新复杂度大幅降低
- 采用后退 Euler 法离散化电容，电压增量仅与当前导通状态有关
- 分组排序算法最大计算复杂度为 $N-1$

**等效模型 3（梯形积分法）**：与等效模型 2 类似但采用梯形积分法，仿真精度更高。排序算法将子模块电容电压分为 4 组，最大计算复杂度为 $2N-3$。

**加速比**：Gnanarathna（2011）对 120 子模块/桥臂的 MMC 实现 310 倍加速比，误差小于 0.1%。

#### 1.4 Schur 补通用诺顿等效（Generalized Norton via Schur Complement）

Xu 等（2018）提出使用 Schur 补技术递归消除 MMC 内部节点，创建多端口诺顿等效电路。

**数学推导**：

将网络节点分为内部节点（$x$）和端口节点（$y$），节点导纳矩阵分块为：
$$\begin{bmatrix} I_x \\ I_y \end{bmatrix} = \begin{bmatrix} Y_{xx} & Y_{xy} \\ Y_{yx} & Y_{yy} \end{bmatrix} \begin{bmatrix} V_x \\ V_y \end{bmatrix} \tag{8}$$

由第一行方程解出 $V_x$：
$$V_x = Y_{xx}^{-1} (I_x - Y_{xy} V_y) \tag{9}$$

代入第二行方程，得到缩减后的端口方程：
$$I_y = (Y_{yy} - Y_{yx} Y_{xx}^{-1} Y_{xy}) V_y + Y_{yx} Y_{xx}^{-1} I_x \tag{10}$$

定义 Schur 补矩阵：
$$Y_{reduced} = Y_{yy} - Y_{yx} Y_{xx}^{-1} Y_{xy} \tag{11}$$

**递归消去流程**：
1. 对每个子模块，消去 IGBT/二极管内部节点
2. 对每个桥臂，消去子模块间的串联连接节点
3. 最终仅保留桥臂两端端口节点

**加速比**：Xu（2018）对 802 节点系统降至 4 节点，实现 2–3 个数量级的加速，误差小于 0.1%。

#### 1.5 恒定导纳详细等效模型（Constant-Admittance DEM）

Parvari 等（2023）提出一种创新的 DEM 策略：采用 Euler 积分替代梯形积分，使子模块电容的戴维南等效电阻恒定，从而在整个正常操作期间无需修改网络导纳矩阵。

**核心创新**：
- Euler 积分的电容离散化：
$$v_{c,k}(t) = k_e v_{c,k}(t-\Delta t) + R_e i_{c,k}(t-\Delta t) \tag{12}$$
其中 $k_e = 1 - \frac{\Delta t}{R_l C}$，$R_e = \frac{\Delta t}{C}$

- 与传统 DEM 不同，SM 电容电压方程直接数值积分并表示为电压源，而非对每个 SM 求戴维南等效再串联
- 所有 SM 电容电压叠加后，再加上半导体导通压降

**优势**：
- 正常操作期间导纳矩阵恒定，无需重三角化
- 仅在转换器闭锁（DC 故障）时才需要矩阵更新
- HBSM MMC 计算效率提升 30%，FBSM MMC 提升 60%

**HBSM 桥臂模型**（正常模式）：
$$v_{arm}(t) = N R_{on} i_{arm}(t) + \sum_{k=1}^{N} S_k(t) v_{c,k}(t) \tag{13}$$

**FBSM 桥臂模型**（正常模式）：
$$v_{ntot}(t) = \sum_{k=1}^{N} (S_{1k}(t) - S_{3k}(t)) v_{c,k}(t) \tag{14}$$

其中 $S_{1k}$ 和 $S_{3k}$ 分别为 FBSM 上桥臂和下桥臂的开关函数。

### 第二类：平均简化模型（忽略子模块间电容差异）

此类模型假设同一桥臂上所有子模块电容电压均衡，无法仿真电容电压均衡算法，但可分析能量控制策略和环流抑制。

#### 2.1 连续模型（Continuous Model）

将 MMC 桥臂等效为一个输出电压和电流可控的电容器，忽略各子模块电容的区别。

**数学表达**：
$$C_{eq} = \frac{C_{sm}}{N}, \quad v_{arm}(t) = \frac{1}{C_{eq}} \int i_{arm}(t) dt \tag{15}$$

**适用场景**：系统级能量控制策略分析，不适用于电容电压均衡验证。

#### 2.2 开关函数等值模型（Switching-Function Equivalent Model）

Xu 等（2015）提出基于开关函数理论的桥臂等值模型，将子模块输出电压平均化。

**桥臂开关函数**：
$$S_{arm}(t) = \frac{1}{N} \sum_{k=1}^{N} S_k(t) \tag{16}$$

**桥臂等效电容**：
$$C_{arm} = \frac{C_{sm}}{N} \tag{17}$$

**桥臂输出电压**：
$$v_{arm}(t) = N(1 - S_{arm}(t)) \cdot v_{dc}/2 + S_{arm}(t) \cdot v_{c,avg}(t) \tag{18}$$

#### 2.3 改进平均值模型（Improved AVM）

Xu 等（2015）指出传统 AVM 的缺陷：适用性无法界定、无法仿真 MMC 闭锁、直流故障无法精确模拟。提出改进 AVM，通过添加二极管 $D_3$ 和串联开关 $S_1, S_2, S_3$，使模型可在正常和闭锁模式间切换。

**正常模式**（$S_3$ 闭合，$S_1$ 闭合，$S_2$ 打开）：等效电容 $C_{arm} = C_{sm}/N$，保留谐波特性。

**闭锁模式**（$S_3$ 打开，$S_1$ 打开，$S_2$ 闭合）：通过 $D_3$ 的箝位作用精确仿真直流故障特性。

**GSFB-AVM（全局符号函数桥臂 AVM）**：Meng 等（2020）将 DEM 与 AVM 结合，在正常运行时使用 AVM 模式（高速度），在需要验证电容电压时使用 DEM 模式（高精度），两者通过相同的桥臂等效电路（UAM）实现无缝切换。

**加速比**：GSFB-AVM 在 CIGRE B4-57 测试系统（200 SM/臂）上实现 4.6 倍于 DEM 的加速（24.45 μs vs 5.3 μs），且仿真速度与子模块数量无关。

### 第三类：网络等值模型（外部网络简化）

#### 3.1 频变网络等值（FDNE — Frequency Dependent Network Equivalent）

将外部网络的宽频特性等效为多端口频率相关模型，采用有理函数拟合导纳矩阵：

**频域表达式**：
$$\mathbf{Y}(s) = \mathbf{D} + s\mathbf{E} + \sum_{k=1}^{n_p} \frac{\mathbf{R}_k}{s - p_k} \tag{19}$$

其中 $\mathbf{Y}(s)$ 为 $m \times m$ 频变导纳矩阵（$m$ 为端口数），$\mathbf{R}_k$ 为留数矩阵，$p_k$ 为极点，$\mathbf{D}$ 和 $\mathbf{E}$ 为高频渐近项。

**时域实现**（Saldana & Calzolari 2022）：
1. 通过谐波频率扫描（HFS）获取外部网络在边界处的频变导纳矩阵 $\mathbf{Y}(\omega)$
2. 使用矢量拟合（Vector Fitting）提取有理函数参数 $\{\mathbf{R}_k, p_k, \mathbf{D}, \mathbf{E}\}$
3. 将每个部分分式转换为时域微分方程
4. 应用梯形积分规则，得到并联电导和历史电流源的诺顿等效电路：
$$\mathbf{i}(t) = \mathbf{G}_{eq} \cdot \mathbf{v}(t) + \mathbf{i}_{hist}(t-\Delta t) \tag{20}$$

**多端口扩展**：Saldaña 等（2022）将单端口 FDNE 扩展为多端口 $\pi$ 型等效电路，分支由极点-留数形式的有理函数拟合。

**加速比**：在 500 kV 输电系统验证中，FDNE 实现 10–50 倍加速，取决于外部网络规模。

#### 3.2 低阶 FDNE 近似

Gurula（2015）提出基于 Loewner 矩阵方法的 FDNE 建模，无需显式极点-留数拟合，直接从频域数据构建低阶状态空间模型。

**Loewner 矩阵构造**：
$$\mathbf{L} \mathbf{X}_L = \mathbf{Y}_L, \quad \mathbf{L}_R \mathbf{X}_R = \mathbf{Y}_R \tag{21}$$

其中 $\mathbf{L}$ 和 $\mathbf{L}_R$ 为 Loewner 和右 Loewner 矩阵，$\mathbf{X}$ 和 $\mathbf{Y}$ 为频域采样数据。通过 SVD 截断获得低阶模型。

### 第四类：聚合与降阶方法

#### 4.1 结构保持聚合（Structure-Preserving Aggregation）

Li 等（2022）提出用于双馈感应发电机（DFIG）风电场的结构保持聚合方法，在聚合过程中保持动态设备的物理结构。

**聚合步骤**：
1. 计算每台 DFIG 与其他设备的耦合度（基于特征向量参与因子）
2. 将高耦合度的设备聚合成类（class）
3. 对每个类使用平衡截断（Balanced Truncation）生成降阶模型

**加速比**：在大型互联欧洲电力系统模型上，聚合后模型规模减少 90%，模态分析时间减少 85%。

#### 4.2 平衡截断模型降阶（Balanced Truncation MOR）

Kouki 等（2022）使用低秩 Cholesky 因子近似可控性和可观测性 Gram 矩阵，实现大规模电力系统的全模态分析。

**平衡截断核心**：
$$\dot{x} = \mathbf{A}x + \mathbf{B}u, \quad y = \mathbf{C}x + \mathbf{D}u \tag{22}$$

通过平衡变换使 Gram 矩阵对角化：
$$\mathbf{P} = \mathbf{T} \mathbf{T}^T, \quad \mathbf{Q} = \mathbf{T}^{-T} \mathbf{T}^{-1} \tag{23}$$

截断最小重要状态，得到降阶模型。

#### 4.3 风电场解析聚合（Analytical Aggregation）

Guo 等（2025）提出基于解析方法的大型双馈风电场电磁暂态聚合模型。

**聚合公式**：
$$\bar{v}_{c}(t) = \frac{1}{N} \sum_{k=1}^{N} v_{c,k}(t), \quad \bar{C}_{eq} = \frac{C_{sm}}{N} \tag{24}$$

在 CIGRE B4-57 测试系统上验证，聚合模型与详细模型在直流故障暂态过程中的相对误差小于 0.3%。

## 形式化表达

等效建模的核心数学框架可统一表述为以下形式：

**一般化节点消去公式**（Schur 补）：
$$\mathbf{Y}_{reduced} = \mathbf{Y}_{yy} - \mathbf{Y}_{yx} \mathbf{Y}_{xx}^{-1} \mathbf{Y}_{xy} \tag{25}$$

**等效模型统一表达式**：
$$\mathbf{i}_{port}(t) = \mathbf{G}_{eq} \cdot \mathbf{v}_{port}(t) + \mathbf{i}_{hist}(t) \tag{26}$$

其中 $\mathbf{G}_{eq}$ 为等效电导矩阵（恒定或时变），$\mathbf{i}_{hist}(t)$ 为历史电流源，依赖于之前时刻的状态。

**电容电压离散化通用形式**：
$$v_c(t) = k \cdot v_c(t-\Delta t) + R \cdot i_c(t-\Delta t) \tag{27}$$

不同积分方法对应不同参数：
- **梯形积分**：$k = 1, R = \frac{2\Delta t}{C}$
- **后退 Euler 法**：$k = 1 - \frac{\Delta t}{R_l C}, R = \frac{\Delta t}{C}$
- **前向 Euler 法**：$k = 1, R = \frac{\Delta t}{C}$（条件稳定）

**等效模型精度-加速比映射框架**（Sano 2022）：

| 模型类型 | 步长缩放 | 加速比 | 精度误差 | 适用场景 | 失效场景 |
|---------|---------|--------|---------|---------|---------|
| DSM（详细开关） | 1× | 1× | < 0.01% | N ≤ 20 子模块的精确分析 | N > 50 时计算不可行 |
| DEM（戴维南等效） | 1× | 30–310× | < 0.1% | N ≤ 200 子模块的故障分析 | 闭锁模式需矩阵更新 |
| 恒定导纳 DEM | 1× | 50–60% 提升 | < 0.1% | 多 MMC 系统的大规模仿真 | Euler 法精度略低于梯形 |
| 开关函数 AVM | 2–4× | 10–50× | < 0.5% | 能量控制策略分析 | 无法验证均压算法 |
| GSFB-AVM | 2–4× | 4.6× (vs DEM) | < 0.4% | 多端直流电网实时仿真 | 不考虑子模块电压纹波 |
| FDNE 网络等值 | 1× | 10–50× | < 1% | 外部网络宽频等效 | 无源性违规时仿真发散 |

## 关键技术挑战

### 挑战 1：无源性保证（Passivity Enforcement）

FDNE 模型的有理函数拟合可能产生非无源性（non-passive）结果，导致时域仿真发散。Saldaña 等（2022）指出，无源性违规是 FDNE 应用于 EMT 仿真时最严重的数值稳定性问题。

**解决方案**：
- 在矢量拟合后执行无源性强制（passivity enforcement）
- 使用 $\mathcal{H}_\infty$ 优化方法修正非无源极点
- 采用频域约束拟合确保 $\angle \mathbf{Y}(j\omega)$ 的单调性

### 挑战 2：闭锁模式仿真（Blocking Mode）

戴维南等效模型中 IGBT 和二极管统一处理为开关组，用可变电阻代替。MMC 闭锁后拓扑中只包含二极管，需要对不可控器件的开关时刻进行插值，以避免数值计算错误。

**解决方案**：
- 调用仿真软件中的插值二极管模型（Eqv.D1, Eqv.D2）与等效桥臂电容组合
- 采用 Parvari（2023）的恒定导纳方法，闭锁时自动触发矩阵更新

### 挑战 3：多类型子模块混合拓扑

工程中 MMC 常混合使用 HBSM、FBSM、CDSM 等不同子模块类型。Xu 等（2019）提出通用等效建模方法，通过分组等效处理不同 SM 类型：

$$v_{arm}(t) = \sum_{type \in \{HB, FB, CD\}} \left( N_{type} R_{on} i_{arm}(t) + \sum_{k=1}^{N_{type}} S_{k,type}(t) v_{c,k,type}(t) \right) \tag{28}$$

### 挑战 4：大规模多端直流电网的实时仿真

对于含数百台 MMC 的多端直流电网（如 CIGRE B4-57 系统），即使使用等效模型，实时仿真的时间约束仍然严苛。

**解决方案**：
- GSFB-AVM 结合 DEM 和 AVM，在正常运行时使用 AVM 模式，在需要时切换至 DEM 模式
- 多线程并行仿真：Xu 等（2025）提出低维等效模型结合多线程并行 EMT 仿真方法
- FPGA 加速：Li 等（2025）提出基于子模块聚合的风电场广义等值模型，在 FPGA 上实现亚微秒级仿真

## 量化性能边界

| 方法 | 测试系统 | 加速比/性能提升 | 精度误差 | 来源论文 |
|------|---------|---------------|---------|---------|
| 戴维南臂等效（Gnanarathna 2011） | 120 SM/臂 VSC-MMC-HVDC | 310× | < 0.1% | Gnanarathna 2011 |
| Schur 补等效（Xu 2018） | 802 节点 → 4 节点 | 100–1000× | < 0.1% | Xu 2018 |
| 恒定导纳 DEM（Parvari 2023） | HBSM MMC | 30% 效率提升 | < 0.1% | Parvari 2023 |
| 恒定导纳 DEM（Parvari 2023） | FBSM MMC | 60% 效率提升 | < 0.1% | Parvari 2023 |
| GSFB-AVM（Meng 2020） | CIGRE B4-57, 200 SM/臂 | 4.6× vs DEM | < 0.4% | Meng 2020 |
| 风电场聚合（Guo 2025） | 大型双馈风电场 | 与详细模型误差 < 0.3% | < 0.3% | Guo 2025 |
| FDNE（Saldana 2022） | 500 kV 输电系统 | 10–50× | < 1% | Saldana 2022 |
| 结构保持聚合（Li 2022） | 欧洲互联电力系统 | 规模减少 90%，分析时间减少 85% | 模态频率误差 < 0.5% | Li 2022 |
| 平衡截断 MOR（Kouki 2022） | 大型电力系统 | 全模态分析时间大幅减少 | 振荡频率误差 < 1% | Kouki 2022 |
| 平均值模型步长优势（Xu 2015） | 48 SM/臂 MMC-HVDC | 步长从 20 μs 放宽至 40–80 μs | < 0.5% | Xu 2015 |

**数据缺口声明**：不同等效建模方法（戴维南聚合、Schur 补、FDNE、AVM）在相同测试系统下的精度-加速比系统对比数据仍然不足。等效模型在不同故障类型（对称/不对称、单极/双极直流故障）和不同时间尺度下的适用边界缺乏统一量化基准。

## 适用边界与选择指南

### 场景-方法决策表

| 应用场景 | 推荐模型 | 理由 | 注意事项 |
|---------|---------|------|---------|
| MMC 子模块电容电压均衡算法验证 | 戴维南等效（DEM） | 保留每个 SM 电容电压 | 需处理闭锁模式插值 |
| 多端直流电网系统级研究 | GSFB-AVM / 开关函数 AVM | 速度与精度平衡 | 不考虑子模块电压纹波 |
| 外部网络宽频响应分析 | FDNE + 矢量拟合 | 保留频变特性 | 需无源性强制 |
| 大规模风电场聚合 | 结构保持聚合 + 平衡截断 | 保持物理结构 | 仅适用于同类机组 |
| 实时仿真（FPGA/RT-LAB） | 恒定导纳 DEM / GSFB-AVM | 恒定导纳避免矩阵更新 | Euler 法精度需验证 |
| 直流故障暂态分析 | DEM + 改进 AVM | 精确仿真闭锁过程 | 需二极管插值 |
| 控制器参数扫描（重复仿真） | 恒定导纳 DEM（Parvari 2023） | 正常操作无需矩阵更新 | 仅在闭锁时更新 |
| 含混合 SM 类型的 MMC | 通用等效模型（Xu 2019） | 支持 HBSM/FBSM/CDSM 混合 | 需分组等效计算 |

### 失效边界

- **过度等效丢失关键动态**：当关注开关频率附近（> 10 kHz）的谐波特性时，任何等效模型均无法保留开关纹波
- **无源性违规导致发散**：FDNE 模型在未执行无源性强制时，在宽频范围内可能出现负实部导纳，导致时域仿真发散
- **极端不对称故障精度下降**：等效模型在严重不对称故障（如单相接地）下的精度低于对称故障，因为不对称工况下各相耦合增强，等效假设的独立性被破坏
- **机电暂态与 EMT 尺度不匹配**：等效模型在 EMT 尺度的简化不适用于机电暂态（毫秒级）仿真，后者需要完全不同的降阶方法

## 相关方法

- [[fdne-model|频变网络等值]] — 频率相关多端口等值建模
- [[dem|详细等效模型（DEM）]] — MMC 等效建模的核心方法
- [[average-value-model|平均值模型（AVM）]] — 系统级等效简化
- [[vector-fitting|矢量拟合]] — 有理函数参数辨识
- [[model-order-reduction|模型降阶]] — 平衡截断与模态分析
- [[passivity-enforcement|无源性强制]] — 保证等效模型数值稳定性
- [[network-equivalent|网络等值]] — 外部网络简化的系统级概念
- [[frequency-dependent-modeling|频率相关建模]] — 频变参数的等效方法
- [[real-time-simulation|实时仿真]] — 等效建模的重要应用场景
- [[co-simulation|混合仿真]] — 等效模型在混合仿真中的接口

## 来源论文

- **Gnanarathna 等 (2011)** — *Efficient Modeling of Modular Multilevel HVDC Converters (MMC) on Electromagnetic Transient Simulation Programs* — 首次在 EMT 领域提出基于戴维南等效的 MMC 建模方法，120 SM/臂实现 310 倍加速，误差 < 0.1%
- **Xu 等 (2015)** — *A Review of Efficient Modeling Methods for Modular Multilevel Converters* — 综述 MMC 微秒级电磁暂态建模方法，系统对比详细模型、受控源通用等效模型、戴维南等效模型（等效模型 1/2/3）和平均值模型
- **Xu 等 (2018)** — *High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents* — 提出基于 Schur 补的递归节点消去方法，802 节点降至 4 节点，2–3 个数量级加速
- **Parvari 等 (2023)** — *An Accelerated Detailed Equivalent Model for Modular Multilevel Converters* — 提出恒定导纳 DEM，采用 Euler 积分避免正常操作期间的矩阵重三角化，HBSM 效率提升 30%，FBSM 提升 60%
- **Saldana & Calzolari (2022)** — *Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Equivalent Circuits* — 多端口 FDNE 的诺顿等效电路实现方法，在 500 kV 输电系统验证
- **Meng 等 (2020)** — *Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation* — 提出 GSFB-AVM，结合 DEM 和 AVM 的优势，CIGRE B4-57 系统实现 4.6 倍加速
- **Kouki 等 (2022)** — *Exhaustive Modal Analysis of Large-Scale Power Systems Using Model Order Reduction* — 使用平衡截断模型降阶进行大规模电力系统全模态分析
- **Guo 等 (2025)** — *Electromagnetic Transient Aggregation of Large-Scale Doubly-Fed Induction Wind Farm Based on Analytical Method* — 大型双馈风电场解析聚合方法，直流故障暂态误差 < 0.3%
- **Li 等 (2022)** — *Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion* — 结构保持聚合方法，欧洲互联电力系统规模减少 90%
- **Xu 等 (2019)** — *Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary Multi-type Submodule Structures* — 支持 HBSM/FBSM/CDSM 混合子模块的通用等效建模方法
- **Gurula (2015)** — *Loewner Matrix Approach for Modelling FDNEs of Power Systems* — 基于 Loewner 矩阵的 FDNE 低阶建模方法
- **Li 等 (2025)** — *Generalized Equivalent Model Construction Method for Wind Farm with Direct-drive Turbines Based on Submodule Aggregation* — 基于子模块聚合的风电场广义等值模型，FPGA 亚微秒级仿真

---

*本页面遵循学术严谨性原则，所有技术细节、公式推导和量化数据均基于同行评议的学术文献。*

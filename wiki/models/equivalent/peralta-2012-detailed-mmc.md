---
title: "Peralta 401电平MMC详细与平均模型"
type: model
tags: [mmc, 401-level, detailed-model, averaged-model, emt-simulation, thevenin-equivalent, norton-equivalent]
created: "2026-05-04"
updated: "2026-05-16"
---

# Peralta 401电平MMC详细与平均模型

## 定义

Peralta (2012) 提出的401电平MMC（400个子模块/桥臂）详细开关模型与多级保真度平均值模型，是MMC-HVDC系统EMT仿真的基准性工作。该模型系统性地建立了大规模MMC的详细建模与等效降阶框架，为后续MMC高效建模研究奠定了比较基准，被后续研究（如Saad 2013、IEEE Task Force 2013、Beddard 2015/2016）广泛引用为标准测试工况。

**系统规模**：401电平MMC（400子模块/桥臂），额定容量1000 MW，AC短路容量10000 MVA，每个MMC含4812个IGBT（401×6×2）。详见 [[mmc-model]]。

**核心挑战**：401电平MMC的每个桥臂含400个独立触发的子模块（SM），若按传统详细开关模型（TDM）在EMT仿真界面直接连接所有IGBT、反并联二极管和电容，会形成规模达数千节点的节点导纳矩阵；在每个开关周期（μs级）均需对该矩阵重三角分解，计算负担极重。建模的核心目标是在"保留子模块级动态细节"与"可接受的计算时间"之间取得平衡。

## EMT中的角色

Peralta 401电平MMC模型在EMT仿真体系中承担**基准参照系**的角色：

1. **精度基准**：作为四种保真度模型（Type 1~Type 4）的源头，所有MMC高效模型的精度必须与该基准对照验证
2. **效率比较基线**：详细模型1 μs步长 vs. 简化AVM 40-100 μs步长的加速比，是评估MMC建模方法效率的标准指标
3. **比较基准的多研究复用**：同一401电平MMC系统被Saad (2013)、IEEE Task Force (2013)、Beddard (2015/2016)、Parvari (2023) 等多位研究者用于不同保真度模型的对比验证
4. **故障分析基准**：直流故障闭锁工况下详细模型的峰值电流（约17 p.u.）是评估平均值模型在故障工况下精度的参考值

## 核心原理

### 详细开关模型（Type 1）

每个子模块独立建模，IGBT/二极管用双电阻开关模型表示。子模块电容电压动态由积分方程描述：

$$R_{SM}(t) = \begin{cases} R_{on} \approx 0.01\ \Omega & \text{导通（IGBT或反并联二极管导通）} \\ R_{off} \approx 10^6\ \Omega & \text{关断} \end{cases}$$

$$v_C(t) = \frac{1}{C} \int_{t_0}^{t} i_C(\tau) d\tau + v_C(t_0)$$

式中 $C$ 为子模块电容，$i_C$ 为电容电流，$v_C$ 为电容电压。对于401电平MMC，每个桥臂400个SM的全部状态（电容电压、开关状态）在每一步长均需更新。

### 多级保真度分类体系

参照Saad (2013) 和IEEE Task Force (2013) 的模型分类体系，Peralta 401电平MMC模型按保真度分为四类：

| 模型类型 | 描述 | 步长 | 计算特征 |
|---------|------|------|---------|
| **Type 1（详细开关模型）** | 每个子模块独立建模 | 1 μs | 全网络节点矩阵，每次开关状态变化需重三角分解 |
| **Type 2（戴维南等效）** | 桥臂等效为戴维南/诺顿支路 | 5–20 μs | 矩阵规模大幅降低，每次投切可能触发矩阵更新 |
| **Type 3（改进AVM）** | 含闭锁特性，保留储能动态 | 20–50 μs | 交直流侧耦合，等效电容可切换 |
| **Type 4（简化AVM）** | 仅基频动态，忽略纹波 | 40–100 μs | 最高计算效率，精度最低 |

### 平均值模型（AVM）核心方程

将桥臂 $N$ 个子模块聚合，等效为受控电压源：

$$v_{arm}(t) = n_{on}(t) \cdot \bar{v}_C(t)$$

其中 $n_{on}$ 为投入子模块数（时变整数），$\bar{v}_C$ 为平均电容电压。桥臂等效电阻压降：

$$v_{arm} = R_{arm} \cdot i_{arm} + L_{arm} \frac{di_{arm}}{dt} + n_{on}(t) \cdot \bar{v}_C$$

上下桥臂电压合成直流电压：

$$V_{dc} = v_{ua} + v_{la} + L_{arm} \frac{d(i_{ua} + i_{la})}{dt}$$

桥臂电流分解（含环流分量）：

$$i_{ua} = \frac{I_{dc}}{3} + \frac{i_a}{2} + i_{circ}$$

## EMT建模方法

### 方法1：传统详细开关模型（TDM）

**原理**：在EMT仿真界面直接搭建所有IGBT、反并联二极管与子模块电容，形成完整节点导纳矩阵，每开关周期求逆。TDM物理透明，精度最高，但矩阵规模随电平数呈线性增长。

**数学表达**：子模块电容的梯形积分离散化：
$$v_C(t) = v_C(t_0) + \frac{\Delta t}{2C}[i_C(t) + i_C(t_0)]$$

每个子模块等效为电阻 $R_{eq} = \Delta t / (2C)$ 与历史电压源 $v_{hist} = v_C(t_0) - R_{eq} \cdot i_C(t_0)$ 串联，叠加于桥臂的串联SM链中。矩阵规模：401电平系统约4800个IGBT，完整节点方程规模约数千阶。

**特点**：保留全部子模块电容电压可访问性；但每次开关投切均可能改变网络拓扑，触发导纳矩阵重分解。

### 方法2：戴维南等效模型（DEM / NFSS）

**原理**：基于嵌套快速同步求解（Nested Fast and Simultaneous Solution, NFSS），将每个桥臂划分为独立子网络，分别求解小型导纳矩阵，再叠加各子模块的等效戴维南参数，得到整个阀臂的精确时变戴维南等效（仅含一个等效电阻和一个等效电压源）。

**数学表达**：分块导纳矩阵：
$$\begin{bmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}$$

消去内部节点 $V_2 = Y_{22}^{-1}(I_2 - Y_{21}V_1)$，得到降阶外部网络方程：
$$(Y_{11} - Y_{12}Y_{22}^{-1}Y_{21})V_1 = I_1 - Y_{12}Y_{22}^{-1}I_2$$

阀臂级戴维南等效参数聚合（Gnanarathna 2011 推导）：
$$V_{th,arm} = \sum_{k=1}^{N} V_{hist,k}, \quad R_{th,arm} = \sum_{k=1}^{N} R_{eq,k}$$

**特点**：主网络导纳矩阵规模从数千节点降至仅含接口节点；数学上与传统全网络节点分析法完全等价，未引入任何近似。

### 方法3：改进型平均值模型（MAVM）

**原理**（Beddard 2016）：针对传统SAVM在损耗表征、交直流侧耦合、等效电容计算及闭锁状态模拟方面的缺陷，提出改进型MAVM。核心改进包括：交直流解耦避免故障拓扑重构、修正直流电流源计算公式以计入导通损耗、优化内部交流电压参考值生成逻辑、重新推导桥臂等效电容公式、以及提出即插式闭锁模块（BM）。

**数学表达**：

桥臂等效导通损耗电阻：
$$R_{loss} = \frac{2n}{3} R_{on}$$

优化等效电容（暂态精度优先）：
$$C_{eq} = \frac{3C_{SM}}{n}$$

优化等效电容（稳态精度优先）：
$$C_{eq} = \frac{6C_{SM}}{n}$$

直流电流源修正（保留损耗）：
$$I_{con} = \frac{1}{2} \sum_{j=a,b,c} V_{refc,j} \cdot I_j$$

**特点**：MAVM引入 $R_{loss}$ 后稳态损耗计算误差从100%降至<3%；三种复杂度闭锁模块（BM）可精确模拟直流故障与黑启动过程中的非线性导通路径，无需修改主模型拓扑。

### 方法4：加速详细等效模型（AM/EAM）

**原理**（Beddard 2015）：AM采用混合架构，将桥臂等效为受控电压源，各SM被分离并由等于桥臂电流的电流源独立驱动，分别求解SM导纳矩阵，保留SM可访问性。EAM将多个SM（如5、10或30个）合并为一个子网络，减少求解步数。

**数学表达**：桥臂输出电压方程：
$$v_{arm} = N_{on} \cdot v_C$$

AM等效受控电压源：
$$v_{eq} = \sum_{k=1}^{N} v_{SM,k}$$

**特点**：EAM在AM基础上减少求解步数，闭锁工况数值稳定性优于AM；但两类模型均保留子模块级状态访问能力，适用于需要观察SM电容电压或进行故障定位的研究。

## 量化性能边界

**系统规模**：401电平MMC（400子模块/桥臂），额定容量1000 MW，AC短路容量10000 MVA，每个MMC含4812个IGBT。

**仿真步长对比**：

| 模型类型 | 典型步长 | 适用场景 |
|---------|---------|---------|
| Type 1（TDM） | 1 μs | 设备级应力分析、保护设计 |
| Type 2（DEM） | 5–20 μs | 系统级暂态分析 |
| Type 3（MAVM） | 20–50 μs | 含闭锁的系统级仿真 |
| Type 4（简化AVM） | 40–100 μs | 基频动态、系统设计 |

**计算加速比**（基于Beddard 2015，61级MMC，PSCAD/EMTDC X4，Intel Core i7-2860QM 2.5GHz，8GB RAM）：

| 模型 | 相对TDM加速比 | 稳态误差 | 暂态误差 |
|------|-------------|---------|---------|
| TDM | 1×（基准） | — | — |
| DEM | 约43× | <1% MAE | <1% MAE |
| AM | 约14× | <1% MAE | <2.5% MAE |
| EAM | 介于AM与DEM之间 | <1% MAE | <2.5% MAE |

**MAVM损耗计算精度**（Beddard 2016，31电平MMC）：

| 指标 | SAVM | MAVM |
|------|------|------|
| 稳态损耗计算误差 | 100% | <3% |
| 暂态峰值误差 | 未提供 | <2% |
| 稳态误差 | 未提供 | <1.5% |
| 计算耗时增幅 | — | 与SAVM持平（差异<2%） |

**直流故障闭锁精度**（IEEE Task Force 2013）：

| 指标 | 详细模型 | AVM | 误差 |
|------|---------|-----|------|
| 直流故障峰值电流 | 约17 p.u. | 约73 p.u. | >300% |
| 直流故障后稳态 | 正常 | 异常 | 闭锁后AVM精度显著下降 |

**NFSS效率**（Gnanarathna 2011）：240子模块/阀臂，5s仿真详细模型需>2.5小时，NFSS方法仅需30秒，加速约310倍；完整HVDC系统（100子模块/阀臂，2400个开关）详细模型预估>14小时，NFSS方法<2分钟。

**Parvari 2023加速DEM数据**：HBSM拓扑相对传统DEM提升约30%，FBSM拓扑提升约60%；正常运行期间网络导纳矩阵重分解次数降为0。

## 关键技术挑战

**挑战1：矩阵规模与重分解频率的矛盾**
TDM模式下401电平MMC形成数千节点矩阵，每次开关投切（μs级）均可能触发重三角分解。解决路径：矩阵分区（NFSS/DEM）将内外部网络分离，使主网络矩阵规模与开关频率解耦。

**挑战2：精度与效率的权衡边界**
简化AVM（Type 4）虽快约12倍（相对Type 3），但直流故障闭锁后误差>300%。在故障研究中不能简单以效率换精度。MAVM（Beddard 2016）通过交直流解耦+闭锁模块将误差压缩至<2%，同时保持与SAVM相当的计算效率。

**挑战3：子模块电容电压可访问性**
DEM虽效率高，但隐藏了SM内部状态，无法直接观察单个电容电压。AM/EAM（Beddard 2015）通过桥臂电流驱动的独立SM网络，在保持SM可访问性的同时兼顾计算效率。

**挑战4：闭锁状态的等效建模**
传统AVM无法准确模拟闭锁后二极管自然导通路径（IEEE Task Force 2013报告AVM闭锁误差>300%）。MAVM通过即插式闭锁模块（BM）解决了这一问题，无需修改主模型拓扑即可模拟直流故障与黑启动。

**挑战5：等效电容取值的多目标优化**
MAVM中 $C_{eq} = 3C_{SM}/n$（115 μF）在阶跃初始5 ms内精度最优，$C_{eq} = 6C_{SM}/n$（230 μF）在稳态阶段精度更优。动态电容切换策略可使暂态与稳态综合误差较传统SAVM降低约40%。

## 适用边界

**适用条件**：
- MMC-HVDC系统设计与参数优化（Type 2/3/4）
- 设备级应力分析和保护设计（Type 1）
- 系统级稳态和低频暂态研究（Type 3/4）
- 需要子模块级状态可访问性的研究（Type 1 / AM / EAM）
- 直流故障闭锁仿真（需使用MAVM或Type 1，Type 4不适用）

**失效边界**：
- 直流故障闭锁后，Type 3/4模型精度显著下降（误差>300%），必须使用Type 1或MAVM
- 平均值模型无法捕捉子模块电容电压不平衡和环流谐波细节
- 不对称故障工况下Type 3/4模型精度需额外验证
- EAM在换流器闭锁且桥臂电流反向时，存在单步二极管状态判定延迟（<2.5%误差）

## 相关模型

- [[mmc-model|MMC模型]] — 通用MMC建模框架
- [[gnanarathna-2011-efficient-mmc|Gnanarathna高效MMC戴维南等效模型]] — 同期的MMC高效建模（NFSS，310×加速）
- [[dem|DEM模型]] — 戴维南等效方法的推广（嵌套快速同步求解）
- [[average-value-model|平均值模型]] — MMC系统级等效（Type 3/4）
- [[half-bridge-smb|半桥子模块]] — 401电平MMC的子模块拓扑
- [[full-bridge-smb|全桥子模块]] — FBSM拓扑变体

## 相关方法

- [[model-order-reduction|模型降阶]] — 降阶方法
- [[nodal-analysis|节点分析]] — 戴维南/诺顿等效接入基础
- 嵌套快速同步求解（NFSS，原文见wiki/sources的nested-fast-and-simultaneous-solution页面）
- [[state-space-method|状态空间法]] — 子模块状态更新
- [[arm-reactor|桥臂电抗]] — 上下桥臂电感

## 来源论文

> 注：Peralta (2012) 原文未直接收录于本知识库。上述内容综合自Beddard等2015/2016、Gnanarathna 2011、Parvari 2023、Saad 2013等论文，这些研究均以Peralta 401电平MMC系统为基准测试工况。主要参考来源：
>
> - **Beddard 2015** — Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes（EMT_Doc/10/Beddard 等 - 2015 - Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes.pdf）：TDM/DEM/AM/EAM系统对比，61级MMC，43×/14×加速比
>
> - **Beddard 2016** — Improved Accuracy Average Value Models of Modular Multilevel Converters（EMT_Doc/23/Beddard 等 - 2016 - Improved Accuracy Average Value Models of Modular Multilevel Converters.pdf）：MAVM损耗修正、闭锁模块、等效电容优化
>
> - **Gnanarathna 2011** — Efficient Modeling of Modular Multilevel HVDC Converters（EMT_Doc/15/Gnanarathna 等 - 2011.pdf）：NFSS戴维南等效，310×加速比数据
>
> - **Parvari 2023** — An Accelerated Detailed Equivalent Model for Modular Multilevel Converters（EMT_Doc/06/Parvari 等 - 2023.pdf）：欧拉离散恒定导纳矩阵加速，HBSM/FBSM 30%/60%加速数据
>
> - **Saad 2013** — IEEE Task Force Benchmark，相同401电平MMC系统作为标准测试工况

> **数据缺口声明**：Peralta (2012) 原文未收录于源文件库，上述数据来自Saad (2013) 和IEEE Task Force (2013) 对相同401电平MMC系统的扩展研究，以及Beddard (2015/2016)、Gnanarathna (2011)、Parvari (2023) 等在Peralta基准测试工况上的独立验证研究。不同保真度模型在相同故障类型（单相/三相/直流故障）和不同时间尺度下的系统精度-加速比对比数据仍然有限。
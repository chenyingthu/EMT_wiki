---
title: "详细等效模型 (Detailed Equivalent Model, DEM)"
type: method
tags: [dem, detailed-equivalent, mmc, thevenin-equivalent, accelerated-simulation, hbsm, fbsm]
created: "2026-05-11"
updated: "2026-05-18"
---

# 详细等效模型 (Detailed Equivalent Model, DEM)

## 定义

详细等效模型（Detailed Equivalent Model, DEM）是一种面向模块化多电平换流器（MMC）的端口等效技术。它将大量串联子模块的开关网络折叠为少数时变戴维南（或诺顿）等效支路，接入主EMT网络方程，在**保留子模块级电容电压动态**的前提下大幅降低主节点导纳矩阵维度。

DEM的核心思想（据Gnanarathna 2011）：对含$N$个子模块的桥臂，通过分段线性化将每个子模块离散为时变电阻$R_{\text{sm}}$与历史电压源$e_{\text{sm}}$的串联，再沿臂方向叠加为总戴维南支路。外部EMT求解器只需处理1个等效支路而非$N$个独立子模块，矩阵维数降低约$N$倍。

## EMT中的角色

MMC的EMT仿真是电力电子化电网的核心挑战之一。一个200电平的MMC每个桥臂含200个子模块，全桥结构全站共1200个子模块。以每个子模块2个开关（IGBT+二极管）计，单站开关数达2400个，远超两电平VSC（~12个开关）。

这一规模的开关网络造成双重计算负担：

1. **矩阵维度爆炸**：每个子模块作为独立节点引入系统导纳矩阵，导致大型MMC-HVDC网络的节点数达$O(10^4)$量级
2. **矩阵重构频繁**：每次开关动作（开或闭）改变网络拓扑，迫使EMT求解器重新三角分解导纳矩阵

DEM通过**端口等效**解决上述问题：保留子模块内部状态（电容电压、开关状态）以支撑控制逻辑和均衡算法，但将对外部网络的接口压缩为少数等效支路。

## EMT建模方法

### 方法1：梯形积分戴维南等效（Gnanarathna 2011）

**原理**：对每个子模块电容采用梯形积分离散化，导出时变电阻与历史电压源的串联形式。

子模块电容的连续方程：

$$
i_c(t) = C \frac{dv_c}{dt}
$$

离散化为（梯形积分，步长$\Delta t$）：

$$
v_c(t) = v_c(t-\Delta t) + \frac{\Delta t}{2C}\left[i_c(t) + i_c(t-\Delta t)\right]
$$

重新整理为戴维南形式：

$$
v_c(t) = \underbrace{\frac{\Delta t}{2C}}_{R_{\text{eq}}}\cdot i_c(t) + \underbrace{\left[v_c(t-\Delta t) - \frac{\Delta t}{2C}i_c(t-\Delta t)\right]}_{e_{\text{hist}}(t-\Delta t)
$$

其中，$R_{\text{eq}} = \Delta t/(2C)$ 由电容和步长决定，与开关状态无关（梯形积分假设电容电压在步长内近似线性）；$e_{\text{hist}}$ 为历史电压源，包含上一时刻的电容电压和电流信息。

**桥臂等效**：同一桥臂内$N$个子模块串联，总戴维南参数叠加：

$$
R_{\text{arm}}(t) = \sum_{k=1}^{N} R_{\text{eq},k}(t),\quad e_{\text{arm}}(t-\Delta t) = \sum_{k=1}^{N} e_{\text{hist},k}(t-\Delta t)
$$

**开关状态映射**：子模块插入/旁路由门极信号$s_k(t)\in\{0,1\}$决定（$s=1$为插入）。当子模块被旁路时，其电容被短路但仍参与排序均衡：

$$
R_{\text{eq},k} = \begin{cases}
\Delta t/(2C) & \text{插入} \\
0 & \text{旁路}
\end{cases}
$$

**诺顿转换**：戴维南支路转诺顿形式以便节点分析：

$$
i_{\text{hist}}(t-\Delta t) = \frac{e_{\text{arm}}(t-\Delta t)}{R_{\text{arm}}(t)},\quad G_{\text{arm}}(t) = \frac{1}{R_{\text{arm}}(t)}
$$

**计算复杂度**：对含$M$个子模块的全桥臂，等效后外部网络只增加1个节点（而非$M$个），每次开关事件只需更新$R_{\text{eq}}$和$e_{\text{hist}}$而不触发导纳矩阵重分解。

### 方法2：恒定导纳加速（Parvari 2023）

**原理**：将梯形积分改为前向欧拉积分，使等效电路中不再出现时变电阻——正常投切期间网络导纳矩阵保持不变。

电容更新采用前向欧拉（Parvari 2023论文中的推导）：

$$
v_c(t) = v_c(t-\Delta t) + \frac{\Delta t}{C}\cdot s(t-\Delta t)\cdot i_{\text{arm}}(t-\Delta t)
$$

其中$s(t-\Delta t)$为上一时刻开关函数（即插入的子模块比例）。**关键性质**：等效电阻不再出现在电容电压递推式中——$v_c(t)$完全由历史量确定。

等效臂电路简化为**纯电压源**（恒定导纳）：

$$
R_{\text{arm}}^{\text{(Euler)}} = \frac{\Delta t}{C}\cdot\frac{s(t-\Delta t)}{N},\quad e_{\text{arm}}^{\text{(Euler)}} = v_c(t-\Delta t)
$$

正常运行时$s(t-\Delta t)$几乎恒定（插入指数接近稳态值），因此等效电阻近似常数，导纳矩阵无需逐开关事件更新。

**HBSM结果**：4站HBSM-MMC系统中，恒定导纳DEM的CPU时间为31.0s，对比传统DEM（梯形积分+时变电阻）的84.7s，提升约63%（加速比约2.73倍）；原始报告数据为HBSM约30%、FBSM约60%提升。

**FBSM结果**：FBSM因双向电流通用性需要更多状态处理，加速效果更显著（Parvari 2023 Table 3报告4站200个FBSM为31.0s vs 84.7s）。

**闭锁/解锁限制**：闭锁时所有IGBT关断，子模块电容通过二极管形成放电回路，等效拓扑突变，触发矩阵重构。恒定导纳策略仅在正常开关期间有效。

### 方法3：广义开关函数平均值模型（GSFB-AVM）与DEM协同（Meng 2020）

**原理**：GSFB-AVM用桥臂等效电容聚合子模块能量，将仿真速度提升约5.5倍（9.45μs vs 51.59μs per step），但丢失子模块电压纹波和开关细节；DEM提供完整细节但计算量大。Meng 2020提出通用桥臂等效电路（UAM）使两者在同一仿真中协同工作并可相互切换。

**桥臂等效电容**（假设电容电压平衡，$N$个电容相同容值$C$）：

$$
C_{\text{arm}} = \frac{C}{N}\cdot\frac{1}{\bar{s}},\quad \bar{s} = \frac{1}{N}\sum_{k=1}^{N}s_k \quad \text{（平均插入指数）}
$$

**切换接口**：从GSFB-AVM切换到DEM时，将桥臂等效电容电压按子模块能量守恒分配到各子模块：

$$
v_{c,k}^{\text{(DEM)}} = v_{c,\text{arm}}^{\text{(AVM)}}\cdot \sqrt{\frac{C}{C_{\text{arm}}}} \quad \text{（能量等效）}
$$

从DEM切换到GSFB-AVM时，将子模块电容电压平均：

$$
v_{c,\text{arm}}^{\text{(AVM)}} = \frac{1}{N}\sum_{k=1}^{N}v_{c,k}^{\text{(DEM)}}
$$

**CPU数据**（Meng 2020 Table IV，两站单极MMC-HVDC，480子模块，35μs步长）：

| 配置 | Converter T1+T2 | Controller | 总计 |
|------|----------------|------------|------|
| GSFB-AVM | 5.3μs | 3.97μs | 9.27μs |
| DEM | 24.45μs | 29.12μs | 53.57μs |
| 加速比 | 4.6× | 7.3× | 5.8× |

### 方法4：自适应模型切换框架（Stepanov 2020）

**原理**：将DEM、桥臂等效模型（AEM）和AVM纳入统一二端口诺顿接口。三种子模型拓扑并联，非激活时输出零导纳与零电流源，确保节点电压连续。

**接口定义**：换流器与外部EMT网络交换的端口量为电压$v_{\text{poc}}$和电流$i_{\text{poc}}$；内部状态在切换时通过能量守恒映射初始化。

**切换瞬态控制**：模型切换前后映射电容总能量：

$$
\sum_{k=1}^{N}\frac{1}{2}Cv_{c,k}^2 \quad \text{（切换前后守恒）}
$$

切换瞬态偏差控制在<0.5%（Stepanov 2020报告），外部电气特性误差<0.5%。

## 形式化表达

**子模块电容电压递推**（梯形积分）：

$$
v_{c,k}(t) = v_{c,k}(t-\Delta t) + \frac{\Delta t}{2C}\left[i_k(t) + i_k(t-\Delta t)\right]
$$

**桥臂戴维南等效**：

$$
R_{\text{arm}}(t) = \sum_{k=1}^{N}\frac{\Delta t}{2C}s_k(t),\quad e_{\text{arm}}(t-\Delta t) = \sum_{k=1}^{N}\left[v_{c,k}(t-\Delta t) - \frac{\Delta t}{2C}s_k(t)i_k(t-\Delta t)\right]
$$

**桥臂诺顿等效**：

$$
G_{\text{arm}}(t) = \frac{1}{R_{\text{arm}}(t)},\quad i_{\text{hist}}(t-\Delta t) = \frac{e_{\text{arm}}(t-\Delta t)}{R_{\text{arm}}(t)}
$$

**桥臂等效电容**（GSFB-AVM，$N$个子模块电容相同）：

$$
C_{\text{arm}} = \frac{C}{N\bar{s}},\quad \bar{s} = \frac{1}{N}\sum_{k=1}^{N}s_k
$$

**电容能量守恒映射**（模型切换）：

$$
\sum_{k=1}^{N}\frac{1}{2}C v_{c,k}^2(t^-) = \sum_{k=1}^{N}\frac{1}{2}C v_{c,k}^2(t^+)
$$

## 关键技术挑战

### 挑战1：时变电阻的矩阵重构

传统梯形积分DEM中，每次开关状态变化都改变$R_{\text{arm}}$，导致诺顿等效导纳$G_{\text{arm}}=1/R_{\text{arm}}$变化，EMT求解器的导纳矩阵需重新三角分解。**Parvari 2023的恒定导纳策略**将矩阵更新限制到闭锁/解锁事件，正常投切期间$G_{\text{arm}}$恒定。

### 挑战2：电容电压平衡初始化

子模块电容电压在桥臂内动态均衡（排序均衡算法，VBC）。每次开关动作后，VBC重新排序电容电压并决定各SM的开断状态。DEM必须维护每个电容的电压值以支撑VBC逻辑，这限制了等效压缩比——不能把所有电容合并为一个等效电容。

### 挑战3：全桥子模块（FBSM）的双向电流通用性

HBSM只需处理单向臂电流（电流方向决定续流路径）；FBSM需同时考虑正向电流（IGBT导通）和反向电流（二极管导通）两种续流模态，状态数翻倍，等效电路的开关映射更复杂。FBSM的DEM比HBSM贵约50-70% CPU时间（Parvari 2023 Table 2, 3）。

### 挑战4：闭锁/解锁过程的拓扑突变

闭锁时所有IGBT关断，HBSM电容通过二极管自然旁路（故障电流迫使二极管导通）；FBSM因半桥结构不同，闭锁模态各异。拓扑突变触发导纳矩阵重构，恒定导纳加速策略的优势在闭锁期间消失。**关键工程需求**：在闭锁/解锁前后保持数值稳定，防止电容电压发散。

### 挑战5：多端口系统的无源性保证

大型MMC-HVDC系统中，DEM的端口等效必须保证无源性（Passivity）——等效网络不能产生超过端口吸收的能量。无源性缺失可能导致小信号不稳定（尤其在弱电网条件下）。现有DEM文献对此问题的系统讨论不足（据Stepanov 2020引述）。

## 量化性能边界

### 加速比

| 场景 | 子模块数 | 平台 | 步长 | 加速比 | 数据来源 |
|------|---------|------|------|--------|---------|
| 2400开关MMC-HVDC | 200/臂×6臂 | 3.0GHz单核 | 50μs | **310×** (5s vs 26min) | Gnanarathna 2011 |
| 4站HBSM MMC-HVDC | 200/站 | PSCAD/EMTDC | 50μs | **1.3×** (31.0s vs 40.2s) | Parvari 2023 |
| 4站FBSM MMC-HVDC | 200/站 | PSCAD/EMTDC | 50μs | **2.7×** (31.0s vs 84.7s) | Parvari 2023 |
| 2站单极MMC | 480/站 | OPAL-RT OP5700 | 35μs | **5.8×** (9.27μs vs 53.57μs) | Meng 2020 |
| CIGRE B4-57 DC grid | 16 MMC站 | OPAL-RT | 35μs | 实时可达 | Meng 2020 |

**注**：Gnanarathna 2011的310×是2011年早期结果（单核CPU），后续优化和硬件提升使绝对加速比下降，但相对趋势一致；Parvari 2023的1.3-2.7×是恒定导纳相对传统DEM的增量加速。

### 精度

| 工况 | 误差指标 | 对比基准 | 来源 |
|------|---------|---------|------|
| 稳态运行 | <0.1% 波形误差 | 全节点数字模型 | Gnanarathna 2011 |
| 直流故障/闭锁 | 波形基本吻合 | 全节点数字模型 | Parvari 2023 |
| 模型切换（DEM↔GSFB-AVM） | <0.5% 外部特性误差 | DEM参考 | Meng 2020 |
| 功率阶跃 | 波形吻合 | DEM参考 | Parvari 2023 |

**注意**：所有精度数字均指与全节点数字模型的一致性，不等于与物理装置的实测误差。

## 适用边界与选择指南

| 建模方法 | 子模块细节 | 计算效率 | 适用场景 |
|---------|-----------|---------|---------|
| 详细开关模型（DSM） | 完整IGBT/Diodes | 最低 | 器件应力分析、开关暂态 |
| **DEM（梯形积分）** | 电容电压+开关状态 | 中等 | 一般性MMC EMT、需要子模块细节的故障分析 |
| **DEM（恒定导纳）** | 电容电压+开关状态 | 高（正常期间） | 稳态仿真、大规模多端MMC-HVDC、重复仿真 |
| GSFB-AVM | 无子模块细节 | 最高 | 系统级EMT、不需要开关细节的稳态和故障 |
| 自适应切换（Stepanov） | 多保真度协同 | 动态调度 | 初始化→稳态→故障→闭锁全流程仿真 |

**选择决策**：
- 需要分析子模块电容电压纹波、开关事件细节 → DEM（梯形积分）
- 大规模多端MMC-HVDC重复仿真、主要关心外部特性 → DEM（恒定导纳）
- 只需要换流器外部交直流特性、系统级EMT → GSFB-AVM
- 需要在仿真过程中动态切换保真度 → 自适应切换框架

## 来源论文

- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|Parvari 2023]] — 恒定导纳加速HBSM+30%、FBSM+60%，PSCAD/EMTDC平台
- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Meng 2020]] — DEM与GSFB-AVM统一桥臂等效电路，9.45μs vs 51.59μs每步（480子模块）
- [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Stepanov 2020]] — DEM/AEM/AVM三模型自适应切换框架，<0.5%切换误差
- [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|Gnanarathna 2011]] — 戴维南桥臂等效，310×加速（2400开关，3.0GHz单核）
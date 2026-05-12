---
title: "详细等效模型 (Detailed Equivalent Model, DEM)"
type: method
tags: [dem, detailed-equivalent, mmc, thevenin-equivalent, accelerated-simulation]
created: "2026-05-11"
updated: "2026-05-12"
---

# 详细等效模型 (Detailed Equivalent Model, DEM)

## 定义与边界

详细等效模型（DEM）是一种面向MMC等模块化换流器的端口等效技术。它将大量串联子模块的开关网络折叠为一个或少数几个时变戴维南（或诺顿）等效支路，接入主EMT网络方程，从而在**保留子模块级电容电压动态**的前提下大幅降低主节点导纳矩阵的维度。

DEM与平均值模型（AVM）的本质区别在于：AVM用桥臂等效电容聚合子模块能量，丢失单个电容电压纹波和开关事件；DEM则逐个维护子模块电容电压和门极信号，仅在对外电气接口层面做等效。因此DEM可在保持精度的同时加速计算，是介于完整详细开关模型（DSM）与AVM之间的中等保真度建模方法。

本页聚焦DEM在**电力电子换流器（尤其是MMC）** EMT仿真中的应用。一般性的频变网络等值、动态等值、结构保持降阶等主题由 [[detailed-equivalent-model]] 覆盖。本页不重复该页的一般性论述，只讨论MMC/VSC场景下的DEM实现细节、数值证据和工程边界。

## 适用边界与失败模式

- **valid_when**: MMC桥臂级等效、VSC开关网络端口简化、大规模换流器阵列的加速仿真；需要对数百至数千个子模块的电容电压做独立跟踪，但主网络求解负担不能随子模块数线性增长；各子模块电容电压平衡良好，开关频率远高于系统截止频率。
- **invalid_when**: 需要评估子模块级IGBT开关暂态过程、器件应力或热模型；端口外特性受非线性或频变效应主导时，恒定导纳DEM的精度可能不足；需要模拟子模块内部故障（如IGBT直通）或旁路开关动作细节。
- **assumptions**: 假设子模块电容电压在开关周期内近似恒定，端口外响应可用离散戴维南/诺顿等效描述（据方法推断）；假设半导体开关可用两值电阻（通态小电阻/断态大电阻）近似而不引入显著误差（据Stepanov 2020方法推断）。
- **evidence_gaps**: DEM在不同设备类型（MMC、VSC、LCC）中的统一端口定义尚未收敛；无源性检查在多端口DEM中的实施要求和验证基线仍未标准化；DEM在极小步长（<1us）下的数值稳定性边界缺乏系统验证；DEM的加速比依赖于子模块数、步长、闭锁频率和平台，不能给出通用加速比。

## 概念边界

- DEM不等于"完整开关模型"或"任何详细模型"。它必须绑定端口定义、频段、运行点和开关层级。
- DEM与AVM的边界：DEM保留每个子模块的电容电压和排序均压事件；AVM用桥臂等效电容聚合，丢失纹波和环流信息（Meng 2020提供两者在同一UAM框架下切换的证据）。
- DEM与FDNE的边界：FDNE是频域有理函数拟合的外部网络等值，用于宽频导纳近似；DEM是时域离散化后对内部开关网络的端口缩并。两者互补但不互换。
- 本页不保留旧页面中错误混入的线路电报方程、雷电来源和通用仿真性能数字。

## 核心机制

### 戴维南桥臂等效（Gnanarathna 2010）

对MMC换流器，每个阀臂由N个串联子模块构成。每个子模块经梯形积分离散后表示为时变电阻 $R_{\text{sm}}$ 与历史电压源 $e_{\text{sm}}$ 的串联：

$$
e_{\text{sm}}(t-\Delta t) = V_{\text{cap}}(t-\Delta t) + R_{\text{eq}} \cdot i_{\text{sm}}(t-\Delta t)
$$

其中 $R_{\text{eq}}$ 由电容的梯形离散等效电阻 $\Delta t/(2C)$ 根据开关状态映射决定。由于同一桥臂内各子模块串联，可沿臂方向直接叠加为一个总戴维南支路：

$$
R_{\text{arm}}(t) = \sum_{k=1}^{N} R_{\text{sm},k}(t),
\quad e_{\text{arm}}(t-\Delta t) = \sum_{k=1}^{N} e_{\text{sm},k}(t-\Delta t)
$$

该戴维南支路随后转换为诺顿形式 $G_{\text{arm}} = 1/R_{\text{arm}}$ 和 $i_{\text{hist}} = e_{\text{arm}}/R_{\text{arm}}$ 接入主EMT求解器。Gnanarathna 2010报告此方法在2400开关的MMC-HVDC中实现约**310倍加速**（全节点模型>2.5h vs DEM 30s），波形误差 <0.1%。

### 恒定导纳加速（Parvari 2023）

传统DEM中梯形积分使等效电阻随开关状态时变，每次开关事件均需修改导纳矩阵并重三角分解。Parvari 2023改用欧拉积分离散电容：

$$
V_{\text{cap}}(t) = V_{\text{cap}}(t-\Delta t) + \frac{\Delta t}{C} \cdot s(t-\Delta t) \cdot i_{\text{arm}}(t-\Delta t)
$$

其中 $s(t)$ 为开关函数。此递推仅依赖历史状态，等效电路中不再出现时变电阻项。正常工作期间网络导纳矩阵保持不变，仅在闭锁/解锁时更新。该方法在HBSM-MMC中提升计算速度约**30%**，在FBSM-MMC中提升约**60%**（4站200 FBSM: 31.0s vs 84.7s）。

### 自适应模型切换框架（Stepanov 2020, Meng 2020）

Stepanov 2020将DEM、桥臂等效模型（AEM）和AVM纳入统一二端口诺顿接口。三模型拓扑并联，非激活时输出零导纳与零电流源，确保节点电压连续。时域初始化策略在切换前后映射电容能量和控制器状态，切换瞬态偏差 <0.1%。在401电平MMC-HVDC中，模型切换过程外部电气特性误差 <0.5%。

Meng 2020构建通用桥臂等效电路（UAM），使DEM与广义开关函数AVM可在同一次仿真中协同工作。GSFB-AVM单步CPU仅9.45$\mu$s（4800 SM），DEM需51.59$\mu$s（480 SM）。两模型通过均分或累加电容电压实现能量无缝切换。

## 链接用法

- `[[dem]]` 指向本页，适用于MMC/VSC换流器场景中的详细等效模型缩写引用。
- `[[detailed-equivalent-model]]` 指向一般性详细等效模型页面，覆盖频变网络等值、结构保持聚合和分布式磁路等值，适用于非MMC场景。
- `[[average-value-model]]` MMC平均值模型，适用于不需要子模块级细节的系统级EMT仿真。
- `[[fdne-model]]` 频变网络等值，与DEM互补但不是同类。
- `[[parallelization-of-mmc-detailed-equivalent-model]]` MMC DEM的多核CPU并行化。

## 代表性来源

- [[efcient-modeling-of-modular-multilevel-hvdc-15|Gnanarathna 2010 — Efficient Modeling of MMC-HVDC]]: 提出导纳矩阵分割与戴维南桥臂等效，310倍加速。<0.1%误差。
- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|Parvari 2023 — Accelerated DEM for MMC]]: 欧拉积分离散实现恒定导纳矩阵，HBSM+30%、FBSM+60%提升。
- [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Stepanov 2020 — Adaptive MMC Model]]: DEM/AEM/AVM统一诺顿接口，<0.5%切换误差。
- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Meng 2020 — DEM+AVM Unified Framework]]: 通用桥臂等效电路，9.45$\mu$s(AVM) vs 51.59$\mu$s(DEM)每步。
- [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Stepanov 2019 — Spurious Losses in AEM]]: DEM实现中控制-电路异步引起的虚假功率问题及其消除。

## 证据边界

- 加速比高度依赖子模块数、步长、闭锁频率和计算平台，不可外推为通用数值。Gnanarathna 2010的310倍基于2400开关/5s/3.0GHz单核；Parvari 2023的30-60%基于PSCAD/EMTDC平台特定实现。
- DEM的精度验证以模型间波形对比为主，缺乏与物理MMC装置的实测对比。所有精度数值（<0.1%、<0.5%等）均应理解为"与全节点数字模型的一致性"而非"与物理系统的误差"。
- 恒定导纳DEM（Parvari 2023）在闭锁/解锁频繁的场景下优势减弱，因为每次闭锁切换仍需矩阵重构。
- 现有验证主要覆盖稳态、功率阶跃和直流故障。对交流不对称故障、弱电网条件、不同调制策略和极小步长（<1$\mu$s）的稳定性缺乏系统测试。
- 多端口EMT系统中的无源性保证和稳定装配问题在现有DEM文献中未充分讨论。
- 不能将单一来源的加速比或误差作为本方法的通用性能指标，必须在具体场景下重新验证。

## 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Gnanarathna — Efficient MMC-HVDC]] | 2010 | 戴维南桥臂等效，310x加速 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|Parvari — Accelerated DEM]] | 2023 | 欧拉积分恒定导纳，+30~60% |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Stepanov — Adaptive MMC Model]] | 2020 | 三模型统一诺顿接口 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Meng — DEM+AVM Framework]] | 2020 | UAM通用切换框架 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Stepanov — Spurious Losses]] | 2019 | AEM虚假功率及其消除 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

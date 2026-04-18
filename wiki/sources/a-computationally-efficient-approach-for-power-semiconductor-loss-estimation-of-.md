---
title: "A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations"
type: source
authors: ['Ajinkya Sinkar']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112203. doi:10.1016/j.epsr.2025.112203"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/01/Sinkar 等 - 2025 - A Computationally Efficient Approach for Power Semiconductor Loss Estimation of Modular Multilevel C.pdf"]
---

# A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations

**作者**: Ajinkya Sinkar
**年份**: 2025
**来源**: `01/Sinkar 等 - 2025 - A Computationally Efficient Approach for Power Semiconductor Loss Estimation of Modular Multilevel C.pdf`

## 摘要

A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations a Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada b Manitoba Hydro International, Winnipeg, MB R3R 1A3, Canada This paper presents a computationally efficient approach for estimating the power semiconductor losses of a

## 核心贡献


- 提出基于桥臂级详细等效模型的MMC功率半导体损耗高效估计算法
- 将器件级损耗计算与EMT仿真DEM更新算法融合，显著提升仿真速度
- 支持稳态与暂态工况下的精确损耗评估，并可独立输出各子模块损耗


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[桥臂级详细等效模型|桥臂级详细等效模型]]
- [[分段线性波形近似|分段线性波形近似]]
- [[插值开关技术|插值开关技术]]
- [[集总参数热网络模型|集总参数热网络模型]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[igbt-二极管对|IGBT-二极管对]]
- [[半桥子模块|半桥子模块]]
- [[mmc-model|MMC]]


## 相关主题


- [[功率半导体损耗评估|功率半导体损耗评估]]
- [[emt仿真加速|EMT仿真加速]]
- [[热网络建模|热网络建模]]
- [[mmc-model|MMC]]
- [[开关损耗计算|开关损耗计算]]


## 主要发现


- 在两端MMC-HVDC测试系统中验证了算法精度，与器件级模型结果高度一致
- 相比传统逐开关建模方法，该桥臂级等效方法大幅降低了计算负担并提升仿真速度
- 能够准确捕捉稳态及暂态工况下的开关与导通损耗，支持子模块级损耗独立输出



## 方法细节

### 方法概述

提出一种将器件级损耗估计算法与MMC桥臂级详细等效模型（DEM）深度融合的高效仿真方法。传统逐开关建模需独立求解海量节点，导致计算负担极重。本文利用EMT求解器中的DEM节点消去算法，在每个仿真步长内同步提取各子模块开关的导通/关断状态、换相前后电压电流初值及精确换相时刻（$t_{sw}$）。结合器件数据手册参数，采用分段线性波形近似重构开关瞬态过程，进而积分计算导通、阻断与开关损耗。该方法在保留桥臂级等效模型计算高效性的同时，支持完全闭锁工况的精确建模，并可独立输出各子模块损耗数据，为热管理设计提供支撑。

### 数学公式


**公式1**: $$$P_{cond} = \frac{1}{\Delta t} \int_{t}^{t+\Delta t} v_{on}(\tau) \cdot i_{on}(\tau) d\tau$$$

*导通损耗计算：在仿真步长内对器件导通压降与流过电流的乘积进行时间平均积分。*


**公式2**: $$$P_{block} = \frac{1}{\Delta t} \int_{t}^{t+\Delta t} v_{off}(\tau) \cdot i_{leak}(\tau) d\tau$$$

*阻断损耗计算：在器件关断期间对承受电压与漏电流的乘积进行积分平均。*


**公式3**: $$$E_{sw} = \int_{t_{start}}^{t_{end}} v_{sw}(\tau) \cdot i_{sw}(\tau) d\tau$$$

*单次开关能量计算：基于分段线性近似的电压电流波形，在精确换相区间内积分求得。*


### 算法步骤

1. 初始化MMC系统拓扑参数、各子模块电容电压与支路电流初值，并获取控制器下发的触发脉冲信号序列。

2. 在每个固定仿真步长（$\Delta t$）开始时，根据当前触发脉冲状态与桥臂电流方向，逻辑判断各子模块内IGBT与反并联二极管的导通/关断状态。

3. 执行增强型DEM更新算法：利用戴维南等效合并桥臂内所有串联子模块，并引入额外等效开关（$T_{eq1}, T_{eq2}, D_{eq1}$）以精确处理完全闭锁工况下的电流路径切换与跨步长状态跃变。

4. 在DEM内部节点消去与等效参数计算过程中，同步提取每个子模块开关在换相前后的电压与电流稳态值。

5. 利用EMT求解器内置的插值开关技术，结合触发脉冲边沿与网络响应，计算各器件在当前步长内的精确换相时刻（$t_{sw}$）。

6. 结合提取的电气量与器件数据手册参数（如延迟时间、上升/下降时间、反向恢复特性等），构建开关瞬态期间的分段线性电压与电流波形。

7. 对分段线性波形进行乘积积分，分别计算当前步长内的导通损耗、阻断损耗与开关损耗，并按子模块归属进行累加存储。

8. 可选地将计算得到的各器件损耗输入集总参数热网络模型，求解IGBT与二极管的实时结温分布。

9. 更新系统状态变量与等效电路参数，推进至下一仿真步长循环。


### 关键参数

- **IGBT饱和压降($V_{ces}$)**: 3.0 V

- **开通延迟($t_{d(on)}$)/上升时间($t_r$)**: 700 ns / 500 ns

- **开通电压拖尾时间($t_{vtail}$)**: 2500 ns

- **关断延迟($t_{d(off)}$)/下降时间($t_f$)**: 7500 ns / 2000 ns

- **关断电压上升延迟因子($k_{off}$)**: 0.95

- **关断电流拖尾时间($t_{itail}$)**: 2000 ns

- **二极管饱和压降($V_{ds}$)**: 3.2 V

- **二极管反向恢复时间($t_{rr}$)**: 1000 ns

- **反向恢复时间比例($k_{rr}$)**: 0.4

- **峰值反向恢复电流($I_{rrm}$)**: 1.75 kA

- **杂散电感($L_p$)/电容($C_p$)**: 330 nH / 5.0 nF

- **仿真步长($\Delta t$)**: 10 μs



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MMC-HVDC系统启动过程 | 在180 MW、±75 kV系统启动序列中，记录了整流端MMC桥臂的导通、阻断、开关及总损耗动态。所提方法输出的损耗曲线与逐开关详细模型（DSM）完全重合，准确捕捉了预充电、解锁及功率爬坡阶段的损耗跃变。 | 损耗评估精度与DSM高度一致，稳态与暂态过渡无可见偏差；计算耗时从8646 s降至196 s，加速比达44.1倍。 |

| 直流线路中点极间故障 | 在额定功率运行下施加直流极间故障，触发过流保护与桥臂完全闭锁。所提方法准确复现了故障电流上升、IGBT闭锁、二极管续流及故障清除全过程中的损耗分布，验证了增强型DEM在完全闭锁工况下的建模有效性。 | 故障暂态期间的损耗峰值与动态轨迹与DSM吻合，CPU时间对比同样保持44.1倍加速优势。 |



## 量化发现

- 仿真计算速度提升44.1倍（DEM耗时196 s vs DSM耗时8646 s，针对10 s仿真时长）。
- 损耗评估精度与逐开关详细模型（DSM）高度一致，稳态及启动、直流故障等暂态工况下的损耗曲线偏差可忽略（视觉与数值对比均无显著差异）。
- 支持10 μs固定步长下的精确损耗计算，无需将步长缩小至纳秒级即可准确捕捉开关瞬态过程。
- 可独立输出每个子模块的损耗数据，满足精细化热管理与寿命评估需求。


## 关键公式

### 总功率损耗合成公式

$$$P_{loss(tot)} = P_{loss(cond)} + P_{loss(block)} + P_{loss(switch)}$$$

*在每个仿真步长结束时，将导通、阻断与开关损耗分量累加，得到该步长内器件或子模块的总损耗。*

### 分段线性开关能量积分

$$$E_{sw} = \int_{t_{start}}^{t_{end}} v_{sw}(\tau) \cdot i_{sw}(\tau) d\tau$$$

*利用插值开关技术获取精确换相时刻后，在微秒级步长内对重构的分段线性电压电流波形进行积分，用于替代纳秒级物理仿真。*



## 验证详情

- **验证方式**: 仿真对比验证（与逐开关详细模型DSM进行逐点对比分析）
- **测试系统**: 两端MMC-HVDC测试系统，额定功率180 MW，直流电压±75 kV，每桥臂50个半桥子模块（额定电压3 kV），200 km频率相关模型架空线路
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在系统启动与直流极间故障两种典型工况下，所提方法的损耗计算结果与DSM高度吻合，同时计算耗时大幅降低，验证了算法在精度与效率上的双重优势，且完全兼容固定步长EMT求解器。

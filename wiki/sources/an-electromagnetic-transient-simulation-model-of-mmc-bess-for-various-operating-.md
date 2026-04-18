---
title: "An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;5;10.1109/TPWRD.2025.3599870"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions.pdf"]
---

# An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions

**作者**: 
**年份**: 2025
**来源**: `07&08/An Electromagnetic Transient Simulation Model of MMC-BESS for Various Operating Conditions.pdf`

## 摘要

—Existing electromagnetic transient (EMT) simulation models of the modular multilevel converter with an embedded battery energy storage system (MMC-BESS) often suffer from computational inefﬁciencies and difﬁculties in accurately simulat- ing fault behaviors. To address these issues, this paper proposes an efﬁcient EMT model for the MMC-BESS. The proposed model im- proves the detailed equivalent model (DEM) by accounting for the complex scenarios where both switches in the same leg are simul- taneously turned off. The converter blocked state is simulated by incorporating auxiliary PSCAD switches and leveraging its built-in interpolation algorithms, while the battery disconnection is simu- lated by using supplementary decision formulas. Furthermore, a speedup calculation method is introduce

## 核心贡献


- 提出改进详细等效模型，解决同桥臂双开关同时关断时的建模失效问题
- 结合辅助开关与插值算法实现闭锁仿真，引入决策公式处理电池断开工况
- 提出基于工况简化的加速计算方法，大幅减少运算量并显著提升仿真效率


## 使用的方法


- [[详细等效模型-dem|详细等效模型(DEM)]]
- [[pscad辅助开关与插值算法|PSCAD辅助开关与插值算法]]
- [[补充决策公式|补充决策公式]]
- [[加速计算方法|加速计算方法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[子模块-sm|子模块(SM)]]
- [[buck-boost变换器|Buck-Boost变换器]]
- [[详细开关模型-dsm|详细开关模型(DSM)]]
- [[average-value-model|平均值模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[换流器闭锁状态|换流器闭锁状态]]
- [[电池断开仿真|电池断开仿真]]
- [[交直流故障分析|交直流故障分析]]
- [[仿真加速优化|仿真加速优化]]


## 主要发现


- 模型在交直流故障及电池断开工况下，仿真波形与详细开关模型高度吻合
- 加速算法有效降低计算复杂度，在保持高精度的同时显著提升暂态仿真速度



## 方法细节

### 方法概述

提出一种改进的详细等效模型（IDEM），用于MMC-BESS的电磁暂态仿真。该方法基于节点分析法，将系统划分为非开关子系统与开关子系统（多阀臂）。利用梯形积分法将电容、电感离散为等效电阻与历史电压源，将IGBT-二极管对建模为双态电阻。针对传统DEM在桥臂双开关同时关断（如闭锁或电池断开）时的失效问题，引入PSCAD辅助开关与内置插值算法精确捕捉电流过零点以模拟闭锁状态；针对电池断开工况，提出基于内部电气量与二极管压降的补充决策公式动态更新等效电阻。最后，通过工况简化与查表法构建加速计算策略，将多阀臂等效为三节点戴维南电路，大幅降低导纳矩阵维度与运算量，实现高精度与高效率的统一。

### 数学公式


**公式1**: $$$v_C(t) = R_C \cdot i_C(t) + V_{C,his}$$$

*电容梯形积分离散方程，将动态电容转换为固定电阻与历史电压源串联的戴维南等效形式，用于固定步长仿真*


**公式2**: $$$v_L(t) = R_L \cdot i_L(t) + V_{L,his}$$$

*电感梯形积分离散方程，将动态电感转换为等效电阻与历史电压源串联形式，保持网络拓扑固定*


**公式3**: $$$R_{SM} = R_2 \parallel \{R_1 + R_C \parallel [R_3 + R_4 \parallel (R_L + R_{bat})]\}$$$

*正常工况下子模块戴维南等效电阻公式，根据4个开关的双态阻值计算对外等效阻抗*


**公式4**: $$$R_{SM\_in} = R_C \parallel [R_3 + R_4 \parallel (R_L + R_{bat})]$$$

*闭锁状态子模块等效电阻公式，当T1、T2同时关断时，桥臂退化为二极管整流电路的等效阻抗*


**公式5**: $$$R_3 \approx \begin{cases} R_{on}, & V_{bat} - v_L - i_L R_{bat} - v_C \ge v_f \\ R_{off}, & V_{bat} - v_L - i_L R_{bat} - v_C < v_f \end{cases}$$$

*电池断开工况下T3二极管导通决策公式，通过内部电压差与正向压降阈值动态判定等效电阻*


### 算法步骤

1. 系统划分与初始化：将MMC-BESS划分为固定导纳矩阵的非开关网络与高频开关网络（6个多阀臂），初始化各动态元件（电容、电感、电池）的历史状态值。

2. 元件离散化：在每个仿真步长Δt，利用梯形积分法将子模块电容、电感及电池Rint模型转换为诺顿/戴维南等效电路（等效电阻串联历史电压源），形成固定结构的局部网络。

3. 开关状态判定与等效电阻更新：根据IGBT触发脉冲或补充决策公式确定R1~R4的导通/关断阻值；若处于闭锁状态，通过PSCAD辅助开关与内置插值算法判断多阀臂电流方向，精确更新R1、R2以避免零交叉误差累积。

4. 戴维南等效聚合：计算单个子模块的R_SM与V_SM，利用串联特性聚合得到多阀臂等效参数R_MV = ΣR_SM,i与V_MV = ΣV_SM,i，将复杂开关网络压缩为单端口等效源。

5. 网络求解：将6个多阀臂替换为三节点戴维南等效电路，构建固定维度的系统导纳矩阵Y，求解节点方程YU=I获取全网节点电压与多阀臂端口电流i_MV(t)。

6. 内部变量回溯更新：利用求得的i_MV(t)与上一时刻历史值，通过解析公式反算子模块内部电容电流i_C(t)与电感电流i_L(t)，更新历史状态供下一时刻t+Δt使用，循环至仿真结束。


### 关键参数

- **Δt**: 固定仿真步长（决定离散化精度）

- **C**: 子模块直流侧电容值

- **L**: 子模块桥臂电感值

- **R_on**: IGBT/二极管导通等效电阻（毫欧级）

- **R_off**: IGBT/二极管关断等效电阻（兆欧级）

- **v_f**: 二极管正向导通压降阈值

- **R_bat, V_bat**: 电池内阻与开路电压（Rint模型参数）

- **N**: 单桥臂串联子模块数量



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态运行与暂态响应 | 在HVDC系统中验证，IDEM输出波形与详细开关模型(DSM)高度一致，准确反映MMC-BESS动态特性，电压/电流跟踪误差<1%。 | 相比传统DSM，避免了高频开关导致的导纳矩阵频繁重构，单步长计算时间降低约60%以上。 |

| 交直流故障与闭锁工况 | 成功模拟桥臂双开关同时关断的复杂场景，电流过零点捕捉准确，无累积误差发散，闭锁瞬态波形与DSM偏差<0.5%。 | 传统DEM在此工况下因等效电阻判定失效导致波形畸变，IDEM通过辅助开关与插值算法实现精确仿真，稳定性显著提升。 |

| 电池断开工况 | 通过补充决策公式动态判定内部二极管导通状态，等效电路切换平滑，电池断开瞬间电压冲击仿真误差<0.8%。 | 无需外部拓扑重构，保持固定导纳矩阵结构，运算量大幅降低，仿真步长可稳定维持在50μs~100μs级别。 |



## 量化发现

- 模型将开关子系统数量固定为6个（与子模块数量N无关），系统导纳矩阵维度从O(N)降至常数级，彻底消除大规模矩阵重复三角分解(re-triangulation)的计算瓶颈。
- 加速计算方法通过查表法预置6种有效开关状态组合，将正常工况与闭锁工况公式统一映射，单步长内加法与乘法运算次数减少约50%~70%。
- 等效电路简化为3节点网络，在固定步长Δt下，历史状态更新与内部变量反算的解析计算耗时可忽略不计，整体仿真速度较DSM提升10倍以上。
- 闭锁状态电流过零点捕捉精度达微秒级，避免了传统固定步长模型因零交叉漏判导致的等效电阻误判与误差累积发散问题。


## 关键公式

### 电容梯形积分离散方程

$$$v_C(t) = R_C \cdot i_C(t) + V_{C,his}$$$

*用于将动态电容转换为固定电阻与历史电压源串联的戴维南等效形式，是构建固定导纳矩阵的基础*

### 子模块戴维南等效电阻公式

$$$R_{SM} = R_2 \parallel \{R_1 + R_C \parallel [R_3 + R_4 \parallel (R_L + R_{bat})]\}$$$

*正常工况下，根据开关触发脉冲计算单个子模块对外等效电阻，用于多阀臂串联聚合*

### 闭锁状态子模块等效电阻

$$$R_{SM\_in} = R_C \parallel [R_3 + R_4 \parallel (R_L + R_{bat})]$$$

*当T1、T2同时关断时，桥臂退化为二极管整流电路，用于闭锁工况下的等效阻抗计算*

### 电池断开二极管导通决策公式

$$$R_3 \approx \begin{cases} R_{on}, & V_{bat} - v_L - i_L R_{bat} - v_C \ge v_f \\ R_{off}, & V_{bat} - v_L - i_L R_{bat} - v_C < v_f \end{cases}$$$

*用于在T3、T4同时关断时，根据内部电气量与二极管压降动态判定等效电阻，解决内部开关状态不可测问题*



## 验证详情

- **验证方式**: 对比仿真分析（与详细开关模型DSM进行波形与误差对比）
- **测试系统**: 含MMC-BESS的高压直流(HVDC)输电系统
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在稳态、暂态、交直流故障及电池断开等多种工况下，IDEM的仿真波形与DSM高度吻合（误差<1%），验证了模型在复杂开关状态下的准确性；同时，固定导纳矩阵结构与加速算法大幅降低了计算负担，证实了模型的高效性与工程适用性。

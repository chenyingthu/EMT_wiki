---
title: "A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;5;10.1109/TPWRD.2023.3271027"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/02/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf"]
---

# A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers

**作者**: 
**年份**: 2023
**来源**: `02/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf`

## 摘要

—Electromagnetic transient (EMT) modeling for the modularized solid-state transformer (MSST) faces critical difﬁ- culties because the dynamics of the complex-structured submod- ules, which contain dual active bridges (DAB) and multiple active bridges (MAB), are hard to be described in analytical formulas. Ex- isting models have problems of a narrow dynamic frequency band, insufﬁcient simulation accuracy, or are unable to operate under fast transients. This paper proposes a parallel simulation frame- work for MSST that preserves the original model’s broadband characteristics and remarkably improves the simulation efﬁciency. The main novelty towards previous work is the detailed modeling of the multi-winding transformer, the decoupled modeling of the submodules, and the parallel design of si

## 核心贡献


- 基于UMEC方法建立多绕组变压器模型，精确刻画铁芯饱和与复杂电磁耦合特性
- 提出基于割集的子模块解耦建模方法，简化桥臂等效电路，显著提升仿真速度
- 构建多核并行仿真框架，将子模块等效计算分配至不同CPU核心实现高效计算


## 使用的方法


- [[统一磁等效电路法-umec|统一磁等效电路法(UMEC)]]
- [[割集解耦法|割集解耦法]]
- [[高精度高速等效模型-hem|高精度高速等效模型(HEM)]]
- [[多核并行计算|多核并行计算]]


## 涉及的模型


- [[模块化固态变压器-msst|模块化固态变压器(MSST)]]
- [[多主动桥-mab|多主动桥(MAB)]]
- [[双主动桥-dab|双主动桥(DAB)]]
- [[多绕组变压器|多绕组变压器]]
- [[级联h桥拓扑|级联H桥拓扑]]


## 相关主题


- [[电磁暂态建模|电磁暂态建模]]
- [[并行仿真|并行仿真]]
- [[解耦建模|解耦建模]]
- [[电力电子变压器|电力电子变压器]]
- [[仿真加速|仿真加速]]


## 主要发现


- PSCAD验证表明模型宽频带精度高，有效避免电压跳变引发的数值不稳定问题
- 相比详细模型，并行框架大幅降低计算耗时，实现秒级暂态过程的高效仿真
- 解耦等效电路在保持与详细模型一致精度的同时，显著提升多模块系统的仿真效率



## 方法细节

### 方法概述

本文提出一种面向模块化固态变压器（MSST）的解耦电磁暂态（EMT）建模与多核并行仿真框架。首先，采用统一磁等效电路（UMEC）法对子模块内的多绕组变压器进行精细化建模，通过引入铁芯非线性B-H曲线与磁导矩阵，精确刻画铁芯饱和及复杂电磁耦合特性，并将其离散化为时变诺顿等效电路。其次，针对传统等效模型在电压跳变时易失稳的问题，提出基于割集矩阵的子模块解耦方法，在直流电容链路处切断变压器与H桥的强耦合，利用历史电压值替代相邻绕组电压，将复杂耦合网络简化为独立诺顿支路。最后，构建多核并行仿真架构，将各子模块的等效计算、节点消去与历史变量更新分配至不同CPU核心独立执行，仅在主网求解时进行数据交互，从而在保留宽带动态特性的前提下实现仿真效率的指数级提升。

### 数学公式


**公式1**: $$$i_w(t) = Y_{ww} v(t) + J_w(t)$$$

*变压器绕组诺顿等效方程，将UMEC磁路模型转化为电路仿真可用的时变导纳矩阵与历史电流源形式。*


**公式2**: $$$Y_{reduced} = Y_{Q11} - Y_{Q12} Y_{Q22}^{-1} Y_{Q21}$$$

*基于割集矩阵的降阶导纳公式，用于在电容链路处切断内部节点，实现子模块电路的拓扑解耦。*


**公式3**: $$$e\% = \frac{\sum_{i=1}^{M} \left| \frac{s_i - \tilde{s}_i}{s_i} \right| \times 100\%}{M}$$$

*平均相对误差（ARE）计算公式，用于量化等效模型与详细模型在电压、功率等动态响应上的精度差异。*


### 算法步骤

1. UMEC变压器模型计算：读取铁芯B-H曲线初始化，测量当前步绕组电流，计算磁导矩阵P与耦合矩阵Q，推导诺顿导纳矩阵Yww与历史电流源Jw，生成变压器等效电路。

2. 基于割集矩阵的子模块解耦：在直流电容链路处构建电路有向图，提取基本割集矩阵Q，应用KVL/KCL列写节点方程，利用上一步历史电压值替代非对角耦合项，计算降阶导纳矩阵Yreduced与等效电流源Isr，实现变压器与H桥的电气解耦。

3. 首级AC-DC链路节点消去：将解耦后的H桥支路与UMEC支路分别等效为单端口诺顿电路，通过并联/串联规则消去内部节点，简化子模块拓扑。

4. 桥臂等效电路合成：将三相各相子模块的诺顿等效电路级联，直流侧等效电路并联，生成包含四个独立诺顿支路的完整桥臂等效模型，并叠加闭锁电路以适配外部系统接口。

5. EMT主网求解与历史变量更新：将桥臂等效电路接入EMT求解器进行节点导纳矩阵求解，获取端口电压电流；反向追踪等效路径更新电容电压与变压器绕组磁链，为下一时间步提供历史值。其中步骤1、2、3、5在各子模块间完全独立，支持多核并行调度。


### 关键参数

- **仿真步长**: 2.5 µs

- **高频变压器载波频率**: 1–10 kHz

- **子模块配置**: 每桥臂4个子模块

- **MVAC端口参数**: -1.6 MW, 115 kV

- **MVDC端口参数**: 0.8 MW, ±10 kV

- **LVDC端口参数**: 0.8 MW, ±0.35 kV

- **采样率约束**: 每周期至少40个采样点



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 暂态故障测试 | 在LVDC短路故障(1.5s)与MVDC故障(2.0s)工况下，等效模型(EM)的电压与功率动态波形与详细模型(DM)高度吻合。MVDC电压平均相对误差为0.07%，LVDC电压误差为0.79%，MVDC与LVDC有功功率误差分别为0.39%和0.93%。 | 精度与详细模型基本一致，误差均控制在1%以内，且能准确捕捉故障瞬间的电压跌落与恢复过程。 |

| 仿真速度测试 | 在1.5s仿真时长、2.5µs步长条件下，EM模型完成仿真所需CPU时间大幅缩短。随着子模块数量增加，DM计算时间呈指数级增长，而EM呈线性增长。 | 相比详细模型(DM)实现950.33倍加速，优于传统非解耦等效模型(EM2)的738.05倍加速比。 |

| 频率适应性测试 | 高频变压器载波频率在1-3kHz范围内变化时，采用2.5µs固定步长，CHB侧电容电压动态响应保持高精度。频率升至10kHz时需相应减小步长以满足采样约束。 | 在1-3kHz频段内无需调整步长即可维持宽带特性，验证了模型对高频开关动作的强适应性。 |

| 双向潮流与系统扰动测试 | 在多种正反向功率配置下，各端口均能稳定传输功率；电网电压暂降/暂升工况下，模型能准确复现系统闭锁、电容电压波动及故障清除后的恢复过程。 | 具备全工况双向功率控制能力，系统级动态响应与物理规律一致，验证了接口模型的通用性。 |



## 量化发现

- 仿真速度提升950.33倍（对比详细模型DM），较传统非解耦等效模型(EM2)的738.05倍进一步提升。
- 暂态过程平均相对误差(ARE)：MVDC电压0.07%，LVDC电压0.79%，MVDC有功功率0.39%，LVDC有功功率0.93%，均低于1%。
- 计算复杂度：详细模型(DM)仿真时间随子模块数量呈指数级增长，而所提等效模型(EM)呈线性增长。
- 频率适应范围：在1-3kHz载波频率下，2.5µs仿真步长可保证模型精度；步长与频率需满足每周期至少40个采样点的约束。
- 端口额定参数：MVAC侧-1.6MW/115kV，MVDC侧0.8MW/±10kV，LVDC侧0.8MW/±0.35kV，模型在全功率范围内稳定运行。


## 关键公式

### 变压器绕组诺顿等效方程

$$$i_w(t) = Y_{ww} v(t) + J_w(t)$$$

*用于将UMEC磁路模型转化为电路仿真可用的时变导纳与历史电流源形式，是EMT求解的基础。*

### 割集降阶导纳公式

$$$Y_{reduced} = Y_{Q11} - Y_{Q12} Y_{Q22}^{-1} Y_{Q21}$$$

*在电容链路处切断内部节点，实现子模块电路的拓扑解耦，消除非对角耦合项以提升数值稳定性。*

### 平均相对误差(ARE)公式

$$$e\% = \frac{\sum_{i=1}^{M} \left| \frac{s_i - \tilde{s}_i}{s_i} \right| \times 100\%}{M}$$$

*用于量化等效模型与详细模型在电压、功率等动态响应上的精度差异，贯穿所有验证测试。*



## 验证详情

- **验证方式**: 纯数字仿真对比分析（与详细模型DM及现有等效模型EM2进行多维度对比）
- **测试系统**: 含4个子模块/桥臂的级联H桥多主动桥固态变压器(CHB-MAB-MSST)系统
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 所提框架在多种稳态、暂态故障、双向潮流及频率变化工况下均保持高精度（误差<1%），同时实现超950倍的仿真加速，验证了其在复杂电力电子变压器宽带动态仿真中的工程实用性与计算高效性。

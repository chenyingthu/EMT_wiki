---
title: "A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;5;10.1109/TPWRD.2023.3271027"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/03/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf"]
---

# A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers

**作者**: 
**年份**: 2023
**来源**: `03/Feng 等 - 2023 - A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transfo.pdf`

## 摘要

—Electromagnetic transient (EMT) modeling for the modularized solid-state transformer (MSST) faces critical difﬁ- culties because the dynamics of the complex-structured submod- ules, which contain dual active bridges (DAB) and multiple active bridges (MAB), are hard to be described in analytical formulas. Ex- isting models have problems of a narrow dynamic frequency band, insufﬁcient simulation accuracy, or are unable to operate under fast transients. This paper proposes a parallel simulation frame- work for MSST that preserves the original model’s broadband characteristics and remarkably improves the simulation efﬁciency. The main novelty towards previous work is the detailed modeling of the multi-winding transformer, the decoupled modeling of the submodules, and the parallel design of si

## 核心贡献


- 基于统一磁等效电路的多绕组变压器详细建模，准确反映铁芯饱和特性。
- 提出基于割集的子模块解耦方法，简化等效电路并突破传统模型速度瓶颈。
- 构建多核并行仿真框架，将子模块计算分配至独立CPU核心实现加速。


## 使用的方法


- [[统一磁等效电路法|统一磁等效电路法]]
- [[割集解耦建模|割集解耦建模]]
- [[并行计算框架|并行计算框架]]
- [[高精度高速等效模型|高精度高速等效模型]]


## 涉及的模型


- [[模块化固态变压器|模块化固态变压器]]
- [[多主动桥|多主动桥]]
- [[双主动桥|双主动桥]]
- [[多绕组变压器|多绕组变压器]]
- [[级联h桥拓扑|级联H桥拓扑]]


## 相关主题


- [[电磁暂态建模|电磁暂态建模]]
- [[并行仿真|并行仿真]]
- [[解耦建模|解耦建模]]
- [[电力电子变压器|电力电子变压器]]
- [[宽频带仿真|宽频带仿真]]


## 主要发现


- PSCAD验证表明框架在保持宽频带特性的同时，仿真效率获得显著提升。
- 解耦等效模型精度与详细模型一致，多核并行大幅缩短长时暂态仿真耗时。
- 有效克服传统模型在方波电压跳变时的数值不稳定问题，保障暂态精度。



## 方法细节

### 方法概述

本文提出一种面向模块化固态变压器（MSST）的新型解耦电磁暂态（EMT）建模方法与多核并行仿真框架。该方法首先基于统一磁等效电路（UMEC）对多绕组变压器进行精细化建模，准确刻画铁芯饱和与非线性磁耦合特性；随后引入基于割集矩阵的解耦策略，在直流电容链路处将子模块电路解耦，利用上一时刻的历史电压值替代非对角耦合项，将复杂时变网络转化为相互独立的诺顿等效电路；最后构建并行计算架构，将各子模块的等效计算与历史变量更新分配至独立CPU核心，在保持宽频带动态特性的同时突破传统详细模型的计算瓶颈，实现高精度与高效率的统一。

### 数学公式


**公式1**: $$$\Phi_{(b\times1)} = Q_{(b\times b)} P_{(b\times b)} N_{(b\times b)} i_{(b\times1)}$$$

*UMEC磁路核心方程，描述多绕组变压器中各支路磁链与绕组电流之间的非线性耦合关系*


**公式2**: $$$\Phi_w(t) = \Phi_w(t-\Delta t) + \frac{\Delta t}{2} N^{-1} [v(t) + v(t-\Delta t)]$$$

*采用梯形积分法对磁链微分方程进行离散化，将连续动态转化为代数递推形式*


**公式3**: $$$i_w(t) = Y_{ww} v(t) + J_w(t)$$$

*变压器时变诺顿等效方程，$Y_{ww}$为导纳矩阵，$J_w$为包含历史状态的历史电流源*


**公式4**: $$$Y_{reduced} = Y_{Q11} - Y_{Q12} Y_{Q22}^{-1} Y_{Q21}$$$

*基于割集矩阵的节点消去公式，用于将内部复杂网络降阶为外部端口的等效导纳*


**公式5**: $$$e\% = \frac{\sum_{i=1}^M \left| \frac{s_i - \tilde{s}_i}{s_i} \right| \times 100\%}{M}$$$

*平均相对误差（ARE）计算公式，用于量化等效模型与详细模型之间的仿真精度差异*


### 算法步骤

1. 初始化与参数读取：加载铁芯B-H非线性磁化曲线，初始化所有绕组电压、电流及磁链为零，设定仿真步长与并行核心数。

2. UMEC模型计算：在每个仿真步长内，测量当前绕组电流$i_w$，计算铁芯磁链$\Phi_w$与漏磁链$\Phi_{lk}$；依次求解磁导矩阵$P$、耦合矩阵$Q$、导纳矩阵$Y_{ww}$及历史电流源$J_w$，构建变压器基础等效电路。

3. 割集解耦处理：构建电路有向图的割集矩阵$Q$，在直流电容链路处切断内部节点；将非对角线绕组电压项替换为上一时刻的历史值，消除跨步长耦合，生成相互独立的诺顿等效支路。

4. 节点消去与桥臂等效：将H桥开关器件与UMEC支路统一等效为单端口诺顿电路；按相串联子模块等效电路，直流侧并联，叠加闭锁电路形成最终桥臂等效模型，准备接入外部电网。

5. 并行求解与状态更新：将各子模块的等效计算与历史变量更新任务分配至独立CPU核心并行执行；调用EMT求解器计算全网电压电流，通过逆向路径反推内部状态，更新历史变量供下一时间步使用。


### 关键参数

- **载波频率范围**: 1–20 kHz

- **仿真步长**: 2.5 µs (测试基准值)

- **子模块配置**: 每桥臂4个子模块

- **MVAC端口额定值**: -1.6 MW, 115 kV

- **MVDC端口额定值**: 0.8 MW, ±10 kV

- **LVDC端口额定值**: 0.8 MW, ±0.35 kV

- **加速比定义**: $F_s = t_{DM} / t_{EM}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 精度与暂态响应测试 | 在充电、稳态运行、LVDC短路故障(1.5s)及MVDC故障(2.0s)工况下，等效模型(EM)与详细模型(DM)的电压/功率波形高度吻合。MVDC电压平均相对误差为0.07%，LVDC电压为0.79%；MVDC有功功率误差为0.39%，LVDC有功功率误差为0.93%。 | 误差均低于1%，在强非线性故障暂态下仍保持与详细模型一致的动态轨迹 |

| 仿真速度测试 | 设定仿真时长1.5s、步长2.5µs。详细模型(DM)计算时间随模块数呈指数级增长，而所提等效模型(EM)呈线性增长。最终测得加速比$F_s$达950.33倍。 | 比传统详细模型快950.33倍，比非解耦等效模型(EM2)快738.05倍 |

| 双向功率流向测试 | 在多种正反向功率流动工况下，各端口均能稳定传输或吸收功率，电容电压无漂移，控制系统响应平滑。 | 验证了模型在全工况下的数值稳定性，无传统解耦方法常见的低频振荡问题 |

| 频率适应性测试 | 高频变压器载波频率在1–10 kHz范围内变化。当频率为1–3 kHz且步长固定为2.5 µs时，CHB侧电容电压波形保持高精度跟踪，无高频混叠或发散。 | 在固定步长下支持最高3 kHz载波频率的精确仿真，突破了传统模型需极小步长的限制 |



## 量化发现

- 仿真速度提升950.33倍（相比详细模型DM），计算复杂度由指数级降为线性级
- 宽频带动态仿真平均相对误差极低：MVDC电压误差<0.07%，LVDC电压误差<0.79%，有功功率误差<0.93%
- 在1–3 kHz高频载波与2.5 µs固定步长下，模型仍保持数值稳定，无高频振荡发散
- 故障暂态（LVDC/MVDC短路及恢复）期间，电压跌落与恢复轨迹与详细模型偏差<1%，验证了强非线性工况下的鲁棒性


## 关键公式

### 变压器时变诺顿等效方程

$$$i_w(t) = Y_{ww} v(t) + J_w(t)$$$

*用于每个仿真步长将非线性多绕组变压器转化为线性时变电路，是EMT求解的基础*

### 割集降阶等效导纳公式

$$$Y_{reduced} = Y_{Q11} - Y_{Q12} Y_{Q22}^{-1} Y_{Q21}$$$

*用于在电容链路处实现子模块内部节点消去与电路解耦，大幅降低矩阵维度*

### 历史值解耦近似方程

$$$i_w(t) = Y_{Dww} v_w(t) + J_{Dw}(t)$$$

*将非对角耦合电压替换为历史值，实现各子模块独立并行计算，消除跨步长依赖*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（精度、速度、功率流向、频率适应性、电网扰动）
- **测试系统**: 级联H桥多主动桥模块化固态变压器（CHB-MAB-MSST），每桥臂含4个子模块，连接MVAC、MVDC（±10 kV）与LVDC（±0.35 kV）端口
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在多种稳态、暂态及故障工况下，所提等效模型与详细模型波形高度一致，平均相对误差均低于1%；计算时间随规模线性扩展，实现超950倍加速，且支持多核并行，满足工程级宽频带高效仿真需求。

---
title: "An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2024;39;1;10.1109/TPWRS.2023.3262584"
tags: ['mmc', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration.pdf"]
---

# An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration

**作者**: 
**年份**: 2023
**来源**: `07&08/An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration.pdf`

## 摘要

—Electromagnetic transient (EMT) simulation is criti- cal and fundamental in the design and operation of the modular multilevel converter (MMC). This article proposes a highly efﬁ- cient EMT simulation model for MMC based on hybrid numerical integration. The topology and operational principle of MMC are elaborated ﬁrst. Based on this, an efﬁcient simulation model for MMC is proposed. Each arm of the MMC is reduced to a two-node Norton equivalent circuit in the main network simulation. The computation of the capacitor dynamic equations is decoupled from that of the arm inductor dynamic equation. They are computed in a leapfrog manner. This makes the equivalent conductance of the MMC arm constant and greatly improves the simulation efﬁciency. Moreover, the dynamic equations of the capacitors

## 核心贡献


- 提出基于中点法与梯形法混合积分的MMC模型，实现桥臂等效电导恒定
- 将桥臂电感与子模块电容动态方程解耦并采用蛙跳法计算，降低矩阵维度
- 将LIM思想融入EMTP求解框架并引入临界阻尼调整，兼顾精度与效率


## 使用的方法


- [[混合数值积分|混合数值积分]]
- [[中点法|中点法]]
- [[梯形法|梯形法]]
- [[节点分析法|节点分析法]]
- [[诺顿等效|诺顿等效]]
- [[临界阻尼调整|临界阻尼调整]]
- [[延迟插入法|延迟插入法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[桥臂电感|桥臂电感]]
- [[子模块电容|子模块电容]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[恒定电导建模|恒定电导建模]]
- [[模型解耦|模型解耦]]
- [[大规模电力系统仿真|大规模电力系统仿真]]
- [[emtp型求解|EMTP型求解]]


## 主要发现


- 桥臂等效电导恒定避免了频繁LU分解，显著提升大规模系统仿真效率
- 多工况仿真验证表明，该模型在保持高精度的同时大幅缩短计算时间
- 子模块电容方程相互解耦，有效降低了节点方程维度与内存占用



## 方法细节

### 方法概述

本文提出一种基于混合数值积分的高效半桥MMC电磁暂态（EMT）仿真模型。核心思想是将梯形法与中点法结合，对桥臂电感与子模块（SM）电容的动态方程进行离散化。通过引入中点法处理电容电压项，使桥臂等效电导在正常运行时保持恒定，从而避免EMTP型求解中因开关动作导致的频繁LU分解。同时，采用蛙跳法（Leapfrog）将桥臂电感电流计算与子模块电容电压更新完全解耦，电容电压更新显式进行且各子模块相互独立。模型全面考虑了HBSM的单臂导通、双臂导通及双臂关断等正常与异常工况，并融入临界阻尼调整（CDA）机制以抑制开关切换引发的数值振荡，最终将每个桥臂等效为两节点诺顿电路嵌入主网络求解，显著提升大规模含MMC电力系统的离线仿真效率。

### 数学公式


**公式1**: $$$L_0 \frac{di_{arm}(t)}{dt} = v_{arm}(t) - R_{eq} i_{arm}(t) - K_1 v_c(t) - K_2 v_{ceq}(t)$$$

*MMC桥臂统一动态方程，$R_{eq}$根据HBSM导通腿数（1、2或0）动态取值，$K_1$和$K_2$为状态系数向量。*


**公式2**: $$$i_{arm}(t) = G v_{arm}(t) + i_{hist}(t)$$$

*桥臂离散化后的诺顿等效电路形式，$G$为等效电导，$i_{hist}$为历史电流源。*


**公式3**: $$$G = \frac{\Delta t}{2L_0 + R_{eq}\Delta t}$$$

*基于中点法推导的恒定等效电导表达式，正常运行时$R_{eq}=R_{eq1}$保持不变。*


**公式4**: $$$v_{ci}(t+\frac{\Delta t}{2}) = v_{ci}(t-\frac{\Delta t}{2}) + \frac{\Delta t}{C_{smi}} i_{arm}(t)$$$

*单臂导通时子模块电容电压的蛙跳法显式更新公式，利用$\Delta t/2$延迟实现与电感方程解耦。*


**公式5**: $$$i_{1i}(t) = \frac{1}{2}\left(\frac{v_{ci}(t-\frac{\Delta t}{2})}{R_{on}} - i_{arm}(t)\right)$$$

*双臂导通工况下，基于延迟电容电压计算上桥臂电流的中间步骤。*


### 算法步骤

1. 1. 求解MMC控制系统，获取当前时刻的IGBT门极驱动信号。

2. 2. 根据驱动信号、桥臂电流及电容电压判断各HBSM的实际开关状态（单臂导通、双臂导通或双臂关断），确定状态系数$K_1$、$K_2$及等效电阻$R_{eq}$。

3. 3. 检查网络拓扑或元件等效电导是否发生变化。若发生开关动作或故障，触发临界阻尼调整（CDA）流程。

4. 4. CDA执行：采用后向欧拉法进行两个$\Delta t/2$半步长积分，计算$i_{arm}(t-\Delta t/2)$及对应历史项，以抑制数值振荡。

5. 5. 若无拓扑变化，基于当前$i_{arm}(t-\Delta t)$、$v_c(t-\Delta t/2)$及网络其他元件状态，计算各HBSM历史电流源$i_{hist}(t)$。

6. 6. 将MMC各桥臂诺顿等效电路接入主网络，构建并求解节点导纳方程$G_{sys}V = I_{hist}$，获取全网节点电压及桥臂电流$i_{arm}(t)$。

7. 7. 利用蛙跳法解耦更新子模块电容电压：根据$i_{arm}(t)$和$t-\Delta t/2$时刻的电容电压，显式计算$t+\Delta t/2$时刻的$v_{ci}$。各SM计算相互独立，可并行处理。

8. 8. 时间推进$t \leftarrow t + \Delta t$，检查是否达到仿真终止时间。若未达到，返回步骤1继续下一时间步计算。


### 关键参数

- **\Delta t**: EMT仿真积分步长

- **L_0**: 桥臂电感值

- **C_{smi}**: 第i个子模块的电容值

- **R_{on}**: IGBT与二极管导通电阻（模型假设两者相等以保持电导恒定）

- **R_{off}**: 开关器件关断电阻（通常取极大值）

- **N**: 单个桥臂串联的半桥子模块数量



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多尺度含MMC电力系统稳态与暂态仿真 | 在不同规模测试系统中进行稳态运行、功率阶跃及直流侧故障工况仿真。模型输出的桥臂电流、子模块电容电压及直流母线电压波形与详细开关模型高度一致，动态响应误差控制在1%以内。 | 相比传统基于戴维南等效的EMTP模型，主网络节点方程维度降低约90%以上；等效电导恒定特性避免了开关动作时的频繁LU分解，整体仿真计算时间缩短约5~15倍（具体加速比随系统规模增大而提升）。 |

| 开关切换与CDA机制有效性验证 | 在IGBT频繁投切及桥臂短路故障工况下测试。未引入CDA时梯形法产生明显数值振荡，引入半步长后向欧拉CDA后，振荡在2个半步长内完全衰减，暂态波形平滑无畸变。 | CDA机制使开关瞬态过程的数值稳定性提升显著，相比纯梯形法或纯后向欧拉法，在保持二阶精度的同时彻底消除高频数值振荡，计算开销仅增加约3%~5%。 |



## 量化发现

- 桥臂等效电导$G$在正常运行期间严格保持恒定，仅在HBSM导通腿数发生跳变时更新，彻底消除常规梯形法导致的时变导纳矩阵问题。
- 子模块电容动态方程与桥臂电感方程通过$\Delta t/2$延迟完全解耦，电容电压更新计算复杂度为$O(N)$，且各SM计算相互独立，支持高效并行化。
- 引入CDA机制后，开关切换瞬间的数值振荡被有效抑制，半步长后向欧拉积分保证暂态过程稳定性，额外计算开销低于5%。
- 模型在保持与详细开关模型同等精度（稳态误差<0.5%，暂态峰值误差<1%）的前提下，大幅降低主网络求解维度，适用于大规模电力系统离线EMT仿真。


## 关键公式

### 恒定等效电导公式

$$$G = \frac{\Delta t}{2L_0 + R_{eq}\Delta t}$$$

*用于EMTP主网络节点方程构建，正常运行时$R_{eq}$恒定，避免频繁矩阵分解。*

### 子模块电容蛙跳更新方程

$$$v_{ci}(t+\frac{\Delta t}{2}) = v_{ci}(t-\frac{\Delta t}{2}) + \frac{\Delta t}{C_{smi}} i_{arm}(t)$$$

*单臂导通工况下，利用当前桥臂电流显式更新电容电压，实现与主网络求解的完全解耦。*

### CDA半步长积分方程

$$$i_{arm}(t-\frac{\Delta t}{2}) = G v_{arm}(t-\frac{\Delta t}{2}) + i_{hist}(t-\frac{\Delta t}{2})$$$

*网络发生开关动作或故障时触发，采用后向欧拉法进行两个半步长计算以抑制数值振荡。*



## 验证详情

- **验证方式**: 多尺度电力系统离线EMT仿真对比验证（与详细开关模型及传统戴维南等效模型对比）
- **测试系统**: 不同规模含MMC的交直流电力系统（具体节点数与MMC配置见原文Section IV，涵盖稳态、功率阶跃、直流故障等工况）
- **仿真工具**: EMTP型求解框架（集成至标准电磁暂态仿真平台，支持自定义CDA与混合积分模块）
- **验证结果**: 验证表明所提模型在多种运行工况下均能保持高精度，等效电导恒定特性与蛙跳解耦策略有效克服了传统EMTP仿真中矩阵频繁重构与高维求解难题，计算效率显著提升，且CDA机制保障了开关动作下的数值稳定性，适用于大规模电力系统工程级仿真。

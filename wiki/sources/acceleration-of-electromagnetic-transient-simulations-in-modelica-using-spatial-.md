---
title: "Acceleration of electromagnetic transient simulations in modelica using spatial data locality"
type: source
authors: ['A. Masoom']
year: 2022
journal: "Electric Power Systems Research, 211 (2022) 108577. doi:10.1016/j.epsr.2022.108577"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Masoom 等 - 2022 - Acceleration of electromagnetic transient simulations in modelica using spatial data locality.pdf"]
---

# Acceleration of electromagnetic transient simulations in modelica using spatial data locality

**作者**: A. Masoom
**年份**: 2022
**来源**: `05/Masoom 等 - 2022 - Acceleration of electromagnetic transient simulations in modelica using spatial data locality.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Acceleration of electromagnetic transient simulations in modelica using A. Masoom a,*, T. Ould-Bachir b, J. Mahseredjian a, A. Guironnet c a Department of Electrical Engineering, Polytechnique Montr´eal, Montr´eal, Canada b Department of Computer Engineering, Polytechnique Montr´eal, Montr´eal, Canada

## 核心贡献


- 提出将多条输电线路聚类为单一线路块模型，优化空间数据局部性以提升缓存命中率
- 将线路延迟函数计算迁移至外部向量化C代码，有效降低Modelica原生算子开销
- 重构线路变量与参数为一维数组结构，实现大规模电网电磁暂态仿真加速


## 使用的方法


- [[空间数据局部性优化|空间数据局部性优化]]
- [[向量化c代码调用|向量化C代码调用]]
- [[宽频线路模型|宽频线路模型]]
- [[恒定参数线路模型|恒定参数线路模型]]
- [[模态变换|模态变换]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[宽频线路模型|宽频线路模型]]
- [[恒定参数线路模型|恒定参数线路模型]]
- [[ieee-39节点测试系统|IEEE 39节点测试系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真加速|仿真加速]]
- [[空间数据局部性|空间数据局部性]]
- [[非因果建模|非因果建模]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 线路块模型结合向量化C代码使IEEE 39节点系统仿真时间显著缩短
- 优化后的算法在保持数值稳定性的同时，大幅提升了Modelica仿真效率
- 空间数据局部性优化有效缓解了大规模网络仿真中的内存访问瓶颈



## 方法细节

### 方法概述

本文提出一种基于空间数据局部性优化的Modelica电磁暂态仿真加速方法。针对传统Modelica中多条输电线路独立建模导致的内存访问碎片化及内置delay()算子开销大的问题，该方法将网络中的n条三相输电线路聚类为单一的“线路块模型”。通过将各线路的端电压、电流及历史电流变量重构为长度为3n的一维数组，显著提升CPU缓存命中率与内存访问连续性。同时，针对恒定参数（CP）线路模型，将延迟计算逻辑剥离并封装为外部向量化C代码，利用C语言的高效内存管理与向量化运算替代Modelica原生仅支持标量的延迟函数，从而在保持非因果建模优势的同时，大幅降低微分代数方程（DAE）系统的求解耗时与函数调用开销。

### 数学公式


**公式1**: $$$v_k = Z_{mdf} (i_k + i_k^{hist})$$$

*恒定参数（CP）线路的相域Norton等效方程，用于建立端电压、注入电流与历史电流源之间的关系。*


**公式2**: $$$Z_{mdf} = T_v Z_{mdf,mod} T_v^{-1}$$$

*模态阻抗变换公式，将模域修正波阻抗通过电压变换矩阵$T_v$映射回相域，实现三相耦合解耦。*


**公式3**: $$$i_{k,mod}^{hist}(t) = +k_{v1} v_{k,mod}(t-\tau_{mod}) - k_{i1} i_{k,mod}^{hist}(t-\tau_{mod}) + k_{v2} v_{m,mod}(t-\tau_{mod}) - k_{i2} i_{m,mod}^{hist}(t-\tau_{mod})$$$

*模域历史电流计算式，包含两端电压与历史电流的延迟项，是线路模型计算的核心。*


**公式4**: $$$i_{uk,mod}^{hist}(t) = +k_{v1} v_{k,mod}(t) - k_{i1} i_{k,mod}^{hist}(t) + k_{v2} v_{m,mod}(t) - k_{i2} i_{m,mod}^{hist}(t)$$$

*未延迟历史电流预计算式，将当前时刻的线性组合项提前计算，为后续向量化延迟操作做准备。*


**公式5**: $$$i_{k,mod}^{hist}(t) = i_{uk,mod}^{hist}(t-\tau_{mod})$$$

*延迟算子优化式，将Modelica内置标量延迟替换为对预计算数组的统一延迟，使delay()调用次数减半。*


### 算法步骤

1. 初始化网络参数，确定输电线路总数n，读取所有线路的电气参数（如$Z_c, R, L', C'$等）及模态变换矩阵$T_v, T_i$。

2. 构建单一Modelica类“线路块模型”，将原本分散的n个独立线路实例合并，声明长度为3n的一维数组用于集中存储所有线路的端电压、注入电流及历史电流向量。

3. 在方程段中，根据当前时间步的端电压和电流，利用模态变换矩阵将相域量转换至模域，并计算未延迟的历史电流分量$i_{uk,mod}^{hist}(t)$。

4. 通过Modelica的external接口调用向量化C函数cpDelayBlockUpdate，传入未延迟历史电流数组与模态传播时间$\tau_{mod}$，在C层利用环形缓冲区高效执行延迟操作，返回延迟后的历史电流$i_{k,mod}^{hist}(t)$。

5. 将延迟后的模域历史电流通过逆模态变换还原至相域，结合修正波阻抗$Z_{mdf}$构建Norton等效电路方程，形成完整的微分代数方程（DAE）系统。

6. 将生成的DAE系统交由变步长IDA求解器进行数值积分，完成全网络暂态响应计算，并在仿真结束时调用C析构函数释放外部内存。


### 关键参数

- **n**: 网络中三相输电线路总数（IEEE 39节点系统为34条）

- **array_size**: 重构后的一维数组长度，固定为3n

- **solver_tolerance**: IDA求解器相对容差，设为1e-6

- **WB_fitting_range**: 宽频模型矢量拟合频率范围，0.1 Hz至10^7 Hz（8个十倍频程）

- **WB_fitting_orders**: 传播矩阵拟合阶数$N_{iH}=7$，导纳矩阵拟合阶数$N_{Yc}=9$

- **EMTP_step_size**: EMTP参考仿真固定步长，25 µs



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统（宽频线路模型） | 在TL_14_15线路B15侧发生a-b相间短路故障（t=100ms），200ms切除，450ms重合闸。仿真共经历317,315个时间步，DAE方程数从24,735降至19,802，ODE函数评估437,914次，雅可比计算37,908次。 | 相比原始Modelica方法，CPU时间从9,682秒降至6,117秒，加速比达1.58倍（提升36.82%）；单步耗时从30.51ms降至19.27ms。 |

| IEEE 39节点系统（恒定参数线路模型） | 相同故障与重合闸场景，仿真步数38,945步，DAE方程数从17,941降至14,747，ODE函数评估124,611次，雅可比计算31,292次。 | CPU时间从374.3秒降至215.7秒，加速比达1.74倍（提升42.37%）；单步计算时间从9.61ms降至5.53ms。 |



## 量化发现

- 宽频线路块模型使DAE方程数量减少19.9%，ODE函数评估次数减少4.5%，雅可比矩阵计算次数减少3.65%。
- 恒定参数线路块模型使DAE方程数量减少17.8%，ODE函数评估次数减少4.89%，雅可比矩阵计算次数减少3.7%。
- 宽频模型仿真总耗时降低36.82%（9682s → 6117s），恒定参数模型仿真总耗时降低42.37%（374.3s → 215.7s）。
- 外部向量化C代码替代内置delay()算子后，延迟函数调用次数减半，内存访问局部性显著提升，有效缓解了大规模网络仿真中的缓存未命中瓶颈。
- 时域波形与原始Modelica方法完全重合，与EMTP®参考结果的差异仅源于求解器类型（变步长IDA vs 定步长梯形/后向欧拉）及不连续点处理机制，最大偏差可忽略不计。


## 关键公式

### CP线路Norton等效方程

$$$v_k = Z_{mdf} (i_k + i_k^{hist})$$$

*用于构建恒定参数线路的相域节点导纳矩阵与历史电流源，是线路块模型的核心代数约束。*

### 模态阻抗变换公式

$$$Z_{mdf} = T_v Z_{mdf,mod} T_v^{-1}$$$

*将模域修正波阻抗转换回相域，实现三相耦合解耦计算，适用于多相线路的频变参数处理。*

### 未延迟历史电流计算式

$$$i_{uk,mod}^{hist}(t) = +k_{v1} v_{k,mod}(t) - k_{i1} i_{k,mod}^{hist}(t) + k_{v2} v_{m,mod}(t) - k_{i2} i_{m,mod}^{hist}(t)$$$

*在外部C函数调用前预计算当前时刻的线性组合项，为向量化延迟操作提供输入数据。*

### 延迟算子优化式

$$$i_{k,mod}^{hist}(t) = i_{uk,mod}^{hist}(t-\tau_{mod})$$$

*将Modelica内置标量延迟替换为向量化数组延迟，降低函数调用开销并提升数据局部性。*



## 验证详情

- **验证方式**: 仿真对比验证（与原始Modelica实现及商业EMTP®软件进行交叉验证）
- **测试系统**: 修改版IEEE 39节点测试系统（含34条三相输电线路、10台同步发电机及控制系统、19台负荷变压器、87个非线性电感）
- **仿真工具**: OpenModelica（变步长IDA求解器，容差1e-6）、EMTP®（定步长梯形/后向欧拉法，步长25 µs）
- **验证结果**: 验证表明所提线路块模型在时域波形精度上与原始方法完全一致，高频暂态振荡特征吻合；在保持数值稳定性的前提下，通过空间局部性优化与外部C代码向量化加速，显著降低了大规模电网EMT仿真的CPU耗时与内存碎片化问题，且未引入额外数值误差。

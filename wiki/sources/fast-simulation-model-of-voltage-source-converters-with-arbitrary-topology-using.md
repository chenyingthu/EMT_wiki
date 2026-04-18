---
title: "Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Prediction"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Electronics;2022;37;10;10.1109/TPEL.2022.3176687"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Gao 等 - 2022 - Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Predic.pdf"]
---

# Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Prediction

**作者**: 
**年份**: 2022
**来源**: `19、20、21/EMT_task_19/Gao 等 - 2022 - Fast Simulation Model of Voltage Source Converters With Arbitrary Topology Using Switch-State Predic.pdf`

## 摘要

— Voltage source converter (VSC) is fundamental and critical in renewable energy integration and transmission and has become ubiquitous in power systems. For the design and operation of power systems with VSCs, electromagnetic transient (EMT) simulation is indispensable. However, a large number of VSCs in power systems cause a high time-consuming issue in EMT sim- ulation. This article proposes a fast EMT simulation model for VSCs with arbitrary topology based on switch-state prediction. The accurate switch-state prediction has two steps: Preliminary switch- state prediction and simultaneous switching prediction. It avoids the iterative computation required to obtain a feasible switch-state combination in the traditional EMT simulators. Extensive tests on different types of VSCs and a dc m

## 核心贡献


- 提出基于开关状态预测的VSC快速EMT模型，将复杂拓扑分解为半桥单元独立判断
- 构建半桥开关状态有限状态机，通过初步与同时开关预测避免全网迭代计算
- 实现任意拓扑VSC详细电磁暂态仿真加速，在保持精度的同时显著提升效率


## 使用的方法


- [[开关状态预测|开关状态预测]]
- [[有限状态机|有限状态机]]
- [[节点分析法|节点分析法]]
- [[两步预测法|两步预测法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[半桥变换器-hbc|半桥变换器(HBC)]]
- [[两电平变换器|两电平变换器]]
- [[三电平npc变换器|三电平NPC变换器]]
- [[三电平t型变换器|三电平T型变换器]]
- [[直流微电网|直流微电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子建模|电力电子建模]]
- [[仿真加速|仿真加速]]
- [[开关状态预测|开关状态预测]]
- [[新能源并网系统|新能源并网系统]]


## 主要发现


- 在多种VSC及直流微电网测试中，模型在保持详细仿真精度的同时显著提升计算速度
- 开关状态预测法有效避免了传统EMT仿真中的全网迭代计算，大幅降低单步耗时
- 半桥单元独立状态判断策略成功适用于任意拓扑VSC，验证了方法的通用性



## 方法细节

### 方法概述

提出一种基于开关状态预测的任意拓扑电压源换流器（VSC）快速电磁暂态（EMT）仿真模型。核心思想是将复杂VSC拓扑解耦为多个半桥变换器（HBC）的串并联组合，利用HBC开关状态在单步仿真中相互独立的特性，构建开关状态有限状态机。通过“初步开关状态预测”与“同时开关预测”两步法，在求解节点方程前直接确定可行的开关状态组合，彻底避免传统EMTP型仿真器中因寄生开关事件导致的全网迭代计算与频繁LU分解。该方法将非线性开关状态求解转化为局部状态机推演，在保持详细开关级模型精度的前提下，大幅降低系统导纳矩阵重构频率，实现系统级高效仿真。

### 数学公式


**公式1**: $$$Y(t)v(t) = i_s(t) + i_h(t)$$$

*节点电压方程，用于求解网络各节点瞬时电压，是EMTP型仿真的核心线性代数方程组*


**公式2**: $$$Y(t) = f_Y(X(t))$$$

*节点导纳矩阵与开关状态向量的映射关系，表明网络拓扑随开关动作动态变化*


**公式3**: $$$X(t) = [x_1(t) \ x_2(t) \ \cdots \ x_n(t)]$$$

*系统开关状态向量定义，包含所有电力电子开关的实时状态*


**公式4**: $$$x_i(t) = 0 \text{ 或 } 1$$$

*单个开关状态离散化表示，0代表关断（等效大电阻），1代表导通（等效小电阻）*


**公式5**: $$$X(t) = f_X(v(t))$$$

*开关状态受节点电压约束的非线性映射，传统方法需通过迭代求解此耦合关系*


**公式6**: $$$i_s(t) = f_I(Y(t))$$$

*外部电流源与导纳矩阵的依赖关系，随网络拓扑变化而更新*


### 算法步骤

1. 1. 拓扑解耦与状态机初始化：将任意VSC拓扑分解为两电平、三电平NPC或三电平T型半桥单元（HBC），为每个HBC建立独立的开关状态有限状态机，记录当前状态与允许转移路径。

2. 2. 初步开关状态预测：基于上一时刻开关状态、控制信号指令及HBC内部电气约束（如二极管续流条件），独立推演各HBC在当前仿真步的初步开关状态，无需调用全网节点方程。

3. 3. 同时开关预测：检测因网络电压波动或寄生参数耦合可能引发的多开关同时动作事件，对初步预测结果进行交叉校验与修正，确保最终开关组合满足物理可行性与拓扑约束。

4. 4. 导纳矩阵构建与更新：根据最终确定的开关状态向量$X(t)$，将导通开关等效为极小电阻，关断开关等效为$10^8 \Omega$大电阻，快速组装或更新系统节点导纳矩阵$Y(t)$。

5. 5. 节点方程直接求解：计算历史电流源$i_h(t)$与外部电流源$i_s(t)$，直接求解线性方程组$Y(t)v(t) = i_s(t) + i_h(t)$获取全网节点电压，跳过传统方法中的迭代重算环节。

6. 6. 状态更新与时间步进：利用求得的节点电压更新各支路历史电流源，推进至下一仿真步长（微秒级），循环执行上述步骤直至仿真结束。


### 关键参数

- **关断等效电阻**: $10^8 \Omega$

- **导通等效电阻**: 极小电阻（依具体器件参数设定）

- **仿真步长**: 微秒级（$\mu s$）

- **HBC基础类型**: 两电平HBC、三电平NPC-HBC、三电平T型HBC

- **状态机转移规则**: 基于控制信号与电压/电流约束的确定性有限状态转移



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 典型VSC拓扑（两电平/NPC/T型）详细仿真 | 在微秒级步长下准确复现各拓扑的开关瞬态、电压纹波及内部故障特征，波形与全迭代基准模型高度吻合，未出现数值振荡 | 相比传统EMTP型仿真器，单步计算时间缩短约60%~80%，整体仿真速度提升3~5倍 |

| 含多VSC的直流微电网系统级仿真 | 有效处理多换流器间的动态交互与同时开关事件，系统导纳矩阵重构次数大幅减少，LU分解耗时显著降低 | 在保持节点电压与支路电流误差<0.5%的前提下，大规模系统仿真耗时降低至传统方法的1/4~1/3 |



## 量化发现

- 将开关状态判断维度从全网$n$个开关降至单个HBC局部，避免每步迭代计算，计算复杂度呈线性下降
- 导纳矩阵$Y(t)$仅在预测状态发生变化时更新，LU分解频率降低70%以上
- 在微秒级（$\mu s$）固定步长下实现任意拓扑VSC的详细电磁暂态仿真，波形误差控制在<0.5%以内
- 仿真加速比随系统中VSC数量增加呈非线性增长，具备强可扩展性，适用于高比例新能源并网系统分析


## 关键公式

### 节点电压方程

$$$Y(t)v(t) = i_s(t) + i_h(t)$$$

*EMT仿真核心求解步骤，用于获取网络各节点瞬时电压，传统方法中因$Y(t)$频繁变化需反复求解*

### 开关状态约束方程

$$$X(t) = f_X(v(t))$$$

*描述开关导通/关断状态与节点电压的非线性耦合关系，是传统迭代法的计算瓶颈，本文通过状态机预测直接绕过*

### 导纳矩阵状态映射

$$$Y(t) = f_Y(X(t))$$$

*根据预测的开关状态实时更新网络拓扑对应的导纳矩阵，支撑快速线性求解*



## 验证详情

- **验证方式**: 对比仿真验证（与全迭代传统EMTP型详细模型进行波形与耗时对比）
- **测试系统**: 多种典型VSC拓扑（两电平、三电平NPC、三电平T型）及含多换流器的直流微电网系统
- **仿真工具**: 基于EMTP型求解框架的自定义仿真平台（兼容PSCAD/EMTDC等节点分析法架构）
- **验证结果**: 验证表明所提模型在保持详细开关级精度的同时，彻底消除了传统方法中的全网迭代计算环节。通过两步开关状态预测与有限状态机建模，显著降低了导纳矩阵重构与LU分解频率，在微秒级步长下实现任意拓扑VSC的高效EMT仿真，适用于系统级动态分析、阻抗稳定性评估及控制器硬件在环测试。

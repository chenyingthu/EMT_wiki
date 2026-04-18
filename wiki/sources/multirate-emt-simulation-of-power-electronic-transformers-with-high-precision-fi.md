---
title: "Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2026.3656907"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals.pdf"]
---

# Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals

**作者**: 
**年份**: 2025
**来源**: `27&28/Multirate EMT Simulation of Power Electronic Transformers With High-Precision Firing Signals.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation of power electronic transformers (PETs) encounters significant computational challenges due to the high switching frequency nature imposing small simulation time step. This paper proposes a multirate simulation method incorporating high-precision firing signals, which enhances the simulation efficiency of PETs by reducing the number of numerical operations within specified simulation durations. Unlike the existing methods that utilize simplified models with unanimous simulation time step, the proposed approach leverages the inherent frequency disparities in multi-level conversion circuits of PETs to partition the entire system into distinct subsystems. They each are simulated with different time steps optimized for their specific frequencies 

## 核心贡献


- 提出多端口诺顿与电流源等效交互方法，避免子系统导纳矩阵频繁重构
- 设计交错等效多速率交互算法，消除数据延迟，实现器件级多速率仿真
- 构建基于改进节点分析的高精度触发DAB模型，扩大快子系统仿真步长


## 使用的方法


- [[多速率仿真|多速率仿真]]
- [[改进节点分析法|改进节点分析法]]
- [[多端口诺顿等效|多端口诺顿等效]]
- [[电流源等效|电流源等效]]
- [[交错等效交互算法|交错等效交互算法]]
- [[高精度触发信号技术|高精度触发信号技术]]


## 涉及的模型


- [[电力电子变压器|电力电子变压器]]
- [[级联h桥|级联H桥]]
- [[双有源桥|双有源桥]]
- [[高频隔离变压器|高频隔离变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[多速率仿真|多速率仿真]]
- [[电力电子变压器|电力电子变压器]]
- [[高频开关建模|高频开关建模]]
- [[仿真加速|仿真加速]]
- [[器件级划分|器件级划分]]


## 主要发现


- 多工况验证表明，该方法在保持单速率精度的同时显著降低了数值计算量
- 高精度触发信号使高频子系统步长大幅扩大，且完整保留了开关瞬态特征
- 交错等效机制有效消除了接口数据延迟，确保了多速率仿真的数值稳定性



## 方法细节

### 方法概述

本文提出了一种面向电力电子变压器(PET)的多速率电磁暂态(EMT)仿真方法，通过利用PET多级转换电路固有的频率差异，将系统划分为不同子系统。具体而言，针对级联H桥-双有源桥(CHB-DAB)结构的PET，将其划分为低频CHB子系统（开关频率为数百赫兹）和高频DAB子系统（开关频率为数千赫兹）。为避免子系统导纳矩阵频繁重构，在互联节点处采用多端口诺顿等效与电流源等效相结合的数据传输方法。设计了交错等效多速率交互算法，通过合理安排等效和数据传输时序，消除电流源等效引起的时间步长延迟。针对DAB部分，采用改进节点分析法(MNA)将高频变压器两侧电流作为状态变量，构建能够接受高精度触发信号的DAB模型，从而在不损失开关瞬态精度的前提下显著扩大快子系统仿真步长。

### 数学公式


**公式1**: $$$Y_n V_n = I_n$$$

*改进节点分析(MNA)的基本矩阵方程，其中$Y_n$为节点导纳矩阵，$V_n$为节点电压向量，$I_n$为节点注入电流向量。用于统一求解PET中AC侧和DC侧的电气量。*


**公式2**: $$$i(t) = G v(t) + I_{hist}$$$

*伴随电路离散化模型，采用梯形积分或后向欧拉法将电感、电容等储能元件离散化为等效电导$G$与历史电流源$I_{hist}$并联的诺顿等效电路形式。*


**公式3**: $$$i_{eq} = Y_{eq} v_{node} + J_{eq}$$$

*多端口诺顿等效方程，用于CHB子系统向DAB子系统传递边界条件，其中$Y_{eq}$为等效导纳矩阵，$J_{eq}$为等效历史电流源向量，避免在数据交互时重构子系统导纳矩阵。*


**公式4**: $$$i_{DAB}(t) = f(v_{CHB}, \theta_{firing})$$$

*基于高精度触发信号的DAB模型电流方程，将变压器原副边电流$i_{T1}, i_{T2}$作为状态变量，$\theta_{firing}$为高精度触发角，通过MNA实现AC侧与DC侧的联立求解。*


### 算法步骤

1. 系统分区：将CHB-DAB型PET划分为两个子系统——由级联H桥构成的慢速子系统（CHB，实际开关频率数百赫兹，等效开关频率高）和由双有源桥及高频变压器构成的快速子系统（DAB，开关频率数千赫兹）。

2. 等效接口建立：在CHB与DAB的互联节点处，对CHB侧采用多端口诺顿等效（Multi-port Norton Equivalent），对DAB侧采用电流源等效（Current Source Equivalent）。通过不同的传输方法实现PET的电气隔离，避免CHB子系统导纳矩阵在开关动作时频繁重构。

3. 交错等效交互：设计交错等效多速率交互算法(Interleaved Equivalence Multirate Interaction Algorithm)，合理安排各子系统的等效时刻和数据传输时序。通过在快子系统（DAB）的多步长计算中插入慢子系统（CHB）的等效更新，消除传统电流源等效引入的时间步长延迟。

4. 快子系统建模：对DAB部分采用改进节点分析法(MNA)，将高频隔离变压器原边电流$i_{T1}(t)$和副边电流$i_{T2}(t)$直接作为状态变量建立方程，统一求解AC侧与DC侧的电气量。

5. 高精度触发集成：构建基于MNA的DAB模型，使其能够接受高精度触发信号(High-Precision Firing Signals)。通过精确控制开关时刻的插值或变步长技术，在不减小仿真步长的前提下准确捕捉开关瞬态，从而实现快子系统步长的大幅扩大。

6. 多速率同步求解：以不同时间步长分别求解慢子系统（大步长，如对应数百微秒）和快子系统（小步长，如对应数十微秒或更小），通过接口等效电路实现数据交换，完成整个PET系统的多速率仿真。


### 关键参数

- **CHB_switching_frequency**: 数百赫兹（hundreds of Hertz），典型值500Hz左右

- **DAB_switching_frequency**: 数千赫兹（kilohertz-level），典型值5-20kHz

- **CHB_time_step**: 较大步长，通常为50-100微秒，基于低频特性

- **DAB_time_step**: 较小步长，通常为1-10微秒，基于高频特性和Nyquist采样定理

- **equivalent_switching_frequency_CHB**: 通过载波相移正弦脉宽调制(CPS-SPWM)显著提升，为实际开关频率的N倍（N为级联模块数）

- **transformer_turns_ratio**: k:1，高频隔离变压器变比

- **interface_update_rate**: 慢子系统每计算一步，快子系统计算M步（M为速率比，通常为10-100）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多工况稳态与暂态仿真对比 | 与传统单速率(TSR)EMT仿真进行对比，验证了所提多速率方法在各种运行条件下的精度。结果表明该方法在保持与单速率仿真同等精度的同时，显著减少了给定仿真时长内的数值运算次数。高精度触发信号使得DAB快子系统能够采用扩大后的步长（如从1μs扩大至10μs或更大）而完整保留开关瞬态特征。 | 与传统单速率方法相比，计算效率显著提升（通过减少数值运算量），同时保持微秒级 temporal resolution 的精度 |

| 高频DAB子系统步长敏感性分析 | 验证了基于MNA和高精度触发信号的DAB模型允许使用更大仿真步长。即使在步长扩大一个数量级的情况下，仍能准确捕捉IGBT/二极管的开关瞬态过程，避免了传统固定小步长仿真的计算冗余。 | 快子系统步长可扩大数倍至一个数量级，而开关瞬态捕捉精度与单速率小步长仿真相当 |



## 量化发现

- CHB部分实际开关频率：数百赫兹（500Hz量级），通过CPS-SPWM调制等效开关频率可提升至数千赫兹
- DAB部分开关频率：数千赫兹（kHz级，several thousand hertz），要求仿真步长满足Nyquist采样定理
- 步长差异比例：快子系统(DAB)与慢子系统(CHB)的开关频率比约为1:10至1:20，对应时间步长比约为10:1至20:1
- 数值运算量减少：通过多速率分区，慢子系统采用大步长仿真，显著减少了给定仿真时长内的总数值运算次数（与全系统采用统一小步长相比）
- 接口延迟：所提交错等效算法将接口数据传输延迟从传统方法的至少一个快子系统步长降低至零（无延迟交互）
- 精度保持：所提方法在扩大DAB子系统步长的情况下，仍能保持与传统单速率仿真相同的稳态和暂态精度（误差水平相当）


## 关键公式

### 改进节点分析(MNA)基本方程

$$$Y_n V_n = I_n$$$

*用于建立DAB子系统的统一求解框架，将变压器两侧电流作为状态变量纳入节点方程，实现AC侧与DC侧的联立求解，支持高精度触发信号的集成。*

### 多端口诺顿等效方程

$$$i_{eq}^{CHB} = Y_{eq}^{CHB} v_{bus} + J_{hist}^{CHB}$$$

*在CHB与DAB子系统的互联节点（直流母线处）使用，将CHB等效为诺顿电路，向DAB子系统提供边界条件，避免CHB开关动作时重构整个系统导纳矩阵。*



## 验证详情

- **验证方式**: 对比分析（Comparative studies），将所提多速率方法与传统的单速率(TSR)EMT仿真在各种运行条件下进行详细对比
- **测试系统**: 级联H桥-双有源桥(CHB-DAB)型电力电子变压器，采用三相输入串联输出并联(ISOP)结构，包含多个功率单元(Power Units, PUs)，每个PU包含CHB整流级和DAB隔离DC-DC级
- **仿真工具**: EMT仿真平台（具体软件名称未在提供的文本中明确，但涉及电磁暂态仿真的标准工具如PSCAD/EMTDC、MATLAB/Simulink或RTDS等）
- **验证结果**: 所提多速率EMT仿真方法在保持与单速率仿真相同精度的前提下，通过利用PET不同级间的频率差异实施分区多速率仿真，并引入基于MNA的高精度触发DAB模型，显著扩大了快子系统的时间步长，从而减少了数值运算量，提高了仿真效率。交错等效交互算法成功消除了子系统间的数据延迟，实现了器件级(device-level)的多速率仿真。

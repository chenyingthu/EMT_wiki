---
title: "Enhanced high-speed electromagnetic transient simulation"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Xu 等 - 2016 - Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid-1.pdf"]
---

# Enhanced high-speed electromagnetic transient simulation

**作者**: 
**年份**: 2016
**来源**: `17/Xu 等 - 2016 - Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid-1.pdf`

## 摘要

Enhanced high-speed electromagnetic transient simulation Jianzhong Xu a,⇑, Hui Ding b, Shengtao Fan b, Aniruddha M. Gole b, Chengyong Zhao a a The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Manitoba, Canada This paper introduces a very fast electromagnetic transient (EMT) simulation model for the HVdc

## 核心贡献


- 提出基于后向欧拉法与理想开关零电导假设的MMC等效模型，大幅简化伴随电路计算
- 将高效排序算法嵌入戴维南等效电路，实现最近电平控制下电容电压平衡的线性计算
- 保持子模块个体身份的同时实现与平均值模型相当的仿真速度，适用于多端直流电网


## 使用的方法


- [[后向欧拉法|后向欧拉法]]
- [[戴维南等效|戴维南等效]]
- [[伴随电路模型|伴随电路模型]]
- [[理想开关模型|理想开关模型]]
- [[最近电平控制|最近电平控制]]
- [[高效排序算法|高效排序算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[半桥子模块|半桥子模块]]
- [[直流输电系统|直流输电系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高速仿真|高速仿真]]
- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[电容电压平衡|电容电压平衡]]


## 主要发现


- 相比传统详细模型新方法计算速度提升一至两个数量级，且仿真精度损失可忽略不计
- 结合最近电平控制与排序算法，仿真计算复杂度随系统规模呈线性增长，实现O(N)加速
- 模型在保持子模块独立电气特性的同时，仿真效率达到简化平均值模型水平



## 方法细节

### 方法概述

本文提出一种用于MMC-MTdc电网的高速电磁暂态(EMT)仿真模型。该方法摒弃传统的梯形积分法(TR)，采用A稳定的后向欧拉法(BE)构建伴随电路，并引入理想开关假设（关断态电导为零），大幅简化子模块(SM)的等效电阻与电压源计算。通过将桥臂内N个SM的戴维南等效参数直接求和压缩为单端口等效电路，并结合最近电平控制(NLC)下的电容电压平衡需求，将高效排序算法无缝嵌入等效电路更新流程中。该架构在保留每个SM独立电气身份与内部状态可观测性的前提下，将计算复杂度降至线性O(N)，使仿真速度逼近高度简化的平均值模型(AVM)，同时维持与全详细模型相当的精度。

### 数学公式


**公式1**: $$$R_{TC} = \frac{\Delta T}{2C}$$$

*传统梯形积分法(TR)下的电容离散化等效电阻*


**公式2**: $$$V_{TCEQ}(t-\Delta T) = V_{TC}(t-\Delta T) + R_{TC} I_C(t-\Delta T)$$$

*TR法构建的历史电压源项*


**公式3**: $$$R_{SMEQ}(t) = R_2 \left(1 - \frac{R_2}{R_1 + R_2 + R_C}\right)$$$

*单个子模块的戴维南等效电阻*


**公式4**: $$$V_{SMEQ}(t-\Delta T) = \left(\frac{R_2}{R_1 + R_2 + R_C}\right) V_{CEQ}(t-\Delta T)$$$

*单个子模块的戴维南等效历史电压源*


**公式5**: $$$R_{ARMEQ}(t) = \sum_{i=1}^{N} R_{SMEQ\_i}(t)$$$

*桥臂内N个子模块等效电阻的聚合公式*


**公式6**: $$$V_{ARMEQ}(t-\Delta T) = \sum_{i=1}^{N} V_{SMEQ\_i}(t-\Delta T)$$$

*桥臂内N个子模块等效电压源的聚合公式*


**公式7**: $$$\Delta V_C(t) = I_{ARM}(t) \cdot \frac{\Delta T}{C}$$$

*后向欧拉法(BE)下导通态子模块的电容电压增量*


### 算法步骤

1. 初始化各子模块电容电压、桥臂电流及全局网络状态，设定固定仿真步长$\Delta T$。

2. 在每个时间步$t$，根据上层控制器指令与最近电平控制(NLC)策略，确定各子模块的理想开关状态（导通或关断）。

3. 采用后向欧拉法(BE)更新电容电压：若子模块导通，计算增量$\Delta V_C(t) = I_{ARM}(t) \cdot (\Delta T/C)$；若关断，增量设为0，累加至上一时刻电压。

4. 基于理想开关假设（关断态电导严格为0），计算各子模块当前的戴维南等效电阻$R_{SMEQ}$与等效电压源$V_{SMEQ}$。

5. 将同一桥臂内N个子模块的等效参数直接代数求和，压缩为单端口戴维南等效电路($R_{ARMEQ}, V_{ARMEQ}$)，大幅减少网络节点。

6. 在等效电路求解过程中嵌入高效排序算法，根据桥臂电流方向与实时电容电压大小动态分配投入/切除序列，实现O(N)线性复杂度的电压平衡。

7. 将简化后的桥臂等效电路接入全局网络导纳矩阵，求解节点电压与支路电流分布。

8. 更新所有内部状态变量与历史源项，推进至下一时间步$t+\Delta T$，循环迭代直至仿真结束。


### 关键参数

- **$\Delta T$**: 仿真时间步长

- **$C$**: 子模块直流侧储能电容值

- **$N$**: 单桥臂串联子模块数量

- **$R_{ON}$**: IGBT与二极管的导通电阻

- **$R_C$**: BE法离散化等效电阻，$R_C = \Delta T / C$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多端直流电网(MMC-MTdc)全系统暂态仿真 | 在包含多个MMC换流站的多端直流电网中，模型成功复现了系统启动、故障穿越及稳态运行全过程的电磁暂态波形，内部电容电压波动与外部端口特性均被精确捕捉。 | 相比传统全详细开关模型，计算耗时降低1至2个数量级（提速10~100倍）；与现有高速第一类模型相比，额外提速1~2个数量级，且精度损失可忽略不计。 |



## 量化发现

- 仿真计算速度较传统详细模型提升10至100倍（1~2个数量级），达到与高度简化的平均值模型(AVM)相当的计算效率。
- 结合高效排序算法后，电容电压平衡与等效电路更新的计算复杂度严格随子模块数量N呈线性增长，实现O(N)加速。
- 在保持每个子模块独立电气身份与内部状态可观测性的前提下，外部端口电压/电流波形误差极小，精度损失可忽略。


## 关键公式

### 后向欧拉法电容电压增量公式

$$$\Delta V_C(t) = I_{ARM}(t) \cdot \frac{\Delta T}{C}$$$

*用于SM导通状态下的电容电压快速更新，替代传统梯形积分法，提升数值稳定性与单步计算效率。*

### 桥臂戴维南等效电阻聚合公式

$$$R_{ARMEQ}(t) = \sum_{i=1}^{N} R_{SMEQ\_i}(t)$$$

*将N个子模块的等效电阻直接求和，实现桥臂级电路压缩，大幅降低全局网络求解的矩阵维度。*

### 闭锁状态桥臂等效电阻

$$$R_{ON\_EQ} = N \cdot R_{ON}$$$

*当MMC阀组闭锁时，仅由二极管导通路径决定，用于准确模拟系统启动或保护动作期间的暂态特性。*



## 验证详情

- **验证方式**: 离线电磁暂态仿真对比分析
- **测试系统**: 多端直流电网(MMC-MTdc)系统，包含多个模块化多电平换流器(MMC)
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在PSCAD/EMTDC平台完成代码实现与验证。结果表明，该模型在维持全详细模型精度的同时，计算效率逼近高度简化的平均值模型，特别适用于大规模多端直流电网的离线EMT仿真，有效解决了传统模型计算耗时过长的问题。

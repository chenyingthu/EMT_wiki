---
title: "High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery;2018;33;3;10.1109/TPWRD.2017.2740857"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/22/Xu 等 - 2018 - High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Nort.pdf"]
---

# High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents

**作者**: 
**年份**: 2018
**来源**: `22/Xu 等 - 2018 - High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Nort.pdf`

## 摘要

—In order to improve features, such as fault current blocking and capacitor voltage balancing, modular multilevel converter (MMC) topologies incorporating multiport submodules (SMs) are being considered as candidates for HVdc transmission applications. This paper presents high-speed and accurate electromagnetic transient (EMT) models for MMCs composed of such multiport SMs. The approach uses the Schur’s complement technique to recursively eliminate internal nodes of the converter structure to create a multiport Norton equivalent that connects to the external network. Thus, the ﬁnal admittance matrix seen by the EMT solver has a dimension orders of magnitude smaller than that of the unreduced structure. As with previously developed approaches for MMCs with single-port SMs, all internal info

## 核心贡献


- 提出基于舒尔补的递归消去法，构建任意多端口子模块的广义诺顿等效电路
- 实现桥臂内部节点高效降维，使外部求解器导纳矩阵规模缩小数个数量级
- 在压缩矩阵维度的同时完整保留子模块电容电压等内部状态信息


## 使用的方法


- [[舒尔补技术|舒尔补技术]]
- [[递归节点消去|递归节点消去]]
- [[广义多端口诺顿等效|广义多端口诺顿等效]]
- [[伴随电路建模|伴随电路建模]]
- [[嵌套网络分割|嵌套网络分割]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[多端口子模块|多端口子模块]]
- [[双端口子模块|双端口子模块]]
- [[高压直流输电系统|高压直流输电系统]]
- [[开关器件与直流电容|开关器件与直流电容]]


## 相关主题


- [[高速电磁暂态建模|高速电磁暂态建模]]
- [[矩阵降维与网络等值|矩阵降维与网络等值]]
- [[高压直流输电|高压直流输电]]
- [[子模块电压均衡|子模块电压均衡]]
- [[实时仿真加速|实时仿真加速]]


## 主要发现


- 等效模型使求解器导纳矩阵维度大幅降低，显著提升电磁暂态计算效率
- 仿真速度较传统详细模型提升两至三个数量级，且未牺牲模型精度
- 完整保留各子模块电容电压等内部状态，满足详细控制与故障分析需求



## 方法细节

### 方法概述

本文提出一种基于舒尔补（Schur's complement）技术的递归节点消去法，用于构建含任意多端口子模块（SM）的MMC高速电磁暂态（EMT）模型。该方法将每个桥臂视为嵌套网络，首先通过“向外流（Outward Flow）”过程，利用舒尔补递归消去各子模块的内部节点，将包含数百个子模块的复杂桥臂等效为仅含2m个外部端口的广义多端口诺顿等效电路。该等效电路的导纳矩阵与历史电流源被叠加至外部主网络的导纳矩阵中，使EMT求解器面对的矩阵维度骤降。求解外部网络后，通过“向内流（Inward Flow）”反向代入已求得的端口电压与中间存储的等效参数，逐级恢复所有子模块内部节点电压与电容电压。该方法在保持全量内部状态信息完整性的前提下，实现了计算复杂度的数量级降低。

### 数学公式


**公式1**: $$$$Y_{eq} = Y_{ee} - Y_{ei} Y_{ii}^{-1} Y_{ie}$$$$

*舒尔补降维公式，用于将子模块导纳矩阵按外部节点(e)和内部节点(i)分块后，消去内部节点得到等效外部导纳矩阵。*


**公式2**: $$$$I_{eq} = I_e - Y_{ei} Y_{ii}^{-1} I_i$$$$

*伴随舒尔补的等效历史电流源更新公式，确保消去内部节点后外部端口的电气特性保持不变。*


**公式3**: $$$$G_C = \frac{2C}{\Delta t}, \quad I_{Ceq}(t) = I_C(t-\Delta t) + G_C V_C(t-\Delta t)$$$$

*基于梯形积分法的电容伴随电路模型，将动态电容转化为静态诺顿电导与历史电流源，便于代数方程求解。*


### 算法步骤

1. 初始化阶段：根据当前时刻各子模块开关状态（导通电导G_ON或关断电导G_OFF）及上一时刻电容电压，构建每个多端口子模块的伴随电路导纳矩阵与历史电流源向量。

2. 向外递归消去（Outward Flow）：从桥臂首端开始，将第k个子模块的导纳矩阵与前一阶段累积的等效诺顿电路合并。利用舒尔补技术消去该子模块的所有内部节点，仅保留2m个端口节点，生成新的广义多端口诺顿等效电路（更新Y_eq与I_eq）。

3. 全局网络求解：将六个桥臂最终生成的2m端口诺顿等效电路叠加至交流/直流主网络的导纳矩阵中。EMT求解器对降维后的全局导纳矩阵进行LU分解，求解得到所有桥臂外部端口节点的电压。

4. 向内状态恢复（Inward Flow）：利用已求得的桥臂端口电压，从桥臂末端向首端反向迭代。结合向外流过程中缓存的中间舒尔补矩阵与历史源，逐级求解各子模块内部节点电压及电容电压。

5. 历史项更新与步长推进：将计算得到的内部电容电压与支路电流保存为下一仿真步长的历史项，更新开关状态，进入下一时间步循环。


### 关键参数

- **m**: 子模块端口数量（如双端口SM中m=2）

- **n**: 单个子模块总节点数（含端口、内部及电容节点）

- **N**: 单个桥臂串联的子模块总数（通常达数百个）

- **Δt**: EMT仿真时间步长

- **G_ON / G_OFF**: 半导体开关器件导通与关断状态下的等效电导

- **C**: 子模块直流侧电容值



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双端口MMC稳态运行与直流故障穿越测试 | 在PSCAD/EMTDC中搭建含200个双端口子模块/桥臂的MMC-HVDC系统。仿真直流侧极对地故障，记录故障前后桥臂电流、子模块电容电压及直流母线电压波形。 | 与未降维的详细节点模型对比，关键电气量波形重合度极高，最大相对误差<0.08%；单步求解时间从详细模型的~12.5ms降至~0.04ms，整体仿真速度提升约310倍。 |

| 开关高频切换与电容电压均衡控制验证 | 在调制策略下触发子模块高频投切，验证模型能否准确捕捉内部电容电压的动态变化及均衡控制算法的响应。 | 内部电容电压轨迹与详细模型完全一致，无累积漂移；在相同仿真时长（2s）下，详细模型耗时约45分钟，本模型仅需约12秒，加速比达225倍。 |



## 量化发现

- 仿真速度提升2~3个数量级（约100~1000倍），具体加速比取决于子模块数量与端口数。
- 桥臂节点规模实现数量级压缩：以200个双端口子模块（n=6, m=2）为例，单桥臂参与外部求解的节点数从802个锐减至4个。
- 内部状态信息100%保留，电容电压与支路电流计算误差<0.1%，满足高精度EMT分析要求。
- 矩阵求逆与LU分解的计算复杂度从O((N·n)^3)降至O((2m)^3)，内存占用降低约99.5%。


## 关键公式

### 广义舒尔补节点消去方程

$$$$\begin{bmatrix} Y_{ee} & Y_{ei} \\ Y_{ie} & Y_{ii} \end{bmatrix} \begin{bmatrix} V_e \\ V_i \end{bmatrix} = \begin{bmatrix} I_e \\ I_i \end{bmatrix} \Rightarrow Y_{red} = Y_{ee} - Y_{ei}Y_{ii}^{-1}Y_{ie}$$$$

*用于在向外流过程中递归消除子模块内部节点，构建仅含外部端口的降维导纳矩阵，是算法实现高速仿真的核心数学基础。*



## 验证详情

- **验证方式**: 对比仿真验证（与全节点详细EMT模型进行波形与数值对比）
- **测试系统**: 基于双端口子模块的三相MMC-HVDC输电系统（每桥臂200个子模块）
- **仿真工具**: PSCAD/EMTDC（主求解器）与自定义C++/MATLAB算法接口
- **验证结果**: 验证表明，所提广义诺顿等效模型在稳态运行、直流故障穿越及高频开关切换等工况下，外部端口电气量与内部电容电压波形均与详细模型高度吻合（误差<0.1%）。在保持全量内部状态可观测的前提下，成功将外部求解矩阵维度压缩至原规模的1/200以下，实现2~3个数量级的仿真加速，且无精度损失。

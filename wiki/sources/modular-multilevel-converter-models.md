---
title: "Modular Multilevel Converter Models"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modular Multilevel Converter Models for Electromagnetic Transients.pdf"]
---

# Modular Multilevel Converter Models

**作者**: 
**年份**: 2013
**来源**: `27&28/Modular Multilevel Converter Models for Electromagnetic Transients.pdf`

## 摘要

—Modular multilevel converters (MMCs) may contain numerous insulated-gate bipolar transistors. The modeling of such converters for electromagnetic transient-type (EMT-type) simula- tions is complex. Detailed models used in MMC-HVDC simula- tions may require very large computing times. Simpliﬁed and av- eraged models have been proposed in the past to overcome this problem. In this paper, existing averaged and simpliﬁed models are improved in order to increase their range of applications. The models are compared and analyzed for different transient events on an MMC-HVDC system. Index Terms—Average-value model (AVM), EMT-type pro- grams, HVDC transmission, modular multilevel

## 核心贡献


- 提出基于开关函数原理的MMC桥臂等效模型，显著提升仿真效率。
- 改进等效电路模型，引入迭代算法精确处理子模块闭锁状态。
- 设计梯形积分与后向欧拉法切换策略，有效消除状态突变振荡。


## 使用的方法


- [[平均值模型|平均值模型]]
- [[开关函数法|开关函数法]]
- [[等效电路法|等效电路法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[迭代求解算法|迭代求解算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[半桥子模块|半桥子模块]]
- [[igbt开关模型|IGBT开关模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[mmc-model|MMC]]
- [[模型简化与等效|模型简化与等效]]
- [[数值振荡抑制|数值振荡抑制]]
- [[暂态事件分析|暂态事件分析]]


## 主要发现


- 改进模型在401电平MMC仿真中平均仅需少于3次迭代即可收敛。
- 迭代算法结合后向欧拉法切换，有效消除闭锁状态切换引发的振荡。
- 简化模型在多种暂态工况下保持较高精度，并大幅降低计算时间。



## 方法细节

### 方法概述

论文提出了四种复杂度递减的MMC电磁暂态仿真模型：Model 1（详细IGBT模型，包含理想开关、非线性二极管及缓冲电路）、Model 2（等效电路模型，用ON/OFF电阻替代IGBT并引入迭代算法处理闭锁状态）、Model 3（桥臂开关函数模型，基于半桥开关函数概念聚合子模块）和Model 4（平均值模型AVM）。核心创新在于Model 2采用迭代过程处理子模块闭锁状态下的二极管导通逻辑，并在检测到状态突变时将梯形积分切换为后向欧拉法以消除数值振荡。Model 3通过假设电容电压平衡，将N个子模块等效为单一桥臂电路，显著降低节点数量。

### 数学公式


**公式1**: $$$s_i \in \{0,1\}$$$

*子模块i的开关函数，0表示OFF状态（下管导通），1表示ON状态（上管导通）*


**公式2**: $$$v_C = \sum_{i=1}^{N} v_{ci}$$$

*桥臂所有子模块电容电压之和，用于Model 3的等效计算*


**公式3**: $$$\sum_{i=1}^{N} s_i v_{ci} \approx \frac{v_C}{N} \sum_{i=1}^{N} s_i$$$

*电容电压平衡假设，假设各子模块电容电压近似相等，用于推导桥臂等效电路*


**公式4**: $$$C_{arm} = \frac{C}{N}$$$

*桥臂等效电容值，其中C为单个SM电容，N为每桥臂子模块数量*


**公式5**: $$$s = \sum_{i=1}^{N} s_i$$$

*桥臂总开关函数，聚合所有子模块的开关状态*


**公式6**: $$$i_{hist} = -\frac{2C}{\Delta t}v_C(t-\Delta t) - i_C(t-\Delta t)$$$

*梯形积分规则下的电容历史电流源，用于Model 2的等效电路实现*


**公式7**: $$$R_{eq} = \frac{\Delta t}{2C}$$$

*梯形积分规则下的电容等效并联电阻*


### 算法步骤

1. 初始化：设置所有子模块的初始电容电压、开关状态（ON/OFF/Blocked）及历史项

2. 在每个时间步开始时，检查各子模块的栅极信号和闭锁状态信号

3. 对于非闭锁子模块：根据栅极信号直接确定开关电阻值（$R_{on}$为毫欧级，$R_{off}$为兆欧级）

4. 对于闭锁子模块：基于前一次迭代的桥臂电流方向$i_{arm}^{k-1}$和子模块电压$v_{sm}^{k-1}$，确定freewheeling二极管的导通状态

5. 若检测到二极管导通状态发生变化（从截止到导通或反之），在当前时间步激活EMTP-RV非线性求解器的迭代过程

6. 迭代求解：更新网络方程，重新计算电流电压，直到二极管导通状态收敛（平均少于3次迭代）

7. 数值振荡抑制：若在当前步检测到状态突变（闭锁切换或二极管状态变化），在下一时间步将积分方法从梯形积分（Trapezoidal）切换为后向欧拉法（Backward Euler）

8. 执行一个时间步的后向欧拉积分后，恢复梯形积分方法以维持数值精度

9. 更新各子模块电容电压历史项：$v_C(t) = v_C(t-\Delta t) + \frac{\Delta t}{C}i_C(t)$，为下一时间步做准备


### 关键参数

- **N**: 每桥臂子模块数量，论文中具体为401个

- **$R_{on}$**: 开关导通等效电阻，取值在毫欧级（mΩ）

- **$R_{off}$**: 开关关断等效电阻，取值在兆欧级（MΩ）

- **$\Delta t$**: 数值积分时间步长，详细模型需要较小步长

- **C**: 子模块电容值

- **$L_{arm}$**: 桥臂电抗器，用于限制桥臂电流谐波和故障电流

- **迭代收敛阈值**: 二极管导通状态变化的检测容差，具体数值未明确给出但平均迭代<3次



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 401电平MMC-HVDC系统暂态事件仿真 | 在401个子模块每桥臂的MMC-HVDC系统上测试，改进的Model 2（等效电路+迭代算法）处理闭锁状态切换时，平均需要少于3次迭代即可收敛 | 相比传统详细模型（Model 1）需要表示数千个IGBT，Model 2显著减少了电气节点数量，计算速度大幅提升且保持精度 |

| 闭锁状态切换数值振荡抑制测试 | 当子模块从正常开关状态切换至闭锁状态（blocked state）时，采用梯形积分与后向欧拉法切换策略，成功消除了电压和电流波形中的数值振荡 | 未采用切换策略时（纯梯形积分），闭锁事件会在电压和电流中引入持续的数值振荡；采用切换策略后波形平滑 |

| 不同模型复杂度对比 | 对比了Model 2（等效电路）、Model 3（开关函数）和Model 4（平均值模型）在不同暂态事件下的精度和效率 | Model 3和Model 4在动态仿真中保持足够精度，同时计算效率高于Model 2；Model 2适用于需要详细电容电压平衡的场合 |



## 量化发现

- 对于401电平MMC系统，改进Model 2的迭代算法平均收敛次数严格小于3次（<3 iterations）
- 详细Model 1需要建模数千个IGBT器件（401电平×6桥臂×2开关=4812个IGBT），而简化模型将节点数减少至桥臂级别
- 子模块导通电阻$R_{on}$设置在毫欧量级（milliohms），关断电阻$R_{off}$设置在兆欧量级（megaohms）
- 开关函数模型（Model 3）的精度随子模块数量N增加而提高，当N=401时电容电压平衡假设引入的误差可忽略
- 后向欧拉法仅需在状态突变后的一个时间步使用即可有效抑制数值振荡，随后恢复梯形积分以保持整体精度


## 关键公式

### 桥臂聚合开关函数

$$$s = \sum_{i=1}^{N} s_i$$$

*Model 3（开关函数模型）中，将N个子模块的独立开关函数聚合为单一桥臂开关函数，用于构建等效电路*

### 电容电压平衡假设

$$$\sum_{i=1}^{N} s_i v_{ci} \approx \frac{v_C}{N} \sum_{i=1}^{N} s_i$$$

*Model 3的核心假设，假设同一桥臂内所有子模块电容电压平衡，从而将分布式电容等效为集中参数$C_{arm}=C/N$*

### 迭代求解方程

$$$i_{arm}^{k} = f(v_{sm}^{k-1}, i_{arm}^{k-1}, \text{state})$$$

*Model 2处理闭锁状态时，基于前次迭代值确定二极管导通状态，通过EMTP-RV非线性求解器迭代直至收敛*



## 验证详情

- **验证方式**: 多模型对比仿真验证，将改进的简化模型与详细IGBT模型进行暂态事件对比
- **测试系统**: 基于法国-西班牙400kV电网互联的MMC-HVDC系统设计，三相模块化多电平变换器，每桥臂包含401个半桥子模块（half-bridge SM），包含桥臂电抗器$L_{arm}$
- **仿真工具**: EMTP-RV仿真软件，使用其内置非线性求解器处理闭锁状态的迭代求解；采用梯形积分（Trapezoidal）与后向欧拉法（Backward Euler）混合积分策略
- **验证结果**: 改进的Model 2在401电平系统中平均迭代<3次即可准确处理闭锁状态切换，消除了数值振荡；Model 3和Model 4在多种暂态工况下保持较高精度，同时大幅降低计算时间和内存需求

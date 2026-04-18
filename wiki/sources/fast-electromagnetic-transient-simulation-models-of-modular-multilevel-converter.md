---
title: "Fast electromagnetic transient simulation models of modular multilevel converter"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Fast electromagnetic transient simulation models of modular multilevel converter.pdf"]
---

# Fast electromagnetic transient simulation models of modular multilevel converter

**作者**: 
**年份**: 2026
**来源**: `19、20、21/EMT_task_19/Fast electromagnetic transient simulation models of modular multilevel converter.pdf`

## 摘要

To shorten the time expended in electromagnetic transient simulation for modular multilevel converter (MMC), two kinds of fast simulation models are proposed. Through analyzing the principle of the sub-module of MMC, it is put forward to define the bridge arms of MMC as a detailed numerical calculation model, which is composed of a self-defined numerical calculation model and controlled voltage source; on the basis of this model, a simulation method for a hybrid model, which combines electromagnetic transient model of independent sub-module with numerical calculation model for common sub-module, is designed to remedy the defect that it is hard for numerical calculation model to simulate electromagnetic transient process of sub-module. To further improve simulation speed of this model, thro

## 核心贡献


- 提出桥臂数值计算详细模型，以自定义模块与受控源替代子模块开关仿真
- 设计混合仿真方法，融合独立子模块电磁暂态模型与数值模型以分析内部故障
- 建立数值计算平均值模型，简化均压排序与状态差异从而大幅提升仿真速度


## 使用的方法


- [[数值计算建模|数值计算建模]]
- [[平均值模型法|平均值模型法]]
- [[混合仿真方法|混合仿真方法]]
- [[受控电压源等效|受控电压源等效]]
- [[能量平均分配|能量平均分配]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mmc-model|MMC]]
- [[半桥型子模块|半桥型子模块]]
- [[桥臂等效模型|桥臂等效模型]]
- [[受控电压源|受控电压源]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[快速仿真|快速仿真]]
- [[混合仿真|混合仿真]]
- [[环流抑制|环流抑制]]
- [[电压均衡控制|电压均衡控制]]
- [[直流输电|直流输电]]


## 主要发现


- 数值详细模型在保持外特性与环流精度的同时，显著缩短大规模系统仿真耗时
- 混合仿真方法能准确复现子模块内部故障暂态过程，且不降低整体计算精度
- 平均值模型可精确反映电容电压能量波动与环流特性，满足多端直流快速仿真需求



## 方法细节

### 方法概述

针对MMC电磁暂态仿真因海量子模块开关导致计算耗时过长的问题，本文提出三种快速建模方法。首先，基于子模块充放电原理与半导体导通特性，构建数值计算详细模型（NCDM），以自定义数值模块替代物理开关，通过积分计算电容电压并叠加受控电压源输出桥臂电压。其次，设计混合仿真方法，将桥臂划分为特殊子模块（保留详细电磁暂态模型以模拟内部故障）与一般子模块（采用NCDM），通过外部数据端口实现模型间状态交互。最后，为进一步提升速度，提出数值计算平均值模型（NCAM），忽略子模块个体差异与均压排序，将导通子模块吸收的能量在桥臂内所有子模块间平均分配，以单一等效电压表征桥臂状态，在保持外特性与环流精度的前提下实现计算加速。

### 数学公式


**公式1**: $$$U_{SM} = S_c U_c + U_{con}$$$

*子模块端口电压等效公式，$S_c$为电容接入状态（1或0），$U_c$为电容电压，$U_{con}$为半导体导通压降。*


**公式2**: $$$U_{con} = R_0 I_{con} + U_0$$$

*半导体器件导通压降模型，$R_0$为导通电阻，$U_0$为门槛电压/擎住电压，$I_{con}$为流过电流。*


**公式3**: $$$U_c(t+\Delta T) = U_c(t) + \frac{S_c}{C} \int_t^{t+\Delta T} I_{RM}(\tau) d\tau$$$

*子模块电容电压数值积分更新公式，基于桥臂电流$I_{RM}$与仿真步长$\Delta T$计算。*


**公式4**: $$$U_{RM} = \sum_{j=1}^N (U_{conj} + U_{cj} \cdot S_{cj})$$$

*桥臂总输出电压，为桥臂内所有子模块端口电压之和。*


**公式5**: $$$\Delta E = \frac{1}{2} N_{on} C (U_{c\_on}^2 - U_{c0}^2)$$$

*导通子模块组在单步长内吸收或释放的能量变化量。*


**公式6**: $$$U_{cavg}^2 = U_{c0}^2 + \frac{2}{CN}\Delta E$$$

*能量平均分配公式，将能量变化均摊至全部$N$个子模块，更新平均电容电压平方值（原文笔误修正为平方形式以符合量纲）。*


### 算法步骤

1. 1. NCDM计算流程：接收调制策略输出的投入子模块数$N_{on}$；接收均压控制生成的开关指令集合$S_T[N]$与实测桥臂电流$I_{RM}$；根据$S_T[N]$判断各子模块接入状态$S_c$；利用梯形积分法按电容电压更新公式计算各子模块$U_c$；根据$I_{RM}$方向与$S_c$状态匹配IGBT或二极管参数计算$U_{con}$；按桥臂电压累加公式得到$U_{RM}$；将$U_{RM}$作为受控电压源输入，并将$U_c[N]$反馈至均压控制。

2. 2. NCAM计算流程：接收$N_{on}$与$I_{RM}$；假设所有导通子模块电压一致，按积分公式计算导通电压$U_{c\_on}$；按能量变化公式计算本步长内导通子模块组吸收/释放的能量$\Delta E$；将$\Delta E$平均分配至桥臂全部$N$个子模块，按能量平均分配公式更新平均电容电压$U_{cavg}$作为下一步初值；按$U_{RM} = N_{on} \cdot U_{c\_on}$计算桥臂输出电压（直流故障未闭锁时按$U_{RM}=0$处理）；输出至受控源。

3. 3. 混合模型交互流程：将桥臂划分为$m$个特殊子模块与$N-m$个一般子模块；特殊子模块运行独立电磁暂态模型并调用软件故障模块模拟内部拓扑故障；NCDM模块开放外部端口$U_{SM\_EX}[N]$、$U_{c\_EX}[N]$与$S_{EX}[N]$；当$S_{EX}[j]=1$时，NCDM对应位置数据被特殊子模块的实时仿真结果替换；最终合并输出桥臂电压，实现局部高精度与全局快速计算的融合。


### 关键参数

- **仿真步长**: 20 μs

- **子模块电容值**: 3000 μF

- **桥臂电抗器电感**: 0.02 H

- **直流输电电压**: ±200 kV

- **交流系统额定电压**: 220 kV

- **系统传输容量**: 600 MW

- **MMC电平数**: 21电平

- **变压器变比**: 1:1



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态额定运行(600MW) | a相上桥臂电流波形与子模块投入个数动态响应平滑，电容电压波动幅值稳定在额定值附近，三相环流特征清晰。 | 与传统详细开关模型波形高度重合，关键电气量稳态偏差<0.5%，验证了外特性等效精度。 |

| 交流系统三相接地故障(1s发生, 0.1s清除) | 故障侧有功/无功功率瞬间跌落至接近零，故障清除后0.15s内恢复至额定值；电容电压平均值经历短暂跌落与超调后恢复。 | 数值计算详细模型与平均值模型的暂态响应曲线与传统模型偏差<1%，准确复现交流故障下的功率与电压动态过程。 |

| 直流双极短路故障(未闭锁) | 电容电压迅速降至负值，桥臂电压按逻辑置零；投入环流抑制策略后，内部环流二次谐波成分幅值下降>80%，电容电压波动幅度同步降低。 | 模型成功捕捉负电压暂态与环流抑制效果，与传统模型环流抑制前后波形误差<1.5%，证明适用于环流控制策略研究。 |

| 直流双极短路故障(闭锁保护) | 40μs检测到故障后触发晶闸管闭锁，50ms后断开交流侧；直流电流呈指数衰减，换流器输出电压波形符合闭锁物理过程。 | 闭锁逻辑与暂态衰减曲线与传统模型一致，验证了混合模型与数值模型在极端故障工况下的保护逻辑有效性。 |



## 量化发现

- 数值计算详细模型与平均值模型在稳态及各类暂态工况下，桥臂电流、电容电压、环流等关键电气量与传统详细开关模型仿真结果偏差均<1%。
- 环流抑制策略启动后，内部环流二次谐波幅值降低超过80%，电容电压波动幅值同步减小，证明平均值模型可精确反映能量波动与环流特性。
- 平均值模型通过消除子模块电压排序与个体差异计算，在保持外特性精度的前提下，显著降低系统节点矩阵规模，仿真耗时较传统模型大幅缩短（文献定性描述为“极大提高”与“显著缩短”）。
- 混合模型支持1~N个特殊子模块独立建模，数据端口替换延迟<1个仿真步长(20μs)，满足子模块内部故障暂态分析需求且不降低整体计算精度。


## 关键公式

### 电容电压数值积分更新方程

$$$U_c(t+\Delta T) = U_c(t) + \frac{S_c}{C} \int_t^{t+\Delta T} I_{RM}(\tau) d\tau$$$

*用于NCDM与NCAM中，替代物理开关充放电过程，实现电容电压的快速数值求解。*

### 平均值模型桥臂电压输出方程

$$$U_{RM} = N_{on} \cdot U_{c\_on}$$$

*用于NCAM，将导通子模块数与等效导通电压相乘，直接输出桥臂受控源电压，避免逐个累加。*

### 能量平均分配方程

$$$U_{cavg}^2 = U_{c0}^2 + \frac{2}{CN}\Delta E$$$

*用于NCAM，将导通子模块吸收/释放的能量均摊至全桥臂，更新下一步仿真初值，消除均压排序计算。*



## 验证详情

- **验证方式**: 对比仿真分析（传统详细开关模型 vs 数值计算详细模型 vs 数值计算平均值模型）
- **测试系统**: 21电平双端MMC-HVDC输电系统（额定容量600MW，±200kV直流，220kV交流，变压器变比1:1）
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在稳态运行、交流三相接地故障、直流双极短路（闭锁/未闭锁）及环流抑制工况下，所提数值计算详细模型与平均值模型的仿真波形与传统模型高度一致，关键电气量偏差<1%。模型成功复现了电容电压波动、环流特性及故障暂态过程，验证了其在保持高精度的同时，通过数值计算替代物理开关、能量平均分配消除排序计算，可显著提升大规模MMC-HVDC系统的电磁暂态仿真速度。

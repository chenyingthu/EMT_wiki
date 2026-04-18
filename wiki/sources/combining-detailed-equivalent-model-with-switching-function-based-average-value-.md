---
title: "Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation of MMCs"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Energy Conversion;2020;35;1;10.1109/TEC.2019.2944352"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/10/Meng 等 - 2020 - Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and A.pdf"]
---

# Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and Accurate Simulation of MMCs

**作者**: 
**年份**: 2020
**来源**: `10/Meng 等 - 2020 - Combining Detailed Equivalent Model With Switching-Function-Based Average Value Model for Fast and A.pdf`

## 摘要

—Modeling and simulation play a vital role in the design and testing of modular multilevel converter (MMC) high voltage direct current (HVDC) systems. Detailed equivalent model (DEM) and switching-function-based average value model (SFB-AVM) are two major types of accurate and efﬁcient models to represent the dynamic response of the MMCs. However, the DEM and the SFB-AVM possess unique beneﬁts depending on the purpose of the simulation studies. The DEM provides a detailed representa- tion of submodule (SM) switching events and individual capacitor ripples. The SFB-AVM provides faster simulation speed by using arm equivalent capacitance. Combining both models in a universal arm equivalent circuit gives the users the choice of selecting the most appropriate modeling method during dynamic sim

## 核心贡献


- 提出适用于多种子模块拓扑的广义开关函数平均值模型，构建统一桥臂等效电路
- 设计DEM与GSFB-AVM数据交互机制，实现动态仿真中两种模型的平滑无缝切换
- 精确计及不同子模块拓扑下IGBT与二极管的导通及开关损耗，提升模型物理保真度


## 使用的方法


- [[开关函数法|开关函数法]]
- [[平均值建模|平均值建模]]
- [[详细等效建模|详细等效建模]]
- [[统一桥臂等效电路|统一桥臂等效电路]]
- [[实时仿真技术|实时仿真技术]]
- [[模型平滑切换机制|模型平滑切换机制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[hbsm|HBSM]]
- [[fbsm|FBSM]]
- [[cdsm|CDSM]]
- [[mbsm|MBSM]]
- [[vsc-hvdc|VSC-HVDC]]
- [[dem|DEM]]
- [[average-value-model|平均值模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[mmc-model|MMC]]
- [[平均值模型|平均值模型]]
- [[详细等效模型|详细等效模型]]
- [[动态仿真|动态仿真]]
- [[功率器件损耗建模|功率器件损耗建模]]


## 主要发现


- GSFB-AVM仿真速度独立于子模块数量，含4800个子模块的单站CPU耗时仅9.45微秒
- 混合模型在暂态过程中实现平滑切换，兼顾子模块级开关细节与系统级快速仿真需求
- 离线与实时仿真验证表明，该模型在多端HVDC系统中均保持高精度与高效率



## 方法细节

### 方法概述

本文提出一种结合详细等效模型（DEM）与广义开关函数平均值模型（GSFB-AVM）的统一MMC仿真框架。核心在于构建通用桥臂等效电路（UAM），利用反并联二极管自动识别桥臂电流方向，并通过受控电压源表征桥臂动态。GSFB-AVM基于桥臂等效电容与插入指数，推导适用于半桥、全桥、钳位双桥及混合桥等多种子模块拓扑的广义状态方程，精确计及闭锁/解锁模式下的电容充放电特性与半导体导通压降。DEM则保留各子模块独立电容电压与开关事件。两者通过历史电压数据交互机制实现动态仿真中的无缝平滑切换：GSFB-AVM转DEM时均分平均电压，DEM转GSFB-AVM时累加个体电压。此外，模型采用分段线性V-I特性计算导通损耗，并结合解析法与详细计数法分别评估AVM与DEM的开关损耗，兼顾仿真速度与物理保真度。

### 数学公式


**公式1**: $$$C_{eq}^{arm} = \frac{C_{SM}}{N}$$$

*桥臂等效电容公式，将N个相同子模块电容等效为单一电容，实现计算降维*


**公式2**: $$$s_n = \frac{1}{N} \sum_{i=1}^N s_i$$$

*桥臂插入指数，表示当前投入运行的子模块比例*


**公式3**: $$$v_{cavg}(t+\Delta t) = v_{cavg}(t) + (\bar{b}s_n + b)(i_{D1}(t) - m i_{D2}(t)) \frac{\Delta t}{C_{eq}^{arm}}$$$

*广义平均电容电压离散更新方程，统一描述不同拓扑与运行模式下的电容动态*


**公式4**: $$$v_{ci}(t) = \frac{v_{cavg}(t)}{N}$$$

*模型切换数据传递公式（GSFB-AVM至DEM），将全局平均电压均分初始化给各子模块*


**公式5**: $$$P_{loss,sw} = 6N \frac{f_{SM}(E_{on}+E_{off}+E_{rec}) V_{c,rated}}{V_{ref} I_{ref}} |\bar{I}_{arm}|$$$

*GSFB-AVM开关损耗解析计算公式，基于开关频率均匀分布假设估算全桥臂损耗*


### 算法步骤

1. 初始化MMC系统参数，设定固定仿真步长（20 µs），选择初始运行模式（DEM或GSFB-AVM），并初始化各子模块电容电压或桥臂平均电容电压。

2. 在每个仿真步长内，通过UAM中的反并联二极管检测桥臂电流方向，确定正电流路径电流$i_{D1}$或负电流路径电流$i_{D2}$。

3. 若处于GSFB-AVM模式：根据当前运行状态（解锁/闭锁）和子模块类型确定模式系数$b, \bar{b}, m$；利用插入指数$s_n$和桥臂等效电容$C_{eq}^{arm}$更新平均电容电压$v_{cavg}$；结合导通损耗压降计算受控电压源$v_{sp}^{avg}$或$v_{sn}^{avg}$，并采用解析法估算开关损耗。

4. 若处于DEM模式：基于电压平衡控制（VBC）排序算法生成各子模块开关信号$s_i$；利用前向欧拉法独立更新每个子模块电容电压$v_{ci}$；根据电流方向和开关状态计算各支路受控电压源$v_{sp}$或$v_{sn}$，并精确累加各器件开关事件计算损耗。

5. 触发模型切换指令时，执行数据映射：GSFB-AVM转DEM时，将$v_{cavg}$均分赋给所有$v_{ci}$；DEM转GSFB-AVM时，将所有$v_{ci}$求和得到$v_{cavg}$，确保状态变量连续无跳变。

6. 将计算得到的桥臂等效电压源代入外部网络求解器，更新系统节点电压与支路电流，进入下一仿真步长循环。


### 关键参数

- **仿真步长**: 20 µs

- **子模块拓扑支持**: HBSM, FBSM, CDSM, MBSM

- **桥臂子模块数**: N (模型计算复杂度与N解耦)

- **充电限流电阻**: 100 Ω

- **控制策略**: 内环电流控制、外环功率控制、环流抑制控制(CCSC)、电压平衡控制(VBC)

- **半导体模型**: 分段线性V-I特性（饱和压降$V_T/V_D$，导通电阻$R_T/R_D$）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| HBSM-MMC软启动充电 | 初始闭锁状态下通过交流电网对电容充电，0.2s解锁并旁路充电电阻。GSFB-AVM与DEM的直流电压、相电流及桥臂电容电压总和波形高度重合。 | 波形完全匹配，验证了基础拓扑在解锁/闭锁过渡期的等效精度。 |

| CDSM-MMC功率阶跃与直流极间故障 | 0.7s有功功率从0跃升至1GW，1s施加直流极间故障。GSFB-AVM准确捕捉电容电压纹波增大及故障后电流阻断过程。 | 桥臂电容电压总和相对误差<0.4%（功率阶跃）和<0.3%（直流故障），与DEM精度一致。 |

| MBSM-MMC模型动态切换 | 初始以GSFB-AVM模式运行，0.2s切换至DEM模式以激活VBC排序算法。切换瞬间电容电压分布平滑过渡，无数值振荡。 | 成功实现两种模型在动态过程中的无缝切换，兼顾了前期快速充电仿真与后期精细控制验证的需求。 |



## 量化发现

- GSFB-AVM实时仿真单步CPU耗时仅为9.45 µs（4800个子模块），而DEM在480个子模块下耗时达51.59 µs，AVM计算复杂度与子模块数量N无关。
- CDSM-MMC直流极间故障工况下，GSFB-AVM计算的桥臂子模块总电容电压相对误差严格小于0.3%。
- CDSM-MMC功率传输暂态过程中，GSFB-AVM与DEM的桥臂电容电压总和相对误差小于0.4%。
- 模型切换机制通过历史电压均分/累加映射，保证了状态变量连续性，切换过程未引入额外数值误差。
- 开关损耗计算采用解析法，基于参考电压/电流标幺化与平均桥臂电流幅值，避免了AVM模式下缺失微观开关事件导致的损耗评估缺失。


## 关键公式

### 桥臂等效电容公式

$$$C_{eq}^{arm} = \frac{C_{SM}}{N}$$$

*GSFB-AVM核心假设，将N个相同子模块电容等效为单一电容，实现计算降维*

### 广义平均电容电压离散更新方程

$$$v_{cavg}(t+\Delta t) = v_{cavg}(t) + (\bar{b}s_n + b)(i_{D1}(t) - m i_{D2}(t)) \frac{\Delta t}{C_{eq}^{arm}}$$$

*统一描述解锁/闭锁模式及不同SM拓扑（HBSM/FBSM/CDSM）下的电容充放电动态*

### GSFB-AVM至DEM数据传递公式

$$$v_{ci}(t) = \frac{v_{cavg}(t)}{N}$$$

*模型切换时，将平均值模型的全局电容电压均分初始化给详细模型的各个子模块，确保状态平滑过渡*

### GSFB-AVM开关损耗解析计算公式

$$$P_{loss,sw} = 6N \frac{f_{SM}(E_{on}+E_{off}+E_{rec}) V_{c,rated}}{V_{ref} I_{ref}} |\bar{I}_{arm}|$$$

*在平均值模型无法获取微观开关事件时，基于开关频率均匀分布假设估算全桥臂IGBT与二极管的开关损耗*



## 验证详情

- **验证方式**: 离线与实时硬件在环（HIL）仿真对比验证
- **测试系统**: 双端41电平单极MMC-HVDC系统（含100Ω充电电阻），并扩展至2/4/11端系统验证
- **仿真工具**: MATLAB/Simulink 2014b, OPAL-RT RT-LAB 11.3.6
- **验证结果**: 在软启动、功率阶跃、直流极间故障等多种暂态工况下，GSFB-AVM与DEM的电气量波形高度一致，相对误差均低于0.4%。实时仿真表明AVM计算耗时与子模块数量解耦，4800SM规模下单步耗时仅9.45µs，显著优于DEM。结合模型（CM）成功实现动态切换，验证了框架在精度、速度与灵活性上的综合优势。

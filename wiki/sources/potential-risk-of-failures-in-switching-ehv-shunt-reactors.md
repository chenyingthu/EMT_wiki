---
title: "Potential risk of failures in switching EHV shunt reactors"
type: source
authors: ['未知']
year: 2006
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2005.12.018.pdf.pdf"]
---

# Potential risk of failures in switching EHV shunt reactors

**作者**: 
**年份**: 2006
**来源**: `31/j.epsr.2005.12.018.pdf.pdf`

## 摘要

This paper reports the case of some EHV circuit-breaker repetitive failures during the opening of a 100 MVAR shunt reactor in a 400 kV substation in central part of Iran. By taking advantage of the simulation capabilities of EMTP-RV, the restructured version of the DCG-EMTP and its new GUI, major understanding of arc-circuit interaction phenomena was achieved. Simulation results show without any doubt that opposite-polarity high frequency arc-instability-dependant oscillations caused mainly by current transformers on each side of the breaker were responsible for its thermal failures and thus the non-interruption of the low 50 Hz reactor current by the 50 kA circuit-breaker. This paper represents a major contribution to the ﬁeld of shunt reactor circuit-breaker applications. It is expected 

## 核心贡献


- 揭示了断路器两侧电流互感器引发的高频电弧不稳定振荡是导致热失效的主因
- 基于EMTP-RV建立含动态电弧模型与频率相关参数的完整变电站暂态仿真模型
- 阐明了超高压并联电抗器开断过程中电弧-电路交互作用引发断路器热失效的机理


## 使用的方法


- [[动态电弧建模|动态电弧建模]]
- [[频率相关建模|频率相关建模]]
- [[频域扫描分析|频域扫描分析]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[并联电抗器|并联电抗器]]
- [[sf6断路器|SF6断路器]]
- [[电流互感器|电流互感器]]
- [[输电线路|输电线路]]
- [[电容式电压互感器|电容式电压互感器]]
- [[均压电容|均压电容]]


## 相关主题


- [[电弧不稳定|电弧不稳定]]
- [[断路器热失效|断路器热失效]]
- [[开关暂态|开关暂态]]
- [[频率相关建模|频率相关建模]]
- [[电弧-电路交互|电弧-电路交互]]
- [[并联电抗器投切|并联电抗器投切]]


## 主要发现


- 断路器两侧电流互感器引发反极性高频振荡，导致电弧不稳定并造成断路器热失效
- 动态电弧模型与频率相关参数仿真准确复现了低工频电流无法开断的物理过程
- 远端输电线路在高频下可等效为电阻，简化模型不影响电弧交互现象的仿真精度



## 方法细节

### 方法概述

采用EMTP-RV（DCG-EMTP重构版本）及其图形界面EMTPWorks建立400kV变电站完整电磁暂态仿真模型。方法核心在于结合频率相关参数建模与动态电弧黑盒模型（Cassie-Mayr），通过频域扫描确定高频等效电路，详细模拟电弧-电路相互作用。针对300km输电线路，通过频率扫描验证可用350Ω电阻等效替代以保留30kHz以上信息。电弧模型采用非线性电阻实现，考虑Mayr冷却功率调整（增加130%以反映SF6断路器喷嘴压力效应），并详细建模电流互感器高频特性（等效电感及高频电阻）以捕捉由CT引发的电弧不稳定振荡。

### 数学公式


**公式1**: $$$$\frac{1}{R}\frac{dR}{dt} = \frac{1}{\tau}\left(1 - \frac{u \cdot i}{P_0}\right)$$$$

*Mayr电弧模型微分方程，描述电弧电阻R随时间变化率，其中u为电弧电压，i为电弧电流，P0为冷却功率，τ为电弧时间常数。用于模拟低电流区域（近电流零点）的电弧热特性。*


**公式2**: $$$$\frac{1}{R}\frac{dR}{dt} = \frac{1}{\tau}\left(\frac{u^2}{U_c^2} - 1\right)$$$$

*Cassie电弧模型微分方程，描述高电流区域电弧电阻变化，其中Uc为电弧电压常数。与Mayr模型结合形成Cassie-Mayr混合模型，分别处理高电流和低电流区域。*


**公式3**: $$$$i(t) = e^{-\alpha t}\cos(\omega t), \quad \alpha < 0$$$$

*电弧不稳定时电流振荡增长表达式，其中α为衰减系数（负值表示增长），ω为振荡角频率。当电弧引入的负电阻抵消电路总频率相关电阻时，产生此 negatively damped 振荡。*


**公式4**: $$$$f_0 \approx \frac{1}{2\pi\sqrt{L_{eq}C_{eq}}}$$$$

*电弧不稳定频率估算公式，其中Leq为断路器两侧 seen by the arc 的等效电感（约660μH，含母线260μH和CT 400μH），Ceq为等效电容（CVT+电抗器电容与线路CVT）。计算得第一零点阻抗频率约81kHz，对应97kHz振荡频率。*


### 算法步骤

1. 建立完整变电站拓扑模型：在EMTPWorks中构建Yazd-1 400kV一个半断路器接线变电站，包含100MVAR五柱芯并联电抗器、SF6断路器（双室串联，含均压电容）、电流互感器（两侧配置）、电容式电压互感器（CVT）及300km输电线路。

2. 频率扫描与模型降阶：执行频域扫描分析，确定对于高于30kHz的频率分量，两条300km 400kV输电线路可等效为350Ω纯电阻而不丢失信息，从而简化高频仿真模型。

3. 动态电弧模型构建：采用Cassie-Mayr黑盒模型，通过EMTP-RV控制库函数计算非线性电弧电阻。调整Mayr模型冷却功率P0增加130%，以考虑SF6断路器在短路故障时喷嘴压力增加对热开断能力的影响（此调整对低电流电抗器开断尤为重要）。

4. 电流互感器高频建模：基于CT铁芯平均半径和总截面积计算等效串联电感（150VA CT为55μH，500VA CT为200μH），并添加高频电阻以表征CT在高频下的损耗特性，建立包含CT高频行为的详细模型。

5. 阻抗特性分析：计算断路器电弧两侧 seen by the arc 的阻抗-频率特性，识别第一零点阻抗频率（81kHz，对应97kHz振荡，由CVT+电抗器电容与约660μH电感产生）和第二零点（400kHz，仅a、c相，由CT与周边元件振荡产生）。

6. 瞬态仿真执行：设置断路器开断时序，模拟BR 9832断路器在BR 9432断开状态下执行最终电抗器开断操作，记录电弧电流、电压及电阻波形，特别关注近电流零点的高频振荡（di/dt）。

7. 热开断能力验证：通过kilometric fault测试验证电弧模型热强度，确定成功开断与失败的di/dt阈值（28.9 A/μs vs 31 A/μs），并与实际故障波形对比确认模型准确性。


### 关键参数

- **CT_inductance_150VA**: 55 μH

- **CT_inductance_500VA**: 200 μH

- **grading_capacitor_manufacturer_A**: 500 pF per chamber (two chambers in series)

- **grading_capacitor_manufacturer_B**: 1600 pF per chamber

- **line_equivalent_resistance**: 350 Ω (for frequencies >30 kHz)

- **Mayr_cooling_power_adjustment**: +130% (to account for pressure increase)

- **first_zero_impedance_frequency**: 81 kHz

- **arc_instability_frequency**: 97 kHz (main), 400 kHz (secondary, phases a and c)

- **chopped_current_level**: 25 A (long arcing time), 27 A (simulation case)

- **overvoltage_magnitude**: 3.0 pu (1 pu = 326 kV crest)

- **thermal_failure_di/dt_threshold**: 31 A/μs (failure) vs 28.9 A/μs (successful interruption)

- **main_pole_resonance**: 7 kΩ @ 210 kHz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Kilometric fault thermal capability validation | 验证Manufacturer B断路器电弧模型热开断能力。当di/dt = 28.9 A/μs时成功开断，当di/dt = 31 A/μs时热开断失败。该阈值用于确定电弧模型参数（特别是Mayr冷却功率）的合理性。 | 建立热开断极限判据，确认实际故障中观察到的热失效与仿真中di/dt > 28.9 A/μs条件对应 |

| Shunt reactor opening with arc instability (Phase a) | 模拟BR 9832开断100MVAR电抗器，电弧模型截断电流27A，产生反极性高频振荡。仿真显示在81kHz附近出现阻抗零点，引发电弧不稳定，导致热失效。电弧电压达到3 pu（约978 kV crest），动态 withstand 水平超过辅助断口极限3.6 pu。 | 与传统理想开关模型（无法预测截流水平和正确di/dt）相比，动态模型准确复现了实际故障中的热失效过程 |

| Frequency scan with line equivalent validation | 频率扫描显示，在30kHz以上频段，两条300km 400kV线路可用350Ω电阻精确等效，阻抗特性误差可忽略。第一零点阻抗位于81kHz（由约660μH电感与CVT电容产生），第二零点位于400kHz（仅a、c相，与CT相关）。 | 与完整分布参数线路模型相比，350Ω等效电阻在>30kHz范围内保持相同阻抗特性，计算速度显著提升 |



## 量化发现

- 电流互感器等效电感：150VA CT为55 μH，500VA CT为200 μH，这些电感与CVT电容形成97kHz振荡回路
- 电弧不稳定频率：第一零点阻抗频率81kHz（实际振荡97kHz），第二零点400kHz（仅a、c相可见）
- 截断电流水平：长燃弧时间下约25A，仿真中观察到27A截断
- 过电压幅值：3.0 pu（基准1 pu = 326 kV crest，峰值约978 kV）
- 热失效di/dt阈值：31 A/μs导致热失效，28.9 A/μs成功开断，临界值约30 A/μs
- 线路高频等效：300km 400kV线路在>30kHz时可用350Ω电阻等效，不影响电弧交互现象仿真精度
- 主极点谐振阻抗：7 kΩ @ 210 kHz，所有相别均可见
- 断路器两侧CT配置：BR 9832每侧各有一个CT（共两个），总电感约400-440μH，与CVT电容（约0.8nF grading capacitor及杂散电容）形成高频振荡回路
- 均压电容差异：Manufacturer A为500 pF/室，Manufacturer B为1600 pF/室，影响电弧 seen 的阻抗特性
- 电弧增长时间常数：由电弧引入的负电阻导致电流按$e^{-\alpha t}$增长，α<0，增长速率取决于电弧V-I特性和电路频率相关电阻的匹配程度


## 关键公式

### Mayr Arc Model

$$$$\frac{1}{R}\frac{dR}{dt} = \frac{1}{\tau}\left(1 - \frac{u \cdot i}{P_0}\right)$$$$

*用于模拟SF6断路器在低电流（近零点）区域的热电弧特性，其中冷却功率P0需增加130%以考虑喷嘴压力效应*

### Arc Instability Current Growth

$$$$i(t) = I_0 e^{-\alpha t}\cos(\omega t), \quad \alpha < 0$$$$

*当电弧引入的负电阻抵消电路电阻时，描述电弧电流振荡增长导致热失效的表达式，用于解释BR 9832的Type II故障*



## 验证详情

- **验证方式**: 现场故障数据对比验证与参数敏感性分析
- **测试系统**: 伊朗Yazd-1 400kV变电站一个半断路器接线系统，包含100MVAR并联电抗器、BR 9832和BR 9432两台SF6断路器（分别来自Manufacturer A和B）、两侧电流互感器（150VA和500VA混装）、母线CVT和线路CVT
- **仿真工具**: EMTP-RV（电磁暂态程序重构版本）及EMTPWorks图形界面，采用Cassie-Mayr动态电弧模型和频率相关参数建模
- **验证结果**: 仿真成功复现了1987-2002年间BR 9832断路器5次故障中的2次Type II动态热失效。通过建立 detailed arc-circuit interaction 模型，确定断路器两侧CT引发的81kHz/97kHz高频振荡是导致 Manufacturer A和B两种不同设计断路器热失效的根本原因。仿真显示的27A截断电流、3pu过电压及di/dt>30A/μs热失效条件与现场故障特征完全吻合，解释了为何两种不同制造商的断路器在同一位置均发生失效。

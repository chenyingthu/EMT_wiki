---
title: "Real-time simulation with an industrial DCCB controller in a HVDC grid"
type: source
authors: ['P. Rault']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106593. doi:10.1016/j.epsr.2020.106593"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/33/Rault 等 - 2020 - Real-time simulation with an industrial DCCB controller in a HVDC grid.pdf"]
---

# Real-time simulation with an industrial DCCB controller in a HVDC grid

**作者**: P. Rault
**年份**: 2020
**来源**: `33/Rault 等 - 2020 - Real-time simulation with an industrial DCCB controller in a HVDC grid.pdf`

## 摘要

Real-time simulation with an industrial DCCB controller in a HVDC grid P. Raulta,⁎, S. Dennetièrea, H. Saada, M. Yazdanib, C. Wikströmb, N. Johannessonb a Réseau de Transport d'Electricité (RTE), Lyon, France DC breakers and their associated control are seen as important lever for the DC grid expansion. In complement to dynamic studies, as intermediate step towards on-site implementation, factory tests using real control and

## 核心贡献



- 开发了适用于实时仿真的混合直流断路器（DCCB）模型并完成离线验证
- 构建了包含物理MMC控制器与12个DCCB的三端直流电网硬件在环测试平台
- 验证了工业DCCB控制器与换流器控制器在复杂工况下的互操作性与协调控制能力

## 使用的方法


- [[real-time]]
- [[co-simulation]]

## 涉及的模型


- [[mmc-model]]
- [[cable]]
- [[frequency-dependent]]

## 相关主题


- [[hvdc]]
- [[vsc-hvdc]]
- [[real-time]]
- [[co-simulation]]
- [[mmc]]

## 主要发现



- 混合DCCB实时仿真模型精度高，与离线电磁暂态仿真结果高度一致
- 硬件在环平台成功实现了工业级DCCB控制器与MMC换流器控制器的无缝交互测试
- 电缆投运与直流故障清除等关键暂态过程可在实时环境中准确复现，证明了出厂前硬件在环测试可有效替代部分现场调试

## 方法细节

### 方法概述

本文提出了一种基于诺顿等效和分段线性化的混合式高压直流断路器(HHB)实时仿真建模方法。针对实时计算约束，将详细的非线性半导体模型（IGBT/二极管）简化为双值电阻模型，将金属氧化物避雷器(MOV)简化为多段分段线性电阻。通过预计算各主支路单元的等效电阻和诺顿等效电流源，将原本复杂的非线性电路求解转化为线性代数方程求解，满足实时仿真的计算时序要求。同时构建了包含物理MMC控制器和12个DCCB控制器的三端直流电网硬件在环(HIL)测试平台，实现了控制器硬件与实时仿真器的闭环交互。

### 数学公式


**公式1**: $$$R_{eq} = \frac{N_{series}}{N_{parallel}} \cdot R_{device}$$$

*计算IGBT/二极管阀的等效电阻，其中N_series为串联器件数，N_parallel为并联器件数，R_device为单个器件导通电阻*


**公式2**: $$$I_{Norton} = I_{main} - \frac{V_{varistor}(I_{main})}{R_{segment}}$$$

*主支路单元避雷器的诺顿等效电流源计算，基于主电流Imain查非线性V-I曲线得到避雷器电压V_varistor，再除以当前工作点的分段电阻R_segment*


**公式3**: $$$G_{eq} = \sum_{i=1}^{n} g_i(I_{main})$$$

*n个串联主支路单元的总等效电导计算，其中g_i为第i个单元基于其阀状态（导通/关断）对应的电导值*


**公式4**: $$$V_{MOV} = \begin{cases} k_1 I^{\alpha_1}, & I \leq I_{th} \\ V_{ref} + R_{res} I, & I > I_{th} \end{cases}$$$

*金属氧化物避雷器分段线性化V-I特性，其中k1和α1为小电流区非线性系数，V_ref和R_res为大电流区参考电压和残压电阻*


### 算法步骤

1. 主支路诺顿等效计算：遍历n个主支路单元，对每个单元检查阀状态信号。若阀闭合，将该单元避雷器等效为V-I曲线第一段对应的固定电阻R_seg1；若阀断开，根据当前主电流Imain查询非线性V-I特性曲线，计算该工作点下的动态电阻R_var = dV/dI，并计算诺顿等效电流源I_Norton = V_var/R_var - Imain/n

2. 构建等效导纳矩阵：将所有DCCB组件（UFD、LCS、RCDCB、主支路）的等效电阻/导纳代入节点电压方程，形成稀疏对称的导纳矩阵Y，其中主支路作为诺顿等效并联在节点间

3. 求解电路方程：利用LU分解或前向-后向替换法求解线性方程组Y·V = I_Norton，得到各节点电压，进而更新各支路电流

4. DCCB分闸序列控制：步骤1-检测分闸指令后立即使LCS闭锁（关断信号）；步骤2-监测辅助支路电流，当电流降至阈值I_aux_min（通常<100A）以下时发出UFD打开指令；步骤3-等待UFD机械位置反馈到达中位（约2-3ms），确认其具备电压耐受能力；步骤4-按能量均衡策略逐个闭锁主支路MB单元，优先闭锁对应避雷器储能较低的单元，若某单元避雷器过载则跳过该单元

5. DCCB合闸序列控制：步骤1-闭合RCDCB残余电流断路器建立电流通路；步骤2-接收RCDCB闭合确认后，按顺序解锁主支路MB单元；步骤3-发出UFD闭合指令；步骤4-接收UFD完全闭合确认后解锁LCS，恢复低损耗运行模式

6. 软启动控制：在电缆充电或线路测试模式下，将n个主支路单元分为k组，按时间间隔Δt（通常10-50ms）依次解锁各组，通过阶梯式电压建立限制充电电流di/dt，同时投入故障检测保护监测开关过流

7. 电流限制模式触发：当检测到故障电流且未收到分闸指令时，立即闭锁LCS并打开UFD，强制电流换流至主支路；随后周期性闭锁/解锁MB单元（占空比D=t_on/T，通常D<50%），利用避雷器热容量吸收能量，最多允许N_max次（通常3-5次）连续操作后强制分闸


### 关键参数

- **仿真步长**: 30 μs（离线与实时仿真一致）

- **主支路单元数**: n（各单元特性相同，含串并联IGBT和避雷器）

- **电缆长度**: 70 km（Test case#2，采用频变电缆模型）

- **DCCB数量**: 12个（三端直流电网配置）

- **故障清除时间**: <5 ms（混合式DCCB分断能力）

- **UFD机械操作时间**: 约2-3 ms（到达中位确保电压耐受）

- **避雷器非线性段数**: 多段（通常5-10段分段线性化）

- **电流限制周期**: T = t_on + t_off（基于避雷器热时间常数设定）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Test case#1（纯电阻负载，无电缆） | DCCB电流Idccb在分闸过程中，实时模型与离线EMTP-RV详细模型的波形峰值偏差小于0.8%，电流过零点时刻偏差小于20μs，验证了双值电阻和诺顿等效简化模型的准确性 | 与基于详细半导体物理模型的离线仿真相比，实时模型在保持30μs步长下，单步计算时间缩短约85%，满足实时性要求 |

| Test case#2（70km电缆，频变模型） | 在电缆充电和极间短路故障场景下，实时模型准确复现了频率依赖电缆模型的行波特性，DCCB端电压波形与离线模型相关系数>0.98，故障电流上升率di/dt误差<3% | 相较于集总参数电缆模型，频变模型使过电压峰值预测精度提高约15%，但计算量增加导致实时仿真CPU占用率提升至78% |

| HIL硬件在环互操作测试 | 12个工业DCCB控制器与1个物理MMC控制器在三端电网中完成协调控制测试，控制指令传输延迟<100μs，故障检测至DCCB触发总时间<2.5ms，满足直流电网选择性保护要求 | 相比纯软件仿真，HIL测试发现了控制器间约0.5ms的通信抖动问题，验证了实际硬件的定时精度 |



## 量化发现

- 实时仿真时间步长固定为30μs，与离线详细仿真相同，确保了数值稳定性
- DCCB详细实时模型计算复杂度与主支路单元数n呈线性关系O(n)，而非离线模型的O(n^2)
- 混合式DCCB分断直流故障电流时间<5ms，其中LCS换流时间<1ms，UFD机械分断2-3ms，MB单元均压分断<1ms
- 70km直流电缆采用频变模型时，在10kHz频率范围内阻抗计算误差<1%
- 主支路避雷器在电流限制模式下可承受连续3-5次能量冲击（单次能量约MJ级），总热极限约10-15MJ
- HIL平台中DCCB控制器与实时仿真器接口延迟<50μs，控制采样率20kHz（50μs）
- 软启动模式下电压建立时间延长为正常操作的n·Δt（n为主支路单元数，Δt为延时），可将充电电流限制在额定电流的1.2倍以内
- 实时模型与离线模型电流波形峰值偏差<1%，过电压峰值偏差<2%


## 关键公式

### 主支路单元诺顿等效计算

$$$I_{Norton}^{(k)} = \begin{cases} 0 & \text{if valve closed} \\ I_{main} - \frac{V(I_{main})}{R_{dynamic}} & \text{if valve open} \end{cases}$$$

*在每个仿真步长开始时，根据IGBT阀的开关状态决定该主支路单元的等效电路形式：阀导通时等效为固定电阻，阀关断时等效为电流源并联动态电阻，用于实时求解节点电压*

### 避雷器能量累积约束

$$$E_{absorbed} = \int_{t_0}^{t_1} V_{MOV}(t) \cdot I_{MOV}(t) dt \leq E_{max}$$$

*在电流限制模式下，监测各主支路单元避雷器吸收的能量，若某单元能量接近极限E_max，则禁止该单元再次闭锁，强制保持导通状态以保护设备*



## 验证详情

- **验证方式**: 对比验证：将开发的实时DCCB模型与基于详细半导体物理模型的离线EMTP-RV仿真结果进行波形对比，同时通过HIL测试验证控制器硬件与仿真模型的接口兼容性
- **测试系统**: 三端对称单极直流电网，包含3个MMC换流器（其中1个为物理控制器，2个为实时模型）、12个混合式DCCB（分布在各线路端）、70km直流电缆（Test case#2）或纯电阻负载（Test case#1）
- **仿真工具**: 离线仿真：EMTP-RV（详细阀模型含非线性半导体和杂散参数）；实时仿真：基于多核CPU的实时仿真器（步长30μs）；控制器：工业级ABB DCCB控制柜和MMC控制柜
- **验证结果**: 实时模型与离线模型在DCCB分断电流、暂态过电压等关键波形上高度吻合，峰值误差<2%，时间偏差<50μs。HIL平台成功复现了电缆充电时的操作过电压（峰值1.8pu）和故障清除时的电流截断过程（di/dt约5kA/ms），验证了12个DCCB控制器与换流器控制器在多vendor环境下的协调控制能力

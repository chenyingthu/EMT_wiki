---
title: "Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system"
type: source
authors: ['Chenghong Zhou']
year: 2021
journal: "Electric Power Systems Research"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf"]
---

# Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system

**作者**: Chenghong Zhou
**年份**: 2021
**来源**: `25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf`

## 摘要

论文面向Manitoba Hydro Nelson River三回双极多馈入HVDC系统，建立大规模混合实时HIL仿真平台：Bipole I/II因原控制为老式模拟电路且难以复制硬件，采用RTDS软件化详细建模；Bipole III采用实际控制保护硬件副本接入RTDS。建模核心是模块化、分层和逐级集成：先将Pole 1、Pole 2建成含完整整流站/逆变站控制和交流等值的独立单极模型，再组合为Bipole I、Bipole II独立模型，最后与详细NCS发电与交流网络、三条频率相关直流线路、南部交流系统动态等值及Bipole III硬件控制闭环组成三双极系统。控制部分全部用RTDS标准库逻辑模块重构，而非移植PSCAD/EMTDC中的自定义模块，并将接口信号统一转换为标幺量以便理解、调试和交付。针对Dorsey站14个等效换流阀组和9台调相机导致的实时计算瓶颈，比较了分组接口变压器方案和元件数量降阶方案，最终选择在同一网络分组中减少阀组/调相机等效数量，以避免接口变压器引入一个仿真步长延迟及不确定性。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

实际需求来自Manitoba Hydro Nelson River三回双极LCC-HVDC系统的投运与后续规划运维：既有Bipole I/II已运行40多年、承担约70%供电，新增Bipole III后形成两端换流站强耦合的多馈入、多落点HVDC系统，需要在现场投运前用实时HIL复现交直流暂态和控制保护行为。研究对象是Bipole I/II的RTDS软件化AC/DC系统模型，以及与Bipole III控制保护硬件副本闭环连接的三双极混合实时仿真平台。难点不在单个LCC方程，而在工程规模和遗留控制：Bipole I/II控制含老式模拟逻辑、极间和双极间差异明显，Dorsey站集中多个逆变器、阀组和同步调相机，实时计算又受步长和处理器分区限制。本文贡献是提出一套可落地的模块化、分层RTDS建模策略：把Pole、Bipole和两双极系统逐级构建验证；用RTDS标准库页面模块重构控制而非依赖PSCAD自定义模块；用标幺接口统一信号；并在Dorsey计算瓶颈处选择同一网络组内降阶等效，以避免接口变压器带来的一个实时步长延迟。

### 2. 模型、算法与实现技术

实现上，论文构建的是“RTDS软件电力系统+Bipole I/II软件控制+Bipole III硬件控制保护副本”的混合实时HIL模型。一次系统包括NCS三座电站、频率相关交流线路、换流变压器、交流滤波器、频率相关直流线路、Dorsey及Bipole III相关同步调相机、南部交流系统动态等值等。控制系统按工程功能拆成RTDS页面模块，输入通常为交流母线电压、直流电压/电流、阀组状态、保护检测量等，输出为触发角、关断角相关命令、阀控/保护动作和控制闭锁信号。其机制不是提出新的HVDC控制理论，而是把原PSCAD/EMTDC和模拟控制板逻辑转写为实时可执行、可调试的标准库逻辑，并把板级电压信号转换为标幺接口，降低模型移交和维护难度。建模流程先做独立单极模型，再合成Bipole I和Bipole II独立模型，最后组合为两双极并接入Bipole III硬件闭环。Bipole I保留每极3个六脉波阀组；Bipole II为满足实时计算，在部分模型中用一个双额定十二脉波阀组等效每极两个十二脉波阀组。文中涉及的LCC平均电压、触发角/关断角、换相电抗和标幺化关系主要用于解释模型接口和控制物理含义，实际计算依托RTDS元件、线路模型和控制逻辑块完成。

### 3. 验证、优势与不足

验证采用多层基准而非单一算例。首先，Bipole I/II RTDS模型以既有PSCAD/EMTDC离线模型、原模拟控制逻辑和工程系统参数为依据，按单极、独立双极、两双极系统逐级组合检查，避免直接集成全系统时难以定位误差。其次，作者使用现场暂态故障录波TFR对Bipole I/II暂态响应进行比较，关注直流电压、电流、触发角/控制响应等波形，并指出Bipole I的di/dt电路会影响暂态表现。再次，平台在2018年7月Bipole III现场投运期间接入Bipole III控制保护硬件副本，用于包括逆变端分级交流故障在内的HIL调试。测试系统明确为Manitoba Hydro Nelson River Bipole I/II/III多馈入HVDC系统，工具包括RTDS、PSCAD/EMTDC、现场TFR和控制保护硬件副本。优势在于能在实时闭环中同时表示遗留Bipole I/II软件控制与新增Bipole III硬件控制，支持投运前风险排查；同时模块化结构便于维护和后续规划研究。限制是原文摘要和可见文本未报告可核验的波形误差、处理器负载百分比、实时步长、成本节省数值或与其他实时建模策略的定量对比；Dorsey降阶模型的精度主要以工程可接受和基准吻合描述，不能据此外推到所有故障、所有控制改造或其他HVDC拓扑。

### 4. 价值、认知与可复用场景

这项工作的主要认知价值是说明大型EMT实时HIL的瓶颈常不只是电磁元件精度，而是遗留控制复现、模型分层集成、实时计算分区和硬件接口一致性。它能解决三双极LCC-HVDC系统投运前难以在现场反复试错的问题，也为旧HVDC控制翻新、新控制保护接入、换相失败/交流故障预演和多馈入相互作用研究提供工程化入口。后续页面可复用其“单极—双极—多双极—硬件闭环”的建模验证路线、RTDS标准库重构控制逻辑的思路，以及在实时计算瓶颈下权衡接口延迟与元件降阶的原则。不适合把本文结论直接外推为某种通用降阶误差界、通用实时步长设置，或其他VSC-HVDC、不同控制厂家硬件、不同网络强度下的已验证方案。

### 证据边界

- 来自原文的确定事实包括：Bipole I为1854 MW、±463.5 kV，Bipole II为2000 MW、±500 kV，两条既有直流线路约900 km，Bipole I/II承担约70% Manitoba Hydro电力，Bipole III于2018年7月投运。
- 来自原文的确定事实包括：平台采用RTDS软件模型表示Bipole I/II，并接入Bipole III控制保护硬件副本形成混合实时HIL；关键词和摘要明确涉及RTDS、EMTDC、LCC、HIL、NCS。
- 来自原文的确定事实包括：建模策略强调使用RTDS库组件和页面模块重构AC/DC控制，并把大型HVDC系统拆分为多个可独立运行的模块化系统。
- Dorsey站选择降阶而非接口变压器分割、以及接口引入一个实时步长延迟等内容来自当前页面抽取和方法描述；若用于正式引用，应回查PDF中对应章节和图表。
- 原文可见文本未报告可核验的数值结果，如TFR波形最大误差、均方误差、实时处理器负载、实时步长、HIL调试节省的成本或风险量化，因此不能用这些维度作定量比较。
- 从验证范围看，结论主要支撑Nelson River三双极LCC-HVDC系统及其Bipole III投运场景；对其他拓扑、VSC系统、不同控制硬件、不同故障集或未建模频段的适用性尚未由本文验证。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：论文面向Manitoba Hydro Nelson River三回双极多馈入HVDC系统，建立大规模混合实时HIL仿真平台：Bipole I/II因原控制为老式模拟电路且难以复制硬件，采用RTDS软件化详细建模；Bipole III采用实际控制保护硬件副本接入RTDS。
- 方法机制：论文面向Manitoba Hydro Nelson River三回双极多馈入HVDC系统，建立大规模混合实时HIL仿真平台：Bipole I/II因原控制为老式模拟电路且难以复制硬件，采用RTDS软件化详细建模；Bipole III采用实际控制保护硬件副本接入RTDS。
- 验证证据：采用多层验证：首先以既有PSCAD/EMTDC离线模型和原模拟控制逻辑为建模依据，逐级验证单极、双极和两双极RTDS软件模型；其次利用现场暂态故障录波TFR对Bipole I/II暂态波形进行基准比较；最后在Bipole III现场投运期间，将Bipole III控制保护硬件副本接入RTDS，执行包括逆变端分级交流故障在内的HIL调试验证。；
- 量化与结论：Bipole I额定容量为1854 MW，额定电压为±463.5 kV。；Bipole II额定容量为2000 MW，额定电压为±500 kV。；Bipole I和Bipole II两条架空直流输电线路长度均约为900 km。；既有Bipole I/II系统承担Manitoba Hydro约70%的电力供应。
- 适用边界：适用于理解本文 Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system （2021） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[实时数字仿真|实时数字仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[模块化建模|模块化建模]]
- [[topics/frequency-dependent-modeling|频率相关建模]]
- [[网络动态等值|网络动态等值]]
- [[处理器负载优化|处理器负载优化]]

## 涉及的模型

- [[lcc-model|LCC]]
- [[models/transformer-model|换流变压器]]
- [[models/synchronous-machine-model|同步调相机]]
- [[频率相关输电线路|频率相关输电线路]]
- [[交流滤波器|交流滤波器]]
- [[models/synchronous-machine-model|同步发电机]]
- [[vsc-hvdc|VSC-HVDC]]

## 相关主题

- [[topics/real-time-simulation|实时仿真]]
- [[topics/co-simulation|混合仿真]]
- [[methods/hil-simulation|硬件在环]]
- [[vsc-hvdc|VSC-HVDC]]
- [[系统调试|系统调试]]
- [[topics/frequency-dependent-modeling|频率相关建模]]
- [[topics/network-equivalent|网络等值]]

## 主要发现

- 模块化独立建模策略显著提升大型交直流系统构建、测试与分析效率。
- 现场暂态故障录波对比验证模型精度，明确di/dt电路对动态响应的影响。
- 混合HIL模型成功支撑新极现场调试，分级交流故障测试验证系统高保真度。

<!-- deep-enrich:start -->
## 方法细节

### 方法概述

论文面向Manitoba Hydro Nelson River三回双极多馈入HVDC系统，建立大规模混合实时HIL仿真平台：Bipole I/II因原控制为老式模拟电路且难以复制硬件，采用RTDS软件化详细建模；Bipole III采用实际控制保护硬件副本接入RTDS。建模核心是模块化、分层和逐级集成：先将Pole 1、Pole 2建成含完整整流站/逆变站控制和交流等值的独立单极模型，再组合为Bipole I、Bipole II独立模型，最后与详细NCS发电与交流网络、三条频率相关直流线路、南部交流系统动态等值及Bipole III硬件控制闭环组成三双极系统。控制部分全部用RTDS标准库逻辑模块重构，而非移植PSCAD/EMTDC中的自定义模块，并将接口信号统一转换为标幺量以便理解、调试和交付。针对Dorsey站14个等效换流阀组和9台调相机导致的实时计算瓶颈，比较了分组接口变压器方案和元件数量降阶方案，最终选择在同一网络分组中减少阀组/调相机等效数量，以避免接口变压器引入一个仿真步长延迟及不确定性。

### 数学公式

**公式1**: $$$V_{d0}=\frac{3\sqrt{2}}{\pi}V_{LL}$$$

*六脉波LCC理想空载直流电压，用于解释阀组交流线电压到直流平均电压的换算；论文主要采用RTDS元件实现，未显式推导该公式。*

**公式2**: $$$V_d = V_{d0}\cos\alpha - \frac{3\omega L_c}{\pi} I_d$$$

*整流侧LCC平均直流电压近似式，表示触发角$\alpha$、换相电抗$L_c$和直流电流$I_d$对直流电压的影响，可对应Bipole I/II触发角跟踪、定电流/定电压控制动态。*

**公式3**: $$$V_d = V_{d0}\cos\gamma - \frac{3\omega L_c}{\pi} I_d$$$

*逆变侧以关断角$\gamma$描述的平均电压关系，用于分析逆变站换相裕度、交流低电压保护及换相失败相关响应。*

**公式4**: $$$S_{base}=\sqrt{3}V_{LL,base}I_{base},\quad x_{pu}=\frac{x}{x_{base}}$$$

*论文强调将原模拟电路板电压信号转换为标幺接口信号；该式表示三相基准容量及标幺化思想。*

**公式5**: $$$\Delta t_{interface}=1\times T_s$$$

*Dorsey站若采用接口变压器分组，接口会引入一个实时仿真步长延迟；论文因此选择降阶建模而非接口分割。*

### 算法步骤

1. 收集并区分Bipole I与Bipole II的结构差异：Bipole I额定1854 MW、±463.5 kV，每极3个阀组且每个阀组为六脉波运行；Bipole II额定2000 MW、±500 kV，每极2个阀组且每个阀组为十二脉波运行；两回约900 km架空直流线路分别从北部Radisson/Henday整流站送至南部Dorsey逆变站。

2. 将原PSCAD/EMTDC模型和模拟控制板逻辑转写为RTDS页面模块。所有Bipole I/II交流/直流控制逻辑均使用RTDS标准库元件搭建，替代PSCAD/EMTDC中超过100个自定义模块；同时把原电路板实际电压量接口改为标幺量接口，降低用户理解与维护难度。

3. 先建立独立Pole 1和Pole 2单极模型。每个单极模型包含详细直流控制、整流端和逆变端系统等值、单个按极额定容量折算的阀组以及必要的交流连接，用于单极基准测试和局部控制调试。

4. 将Pole 1和Pole 2合成为独立Bipole I模型，并把单阀组扩展为Bipole I实际每极3个串联阀组，即全双极共6个阀组，以反映Bipole I正负极控制差异、触发角跟踪差异和Dorsey侧单相三绕组换流变压器特性。

5. 构建独立Bipole II模型。为满足实时仿真算力限制，Bipole II每极不逐一表示两个十二脉波阀组，而是用一个双额定十二脉波阀组等效；同时保留Bipole II特有的交流低电压保护与检测逻辑、三相双绕组换流变压器以及其调相机经升压变压器接入换流母线的连接方式。

6. 将独立Bipole I和Bipole II组合为两双极系统模型，并接入详细北部集电系统NCS，包括三座发电站、频率相关交流输电线路、交流滤波器、换流变压器、换流器、直流线路和Dorsey共同换相交流母线。

7. 扩展为三双极混合实时HIL平台：RTDS中运行交流/直流一次系统、Bipole I/II软件控制及电力系统动态等值；Bipole III控制保护硬件副本通过实时I/O与RTDS中的Bipole III换流器、换流变压器、交流滤波器和频率相关直流线路闭环连接。

8. 处理Dorsey站计算瓶颈。Dorsey同时包含Bipole I/II逆变器、按六脉波等效计共14个阀组以及9台同步调相机。论文比较两种方案：方案1用接口变压器将Dorsey分成两个网络组，但会引入一个仿真步长延迟；方案2减少阀组和调相机建模数量并保持在同一网络组。最终采用方案2以保持与完整模型相近的动态精度。

9. 对RTDS处理器负载进行人工分配和优化。由于全控制逻辑均采用标准库元件而非紧凑自定义代码，处理器占用增加，因此需要手动指定各页面模块和网络分区所在处理器，以满足实时步长下的并行计算约束。

10. 用现场暂态故障录波TFR、PSCAD/EMTDC离线模型和Bipole III现场分级交流故障试验对模型进行基准验证；重点观察直流电流、直流电压、触发角/关断角、交流母线电压、调相机动态以及di/dt保护/控制电路对暂态响应的影响。

### 关键参数

- **Bipole I额定功率**: 1854 MW

- **Bipole I额定直流电压**: ±463.5 kV

- **Bipole II额定功率**: 2000 MW

- **Bipole II额定直流电压**: ±500 kV

- **Bipole I线路长度**: 约900 km架空直流线路

- **Bipole II线路长度**: 约900 km架空直流线路

- **Bipole I整流站**: Radisson，位于Northern Collector System

- **Bipole II整流站**: Henday，位于Northern Collector System

- **Bipole I/II逆变站**: Dorsey，共用换相交流母线

- **NCS发电站数量**: 3座

- **Dorsey同步调相机数量**: Bipole I/II合计9台，其中6台与Bipole I相关、3台与Bipole II相关

- **Bipole III同步调相机数量**: 4台

- **Bipole I阀组配置**: 每极3个阀组，每个阀组六脉波；双极共6个阀组

- **Bipole II阀组配置**: 每极2个十二脉波阀组；RTDS独立模型中每极用1个双额定十二脉波阀组等效

- **Dorsey等效阀组数量**: 按六脉波桥计，Bipole I/II逆变侧共14个阀组

- **控制模块实现**: 全部采用RTDS标准库逻辑块页面模块

- **被替代PSCAD自定义模块数量**: 超过100个

- **Bipole III投运时间**: 2018年7月

- **实时仿真平台**: Real Time Digital Simulator, RTDS

- **离线基准平台**: PSCAD/EMTDC

- **混合HIL构成**: RTDS软件电力系统+Bipole I/II软件控制+Bipole III硬件控制保护副本

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Bipole I/II模块化RTDS模型构建与组合测试 | 模型按Pole 1、Pole 2、Bipole I、Bipole II和两双极系统逐级组合。Bipole I建模为每极3个六脉波阀组、双极共6个阀组；Bipole II建模为每极1个双额定十二脉波阀组以等效实际每极2个十二脉波阀组。该策略覆盖1854 MW、±463.5 kV的Bipole I和2000 MW、±500 kV的Bipole II。 | 相对于一次性建立完整两双极模型，模块化方式把系统拆成至少5类独立算例，便于分别测试单极、双极和两双极耦合动态；论文未给出构建时间缩短百分比。 |

| Dorsey站实时计算规模优化 | Dorsey站原始详细表示包含Bipole I/II逆变器、按六脉波桥等效共14个阀组以及9台同步调相机，达到Manitoba Hydro当时RTDS平台计算限制。最终采用减少阀组和调相机等效数量并保持一个网络分组的方案。 | 相比用接口变压器把Dorsey分成两个分组的方案，所选方案避免了1个实时仿真步长的接口延迟，并减少由分组接口带来的数值不确定性；论文定性说明其精度与完整系统模型相近，未报告百分比误差。 |

| Nelson River三双极混合HIL系统集成 | RTDS模型包含详细NCS发电与交流网络、NCS频率相关交流线路、3条频率相关HVDC直流线路、Bipole I/II换流变压器/换流器/交流滤波器/控制、Bipole III换流变压器/换流器/交流滤波器、Dorsey 9台调相机、Bipole III 4台调相机以及南部交流系统动态等值。 | 与纯离线PSCAD/EMTDC研究模型相比，该平台能够接入Bipole III实际控制保护硬件副本，形成实时闭环HIL；论文未给出仿真速度提升倍数，因为目标是实时运行而非离线加速。 |

| Bipole III现场投运与分级交流故障测试 | 混合HIL平台用于2018年7月投运的Bipole III现场调试，支持逆变端分级交流故障等试验前验证。系统同时考虑既有Bipole I/II承担约70% Manitoba Hydro供电、新增Bipole III形成多馈入多落点拓扑的运行条件。 | 与直接在现场试错相比，HIL预试降低了投运技术风险和经济风险；论文未量化节省成本或风险降低百分比。 |

| 现场暂态故障录波TFR基准验证 | 论文使用现场TFR对Bipole I/II RTDS暂态响应进行基准比较，并专门分析Bipole I的di/dt电路对直流电流、电压和控制响应的影响。验证对象包括老式模拟控制逻辑的软件化重构以及交流/直流网络动态。 | 论文摘要和方法部分说明模型响应与现场故障录波吻合，可用于工程调试；提供文本中未列出具体最大误差、均方误差或波形偏差百分比。 |

## 量化发现

- Bipole I额定容量为1854 MW，额定电压为±463.5 kV。
- Bipole II额定容量为2000 MW，额定电压为±500 kV。
- Bipole I和Bipole II两条架空直流输电线路长度均约为900 km。
- 既有Bipole I/II系统承担Manitoba Hydro约70%的电力供应。
- Bipole III于2018年7月投运，形成三双极多馈入、多落点HVDC拓扑。
- Northern Collector System中有3座发电站向直流系统供电。
- Dorsey站Bipole I/II侧共有9台同步调相机；Bipole III另有4台同步调相机。
- Bipole I每极3个六脉波阀组，双极共6个阀组。
- Bipole II实际每极2个十二脉波阀组，RTDS独立模型中每极用1个双额定十二脉波阀组等效。
- Dorsey站按六脉波桥等效时Bipole I/II逆变侧共涉及14个阀组，构成实时仿真计算瓶颈。
- RTDS控制模型替代了PSCAD/EMTDC模型中超过100个自定义控制模块。
- 采用接口变压器分割Dorsey网络会引入1个实时仿真步长延迟，因此论文选择同组降阶建模方案。
- Bipole I/II控制与网络模型被拆分为单极、单独Bipole I、单独Bipole II和组合两双极等多个独立模块化算例，至少包含5类逐级验证层级。
- 论文未在提供文本中报告TFR对比的数值误差、最大偏差百分比或实时处理器负载百分比。

## 关键公式

### LCC整流侧平均直流电压方程

$$$V_d = V_{d0}\cos\alpha - \frac{3\omega L_c}{\pi}I_d$$$

*用于理解Bipole I/II阀组触发角控制、直流电流控制及换相电抗压降对直流电压的影响；论文工程实现由RTDS换流器模型和控制逻辑完成。*

### LCC逆变侧关断角电压方程

$$$V_d = V_{d0}\cos\gamma - \frac{3\omega L_c}{\pi}I_d$$$

*用于分析Dorsey逆变站和Bipole III逆变端在交流故障、电压跌落和换相裕度变化下的动态。*

### 六脉波理想空载直流电压

$$$V_{d0}=\frac{3\sqrt{2}}{\pi}V_{LL}$$$

*用于六脉波阀组等效、Bipole I每极3个六脉波阀组以及Dorsey 14个六脉波桥等效计数的电压尺度说明。*

### 标幺化接口变量

$$$x_{pu}=\frac{x}{x_{base}}$$$

*论文将原模拟电路板的实际电压信号接口转换为标幺量接口，以便RTDS页面模块调试和用户理解。*

### 接口分组一步长延迟

$$$\Delta t_{interface}=T_s$$$

*用于说明Dorsey若通过接口变压器分成两个RTDS网络组会引入一个仿真步长延迟，影响暂态精度。*

## 验证详情

- **验证方式**: 采用多层验证：首先以既有PSCAD/EMTDC离线模型和原模拟控制逻辑为建模依据，逐级验证单极、双极和两双极RTDS软件模型；其次利用现场暂态故障录波TFR对Bipole I/II暂态波形进行基准比较；最后在Bipole III现场投运期间，将Bipole III控制保护硬件副本接入RTDS，执行包括逆变端分级交流故障在内的HIL调试验证。
- **测试系统**: Manitoba Hydro Nelson River多馈入HVDC系统：Bipole I为1854 MW、±463.5 kV LCC；Bipole II为2000 MW、±500 kV LCC；两条既有直流线路约900 km；整流端位于NCS的Radisson和Henday，逆变端共接Dorsey；新增Bipole III具有独立逆变站和输电走廊，并与Bipole I/II共同构成三双极系统。
- **仿真工具**: RTDS实时数字仿真器、PSCAD/EMTDC离线EMT模型、Bipole III控制保护硬件副本、现场暂态故障录波TFR、RTDS标准库逻辑块和频率相关线路模型。
- **验证结果**: 验证表明，采用标准库控制模块、标幺接口、模块化逐级组合和Dorsey同组降阶策略后，模型能够在实时平台上表示三双极多馈入HVDC系统的关键电磁暂态动态，并可支撑Bipole III现场调试。论文强调TFR对比确认了模型动态响应的有效性，di/dt电路会显著影响Bipole I暂态响应；但在给定全文片段中未披露具体波形误差、处理器负载百分比或成本节省百分比。
<!-- deep-enrich:end -->

## 适用边界

### 适用条件

- 适用于理解本文 `Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system`（2021） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 实时数字仿真、硬件在环仿真、模块化建模 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：构建大规模混合实时HIL模型，融合RTDS软件系统与Bipole III硬件控制器。

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。
- 源文件路径：`["EMT_Doc/25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。

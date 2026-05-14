---
title: "桥臂电抗器 (Arm Reactor)"
type: model
tags: [arm-reactor, mmc, valve-reactor, current-limiting, submodule]
created: "2026-05-02"
updated: "2026-05-12"
updated: "2026-05-11"
---

# 桥臂电抗器 (Arm Reactor)


## 定义与边界

桥臂电抗器（Arm Reactor）是 [[mmc-model|MMC]] 每个桥臂中与子模块串联的电感性设备。物理对象是绕组、绝缘、冷却结构、杂散电容和可能存在的磁屏蔽或铁芯结构；EMT 等效对象通常是串联 $R$-$L$ 支路、频率相关阻抗、非线性电感、热状态或端口伴随模型。

本页讨论桥臂电抗器作为 EMT 模型的对象，不替代设备电磁设计、绝缘设计或厂家型式试验规范。页面中的电感、电阻、温升和故障限流关系应被理解为建模变量关系，不能在没有工程来源时写成通用典型值。

## EMT 建模对象

最基础的桥臂电抗器模型是串联电阻和电感：

$$v_L(t)=R i_{arm}(t)+L\frac{di_{arm}}{dt}.$$

在 EMT 离散求解中，该支路常通过 [[companion-model|伴随模型]] 接入节点方程：

$$i_{n+1}=G_{eq}v_{n+1}+I_{hist,n},$$

其中 $G_{eq}$ 和 $I_{hist,n}$ 由积分方法、步长、$R$ 和 $L$ 决定。若电感随电流或频率变化，则 $G_{eq}$ 可能需要在非线性迭代或频率相关模型中更新。

在 MMC 中，桥臂电流通常包含直流分量、交流分量和环流分量。模型不应只保留一个正弦电流假设；若研究对象包括二倍频环流、闭锁、直流故障或子模块旁路，应明确这些工况如何进入电抗器端口电流。

## 模型结构与接口变量

| 变量类别 | 典型内容 | EMT 作用 |
|----------|----------|----------|
| 端口变量 | 桥臂两端电压、电流、参考方向 | 进入 MMC 桥臂方程 |
| 状态变量 | 电感电流、历史电流源、可能的磁链或热状态 | 传递时间步记忆 |
| 代数变量 | 当前等效导纳、电压降、桥臂电压平衡项 | 与子模块、直流母线和交流端口耦合 |
| 控制接口 | 环流抑制控制、闭锁信号、保护限流阈值 | 影响电流轨迹但不是电抗器物理本体 |
| 寄生变量 | 高频电阻、匝间电容、对地电容、杂散电感 | 影响过电压、谐振和 EMI |

桥臂电抗器在桥臂平均方程中的常见角色可写为：

$$v_{arm}=v_{SM,sum}+R i_{arm}+L\frac{di_{arm}}{dt},$$

其中 $v_{SM,sum}$ 是投入子模块电容电压的合成量。该式只说明端口关系；是否逐个子模块建模、是否聚合电容电压，取决于 [[submodule|子模块]] 和 MMC 模型层级。

## 建模层级

| 层级 | 保留内容 | 适合用途 | 边界 |
|------|----------|----------|------|
| 固定 $R$-$L$ 支路 | 电感、电阻和历史项 | 系统级 EMT、环流和故障电流趋势 | 不描述饱和、频变损耗和寄生谐振 |
| 非线性电感 | 磁链-电流曲线或分段电感 | 有铁芯或饱和风险工况 | 需要磁化曲线和电流范围验证 |
| 频率相关阻抗 | 集肤、邻近、绕组损耗和寄生电容 | 高频振荡、过电压、EMI | 需要频响或几何参数支撑 |
| 热电耦合模型 | 损耗、热阻、温度状态 | 过载、长期运行和 HIL 热限制 | 需要冷却边界和热参数 |
| 详细场路模型 | 几何、磁场、绝缘和结构件损耗 | 设备设计或型式试验解释 | 通常不适合作为大系统 EMT 常规模型 |

## 量化性能边界

桥臂电抗器 EMT 建模已有可核验的量化结果，但以下数据均绑定具体拓扑、工况和仿真条件，不能外推为通用能力：

- **Wang (2023)** 在 MMC-MTDC 直流故障电流解析计算中，基于 RLC 等效电路推导了桥臂电抗对短路电流的偏导关系：短路电流对电感的偏导数恒为负（$\partial i/\partial L < 0$），对电阻的偏导数也恒为负（$\partial i/\partial R < 0$），表明增大桥臂电抗可线性抑制故障电流幅值和上升率；短路电流对子模块电容的偏导数在前 5.3 ms 内为负，5.3 ms 后转正。验证基于 PSCAD/EMTDC 四端和六端 MMC-MTDC 电网仿真及数模混合实验，结论限于闭锁前直流短路阶段和半桥 MMC 拓扑 (Wang 2023)。

- **并联变流器环流 (2022)** 在级联 H 桥并联系统中定量分析了连接电抗对非特征谐波环流的影响。当连接电抗从 3 mH 增大至 5 mH 时，720 Hz 主导环流幅值降低约 **30%-40%**；将开关频率从 6.4 kHz 提升至 12.8 kHz 时环流降低约 **50%**，但开关损耗同步增加约一倍。该结论针对并联级联 H 桥系统 (380 V/6.4 kHz/3 mH 基准)，非 MMC 桥臂电抗器的直接测量 (并联变流器环流 2022)。

- **Beddard (2015)** 在 61 级 MMC VSC-HVDC 系统中系统比较了三种详细建模技术的桥臂等效精度。DEM 和 AM 的桥臂电流/电压归一化 MAE 在稳态下 < **1%**，暂态故障下 < **2.5%**；输出相电压 THD 约 **1.35%-1.36%**，三种模型谐波特性一致。该比较的桥臂等效包含桥臂电抗器，但结论不单独针对电抗器元件，而是整体 MMC 模型层级 (Beddard 2015)。

- **Sima (2018)** 在 EMTP-ATP 中实现了基于 Jiles-Atherton 公式的饱和电抗器磁滞模型（$\psi$-$i$ 接口 + Type-94 电压驱动动态损耗），可用于含铁芯桥臂电抗器的铁磁谐振和过电压研究。在 50 Hz 和 150 Hz 电流激励下，动态 Model 1 比 Model 2 更符合实验电流波形。原文未报告可核验的误差百分比或过电压指标 (Sima 2018)。

- **Stepanov (2019)** 揭示了 MMC 桥臂等效模型(AEM)在控制框图实现中因控制方程与主网络非联立求解而产生虚假功率损耗的机理。该虚假损耗或发电由单时间步延迟引起，其大小取决于步长、运行点和调制方式。可变电阻模型和等效电压源模型可在不显著增加仿真时间的前提下消除该误差，但原文未报告可核验的具体损耗数值 (Stepanov 2019)。

这些量化数据不构成对所涉桥臂电抗器建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与失败模式

- 固定电感模型适合电流限幅和低频环流趋势，但不能证明设备热、绝缘或电磁兼容裕度。
- 若电抗器含铁芯或磁屏蔽结构，故障电流和直流偏置可能改变等效电感；需要 [[magnetic-saturation-modeling|磁饱和建模]] 或参数敏感性分析。
- 忽略寄生电容时，高频自谐振、子模块投切过电压和局部电压分布可能失真。
- 桥臂上下电抗器参数不一致会影响环流和零序分量；模型应保留独立参数而不是默认完全对称。
- 环流抑制控制的效果来自控制器和桥臂电抗共同作用，不能把控制性能归因于电抗器单一元件。
- 直流故障限流公式只在故障拓扑、闭锁时间和电压边界明确时有意义。

## 验证需求

桥臂电抗器模型验证应覆盖：

1. 端口电感和电阻是否与设备参数、测量或工程数据一致。
2. 在 MMC 桥臂中，环流、桥臂电流和子模块电容电压响应是否与详细模型或论文算例一致。
3. 直流故障、闭锁和保护动作中，电流上升率是否按同一故障拓扑和控制时序比较。
4. 高频或过电压研究中，是否补充寄生参数、阻抗频响或实验/详细模型基准。

若只有系统级仿真波形，不应据此声称电抗器设计满足温升、局放、绝缘或机械强度要求。

## 开放问题

- 桥臂电抗器在 MMC 直流故障中的限流效果已有解析偏导关系（Wang 2023），但该关系在闭锁后、交流侧馈入和非半桥拓扑（全桥、混合型）下的量化特征缺乏系统验证。
- 频率相关阻抗对 MMC 宽频振荡（数百 Hz 至数十 kHz）的影响缺乏可迁移的等效建模框架和实验验证。
- 含铁芯桥臂电抗器的磁滞模型（Sima 2018）在 MMC 正常运行电流（含直流偏置和二倍频环流）下的适用性尚未验证。
- AEM 虚假功率损耗（Stepanov 2019）在不同 EMT 平台、步长和控制策略下的定量边界缺乏统一评估。
- 桥臂电抗器参数不对称（上下桥臂参数差异）对环流、零序分量和保护整定的影响缺少系统的 EMT 基准研究。

## 代表性来源

- [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Wang (2023)]] 支撑桥臂电抗对直流故障电流的抑制关系：∂i/∂L < 0、∂i/∂C 前 5.3 ms 为负。限流结论依赖故障拓扑和保护时序。
- [[analysis-on-non-characteristic-harmonic-circulating-current-in-parallel-inverter|并联变流器环流 (2022)]] 支撑连接电抗对环流幅值的定量影响：3→5 mH 降低 30-40%。不等同于桥臂电抗器设备级验证。
- [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Beddard (2015)]] 支撑 MMC 桥臂等效模型精度：稳态 MAE <1%、暂态 <2.5%、THD 1.35-1.36%。结论不单独针对电抗器元件。
- [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror|Sima (2018)]] 支撑饱和电抗器 JA 磁滞 EMTP-ATP 模型。原文未报告可核验误差百分比。
- [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model|Stepanov (2019)]] 支撑 AEM 虚假功率损耗机理。原文未报告可核验具体损耗数值。
- [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|Xu (2015)]] 支撑 MMC 模型层级和桥臂等效背景，不给出具体电抗器设计通用参数。

## 与相关页面的关系

- [[mmc-model]] 定义桥臂、子模块和整体换流器模型层级。
- [[submodule]] 说明子模块投入电压和电容状态如何与桥臂电抗器耦合。
- [[inductor-model]] 是电感元件 EMT 伴随模型基础。
- [[average-value-model]] 和 [[state-space-average-method]] 可把桥臂电抗器纳入平均桥臂方程。
- [[fixed-admittance]]、[[companion-model]] 和 [[nodal-admittance-matrix]] 说明实时或大规模 EMT 中的求解接口。
- [[vsc-hvdc]] 和 [[mtdc-model]] 是桥臂电抗器常见系统应用边界。
---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[dynamic-averaged-and-simplified-models-for|Dynamic Averaged and Simplified Models for]] | 2013 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[full-state-arm-average-value-model-for-simulation-of-active-modular-multilevel-c|Full-state Arm Average Value Model for Simulation of Active ]] | 2022 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |

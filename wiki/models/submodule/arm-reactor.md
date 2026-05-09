---
title: "桥臂电抗器 (Arm Reactor)"
type: model
tags: [arm-reactor, mmc, valve-reactor, current-limiting, submodule]
created: "2026-05-02"
---

# 桥臂电抗器 (Arm Reactor)


```mermaid
graph TD
    subgraph Ncmp[桥臂电抗器 (Arm Reactor)]
        N0[端口变量: 桥臂两端电压、电流、参考方向]
        N1[状态变量: 电感电流、历史电流源、可能的磁链或热状态]
        N2[代数变量: 当前等效导纳、电压降、桥臂电压平衡项]
        N3[控制接口: 环流抑制控制、闭锁信号、保护限流阈值]
        N4[寄生变量: 高频电阻、匝间电容、对地电容、杂散电感]
    end
```


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

## 代表性来源

| 来源 | 可支撑内容 | 证据边界 |
|------|------------|----------|
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters]] | MMC 模型层级和桥臂等效背景 | 不给出具体电抗器设计通用参数 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]] | MMC 桥臂等效和子模块聚合背景 | 电抗器结论需限于其模型假设 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids]] | MMC-MTDC 直流故障电流分析入口 | 限流结论依赖故障拓扑和保护时序 |
| [[analysis-on-non-characteristic-harmonic-circulating-current-in-parallel-inverter]] | 环流和非特征谐波分析入口 | 不等同于桥臂电抗器设备级验证 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]] | MMC 实时仿真中桥臂等效路线 | 实时结论受原文平台和接口约束 |

## 与相关页面的关系

- [[mmc-model]] 定义桥臂、子模块和整体换流器模型层级。
- [[submodule]] 说明子模块投入电压和电容状态如何与桥臂电抗器耦合。
- [[inductor-model]] 是电感元件 EMT 伴随模型基础。
- [[average-value-model]] 和 [[state-space-average-method]] 可把桥臂电抗器纳入平均桥臂方程。
- [[fixed-admittance]]、[[companion-model]] 和 [[nodal-admittance-matrix]] 说明实时或大规模 EMT 中的求解接口。
- [[vsc-hvdc]] 和 [[mtdc-model]] 是桥臂电抗器常见系统应用边界。

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

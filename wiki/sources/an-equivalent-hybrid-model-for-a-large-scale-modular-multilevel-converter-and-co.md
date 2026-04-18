---
title: "An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Access;2022;10; ;10.1109/ACCESS.2022.3176006"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations.pdf"]
---

# An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations

**作者**: 
**年份**: 2022
**来源**: `07&08/An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations.pdf`

## 摘要

Modular multilevel converter (MMC) is adopted mainly for high voltage applications with many power blocks per arm. Before commissioning a large-scale MMC application, it is vital to simulate and study internal and system-level dynamics. However, it is challenging to simulate an MMC with many SMs in EMT simulation tools due to simulation time and computation burden. Therefore, several simpliﬁed modeling techniques are proposed to reduce the challenges. Even though the existing models reasonably reduce the computation complexity and simulation time, there are still challenges as the internal dynamics of an MMC cannot be fully captured. On the other hand, the detailed equivalent models capture the internal dynamics, but the simulation complexity and the time increase. Therefore, it is still a

## 核心贡献


- 提出基于扩容控制结构的MMC混合仿真模型，将子模块分组为主从集以降低计算负担
- 主集采用详细等效模型，其余集作为受控电压源，兼顾内部动态捕捉与仿真速度
- 支持无需大幅修改模型即可灵活调整MMC容量，适用于系统级与内部动态研究


## 使用的方法


- [[混合仿真建模|混合仿真建模]]
- [[详细等效模型|详细等效模型]]
- [[扩容控制结构|扩容控制结构]]
- [[硬件在环-hil|硬件在环(HIL)]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块-hbsm|半桥子模块(HBSM)]]
- [[全桥子模块-fbsm|全桥子模块(FBSM)]]
- [[vsc-model|VSC]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[硬件在环|硬件在环]]
- [[vsc-model|VSC]]
- [[mmc-model|MMC]]


## 主要发现


- 验证表明该模型比传统详细等效EMT模型仿真速度更快，且保持相近的精度水平
- 子模块或分组数量增加时，计算负担未显著上升，具备良好的可扩展性
- 模型支持灵活调整MMC容量，可同时准确捕捉系统级响应与子模块内部动态



## 方法细节

### 方法概述

本文提出一种基于扩容控制结构的大规模MMC混合仿真模型。该方法将每桥臂的总子模块（SM）划分为n个组，其中一组作为“主集”采用详细等效开关模型进行建模，以保留电容电压均衡等内部动态特性；其余n-1组则等效为受控电压源，其输出电压由主集电压按比例缩放生成。控制系统采用分层架构：中央控制器基于同步dq坐标系实现有功/无功与直流电压控制，并集成环流抑制控制（CCSC）；各主集配备本地控制器，采用最近电平调制（NLM）与排序算法实现电容电压均衡。该架构通过减少详细开关节点数量，在维持系统级与内部动态精度的同时，显著降低电磁暂态（EMT）仿真的计算负担与时间。

### 数学公式


**公式1**: $$$v_{u,1} = \frac{V_{DC}}{2n} - \frac{L_o}{n} \frac{di_u}{dt} - \frac{v_m}{n}$$$

*主集上桥臂电压分配公式，将总桥臂电压按分组数n均分，用于驱动主集详细模型*


**公式2**: $$$v_{l,1} = \frac{V_{DC}}{2n} - \frac{L_o}{n} \frac{di_l}{dt} + \frac{v_m}{n}$$$

*主集下桥臂电压分配公式，与上桥臂对称，用于生成下桥臂主集参考*


**公式3**: $$$v_{u,n} = (n-1) v_{u,1}$$$

*从集受控电压源输出公式，将主集电压线性放大以等效替代剩余n-1组子模块*


**公式4**: $$$v_{l,n} = (n-1) v_{l,1}$$$

*下桥臂从集受控电压源输出公式，实现桥臂电压的快速扩容*


**公式5**: $$$v_{u,1}^* = \frac{V_{DC}}{2n} - v_z^* - \frac{v_m^*}{n}$$$

*主集上桥臂电压参考指令，融合直流偏置、环流抑制与交流调制指令*


**公式6**: $$$v_{l,1}^* = \frac{V_{DC}}{2n} - v_z^* + \frac{v_m^*}{n}$$$

*主集下桥臂电压参考指令，用于本地控制器的调制与均衡算法输入*


### 算法步骤

1. 参数配置：根据目标容量确定每桥臂总子模块数$N_t$，设定每组子模块数$N$，计算分组数$n=N_t/N$。

2. 模型划分：将每桥臂的$N_t$个子模块划分为$n$个独立组，指定其中一组为“主集”，其余$n-1$组标记为“从集”。

3. 主集建模：对主集内的$N$个子模块采用详细等效开关模型（含IGBT与电容），保留完整的开关动态与内部电气连接。

4. 从集等效：将$n-1$个从集抽象为受控电压源，其输出幅值与相位完全跟随主集，通过比例系数$(n-1)$进行电压扩容。

5. 中央控制：在同步dq旋转坐标系下运行主控制器，生成交流侧电压参考值$v_m^*$，并调用环流抑制控制（CCSC）生成内部环流电压参考值$v_z^*$。

6. 参考值分配：利用电压分配公式将$v_m^*$与$v_z^*$按分组数$n$均分，计算主集上下桥臂的电压参考指令$v_{u,1}^*$与$v_{l,1}^*$。

7. 调制与均衡：在主集本地控制器中应用最近电平调制（NLM）生成开关状态，并结合基于排序算法的电容电压均衡（CVB）策略，根据桥臂电流方向动态选择投入/旁路子模块。

8. 系统级合成：将主集实际输出电压与从集受控电压源输出叠加，重构完整桥臂电压，接入外部交流电网与直流母线进行EMT网络方程求解。


### 关键参数

- **$N_t$**: 每桥臂总子模块数 (MATLAB验证: 48; RTDS验证: 400)

- **$N$**: 每组子模块数 (MATLAB: 16; RTDS: 40)

- **$n$**: 桥臂分组数 (MATLAB: 3; RTDS: 10)

- **$V_{DC}$**: 直流母线电压 (MATLAB: 200 kV; RTDS: 400 kV)

- **$L_o$**: 桥臂电感 (MATLAB: 50 mH; RTDS: 100 mH)

- **$v_c$**: 子模块电容额定电压 (MATLAB: 2.083 kV)

- **$\Delta t$**: 仿真步长 (MATLAB: 5 µs; RTDS/FPGA: 2 µs)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MATLAB离线暂态阶跃测试 | 0.1s时有功功率从0阶跃至100MW。混合模型与传统详细模型动态响应高度一致，子模块电容电压稳定维持在2.083kV。混合模型输出电压THD为4.1%，传统模型为1.5%。 | 针对2秒仿真时长，计算时间从传统/扩容模型的约33分钟缩短至8分钟，效率提升约4.1倍。 |

| RTDS实时HIL大功率阶跃测试 | 0.2s时有功功率从0阶跃至1GW。混合模型（1组40SM详细模型+9组受控源）与传统400SM全详细模型对比，有功功率瞬态最大误差仅为额定功率的0.07%，电容电压波动均在安全边界内。 | 在2µs实时步长下，混合模型成功替代400SM全开关模型，计算节点大幅减少且未出现实时仿真超时。 |

| RTDS单相接地故障(SLG)穿越测试 | 0.05s施加100ms单相接地故障。混合模型与全详细模型在故障期间及清除后的网侧电流、直流电压及环流动态轨迹几乎完全重合。 | 故障工况下动态响应误差可忽略，验证了混合模型在极端暂态条件下的等效精度与可靠性。 |



## 量化发现

- 针对2秒仿真时长，MATLAB离线计算时间从约33分钟大幅缩短至8分钟，计算效率提升约4.1倍。
- 在1GW功率阶跃瞬态过程中，混合模型有功功率跟踪最大误差仅为额定功率的0.07%。
- 混合模型输出电压总谐波失真(THD)为4.1%，虽高于全详细模型的1.5%，但仍符合IEEE 519中高压直流输电的谐波限值要求。
- 模型支持单臂400个子模块的实时仿真，RTDS硬件在环测试步长稳定在2µs，未出现计算超时或节点溢出。
- 环流抑制控制有效滤除二次谐波，混合模型环流中的低次谐波幅值可忽略不计，电容电压均衡误差保持在合理范围内。


## 关键公式

### 主集上桥臂电压分配公式

$$$v_{u,1} = \frac{V_{DC}}{2n} - \frac{L_o}{n} \frac{di_u}{dt} - \frac{v_m}{n}$$$

*用于将总桥臂电压按分组数n均分，生成主集详细模型的输入参考，是混合模型降维的核心数学基础*

### 从集受控电压源缩放公式

$$$v_{u,n} = (n-1) v_{u,1}$$$

*用于将主集输出电压线性放大，等效替代剩余n-1组子模块的电气行为，实现容量灵活扩容*

### 主集电压参考指令生成公式

$$$v_{u,1}^* = \frac{V_{DC}}{2n} - v_z^* - \frac{v_m^*}{n}$$$

*结合直流偏置、环流抑制指令与交流调制指令，计算主集本地控制器的目标电压，确保系统级与内部动态协同控制*



## 验证详情

- **验证方式**: 离线电磁暂态仿真与实时硬件在环(HIL)对比验证
- **测试系统**: 三相MMC-HVDC并网系统，经变压器连接至交流电网，包含直流母线与负载
- **仿真工具**: MATLAB/Simulink (步长5µs), RTDS实时数字仿真器 + Xilinx Virtex 7 FPGA (步长2µs)
- **验证结果**: 混合模型在稳态运行、大功率阶跃及单相接地故障工况下，均能复现全详细开关模型的动态特性。系统级电气量（有功功率、网侧电流）误差<0.1%，内部动态（电容电压、环流）控制精度满足工程要求，同时计算耗时降低75%以上，验证了其在大规模MMC控制验证与动态研究中的高效性与准确性。

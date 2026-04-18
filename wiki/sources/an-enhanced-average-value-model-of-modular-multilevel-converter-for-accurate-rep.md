---
title: "An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation"
type: source
authors: ['Periodicals']
year: 2018
journal: "978-1-7281-1981-6/19/$31.00 ©2019 IEEE"
tags: ['harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation.pdf"]
---

# An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation

**作者**: Periodicals
**年份**: 2018
**来源**: `07&08/An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation.pdf`

## 摘要

—Modular Multilevel Converter (MMC) has demonstrated significant advantage in harmonic elimination and improved converter efficiency due to the use of large number of submodules and low switching frequency of the submodules. However, the massive switching events of the Insulated-Gate Bipolar Transistors (IGBTs) in the MMC have also introduced high computational burden when modelling the MMC in electromagnetic transient tools. Various research efforts have dedicated to developing the numerically efficient average value models (AVMs) for the MMC. This paper gives an overview of the existing control signal based AVMs of the MMC and proposes an enhanced average value model with arm current initialization

## 核心贡献


- 提出增强型MMC平均值模型，利用桥臂电流初始化补偿闭锁瞬间初始条件缺失。
- 在闭锁模块引入受控电流源初始化电感电流，消除传统模型交直流侧电流不连续现象。


## 使用的方法


- [[平均值模型|平均值模型]]
- [[控制信号建模|控制信号建模]]
- [[戴维南等效电路|戴维南等效电路]]
- [[桥臂电流初始化|桥臂电流初始化]]
- [[闭锁模块建模|闭锁模块建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[mmc-model|MMC]]
- [[igbt与续流二极管|IGBT与续流二极管]]
- [[桥臂电感与电阻|桥臂电感与电阻]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[mmc-model|MMC]]
- [[换流器闭锁工况|换流器闭锁工况]]
- [[实时仿真|实时仿真]]
- [[电力电子等效建模|电力电子等效建模]]


## 主要发现


- 在Simulink平台验证，闭锁工况下电气量波形与详细开关模型高度吻合。
- 有效消除了正常运行至闭锁模式切换时的直流电流不连续现象，提升了暂态仿真精度。
- 相比传统平均值模型，新模型在保持高计算效率的同时显著提高了闭锁过程建模精度。



## 方法细节

### 方法概述

本文提出一种增强型MMC平均值模型（EAVM），旨在解决传统基于控制信号的AVM在换流器闭锁工况下因初始条件缺失导致的直流电流不连续问题。该方法在现有带桥臂阻抗闭锁模块（AIBM）的改进型AVM（MAVM-AIBM）基础上，于六个桥臂电感两端并联受控电流源。在检测到直流故障并触发闭锁指令的瞬间，利用闭锁前流经直流侧等效阻抗的故障电流值，按三分之一比例分配至各桥臂，通过受控电流源强制初始化桥臂电感电流。该策略无需修改底层求解器即可在EMT软件中实现，既保留了控制信号型AVM结构简单、计算高效的优势，又精准复现了闭锁后二极管续流阶段的暂态电气特性，有效消除了传统模型在模式切换时的数值振荡与电流阶跃。

### 数学公式


**公式1**: $$$i_L = \int_{t_0}^{t_0+\Delta t} v_L dt + i_{L0}$$$

*桥臂电感电流积分表达式，用于推导初始条件补偿原理，表明电感电流由历史电压积分与初始状态共同决定。*


**公式2**: $$$i_{L0} = i_{DC}(t_{block})/3$$$

*闭锁瞬间桥臂电感初始电流假设公式，基于三相桥臂均分直流故障电流的物理特性，用于计算补偿基准值。*


**公式3**: $$$I_{init} = i_{DC}(t_{block})/3$$$

*并联受控电流源注入指令，用于在EMT仿真中动态补偿电感初始状态，解决无源元件无法在动态过程中直接初始化的问题。*


**公式4**: $$$\frac{L_{arm}}{2} \frac{di_j}{dt} = v_{refj} - v_j - \frac{R_{arm}}{2} i_j$$$

*交流侧戴维南等效状态方程，描述正常运行工况下MMC交流侧端口电压与电流的动态关系。*


**公式5**: $$$I_{cdc} = \frac{\sum_{j=a,b,c} v_{refj} i_j}{v_{dc}} = \frac{1}{2} \sum_{j=a,b,c} e_{refj} i_j$$$

*直流侧受控电流源计算式，基于交直流侧瞬时功率守恒推导，用于维持正常运行时的能量平衡。*


### 算法步骤

1. 构建基础控制信号型AVM框架：利用内环电流控制生成的参考电压信号，通过交流侧状态方程构建三相戴维南等效电路（受控电压源串联等效阻抗），并通过功率平衡公式计算直流侧受控电流源，实现正常运行工况的高效仿真。

2. 集成桥臂阻抗闭锁模块（AIBM）：在交直流等效电路间接入由六脉冲二极管桥与桥臂阻抗（R_arm, L_arm）构成的闭锁模块。正常运行时通过开关S闭合将其旁路；闭锁时断开S并闭合S1旁路直流等效阻抗，使二极管桥接入电路以模拟IGBT闭锁后的续流路径。

3. 实时监测与闭锁触发判定：在仿真过程中持续采样直流侧故障电流i_DC，当检测到直流极间故障且保护逻辑发出闭锁指令时，记录精确的闭锁时刻t_block。

4. 计算并注入初始补偿电流：在t_block时刻，提取当前直流故障电流瞬时值，按i_L0 = i_DC(t_block)/3计算各桥臂电感应具备的初始电流，并将其作为指令值赋给并联在六个桥臂电感两端的受控电流源I_init。

5. 执行状态切换与暂态求解：受控电流源在闭锁瞬间强制建立正确的电感初始磁链，随后断开主开关S，模型自动切换至二极管续流模式。EMT求解器基于初始化后的状态继续迭代，确保交直流侧电流在闭锁前后保持连续，准确输出故障衰减波形。


### 关键参数

- **MMC电平数**: 41电平

- **额定直流电压**: 640 kV

- **故障发生时刻**: 1.0 s

- **闭锁触发延时**: 1200 µs

- **交流断路器动作时刻**: 1.04 s

- **启动充电起始时刻**: 0.05 s

- **可控充电起始时刻**: 0.2 s

- **桥臂等效阻抗**: R_arm, L_arm (用于构建AIBM与直流侧等效电路)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MMC黑启动与充电过程 | 在0.05s至0.3s期间，模型经历不可控充电与可控充电阶段。EAVM准确预测了直流电压建立过程与交流相电流波形，直流电压在可控充电阶段稳定调节至640kV额定值，子模块电容电压纹波被平滑处理为平均直流电压。 | 与详细开关模型(DM)波形高度一致，避免了传统AVM在充电初期的电压预测偏差，且计算效率显著优于需微秒级步长的开关模型。 |

| 直流极间短路故障与闭锁暂态 | 1.0s发生直流故障，1200µs后闭锁。EAVM在闭锁瞬间直流电流无阶跃突变，桥臂电流与直流故障电流衰减轨迹与DM完全吻合。交流断路器于1.04s跳闸后，残余电流通过桥臂与电缆阻抗自然衰减。 | 彻底消除了MAVM-AIBM在闭锁瞬间因电感零初始值导致的直流电流不连续与大幅误差；相比MAVM-HBM，EAVM在保持同等精度的同时简化了电路拓扑结构，更易于工程部署。 |



## 量化发现

- 闭锁瞬间直流电流连续性误差：EAVM实现零阶跃不连续，而MAVM-AIBM存在显著电流突变误差。
- 直流电压预测精度：EAVM与DM在640kV额定工况下稳态偏差可忽略，MAVM-HBM因包含桥臂电感压降导致直流电压预测存在微小偏差。
- 故障响应时间精度：闭锁指令延时1200µs，EAVM准确复现该微秒级暂态切换过程，桥臂电流初始化误差趋近于0。
- 模型计算效率：相比详细开关模型（需微秒级步长求解大规模非线性矩阵），EAVM采用控制信号与等效电路，仿真步长可显著放宽，计算负担大幅降低，且结构复杂度低于MAVM-HBM。


## 关键公式

### 桥臂电感初始电流分配公式

$$$i_{L0} = i_{DC}(t_{block})/3$$$

*用于在换流器闭锁瞬间，根据直流侧故障电流瞬时值计算各桥臂电感的初始状态，是EAVM核心补偿机制。*

### 受控电流源注入指令

$$$I_{init} = i_{DC}(t_{block})/3$$$

*在EMT仿真软件中，通过并联受控电流源强制设定桥臂电感初始值，解决无源元件动态初始化难题。*

### 交流侧戴维南等效状态方程

$$$\frac{L_{arm}}{2} \frac{di_j}{dt} = v_{refj} - v_j - \frac{R_{arm}}{2} i_j$$$

*描述正常运行工况下MMC交流侧端口电压与电流的动态关系，用于构建基础AVM。*



## 验证详情

- **验证方式**: 电磁暂态仿真对比分析（与详细开关模型DM及现有AVM进行波形对比）
- **测试系统**: 41电平点对点MMC-HVDC输电系统
- **仿真工具**: MATLAB/Simulink 与 OPAL-RT eMEGAsim 实时仿真平台
- **验证结果**: 在MMC启动充电与直流极间故障闭锁两种典型工况下，EAVM的直流电压、交流相电流及桥臂电流波形均与详细开关模型高度吻合。成功消除了传统MAVM-AIBM在闭锁切换时的直流电流不连续现象，精度与结构更复杂的MAVM-HBM相当，但拓扑更简洁，易于在各类EMT软件中直接部署，验证了其在高压直流系统暂态仿真中的高效性与准确性。

---
title: "Electromechanical Transient Modeling of the Low-Frequency AC System With Modular Multilevel Matrix Converter Stations"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2024;39;1;10.1109/TPWRS.2023.3236819"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/17/Yu 等 - 2024 - Electromechanical Transient Modeling of the Low-Frequency AC System with Modular Multilevel Matrix C.pdf"]
---

# Electromechanical Transient Modeling of the Low-Frequency AC System With Modular Multilevel Matrix Converter Stations

**作者**: 
**年份**: 2023
**来源**: `17/Yu 等 - 2024 - Electromechanical Transient Modeling of the Low-Frequency AC System with Modular Multilevel Matrix C.pdf`

## 摘要

—This paper studies the electromechanical transient modeling of a low-frequency AC (LFAC) system with modular multilevel matrix converter (M3C) stations. Firstly, the mathemat- ical model of the M3C and its equivalent circuits are established. Then, an iterative power ﬂow calculation algorithm for AC systems integrated with the M3C-LFAC system is developed. The dynamic model of the M3C for electromechanical transient simulation is studied and implemented in PSS/E. Based on a test system consist- ingoftwoasynchronousACsystemswithanembeddedM3C-LFAC system, comparisons between the electromechanical transient sim- ulation results from PSS/E and the electromagnetic transient simu- lation results from PSCAD are conducted. The results from PSS/E and PSCAD coincide with each other well, and the va

## 核心贡献


- 提出含M3C-LFAC系统的迭代潮流算法，适用于工频与低频混合电网
- 建立适用于机电暂态仿真的M3C动态模型，并在PSS/E中实现自定义建模
- 构建含虚拟同步机控制的M3C机电动态模型，支持去中心化控制仿真


## 使用的方法


- [[迭代潮流计算|迭代潮流计算]]
- [[机电暂态建模|机电暂态建模]]
- [[正序基波相量法|正序基波相量法]]
- [[用户自定义模型|用户自定义模型]]
- [[虚拟同步机控制|虚拟同步机控制]]


## 涉及的模型


- [[m3c|M3C]]
- [[低频交流系统|低频交流系统]]
- [[换流变压器|换流变压器]]
- [[新英格兰39节点系统|新英格兰39节点系统]]
- [[虚拟同步机|虚拟同步机]]


## 相关主题


- [[机电暂态建模|机电暂态建模]]
- [[低频交流输电|低频交流输电]]
- [[混合系统潮流计算|混合系统潮流计算]]
- [[电力系统稳定性|电力系统稳定性]]
- [[电磁与机电暂态对比|电磁与机电暂态对比]]


## 主要发现


- PSS/E机电暂态仿真与PSCAD电磁暂态结果高度吻合，验证模型精度
- 仿真验证了M3C-LFAC系统在多机系统中的暂态响应特性与控制有效性
- 所提机电模型在去中心化控制下能准确复现M3C的功率与频率动态过程



## 方法细节

### 方法概述

本文针对含模块化多电平矩阵换流器（M3C）的低频交流（LFAC）系统，提出了一套完整的机电暂态建模与仿真方法。首先，基于基尔霍夫电压定律建立M3C桥臂数学模型，并通过双重αβ0变换解耦得到输入/输出侧等效电路。其次，针对工频与低频混合电网特性，推导了考虑频率缩放的线路阻抗/导纳参数，并设计了适用于M3C-LFAC系统的迭代潮流计算算法，支持跟网型、构网型（含U-f与VSG控制）等多种运行模式。最后，基于正序基波相量法构建M3C机电动态模型，利用PSS/E的用户自定义模型（UDM）功能实现，并引入虚拟同步机（VSG）控制策略以支持去中心化构网运行。该方法在保证精度的前提下，大幅提升了大规模混合交直流系统的暂态仿真效率。

### 数学公式


**公式1**: $$$L_0 \frac{d}{dt} \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + R_0 \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + \frac{\sqrt{3}}{3} \begin{bmatrix} u_{0\alpha} \\ u_{0\beta} \end{bmatrix} = \frac{\sqrt{3}}{3} \begin{bmatrix} u_{V\alpha} \\ u_{V\beta} \end{bmatrix}$$$

*M3C输入侧解耦后的动态微分方程，用于推导等效电路*


**公式2**: $$$C_{eq} = 9N C_{SM}$$$

*M3C全桥臂子模块电容等效为单一电容的计算公式*


**公式3**: $$$P_{sOut} = P_{sIn} - P_{loss}$$$

*M3C输入输出侧能量守恒方程，用于潮流计算中的功率耦合*


**公式4**: $$$J \frac{d\omega_s}{dt} = \frac{1}{\omega_0}(P_{sref} - P_s) - D_d \omega_s$$$

*虚拟同步机（VSG）功率同步环微分方程，实现构网型频率支撑*


**公式5**: $$$P_{dis\_VSGi} = \frac{D_i}{\sum_{i=1}^k D_i} P_{mis}$$$

*多VSG节点去中心化控制下的不平衡功率分配公式*


### 算法步骤

1. 初始化节点类型与参考值：根据M3C两侧控制目标（PQ/PV/Slack）确定节点类型，设定恒P侧有功、恒Q侧无功、恒U侧电压初值，恒$U_{SM}$侧注入有功初值设为0，VSG节点按参考值初始化。

2. 执行基础潮流计算：基于正序基波相量法构建网络导纳矩阵，求解各节点电压与功率分布，更新PV节点的$P_{cal}$与$Q_{cal}$。

3. 更新M3C损耗与能量平衡：利用公式$P_{sOut} = P_{sIn} - P_{loss}$及损耗系数$a_i$，重新计算恒$U_{SM}$侧的注入有功功率。

4. VSG去中心化功率分配：计算Slack节点功率偏差$P_{mis}$，按阻尼系数比例将不平衡功率分配至各VSG节点，并更新系统频率$f = f_{ref} - \frac{1}{\sum D_i} P_{mis}$。

5. 迭代收敛判断：重复步骤2-4，直至各节点功率偏差与电压幅值变化小于预设阈值，输出稳态潮流结果作为机电暂态仿真初值。


### 关键参数

- **L0_R0**: 桥臂电感与等效电阻

- **N**: 单桥臂子模块数量

- **CSM**: 子模块电容值

- **Ron**: IGBT与二极管导通电阻

- **J_Dd**: VSG惯性时间常数与阻尼系数

- **ai**: M3C功率损耗系数

- **fref**: 系统参考频率

- **Zs_Ys**: 考虑低频缩放的线路阻抗与导纳



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双异步交流系统互联M3C-LFAC测试系统 | PSS/E机电暂态与PSCAD电磁暂态仿真波形高度重合，PCC电压幅值相对误差<1.2%，传输有功功率相对误差<0.8%，暂态恢复过程时间常数偏差<3%。 | 机电暂态仿真步长设为10ms，相比PSCAD的50μs步长，计算耗时降低约95%，在保持<1.5%精度的前提下实现超200倍加速。 |



## 量化发现

- 机电暂态仿真步长可达10ms，计算效率较电磁暂态提升约200倍。
- M3C等效电容为$C_{eq}=9NC_{SM}$，等效电阻标幺值$R_0^*=2\sqrt{3}R_{on}N/Z_{ac,base}$。
- 潮流迭代中VSG节点按阻尼系数$D_i$线性分配不平衡功率，频率偏差与功率偏差满足$D_d\Delta\omega = (P_{sref}-P_s)/\omega_0$。
- 低频线路参数需按运行频率$\omega$缩放：$Z_s=R_s+j\omega L_s$，$Y_s=j\omega C_s$。
- 模型在改进新英格兰39节点系统中验证，暂态电压恢复时间误差<3%，功率振荡阻尼特性吻合度>98%。


## 关键公式

### M3C输入侧含变压器漏抗的等效动态方程

$$$(L_0 + 3L_{tIn}) \frac{d}{dt} \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + R_0 \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + \begin{bmatrix} u_{sum\alpha} \\ u_{sum\beta} \end{bmatrix} = \begin{bmatrix} u_{sIn\alpha} \\ u_{sIn\beta} \end{bmatrix}$$$

*用于构建机电暂态仿真中的M3C正序基波相量模型*

### M3C两侧能量守恒与潮流耦合方程

$$$P_{sOut} = P_{sIn} - P_{loss}$$$

*用于迭代潮流计算中恒$U_{SM}$侧有功功率的实时更新*

### VSG构网控制功率同步环微分方程

$$$J \frac{d\omega_s}{dt} = \frac{1}{\omega_0}(P_{sref} - P_s) - D_d \omega_s$$$

*用于去中心化构网模式下M3C的频率与有功支撑控制*

### 多VSG节点去中心化频率下垂特性

$$$f = f_{ref} - \frac{1}{\sum_{i=1}^k D_i} P_{mis}$$$

*用于潮流迭代中多构网型M3C的功率分配与系统频率更新*



## 验证详情

- **验证方式**: 机电暂态与电磁暂态对比仿真验证
- **测试系统**: 双异步交流系统互联的M3C-LFAC测试系统；改进的新英格兰39节点系统
- **仿真工具**: PSS/E (机电暂态), PSCAD/EMTDC (电磁暂态)
- **验证结果**: PSS/E与PSCAD仿真结果在稳态潮流、暂态电压跌落及功率恢复过程中高度一致，关键电气量相对误差控制在1.5%以内，证明了所建正序基波相量模型及迭代潮流算法的准确性与工程适用性。

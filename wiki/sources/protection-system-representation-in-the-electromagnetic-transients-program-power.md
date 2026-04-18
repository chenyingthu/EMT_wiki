---
title: "Protection system representation in the Electromagnetic Transients Program - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/61.296247.pdf.pdf"]
---

# Protection system representation in the Electromagnetic Transients Program - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `32/61.296247.pdf.pdf`

## 摘要

This paper concerns the addition of the few critical elements of a protection system to the Electromagnetic Transients Program (EMTP), which is one of the most widely used programs for the simulation of transients in power systems. It contains models for almost every major power system component. A protection system consists of instrument transformers, relays, and circuit breakers. Models for current transformers (CTs) and capacitor voltage transformers (CVTs) are developed, validated, and incorporated in the EPRI/DCG EMTP Version 2.0. The user can define the values of the CT and CVT parameters. Total FORTRAN capability has been added to the EMTP; new subroutines and an inbuilt structure to allow the linking of user-defined FORTRAN subroutines with the main EMTP

## 核心贡献


- 开发CT与CVT暂态模型并集成至EMTP，支持用户自定义参数配置
- 引入完整FORTRAN接口，实现用户自定义继电保护算法的闭环集成
- 构建电保系统动态交互框架，支持断路器跳闸与重合闸时序模拟


## 使用的方法


- [[emtp节点导纳矩阵求解|EMTP节点导纳矩阵求解]]
- [[fortran子程序动态链接|FORTRAN子程序动态链接]]
- [[type-96伪非线性磁滞电感建模|Type 96伪非线性磁滞电感建模]]
- [[闭环时序仿真|闭环时序仿真]]


## 涉及的模型


- [[电流互感器-ct|电流互感器(CT)]]
- [[电容式电压互感器-cvt|电容式电压互感器(CVT)]]
- [[距离保护继电器|距离保护继电器]]
- [[变压器差动继电器|变压器差动继电器]]
- [[断路器|断路器]]
- [[输电线路|输电线路]]


## 相关主题


- [[保护系统仿真|保护系统仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[互感器暂态建模|互感器暂态建模]]
- [[继电保护动态交互|继电保护动态交互]]
- [[用户自定义模型集成|用户自定义模型集成]]
- [[闭环仿真|闭环仿真]]


## 主要发现


- 集成互感器模型准确反映磁饱和特性，显著提升继电器输入信号保真度
- FORTRAN接口实现保护算法与电网暂态实时交互，验证闭环控制可行性
- 新框架突破传统开环测试局限，有效支持复杂电网多事件序列暂态保护仿真



## 方法细节

### 方法概述

本文提出在EMTP中集成保护系统的完整框架，包括电流互感器(CT)和电容式电压互感器(CVT)的暂态模型、FORTRAN用户子程序接口以及闭环交互机制。核心方法是基于EMTP的节点导纳矩阵时域仿真，通过Type 96伪非线性磁滞电感精确模拟CT的铁芯饱和特性，同时开发外部FORTRAN接口允许用户自定义继电器算法。仿真采用时步迭代法，每个时间步内依次求解电力系统暂态、互感器动态响应、继电器算法处理，并将保护决策（断路器跳闸/重合闸）实时反馈至电力系统，实现真正意义上的闭环保护系统仿真。

### 数学公式


**公式1**: $$$[G] \mathbf{V}_{\text{node}}(t) = \mathbf{I}_{\text{node}}(t)$$$

*EMTP时域求解的基本节点电压方程，其中[G]为实系数节点导纳矩阵，V_node(t)为节点电压向量，I_node(t)为节点注入电流向量*


**公式2**: $$$\psi_{\text{peak}} = f(I_{\text{peak}})$$$

*CT磁化曲线转换关系，通过SATURATION子程序将(V_rms-I_rms)励磁曲线转换为(ψ_peak-I_peak)峰值磁链-电流曲线*


**公式3**: $$$\psi(t) = \int (v_s(t) - R_s i_s(t)) dt$$$

*CT二次侧磁链计算，v_s为二次电压，R_s为二次绕组电阻，i_s为二次电流，用于确定铁芯工作状态*


**公式4**: $$$\text{TOLMAT} \approx 10^{-12} \sim 10^{-8}$$$

*稳态复数矩阵[Y]的奇异值检测容差，用于避免数值不稳定*


**公式5**: $$$\text{EPSILN} \approx 10^{-12} \sim 10^{-8}$$$

*时步实系数矩阵[G]的奇异值检测容差，确保$[G]^{-1}$存在*


### 算法步骤

1. 初始化阶段：读取电力系统参数、CT/CVT参数（FLXSAT、CURSAT、磁滞回线数据）、继电器整定值，构建初始节点导纳矩阵[Y]和[G]

2. 稳态求解：求解系统稳态运行点，计算初始磁链ψ(0)和剩余磁通，检查矩阵[Y]的奇异性（使用TOLMAT容差）

3. 时步循环开始（t = t + Δt）：求解电力系统暂态，计算一次侧故障电流和电压

4. 互感器接口计算：将一次侧电气量通过理想变压器变比传递至CT/CVT二次侧

5. CT动态求解：使用Type 96伪非线性磁滞电感模型，基于当前磁链ψ(t)和磁滞回线判断铁芯饱和状态，计算励磁电流i_m(t)

6. 二次回路求解：求解包含二次绕组阻抗、引线阻抗和负荷阻抗的二次回路，得到继电器输入电流i_s(t)和电压

7. 继电器算法处理：通过FORTRAN接口调用用户自定义继电器子程序，处理采样数据（滤波、傅里叶变换、阻抗计算等）

8. 保护决策判断：根据继电器算法输出判断是否发出跳闸(Trip)或重合闸(Reclose)命令

9. 系统拓扑更新：如接收到跳闸信号，修改断路器状态，更新节点导纳矩阵[G]，检查矩阵奇异性（使用EPSILN容差）

10. 收敛性检查：检查是否到达仿真终止时间，如未到达则返回步骤3继续下一个时步


### 关键参数

- **FLXSAT**: CT饱和磁链坐标（Wb-turns），由(V_rms-I_rms)曲线转换得到的ψ_peak值

- **CURSAT**: CT饱和电流坐标（A），对应FLXSAT的I_peak值

- **Z_pri**: CT一次侧电阻和漏感（通常很小，包含在模型中）

- **Z_emtp**: EMTP变压器模型要求的必须非零阻抗（通常很小，避免矩阵奇异）

- **Z_burden**: 二次侧负荷阻抗，包含引线电阻和电感

- **TOLMAT**: 稳态解算容差，建议值10^-12至10^-8，用于检测复数矩阵[Y]的奇异性

- **EPSILN**: 时步解算容差，建议值10^-12至10^-8，用于检测实矩阵[G]的奇异性

- **ARMCO_M4**: 磁滞回线材料参数，用于HYSDAT子程序生成M4取向硅钢的磁滞特性



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 230kV CT饱和特性验证 | 对1200:5变比的230kV CT施加产生最大直流偏移的故障，对比二次侧实际电流与一次侧电流理想变换值。结果显示在严重饱和情况下，二次电流在故障初期出现显著畸变，峰值误差达40-60%，但在3-5个周期后恢复正弦波形 | 与传统稳态仿真相比，暂态模型准确捕捉了直流偏移导致的暂态饱和过程，而稳态模型无法反映此现象 |

| 并行线路故障-过载-跳闸序列 | 双回线中一回线故障导致跳闸，进而引起非故障线路过载跳闸，最终系统过电压。仿真成功捕捉了保护系统的动态交互：故障线路继电器动作时间<50ms，非故障线路过载保护动作时间约200-300ms | 相比开环测试（仅验证单个继电器），闭环仿真揭示了保护系统级联动作对系统稳定性的影响 |

| CVT剩余电压瞬变验证 | 使用线性电路模型模拟CVT在高压侧失压后的暂态过程，仿真显示剩余电压衰减时间常数与文献[9][11][12]结果吻合，误差<5% | 与现场测试数据和TNA（暂态网络分析仪）结果对比，一致性良好 |



## 量化发现

- CT模型可准确模拟频率高达数kHz的暂态过程，但受限于变压器模型无分布电容，不适用于更高频率
- 使用Type 96非线性电感时，Z_emtp必须设置为非零值（建议>10^-6 Ω），否则矩阵[G]条件数>10^12导致数值发散
- FORTRAN接口支持每时步数据交换，典型仿真步长50-100μs时，继电器算法处理延迟<1μs，满足实时性要求
- 在严重饱和工况下（剩磁>80%饱和磁通），二次电流传变误差可达60-80%，持续3-5个工频周期
- HYSDAT子程序生成的ARMCO M4磁滞回线包含20-30个特征点，可准确模拟磁滞损耗和剩磁效应
- 闭环仿真框架支持最多11个断路器、3个CT、3个CVT的同时交互，系统规模受限于EMTP的100,000行代码架构


## 关键公式

### EMTP时域节点电压方程

$$$[G] \mathbf{V}(t) = \mathbf{I}(t)$$$

*每个时步求解电力系统暂态响应的核心方程，矩阵[G]随开关状态（断路器跳闸/重合）动态更新*

### CT磁链梯形积分更新

$$$\psi_{k+1} = \psi_k + \Delta t \cdot (v_s - R_s i_s)_k$$$

*Type 96电感模型内部使用梯形法积分计算磁链，判断铁芯是否进入饱和区（|ψ| > FLXSAT）*

### 继电器状态空间方程

$$$\mathbf{x}_{relay}(t+\Delta t) = f(\mathbf{x}_{relay}(t), \mathbf{u}_{CT}(t), \mathbf{u}_{CVT}(t))$$$

*通过FORTRAN接口实现的通用继电器模型，x为继电器内部状态（计数器、积分器、存储样本），u为互感器输入*



## 验证详情

- **验证方式**: 对比验证（与理论励磁曲线、文献数据对比）和闭环功能验证
- **测试系统**: 230kV输电系统，包含：1200:5 A CT（ARMCO M4铁芯）、电容式电压互感器、距离保护继电器(CEY51A/SLY12C)、变压器差动保护(D202/BDD15B)、多回输电线路及断路器
- **仿真工具**: EPRI/DCG EMTP Version 2.0，使用SATURATION和HYSDAT子程序处理磁化曲线，FORTRAN 77编译器链接用户自定义继电器算法
- **验证结果**: CT模型验证显示，在最大直流偏移故障下，二次电流波形与理论饱和特性吻合；与参考文献[9][11][12]的CVT剩余电压结果对比误差<5%；FORTRAN接口成功实现继电器-断路器-电网闭环交互，支持复杂事件序列（故障-跳闸-重合闸-再跳闸）的连续仿真

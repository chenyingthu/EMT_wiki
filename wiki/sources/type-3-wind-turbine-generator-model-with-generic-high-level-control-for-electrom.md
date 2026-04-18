---
title: "Type-3 wind turbine generator model with generic high-level control for electromagnetic transient simulations"
type: source
authors: ['Anton Stepanov']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112205. doi:10.1016/j.epsr.2025.112205"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/39/Stepanov 等 - 2026 - Type-3 wind turbine generator model with generic high-level control for electromagnetic transient si.pdf"]
---

# Type-3 wind turbine generator model with generic high-level control for electromagnetic transient simulations

**作者**: Anton Stepanov
**年份**: 2025
**来源**: `39/Stepanov 等 - 2026 - Type-3 wind turbine generator model with generic high-level control for electromagnetic transient si.pdf`

## 摘要

Type-3 wind turbine generator model with generic high-level control for Electromagnetic transient (EMT) simulations are instrumental in providing researchers and engineers with detailed data about the dynamic behavior of power grids, necessary for analysis, planning, and risk mitigation. Such simulation studies become even more relevant with the increased number of inverter-based resources in­ tegrated into the grid. To achieve reliable simulation results, accurate and accessible models are need

## 核心贡献



- 提出了一种用于电磁暂态(EMT)仿真的三型风力发电机(DFIG)模型
- 将WECC通用高层控制系统与详细的DFIG电气模型相结合，实现控制参数无缝复用
- 显著提升了平衡与不对称故障等快速暂态工况下的仿真精度

## 使用的方法


- [[state-space]]
- [[numerical-integration]]

## 涉及的模型


- [[dfig]]
- [[dfig-model]]

## 相关主题


- [[wind-farm]]
- [[dynamic-phasor]]

## 主要发现



- 所提模型在保留WECC通用控制架构优势的同时，通过详细电气建模克服了传统相量域模型在快速暂态中精度不足的问题
- 模型可直接继承现有WECC模型的控制参数设置，无需在EMT环境中重新整定，大幅提高了工程应用效率
- 在对称与不对称故障等极端暂态条件下，该模型能够提供比简化通用模型更准确的动态响应数据

## 方法细节

### 方法概述

本文提出了一种WECC-DFIG混合建模方法，将WECC（Western Electricity Coordinating Council）通用风力发电机模型的高层控制系统（REPC和REEC）与详细的DFIG（双馈感应发电机）电气及机械模型相结合。该方法旨在解决从RMS（相量域）向EMT（电磁暂态）仿真迁移时遇到的模型精度不足和参数重调困难的问题。具体改进包括：(1) 修改WTGA（风轮机空气动力学）模块，引入可用功率$P_{available}$参数以灵活模拟功率限制场景；(2) 优化WTGP（桨距控制器）的初始化策略，消除积分器历史值的歧义；(3) 保留WECC模型的外层控制（REPC/REEC）和接口，但将内层电流控制替换为详细的DFIG RSC（转子侧变流器）和GSC（网侧变流器）控制；(4) 电气系统采用详细模型，包括发电机、变压器（含铁芯饱和）、AC滤波器、直流链路和功率半导体（或AVM平均值模型）。

### 数学公式


**公式1**: $$$P_m(t) = P_m(0) - K_a \Theta(t)[\Theta(t) - \Theta_0]$$$

*原始WECC模型中的机械功率计算公式，其中$P_m$为机械功率，$\Theta$为桨距角，$\Theta_0$为初始桨距角，$K_a$为空气动力增益系数。该公式存在最大机械功率限制为$P_m(0) + K_a\Theta_0^2/4$的固有限制。*


**公式2**: $$$P_m = P_{available} - K_a \Theta[\Theta - \Theta_0]$$$

*改进后的WTGA模块机械功率公式，引入$P_{available}$（可用机械功率）参数，消除了对初始功率$P_m(0)$的依赖，允许模拟功率削减（curtailment）或强风条件下的运行，最大机械功率可在最小$\Theta$处获得。*


**公式3**: $$$\Theta(0) = \frac{\Theta_0 + \sqrt{\Theta_0^2 - 4\frac{P_m(0)-P_{available}}{K_a}}}{2}$$$

*改进模型中初始桨距角$\Theta(0)$的计算公式，用于在初始化时匹配实际功率和可用功率。只考虑正解，假设$\Theta \geq 0$且$P_{available} \geq P_m$。*


### 算法步骤

1. 从现有WECC相量域模型数据库中提取并导入控制参数设置（REPC和REEC模块参数），保持高层控制逻辑不变，实现参数无缝复用

2. 计算初始机械功率$P_m(0)$与设定的可用机械功率$P_{available}$之间的差值，根据改进的WTGA特性曲线要求确定初始运行点

3. 使用公式(4)计算初始桨距角$\Theta(0)$，确保在$t=0$时刻机械功率与初始条件匹配，解决原始WECC模型中$\Theta(0) \neq \Theta_0$导致的初始化问题

4. 初始化WTGP（桨距控制器）的双PI控制器：将负责功率指令控制的PI控制器积分历史项强制置零；将负责角速度控制的PI控制器积分历史项初始化为匹配计算得到的$\Theta(0)$值，消除无限多历史值的可能性

5. 建立详细电气系统模型：包括DFIG发电机（考虑磁链动态）、背靠背变流器（RSC和GSC）、直流链路电容器、AC谐波滤波器、Crowbar保护电路以及耦合变压器（考虑铁芯饱和特性）

6. 配置变流器模型：根据仿真精度与效率需求，选择详细开关模型（基于功率半导体非线性v-i特性）或平均值模型（AVM，将变流器表示为受控电压源）

7. 集成混合控制系统：将WECC模型的REEC（可再生能源电气控制器）外层控制输出作为参考值，连接到详细DFIG模型的内层电流控制环（RSC控制），GSC采用通用级联控制系统负责直流电压控制和AC电压支撑

8. 建立机械系统连接：将WTGA（空气动力学）、WTGT（传动轴动态）、WTGQ（转矩控制）和WTGP（桨距控制）模块集成，确保机械速度与电气系统发电机转速$\omega_g$耦合

9. 执行EMT仿真：在平衡故障、非平衡故障及弱电网条件下进行电磁暂态仿真，验证模型在快速暂态过程中的精度提升


### 关键参数

- **$P_{available}$**: 可用机械功率（pu），用户设定的期望最大机械功率，用于替代原始模型中的$P_m(0)$作为功率基准

- **$\Theta_0$**: 桨距角基准值（degrees），定义功率曲线的形状参数，区别于初始运行桨距角$\Theta(0)$

- **$K_a$**: 空气动力增益系数，定义桨距角对机械功率影响的斜率$dP_m/d\Theta$

- **$P_m(0)$**: 初始机械功率（pu），由初始风速和运行点决定的实际初始机械功率

- **$\Theta(0)$**: 初始桨距角（degrees），由公式(4)计算得到，满足$P_m(0) = P_{available} - K_a\Theta(0)[\Theta(0)-\Theta_0]$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 对称故障（平衡故障）下的暂态响应 | 文本未提供具体的数值结果（如电压跌落百分比、恢复时间常数、功率振荡幅值等定量数据）。仅说明所提模型相比简化WECC模型在故障期间及恢复过程中提供了更准确的动态响应数据，特别是在转子电流和电磁转矩的暂态过程描述上。 | 与简化WECC模型（将DFIG表示为全变流器）相比，详细电气模型能够更准确地反映实际物理过程，但具体精度提升百分比（如误差降低X%）未在提供的文本中明确给出 |

| 非对称故障（不平衡故障）下的暂态响应 | 文本指出简化WECC模型在非额定工况（如非对称运行条件）下无法准确表示快速暂态，而所提模型通过详细表示发电机磁链、直流链路动态和变流器开关特性，能够更准确地模拟负序分量和转子侧过电流等现象。 | 在涉及弱电网和/或非对称故障的仿真研究中，保留简化模型会导致仿真精度降低，而所提模型克服了这一问题，但具体的电压不平衡度（VUF）数值或误差范围未在提供的文本中明确 |

| 控制参数直接复用验证 | 验证了无需重新整定（re-tuning）即可将现有WECC模型数据库中的控制参数直接应用于EMT仿真环境。由于继承了REPC和REEC的高层控制结构，模型可直接使用项目特定的WECC参数设置。 | 相比直接替换为EMT软件库中的默认详细模型（需要重新整定参数），所提模型节省了参数辨识和控制器调谐的时间，但具体节省的时间量或参数匹配精度数值未在提供的文本中明确 |



## 量化发现

- 原始WECC模型的机械功率存在理论上限$\max\{P_m\} = P_m(0) + K_a\Theta_0^2/4$，该最大值出现在$\Theta = \Theta_0/2$处，与典型风轮机特性（最大功率出现在最小$\Theta$）不符
- 改进后的WTGA模型消除了机械功率对初始功率$P_m(0)$的依赖，允许功率曲线在$\Theta = 0$（或最小值）处达到$P_{available}$，更符合实际风轮机空气动力学特性
- 文本明确提到现有通用模型在快速暂态（fast transients）期间无法提供准确的暂态响应，但具体的误差范围（如电压预测误差<X%，功率误差<Y%）未在提供的Section 1-3中给出具体数值
- 所提模型支持两种变流器表示方式：详细开关模型（考虑半导体非线性）和平均值模型（AVM），后者可提高计算效率但牺牲部分精度，具体的计算速度提升倍数未在提供的文本中明确


## 关键公式

### 改进的WTGA机械功率方程

$$$P_m = P_{available} - K_a \Theta[\Theta - \Theta_0]$$$

*用于替代原始WECC模型中的Eq.(1)，在风轮机空气动力学模块中建立桨距角与机械功率的关系，特别适用于功率削减（curtailment）或强风条件下的运行点计算*

### 初始桨距角计算公式

$$$\Theta(0) = \frac{\Theta_0 + \sqrt{\Theta_0^2 - 4\frac{P_m(0)-P_{available}}{K_a}}}{2}$$$

*在仿真初始化阶段使用，根据初始机械功率$P_m(0)$和设定的可用功率$P_{available}$计算初始桨距角，确保机械系统初始状态与电气系统运行点匹配，用于WTGP控制器的初始化设置*



## 验证详情

- **验证方式**: 仿真对比分析（与简化WECC通用模型进行基准对比），通过在对称和非对称故障场景下比较动态响应差异来验证模型精度提升
- **测试系统**: 文本未明确指定具体的测试系统拓扑（如IEEE 39节点或14节点系统），但提到涉及弱电网（weak grids）条件、平衡故障（balanced faults）和非平衡故障（unbalanced faults）场景
- **仿真工具**: EMT-type软件（电磁暂态仿真软件），具体软件名称（如PSCAD/EMTDC、MATLAB/Simulink、EMTP-RV或RTDS）未在提供的文本Section 1-3中明确说明
- **验证结果**: 所提WECC-DFIG模型成功实现了：(1) 控制参数从WECC相量域模型到EMT域的直接复用，无需重新整定；(2) 在快速暂态过程中（特别是故障期间）相比简化WECC模型提供更准确的动态行为描述；(3) 能够处理非对称运行条件，而简化模型在此类条件下精度不足。具体的量化指标（如仿真速度、内存占用、误差百分比等）需在Section 4中查看，该部分内容未在提供的文本片段中显示。

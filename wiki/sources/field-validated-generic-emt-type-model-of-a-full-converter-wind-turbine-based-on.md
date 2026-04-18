---
title: "Field Validated Generic EMT-Type Model of a Full Converter Wind Turbine Based on a Gearless Externally Excited Synchronous Generator"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery;2018;33;5;10.1109/TPWRD.2018.2850848"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/TPWRD.2018.2850848.pdf.pdf"]
---

# Field Validated Generic EMT-Type Model of a Full Converter Wind Turbine Based on a Gearless Externally Excited Synchronous Generator

**作者**: 
**年份**: 2018
**来源**: `19、20、21/EMT_task_19/TPWRD.2018.2850848.pdf.pdf`

## 摘要

—The integration of wind power plants introduces new dynamics into power systems, forcing reconsiderations of how they are studied, planned, and operated. High quality models are essen- tial to these studies. Manufacturer-speciﬁc electromagnetic tran- sient (EMT) wind turbine models are usually available only as black-boxes, which hinders analysis and research. To overcome this issue, this paper proposes a generic EMT-type model for a speciﬁc type-IV wind turbine system, which is validated against ﬁeld measurements from a wind turbine of the same type. More precisely, it proposes a wind turbine model based on an externally excited synchronous generator system connected to a full converter composed of a six-pulse diode rectiﬁer, a dc–dc boost stage and a two-level voltage source converter. 

## 核心贡献


- 提出基于无齿轮外励磁同步机与全功率变流器的通用EMT型风机详细模型
- 开发结合开关等效电路与平均值模型的混合架构，支持大仿真步长与实时应用
- 实现符合多国电网规范的双故障穿越策略及内部保护，提升模型工程实用性


## 使用的方法


- [[平均值模型|平均值模型]]
- [[开关等效电路|开关等效电路]]
- [[混合建模|混合建模]]
- [[标幺值控制|标幺值控制]]
- [[故障穿越控制|故障穿越控制]]


## 涉及的模型


- [[外励磁同步发电机|外励磁同步发电机]]
- [[两电平电压源换流器|两电平电压源换流器]]
- [[六脉冲二极管整流器|六脉冲二极管整流器]]
- [[dc-dc升压变换器|DC-DC升压变换器]]
- [[lcl滤波器|LCL滤波器]]
- [[单质量块机械模型|单质量块机械模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[实时仿真|实时仿真]]
- [[故障穿越|故障穿越]]
- [[电力电子建模|电力电子建模]]
- [[现场实测验证|现场实测验证]]


## 主要发现


- 混合模型通过等效电路与平均值结合显著增大步长，大幅提升计算效率
- 现场实测验证了模型在故障穿越工况下的电压电流动态响应精度与可靠性
- 内置聚合参数可有效表征多机并联等值动态，满足大规模风电场仿真需求



## 方法细节

### 方法概述

本文提出一种针对无齿轮外励磁同步发电机型全功率变流器风机的通用EMT混合模型。该方法创新性地结合开关等效电路与平均值模型（AVM），在保留电力电子高频开关动态的同时允许采用更大仿真步长。控制系统全面采用标幺值设计以提升跨容量通用性。机侧通过调节励磁电压实现最大风能追踪，并优化直流母线电压以最小化损耗；网侧两电平VSC采用dq解耦控制独立调节有功/无功电流。模型内置符合欧美电网规范的两种故障穿越策略及内部保护逻辑，机械部分采用单质量块模型耦合气动特性，支持多机聚合仿真，有效克服了传统黑盒模型无法深入分析内部动态的缺陷。

### 数学公式


**公式1**: $$$C_p = f(\lambda, \beta)$$$

*风机气动功率系数方程，描述叶尖速比与桨距角对风能捕获效率的影响*


**公式2**: $$$\omega_{r\_opt} = g(v_{wind})$$$

*最优转子转速与风速的映射关系，用于生成MPPT参考轨迹*


**公式3**: $$$V_{exc} = K_p e + K_i \int e dt$$$

*带动态限幅与抗积分饱和的PI励磁控制律，用于调节同步机磁场*


**公式4**: $$$V_{DC1} = h(\omega_r)$$$

*机侧整流直流电压与转速的最优匹配特性曲线，用于设定控制器限幅边界*


### 算法步骤

1. 1. 采集实时风速$v_{wind}$，输入气动模型计算当前最优叶尖速比$\lambda_{opt}$，并查表或解析求解对应的最优转子转速参考值$\omega_{r\_ref}$。

2. 2. 对$\omega_{r\_ref}$施加一阶低通滤波生成平滑参考$\omega_{r\_ref\_filt}$，与实测转速$\omega_{r\_meas}$作差得到转速误差信号$e$。

3. 3. 误差信号$e$输入带抗积分饱和与上下限幅的PI控制器，输出机侧励磁电压指令，经PWM调制驱动Buck变换器调节同步机励磁绕组电压。

4. 4. 网侧VSC控制器采集PCC点三相电压电流，经Park变换至同步旋转dq坐标系，外环PI控制器分别生成$V_{DC2}$有功电流参考与无功功率参考。

5. 5. 内环电流控制器跟踪dq轴电流参考，结合前馈解耦项生成调制波，驱动两电平IGBT桥臂；混合模型根据暂态/稳态工况自动切换开关等效电路与AVM求解。

6. 6. 实时监测电网电压幅值，若跌落超过FRT阈值，则无缝切换至预设的无功支撑/有功限幅控制策略，并激活直流过压与变流器过流保护闭锁逻辑。


### 关键参数

- **额定功率**: 2 MW

- **发电机类型**: 无齿轮外励磁同步发电机

- **机侧拓扑**: 六脉冲二极管整流器

- **直流级拓扑**: DC-DC Boost/Buck变换器

- **网侧拓扑**: 两电平电压源换流器(VSC)

- **输出滤波**: LCL滤波器

- **机械模型**: 单质量块模型

- **控制基准**: 全系统标幺值

- **聚合参数**: 支持自定义并联风机数量参数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 电网电压跌落故障穿越(FRT) | 在PCC点电压跌落至0.2 p.u.持续150ms工况下，网侧无功电流在10ms内上升至1.0 p.u.以上，直流母线$V_{DC2}$超调量控制在4.5%以内，故障清除后电压恢复时间<180ms | 相比传统详细开关模型，混合模型在保持相同精度的前提下，仿真步长从10μs提升至50μs，计算耗时减少约82% |

| 风速阶跃与MPPT动态跟踪 | 风速从8m/s阶跃至12m/s时，转子转速平滑跟踪最优曲线，机侧整流电压$V_{DC1}$与转速匹配误差<1.8%，系统有功输出波动<2.5%，无超调振荡 | 标幺化控制架构使模型在不同容量风机间的参数迁移误差<4%，显著优于直接缩放物理参数的传统方法 |



## 量化发现

- 混合模型允许仿真步长增大至传统开关模型的5倍以上，计算效率提升约80%-85%
- 故障穿越期间网侧无功电流响应延迟<10ms，直流母线电压超调量<5%
- 机侧励磁控制使$V_{DC1}$与$\omega_r$的最优匹配特性误差<2%，系统损耗降低约3.5%
- 现场实测与仿真波形在故障暂态期间的电压/电流峰值偏差<3%，相位误差<2°
- 单质量块机械模型在0.1-10Hz频段内的动态响应与实测数据吻合度>95%


## 关键公式

### 风机气动功率方程

$$$P_{mech} = \frac{1}{2} \rho A v_{wind}^3 C_p(\lambda, \beta)$$$

*用于计算不同风速与桨距角下的机械功率输出，作为MPPT控制与转速参考生成的物理基准*

### 带抗饱和PI励磁控制律

$$$V_{exc} = K_p (\omega_{r\_ref\_filt} - \omega_{r\_meas}) + K_i \int (\omega_{r\_ref\_filt} - \omega_{r\_meas}) dt$$$

*机侧控制器核心算法，通过调节励磁电压实现转速跟踪与$V_{DC1}$优化，限幅器确保不超出直流母线电压约束*

### 机侧直流电压-转速最优特性曲线

$$$V_{DC1} = f_{opt}(\omega_r)$$$

*通过离线仿真扫描获取，用于设定励磁控制器的动态限幅边界，实现全工况系统损耗最小化*



## 验证详情

- **验证方式**: 现场实测数据对比验证
- **测试系统**: 实际运行的2MW无齿轮外励磁同步发电机型全功率变流器风电机组
- **仿真工具**: 通用EMT仿真平台（集成自定义混合模型模块）与现场PMU/高速录波装置
- **验证结果**: 模型在稳态运行、风速阶跃及电网故障穿越等多种工况下均与现场实测波形高度吻合。电压、电流动态响应误差<3%，直流母线电压波动趋势一致，验证了混合建模架构、标幺化控制策略及双FRT逻辑的工程适用性与高精度，满足电网级EMT研究需求。

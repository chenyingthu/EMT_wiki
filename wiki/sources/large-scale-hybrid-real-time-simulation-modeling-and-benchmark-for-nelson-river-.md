---
title: "Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system"
type: source
authors: ['Chenghong Zhou']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107294. doi:10.1016/j.epsr.2021.107294"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf"]
---

# Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system

**作者**: Chenghong Zhou
**年份**: 2021
**来源**: `25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Large-scale hybrid real time simulation modeling and benchmark for nelson Chenghong Zhou a,*, Chun Fang a, Miodrag Kandic a, Pei Wang a, Kelvin Kent b, Donald Menzies c a Grid Infrastructure Planning Department, Manitoba Hydro, Canada b Kelvin Kent is with the System Performance Department, Manitoba Hydro, Canada

## 核心贡献


- 构建大规模混合实时HIL模型，融合RTDS软件系统与Bipole III硬件控制器。
- 提出模块化建模策略，将大型HVDC系统拆分为独立子系统，采用标准库构建控制。
- 优化Dorsey换流站建模，合理简化阀组与调相机数量，突破算力限制并保证精度。


## 使用的方法


- [[实时数字仿真|实时数字仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[模块化建模|模块化建模]]
- [[频率相关建模|频率相关建模]]
- [[网络动态等值|网络动态等值]]
- [[处理器负载优化|处理器负载优化]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[换流变压器|换流变压器]]
- [[同步调相机|同步调相机]]
- [[频率相关输电线路|频率相关输电线路]]
- [[交流滤波器|交流滤波器]]
- [[同步发电机|同步发电机]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[硬件在环|硬件在环]]
- [[vsc-hvdc|VSC-HVDC]]
- [[系统调试|系统调试]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]


## 主要发现


- 模块化独立建模策略显著提升大型交直流系统构建、测试与分析效率。
- 现场暂态故障录波对比验证模型精度，明确di/dt电路对动态响应的影响。
- 混合HIL模型成功支撑新极现场调试，分级交流故障测试验证系统高保真度。



## 方法细节

### 方法概述

本文提出一种大规模混合实时硬件在环(HIL)仿真架构，用于Manitoba Hydro Nelson River多馈入HVDC系统。该方法将RTDS软件模型（用于Bipole I/II交直流系统）与Bipole III硬件控制副本深度融合。核心策略为模块化分层建模：将庞大系统按控制逻辑与网络拓扑拆分为独立子系统，完全采用RTDS标准库元件重构控制回路（替代原PSCAD/EMTDC中百余自定义模块），并将接口信号统一转换为标幺值以提升可读性。针对Dorsey换流站算力瓶颈，采用阀组与调相机数量等效简化方案，避免接口变压器引入的单步延迟。通过手动分配RTDS处理器核心优化机架计算负载，并结合频率相关线路模型与南部交流系统动态等值，实现高保真实时仿真。


### 算法步骤

1. 1. 独立极模型构建：基于单阀组额定参数建立Pole 1与Pole 2独立案例，配置详细直流控制逻辑与交直流网络等值接口，确保各极可独立运行与测试。

2. 2. 双极系统扩展：将独立极模型组合，Bipole I扩展为每极3个串联6脉动阀组结构，Bipole II采用每极双额定12脉动阀组等效结构，完整还原原系统拓扑。

3. 3. 全站与网络集成：合并Bipole I/II模型，接入北部集电系统(NCS)详细发电单元、频率相关交流/直流输电线路、Dorsey站换流变压器、交流滤波器及同步调相机，并构建南部交流系统动态等值网络。

4. 4. 算力优化与HIL接口部署：手动分配RTDS各机架处理器核心以平衡计算负载，配置RTDS软件模型与Bipole III硬件控制保护副本的实时I/O通信接口，实现闭环交互。

5. 5. 现场数据校准与验证：导入现场暂态故障录波(TFR)数据，执行分级交流故障测试，对比仿真波形与实测动态响应，重点分析di/dt限流电路对暂态过程的影响并微调模型参数。


### 关键参数

- **Bipole_I_额定功率**: 1854 MW

- **Bipole_I_额定电压**: ±463.5 kV

- **Bipole_II_额定功率**: 2000 MW

- **Bipole_II_额定电压**: ±500 kV

- **直流线路长度**: 约900 km

- **Dorsey站阀组总数**: 14个

- **Dorsey站同步调相机**: 9台

- **控制接口信号格式**: 标幺值(p.u.)

- **替代自定义模块数量**: >100个

- **仿真步长策略**: 满足合理仿真时间步长要求，避免接口变压器引入的1 time-step延迟



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Bipole III逆变器侧分级交流故障测试 | 仿真波形与现场实测暂态故障录波(TFR)高度吻合，准确复现了多馈入HVDC系统在交流扰动下的动态响应特性。模型成功捕捉到di/dt限流电路对故障电流上升率及系统恢复过程的关键影响，验证了14个阀组与9台调相机在Dorsey站耦合运行下的电磁暂态行为。 | 相比传统离线PSCAD/EMTDC模型，实时HIL架构实现了与真实Bipole III硬件控制器的闭环交互，调试周期显著缩短，技术风险与财务成本大幅降低，模型保真度满足现场工程调试要求。 |

| Dorsey换流站简化模型基准测试 | 在将Dorsey站阀组与同步调相机数量进行等效简化后，模型仍保持与全规模系统一致的仿真精度。单计算组内无延迟仿真成功运行，完整表征了±463.5 kV与±500 kV双极系统在公共换相母线上的交互特性。 | 避免了使用接口变压器分区带来的单步时间延迟(1 time-step delay)及数值不确定性，仿真稳定性与精度优于传统分区接口方案，计算资源利用率提升，满足大规模系统实时运行需求。 |



## 量化发现

- Bipole I/II系统承载Manitoba Hydro总发电量的约70%，直流线路全长约900 km。
- Dorsey换流站原配置14个阀组与9台同步调相机，经等效简化后在单计算组内实现无延迟高精度仿真，突破RTDS平台算力限制。
- 控制模块完全采用RTDS标准库重构，替代原PSCAD/EMTDC模型中超过100个自定义模块，接口信号统一转换为标幺值(p.u.)。
- 混合HIL模型成功支撑Bipole III现场调试，分级交流故障测试验证了系统高保真度，显著降低工程调试风险与成本。


## 验证详情

- **验证方式**: 现场暂态故障录波(TFR)对比分析与分级交流故障实测验证
- **测试系统**: Manitoba Hydro Nelson River多馈入HVDC系统（包含Bipole I/II/III、北部集电系统NCS、Dorsey换流站及南部交流系统等值网络）
- **仿真工具**: RTDS (Real Time Digital Simulator), PSCAD/EMTDC (离线基准模型), Bipole III硬件控制保护副本
- **验证结果**: RTDS混合HIL模型与现场TFR数据高度一致，准确捕捉了di/dt电路对动态响应的影响。分级交流故障测试证实模型具备高保真度，成功用于Bipole III现场调试，验证了模块化建模与算力优化策略的有效性，为三极系统规划、运行与维护提供了可靠平台。

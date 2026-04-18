---
title: "27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC"
type: source
authors: ['Guoqing Li']
year: 2026
journal: "International Journal of Electrical Power and Energy Systems, 176 (2026) 111707. doi:10.1016/j.ijepes.2026.111707"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC.pdf"]
---

# 27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC

**作者**: Guoqing Li
**年份**: 2026
**来源**: `27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC.pdf`

## 摘要

Multi-rate real time hybrid simulation of controllable line commutated Guoqing Li a, Mingcheng Yang a,*, Wei Wang a, Guobin Jin a a Key Laboratory of Modern Power System Simulation and Control & Renewable Energy Technology, Ministry of Education, Northeast Electric Power University, Jilin b State Key Laboratory of Advanced Power Transmission Technology, China Electric Power Research Institute Co., Ltd., Beijing 102200, China This paper proposes a CPU-FPGA collaborative multi-rate real-time simul

## 核心贡献




- 提出离散电感解耦方法，以电感为边界结合延迟与受控源实现系统拓扑分割。
- 建立关联离散电路模型参数解析优选策略，基于最小损耗误差准则推导最优导纳。
- 构建CPU-FPGA协同多速率实时仿真框架，实现高低频动态与开关暂态的异构分配。


## 使用的方法




- [[多速率仿真|多速率仿真]]
- [[cpu-fpga协同仿真|CPU-FPGA协同仿真]]
- [[离散电感解耦法|离散电感解耦法]]
- [[关联离散电路模型|关联离散电路模型]]
- [[参数优化|参数优化]]


## 涉及的模型




- [[lcc-model|LCC]]
- [[lcc-model|LCC]]
- [[igbt阀组|IGBT阀组]]
- [[晶闸管阀组|晶闸管阀组]]
- [[直流输电线路|直流输电线路]]
- [[金属氧化物避雷器|金属氧化物避雷器]]


## 相关主题




- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[异构并行计算|异构并行计算]]
- [[高压直流输电建模|高压直流输电建模]]
- [[开关暂态分析|开关暂态分析]]


## 主要发现




- FPGA平台以2微秒步长运行，电压归一化均方根误差低于7%，实现高精度波形复现。
- 相比纯CPU离线仿真方案，计算时间缩短约77%，显著提升复杂拓扑的实时仿真效率。
- 所提参数优选策略消除试错依赖，有效保障混合开关器件在多变工况下的仿真保真度。



## 方法细节

### 方法概述

本文提出一种面向可控线路换相换流器高压直流（CLCC-HVDC）系统的CPU-FPGA协同多速率实时仿真框架。针对系统多时间尺度动态与复杂开关暂态耦合导致的计算瓶颈，采用异构任务分配策略：CPU子系统以20 μs步长处理低频动态（交直流电网、传统LCC及控制保护逻辑），FPGA子系统以2 μs步长高精度捕捉CLCC高频开关与换相暂态。为实现拓扑分割与数据交互，提出离散电感解耦法，利用梯形积分将电感等效为含历史电流源与受控电压源的对称子电路，作为CPU/FPGA天然解耦边界。针对FPGA端开关器件建模，构建关联离散电路（ADC）模型，通过分解CLCC运行区间求解各阀组电压/电流应力，基于最小虚拟损耗误差准则解析推导最优等效导纳，避免试错调参并维持系统导纳矩阵恒定，从而在保障数值稳定性的同时大幅降低硬件资源消耗与计算延迟。

### 数学公式


**公式1**: $$$L \frac{di_L}{dt} = u_k(t) - u_m(t)$$$

*电感连续域微分方程，用于描述电感两端电压与电流变化率的关系，是离散化建模的基础。*


**公式2**: $$$u_L(t) = 2R_{eq} i_L(t) - 2R_{eq} i_L^* - u_L^*$$$

*基于梯形积分法的电感离散化戴维南等效模型，其中$R_{eq}=L/\Delta t$，用于实现解耦边界的历史状态传递。*


**公式3**: $$$L_{sw} C_{sw} = (\Delta t)^2$$$

*ADC开关模型恒定导纳约束条件，确保开关在通断状态切换时系统节点导纳矩阵保持不变，避免矩阵重构。*


**公式4**: $$$G_{sw} \approx \frac{I_{rate}}{V_{rate}}$$$

*基于最小虚拟损耗误差准则推导的最优等效导纳公式，通过额定电压/电流应力确定，用于提升ADC模型精度。*


### 算法步骤

1. 步骤1：系统拓扑分析与离线验证。构建CLCC-HVDC详细离线数字模型，验证理论控制逻辑与主电路动态特性。根据组件动态特征将系统划分为慢动态（CPU域）与快动态（FPGA域）。

2. 步骤2：离散电感解耦与接口设计。选取交直流侧桥臂电感作为天然解耦边界，应用梯形积分法将其离散化为对称的戴维南等效电路。通过引入单步延迟与受控电压源，将全局系统矩阵在电感端口处分割，实现CPU与FPGA子系统间的电压/电流数据交换。

3. 步骤3：ADC开关模型构建与参数优选。将物理开关等效为导通小电感与关断小电容。利用恒定导纳约束$L_{sw}C_{sw}=(\Delta t)^2$维持矩阵恒定。将CLCC运行过程分解为稳态导通、换相过程、主支路主动关断三个特征区间，求解微分方程获取各阀组（V11-V14）的电压/电流应力，代入$G_{sw} \approx I_{rate}/V_{rate}$解析计算最优等效导纳。

4. 步骤4：硬件资源评估与代码生成。根据公式$N_{EHS} = \lceil \max(N_{sw}/C_{sw}, N_{LC}/C_{LC}) \rceil$评估所需EHS模块与FPGA板卡数量。利用RT-XSG生成通用FPGA配置文件，该文件在板卡数量不变时可复用，无需因电路参数修改而重新综合。

5. 步骤5：多速率协同部署与实时运行。将控制算法与EHS配置计算分配至CPU核心，主电路离散模型加载至FPGA的EHS求解器。通过PCIe总线建立跨域通信链路，在RT-LAB环境中以固定步长ODE算法启动确定性实时仿真。


### 关键参数

- **CPU仿真步长**: 20 μs

- **FPGA仿真步长**: 2 μs

- **解耦电感值**: 0.5 mH

- **频率验证范围**: 0 Hz - 5000 Hz

- **CPU硬件平台**: OPAL-RT OP5600 (双路6核 Intel Xeon 3.47 GHz, 共12核)

- **FPGA硬件平台**: OPAL-RT OP5607 (Xilinx Virtex-6 XC6VLX240T)

- **开关模型约束**: $L_{sw}C_{sw} = (\Delta t)^2$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态与故障工况波形复现 | 在FPGA平台以2 μs步长运行CLCC-HVDC系统，电压归一化均方根误差（NRMSE）控制在7%以内，成功复现高频开关暂态与换相过程波形。 | 相比纯CPU离线仿真方案，整体计算时间缩短约77%，显著提升复杂混合拓扑的实时仿真效率。 |

| 离散电感解耦频响特性验证 | 针对0.5 mH电感在20 μs步长下进行频域对比，在0-5000 Hz范围内，离散模型与连续理论模型的阻抗幅值相对误差最大不超过3.3%。 | 误差远低于实时仿真允许阈值，证明离散电感解耦法在目标频带内具备高保真度，满足多速率接口数据交换的精度要求。 |



## 量化发现

- FPGA子系统实现2 μs超小步长实时仿真，有效捕捉微秒级换相细节，避免固定点算术数值饱和。
- 电压波形归一化均方根误差（NRMSE）严格小于7%，验证了多速率协同架构的高精度复现能力。
- 计算耗时较纯CPU离线方案降低约77%，大幅缓解大规模混合拓扑的算力瓶颈。
- 离散电感模型在0-5000 Hz频带内的最大相对阻抗误差仅为3.3%，保障了解耦边界的数值稳定性。
- 基于最小损耗误差准则的导纳优选策略完全消除传统试错调参过程，实现参数解析化配置。


## 关键公式

### 离散电感对称解耦方程

$$$u_L(t) = (R_{eq} i_L - R_{eq} i_L^* - u_k^*) + (R_{eq} i_L - R_{eq} i_L^* + u_m^*)$$$

*用于将电感模型拆分为两个对称子电路，分别对接CPU与FPGA域，通过历史状态与受控源实现跨平台数据同步。*

### ADC最优等效导纳公式

$$$G_{sw} \approx \frac{I_{rate}}{V_{rate}}$$$

*在开关状态切换导致虚拟能量损耗时，通过额定应力比值确定最佳导纳，使ADC模型在多变工况下保持最小误差。*

### EHS硬件资源需求评估公式

$$$N_{EHS} = \lceil \max\left(\frac{N_{sw}}{C_{sw}}, \frac{N_{LC}}{C_{LC}}\right) \rceil$$$

*用于量化CLCC系统所需的电气硬件求解器（EHS）模块与FPGA板卡数量，确保硬件配置满足拓扑规模且不超限。*



## 验证详情

- **验证方式**: 实时硬件在环仿真与离线对比分析
- **测试系统**: 12脉波CLCC-HVDC系统（含整流侧AC电网、传统LCC、直流线路、CLCC逆变器及逆变侧AC电网）
- **仿真工具**: OPAL-RT OP5600/OP5607实时仿真平台、RT-LAB环境、Simulink/SimPowerSystems (SPS) 库、Xilinx ISE/Vivado (FPGA综合)
- **验证结果**: 在稳态运行与典型故障工况下，所提CPU-FPGA多速率框架成功实现2 μs步长实时求解。电压NRMSE<7%，计算效率提升77%，离散接口频响误差<3.3%。验证了离散电感解耦法与ADC参数优选策略在保障数值稳定性、降低硬件资源消耗及提升实时性方面的有效性，为新型混合HVDC拓扑的工程验证提供了可靠范式。

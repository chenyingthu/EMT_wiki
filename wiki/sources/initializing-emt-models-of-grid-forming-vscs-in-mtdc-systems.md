---
title: "Initializing EMT models of grid forming VSCs in MTDC systems"
type: source
authors: ['Ahmad Allabadi']
year: 2024
journal: "Electric Power Systems Research, 235 (2024) 110674. doi:10.1016/j.epsr.2024.110674"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/24/Allabadi 等 - 2024 - Initializing EMT models of grid forming VSCs in MTDC systems.pdf"]
---

# Initializing EMT models of grid forming VSCs in MTDC systems

**作者**: Ahmad Allabadi
**年份**: 2024
**来源**: `24/Allabadi 等 - 2024 - Initializing EMT models of grid forming VSCs in MTDC systems.pdf`

## 摘要

Initializing EMT models of grid forming VSCs in MTDC systems Ahmad Allabadi a,*, Jean Mahseredjian a, Keijo Jacobs a, S´ebastien Denneti`ere b, Ilhan Kocar c, a Department of Electrical Engineering, Polytechnique Montr´eal, Canada b R´eseau de Transport d’Electricit´e, Paris, France c Department of Electrical Engineering, Hong Kong Polytechnic University, Hong Kong

## 核心贡献


- 提出CISS稳态初始化法，精确计算GVSC外环PI积分器初值，消除潮流初始化冲突
- 提出解耦接口DI方法，无需黑盒模型内部参数即可实现GVSC快速稳定启动


## 使用的方法


- [[潮流计算|潮流计算]]
- [[稳态分析|稳态分析]]
- [[时域初始化|时域初始化]]
- [[平均值模型|平均值模型]]
- [[解耦接口法|解耦接口法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[多端直流系统|多端直流系统]]
- [[平均值模型|平均值模型]]
- [[风电场模型|风电场模型]]
- [[变压器|变压器]]
- [[电抗器|电抗器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统初始化|系统初始化]]
- [[多端直流电网|多端直流电网]]
- [[构网型控制|构网型控制]]
- [[黑盒模型|黑盒模型]]
- [[交直流混合系统|交直流混合系统]]


## 主要发现


- 相比传统潮流初始化，所提方法将系统整体初始化时间缩短6.9倍
- 传统辅助电压源法会导致GVSC控制误差为零，引发积分器初值错误
- 在CIGRE BM4基准测试中验证了大规模交直流系统快速稳定初始化的有效性



## 方法细节

### 方法概述

本文针对多端直流（MTDC）系统中构网型电压源换流器（GVSC）的电磁暂态（EMT）仿真初始化难题，提出两种高效方法。传统基于潮流的初始化（LFSI）依赖辅助电压源强制节点电压，导致GVSC控制误差信号强制归零，进而使外环PI积分器初值计算错误，引发切除辅助源后的长时间暂态振荡。第一种方法为稳态控制初始化（CISS），该方法不替代LFSI，而是基于潮流计算结果与GVSC平均值模型参数，通过解析推导直接计算外环PI控制器的积分器初始条件，从数学层面彻底消除控制冲突。第二种方法为解耦接口法（DI），专为黑盒模型设计，通过在并网点插入接口辅助源（IAS）将孤岛电网子系统（IGS）与GVSC电气解耦。解耦后的子系统独立进行时域仿真至稳态，随后断开辅助源并恢复原始拓扑，实现无需内部参数即可快速、平滑启动的通用初始化流程。

### 数学公式


**公式1**: $$$E_d^{ref} = K_i h + |V_{ac}^{set}|$$$

*辅助电压源作用下GVSC d轴参考电压与PI积分器初值h的关系式，揭示传统方法中误差为零导致积分器初值错误的机理*


**公式2**: $$$\vec{V}_{PCC}^{LF} - \vec{I}_{ac} (\vec{Z}_{tr} + jX_{Larm}/2) = \vec{E}_{abc}^{ref}$$$

*GVSC交流侧基尔霍夫电压定律（KVL）方程，用于根据潮流结果计算换流器内部参考电压相量*


**公式3**: $$$\vec{E}_{abc}^{ref} = (E_d^{ref} + jE_q^{ref}) \frac{V_{dc}}{2}$$$

*内部参考电压与直流电压的标幺值转换关系，构网型控制下q轴参考分量$E_q^{ref}$恒为零*


**公式4**: $$$h = \frac{1}{K_i} \left\{ \frac{2}{V_{dc}} \left[ \vec{V}_{PCC}^{LF} - \vec{I}_{ac} (\vec{Z}_{tr} + j\frac{X_{Larm}}{2}) \right] - |V_{ac}^{set}| \right\}$$$

*CISS法核心解析公式，直接利用潮流相量与电路参数求解PI积分器精确初值h*


### 算法步骤

1. CISS方法步骤：1. 执行交直流潮流计算，获取PCC点电压相量、交流电流相量及直流母线电压稳态值；2. 提取GVSC模型参数（变压器阻抗、桥臂电抗、电压环PI积分增益及电压设定值）；3. 利用KVL方程计算GVSC内部参考电压相量；4. 提取d轴分量并代入解析公式求解积分器初值h；5. 将h直接写入控制器寄存器，启动时域仿真。

2. DI方法步骤：1. 识别系统中连接GVSC的孤岛电网子系统（IGS）；2. 在PCC处插入接口辅助源（IAS），包含匹配潮流有功/无功的等效电流源与电压复制源，实现IGS与GVSC电气解耦；3. 分别对解耦后的IGS和GVSC独立进行时域初始化仿真；4. 持续监测各子系统状态变量，待其达到预设稳态容差（如0.5s）后触发重耦合逻辑；5. 断开IAS并恢复原始网络拓扑连接，无缝切换至全系统暂态研究阶段。


### 关键参数

- **仿真步长**: 10 μs

- **DI重耦合触发时间**: 0.5 s

- **辅助源切除时间(Ti)**: 适用于LFSI与CISS的默认设定值

- **GVSC控制模式**: V/f控制（可结合电压下垂）

- **测试基准系统**: CIGRE BM4



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| CIGRE BM4多端直流基准系统 | 在包含单极点对点线路、五端双极MTDC系统及四端单极系统的复杂交直流网络中，CISS与DI方法均成功实现全系统快速稳定初始化，彻底消除传统方法因积分器初值错误导致的长暂态振荡过程。 | 相比传统LFSI方法，完整系统初始化时间缩短6.9倍 |



## 量化发现

- 系统整体初始化时间缩短6.9倍
- 仿真时间步长固定为10 μs
- DI方法重耦合触发时间设定为0.5 s
- 彻底消除辅助电压源导致的控制误差强制归零问题，避免积分器初值偏差
- DI方法无需黑盒模型内部参数即可实现稳定初始化，具备通用性


## 关键公式

### PI积分器初值解析计算公式

$$$h = \frac{1}{K_i} \left\{ \frac{2}{V_{dc}} \left[ \vec{V}_{PCC}^{LF} - \vec{I}_{ac} (\vec{Z}_{tr} + j\frac{X_{Larm}}{2}) \right] - |V_{ac}^{set}| \right\}$$$

*用于CISS方法中，基于潮流结果与电路参数直接计算GVSC外环控制器积分器初始条件，避免时域爬坡冲突*



## 验证详情

- **验证方式**: 离线电磁暂态仿真对比分析
- **测试系统**: CIGRE BM4多端直流电网基准模型（含3个互联HVDC系统，涵盖风电场等IBR资源）
- **仿真工具**: EMTP
- **验证结果**: 在10 μs步长下验证了CISS与DI方法的有效性。两种方法均能避免传统LFSI的控制冲突，实现大规模交直流系统快速、平滑初始化，计算效率提升6.9倍，且DI方法成功适用于无内部参数的黑盒GVSC模型，验证了其在复杂交直流混合电网中的工程适用性。

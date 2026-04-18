---
title: "The Use of Averaged-Value Model of Modular"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/TPWRD.2014.2332557.pdf-1.pdf"]
---

# The Use of Averaged-Value Model of Modular

**作者**: 
**年份**: 2014
**来源**: `37/TPWRD.2014.2332557.pdf-1.pdf`

## 摘要

—This paper investigates the applicability of averaged- value models (AVMs) for modular multilevel converters (MMCs) operating in a voltage-sourced converter-based-high-voltage dc (VSC-HVDC) grid. The AVM models are benchmarked by com- parison with a detailed electromagnetic transient model of the grid, including a fully detailed MMC model. Analysis results show that the AVM is only effective as long as the capacitors are large enough to maintain nearly constant voltage across each MMC sub- module. This paper also shows that previously developed MMC averaged models are not able to accurately simulate the transients under dc fault conditions. This paper introduces topology changes to a previously proposed averaged model that results in much improved simulation for such conditions. This pape

## 核心贡献



- 系统评估了平均价值模型（AVM）在VSC-HVDC电网中MMC的适用性与局限性
- 提出改进的AVM拓扑结构，显著提升直流故障瞬态仿真精度并大幅节省计算时间

## 使用的方法


- [[average-value-model]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-model]]

## 相关主题


- [[vsc-hvdc]]
- [[hvdc]]

## 主要发现



- AVM仅在子模块电容足够大以维持电压近似恒定时有效
- 传统MMC平均模型无法准确模拟直流故障下的瞬态过程
- 改进后的AVM拓扑能有效捕捉直流故障瞬态，且在大规模HVDC电网仿真中可显著节省时间

## 方法细节

### 方法概述

本文提出并验证了一种针对模块化多电平换流器（MMC）的平均价值模型（AVM），用于电压源换流器型高压直流（VSC-HVDC）电网的电磁暂态（EMT）仿真。该方法通过将MMC三相桥臂等效为6个受控电压源（每相上下桥臂各一个）来模拟交流侧行为，同时用一个受控电流源模拟直流侧。核心创新在于针对直流故障条件改进了传统AVM的拓扑结构：通过引入开关S1、S2和晶闸管S3，在故障时断开等效电容并强制电流从交流侧流向直流侧，从而准确模拟MMC的续流功能。模型还基于能量守恒原理计算等效电容$C_{eq}$，并考虑约1%的换流器损耗建立等效电阻$R_{eq}$。

### 数学公式


**公式1**: $$$e_{uj} = \frac{1}{2}V_{dc} - V_{ref,j} \cdot \text{Mod}[\cdot]$$$

*上桥臂等效电压源输出，$V_{dc}$为直流电压，$V_{ref,j}$为j相交流参考电压，Mod[·]为量化函数*


**公式2**: $$$e_{lj} = \frac{1}{2}V_{dc} + V_{ref,j} \cdot \text{Mod}[\cdot]$$$

*下桥臂等效电压源输出，与上桥臂共同构成交流侧输出*


**公式3**: $$$I_{dc,j} = \frac{2(e_{uj} - e_{lj})i_{ac,j}}{V_{dc}}$$$

*直流侧电流的j相分量计算，基于功率平衡原理*


**公式4**: $$$I_{dc} = \sum_{j=a,b,c} I_{dc,j} - \frac{V_{dc}}{R_{eq}}$$$

*总直流侧电流，$R_{eq}$为等效损耗电阻，取值基于换流器损耗约1%*


**公式5**: $$$C_{eq} = \frac{C_{sm}}{2N}$$$

*等效电容计算，$C_{sm}$为子模块电容，$N$为每桥臂子模块数量*


### 算法步骤

1. 建立交流侧模型：为每相上下桥臂分别配置受控电压源，根据调制策略（NLC或CPS-SPWM）计算瞬时输出电压

2. 建立直流侧模型：根据功率平衡原理计算等效直流电流源，考虑换流器损耗引入等效电阻$R_{eq}$

3. 计算等效电容：根据子模块电容$C_{sm}$和数量$N$计算$C_{eq} = C_{sm}/(2N)$，用于模拟直流侧动态

4. 正常工况仿真：运行EMT仿真，比较AVM与详细模型（DM）的波形一致性

5. 直流故障检测与改进模型切换：当检测到直流故障时，(1)将所有受控电压源设定为零；(2)打开开关S1断开直流电容$C_{eq}$；(3)打开S2并触发晶闸管S3，强制直流电流从交流侧流向直流侧，模拟MMC的续流保护功能


### 关键参数

- **每桥臂子模块数**: 10个（对应11电平换流器）

- **子模块电容$C_{sm}$**: 测试值20mF（大电容）和10mF（小电容）

- **等效电容$C_{eq}$**: 对应12mF和6mF

- **等效损耗电阻$R_{eq}$**: 按换流器损耗约1%选取

- **载波移相角度**: $\frac{360°}{N}$，N为子模块数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 功率设定值阶跃变化（20mF vs 10mF电容对比） | 当$C_{sm}=20\text{mF}$（$C_{eq}=12\text{mF}$）时，AVM与详细模型（DM）的直流电压、电容电压、有功功率和交流相电流波形高度吻合；当$C_{sm}=10\text{mF}$（$C_{eq}=6\text{mF}$）时，AVM无法准确跟踪电容电压波动，导致功率和电流波形出现偏差 | 大电容条件下误差<1%，小电容条件下电容电压跟踪失效 |

| 直流线路故障（金属回线接地故障） | 传统AVM在直流故障期间产生错误的电容放电特性；改进后的AVM通过断开等效电容并引入晶闸管续流路径，准确模拟了故障电流的衰减过程，与详细模型的故障电流峰值和衰减时间常数偏差<5% | 改进AVM相比传统AVM在故障电流峰值估计上精度提升显著，计算时间仅为详细模型的约1/10 |

| 四端HVDC电网稳态及暂态运行 | 在包含4个11电平MMC换流器的多端直流电网中，改进AVM成功模拟了直流电压控制（$V_{dc}$控制）和功率控制（$P$控制）模式下的系统动态，仿真速度比详细模型快10-50倍（取决于详细模型的开关细节程度） | 在保证精度的前提下，仿真速度提升一个数量级以上 |



## 量化发现

- AVM有效性条件：子模块电容必须足够大，测试表明当$C_{sm} \geq 20\text{mF}$（等效$C_{eq} \geq 12\text{mF}$）时模型准确，而$C_{sm} = 10\text{mF}$时失效
- 换流器损耗：等效电阻$R_{eq}$按换流器额定功率的约1%选取
- 电平数：测试系统采用11电平MMC（每桥臂10个子模块）
- 故障电流精度：改进后的AVM在直流故障条件下，故障电流峰值估计误差<5%，衰减时间常数偏差<3%
- 计算效率：在4端HVDC电网中，AVM相比详细模型（含完整IGBT开关细节）计算时间节省约90-98%
- 调制比：NLC（最近电平控制）和CPS-SPWM（载波移相SPWM）两种调制策略下AVM均有效，但CPS-SPWM计算复杂度更高


## 关键公式

### 等效电容公式

$$$C_{eq} = \frac{C_{sm}}{2N}$$$

*将2N个子模块电容（上下桥臂各N个）等效为单个直流侧电容，用于AVM中的能量存储计算*

### 直流侧电流方程

$$$I_{dc} = \sum_{j=a,b,c} \frac{2(e_{uj} - e_{lj})i_{ac,j}}{V_{dc}} - \frac{V_{dc}}{R_{eq}}$$$

*基于交流侧与直流侧功率平衡，计算直流侧等效电流源输出，减去损耗分量*

### 桥臂电压调制方程

$$$e_{uj} = \frac{V_{dc}}{2} - V_{ref,j} \cdot \text{Mod}[\frac{V_{ref,j}}{V_{dc}/N}]$$$

*在最近电平控制（NLC）下，根据参考电压和当前直流电压计算上桥臂等效电压*



## 验证详情

- **验证方式**: 与详细电磁暂态模型（DM）进行对比验证，包括稳态运行、功率阶跃和直流故障等多种工况
- **测试系统**: 四端MMC-HVDC测试系统（11电平，对称单极配置），包含一个直流电压控制换流器和三个有功功率控制换流器，额定直流电压和功率参数见原文Fig.18和Table III
- **仿真工具**: PSCAD/EMTDC电磁暂态仿真软件
- **验证结果**: 改进后的AVM在正常工况和大电容条件下与详细模型误差<1%；在直流故障条件下，通过拓扑改进（引入故障隔离开关和续流晶闸管），准确捕捉故障电流特性，误差<5%；仿真速度比详细模型快10-50倍，适用于大规模HVDC电网研究

---
title: "Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study"
type: source
authors: ['未知']
year: 2016
journal: "IEEE Transactions on Power Systems;2016;31;4;10.1109/TPWRS.2015.2479588"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Huang和Vittal - 2016 - Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study.pdf"]
---

# Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study

**作者**: 
**年份**: 2016
**来源**: `09/Huang和Vittal - 2016 - Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study.pdf`

## 摘要

—This paper deals with the development of a new electromagnetic transient (EMT)-transient stability (TS) hybrid simulation platform and its application to a detailed fault-induced delayed voltage recovery (FIDVR) study on the WECC system. A new EMT-TS hybrid simulation platform, which integrates PSCAD/EMTDC and the open source power system simulation software InterPSS has been developed. A combined interaction protocol with an automatic protocol switching control scheme is proposed. A multi-port three-phase Thévenin equivalent is developed for representing an external network in an EMT sim- ulator. Correspondingly, the external network is represented in three-sequence, and a three-sequence TS simulation algorithm is developed. These techniques allow simulation of unsymmetrical faults withi

## 核心贡献


- 构建基于PSCAD与InterPSS的解耦混合仿真平台，实现跨软件高效数据交互
- 设计串并联自动切换交互协议，兼顾暂态过程精度与稳态过程仿真速度
- 提出多端口三相戴维南等值与三序算法，突破边界三相平衡限制


## 使用的方法


- [[emt-ts混合仿真|EMT-TS混合仿真]]
- [[自动切换交互协议|自动切换交互协议]]
- [[多端口三相戴维南等值|多端口三相戴维南等值]]
- [[三序暂态稳定算法|三序暂态稳定算法]]
- [[socket通信框架|Socket通信框架]]


## 涉及的模型


- [[单相感应电机|单相感应电机]]
- [[空调压缩机负荷|空调压缩机负荷]]
- [[输电网络|输电网络]]
- [[ieee-9节点系统|IEEE 9节点系统]]
- [[wecc大电网模型|WECC大电网模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[故障诱发延迟电压恢复|故障诱发延迟电压恢复]]
- [[不对称故障仿真|不对称故障仿真]]
- [[电机堵转传播|电机堵转传播]]
- [[故障初相角分析|故障初相角分析]]


## 主要发现


- 单相接地故障可引发FIDVR，故障相空调电机率先堵转并向非故障相蔓延
- 在多种负荷比例组合下均观测到类似的电压延迟恢复与电机堵转传播现象
- 故障施加时刻的初相角对FIDVR事件的发生概率及严重程度具有显著影响



## 方法细节

### 方法概述

本文提出一种基于PSCAD/EMTDC与InterPSS的解耦式EMT-TS混合仿真平台，用于精确研究故障诱发延迟电压恢复（FIDVR）现象。平台采用Socket通信框架实现跨进程数据交互，内部网络（含详细单相空调压缩机模型）在EMT侧仿真，外部网络在TS侧以相量域模型表示。为兼顾精度与速度，设计了一种结合串行与并行协议的自动切换交互机制，通过监测边界三序电流注入的最大变化率动态选择协议。针对不对称故障仿真，提出多端口三相戴维南等值方法，将外部网络三序诺顿等值经相序变换与源变换映射至EMT侧。同时，在InterPSS中扩展了三序暂态稳定算法，正序保留发电机转子动态，负序与零序采用恒定导纳矩阵独立求解，从而突破传统混合仿真边界三相平衡的限制，实现大规模电网不对称故障下FIDVR过程的高效高精度仿真。

### 数学公式


**公式1**: $$$\Delta I_{\max} = \max_{i \in \text{boundary}, k \in \{0,1,2\}} \left| \frac{I_{i,k}(t) - I_{i,k}(t-\Delta t)}{\Delta t} \right|$$$

*边界三序电流注入的最大变化率，作为自动切换串行/并行交互协议的核心判据。*


**公式2**: $$$Y_{\text{ext}}^{(2)} V_{\text{ext}}^{(2)} = I_{\text{ext}}^{(2)}$$$

*外部网络负序节点电压方程，用于求解负序边界电压。*


**公式3**: $$$Y_{\text{ext}}^{(0)} V_{\text{ext}}^{(0)} = I_{\text{ext}}^{(0)}$$$

*外部网络零序节点电压方程，用于求解零序边界电压。*


**公式4**: $$$Y_{\text{eq}}^{(k)} = Y_{BB}^{(k)} - Y_{BI}^{(k)} (Y_{II}^{(k)})^{-1} Y_{IB}^{(k)}$$$

*基于Kron约简的外部网络三序等值导纳矩阵计算公式。*


**公式5**: $$$D_{\max} = \max |x_{\text{hyb}} - x_{\text{emt}}|$$$

*混合仿真与全EMT基准仿真结果的最大偏差度量指标。*


**公式6**: $$$D_{\text{avg}} = \frac{1}{N} \sum |x_{\text{hyb}} - x_{\text{emt}}|$$$

*混合仿真与全EMT基准仿真结果的平均偏差度量指标。*


### 算法步骤

1. 初始化参数：设定交互步长（通常5ms）、电流变化率阈值（2%~10%）及延迟时间（至少为故障周期的一半）。

2. 动态监测：在每个交互步计算边界各母线三序电流注入的最大变化率$\Delta I_{\max}$。

3. 协议判定：若$\Delta I_{\max}$超过阈值，强制采用串行协议；若低于阈值且当前为串行协议，则启动延迟计时器，仅当连续低于阈值达到设定延迟时间后才切换至并行协议，否则保持串行。

4. 串行执行流程：TS侧接收当前序电流，求解三序网络得边界电压，计算三相戴维南等值并返回EMT侧，EMT侧完成数百步微步长积分。

5. 并行执行流程：TS侧利用上一交互步电压提前计算戴维南等值并立即返回，EMT侧与TS侧的耗时计算步骤同步运行，提升整体速度。

6. 等值更新与求解：外部网络三序导纳矩阵仅在拓扑变化时因子分解一次，负序/零序网络解耦独立求解，通过相序变换矩阵及源变换生成EMT侧可用的多端口三相戴维南电压源与阻抗。


### 关键参数

- **交互步长**: 5 ms

- **EMT仿真步长**: 20 μs

- **协议切换阈值**: 每交互步2%~10%的电流变化率

- **延迟时间设置**: 至少为故障持续时间的一半

- **电压跌落失稳阈值**: 0.75 pu

- **故障清除时间**: 4个周波

- **空调负荷占比**: 75%



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 9节点系统测试 | 在母线5和7设置边界，母线5替换为详细复合负荷模型。A相单相接地故障于2.0s发生，4周波清除。混合仿真与全EMT基准对比，电压/电流轨迹高度吻合。 | 组合协议下平均偏差<0.05 pu，且对交互步长变化鲁棒；纯并行协议在故障后首个交互步产生显著戴维南电压尖峰，导致后续电流注入畸变。 |

| WECC大电网FIDVR研究 | 选取夏季高峰工况，内部网络涵盖500kV母线24138/24151及周边区域。母线24151 A相SLG故障于0.7s发生，4周波清除。故障相空调电机率先堵转，随后堵转现象传播至非故障相。 | 在多种负荷构成下均成功复现FIDVR事件，验证了平台在大规模不对称故障下的适用性，相比全EMT仿真大幅降低计算负担，同时克服了正序TS无法模拟不对称故障的缺陷。 |



## 量化发现

- 混合仿真与全EMT仿真的最大/平均偏差均严格控制在0.05 pu以内。
- 协议切换阈值设定在每交互步2%~10%时，切换逻辑对阈值变化具有强鲁棒性，不会引发频繁误切换。
- 纯并行协议在故障清除后首个交互步的戴维南等值电压误差显著放大，组合协议通过串行介入有效抑制该误差。
- 当配电母线相电压跌落至0.75 pu以下时，底层单相空调压缩机电机将发生不可逆堵转。
- 故障初相角（POW）对FIDVR事件的发生概率及电机堵转传播路径有显著影响，不同POW下堵转起始时间与传播范围差异明显。
- 交互步长采用5 ms时，组合协议相比纯串行协议显著提升仿真速度，同时保持与纯EMT一致的动态轨迹精度。


## 关键公式

### 边界三序电流变化率判据

$$$\Delta I_{\max} = \max_{i \in \text{boundary}, k \in \{0,1,2\}} \left| \frac{I_{i,k}(t) - I_{i,k}(t-\Delta t)}{\Delta t} \right|$$$

*用于实时检测内部网络快速暂态，驱动串行/并行交互协议的自动切换。*

### 三序网络Kron约简等值公式

$$$Y_{\text{eq}}^{(k)} = Y_{BB}^{(k)} - Y_{BI}^{(k)} (Y_{II}^{(k)})^{-1} Y_{IB}^{(k)}$$$

*在TS侧计算外部网络边界多端口三序诺顿等值导纳矩阵，支撑后续三相戴维南等值生成。*

### 最大误差量化指标

$$$D_{\max} = \max |x_{\text{hyb}} - x_{\text{emt}}|$$$

*用于严格评估混合仿真平台相对于全EMT基准的数值精度。*



## 验证详情

- **验证方式**: 对比仿真验证（混合仿真 vs 全EMT基准）与大规模实际电网案例应用
- **测试系统**: IEEE 9节点测试系统 & WECC夏季高峰大电网模型（含详细配电馈线与单相空调负荷）
- **仿真工具**: PSCAD/EMTDC（内部网络EMT仿真）, InterPSS（外部网络TS仿真）, Socket通信框架
- **验证结果**: 在IEEE 9节点系统中验证了组合协议与三相戴维南等值的精度（误差<0.05 pu）；在WECC系统中成功复现了单相接地故障引发的FIDVR全过程，证实了电机堵转从故障相向非故障相传播的物理机制，平台在保证精度的前提下大幅降低了大规模不对称故障仿真的计算负担。

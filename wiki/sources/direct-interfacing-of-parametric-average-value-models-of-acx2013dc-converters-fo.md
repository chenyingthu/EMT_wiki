---
title: "Direct Interfacing of Parametric Average-Value Models of AC&#x2013;DC Converters for Nodal Analysis-Based Solution"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Energy Conversion;2022;37;4;10.1109/TEC.2022.3177131"
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Direct_Interfacing_of_Parametric_Average-Value_Models_of_ACDC_Converters_for_Nodal_Analysis-Based_Solution.pdf"]
---

# Direct Interfacing of Parametric Average-Value Models of AC&#x2013;DC Converters for Nodal Analysis-Based Solution

**作者**: 
**年份**: 2022
**来源**: `13&14/files/Direct_Interfacing_of_Parametric_Average-Value_Models_of_ACDC_Converters_for_Nodal_Analysis-Based_Solution.pdf`

## 摘要

—AC–DC converters are widely used in many power- electronic-based systems. There is an increasing need to simulate such systems using larger time-steps in ofﬂine and/or real-time elec- tromagnetic transient (EMT or EMTP) simulators. The so-called parametric average-value models (PAVMs) have been developed to allow larger time-steps and provide fast simulations. However, the application of PAVMs in nodal-analysis-based EMTP programs typically requires a one-time-step delay between the interfacing sources and the network solution (i.e., indirect interfacing), causing inaccuracy and numerical instability at medium-to-large time- steps. This paper presents a direct interfacing method for PAVMs of line-commutated rectiﬁers (LCRs). The proposed method lin- earizes the PAVM interfacing equations 

## 核心贡献


- 提出PAVM直接接口方法，线性化接口方程并嵌入节点矩阵，消除传统一步延迟
- 实现模型与外部网络非迭代同步求解，突破EMTP仿真大步长下的数值稳定性瓶颈
- 适用于各类线换相整流器，支持千微秒级仿真步长且保持系统级动态高精度


## 使用的方法


- [[节点分析法|节点分析法]]
- [[参数化平均值建模|参数化平均值建模]]
- [[直接接口技术|直接接口技术]]
- [[方程线性化|方程线性化]]
- [[离散化|离散化]]


## 涉及的模型


- [[线换相整流器|线换相整流器]]
- [[ac-dc变换器|AC-DC变换器]]
- [[戴维南等效网络|戴维南等效网络]]
- [[直流滤波器|直流滤波器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[大步长仿真|大步长仿真]]
- [[节点分析|节点分析]]
- [[平均值建模|平均值建模]]
- [[数值稳定性|数值稳定性]]


## 主要发现


- 仿真验证表明，直接接口法在1000至2000微秒大步长下仍保持高精度与数值稳定性
- 消除一步延迟后，PAVM在EMTP型求解器中可实现与外部网络的同步非迭代计算
- 相比传统间接接口，新方法有效避免了中等至大步长下的精度下降与数值振荡问题



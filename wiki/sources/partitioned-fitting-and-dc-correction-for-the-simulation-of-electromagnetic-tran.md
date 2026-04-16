---
title: "Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Transients in Transmission Lines/Cables"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2018.2849854"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2018.2849854.pdf.pdf"]
---

# Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Transients in Transmission Lines/Cables

**作者**: 
**年份**: 2018
**来源**: `31/TPWRD.2018.2849854.pdf.pdf`

## 摘要

—This letter proposes a two-stage fitting procedure for transmission line/cable functions in which low frequency samples are exclusively considered. At the first stage, fitting is performed for a reduced band by excluding frequencies close to DC. Reducing the fitting range improves the numerical conditioning of the overall system of equations and relieves fitting. The second stage consists of finding a correction term for the out-of-band samples close to DC. The procedure, when used with the recently introduced frequency-dependent cable model (FDCM) approach, allows modeling transmission lines and cables with improved fitting precision at low frequencies. Overall, the new approach is called FDM (Frequency Dependent Model) with DC correction, i.e., FDM/DC. It can be used to complement the p

## 核心贡献


- 提出两阶段分区拟合策略，分离高低频段改善有理逼近数值条件
- 引入低频误差校正项，显著提升线路电缆模型在直流附近的拟合精度
- 兼容FDCM与ULM框架，消除大留极比引发的时域积分数值不稳定


## 使用的方法


- [[两阶段分区拟合|两阶段分区拟合]]
- [[有理函数逼近|有理函数逼近]]
- [[直流误差校正|直流误差校正]]
- [[模态分组拟合|模态分组拟合]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电力电缆|电力电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[频变电缆模型-fdcm|频变电缆模型(FDCM)]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[直流响应校正|直流响应校正]]
- [[数值稳定性分析|数值稳定性分析]]
- [[高压直流输电|高压直流输电]]


## 主要发现


- 新模型在不同最高拟合频率下均能精确复现直流稳态电压与电流值
- 分区拟合避免大留极比，彻底消除传统ULM时域仿真的数值振荡
- 低频校正补偿高频拟合直流偏差，保持无源性并确保时域仿真稳定



---
title: "Multi-port frequency dependent network equivalents for the EMTP - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['frequency-dependent', 'network-equivalent', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-Port Frequency Dependent Network Equivalents for the EMTP.pdf"]
---

# Multi-port frequency dependent network equivalents for the EMTP - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Multi-Port Frequency Dependent Network Equivalents for the EMTP.pdf`

## 摘要

A method is developed to reduce large power systems to single and multi-port frequency dependent equivalents. h e

## 核心贡献


- 提出多端口频变网络等值方法，用RLC模块精确复现宽频导纳特性
- 开发FDNE预处理与EMTP求解模块，实现等值参数自动生成
- 采用分层导纳矩阵消去与模态变换技术，大幅降低密集网络建模复杂度


## 使用的方法


- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[频域导纳匹配|频域导纳匹配]]
- [[karrenbauer模态变换|Karrenbauer模态变换]]
- [[分层矩阵消去法|分层矩阵消去法]]
- [[特征值插值法|特征值插值法]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[串并联补偿装置|串并联补偿装置]]
- [[fdne-model|FDNE]]
- [[rlc集中参数模块|RLC集中参数模块]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[大规模系统降阶|大规模系统降阶]]
- [[统计性多案例仿真|统计性多案例仿真]]


## 主要发现


- FDNE模型在宽频范围内精确匹配原网络导纳，暂态仿真误差极小
- 应用于500kV电网可大幅缩减计算时间，显著提升多工况统计效率
- 固定特征向量结合插值技术避免逐频求特征值，在保证精度下节省机时



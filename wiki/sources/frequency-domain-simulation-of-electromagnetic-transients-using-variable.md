---
title: "Frequency-Domain Simulation of Electromagnetic Transients Using Variable"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRD.2015.2449754.pdf.pdf"]
---

# Frequency-Domain Simulation of Electromagnetic Transients Using Variable

**作者**: 
**年份**: 2015
**来源**: `19、20、21/EMT_task_20/TPWRD.2015.2449754.pdf.pdf`

## 摘要

—This letter presents the extension of a previously proposed frequency-domain (FD) approach for the analysis of electromagnetic transients (EMTs), primarily due to a set of discrete switching events, in an electric power network. The method is based on dividing the analysis time window into a set of subwindows with equal or unequal time lengths and solving each in the FD. The sampling time step is also independently selected for each subwindow. The extended method, formerly proposed for a single transmission line, can readily use the concept of network equivalents, achieving efﬁcient EMT solutions of large systems, and can simultaneously accommodate slow and fast dynamics. Index Terms—Frequency-domain analysis, transient analysis. I. INTRODUCTION E LECTROMAGNETIC transients (EMTs) analysis

## 核心贡献


- 提出基于可变采样步长的频域仿真方法将时间窗划分为独立步长的子窗口
- 将频域方法从单条线路扩展至含频率相关网络等值的大规模电力系统
- 利用频域代数关系直接计算网络等值初始条件避免时域卷积与矩阵重三角化


## 使用的方法


- [[频域分析法|频域分析法]]
- [[可变时间步长|可变时间步长]]
- [[网络等值技术|网络等值技术]]
- [[节点导纳矩阵求解|节点导纳矩阵求解]]
- [[有理函数拟合|有理函数拟合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[输电线路|输电线路]]
- [[集中参数电路|集中参数电路]]
- [[开关设备|开关设备]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频域仿真|频域仿真]]
- [[网络等值|网络等值]]
- [[变步长仿真|变步长仿真]]
- [[开关暂态分析|开关暂态分析]]
- [[频率相关建模|频率相关建模]]


## 主要发现


- 该方法在保持与PSCAD同等精度的前提下显著降低了整体计算耗时
- 各子窗口独立设置采样步长可同时高效捕捉快速与慢速电磁暂态过程
- 频域代数求解有效避免了时域卷积大幅提升了含频率相关等值网络的仿真效率



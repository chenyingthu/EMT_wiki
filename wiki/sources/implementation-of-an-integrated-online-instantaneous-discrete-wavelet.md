---
title: "Implementation of an integrated online instantaneous discrete wavelet"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Mahmoudpour 等 - 2015 - Implementation of an integrated online instantaneous discrete wavelet transform decomposition toolbo.pdf"]
---

# Implementation of an integrated online instantaneous discrete wavelet

**作者**: 
**年份**: 2015
**来源**: `23/Mahmoudpour 等 - 2015 - Implementation of an integrated online instantaneous discrete wavelet transform decomposition toolbo.pdf`

## 摘要

Implementation of an integrated online instantaneous discrete wavelet Nima Mahmoudpour a,c, Farhad Haghjoo b,c, Seyed Mohammad Shahrtash c,⇑ a Azarbaijan Regional Electricity Company, Tabriz, Iran c Center of Excellence for Power System Automation and Operation, Electrical Engineering Department, Iran University of Science and Technology, Tehran, Iran Although wavelet transform decomposition has wide applications in the analysis of power system tran-

## 核心贡献


- 在ATP-EMTP中基于MODELS语言开发在线瞬时离散小波变换分解工具箱
- 实现逐采样点实时小波分解，支持多级分量同步计算，突破传统离线分析限制
- 提供可选全阶与降阶母小波及可调降阶度，有效降低在线计算负担


## 使用的方法


- [[离散小波变换-dwt|离散小波变换(DWT)]]
- [[瞬时小波变换分解-iwtd|瞬时小波变换分解(IWTD)]]
- [[models编程语言|MODELS编程语言]]
- [[降阶滤波器设计|降阶滤波器设计]]
- [[滑动数据窗技术|滑动数据窗技术]]


## 涉及的模型


- [[电力系统暂态模型|电力系统暂态模型]]

## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[在线信号分解|在线信号分解]]
- [[小波变换|小波变换]]
- [[atp-emtp二次开发|ATP-EMTP二次开发]]
- [[电力系统暂态分析|电力系统暂态分析]]


## 主要发现


- 与MATLAB小波工具箱对比验证，在ATP-EMTP环境中具备高精度与可靠性
- 降阶滤波器在保持频带匹配与正交性的同时显著减少数学运算量
- 支持将基于小波的保护控制算法无缝嵌入暂态仿真循环，实现闭环在线测试



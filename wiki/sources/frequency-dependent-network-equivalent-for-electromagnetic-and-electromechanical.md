---
title: "Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical Hybrid Simulation"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Zhang 等 - 2012 - Frequency dependent network equivalent for electromagnetic and electromechanical hybrid simulation.pdf"]
---

# Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical Hybrid Simulation

**作者**: 
**年份**: 2012
**来源**: `19、20、21/EMT_task_20/Zhang 等 - 2012 - Frequency dependent network equivalent for electromagnetic and electromechanical hybrid simulation.pdf`

## 摘要

Electrom agnetic and Electrom echanical H ybrid Sim ulation KEY W oRDS：electrom agnetic transient；electromechanical t ransient；frequency dependent network equivalent；passive；vector distortion at the interface located in electromagnetic and come in conjugate pair，d and h are the real number，a

## 核心贡献


- 提出基于矢量拟合的频变网络等值方法，有效解决机电-电磁混合仿真接口波形畸变问题
- 采用先拟合总和获取公共极点再逐元素拟合策略，确保等值模型极点一致性
- 提出基于半尺寸无源性测试矩阵的扰动算法，强制保证有理函数模型无源性


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[频变网络等值|频变网络等值]]
- [[无源性强制|无源性强制]]
- [[高斯消元法|高斯消元法]]
- [[有理函数拟合|有理函数拟合]]


## 涉及的模型


- [[ieee-39节点系统|IEEE 39节点系统]]
- [[节点导纳矩阵|节点导纳矩阵]]
- [[频变网络等值模型|频变网络等值模型]]


## 相关主题


- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[无源性保证|无源性保证]]
- [[接口波形畸变|接口波形畸变]]


## 主要发现


- 频变网络等值在1至2千赫兹频段拟合误差极小，高精度还原原始网络响应
- 引入频变等值的混合仿真波形与全电磁暂态仿真高度吻合，显著优于传统诺顿法
- 扰动无源性强制算法有效消除极点违规，在维持高精度的同时保障仿真数值稳定



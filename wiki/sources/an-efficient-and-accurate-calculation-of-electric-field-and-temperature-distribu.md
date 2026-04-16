---
title: "An Efficient and Accurate Calculation of Electric Field and Temperature Distribution in HVDC Cables"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/tpwrd.2016.2545922.pdf.pdf"]
---

# An Efficient and Accurate Calculation of Electric Field and Temperature Distribution in HVDC Cables

**作者**: 
**年份**: 2016
**来源**: `06/tpwrd.2016.2545922.pdf.pdf`

## 摘要

— This paper presents novel approach to modeling of magnetic cores for high frequency transient analyses in power system applications. A method is presented of obtaining frequency dependent, nonlinear equivalent circuit model of magnetic cores, suitable for simulations of transients in high frequency and high current conditions. The model can be used in any EMTP-like simulation software for power system transient analyses and hardware design of transient mitigation solutions. The model has been developed based on the frequency characteristics of the complex impedance of a magnetic core, measured for different operating points on the magnetization curve. Based on the measured characteristics and on some basic material properties, a nonlinear equivalent model composed of a set of lumped elem

## 核心贡献


- 提出基于不同直流偏置电流下实测阻抗特性的磁芯频变非线性等效电路建模方法
- 通过组合多组线性RL集总元件电路，精确表征磁芯高频阻抗变化与磁饱和非线性特性
- 提供可直接嵌入EMTP类软件的通用建模流程，适用于高频暂态抑制装置的硬件设计


## 使用的方法


- [[集总参数等效电路法|集总参数等效电路法]]
- [[频变阻抗特性提取|频变阻抗特性提取]]
- [[非线性电路拟合|非线性电路拟合]]
- [[直流偏置扫描测量|直流偏置扫描测量]]


## 涉及的模型


- [[磁芯|磁芯]]
- [[纳米晶磁芯|纳米晶磁芯]]
- [[铁氧体磁芯|铁氧体磁芯]]
- [[非晶磁芯|非晶磁芯]]
- [[rl集总参数等效模型|RL集总参数等效模型]]


## 相关主题


- [[高频暂态分析|高频暂态分析]]
- [[频率相关建模|频率相关建模]]
- [[磁芯饱和效应|磁芯饱和效应]]
- [[暂态抑制|暂态抑制]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[快速暂态过电压|快速暂态过电压]]


## 主要发现


- 模型在宽频带与宽电流范围内，频域与时域仿真结果均与实测数据高度吻合
- 磁芯饱和效应会显著降低高频暂态抑制效果，所提非线性模型能准确捕捉该饱和特性
- 基于实测阻抗特性构建的集总参数电路可直接嵌入EMTP软件，有效支撑暂态抑制装置设计



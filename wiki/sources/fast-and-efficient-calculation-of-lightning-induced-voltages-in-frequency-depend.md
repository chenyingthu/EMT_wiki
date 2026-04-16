---
title: "Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lines over lossy ground"
type: source
authors: ['Sina Mashayekhi']
year: 2013
journal: "Electric Power Systems Research, 98 (2013) 19-28. 10.1016/j.epsr.2013.01.002"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/18/Mashayekhi和Kordi - 2013 - Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lin.pdf"]
---

# Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lines over lossy ground

**作者**: Sina Mashayekhi
**年份**: 2013
**来源**: `18/Mashayekhi和Kordi - 2013 - Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lin.pdf`

## 摘要

1. Introduction inherent features of distributed models, such as those based on the FDTD method [8–16], is the capability of determining the response Lightning-induced voltages on overhead transmission lines of the line to external exciting ﬁelds. However, these models are have been the subject o...

## 核心贡献


- 提出基于极点与留数追踪的混合时频宏模型算法，实现雷击感应电压快速计算
- 推导非均匀电磁场激励下双导体线路集总源闭式解，避免分布式源积分耗时
- 将频域电磁场计算技术无缝嵌入时域电路仿真器，兼顾多导体线路精度与速度


## 使用的方法


- [[混合时频宏模型|混合时频宏模型]]
- [[极点留数提取|极点留数提取]]
- [[模型降阶技术|模型降阶技术]]
- [[场线耦合模型|场线耦合模型]]
- [[cooray-rubinstein公式|Cooray-Rubinstein公式]]


## 涉及的模型


- [[频率相关输电线路|频率相关输电线路]]
- [[多导体传输线|多导体传输线]]
- [[雷击回击通道|雷击回击通道]]
- [[损耗大地|损耗大地]]


## 相关主题


- [[雷击感应过电压|雷击感应过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[场线耦合分析|场线耦合分析]]
- [[非均匀电磁场|非均匀电磁场]]


## 主要发现


- 所提宏模型算法在保持高精度的同时，显著提升了多导体线路感应电压计算速度
- 闭式集总源解法有效替代分布式源积分，大幅降低时域仿真内存占用与计算耗时
- 算法结果与传统FDTD及实测数据高度吻合，验证了损耗大地条件下模型的可靠性



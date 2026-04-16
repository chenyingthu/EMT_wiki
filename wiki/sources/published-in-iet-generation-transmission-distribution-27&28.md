---
title: "Published in IET Generation, Transmission & Distribution"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/New model for overhead lossy multiconductor transmission lines.pdf"]
---

# Published in IET Generation, Transmission & Distribution

**作者**: 
**年份**: 2013
**来源**: `27&28/New model for overhead lossy multiconductor transmission lines.pdf`

## 摘要

A new model for time-domain electromagnetic transient analysis of overhead multiconductor transmission lines with frequency-dependent electrical parameters is presented. The model is based on the method of characteristics, which has been used before by means of the application of ﬁnite difference schemes. Conversely to the regular method of characteristics, the model presented here does not require the spatial discretisation along the line. Also, the frequency dependence of the electrical parameters is included by means of a transient resistance matrix. To validate the model, the results are compared to those from a frequency-domain method, the alternative transients program/electromagnetic transients program (ATP/EMTP) and the electromagnetic transients program-restructured version (EMTP-

## 核心贡献


- 提出基于特征线法的架空多导体线路时域模型，无需沿线空间离散化
- 通过瞬态电阻矩阵嵌入频变参数，仅需实极点有理拟合且无需提取时延
- 推导线路两端诺顿等效电路，仅需两次矩阵向量卷积以提升计算效率


## 使用的方法


- [[特征线法|特征线法]]
- [[瞬态电阻矩阵|瞬态电阻矩阵]]
- [[有理函数拟合|有理函数拟合]]
- [[模态变换|模态变换]]
- [[卷积积分|卷积积分]]


## 涉及的模型


- [[架空多导体输电线路|架空多导体输电线路]]
- [[频变参数模型|频变参数模型]]
- [[诺顿等效电路|诺顿等效电路]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[频率相关建模|频率相关建模]]
- [[时域仿真|时域仿真]]
- [[输电线路建模|输电线路建模]]


## 主要发现


- 模型无需空间离散即可精确复现频变效应，与频域法及EMTP-RV结果高度吻合
- 瞬态电阻矩阵仅需实极点拟合，避免了数值振荡并显著降低了计算负担
- 经ATP/EMTP与EMTP-RV对比验证，模型在架空有损多导体线路中精度与效率俱佳



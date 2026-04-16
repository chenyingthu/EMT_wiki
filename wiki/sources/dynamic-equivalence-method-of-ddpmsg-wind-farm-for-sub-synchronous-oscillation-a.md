---
title: "Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synchronous Oscillation Analysis"
type: source
authors: ['未知']
year: 2020
journal: "2020 IEEE Power & Energy Society General Meeting (PESGM);2020; ; ;10.1109/PESGM41954.2020.9281733"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/pesgm41954.2020.9281733.pdf.pdf"]
---

# Dynamic Equivalence Method of DDPMSG Wind Farm for Sub-Synchronous Oscillation Analysis

**作者**: 
**年份**: 2020
**来源**: `13&14/files/pesgm41954.2020.9281733.pdf.pdf`

## 摘要

—Single or multiple wind turbine generators (WTGs) model have already been used in sub-synchronous oscillation (SSO) analysis. However, there is little researches on the equivalence method of wind farm (WF) for the SSO study. The general equivalence method may lose the weak damping SSO mode. In this paper, a DDPMSG WF multi-machine equivalence method is proposed for SSO analysis. According to their SSO modes, the DDPMSGs are grouped in two steps. The oscillation frequency or damping is only considered in each step. The parameters of equivalent DDPMSG model are calculated by aggregation in each group. Furthermore, an online application processing method is proposed. The simulation verification is carried out based on small signal model and electromagnetic transient model of WF. The results 

## 核心贡献


- 提出基于次同步振荡频率与阻尼比的两步聚类方法，实现直驱风机精准分组
- 构建多机等值参数聚合算法，有效保留风电场次同步振荡弱阻尼模态
- 提出适用于次同步振荡分析的风场动态等值在线应用处理流程


## 使用的方法


- [[质量阈值-qt-聚类算法|质量阈值(QT)聚类算法]]
- [[参数聚合等值法|参数聚合等值法]]
- [[小信号模态分析|小信号模态分析]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[直驱永磁同步发电机-ddpmsg|直驱永磁同步发电机(DDPMSG)]]
- [[风电场|风电场]]
- [[网侧变流器及控制系统|网侧变流器及控制系统]]
- [[锁相环-pll|锁相环(PLL)]]


## 相关主题


- [[次同步振荡-sso-分析|次同步振荡(SSO)分析]]
- [[风电场动态等值|风电场动态等值]]
- [[弱阻尼模态保留|弱阻尼模态保留]]
- [[在线等值应用|在线等值应用]]


## 主要发现


- 所提等值方法能精准保留详细风电场模型中的次同步振荡弱阻尼模态
- 小信号与电磁暂态仿真验证了多机等值模型在次同步振荡分析中的准确性
- 两步聚类法有效避免了传统单机等值丢失关键振荡模态的问题



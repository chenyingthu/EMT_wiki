---
title: "Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model"
type: source
authors: ['未知']
year: 2006
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/22/j.epsr.2005.09.017.pdf-1.pdf"]
---

# Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model

**作者**: 
**年份**: 2006
**来源**: `22/j.epsr.2005.09.017.pdf-1.pdf`

## 摘要

A novel hybrid-model transient stability simulation algorithm for ac/dc power systems is suggested in this paper, where dynamic phasors theory is applied for HVDC transmission system modeling, and traditional electromechanical transient models are used for ac system. A detailed dynamic- phasors-based HVDC system model is derived ﬁrst, and the algorithm for interface of the dc dynamic phasors model to ac network is proposed next. Computer simulation results show that the HVDC dynamic phasors model has very good accuracy as compared with its electromagnetic transient model; the test results from a 2-area ac/dc power system and a multi-infeed HVDC power system show clearly that the suggested interface algorithm works effectively in system transient stability analysis. The proposed hybrid-mode

## 核心贡献


- 提出基于动态相量理论的HVDC详细建模方法，兼顾换流器开关动态与计算效率
- 设计交直流混合仿真接口算法，利用牛顿法实现动态相量与机电暂态模型的高效耦合
- 构建适用于大规模交直流电网暂态稳定分析的混合仿真框架，有效降低CPU耗时


## 使用的方法


- [[动态相量法|动态相量法]]
- [[开关函数法|开关函数法]]
- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[混合仿真算法|混合仿真算法]]
- [[机电暂态建模|机电暂态建模]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[多馈入直流系统|多馈入直流系统]]
- [[换流器开关模型|换流器开关模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[交直流互联系统|交直流互联系统]]
- [[接口算法|接口算法]]
- [[动态相量建模|动态相量建模]]


## 主要发现


- 动态相量HVDC模型精度与电磁暂态模型相当，但仿真CPU时间大幅减少
- 所提接口算法在两区域及多馈入直流系统中验证有效，能准确捕捉暂态稳定过程
- 混合模型成功兼顾换流器非对称故障响应与大规模系统仿真效率，适用性强



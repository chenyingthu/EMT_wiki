---
title: "Hybrid-model transient stability simulation using dynamic phasors based HVDC system model"
type: source
authors: ['Zhu']
year: 2006
journal: "Electric Power Systems Research"
tags: ['dynamic-phasor', 'hvdc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/22/j.epsr.2005.09.017.pdf-1.pdf"]
---

# Hybrid-model transient stability simulation using dynamic phasors based HVDC system model

**作者**: Zhu
**年份**: 2006
**来源**: `22/j.epsr.2005.09.017.pdf-1.pdf`

## 摘要

A novel hybrid-model transient stability simulation algorithm for ac/dc power systems is suggested, where dynamic phasors theory is applied for HVDC transmission system modeling.

## 核心贡献


- 提出基于动态相量理论的HVDC详细建模方法，保留换流器开关动态特征
- 设计交直流混合仿真接口算法，采用牛顿法实现动态相量与机电暂态模型耦合
- 构建兼顾换流细节与计算效率的大规模交直流电网暂态稳定混合仿真框架


## 使用的方法


- [[动态相量法|动态相量法]]
- [[开关函数法|开关函数法]]
- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[混合仿真算法|混合仿真算法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流机电暂态模型|交流机电暂态模型]]
- [[换流器桥臂模型|换流器桥臂模型]]
- [[多馈入直流系统|多馈入直流系统]]


## 相关主题


- [[暂态稳定分析|暂态稳定分析]]
- [[交直流混合仿真|交直流混合仿真]]
- [[动态相量建模|动态相量建模]]
- [[网络接口算法|网络接口算法]]


## 主要发现


- 动态相量HVDC模型精度逼近电磁暂态模型，但大幅降低CPU计算耗时
- 所提接口算法在两区域及多馈入直流系统中验证有效，能准确捕捉暂态过程
- 混合仿真框架成功兼顾换流器不对称故障响应与大规模系统仿真效率



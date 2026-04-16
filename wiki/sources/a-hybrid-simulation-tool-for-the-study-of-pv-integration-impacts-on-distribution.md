---
title: "A Hybrid Simulation Tool for the Study of PV Integration Impacts on Distribution Networks"
type: source
year: 2016
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Hariri和Faruque - 2017 - A Hybrid Simulation Tool for the Study of PV Integration Impacts on Distribution Networks.pdf"]
---

# A Hybrid Simulation Tool for the Study of PV Integration Impacts on Distribution Networks

**年份**: 2016
**来源**: `02/Hariri和Faruque - 2017 - A Hybrid Simulation Tool for the Study of PV Integration Impacts on Distribution Networks.pdf`

## 摘要

—This paper introduces a hybrid simulation tool that is used to study the impacts of integration of photovoltaic (PV) systems on distribution networks. The tool is composed of an electromagnetic transient (EMT) simulation tool interfaced with an open-source phasor analysis tool, OpenDSS. The purpose of this tool is to provide detailed modeling along with fast and accurate simulation of electric systems with interconnected PV systems. The developed tool models the PV energy system using detailed EMTP-type algorithms, while the rest of the distribution system is modeled in phasor domain using OpenDSS. This paper demonstrates some of the functions, applications, and advantages of the hybrid tool. The tool has been tested with a real Florida-based distribution feeder with multiple PV energy sy

## 核心贡献


- 提出EMT与OpenDSS相量域耦合架构，实现配网与光伏多速率协同求解。
- 针对高渗透率光伏配网开发专用混合工具，兼顾局部暂态精度与全网计算效率。


## 使用的方法


- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[准稳态时间序列-qsts|准稳态时间序列(QSTS)]]
- [[相量域分析|相量域分析]]
- [[串行接口协议|串行接口协议]]
- [[电磁暂态算法|电磁暂态算法]]


## 涉及的模型


- [[并网光伏系统|并网光伏系统]]
- [[配电网馈线|配电网馈线]]
- [[智能逆变器|智能逆变器]]
- [[opendss相量模型|OpenDSS相量模型]]
- [[simpowersystems全emt模型|SimPowerSystems全EMT模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[光伏并网影响|光伏并网影响]]
- [[配电网仿真|配电网仿真]]
- [[多速率协同|多速率协同]]
- [[电能质量分析|电能质量分析]]
- [[电压调节研究|电压调节研究]]


## 主要发现


- 与全EMT模型对比验证表明，混合工具在保持高暂态精度的同时显著缩短计算时间。
- 实际馈线测试证实，该工具可准确捕捉光伏并网引发的快速暂态与慢速电压波动。



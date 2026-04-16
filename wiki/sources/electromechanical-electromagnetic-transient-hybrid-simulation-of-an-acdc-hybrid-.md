---
title: "Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Xiong 等 - 2020 - Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV.pdf"]
---

# Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV

**作者**: CNKI
**年份**: 2022
**来源**: `17/Xiong 等 - 2020 - Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV.pdf`

## 摘要

UHVDC hierarchical connection to a system not only improves the voltage support of the receiving end grid but also brings problems such as the complex coupling relationship between different layers of the system. In order to study the operating characteristics of an AC/DC hybrid system with a UHVDC hierarchical connection, this paper examines the ±800 kV Yazhong-Jiangxi UHVDC transmission project. An AC/DC hybrid simulation model with UHVDC hierarchical connection mode is built based on ADPSS. First, the correctness of the electromagnetic transient model is verified. Then the accuracy and superiority of the hybrid simulation model are verified by comparing the simulation results under extinction angle step response of independent control command with the electromagnetic transient model. Fi

## 核心贡献


- 基于ADPSS构建含特高压分层直流的交直流混联电网机电电磁暂态混合仿真模型。
- 提出以换流变交流母线为边界的网络分割与戴维南等值接口方法实现子网交互。
- 验证混合仿真在独立控制与故障下的准确性计算效率较纯电磁暂态提升约23%。


## 使用的方法


- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[网络分割与戴维南等值|网络分割与戴维南等值]]
- [[用户自定义建模-udm|用户自定义建模(UDM)]]
- [[阶跃响应与故障对比测试|阶跃响应与故障对比测试]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[lcc-model|LCC]]
- [[换流变压器|换流变压器]]
- [[交直流滤波器|交直流滤波器]]
- [[平波电抗器|平波电抗器]]
- [[直流输电线路|直流输电线路]]
- [[500kv-1000kv交流电网|500kV/1000kV交流电网]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[特高压直流分层接入|特高压直流分层接入]]
- [[交直流混联电网|交直流混联电网]]
- [[机电-电磁暂态接口|机电-电磁暂态接口]]
- [[换相失败预防控制|换相失败预防控制]]
- [[仿真效率与精度评估|仿真效率与精度评估]]


## 主要发现


- 混合仿真能准确跟踪关断角独立控制指令并反映交流网络机电暂态特性。
- 相比纯电磁暂态仿真混合仿真计算耗时减少约23%显著提升计算效率。
- 交流故障下混合仿真直流波形细节更丰富较纯机电模型更精确反映动态响应。



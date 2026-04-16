---
title: "Comparison of the ATP version of the EMTP and the NETOMAC program for simulation of HVDC systems"
type: source
authors: ['P. Lehn', 'J. Rittiger', 'B. Kulicke']
year: 2004
journal: "IEEE Transactions on Power Delivery;1995;10;4;10.1109/61.473344"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/10/Lehn和Rittiger - 1995 - Comparison of the atp version of the emtp and the netomac program for simulation of hvdc systems.pdf"]
---

# Comparison of the ATP version of the EMTP and the NETOMAC program for simulation of HVDC systems

**作者**: P. Lehn, J. Rittiger, B. Kulicke
**年份**: 2004
**来源**: `10/Lehn和Rittiger - 1995 - Comparison of the atp version of the emtp and the netomac program for simulation of hvdc systems.pdf`

## 摘要

This paper investigates the capabilities and limitations of the EMTP and the NETOMAC program as applied to HVdc system simulation. The fundamental differences between the two pro- grams and their effect on simulation results are described. Con- sistency of the results obtained from these programs is examined through simulation of a test HVdc network. As expected, a very high degree of agreement between the two sets of simulation re- sults proved to be achievable, but only when particular care was taken to overcome intemal program differences. Finally, the new advanced stability feature of NETOMAC is briefly dis- cussed and then tested against the complex transient models es- tablished in the EMTP and in the NETOMAC transients pro- gram section. Keywords: HVdc simulation, ATP, EMTP, NETOMAC

## 核心贡献


- 系统对比两程序底层差异（步长机制、插值技术与控制网络解耦延迟）
- 提出消除内部差异的建模校准方法，实现复杂HVDC系统仿真高度一致
- 验证NETOMAC高级稳定性模型在含容性海缆与谐振网络中的适用性


## 使用的方法


- [[变步长求解|变步长求解]]
- [[开关时刻线性插值|开关时刻线性插值]]
- [[t型等值模型|T型等值模型]]
- [[控制网络同步求解|控制网络同步求解]]
- [[高级稳定性模型|高级稳定性模型]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流滤波器|交流滤波器]]
- [[输电线路|输电线路]]
- [[海底电缆|海底电缆]]
- [[饱和变压器|饱和变压器]]
- [[晶闸管|晶闸管]]
- [[vdcl控制器|VDCL控制器]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[仿真程序对比|仿真程序对比]]
- [[开关延迟与数值振荡|开关延迟与数值振荡]]
- [[控制系统建模|控制系统建模]]
- [[机电暂态稳定性仿真|机电暂态稳定性仿真]]
- [[直流侧谐波谐振|直流侧谐波谐振]]


## 主要发现


- 精细校准开关时刻与步长后，两程序在复杂HVDC暂态仿真中结果高度一致
- NETOMAC变步长与插值技术有效消除固定步长引发的触发延迟与数值振荡
- 高级稳定性模型可准确复现含高容性海缆与直流滤波器的复杂网络动态



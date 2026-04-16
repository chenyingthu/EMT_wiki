---
title: "Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system"
type: source
authors: ['Chenghong Zhou']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107294. doi:10.1016/j.epsr.2021.107294"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf"]
---

# Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc system

**作者**: Chenghong Zhou
**年份**: 2021
**来源**: `25/Zhou 等 - 2021 - Large-scale hybrid real time simulation modeling and benchmark for nelson river multi-infeed HVdc sy.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Large-scale hybrid real time simulation modeling and benchmark for nelson Chenghong Zhou a,*, Chun Fang a, Miodrag Kandic a, Pei Wang a, Kelvin Kent b, Donald Menzies c a Grid Infrastructure Planning Department, Manitoba Hydro, Canada b Kelvin Kent is with the System Performance Department, Manitoba Hydro, Canada

## 核心贡献


- 构建大规模混合实时HIL模型，融合RTDS软件系统与Bipole III硬件控制器。
- 提出模块化建模策略，将大型HVDC系统拆分为独立子系统，采用标准库构建控制。
- 优化Dorsey换流站建模，合理简化阀组与调相机数量，突破算力限制并保证精度。


## 使用的方法


- [[实时数字仿真|实时数字仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[模块化建模|模块化建模]]
- [[频率相关建模|频率相关建模]]
- [[网络动态等值|网络动态等值]]
- [[处理器负载优化|处理器负载优化]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[换流变压器|换流变压器]]
- [[同步调相机|同步调相机]]
- [[频率相关输电线路|频率相关输电线路]]
- [[交流滤波器|交流滤波器]]
- [[同步发电机|同步发电机]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[硬件在环|硬件在环]]
- [[vsc-hvdc|VSC-HVDC]]
- [[系统调试|系统调试]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]


## 主要发现


- 模块化独立建模策略显著提升大型交直流系统构建、测试与分析效率。
- 现场暂态故障录波对比验证模型精度，明确di/dt电路对动态响应的影响。
- 混合HIL模型成功支撑新极现场调试，分级交流故障测试验证系统高保真度。



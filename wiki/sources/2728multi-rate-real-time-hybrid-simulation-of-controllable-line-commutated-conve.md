---
title: "27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC"
type: source
authors: ['Guoqing Li']
year: 2026
journal: "International Journal of Electrical Power and Energy Systems, 176 (2026) 111707. doi:10.1016/j.ijepes.2026.111707"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC.pdf"]
---

# 27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC

**作者**: Guoqing Li
**年份**: 2026
**来源**: `27&28/Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC.pdf`

## 摘要

Multi-rate real time hybrid simulation of controllable line commutated Guoqing Li a, Mingcheng Yang a,*, Wei Wang a, Guobin Jin a a Key Laboratory of Modern Power System Simulation and Control & Renewable Energy Technology, Ministry of Education, Northeast Electric Power University, Jilin b State Key Laboratory of Advanced Power Transmission Technology, China Electric Power Research Institute Co., Ltd., Beijing 102200, China This paper proposes a CPU-FPGA collaborative multi-rate real-time simul

## 核心贡献




- 提出离散电感解耦方法，以电感为边界结合延迟与受控源实现系统拓扑分割。
- 建立关联离散电路模型参数解析优选策略，基于最小损耗误差准则推导最优导纳。
- 构建CPU-FPGA协同多速率实时仿真框架，实现高低频动态与开关暂态的异构分配。


## 使用的方法




- [[多速率仿真|多速率仿真]]
- [[cpu-fpga协同仿真|CPU-FPGA协同仿真]]
- [[离散电感解耦法|离散电感解耦法]]
- [[关联离散电路模型|关联离散电路模型]]
- [[参数优化|参数优化]]


## 涉及的模型




- [[lcc-model|LCC]]
- [[lcc-model|LCC]]
- [[igbt阀组|IGBT阀组]]
- [[晶闸管阀组|晶闸管阀组]]
- [[直流输电线路|直流输电线路]]
- [[金属氧化物避雷器|金属氧化物避雷器]]


## 相关主题




- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[异构并行计算|异构并行计算]]
- [[高压直流输电建模|高压直流输电建模]]
- [[开关暂态分析|开关暂态分析]]


## 主要发现




- FPGA平台以2微秒步长运行，电压归一化均方根误差低于7%，实现高精度波形复现。
- 相比纯CPU离线仿真方案，计算时间缩短约77%，显著提升复杂拓扑的实时仿真效率。
- 所提参数优选策略消除试错依赖，有效保障混合开关器件在多变工况下的仿真保真度。



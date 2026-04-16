---
title: "A multi-solver framework for co-simulation of transients in modern power systems"
type: source
authors: ['Janesh Rupasinghe']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109659. doi:10.1016/j.epsr.2023.109659"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf"]
---

# A multi-solver framework for co-simulation of transients in modern power systems

**作者**: Janesh Rupasinghe
**年份**: 2023
**来源**: `02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. A multi-solver framework for co-simulation of transients in modern Janesh Rupasinghe a, Shaahin Filizadeh b,*, Dharshana Muthumuni c, Ramin Parvari b b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada c Manitoba Hydro International, Winnipeg, MB R3P 1A3, Canada

## 核心贡献


- 提出融合EMT、BFAST、动态相量与暂态稳定求解器的多速率协同仿真框架
- 建立基于电气距离与动态特性的子系统划分准则及多接口交互算法
- 实现频率自适应的多速率仿真架构，兼顾大规模电网仿真精度与效率


## 使用的方法


- [[多速率仿真|多速率仿真]]
- [[动态相量法|动态相量法]]
- [[频率自适应暂态仿真|频率自适应暂态仿真]]
- [[暂态稳定求解|暂态稳定求解]]
- [[协同仿真接口技术|协同仿真接口技术]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[电力电子变换器|电力电子变换器]]
- [[平均值模型|平均值模型]]
- [[118节点测试系统|118节点测试系统]]


## 相关主题


- [[协同仿真|协同仿真]]
- [[多速率仿真|多速率仿真]]
- [[频率自适应仿真|频率自适应仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[暂态稳定|暂态稳定]]
- [[网络分区|网络分区]]


## 主要发现


- 在含MMC-HVDC的118节点系统中验证了框架的精度与计算效率优势
- 动态相量缓冲区有效隔离了EMT与暂态稳定求解器，提升了数值稳定性
- BFAST求解器能根据暂态频率自动切换步长，显著降低稳态计算耗时



---
title: "Parallelization of MMC detailed equivalent model"
type: source
authors: ['A. Stepanov']
year: 2021
journal: "Electric Power Systems Research, 195 (2021) 107168. doi:10.1016/j.epsr.2021.107168"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/30/j.epsr.2021.107168.pdf.pdf"]
---

# Parallelization of MMC detailed equivalent model

**作者**: A. Stepanov
**年份**: 2021
**来源**: `30/j.epsr.2021.107168.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A. Stepanov a,*, J. Mahseredjian a, H. Saad b, U. Karaagac c a Department of Electrical Engineering, Polytechnique Montr´eal, Montreal, QC, Canada b R´eseau de Transport d’Electricit´e, Paris, France c Department of Electrical Engineering, Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

## 核心贡献


- 提出MMC详细等效模型多核并行方法，将各桥臂封装为独立DLL与主求解器交互。
- 设计电容均压算法并行方案，与电路计算协同提升整体仿真效率。
- 构建通用并行架构，支持任意核数与模块数量，实现离线电磁暂态仿真加速。


## 使用的方法


- [[并行计算|并行计算]]
- [[openmp多线程技术|OpenMP多线程技术]]
- [[动态链接库接口|动态链接库接口]]
- [[诺顿等效电路法|诺顿等效电路法]]
- [[电容均压算法|电容均压算法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[详细等效模型|详细等效模型]]
- [[子模块|子模块]]
- [[mmc-model|MMC]]
- [[igbt|IGBT]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[离线仿真|离线仿真]]
- [[多核cpu加速|多核CPU加速]]
- [[mmc-model|MMC]]
- [[电容均压|电容均压]]


## 主要发现


- 所提并行方法可使仿真速度最高提升五倍，且完全保持原有计算精度。
- 电容均压算法并行化对提速贡献显著，其加速效果有时超过电路方程并行。
- 理论加速比受限于主网络方程求解时间，实际加速受线程创建与管理开销影响。



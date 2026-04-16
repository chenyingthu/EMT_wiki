---
title: "Analysis and general calculation of DC fault currents in MMC-MTDC grids"
type: source
authors: ['Zhuoya Wang']
year: 2023
journal: "Electric Power Systems Research, 224 (2023) 109709. doi:10.1016/j.epsr.2023.109709"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Wang et al. - 2023 - Analysis and general calculation of DC fault currents in MMC-MTDC grids.pdf"]
---

# Analysis and general calculation of DC fault currents in MMC-MTDC grids

**作者**: Zhuoya Wang
**年份**: 2023
**来源**: `07&08/Wang et al. - 2023 - Analysis and general calculation of DC fault currents in MMC-MTDC grids.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Analysis and general calculation of DC fault currents in MMC-MTDC grids Zhuoya Wang , Liangliang Hao *, Le Wang , Jinghan He College of Electrical Engineering, Beijing Jiaotong University, Beijing 100044, China The short-circuit fault of MMC-MTDC has great influence on the safe and stable operation of the MMC-HVDC

## 核心贡献


- 提出具有明确物理意义的短路电流解析表达式，揭示RLC参数影响规律
- 将换流站放电电流分为顺逆时针路径，提出多端复杂电网简化为双端模型的方法
- 构建适用于任意故障位置的MMC-MTDC电网直流短路电流通用解析计算方法


## 使用的方法


- [[解析计算法|解析计算法]]
- [[等效电路法|等效电路法]]
- [[rlc参数化建模|RLC参数化建模]]
- [[pscad-emtdc电磁暂态仿真|PSCAD/EMTDC电磁暂态仿真]]
- [[数模混合仿真|数模混合仿真]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块-hbsm|半桥子模块(HBSM)]]
- [[多端直流电网-mtdc|多端直流电网(MTDC)]]
- [[直流断路器|直流断路器]]
- [[桥臂电抗器|桥臂电抗器]]
- [[直流输电线路|直流输电线路]]


## 相关主题


- [[直流故障分析|直流故障分析]]
- [[短路电流计算|短路电流计算]]
- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数模混合仿真|数模混合仿真]]
- [[保护设计|保护设计]]


## 主要发现


- 理论解析法能准确刻画闭锁前故障电流变化趋势，计算结果与仿真波形高度一致
- 多端电网简化双端模型有效复现各换流站放电特性，大幅降低高维矩阵求解复杂度
- 数模混合实验验证了通用计算方法的工程有效性，可为直流保护定值整定提供依据



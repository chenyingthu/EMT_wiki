---
title: "Equivalent Modeling Method of Parallel Elements for Fast Electromagnetic Transient Simulation"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Sun和Xu - 2023 - Equivalent Modeling Method of Parallel Electromagnetic Transient Simulation for Power Electronic Tra.pdf"]
---

# Equivalent Modeling Method of Parallel Elements for Fast Electromagnetic Transient Simulation

**作者**: CNKI
**年份**: 2023
**来源**: `18/Sun和Xu - 2023 - Equivalent Modeling Method of Parallel Electromagnetic Transient Simulation for Power Electronic Tra.pdf`

## 摘要

文章编号：1000-3673（2023）07-2829-11    中图分类号：TM 721    文献标志码：A    学科代码：470·40 Equivalent Modeling Method of Parallel Electromagnetic Transient Simulation for (State Key Laboratory of Alternate Electrical Power System With Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China) 1ABSTRACT: Power electronic transformer (PET) has the

## 核心贡献


- 提出导纳单元预存与叠加定理结合的诺顿等效方法，避免每步长矩阵求逆运算
- 证明H桥对外仅含两种等效导纳，将复杂时变网络简化为二值导纳单元
- 构建基于模型高度并行性的多线程并行仿真框架，实现系统级高效解算


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[二值电阻等值|二值电阻等值]]
- [[诺顿等效|诺顿等效]]
- [[叠加定理|叠加定理]]
- [[端口解耦|端口解耦]]
- [[多线程并行计算|多线程并行计算]]


## 涉及的模型


- [[电力电子变压器-pet|电力电子变压器(PET)]]
- [[级联h桥型pet-chb-pet|级联H桥型PET(CHB-PET)]]
- [[功率模块-pm|功率模块(PM)]]
- [[h桥单元|H桥单元]]
- [[高频隔离变压器|高频隔离变压器]]
- [[igbt-二极管开关组|IGBT-二极管开关组]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[等效建模|等效建模]]
- [[仿真加速|仿真加速]]
- [[系统级仿真|系统级仿真]]


## 主要发现


- 多工况下等效模型与详细模型高度拟合，电压电流最大误差严格控制在3%以内
- 单相模块数为48时，并行等效模型相比详细模型实现超一万倍的仿真速度提升



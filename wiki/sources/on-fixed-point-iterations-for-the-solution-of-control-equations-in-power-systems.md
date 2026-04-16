---
title: "On fixed-point iterations for the solution of control equations in power systems transients"
type: source
authors: ['C.F. Mugombozi']
year: 2014
journal: "Electric Power Systems Research, Corrected proof. doi:10.1016/j.epsr.2014.03.035"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/29/j.epsr.2014.03.035.pdf.pdf"]
---

# On fixed-point iterations for the solution of control equations in power systems transients

**作者**: C.F. Mugombozi
**年份**: 2014
**来源**: `29/j.epsr.2014.03.035.pdf.pdf`

## 摘要

On ﬁxed-point iterations for the solution of control equations in power systems transients C.F. Mugombozi a,b,∗ , J. Mahseredjian a , O. Saad b a Ecole Polytechnique de Montréal, Canada b IREQ/Hydro-Quebec, Montréal, Canada

## 核心贡献


- 提出基于压缩映射与雅可比谱范数的不动点迭代收敛性形式化分析方法
- 结合图论技术识别控制回路反馈路径，建立电磁暂态仿真中不动点法的安全应用准则
- 在EMTP-RV中实现该算法，验证其在保证精度前提下相比牛顿法的计算效率优势


## 使用的方法


- [[不动点迭代法|不动点迭代法]]
- [[牛顿法|牛顿法]]
- [[压缩映射定理|压缩映射定理]]
- [[雅可比矩阵谱范数分析|雅可比矩阵谱范数分析]]
- [[coates图论分析|Coates图论分析]]
- [[梯形积分离散|梯形积分离散]]


## 涉及的模型


- [[锁相环-pll-控制系统|锁相环(PLL)控制系统]]
- [[异步电机模型|异步电机模型]]
- [[用户自定义控制模型|用户自定义控制模型]]


## 相关主题


- [[控制系统方程求解|控制系统方程求解]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[收敛性分析|收敛性分析]]
- [[代数环处理|代数环处理]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 小步长下不动点法收敛可靠且精度与牛顿法一致，可显著缩短仿真计算时间
- 输入突变或步长增大时，数值导数与离散化效应会导致不动点法收敛性能下降
- 合理设置相对/绝对容差可使不动点迭代在保证精度的同时维持对牛顿法的计算优势



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

*（摘要未提取到）*

## 核心贡献

- 建立了通过不动点迭代求解电力系统控制系统方程的正式分析方法
- 提出了基于函数收缩性质的不动点迭代收敛性判据
- 在EMTP-RV中验证了该算法，证明其在提升计算性能的同时未牺牲仿真精度

## 使用的方法

- [[不动点迭代法|不动点迭代法]]
- [[基于收缩性质的收敛性分析|基于收缩性质的收敛性分析]]
- [[科茨图-coates-graph-分析|科茨图（Coates graph）分析]]
- [[与牛顿法的对比评估|与牛顿法的对比评估]]

## 涉及的模型

- [[风力发电控制系统|风力发电控制系统]]
- [[用户自定义控制模型|用户自定义控制模型]]
- [[含代数环与非线性反馈环节的控制系统模型|含代数环与非线性反馈环节的控制系统模型]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态（EMT）仿真]]
- [[控制系统方程求解|控制系统方程求解]]
- [[代数环处理|代数环处理]]
- [[非线性方程迭代求解|非线性方程迭代求解]]
- [[电力系统暂态分析|电力系统暂态分析]]

## 主要发现

- 不动点迭代法的收敛性严格依赖于迭代函数的收缩性质，所提判据可在实际迭代前有效预测收敛行为
- 相较于传统牛顿法，该方法无需耗时的线性化与矩阵运算，计算效率更高，且能准确处理含非线性模块的代数环问题

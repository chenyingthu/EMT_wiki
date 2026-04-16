---
title: "Efficiently computing the electrical parameters of cables with arbitrary cross-sections using the method-of-moments"
type: source
authors: ['M. Shafieipour']
year: 2018
journal: "Electric Power Systems Research, 162 (2018) 37-49. doi:10.1016/j.epsr.2018.04.013"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficiently computing the electrical parameters of cables with arbitrary cross-sections using the me_Shafieipour 等_2018.pdf"]
---

# Efficiently computing the electrical parameters of cables with arbitrary cross-sections using the method-of-moments

**作者**: M. Shafieipour
**年份**: 2018
**来源**: `15/Efficiently computing the electrical parameters of cables with arbitrary cross-sections using the me_Shafieipour 等_2018.pdf`

## 摘要

(http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 核心贡献


- 提出基于二维矩量法的准静电场离散格式，高效提取任意截面电缆的并联导纳矩阵
- 引入矩量法优化策略，实现任意形状电缆全频域单位长度阻抗与导纳矩阵的快速计算
- 突破传统闭式近似限制，为电磁暂态程序提供高精度、低耗时的电缆参数提取工具


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[准静电场积分方程|准静电场积分方程]]
- [[二维离散技术|二维离散技术]]
- [[有限元法-fem|有限元法(FEM)]]
- [[闭式近似公式|闭式近似公式]]


## 涉及的模型


- [[地下电缆|地下电缆]]
- [[任意截面电缆|任意截面电缆]]
- [[管型电缆|管型电缆]]
- [[扇形电缆|扇形电缆]]
- [[同轴电缆|同轴电缆]]
- [[多导体传输线|多导体传输线]]


## 相关主题


- [[电缆参数提取|电缆参数提取]]
- [[频率相关建模|频率相关建模]]
- [[集肤与邻近效应|集肤与邻近效应]]
- [[电磁暂态仿真-emtp|电磁暂态仿真(EMTP)]]
- [[计算电磁学|计算电磁学]]


## 主要发现


- 矩量法提取的导纳矩阵与有限元结果高度吻合，显著优于传统圆形截面近似公式
- 优化算法大幅降低计算耗时，使任意截面电缆参数提取可在常规计算机上快速完成
- 时域电磁暂态仿真验证了所提参数的高精度，有效避免了传统模型带来的波形误差



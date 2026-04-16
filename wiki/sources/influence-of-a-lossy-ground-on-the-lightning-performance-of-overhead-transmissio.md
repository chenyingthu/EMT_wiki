---
title: "Influence of a lossy ground on the lightning performance of overhead transmission lines"
type: source
authors: ['Rafael Alipio']
year: 2022
journal: "Electric Power Systems Research, 214 (2023) 108951. doi:10.1016/j.epsr.2022.108951"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/24/Alipio 等 - 2023 - Influence of a lossy ground on the lightning performance of overhead transmission lines.pdf"]
---

# Influence of a lossy ground on the lightning performance of overhead transmission lines

**作者**: Rafael Alipio
**年份**: 2022
**来源**: `24/Alipio 等 - 2023 - Influence of a lossy ground on the lightning performance of overhead transmission lines.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Influence of a lossy ground on the lightning performance of overhead Rafael Alipio a,*, Alberto De Conti b, Naiara Duarte c, Farhad Rachidi c a Department of Electrical Engineering, Federal Center of Technological Education of Minas Gerais (CEFET-MG), Av. Amazonas, 7675 - Nova Gameleira, Belo Horizonte, b Department of Electrical Engineering, Federal University of Minas Gerais (UFMG), Belo Horizonte, Brazil

## 核心贡献


- 将位移电流与频变土壤参数引入Sunde大地返回阻抗计算，提升瞬态建模精度
- 在ATP时域仿真器中实现改进型Marti线路模型，支持频变大地参数计算
- 首次系统评估精确损耗大地模型对架空线路雷击反击跳闸率的影响


## 使用的方法


- [[sunde大地返回阻抗公式|Sunde大地返回阻抗公式]]
- [[marti输电线路模型|Marti输电线路模型]]
- [[alipio-visacro频变土壤模型|Alipio-Visacro频变土壤模型]]
- [[heidler雷电流函数|Heidler雷电流函数]]
- [[atp电磁暂态仿真|ATP电磁暂态仿真]]
- [[carson公式对比|Carson公式对比]]


## 涉及的模型


- [[138kv-230kv架空输电线路|138kV/230kV架空输电线路]]
- [[杆塔接地阻抗|杆塔接地阻抗]]
- [[绝缘子串|绝缘子串]]
- [[频变损耗大地模型|频变损耗大地模型]]
- [[雷电流源|雷电流源]]


## 相关主题


- [[雷击反击跳闸率|雷击反击跳闸率]]
- [[频变土壤参数建模|频变土壤参数建模]]
- [[大地返回阻抗|大地返回阻抗]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[过电压分析|过电压分析]]
- [[线路防雷性能|线路防雷性能]]


## 主要发现


- 考虑频变土壤的Sunde公式计算的雷击过电压峰值显著高于传统Carson公式
- 高阻土壤中效应显著，1000至10000Ωm土壤使反击跳闸率提升4%至15%
- 无论采用快波头或慢波头雷电流，精确大地模型均呈现一致的跳闸率上升趋势



---
title: "Inaccuracies due to the frequency warping in simulation of electrical systems using combined stateâ&#x80;&#x93;space nodal analysis"
type: source
authors: ['A.A. Kida']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109657. doi:10.1016/j.epsr.2023.109657"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Kida 等 - 2023 - Inaccuracies due to the frequency warping in simulation of electrical systems using combined state–s.pdf"]
---

# Inaccuracies due to the frequency warping in simulation of electrical systems using combined stateâ&#x80;&#x93;space nodal analysis

**作者**: A.A. Kida
**年份**: 2023
**来源**: `23/Kida 等 - 2023 - Inaccuracies due to the frequency warping in simulation of electrical systems using combined state–s.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Inaccuracies due to the frequency warping in simulation of electrical systems A.A. Kida a,b,∗, A.C.S. Lima c, F.A. Moreira b, J.R. Martí d, J. Tarazona d b Federal University of Bahia, Salvador, BA, Brazil c Federal University of Rio de Janeiro, COPPE/UFRJ, Rio de Janeiro, Brazil

## 核心贡献


- 揭示梯形积分法引发频率畸变的机理，阐明其对系统固有振荡频率的偏移影响
- 构建状态空间与节点联合分析框架，对比梯形法与递归卷积法的数值误差特性
- 量化双线性变换导致的元件频变特性与特征值扰动，揭示误差随时间累积规律


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[递归卷积法|递归卷积法]]
- [[状态空间与节点联合分析法|状态空间与节点联合分析法]]
- [[双线性变换|双线性变换]]
- [[伴随电路法|伴随电路法]]


## 涉及的模型


- [[四阶rlc集总电路|四阶RLC集总电路]]
- [[伴随电路模型|伴随电路模型]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率畸变|频率畸变]]
- [[数值积分误差|数值积分误差]]
- [[特征值扰动|特征值扰动]]
- [[误差累积分析|误差累积分析]]


## 主要发现


- 梯形积分法导致离散化电感电容频变，使系统固有振荡频率发生显著偏移
- 频率畸变引发绝对误差呈脉动特性，且全局截断误差随仿真时间持续累积
- 即使步长满足理论要求，频率畸变仍会导致长期仿真结果严重偏离解析解



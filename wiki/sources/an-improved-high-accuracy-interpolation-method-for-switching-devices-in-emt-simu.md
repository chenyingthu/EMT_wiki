---
title: "An improved high-accuracy interpolation method for switching devices in EMT simulation programs"
type: source
authors: ['J. Na']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109630. doi:10.1016/j.epsr.2023.109630"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Na et al. - 2023 - An improved high-accuracy interpolation method for switching devices in EMT simulation programs.pdf"]
---

# An improved high-accuracy interpolation method for switching devices in EMT simulation programs

**作者**: J. Na
**年份**: 2023
**来源**: `07&08/Na et al. - 2023 - An improved high-accuracy interpolation method for switching devices in EMT simulation programs.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. An improved high-accuracy interpolation method for switching devices in J. Na a,d, H. Kim b, H. Zhao c, A.M. Gole c, K. Hur a,∗ a School of Electrical and Electronic Engineering, Yonsei University, Seoul 03722, South Korea b R&D Center, Pion Electric, Gyeonggi-do 14348, Republic of Korea

## 核心贡献


- 提出结合半步长后向欧拉与插值外推的改进算法，精准还原开关动作时刻状态
- 消除强制换流开关的虚假损耗与数值振荡，计算步数与工业标准瞬时插值法一致
- 在固定步长EMT仿真中实现高精度开关暂态模拟，兼顾计算效率与数值稳定性


## 使用的方法


- [[后向欧拉法|后向欧拉法]]
- [[梯形积分法|梯形积分法]]
- [[线性插值|线性插值]]
- [[瞬时解插值|瞬时解插值]]
- [[节点分析|节点分析]]
- [[固定步长仿真|固定步长仿真]]


## 涉及的模型


- [[igbt|IGBT]]
- [[晶闸管|晶闸管]]
- [[二极管|二极管]]
- [[电感|电感]]
- [[电压源|电压源]]
- [[电力电子电路|电力电子电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[开关不连续性处理|开关不连续性处理]]
- [[数值振荡抑制|数值振荡抑制]]
- [[固定步长仿真|固定步长仿真]]
- [[电力电子开关建模|电力电子开关建模]]


## 主要发现


- 改进算法有效消除开关虚假损耗与数值振荡，电感电压电流波形精度显著提升
- 在简单与复杂电力电子电路测试中，开关时刻捕捉准确且未增加额外计算耗时
- 半步长后向欧拉结合外推策略成功避免储能元件相位延迟，验证了方法的高效性



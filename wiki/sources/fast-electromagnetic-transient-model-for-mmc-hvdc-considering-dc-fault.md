---
title: "Fast Electromagnetic Transient Model for MMC-HVDC Considering DC Fault"
type: source
authors: ['ilhan']
year: 2018
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRD.2018.2796089.pdf.pdf"]
---

# Fast Electromagnetic Transient Model for MMC-HVDC Considering DC Fault

**作者**: ilhan
**年份**: 2018
**来源**: `19、20、21/EMT_task_20/TPWRD.2018.2796089.pdf.pdf`

## 摘要

0885-8977 (c) 2018 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information. This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPWRD.2018.2796089, IEEE impedance and admittance for underground cables is proposed based on a

## 核心贡献


- 提出基于完整场解的地下电缆大地返回阻抗与导纳广义公式，突破准TEM假设限制
- 推导多相电缆精确电压积分方程，实现大地返回参数的高频与低频统一建模
- 揭示大地返回导纳在低频段对电缆波传播特性的显著影响，修正传统EMTP模型


## 使用的方法


- [[完整场解法|完整场解法]]
- [[电报方程|电报方程]]
- [[准tem近似|准TEM近似]]
- [[矩量法-mom-so|矩量法(MoM-So)]]
- [[特征值分析|特征值分析]]


## 涉及的模型


- [[地下电缆|地下电缆]]
- [[交叉互联电缆|交叉互联电缆]]
- [[多相电缆系统|多相电缆系统]]
- [[大地返回阻抗-导纳模型|大地返回阻抗/导纳模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[波传播特性|波传播特性]]
- [[浪涌分析|浪涌分析]]
- [[频率相关建模|频率相关建模]]
- [[现场试验验证|现场试验验证]]


## 主要发现


- 新公式在浪涌仿真中呈现更强阻尼特性，且能平滑收敛至稳态，优于传统EMTP模型
- 即使在数十kHz低频段，大地返回导纳对电缆波传播特性影响显著，不可忽略
- 所提公式与110kV交叉互联电缆现场测试数据高度吻合，验证了模型准确性



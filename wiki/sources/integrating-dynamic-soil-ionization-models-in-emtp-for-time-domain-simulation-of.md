---
title: "Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistance"
type: source
authors: ['Ruyguara', 'A.', 'Meyberg']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112327. doi:10.1016/j.epsr.2025.112327"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/24/Meyberg 等 - 2026 - Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistanc.pdf"]
---

# Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistance

**作者**: Ruyguara, A., Meyberg
**年份**: 2025
**来源**: `24/Meyberg 等 - 2026 - Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistanc.pdf`

## 摘要

Integrating dynamic soil ionization models in EMTP for time-domain b Polytechnique Montreal, Montreal, QC H3T 1J4, Canada c Instituto Superior Tecnico, Universidade de Lisboa, 1049-001 Lisbon, Portugal Soil ionization can have a significant impact on the surge characteristics of grounding electrodes and should be considered when assessing the lightning performance of concentrate arrangements of grounding electrodes in

## 核心贡献


- 将基于变电阻率法的动态土壤电离模型通过DLL集成至EMTP
- 提出高效时域仿真方法替代高计算成本的FDTD进行接地电阻计算
- 验证了DLL模型在多种接地极配置下的精度与FDTD结果高度一致


## 使用的方法


- [[动态链接库集成|动态链接库集成]]
- [[变电阻率法|变电阻率法]]
- [[时域仿真|时域仿真]]
- [[等位面法|等位面法]]
- [[有限差分时域法对比|有限差分时域法对比]]


## 涉及的模型


- [[接地极|接地极]]
- [[单根垂直接地棒|单根垂直接地棒]]
- [[平行接地棒阵列|平行接地棒阵列]]
- [[土壤电离动态模型|土壤电离动态模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[接地电阻计算|接地电阻计算]]
- [[土壤电离效应|土壤电离效应]]
- [[雷击冲击特性|雷击冲击特性]]
- [[时域建模|时域建模]]


## 主要发现


- DLL仿真结果与FDTD计算值及实测数据高度吻合，验证了模型精度
- 该方法能准确捕捉土壤电离与去电离过程中的接地电阻动态变化
- 相比FDTD大幅降低计算成本，适用于大规模电网电磁暂态仿真



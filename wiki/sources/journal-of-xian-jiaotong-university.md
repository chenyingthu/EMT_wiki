---
title: "JOURNAL OF XI′AN JIAOTONG UNIVERSITY"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/王晓彤，牛晓民，施围 - 1999 - 电磁暂态计算中新的变压器模型.pdf"]
---

# JOURNAL OF XI′AN JIAOTONG UNIVERSITY

**作者**: 
**年份**: 2026
**来源**: `40/王晓彤，牛晓民，施围 - 1999 - 电磁暂态计算中新的变压器模型.pdf`

## 摘要

：Based on the T-form equivalent circuita transformer model that accounts for turn ratiointer- phase coupleconnectionphase thiftetc．is presented．The main functions are compared separately with EMTP（Electro-Magnetic Transient Program）showing the validity of the model． Keywords：electro-magnetic transient；coupled turns ratio；connection；transformer model 在电磁暂态计算中变压器是较难模拟的器件 之一．其复杂性在于它不仅是一个多相的耦合性元 件而且是一个具有磁滞效应的饱和性电感元件．如 果计算快速暂态过程（雷电过电压或VFTO）计及变 压器的杂散电容时它还是一个与频率有关的元件． 人们在很早就开发了变压器的暂态计算模型［1］当 然都是在忽略某些因素的条件下如T 型等值电路 模型、理想变压器模型、“饱和变压器元件”、以及“准 非线性磁滞电抗”等．但是这些模型只能较准确地 描述变压器的某一特性很难满足各种暂态计算的 需要．所以人们至今仍在努力试图建立一个较为 完善的变压器模型［2］．

## 核心贡献


- 基于T型等值电路推导含变比的节点导纳矩阵，避免理想变压器模型附加节点问题
- 通过耦合绕组编号自动模拟联结组与相移，直接求解中性点电压无需额外星形电路
- 引入正序与零序参数构建三相导纳矩阵，有效计及三相三柱式变压器的相间磁耦合


## 使用的方法


- [[节点分析法|节点分析法]]
- [[t型等值电路|T型等值电路]]
- [[差分方程法|差分方程法]]
- [[导纳矩阵法|导纳矩阵法]]


## 涉及的模型


- [[变压器|变压器]]
- [[三相三柱式变压器|三相三柱式变压器]]
- [[输电线路|输电线路]]


## 相关主题


- [[电磁暂态计算|电磁暂态计算]]
- [[变压器建模|变压器建模]]
- [[相间耦合|相间耦合]]
- [[联结组与相移|联结组与相移]]
- [[零序网络|零序网络]]


## 主要发现


- 稳态计算准确反映变比关系与Y/Δ接法30度相移，低压侧电压幅值相位均正确
- 三相开关不同时刻合闸暂态波形与EMTP高度吻合，验证模型动态响应准确性
- 模型可直接输出中性点电压波形，无需额外星形计算电路，简化了仿真建模流程



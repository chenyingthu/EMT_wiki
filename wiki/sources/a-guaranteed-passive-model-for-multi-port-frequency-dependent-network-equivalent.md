---
title: "A guaranteed passive model for multi-port frequency dependent network equivalents using network synthesis approach"
type: source
authors: ['Meysam Ahmadi']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107248. doi:10.1016/j.epsr.2021.107248"
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/01/Ahmadi 等 - 2021 - A guaranteed passive model for multi-port frequency dependent network equivalents using network synt.pdf"]
---

# A guaranteed passive model for multi-port frequency dependent network equivalents using network synthesis approach

**作者**: Meysam Ahmadi
**年份**: 2021
**来源**: `01/Ahmadi 等 - 2021 - A guaranteed passive model for multi-port frequency dependent network equivalents using network synt.pdf`

## 摘要

0378-7796/Crown Copyright © 2021 Published by Elsevier B.V. All rights reserved. A guaranteed passive model for multi-port frequency dependent network Meysam Ahmadi a,*, Shengtao Fan a, Aniruddha M. Gole a, H. M. Jeewantha De Silva b a Power Systems Research Group, Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada b Manitoba Hydro International, Winnipeg, MB, Canada, R3P 1A3

## 核心贡献


- 提出基于网络综合法的多端口FDNE建模方法，直接由频响表格数据构建RLCM无源网络。
- 自动化Tellegen综合法适配表格阻抗数据，实现多端口等值且无需额外无源性校正。
- 从根本上保证多端口FDNE无源性，避免矢量拟合法强制无源导致的精度损失与不收敛。


## 使用的方法


- [[brune综合法|Brune综合法]]
- [[tellegen综合法|Tellegen综合法]]
- [[网络综合法|网络综合法]]
- [[正实矩阵实现|正实矩阵实现]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[rlcm网络|RLCM网络]]
- [[多端口阻抗矩阵|多端口阻抗矩阵]]
- [[外部网络等值|外部网络等值]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关网络等值|频率相关网络等值]]
- [[无源性保证|无源性保证]]
- [[多端口网络建模|多端口网络建模]]
- [[实时仿真|实时仿真]]


## 主要发现


- 案例验证表明该方法能精确复现外部网络频响特性，且全程自动保证模型无源性。
- 相比矢量拟合法，该方法无需后处理无源性校正，彻底避免了精度损失与迭代不收敛问题。
- 成功将单端口综合法推广至多端口系统，生成的RLCM网络可直接用于EMT仿真工具。



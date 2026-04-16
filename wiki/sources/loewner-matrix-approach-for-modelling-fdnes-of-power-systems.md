---
title: "Loewner matrix approach for modelling FDNEs of power systems"
type: source
authors: ['Gurunath Gurrala']
year: 2015
journal: "Electric Power Systems Research, 125 (2015) 116-123. doi:10.1016/j.epsr.2015.03.016"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Gurrala - 2015 - Loewner matrix approach for modelling FDNEs of power systems.pdf"]
---

# Loewner matrix approach for modelling FDNEs of power systems

**作者**: Gurunath Gurrala
**年份**: 2015
**来源**: `25/Gurrala - 2015 - Loewner matrix approach for modelling FDNEs of power systems.pdf`

## 摘要

to  vector  ﬁtting  in  terms  of  accuracy,  stability

## 核心贡献


- 提出基于Loewner矩阵与切向插值的FDNE建模新方法，实现非迭代状态空间模型拟合
- 设计简洁的矩阵构建流程与MATLAB稳定模型提取算法，有效分离不规则部分
- 揭示数据划分策略对拟合精度的关键影响，为多端口网络等值提供实用指导


## 使用的方法


- [[loewner矩阵方法|Loewner矩阵方法]]
- [[切向插值|切向插值]]
- [[奇异值分解-svd|奇异值分解(SVD)]]
- [[描述符状态空间实现|描述符状态空间实现]]
- [[非迭代有理逼近|非迭代有理逼近]]
- [[矢量拟合|矢量拟合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[多端口电力系统网络|多端口电力系统网络]]
- [[导纳矩阵-y矩阵-模型|导纳矩阵(Y矩阵)模型]]
- [[广义描述符系统|广义描述符系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[无源性验证|无源性验证]]
- [[模型阶数辨识|模型阶数辨识]]
- [[有理函数逼近|有理函数逼近]]


## 主要发现


- Loewner矩阵法在精度、稳定性与无源性方面与矢量拟合相当，且无需初始极点
- 该方法为非迭代算法，彻底避免收敛问题，并能自动指示系统最优阶数
- 提取不规则部分后的状态空间模型保持稳定，阶跃响应与Y矩阵实部特征值验证无源



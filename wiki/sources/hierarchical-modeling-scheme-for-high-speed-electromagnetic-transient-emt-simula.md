---
title: "Hierarchical Modeling Scheme for High-Speed Electromagnetic Transient (EMT) Simulations of Power Electronic Transformers"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Electronics; ;PP;99;10.1109/TPEL.2021.3061421"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/tpel.2021.3061421.pdf.pdf"]
---

# Hierarchical Modeling Scheme for High-Speed Electromagnetic Transient (EMT) Simulations of Power Electronic Transformers

**作者**: 
**年份**: 2021
**来源**: `19、20、21/EMT_task_21/tpel.2021.3061421.pdf.pdf`

## 摘要

0885-8993 (c) 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information. This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TPEL.2021.3061421, IEEE Moke Feng, Chenxiang Gao, Jiangping Ding, Hui Ding, Member, IEEE, Jianz

## 核心贡献


- 提出分层建模方案，递归消去内部节点获取相桥臂广义诺顿等效电路
- 无近似降阶导纳矩阵至四阶，直接叠加外部系统大幅降低计算量
- 设计状态反演算法，实现降阶后内部节点电压与支路电流的精确恢复


## 使用的方法


- [[分层建模|分层建模]]
- [[广义诺顿等效|广义诺顿等效]]
- [[递归节点消去|递归节点消去]]
- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[双端口等效建模|双端口等效建模]]


## 涉及的模型


- [[电力电子变压器|电力电子变压器]]
- [[级联h桥双有源桥|级联H桥双有源桥]]
- [[功率模块|功率模块]]
- [[高频隔离变压器|高频隔离变压器]]
- [[中压直流系统|中压直流系统]]


## 相关主题


- [[高速电磁暂态仿真|高速电磁暂态仿真]]
- [[网络等值|网络等值]]
- [[模型降阶|模型降阶]]
- [[电力电子化配电系统|电力电子化配电系统]]
- [[大规模节点消去|大规模节点消去]]


## 主要发现


- PSCAD验证表明，相比详细模型仿真速度提升一至两个数量级
- 多工况下仿真波形与详细模型高度一致，精度损失可忽略不计
- 等效矩阵降阶有效解决超大规模节点导纳矩阵求逆导致的耗时瓶颈



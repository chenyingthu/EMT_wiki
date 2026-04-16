---
title: "A component-level modeling and fine-grained simulation method for renewable energy power systems suitable for EMT-type studies"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Xu 等 - 2024 - A General Equivalent Modeling Method of N-port Networks Suitable for the Electromagnetic Transient S.pdf"]
---

# A component-level modeling and fine-grained simulation method for renewable energy power systems suitable for EMT-type studies

**作者**: 
**年份**: 2026
**来源**: `01/Xu 等 - 2024 - A General Equivalent Modeling Method of N-port Networks Suitable for the Electromagnetic Transient S.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献


- 提出适用于任意N端口子模块及级联方式的通用等效建模方法
- 基于离散状态空间表达式提取端口特性并反向构造等效电路
- 推导系数矩阵通用计算公式实现复杂网络的计算机自动建模


## 使用的方法


- [[节点分析法|节点分析法]]
- [[状态空间法|状态空间法]]
- [[数值积分离散化|数值积分离散化]]
- [[等效电路建模|等效电路建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[双有源桥-dab|双有源桥(DAB)]]
- [[固态变压器-sst|固态变压器(SST)]]
- [[n端口网络|N端口网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[等效建模|等效建模]]
- [[级联型电力电子拓扑|级联型电力电子拓扑]]
- [[实时仿真|实时仿真]]
- [[网络等值|网络等值]]


## 主要发现


- 消除子模块内部节点可显著提升级联电力电子拓扑的仿真计算效率
- 通用模型支持自定义拓扑与级联方式，且兼容传统MMC桥臂等效模型
- 状态空间系数矩阵自动推导算法验证了复杂N端口网络建模的可行性



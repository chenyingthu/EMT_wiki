---
title: "High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery;2018;33;3;10.1109/TPWRD.2017.2740857"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/22/Xu 等 - 2018 - High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Nort.pdf"]
---

# High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents

**作者**: 
**年份**: 2018
**来源**: `22/Xu 等 - 2018 - High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Nort.pdf`

## 摘要

—In order to improve features, such as fault current blocking and capacitor voltage balancing, modular multilevel converter (MMC) topologies incorporating multiport submodules (SMs) are being considered as candidates for HVdc transmission applications. This paper presents high-speed and accurate electromagnetic transient (EMT) models for MMCs composed of such multiport SMs. The approach uses the Schur’s complement technique to recursively eliminate internal nodes of the converter structure to create a multiport Norton equivalent that connects to the external network. Thus, the ﬁnal admittance matrix seen by the EMT solver has a dimension orders of magnitude smaller than that of the unreduced structure. As with previously developed approaches for MMCs with single-port SMs, all internal info

## 核心贡献


- 提出基于舒尔补的递归消去法，构建任意多端口子模块的广义诺顿等效电路
- 实现桥臂内部节点高效降维，使外部求解器导纳矩阵规模缩小数个数量级
- 在压缩矩阵维度的同时完整保留子模块电容电压等内部状态信息


## 使用的方法


- [[舒尔补技术|舒尔补技术]]
- [[递归节点消去|递归节点消去]]
- [[广义多端口诺顿等效|广义多端口诺顿等效]]
- [[伴随电路建模|伴随电路建模]]
- [[嵌套网络分割|嵌套网络分割]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[多端口子模块|多端口子模块]]
- [[双端口子模块|双端口子模块]]
- [[高压直流输电系统|高压直流输电系统]]
- [[开关器件与直流电容|开关器件与直流电容]]


## 相关主题


- [[高速电磁暂态建模|高速电磁暂态建模]]
- [[矩阵降维与网络等值|矩阵降维与网络等值]]
- [[高压直流输电|高压直流输电]]
- [[子模块电压均衡|子模块电压均衡]]
- [[实时仿真加速|实时仿真加速]]


## 主要发现


- 等效模型使求解器导纳矩阵维度大幅降低，显著提升电磁暂态计算效率
- 仿真速度较传统详细模型提升两至三个数量级，且未牺牲模型精度
- 完整保留各子模块电容电压等内部状态，满足详细控制与故障分析需求



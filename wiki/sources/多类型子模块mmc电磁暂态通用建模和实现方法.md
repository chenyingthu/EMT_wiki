---
title: "多类型子模块MMC电磁暂态通用建模和实现方法"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/许建中 等 - 2019 - 多类型子模块MMC电磁暂态通用建模和实现方法.pdf"]
---

# 多类型子模块MMC电磁暂态通用建模和实现方法

**作者**: CNKI
**年份**: 2023
**来源**: `40/许建中 等 - 2019 - 多类型子模块MMC电磁暂态通用建模和实现方法.pdf`

## 摘要

The key issue of electromagnetic transient (EMT) modelling of modular multilevel converters (MMC) is calculation of equivalent circuit of entire MMC arm containing a large number of cascaded sub-modules (SM) with identical structure. During this process, all internal information should be preserved. This paper proposes a general EMT modelling approach for arbitrary multi-port MMC topologies, also suitable for traditional single-port MMC and emerging two-port MMC. A submodule topology identification method is proposed to minimize the efforts of the model users when they have specific MMC topologies at hand. In addition, the model codes can be inherited to a large extent. Finally, the approaches are validated in PSCAD/EMTDC with results of very good applicability of the

## 核心贡献



- 提出了一种适用于任意多端口（单端口/双端口）MMC拓扑的电磁暂态通用等效建模方法
- 提出了一种子模块拓扑自动识别方法，大幅降低特定拓扑建模工作量并实现模型代码的高度继承

## 使用的方法


- [[nodal-analysis]]
- [[numerical-integration]]
- [[network-equivalent]]

## 涉及的模型


- [[mmc-model]]
- [[mmc]]

## 相关主题


- [[hvdc]]
- [[vsc-hvdc]]
- [[mmc]]

## 主要发现



- 所提出的通用等效建模算法能够在消除大量内部节点的同时精确反解保留内部信息，且适用于传统单端口及新型双端口MMC
- 在PSCAD/EMTDC中的仿真验证表明该算法具有极强的通用性、高计算效率及良好的工程适用性
---
title: "Proximity effect in fast transient simulations of an underground transmission cable"
type: source
authors: ['U.S. Gudmundsdottir']
year: 2014
journal: "Electric Power Systems Research, Corrected proof. doi:10.1016/j.epsr.2014.03.016"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/j.epsr.2014.03.016.pdf.pdf"]
---

# Proximity effect in fast transient simulations of an underground transmission cable

**作者**: U.S. Gudmundsdottir
**年份**: 2014
**来源**: `32/j.epsr.2014.03.016.pdf.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了一种在EMT仿真中纳入邻近效应计算的有效方法
- 构建了包含半导体层、绝缘层及双导体材料屏蔽层的完整相阻抗矩阵
- 通过现场实测数据验证了改进模型，显著提升了高频暂态仿真的准确性

## 使用的方法

- [[导体细分法-subdivision-of-conductors-method|导体细分法（Subdivision of conductors method）]]
- [[通用线路模型-universal-line-model-ulm|通用线路模型（Universal Line Model, ULM）]]
- [[全相阻抗矩阵构建技术|全相阻抗矩阵构建技术]]
- [[现场测量对比验证|现场测量对比验证]]

## 涉及的模型

- [[高压交联聚乙烯-xlpe-地下电缆|高压交联聚乙烯（XLPE）地下电缆]]
- [[电缆常数模型-cable-constants-cc|电缆常数模型（Cable Constants, CC）]]
- [[通用线路模型-universal-line-model|通用线路模型（Universal Line Model）]]
- [[电缆芯线与金属屏蔽层-护套结构模型|电缆芯线与金属屏蔽层/护套结构模型]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态（EMT）仿真]]
- [[邻近效应-proximity-effect|邻近效应（Proximity effect）]]
- [[地下输电电缆建模|地下输电电缆建模]]
- [[高频-快速暂态分析|高频/快速暂态分析]]
- [[电缆串联阻抗计算|电缆串联阻抗计算]]

## 主要发现

- 传统电缆常数（CC）方法因忽略邻近效应，在高频仿真中会产生显著误差
- 引入邻近效应计算后，仿真结果与现场测量数据高度吻合，即使在护套间模式（intersheath mode）下也能实现精确匹配

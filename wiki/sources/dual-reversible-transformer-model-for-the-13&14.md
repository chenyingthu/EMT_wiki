---
title: "Dual Reversible Transformer Model for the"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2013.2268857.pdf.pdf"]
---

# Dual Reversible Transformer Model for the

**作者**: 
**年份**: 2013
**来源**: `13&14/files/TPWRD.2013.2268857.pdf.pdf`

## 摘要

—This paper presents a physically consistent dual model applicable to single-phase two-winding transformers for the calculation of low-frequency transients. First, the topology of a dual electrical equivalent circuit is obtained from the direct application of the principle of duality. Then, the model parame- ters are computed considering the variations of the transformer electromagnetic behavior under various operating conditions. Current modeling techniques use different topological models to represent diverse transient situations. The reversible model proposed in this paper uniﬁes the terminal and topological equiv- alent circuits. The model remains invariable for all low-frequency transients including deep saturation conditions driven from any of the two windings. The proposed model is 

## 核心贡献


- 基于对偶原理构建统一拓扑与端口的单相变压器可逆等效电路模型
- 引入非线性空气电感，实现单一参数集自适应表征双侧绕组深度饱和特性
- 模型完全兼容EMTP程序，无需几何参数即可通过端子测试获取全部参数


## 使用的方法


- [[对偶原理|对偶原理]]
- [[三维有限元仿真|三维有限元仿真]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]
- [[非线性电感建模|非线性电感建模]]


## 涉及的模型


- [[单相双绕组变压器|单相双绕组变压器]]
- [[对偶可逆等效电路|对偶可逆等效电路]]
- [[非线性磁滞电感|非线性磁滞电感]]
- [[空气漏磁非线性电感|空气漏磁非线性电感]]


## 相关主题


- [[低频暂态计算|低频暂态计算]]
- [[变压器建模|变压器建模]]
- [[励磁涌流|励磁涌流]]
- [[铁磁谐振|铁磁谐振]]
- [[地磁感应电流|地磁感应电流]]
- [[深度饱和特性|深度饱和特性]]


## 主要发现


- 实验证实内外侧绕组励磁涌流首峰差异达31.5%，源于深度饱和下空气芯电感不同
- 仿真与实测对比表明，该模型在涌流、铁磁谐振及GIC工况下均保持高精度
- 三维有限元验证了铁芯饱和时磁通向空气渗透现象，非线性电感建模有效捕捉该特性



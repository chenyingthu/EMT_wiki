---
title: "A Novel Linking-Domain Extraction Decomposition Method for Parallel Electromagnetic Transient Simulation of Large-Scale AC/DC Networks"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2998397"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/03/tpwrd.2020.2998397.pdf.pdf"]
---

# A Novel Linking-Domain Extraction Decomposition Method for Parallel Electromagnetic Transient Simulation of Large-Scale AC/DC Networks

**作者**: 
**年份**: 2020
**来源**: `03/tpwrd.2020.2998397.pdf.pdf`

## 摘要

—Domain decomposition of the network conductance matrix is one of the efﬁcient approaches to solve large-scale networks in parallel, wherein the most commonly-used non- iterative method is the Schur complement (SC) method. However, the SC method could not obtain the network conductance matrix inversion directly, and the computational cost will increase fast when the overlapping domain expands. In this work, a novel Linking-Domain Extraction (LDE) based decomposition method is proposed, in which the network matrix is expressed as the sum of a linking-domain matrix (LDM) and a diagonal block matrix (DBM) composed of multiple block matrices in diagonal. Through mathematical analysis over LDM, one lemma about the nature of LDM and its proof are proposed. Based on this lemma, the general formul

## 核心贡献

- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[区域分解法|区域分解法]]
- [[舒尔补法|舒尔补法]]
- [[链接域提取分解法-lde|链接域提取分解法(LDE)]]
- [[伍德伯里矩阵恒等式|伍德伯里矩阵恒等式]]
- [[并行计算|并行计算]]
- [[fpga-gpu硬件加速|FPGA/GPU硬件加速]]

## 涉及的模型

- [[大规模交直流网络|大规模交直流网络]]
- [[mmc-model|MMC]]
- [[子模块|子模块]]

## 相关主题

- [[parallel-computing]]

## 主要发现

—Domain decomposition of the network conductance matrix is one of the efﬁcient approaches to solve large-scale networks in parallel, wherein the most commonly-used non- iterative method is the Schur c

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


- 提出基于连接域提取的导纳矩阵分解方法，实现大规模网络并行求解
- 证明连接域矩阵可通过0/1/-1变换矩阵由对角阵转换并推导数学引理
- 结合Woodbury恒等式直接并行计算网络矩阵逆矩阵，避免每步迭代


## 使用的方法


- [[连接域提取分解法|连接域提取分解法]]
- [[舒尔补法|舒尔补法]]
- [[woodbury矩阵恒等式|Woodbury矩阵恒等式]]
- [[并行计算|并行计算]]
- [[fpga-gpu硬件加速|FPGA/GPU硬件加速]]


## 涉及的模型


- [[大规模交直流电网|大规模交直流电网]]
- [[mmc-model|MMC]]
- [[输电线路|输电线路]]
- [[线性网络导纳矩阵|线性网络导纳矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[网络分解|网络分解]]
- [[矩阵求逆加速|矩阵求逆加速]]
- [[fpga-gpu硬件实现|FPGA/GPU硬件实现]]


## 主要发现


- 在FPGA与GPU架构上验证算法，相比舒尔补法显著提升求解速度与精度
- 直接并行计算矩阵逆矩阵，有效克服重叠域扩大导致的计算成本激增问题
- 导纳矩阵恒定支持预先求逆，大幅降低单步仿真延迟，验证了算法高效性



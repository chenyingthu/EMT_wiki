---
title: "Unified High-Speed EMT Equivalent and Implementation Method of MMCs with Single-Port Submodules"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2018.2875073"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/39/tpwrd.2018.2875073.pdf.pdf"]
---

# Unified High-Speed EMT Equivalent and Implementation Method of MMCs with Single-Port Submodules

**作者**: 
**年份**: 2018
**来源**: `39/tpwrd.2018.2875073.pdf.pdf`

## 摘要

—This paper proposes a unified high-speed electromagnetic transient (EMT) equivalent and implementation method for modular multilevel converter (MMC) with arbitrary single-port submodule (SM) structures. The proposed method, interacts with the users by the incidence matrix, branch admittance matrix and the column vector of the current sources as input, then a nodal admittance matrix is automatically generated for each individual SM and the internal node information of the SMs are transferred to the interfacing nodes. Hence the internal nodes are eliminated without obtaining the complicated analytical solutions, the reduced-order equivalent

## 核心贡献



- 提出适用于任意单端口子模块结构的MMC统一高速EMT等效与实现方法
- 基于节点导纳矩阵自动生成与内部节点消去技术，实现子模块降阶等效与桥臂戴维南等效
- 通过时间步末更新机制恢复被消去的内部节点信息，确保稳态与暂态仿真无细节丢失

## 使用的方法


- [[nodal-analysis]]
- [[network-equivalent]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-hvdc]]

## 相关主题


- [[mmc]]
- [[hvdc]]
- [[real-time]]

## 主要发现



- 所提方法无需推导复杂解析解即可自动处理任意子模块拓扑，显著提升EMT仿真计算效率
- 降阶等效模型在大幅减少系统节点数量的同时，完整保留了子模块内部电容电压与电流的暂态动态特性
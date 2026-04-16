---
title: "An FPGA based electromagnetic transient analysis of power distribution network"
type: source
authors: ['Swati Shukla']
year: 2021
journal: "Electric Power Systems Research, 202 (2022) 107577. doi:10.1016/j.epsr.2021.107577"
tags: ['fpga']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An FPGA based electromagnetic transient analysis of power distribution network.pdf"]
---

# An FPGA based electromagnetic transient analysis of power distribution network

**作者**: Swati Shukla
**年份**: 2021
**来源**: `07&08/An FPGA based electromagnetic transient analysis of power distribution network.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. An FPGA based electromagnetic transient analysis of power Swati Shukla a,*, Abhishek Agrawal b, Balbir Singh b, Gaurav Trivedi b a School of Energy Sciences and Engineering, Indian Institute of Technology Guwahati, India b Department of Electronics and Electrical Engineering, Indian Institute of Technology Guwahati, India

## 核心贡献


- 提出基于SoC-FPGA的配电网电磁暂态仿真框架实现软硬件协同加速
- 设计预处理共轭梯度求解器采用稀疏矩阵存储与流水线浮点运算优化
- 针对病态对称正定导纳矩阵开发并行迭代架构显著提升求解效率


## 使用的方法


- [[共轭梯度法|共轭梯度法]]
- [[预处理共轭梯度法|预处理共轭梯度法]]
- [[节点分析法|节点分析法]]
- [[稀疏矩阵压缩存储|稀疏矩阵压缩存储]]
- [[流水线浮点运算|流水线浮点运算]]
- [[emtp型数值积分|EMTP型数值积分]]


## 涉及的模型


- [[配电网|配电网]]
- [[配电变压器|配电变压器]]
- [[配电馈线|配电馈线]]
- [[rlc无源网络|RLC无源网络]]
- [[变电站等值模型|变电站等值模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件加速|硬件加速]]
- [[并行计算|并行计算]]
- [[网络矩阵求解|网络矩阵求解]]
- [[配电网动态仿真|配电网动态仿真]]


## 主要发现


- FPGA仿真器精度与MATLAB一致计算速度提升约十二点五倍
- 预处理共轭梯度法有效克服导纳矩阵病态问题保证大规模网络迭代收敛
- 稀疏存储与流水线浮点设计显著降低硬件资源占用实现高效并行求解



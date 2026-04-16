---
title: "Parallel computation of power system EMTs through Polyphase-QMF filter banks"
type: source
authors: ['J.R. Zuluaga']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107317. doi:10.1016/j.epsr.2021.107317"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/j.epsr.2021.107317.pdf.pdf"]
---

# Parallel computation of power system EMTs through Polyphase-QMF filter banks

**作者**: J.R. Zuluaga
**年份**: 2021
**来源**: `30/j.epsr.2021.107317.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Parallel computation of power system EMTs through Polyphase-QMF J.R. Zuluaga a,*, J.L. Naredo a, L.J. Casta˜n´on a, M. Vega b, O. Ramos-Lea˜nos c The analysis of electromagnetic transients in power systems often requires intensive computations. Various methods have been proposed to reduce execution times and computational costs. A new technique is proposed

## 核心贡献


- 提出拉普拉斯域长卷积仿真方法，避免有理逼近导致的无源性破坏问题
- 利用Kron降阶法缩减节点矩阵，仅保留开关与观测节点以降低计算维度
- 设计基于多相QMF滤波器组的并行卷积算法，实现超实时仿真并验证FPGA可行性


## 使用的方法


- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[kron网络降阶|Kron网络降阶]]
- [[长卷积计算|长卷积计算]]
- [[多相qmf滤波器组|多相QMF滤波器组]]
- [[并行处理算法|并行处理算法]]
- [[分段线性化建模|分段线性化建模]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[17节点测试电网|17节点测试电网]]
- [[理想开关模型|理想开关模型]]
- [[辅助电压电流源|辅助电压电流源]]
- [[分段线性非线性元件|分段线性非线性元件]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[超实时仿真|超实时仿真]]
- [[网络等值降阶|网络等值降阶]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[统计性暂态分析|统计性暂态分析]]


## 主要发现


- 17节点电网仿真结果与PSCAD及传统拉氏变换高度吻合，验证了算法精度
- 多相QMF并行卷积架构显著提升计算效率，实现百倍于实时的超快速暂态仿真
- FPGA实现验证了并行架构的硬件适用性，但该方法暂不适用于长时或详细电力电子仿真



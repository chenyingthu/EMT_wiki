---
title: "State equation approximation of transfer matrices and its application to the phase domain calculatio - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/36/59.317582.pdf.pdf"]
---

# State equation approximation of transfer matrices and its application to the phase domain calculatio - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `36/59.317582.pdf.pdf`

## 摘要

A general methodology is presented for the state equa- tion appmximation of a multiple input-output linear system from transfer matrix data A complex transformation matrix, obtained by eigenandysis at a fixed frequency. is used for diagonalization of the trapsfer matrix over the whole frequency range. A scalar estimation r e d u r e  is applied for identification of the modal transfer functions. e state equations in the original coordinates are obtained by inverse transformation. An iterative Gauss-Newton refinement process is used to reduce the overall QIor of the approximation. The developed methodology is applied to the phase domain modeling of untransped transmission lines. The approach makes it possible to paform EMTP calculations directly in the phase domain. This results in conceptu

## 核心贡献



- 提出了一种基于传递矩阵数据的多输入多输出线性系统状态方程近似通用方法
- 将该方法应用于非换位输电线路的相域建模，实现了直接在相域进行EMTP计算，避免了传统模态变换，显著提升了计算效率

## 使用的方法


- [[state-space]]
- [[frequency-dependent]]
- [[vector-fitting]]

## 涉及的模型


- [[transmission-line]]
- [[transformer]]

## 相关主题


- [[state-space]]
- [[frequency-dependent]]
- [[transmission-line]]
- [[network-equivalent]]

## 主要发现



- 通过在单一固定频率下进行特征分析获得的复变换矩阵，可有效实现对全频段传递矩阵的对角化
- 迭代Gauss-Newton优化过程能显著降低整体近似误差，且所得状态方程为最小实现，模型阶数较低
- 直接在相域进行电磁暂态计算可省去模态变换步骤，在保证精度的同时大幅节省计算时间
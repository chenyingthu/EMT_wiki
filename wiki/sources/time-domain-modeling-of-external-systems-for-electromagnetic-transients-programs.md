---
title: "Time domain modeling of external systems for electromagnetic transients programs - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/59.260813.pdf.pdf"]
---

# Time domain modeling of external systems for electromagnetic transients programs - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `37/59.260813.pdf.pdf`

## 摘要

An external network model to be used in Electromagnetic Tran- sients Programs (EMTPs) is developed based on techniques directly applicable in the time domain. This is in contrast to the currently available models which are derived based on the frequency domain methods. The model is in form of a discrete-time filter which is built from the EMTP simulation of the external system’s response to a multisine excitation sig- nal. The developed filter is converted into a Norton equivalent source and integrated into the EMTP model of the study (in- ternal) system. The proposed model is verified by simulating the energization transients on an open-ended transmission line connected to the (external) network in a three phase test sys- tem. Keywords: Network Equivalents, Electromagnetic Tran- sients, S

## 核心贡献



- 提出了一种直接在时域构建外部系统等效模型的方法，避免了传统频域拟合的复杂性
- 基于多正弦激励响应构建离散时间滤波器，并将其转换为诺顿等效源直接集成到EMTP中
- 提供了一种易于实现且可直接应用于现有电磁暂态仿真程序的外部网络等效技术

## 使用的方法


- [[network-equivalent]]

## 涉及的模型


- [[transmission-line]]
- [[network-equivalent]]

## 相关主题


- [[network-equivalent]]

## 主要发现



- 时域离散滤波器能够准确复现外部系统在宽频暂态过程中的动态响应
- 无需显式综合RLC元件网络，直接生成的诺顿等效源可无缝集成至现有EMTP程序
- 在空载输电线路合闸暂态测试中，该等效模型与完整系统仿真结果高度一致，验证了其有效性与计算效率
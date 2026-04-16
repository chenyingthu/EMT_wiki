---
title: "Improved control systems simulation in the EMTP through compensation"
type: source
authors: ['S. Lefebvre', 'J. Mahseredjian']
year: 2004
journal: "IEEE Transactions on Power Delivery;1994;9;3;10.1109/61.311197"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/23/Lefebvre和Mahseredjian - 1994 - Improved control systems simulation in the EMTP through compensation.pdf"]
---

# Improved control systems simulation in the EMTP through compensation

**作者**: S. Lefebvre, J. Mahseredjian
**年份**: 2004
**来源**: `23/Lefebvre和Mahseredjian - 1994 - Improved control systems simulation in the EMTP through compensation.pdf`

## 摘要

The control systems, devices and phenomena modelled in TACS, and the electric network modeled in EMTP are solved separately with one-time-step error at the interface. This provides an efficient time-step solution, but there can be numerical stability and accuracy problems associated with the one-time-step error. This paper shows a technique which can eliminate the time delay, without having to use a simultaneous EMTP and TACS solution. Keywords : EMTI? compensation, power electronics TACS 1. INTRODUCTION

## 核心贡献


- 提出接口补偿技术，消除EMTP与TACS间的一步时间延迟，提升数值稳定性。
- 将真非线性补偿法扩展至控制接口，避免全联立求解，维持分步计算效率。


## 使用的方法


- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[补偿法|补偿法]]
- [[预测校正法|预测校正法]]
- [[矩阵三角分解|矩阵三角分解]]


## 涉及的模型


- [[tacs控制模型|TACS控制模型]]
- [[电力电子换流阀|电力电子换流阀]]
- [[同步机励磁系统|同步机励磁系统]]
- [[facts装置|FACTS装置]]
- [[断路器电弧|断路器电弧]]


## 相关主题


- [[控制系统仿真|控制系统仿真]]
- [[接口延迟补偿|接口延迟补偿]]
- [[数值稳定性|数值稳定性]]
- [[电力电子仿真|电力电子仿真]]
- [[分步解耦仿真|分步解耦仿真]]


## 主要发现


- 补偿技术有效消除接口一步延迟，解决断路器电弧仿真中的数值不稳定问题。
- 该方法无需联立求解电网与控制模型，在保持计算效率的同时显著提升精度。



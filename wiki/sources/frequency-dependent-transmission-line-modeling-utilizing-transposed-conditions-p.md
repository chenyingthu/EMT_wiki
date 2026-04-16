---
title: "Frequency-dependent transmission line modeling utilizing transposed conditions - Power Delivery, IEEE Transactions on"
type: source
authors: ['未知']
year: 2001
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/tpwrd.2002.1022812.pdf.pdf"]
---

# Frequency-dependent transmission line modeling utilizing transposed conditions - Power Delivery, IEEE Transactions on

**作者**: 
**年份**: 2001
**来源**: `19、20、21/EMT_task_20/tpwrd.2002.1022812.pdf.pdf`

## 摘要

—Existing phase domain transmission line models are capable of producing highly accurate results for both overhead lines and underground cables. This paper introduces a hybrid line model which gives substantial savings in computation time without loss of accuracy, when one or more circuits of a transmission system are treated as continuously transposed. This is achieved by means of a constant transformation matrix in combination with a reduced-size phase domain line model and a number of single-phase (modal) line models. The calculated examples demon- strate a potential speed increase over a full phase domain model between three and four. If none of the circuits are transposed, the line model degenerates into a full phase domain line model. Index Terms—Electromagnetic transients, multicirc

## 核心贡献


- 提出结合恒定变换矩阵、降阶相域模块与单相模态模型的混合线路建模方法
- 利用连续换位特性实现阻抗矩阵块对角化，大幅降低多回线路仿真计算复杂度
- 在保持非换位部分相域精度的同时，通过模态分解实现换位线路的高效仿真


## 使用的方法


- [[恒定变换矩阵法|恒定变换矩阵法]]
- [[模态分解|模态分解]]
- [[相域建模|相域建模]]
- [[梯形积分法|梯形积分法]]
- [[混合建模|混合建模]]


## 涉及的模型


- [[多回架空线路|多回架空线路]]
- [[地下电缆|地下电缆]]
- [[频率相关输电线路模型|频率相关输电线路模型]]
- [[连续换位线路模型|连续换位线路模型]]
- [[单相模态线路模型|单相模态线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[线路换位处理|线路换位处理]]
- [[计算加速|计算加速]]


## 主要发现


- 混合模型相比全相域模型计算速度提升3至4倍，且未牺牲仿真精度
- 当线路无换位时模型自动退化为全相域模型，保证了算法的通用性
- 通过降阶相域模块精确计及换位与非换位线路间的零序耦合效应



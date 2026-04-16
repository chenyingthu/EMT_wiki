---
title: "Noda | A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Noda - 2007 - A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi.pdf"]
---

# Noda | A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi

**作者**: 
**年份**: 2007
**来源**: `01/Noda - 2007 - A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equi.pdf`

## 摘要

—Previously, a method for identifying a multiphase net- work equivalent for electromagnetic transient calculations using partitioned frequency response has been proposed. The method ac- curately and robustly identiﬁes an equivalent of the target network by dividing its frequency response into sections, but no speciﬁc al- gorithm for the frequency-region partitioning has been proposed. To make the entire identiﬁcation process automatic, this letter pro- poses a binary partitioning algorithm. Index Terms—Electromagnetic transient analysis, equivalent circuits, frequency response, interconnected power systems, power system modeling, power system simulation. I. INTRODUCTION E LECTROMAGNETIC TRANSIENT (EMT) simulations have become crucial for the design and operation of a power system. For redu

## 核心贡献


- 提出二分频率区域划分算法，实现多相网络等值辨识全自动化。
- 基于拟合精度与幅值极小值自适应划分频段，避免有理拟合病态。
- 结合增强型有理拟合与矩阵部分分式展开，实现宽频导纳高精度等值。


## 使用的方法


- [[增强型有理拟合|增强型有理拟合]]
- [[矩阵部分分式展开-mpfe|矩阵部分分式展开(MPFE)]]
- [[最小二乘法|最小二乘法]]
- [[二分频率划分算法|二分频率划分算法]]
- [[极点辨识|极点辨识]]


## 涉及的模型


- [[多相网络等值模型|多相网络等值模型]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[同步发电机|同步发电机]]
- [[导纳矩阵|导纳矩阵]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络等值|网络等值]]
- [[频率相关建模|频率相关建模]]
- [[频域系统辨识|频域系统辨识]]
- [[降阶建模|降阶建模]]


## 主要发现


- 算法在1%误差容限下自动划分9个频段，极点辨识精度极高。
- MPFE模型精确复现多相导纳矩阵各元素，频域拟合偏差极小。
- 等值模型用于开关暂态仿真，时域波形与全系统详细模型几乎一致。



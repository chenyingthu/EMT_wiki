---
title: "Ahmed 等 | A Computationally Efficient Continuous Model for the Modular Multilevel Converter"
type: source
authors: ['Periodicals']
year: 2014
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/01/Ahmed 等 - 2014 - A Computationally Efficient Continuous Model for the Modular Multilevel Converter.pdf"]
---

# Ahmed 等 | A Computationally Efficient Continuous Model for the Modular Multilevel Converter

**作者**: Periodicals
**年份**: 2014
**来源**: `01/Ahmed 等 - 2014 - A Computationally Efficient Continuous Model for the Modular Multilevel Converter.pdf`

## 摘要

—Simulation models of the modular multilevel converter (MMC) play a very important role for studying the dynamic performance. Detailed modeling of the MMC in electromagnetic transient (EMT) simulation programs is cumbersome, as it requires high computational effort and simulation time. Several averaged or continuous models proposed in the literature lack the capability to describe the blocked state. This paper presents a continuous model which is capable of accurately simulating the blocked state. This feature is very important for accurate simulation of faults. The model is generally applicable, although it is particularly useful in high-

## 核心贡献


- 提出可精确模拟闭锁状态的MMC连续模型，弥补传统平均模型无法描述故障工况的缺陷。
- 基于桥臂总电容电压与环流构建状态空间方程，有效降低多子模块系统的仿真计算复杂度。
- 模型隐去开关动作细节，在保持系统级动态精度的同时实现极高的电磁暂态仿真计算效率。


## 使用的方法


- [[连续模型|连续模型]]
- [[状态空间法|状态空间法]]
- [[平均值法|平均值法]]
- [[支路建模|支路建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[半桥子模块|半桥子模块]]
- [[桥臂等效电路|桥臂等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[故障仿真|故障仿真]]
- [[闭锁状态建模|闭锁状态建模]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 仿真波形与PSCAD详细模型高度一致，验证了该模型在正常及故障工况下的动态精度。
- 十千伏安样机实验证实模型能准确复现闭锁期间的电容充电与二极管续流物理过程。
- 相比详细开关模型，该连续模型大幅减少网络节点与状态变量，显著缩短电磁暂态仿真时间。



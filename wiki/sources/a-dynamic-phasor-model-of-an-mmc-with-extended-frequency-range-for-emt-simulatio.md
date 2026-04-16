---
title: "A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT Simulations"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics; ;PP;99;10.1109/JESTPE.2018.2886698"
tags: ['mmc', 'dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/01/Rupasinghe 等 - 2019 - A Dynamic Phasor Model of an MMC With Extended Frequency Range for EMT Simulations.pdf"]
---

# A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT Simulations

**作者**: 
**年份**: 2018
**来源**: `01/Rupasinghe 等 - 2019 - A Dynamic Phasor Model of an MMC With Extended Frequency Range for EMT Simulations.pdf`

## 摘要

—This paper presents a new dynamic phasor model of a modular multilevel converter (MMC) with extended frequency range for direct interfacing to an electromagnetic transient (EMT) simulator. The internal dynamics of the MMC are modeled considering dominant harmonic components of each variable. To model the external dynamics of the converter a novel construct referred to as a base-frequency dynamic phasor is employed, which allows to capture and model any number of frequency components of external variables without significant increase in computational burden. The proposed model is validated against detailed EMT models by comparing its results for an inverter system, a back-to- back HVDC system, and a 12-bus power system built in PSCAD/EMTDC simulator. Simulation results prove that the new m

## 核心贡献


- 提出基频动态相量新结构，实现外部变量任意频率分量的高效建模
- 构建可直接嵌入EMT仿真器的MMC模型，支持任意拓扑网络接口
- 实现模型精度与计算负担灵活调节，兼顾内部谐波动态与外部交互


## 使用的方法


- [[动态相量法|动态相量法]]
- [[基频动态相量建模|基频动态相量建模]]
- [[最近电平逼近调制|最近电平逼近调制]]
- [[电容电压平衡算法|电容电压平衡算法]]
- [[节点导纳矩阵求解|节点导纳矩阵求解]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[vsc-model|VSC]]
- [[背靠背直流系统|背靠背直流系统]]
- [[12节点交流系统|12节点交流系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[扩展频率范围建模|扩展频率范围建模]]
- [[谐波分析|谐波分析]]
- [[计算效率优化|计算效率优化]]
- [[vsc-hvdc|VSC-HVDC]]


## 主要发现


- 在逆变器、背靠背HVDC及12节点系统中验证，精度与详细EMT模型高度一致
- 相比现有模型计算效率显著提升，支持灵活调节谐波数量且不增加计算负担
- 缩比实验室台架实验验证了模型在真实硬件接口下的动态响应准确性



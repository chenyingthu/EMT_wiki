---
title: "Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Energy Conversion;2019;34;4;10.1109/TEC.2019.2937761"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/26/Herath 等 - 2019 - Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Electromagnetic Transien.pdf"]
---

# Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2019
**来源**: `26/Herath 等 - 2019 - Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Electromagnetic Transien.pdf`

## 摘要

—This paper proposes a detailed equivalent model for electromagnetic transient simulation of a modular multilevel con- verter with embedded battery energy storage in its submodules. The model offers an accuracy identical to that of a detailed switch- ing model (DSM), while it markedly reduces the computational complexity of simulations. This is achieved by modeling each mul- tivalve as a Thevenin equivalent considering the full dynamics of each constituent submodule, which results in a signiﬁcant reduction in the number of switchable nodes in the converter model and hence the dimensions of the system’s admittance matrix. The paper presents the mathematical development of the model and validates it against detailed switching models through several case studies. Experimental results from a s

## 核心贡献


- 提出含嵌入式储能的MMC详细等效模型以替代传统开关模型
- 将多阀臂等效为戴维南电路，保留子模块全动态并大幅减少可切换节点
- 显著降低导纳矩阵维度与求逆频率，实现高精度与低计算复杂度的统一


## 使用的方法


- [[戴维南等效|戴维南等效]]
- [[节点分析法|节点分析法]]
- [[详细等效模型|详细等效模型]]
- [[最近电平控制|最近电平控制]]
- [[状态均衡控制|状态均衡控制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[电池储能系统|电池储能系统]]
- [[子模块|子模块]]
- [[双向dc-dc变换器|双向DC-DC变换器]]
- [[详细开关模型|详细开关模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[储能集成建模|储能集成建模]]
- [[计算效率优化|计算效率优化]]
- [[电力电子变换器建模|电力电子变换器建模]]
- [[详细等效建模|详细等效建模]]


## 主要发现


- 模型精度与详细开关模型完全一致，完整复现了系统电磁暂态动态特性
- 大幅减少可切换节点，使导纳矩阵求逆计算负担降低数个数量级
- 缩比实验验证了模型在各类暂态工况下的准确性与数值稳定性



---
title: "Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Model on FPGA for HIL Emulation"
type: source
authors: ['Jiadai Liu', 'Venkata Dinavahi']
year: 2016
journal: "IEEE Transactions on Power Delivery;2016;31;6;10.1109/TPWRD.2016.2518676"
tags: ['real-time', 'fpga', 'transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Mode.pdf"]
---

# Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Model on FPGA for HIL Emulation

**作者**: Jiadai Liu, Venkata Dinavahi
**年份**: 2016
**来源**: `27&28/Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Mode.pdf`

## 摘要

—Strategic power-ﬂow control using a Sen transformer (ST) can be a robust and cost-effective solution to relieve grid con- gestion due to increased installation of renewables. The ST con- sists of a multiwinding transformer and tap changer that can reg- ulate the power ﬂow through a transmission line by injecting a series-connected controllable voltage. This paper develops a real- time high-ﬁdelity magnetic equivalent circuit-based electromag- netic transient model for the ST on the ﬁeld-programmable gate array (FPGA) for hardware-in-the-loop applications. This geom- etry-based model was developed to depict the major ﬂux paths in the transformer core, and complex nonlinear phenomena, such as saturation, hysteresis, and eddy currents. The entire real-time ST model and other power system com

## 核心贡献


- 提出基于几何结构的非线性磁等效电路模型，精确刻画铁芯饱和与磁滞涡流效应
- 设计全并行流水线FPGA架构，实现32位浮点精度的低延迟实时电磁暂态仿真
- 将Preisach磁滞理论与频变等效网络融入时变节点导纳矩阵的实时更新算法


## 使用的方法


- [[磁等效电路法|磁等效电路法]]
- [[preisach磁滞模型|Preisach磁滞模型]]
- [[频变等效网络|频变等效网络]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[并行流水线架构|并行流水线架构]]
- [[硬件描述语言|硬件描述语言]]


## 涉及的模型


- [[sen变压器|Sen变压器]]
- [[多绕组变压器|多绕组变压器]]
- [[输电线路|输电线路]]
- [[分接开关|分接开关]]
- [[三维有限元模型|三维有限元模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[fpga实现|FPGA实现]]
- [[非线性磁路建模|非线性磁路建模]]
- [[潮流控制|潮流控制]]
- [[并行计算|并行计算]]


## 主要发现


- FPGA实时仿真结果与三维有限元软件高度吻合，验证了模型的高保真度
- 全并行流水线架构显著降低计算延迟与逻辑资源占用，满足微步长实时要求
- 磁等效电路法有效克服分段线性近似的数值振荡问题，准确复现复杂非线性暂态



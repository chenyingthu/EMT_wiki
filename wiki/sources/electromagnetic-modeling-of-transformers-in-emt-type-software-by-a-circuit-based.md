---
title: "Electromagnetic Modeling of Transformers in EMT-Type Software by a Circuit-Based Method"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;6;10.1109/TPWRD.2022.3177137"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic modeling of transformers in EMT-type software by a circuit-based method_Pordanjani 等_2022.pdf"]
---

# Electromagnetic Modeling of Transformers in EMT-Type Software by a Circuit-Based Method

**作者**: 
**年份**: 2022
**来源**: `15/Electromagnetic modeling of transformers in EMT-type software by a circuit-based method_Pordanjani 等_2022.pdf`

## 摘要

—This work proposes a fully circuit-based method for modelling electrical transformers. This method not only offers the advantages of circuit-based methods and can be implemented in electromagnetic transient (EMT) type software, but it can also provide a detailed representation of transformers, comparable to the ﬁnite element method (FEM). The proposed method enables a detailed geometrical modelling, as well as representation of mag- netic ﬂux paths and consideration of iron core saturation. It can be implemented in EMT-type software to see the effect of power networks on transformers. In addition, the proposed method can represent internal faults in transformers. The problem is con- strained to a 2-D domain, which is often used in FEMs to represent the magnetic behavior of power equipment

## 核心贡献


- 提出分布式磁阻网络模型，在EMT软件中实现媲美有限元的变压器详细电磁建模。
- 采用网格化磁路离散方法，精确表征磁通路径分布、铁芯饱和及非均匀材料特性。
- 实现变压器内部匝间与对地故障的高效电路级仿真，兼顾计算精度与速度。


## 使用的方法


- [[磁路等效电路法|磁路等效电路法]]
- [[分布式磁阻网络模型|分布式磁阻网络模型]]
- [[空间网格离散|空间网格离散]]
- [[霍普金森类比|霍普金森类比]]
- [[有限元法验证|有限元法验证]]


## 涉及的模型


- [[变压器|变压器]]
- [[壳式变压器|壳式变压器]]
- [[三相双绕组变压器|三相双绕组变压器]]
- [[铁芯|铁芯]]
- [[绕组|绕组]]
- [[内部故障模型|内部故障模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器详细建模|变压器详细建模]]
- [[铁芯饱和|铁芯饱和]]
- [[内部故障仿真|内部故障仿真]]
- [[磁路网络建模|磁路网络建模]]
- [[路场等效|路场等效]]


## 主要发现


- DRNM模型在正常运行与暂态工况下的仿真结果与有限元法高度吻合。
- 相比传统场路耦合方法，该纯电路模型大幅提升了计算效率且保持高精度。
- 模型能准确复现匝间及对地故障下的漏磁分布与铁芯饱和非线性特性。



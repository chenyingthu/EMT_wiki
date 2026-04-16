---
title: "A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations"
type: source
authors: ['Ajinkya Sinkar']
year: 2021
journal: "Electric Power Systems Research, 198 (2021) 107360. doi:10.1016/j.epsr.2021.107360"
tags: ['state-space']
created: "2026-04-13"
sources: ["EMT_Doc/01/Sinkar 等 - 2021 - A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descripto.pdf"]
---

# A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations

**作者**: Ajinkya Sinkar
**年份**: 2021
**来源**: `01/Sinkar 等 - 2021 - A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descripto.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations Ajinkya Sinkar , Huanfeng Zhao , Bolin Qu , Aniruddha M. Gole Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2 Canada

## 核心贡献


- 提出基于修正节点分析自动构建描述符状态空间方程的方法，避免复杂图论操作。
- 设计描述符状态空间方程与伴随电路仿真器的接口算法，实现无延迟的并行计算。
- 验证描述符状态空间方程的稀疏矩阵特性，支持直接进行系统特征值分析。


## 使用的方法


- [[伴随电路法|伴随电路法]]
- [[描述符状态空间方程|描述符状态空间方程]]
- [[修正节点分析|修正节点分析]]
- [[梯形积分法|梯形积分法]]
- [[并行接口技术|并行接口技术]]


## 涉及的模型


- [[集中参数rlc元件|集中参数RLC元件]]
- [[独立电压-电流源|独立电压/电流源]]
- [[ieee-39节点系统|IEEE 39节点系统]]
- [[vsc-hvdc|VSC-HVDC]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络方程建模|网络方程建模]]
- [[混合仿真接口|混合仿真接口]]
- [[并行计算|并行计算]]
- [[系统特征值分析|系统特征值分析]]


## 主要发现


- 描述符状态空间方程与伴随电路法精度一致，稀疏矩阵特性更利于大规模系统求解。
- 接口算法在IEEE 39节点含HVDC系统中验证成功，实现无时间步延迟的并行加速。
- 描述符状态空间方程可直接导出连续域矩阵，便于直接计算系统特征值无需后处理。



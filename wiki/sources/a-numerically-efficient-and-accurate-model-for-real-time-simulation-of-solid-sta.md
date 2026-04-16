---
title: "A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using Implicit-Explicit Integration Methods"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Electronics;2026;41;6;10.1109/TPEL.2025.3650144"
tags: ['real-time', 'transformer']
created: "2026-04-13"
sources: ["EMT_Doc/03/Li 等 - 2026 - A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using.pdf"]
---

# A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using Implicit-Explicit Integration Methods

**作者**: 
**年份**: 2026
**来源**: `03/Li 等 - 2026 - A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using.pdf`

## 摘要

—Electromagnetic transient (EMT) models of power electronic converters are essential for converter design, control, and fault analysis. This article proposes a switching-function-based detailed equivalent model (SFB-DEM) using combined implicit and explicit (ImEx) multistep Gear’s integration methods for nu- merically efﬁcient and accurate EMT simulation. The proposed SFB-DEM integrates the beneﬁts of ImEx solvers, featuring con- verter circuit decoupling, node number reduction, and constant nodal-network conductance(G)-matrix in the EMT model. The SFB-DEMs employing the ImEx 2nd and 3rd order Gear’s (i.e., ImEx-G2O and ImEx-G3O) methods are implemented for solid- state transformer (SST) simulation. In addition, a switching inter- polation technique is proposed and integrated with the ImEx

## 核心贡献


- 提出基于开关函数的详细等效模型，结合隐显式Gear法实现电路解耦与节点缩减
- 构建恒定网络导纳矩阵策略，消除开关切换导致的导纳矩阵重复分解计算负担
- 提出适配隐显式多步法的开关插值技术，精确捕捉步内开关事件以提升数值精度


## 使用的方法


- [[numerical-integration|数值积分]]
- [[基于开关函数的详细等效建模|基于开关函数的详细等效建模]]
- [[开关插值技术|开关插值技术]]
- [[恒定导纳矩阵法|恒定导纳矩阵法]]
- [[电路解耦与节点缩减|电路解耦与节点缩减]]


## 涉及的模型


- [[固态变压器|固态变压器]]
- [[级联全桥子模块|级联全桥子模块]]
- [[双有源桥dc-dc变换器|双有源桥DC-DC变换器]]
- [[中频变压器|中频变压器]]
- [[输入串联输出并联拓扑|输入串联输出并联拓扑]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子变换器建模|电力电子变换器建模]]
- [[数值稳定性|数值稳定性]]
- [[步内开关事件处理|步内开关事件处理]]


## 主要发现


- 60子模块SST仿真中，ImEx-G3O模型较传统详细模型提速171倍
- 相比变导纳矩阵模型，所提模型在保持精度的同时实现7.5倍计算加速
- 隐显式Gear法结合开关插值有效抑制数值振荡，显著提升高频开关仿真精度



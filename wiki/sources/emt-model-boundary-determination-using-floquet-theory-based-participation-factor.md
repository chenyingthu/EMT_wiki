---
title: "EMT Model Boundary Determination Using Floquet Theory-based Participation Factors"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Systems; ;PP;99;10.1109/TPWRS.2026.3674489"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Sajjadi 等 - 2026 - EMT Model Boundary Determination Using Floquet Theory-based Participation Factors.pdf"]
---

# EMT Model Boundary Determination Using Floquet Theory-based Participation Factors

**作者**: 
**年份**: 2026
**来源**: `17/Sajjadi 等 - 2026 - EMT Model Boundary Determination Using Floquet Theory-based Participation Factors.pdf`

## 摘要

—To accelerate electromagnetic transient (EMT) simulations for power systems with inverter-based resources (IBRs), this paper proposes a new approach for determining the EMT model boundary using Floquet theory-based participation factors (PFs). The approach can significantly reduce the computational burden of EMT simulation to focus on a localized area whose components highly participate in the dynamics of interest such as sub-synchronous oscillations (SSOs), while the rest of the grid is represented using a simple Norton equivalent. Floquet theory enables the calculation of participation factors over a single cycle of the system in an EMT model, where the vector field exhibits periodic behavior around the synchronous frequency. A data-driven method is also proposed for estimating particip

## 核心贡献


- 提出基于Floquet理论的参与因子算法，仅需单周期数据即可精准识别次同步振荡关键元件。
- 建立线性时不变与时周期系统参与因子的数学联系，证明相量域方法仅为零次谐波特例。
- 提出数据驱动参与因子估计与谐波筛选准则，实现电磁暂态仿真边界的自动化高精度划分。


## 使用的方法


- [[floquet理论|Floquet理论]]
- [[参与因子分析|参与因子分析]]
- [[线性时周期系统分析|线性时周期系统分析]]
- [[数据驱动估计|数据驱动估计]]
- [[多端口诺顿等值|多端口诺顿等值]]
- [[emt模型线性化|EMT模型线性化]]
- [[谐波筛选|谐波筛选]]


## 涉及的模型


- [[逆变器型资源-ibr|逆变器型资源(IBR)]]
- [[同步发电机|同步发电机]]
- [[输电线路与母线|输电线路与母线]]
- [[多端口诺顿等值模型|多端口诺顿等值模型]]
- [[改进kundur两区域系统|改进Kundur两区域系统]]
- [[ieee-39节点系统|IEEE 39节点系统]]


## 相关主题


- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[emt边界划分|EMT边界划分]]
- [[次同步振荡分析|次同步振荡分析]]
- [[网络等值|网络等值]]
- [[高比例新能源系统动态|高比例新能源系统动态]]
- [[模型降阶|模型降阶]]


## 主要发现


- 结合诺顿等值仅保留关键区域，显著降低计算量且精确复现次同步振荡动态。
- Floquet方法突破相量域局限，准确识别高频谐波贡献与关键电气耦合路径。
- 数据驱动法仅需单周期响应即可快速估算参与因子，验证了多故障场景下的鲁棒性。



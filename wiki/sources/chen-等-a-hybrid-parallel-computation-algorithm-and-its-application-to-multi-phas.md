---
title: "Chen 等 | A hybrid parallel computation algorithm and its application to multi-phase hybrid ACDC power system"
type: source
authors: ['未知']
year: 2010
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Chen 等 - 2010 - A hybrid parallel computation algorithm and its application to multi-phase hybrid ACDC power system.pdf"]
---

# Chen 等 | A hybrid parallel computation algorithm and its application to multi-phase hybrid ACDC power system

**作者**: 
**年份**: 2010
**来源**: `01/Chen 等 - 2010 - A hybrid parallel computation algorithm and its application to multi-phase hybrid ACDC power system.pdf`

## 摘要

：The integrated power system is atypical hybrid AC／DC power system，which usually consists of multi—phase motors and power electronic devices．Because of the many electrical ports used．the multi—phase motors眦hard to be decomposed optimally for parallel computing，which limit the speedup of the electromagnetic transients simulation of

## 核心贡献


- 提出结合元件级与网络级并行的混合算法，提升多相电机系统分区灵活性。
- 将多相电机拆分为多个耦合小电机，降低单元件计算量并优化系统切分方案。
- 优化并行计算流程，利用协调侧等待时间执行元件级任务，显著降低同步开销。


## 使用的方法


- [[隐式梯形积分法|隐式梯形积分法]]
- [[诺顿等效模型|诺顿等效模型]]
- [[多端口戴维南等效-mate|多端口戴维南等效(MATE)]]
- [[元件级并行|元件级并行]]
- [[网络级并行|网络级并行]]
- [[分解协调计算|分解协调计算]]


## 涉及的模型


- [[十二相发电机|十二相发电机]]
- [[十五相电动机|十五相电动机]]
- [[多相电机|多相电机]]
- [[三相不控整流桥|三相不控整流桥]]
- [[spwm逆变器|SPWM逆变器]]
- [[交直流混合电力系统|交直流混合电力系统]]


## 相关主题


- [[并行计算|并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统切分与负载均衡|系统切分与负载均衡]]
- [[超实时仿真|超实时仿真]]
- [[综合电力系统|综合电力系统]]


## 主要发现


- 混合并行算法仿真误差控制在10^-4量级内，验证了模型分解与协调计算的正确性。
- 相比传统MATE算法，该混合并行方案加速比达5.20，成功实现超实时仿真。
- 元件级拆分有效降低协调侧方程维数，显著改善分区负载均衡并减少同步等待时间。



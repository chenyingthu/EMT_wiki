---
title: "恒导纳模型 (Fixed Admittance / ADC Model)"
type: method
tags: [fixed-admittance, adc, real-time, companion-circuit]
created: "2026-04-13"
---

# 恒导纳模型 (Fixed Admittance / ADC Model)

## 定义与概述

恒导纳模型（Fixed Admittance Model）也常被称为关联离散电路模型（Associated Discrete Circuit, ADC）。它通过伴随电路和等效历史源把开关器件、桥臂模块或局部子网络表示为导纳矩阵不随开关状态改变的模型。开关动作只改变右端注入项或历史源，从而避免每次拓扑变化都重新组装和分解网络矩阵。

该方法主要服务于含大量开关器件的 EMT 仿真，尤其是实时仿真、FPGA/CPU 异构仿真、MMC 桥臂等效和电力电子变换器快速模型。

## 作用机制

常规详细开关模型会随导通/关断状态改变网络拓扑，导致导纳矩阵频繁变化。恒导纳模型的关键做法是：

$$
i_k=Y_{\mathrm{fix}}v_k+i_{\mathrm{hist}}(s_k,x_{k-1})
$$

其中 $Y_{\mathrm{fix}}$ 在开关状态 $s_k$ 改变时保持不变，开关动作和历史状态被转移到右端历史源 $i_{\mathrm{hist}}$。这样主网络矩阵可重复使用，但必须检查历史源构造是否引入虚拟损耗或状态误差。

- 为开关状态构造共享的等效导纳，使主网络矩阵在仿真过程中保持不变。
- 把开关状态、历史电压电流和控制量的影响放入等效电流源或历史源。
- 在初始化阶段完成矩阵组装和分解，后续时步主要执行右端项更新与前代/回代。
- 对桥臂、半桥腿或子模块进行分组等效，减少端口数量和全局耦合。
- 在需要保持开关时刻精度时，配合插值、分数步长或局部修正控制虚拟损耗。

恒导纳模型与 [[numerical-integration|数值积分]] 紧密相关：积分公式决定动态元件的伴随导纳和历史源形式；与 [[nodal-analysis|节点分析法]] 结合时，它的主要收益来自矩阵重复利用。

## 适用边界

- 适合开关数量多、拓扑变化频繁、矩阵分解成本占主导的电力电子 EMT 仿真。
- 适合实时仿真和硬件在环，因为固定矩阵更容易满足确定性计算时间。
- 若研究目标是器件级开关损耗、极短时标过电压或保护动作临界时刻，应检查恒导纳等效和插值策略是否保留足够细节。
- 固定导纳构造可能引入虚拟损耗、接口延迟或条件数问题，需要通过能量误差、波形对比和极端工况验证。
- 对强非线性器件或状态依赖参数，通常需要局部迭代、分段线性化或混合模型，而不是把所有元件都强行纳入同一个固定矩阵。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul|A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation]] | 2025 | 面向变流器桥臂模块的固定导纳 ADC 建模。 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等：A fixed-admittance algorithm for the FPGA-based microsecond-level nonlinear EMT simulation]] | 2025 | 面向 FPGA 微秒级实时仿真的恒导纳算法。 |
| [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-|Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit]] | 2026 | 以 ADC 形式解析建模半桥腿。 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State-Variables-Elimination-Based EMTP-Type Constant-Admittance Equivalent Model]] | 2024 | 通过状态变量消元构造恒导纳等效。 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified high-speed EMT equivalent and implementation method of MMCs]] | 2024 | 将恒定矩阵思想用于 MMC 高速等效。 |

## 相关页面

- [[nodal-analysis|节点分析法]]
- [[numerical-integration|数值积分]]
- [[state-space-method|状态空间法]]
- [[average-value-model|平均值模型]]
- [[models/mmc-model|MMC 模型]]
- [[topics/real-time-simulation|实时仿真]]

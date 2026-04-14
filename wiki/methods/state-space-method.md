---
title: "状态空间法"
type: method
tags: []
created: "2026-04-13"
---

# 状态空间法

## 论文方法分析
> 基于 8 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 状态空间法 | 3 | A state-space approach for accelerated simulation of modular multileve |
| 分段广义状态空间平均法(P-GSSA) | 2 | A Piecewise Generalized State Space Model of Power Converters for Elec |
| 多时间尺度建模 | 2 | A Piecewise Generalized State Space Model of Power Converters for Elec |
| 描述符状态空间方程(DSE) | 1 | A Comparative Study of Electromagnetic Transient Simulations using Com |
| 伴随电路(CC)法 | 1 | A Comparative Study of Electromagnetic Transient Simulations using Com |
| 改进节点分析法(MNA) | 1 | A Comparative Study of Electromagnetic Transient Simulations using Com |
| 梯形积分法 | 1 | A Comparative Study of Electromagnetic Transient Simulations using Com |
| 广义状态空间平均法(GSSA) | 1 | A Piecewise Generalized State Space Model of Power Converters for Elec |
| 子模块开关状态分组技术 | 1 | A state-space approach for accelerated simulation of modular multileve |
| 辅助状态变量引入 | 1 | A state-space approach for accelerated simulation of modular multileve |
| 电容电压均衡算法 | 1 | A state-space approach for accelerated simulation of modular multileve |
| 频变集总参数模型(FDLPM) | 1 | Alternative method to include the frequency-effect on transmission lin |
| 时域直接求解法 | 1 | Alternative method to include the frequency-effect on transmission lin |
| π型电路级联建模 | 1 | Alternative method to include the frequency-effect on transmission lin |
| Splitting state-space method | 1 | Splitting State-Space Method for Converter-Integrated Power Systems EM |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 并网变流器 | 2 |
| 通用电力网络 | 1 |
| 电路网表 | 1 |
| 电感与电容动态元件 | 1 |
| 新能源并网系统 | 1 |
| 模块化多电平换流器(MMC) | 1 |
| MMC-HVDC系统 | 1 |
| 子模块(SM) | 1 |
| 输电线路 | 1 |
| 单相/三相输电线路 | 1 |
| 频变集总参数模型 | 1 |
| π型等效电路 | 1 |
| Converter-integrated power systems | 1 |
| Distribution network with DC load | 1 |
| LLC resonant converter | 1 |
### 验证方式分布
- **仿真**: 4 篇
- **仿真对比**: 3 篇
- **仿真/对比**: 1 篇
## 技术演进脉络
### 2016年 (1篇)
- **线性开关电路电磁暂态分析的状态方程法**
  - 💡 提出以节点电位为状态变量的状态方程法，结合能量守恒原理与混合数值积分策略，实现了开关电路拓扑变化的高效更新与数值振荡的有效抑制。
  - 提出以节点电位为状态变量的状态方程法，基于能量守恒原理列写方程，速度远优于传统方法。
  - 针对开关动作引起的拓扑变化，仅需更新特定支路信息，无需重新分解和列写整个电路方程。
### 2019年 (2篇)
- **基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法**
  - 💡 通过引入辅助变量将HVDC系统非齐次微分方程转化为齐次形式，实现了电磁暂态简化模型的高效解析求解，兼顾了计算速度与仿真精度。
  - 提出了一种基于状态空间法的HVDC系统电磁暂态简化模型解析算法，专门用于模拟逆变侧交流故障下的暂态响应。
  - 利用准稳态模型对整流侧进行等效简化，并将不同工况下的换流器统一表示为分时段线性非齐次微分方程组。
- **适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型**
  - 💡 将分段技术与广义状态空间平均法相结合，通过合并相似动作特性的时间段实现多时间尺度变尺度建模，从而在电磁暂态仿真中兼顾精度与效率。
  - 提出了一种适用于大规模新能源并网变流器的分段广义状态空间平均(P-GSSA)建模方法。
  - 将分段技术引入广义状态空间平均模型，实现了动作特性相似时间段的合并与变尺度建模。
### 2021年 (1篇)
- **A Comparative Study of Electromagnetic Transient Simulations using Companion Cir**
  - 💡 提出基于描述符状态空间方程的自动化EMT建模方法，并首创与主流伴随电路仿真器的通用接口，兼顾了建模灵活性与并行计算加速潜力。
  - 提出了一种直接从电路网表自动生成描述符状态空间方程(DSE)的EMT仿真建模流程。
  - 系统对比了DSE方法与传统伴随电路(CC)方法在方程构建、数值稳定性及计算效率上的优缺点。
### 2022年 (1篇)
- **A Piecewise Generalized State Space Model of Power Converters for Electromagneti**
  - 💡 将分段技术引入广义状态空间平均法，通过合并动作特性一致的时间段，实现了变流器电磁暂态的多时间尺度高效建模。
  - 提出了一种适用于电力电子变流器的分段广义状态空间平均(P-GSSA)建模方法。
  - 将分段技术应用于GSSA模型，通过合并动作特性一致的时间段，实现了变流器电磁暂态的多时间尺度建模。
### 2023年 (1篇)
- **Alternative method to include the frequency-effect on transmission line paramete**
  - 💡 通过独立求解各π型电路的状态空间方程以降低矩阵阶数，实现了无需频时转换的高效、高精度时域频变输电线路暂态仿真。
  - 提出了一种直接在时域求解频变输电线路参数的替代方法，避免了传统频时转换工具的使用。
  - 通过独立求解每个π型电路的状态空间方程，有效降低了整体状态空间矩阵的阶数。
### 2025年 (2篇)
- **A state-space approach for accelerated simulation of modular multilevel converte**
  - 💡 创新性地将子模块开关状态分组与辅助状态变量引入状态空间框架，实现状态矩阵降维与仿真加速，突破了传统节点分析等效模型的局限。
  - 提出了一种基于状态空间框架的MMC仿真加速方法，通过按开关状态组合对子模块分组并引入辅助状态变量，显著降低了状态矩阵维度。
  - 利用状态变量分组特性，设计了一种高效的电容电压均衡算法，提升了仿真过程中的控制与计算效率。
- **Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulati**
  - 💡 提出结合自动开关分组解耦与多阶指数分裂公式的状态空间求解框架，实现含变流器电力系统EMT仿真的高效计算与误差控制。
  - 提出基于开关状态依赖子电路拓扑的通用解耦原理，实现状态空间方程的高效分裂。
  - 引入多阶精度的指数分裂公式，在控制数值误差的同时加速矩阵指数运算。
## 关键发现汇总
- [2016] **线性开关电路电磁暂态分析的状态方程法**: 成功消除了开关动作时刻的数值振荡现象。
- [2016] **线性开关电路电磁暂态分析的状态方程法**: 在线性时间段内保持了二阶数值精度。
- [2016] **线性开关电路电磁暂态分析的状态方程法**: 相比传统节点分析法，在大规模开关电路仿真中展现出更优的稳定性与计算灵活性。
- [2019] **基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法**: 所提解析算法在Matlab中的计算速度显著快于传统PSCAD小步长数值积分仿真。
- [2019] **基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法**: 该算法在提高计算效率的同时，未降低对逆变侧动态响应及换相失败过程的模拟精度。
- [2019] **基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法**: 有效避免了传统电磁暂态仿真中因插值获取换相电流过零点而引发的数值振荡问题。
- [2019] **适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型**: 所提模型在变流器暂态仿真中实现了计算效率与精度的有效平衡。
- [2019] **适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型**: 该模型能够适应大规模新能源并网场景下变流器的高效电磁暂态仿真需求。
- [2021] **A Comparative Study of Electromagnetic Transient Simulations**: DSE方法利用描述符变量允许线性相关的特性，彻底避免了传统状态空间法中对电感割集和电容回路的特殊拓扑处理。
- [2021] **A Comparative Study of Electromagnetic Transient Simulations**: 所提出的DSE-CC接口流程能够无缝对接主流商业EMT仿真平台，实现了自定义模型与成熟求解器的兼容。
- [2021] **A Comparative Study of Electromagnetic Transient Simulations**: 基于该接口架构的并行计算方案有效突破了传统串行仿真的瓶颈，为大规模电力网络EMT仿真提供了加速途径。
- [2022] **A Piecewise Generalized State Space Model of Power Converter**: 所提P-GSSA模型在变流器暂态仿真中成功实现了计算效率与模型精度的平衡。
- [2022] **A Piecewise Generalized State Space Model of Power Converter**: 该模型能够适应大规模新能源并网变流器的高效电磁暂态仿真需求。
- [2023] **Alternative method to include the frequency-effect on transm**: 该方法的暂态响应结果与经典方法高度一致，验证了其优异的仿真精度。
- [2023] **Alternative method to include the frequency-effect on transm**: 在相同固定时间步长下，新方法的计算时间比传统方法缩短了230至300倍。
- [2025] **A state-space approach for accelerated simulation of modular**: 所提方法通过状态矩阵降维显著加快了数值积分速度，有效解决了高阶MMC系统仿真耗时过长的问题。
- [2025] **A state-space approach for accelerated simulation of modular**: 仿真案例验证了该加速模型在保持电磁暂态仿真精度的同时，大幅提升了整体计算效率。
- [2025] **Splitting State-Space Method for Converter-Integrated Power **: 所提方法在多种测试案例中实现了与详细EMT模型相当的高保真仿真精度。
- [2025] **Splitting State-Space Method for Converter-Integrated Power **: 多阶指数分裂方案显著加速了矩阵指数计算过程，并有效控制了数值误差。

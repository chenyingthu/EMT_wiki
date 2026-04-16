---
title: "A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation"
type: source
authors: ['Dong Li']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112427. doi:10.1016/j.epsr.2025.112427"
tags: ['real-time', 'pmsm']
created: "2026-04-13"
sources: ["EMT_Doc/01/Li 等 - 2025 - A Flux-Defined Pmsm Model Based on Fea Results for Real-Time Emt Simulation.pdf"]
---

# A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation

**作者**: Dong Li
**年份**: 2025
**来源**: `01/Li 等 - 2025 - A Flux-Defined Pmsm Model Based on Fea Results for Real-Time Emt Simulation.pdf`

## 摘要

A Flux-Defined PMSM Model Based on FEA Results for Real-Time To expedite the PMSM design and test process, high-fidelity PMSM model derived from Finite Element Analysis (FEA) has been studied by many researchers. This paper proposed a new approach to calculate derivatives of currents with flux linkage data, which does not require taking hours to inverse the data table. Detailed math­ ematical proof is reported, based on which the implementation is explained, including presenting an efficient

## 核心贡献


- 提出基于磁链数据直接求解电流导数的方法，免去传统查表反演耗时。
- 设计高效三线性插值与外推平滑策略，提升实时仿真数值稳定性。
- 将FEA降阶模型部署于RTDS平台，实现亚微秒步长实时电磁暂态仿真。


## 使用的方法


- [[有限元分析-fea|有限元分析(FEA)]]
- [[查表法-lut|查表法(LUT)]]
- [[降阶模型-rom|降阶模型(ROM)]]
- [[三线性插值|三线性插值]]
- [[外推平滑算法|外推平滑算法]]
- [[dq0坐标变换|dq0坐标变换]]


## 涉及的模型


- [[pmsm-model|PMSM]]
- [[pmsm-model|PMSM]]
- [[集中参数电机模型|集中参数电机模型]]
- [[电动汽车动力总成|电动汽车动力总成]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[基于有限元的降阶建模|基于有限元的降阶建模]]
- [[空间谐波与磁饱和建模|空间谐波与磁饱和建模]]
- [[硬件在环测试|硬件在环测试]]
- [[电动汽车动力总成仿真|电动汽车动力总成仿真]]


## 主要发现


- 模型在RTDS上以小于1微秒步长稳定运行，计算效率显著优于传统FEA联合仿真。
- 仿真结果与FEA及集中参数模型对比验证，新模型能精确捕捉空间谐波与饱和效应。
- 外推平滑策略有效解决查表越界数值振荡，保障电动汽车工况下的仿真精度。



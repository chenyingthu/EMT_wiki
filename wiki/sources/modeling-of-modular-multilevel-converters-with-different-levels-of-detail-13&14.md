---
title: "Modeling of Modular Multilevel Converters with Different Levels of Detail"
type: source
authors: ['未知']
year: 2017
journal: "IEEE Transactions on Power Delivery"
tags: ['mmc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2017.2774806.pdf.pdf"]
---

# Modeling of Modular Multilevel Converters with Different Levels of Detail

**作者**: 未知
**年份**: 2017
**来源**: `13&14/files/TPWRD.2017.2774806.pdf.pdf`

## 摘要

The model of a modular multilevel converter (MMC) determines the extent of critical circuit information that electromagnetic transient simulations can reveal. Two MMC models are proposed for analysis.

## 核心贡献


- 提出基于IGBT动态曲线拟合的非线性开关模型，实现器件级电热暂态高精度仿真
- 将子模块等效为传输线短截线模型，构建混合桥臂以提升FPGA实时计算效率
- 采用电路分区与合并简化策略，解决大规模MMC网络实时仿真步长受限问题


## 使用的方法


- [[传输线短截线建模-tlm-stub|传输线短截线建模(TLM-stub)]]
- [[动态曲线拟合|动态曲线拟合]]
- [[电路分区与合并|电路分区与合并]]
- [[戴维南等效|戴维南等效]]
- [[分段线性化|分段线性化]]
- [[fpga硬件在环仿真|FPGA硬件在环仿真]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[直流-直流变换器|直流-直流变换器]]
- [[igbt功率器件|IGBT功率器件]]
- [[中频变压器-mft|中频变压器(MFT)]]
- [[多端直流电网-mtdc|多端直流电网(MTDC)]]
- [[子模块-sm|子模块(SM)]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环-hil|硬件在环(HIL)]]
- [[电热耦合仿真|电热耦合仿真]]
- [[fpga并行计算|FPGA并行计算]]
- [[多端直流系统|多端直流系统]]
- [[固态变压器-sst|固态变压器(SST)]]
- [[器件级建模|器件级建模]]


## 主要发现


- 曲线拟合模型可精确复现IGBT开关损耗与结温变化，满足电热设计评估需求
- TLM短截线混合桥臂模型显著降低FPGA硬件资源占用并提升仿真步长
- 三端HVDC系统硬件在环结果与PSCAD离线仿真高度吻合，验证模型有效性



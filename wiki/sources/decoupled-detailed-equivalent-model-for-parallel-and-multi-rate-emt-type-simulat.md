---
title: "Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Delivery;2026;41;2;10.1109/TPWRD.2025.3648650"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf"]
---

# Decoupled Detailed Equivalent Model for Parallel and Multi-Rate EMT-Type Simulation of Modular Multilevel Converter With Battery Energy Storage

**作者**: 
**年份**: 2026
**来源**: `12/Decoupled_Detailed_Equivalent_Model_for_Parallel_and_Multi-Rate_EMT-Type_Simulation_of_Modular_Multilevel_Converter_With_Battery_Energy_Storage.pdf`

## 摘要

—Modular multilevel converters (MMCs) integrated with battery energy storage systems (BESS) enable efﬁcient uti- lization of renewable energy resources such as wind and photo- voltaic, while enhancing reliability and scalability of high-voltage direct current systems. This paper proposes a decoupled detailed equivalent model (D-DEM) for BESS-integrated MMC for elec- tromagnetic transient (EMT) simulation. The proposed model can accurately represent the dynamics of the converter under deblock- ing and blocking modes. To efﬁciently utilize available hardware resources, a multi-rate simulation technique is adopted to sim- ulate the MMC subsystems with different time steps. Addition- ally, switching interpolation technique is proposed to accurately compensate for the intra-time-step switching 

## 核心贡献


- 提出解耦详细等效模型实现恒定导纳矩阵与节点缩减支持闭锁解锁状态
- 提出多速率仿真与开关插值技术实现变步长求解与步内开关事件精确补偿
- 开发CPU-GPU混合并行求解器大幅提升含储能MMC电磁暂态仿真效率


## 使用的方法


- [[多速率仿真|多速率仿真]]
- [[开关插值技术|开关插值技术]]
- [[节点分析法|节点分析法]]
- [[混合并行计算|混合并行计算]]
- [[等效电路建模|等效电路建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[bess|BESS]]
- [[子模块|子模块]]
- [[dc-dc变换器|DC-DC变换器]]
- [[详细等效模型|详细等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[多速率仿真|多速率仿真]]
- [[mmc-model|MMC]]
- [[储能系统集成|储能系统集成]]
- [[开关事件补偿|开关事件补偿]]


## 主要发现


- D-DEM在1微秒步长下与详细模型精度一致CPU单核仿真速度提升2.81倍
- 采用CPU-GPU混合并行求解器后仿真速度较纯CPU串行实现提升79倍
- 多速率与开关插值技术有效支持大时间步长同时保持闭锁解锁动态高精度



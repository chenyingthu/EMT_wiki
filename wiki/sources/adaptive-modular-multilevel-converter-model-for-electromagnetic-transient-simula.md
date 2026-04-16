---
title: "Adaptive Modular Multilevel Converter Model for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2993502"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/05/TPWRD.2020.2993502.pdf.pdf"]
---

# Adaptive Modular Multilevel Converter Model for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2020
**来源**: `05/TPWRD.2020.2993502.pdf.pdf`

## 摘要

—This paper proposes an adaptive model of modular multilevel converter (MMC) for electromagnetic transient (EMT) simulations. The model is applicable to MMCs with arbitrary numbers of half-bridge and full-bridge submodules. The proposed design includes average value model, arm equivalent model, and detailed equivalent model. It allows smoothly transitioning from one model to another during time-domain simulations depending on the desired accuracy and execution time constraints. Modifications required in conventional MMC models to achieve smooth transitions are presented in the paper. Time-domain initialization methods are developed for each constituting model, including initialization of the appropriate control system blocks. Validity and effectiveness of the proposed adaptive model is dem

## 核心贡献


- 提出包含三种等效模型的自适应MMC架构，实现仿真过程平滑切换
- 设计新型桥臂平均值模型统一电气接口，消除切换时的拓扑结构突变
- 开发各模型时域初始化与控制切换策略，确保状态转移无暂态冲击


## 使用的方法


- [[模型切换技术|模型切换技术]]
- [[平均值模型|平均值模型]]
- [[桥臂等效模型|桥臂等效模型]]
- [[详细等效模型|详细等效模型]]
- [[时域初始化|时域初始化]]
- [[诺顿等效|诺顿等效]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[全桥子模块|全桥子模块]]
- [[mmc-model|MMC]]
- [[耦合变压器|耦合变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[仿真加速|仿真加速]]
- [[mmc-model|MMC]]
- [[控制系统建模|控制系统建模]]


## 主要发现


- 在401电平MMC-HVDC系统中验证了模型切换的平滑性与接口一致性
- 自适应模型在保持外部电气特性精度的同时，显著降低了仿真计算耗时
- 所提时域初始化方法有效消除了模型切换瞬间产生的电压电流暂态冲击



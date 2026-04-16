---
title: "Modeling of MMC-based STATCOM with embedded energy storage for the simulation of electromagnetic transients"
type: source
authors: ['Anton Stepanov']
year: 2023
journal: "Electric Power Systems Research, 220 (2023) 109316. doi:10.1016/j.epsr.2023.109316"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modeling of MMC-based STATCOM with embedded energy storage for the simulation of electromagnetic tra.pdf"]
---

# Modeling of MMC-based STATCOM with embedded energy storage for the simulation of electromagnetic transients

**作者**: Anton Stepanov
**年份**: 2023
**来源**: `27&28/Modeling of MMC-based STATCOM with embedded energy storage for the simulation of electromagnetic tra.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Modeling of MMC-based STATCOM with embedded energy storage for the Anton Stepanov a,*, Hani Saad b, Jean Mahseredjian c The Delta-connected STATCOM is regarded as the most advantageous topology for STATCOMs based on the Modular Multilevel Converter (MMC) technology. Embedding energy storage devices into the MMCs has gained

## 核心贡献


- 提出三角形连接MMC-STATCOM灵活建模框架，实现换流器与储能模型无缝接口
- 系统应用四种MMC暂态模型，阐明储能装置在子模块、桥臂及等效层的集成方法
- 分析主换流器与储能控制环路交互，提供时间常数整定准则以避免动态耦合冲突


## 使用的方法


- [[详细模型-dm|详细模型(DM)]]
- [[详细等效模型-dem|详细等效模型(DEM)]]
- [[桥臂等效模型-aem|桥臂等效模型(AEM)]]
- [[average-value-model|平均值模型]]
- [[级联控制策略|级联控制策略]]
- [[双端口电路建模|双端口电路建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[statcom|STATCOM]]
- [[全桥子模块|全桥子模块]]
- [[超级电容|超级电容]]
- [[蓄电池|蓄电池]]
- [[dc-dc变换器|DC/DC变换器]]
- [[耦合变压器|耦合变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[储能集成建模|储能集成建模]]
- [[mmc-model|MMC]]
- [[statcom控制|STATCOM控制]]
- [[暂态性能分析|暂态性能分析]]
- [[电网频率支撑|电网频率支撑]]


## 主要发现


- 仿真表明桥臂等效与平均值模型在保持关键动态精度同时，显著降低计算耗时
- 合理设置控制环路时间常数可有效解耦主换流器与储能控制，避免动态交互冲突
- 双端口接口方法成功实现多种储能模型与不同精度换流器模型的灵活兼容



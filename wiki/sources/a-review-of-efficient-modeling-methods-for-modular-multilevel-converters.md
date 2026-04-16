---
title: "A review of efficient modeling methods for modular multilevel converters"
type: source
year: 2015
journal: "OCR-PDF"
created: "2026-04-13"
sources: ["EMT_Doc/03/Xu 等 - 2015 - A review of efficient modeling methods for modular multilevel converters.pdf"]
---

# A review of efficient modeling methods for modular multilevel converters

**年份**: 2015
**来源**: `03/Xu 等 - 2015 - A review of efficient modeling methods for modular multilevel converters.pdf`

## 摘要

：The modular multilevel converter(MMC】based HVDC system has shown its significant project prospects， hence the efficient modeling method of MMC iS the basis for a series of theoretical and engineering studies．This paper respectively focused OH different time scales and application

## 核心贡献


- 系统梳理不同时间尺度MMC建模方法，明确各模型适用场景与核心问题
- 严格对比验证受控源通用模型与两种戴维南等效整体模型的精度与加速比
- 验证电磁暂态平均简化模型在严重交直流暂态下的适用性并界定使用场景


## 使用的方法


- [[受控源等效法|受控源等效法]]
- [[戴维南等效法|戴维南等效法]]
- [[后退欧拉法|后退欧拉法]]
- [[梯形积分法|梯形积分法]]
- [[平均值模型|平均值模型]]
- [[矩阵降阶技术|矩阵降阶技术]]
- [[分组排序算法|分组排序算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[全桥子模块|全桥子模块]]
- [[换流变压器|换流变压器]]
- [[直流电缆|直流电缆]]
- [[戴维南等效模型|戴维南等效模型]]
- [[受控源模型|受控源模型]]
- [[平均值模型|平均值模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[vsc-model|VSC]]
- [[高效建模|高效建模]]
- [[电容均压算法|电容均压算法]]
- [[换流器闭锁|换流器闭锁]]
- [[交直流暂态分析|交直流暂态分析]]


## 主要发现


- 三种戴维南等效模型均具备极高仿真精度，后退欧拉法精度略低于梯形法
- 优化排序算法的戴维南模型仿真耗时随子模块数线性增长，提速效果显著
- 平均值模型可有效仿真严重交直流暂态，但无法精确反映子模块电容均压



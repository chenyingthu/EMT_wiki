---
title: "General approach for accurate resonance analysis in transformer windings"
type: source
authors: ['M. Popov']
year: 2018
journal: "Electric Power Systems Research, 161 (2018) 45-51. doi:10.1016/j.epsr.2018.04.002"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/j.epsr.2018.04.002.pdf.pdf"]
---

# General approach for accurate resonance analysis in transformer windings

**作者**: M. Popov
**年份**: 2018
**来源**: `19、20、21/EMT_task_20/j.epsr.2018.04.002.pdf.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了一种基于变压器绕组阻抗矩阵的精确谐振分析方法
- 引入放大系数作为关键指标，用于定位绕组中最严重的瞬态过电压发生位置
- 通过测试线圈实验与ATP-EMTP仿真验证了该方法的有效性，并证明其适用于含频变参数的多绕组变压器系统

## 使用的方法

- [[基于阻抗矩阵的频域分析方法|基于阻抗矩阵的频域分析方法]]
- [[放大系数-amplification-factor-计算法|放大系数（Amplification factor）计算法]]
- [[atp-emtp电磁暂态仿真验证|ATP-EMTP电磁暂态仿真验证]]
- [[矢量拟合-vector-fitting-与黑盒建模技术|矢量拟合（Vector Fitting）与黑盒建模技术]]

## 涉及的模型

- [[变压器绕组等效电路模型|变压器绕组等效电路模型]]
- [[测试线圈物理模型|测试线圈物理模型]]
- [[atp-emtp数值仿真模型|ATP-EMTP数值仿真模型]]
- [[频变电感-电容矩阵模型|频变电感/电容矩阵模型]]

## 相关主题

- [[电磁暂态-emt-分析|电磁暂态（EMT）分析]]
- [[变压器绕组谐振特性|变压器绕组谐振特性]]
- [[瞬态过电压评估|瞬态过电压评估]]
- [[绕组内部电压分布|绕组内部电压分布]]
- [[频变参数建模|频变参数建模]]

## 主要发现

- 最大谐振过电压的幅值直接取决于外部激励信号的持续时间及其对应的谐振频率
- 通过计算放大系数可以准确识别变压器绕组中瞬态过电压最严重的物理位置
- 基于精确阻抗矩阵的分析方法能够有效处理频率相关参数，为变压器绝缘设计与系统规划提供可靠依据

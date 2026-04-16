---
title: "A transformer model for winding fault studies - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/04/61.296246.pdf.pdf"]
---

# A transformer model for winding fault studies - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `04/61.296246.pdf.pdf`

## 摘要

This paper deals with a method of modeling intemal faults in a power transformer. The method leads to a model which is entirely compatible with the EMTP software. It enables simulation of faults between any turn and the earth or between any two turns of the transformer windings. Implementation of the proposed method assumes knowledge of how to evaluate the leakage factors between the various coils of the transformer. A very simple method is proposed to evaluate these leakage factors. At last, an experimental validation of the model allows the estimation of its accuracy. INTRODUCTION The development and the validation of algorithms for a digital differential transformer protection require the preliminary determination of a power transformer model [SI. This model must allow to simulate all t

## 核心贡献


- 提出线圈分割法构建变压器内部故障模型，将EMTP标准6阶RL矩阵扩展为7或8阶
- 结合一致性、漏磁与比例原则，推导故障子绕组自感与互感矩阵元素的解析计算公式
- 建立仅依赖几何尺寸与故障位置的漏磁系数快速评估方法，免除额外短路试验需求


## 使用的方法


- [[bctran例程|BCTRAN例程]]
- [[矩阵扩展法|矩阵扩展法]]
- [[漏磁系数计算|漏磁系数计算]]
- [[多绕组耦合建模|多绕组耦合建模]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[绕组故障模型|绕组故障模型]]
- [[匝间短路模型|匝间短路模型]]
- [[对地短路模型|对地短路模型]]


## 相关主题


- [[变压器内部故障|变压器内部故障]]
- [[继电保护验证|继电保护验证]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[漏磁参数辨识|漏磁参数辨识]]


## 主要发现


- 扩展矩阵模型可精确复现匝间及对地故障暂态波形，实验测量数据与仿真结果高度吻合
- 几何漏磁系数评估法在无需额外试验条件下，仍能保证故障短路电流计算的高精度
- 模型在正常工况下与原BCTRAN矩阵等效，故障时能准确表征漏抗突变对电流的影响



---
title: "Equivalent modeling of electromagnetic transient for MMC-HVDC based on semi-implicit delay model"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Zhao 等 - 2021 - Equivalent modeling of electromagnetic transient simulation for hybrid braking resistance converter;.pdf"]
---

# Equivalent modeling of electromagnetic transient for MMC-HVDC based on semi-implicit delay model

**作者**: 
**年份**: 2026
**来源**: `18/Zhao 等 - 2021 - Equivalent modeling of electromagnetic transient simulation for hybrid braking resistance converter;.pdf`

## 摘要

PSCAD／EMTDC 开展等效模型与原始模型的一致性仿真测试及仿真速度对比分析，结果表明所提方法能高 Project supported by the Science and Technology Project of the Headquarters of SGCC（The Research on Key Tech‐

## 核心贡献


- 提出基于戴维南等效与嵌套迭代的混合式制动电阻变换器电磁暂态等效建模方法
- 将数百个子模块按开关状态分类解耦，大幅降低全支路网络节点规模与计算复杂度
- 构建支路等效历史电压源与电阻串联模型，实现内外电气特性的高精度反推求解


## 使用的方法


- [[戴维南等效|戴维南等效]]
- [[嵌套迭代|嵌套迭代]]
- [[理想开关模型|理想开关模型]]
- [[梯形积分法|梯形积分法]]
- [[滞回比较触发|滞回比较触发]]


## 涉及的模型


- [[混合式制动电阻变换器|混合式制动电阻变换器]]
- [[子模块|子模块]]
- [[vsc-model|VSC]]
- [[集中制动电阻|集中制动电阻]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[等效建模|等效建模]]
- [[柔性直流送出系统|柔性直流送出系统]]
- [[功率盈余控制|功率盈余控制]]
- [[仿真加速|仿真加速]]


## 主要发现


- 等效模型能高度还原变换器外部运行特性及内部子模块电容电压变化特性
- 在满功率与半功率故障工况下，等效模型与原始模型仿真波形高度一致
- 该方法有效规避庞大节点网络求解，大幅缩短电磁暂态仿真计算时长



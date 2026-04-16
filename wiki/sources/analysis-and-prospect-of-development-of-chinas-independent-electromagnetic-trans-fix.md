---
title: "Analysis and Prospect of Development of China's Independent Electromagnetic Transient Simulation Platform"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Analysis and Prospect of Development of China's Independent Electromagnetic Transient Simulation Platformpdf.pdf"]
---

# Analysis and Prospect of Development of China's Independent Electromagnetic Transient Simulation Platform

**作者**: CNKI
**年份**: 2022
**来源**: `07&08/Analysis and Prospect of Development of China's Independent Electromagnetic Transient Simulation Platformpdf.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献


- 提出模块化电力电子装备一般化加速仿真框架，涵盖开关等效、子模块提速与级联算法
- 剖析国外平台模型匮乏与底层封闭痛点，指明国产平台底层开放与易用性优化方向
- 归纳并行计算与智能算法在仿真内核优化中的应用路径，为国产平台开发提供理论指导


## 使用的方法


- [[快速嵌套求解法|快速嵌套求解法]]
- [[半隐式延迟解耦|半隐式延迟解耦]]
- [[参数矩阵级联法|参数矩阵级联法]]
- [[二值电阻模型|二值电阻模型]]
- [[平均值模型|平均值模型]]
- [[并行计算|并行计算]]
- [[离散状态事件驱动|离散状态事件驱动]]
- [[节点导纳矩阵求逆|节点导纳矩阵求逆]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[pet|PET]]
- [[dccb|DCCB]]
- [[dc-fcl|DC-FCL]]
- [[dc-pfc|DC-PFC]]
- [[chb-dab|CHB-DAB]]
- [[h桥子模块|H桥子模块]]
- [[高频隔离变压器|高频隔离变压器]]
- [[igbt|IGBT]]


## 相关主题


- [[电磁暂态仿真平台|电磁暂态仿真平台]]
- [[仿真效率加速|仿真效率加速]]
- [[模块化电力电子建模|模块化电力电子建模]]
- [[实时仿真|实时仿真]]
- [[硬件在环|硬件在环]]
- [[并行计算优化|并行计算优化]]
- [[网络解耦等值|网络解耦等值]]
- [[国产化软件生态|国产化软件生态]]


## 主要发现


- 快速嵌套求解与参数矩阵级联法可大幅消减网络节点，实现数十倍仿真加速且保持高精度
- 国外平台底层封闭且模型更新滞后，难以满足大规模电力电子化电网的实时仿真需求
- 引入现代数学库与多线程并行技术可显著优化矩阵求逆效率，突破传统电磁暂态解算瓶颈



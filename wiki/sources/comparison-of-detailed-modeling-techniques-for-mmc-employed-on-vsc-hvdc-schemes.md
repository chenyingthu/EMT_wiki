---
title: "Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Transactions on Power Delivery;2015;30;2;10.1109/TPWRD.2014.2325065"
tags: ['mmc', 'vsc']
created: "2026-04-13"
sources: ["EMT_Doc/10/Beddard 等 - 2015 - Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes.pdf"]
---

# Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes

**作者**: 
**年份**: 2015
**来源**: `10/Beddard 等 - 2015 - Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes.pdf`

## 摘要

—Modular multilevel converters (MMC) are presently the converter topology of choice for voltage-source converter high-voltage direct-current (VSC-HVDC) transmission schemes due to their very high efﬁciency. These converters are complex, yet fast and detailed electromagnetic transients simulation models are necessary for the research and development of these transmis- sion schemes. Excellent work has been done in this area, though little objective comparison of the models proposed has yet been undertaken. This paper compares for the ﬁrst time, the three leading techniques for producing detailed MMC VSC-HVDC models in terms of their accuracy and simulation speed for sev- eral typical simulation cases. In addition, an improved model is proposed which further improves the computational efﬁcien

## 核心贡献


- 首次在同一平台客观对比TDM、DEM与AM三种MMC详细模型的精度与仿真速度
- 提出增强型加速模型EAM，通过优化网络划分进一步提升MMC电磁暂态仿真计算效率
- 基于对比实验结果，给出针对不同研究场景的MMC详细模型选型建议与适用指南


## 使用的方法


- [[传统详细建模-tdm|传统详细建模(TDM)]]
- [[详细等效建模-dem|详细等效建模(DEM)]]
- [[加速建模-am|加速建模(AM)]]
- [[嵌套快速同步求解-nfss|嵌套快速同步求解(NFSS)]]
- [[节点导纳矩阵求解|节点导纳矩阵求解]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[半桥子模块|半桥子模块]]
- [[桥臂电抗器|桥臂电抗器]]
- [[igbt-反并联二极管|IGBT/反并联二极管]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[仿真效率优化|仿真效率优化]]
- [[模型精度对比|模型精度对比]]
- [[电力电子详细建模|电力电子详细建模]]


## 主要发现


- DEM相比TDM大幅缩短仿真时间且精度无损，但无法观测子模块内部电气状态
- AM在保持组件可见性的同时显著提升计算效率，但特定工况下存在数值稳定性局限
- 提出的EAM进一步优化了AM的求解结构，在典型测试案例中实现仿真速度再提升



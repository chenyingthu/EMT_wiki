---
title: "Full-wave black-box transmission line tower model for the assessment of lightning backflashover"
type: source
authors: ['Bamdad Salarieh']
year: 2021
journal: "Electric Power Systems Research, 199 (2021) 107399. doi:10.1016/j.epsr.2021.107399"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/j.epsr.2021.107399.pdf.pdf"]
---

# Full-wave black-box transmission line tower model for the assessment of lightning backflashover

**作者**: Bamdad Salarieh
**年份**: 2021
**来源**: `19、20、21/EMT_task_20/j.epsr.2021.107399.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Full-wave black-box transmission line tower model for the assessment of Department of Electrical & Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada In order to calculate the overvoltages across the insulator strings of overhead lines, electromagnetic transient (EMT)-type simulators require a model of the tower and its grounding system. In this paper, an electromagnetic

## 核心贡献


- 基于全波频域麦克斯韦方程建立杆塔电磁场模型，生成EMT兼容黑盒等效模型
- 采用矢量拟合将频域多端口网络转化为状态空间FDNE模型，直接接入时域仿真
- 综合考虑杆塔精细几何结构与接地极，并精确计及土壤参数的频率依赖性


## 使用的方法


- [[有限元法-fem|有限元法(FEM)]]
- [[全波频域麦克斯韦方程求解|全波频域麦克斯韦方程求解]]
- [[vector-fitting|矢量拟合]]
- [[多端口网络建模|多端口网络建模]]
- [[fdne-model|FDNE]]
- [[诺顿等效与卷积算子|诺顿等效与卷积算子]]


## 涉及的模型


- [[400kv双回输电杆塔|400kV双回输电杆塔]]
- [[接地系统-水平接地极|接地系统(水平接地极)]]
- [[避雷线与相导线|避雷线与相导线]]
- [[绝缘子串|绝缘子串]]
- [[fdne-model|FDNE]]


## 相关主题


- [[雷击反击闪络评估|雷击反击闪络评估]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关土壤建模|频率相关土壤建模]]
- [[网络等值|网络等值]]
- [[防雷保护|防雷保护]]
- [[暂态过电压分析|暂态过电压分析]]


## 主要发现


- 黑盒模型能精确计算绝缘子串暂态过电压，显著优于IEEE与CIGRE简化模型
- 计及土壤频率特性可大幅提升接地系统暂态响应与反击闪络率计算精度
- 结合DE与LP闪络模型的概率分析，可准确评估不同土壤条件下的反击闪络率



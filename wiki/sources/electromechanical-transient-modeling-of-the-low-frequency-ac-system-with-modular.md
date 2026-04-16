---
title: "Electromechanical Transient Modeling of the Low-Frequency AC System With Modular Multilevel Matrix Converter Stations"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2024;39;1;10.1109/TPWRS.2023.3236819"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/17/Yu 等 - 2024 - Electromechanical Transient Modeling of the Low-Frequency AC System with Modular Multilevel Matrix C.pdf"]
---

# Electromechanical Transient Modeling of the Low-Frequency AC System With Modular Multilevel Matrix Converter Stations

**作者**: 
**年份**: 2023
**来源**: `17/Yu 等 - 2024 - Electromechanical Transient Modeling of the Low-Frequency AC System with Modular Multilevel Matrix C.pdf`

## 摘要

—This paper studies the electromechanical transient modeling of a low-frequency AC (LFAC) system with modular multilevel matrix converter (M3C) stations. Firstly, the mathemat- ical model of the M3C and its equivalent circuits are established. Then, an iterative power ﬂow calculation algorithm for AC systems integrated with the M3C-LFAC system is developed. The dynamic model of the M3C for electromechanical transient simulation is studied and implemented in PSS/E. Based on a test system consist- ingoftwoasynchronousACsystemswithanembeddedM3C-LFAC system, comparisons between the electromechanical transient sim- ulation results from PSS/E and the electromagnetic transient simu- lation results from PSCAD are conducted. The results from PSS/E and PSCAD coincide with each other well, and the va

## 核心贡献


- 提出含M3C-LFAC系统的迭代潮流算法，适用于工频与低频混合电网
- 建立适用于机电暂态仿真的M3C动态模型，并在PSS/E中实现自定义建模
- 构建含虚拟同步机控制的M3C机电动态模型，支持去中心化控制仿真


## 使用的方法


- [[迭代潮流计算|迭代潮流计算]]
- [[机电暂态建模|机电暂态建模]]
- [[正序基波相量法|正序基波相量法]]
- [[用户自定义模型|用户自定义模型]]
- [[虚拟同步机控制|虚拟同步机控制]]


## 涉及的模型


- [[m3c|M3C]]
- [[低频交流系统|低频交流系统]]
- [[换流变压器|换流变压器]]
- [[新英格兰39节点系统|新英格兰39节点系统]]
- [[虚拟同步机|虚拟同步机]]


## 相关主题


- [[机电暂态建模|机电暂态建模]]
- [[低频交流输电|低频交流输电]]
- [[混合系统潮流计算|混合系统潮流计算]]
- [[电力系统稳定性|电力系统稳定性]]
- [[电磁与机电暂态对比|电磁与机电暂态对比]]


## 主要发现


- PSS/E机电暂态仿真与PSCAD电磁暂态结果高度吻合，验证模型精度
- 仿真验证了M3C-LFAC系统在多机系统中的暂态响应特性与控制有效性
- 所提机电模型在去中心化控制下能准确复现M3C的功率与频率动态过程



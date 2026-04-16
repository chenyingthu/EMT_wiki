---
title: "Analysis and Mitigation of Subsynchronous Resonance in Series-Compensated Wind Power Systems"
type: source
authors: ['Grain', 'Philip', 'Adam']
year: 2014
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/JESTPE.2014.2315833.pdf.pdf"]
---

# Analysis and Mitigation of Subsynchronous Resonance in Series-Compensated Wind Power Systems

**作者**: Grain, Philip, Adam
**年份**: 2014
**来源**: `19、20、21/EMT_task_21/JESTPE.2014.2315833.pdf.pdf`

## 摘要

—This paper presents an improved electromagnetic transient (EMT) simulation models for the half and full-bridge modular multilevel converters that can be used for full-scale simulation of multilevel high-voltage dc transmission systems, with hundreds of cells per arm. The presented models employ minimum software overhead within their electromagnetic transient parts to correctly represent modular multilevel converters (MMC)

## 核心贡献


- 提出半桥全桥MMC改进型EMT模型，降低开销并准确复现器件闭锁工况
- 基于戴维南等效与两态电阻简化桥臂，保留调制与电容均压控制细节
- 实现含两百余子模块的全规模直流系统仿真，支持交直流故障动态分析


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[戴维南等效电路|戴维南等效电路]]
- [[两态电阻模型|两态电阻模型]]
- [[广义电路理论|广义电路理论]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥-全桥子模块|半桥/全桥子模块]]
- [[vsc-model|VSC]]
- [[多端直流电网|多端直流电网]]
- [[桥臂电抗器|桥臂电抗器]]


## 相关主题


- [[全规模仿真|全规模仿真]]
- [[直流故障穿越|直流故障穿越]]
- [[换流器闭锁特性|换流器闭锁特性]]
- [[环流抑制|环流抑制]]
- [[vsc-hvdc|VSC-HVDC]]


## 主要发现


- 故障下模型可自然生成直流分量与环流，准确复现交直流侧功率动态
- 闭锁工况计算开销极低，精确捕捉电容电压与桥臂电流微观暂态过程
- 全规模闭环仿真验证了模型在正常运行及各类故障工况下的高精度特性



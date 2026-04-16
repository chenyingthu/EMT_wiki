---
title: "Modeling of inductive constant power load for electromagnetic-transient simulations–Part II"
type: source
authors: ['Kamel Alboaouh']
year: 2025
journal: "Electric Power Systems Research, 242 (2025) 111415. doi:10.1016/j.epsr.2025.111415"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Alboaouh 等 - 2025 - Modeling of inductive constant power load for electromagnetic-transient simulations–Part II.pdf"]
---

# Modeling of inductive constant power load for electromagnetic-transient simulations–Part II

**作者**: Kamel Alboaouh
**年份**: 2025
**来源**: `26/Alboaouh 等 - 2025 - Modeling of inductive constant power load for electromagnetic-transient simulations–Part II.pdf`

## 摘要

Modeling of inductive constant power load for electromagnetic-transient a Dept.of Eng.Tech, Norfolk State Univ., 700 Park Ave,RTC Building,Suite 420M, Norfolk VA 23501, USA b Power Syst.Eng.Center, Nat.Renewable Energy Lab., Golden CO, USA c Power Syst.Eng.Center, Nat. Renewable Energy Lab., Golden CO,USA This paper improves the dynamic constant power (CP) load model that was published in Part I, which is

## 核心贡献


- 提出逐时间步求解的恒功率负载模型，克服原模型需整周期计算的求解器集成障碍。
- 引入虚拟变量实现RMS量递归更新，使模型严格适配EMT仿真器的步进计算机制。
- 保留感性负载固定功率与功率因数约束，同时兼容正弦与非正弦电网运行工况。


## 使用的方法


- [[数值建模|数值建模]]
- [[逐时间步求解|逐时间步求解]]
- [[基尔霍夫定律|基尔霍夫定律]]
- [[递归rms量计算|递归RMS量计算]]
- [[恒阻抗负载合成验证|恒阻抗负载合成验证]]


## 涉及的模型


- [[恒功率负载|恒功率负载]]
- [[恒阻抗负载|恒阻抗负载]]
- [[感性rl电路|感性RL电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[负荷建模|负荷建模]]
- [[恒功率负载|恒功率负载]]
- [[数值求解器集成|数值求解器集成]]
- [[固定功率因数|固定功率因数]]


## 主要发现


- 仿真验证表明模型可无缝嵌入EMT数值求解器，实现单步迭代且计算逻辑稳定。
- 在正弦与非正弦工况下，模型均能精确维持预设的有功功率消耗与固定功率因数。
- 与恒阻抗负载合成数据对比结果高度吻合，证实了模型在动态暂态过程中的准确性。



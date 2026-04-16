---
title: "Modeling of inductive constant power load for electromagnetic-transient simulations–Part II"
type: source
authors: ['Kamel Alboaouh']
year: 2025
journal: "Electric Power Systems Research, 242 (2025) 111415. doi:10.1016/j.epsr.2025.111415"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modeling of inductive constant power load for electromagnetic-transient simulations–Part II.pdf"]
---

# Modeling of inductive constant power load for electromagnetic-transient simulations–Part II

**作者**: Kamel Alboaouh
**年份**: 2025
**来源**: `27&28/Modeling of inductive constant power load for electromagnetic-transient simulations–Part II.pdf`

## 摘要

Modeling of inductive constant power load for electromagnetic-transient a Dept.of Eng.Tech, Norfolk State Univ., 700 Park Ave,RTC Building,Suite 420M, Norfolk VA 23501, USA b Power Syst.Eng.Center, Nat.Renewable Energy Lab., Golden CO, USA c Power Syst.Eng.Center, Nat. Renewable Energy Lab., Golden CO,USA This paper improves the dynamic constant power (CP) load model that was published in Part I, which is

## 核心贡献


- 将恒功率负载模型由全周期求解改进为逐时间步序贯计算，实现与EMT求解器无缝集成
- 构建保持固定功率因数与恒定功率的时变动态模型，兼容正弦与非正弦电网工况


## 使用的方法


- [[基尔霍夫定律|基尔霍夫定律]]
- [[逐时间步数值积分|逐时间步数值积分]]
- [[有效值递推分解|有效值递推分解]]
- [[动态负载建模|动态负载建模]]


## 涉及的模型


- [[恒功率负载|恒功率负载]]
- [[恒阻抗负载|恒阻抗负载]]
- [[rl串联电路|RL串联电路]]
- [[时变动态负载模型|时变动态负载模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[负载建模|负载建模]]
- [[恒功率负载|恒功率负载]]
- [[非正弦工况分析|非正弦工况分析]]
- [[数值求解器集成|数值求解器集成]]


## 主要发现


- 改进模型成功实现逐时间步求解，与EMT数值求解器兼容且计算流程完全适配
- 在正弦与非正弦工况下均能严格维持恒定有功无功功率及固定功率因数特性
- 与恒阻抗负载合成数据对比验证表明，该模型动态响应准确且仿真结果高度吻合



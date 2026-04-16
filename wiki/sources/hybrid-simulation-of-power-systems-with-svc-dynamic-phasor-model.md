---
title: "Hybrid simulation of power systems with SVC dynamic phasor model"
type: source
authors: ['"E Zhijun', 'D.Z. Fang', 'K.W. Chan', 'S.Q. Yuan"']
year: 2009
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/22/Zhijun 等 - 2009 - Hybrid simulation of power systems with SVC dynamic phasor model.pdf"]
---

# Hybrid simulation of power systems with SVC dynamic phasor model

**作者**: "E Zhijun, D.Z. Fang, K.W. Chan 等
**年份**: 2009
**来源**: `22/Zhijun 等 - 2009 - Hybrid simulation of power systems with SVC dynamic phasor model.pdf`

## 摘要

Hybrid simulation of power systems with SVC dynamic phasor model E Zhijun a, D.Z. Fang a,*, K.W. Chan b, S.Q. Yuan a,b a Key Laboratory of Power System Simulation and Control of Ministry of Education of China, Tianjin University, 300072 Tianjin, China b Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong, China A novel hybrid method for simulation of power systems equipped with static var compensators (SVC) is

## 核心贡献


- 提出SVC单相动态相量模型，设计其与机电暂态子系统的混合仿真接口算法
- 采用较大积分步长求解动态相量方程，显著提升含SVC大电网的混合仿真速度
- 建立仅含基波与五次谐波的TCR动态相量模型，兼顾波形精度与计算效率


## 使用的方法


- [[动态相量法|动态相量法]]
- [[混合仿真|混合仿真]]
- [[接口算法|接口算法]]
- [[单相等效建模|单相等效建模]]
- [[状态空间平均法|状态空间平均法]]


## 涉及的模型


- [[svc|SVC]]
- [[tcr|TCR]]
- [[交流子系统|交流子系统]]
- [[rlc滤波器|RLC滤波器]]
- [[机电暂态模型|机电暂态模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[动态相量建模|动态相量建模]]
- [[机电-电磁暂态混合|机电-电磁暂态混合]]
- [[facts设备仿真|FACTS设备仿真]]
- [[大电网动态仿真|大电网动态仿真]]


## 主要发现


- 9节点与39节点系统测试表明，SVC动态相量模型波形精度与EMTP基准高度一致
- 较大积分步长下的动态相量仿真在保证精度的同时，大幅降低混合仿真计算耗时
- 忽略五次以上谐波的简化模型仍能准确反映SVC非线性动态特性，验证了方法有效性



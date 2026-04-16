---
title: "Hybrid simulation of power systems with SVC dynamic phasor model"
type: source
authors: ['"E Zhijun', 'D.Z. Fang', 'K.W. Chan', 'S.Q. Yuan"']
year: 2009
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/22/j.ijepes.2009.01.002.pdf.pdf"]
---

# Hybrid simulation of power systems with SVC dynamic phasor model

**作者**: "E Zhijun, D.Z. Fang, K.W. Chan 等
**年份**: 2009
**来源**: `22/j.ijepes.2009.01.002.pdf.pdf`

## 摘要

Hybrid simulation of power systems with SVC dynamic phasor model E Zhijun a, D.Z. Fang a,*, K.W. Chan b, S.Q. Yuan a,b a Key Laboratory of Power System Simulation and Control of Ministry of Education of China, Tianjin University, 300072 Tianjin, China b Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong, China A novel hybrid method for simulation of power systems equipped with static var compensators (SVC) is

## 核心贡献


- 推导仅含基波与五次谐波的SVC单相动态相量模型，实现非线性开关器件高效表征。
- 提出动态相量子系统与机电暂态子系统接口算法，有效抑制传统混合仿真相位突变。
- 构建新型混合仿真架构，采用较大积分步长替代全电磁暂态仿真，大幅提升计算效率。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[混合仿真|混合仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[时变傅里叶级数展开|时变傅里叶级数展开]]
- [[接口算法|接口算法]]


## 涉及的模型


- [[svc|SVC]]
- [[tcr|TCR]]
- [[交流机电暂态模型|交流机电暂态模型]]
- [[rlc滤波器|RLC滤波器]]
- [[9节点测试系统|9节点测试系统]]
- [[new-england-39节点系统|New England 39节点系统]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[动态相量建模|动态相量建模]]
- [[暂态稳定分析|暂态稳定分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[facts设备建模|FACTS设备建模]]
- [[谐波分析|谐波分析]]


## 主要发现


- 9节点与39节点测试表明，单相SVC动态相量模型精度与全电磁暂态模型高度一致。
- 相比传统EMTP，新方法采用较大积分步长，在保证波形精度的同时显著提升计算速度。
- 接口算法有效消除子系统交互时的相位不连续与直流偏移，验证了混合仿真框架有效性。



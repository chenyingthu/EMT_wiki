---
title: "Assessment of dynamic phasor extraction methods for power system co-simulation applications"
type: source
authors: ['Janesh Rupasinghe']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107319. doi:10.1016/j.epsr.2021.107319"
tags: ['cosimulation', 'dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/09/Rupasinghe 等 - 2021 - Assessment of dynamic phasor extraction methods for power system co-simulation applications.pdf"]
---

# Assessment of dynamic phasor extraction methods for power system co-simulation applications

**作者**: Janesh Rupasinghe
**年份**: 2021
**来源**: `09/Rupasinghe 等 - 2021 - Assessment of dynamic phasor extraction methods for power system co-simulation applications.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Assessment of dynamic phasor extraction methods for power system Janesh Rupasinghe a, Shaahin Filizadeh *,a, Kai Strunz b a Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Canada The paper examines a number of methods for extracting dynamic phasors from samples of natural waveforms

## 核心贡献


- 系统评估多种动态相量提取方法的理论基础与数值实现流程
- 深入分析含振荡、直流、谐波及不平衡信号下提取相量的特性与局限
- 构建EMT-动态相量联合仿真算例，验证不同提取方法的适用性


## 使用的方法


- [[动态相量提取|动态相量提取]]
- [[广义平均法|广义平均法]]
- [[移频分析法|移频分析法]]
- [[快速时变相量变换|快速时变相量变换]]


## 涉及的模型


- [[三相交流线性电路模型|三相交流线性电路模型]]
- [[动态相量数学模型|动态相量数学模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[联合仿真|联合仿真]]
- [[动态相量提取|动态相量提取]]
- [[谐波分析|谐波分析]]
- [[频域建模|频域建模]]


## 主要发现


- 广义平均法可灵活选择谐波分量，但多谐波计算时计算负担显著增加
- 快速时变相量法仅适用于平衡三相系统，处理零序分量时复杂度剧增
- 不同提取方法在应对直流偏置与任意暂态时表现出显著的频谱精度差异



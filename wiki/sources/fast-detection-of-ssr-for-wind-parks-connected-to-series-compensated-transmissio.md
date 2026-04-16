---
title: "Fast Detection of SSR for Wind Parks Connected to Series-Compensated Transmission Systems"
type: source
authors: ['Younes Seyedi']
year: 2022
journal: "Electric Power Systems Research, 211 (2022) 108321. doi:10.1016/j.epsr.2022.108321"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Seyedi 等 - 2022 - Fast Detection of SSR for Wind Parks Connected to Series-Compensated Transmission Systems.pdf"]
---

# Fast Detection of SSR for Wind Parks Connected to Series-Compensated Transmission Systems

**作者**: Younes Seyedi
**年份**: 2022
**来源**: `18/Seyedi 等 - 2022 - Fast Detection of SSR for Wind Parks Connected to Series-Compensated Transmission Systems.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Fast Detection of SSR for Wind Parks Connected to Series-Compensated Younes Seyedi a,*, Jean Mahseredjian a, Houshang Karimi a, Ulas Karaagac c, a Department of Electrical Engineering, Polytechnique Montreal, QC Canada c Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong

## 核心贡献


- 提出扰动与扫描方法，利用小扰动激发模态并结合频谱分析快速定位SSR候选频段
- 设计选择性阻抗扫描策略，仅在峰值频段评估稳定性判据，大幅降低EMT仿真计算量
- 构建自动化SSR检测流程，支持电网拓扑变化下的自适应风险评估与保护策略优化


## 使用的方法


- [[时域电磁暂态仿真|时域电磁暂态仿真]]
- [[频谱分析|频谱分析]]
- [[正序阻抗扫描|正序阻抗扫描]]
- [[小扰动注入|小扰动注入]]
- [[选择性频段扫描|选择性频段扫描]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[全功率变流器风机|全功率变流器风机]]
- [[串联补偿输电线路|串联补偿输电线路]]
- [[风电场|风电场]]
- [[电网正序阻抗模型|电网正序阻抗模型]]


## 相关主题


- [[次同步谐振检测|次同步谐振检测]]
- [[串补输电系统|串补输电系统]]
- [[风电并网稳定性|风电并网稳定性]]
- [[阻抗频率扫描|阻抗频率扫描]]
- [[控制交互作用|控制交互作用]]


## 主要发现


- 仅需少量EMT仿真即可准确识别SSR工况，显著缩短检测时间并降低计算负担
- 在III型和IV型风机系统中验证有效，能精准区分阻尼振荡与无阻尼失稳振荡
- 结合阻抗扫描与稳定性判据，可自适应评估网络拓扑变化下的次同步谐振风险



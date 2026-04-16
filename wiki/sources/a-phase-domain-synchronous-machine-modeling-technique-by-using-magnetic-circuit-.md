---
title: "A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings"
type: source
authors: ['R. Yonezawa']
year: 2023
journal: "Electric Power Systems Research, 219 (2023) 109248. doi:10.1016/j.epsr.2023.109248"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/03/Yonezawa - 2023 - A phase-domain synchronous machine modeling technique by using magnetic circuit representation of ar.pdf"]
---

# A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings

**作者**: R. Yonezawa
**年份**: 2023
**来源**: `03/Yonezawa - 2023 - A phase-domain synchronous machine modeling technique by using magnetic circuit representation of ar.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings Grid and Communication Technology Division, Grid Innovation Research Laboratory, CRIEPI (Central Research Institute of Electric Power Industry), 2-6-1, Nagasaka, A phase-domain synchronous machine modeling technique by using only basic circuit components and applying

## 核心贡献


- 提出基于磁路表示的相域同步电机建模技术，仅用基本电路元件构建，免改源码
- 支持用户自由编辑模型结构，可精确模拟空间谐波、三相不平衡及内部故障工况
- 实现磁路与外部电网电路的直接耦合求解，显著提升相域模型的数值稳定性与精度


## 使用的方法


- [[磁路建模|磁路建模]]
- [[相域建模|相域建模]]
- [[电-磁电路耦合求解|电-磁电路耦合求解]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[电枢绕组|电枢绕组]]
- [[励磁绕组|励磁绕组]]
- [[阻尼绕组|阻尼绕组]]
- [[变压器|变压器]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[空间谐波分析|空间谐波分析]]
- [[三相不平衡建模|三相不平衡建模]]
- [[内部故障仿真|内部故障仿真]]
- [[相域建模|相域建模]]


## 主要发现


- 在无穷大系统三相接地故障仿真中，所提模型与常规派克模型动态响应高度一致
- 模型无需dq0变换即可准确复现同步电机电气与机械暂态行为，数值稳定性优异
- 验证了磁路表示法在模拟空间谐波及三相不平衡工况下的有效性与高精度



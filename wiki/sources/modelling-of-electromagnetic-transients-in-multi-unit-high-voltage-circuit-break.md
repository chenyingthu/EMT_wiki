---
title: "Modelling of electromagnetic transients in multi-unit high-voltage circuit-breakers"
type: source
authors: ['Antoine Mailhot']
year: 2024
journal: "Electric Power Systems Research, 235 (2024) 110766. doi:10.1016/j.epsr.2024.110766"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modelling of electromagnetic transients in multi-unit high-voltage circuit-breaker.pdf"]
---

# Modelling of electromagnetic transients in multi-unit high-voltage circuit-breakers

**作者**: Antoine Mailhot
**年份**: 2024
**来源**: `27&28/Modelling of electromagnetic transients in multi-unit high-voltage circuit-breaker.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Modelling of electromagnetic transients in multi-unit high-voltage Antoine Mailhot a,*, Ryszard Pater a, S´ebastien Poirier a, Jean Mahseredjian b, Ren´e Doche c a Institut de recherche d’Hydro-Qu´ebec (IREQ), Varennes, Canada High-voltage (HV) circuit-breakers (CBs) often consist of several making and breaking units (MBUs) in series. A

## 核心贡献


- 提出多断口高压断路器EMTP模型，集成开断介质恢复与关合击穿下降曲线
- 采用集中参数耦合各断口，精确模拟机械不同步引发的高频暂态过程
- 模型适配真空与SF6介质，可复现传统模型难以模拟的多次重燃现象


## 使用的方法


- [[emtp仿真|EMTP仿真]]
- [[集中参数建模|集中参数建模]]
- [[开关逻辑控制|开关逻辑控制]]
- [[击穿电压包络线法|击穿电压包络线法]]
- [[帕邢定律近似|帕邢定律近似]]


## 涉及的模型


- [[多断口高压断路器|多断口高压断路器]]
- [[合分闸单元-mbu|合分闸单元(MBU)]]
- [[均压电容|均压电容]]
- [[真空断路器-vcb|真空断路器(VCB)]]
- [[sf6断路器|SF6断路器]]
- [[电弧阻抗模型|电弧阻抗模型]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[开关暂态|开关暂态]]
- [[断路器建模|断路器建模]]
- [[预击穿与重燃|预击穿与重燃]]
- [[介质恢复特性|介质恢复特性]]
- [[高频暂态分析|高频暂态分析]]


## 主要发现


- 标准允许的最大断口不同步度会引发开断多次重燃或关合严重过电压
- 单断口预击穿导致均压电容电荷积累，造成断口间电压分布瞬时失衡
- 真空快速熄弧特性易在多断口结构中诱发连续重燃，增加高压设计难度



---
title: "Measurement-based frequency-dependent model of a HVDC transformer for electromagnetic transient studies"
type: source
authors: ['Bjørn Gustavsen']
year: 2019
journal: "Electric Power Systems Research, 180 (2020) 106141. doi:10.1016/j.epsr.2019.106141"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/26/Gustavsen和Vernay - 2020 - Measurement-based frequency-dependent model of a HVDC transformer for electromagnetic transient stud.pdf"]
---

# Measurement-based frequency-dependent model of a HVDC transformer for electromagnetic transient studies

**作者**: Bjørn Gustavsen
**年份**: 2019
**来源**: `26/Gustavsen和Vernay - 2020 - Measurement-based frequency-dependent model of a HVDC transformer for electromagnetic transient stud.pdf`

## 摘要

Measurement-based frequency-dependent model of a HVDC transformer for SINTEF Energy Research, P.O. Box 4761 Sluppen, Trondheim, NO-7465, Norway A wide-band, frequency-dependent ﬁve-terminal model is developed that represents one HVDC transformer unit in the French-English IFA2000 HVDC interconnection. Three such interconnected 1-ph units constitute one 3-ph transformer bank needed in 12-pulse conversion. The model is obtained via admittance frequency sweep

## 核心贡献


- 提出特征值缩放新方法，修正小信号测量导致的50Hz励磁电流失真问题。
- 引入模态揭示变换保留小特征值精度，实现含高阻抗接地耦合的宽频建模。
- 首次基于终端导纳扫频构建无源稳定有理模型，用于HVDC变压器EMT仿真。


## 使用的方法


- [[导纳扫频测量|导纳扫频测量]]
- [[特征值缩放|特征值缩放]]
- [[模态揭示变换|模态揭示变换]]
- [[矢量拟合|矢量拟合]]
- [[黑盒建模|黑盒建模]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[五端宽频模型|五端宽频模型]]
- [[lcc-model|LCC]]
- [[经典集总参数模型|经典集总参数模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[绝缘配合研究|绝缘配合研究]]
- [[宽频黑盒建模|宽频黑盒建模]]
- [[换相过电压分析|换相过电压分析]]


## 主要发现


- 修正后的模型在5Hz至10MHz频段内导纳矩阵与实测高度吻合，且严格满足无源性。
- 时域阶跃响应仿真与实测波形一致，验证了模型在宽频范围内的动态准确性。
- 完整HVDC链路仿真表明，该模型能更精确捕捉换相过电压波形，优于传统简化模型。



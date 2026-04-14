---
title: "Surge and energization tests and modeling on a 225kV HVAC cable"
type: source
authors: ['Isabel Lafaia']
year: 2018
journal: "Electric Power Systems Research, 160 (2018) 273-281. doi:10.1016/j.epsr.2018.03.003"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/j.epsr.2018.03.003.pdf.pdf"]
---

# Surge and energization tests and modeling on a 225kV HVAC cable

**作者**: Isabel Lafaia
**年份**: 2018
**来源**: `37/j.epsr.2018.03.003.pdf.pdf`

## 摘要

1. Introduction we can excite each propagation mode separately and observe the respective cable responses, which is useful for model validation. In Projects of new cable installations have taken place worldwide the energization test, the full 64 km long cable was connected to in the last few year...

## 核心贡献

- 提供了225kV长距离XLPE地下电缆（64km，交叉互联护套）的浪涌与投切实验现场测试数据
- 在EMTP中对比了详细分段模型与全长均匀等效简化模型的仿真表现
- 验证了简化电缆模型在特定应用场景下的有效性与工程实用性

## 使用的方法

- [[现场浪涌测试-surge-tests|现场浪涌测试（Surge tests）]]
- [[现场投切测试-energization-tests|现场投切测试（Energization tests）]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]
- [[详细分段建模与均匀等效简化建模对比分析|详细分段建模与均匀等效简化建模对比分析]]

## 涉及的模型

- [[225-kv-xlpe地下交流电缆-含交叉互联护套|225 kV XLPE地下交流电缆（含交叉互联护套）]]
- [[电网变压器|电网变压器]]
- [[无功补偿装置|无功补偿装置]]
- [[emtp电缆详细模型-各小段独立建模|EMTP电缆详细模型（各小段独立建模）]]
- [[emtp电缆简化模型-全长均匀等效|EMTP电缆简化模型（全长均匀等效）]]

## 相关主题

- [[电磁暂态-emt|电磁暂态（EMT）]]
- [[地下电缆建模与测试|地下电缆建模与测试]]
- [[电缆投切与浪涌过电压|电缆投切与浪涌过电压]]
- [[交叉互联接地系统|交叉互联接地系统]]
- [[emtp仿真验证|EMTP仿真验证]]

## 主要发现

- 浪涌测试能有效激发不同的传播模式并观测电缆响应，为模型验证提供了有效手段
- 投切测试的瞬态测量结果清晰反映了系统中变压器和无功补偿装置对暂态过程的影响
- 当仿真仅关注芯线导体的电压和电流时，使用全长均匀等效的简化电缆模型不会降低仿真精度

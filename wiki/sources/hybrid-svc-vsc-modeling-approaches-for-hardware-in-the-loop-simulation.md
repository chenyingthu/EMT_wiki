---
title: "Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation"
type: source
authors: ['P. Le-Huy']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109651. doi:10.1016/j.epsr.2023.109651"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/22/Le-Huy和Tremblay - 2023 - Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation-1.pdf"]
---

# Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation

**作者**: P. Le-Huy
**年份**: 2023
**来源**: `22/Le-Huy和Tremblay - 2023 - Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation-1.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation Power System Simulation group at IREQ, Hydro-Qu´ebec’s research center, 1800 boul. Lionel-Boulet, Varennes, Qu´ebec, J3 × 1S1, Canada Hydro-Qu´ebec built two static var compensators at the 735-kV La Verendrye substation in 1985. Each has a capacity of +330/-110 Mvar t

## 核心贡献


- 提出混合SVC-VSC系统的两种硬件在环建模方法并开展对比验证
- 证明合理配置MMCsim接口与等效电压模型时，常规EMT仿真精度可媲美小步长方法
- 为老旧SVC改造为混合拓扑的实时控制保护测试提供完整工程验证方案


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[小步长仿真|小步长仿真]]
- [[常规大步长仿真|常规大步长仿真]]
- [[等效电压源建模|等效电压源建模]]
- [[硬件在环仿真|硬件在环仿真]]


## 涉及的模型


- [[svc|SVC]]
- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[tsc|TSC]]
- [[耦合变压器|耦合变压器]]
- [[控制保护系统|控制保护系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[混合无功补偿|混合无功补偿]]
- [[svc改造|SVC改造]]
- [[控制保护测试|控制保护测试]]
- [[仿真步长对比|仿真步长对比]]


## 主要发现


- 常规大步长与小步长EMT仿真在精确处理MMC等效接口时波形与动态响应高度一致
- 小步长非HIL唯一方案，常规大步长配合等效建模完全满足SVC改造控制测试需求
- MMCsim接口通过等效电压与桥臂电流交互，实现全桥MMC电容电压实时闭环



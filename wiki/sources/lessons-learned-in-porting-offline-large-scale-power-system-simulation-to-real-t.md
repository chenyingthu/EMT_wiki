---
title: "Lessons learned in porting offline large-scale power system simulation to real-time for wide-area monitoring, protection and control"
type: source
authors: ['P. Le-Huy']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109663. doi:10.1016/j.epsr.2023.109663"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/25/Le-Huy 等 - 2023 - Lessons learned in porting offline large-scale power system simulation to real-time for wide-area mo.pdf"]
---

# Lessons learned in porting offline large-scale power system simulation to real-time for wide-area monitoring, protection and control

**作者**: P. Le-Huy
**年份**: 2023
**来源**: `25/Le-Huy 等 - 2023 - Lessons learned in porting offline large-scale power system simulation to real-time for wide-area mo.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Lessons learned in porting offline large-scale power system simulation to real-time for wide-area monitoring, protection and control Power System Simulation Group, IREQ, Hydro-Qu´ebec’s Research Center, 1800 boul. Lionel-Boulet, Varennes, Qu´ebec J3 × 1S1, Canada At Hydro-Qu´ebec, power system studies are mainly done with offline electro

## 核心贡献


- 提出离线EMT仿真向实时环境移植的系统性经验与最佳实践指南。
- 开发模型兼容层与统一GUI接口，实现EMTP至HYPERSIM的自动化网表转换。
- 总结系统初始化与控制建模技巧，保障大规模电网实时仿真精度与稳定性。


## 使用的方法


- [[离线至实时仿真移植|离线至实时仿真移植]]
- [[模型兼容层映射|模型兼容层映射]]
- [[网表自动导入导出|网表自动导入导出]]
- [[硬件在环联合仿真|硬件在环联合仿真]]
- [[数值阻尼优化|数值阻尼优化]]


## 涉及的模型


- [[大规模电力系统|大规模电力系统]]
- [[vsc-hvdc|VSC-HVDC]]
- [[无功补偿装置|无功补偿装置]]
- [[继电保护与控制设备|继电保护与控制设备]]
- [[用户自定义代码模型|用户自定义代码模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[离线仿真移植|离线仿真移植]]
- [[广域监测保护与控制|广域监测保护与控制]]
- [[硬件在环仿真|硬件在环仿真]]
- [[电磁暂态建模|电磁暂态建模]]
- [[模型兼容性|模型兼容性]]


## 主要发现


- 离线与实时工具结果差异源于模型参数或数值阻尼设置不同，需精细校准。
- 离线仿真中的稳态加速初始化技巧在实时环境中易引发长期数值不稳定问题。
- 模型兼容层与统一GUI接口显著降低大规模电网移植人工成本并提升可读性。



---
title: "Co-simulation applied to power systems with high penetration of distributed energy resources"
type: source
authors: ['Igor', 'Borges', 'de', 'Oliveira', 'Chagas']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108413. doi:10.1016/j.epsr.2022.108413"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Chagas和Tomim - 2022 - Co-simulation applied to power systems with high penetration of distributed energy resources.pdf"]
---

# Co-simulation applied to power systems with high penetration of distributed energy resources

**作者**: Igor, Borges, de 等
**年份**: 2022
**来源**: `10/Chagas和Tomim - 2022 - Co-simulation applied to power systems with high penetration of distributed energy resources.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Co-simulation applied to power systems with high penetration of distributed Igor Borges de Oliveira Chagas ∗, Marcelo Aroca Tomim Department of Electrical Energy, Federal University of Juiz de Fora (UFJF), MG, Brazil Although co-simulation in power systems has not been widely explored yet, it has been shown to be

## 核心贡献


- 提出基于虚构传输线的联合仿真接口，实现异质子系统的解耦与历史项数据交互
- 建立基于离散系统数值稳定性的虚构线路参数选取准则，保障仿真收敛性
- 开发基于Python的FMI主算法，实现OpenModelica与OpenDSS跨平台协同


## 使用的方法


- [[联合仿真|联合仿真]]
- [[功能模型接口-fmi|功能模型接口(FMI)]]
- [[虚构传输线法|虚构传输线法]]
- [[transmission-line-model|Bergeron线路模型]]
- [[行波理论|行波理论]]
- [[正序建模|正序建模]]
- [[相域建模|相域建模]]
- [[sundials-cvode求解器|SUNDIALS CVODE求解器]]
- [[主算法同步|主算法同步]]


## 涉及的模型


- [[输电网-11节点|输电网(11节点)]]
- [[配电网-38节点-ieee-34节点|配电网(38节点/IEEE 34节点)]]
- [[分布式能源-der|分布式能源(DER)]]
- [[静态电源与负荷|静态电源与负荷]]
- [[功能模型单元-fmu|功能模型单元(FMU)]]


## 相关主题


- [[联合仿真|联合仿真]]
- [[高渗透率分布式能源|高渗透率分布式能源]]
- [[跨平台仿真|跨平台仿真]]
- [[动态仿真|动态仿真]]
- [[计算效率优化|计算效率优化]]
- [[fmi标准|FMI标准]]


## 主要发现


- 联合仿真结果与完整系统仿真高度一致，验证了虚构线路接口方法的准确性
- 相比单一工具仿真，联合仿真架构显著降低了大规模DER系统的计算耗时
- 成功实现正序域Modelica模型与相域OpenDSS模型的无缝数据交互



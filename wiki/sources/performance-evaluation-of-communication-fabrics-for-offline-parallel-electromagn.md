---
title: "Performance evaluation of communication fabrics for offline parallel electromagnetic transient simulation based on MPI"
type: source
authors: ['P. Le-Huy']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109629. doi:10.1016/j.epsr.2023.109629"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/Le-Huy 等 - 2023 - Performance evaluation of communication fabrics for offline parallel electromagnetic transient simul.pdf"]
---

# Performance evaluation of communication fabrics for offline parallel electromagnetic transient simulation based on MPI

**作者**: P. Le-Huy
**年份**: 2023
**来源**: `31/Le-Huy 等 - 2023 - Performance evaluation of communication fabrics for offline parallel electromagnetic transient simul.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Performance evaluation of communication fabrics for offline parallel Power System Simulation group at the Hydro-Qu´ebec Research Center (IREQ), 1800 boul. Lionel-Boulet, Varennes, Qu´ebec, J3 × 1S1, Canada Offline electromagnetic transient (EMT) simulation is a very time-consuming activity for large-scale and complex power systems. Hydro

## 核心贡献


- 评估了四种MPI通信架构在离线并行电磁暂态仿真中的性能表现与通信开销
- 引入扩展Amdahl定律与Karp-Flatt指标量化并行效率及负载不平衡问题
- 验证了基于PC集群的MPI并行方案可有效扩展大规模电网离线仿真能力


## 使用的方法


- [[mpi消息传递接口|MPI消息传递接口]]
- [[扩展amdahl定律分析|扩展Amdahl定律分析]]
- [[karp-flatt串行分数度量|Karp-Flatt串行分数度量]]
- [[并行加速比与计算效率评估|并行加速比与计算效率评估]]


## 涉及的模型


- [[魁北克输电系统模型|魁北克输电系统模型]]


## 相关主题


- [[离线电磁暂态仿真|离线电磁暂态仿真]]
- [[大规模并行计算|大规模并行计算]]
- [[mpi通信架构评估|MPI通信架构评估]]
- [[pc集群部署|PC集群部署]]
- [[并行性能度量|并行性能度量]]


## 主要发现


- Karp-Flatt指标能有效诊断并行负载不均与同步开销导致的性能瓶颈
- 扩展Amdahl定律揭示了内存访问与IO延迟对单核基准时间的显著影响
- 基于MPI的PC集群方案可突破单机限制，显著提升大规模电网离线仿真速度



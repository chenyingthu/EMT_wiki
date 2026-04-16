---
title: "Published in IET Generation, Transmission & Distribution"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-FPGA digital hardware design for detailed large-scale real-time electromagnetic transient simulation of power systems.pdf"]
---

# Published in IET Generation, Transmission & Distribution

**作者**: 
**年份**: 2013
**来源**: `27&28/Multi-FPGA digital hardware design for detailed large-scale real-time electromagnetic transient simulation of power systems.pdf`

## 摘要

Large-scale electromagnetic transient simulation of power systems in real-time using detailed modelling is computationally very demanding. This study introduces a multi-ﬁeld programmable gate array (FPGA) hardware design for this purpose. A functional decomposition method is proposed to map FPGA hardware resources to system modelling. This systematic method lends itself to fully pipelined and parallel hardware emulation of individual component models and numerical solvers, while preserving original system characteristics without the need for extraneous components to partition the system. Proof-of-concept is provided in terms of a 3-FPGA and 10-FPGA real-time hardware emulation of a three-phase 42-bus and 420-bus power systems using detailed modelling of various system components and iterat

## 核心贡献


- 提出功能分解法，将同类组件映射至独立FPGA模块，实现全流水线并行处理
- 摒弃人工传输线分区策略，无需额外解耦元件即可保持原系统拓扑特性
- 构建支持全牛顿迭代与32位浮点运算的多FPGA实时硬件仿真架构


## 使用的方法


- [[功能分解法|功能分解法]]
- [[全流水线并行计算|全流水线并行计算]]
- [[多速率仿真|多速率仿真]]
- [[梯形积分法|梯形积分法]]
- [[全牛顿迭代法|全牛顿迭代法]]
- [[离散时间等效|离散时间等效]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[同步电机|同步电机]]
- [[变压器|变压器]]
- [[线性集总rlcg元件|线性集总RLCG元件]]
- [[非线性元件|非线性元件]]
- [[负荷|负荷]]
- [[断路器|断路器]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[多fpga并行计算|多FPGA并行计算]]
- [[频率相关建模|频率相关建模]]
- [[大规模电力系统仿真|大规模电力系统仿真]]
- [[数字硬件仿真|数字硬件仿真]]


## 主要发现


- 3与10片FPGA架构成功实现42及420节点系统的百兆赫兹实时仿真
- 实时仿真结果与离线EMTP高度吻合，验证了架构的计算精度与可扩展性
- 功能分解法有效均衡硬件负载，消除传统分区引入的通信延迟与频率误差



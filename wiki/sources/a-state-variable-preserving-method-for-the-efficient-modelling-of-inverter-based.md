---
title: "A state-variable-preserving method for the efficient modelling of inverter-based resources in parall"
type: source
year: 2025
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/Wang 等 - 2025 - A state-variable-preserving method for the efficient modelling of inverter-based resources in parall.pdf"]
---

# A state-variable-preserving method for the efficient modelling of inverter-based resources in parall

**年份**: 2025
**来源**: `04/Wang 等 - 2025 - A state-variable-preserving method for the efficient modelling of inverter-based resources in parall.pdf`

## 摘要

The aggregation models of renewable energy power stations are difﬁcult to apply to the stability research of the fault inside the station or the oscillation analysis between the station and the grid-side system, and the high dimensional characteristics of their detailed model will pose an enormous challenge to the simulation efﬁciency. To alleviate the contradiction between accuracy and efﬁciency, this paper proposes a state-variable-preserving method to efﬁciently model inverter-based resources and a node tearing method to realize parallel simulation of the renewable energy power station consisting of inverter-based resources. The state-variable-preserving model uses discrete state space expression to eliminate the internal nodes on the basis of preserving the original variables of the ge

## 核心贡献


- 提出状态变量保持法，利用离散状态空间消除内部节点并保留原始变量，降低求解规模
- 提出节点撕裂法重构节点电压方程，降低关联变量求解复杂度，适配共母线互联拓扑
- 设计分层并行算法，利用机组与集群求解独立性，显著提升大规模场站EMT仿真效率


## 使用的方法


- [[状态变量保持法|状态变量保持法]]
- [[节点撕裂法|节点撕裂法]]
- [[离散状态空间法|离散状态空间法]]
- [[分层并行算法|分层并行算法]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[逆变器型资源|逆变器型资源]]
- [[光伏发电单元|光伏发电单元]]
- [[光伏电站|光伏电站]]
- [[dc-dc变换器|DC/DC变换器]]
- [[dc-ac逆变器|DC/AC逆变器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[新能源场站建模|新能源场站建模]]
- [[网络解耦|网络解耦]]
- [[模型降阶|模型降阶]]


## 主要发现


- 数值精度与稳定性分析验证了所提模型在光伏电站内部故障与振荡分析中的可靠性
- 改变光伏电站规模测试表明，分层并行算法显著降低计算耗时，提升大规模仿真效率
- 节点撕裂法相比传统支路切割法，有效降低了共母线互联拓扑下关联变量的求解复杂度



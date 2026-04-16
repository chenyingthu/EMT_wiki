---
title: "A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT and Transient Stability"
type: source
year: 2017
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/TPWRD.2017.2690145.pdf.pdf"]
---

# A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT and Transient Stability

**年份**: 2017
**来源**: `03/TPWRD.2017.2690145.pdf.pdf`

## 摘要

—The steady increase of power electronic devices and nonlinear dynamic loads in large scale AC/DC systems desperately requires an efﬁcient simulation method. However, the traditional hybrid simulation, which incorporates various components into a single EMT subsystem, causes great difﬁculty in network partitioning and signiﬁcant deterioration in simu- lation efﬁciency. To resolve these issues, a distributed hybrid simulation method is proposed in this paper. The key factor leading the success of this method is a distinct interfacing technique, which includes: i) a new approach based on the two- level Schur complement to update the interfaces by taking full consideration of the couplings between different EMT subsys- tems; and ii) a combined interaction protocol to further improve the efﬁci

## 核心贡献


- 提出基于两级舒尔补的接口更新策略，充分计及多EMT子系统间动态耦合
- 构建三相戴维南与三序诺顿等效接口模型，突破传统三相平衡假设限制
- 设计组合式交互协议实现多程序并行协调，显著提升大规模系统仿真效率


## 使用的方法


- [[分布式混合仿真|分布式混合仿真]]
- [[两级舒尔补法|两级舒尔补法]]
- [[节点分析法|节点分析法]]
- [[组合交互协议|组合交互协议]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[非线性动态负荷|非线性动态负荷]]
- [[同步电机|同步电机]]
- [[输电线路|输电线路]]
- [[机电暂态模型|机电暂态模型]]
- [[电磁暂态模型|电磁暂态模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[分布式仿真|分布式仿真]]
- [[网络等值|网络等值]]
- [[接口技术|接口技术]]
- [[并行协调仿真|并行协调仿真]]
- [[vsc-model|VSC]]


## 主要发现


- IEEE 39节点及实际系统验证表明，该方法精度与效率显著优于传统混合仿真
- 舒尔补策略有效消除多EMT子系统耦合误差，避免网络划分不当引发的数值失稳
- 组合交互协议在保证接口数据同步精度的同时，大幅降低了多机通信与计算开销



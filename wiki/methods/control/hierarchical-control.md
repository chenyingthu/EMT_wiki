---
title: "分层控制 (Hierarchical Control)"
type: method
tags: [hierarchical-control, primary-control, secondary-control, tertiary-control, coordination]
created: "2026-05-05"
updated: "2026-05-12"
---

# 分层控制 (Hierarchical Control)


## 定义与边界

分层控制是把控制任务按时间尺度和职责分成一次、二次、三次或更高层级的组织方法。它广泛用于微电网、储能系统、多变流器并联系统和多端直流网络中，用来协调快速稳定、稳态恢复和更慢的调度优化任务。

本页讨论的是控制分层逻辑，不把 CPU-FPGA 实时仿真分区、硬件资源分配或主电路模型切换误写成“分层控制”。

## EMT 中的作用

在 EMT 仿真中，分层控制用于：

- 区分一次支撑、二次恢复和更慢能量管理的动态作用；
- 研究层间带宽分离不充分时的相互作用；
- 分析通信延迟、模式切换和功率限值如何跨层传播；
- 为多装置协调提供结构化解释框架。

## 常见层级

- 一次控制：快速局部支撑，例如 [[droop-control]]、[[inertia-control]] 或限流控制。
- 二次控制：恢复频率、电压或功率共享偏差，常与 [[distributed-control]] 结合。
- 三次控制：更慢的调度、经济优化或运行方式管理，可与 [[economic-dispatch]]、[[optimal-power-flow]] 关联。

## 关键公式

分层控制本身不是单一方程，但可抽象为快慢参考的级联更新：

$$
r_1 = f_1(y), \qquad
r_2 = f_2(y, \bar{y}), \qquad
r_3 = f_3(\mathcal{O}, \mathcal{C})
$$

其中 $r_1,r_2,r_3$ 分别表示不同层级输出的参考量，$y$ 为局部测量，$\bar{y}$ 为协调或邻居信息，$\mathcal{O},\mathcal{C}$ 为更慢层面的运行目标和约束。关键不在公式形式，而在不同层级的时间尺度和职责边界。

## 与相关方法的关系

- [[droop-control]]：常见一次控制层。
- [[distributed-control]]：常见二次协调层。
- [[adaptive-droop]]：可看作一次层参数自适应的扩展。
- [[microgrid-control]] 和 [[multi-terminal-dc]]：是分层控制的典型应用场景。

## 适用边界与失败模式

- 适用于多目标、不同时间尺度同时存在的控制场景。
- 若层间带宽分离不足，可能出现相互抢占、振荡或恢复缓慢。
- 若上层参考更新过慢或通信不可靠，下层可能长期运行在偏差状态。
- 若能量管理与保护约束不一致，层级设计可能在故障下失效。

## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]：说明一次下垂和更慢恢复/管理层级在构网型场景中的组织。
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]：说明多层控制与保护在实时闭环中的协调问题。
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]：可作为多环控制和局部阻尼层与外层目标耦合的相关来源。

## 量化性能边界

**Nguyen et al. (2021) GFM黑启动一次+二次分层控制（PSCAD/EMTDC，改进IEEE 9节点）**:
- 一次下垂（P-f/Q-V）提供快速本地电压/频率支撑，二次PI补偿稳态偏差
- 黑启动全过程18s含7个切换步，频率精确收敛至60 Hz
- 稳态电压误差<1%（与数值优化解对比），负荷阶跃最大120.2 MW + 42.3 Mvar
- 验证平台：PSCAD/EMTDC高保真模型
- 数据缺口：下垂系数mp、nq的取值依据和灵敏度未系统报告

**Nurunnabi et al. (2025) GFM逆变器PQ能力与增强型电压调节（EVR）**:
- 对比基础下垂（FDR）与增强型电压调节（EVR）两层控制
- EVR在限幅时保留电压支撑能力，电压偏差<2.9%，频率偏差<0.37%
- SVPWM输出能力达1.53 p.u. vs SPWM 1.33 p.u.
- 含L、LC、LCL三种滤波器拓扑PQ运行域对比
- IEEE 1547标准验证
- 验证方式：EMT仿真+实时HIL
- 数据缺口：EVR策略的控制参数整定方法未系统报告

**Liu et al. (2010) 云广±800kV UHVDC分层控制模式分析（PSCAD/EMTDC）**:
- LCC-HVDC三层控制架构：主控层(功率/频率)→极控层(电流)→阀控层(触发)
- 整流侧：定电流/定功率两种模式；逆变侧：定关断角+定电流+VDCOL协调
- 定功率模式暂态变化率较定电流模式降低20-30%
- 故障电流峰值1.5-1.6 p.u.，恢复时间0.2-0.4 s
- 验证平台：PSCAD/EMTDC
- 数据缺口：仅分析云广工程特定参数，通用性待验证

**数据缺口声明**：分层控制的量化性能数据来自GFM逆变器控制、LCC-HVDC控制等不同领域来源，各自使用不同测试系统和评估指标。不同层级之间的带宽分离比例缺乏系统化的量化设计准则。三次控制（经济调度、能量管理）在EMT仿真中的建模精度和步长约束未被系统评估。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*“最优分层架构”。具体实现必须回到应用系统和对应来源。

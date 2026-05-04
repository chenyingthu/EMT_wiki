---
title: "调度运行 (Dispatch Operation)"
type: topic
tags: [dispatch, operation, control-center, scada, ems, power-grid]
created: "2026-05-02"
---

# 调度运行 (Dispatch Operation)

## 定义与边界

调度运行是电力系统运行控制中的计划、监视、校核和再调度活动，核心对象是发电、负荷、输电约束、备用、无功电压和运行风险。它不是 EMT 仿真方法，也不是单一优化算法；[[power-flow-calculation]]、[[optimal-power-flow]]、[[economic-dispatch]] 和安全稳定校核只是调度运行中的分析工具。

在 EMT Wiki 中，本页只讨论调度运行与 EMT 的接口：哪些运行方式、扰动、控制策略和保护场景需要进入 EMT 或实时仿真验证，以及哪些调度结论不能由 EMT 波形直接推出。

## EMT 中的作用

调度运行通常工作在分钟、小时和日前尺度，而 [[emt-simulation]] 关注微秒至秒级暂态。二者相接的位置包括：

- 调度给出运行方式、潮流断面、机组出力、HVDC 功率指令、无功补偿状态和新能源出力场景，作为 EMT 初始条件和扰动集合。
- EMT 检查运行方式下的换流器控制交互、保护动作、故障穿越、暂态过电压和宽频振荡风险，结果可反馈为运行约束或校核规则。
- [[real-time-simulation]] 和 [[hil-simulation]] 可用于调度员培训、保护控制闭环演练和 WAMPAC 类应用，但其有效性受模型移植、通信接口和实时约束限制。

## 主要分支与机制

- 经济与安全调度：以成本、备用、输电限额和安全约束为主，常依赖 [[economic-dispatch]]、[[optimal-power-flow]] 和 N-1 校核。它们通常不表示开关暂态和相域不平衡。
- 动态安全评估：把 [[transient-stability-analysis]]、小信号振荡、电压稳定和频率安全作为调度约束来源。是否需要 EMT 取决于电力电子渗透率、保护判据和暂态对象。
- 新能源与储能调度：处理预测误差、爬坡、备用和电压支撑。若控制器、PLL、限流器或构网控制行为影响安全边界，应与 [[renewable-energy-integration]]、[[gfl-inverter-model]]、[[gfm-inverter-model]] 的 EMT 模型联动。
- 调度培训与在线预演：通过离线仿真、超实时仿真或实时 HIL 演练事故处置。此类应用不能仅凭界面或场景脚本证明物理模型有效。

## 形式化表达

调度运行与 EMT 的接口可以理解为从慢时间尺度运行点到快时间尺度暂态场景的映射：

$$
\mathcal{S}_{\mathrm{EMT}} = G(P_G,Q_G,P_L,Q_L,V,\theta,c,\mathcal{D})
$$

其中 $P_G,Q_G$ 表示发电和无功设定，$P_L,Q_L$ 表示负荷，$V,\theta$ 表示潮流初值，$c$ 表示控制和保护定值，$\mathcal{D}$ 表示故障或扰动集合。EMT 校核的是 $\mathcal{S}_{\mathrm{EMT}}$ 下的暂态响应；它不能直接给出调度优化目标或市场结算结果。

## 适用边界与失败模式

- 调度模型中的正序、稳态或准稳态约束不能直接替代三相 EMT。换流失败、保护误动、暂态过电压、谐波放大和控制限幅通常需要更细模型。
- EMT 算例也不能自动给出经济最优或市场出清结果。它只能在给定运行点下检验暂态响应和边界条件。
- 若运行数据、保护定值、控制参数或新能源预测误差未绑定来源，调度-EMT 联合结论应降级为场景研究。
- 调度员培训仿真重在操作流程和风险识别；若用于设备动作结论，应说明是否采用 EMT、RMS、混合仿真或脚本化逻辑。

## 代表性来源

- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] 说明大规模 EMT 模型进入实时环境时，模型兼容、控制模块和信号校核是 WAMPAC 与调度支撑应用的关键证据边界。
- [[flexible-time-stepping-dynamic-emulation-of-acdc-grid-for-faster-than-scada-appl]] 支撑“快于 SCADA 的动态预演需要明确模型、步长和接口”的限定性表述。
- [[improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi]] 可作为新能源优化调度与约束处理的来源入口；其结论不应外推为 EMT 暂态验证。

## 与相关页面的关系

- [[power-flow-calculation]] 和 [[optimal-power-flow]] 解释稳态潮流与优化计算，本页讨论这些结果如何成为 EMT 场景输入。
- [[transient-stability-analysis]] 面向机电暂态稳定；当控制器、换流器或保护依赖快速波形时，需要与 [[emt-simulation]] 衔接。
- [[renewable-energy-integration]] 关注新能源并网机制；调度运行关注这些机制如何转化为运行约束和场景选择。
- [[real-time-simulation]]、[[hil-simulation]] 讨论仿真平台和闭环测试，不等同于调度决策本身。

## 开放问题

- 如何把 EMT 暂态风险压缩成可用于调度优化的可审核约束，而不丢失控制器和保护边界。
- 如何在新能源高占比系统中统一调度预测误差、控制限幅、保护动作和 EMT 模型不确定性。
- 如何验证在线预演或调度数字孪生的实时性、模型一致性和决策可追溯性。

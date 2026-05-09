---
title: "Anti Islanding"
type: method
tags: [anti-islanding]
created: "2026-05-04"
---

# Anti Islanding

## 定义与边界

Anti-islanding 指并网分布式电源、逆变器或微电网在外部电网失电后识别非计划孤岛并按保护要求脱网或切换控制的功能集合。在当前 Wiki 中，它更适合作为受控入口，而不是单独扩写成完整方法页：已有页面已经覆盖微电网控制、构网型控制、低电压穿越和并网/孤岛运行边界。

本页不讨论某个固定检测算法，也不声称任何检测时间、盲区或网规门槛。具体性能必须绑定设备、保护规范、负荷匹配程度和测试系统。

## 概念边界

- 与 [[microgrid-control]] 的关系：微电网控制可包含计划孤岛、黑启动和并网切换；anti-islanding 更关注非计划孤岛识别和保护动作。
- 与 [[grid-forming-control]] 的关系：构网型控制可在孤岛或弱网中建立电压频率，但不等于防孤岛保护。
- 与 [[lvrt-control]] 的关系：LVRT 关注故障期间持续并网能力；anti-islanding 关注外部电网失电后的识别和动作边界。
- 与 [[droop-control]] 的关系：下垂控制可支撑孤岛运行，但不能替代孤岛检测和并网保护判据。

## 核心机制

Anti-islanding 检测的核心逻辑可以抽象为在 PCC 测量点连续评估以下判定条件：

$$
f(\mathbf{v}, \mathbf{i}, f) \begin{cases} \leq \tau_{\text{trip}} & \Rightarrow \text{island detected} \\ > \tau_{\text{trip}} & \Rightarrow \text{grid-connected} \end{cases}
$$

其中 $\mathbf{v}, \mathbf{i}$ 为 PCC 电压电流相量，$f$ 为频率，$\tau_{\text{trip}}$ 为保护动作阈值。具体实现分为被动式（检测电压/频率/相位的异常偏移）和主动式（向 PCC 注入小扰动并观察响应）。

## 适用边界与失败模式

- **valid_when**: 分布式电源容量远小于本地负荷，功率不平衡度足够大；被动法在净功率接近零时无效。
- **invalid_when**: 多机并联时主动式注入可能互相干扰；含储能或构网型变流器时孤岛电压频率可能被支撑在正常范围。
- **assumptions**: 假设并网开关断开后 PCC 与外部电网的电气隔离是完整的（据方法推断）。
- **evidence_gaps**: 不同电网规范（IEEE 1547、VDE-AR-N 4105）的检测时间要求和频段/电压阈值不同，不能混写为统一指标。

## 链接用法

需要说明孤岛运行控制时，链接 [[microgrid-control]] 或 [[grid-forming-control]]。需要说明故障穿越时，链接 [[lvrt-control]]。只有在明确讨论 "anti-islanding / 防孤岛" 保护语义时才链接本页。

## 代表性来源

- [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]]：提供孤岛混合 AC/DC 微电网运行点建模背景，但不是防孤岛检测算法来源。
- [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-]]：包含故障清除后孤岛运行场景，可作为 EMT 场景边界参考。
- [[sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul]]：包含微电网孤岛模式切换的实时仿真背景，但不证明任何通用防孤岛性能。

## 证据边界

当前本地证据主要支持"孤岛/并网切换是多个页面共享的运行场景"。缺少专门防孤岛检测论文支撑，因此本页只保留受控入口和链接规则，不写主动/被动检测分类、阈值、动作时间或标准符合性结论。

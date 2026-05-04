---
title: "最优潮流 (Optimal Power Flow, OPF)"
type: method
tags: [optimal, power-flow, optimization, dispatch, economic, security]
created: "2026-05-02"
---

# 最优潮流 (Optimal Power Flow, OPF)

## 定义与边界

最优潮流（Optimal Power Flow, OPF）是在潮流方程和运行约束下优化电力系统运行点的方法。它把 [[power-flow-calculation]] 的等式约束与发电、负荷、电压、线路容量、无功设备和安全约束放入统一优化框架。

OPF 属于稳态或准稳态系统分析方法。它不是 EMT 的核心数值积分方法，也不直接求解开关器件瞬时状态、宽频网络响应或电磁暂态波形。OPF 与 EMT 的合理关系是：生成稳态运行点、约束可行边界或调度场景，再由 EMT 模型验证局部快速动态。

## 输入与输出

典型输入包括：

- 网络拓扑、节点导纳矩阵和支路参数；
- 发电机有功/无功边界、成本或报价函数；
- 负荷、无功补偿、变压器分接头和运行限值；
- 目标函数和约束集合，例如成本、网损、电压偏差或安全约束。

典型输出包括：

- 节点电压幅值和相角；
- 发电机有功、无功和可调设备设定值；
- 线路潮流、约束裕度和紧绑定约束；
- 目标函数值及拉格朗日乘子等灵敏度信息。

## 数学形式

通用 OPF 可写为：

$$
\min_{x,u} f(x,u)
$$

满足：

$$
h(x,u) = 0,\qquad g(x,u) \leq 0
$$

其中 $x$ 通常包含节点电压幅值和相角，$u$ 包含发电出力、无功控制或其他可控量。$h$ 表示交流潮流平衡方程，$g$ 表示设备和运行约束。

交流 OPF 的节点功率平衡可写为：

$$
P_{Gi}-P_{Di}=V_i\sum_j V_j(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij})
$$

$$
Q_{Gi}-Q_{Di}=V_i\sum_j V_j(G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij})
$$

这些方程来自稳态相量模型。它们不能替代 EMT 中的三相瞬时网络方程。

## 主要变体

- 交流 OPF：保留非线性交流潮流方程，可描述有功、无功和电压耦合。
- 直流 OPF：采用线性化有功潮流近似，适合调度和市场分析中的简化问题，但不反映无功和电压约束。
- 安全约束 OPF：在基态约束之外加入预想事故约束，用于安全校核或预防控制。
- 多时段 OPF：引入爬坡、储能状态、负荷变化和可再生能源时间相关性。
- 鲁棒或随机 OPF：把不确定性显式纳入场景、置信集或概率约束。

## 求解机制

OPF 求解通常围绕 KKT 条件、拉格朗日函数和非线性方程组展开。常见路线包括：

- 牛顿型或序列二次规划方法，用局部线性化/二次化迭代逼近最优点；
- 内点法，通过障碍函数处理不等式约束；
- 凸松弛或线性近似，用可验证的近似模型换取求解便利；
- 混合整数规划，在离散分接头、开关状态或机组状态显式建模时使用。

算法性能依赖网络规模、初值、约束活跃集、模型凸性和求解器实现。本页不给出无来源的固定收敛速度或最优性保证。

## 与 EMT 仿真的关系

OPF 可服务于 EMT 的前处理和场景设计：

- 通过 OPF 生成运行方式，再由 [[steady-state-initialization]] 转换为 EMT 初始状态；
- 用 OPF 筛选高负荷、弱电压、潮流重载或可再生能源高占比工况；
- 在 [[electromechanical-electromagnetic-hybrid-simulation]] 中作为慢时间尺度机电侧或调度侧模型的一部分；
- 对换流器、保护和控制细节，OPF 只能给出设定点或边界条件，不能替代 [[emt-simulation]]。

当研究对象是谐波、开关过电压、换相失败、控制限幅或保护动作时，OPF 输出需要经过 EMT 或其他动态模型验证。

## 适用边界与失败模式

- 交流 OPF 可能存在非凸性，局部最优和初值敏感需要通过算例说明。
- 直流 OPF 的线性化假设在高电阻线路、重载、无功受限或电压问题中可能失效。
- 安全约束 OPF 只覆盖被列入的预想事故，不代表对所有扰动安全。
- 多时段或随机 OPF 的结果依赖场景生成、概率模型和预测误差处理。

## 代表性来源

- [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t]]：可用于说明优化设定可参与稳定控制策略生成；不能由此推出 OPF 对所有 SSCI 场景有效。
- [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi]]：包含交直流潮流和动态模型接口，可支撑 OPF/潮流结果作为动态仿真初值的边界说明。
- [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a]]：说明稳态运行点和接口边界会影响混合仿真；不应把优化模型替代 EMT 验证。

## 与相关页面的关系

- [[power-flow-calculation]] 是 OPF 的稳态等式约束基础。
- [[economic-dispatch]] 可视为不显式建模完整网络约束的简化运行优化问题。
- [[newton-raphson-method]] 常用于潮流和部分非线性优化迭代中的方程求解。
- [[steady-state-initialization]] 把 OPF 或潮流结果映射到 EMT 初值。
- [[large-scale-power-system]] 涉及 OPF 在大规模系统分析中的建模取舍。

## 证据边界

本页只描述 OPF 的通用数学结构和 EMT 接口角色。任何关于“实时”“全局最优”“工程主流”“固定电压范围”或特定求解器优劣的判断，都需要绑定具体标准、软件版本、系统规模和算例证据后再写入。

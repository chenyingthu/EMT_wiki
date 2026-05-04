---
title: "补偿方法 (Compensation Method)"
type: method
tags: [compensation, reactive-power, facts, voltage-control, power-flow-control, series, shunt]
created: "2026-05-02"
---

# 补偿方法 (Compensation Method)

## 定义与边界

补偿方法（Compensation Method）在 EMT 数值求解语境中，指把一个难以直接并入主网络的元件、子网络或接口从主系统中分离出来，用端口等效和补偿变量保持两侧伏安关系一致。它常用于网络分区、并行 EMT、非线性元件求解、机器接口和多区域 Thevenin/Norton 等值。

本页讨论数值求解和网络分区中的补偿法，不把它扩写为无功补偿、FACTS 设备控制或电能质量补偿的总论。若研究对象是 SVC、STATCOM、串联电容或潮流控制，应转到 [[facts]]、[[svc-model]]、[[statcom-model]] 等模型/主题页。

## EMT 中的作用

EMT 系统通常包含规模很大的线性网络和少量强非线性、强开关或高频子系统。补偿法的作用是让主网络保持较稳定的求解结构，同时把局部复杂性放到接口方程中处理。典型用途包括：

- 把非线性避雷器、饱和电感或电弧模型从线性网络中分离。
- 把电气距离很近、无法用传输线时延自然解耦的子网络分配到不同处理器。
- 在 MATE、节点撕裂或多区域 EMT 中用端口 Thevenin/Norton 关系交换接口量。
- 在实时仿真中局部化开关导致的矩阵时变性。

补偿法不是免费解耦。接口迭代、端口等值更新、通信延迟和强耦合误差会决定它是否适合目标工况。

## 核心机制

设主网络从某个端口看进去可等效为 Thevenin 形式：

$$
\mathbf{v}=\mathbf{v}_{oc}-\mathbf{Z}_{th}\mathbf{i}.
$$

若被分离元件满足

$$
\mathbf{v}=\mathbf{f}(\mathbf{i},\mathbf{x},t),
$$

则接口电流可由残差

$$
\mathbf{F}(\mathbf{i})
=\mathbf{f}(\mathbf{i},\mathbf{x},t)
-\mathbf{v}_{oc}
+\mathbf{Z}_{th}\mathbf{i}
=\mathbf{0}
$$

求得。线性子系统可直接解接口方程；非线性子系统通常需要 [[newton-raphson-method]]、分段线性化或查表迭代。

在 Norton 形式下，端口关系也可写成

$$
\mathbf{i}=\mathbf{i}_{N}-\mathbf{Y}_{N}\mathbf{v}.
$$

Thevenin 和 Norton 表征可以互换，但数值上应考虑矩阵条件数、接口变量选择、端口数和是否便于并行通信。

## 分类与变体

| 变体 | 机制 | 典型用途 | 边界 |
|---|---|---|---|
| 非线性元件补偿 | 线性网络给出端口等值，非线性支路单独迭代 | 避雷器、饱和变压器、电弧模型 | 强耦合多端口非线性会增加迭代风险 |
| MATE/多区域补偿 | 各区域形成端口 Thevenin/Norton 等值，再解接口方程 | 大系统分区、多速率 EMT | 接口延迟和收敛判据必须显式记录 |
| 节点撕裂 | 在撕裂节点引入接口电流或电压补偿量 | 并行网络求解、实时仿真 | 撕裂点选择影响通信和病态程度 |
| Solution-level partitioning | 把时变开关网络限制在局部子网络中 | FPGA/DRTS 的近距离电力电子集群 | 外部网络假设过强时会失效 |
| 端口等效加回代 | 主网络只见低维端口，内部量后处理恢复 | MMC 子模块、复杂外部网络等值 | 需保存足够回代信息，不能只保留端口波形 |

## 适用边界与失败模式

- 接口两侧如果强耦合且没有足够迭代，补偿法可能引入滞后误差或能量不守恒。
- 端口等值通常来自某一线性化、拓扑或频率范围；拓扑切换后需要更新或重新计算。
- 多处理器实现中，通信延迟、同步策略和数据插值可能主导误差。
- 对频率相关网络，简单阻抗矩阵等值可能破坏无源性，需要与 [[passivity-enforcement]] 或 FDNE 验证配合。
- 对非线性元件，补偿迭代失败不应被静默接受；应记录残差、最大迭代和回退策略。

## 代表性证据

| 来源 | 支持的认识 | 证据边界 |
|---|---|---|
| [[use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation]] | 并行实时 EMT 可用传输线延时、补偿法、MATE 或节点撕裂做任务分离，再做任务映射 | 支持补偿法在任务分离中的角色；不提供通用分区最优规则 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga]] | 线性网络可对非线性端口形成 Thevenin 等效，再通过连续或分段 Newton 求端口电流 | 支持非线性元件补偿机制；案例范围有限 |
| [[35tpwrd20192933610]] | Solution-level partitioning 把电力电子开关网络与外部系统分离，意在避免近距离 PEC 对 stub line 的依赖 | 支持实时开关网络局部化；不能外推任意规模或任意 FPGA 资源 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems]] | SFA-EMT 接口讨论传统 TS-EMT 延迟、Thevenin/Norton 等值和 MATE 类接口问题 | 支持多区域接口补偿的动机；具体精度取决于原文接口协议 |

## 与相关页面的关系

- [[network-partitioning]]：补偿法常作为网络分区后的接口求解机制。
- [[multirate-and-network-partitioning]] 和 [[multirate-method]]：补偿接口常与不同步长区域结合。
- [[thevenin-equivalent]]、[[norton-equivalent]] 和 [[thevenin-norton-equivalent]]：补偿法的端口等效基础。
- [[algebraic-characterization]]：补偿接口最终表现为代数残差或端口矩阵。
- [[sparse-matrix-solver]]：主网络和接口方程的计算后端。

## 修订与证据使用注意事项

本页不应加入无功补偿容量、FACTS 响应时间、潮流提升比例或设备配置建议。若必须讨论电气补偿设备，应明确其只是被补偿法分区或端口等效的对象，而不是本页方法定义本身。

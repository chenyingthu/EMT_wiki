---
title: "分层接入 (Layered Connection)"
type: method
tags: [layered, connection, hvdc, grid, uhvdc, multi-infeed, hierarchical]
created: "2026-05-02"
---

# 分层接入 (Layered Connection)

## 定义与边界

分层接入是把一个外部系统、换流站或等值网络拆成若干电气层，并在边界端口处分别给出端口电压、电流、功率或导纳关系的建模方法。它在 EMT 语境下更接近一种边界组织方法，而不是某一种固定设备模型。常见对象包括多电压等级交流接入、机电-电磁混合仿真接口、频变网络等值的详细层与外部等值层，以及多端口换流站或外部系统等值。

本页不把分层接入写成“必然提高稳定性”或“通用最优接入方式”。分层是否有价值取决于研究边界、端口选择、各层网络强度、控制耦合和验证对象。若页面讨论的是 UHVDC 工程接入方案，应绑定具体工程资料；若讨论的是 EMT 方法，本页只保留网络等值和接口建模层面的机制。

## EMT 中的作用

在 EMT 仿真中，分层接入主要用于三类问题：

- 将详细 EMT 区域与外部交流网络分开，避免把远方系统完整展开。
- 在多端口边界处分别表示不同电压层级、不同换流器群或不同外部网络分区的端口特性。
- 对频率相关网络等值进行结构化处理，例如把扰动测试得到的详细层导纳与解析外部层导纳组合后进入时域仿真。

它的核心价值是把“一个边界”改写成“多个可解释端口或层”。这样可以明确哪些动态由详细模型承担，哪些动态由等值模型承担，哪些跨层耦合必须通过矩阵项或接口算法保留。

## 核心机制

### 层与端口

设边界端口按层分为 $L_1, L_2, \ldots, L_m$。每层端口电压和电流可写成向量：

$$
\mathbf{v} =
\begin{bmatrix}
\mathbf{v}_1 \\
\mathbf{v}_2 \\
\cdots \\
\mathbf{v}_m
\end{bmatrix},
\quad
\mathbf{i} =
\begin{bmatrix}
\mathbf{i}_1 \\
\mathbf{i}_2 \\
\cdots \\
\mathbf{i}_m
\end{bmatrix}
$$

若外部网络在目标频段可近似为线性多端口导纳，则有：

$$
\mathbf{i}(s)=\mathbf{Y}_{\mathrm{eq}}(s)\mathbf{v}(s)+\mathbf{i}_{\mathrm{src}}(s)
$$

其中 $\mathbf{Y}_{\mathrm{eq}}(s)$ 的对角块表示各层自导纳，非对角块表示层间耦合。分层接入不能只保留对角块；如果不同电压层、换流器群或交流区域之间存在显著耦合，忽略非对角项会改变故障电流分配、振荡阻尼或高频传播路径。

### 双层频变等值

在频变网络等值中，分层可以写成：

$$
\mathbf{Y}_{\mathrm{total}}(s)=\mathbf{Y}_{\mathrm{detail}}(s)+\mathbf{Y}_{\mathrm{external}}(s)+\mathbf{Y}_{\mathrm{comp}}(s)
$$

$\mathbf{Y}_{\mathrm{detail}}(s)$ 可来自端口扰动测试或详细 EMT 子网扫描，$\mathbf{Y}_{\mathrm{external}}(s)$ 可来自外部网络拓扑和参数的解析消去，$\mathbf{Y}_{\mathrm{comp}}(s)$ 可用于局部无源性补偿。该表达式说明“分层”并非简单叠加容量，而是把不同证据来源和不同建模可信度的导纳贡献放在同一端口方程中。

### 功率分配与接口约束

若分层接入用于 HVDC 或换流站功率注入，可用功率平衡表达接口约束：

$$
P_{\mathrm{dc}}=\sum_{k=1}^{m} P_k + P_{\mathrm{loss}}
$$

$$
Q_k = Q_{\mathrm{filter},k}+Q_{\mathrm{control},k}+Q_{\mathrm{network},k}
$$

这里 $P_k$ 和 $Q_k$ 是第 $k$ 层交流侧注入或吸收的有功、无功。固定比例分配只是控制策略之一，不能作为所有工况的默认规律。故障、限流、换相失败、控制模式切换和无功约束都会改变各层功率和电压响应。

## 分类与变体

| 变体 | 建模对象 | EMT 表示 | 主要边界 |
|------|----------|----------|----------|
| 电压等级分层接入 | 直流或换流站接入不同交流电压层 | 多端口功率注入或换流器详细模型 | 需绑定具体工程和控制策略 |
| 双层频变网络等值 | 详细层加外部等值层 | $\mathbf{Y}_{\mathrm{detail}}(s)+\mathbf{Y}_{\mathrm{external}}(s)$ | 需检查拟合、无源性和端口定义 |
| 分区混合仿真接口 | EMT 区域与机电区域 | 戴维南、诺顿或动态导纳接口 | 多速率同步和延迟会影响结果 |
| 多馈入等值边界 | 多个换流器或多端口交流网络 | 块导纳矩阵和耦合项 | 不能把端口独立化后忽略耦合 |
| 分层控制接入 | 多换流器或多层电压控制 | 控制环加网络方程 | 控制模式和限幅需要显式说明 |

## 适用边界与失败模式

分层接入适合边界清晰、端口可定义、层间耦合可测量或可计算的系统。它不适合在缺少端口数据、拓扑频繁改变或控制逻辑不可见时直接替代详细模型。

常见失败模式包括：

- 把工程层级或电压等级写成自然解耦，忽略层间互导纳和控制耦合。
- 只按额定容量分配功率，而没有验证故障、低短路比或限流工况。
- 用工频等值表示外部网络，却研究高频振荡、操作过电压或宽频相互作用。
- 频变等值拟合后未做 [[passivity-enforcement]]，导致 EMT 时域接口出现非物理能量注入。
- 把单篇 UHVDC 或 MMC 混合仿真论文的测试系统结果外推为所有分层接入工程的普遍结论。

## 代表性证据

- [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio]]：该来源页明确讨论 two-layer FDNE，用详细层扰动测试和外部层解析导纳构成混合仿真接口，并用局部无源性补偿处理非无源风险。可支撑“分层等值可组织不同证据来源的端口导纳”，但不能据此声称任意系统都有固定误差或固定加速比。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：支撑机电-电磁混合仿真中用频变网络等值表示外部交流网络。该来源的 IEEE 39 节点验证应作为算例证据，而不是通用稳定性保证。
- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]：支撑多端口导纳矩阵、端口间耦合和 EMTP 可实现等值网络的思想。其 Ontario Hydro 500 kV 算例不能直接外推为所有外部网络等值都具有同等精度。
- [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc]]：可作为 UHVDC 控制模式和受端交流网络交互的来源入口。若用于工程分层接入，应回到原文确认工程对象和控制细节。

## 与相关页面的关系

- [[network-equivalent]] 是更高层主题，覆盖外部系统等值、动态等值和频率相关等值。
- [[ac-coupled-network-equivalent]] 关注交流接口的端口变量和混合仿真边界；分层接入可视为其多层或多端口组织形式。
- [[detailed-equivalent-model]] 关注在端口处保留宽频动态的详细等值；分层接入可把详细等值作为某一层。
- [[norton-equivalent]] 和 [[equivalent-circuit-method]] 提供端口电路形式，常用于各层边界的时域实现。
- [[transformer-network]] 与 [[ideal-transformer-equivalent]] 处理变压器端口和绕组关系，常出现在换流站或多电压层接入中。
- [[passivity-enforcement]] 是频变分层等值进入 EMT 前的重要校核步骤。

## 开放问题

- 多层边界的端口选择如何影响高频耦合和故障电流分配，仍需按具体网络复核。
- 含强非线性换流器控制、保护动作和拓扑切换的分层等值，需要多运行点或事件驱动模型，不能只靠单一线性导纳。
- 工程分层接入的运行收益、短路容量要求和电压稳定性结论必须绑定工程数据、运行方式和验证基线。

## 来源论文

参见 [[index]] 获取更多分层接入相关文献。

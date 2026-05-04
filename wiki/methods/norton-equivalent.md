---
title: "诺顿等效 (Norton Equivalent)"
type: method
tags: [norton, equivalent, current-source, admittance, network, circuit-theory]
created: "2026-05-02"
---

# 诺顿等效 (Norton Equivalent)

## 定义与边界

诺顿等效是把线性单端口或多端口网络表示为等效电流源与并联导纳的端口模型。对 EMT 节点分析而言，诺顿形式特别自然，因为网络方程通常以“导纳矩阵乘节点电压等于注入电流”的形式求解。

诺顿等效只保证指定端口的外部电压-电流关系。它不保留被等值网络的内部节点电压、内部故障位置、控制状态或非线性事件。用于非线性设备时，必须说明是某个运行点附近的线性化、分段等效，还是每个时间步更新的伴随模型。

## EMT 中的作用

诺顿等效在 EMT 中常用于：

- 将电感、电容、线路和电力电子子模块离散为并联导纳加历史电流源。
- 在节点导纳矩阵中表示外部系统、故障点、源网络或设备端口。
- 将频率相关网络等值、变压器端口模型或多端口 FDNE 转化为时域可注入电流。
- 在分区仿真和混合仿真接口中交换端口电压和电流。

与戴维南形式相比，诺顿形式通常更适合直接进入 [[nodal-admittance-matrix]]，但两者的物理边界相同。

## 核心机制

### 单端口诺顿形式

对线性单端口，取端口电流流出等值网络或流入网络的符号必须先定义。常见写法为：

$$
i = I_{\mathrm{N}} - Y_{\mathrm{N}}v
$$

其中 $I_{\mathrm{N}}$ 是端口短路电流，$Y_{\mathrm{N}}$ 是从端口看入的等效导纳。若采用注入节点的电流方向，也可写成：

$$
i_{\mathrm{inj}} = I_{\mathrm{hist}} + Y_{\mathrm{N}}v
$$

两种写法的符号不同，页面和代码应保持同一约定。

### 与戴维南等效转换

若戴维南等效为 $V_{\mathrm{th}}$ 串联 $Z_{\mathrm{th}}$，且 $Z_{\mathrm{th}}$ 可逆，则：

$$
Y_{\mathrm{N}}=Z_{\mathrm{th}}^{-1}
$$

$$
I_{\mathrm{N}}=Y_{\mathrm{N}}V_{\mathrm{th}}
$$

多端口情况下，$Z_{\mathrm{th}}$ 和 $Y_{\mathrm{N}}$ 是矩阵；只有矩阵可逆且端口定义一致时才能直接转换。

### 多端口诺顿形式

对 $m$ 个边界端口：

$$
\mathbf{i}=\mathbf{I}_{\mathrm{N}}-\mathbf{Y}_{\mathrm{N}}\mathbf{v}
$$

$\mathbf{Y}_{\mathrm{N}}$ 的对角项是自导纳，非对角项是端口耦合。外部网络等值、变压器高频端口模型和多馈入系统常需要保留非对角项。若把多端口拆成多个独立单端口，必须证明端口间耦合可忽略。

### 伴随模型中的历史源

EMT 梯形积分可把动态支路转成诺顿伴随形式：

$$
i^{n+1}=G_{\mathrm{eq}}v^{n+1}+i_{\mathrm{hist}}^{n}
$$

历史电流源 $i_{\mathrm{hist}}^{n}$ 来自上一时间步状态。对频率相关有理函数模型，也可通过状态空间离散得到类似的当前导纳加历史注入项。

## 分类与变体

| 类型 | 电流源来源 | 导纳来源 | 适用边界 |
|------|------------|----------|----------|
| 静态单端口诺顿 | 短路电流 | 输入导纳 | 线性网络、固定频率或工频近似 |
| 多端口诺顿 | 端口短路电流向量 | 端口导纳矩阵 | 外部网络和多边界接口 |
| 伴随诺顿 | 历史项 | 数值积分等效导纳 | EMT 时间步支路 |
| 频变诺顿 | 状态空间或卷积历史源 | $\mathbf{Y}(s)$ 离散化 | 宽频网络等值 |
| 线性化诺顿 | 运行点附近增量源 | 小信号导纳 | 控制器和非线性设备局部分析 |

## 适用边界与失败模式

诺顿等效的常见风险包括：

- 短路电流和开路电压来自不同运行点，导致 $I_{\mathrm{N}}$ 与 $Y_{\mathrm{N}}$ 不一致。
- 对含限流、保护、饱和或开关动作的设备使用固定线性导纳，却没有说明线性化范围。
- 多端口导纳矩阵条件数差或非对称，未检查端口方向和测量独立性。
- 频变诺顿模型拟合后未检查极点稳定性和无源性。
- 在故障计算中把端口等值结果外推到被等值网络内部支路电流。
- 忘记符号约定，导致注入电流方向在代码、公式和图中不一致。

## 代表性证据

- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]：支撑多端口诺顿型频变网络等值和端口导纳矩阵在 EMTP 中的使用。来源页说明了端口导纳、RLC 支路和外部大网络等值的关系。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：支撑混合仿真接口中频变诺顿等值的有理函数和无源性处理流程。
- [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio]]：支撑 two-layer FDNE 最终离散为诺顿等效电路并用于 TS-EMT 混合仿真接口，但其数值结论需限于原文验证系统。
- [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks]]：包含开关事件辅助源转换为诺顿等效电流源的机制，可作为暂态事件端口等效的代表证据。
- [[equivalent-modelling-method-of-single-active-network-for-fast-electromagnetic-tr]]：可作为有源网络快速 EMT 等值的相关来源，使用时应核对其具体端口和验证范围。

## 与相关页面的关系

- [[equivalent-circuit-method]] 是包含诺顿、戴维南、RLC 和磁路等效的通用方法页。
- [[thevenin-equivalent]] 是诺顿等效的对偶形式。
- [[thevenin-norton-equivalent]] 解释两者在 EMT 离散求解中的互换关系。
- [[current-injection]] 与诺顿等效共享电流注入接口，但更强调设备向网络注入电流的建模方式。
- [[detailed-equivalent-model]] 常把宽频端口模型最终转成诺顿形式进入时域求解。
- [[ac-coupled-network-equivalent]] 和 [[layered-connection]] 中的外部交流边界常使用多端口诺顿表示。

## 开放问题

- 对强非线性设备，固定诺顿导纳与每步重线性化之间的选择需要结合求解器稳定性和模型目标。
- 多端口频变诺顿模型的无源性、稀疏性和低阶实现之间存在取舍。
- 测量型诺顿等值需要报告端口短路或扰动实验的可实现性，现场系统往往不能直接短路测试。

## 来源论文

参见 [[index]] 获取更多诺顿等效相关文献。

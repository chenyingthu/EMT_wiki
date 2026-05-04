---
title: "平均值模型"
type: method
tags: [average-value-model, avm, converter, emt]
created: "2026-04-13"
---

# 平均值模型

## 定义与边界

平均值模型（Average-Value Model, AVM）用开关周期平均量、调制函数或等效受控源替代详细开关动作。它保留变流器的低频功率交换、控制响应和主要储能状态，但通常不保留单个器件的开关沿、载波纹波、反向恢复和高频共模。

AVM 与 [[phasor-model]] 的区别在于：AVM 多数仍在时域中描述控制和暂态平均量；相量模型主要表示选定频率的幅值和相角。AVM 与 [[three-phase-instantaneous-model]] 的区别在于：瞬时值模型直接求解 $abc$ 波形，而 AVM 把开关周期内的细节压缩为平均变量。

## EMT 中的作用

AVM 常用于 EMT 系统级研究中的电力电子子系统：

- VSC、MMC、LCC、DC-DC 变换器和新能源并网变流器的低频等效。
- 控制器调试、故障穿越策略和大系统暂态扫描。
- EMT 与机电暂态或频域模型的混合仿真接口。
- 与详细开关模型切换，以在局部事件期间恢复高保真。

使用 AVM 时必须说明哪些状态被保留，例如直流电容电压、桥臂能量、环流、滤波器电流、控制器状态和闭锁状态。

## 核心方程

以两电平 VSC 的平均桥臂为例，调制函数 $\mathbf{m}_{abc}$ 可生成平均交流侧电压：

$$
\bar{\mathbf{v}}_{abc}=
\left(\mathbf{I}-\frac{1}{3}\mathbf{1}\mathbf{1}^{T}\right)
\frac{V_{\mathrm{dc}}}{2}\mathbf{m}_{abc}.
$$

直流侧平均电流可由交流侧电流和调制函数耦合得到：

$$
\bar{i}_{\mathrm{dc}}=\frac{1}{2}\mathbf{m}_{abc}^{T}\mathbf{i}_{abc},
$$

具体系数取决于电压基准、变换定义和功率归一化。一般状态方程可写为：

$$
\dot{\bar{x}}=f(\bar{x},\bar{u},m,\sigma),
$$

其中 $\bar{x}$ 为平均状态，$m$ 为调制或插入指数，$\sigma$ 表示闭锁、限流、故障穿越等运行模式。

对 MMC，桥臂平均电压通常与投入子模块数或插入指数相关：

$$
\bar{v}_{\mathrm{arm}}=n_{\mathrm{ins}}\bar{v}_{C,\mathrm{arm}},
$$

但是否保留子模块电容电压分布、桥臂能量和闭锁二极管路径取决于具体 AVM 变体。

## 变体

| 变体 | 保留内容 | 主要用途 | 边界 |
|------|----------|----------|------|
| 受控源 AVM | 平均交流电压和直流电流 | 系统级暂态 | 接口延迟和功率一致性需验证 |
| 直接接口 AVM | 将平均模型嵌入节点方程 | EMT 节点法耦合 | 推导依赖具体拓扑和离散格式 |
| 参数化 AVM | 由参数或函数重构换流行为 | LCC、VSC 和故障工况近似 | 参数有效域必须声明 |
| 增强 MMC AVM | 桥臂能量、环流、闭锁模式 | MMC-HVDC 故障和控制研究 | 不一定保留单个子模块差异 |
| 谐波保留 AVM | 保留选定频率或傅里叶系数 | 谐波和宽频振荡近似 | 截断频带外不可见 |
| 混合切换模型 | AVM 与详细模型切换 | 局部高保真和全局效率平衡 | 状态映射和历史项初始化是关键 |

## 适用边界与失败模式

- **开关纹波不可见**：载波边带、器件电压应力和开关损耗不能由基础 AVM 直接得到。
- **故障模式缺失**：直流故障、闭锁、旁路、换相失败和限流若未进入模式变量，模型会给出错误路径。
- **接口延迟**：受控源接口可能引入一步延迟和非物理功率误差；直接接口或同步求解需要单独推导。
- **能量不一致**：平均桥臂能量、电容电压和详细子模块状态之间切换时可能不守恒。
- **参数外推**：PAVM 或拟合型 AVM 只能在参数识别覆盖的工况内使用。

## 代表性证据边界

本页保留文献路线，但不保留无绑定的步长、误差和加速比数字。代表性来源包括：

- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]：讨论 MMC AVM 在 VSC-HVDC 网格中的适用边界。
- [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep]]：代表增强 MMC AVM 对闭锁和暂态初始条件的处理路线。
- [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv]]：代表闭锁模块化 AVM 的统一处理思路。
- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-]]：代表详细模型与开关函数 AVM 的切换路线。
- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]]：代表 LCC 在交流不平衡网络下的参数化 AVM。
- [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo]] 和 [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt]]：代表直接接口 AVM 的节点法耦合路线。
- [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal]]：代表把 VSC AVM 写入节点分析框架的数值实现方向。

这些来源各自绑定到具体拓扑、接口和验证工况；不能合并成“AVM 总是高精度或总能大步长稳定”的结论。

## 与相关页面的关系

- [[switching-function-method]]：平均值模型常从开关函数周期平均得到。
- [[state-space-average-method]]：给出 AVM 的状态空间推导形式。
- [[switch-modeling]]：详细开关模型是 AVM 的高保真对照。
- [[three-phase-instantaneous-model]]：用于验证 AVM 丢弃的瞬时波形和不平衡细节。
- [[direct-interface-technique]]：处理 AVM 与 EMT 网络方程同步耦合。
- [[dynamic-phasor]]：同属平均化或频带压缩思想，但变量和频率保留方式不同。

## 开放问题

AVM 的研究重点是边界透明：平均窗口、模式变量、接口方程、能量状态和验证工况必须明确。对于保护动作、闭锁故障、子模块不均衡和高频振荡，应使用增强 AVM 或详细 EMT 模型交叉验证。

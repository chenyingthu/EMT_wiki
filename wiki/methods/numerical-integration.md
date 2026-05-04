---
title: "数值积分"
type: method
tags: [numerical-integration, emt, trapezoidal, dirk, implicit-integration, stability]
created: "2026-04-13"
---

# 数值积分

## 定义与边界

数值积分是用离散时间公式近似连续动态方程积分的算法族。在 EMT 仿真中，它把电感、电容、控制状态、频变等效和移频包络等动态量推进到下一时间步，并通常转换为伴随电路或状态更新式。

本页关注积分公式本身的阶数、稳定性和阻尼边界。元件级伴随电路的通用离散化见 [[discretization-methods]]；开关事件定位见 [[interpolation-method]]；刚性和突变后的处理策略见 [[stiff-system-handling]]。

## EMT 中的作用

EMT 仿真不仅要求连续系统稳定，还要求离散算法在开关、故障、控制限幅和线路行波到达等非连续事件后保持可解释。数值积分决定：

- 当前步节点方程中的等效导纳和历史源。
- 高频数值误差会持续、衰减还是被过度阻尼。
- 隐式方程是否需要重复矩阵分解或非线性迭代。
- 大步长、实时和多速率仿真能否在目标频带内可信。

## 核心机制

对

$$
\dot{x}=f(t,x)
$$

单步积分器给出 $x_{n+1}$ 与 $x_n$ 的关系。常用公式包括：

| 方法 | 公式 | 主要性质 | EMT 边界 |
|------|------|----------|----------|
| 前向欧拉 | $x_{n+1}=x_n+h f(t_n,x_n)$ | 一阶、显式、条件稳定 | 通常不适合作为刚性 EMT 网络主积分器 |
| 后向欧拉 | $x_{n+1}=x_n+h f(t_{n+1},x_{n+1})$ | 一阶、L 稳定 | 抑制高频数值振荡，但可能过度阻尼 |
| 梯形法 | $x_{n+1}=x_n+\frac{h}{2}(f_n+f_{n+1})$ | 二阶、A 稳定、非 L 稳定 | 常用于 EMTP 类伴随模型；突变后可能振荡 |
| DIRK | 分阶段隐式求解 | 可设计为 L 稳定和二阶或更高阶 | 每步阶段数增加，非线性元件仍需线性化处理 |
| BDF/Gear | 多步隐式公式 | 适合刚性平滑动态 | 需要启动和历史数据；高阶稳定区域有限 |

对线性测试方程 $\dot{x}=\lambda x$，稳定函数 $R(z)$（$z=\lambda h$）说明积分器如何处理衰减模态。梯形法有

$$
R_{\mathrm{TR}}(z)=\frac{1+z/2}{1-z/2},
$$

当 $z\to-\infty$ 时趋近 $-1$，高频数值模态不会衰减而可能步间换号。后向欧拉有

$$
R_{\mathrm{BE}}(z)=\frac{1}{1-z},
$$

刚性极限下趋近 $0$，因此有强数值阻尼。

## 分类与变体

### 梯形法

梯形法在经典 EMTP 型求解器中常见，因为它可形成简单伴随电路并保持二阶精度。但它的 A 稳定不等于事件后无振荡；开关、故障和分段非线性工作点变化可能使历史源与新状态不一致。

### 后向欧拉与 CDA

后向欧拉常用于初始化、事件后阻尼或临界阻尼调整。它适合消除由积分格式造成的高频数值模态，但作为长期主积分器时可能牺牲高频物理响应。

### DIRK 与 SDIRK

2S-DIRK 和 3S-SDIRK 用多个隐式阶段换取阻尼与精度之间的折中。[[numerical-integration-by-the-2-stage-diagonally]] 支持 2S-DIRK 在 EMT 动态元件中的伴随电路推导；[[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] 讨论了移频 EMT 中三阶段隐式积分的使用。

### BDF/Gear

BDF 类方法适合刚性且相对平滑的状态推进。由于它依赖多步历史，遇到频繁开关、拓扑切换或步长变化时需要重启动、降阶或历史重构。

### 频率匹配与矩阵指数积分

动态相量、移频模型和矩阵指数方法把积分问题与信号频带或状态空间结构结合。它们不应被写成所有 EMT 场景的通用替代方案；适用性取决于模型是否满足窄带、线性分段或包络假设。

## 适用边界与失败模式

- A 稳定只说明线性测试方程左半平面稳定，不保证开关切换、多速率接口或非线性控制系统稳定。
- L 稳定可抑制数值振荡，但也可能压低研究者关心的高频物理暂态。
- 大步长结论必须绑定模型类型、目标频带、故障或开关设置和误差指标。
- 非线性元件、限幅控制和开关拓扑变化会改变雅可比或导纳结构，不能只按线性 L/C 伴随模型判断成本。
- 多阶段方法的矩阵复用通常有条件：线性元件导纳可相同，非线性斜率变化时仍可能需要更新。

## 代表性来源

| 来源 | 支撑内容 | 证据边界 |
|------|----------|----------|
| [[numerical-integration-by-the-2-stage-diagonally]] | 2S-DIRK 在 EMT 中提供二阶框架和刚性极限阻尼，并推导线性/非线性 L/C 等效 | 当前证据不支持固定加速比例；非线性元件仍可能重线性化 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations]] | 2S-DIRK 的 EMT 应用需要补充处理和实现细节 | 不应把积分器本身写成完整求解器 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn]] | 紧凑格式被用于处理 EMT 数值积分和突变问题 | 具体优势需按原文测试系统限定 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas]] | 动态相量积分可按频率特性优化 | 适用对象是动态相量模型，不是任意详细开关 EMT |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] | 移频 EMT 中三阶段隐式积分将大步长与 L 稳定性结合 | 不能外推为所有大步长 EMT 都更快或更准 |

## 与相关页面的关系

- [[discretization-methods]] 说明积分公式如何变成伴随导纳和历史源。
- [[stiff-system-handling]] 聚焦刚性、多时间尺度和事件后局部降阶。
- [[interpolation-method]] 聚焦步长内部事件和接口量重构。
- [[multirate-method]] 讨论不同积分步长之间的耦合和稳定性。
- [[fixed-admittance]] 使用特定离散化设计固定矩阵结构。
- [[trapezoidal-rule]]、[[backward-euler]] 和 [[gear-method]] 是具体积分器细页。

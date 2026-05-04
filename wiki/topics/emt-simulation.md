---
title: "EMT Simulation (电磁暂态仿真)"
type: topic
tags: [emt, electromagnetic-transient, time-domain, simulation, power-system]
created: "2026-05-02"
---

# EMT Simulation (电磁暂态仿真)

## 定义与边界

电磁暂态仿真是对电力系统相域网络、元件微分方程、开关事件和控制系统进行时域求解的仿真范式。它主要用于研究 [[electromagnetic-transient]]、开关暂态、雷电冲击、故障波形、电力电子控制和保护动作等快速过程。

EMT 仿真不是所有动态仿真的最高保真替代品。若研究对象是长期经济调度、慢速频率恢复或市场出清，正序潮流、机电暂态或优化模型可能更合适；若使用平均值模型或等值模型，结论应随模型层级降级。

## EMT 中的作用

EMT 的价值在于保留对相别、瞬时波形、开关时刻、非线性元件和控制采样敏感的动态。典型问题包括：

- [[switching-transient]]、[[lightning-overvoltage]] 和 [[fault-analysis]] 中的峰值、波前、暂态能量和保护判据。
- [[vsc-hvdc]]、[[mmc-model]]、[[facts]]、[[pv-power-plant]] 等电力电子系统的控制交互和限流行为。
- [[frequency-domain-analysis]] 或 [[harmonic-analysis]] 发现风险后，用时域波形交叉验证振荡、谐波和非线性触发。
- [[real-time-simulation]] 与 [[hil-simulation]] 中的控制保护闭环验证。

## 主要分支与机制

- 网络方程：常以 [[nodal-admittance-matrix]] 组织相域节点电压和支路电流，配合伴随电路或状态方程形成离散步进。
- 状态方程：[[state-space-method]] 适合连续状态、控制器和多端口元件建模，可与节点方程组合。
- 数值积分：[[trapezoidal-rule]]、[[backward-euler]] 和其他 [[numerical-integration]] 方法决定数值阻尼、稳定性和事件后振荡风险。
- 开关与非线性：[[ideal-switch-model]]、[[detailed-switch-model]]、[[magnetic-saturation-modeling]] 和非线性迭代决定模型能否反映关键物理过程。
- 多尺度扩展：[[average-value-model]]、[[dynamic-phasor]]、[[multirate-method]]、[[co-simulation]] 和 [[parallel-computing]] 用于在计算负担和保真度之间折中。

## 形式化表达

EMT 步进通常可以写成离散化后的网络代数方程和元件状态更新：

$$
Y_k v_k = i^{\mathrm{hist}}_k + i^{\mathrm{src}}_k,\qquad
x_{k+1}=F_h(x_k,v_k,u_k,s_k)
$$

其中 $Y_k$ 是可能随拓扑或等值改变的节点导纳矩阵，$v_k$ 是节点电压，$i^{\mathrm{hist}}_k$ 是伴随电路历史源，$x_k$ 是元件或控制状态，$s_k$ 表示开关和事件状态。不同 EMT 工具和方法的差别，主要体现在 $Y_k$ 的组装方式、$F_h$ 的积分公式和事件处理策略。

## 适用边界与失败模式

- 时间步长不能用单一经验比例代替验证；需要根据最高关注频率、开关事件、控制采样和数值稳定性选择。
- EMT 详细波形依赖参数质量。线路频变参数、变压器饱和、控制器限幅和保护定值缺失时，结果只能作为场景分析。
- 梯形积分在开关事件和刚性系统中可能产生数值振荡；后向欧拉或阻尼处理会改变高频响应，需要说明取舍。
- 大规模 EMT 可能因初始化、非线性迭代、矩阵重构和事件密度而失败；加速方法必须报告基准和误差边界。

## 代表性来源

- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]] 是 EMT 建模传统的来源入口，适合追踪 EMTP 型时域建模思想。
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 支撑状态空间与节点方法组合的机制讨论。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] 可用于比较伴随电路 EMT 实现的数值差异。
- [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms]] 提醒算法精度需要绑定测试系统和指标，而不是用”高精度”概括。

## 与相关页面的关系

- [[electromagnetic-transient]] 定义现象对象；本页定义仿真范式。
- [[emt-mathematical-foundation]] 更适合承载 KCL/KVL、微分代数方程和离散化推导。
- [[real-time-simulation]] 讨论实时 deadline；它是 EMT 的一种执行约束，不是所有 EMT 的默认形态。
- [[frequency-domain-analysis]] 提供频域识别和阻抗视角；EMT 提供时域非线性和事件验证。

## 形式化表达补充

### 数值积分稳定性

梯形法则的局部截断误差：
$$\tau_n = -\frac{h^3}{12}y^{(4)}(\xi), \quad \xi \in [t_n, t_{n+1}]$$

后向欧拉法的绝对稳定区域覆盖整个左半平面，适合刚性系统。

### 开关事件处理

开关时刻 $t_{sw}$ 的插值：
$$v(t_{sw}) = v(t_n) + \frac{t_{sw} - t_n}{h}(v(t_{n+1}) - v(t_n))$$

临界点检测：$i(t_n) \cdot i(t_{n+1}) < 0$ 表示二极管在区间内导通。

### 误差控制

相对误差和绝对误差控制：
$$\text{err} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}\left(\frac{|y_i - \hat{y}_i|}{\text{atol} + \text{rtol} \cdot |y_i|}\right)^2}$$

## 开放问题

- 如何为黑盒电力电子设备建立既可共享又可验证的 EMT 模型。
- 如何在大规模系统中系统报告模型层级、参数来源、步长、误差和计算性能。
- 如何把频域稳定性、机电暂态和 EMT 波形验证组织成一致的证据链。
- 如何在保证精度的前提下将 EMT 仿真扩展到大规模系统（>10000节点）。
- 如何处理高比例电力电子设备接入带来的新暂态特性。

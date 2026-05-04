---
title: "复数微分方程求解 (Complex Differential Equation Solving)"
type: method
tags: [complex, differential-equation, numerical, solver, impedance, protection]
created: "2026-05-02"
updated: "2026-05-03"
---

# 复数微分方程求解 (Complex Differential Equation Solving)

## 定义与边界

复数微分方程求解是把电压、电流、磁链、阻抗或包络等电气量表示为复变量，并在复数域或等价的实部-虚部增广系统中求解其动态关系的方法集合。它不是一种单一积分器；实际实现通常仍需调用[[methods/trapezoidal-rule.md]]、[[methods/backward-euler.md]]、[[methods/newton-raphson-method.md]]或直接代数解算。

在 EMT Wiki 中，本页覆盖两类使用场景：

- 用复数瞬时量、对称分量或阻抗变量表达保护与故障分析问题。
- 用解析信号、动态相量或频移包络把实数 EMT 变量改写为复变量，再进行离散化和网络接口求解。

本页不把复数表示本身等同于精度提升或计算加速。任何效率、误差或动作时间结论都必须绑定具体论文、算例、步长、滤波器和比较基线。

## EMT 中的作用

复数微分方程的主要作用是把幅值、相位、序分量或频移包络统一放入一个计算变量中，使某些 EMT 后处理或混合建模问题更容易表达。

在保护应用中，复数形式可把等效故障回路中的电压、电流和正序阻抗写成紧凑关系，然后拆成实部和虚部方程求未知参数。[[sources/a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym.md]]记录的代表性做法是：先由短窗傅里叶滤波得到对称分量，再按故障类型构造复数等效故障回路，用实虚部方程求正序阻抗。

在多尺度 EMT 中，复变量常来自解析信号或[[methods/dynamic-phasor.md]]。这类模型把工频或目标频带附近的量搬移为低频包络，有助于表达慢变化分量；但[[sources/revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits.md]]提醒，频移不会消除电路固有暂态模态，步长仍需受目标模态和数值积分误差约束。

## 核心机制

常见形式为

$$
\frac{d\mathbf{z}}{dt}=\mathbf{f}(\mathbf{z},\mathbf{z}^*,t), \quad \mathbf{z}=\mathbf{x}+j\mathbf{y}.
$$

若函数显式依赖共轭项 $\mathbf{z}^*$，通常不能简单套用复解析函数理论，而应转为实部-虚部增广系统：

$$
\frac{d}{dt}
\begin{bmatrix}
\mathbf{x} \\
\mathbf{y}
\end{bmatrix}
=
\begin{bmatrix}
\operatorname{Re}\mathbf{f}(\mathbf{x}+j\mathbf{y},\mathbf{x}-j\mathbf{y},t) \\
\operatorname{Im}\mathbf{f}(\mathbf{x}+j\mathbf{y},\mathbf{x}-j\mathbf{y},t)
\end{bmatrix}.
$$

对线性或线性化系统，复变量也可写为

$$
\dot{\mathbf{z}}=\mathbf{A}\mathbf{z}+\mathbf{B}\mathbf{u}.
$$

经过隐式离散后，求解器面对的是复线性系统或等价的实增广线性系统。若系统含非线性元件或控制器限幅，仍需形成残差并用[[methods/newton-raphson-method.md]]或其他[[methods/iterative-solvers.md]]求解。

## 分类与变体

| 类型 | 机制 | 常见用途 | 证据边界 |
|---|---|---|---|
| 复阻抗/复故障回路方程 | 用复电压、电流和阻抗参数写等效回路 | [[methods/distance-protection.md]]、[[methods/time-domain-impedance-estimation.md]] | 速度和测距精度依赖滤波窗、采样、故障类型和线路模型 |
| 实部-虚部增广 ODE/DAE | 把复方程转成两倍维度的实系统 | 与通用 EMT 求解器或稀疏线性代数接口 | 维度增加可能抵消复数表达的便利性 |
| 解析信号与频移包络 | 通过 Hilbert 变换或积分因子构造复包络 | [[methods/dynamic-phasor.md]]、[[methods/multirate-method.md]] | 适用于目标频带附近分量，不能自动覆盖宽频开关暂态 |
| 复数梯形/伴随模型 | 将复状态方程离散为导纳和历史源 | 频变电缆、动态相量网络、包络模型 | 历史项需随步长和频移频率一致更新 |

## 适用边界与失败模式

复数微分方程适合在变量天然具有相位、频率搬移或序分量含义时使用。若研究目标是三相不平衡瞬时波形、强非线性开关细节或保护装置饱和行为，复数表示只能作为建模层，不应替代完整的 EMT 验证。

常见失败模式包括：

- 把频移后的低频包络误认为所有暂态模态都变慢，导致步长过大。
- 在依赖共轭项的方程中误用复解析导数，遗漏实部-虚部耦合。
- 用单一频率或短窗滤波得到的复量解释宽频暂态。
- 在电流接近零或噪声较大时直接用 $Z=V/I$，造成阻抗轨迹放大误差。
- 把单个保护算例中的动作速度或测距精度外推到不同线路、CT/PT误差、频偏、负荷转移或实际继电器硬件。

## 代表性来源

| 来源 | 复数方程的作用 | 可采信结论 |
|---|---|---|
| [[sources/a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym.md]] | 用对称分量构造复数等效故障回路，并拆成实虚部求正序阻抗 | 可作为“复数微分方程用于数字距离保护阻抗估计”的来源；具体速度和误差需回查原文表图 |
| [[sources/revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits.md]] | 用积分因子解释动态相量，并分析频移后的特征值关系 | 可作为“复包络不会消除固有暂态模态”的边界证据 |
| [[sources/multi-scale-formulation-of-admittance-based-modeling-of-cables.md]] | 将梯形积分和递归卷积改写为解析信号/复变量形式 | 可作为“复变量用于电缆多尺度导纳模型”的来源；定量加速需原文核验 |
| [[sources/shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems.md]] | 以复值动态相量和实虚部 EMT 副本保持接口一致性 | 可作为“多速率接口必须保持复变量结构”的来源 |

## 与相关页面的关系

- [[methods/dynamic-phasor.md]]：复数微分方程在多尺度建模中的重要来源之一；动态相量更强调频移和谐波系数。
- [[methods/time-domain-impedance-estimation.md]]：复数方程常用于阻抗估计，但估计质量受滤波和故障回路模型约束。
- [[methods/symmetrical-components.md]]：保护场景中复数变量常由序分量组合而来。
- [[methods/trapezoidal-rule.md]]与[[methods/backward-euler.md]]：复数状态方程离散化时常用的底层积分规则。
- [[methods/dae-solvers.md]]：复变量若与网络约束耦合，最终通常成为复数或实增广 DAE。

## 修订与证据使用注意事项

- 不应新增“半周波动作”“某采样率下实时”等定量结论，除非明确绑定来源页、原文图表和算例条件。
- 复数方程的优势应写成“表达紧凑”“便于相位/序分量/包络建模”，不应无来源写成“必然更快”或“更高精度”。
- 引用动态相量或移频模型时，应同时说明它们对固有暂态模态和宽频开关过程的限制。

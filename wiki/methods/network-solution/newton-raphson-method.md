---
title: "牛顿-拉夫逊法 (Newton-Raphson Method)"
type: method
tags: [newton-raphson, iterative, power-flow, non-linear, jacobian, convergence]
created: "2026-05-02"
updated: "2026-05-03"
---

# 牛顿-拉夫逊法 (Newton-Raphson Method)


```mermaid
graph TD
    subgraph Ncmp[牛顿-拉夫逊法 (Newton-Raphson Meth…]
        N0[完整牛顿法: 每次迭代更新雅可比]
        N1[修正牛顿法: 多次迭代复用雅可比]
        N2[阻尼牛顿法: 用 $\alpha\Delta\mathb…]
        N3[线搜索/信赖域牛顿法: 控制步长或搜索区域]
        N4[拟牛顿法: 用近似雅可比或低秩更新]
        N5[解耦/快速解耦变体: 利用问题结构简化雅可比]
    end
```


## 定义与边界

牛顿迭代法（Newton-Raphson Method）是求解非线性方程组 $\mathbf{f}(\mathbf{x})=\mathbf{0}$ 的局部迭代方法。它在当前点用一阶泰勒展开构造线性修正方程：

$$
\mathbf{J}(\mathbf{x}^{(k)})\Delta \mathbf{x}^{(k)}
=-\mathbf{f}(\mathbf{x}^{(k)}), \quad
\mathbf{x}^{(k+1)}=\mathbf{x}^{(k)}+\Delta \mathbf{x}^{(k)}.
$$

其中 $\mathbf{J}$ 是雅可比矩阵。牛顿迭代法不是潮流计算、EMT 或 DAE 求解器的全部；它通常只是隐式离散、接口方程、非线性支路或优化 KKT 系统中的非线性求解内核。

本页不保留未绑定来源的“通常若干次迭代收敛”“固定容差”“实时必然可行”等断言。收敛行为必须与初值、雅可比质量、变量尺度、限幅/开关事件和线性求解器共同讨论。

## EMT 中的作用

在 EMT 和混合暂态研究中，牛顿迭代法常用于以下位置：

- 非线性元件伴随模型，如饱和电感、避雷器、开关器件或电力电子控制约束。
- [[dae-solvers]]中的隐式残差方程。
- 机电-电磁或交直流接口的功率、电流、电压不平衡量求解。
- 潮流、稳态初始化和运行点求解，为后续 EMT 仿真提供一致初值。
- 优化、参数辨识和状态估计中的非线性最小二乘或 KKT 方程。

[[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte]]记录了用梯形积分和牛顿线性化把非线性电感转成诺顿伴随支路的做法。[[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model]]记录了 Newton-Raphson 接口算法在交直流混合暂态稳定仿真中的作用。两类来源都支持“牛顿迭代是接口或非线性支路求解内核”，但不支持无条件定量收敛声明。

## 核心机制

对标量方程 $f(x)=0$，牛顿步为

$$
x^{(k+1)}=x^{(k)}-\frac{f(x^{(k)})}{f'(x^{(k)})}.
$$

对多变量问题，核心是线性化残差：

$$
\mathbf{f}(\mathbf{x}^{(k)}+\Delta\mathbf{x})
\approx
\mathbf{f}(\mathbf{x}^{(k)})+
\mathbf{J}(\mathbf{x}^{(k)})\Delta\mathbf{x}.
$$

令近似残差为零得到修正方程。若 $\mathbf{J}$ 非奇异、初值足够接近解且函数足够光滑，牛顿法可表现出快速局部收敛；但在 EMT 中，事件切换、饱和折线、限幅器、离散控制和变量尺度差异常会破坏这些条件。

实际实现通常包含：

1. 计算残差 $\mathbf{f}(\mathbf{x}^{(k)})$。
2. 形成或更新雅可比矩阵。
3. 解线性方程 $\mathbf{J}\Delta\mathbf{x}=-\mathbf{f}$。
4. 选择步长或阻尼系数并更新变量。
5. 检查残差、修正量、物理限值和最大迭代次数。

## 分类与变体

| 变体 | 机制 | 适用场景 | 边界 |
|---|---|---|---|
| 完整牛顿法 | 每次迭代更新雅可比 | 强非线性、收敛要求高的隐式方程 | 雅可比构造和分解成本高 |
| 修正牛顿法 | 多次迭代复用雅可比 | 雅可比变化较慢或分解昂贵的问题 | 收敛阶可能下降，事件后需重建 |
| 阻尼牛顿法 | 用 $\alpha\Delta\mathbf{x}$ 更新 | 初值较差、非线性强或残差震荡 | 阻尼策略需防止过度保守 |
| 线搜索/信赖域牛顿法 | 控制步长或搜索区域 | 工程优化、稳态初始化、病态潮流 | 实现复杂度高，仍可能失败 |
| 拟牛顿法 | 用近似雅可比或低秩更新 | 雅可比难求的问题 | 需验证近似是否破坏接口物理约束 |
| 解耦/快速解耦变体 | 利用问题结构简化雅可比 | 潮流或弱耦合场景 | 不应直接迁移到强耦合 EMT 非线性网络 |

## 适用边界与失败模式

牛顿迭代法适合光滑、局部可线性化且初值合理的非线性方程。EMT 中常见失败模式包括：

- 初值远离物理解，导致残差增大或迭代跳到错误工作区。
- 雅可比奇异、近奇异或尺度差异过大，线性方程求解不稳定。
- 开关、限幅、死区、饱和折线导致残差不可微或分段切换频繁。
- 固定雅可比跨过事件点复用，导致修正方向失效。
- 收敛判据只看数学残差，忽略电压、电流、功率或状态变量的物理可接受性。
- 在实时仿真中最大迭代次数受限，未收敛结果可能被迫进入下一步。

因此，工程页面应写清楚阻尼、重初始化、失败回退、最大迭代处理和与线性求解器的耦合，而不只列出标准公式。

## 代表性来源

| 来源 | 牛顿迭代的角色 | 可采信边界 |
|---|---|---|
| [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte]] | 对非线性电感曲线线性化，形成等效电导和历史电流源 | 可说明非线性伴随模型机制；具体步长、误差和收敛次数需原文核验 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model]] | 在交直流接口处求解功率/电流不平衡 | 可说明混合接口求解思想；定量效率和迭代稳定性不能无来源外推 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt]] | 在多物理域协同仿真中用于刚性非线性方程或光伏模型求解 | 可作为多物理隐式迭代例子；具体容差和步长需查原文 |
| [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]] | 用统一雅可比求解多频混合微电网稳态方程 | 可作为潮流/稳态初始化类牛顿应用 |

## 与相关页面的关系

- [[dae-solvers]]：牛顿迭代通常是隐式 DAE 每步内的非线性求解器。
- [[iterative-solvers]]：更广泛的线性和非线性迭代方法页面。
- [[sparse-matrix-solver]]：牛顿步内线性方程的主要计算内核。
- [[power-flow-calculation]]与[[steady-state-initialization]]：牛顿迭代常用于给 EMT 提供一致初值。
- [[trapezoidal-rule]]：非线性动态元件经隐式梯形离散后常需要牛顿迭代求解。
- [[companion-circuit]]：牛顿线性化后的非线性支路常以伴随导纳和历史源形式进入网络方程。

## 修订与证据使用注意事项

- “局部二次收敛”只能作为数学性质，并需附带条件；不要写成 EMT 工程模型的必然表现。
- 不新增无来源的固定迭代次数、容差、计算延迟或实时能力。
- 若来源页自身含有未核验量化结果，应优先引用 deep-review 的证据边界，而不是复用页面旧表格中的强断言。

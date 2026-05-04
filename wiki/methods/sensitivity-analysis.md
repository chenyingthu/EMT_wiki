---
title: "灵敏度分析 (Sensitivity Analysis)"
type: method
tags: [sensitivity, analysis, parameter, stability, optimization, eigenvalue, participation-factor]
created: "2026-05-02"
---

# 灵敏度分析 (Sensitivity Analysis)

## 定义与边界

灵敏度分析研究模型输出、误差指标或稳定指标随参数变化的局部或全局响应。它可以回答“哪个参数更影响结果”和“沿哪个方向调整最可能改变指标”，但不能单独证明因果机制、参数可辨识性或控制方案有效。

本页聚焦 EMT 方法用途：参数筛选、模型校准、模态解释、控制整定和不确定性排序。它与[[least-squares-method]]、[[parameter-identification]]、[[small-perturbation-linearization]]和[[modal-analysis]]紧密相关。

## EMT 中的作用

EMT 模型的参数可能包括线路频变参数、换流器控制增益、PLL 参数、机器参数、负荷参数、开关器件等效参数和初始化状态。灵敏度分析可用于：

- 在黑盒 EMT 校准前筛选主导参数。
- 解释某个小信号模态为何随控制参数移动。
- 评估稳态初始化误差对启动暂态的影响。
- 为参数扫描、代理模型和不确定性传播提供变量排序。

输出必须绑定指标，例如波形均方误差、阻尼趋势、频率响应幅值、暂态峰值或稳态功率偏差。

## 局部灵敏度

对指标 $y=f(\mathbf{p})$，参数 $p_i$ 的局部灵敏度为

$$
S_i=\frac{\partial y}{\partial p_i}.
$$

常用无量纲形式为

$$
\tilde{S}_i=
\frac{p_i}{y}\frac{\partial y}{\partial p_i},
$$

但当 $p_i$ 或 $y$ 接近零时，该归一化可能失去解释性。有限差分近似为

$$
\frac{\partial y}{\partial p_i}
\approx
\frac{f(p_i+\Delta p_i)-f(p_i-\Delta p_i)}{2\Delta p_i}.
$$

差分步长应结合参数量纲、仿真噪声和事件时间误差选择，不能无条件套用固定比例。

## 模态和特征值灵敏度

对线性化矩阵 $\mathbf{A}(\mathbf{p})$，若特征值 $\lambda_i$ 简单且左右特征向量满足

$$
\mathbf{A}\mathbf{v}_i=\lambda_i\mathbf{v}_i,\quad
\mathbf{w}_i^T\mathbf{A}=\lambda_i\mathbf{w}_i^T,
$$

则

$$
\frac{\partial\lambda_i}{\partial p}
=
\frac{\mathbf{w}_i^T
\frac{\partial\mathbf{A}}{\partial p}
\mathbf{v}_i}
{\mathbf{w}_i^T\mathbf{v}_i}.
$$

该公式只适用于局部线性模型和非重特征值。接近重根、非正规矩阵或强离散化影响时，特征值灵敏度可能非常不稳定，需要用扰动复算和 EMT 小扰动响应核对。

## 全局灵敏度

全局灵敏度把参数看作随机变量，评估输入不确定性对输出方差的贡献。Sobol 一阶指数的常见形式为

$$
S_i=
\frac{\mathrm{Var}_{p_i}
\left(
\mathbb{E}_{\mathbf{p}_{-i}}[y\mid p_i]
\right)}
{\mathrm{Var}(y)}.
$$

总效应指数还包含 $p_i$ 与其他参数的交互贡献。全局灵敏度适合非线性黑盒 EMT，但需要明确采样范围、分布、样本规模和仿真失败处理。

## 工作流

1. 选定指标：先定义输出、误差函数或稳定指标。
2. 确定参数空间：列出范围、单位、相关性和不可调参数。
3. 选择方法：局部导数、有限差分、伴随法、Sobol、Morris 或采样回归。
4. 运行仿真：记录失败样本、事件触发和随机种子。
5. 排序解释：区分一阶贡献、交互贡献和数值噪声。
6. 验证用途：用筛选后的参数做独立校准、复算或控制整定检查。

## 变体

| 变体 | 机制 | 适用场景 | 风险 |
|---|---|---|---|
| 局部差分 | 单参数小扰动复算 | 快速筛查、白盒模型核对 | 只代表当前运行点附近 |
| 解析/自动微分 | 对方程或代码求导 | 可微模型、控制器线性化 | 事件和限幅不可微 |
| 伴随灵敏度 | 一次反向求解多个参数梯度 | 高维参数、少数指标 | 实现复杂，依赖模型方程 |
| Sobol 全局灵敏度 | 方差分解 | 黑盒 EMT 参数筛选 | 采样成本高，依赖参数分布 |
| Morris 筛选 | 随机轨迹初筛 | 大量候选参数 | 结果较粗，需要复核 |

## 适用边界与失败模式

- 灵敏度高不代表参数可被测量唯一识别；多个参数可能产生相似波形。
- 灵敏度低可能只是当前工况不激励该动态，不代表参数永远不重要。
- 大扰动、保护切换、饱和和拓扑变化会让局部导数失去连续性。
- 全局灵敏度结论依赖参数范围和分布；换范围后排序可能改变。
- 把单篇校准算例的主导参数排序外推到所有 EMT 模型是不合规的强断言。

## 代表性证据

- [[data-driven-parameter-calibration-of-power-system-emt-model-based-on-sobol-sensi]] 支撑 Sobol 灵敏度可用于 EMT 黑盒参数校准前的主导参数筛选；其验证范围仍受原文系统、参数范围和误差定义约束。
- [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] 支撑 Floquet 参与因子和模态边界识别路线；适用性限于周期稳态附近。
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]] 支撑通过 EMT 频率扫描观察参数和频域响应关系；频段和扰动设置需要报告。

## 与相关页面的关系

- [[least-squares-method]]：常用灵敏度判断拟合参数是否可辨识。
- [[parameter-identification]]：把灵敏度排序用于参数反演流程。
- [[modal-analysis]]：使用参与因子和留数解释模态参与。
- [[small-perturbation-linearization]]：提供局部灵敏度和特征值灵敏度的线性模型。
- [[steady-state-initialization]]：可分析初值误差对启动暂态的影响。
- [[frequency-scan]]：提供频域响应对参数变化的观测方式。

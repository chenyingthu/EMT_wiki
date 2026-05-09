---
title: "最小二乘法 (Least Squares Method)"
type: method
tags: [least-squares, parameter-estimation, curve-fitting, optimization, system-identification]
created: "2026-05-02"
---

# 最小二乘法 (Least Squares Method)


```mermaid
graph TD
    subgraph Ncmp[最小二乘法 (Least Squares Method)]
        N0[普通最小二乘: 等权残差平方和]
        N1[加权最小二乘: 按测量方差或工程关注加权]
        N2[正则化最小二乘: 加入参数惩罚或平滑约束]
        N3[约束最小二乘: 显式限制参数范围或符号]
        N4[鲁棒最小二乘: 使用非二次损失或迭代重加权]
    end
```


## 定义与边界

最小二乘法通过最小化残差平方和来估计模型参数。它是 EMT 参数辨识、频响拟合、状态估计、模型校准和曲线拟合中的基础数值方法，但不是“参数一定可辨识”或“拟合结果一定物理正确”的保证。

本页关注方法结构、求解流程和 EMT 证据边界。涉及黑盒 EMT 校准时，还需要配合[[sensitivity-analysis]]、[[parameter-identification]]和独立波形验证。

## EMT 中的作用

在 EMT wiki 语境中，最小二乘法常用于：

- 用频率采样点拟合导纳、阻抗或传递函数，服务[[vector-fitting]]和[[partial-fraction-expansion]]。
- 从 EMT 小扰动响应估计状态空间、阻抗或控制器参数。
- 让模型输出波形与录波、测试或高保真仿真结果对齐。
- 在[[state-estimation]]或参数校准中处理带噪声的测量方程。

这些用途都必须报告输入数据、误差定义、权重、参数范围和验证工况。单一误差指标下降不等于模型机制正确。

## 核心形式

给定观测 $\mathbf{y}\in\mathbb{R}^n$ 和模型 $\hat{\mathbf{y}}=\mathbf{f}(\boldsymbol{\beta})$，最小二乘问题为

$$
\min_{\boldsymbol{\beta}}\; J(\boldsymbol{\beta})
=\|\mathbf{r}(\boldsymbol{\beta})\|_2^2
=\sum_{i=1}^{n} r_i(\boldsymbol{\beta})^2,
$$

其中 $r_i=y_i-f_i(\boldsymbol{\beta})$。

线性模型 $\mathbf{y}=\mathbf{X}\boldsymbol{\beta}+\boldsymbol{\epsilon}$ 的正规方程为

$$
\mathbf{X}^T\mathbf{X}\hat{\boldsymbol{\beta}}
=\mathbf{X}^T\mathbf{y}.
$$

若 $\mathbf{X}$ 满列秩，

$$
\hat{\boldsymbol{\beta}}
=
(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}.
$$

实际计算通常不显式求逆，而用 QR、SVD 或带正则化的线性求解。

## 加权与正则化

测量精度不同或频段重要性不同可使用加权最小二乘：

$$
\min_{\boldsymbol{\beta}}
(\mathbf{y}-\mathbf{X}\boldsymbol{\beta})^T
\mathbf{W}
(\mathbf{y}-\mathbf{X}\boldsymbol{\beta}).
$$

若参数病态或数据不足，可加入正则化，例如

$$
\min_{\boldsymbol{\beta}}
\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|_2^2
+\lambda\|\mathbf{L}\boldsymbol{\beta}\|_2^2.
$$

$\lambda$ 和 $\mathbf{L}$ 是建模选择，必须说明物理含义或选择规则；不应把正则化后的平滑结果直接等同于真实参数。

## 非线性最小二乘

非线性 EMT 模型常写成

$$
\min_{\boldsymbol{\beta}}\|\mathbf{r}(\boldsymbol{\beta})\|_2^2.
$$

在当前参数 $\boldsymbol{\beta}_k$ 附近线性化残差：

$$
\mathbf{r}(\boldsymbol{\beta}_k+\Delta\boldsymbol{\beta})
\approx
\mathbf{r}_k+\mathbf{J}_k\Delta\boldsymbol{\beta}.
$$

Gauss-Newton 步求解

$$
\min_{\Delta\boldsymbol{\beta}}
\|\mathbf{r}_k+\mathbf{J}_k\Delta\boldsymbol{\beta}\|_2^2,
$$

Levenberg-Marquardt 类方法则加入阻尼项来改善远离解时的稳定性。黑盒 EMT 仿真若无法给出雅可比，只能用差分、代理模型或无导数优化；这会显著增加证据边界。

## 求解流程

1. 定义参数：列出可调参数、单位、范围、物理约束和固定参数。
2. 定义残差：说明是波形点误差、频域误差、功率误差、事件时间误差还是组合指标。
3. 缩放和加权：避免量纲差异支配目标函数。
4. 选择求解器：线性问题优先 QR/SVD；非线性问题需初值、收敛准则和失败处理。
5. 检查可辨识性：查看秩、奇异值、参数相关性和灵敏度。
6. 独立验证：在未参与拟合的工况、扰动或频段上比较结果。

## 变体

| 变体 | 机制 | EMT 用途 | 注意事项 |
|---|---|---|---|
| 普通最小二乘 | 等权残差平方和 | 基础曲线拟合 | 对异常值敏感 |
| 加权最小二乘 | 按测量方差或工程关注加权 | 频响拟合、状态估计 | 权重来源要说明 |
| 正则化最小二乘 | 加入参数惩罚或平滑约束 | 病态拟合、降阶 | 可能引入偏差 |
| 约束最小二乘 | 显式限制参数范围或符号 | 物理参数估计 | 约束不当会掩盖模型错误 |
| 鲁棒最小二乘 | 使用非二次损失或迭代重加权 | 含异常录波数据 | 损失函数影响解释 |

## 适用边界与失败模式

- 设计矩阵秩亏、参数相关或灵敏度很低时，最小残差解可能不是唯一物理解。
- 频域拟合误差小，不代表时域故障波形、无源性或稳定性可靠。
- 未缩放变量会让高量级信号主导目标函数。
- 用同一数据集拟合和验证会高估模型可信度。
- 黑盒 EMT 校准中的局部最小、噪声和事件时间错位会使参数解释失真。

## 代表性证据

- [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] 支撑 VF 中固定极点后的留数识别可落入线性最小二乘框架；其数值效果应绑定原文拟合对象。
- [[data-driven-parameter-calibration-of-power-system-emt-model-based-on-sobol-sensi]] 支撑黑盒 EMT 参数校准中先用灵敏度筛选再做概率/优化反演的路线；当前 wiki 证据不足以推广为所有 EMT 模型均高效。
- [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation]] 可作为从扰动响应提取导纳模型的相关证据；拟合质量依赖注入信号、窗口和频段。

## 与相关页面的关系

- [[sensitivity-analysis]]：判断哪些参数值得估计。
- [[parameter-identification]]：更广义的参数反演和辨识流程。
- [[vector-fitting]]：以最小二乘为核心的频域有理拟合方法。
- [[partial-fraction-expansion]]：固定极点后求留数的表示形式。
- [[state-estimation]]：加权最小二乘在电力系统测量融合中的应用。
- [[small-perturbation-linearization]]：非线性最小二乘迭代中常用局部线性化。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[noda-a-binary-frequency-region-partitioning-algorithm-for-the-identification-of-|Noda | A Binary Frequency-Region Partitioning Algorithm for ]] | 2007 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[locating-arc-faults-on-coupling-two-parallel-transmission-lines-using-the-novel-|Locating arc faults on coupling two parallel transmission li]] | 2023 |
| [[electromechanical-transientelectromagnetic-transient-hybrid-simulation-method-co|Electromechanical transientelectromagnetic transient hybrid ]] | 2026 |

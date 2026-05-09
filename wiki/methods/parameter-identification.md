---
title: "参数辨识方法 (Parameter Identification)"
type: method
tags: [parameter-identification, system-identification, least-squares, optimization, emt-modeling]
created: "2026-05-04"
---

# 参数辨识方法 (Parameter Identification)


```mermaid
graph TD
    subgraph Ncmp[参数辨识方法 (Parameter Identifica…]
        N0[线性最小二乘: 回归矩阵和观测向量]
        N1[加权/递推最小二乘: 带权数据流]
        N2[频域拟合: 阻抗/导纳频率扫描]
        N3[时域模态辨识: 脉冲、阶跃或故障响应]
        N4[物理曲线辨识: 电压、电流、磁链或位移]
    end
```


## 定义与边界

参数辨识方法（Parameter Identification）是在给定模型结构、输入激励和观测数据的条件下估计模型参数的技术集合。EMT 中常见的待辨识对象包括线路频率相关参数、变压器磁化曲线、外部网络端口导纳、保护算法中的故障参数，以及由测量或仿真波形提取的模态参数。

参数辨识不是“从任意数据自动得到真实模型”。它至少需要明确模型结构、激励覆盖范围、观测量、噪声处理和误差指标。若模型结构错误、参数不可辨识或激励未覆盖关键频段，优化残差很小也可能得到物理上错误的参数。

## EMT 中的作用

参数辨识在 EMT 中承担三类角色：现场模型校准、黑箱端口建模和暂态后处理。现场校准用于把设备试验或故障记录转成可仿真的参数；黑箱建模用于 [[fdne-model]]、[[transmission-line-model]]、[[cable-model]] 等频率相关模型；暂态后处理则通过 [[prony-analysis]]、矩阵束或最小二乘估计振荡频率、阻尼和故障距离。

它和模型验证的关系是互补的：辨识给出候选参数，验证检查这些参数在未参与拟合的工况、频段或测试系统中是否仍然成立。

## 核心机制

一般辨识问题可写为 $y(t)=f(u(t),\boldsymbol{\theta})+\epsilon(t)$，其中 $\boldsymbol{\theta}$ 是待估参数，$u(t)$ 是激励，$y(t)$ 是观测量，$\epsilon(t)$ 表示噪声、模型误差和数值误差。最小二乘形式为 $\min_{\boldsymbol{\theta}}\sum_n\|y_{\text{meas}}(t_n)-y_{\text{model}}(t_n,\boldsymbol{\theta})\|^2$。

线性回归可形成 $\hat{\boldsymbol{\theta}}=(\mathbf{\Phi}^T\mathbf{\Phi})^{-1}\mathbf{\Phi}^T\mathbf{y}$，但只有在 $\mathbf{\Phi}$ 条件良好且列满秩时才可靠。非线性辨识通常需要迭代优化、参数约束和多初值检查。频域辨识把阻抗、导纳或传递函数采样拟合为参数模型；时域辨识则直接使用暂态波形、脉冲响应或投切记录。

## 分类与变体

| 类型 | 典型输入 | 输出 | EMT 用途 |
|------|----------|------|----------|
| 线性最小二乘 | 回归矩阵和观测向量 | 电阻、电感、线性模型参数 | 简化支路和保护方程参数 |
| 加权/递推最小二乘 | 带权数据流 | 在线或分段参数 | 实时校准、测量噪声抑制 |
| 频域拟合 | 阻抗/导纳频率扫描 | 极点、留数、宽频参数 | [[vector-fitting]]、FDNE、线路/电缆模型 |
| 时域模态辨识 | 脉冲、阶跃或故障响应 | 极点、阻尼、频率 | [[prony-analysis]]、矩阵束、振荡识别 |
| 物理曲线辨识 | 电压、电流、磁链或位移 | 饱和曲线、磁滞参数 | [[transformer-model]] 和非线性设备校准 |

## 适用边界与失败模式

- 可辨识性：不同参数组合可能产生近似相同的端口响应，需检查矩阵秩、灵敏度或置信区间。
- 激励充分性：未被激励的模态和频段不能从数据中可靠恢复。
- 数据质量：积分漂移、传感器相位误差、采样同步和滤波延迟会直接进入参数估计。
- 模型结构：用线性模型拟合饱和、电弧或限幅控制，只能代表局部工作点。
- 数值外推：原页面中若干”误差 <0.5%””提升 3 倍”等数字只有在绑定具体论文、测试频段和指标时才可使用；本页不把它们写成通用精度。

### 可辨识性条件

| 条件 | 描述 | 检验方法 |
|------|------|----------|
| 结构可辨识性 | 模型结构允许参数唯一确定 | 灵敏度矩阵满秩 |
| 激励充分性 | 输入信号覆盖待辨识频段 | 持续激励条件 |
| 数值可辨识性 | 参数估计条件良好 | 条件数检查 |
| 物理合理性 | 参数在物理可行范围内 | 约束优化 |

### 常见问题与对策

| 问题 | 原因 | 对策 |
|------|------|------|
| 参数相关性 | 多个参数影响相同输出 | 重新参数化、固定部分参数 |
| 局部极小值 | 非线性优化多峰 | 多初值、全局优化算法 |
| 过拟合 | 模型复杂度高、数据不足 | 正则化、交叉验证 |
| 噪声敏感 | 信噪比低 | 滤波、加权、贝叶斯方法 |
| 数值不稳定 | 矩阵病态 | 正则化、QR分解、SVD |

## 代表性来源

| 来源或论文线索 | 支撑内容 | 证据边界 |
|----------------|----------|----------|
| Determination of saturation curve from transient measurements | 变压器投切暂态可用于饱和曲线辨识 | 结果依赖原文变压器、采样和校准方法 |
| On-site measurement of hysteresis curve using DC excitation | 直流励磁可用于现场磁滞曲线测量 | 不能替代所有高压交流试验场景 |
| New procedure to derive transmission-line parameters | 单端频域测量可反演线路参数 | 需满足原文关于频率、多值性和线路假设的限制 |
| Distance protection based on parameter identification | 故障距离和过渡电阻可表述为辨识问题 | 只支撑原文算法和故障设置 |
| RTDS-TSA hybrid simulation with FDNE | FDNE 可通过频域采样和有理拟合得到接口参数 | 实时可用性取决于模型阶数和无源性 |

## 与相关页面的关系

- [[vector-fitting]]：参数辨识在频域宽频模型中的典型算法，输出极点、留数和直接项。
- [[prony-analysis]]：时域模态辨识方法，适合从暂态序列中提取阻尼和频率。
- [[state-space-method]]：辨识结果常转成状态空间或递推滤波器参与 EMT 步进。
- [[frequency-dependent-modeling]]：线路、电缆和外部网络的频率相关参数通常需要辨识或拟合。
- [[transformer-model]]：磁化曲线、漏抗和饱和参数辨识必须区分测试工况和工程运行工况。

## 形式化表达

### 最小二乘辨识

线性回归形式的参数估计：

$$\hat{\boldsymbol{\theta}} = (\mathbf{\Phi}^T\mathbf{\Phi})^{-1}\mathbf{\Phi}^T\mathbf{y}$$

其中 $\mathbf{\Phi}$ 为回归矩阵，$\mathbf{y}$ 为观测向量。

加权最小二乘：
$$\hat{\boldsymbol{\theta}} = (\mathbf{\Phi}^T\mathbf{W}\mathbf{\Phi})^{-1}\mathbf{\Phi}^T\mathbf{W}\mathbf{y}$$

其中 $\mathbf{W}$ 为权重矩阵，反映各数据点的可信度。

### 递推最小二乘

在线更新公式：

$$\hat{\boldsymbol{\theta}}_k = \hat{\boldsymbol{\theta}}_{k-1} + \mathbf{K}_k(y_k - \mathbf{\phi}_k^T\hat{\boldsymbol{\theta}}_{k-1})$$

$$\mathbf{K}_k = \frac{\mathbf{P}_{k-1}\mathbf{\phi}_k}{\lambda + \mathbf{\phi}_k^T\mathbf{P}_{k-1}\mathbf{\phi}_k}$$

$$\mathbf{P}_k = \frac{1}{\lambda}(\mathbf{P}_{k-1} - \mathbf{K}_k\mathbf{\phi}_k^T\mathbf{P}_{k-1})$$

其中 $\lambda$ 为遗忘因子（$0 < \lambda \leq 1$），控制历史数据权重。

### 非线性优化

非线性最小二乘目标函数：

$$J(\boldsymbol{\theta}) = \sum_{n=1}^{N} \|y_{\text{meas}}(t_n) - y_{\text{model}}(t_n, \boldsymbol{\theta})\|^2$$

Gauss-Newton迭代：
$$\boldsymbol{\theta}^{(k+1)} = \boldsymbol{\theta}^{(k)} - (\mathbf{J}^T\mathbf{J})^{-1}\mathbf{J}^T\mathbf{r}$$

其中 $\mathbf{J}$ 为Jacobi矩阵，$\mathbf{r}$ 为残差向量。

### 置信区间估计

参数估计的协方差矩阵：
$$\text{Cov}(\hat{\boldsymbol{\theta}}) = \sigma^2(\mathbf{\Phi}^T\mathbf{\Phi})^{-1}$$

第 $i$ 个参数的 $95\%$ 置信区间：
$$\hat{\theta}_i \pm 1.96\sqrt{\text{Cov}_{ii}}$$

---
title: "递归卷积 (Recursive Convolution)"
type: method
tags: [recursive-convolution, frequency-dependent, transmission-line, transient-analysis]
created: "2026-05-04"
---

# 递归卷积 (Recursive Convolution)


```mermaid
graph TD
    subgraph Ncmp[递归卷积 (Recursive Convolution)]
        N0[频域特性: 可用有理函数近似或有指数衰减形式]
        N1[时间步长: $\Delta t \ll \min(\ta…]
        N2[线性时不变: 仅适用于线性时不变元件]
        N3[精度要求: 需验证有理近似的频域精度]
    end
```


## 定义与边界

递归卷积是一种用于电磁暂态(EMT)仿真中计算频变参数元件历史项的数值方法。它通过建立当前时刻与过去时刻的递推关系，避免存储完整的历史数据，从而显著降低存储需求和计算复杂度。

在EMT仿真中，递归卷积主要应用于：
- 频变参数输电线路模型的时域实现
- 频变阻抗元件的暂态响应计算
- 多导体传输线模域模型的历史项更新

**边界限定**：本方法不适用于非线性元件、时变参数系统或需要完整历史信息的频域分析。

## EMT中的作用

递归卷积解决了频变模型在时域仿真中的关键计算瓶颈：

- **存储效率**：将 $O(N)$ 存储需求降为 $O(1)$，其中 $N$ 为时间步数
- **计算效率**：每步计算复杂度从 $O(N)$ 降至 $O(1)$
- **数值稳定性**：通过适当的极点-留数分解保证递推稳定性
- **精度保持**：在保持频变特性精度的同时实现实时或近实时仿真

## 主要分支与机制

### 1. 基于指数函数的递归卷积

适用于具有有理函数频变特性的元件，通过极点-留数展开：
$$Y(s) = \sum_{i=1}^{n} \frac{k_i}{s-p_i}$$

### 2. 基于特性阻抗的递归卷积

用于传输线模型，将特性阻抗的历史项表示为：
$$h(t) = \sum_{i=1}^{m} A_i e^{-\alpha_i t}$$

### 3. 模态域递归卷积

在多导体线路分析中，对各模态分别应用递归卷积：
$$i_k(t) = \sum_{j=1}^{n} Y_{kj}(0) v_j(t) + \sum_{j=1}^{n} h_{kj}(t)$$

## 形式化表达

### 基本递推公式

对于具有指数衰减特性的核函数，递归卷积的历史项可表示为：

$$
h(t) = \sum_{i=1}^{n} h_i(t)
$$

其中各分量满足递推关系：

$$
h_i(t) = k_i x(t) + e^{-\Delta t/\tau_i} h_i(t-\Delta t)
$$

式中：
- $k_i$ 为第 $i$ 个留数
- $\tau_i$ 为第 $i$ 个时间常数
- $\Delta t$ 为仿真时间步长
- $x(t)$ 为当前输入量

### 频变导纳的时域实现

对于频变导纳 $Y(s)$，端口电流可表示为：

$$
i(t) = Y_0 v(t) + \sum_{k=1}^{K} i_k(t)
$$

其中历史电流分量满足：

$$
i_k(t+\Delta t) = \alpha_k i_k(t) + \beta_k [v(t+\Delta t) + v(t)]
$$

系数由极点 $p_k$ 和留数 $r_k$ 决定：

$$
\alpha_k = e^{p_k \Delta t}, \quad \beta_k = \frac{r_k}{p_k \Delta t}(1-\alpha_k)
$$

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 |
|------|------|
| 频域特性 | 可用有理函数近似或有指数衰减形式 |
| 时间步长 | $\Delta t \ll \min(\tau_i)$ 以保证数值稳定性 |
| 线性时不变 | 仅适用于线性时不变元件 |
| 精度要求 | 需验证有理近似的频域精度 |

### 失效边界

- **极点位置**：当极点实部接近零（长时程）或虚部很大（高频振荡）时，递推可能不稳定
- **刚性系统**：时间常数跨度很大（$\tau_{\max}/\tau_{\min} > 10^6$）时，可能产生数值误差
- **非线性效应**：不适用于饱和、电弧等非线性现象
- **多端口耦合**：强耦合多导体系统需要特殊处理交叉模态

### 关键假设

1. 频变特性可用有限阶有理函数充分近似
2. 仿真时间步长足够小以满足稳定性条件
3. 系统在工作点附近可线性化

## 代表性来源

### 经典文献

- Marti, J.R., "Accurate Modelling of Frequency-Dependent Transmission Lines in Electromagnetic Transient Simulations," *IEEE Trans. Power Apparatus and Systems*, 1982. - 递归卷积在输电线路中的开创性应用
- Morched, A., et al., "A Frequency-Dependent Transmission Line Model for EMTP," *IEEE Trans. Power Delivery*, 1987. - 多导体线路的递归卷积实现

### 应用案例

- [[frequency-dependent-line-model]] - 频变线路模型的递归卷积实现
- J.Marti 模型的递归卷积基础
- [[transmission-line-model]] - 输电线路建模中的递归卷积应用

### 数值方法

- [[vector-fitting]] - 用于获取有理近似的矢量拟合方法
- [[numerical-integration]] - 递归卷积与数值积分的配合
- [[modal-analysis]] - 模态分解与递归卷积的结合

## 与相关页面的关系

- [[frequency-dependent-modeling]] - 频变建模的综述
- [[transmission-line-model]] - 输电线路模型
- [[vector-fitting]] - 频变特性有理近似方法
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间实现替代方案

## 开放问题

- 如何在保持递归卷积效率的同时提高极低频精度
- 非均匀传输线（如架空线-电缆混合）的递归卷积统一处理
- 与多速率仿真的兼容性优化

## 参考标准

- IEEE Std. 1313.2 - 输电线路暂态建模导则
- CIGRE TB 696 - 频变参数建模与仿真

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。如有更新或修正，请参考最新研究进展。*

---
title: "指数积分器 (Exponential Integrator)"
type: method
tags: [exponential-integrator, numerical-integration, state-space, gpu, parallel-computation, stability]
created: "2026-05-10"
---

# 指数积分器 (Exponential Integrator)

## 定义与边界

指数积分器是一类利用矩阵指数函数 \(e^{Ah}\) 或其 \(\varphi\) 函数精确积分线性部分的数值积分方法。与梯形法、后向欧拉等经典 EMTP 积分器不同，指数积分器通过解析处理系统矩阵的刚性模态，在较大步长下仍保持数值稳定性，尤其适用于开关级电力电子仿真和含多时间尺度的状态空间 EMT 求解。

本页关注指数积分的基本原理、L 稳定性优势及其在 EMT 仿真中的实现框架。相关的状态空间建模基础见 [[state-space-method]]；基于指数积分的 GPU 加速策略见 [[gpu-accelerated-simulation]]；传统积分器对比见 [[numerical-integration]]。

## EMT 中的作用

指数积分器在 EMT 仿真中的独特价值来自其对刚性系统的处理能力：

- 对线性系统 \(\dot{x}=Ax\)，指数积分给出 \(x(t+h)=e^{Ah}x(t)\)，在任意步长下精确（与 A 的刚性程度无关）。
- 对含开关拓扑变化的电力电子系统，高阶指数积分器具备 L 稳定性，可完全消除梯形法在开关事件处产生的数值振荡。
- 指数积分的计算核可分解为规则矩阵-向量操作，天然适配 GPU SIMT 并行架构，实现跨时间步并行（parallel-rate）和步内运算并行的双重加速。
- 矩阵指数 \(e^{Ah}\) 和 \(\varphi\) 函数可针对每种开关拓扑预计算，在主循环前完成，大幅降低在线计算负载。

## 核心机制

### 线性系统的精确解

对线性状态空间方程

$$
\dot{x}(t) = A x(t) + B u(t)
$$

其精确解为

$$
x(t+h) = e^{Ah} x(t) + \int_0^h e^{A(h-\tau)} B u(t+\tau) \, d\tau
$$

其中 \(e^{Ah}\) 是矩阵指数。线性部分的动态被精确积分，唯一近似来自输入 \(u(t)\) 在积分区间内的变化。

### \(\varphi\) 函数与输入积分

为简化输入项的数值实现，引入 \(\varphi\) 函数：

$$
\varphi_0(z) = e^z, \quad \varphi_1(z) = \frac{e^z - 1}{z}, \quad \varphi_k(z) = \frac{\varphi_{k-1}(z) - \varphi_{k-1}(0)}{z}
$$

当输入 \(u(t)\) 在步长内为常数或多项式时，积分项可表示为这些 \(\varphi\) 函数与输入的组合。例如，对指数 Euler 公式：

$$
x_{n+1} = x_n + h \varphi_1(hA)\left(A x_n + g(t_n, x_n)\right)
$$

其中 \(g(t,x)\) 包含非线性和控制项。

### 并行率（Parallel-Rate）计算

高阶指数积分器的核心优势在于跨时间步并行：由于 \(e^{Ah}\) 在拓扑不变时不变，多个离散步的状态更新可同时计算。对 \(k\) 个并行步：

$$
\begin{bmatrix} x_{n+1} \\ x_{n+2} \\ \vdots \\ x_{n+k} \end{bmatrix} =
F\left( \begin{bmatrix} x_n \\ x_{n+1} \\ \vdots \\ x_{n+k-1} \end{bmatrix} \right)
$$

宏观时间维度上并行计算多个离散时间步的状态更新，微观步内维度上并行化矩阵-向量运算，形成双重并行加速。

## 分类与变体

### 指数 Euler 公式
一阶格式，结构简单，适合作为 GPU 并行化的基础算子：计算核主要为稀疏矩阵-向量乘法和 \(h\varphi_1(hA)\) 与向量的乘法，均可映射到 GPU SIMT 架构。

### 高阶指数积分格式

高阶格式通过纳入更多 \(\varphi\) 函数项或采用多阶段格式提升精度，同时保持 L 稳定性和绝对稳定性。在电力电子系统仿真中，高阶格式可在保证精度的前提下支持更大时间步长，从步数层面减少总计算量。

### 分裂指数积分（Splitting Exponential Integrator）

将系统矩阵分解为常数部分 \(A_1\) 和开关相关时变部分 \(A_2(s)\)，通过指数分裂公式近似：

$$
e^{h(A_1+A_2)} \approx \prod_{i} e^{\alpha_i h A_1} e^{\beta_i h A_2}
$$

常数部分矩阵指数可复用，开关相关部分仅在拓扑变化时更新，避免对完整时变矩阵反复求指数。

## 相关方法

- [[state-space-method]] — 指数积分的基础建模框架
- [[numerical-integration]] — 传统积分方法对比
- [[gpu-accelerated-simulation]] — GPU 并行加速实现
- [[companion-circuit]] — 传统 EMTP 伴随电路方法
- [[stiff-system-handling]] — 刚性系统处理策略

## 相关模型

- [[power-electronics-modeling]] — 电力电子变换器开关级模型
- [[dfig-model]] — 大规模风电场 EMT 模型

## 相关主题

- [[parallel-computing]]
- [[numerical-integration-methods]]
- [[large-scale-system-simulation]]

## 代表性来源

- Paull 等 — GPU Parallel-Rate Exponential Integrator Algorithm for Efficient Simulation of Power Electronic Systems (2026)
- 赵金利等 — 面向指数积分方法的电磁暂态仿真 GPU 并行算法 (2018)
- Fu 等 — Splitting State-Space Method for Converter-Integrated Power Systems EMT Simulations (2025)
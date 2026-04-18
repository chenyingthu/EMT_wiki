---
title: "Huang 等 | A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['ibg']
created: "2026-04-13"
sources: ["EMT_Doc/01/Huang 等 - 2025 - A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso.pdf"]
---

# Huang 等 | A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso

**作者**: 
**年份**: 2025
**来源**: `01/Huang 等 - 2025 - A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems With Inverter-Based Reso.pdf`

## 摘要

—As inverter-based resources (IBRs) penetrate power systems, the dynamics become more complex, exhibiting multiple timescales, including electromagnetic transient (EMT) dynamics of power electronic controllers and electromechanical dynamics of synchronous generators. Consequently, the power system model becomes highly stiff, posing a challenge for efficient simulation using existing methods that focus on dynamics within a single timescale. This paper proposes a Heterogeneous Multiscale Method for highly efficient multi-timescale simulation of a power system represented by its EMT model. The new method alternates between the microscopic EMT model of the system and an automatically reduced macroscopic model, varying the step size accordingly to achieve significant acceleration while maintain

## 核心贡献


- 提出异构多尺度框架，实现EMT微观模型至宏观模型的在线自动降阶
- 引入核卷积方法近似宏观动态，无需显式降阶即可平滑衔接微宏观过程
- 结合半解析解法构建变步长机制，动态跳过非关键微观动态并保留关键暂态


## 使用的方法


- [[异构多尺度方法-hmm|异构多尺度方法(HMM)]]
- [[半解析解法-sas|半解析解法(SAS)]]
- [[变步长求解器|变步长求解器]]
- [[核卷积近似|核卷积近似]]
- [[微分变换|微分变换]]
- [[在线自动降阶|在线自动降阶]]


## 涉及的模型


- [[逆变器型资源-ibr|逆变器型资源(IBR)]]
- [[同步发电机|同步发电机]]
- [[全阶emt网络模型|全阶EMT网络模型]]
- [[ieee-39节点系统|IEEE 39节点系统]]
- [[两区域系统|两区域系统]]


## 相关主题


- [[多时间尺度仿真|多时间尺度仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[高渗透率ibr电网|高渗透率IBR电网]]
- [[刚性微分方程求解|刚性微分方程求解]]
- [[高效时域仿真|高效时域仿真]]


## 主要发现


- 在IEEE 39节点等系统中验证，算法在保持快慢动态精度的同时实现显著加速
- 半解析变步长机制有效跳过非关键微观暂态，大幅提升长时段仿真计算效率
- 理论严格证明了精度、复杂度与加速比的定量关系，确保多尺度仿真数值稳定



## 方法细节

### 方法概述

提出一种基于异构多尺度方法(HMM)的电力系统电磁暂态(EMT)高效仿真框架。该方法针对高渗透率逆变器型资源(IBR)电网中存在的强刚性多时间尺度问题，在微观全阶EMT模型与自动降阶的宏观模型之间交替求解。通过核卷积方法在线近似宏观动态，无需显式推导降阶模型即可实现微宏观过程的平滑衔接。结合半解析解法(SAS)构建自适应变步长机制，在耗散性暂态衰减或振荡进入稳态后动态放大步长，跳过非关键微观动态，同时保留关键EMT暂态与机电动态的精度，实现计算效率的显著提升。

### 数学公式


**公式1**: $$\begin{cases} \dot{x}^I = f^I(x^I, x^{II}, t) \\ \epsilon \dot{x}^{II} = f^{II}(x^I, x^{II}, t) \end{cases}$$

*双时间尺度刚性ODE系统模型，$x^I$为慢变状态（同步发电机机电动态），$x^{II}$为快变状态（IBR控制器与网络EMT动态），$\epsilon$为区分时间尺度的非奇异矩阵*


**公式2**: $$\dot{u} = \bar{f}(u, t)$$

*宏观降阶模型，聚焦于$\|\epsilon\| \to 0$时的慢速动态演化，用于长时间尺度高效推进*


**公式3**: $$\bar{f}(t) = \lim_{\delta \to 0} \lim_{\|\epsilon\| \to 0} \frac{1}{\delta} \int_t^{t+\delta} f(x, \tau) d\tau$$

*基于核卷积的宏观有效力场估计公式，通过微观轨迹的时间平均在线获取宏观动态，避免显式降阶与黑盒模型处理难题*


### 算法步骤

1. 初始化全阶EMT微观模型状态向量$x$，设定初始微秒级步长与时间尺度分离阈值

2. 实时计算系统雅可比矩阵特征值，识别快变耗散/振荡动态与慢变机电动态的分离状态，评估刚性比

3. 当快变暂态未衰减或处于强非线性切换期时，执行微观过程(Micro-process)，采用固定微秒级小步长精确求解刚性ODE

4. 当耗散性EMT暂态衰减或振荡达到稳态后，触发宏观过程(Macro-process)，利用核卷积方法从微观轨迹中在线估计宏观向量场$\bar{f}(u,t)$

5. 结合半解析解法(SAS)动态调整步长，在宏观尺度下采用大步长推进仿真，跳过非关键高频细节，降低计算负担

6. 在微宏观模型间建立双向状态映射与同步机制，当系统再次遭遇扰动或关键暂态触发时，自动无缝切换回微观模型

7. 循环执行交替求解直至仿真结束，输出覆盖微秒至百秒级全时间尺度的高精度动态响应


### 关键参数

- **时间尺度分离矩阵**: \epsilon (特征值接近0，用于数学上区分快慢动态)

- **系统刚性比**: O(\|\epsilon^{-1}\|) \approx 10^8

- **仿真时间跨度**: 10^{-6} s (EMT) 至 10^2 s (机电/准稳态)

- **次同步振荡频段**: 5-60 Hz

- **核函数**: K_{p,q} \in K_{p,q}(I) (用于平滑微宏观过渡与动态平均)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 两区域系统(Two-area system) | 验证HMM框架在基础多机系统中的微宏观交替求解能力，成功捕捉机电振荡与IBR控制器EMT动态的耦合过程，时间跨度覆盖10^{-6} s至10^2 s | 相比传统固定步长EMT求解器，在保持相同精度的前提下，计算步数减少约85%以上，有效克服10^8刚性比带来的数值稳定性限制 |

| IEEE 39节点系统 | 在详细EMT模型下测试，算法自动识别时间尺度间隙，动态调整步长，完整记录故障后微秒级开关暂态至数十秒级机电振荡全过程，次同步振荡(5-60 Hz)波形无失真 | 实现显著加速，关键动态误差<0.1%，仿真耗时较传统全阶EMT降低约90%，验证了在线自动降阶与核卷积近似的工程有效性 |

| 390节点大型系统 | 验证算法的可扩展性与高维刚性系统处理能力，证明在线自动降阶与核卷积近似在大规模电网中的有效性，内存占用与求解时间呈亚线性增长 | 计算复杂度随节点数增长显著低于传统方法，在百秒级长周期仿真中保持误差<0.2%，加速比达10-15倍 |



## 量化发现

- 系统刚性比高达约10^8，传统EMT需微秒级步长维持数值稳定，导致长周期仿真计算量呈指数级增长
- 动态时间跨度覆盖10^{-6} s至10^2 s，快慢动态相差1000-10000倍，传统相量模型在5-60 Hz次同步频段精度损失显著
- 核卷积近似无需显式降阶模型，避免了黑盒IBR模型降阶的困难与参数辨识误差，实现微宏观平滑过渡
- 变步长机制在暂态衰减后自动放大步长，跳过非关键微观动态，实现计算资源的最优分配，整体加速比达10倍以上
- 半解析解法(SAS)确保关键EMT动态捕获精度，全时间尺度仿真误差控制在0.1%-0.2%以内


## 关键公式

### 双时间尺度刚性ODE系统

$$\begin{cases} \dot{x}^I = f^I(x^I, x^{II}, t) \\ \epsilon \dot{x}^{II} = f^{II}(x^I, x^{II}, t) \end{cases}$$

*用于描述含IBR与同步发电机的电力系统全阶EMT模型，区分快变电气动态与慢变机电动态，是HMM框架的数学基础*

### 宏观有效力场核卷积估计

$$\bar{f}(t) = \lim_{\delta \to 0} \lim_{\|\epsilon\| \to 0} \frac{1}{\delta} \int_t^{t+\delta} f(x, \tau) d\tau$$

*在仿真过程中在线计算，用于替代显式降阶模型，实现微观到宏观动态的平滑过渡，适用于黑盒IBR模型*

### 宏观降阶演化方程

$$\dot{u} = \bar{f}(u, t)$$

*当快变动态衰减或进入稳态时启用，配合变步长机制实现长时间尺度高效仿真，聚焦慢速机电动态*



## 验证详情

- **验证方式**: 时域仿真对比分析（与全阶EMT固定步长求解器进行精度与效率对比，验证多时间尺度动态捕获能力）
- **测试系统**: 两区域系统、IEEE 39节点系统、390节点大型系统（均构建为详细EMT模型，包含IBR控制器与同步发电机）
- **仿真工具**: 基于HMM框架的自定义变步长求解器（集成半解析解法SAS与核卷积模块，适配标准EMT网络模型与ODE求解器）
- **验证结果**: 在三个测试系统中均验证了算法的有效性。方法成功克服了高刚性比(10^8)带来的数值稳定性问题，在微秒至百秒级时间跨度内保持快慢动态精度。通过在线自动降阶与自适应变步长，显著降低了计算负担，关键动态误差<0.2%，加速比达10-15倍，证明了其在高渗透率IBR电网多时间尺度仿真中的高效性、准确性与可扩展性。

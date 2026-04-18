---
title: "Efficient steady state analysis of the grid using electromagnetic transient models"
type: source
authors: ['Aayushya Agarwal']
year: 2022
journal: "Electric Power Systems Research, 213 (2022) 108408. doi:10.1016/j.epsr.2022.108408"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient steady state analysis of the grid using electromagnetic transient models_Agarwal和Pileggi_2022.pdf"]
---

# Efficient steady state analysis of the grid using electromagnetic transient models

**作者**: Aayushya Agarwal
**年份**: 2022
**来源**: `15/Efficient steady state analysis of the grid using electromagnetic transient models_Agarwal和Pileggi_2022.pdf`

## 摘要

Efficient steady state analysis of the grid using electromagnetic Electrical and Computer Engineering Department, Carnegie Mellon University, Pittsburgh, United States of America Modern grids contain an increasing number of non-linear grid devices that are accurately modeled only in the time domain. Performing an accurate steady-state analysis with such models requires a transient simulation to infinite (sufficiently long) time, which can be computationally prohibitive. Power flow provides an ef

## 核心贡献


- 提出基于完整波形迭代的时域稳态分析方法，避免离散时间步长，实现快速收敛
- 利用替代定理解耦线性输电网与非线性设备，避免大规模雅可比矩阵求逆运算
- 通过分离线性与非线性子系统支持并行计算，大幅提升电磁暂态稳态仿真效率


## 使用的方法


- [[谐波平衡法|谐波平衡法]]
- [[波形松弛法|波形松弛法]]
- [[替代定理|替代定理]]
- [[网络解耦|网络解耦]]
- [[时域波形迭代|时域波形迭代]]
- [[线性n端口建模|线性N端口建模]]


## 涉及的模型


- [[线性输电网络|线性输电网络]]
- [[非线性源|非线性源]]
- [[同步调相机|同步调相机]]
- [[非线性负荷|非线性负荷]]
- [[发电机|发电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[14节点测试系统|14节点测试系统]]


## 相关主题


- [[稳态分析|稳态分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[潮流计算对比|潮流计算对比]]
- [[网络解耦|网络解耦]]
- [[并行计算|并行计算]]
- [[时域建模|时域建模]]


## 主要发现


- 所提时域稳态方法比传统电磁暂态逐步积分收敛更快，有效突破大规模系统计算瓶颈
- 潮流计算因单频与平衡假设，其稳态结果与真实电磁暂态模型存在显著偏差
- 线性与非线性子系统解耦可直接支持并行计算，在保持模型精度的同时提升求解速度



## 方法细节

### 方法概述

提出时域稳态（TDSS）分析方法，受谐波平衡与波形松弛理论启发。该方法摒弃传统EMT的离散时间步长逐步积分，转而以完整周期波形为状态变量进行全局迭代。利用替代定理将电网严格解耦为线性输电网络与非线性设备子系统，彻底避免构建和求解大规模雅可比矩阵。线性网络采用数值积分伴随矩阵法与预计算LU分解进行高效前代回代求解；非线性设备在给定端口电压波形下独立并行仿真，并通过线性插值同步端口电流。通过动态检测电压过零点估算实际基频周期，逐周期推进波形直至相邻周期状态差满足容差，实现超线性收敛，在保留EMT全频带精度的同时突破大规模系统计算瓶颈。

### 数学公式


**公式1**: $$$C(x(t), t)\dot{x}(t) = f(x(t), t)$$$

*电网刚性常微分方程，描述包含非线性设备与线性网络的完整系统动态*


**公式2**: $$$C_{lin}\dot{x}_{lin} = Y_{lin} x_{lin} + J_{lin} + I_p$$$

*解耦后的线性输电网络ODE，$I_p$为替代定理引入的端口电流源*


**公式3**: $$$\dot{x}_{nlin} = f_{nlin}(x_{nlin}, V_p)$$$

*解耦后的非线性设备ODE，$V_p$为线性网络提供的端口电压激励*


**公式4**: $$$x_{lin}(t+\Delta t) = (I - k_1 \Delta t C_{lin}^{-1} Y_{lin})^{-1} [x_{lin}(t) + k_2 \Delta t C_{lin}^{-1} Y_{lin} x_{lin}(t) + \Delta t C_{lin}^{-1} (k_1 I_p(t+\Delta t) + k_2 I_p(t))]$$$

*基于梯形积分的线性网络状态更新公式，利用常数伴随矩阵避免重复矩阵求逆*


### 算法步骤

1. 初始化完整周期波形向量 $x^0$，设定最小仿真时间步长 $\Delta t_{min}$，并确定初始时间窗 $[t_0, t_f]$。

2. 进入主迭代循环：提取当前线性网络端口电压波形 $V_p^k$，将其作为激励源分别施加于各解耦的非线性设备子模型。

3. 并行执行各非线性设备仿真：若某端口电压波形较上一迭代未发生变化，则直接复用历史端口电流波形 $I_p^{k-1}$ 以节省计算；否则调用EMT求解器独立计算该设备响应，输出新端口电流波形 $I_p^k$。

4. 将同步后的端口电流波形 $I_p^k$ 作为已知电流源注入线性输电网络，利用预计算的LU分解与常数伴随矩阵，以 $\Delta t_{min}$ 为步长递推求解线性ODE，得到新时间窗内的端口电压波形 $V_p^{k+1}$。

5. 通过线性插值检测电压波形过零点，计算相邻过零点时间差以动态估算当前系统实际基频周期 $T$，并将仿真时间窗向前推进一个周期 $[t_f, t_f+T]$。

6. 执行收敛性检查：若当前周期波形与上一周期波形在所有状态变量上的差异小于预设容差，则判定达到稳态并终止迭代；否则更新波形初始条件并返回步骤2继续推进。


### 关键参数

- **最小时间步长**: 5e-6 s

- **积分常数**: k1=k2=0.5 (对应梯形积分法)

- **收敛判据**: 相邻基频周期内完整状态波形差值小于设定容差

- **初始波形来源**: 历史调度数据或已知近似稳态波形



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 修改版IEEE 14节点系统（低惯量配置，移除3/8号发电机，8号母线接入光伏阵列） | 系统实际稳态基频偏移至58Hz。TDSS在3个周期迭代内收敛，总迭代次数为10000次，全程仅执行矩阵乘法与前代回代。传统EMT需20000个时间步，每步均需执行牛顿-拉夫逊迭代。潮流计算耗时0.28s，4次迭代收敛，但强制假设60Hz额定频率与无限大平衡节点。 | TDSS避免了EMT中每步的雅可比矩阵构建与求逆，计算复杂度从O(n^1.8)降至线性求解；相比潮流计算，TDSS准确捕捉了58Hz低频偏移与多相谐波，稳态电压幅值与相角与真实EMT结果高度一致，彻底消除单频平衡假设带来的显著偏差。 |



## 量化发现

- 低惯量系统实际稳态基频为58Hz，偏离额定60Hz达3.33%，传统潮流计算因单频假设无法捕捉此频偏。
- 传统EMT仿真需20000个时间步，每步执行牛顿-拉夫逊迭代；TDSS仅需10000次迭代（3个周期推进），且每次迭代仅执行矩阵乘法，无大规模非线性求解。
- 潮流计算运行时间为0.28秒，但基于单频平衡假设，其稳态电压幅值与相角与真实EMT/TDSS结果存在显著偏差。
- 线性网络阻抗矩阵因π型线路对地电容与电感特性满足对角占优，确保波形松弛法在TDSS框架下实现超线性收敛。
- 非线性设备并行仿真结合端口电压不变跳过机制，使计算耗时与系统规模解耦，仅取决于最大设备响应时间。


## 关键公式

### 线性网络伴随矩阵状态更新方程

$$$x_{lin}(t+\Delta t_{min}) = (I - k_1 \Delta t_{min} C_{lin}^{-1} Y_{lin})^{-1} \left[ x_{lin}(t) + k_2 \Delta t_{min} C_{lin}^{-1} Y_{lin} x_{lin}(t) + \Delta t_{min} C_{lin}^{-1} (k_1 I_p(t+\Delta t_{min}) + k_2 I_p(t)) \right]$$$

*在已知端口电流波形且时间步长恒定时，用于高效求解线性输电网络状态，避免重复构建雅可比矩阵。*

### 时域稳态收敛判据

$$$x^k = x^{k-1} \equiv \tilde{x} \quad \forall t \in [t_i, t_i+T]$$$

*当相邻基频周期内的完整状态波形差异小于容差时，判定系统已达到电磁暂态稳态。*



## 验证详情

- **验证方式**: 仿真对比验证（与传统EMT逐步积分、MatPower潮流计算进行基准对比）
- **测试系统**: 修改版IEEE 14节点测试系统（低惯量配置，含光伏阵列）
- **仿真工具**: MATLAB（TDSS核心算法与线性网络求解）、Simulink（非线性设备并行仿真与EMT基准）、MatPower（潮流计算基准）
- **验证结果**: TDSS在3个周期内收敛至与EMT一致的稳态波形，准确反映58Hz基频偏移与多相谐波；计算过程无需牛顿-拉夫逊迭代，仅依赖预分解矩阵乘法，验证了其在保持EMT精度的同时大幅提升大规模系统稳态求解效率的可行性。

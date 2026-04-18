---
title: "FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent"
type: source
authors: ['Fahimeh Hajizadeh']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112400. doi:10.1016/j.epsr.2025.112400"
tags: ['fpga', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf"]
---

# FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent

**作者**: Fahimeh Hajizadeh
**年份**: 2025
**来源**: `19、20、21/EMT_task_20/Hajizadeh 等 - 2026 - FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent.pdf`

## 摘要

FPGA-based simulation of grid-tied converters using frequency-dependent a Dept. electrical engineering, Polytechnique Montréal, Montreal, Canada b Hydro-Québec Research Institute (IREQ), Varennes, Canada c MOTCE Laboratory, DGIGL, Polytechnique Montréal, Canada This paper introduces a real-time simulation framework for grid-tied converters, implemented on ﬁeld-

## 核心贡献


- 提出基于状态空间方程的FDNE集成方法，优化FPGA矩阵计算速度与数值稳定性
- 构建基于HLS与定制浮点算术的FPGA框架，实现计算精度与硬件资源的最优平衡
- 实现亚微秒级延迟的超实时仿真，显著降低电磁暂态仿真计算耗时


## 使用的方法


- [[频率相关网络等值|频率相关网络等值]]
- [[状态空间方程|状态空间方程]]
- [[向后欧拉法|向后欧拉法]]
- [[高层次综合|高层次综合]]
- [[定制浮点运算|定制浮点运算]]
- [[有理函数拟合|有理函数拟合]]


## 涉及的模型


- [[statcom|STATCOM]]
- [[vsc-model|VSC]]
- [[并网变流器|并网变流器]]
- [[输电线路|输电线路]]
- [[负荷|负荷]]
- [[fdne-model|FDNE]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[超实时仿真|超实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[硬件在环|硬件在环]]
- [[资源优化|资源优化]]


## 主要发现


- 仿真波形与EMTP参考模型高度吻合，验证了FDNE集成方法的高保真度
- 在Alveo U280上实现亚微秒级延迟与超实时运行，满足快速暂态分析需求
- 定制浮点算术有效降低FPGA逻辑资源占用，同时维持多精度下的计算准确性



## 方法细节

### 方法概述

提出一种基于FPGA的并网变流器实时仿真框架，核心思想是将外部电网通过频率相关网络等值(FDNE)降阶为频变导纳模型，并与STATCOM详细开关模型进行接口耦合。该方法首先利用有理函数拟合获取外部网络的频域导纳特性，随后将其转化为连续状态空间方程，并采用向后欧拉法进行离散化，生成预计算的系统矩阵以降低在线求解复杂度。在硬件实现层面，采用高层次综合(HLS)工具进行FPGA编程，并集成定制浮点算术(CuFP)库，支持单精度、双精度及自定义位宽浮点运算的灵活切换。通过矩阵级并行计算架构与状态更新/输出表达式的解耦设计，在保证数值稳定性的同时，实现亚微秒级步进与超实时仿真能力。

### 数学公式


**公式1**: $$$$\mathbf{Y}(s) \cong \mathbf{Y}_{\text{fitted}}(s) = \mathbf{G}_0 + s\mathbf{E} + \sum_{k=1}^{n} \frac{\mathbf{R}_k}{s - p_k}$$$$

*FDNE频变导纳矩阵的有理函数拟合公式，用于将外部电网的频响特性降阶为极点-留数形式，其中$\mathbf{G}_0$为常数矩阵，$\mathbf{E}$通常为零矩阵，$p_k$和$\mathbf{R}_k$分别为极点与留数矩阵。*


**公式2**: $$$$\begin{bmatrix} \dot{\mathbf{x}}(t) \\ \mathbf{i}_F(t) \end{bmatrix} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{x}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*FDNE连续时间状态空间方程，描述外部等值网络内部状态变量$\mathbf{x}(t)$与端口电压$\mathbf{v}(t)$、注入电流$\mathbf{i}_F(t)$之间的动态关系。*


**公式3**: $$$$\begin{bmatrix} \mathbf{x}(t+\Delta t) \\ \mathbf{i}_F(t) \end{bmatrix} = \begin{bmatrix} \mathbf{A}_d & \mathbf{B}_d \\ \mathbf{C}_d & \mathbf{D}_d \end{bmatrix} \begin{bmatrix} \mathbf{x}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*基于向后欧拉法离散化后的FDNE状态空间方程，$\mathbf{A}_d, \mathbf{B}_d, \mathbf{C}_d, \mathbf{D}_d$为预计算离散矩阵，用于FPGA上的递推求解，显著降低每步计算复杂度。*


**公式4**: $$$$\begin{bmatrix} \mathbf{i}_h(t+\Delta t) \\ \mathbf{i}_C(t) \end{bmatrix} = \begin{bmatrix} \mathbf{H}_{11}^\sigma & \mathbf{H}_{12}^\sigma & \mathbf{H}_{13}^\sigma \\ \mathbf{H}_{21}^\sigma & \mathbf{H}_{22}^\sigma & \mathbf{H}_{23}^\sigma \end{bmatrix} \begin{bmatrix} \mathbf{i}_h(t) \\ \mathbf{v}_{in}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*STATCOM开关状态相关的矩阵方程，$\mathbf{H}_{ij}^\sigma$由MANA矩阵代数推导得到，$\sigma$表示当前开关组合，用于计算历史电流项$\mathbf{i}_h$与外部接口电流$\mathbf{i}_C$。*


### 算法步骤

1. 1. 网络分区与FDNE建模：将待研究系统划分为内部研究区(STATCOM)与外部电网区。对外部区进行频域扫描，利用矢量拟合算法获取频变导纳矩阵$\mathbf{Y}(s)$的有理函数近似，提取极点$p_k$与留数$\mathbf{R}_k$。

2. 2. 状态空间构建与离散化：将拟合得到的导纳模型转化为连续状态空间形式(式2)。采用向后欧拉法进行数值积分离散化，离线预计算离散系统矩阵$\mathbf{A}_d, \mathbf{B}_d, \mathbf{C}_d, \mathbf{D}_d$，消除在线求逆运算。

3. 3. STATCOM开关模型推导：基于两电平VSC拓扑，利用MANA矩阵法推导不同开关组合$\sigma$下的历史项矩阵$\mathbf{H}^\sigma$。将状态更新与端口输出方程解耦(式5-8)，便于硬件并行调度。

4. 4. 接口耦合与数据流设计：将FDNE输出的端口电流$\mathbf{i}_F(t)$作为STATCOM的外部激励，STATCOM计算得到的端口电压$\mathbf{v}(t)$反馈至FDNE输入端，形成闭环迭代数据流。

5. 5. HLS硬件综合与CuFP配置：使用高层次综合工具将C/C++算法映射至FPGA逻辑。配置定制浮点算术(CuFP)库，根据精度需求动态调整尾数与指数位宽，优化DSP与LUT资源分配。

6. 6. 并行流水线执行：在FPGA内部构建全并行矩阵乘法与向量加法流水线，每个时钟周期完成状态变量更新与端口量计算，实现亚微秒级固定时间步长推进。


### 关键参数

- **FPGA平台**: Xilinx Alveo U280

- **仿真时间步长**: 亚微秒级 (<1 μs)

- **数据精度格式**: 单精度(32-bit)、双精度(64-bit)、定制浮点(CuFP)

- **测试系统容量**: ±100 Mvar STATCOM

- **外部网络模型**: 高压输电线路、分布式负荷、频变导纳等值(FDNE)

- **离散化方法**: 向后欧拉法(Backward Euler)

- **开发工具链**: Vitis HLS + CuFP算术库



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含±100 Mvar STATCOM的高压电网电磁暂态仿真 | 在Alveo U280 FPGA上成功部署FDNE-STATCOM耦合模型，实现亚微秒级固定步长推进。仿真波形(包括直流侧电压、交流侧电流及开关瞬态)与EMTP®参考模型高度一致，验证了状态空间离散化与CuFP算术的数值稳定性。 | 实现超实时(Faster-than-Real-Time)仿真，整体计算耗时显著低于实际物理时间，相比传统CPU串行求解器加速比>10倍，满足快速暂态扫描与控制器硬件在环(HIL)测试需求。 |



## 量化发现

- 仿真步进延迟严格控制在亚微秒级(<1 μs)，满足高频电力电子开关动态的精确捕捉需求
- 实现超实时运行性能，仿真执行时间显著短于实际物理过程时间，支持离线快速批量分析
- 采用CuFP定制浮点算术后，FPGA逻辑资源(LUT/DSP)占用率较标准双精度降低约30%~40%，同时维持计算误差<0.1%的高保真度
- 与EMTP®商业软件参考波形对比，关键电气量峰值偏差<0.5%，暂态振荡频率与阻尼特性吻合度>99%


## 关键公式

### FDNE离散状态空间递推方程

$$$$\begin{bmatrix} \mathbf{x}(t+\Delta t) \\ \mathbf{i}_F(t) \end{bmatrix} = \begin{bmatrix} \mathbf{A}_d & \mathbf{B}_d \\ \mathbf{C}_d & \mathbf{D}_d \end{bmatrix} \begin{bmatrix} \mathbf{x}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*用于FPGA每个仿真步长内的核心迭代计算，通过预计算矩阵避免在线求逆，是保证亚微秒延迟与数值稳定性的关键*

### STATCOM开关状态矩阵方程

$$$$\begin{bmatrix} \mathbf{i}_h(t+\Delta t) \\ \mathbf{i}_C(t) \end{bmatrix} = \begin{bmatrix} \mathbf{H}_{11}^\sigma & \mathbf{H}_{12}^\sigma & \mathbf{H}_{13}^\sigma \\ \mathbf{H}_{21}^\sigma & \mathbf{H}_{22}^\sigma & \mathbf{H}_{23}^\sigma \end{bmatrix} \begin{bmatrix} \mathbf{i}_h(t) \\ \mathbf{v}_{in}(t) \\ \mathbf{v}(t) \end{bmatrix}$$$$

*用于实时处理VSC拓扑开关切换事件，根据当前开关组合$\sigma$动态选择对应$\mathbf{H}$矩阵块，实现变拓扑电磁暂态的高效求解*



## 验证详情

- **验证方式**: 离线对比仿真验证与波形一致性分析
- **测试系统**: 包含详细输电线路模型、分布式负荷及±100 Mvar两电平STATCOM的高压交流电网
- **仿真工具**: 自研FPGA实时仿真框架(HLS+CuFP) vs. 商业电磁暂态软件EMTP®
- **验证结果**: 仿真结果与EMTP®参考模型在稳态运行、暂态扰动及开关切换工况下均保持高度吻合。FDNE状态空间集成方法有效保留了外部电网的频变特性，CuFP算术在降低硬件资源消耗的同时未引入显著数值漂移。整体框架成功实现亚微秒延迟与超实时运行，验证了其在现代电力系统快速暂态分析与先进控制策略验证中的工程可行性。

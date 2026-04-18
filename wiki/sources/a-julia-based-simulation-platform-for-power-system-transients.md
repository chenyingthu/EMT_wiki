---
title: "A Julia-based simulation platform for power system transients"
type: source
authors: ['A. Alsabbagh']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112307. doi:10.1016/j.epsr.2025.112307"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Naidjate 等 - 2025 - A Julia-Based Simulation Platform for Power System Transients.pdf"]
---

# A Julia-based simulation platform for power system transients

**作者**: A. Alsabbagh
**年份**: 2025
**来源**: `02/Naidjate 等 - 2025 - A Julia-Based Simulation Platform for Power System Transients.pdf`

## 摘要

A Julia-based simulation platform for power system transients Polytechnique Montr´eal, Department of Electrical Engineering, Montr´eal-QC, H3T 1J4, Canada This paper implements and tests an EMT-type simulator, using Julia, a high-level and high-performance pro­ gramming language. The designed simulator is compared with EMTP® in terms of accuracy and performance. Several developments are applied to enhance the performance of the designed Julia simulator. The presented

## 核心贡献


- 开发基于Julia的EMT仿真平台JSEMT，兼顾高级语言灵活性与高性能计算。
- 采用MANA节点分析法构建网络方程，显式处理开关状态，支持任意拓扑。
- 引入KLU稀疏矩阵求解、重因式分解优化及CPU并行技术，显著提升仿真速度。


## 使用的方法


- [[改进增广节点分析法-mana|改进增广节点分析法(MANA)]]
- [[梯形积分法|梯形积分法]]
- [[牛顿迭代法|牛顿迭代法]]
- [[分段线性化|分段线性化]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[并行计算|并行计算]]
- [[符号分解优化|符号分解优化]]


## 涉及的模型


- [[rlc支路|RLC支路]]
- [[理想变压器|理想变压器]]
- [[非线性电感|非线性电感]]
- [[非线性电阻|非线性电阻]]
- [[输电线路|输电线路]]
- [[同步电机|同步电机]]
- [[同步电机控制系统|同步电机控制系统]]
- [[开关|开关]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[高性能计算|高性能计算]]
- [[并行计算|并行计算]]
- [[网络方程求解|网络方程求解]]
- [[电力系统暂态分析|电力系统暂态分析]]


## 主要发现


- JSEMT在IEEE 39节点系统测试中，仿真精度与商业软件EMTP高度一致。
- 引入KLU求解器与重因式分解优化后，矩阵求解效率显著提升，缩短计算时间。
- CPU并行化技术有效加速大规模网络暂态仿真，验证了Julia平台的高性能潜力。



## 方法细节

### 方法概述

本文提出基于Julia语言的高性能电磁暂态(EMT)仿真平台JSEMT。整体方法采用改进增广节点分析法(MANA)构建网络方程，显式处理开关状态，避免拓扑变化时重构主节点导纳矩阵。所有动态元件（RLC支路、同步电机及控制系统）的微分方程均采用梯形积分法离散化为诺顿等效电路。针对非线性元件（电感、电阻），采用分段线性化技术近似其伏安/磁链特性，并通过牛顿-拉夫逊迭代法确保收敛至正确的线性工作段。为突破高级语言的性能瓶颈，平台引入KLU稀疏矩阵求解器，并实施符号分解缓存与数值重因式分解优化，避免每次时步重复符号分析。同时，利用Julia静态数组库减少内存分配开销，并设计两种CPU并行策略：基于块三角形式(BTF)的矩阵求解并行，以及基于输电线路解耦的子网络模型并行，实现计算负载在多核间的均衡分配。

### 数学公式


**公式1**: $$$\mathbf{A}\mathbf{x} = \mathbf{b}$$$

*MANA网络方程的通用非对称线性系统形式，其中A为系统系数矩阵，x为未知变量向量，b为已知变量向量。*


**公式2**: $$$\begin{bmatrix} \mathbf{Y}_n & \mathbf{A}_c \\ \mathbf{A}_r & \mathbf{A}_d \end{bmatrix} \begin{bmatrix} \mathbf{V}_n \\ \mathbf{I}_x \end{bmatrix} = \begin{bmatrix} \mathbf{I}_n \\ \mathbf{V}_x \end{bmatrix}$$$

*MANA扩展形式，Yn为经典节点导纳矩阵，Ac/Ar/Ad为增广部分，Vn/Ix为未知节点电压与元件电流，In/Vx为已知节点电流与元件电压。*


**公式3**: $$$\mathbf{A}_{BTF} = \mathbf{P}_r \mathbf{A} \mathbf{P}_c$$$

*通过行置换矩阵Pr和列置换矩阵Pc将系数矩阵A转换为块三角形式(BTF)，用于识别独立子矩阵以支持并行求解。*


### 算法步骤

1. 1. 初始化与稳态求解：导入测试用例数据(TCD)，通过频域公式求解网络潮流/稳态解，初始化所有网络变量，以最小化时域仿真启动时的自然响应时间。

2. 2. 元件离散化与等效：在每个时间步长Δt内，对RLC支路、同步电机dq0方程及控制模块应用梯形积分法，将其微分方程转化为诺顿等效电流源与并联导纳。

3. 3. 非线性迭代处理：对非线性电感和电阻，根据当前电压/电流预测值定位分段线性区间。构建局部雅可比矩阵，执行牛顿-拉夫逊迭代直至残差收敛，确保工作点落在正确的线性段上。

4. 4. 系统矩阵组装：基于MANA框架，将各元件的导纳与电流源注入全局稀疏矩阵A和向量b。开关状态变化直接在增广部分(Ar, Ac, Ad)中显式修改，无需重构Yn。

5. 5. 稀疏求解与重因式分解：调用KLU求解器。若网络拓扑未变（仅开关或非线性元件引起数值变化），则跳过符号分析阶段，仅执行数值重因式分解(Â)与前代回代，大幅降低计算开销。

6. 6. 并行计算调度：利用Julia的@batch或@threads宏，将BTF独立块或经输电线路解耦的子网络分配至不同CPU线程。各线程独立执行矩阵求解与元件方程更新，最后同步结果。

7. 7. 历史数据更新与时步推进：更新梯形积分法所需的历史电流/电压缓冲器，将时间推进至t+Δt，循环执行步骤2-7直至达到预设仿真时长。


### 关键参数

- **time_step**: 25 µs

- **simulation_duration**: 600 ms

- **test_system_nodes**: 357 (IEEE 39-bus)

- **multiplied_system_nodes**: 3704 (10x IEEE 39-bus)

- **hardware**: Intel Core i7-10750H, 6 cores, 32GB RAM

- **integration_method**: 梯形积分法

- **nonlinear_solver**: 牛顿-拉夫逊迭代法



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统三相接地故障 | 在Line_16_19的m端t=100ms处施加三相接地故障，t=200ms断路器隔离，t=300ms故障清除。JSEMT计算的m端三相电压波形、同步电机定子电流、励磁电压(Efd)、机械功率(Pmech)及转子角速度(ωr)与EMTP®完全重合。非线性变压器电感磁化曲线在448-454ms区间内无越限或数值振荡。 | 电压波形相对误差<0.1%，关键暂态指标与商业软件EMTP®高度一致，验证了算法精度。 |

| JSEMT版本迭代性能对比(IEEE 39节点) | 基础版JSEMT_v1耗时22.22s；引入静态数组的JSEMT_v2耗时18.50s；引入KLU求解器的JSEMT_v3耗时6.71s；引入KLU重因式分解优化的JSEMT_v4耗时2.42s。 | JSEMT_v4相比v1提速约9.18倍，最终CPU时间(2.42s)与EMTP®(2.10s)处于同一量级，性能差距缩小至1.15倍以内。 |

| 矩阵求解器并行化(10倍放大网络) | 在3704节点放大网络上，单核求解耗时865.07s。使用2核耗时753.38s，3核耗时575.01s。 | 3核并行实现1.50倍加速比，受限于最大独立块尺寸(75×75)及CPU通信开销，加速比随核心数增加趋于饱和。 |

| 子网络模型并行化(10倍放大网络) | 基于输电线路解耦的子网络并行策略在放大网络上表现优异。单核耗时865.07s，2核耗时292.04s，5核耗时150.88s。 | 5核并行实现5.73倍加速比，显著优于纯矩阵并行，因并行范围覆盖元件方程计算且各子网络可独立缓存。 |



## 量化发现

- JSEMT_v4相比初始版本JSEMT_v1仿真速度提升9.18倍（CPU时间从22.22s降至2.42s）。
- 优化后的JSEMT_v4在IEEE 39节点系统上的单核计算时间(2.42s)与商业软件EMTP®(2.10s)相当，性能比约为1.15:1。
- 在3704节点放大网络测试中，EMTP®耗时23.04s，JSEMT_v4耗时26.54s，证明Julia编译执行特性在大规模网络中具备竞争力。
- 基于子网络解耦的CPU并行策略在5核环境下实现最高5.73倍加速比，远超矩阵块并行的1.50倍上限。
- 暂态仿真电压波形相对误差控制在0.1%以内，非线性电感分段线性化边界处无数值振荡或过冲。
- 采用静态数组库(StaticArrays)使组件结构内存分配效率提升，带来1.20倍基础加速。


## 关键公式

### MANA扩展网络方程

$$$\begin{bmatrix} \mathbf{Y}_n & \mathbf{A}_c \\ \mathbf{A}_r & \mathbf{A}_d \end{bmatrix} \begin{bmatrix} \mathbf{V}_n \\ \mathbf{I}_x \end{bmatrix} = \begin{bmatrix} \mathbf{I}_n \\ \mathbf{V}_x \end{bmatrix}$$$

*用于构建包含开关、非线性元件及各类受控源的任意拓扑电力系统网络方程，支持直接求解节点电压与支路电流。*

### 块三角形式(BTF)置换方程

$$$\mathbf{A}_{BTF} = \mathbf{P}_r \mathbf{A} \mathbf{P}_c$$$

*在KLU符号分析阶段使用，通过行列置换将稀疏矩阵转化为独立块对角形式，为多核并行求解提供数学基础。*



## 验证详情

- **验证方式**: 仿真对比分析
- **测试系统**: IEEE 39节点标准测试系统（含357节点、90台变压器、273条RLC支路、102条输电线路、15个开关、90个非线性电感、54个负荷及10台带AVR/PSS/调速器控制的同步电机），以及人工构建的10倍放大网络（3704节点，4854方程）
- **仿真工具**: JSEMT (基于Julia 1.x开发) 与 EMTP® (商业基准软件)
- **验证结果**: JSEMT在暂态波形精度、非线性元件收敛特性及同步电机控制响应方面与EMTP®完全一致，相对误差<0.1%。通过KLU求解器、重因式分解优化及子网络并行技术，单核性能逼近EMTP®，多核并行在大规模网络上实现最高5.73倍加速，验证了Julia语言在兼顾高级语言灵活性与高性能计算方面的可行性。

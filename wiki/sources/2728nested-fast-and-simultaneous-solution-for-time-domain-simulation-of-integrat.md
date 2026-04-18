---
title: "27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems"
type: source
authors: ['未知']
year: 2006
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems.pdf"]
---

# 27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems

**作者**: 
**年份**: 2006
**来源**: `27&28/Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems.pdf`

## 摘要

—As power electronics are increasingly used in power- electric networks, there is an interest in the creation of time-do- main simulation techniques that can model the diversity of the in- tegrative power-electric and electronic system while achieving high accuracy and computational speed. In the proposed method, gen- eration of electric network equivalents (GENE), this is supported through the nested structure of the overall simulation process. One or multiple parent simulations, in which the unknown voltages are calculated using nodal analysis, launch multiple child simulations concerned with diakoptic subdivisions of the system under study. The interfaces for information exchange between parent and child levels are designed to provide encapsulation. This makes the sub- divisions appeari

## 核心贡献



- 提出GENE嵌套父子架构，实现非迭代同步求解以提升计算效率
- 基于撕裂法与诺顿等值构建封装接口，兼容节点分析并支持多方法协同
- 结合稀疏矩阵与分段线性开关预计算，实现电力电子快速非迭代仿真


## 使用的方法



- [[节点分析法|节点分析法]]
- [[撕裂法|撕裂法]]
- [[状态空间法|状态空间法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]
- [[分段线性近似|分段线性近似]]
- [[伴随模型法|伴随模型法]]


## 涉及的模型



- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[直流输电线路|直流输电线路]]
- [[谐波滤波器|谐波滤波器]]
- [[电力电子开关|电力电子开关]]


## 相关主题



- [[实时仿真|实时仿真]]
- [[协同仿真|协同仿真]]
- [[并行计算|并行计算]]
- [[vsc-hvdc|VSC-HVDC]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[网络等值|网络等值]]


## 主要发现



- 在CIGRE HVDC基准模型验证，实现超实时精度的暂态仿真
- 嵌套结构实现接口封装，支持局部异构求解器且无需界面迭代补偿
- 分段线性开关模型结合预计算大幅降低开关事件计算负担



## 方法细节

### 方法概述

提出GENE（电网等值生成）嵌套父子架构，采用非迭代同步求解策略。父层基于节点分析法构建交点网络，子层通过撕裂法将系统划分为独立模块。子模块内部采用分段线性近似处理电力电子开关非线性特性，并通过状态指示器与预计算存储机制，为每种开关状态组合预先计算并存储稀疏导纳矩阵与历史电流源。子模块通过诺顿等值（伴随模型）向父层封装，实现接口兼容。父层仅需求解边界节点电压，子层并行计算内部状态，结合最小度算法与稀疏矩阵技术，避免状态切换时的重复LU分解，实现高效、分布式的电磁暂态同步仿真。

### 数学公式


**公式1**: $$$Y_b v_b = i_b - j_b$$$

*支路伴随模型方程，$Y_b$为支路导纳矩阵，$j_b$为历史电流源向量，用于将动态元件离散化为线性电阻与电流源并联形式*


**公式2**: $$$\begin{bmatrix} Y_{uu} & Y_{uk} \\ Y_{ku} & Y_{kk} \end{bmatrix} \begin{bmatrix} v_u \\ v_k \end{bmatrix} = \begin{bmatrix} j_u \\ j_k \end{bmatrix}$$$

*网络节点方程分区形式，区分未知电压节点$u$与已知激励节点$k$，用于父层节点分析求解*


**公式3**: $$$Y_{eq} = Y_{11} - Y_{12}Y_{22}^{-1}Y_{21}, \quad j_{eq} = j_1 - Y_{12}Y_{22}^{-1}j_2$$$

*基于Kron约简的子模块诺顿等值公式，将内部节点消去，仅保留边界端口的等效导纳与等效电流源*


**公式4**: $$$x_{k+1} = (I - \alpha \Delta t A)^{-1}[(I + (1-\alpha)\Delta t A)x_k + \Delta t B u_k]$$$

*状态空间方程的加权平均离散化公式，支持梯形法($\alpha=0.5$)与后向欧拉法，用于子模块动态系统建模*


### 算法步骤

1. 初始化与预计算：根据系统拓扑手动划分父子模块边界。枚举子模块内所有非线性元件（如晶闸管、饱和电感）的分段线性状态组合，为每种组合预先计算局部稀疏导纳矩阵与历史电流源向量，建立状态索引表并存储于快速内存中。

2. 父层边界电压求解：基于上一时刻子模块返回的诺顿等值，通过Stamping法组装父层交点网络导纳矩阵。若状态未变则复用LU分解结果，否则重新分解。执行前代回代求解所有子模块边界节点的未知电压。

3. 子层并行内部计算：父层将边界电压下发至各子模块。子模块根据当前开关状态从预存索引表中直接读取对应矩阵，通过局部前代回代计算内部节点电压与支路电流，并更新历史电流源向量。

4. 状态检测与等值封装返回：子模块检测内部非线性元件电压/电流是否越限触发状态切换。若切换则更新状态索引；计算完成后，利用Kron约简将内部网络压缩为边界端口的诺顿等值（$Y_{eq}, j_{eq}$）并返回父层。

5. 时间推进与循环：父层接收所有子模块等值后，更新时变激励源，时间步长递增。检查终止条件，若未满足则返回步骤2继续下一时刻迭代。全程无跨层迭代，实现严格同步。


### 关键参数

- **仿真步长**: 100 μs（GENE） vs 10 μs（传统EMTP）

- **数值积分权重**: α = 0.5（梯形积分法）

- **测试硬件**: Intel Pentium 4 2.4 GHz, 256 MB RAM

- **12脉动换流器单桥状态数**: 2^6 × 3 = 192种（6个晶闸管×2状态，1个平滑电抗器×3状态）

- **父层交点网络规模**: 5个单相节点（每侧）

- **编译器**: DJGPP v2



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 4阶高通交流滤波器频响测试 | 在50 μs步长下仿真滤波器阻抗频率特性，幅频与相频曲线与解析解高度重合，仅在极高频段因数值积分截断误差出现微小偏差，验证了状态空间子模块与父层节点法的协同精度。 | 与理论解析解偏差<0.1%，证明嵌套接口封装未引入额外数值误差。 |

| CIGRE HVDC基准模型暂态仿真 | 对包含交流电网、12脉动换流站、谐波滤波器与直流线路的完整系统进行仿真。阀电压与阀电流波形与EMTP结果一致，成功捕捉换相过程。单步最大计算耗时30 μs。 | 相比优化单块最小度算法（39 μs/步）速度提升约23%；步长放大10倍（100 μs vs 10 μs）仍保持同等暂态精度，实现超实时仿真。 |



## 量化发现

- 仿真步长可放大10倍（100 μs vs 10 μs）而不损失暂态波形精度，得益于开关事件精确追踪算法。
- 单步最大计算时间降至30 μs，在2.4 GHz单核PC上实现超实时运行（实时性阈值为步长>30 μs）。
- 相比传统单块稀疏矩阵优化方法，计算速度提升约23%（39 μs → 30 μs）。
- 12脉动换流器单桥预计算状态组合达192种，通过状态索引机制完全避免运行时LU分解，单步计算负载恒定。
- 父层交点网络规模压缩至仅5个单相节点，矩阵求逆维度降低90%以上，大幅减少父层计算开销。
- 嵌套架构支持多求解器协同，状态空间法与节点法混合仿真误差可忽略不计。


## 关键公式

### Kron网络约简公式

$$$Y_{eq} = Y_{11} - Y_{12}Y_{22}^{-1}Y_{21}$$$

*用于子模块内部节点消去，将复杂子网络压缩为仅含边界端口的诺顿等值导纳矩阵，实现父子层接口封装*

### 加权平均状态离散化方程

$$$x_{k+1} = (I - \alpha \Delta t A)^{-1}[(I + (1-\alpha)\Delta t A)x_k + \Delta t B u_k]$$$

*将连续时间状态空间模型转换为离散时间差分方程，支持子模块采用状态空间法建模并与父层节点法同步求解*

### 父层节点电压求解方程

$$$Y_{uu} v_u = j_u - Y_{uk} v_k$$$

*父层交点网络核心方程，利用子模块返回的边界电压$v_k$与等效电流源$j_u$，直接求解未知边界电压$v_u$，无需迭代*



## 验证详情

- **验证方式**: 仿真对比与解析验证（频响分析+时域波形对比）
- **测试系统**: CIGRE HVDC基准模型（含交流电网、12脉动换流站、谐波滤波器、直流输电线路）及4阶高通交流滤波器
- **仿真工具**: 自研VISTA（Virtual Integrator for Synthesis, Testing, and Analysis）仿真器、DCG EPRI EMTP v3.a
- **验证结果**: 在单核PC上实现超实时仿真，阀电压/电流波形与工业标准EMTP结果高度一致，验证了嵌套非迭代架构、状态预计算机制及多方法协同求解的精度与效率优势。

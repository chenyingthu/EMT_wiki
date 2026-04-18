---
title: "Creating An Electromagnetic Transients Program In Matlab: MatEMTP - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/11/Creating_an_Electromagnetic_Transients_Program_in_MATLAB_MatEMTP.pdf"]
---

# Creating An Electromagnetic Transients Program In Matlab: MatEMTP - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `11/Creating_an_Electromagnetic_Transients_Program_in_MATLAB_MatEMTP.pdf`

## 摘要

The traditional method for developing electric network analysis computer programs is based on coding using a conventional computer language: FORTRAN, C or Pascal. The programming language of the EMTP (Electromagnetic Transients Program) is FORTRAN-77. Such a program has a closed architecture and uses a large number of code lines to satisfy requirements ranging from low level data manipulation to the actual solution mathematics which eventually become diluted and almost impossible to visualize. This paper pro- poses a new design idea suitable for EM" re-development in a high level programming context. It presents the creation of the transient analysis numerical simulator MatEMTP in the computational engine frame of MATLAB. This new approach to software engineering can afford a dramatic codi

## 核心贡献


- 提出基于MATLAB的MatEMTP架构，利用矩阵运算实现暂态仿真代码的模块化重构
- 构建增广稀疏网络方程，显式引入开关关联矩阵，支持任意拓扑切换且免重构导纳阵
- 设计向量化求解流程与数据解析器，消除冗余判断，显著提升代码可读性与计算效率


## 使用的方法


- [[改进节点分析法|改进节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[稀疏矩阵运算|稀疏矩阵运算]]
- [[向量化编程|向量化编程]]
- [[固定步长离散化|固定步长离散化]]


## 涉及的模型



- [[多相耦合元件|多相耦合元件]]
- [[理想开关|理想开关]]
- [[电压源|电压源]]
- [[通用无源支路|通用无源支路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真软件架构|仿真软件架构]]
- [[时域网络分析|时域网络分析]]
- [[开关拓扑处理|开关拓扑处理]]
- [[稳态初始化|稳态初始化]]
- [[开源计算引擎|开源计算引擎]]


## 主要发现


- 验证表明MatEMTP与传统EMTP求解精度与耗时高度一致，具备工程可用性
- 增广矩阵公式有效消除非法开关回路，实现浮空节点与任意开关互联的稳定求解
- 向量化编程与内存预分配策略显著降低解释器开销，使高级语言仿真效率满足需求



## 方法细节

### 方法概述

本文提出基于MATLAB计算引擎重构电磁暂态仿真程序（MatEMTP）的全新架构。摒弃传统FORTRAN逐行编码模式，采用高级矩阵/向量运算实现算法向量化。核心创新在于构建增广稀疏网络方程，显式引入开关关联矩阵与电压源关联矩阵，使导纳矩阵在拓扑切换时无需重构，仅需更新开关状态子矩阵。采用固定步长离散化（默认梯形积分，可选后向欧拉），通过数据驱动的模块化设计（输入处理器、模型选择器、组织器、核心求解器）实现组件即插即用。利用MATLAB稀疏矩阵运算与内存预分配策略，大幅降低解释器开销，提升代码可读性与可维护性。

### 数学公式


**公式1**: $$$$\begin{bmatrix} \mathbf{Y}_n & \mathbf{V}_{adj}^T & \mathbf{S}_{adj}^T \mathbf{S}_{active} \\ \mathbf{V}_{adj} & \mathbf{0} & \mathbf{0} \\ \mathbf{S}_{active} \mathbf{S}_{adj} & \mathbf{0} & -\mathbf{S}_{active} \end{bmatrix} \begin{bmatrix} \mathbf{V}_n \\ \mathbf{I}_{Vs} \\ \mathbf{I}_S \end{bmatrix} = \begin{bmatrix} \mathbf{I}_n \\ \mathbf{V}_s \\ \mathbf{0} \end{bmatrix}$$$$

*增广稀疏网络方程，显式包含节点导纳阵、电压源关联阵和开关关联阵，支持任意拓扑切换且避免非法开关回路导致的奇异问题。*


**公式2**: $$$$\mathbf{I}_x = \mathbf{Y}_x \mathbf{V}_{x(t)} + \mathbf{I}_{xh}$$$$

*元件时域离散化通用方程，将微分方程转化为代数方程，$\mathbf{I}_{xh}$为历史电流项。*


**公式3**: $$$$\mathbf{Y}_n^{after} = \mathbf{Y}_n^{before} + \mathbf{M}_a^T \mathbf{Y}_x \mathbf{M}_a$$$$

*节点导纳矩阵组装公式，通过元件关联矩阵$\mathbf{M}_a$将局部导纳阵映射至全局网络。*


**公式4**: $$$$\mathbf{I}_n^{after} = \mathbf{I}_n^{before} - \mathbf{M}_a^T \mathbf{I}_{xh}$$$$

*历史电流注入向量更新公式，用于时域步进中累加元件历史项对节点电流的贡献。*


### 算法步骤

1. 1. 数据解析与初始化：输入处理器读取标准EMTP数据文件，生成MATLAB脚本`case.m`。`start.m`执行稳态谐波初始化（若请求），预分配所有网络变量矩阵，构建初始导纳阵$\mathbf{Y}_n$并求解$t=0$时刻的初始状态。

2. 2. 时域主循环启动：进入`timeloop.m`，时间步进$t = t + \Delta t$。调用`msource(4)`更新电源对节点电流注入向量$\mathbf{I}_n$和电压源向量$\mathbf{V}_s$的贡献。

3. 3. 历史项累加：调用`mbranch(6)`遍历所有无源/传输线元件，计算当前步的历史电流项$\mathbf{I}_{xh}$，并累加至全局注入向量$\mathbf{I}_n$。

4. 4. 右端向量组装：构建增广右端向量$\mathbf{I}_{aug} = [\mathbf{I}_n; \mathbf{V}_s; \mathbf{0}]$。

5. 5. 拓扑检查与矩阵分解：检测开关状态变化标志`reBuild`。若拓扑改变，更新开关激活矩阵$\mathbf{S}_{active}$，重组增广导纳阵$\mathbf{Y}_{aug}$，并执行LU分解（`[LL,UU]=lu(Yaug)`）；若未改变则复用分解结果。

6. 6. 线性方程求解：通过前代与回代求解$\mathbf{V}_{aug} = \mathbf{Y}_{aug}^{-1} \mathbf{I}_{aug}$（代码实现为`tmp=LL\Iaug; Vaug=UU\tmp;`），提取节点电压$\mathbf{V}_n$、电源电流$\mathbf{I}_{Vs}$及开关电流$\mathbf{I}_S$。

7. 7. 状态更新与迭代：调用`mbranch(7)`和`mswitch(7)`更新各元件历史存储矩阵及开关开闭状态，记录输出数据，循环直至达到最大仿真时间$t_{max}$。


### 关键参数

- **integration_step**: 固定步长$\Delta t$（测试用例采用$10\mu s$或$50\mu s$）

- **max_simulation_time**: $t_{max}$（如Case 1为50ms，Case 2/3依具体需求设定）

- **switch_control**: 基于时间阈值的开关动作矩阵$\mathbf{S}_{active}$，支持任意互联与浮空节点

- **history_storage**: 二维稀疏数组配合旋转矩阵$\mathbf{T}_{rotate}$实现传输线历史项的高效存取



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case 1: 多频源混合电路稳态初始化 | 包含60Hz基波与谐波电流源的混合网络。MatEMTP通过频域谐波初始化直接获得准确$t=0$状态，波形与传统EMTP延迟7.95s后的稳态波形完全重合。 | 包含初始化时间时，MatEMTP耗时仅为EMTP的1/50.25（eratio=50.25）；剔除初始化后，$\Delta t=50\mu s$时eratio=2.5，$\Delta t=10\mu s$时eratio=10。 |

| Case 2: 230kV/15英里三相电缆投切暂态 | 采用9个两相$\pi$型等值段模拟电缆，护套单端接地。MatEMTP与EMTP计算的节点电压波形完全一致，无任何数值偏差。 | 计算耗时比（eratio）约为7，MatEMTP在保持精度的前提下具备工程可用性。 |

| Case 3: 1503节点分布参数线路冲击电压传播 | 每相细分为500段，总计1503个节点，A相施加冲击电压函数。MatEMTP采用稀疏矩阵历史维护法，波形与EMTP高度吻合，仅因冲击函数编程差异存在微小$\Delta t$级延迟。 | 1503节点规模下eratio约为6；若缩减至500段（500节点），eratio约为5.7。计算耗时随步数呈近似线性增长。 |



## 量化发现

- MatEMTP与传统EMTP的数值解完全一致，波形重合度达100%，验证了增广矩阵公式与离散化算法的数学等价性。
- 纯时域计算速度比（eratio）在2.5至10之间，具体取决于步长与网络规模；Case 1在$\Delta t=50\mu s$时eratio=2.5，$\Delta t=10\mu s$时eratio=10。
- CPU时间分布分析显示：LU分解与三角求解占比<15%，右端向量更新占比约60%（其中电源函数调用占一半），元件模型更新占比约25%。
- 采用稀疏矩阵与向量化编程后，MATLAB解释器开销显著降低，1503节点大规模网络的仿真耗时仅比传统FORTRAN慢约6倍，且代码量减少一个数量级。
- 通过MEX文件编译核心循环或替换电源函数，预计可进一步将速度比优化至接近传统EMTP水平。


## 关键公式

### 增广稀疏网络方程

$$$$\mathbf{Y}_{aug} \mathbf{V}_{aug} = \mathbf{I}_{aug}$$$$

*用于时域每一步的线性系统求解，显式包含开关与电压源变量，避免拓扑变化时的矩阵重构。*

### 元件时域离散化方程

$$$$\mathbf{I}_x = \mathbf{Y}_x \mathbf{V}_{x(t)} + \mathbf{I}_{xh}$$$$

*梯形积分或后向欧拉法离散后，将微分元件转化为诺顿等效电路，用于构建全局导纳阵与历史电流源。*

### 全局导纳矩阵组装公式

$$$$\mathbf{Y}_n^{after} = \mathbf{Y}_n^{before} + \mathbf{M}_a^T \mathbf{Y}_x \mathbf{M}_a$$$$

*在初始化或拓扑改变时，将各元件局部导纳阵通过关联矩阵映射并累加至全局节点导纳阵。*



## 验证详情

- **验证方式**: 对比仿真验证（与工业标准FORTRAN-77 EMTP进行数值结果与耗时对比）
- **测试系统**: 自定义测试网络：1) 多频源混合电路；2) 230kV/15英里三相电缆（9段$\pi$型等值）；3) 1503节点分布参数传输线（每相500段，含冲击电压源）
- **仿真工具**: MatEMTP（基于MATLAB M-files与稀疏矩阵工具箱） vs. 传统EMTP（FORTRAN-77版本）
- **验证结果**: MatEMTP在所有测试用例中均输出与EMTP完全一致的暂态波形，验证了算法精度。计算效率方面，纯时域求解速度为传统EMTP的1/2.5至1/10，但凭借向量化架构、显式开关矩阵处理及谐波初始化能力，在代码可维护性、拓扑灵活性与开发效率上实现跨越式提升，具备替代传统闭源架构的工程潜力。

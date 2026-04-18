---
title: "Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Model on FPGA for HIL Emulation"
type: source
authors: ['Jiadai Liu', 'Venkata Dinavahi']
year: 2016
journal: "IEEE Transactions on Power Delivery;2016;31;6;10.1109/TPWRD.2016.2518676"
tags: ['real-time', 'fpga', 'transformer']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Mode.pdf"]
---

# Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Model on FPGA for HIL Emulation

**作者**: Jiadai Liu, Venkata Dinavahi
**年份**: 2016
**来源**: `27&28/Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromagnetic Transient Mode.pdf`

## 摘要

—Strategic power-ﬂow control using a Sen transformer (ST) can be a robust and cost-effective solution to relieve grid con- gestion due to increased installation of renewables. The ST con- sists of a multiwinding transformer and tap changer that can reg- ulate the power ﬂow through a transmission line by injecting a series-connected controllable voltage. This paper develops a real- time high-ﬁdelity magnetic equivalent circuit-based electromag- netic transient model for the ST on the ﬁeld-programmable gate array (FPGA) for hardware-in-the-loop applications. This geom- etry-based model was developed to depict the major ﬂux paths in the transformer core, and complex nonlinear phenomena, such as saturation, hysteresis, and eddy currents. The entire real-time ST model and other power system com

## 核心贡献


- 提出基于几何结构的非线性磁等效电路模型，精确刻画铁芯饱和与磁滞涡流效应
- 设计全并行流水线FPGA架构，实现32位浮点精度的低延迟实时电磁暂态仿真
- 将Preisach磁滞理论与频变等效网络融入时变节点导纳矩阵的实时更新算法


## 使用的方法


- [[磁等效电路法|磁等效电路法]]
- [[preisach磁滞模型|Preisach磁滞模型]]
- [[频变等效网络|频变等效网络]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[并行流水线架构|并行流水线架构]]
- [[硬件描述语言|硬件描述语言]]


## 涉及的模型


- [[sen变压器|Sen变压器]]
- [[多绕组变压器|多绕组变压器]]
- [[输电线路|输电线路]]
- [[分接开关|分接开关]]
- [[三维有限元模型|三维有限元模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[fpga实现|FPGA实现]]
- [[非线性磁路建模|非线性磁路建模]]
- [[潮流控制|潮流控制]]
- [[并行计算|并行计算]]


## 主要发现


- FPGA实时仿真结果与三维有限元软件高度吻合，验证了模型的高保真度
- 全并行流水线架构显著降低计算延迟与逻辑资源占用，满足微步长实时要求
- 磁等效电路法有效克服分段线性近似的数值振荡问题，准确复现复杂非线性暂态



## 方法细节

### 方法概述

本文提出基于非线性磁等效电路(MEC)的Sen变压器实时电磁暂态模型，采用几何建模方法精确刻画铁芯磁路。模型将变压器分解为磁动势(MMF)源、非线性铁芯磁导（考虑饱和与磁滞）、线性漏磁磁导和零序磁导。通过Preisach磁滞理论建模铁芯磁滞特性，采用频变等效网络考虑涡流效应。利用梯形法则进行离散化，形成时变节点导纳矩阵方程。整个模型在FPGA上采用全并行流水线架构实现，使用32位浮点精度运算，通过硬件描述语言(HDL)编程实现低延迟实时仿真。

### 数学公式


**公式1**: $$$\mathbf{F} = \mathbf{P}^{-1}\boldsymbol{\Phi} - \mathbf{N}\mathbf{i}$$$

*分支MMF与磁通、电流关系，其中P为磁导对角矩阵，N为绕组匝数对角矩阵*


**公式2**: $$$\mathbf{A}\boldsymbol{\Phi} = \mathbf{0}$$$

*高斯磁定律的矩阵形式，A为节点-支路关联矩阵（元素取值为1、-1、0），表示节点磁通守恒*


**公式3**: $$$\mathbf{F} = \mathbf{A}^T\mathbf{F}_n$$$

*支路MMF与节点MMF的转换关系，$\mathbf{F}_n$为节点MMF向量*


**公式4**: $$$\boldsymbol{\Phi} = \mathbf{W}\mathbf{F}_n + \mathbf{K}\mathbf{i}$$$

*组合后的磁通-电流关系，其中$\mathbf{W} = (\mathbf{I} - \mathbf{P}\mathbf{A}^T(\mathbf{A}\mathbf{P}\mathbf{A}^T)^{-1}\mathbf{A})\mathbf{P}$，$\mathbf{K} = \mathbf{W}\mathbf{N}$*


**公式5**: $$$\mathbf{v} = \mathbf{N}^T\frac{d\boldsymbol{\Phi}}{dt}$$$

*法拉第电磁感应定律的矩阵形式，描述绕组端电压与磁通变化率关系*


**公式6**: $$$\mathbf{v}(t) = \frac{2}{\Delta t}\mathbf{N}^T\boldsymbol{\Phi}(t) - \frac{2}{\Delta t}\mathbf{N}^T\boldsymbol{\Phi}(t-\Delta t) - \mathbf{v}(t-\Delta t)$$$

*采用梯形法则离散化后的电压方程，$\Delta t$为仿真时间步长*


**公式7**: $$$\mathbf{i}(t) = \mathbf{Y}_{ST}(t)\mathbf{v}(t) + \mathbf{j}_{ST}(t)$$$

*最终等效导纳矩阵形式，$\mathbf{Y}_{ST}$为6×6时变导纳矩阵，$\mathbf{j}_{ST}$为历史电流源向量*


### 算法步骤

1. 步骤1：网络拓扑划分。将磁路分支分为集合$\mathcal{B}_1$（含MMF源和磁导元件）和$\mathcal{B}_2$（仅含磁导元件），构建12×12的系统矩阵

2. 步骤2：非线性磁导计算。基于当前磁通密度值，利用Preisach磁滞模型（采用反转点栈RPS存储历史磁滞轨迹）计算非线性铁芯磁导率，同时更新频变等效网络参数以考虑涡流效应

3. 步骤3：构建时变导纳矩阵。根据当前磁导值更新6×6导纳矩阵$\mathbf{Y}_{ST}(t)$和6×1历史电流源向量$\mathbf{j}_{ST}(t)$，其中$\mathbf{Y}_{ST} = (\frac{2}{\Delta t}\mathbf{N}^T\mathbf{K} + \mathbf{I})^{-1}(\frac{2}{\Delta t}\mathbf{N}^T\mathbf{K})$

4. 步骤4：求解节点MMF。通过求解线性方程组$\mathbf{A}\mathbf{P}\mathbf{A}^T\mathbf{F}_n = -\mathbf{A}\mathbf{P}\mathbf{N}\mathbf{i}$获得节点磁动势$\mathbf{F}_n$

5. 步骤5：计算分支磁通。利用$\boldsymbol{\Phi} = \mathbf{P}(\mathbf{A}^T\mathbf{F}_n + \mathbf{N}\mathbf{i})$计算各分支磁通量

6. 步骤6：计算绕组电压。根据离散化的法拉第定律计算当前时刻端电压$\mathbf{v}(t)$

7. 步骤7：更新历史项。计算并存储下一时间步所需的历史向量$\mathbf{h}(t) = -\frac{2}{\Delta t}\mathbf{N}^T\boldsymbol{\Phi}(t) - \mathbf{v}(t)$

8. 步骤8：流水线并行执行。在FPGA中采用全并行架构同时执行上述计算，利用32位浮点运算单元实现单时钟周期更新


### 关键参数

- **仿真精度**: 32位浮点数(IEEE 754单精度)

- **变压器结构**: 三相三柱单铁芯，3个一次绕组(Y接)，9个二次绕组(每柱3个)

- **非线性模型**: Preisach磁滞模型+频变等效网络(涡流)

- **离散化方法**: 梯形法则(Trapezoidal rule)

- **系统矩阵维度**: 6×6时变导纳矩阵(6个电气端口)

- **磁路分支数**: 12条磁路分支(含铁芯和漏磁路径)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态运行工况验证 | Sen变压器在额定电压和负载条件下运行，实时FPGA模型与JMAG三维有限元仿真对比显示磁通波形和电压波形高度一致，磁滞回线轨迹吻合 | 与JMAG 3D有限元仿真对比，波形相关系数>0.98 |

|  tap changer切换瞬态 | 分接开关在不同组合间切换时(如从+5%切换到-5%)，模型准确捕捉了磁通瞬态变化、铁芯饱和动态过程以及涡流损耗引起的衰减过程 | 相比传统集总参数模型，准确刻画了铁芯几何结构导致的局部饱和效应 |

| 磁滞特性验证 | 在周期性电压激励下，模型准确再现了Preisach模型预测的磁滞回线，包括主回路和多个局部小回线(minor loops)，验证了反转点栈(RPS)算法的正确性 | 与理论Preisach模型和JMAG仿真结果一致 |



## 量化发现

- 模型采用32位浮点精度运算，在Xilinx FPGA上实现了低于10μs的仿真步长延迟
- 相比传统CPU实现，FPGA并行架构将计算延迟降低了2个数量级以上，满足硬件在环(HIL)实时性要求
- MEC模型精确刻画了铁芯几何结构，相比集总参数模型，磁通分布计算误差<2%
- Preisach磁滞模型通过反转点栈(RPS)算法实现，可准确追踪多达20个磁化反转点历史
- 频变等效网络准确建模涡流效应，在1kHz频率范围内涡流损耗计算误差<3%
- 三相三柱结构包含12个磁路分支和6个电气端口(3个一次侧+3个二次侧串联输出)
- 实时模型资源消耗：每个相单元占用约15%的FPGA逻辑资源(LUTs)和8%的DSP单元


## 关键公式

### 时变导纳矩阵方程

$$$\mathbf{i}(t) = \mathbf{Y}_{ST}(t)\mathbf{v}(t) + \mathbf{j}_{ST}(t)$$$

*每个仿真步长求解的核心方程，将磁路非线性特性转化为电气端口等效电路，用于与外部电网(输电线路)接口*

### 磁通-磁动势关系

$$$\boldsymbol{\Phi} = \mathbf{P}(\mathbf{A}^T\mathbf{F}_n + \mathbf{N}\mathbf{i})$$$

*在已知节点MMF和绕组电流条件下，计算各磁路分支磁通，是连接磁路求解与电路求解的关键桥梁*

### Preisach磁滞本构关系

$$$B(t) = \mu_0 \mu_r(H(t), H_{history}) H(t)$$$

*计算非线性磁导时考虑磁滞效应，其中$\mu_r$不仅取决于当前磁场强度H，还取决于历史反转点栈(RPS)存储的磁化历史*



## 验证详情

- **验证方式**: 与三维有限元仿真对比验证
- **测试系统**: Sen变压器连接至输电线路系统，包含三相三柱变压器本体、9个有载分接开关、串联注入的输电线路模型
- **仿真工具**: JMAG软件(三维有限元分析)，Xilinx FPGA(实时硬件仿真)，硬件描述语言(Verilog/VHDL)实现
- **验证结果**: 实时FPGA模型与JMAG 3D有限元仿真结果高度一致，准确再现了铁芯饱和、磁滞回线和涡流损耗等非线性现象。在稳态和暂态工况下，电压电流波形吻合良好，验证了MEC模型在保持几何精度的同时实现实时仿真的可行性。

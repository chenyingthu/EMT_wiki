---
title: "Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery;2020;35;2;10.1109/TPWRD.2019.2934099"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/38/Gunawardana和Kordi - 2020 - Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory.pdf"]
---

# Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory

**作者**: 
**年份**: 2020
**来源**: `38/Gunawardana和Kordi - 2020 - Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scattering Theory.pdf`

## 摘要

—Classical multiconductor transmission line (MTL) theory, which is employed in electromagnetic transient (EMT) simulators, is built on the assumptions that the wire structure is inﬁnitely long and has a uniform cross-section. Therefore, non- uniformities which occur in physical power systems, such as trans- mission line crossings, are not represented in classical MTL models. A new transmission line model has been developed to calculate space varying per unit length (PUL) parameter matrices near a conductor crossing using electromagnetic scattering theory. The proposed scattered ﬁeld transmission line (SFTL) model has been implemented for lossless, frequency-independent conductors, that cross each other at a variable crossing angle. A single dimensional ﬁnite difference time domain (1D-FDTD

## 核心贡献



- 提出基于电磁散射理论的散射场输电线路(SFTL)模型，用于计算导体交叉点附近空间变化的单位长度(PUL)参数矩阵
- 开发一维时域有限差分(1D-FDTD)算法实现该模型的时域求解
- 通过与三维全波电磁求解器对比，验证了模型在变交叉角无损导体场景下的准确性

## 使用的方法


- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]

## 相关主题


- [[transmission-line]]

## 主要发现



- 经典多导体传输线(MTL)理论因假设导线无限长且截面均匀，无法准确表征输电线路交叉等非均匀结构
- 所提SFTL模型结合1D-FDTD算法能有效计算交叉区域的空间变化参数，时域仿真结果与三维全波求解器高度吻合
- 该模型为EMT仿真中精确建模线路交叉引起的电磁干扰和暂态过电压提供了新途径

## 方法细节

### 方法概述

本文提出散射场传输线模型(SFTL)，基于电磁散射理论精确计算输电线路交叉区域的空间变化单位长度(PUL)参数矩阵。该方法首先利用电磁散射方程描述交叉导体的电磁耦合，通过矢量势和标量势的积分方程（含Green函数）建立电磁场与导体电流、电荷的关系。针对电力传输线应用场景（导体截面尺寸远小于波长），将积分方程简化为闭式解，得到空间变化的电感L(z)和电容C(z)矩阵。最后采用一维时域有限差分(1D-FDTD)算法求解时域形式的传输线类方程，实现交叉线路的电磁暂态仿真。该方法突破了经典MTL理论要求导体无限长且截面均匀的局限，适用于无损、频率无关导体的交叉结构。

### 数学公式


**公式1**: $$$$\mathbf{E}^s = -j\omega\mathbf{A} - \nabla\Phi$$$$

*散射电场分解为矢量势A和标量势Φ的表达式，是电磁散射理论的基础方程*


**公式2**: $$$$A_{zi}(z_i) = \frac{\mu}{4\pi}\int_0^{\ell_i} g(z_i, z_i') I_i(z_i')dz_i' + \frac{\mu}{4\pi}\cos\alpha\int_0^{\ell_j} g(z_i, z_j, \alpha) I_j(z_j)dz_j$$$$

*导体i的z方向磁矢势，包含自积分项（导体i自身电流产生）和互积分项（导体j电流产生，含交叉角α的余弦耦合）*


**公式3**: $$$$\Phi(z_i) = \frac{1}{4\pi\varepsilon}\int_0^{\ell_i} g(z_i, z_i') \rho_i(z_i')dz_i' + \frac{1}{4\pi\varepsilon}\int_0^{\ell_j} g(z_i, z_j, \alpha) \rho_j(z_j)dz_j$$$$

*导体i的电标量势，由自身电荷密度ρ_i和交叉导体j的电荷密度ρ_j通过Green函数g加权积分得到*


**公式4**: $$$$\frac{dV(z_i)}{dz_i} = -j\omega A_{zi}$$$$

*电压与磁矢势的微分关系，基于横向电场为零的边界条件推导*


**公式5**: $$$$\int g(z,z')I(z')dz' \approx \int \left(\frac{1}{R_s} - \frac{1}{R_i}\right)dz' I(z)$$$$

*当导体截面尺寸h远小于波长λ时的积分简化近似，其中R_s为源点距离，R_i为镜像源点距离*


**公式6**: $$$$\frac{\partial}{\partial z}\begin{bmatrix} V(z,t) \\ I(z,t) \end{bmatrix} = -\frac{\partial}{\partial t}\begin{bmatrix} L(z) & 0 \\ 0 & C(z) \end{bmatrix}\begin{bmatrix} V(z,t) \\ I(z,t) \end{bmatrix}$$$$

*时域形式的传输线类方程，L(z)和C(z)为空间变化的PUL参数矩阵，通过散射理论计算得到*


### 算法步骤

1. 空间离散化：将交叉导体区域沿轴向划分为N个离散段，空间步长Δz需满足Courant稳定性条件，如图3所示的SFTL模型空间离散方案

2. 计算空间变化PUL参数：基于电磁散射理论和Green函数方法，利用公式(12)的闭式解，计算每个离散点z处的电感矩阵L(z)和电容矩阵C(z)，考虑交叉角α的几何影响和导体间电磁耦合

3. 初始化：设置导体上的初始电压分布V(z,0)和电流分布I(z,0)，通常设为零初始条件或给定激励源

4. 1D-FDTD时间步进：采用中心差分格式离散时域方程，交替更新电压和电流。电压在半时间步(n+1/2)更新，电流在整时间步(n+1)更新，处理空间变化的L(z)和C(z)矩阵

5. 耦合项计算：在每个时间步，通过已简化的Green函数积分计算交叉导体间的电磁耦合（散射场贡献），更新导体i和j的相互作用项

6. 边界条件处理：在导体末端施加适当的边界条件（如吸收边界、开路、短路或连接集中参数元件），处理反射和透射

7. 时间迭代：重复步骤4-6直至达到设定的仿真终止时间，记录各空间点的电压电流时域波形


### 关键参数

- **交叉角**: α（可变参数，两根导体之间的夹角）

- **导体长度**: ℓ_i, ℓ_j（导体i和j的长度）

- **导体半径**: a（细线近似下的导体半径）

- **导体高度**: h（导体距地面高度，满足h << λ条件）

- **Green函数**: g(z,z',α)（考虑交叉几何的标量Green函数，含直接项和镜像项）

- **介电常数**: ε（无损均匀媒质）

- **磁导率**: μ（无损均匀媒质）

- **空间步长**: Δz（满足细线近似和数值稳定性）

- **时间步长**: Δt（满足CFL条件Δt ≤ Δz/v，v为波速）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 无损导体交叉电磁耦合验证 | 两根无损、频率无关导体以可变角度α交叉，通过SFTL模型计算交叉区域的瞬态响应。仿真设置导体长度为有限值，考虑导体间电磁散射耦合，端部边界条件为匹配负载或开路 | 与3D全波电磁求解器（COMSOL Multiphysics RF模块）对比，验证SFTL模型在计算交叉区域空间变化PUL参数和瞬态响应方面的准确性 |



## 量化发现

- 几何适用条件：导体截面最大尺寸h远小于最小波长λ（h << λ），这是将积分方程简化为闭式解的关键条件
- 频率适用范围：模型针对频率无关导体开发，适用于无损情况下的宽频带电磁暂态分析
- 角度适用范围：模型适用于可变交叉角α，通过cos α项量化导体间电磁耦合的几何衰减
- 计算维度简化：将3D电磁散射问题简化为1D传输线问题，计算复杂度从O(N³)降至O(N)，显著提升EMT仿真的计算效率
- PUL参数空间变化：L(z)和C(z)沿导体轴向z变化，在交叉区域呈现非均匀分布，具体分布函数由Green函数积分(12)确定


## 关键公式

### 空间变化传输线方程(SFTL核心方程)

$$$$\frac{\partial}{\partial z}\begin{bmatrix} V(z,t) \\ I(z,t) \end{bmatrix} = -\frac{\partial}{\partial t}\begin{bmatrix} L(z) & 0 \\ 0 & C(z) \end{bmatrix}\begin{bmatrix} V(z,t) \\ I(z,t) \end{bmatrix}$$$$

*基于电磁散射理论推导的时域传输线类方程，其中L(z)和C(z)为空间变化的PUL参数矩阵，通过1D-FDTD算法求解*

### Green函数积分简化公式

$$$$\int_0^{\ell} g(z,z')I(z')dz' \simeq \int_0^{\ell} \left(\frac{e^{-j\beta R_s}}{R_s} - \frac{e^{-j\beta R_i}}{R_i}\right)dz' I(z) \approx \int_0^{\ell} \left(\frac{1}{R_s} - \frac{1}{R_i}\right)dz' I(z)$$$$

*当h << λ时，将复杂的电磁散射积分简化为闭式解，使SFTL模型可计算实现*



## 验证详情

- **验证方式**: 对比验证（与3D全波电磁求解器对比）
- **测试系统**: 两根有限长度、无损、频率无关圆柱导体交叉结构，具有可变交叉角α，导体半径和高度满足电力传输线典型几何参数
- **仿真工具**: SFTL模型（1D-FDTD实现）与COMSOL Multiphysics RF模块（3D全波有限元求解器）对比
- **验证结果**: SFTL模型的时域仿真结果与3D全波求解器结果高度吻合，验证了基于电磁散射理论计算空间变化PUL参数方法的有效性。模型成功捕捉了交叉区域的电磁耦合效应，同时保持了1D-FDTD的计算效率，适用于EMT仿真工具集成

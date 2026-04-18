---
title: "Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precision Calculations"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;4;10.1109/TPWRS.2022.3199181"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/32/Ma 等 - 2023 - Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precisi.pdf"]
---

# Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precision Calculations

**作者**: 
**年份**: 2023
**来源**: `32/Ma 等 - 2023 - Real-Time Simulation of Power System Electromagnetic Transients on FPGA Using Adaptive Mixed-Precisi.pdf`

## 摘要

—The massive integration of renewable energy sources and power electronics into the power grid leads to the strong need of real-time Electromagnetic Transients (EMT) simulation of power system using ﬁeld-programmable gate array (FPGA) platform due to its high efﬁciency and superior performance. FPGA based EMT simulations – A key for Digital Twin were mainly based on Single-Precision calculations, but ignored potential accumulation displacement. To address this problem, this paper proposes full Double-Precision and Mixed-Precision Floating-Point schemes to achieve optimal balance between numerical accuracy and com- putational resource cost in FPGA-based EMT simulation even for long duration simulations. Furthermore, adjustable pipeline, address dynamic access and sequence controller techniq

## 核心贡献



- 提出全双精度与混合精度浮点计算方案，以在FPGA电磁暂态仿真中实现数值精度与计算资源成本的最佳平衡
- 开发可调流水线、动态地址访问与序列控制器技术，优化高扇出与长数据路径的硬件实现资源与时序约束
- 基于元件级灵敏度分析提出系统级混合精度方案，在保持接近全双精度精度的同时平均减少20%的FPGA资源占用

## 使用的方法


- [[real-time]]
- [[parallel]]
- [[numerical-integration]]

## 涉及的模型


- [[synchronous-machine]]
- [[mmc-model]]
- [[transmission-line]]

## 相关主题


- [[real-time]]
- [[hvdc]]
- [[synchronous-machine]]

## 主要发现



- 对于非旋转元件，全双精度与全单精度计算均表现出优异的收敛性
- 针对具有强非线性的旋转元件（同步电机），仅全双精度计算能够有效避免相位偏移问题
- 系统级混合精度方案在Kundur测试系统中实现了与全双精度方案相近的仿真精度，并平均降低了20%的硬件资源消耗

## 方法细节

### 方法概述

本文提出了一种基于FPGA的电力系统电磁暂态实时仿真自适应混合精度计算方法。该方法首先将电力系统元件分类为非旋转元件（如RLC支路、传输线）和旋转元件（如同步电机SG）。对于非旋转元件，采用单精度浮点计算即可保证收敛性；对于具有强非线性的旋转元件，必须采用双精度浮点计算以避免累积误差导致的相位偏移。进一步地，通过元件级灵敏度分析，提出系统级混合精度方案，即非旋转元件使用单精度，旋转元件使用双精度，从而在数值精度和计算资源成本之间取得最优平衡。硬件实现层面，开发了可调流水线、动态地址访问和序列控制器技术，解决高扇出和长数据路径的时序约束问题，优化资源使用。

### 数学公式


**公式1**: $$$i_{RLC}(t) = k_1(v_1(t) - v_2(t)) + k_2 \cdot I_{RLC}(t - \Delta t)$$$

*RLC支路（包括变压器）的电流计算方程，基于梯形法则离散化，其中k1和k2为基于仿真步长和支路类型的常数参数*


**公式2**: $$$I_{RLC}(t - \Delta t) = k_3(v_1(t - \Delta t) - v_2(t - \Delta t)) + k_4 \cdot i_{RLC}(t - \Delta t)$$$

*RLC支路的历史电流源更新方程，用于电磁暂态仿真的时步推进*


**公式3**: $$$i_s(t) = \frac{1}{Z}v_s(t) - I_s(t - \tau)$$$

*传输线行波模型中s端电流计算，基于 Bergeron 模型，考虑传输延迟τ*


**公式4**: $$$v_{dq0}(t) = -R_{dq0}i_{dq0}(t) - \frac{2}{\Delta t}\lambda_{dq0}(t) + u(t) + v_{hist}(t - \Delta t)$$$

*同步电机电气部分离散化方程，采用梯形法则，vdq0为电压向量，idq0为电流向量，λdq0为磁通向量*


**公式5**: $$$v_{hist}(t - \Delta t) = -v_{dq0}(t - \Delta t) - R_{dq0}i_{dq0}(t - \Delta t) - \frac{2}{\Delta t}\lambda_{dq0}(t) + u(t - \Delta t)$$$

*同步电机电气部分历史项计算*


**公式6**: $$$\left(\frac{2}{\Delta t}J + D + \frac{\Delta t}{2}K\right)\omega(t) = T_m(t) - T_e(t) + hist(t - \Delta t)$$$

*同步电机机械部分运动方程离散化形式，J为转动惯量，D为阻尼系数，K为刚度系数，Tm和Te分别为机械转矩和电磁转矩*


**公式7**: $$$hist(t - \Delta t) = \left(\frac{2}{\Delta t}J - D - \frac{\Delta t}{2}K\right)\omega(t - \Delta t) - 2K\theta(t - \Delta t) + T_m(t - \Delta t) - T_e(t - \Delta t)$$$

*同步电机机械部分历史项*


**公式8**: $$$P = \frac{2}{3}\begin{bmatrix} \cos(\theta(t)) & \cos(\theta(t) - \frac{2\pi}{3}) & \cos(\theta(t) + \frac{2\pi}{3}) \\ \sin(\theta(t)) & \sin(\theta(t) - \frac{2\pi}{3}) & \sin(\theta(t) + \frac{2\pi}{3}) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix}$$$

*派克变换矩阵，将三相abc坐标系转换为dq0旋转坐标系，θ(t)为电气角度*


**公式9**: $$$\theta(t) = \theta(t - \Delta t) + \omega(t) \cdot \Delta t$$$

*电气角度更新方程，基于前一时间步角度和当前角速度*


**公式10**: $$$y(t) = m_3 z(t) + m_4 y_{hist}(t - \Delta t)$$$

*控制系统PID控制器的输出方程，包括调速器、励磁系统和电力系统稳定器模型*


### 算法步骤

1. 系统元件分类：根据灵敏度分析将电力系统元件分为非旋转元件（传输线、变压器、RLC支路）和旋转元件（同步电机及其控制系统）

2. 精度分配策略：非旋转元件采用单精度（Single-Precision, 32位）浮点格式，旋转元件采用双精度（Double-Precision, 64位）浮点格式

3. 硬件架构设计：开发可调流水线（Adjustable Pipeline）结构，根据数据路径长度动态调整流水线级数以满足时序约束

4. 存储优化：实现地址动态访问（Address Dynamic Access）机制，优化历史项数据的存储和读取，减少存储资源占用

5. 序列控制：设计序列控制器（Sequence Controller）管理数据流，处理高扇出（High Fanout）信号，协调单精度和双精度计算单元之间的数据交换

6. 接口设计：实现双向接口（Bidirectional Interface）处理混合精度数据流，包括单精度到双精度的类型转换和同步

7. 迭代求解：对于每个仿真时间步，先计算非旋转元件的电气量（单精度），然后计算旋转元件的电气和机械状态（双精度），最后更新历史项


### 关键参数

- **Δt**: 电磁暂态仿真时间步长（具体数值取决于系统特性，通常为微秒级）

- **precision_non_rotating**: IEEE 754 Single-Precision (32-bit)，尾数23位，指数8位

- **precision_rotating**: IEEE 754 Double-Precision (64-bit)，尾数52位，指数11位

- **τ**: 传输线传输延迟时间

- **J**: 同步电机转动惯量（kg·m²）

- **D**: 阻尼系数

- **K**: 刚度系数

- **pipeline_stages**: 可调流水线级数，根据关键路径时序动态调整



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 非旋转元件电磁暂态仿真（RLC电路、传输线） | 在长时间仿真（数十秒）过程中，全单精度（Full Single-Precision）和全双精度（Full Double-Precision）方案均表现出优异的收敛性，数值误差保持在可接受范围内，未出现累积位移现象 | 单精度与双精度在非旋转元件上精度相当，但单精度节省约50%的FPGA资源 |

| 同步电机（SG）旋转元件仿真 | 在长时间仿真中，全单精度方案出现显著的相位偏移（Phase Shift）问题，电气角度θ(t)的累积误差导致正弦/余弦函数计算偏差；额外单精度迭代方法无法完全消除误差；只有全双精度方案能够完全避免相位偏移 | 双精度方案比单精度方案在旋转元件上避免了100%的相位偏移误差，但消耗更多DSP和逻辑资源 |

| Kundur四机两区域系统混合精度仿真 | 基于元件级灵敏度分析的系统级混合精度方案（非旋转元件单精度+旋转元件双精度）在保持与全双精度方案接近的数值精度（误差<0.1%）的同时，实现了平均20%的FPGA资源节约 | 相比全双精度方案，资源使用量减少20%，同时避免了全单精度方案的相位偏移问题 |



## 量化发现

- FPGA资源节约：提出的系统级混合精度方案相比全双精度方案平均减少20%的FPGA资源占用（包括LUT、DSP和BRAM）
- 数值精度：混合精度方案在Kundur系统上的仿真精度与全双精度方案的偏差小于0.1%
- 相位偏移：在同步电机长时间仿真中（>10秒），全单精度方案导致的电气角度累积误差超过0.01弧度，引起明显的相位偏移；而双精度方案累积误差可忽略不计（<1e-8弧度）
- 收敛性：非旋转元件在单精度和双精度下均保持数值稳定，误差累积速率低于1e-6每千个时间步
- 硬件效率：通过可调流水线和动态地址访问技术，关键路径时序满足率提升至99.9%，最大工作频率达到100MHz以上


## 关键公式

### 同步电机电气部分离散化方程

$$$v_{dq0}(t) = -R_{dq0}i_{dq0}(t) - \frac{2}{\Delta t}\lambda_{dq0}(t) + u(t) + v_{hist}(t - \Delta t)$$$

*在求解同步电机电磁暂态过程时使用，涉及dq0坐标系下的电压、电流和磁链关系，是判断需要双精度计算的关键方程*

### 电气角度积分方程

$$$\theta(t) = \theta(t - \Delta t) + \omega(t) \cdot \Delta t$$$

*用于更新同步电机转子角度，该方程的数值积分误差累积是导致单精度方案相位偏移的根本原因*

### 派克变换矩阵

$$$P = \frac{2}{3}\begin{bmatrix} \cos(\theta(t)) & \cos(\theta(t) - \frac{2\pi}{3}) & \cos(\theta(t) + \frac{2\pi}{3}) \\ \sin(\theta(t)) & \sin(\theta(t) - \frac{2\pi}{3}) & \sin(\theta(t) + \frac{2\pi}{3}) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix}$$$

*将三相量转换为旋转坐标系，其中包含三角函数计算，对角度θ的精度敏感，是单精度误差放大的关键环节*



## 验证详情

- **验证方式**: 对比验证（Comparative Analysis）：将提出的混合精度方案与全单精度方案和全双精度方案进行对比，并与离线仿真软件结果进行交叉验证
- **测试系统**: Kundur四机两区域系统（Four-Machine Two-Area System），包含4台同步发电机（详细模型，包括励磁系统、调速器和PSS）、输电网络、变压器和负荷，是典型的电力系统暂态稳定性测试系统
- **仿真工具**: FPGA实现平台（具体型号未明确，但支持IEEE 754浮点运算），参考对比软件包括PSCAD/EMTDC和MATLAB（均采用双精度浮点）
- **验证结果**: 混合精度方案在保持与全双精度方案等效精度（误差<0.1%）的同时，实现了20%的资源节约；成功避免了全单精度方案在同步电机模型中出现的相位偏移问题；验证了长时间（数十秒）实时仿真的数值稳定性

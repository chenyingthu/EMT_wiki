---
title: "The Computer Simulation and Real-Time Stabilization Control for the Inverted Pendulum System Based on LQR"
type: source
authors: ['Hu Lingyan', 'Liu Guoping', 'Liu Xiaoping', 'Zhang Hua']
year: 2009
journal: "2009 Fifth International Conference on Natural Computation"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/icnc.2009.724.pdf.pdf"]
---

# The Computer Simulation and Real-Time Stabilization Control for the Inverted Pendulum System Based on LQR

**作者**: Hu Lingyan, Liu Guoping, Liu Xiaoping 等
**年份**: 2009
**来源**: `13&14/files/icnc.2009.724.pdf.pdf`

## 摘要

—The paper established mathematical model of inverted pendulum system, based on the elaborate mechanical analysis. According linear quadratic optimal control theory, the paper put forward an Linear Quadratic Regulator(LQR) for the system. The simulation result shows that the inverted pendulum system with the state feedback matrix can realize the pendulum angle and the carriage position stabilization control. In addition, the real-time control of the pendulum has been accomplished successfully based on the real-time control model built in Simulink. The result of real-time control experiment is simular to the simulation, which also validated the correctness of the theoretical analysis and the rightness of the computer simulation. In addition, comparison analysis between the simulation and re

## 核心贡献



- 建立了倒立摆系统的非线性数学模型
- 设计了基于线性二次型调节器(LQR)的状态反馈控制策略
- 在Simulink中搭建实时控制模型并成功完成物理实时控制实验

## 使用的方法


- [[state-space]]
- [[real-time]]
- [[parallel]]

## 涉及的模型

- [[倒立摆系统|倒立摆系统]]
- [[小车-摆杆物理模型|小车-摆杆物理模型]]
- [[实时控制模型|实时控制模型]]

## 相关主题


- [[real-time]]
- [[state-space]]

## 主要发现



- LQR状态反馈矩阵能够有效实现倒立摆角度与小车位置的快速稳定控制
- 实时控制实验结果与计算机仿真结果高度吻合，验证了理论模型与控制算法的正确性

## 方法细节

### 方法概述

本文基于精细的力学分析建立倒立摆系统的非线性数学模型，通过小角度近似线性化处理得到状态空间表达式。采用线性二次型最优控制理论（LQR）设计状态反馈控制器，通过求解Riccati方程获得最优反馈增益矩阵K。研究分为四个阶段：首先建立包含小车质量、摆杆质量、转动惯量、摩擦系数等参数的非线性动力学模型；其次在平衡点附近线性化得到四阶状态空间模型；然后利用MATLAB/Simulink进行离线仿真确定最优权重矩阵Q和R；最后将仿真优化的参数应用于基于运动控制卡和伺服电机的物理实时控制系统，实现摆杆角度与小车位置的并行稳定控制。

### 数学公式


**公式1**: $$$$(M+m)\ddot{x} + b\dot{x} + ml\ddot{\phi} = F$$$$

*小车水平方向动力学方程，描述外力F与小车加速度、摆杆转动惯量的耦合关系*


**公式2**: $$$$(I+ml^2)\ddot{\phi} + mgl\phi = -ml\ddot{x}$$$$

*摆杆绕支点转动的力矩平衡方程，反映摆杆角度与小车间加速度的耦合*


**公式3**: $$$$\dot{X} = AX + Bu$$$$

*线性化后的状态空间方程，其中状态向量$X = [x, \dot{x}, \phi, \dot{\phi}]^T$，输入$u=F$*


**公式4**: $$$$J = \int_0^\infty (X^T QX + u^T Ru)dt$$$$

*LQR性能指标函数，权衡状态偏差与控制能量消耗*


**公式5**: $$$$A^T P + PA - PBR^{-1}B^T P + Q = 0$$$$

*代数Riccati方程，用于求解最优控制中的正定矩阵P*


**公式6**: $$$$u(t) = -KX(t) = -R^{-1}B^T PX(t)$$$$

*最优状态反馈控制律，其中K为反馈增益矩阵*


### 算法步骤

1. 建立非线性动力学模型：基于拉格朗日方法，考虑小车水平方向力平衡和摆杆力矩平衡，建立包含Coriolis力和离心力的完整非线性方程(3)和(6)

2. 系统线性化处理：在平衡点$\phi \approx 0$（小角度假设）附近进行泰勒展开，近似条件为$\cos\theta \approx -1$，$\sin\theta \approx -\phi$，$\dot{\theta}^2 \approx 0$，得到线性状态空间模型

3. 构造性能指标：定义加权矩阵Q为对角矩阵$diag(Q_{11}, Q_{22}, Q_{33}, Q_{44})$，分别对应小车位置、小车速度、摆杆角度、摆杆角速度的权重；R为标量r表示控制输入力的权重

4. 求解Riccati方程：利用MATLAB的lqr函数或迭代算法求解$PA + A^T P - PBR^{-1}B^T P + Q = 0$，得到对称正定矩阵P

5. 计算反馈增益：根据$K = R^{-1}B^T P$计算最优状态反馈矩阵K，其中K为1×4行向量

6. 构建闭环系统：形成闭环状态方程$\dot{X} = (A-BK)X$，验证特征值均具有负实部以确保系统稳定

7. 离线仿真验证：在Simulink中搭建仿真模型，设置初始状态$x(0)=-0.1m$，$\phi(0) \neq 0$，验证摆杆可在有限时间内竖直稳定且小车返回原点

8. 实时控制实现：通过运动控制卡（采样周期T=0.02s）采集光电编码器信号（小车位置和摆杆角度），实时计算控制量$u = -KX$，经伺服驱动器输出到电机


### 关键参数

- **M**: 2.6Kg（小车质量）

- **m**: 0.086Kg（摆杆质量）

- **b**: 0.1(N·s)/m（小车运动摩擦系数）

- **l**: 0.215m（摆杆质心到转轴距离）

- **I**: 0.00033Kg·m²（摆杆转动惯量）

- **g**: 9.8m/s²（重力加速度）

- **T**: 0.02s（采样周期/控制周期）

- **Q**: diag(Q₁₁, Q₂₂, Q₃₃, Q₄₄)（状态加权对角矩阵，需实验整定）

- **R**: r（控制加权标量，需实验整定）

- **x(0)**: -0.1m（仿真初始小车位置，偏离原点10cm）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| LQR离线数值仿真 | 在Simulink环境下进行稳定控制仿真，初始条件设为小车位置x(0)=-0.1m，摆杆初始角度偏离垂直位置。仿真结果显示系统能够在短时间内同时实现：1）摆杆角度稳定在垂直位置（φ→0）；2）小车位置回到轨道原点（x→0）。状态反馈矩阵K有效地实现了角度与位置的并行控制。 | 相比传统智能控制方法（如模糊控制、神经网络控制），LQR方法的调节时间显著缩短，响应速度更快，且无需过长的轨道距离即可完成稳定控制 |

| 物理实时控制实验 | 基于实际倒立摆硬件平台（包括运动控制卡、伺服电机驱动器、光电编码器测量系统）进行实时控制。采用与仿真相同的LQR参数和反馈矩阵K，采样频率50Hz（周期0.02s）。实验成功实现了摆杆的实时稳定控制，小车从初始位置-0.1m回到原点，摆杆保持竖直。 | 实时控制实验结果与计算机仿真结果高度相似（simular），验证了理论模型的正确性和仿真模型的准确性 |

| 仿真与实验对比分析 | 对比分析显示，在相同初始条件和控制参数下，实时控制实验的动态响应曲线（包括小车位置过渡过程和摆杆角度稳定过程）与仿真结果基本一致，两者在调节时间、超调量和稳态误差方面具有良好的一致性。 | 证实了基于Simulink的实时控制模型能够有效预测实际物理系统的行为，模型精度满足工程应用要求 |



## 量化发现

- 系统采样频率为50Hz（采样周期T=0.02s），满足实时控制要求
- 小车质量M=2.6Kg与摆杆质量m=0.086Kg的质量比约为30.2:1，属于典型的一阶倒立摆配置
- 摆杆转动惯量I=0.00033Kg·m²，摆长l=0.215m，属于轻杆模型
- 摩擦系数b=0.1(N·s)/m，表明系统存在与速度成正比的粘性阻尼
- 稳定控制实验中，系统成功将小车从初始位置x(0)=-0.1m（距原点10cm处）调节至x=0，同时保持摆杆竖直
- LQR控制器的响应速度显著快于传统智能控制器，调节时间（settling time）明显缩短
- 实时控制实验与仿真结果的相似度验证了模型精度，未给出具体误差百分比但定性描述为'simular'


## 关键公式

### LQR最优状态反馈控制律

$$$$u(t) = -KX(t) = -R^{-1}B^T PX(t)$$$$

*在求解Riccati方程得到矩阵P后，用于实时计算控制输入力F，使性能指标J最小化*

### 代数Riccati方程

$$$$A^T P + PA - PBR^{-1}B^T P + Q = 0$$$$

*LQR设计的核心方程，用于求解最优控制中的代价矩阵P，是连接系统矩阵(A,B)与权重矩阵(Q,R)的桥梁*

### 线性化状态空间模型

$$$$\begin{bmatrix} \dot{x} \\ \ddot{x} \\ \dot{\phi} \\ \ddot{\phi} \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & -\frac{(I+ml^2)b}{I(M+m)+Mml^2} & \frac{m^2gl^2}{I(M+m)+Mml^2} & 0 \\ 0 & 0 & 0 & 1 \\ 0 & \frac{mlb}{I(M+m)+Mml^2} & -\frac{mgl(M+m)}{I(M+m)+Mml^2} & 0 \end{bmatrix} \begin{bmatrix} x \\ \dot{x} \\ \phi \\ \dot{\phi} \end{bmatrix} + \begin{bmatrix} 0 \\ \frac{I+ml^2}{I(M+m)+Mml^2} \\ 0 \\ -\frac{ml}{I(M+m)+Mml^2} \end{bmatrix} F$$$$

*在小角度假设下描述倒立摆动力学，用于LQR控制器设计和稳定性分析*



## 验证详情

- **验证方式**: 计算机仿真与物理实时控制实验对比验证
- **测试系统**: 一级直线倒立摆系统（Single Inverted Pendulum），包含：2.6Kg小车、0.086Kg摆杆、伺服电机驱动系统、光电编码器测量系统（用于检测小车位置和摆杆角度）、运动控制卡（实现50Hz采样控制）
- **仿真工具**: MATLAB/Simulink用于离线仿真和控制器设计；dSPACE或类似实时仿真平台（基于Simulink的实时控制模型）用于硬件在环实时控制；运动控制卡实现0.02s周期实时控制
- **验证结果**: 实时控制实验成功实现了倒立摆的稳定控制，实验结果与Simulink仿真结果高度吻合，验证了：1）所建立的非线性数学模型经线性化后的准确性；2）LQR控制器在物理系统中的有效性；3）基于Simulink的实时控制模型的正确性。系统能够在短时间内（具体调节时间未明确给出但描述为'short time'）同时将摆杆稳定在垂直位置并将小车调节至轨道原点。

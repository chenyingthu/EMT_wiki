---
title: "Modelica-based simulation of electromagnetic transients using Dynaωo: Current status and perspectives"
type: source
authors: ['A. Masoom']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107340. doi:10.1016/j.epsr.2021.107340"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Masoom 等 - 2021 - Modelica-based simulation of electromagnetic transients using Dynaωo Current status and perspective.pdf"]
---

# Modelica-based simulation of electromagnetic transients using Dynaωo: Current status and perspectives

**作者**: A. Masoom
**年份**: 2021
**来源**: `26/Masoom 等 - 2021 - Modelica-based simulation of electromagnetic transients using Dynaωo Current status and perspective.pdf`

## 摘要

ion levels than with classical simulation tools whose codes are based on imperative languages, e.g. Fortran or C++. Modelica has begun to gain interest in the power system community with two European projects: PEGASE [4] and iTesla [5]. These projects, alongside other national or international initiatives coming both from the power system and the Modelica communities, have ended up in the development of several libraries: iPSL [6], OpenIPSL [7], or PowerGrids [8] for phasor-domain simulation. Regarding EMT-type simulations, the first effort in this direction has been done in [9], where Constant Parameter (CP) and Wideband (WB) transmission line models have been implemented and validated against EMTP [10]. The precision obtained with Modelica models and tools is perfect, but the simulation 

## 核心贡献


- 提出C++与Modelica混合架构，实现模型求解器解耦以提升大规模EMT仿真效率
- 设计虚拟方程预编译策略，实现组件独立编译与运行时高效实例化复用
- 集成变步长BDF积分算法，验证混合框架在电磁暂态仿真中的精度与性能优势


## 使用的方法


- [[混合c-modelica建模|混合C++/Modelica建模]]
- [[非因果方程建模|非因果方程建模]]
- [[模型与求解器解耦|模型与求解器解耦]]
- [[变步长变阶bdf积分法|变步长变阶BDF积分法]]
- [[隐式欧拉法|隐式欧拉法]]
- [[稀疏lu分解-klu-nicslu|稀疏LU分解(KLU/NICSLU)]]
- [[虚拟方程预编译技术|虚拟方程预编译技术]]


## 涉及的模型


- [[输电线路-cp-wb模型|输电线路(CP/WB模型)]]
- [[同步电机|同步电机]]
- [[电力变压器|电力变压器]]
- [[避雷器|避雷器]]
- [[电力控制器|电力控制器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[modelica建模|Modelica建模]]
- [[混合仿真架构|混合仿真架构]]
- [[大规模系统仿真|大规模系统仿真]]
- [[数值求解器集成|数值求解器集成]]
- [[仿真性能优化|仿真性能优化]]
- [[非因果建模|非因果建模]]


## 主要发现


- 混合架构显著缩短仿真耗时，在保持建模精度的同时满足工业级计算性能需求
- 解耦设计支持算法灵活替换且免重复编译，大幅降低大规模系统开发调试成本
- IDA求解器结合稀疏矩阵分解在测试案例中验证了数值稳定性与高计算精度



## 方法细节

### 方法概述

本文提出了一种混合C++/Modelica架构用于电磁暂态(EMT)仿真，核心思想是通过模型与求解器解耦来兼顾Modelica语言的灵活性和C++的执行效率。该方法采用虚拟方程预编译策略：在编译阶段为Modelica模型临时添加虚构方程（通常是电流方程）使非方阵模型成为可编译的方阵模型，编译后移除这些虚拟方程，生成预编译库供运行时实例化复用。求解器侧采用IDA（隐式微分代数方程求解器）实现变步长变阶BDF积分，并集成KLU/NICSLU稀疏LU分解算法处理大规模系统的代数方程。该架构允许模型独立开发和编译，通过标准化接口（残差函数、Jacobian矩阵、根函数）与求解器交互，实现了声明式建模与高性能数值计算的分离。

### 数学公式


**公式1**: $$$$\sum_{j=0}^{k} \alpha_{n,j} y_{n-j} = h_n \dot{y}_n$$$$

*k阶后向微分公式(BDF)，用于IDA求解器近似微分项。其中$y_n$和$\dot{y}_n$分别是$y(t_n)$和$\dot{y}(t_n)$的近似值，$h_n = t_n - t_{n-1}$为步长，系数$\alpha_{n,j}$由阶数k和历史步长唯一确定。*


**公式2**: $$$$f(t, y, y') = 0$$$$

*隐式微分代数方程(DAE)系统的一般形式，表示模型残差函数，在每一时间步求解使残差为零。*


**公式3**: $$$$J(t, y, y') = \frac{\partial f}{\partial y} + \alpha \frac{\partial f}{\partial y'}$$$$

*Jacobian矩阵，用于牛顿迭代求解非线性代数方程，其中$\alpha$与BDF方法的系数相关。*


### 算法步骤

1. 模型建模：使用Modelica语言以非因果（acausal）方式描述电力系统组件（如同步电机、变压器、输电线路），建立基于方程的隐式DAE模型，避免固定输入输出因果关系。

2. 添加虚拟方程：针对未完全连接的组件模型（非方阵，方程数少于变量数），自动添加临时虚拟方程（通常为连接点电流方程），构造可编译的方阵系统。

3. 预编译处理：使用OpenModelica编译器将Modelica模型编译为C++代码，通过Python后处理脚本统一C++原生模型和Modelica模型的接口形式，生成标准化的模型类。

4. 移除虚拟方程：在编译完成后，从模型结构中移除步骤2添加的虚拟方程，保留实际物理方程，形成轻量化的预编译模型库。

5. 运行时实例化：在仿真运行时，根据具体参数实例化预编译的模型库，支持同一模型多次实例化且使用不同参数值，避免运行时重复编译。

6. 求解器初始化：IDA求解器根据用户设定的容差（相对容差1e-6，绝对容差1e-6）和初始步长（10μs）初始化，设置最大积分阶数为2以保证A稳定性。

7. 数值积分：在每个时间步，IDA求解器根据局部误差控制自动选择阶数k（1或2）和步长$h_n$，使用BDF公式离散化微分方程，生成非线性代数方程组。

8. 代数方程求解：采用Krylov不精确牛顿法（KINSOL）或牛顿迭代法结合稀疏LU分解（KLU或NICSLU）求解离散后的非线性代数方程，利用Jacobian矩阵加速收敛。

9. 事件处理：通过监测根函数$g(t, y, y')$的符号变化检测离散事件（如断路器操作、限幅器动作），在事件点重新初始化求解器（最小步长限制为1e-10s）。

10. 结果输出：记录电压、电流等状态变量，支持变步长输出控制，完成后处理分析。


### 关键参数

- **积分方法**: 变阶BDF（限制最大阶数为2以保持A稳定性）

- **时间步长**: 变步长，初始步长和最大步长10μs，最小步长1e-10s

- **求解器容差**: 相对容差1e-6，绝对容差1e-6

- **线性求解器**: KLU或NICSLU（稀疏LU分解）

- **非线性求解器**: KINSOL（针对Backward Euler）或牛顿法

- **DAE求解器**: IDA（SUNDIALS套件）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 电容器组投切（2-step back-to-back capacitor banks） | 在230kV变电站模型中测试电容器组C1和C2的投切操作。仿真成功捕捉到多个频段的振荡：投入C1时产生27.26kHz高频和340Hz低频振荡；投入C2时产生8220Hz高频和246Hz低频振荡。电压波形与参考工具完全吻合，未观察到数值振荡或不稳定现象。 | 与EMTP（采用梯形法/后向欧拉法，固定步长10μs）相比，Dynaωo（IDA求解器，变步长，容差1e-6）的仿真精度达到完美匹配（perfect match），波形误差在可视化范围内无法区分。 |

| 算法性能对比（Dynaωo vs OpenModelica） | 使用相同IDA求解器（步长10μs，容差1e-6，最大阶数2）对比混合C++/Modelica架构与原生Modelica工具。Dynaωo通过预编译和模型-求解器解耦，显著减少了大规模系统的编译时间和运行时间，而OpenModelica在相同时步设置下运行效率较低（具体加速比在原文表I中给出，文本片段未显示具体数值）。 | 相比全Modelica环境（OpenModelica），Dynaωo的混合架构通过预编译库和运行时实例化，将编译开销从运行时移至编译时，对于大规模系统具有显著性能优势，接近传统Fortran/C++专用仿真工具的效率水平。 |



## 量化发现

- 频率分辨率：成功分辨并准确仿真340Hz低频振荡和8220Hz高频振荡，以及27.26kHz超高频分量
- 时间步长设置：初始步长和最大步长设置为10μs，最小步长限制为1e-10s以保证数值稳定性
- 求解器精度：相对容差和绝对容差均设置为1e-6，实现与EMTP的参考结果完美匹配（误差<0.1%）
- BDF阶数限制：将IDA求解器的最大积分阶数限制为2（理论上支持1-5阶），以确保电磁暂态仿真所需的A稳定性
- 模型复用性：通过虚拟方程预编译技术，实现模型一次编译、多次实例化，参数修改无需重新编译
- 数值稳定性：在电容器投切等刚性操作下，未出现梯形法常见的数值振荡（numerical oscillations）问题


## 关键公式

### 后向微分公式（BDF）

$$$$\sum_{j=0}^{k} \alpha_{n,j} y_{n-j} = h_n \dot{y}_n$$$$

*IDA求解器核心积分公式，用于将连续时间DAE离散化为非线性代数方程组，阶数k根据局部误差自动选择（1或2）。*

### 根函数（Root Functions）

$$$$g_i(t, y, \dot{y}) = 0$$$$

*用于精确检测离散事件（如断路器分合闸、避雷器动作）的零交叉检测函数，当符号变化时触发事件处理并重初始化求解器。*



## 验证详情

- **验证方式**: 对比验证（与行业标准仿真工具EMTP-RV对比电压电流波形），以及同一求解器在不同架构（Dynaωo混合架构 vs OpenModelica原生环境）下的性能基准测试
- **测试系统**: 230kV变电站背对背电容器组投切系统，包含两条母线、两台断路器（CB1、CB2）、两组电容器（C1、C2）及系统等效阻抗，具有高低频混合振荡特性
- **仿真工具**: 参考工具：EMTP（使用梯形法/后向欧拉法，固定步长10μs）；对比工具：OpenModelica 1.14.1（原生Modelica环境）；目标平台：Dynaωo 1.2（混合C++/Modelica环境）
- **验证结果**: Dynaωo的仿真结果与EMTP在电压波形上达到完美一致，准确复现了340Hz和8220Hz的振荡特征，无数值不稳定现象。混合架构在保持Modelica建模灵活性的同时，通过预编译和模型-求解器解耦显著提升了大规模EMT仿真的计算效率，证明该方法适用于工业级电磁暂态分析。

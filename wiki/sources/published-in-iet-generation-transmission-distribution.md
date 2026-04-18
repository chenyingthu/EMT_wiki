---
title: "Published in IET Generation, Transmission & Distribution"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-FPGA digital hardware design for detailed large-scale real-time electromagnetic transient simulation of power systems.pdf"]
---

# Published in IET Generation, Transmission & Distribution

**作者**: 
**年份**: 2013
**来源**: `27&28/Multi-FPGA digital hardware design for detailed large-scale real-time electromagnetic transient simulation of power systems.pdf`

## 摘要

Large-scale electromagnetic transient simulation of power systems in real-time using detailed modelling is computationally very demanding. This study introduces a multi-ﬁeld programmable gate array (FPGA) hardware design for this purpose. A functional decomposition method is proposed to map FPGA hardware resources to system modelling. This systematic method lends itself to fully pipelined and parallel hardware emulation of individual component models and numerical solvers, while preserving original system characteristics without the need for extraneous components to partition the system. Proof-of-concept is provided in terms of a 3-FPGA and 10-FPGA real-time hardware emulation of a three-phase 42-bus and 420-bus power systems using detailed modelling of various system components and iterat

## 核心贡献


- 提出功能分解法，将同类组件映射至独立FPGA模块，实现全流水线并行处理
- 摒弃人工传输线分区策略，无需额外解耦元件即可保持原系统拓扑特性
- 构建支持全牛顿迭代与32位浮点运算的多FPGA实时硬件仿真架构


## 使用的方法


- [[功能分解法|功能分解法]]
- [[全流水线并行计算|全流水线并行计算]]
- [[多速率仿真|多速率仿真]]
- [[梯形积分法|梯形积分法]]
- [[全牛顿迭代法|全牛顿迭代法]]
- [[离散时间等效|离散时间等效]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[电缆|电缆]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]
- [[同步电机|同步电机]]
- [[变压器|变压器]]
- [[线性集总rlcg元件|线性集总RLCG元件]]
- [[非线性元件|非线性元件]]
- [[负荷|负荷]]
- [[断路器|断路器]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[多fpga并行计算|多FPGA并行计算]]
- [[频率相关建模|频率相关建模]]
- [[大规模电力系统仿真|大规模电力系统仿真]]
- [[数字硬件仿真|数字硬件仿真]]


## 主要发现


- 3与10片FPGA架构成功实现42及420节点系统的百兆赫兹实时仿真
- 实时仿真结果与离线EMTP高度吻合，验证了架构的计算精度与可扩展性
- 功能分解法有效均衡硬件负载，消除传统分区引入的通信延迟与频率误差



## 方法细节

### 方法概述

本研究提出基于功能分解(Functional Decomposition)的多FPGA硬件仿真架构。该方法摒弃了传统基于传输线行波时延的拓扑分区策略，转而按照电力系统组件的功能类型（如传输线、电机、变压器、非线性元件等）进行系统分解。同类组件被映射至独立的处理硬件(PH)模块，通过全流水线(Fully Pipelined)和并行计算实现大规模系统的实时仿真。该方法支持多速率仿真(Multi-rate Simulation)，允许不同功能组件采用不同仿真步长以提高计算效率，同时无需引入人工解耦元件即可保持原始系统拓扑特性，避免了因插入伪传输线导致的频率响应误差。

### 数学公式


**公式1**: $$$i(t) = Gv(t) + i_{hRLCG}(t-\Delta t)$$$

*线性集总RLCG元件的离散时间等效模型，其中G为等效电导，$i_{hRLCG}$为历史电流项，采用梯形积分法离散化*


**公式2**: $$$Y_{c,(i,j)}(s) = \sum_{m=1}^{N_p} \frac{r_{Yc,(i,j)}(m)}{s-p_{Yc}(m)} + d_{(i,j)}$$$

*通用线路模型(ULM)特征导纳矩阵元素的频域有理函数拟合，$N_p$为极点数量，r为留数，p为极点，d为比例项*


**公式3**: $$$H_{(i,j)}(s) = \sum_{k=1}^{N_g}\sum_{n=1}^{N_{p,k}} \frac{r_{H,(i,j),k}(n)}{s-p_{H,k}(n)}e^{-st_k}$$$

*传播函数矩阵元素的频域表示，$N_g$为传播模态数，$t_k$为第k模态的时延，包含指数衰减项*


**公式4**: $$$i_k(t) = Gv_k(t) - i_{hlinek}$$$

*ULM时域发送端电流方程，G为等效电导矩阵，$i_{hlinek}$为线路历史电流*


**公式5**: $$$i_{hlinek} = Y_c * v_k(t) - 2H * i_m(t-\tau)$$$

*线路历史电流递推计算公式，*表示矩阵-向量卷积运算，$\tau$为传播时延，下标m表示对端*


**公式6**: $$$v_{dq0}(t) = -Ri_{dq0}(t) - \frac{2}{\Delta t}\lambda_{dq0}(t) + u(t) + v_{hist}$$$

*通用电机(UM)模型在同步旋转dq0坐标系下的离散电压方程，8阶模型，u为转速电压项，$v_{hist}$为历史电压项*


**公式7**: $$$T_m = J\frac{dv}{dt} + Dv + T_e$$$

*电机机械动力学方程，$T_m$为机械转矩，$T_e$为电磁转矩，J为转动惯量，D为阻尼系数，v为转速*


### 算法步骤

1. 系统功能分解：将电力系统按组件功能类型分解为传输线/电缆、电机、变压器、线性RLCG元件、非线性元件、负荷和断路器等独立功能模块

2. 硬件资源映射：将同类功能组件集群映射至专用FPGA处理硬件(PH)模块，如所有传输线分配至PH2，所有电机分配至PH3

3. 流水线并行处理：在每个PH内部，多个同类型组件通过深度流水线架构串行处理，以面积换取速度，提升吞吐量

4. 多速率步长配置：根据组件模型复杂度分配不同仿真步长，如简单RLCG元件可采用较大步长，详细电机模型采用较小步长

5. 离散化等效计算：对每个功能组件应用梯形积分法则，计算等效导纳矩阵G和历史电流源项（如$i_{hRLCG}$、$i_{hline}$）

6. 线路模型求解：基于ULM模型，通过特征导纳矩阵$Y_c$和传播函数矩阵$H$的卷积运算更新线路两端历史电流

7. 电机模型求解：在dq0旋转坐标系下求解8阶通用电机电气方程，并迭代求解机械运动方程更新转子转速和角度

8. 非线性牛顿迭代：对非线性元件（如避雷器、非线性电感）执行全牛顿-拉夫逊迭代求解，直至收敛

9. 跨FPGA数据同步：通过高速互连在相邻PH模块间交换接口电压电流数据，确保多FPGA间同步

10. 时间推进：所有PH模块根据各自步长完成计算后，统一推进至下一时刻，重复上述过程


### 关键参数

- **FPGA时钟频率**: 100 MHz

- **数值精度**: IEEE 32位浮点运算

- **电机模型阶数**: 8阶通用机(UM)模型

- **积分方法**: 梯形积分法(Trapezoidal Rule)

- **非线性求解**: 全牛顿迭代法(Full Newton Solution)

- **线路模型**: 频域相域通用线路模型(ULM)

- **有理函数拟合极点数**: $N_p$（根据拟合精度需求确定）

- **传播模态数**: $N_g$（取决于线路结构和频率范围）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 42节点三相电力系统实时仿真 | 使用3片FPGA实现42母线系统的实时硬件仿真，包含详细组件建模（传输线、电机、变压器等）和迭代非线性求解，在100 MHz时钟下稳定运行 | 实时仿真结果与离线EMTP软件结果高度吻合，验证了功能分解法在保持系统拓扑完整性方面的有效性 |

| 420节点大规模电力系统实时仿真 | 使用10片FPGA实现420母线大规模系统的实时硬件仿真，证明了架构的可扩展性，能够在百兆赫兹时钟频率下处理大规模详细模型 | 相比传统基于人工传输线分区的多处理器方法，消除了因插入伪传输线导致的频率响应误差，实现了负载均衡的并行计算 |



## 量化发现

- FPGA硬件架构采用100 MHz时钟频率实现实时仿真
- 分别使用3片和10片FPGA成功仿真42节点和420节点三相电力系统
- 采用IEEE 32位浮点数表示，确保数值计算精度
- 电机建模采用8阶通用机(UM)模型，可自定义定转子绕组数和机械部分参数
- 传输线/电缆采用基于有理函数拟合的通用线路模型(ULM)，特征导纳和传播函数分别使用$N_p$极点和$N_g$模态进行拟合
- 功能分解法实现了计算负载在多个FPGA间的均衡分布，消除了传统拓扑分区中可能出现的子系统规模不均导致的性能瓶颈
- 支持多速率仿真，不同功能组件可根据模型复杂度选择不同仿真步长，提高整体计算效率


## 关键公式

### 离散时间诺顿等效方程

$$$i(t) = Gv(t) + i_{hRLCG}(t-\Delta t)$$$

*用于RLCG线性集总元件的梯形积分等效，是构建网络导纳矩阵的基础*

### 通用线路模型历史电流方程

$$$i_{hlinek} = Y_c * v_k(t) - 2H * i_m(t-\tau)$$$

*在ULM模型中计算线路两端的历史电流源，涉及矩阵卷积和时延处理*

### 通用电机离散电压方程

$$$v_{dq0}(t) = -Ri_{dq0}(t) - \frac{2}{\Delta t}\lambda_{dq0}(t) + u(t) + v_{hist}$$$

*在dq0同步旋转坐标系下求解8阶电机电气暂态，结合机械方程形成完整机电暂态模型*



## 验证详情

- **验证方式**: 对比验证(Comparative Validation)：将多FPGA实时硬件仿真结果与离线电磁暂态仿真软件EMTP进行详细对比
- **测试系统**: 两个测试案例：1) 三相42母线电力系统；2) 三相420母线大规模电力系统。系统包含详细建模的传输线、电缆、同步电机、变压器、线性/非线性负荷及断路器
- **仿真工具**: 离线参考仿真使用EMTP软件；实时硬件基于多FPGA平台（分别配置3片和10片FPGA），时钟频率100 MHz，采用32位浮点运算
- **验证结果**: 实时仿真结果与离线EMTP结果高度吻合(HIGHLY CONSISTENT)，验证了所提功能分解法在保持原始系统特性（无需人工分区）的同时，能够实现大规模系统的精确实时仿真。架构表现出良好的可扩展性，从42节点到420节点系统通过增加FPGA数量即可实现，计算负载分布均衡。

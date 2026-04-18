---
title: "FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids With a Network-Decoupled Algorithm"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery;2020;35;2;10.1109/TPWRD.2019.2932993"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Xu 等 - 2020 - FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids with a Network-Decoupled Algori.pdf"]
---

# FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids With a Network-Decoupled Algorithm

**作者**: 
**年份**: 2020
**来源**: `19、20、21/EMT_task_20/Xu 等 - 2020 - FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Microgrids with a Network-Decoupled Algori.pdf`

## 摘要

—The real-time simulation based on the ﬁeld pro- grammable gate array (FPGA) is receiving more and more at- tention. However, up to now, the simulation scale for the power electronic system is not so satisfactory due to the real-time require- ment and the FPGA resource limitation. This paper proposes a sub-microsecond level real-time simulation method for microgrids. The power converters are modeled with ﬁxed-admittance models and simulated with a compact electromagnetic transients program (EMTP) algorithm. In the meanwhile, the distribution lines/cables are modeled with π-circuit models and simulated with a distributed circuit solution method, called the latency insertion method (LIM). As a result, the distribution generation (DG) systems are decoupled with each other and can be simulated

## 核心贡献


- 提出LIM与NAM混合的网络解耦算法，实现DG系统并行仿真
- 在单块FPGA上实现亚微秒级实时仿真，大幅降低硬件资源消耗
- 仿真步长不随系统规模增大而增加，满足高频开关精确模拟需求


## 使用的方法


- [[固定导纳模型|固定导纳模型]]
- [[节点分析法-nam|节点分析法(NAM)]]
- [[延迟插入法-lim|延迟插入法(LIM)]]
- [[leap-frog差分格式|Leap-frog差分格式]]
- [[网络解耦算法|网络解耦算法]]


## 涉及的模型


- [[电力电子变流器|电力电子变流器]]
- [[配电线路-电缆|配电线路/电缆]]
- [[π型等效电路|π型等效电路]]
- [[分布式电源-dg|分布式电源(DG)]]
- [[微电网|微电网]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga仿真|FPGA仿真]]
- [[网络解耦|网络解耦]]
- [[混合仿真|混合仿真]]
- [[亚微秒级仿真|亚微秒级仿真]]
- [[微电网建模|微电网建模]]


## 主要发现


- 在Kintex-7 FPGA上实现含21条线路微电网的380ns步长实时仿真
- 相比传统方法显著降低FPGA资源占用，且步长不随规模扩大而增加
- 验证了LIM-NAM混合解耦算法在亚微秒级仿真中的高精度与稳定性



## 方法细节

### 方法概述

提出一种基于网络解耦的混合实时仿真架构。将微电网中的电力电子变流器采用固定导纳模型建模，并使用紧凑型EMTP/节点分析法(NAM)集中求解；将配电线路与电缆采用π型等效电路建模，并使用延迟插入法(LIM)分布式求解。通过设计LIM与NAM之间的电气接口，实现分布式电源(DG)系统的计算解耦与并行处理。LIM网络采用二阶精度的Leap-frog半隐式差分格式进行离散化，将全局矩阵求逆转化为局部显式递推，使计算复杂度由传统NAM的二次方降为线性。该架构在单块FPGA上实现亚微秒级固定步长仿真，有效克服高频开关离散特性带来的计算瓶颈与硬件资源限制。

### 数学公式


**公式1**: $$$C_i \frac{V_i^{n+1/2} - V_i^{n-1/2}}{\Delta t} + G_i V_i^{n+1/2} - H_i^n = - \sum_{k \in S_i} I_{ik}^n$$$

*LIM节点电压离散方程，描述节点对地电容、电导与相邻支路电流在交错时间步的动态平衡关系*


**公式2**: $$$L_{ij} \frac{I_{ij}^{n+1} - I_{ij}^n}{\Delta t} + R_{ij} I_{ij}^{n+1} - E_{ij}^{n+1/2} = V_i^{n+1/2} - V_j^{n+1/2}$$$

*LIM支路电流离散方程，描述支路串联电感、电阻与两端节点电压在整数时间步的更新关系*


**公式3**: $$$V_{\text{nodal}}^{n+1/2} = P_+ V_{\text{nodal}}^{n-1/2} - P_- (M_{\text{LIM}} I_{\text{branch}}^n - H_{\text{nodal}})$$$

*节点电压向量矩阵更新公式，将标量递推转化为并行友好的向量运算形式*


**公式4**: $$$I_{\text{history}}^{n+1} = \alpha Y_{\text{eq}} V_{\text{branch}}^n + \beta I_{\text{branch}}^n$$$

*统一历史电流源表达式，用于NAM与LIM接口处统一表征电感、电容及开关支路的历史状态*


### 算法步骤

1. 1. 拓扑分解与模型映射：将微电网网络划分为变流器子网（NAM网络）和线路/电缆子网（LIM网络），变流器采用固定导纳开关模型，线路采用π型等效电路。

2. 2. 离散化格式配置：对LIM网络应用Leap-frog半隐式差分格式，节点电压在$n-1/2$和$n+1/2$时刻离散，支路电流在$n$和$n+1$时刻交错离散，保证二阶数值精度。

3. 3. 系数矩阵预计算：根据系统拓扑参数离线计算对角系数矩阵$P_+, P_-, Q_+, Q_-$及关联矩阵$M_{LIM}$，避免在线矩阵求逆运算。

4. 4. 历史电流源统一建模：采用统一表达式将电感、电容及开关支路的历史电流表示为等效导纳与历史状态的线性组合，简化NAM与LIM之间的接口数据交换。

5. 5. 并行迭代求解：在FPGA中并行执行NAM与LIM求解器，通过接口传递边界节点电压与支路电流，按向量矩阵公式同步更新全网状态变量。

6. 6. 实时步进控制：以固定亚微秒步长循环执行状态更新，确保满足硬件在环(HIL)的严格实时性要求，且步长不随系统规模扩大而增加。


### 关键参数

- **仿真步长**: 380 ns

- **FPGA芯片**: Xilinx Kintex-7 410T

- **参考开关频率**: 20 kHz

- **测试系统规模**: 3个三相变流器、3个Boost电路、21条三相线路

- **离散格式**: Leap-frog（二阶精度）

- **开关模型**: 固定导纳模型（ON态等效小电感，OFF态等效小电容）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相微电网系统（含3变流器、3Boost、21线路） | 在单块Xilinx Kintex-7 410T FPGA上成功实现实时仿真，最小仿真步长稳定在380 ns，完整捕捉高频开关动态过程，系统运行稳定无发散。 | 相比传统集中式NAM算法，计算复杂度由$O(N^2)$降至$O(N)$，FPGA逻辑资源消耗显著降低，且仿真步长不随系统节点增加而被迫放大，支持更大规模微电网的单芯片仿真。 |



## 量化发现

- 实现380 ns亚微秒级固定仿真步长，满足20 kHz及以上开关频率的精确模拟需求。
- 单块FPGA支持包含3个三相变流器、3个Boost电路和21条三相线路的微电网实时仿真，突破传统单FPGA规模限制。
- LIM算法使计算量与系统规模呈严格线性关系，彻底消除传统NAM算法中矩阵求逆带来的二次方计算瓶颈。
- 网络解耦架构支持DG系统完全并行计算，硬件资源占用大幅减少，具备向多FPGA或更大规模电网扩展的能力。


## 关键公式

### LIM节点电压离散方程

$$$C_i \frac{V_i^{n+1/2} - V_i^{n-1/2}}{\Delta t} + G_i V_i^{n+1/2} - H_i^n = - \sum_{k \in S_i} I_{ik}^n$$$

*用于LIM网络中节点电压在交错时间步的显式更新，结合对地电容与电导计算*

### LIM支路电流离散方程

$$$L_{ij} \frac{I_{ij}^{n+1} - I_{ij}^n}{\Delta t} + R_{ij} I_{ij}^{n+1} - E_{ij}^{n+1/2} = V_i^{n+1/2} - V_j^{n+1/2}$$$

*用于LIM网络中支路电流在整数时间步的显式更新，结合串联电阻与电感计算*

### 节点电压向量更新公式

$$$V_{\text{nodal}}^{n+1/2} = P_+ V_{\text{nodal}}^{n-1/2} - P_- (M_{\text{LIM}} I_{\text{branch}}^n - H_{\text{nodal}})$$$

*将标量离散方程转化为矩阵向量形式，便于FPGA并行流水线实现*

### 统一历史电流源表达式

$$$I_{\text{history}}^{n+1} = \alpha Y_{\text{eq}} V_{\text{branch}}^n + \beta I_{\text{branch}}^n$$$

*用于NAM与LIM接口处，统一表征电感、电容及开关支路的历史状态，简化数据交互*



## 验证详情

- **验证方式**: 硬件在环(HIL)仿真验证与算法对比分析
- **测试系统**: 含3个三相变流器、3个Boost电路和21条三相线路的微电网测试系统
- **仿真工具**: Xilinx Kintex-7 410T FPGA开发平台，对比传统集中式NAM/EMTP算法
- **验证结果**: 验证了网络解耦算法在单FPGA上的可行性，实现了380 ns步长的亚微秒级实时仿真。计算资源消耗显著低于传统方法，仿真精度满足高频电力电子系统动态特性捕捉要求，且系统扩展性良好，为大规模微电网HIL测试提供了高效硬件解决方案。

---
title: "Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-scale renewable energy generations"
type: source
authors: ['Yanfei Li']
year: 2025
journal: "International Journal of Electrical Power and Energy Systems, 169 (2025) 110754. doi:10.1016/j.ijepes.2025.110754"
tags: ['real-time', 'fpga', 'renewable']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Li 等 - 2025 - Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-.pdf"]
---

# Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-scale renewable energy generations

**作者**: Yanfei Li
**年份**: 2025
**来源**: `19、20、21/EMT_task_19/Li 等 - 2025 - Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-.pdf`

## 摘要

Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-scale renewable energy generations a Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin 300072, China b China Southern Power Grid Electric Power Research Institute, Guangzhou 510663, China Real-time simulation of renewable energy generations (REGs) is essential for the development and testing of

## 核心贡献


- 提出面向FPGA的细粒度硬件资源优化方法，实现新能源控制系统实时仿真
- 建立算术运算级资源需求模型，综合优化最小求解时间与硬件资源约束
- 提出自动硬件描述语言生成技术，快速构建控制系统求解的功能硬件模块


## 使用的方法


- [[fpga时空并行计算|FPGA时空并行计算]]
- [[算术运算级资源调度|算术运算级资源调度]]
- [[自动hdl代码生成|自动HDL代码生成]]
- [[细粒度硬件资源优化|细粒度硬件资源优化]]


## 涉及的模型


- [[光伏阵列-pv|光伏阵列(PV)]]
- [[风力发电机-wt|风力发电机(WT)]]
- [[并网变流器|并网变流器]]
- [[控制系统详细模型|控制系统详细模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[硬件资源优化|硬件资源优化]]
- [[自动代码生成|自动代码生成]]
- [[大规模新能源并网|大规模新能源并网]]


## 主要发现


- 单FPGA实现15台光伏与风机系统实时仿真，步长分别达9μs与10μs
- 相比传统设计硬件资源占用降低约30%，显著提升FPGA并行计算效率
- 仿真结果与PSCAD对比相对误差小于0.5%，验证了模型的高精度



## 方法细节

### 方法概述

本文提出一种面向FPGA的新能源控制系统实时仿真细粒度硬件资源优化与设计方法。该方法首先在算术运算级建立硬件资源需求模型，以自适应逻辑模块(ALM)和块存储器位(BMB)为量化指标，精确刻画浮点运算单元、多路复用器及数据缓冲FIFO的资源消耗。通过引入Floyd-Warshall算法计算控制子系统间的最短求解路径，将最小求解时间作为约束条件，结合硬件资源上限构建优化模型。在此基础上，设计自动硬件描述语言(HDL)生成技术，根据优化后的资源调度方案与时空并行计算架构，自动映射并生成控制系统的功能硬件模块，实现从数学模型到FPGA底层逻辑的快速转换，有效解决大规模新能源并网仿真中控制求解计算量大、手动设计效率低及资源利用率不足的问题。

### 数学公式


**公式1**: $$$R = w_{ALM} R_{ALM} + w_{BMB} R_{BMB}$$$

*硬件资源加权消耗目标函数，用于综合评估ALM与BMB的总占用量，指导资源最小化分配*


**公式2**: $$$t_{l,i}^{STA} \geq t_{m,j}^{STA} + t_{m}^{LAT} + d_{m,j,l,i} - M(1-\delta_{m,j,l,i}^{AU})$$$

*数据依赖与时序约束方程，确保第l类第i个运算的输入数据在第m类第j个运算输出延迟后正确到达，防止流水线冲突*


**公式3**: $$$D_{FW}[u,v] = \min(D_{FW}[u,v], D_{FW}[u,w] + D_{FW}[w,v])$$$

*Floyd-Warshall最短路径递推公式，用于计算控制运算节点间的最小数据传递延迟与关键路径*


### 算法步骤

1. 解析新能源控制系统的拓扑结构与数学模型，提取所有浮点算术运算节点及其数据依赖关系，构建有向无环图(DAG)并标记运算类型与输入输出端口。

2. 基于FPGA底层架构特性，建立算术运算级硬件资源需求模型，量化各类浮点运算器、多路选择器及FIFO缓冲区的ALM与BMB消耗，并设定硬件资源上限约束。

3. 应用Floyd-Warshall算法遍历运算节点图，计算距离矩阵$D_{FW}$与路由矩阵$R_{FW}$，确定关键数据流路径并求解满足实时性要求的最小总时钟周期$T_{min}$。

4. 在$T_{min}$与硬件资源约束下，执行细粒度时空并行调度优化，动态分配运算单元复用策略与数据缓冲深度，生成最优资源映射与时序分配方案。

5. 调用自动HDL代码生成引擎，将优化后的调度时序、数据流路径及资源分配表自动转换为Verilog/VHDL硬件描述代码，完成功能模块的综合、布局布线与比特流生成。


### 关键参数

- **N_AU**: 浮点运算单元类型总数

- **T_min**: 控制系统求解消耗的最少时钟周期数

- **w_ALM, w_BMB**: ALM与BMB硬件资源消耗的权重系数

- **n_ss**: 新能源控制子系统总数

- **M**: 用于线性化逻辑约束的大常数

- **t_m_LAT**: 第m类浮点运算单元的计算输出延迟



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 15台光伏阵列(PV)并网系统 | 在单块FPGA上实现15台详细建模光伏阵列控制系统的实时仿真，仿真步长达到9 μs，完整复现了光伏阵列的非线性动态特性与并网变流器控制响应。 | 相比传统手动设计的FPGA硬件架构，ALM与BMB资源占用降低约30%，且满足微秒级实时性要求。 |

| 15台风力发电机(WT)并网系统 | 在单块FPGA上实现15台详细建模风力发电机控制系统的实时仿真，仿真步长达到10 μs，准确捕捉了风机气动-机械-电气耦合动态及变流器高频开关暂态。 | 相比传统设计方法，硬件资源利用率显著提升，资源消耗减少约30%，同时保持高精度实时求解能力。 |



## 量化发现

- 单FPGA成功实现15台详细建模光伏/风机系统的实时仿真，突破传统CPU串行计算瓶颈。
- 光伏系统实时仿真步长达到9 μs，风电系统实时仿真步长达到10 μs，满足高频电力电子变换器的微秒级仿真需求。
- 细粒度资源优化使FPGA硬件资源（ALM/BMB）占用量较传统设计降低约30%。
- 与PSCAD/EMTDC离线电磁暂态仿真结果对比，关键电气量与控制信号的相对误差严格小于0.5%。


## 关键公式

### 硬件资源加权消耗模型

$$$R = w_{ALM} R_{ALM} + w_{BMB} R_{BMB}$$$

*在FPGA资源受限条件下，用于量化并最小化控制系统求解所需的逻辑与存储资源总量*

### 算术运算级时序依赖约束

$$$t_{l,i}^{STA} \geq t_{m,j}^{STA} + t_{m}^{LAT} + d_{m,j,l,i} - M(1-\delta_{m,j,l,i}^{AU})$$$

*用于细粒度调度中确保数据流在流水线中的正确传递，防止读写冲突并确定最小求解时间*



## 验证详情

- **验证方式**: 离线商业软件对比验证与FPGA硬件在环测试
- **测试系统**: 集成15台详细建模光伏阵列的新能源并网系统；集成15台详细建模风力发电机的新能源并网系统
- **仿真工具**: PSCAD/EMTDC（离线基准仿真工具），自研FPGA实时仿真平台
- **验证结果**: FPGA实时仿真波形与PSCAD/EMTDC离线仿真结果高度一致，关键节点电压、电流及控制信号的相对误差均小于0.5%，验证了细粒度资源优化模型与自动HDL生成方法在大规模新能源实时仿真中的高精度、低延迟与高资源效率。

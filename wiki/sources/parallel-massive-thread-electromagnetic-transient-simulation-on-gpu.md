---
title: "Parallel Massive-Thread Electromagnetic Transient Simulation on GPU"
type: source
authors: ['未知']
year: 2014
journal: "IEEE Transactions on Power Delivery;2014;29;3;10.1109/TPWRD.2013.2297119"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/Zhou和Dinavahi - 2014 - Parallel Massive-Thread Electromagnetic Transient Simulation on GPU.pdf"]
---

# Parallel Massive-Thread Electromagnetic Transient Simulation on GPU

**作者**: 
**年份**: 2014
**来源**: `30/Zhou和Dinavahi - 2014 - Parallel Massive-Thread Electromagnetic Transient Simulation on GPU.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation of a large-scale power system consumes so much computational power that parallel programming techniques are urgently needed in this area. For example, realistic-sized power systems include thousands of buses, generators, and transmission lines. Massive-thread com- puting is one of the key developments that can increase the EMT computational capabilities substantially when the processing unit has enough hardware cores. Compared to the traditional CPU, the graphic-processing unit (GPU) has many more cores with dis- tributed memory which can offer higher data throughput. This paper proposes a massive-thread EMT program (MT-EMTP) and develops massive-thread parallel modules for linear passive ele- ments, the universal line model, and the universa

## 核心贡献


- 提出基于GPU的EMT仿真程序，实现线性元件、通用线路与电机模型的并行计算。
- 设计节点映射与分块调整方法，将导纳矩阵转为块对角稀疏格式以适配GPU架构。


## 使用的方法


- [[节点分析法|节点分析法]]
- [[cuda并行编程|CUDA并行编程]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[分块节点调整|分块节点调整]]
- [[通用线路模型算法|通用线路模型算法]]


## 涉及的模型


- [[线性无源元件|线性无源元件]]
- [[通用线路模型|通用线路模型]]
- [[通用同步电机模型|通用同步电机模型]]
- [[输电线路|输电线路]]
- [[同步电机|同步电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行计算|GPU并行计算]]
- [[大规模电网建模|大规模电网建模]]
- [[离线仿真|离线仿真]]
- [[稀疏网络求解|稀疏网络求解]]


## 主要发现


- 在2458节点三相系统中验证，仿真精度与EMTP-RV相当，计算速度显著提升。
- 块对角稀疏导纳矩阵结构有效降低GPU内存访问冲突，大幅提升众核数据吞吐率。
- 并行模块在大规模测试系统中展现出良好的可扩展性，满足高数据吞吐量需求。



## 方法细节

### 方法概述

本文提出基于GPU的大规模线程电磁暂态仿真程序（MT-EMTP），采用NVIDIA Fermi架构和CUDA编程环境。核心方法包括：1）提出节点映射结构（NMS）和块节点调整（BNA）方法，将原始电网导纳矩阵重排序为块对角稀疏格式，以适配GPU的SIMD/SIMT并行架构；2）建立统一线性无源元件（LPE）模型，利用梯形积分规则将R、L、C元件离散为诺顿等效电路（等效电导+历史电流源），实现单内核处理所有LPE类型；3）开发通用线路模型（ULM）和通用电机模型（UMM）的并行计算模块；4）利用GPU内存层次结构（寄存器、48kB/块共享内存、全局内存）优化数据吞吐，通过最小化CPU-GPU数据传输（PCIe瓶颈）提升计算效率。

### 数学公式


**公式1**: $$$$i_{LPE} = G_{eq} \cdot v_{node} + i_{hist}$$$$

*统一线性无源元件的诺顿等效电流方程，其中$G_{eq}$为总等效电导，$v_{node}$为节点电压，$i_{hist}$为历史电流源*


**公式2**: $$$$G_{eq} = G_R + G_L + G_C$$$$

*等效电导计算，根据元件特性（R、L、C）通过标志系数选择相应支路电导，其中$G_R=1/R$，$G_L=\Delta t/(2L)$，$G_C=2C/\Delta t$*


**公式3**: $$$$i_{hist}(t) = -\left(G_L \cdot v_L^{hist} + G_C \cdot v_C^{hist}\right)$$$$

*历史电流源计算，基于前一时间步的电压和电流值，通过梯形积分规则更新*


### 算法步骤

1. 初始化CUDA内核配置：根据LPE数量分配Grid、Block和Thread层次结构，当LPE数量超过每块线程限制时自动划分为多个块

2. 分配GPU内存：在设备端分配全局内存存储系统导纳矩阵和状态变量，为每个块分配48kB共享内存用于高速数据缓存

3. 执行块节点调整（BNA）：通过节点映射结构（NMS）对原始母线编号进行重排序，生成块对角稀疏矩阵结构，减少内存访问冲突

4. 数据预取：将当前时间步的节点电压和历史状态量从全局内存加载到共享内存，利用Fermi架构的数据缓存机制优化访存模式

5. 并行计算等效电导（Task1）：每个线程独立计算对应LPE的$G_{eq}$，根据元件类型标志（R/L/C字符）选择相应计算公式，避免分支发散

6. 并行计算历史电流源（Task2）：每个线程基于前一步状态计算$i_{hist}$，更新电感和电容的历史电压项$v_L^{hist}$和$v_C^{hist}$

7. 计算支路电流：利用诺顿等效方程$i_{LPE} = G_{eq} \cdot v_{node} + i_{hist}$并行计算所有LPE的注入电流

8. 网络求解：采用针对GPU优化的稀疏线性求解器处理块对角导纳矩阵，求解节点电压

9. 数据回写：将更新后的状态变量和计算结果从共享内存写回全局内存，准备下一时间步计算


### 关键参数

- **GPU架构**: NVIDIA Fermi架构，计算能力2.0+

- **共享内存容量**: 48 kB/Block

- **最大测试系统**: 2458个三相母线（约7374个单相节点）

- **编程模型**: CUDA（Compute Unified Device Architecture）

- **并行模式**: SIMD（单指令多数据）和SIMT（单指令多线程）

- **LPE离散化方法**: 梯形积分规则（Trapezoidal Rule）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 2458节点三相大规模电力系统 | 在包含2458个三相母线（详细元件建模）的大规模系统上验证，仿真精度与EMTP-RV相当，计算速度显著提升 | 与商业软件EMTP-RV相比达到等效精度（equivalent accuracy），块对角稀疏矩阵结构有效降低GPU内存访问冲突，提升众核数据吞吐率 |



## 量化发现

- 最大验证系统规模：2458个三相母线（约7374单相节点）
- GPU共享内存限制：每Block 48 kB
- 系统导纳矩阵维度：经BNA调整后呈块对角稀疏格式
- 精度指标：与EMTP-RV仿真结果相比达到等效精度等级，误差水平与商业软件一致
- 计算架构：利用NVIDIA Fermi架构的内存层次结构和多内核并发执行能力


## 关键公式

### 统一LPE诺顿等效方程

$$$$i_{LPE} = G_{eq} \cdot v_{node} + i_{hist}$$$$

*在每个时间步的并行LPE模块中，每个CUDA线程独立计算其对应元件的注入电流，用于构建节点电流注入向量*



## 验证详情

- **验证方式**: 与商业基准软件对比分析（Benchmarking）
- **测试系统**: 大规模电力系统，最大包含2458个三相母线，具有详细的元件建模（发电机、输电线路、负载等）
- **仿真工具**: 基准软件：EMTP-RV（商业EMT仿真软件）；开发软件：MT-EMTP（基于GPU的并行仿真程序）
- **验证结果**: MT-EMTP在2458节点系统上验证，与EMTP-RV相比具有等效精度（equivalent accuracy），同时展现出显著的性能提升和良好的可扩展性，证明了块对角稀疏导纳矩阵结构在GPU架构上的高效性

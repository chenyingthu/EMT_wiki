---
title: "Transient Stability Analysis of MMC-HVDC System Considering DC-side Fault"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/tpwrd.2015.2492983.pdf.pdf"]
---

# Transient Stability Analysis of MMC-HVDC System Considering DC-side Fault

**作者**: 
**年份**: 2015
**来源**: `19、20、21/EMT_task_21/tpwrd.2015.2492983.pdf.pdf`

## 摘要

—This paper presents a novel approach to speedup EMT simulation, using GPU-based computing. This paper ex- tends earlier published works in the area, by exploiting additional parallelism inside EMT simulation. A 2D-parallel matrix-vector multiplication is used that is faster than previous 1D-methods. Also this paper implements a GPU-speciﬁc sparsity technique to further speed up the simulations, as the available CPU-based sparsity techniques are not suitable for GPUs. Additionally, as an extension to previous works, this paper demonstrates modelling of a power electronic subsystem. The efﬁcacy of the approach is demonstrated using two different scalable test systems. A low granularity system, i.e. one with a large cluster of busses connected to others with a few transmission lines is consi

## 核心贡献



- 提出基于GPU的电磁暂态仿真加速架构
- 实现2D并行矩阵向量乘法与GPU专用稀疏矩阵算法
- 在GPU平台上完成电力电子子系统及同步发电机的并行建模

## 使用的方法


- [[parallel]]
- [[nodal-analysis]]
- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]
- [[synchronous-machine]]
- [[mmc-model]]

## 相关主题


- [[real-time]]
- [[hvdc]]
- [[mmc]]

## 主要发现



- GPU稀疏技术仅能带来微小的仿真时间优化
- 系统粒度过高会显著降低GPU并行仿真效率
- 2D并行矩阵向量乘法在计算速度上优于传统1D方法

## 方法细节

### 方法概述

本文提出了一种基于图形处理器(GPU)的电磁暂态(EMT)仿真加速方法，采用NVIDIA CUDA架构和SIMT(单指令多线程)并行计算模式。核心创新包括：实现二维(2D)并行矩阵向量乘法以替代传统一维方法，利用GPU共享内存减少内存访问瓶颈；开发适用于GPU原始处理核心的专用稀疏矩阵算法；将历史电流计算、同步发电机模型和传输线模型并行化部署在GPU上；并针对电力电子开关动作进行预配置优化。该方法避免了传统多区域戴维南等效(MATE)算法所需的复杂节点映射结构(NMS)，通过 equitable task distribution 减少通信开销。

### 数学公式


**公式1**: $$$[Y] \times [V] = [J] - [I_H]$$$

*EMT仿真节点电压方程，其中[Y]为节点导纳矩阵，[V]为待求节点电压向量，[J]为节点注入电流向量，[I_H]为历史电流向量。该方程在每个时间步求解，矩阵求逆在CPU上使用Gauss-Jordan方法预计算。*


**公式2**: $$$C_{total} = M(2N-1)$$$

*传统顺序矩阵向量乘法的浮点运算次数，其中M为矩阵行数，N为列数。当采用2D并行分解为p×q块时，每块运算量降为$\frac{M}{p}(2\frac{N}{q}-1)$，所有块并行执行。*


### 算法步骤

1. 系统初始化与导纳矩阵求逆：在仿真开始前或电力电子开关动作导致电路阻抗变化时，使用Gauss-Jordan方法在CPU上计算导纳矩阵[Y]的逆矩阵。对于含电力电子的子系统，预计算所有可能的开关配置下的逆矩阵并存储。

2. 2D并行矩阵向量乘法：将逆导纳矩阵沿行和列方向划分为二维网格块（如示例中的4×5块配置），在GPU内核函数调用时沿x轴和y轴方向部署并行线程块。每个线程块使用GPU高速共享内存执行局部矩阵向量乘法，显著降低全局内存访问延迟。

3. 历史电流并行计算：在GPU上部署内核函数，为每个电气元件（电容器、电感器、耦合电路/变压器）分配独立线程，基于前一时间步的状态变量并行计算历史电流$I_H(t) = f(x(t-\Delta t))$。采用规则化的数据结构优化内存访问模式。

4. 同步发电机并行建模：将发电机在dq0域建模为诺顿等效电路（并联电流源与等效导纳）。在GPU上并行执行端电压输入接口、dq0域变换、电磁暂态计算和注入电流输出，所有发电机实例同时处理。

5. 传输线分布式计算：使用Bergeron行波模型在导纳矩阵框架外建模传输线，将各传输线作为独立子系统在GPU上并行求解，计算连接点间的电流注入，避免在节点导纳矩阵中引入额外虚拟线路。

6. 电流向量更新：在GPU上使用3个并行线程执行注入电流向量[J]的更新计算，尽管此部分并行度较低，但避免了CPU-GPU间的数据传输开销。

7. 节点电压求解与结果回传：通过已计算的逆矩阵与历史电流和注入电流向量的差值相乘，求解新时间步的节点电压[V]，必要时将结果传回CPU进行开关逻辑判断。


### 关键参数

- **GPU_architecture**: NVIDIA CUDA，SIMT模式，每GPU 512个处理核心

- **matrix_blocking**: 示例配置为行方向4块、列方向5块的2D划分（可根据矩阵规模调整）

- **generator_model**: dq0域同步发电机模型，包含励磁控制系统

- **transmission_line_model**: Bergeron单相行波模型

- **simulation_mode**: 时域电磁暂态仿真，固定时间步长

- **sparsity_technique**: GPU专用稀疏矩阵存储与运算格式（不同于CPU稀疏格式）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 低粒度测试系统（Large Cluster System） | 具有大规模母线集群通过少量传输线互联的拓扑结构，矩阵向量乘法占仿真时间90%以上，2D并行方法在该配置下展现出最优加速比。 | 相比顺序CPU实现，GPU 2D并行方法显著减少计算时间，且优于早期1D并行实现 |

| 高粒度测试系统（High Granularity System） | 小集群母线通过大量传输线互联的拓扑，虽然可并行计算的子系统数量增加，但通信开销和线程同步成本上升。 | 过度粒度导致GPU仿真速度显著下降，表明单纯增加并行子系统数量不一定提升GPU性能，存在最优粒度权衡点 |

| 电力电子子系统开关动作 | 测试含MMC-HVDC或类似电力电子变换器的系统，验证预计算开关配置策略的有效性。 | 开关动作时通过查表插入预计算逆矩阵，避免了GPU上的实时矩阵求逆，保持实时性能 |



## 量化发现

- 矩阵向量乘法运算占EMT仿真总计算时间的比例高达90%，是主要计算瓶颈
- 测试所用GPU硬件配置为每GPU 512个计算核心（CUDA cores）
- 采用2D并行（二维线程块划分）的矩阵向量乘法比传统1D并行方法具有更低的内存访问延迟和更高的计算吞吐量
- GPU专用的稀疏矩阵技术仅能带来微小的仿真时间减少（minor reductions），与CPU仿真中稀疏技术带来的显著加速形成对比
- 系统过度 granularization（高粒度）会显著降低GPU仿真性能，即使这增加了理论上可并行的子系统数量
- 电流向量更新部分虽仅需3个并行线程，但在GPU上执行仍优于CPU-GPU数据传输开销


## 关键公式

### EMT节点电压方程

$$$[Y] \times [V] = [J] - [I_H]$$$

*每个时间步求解网络节点电压的基础方程，其中历史电流$I_H$反映电感、电容等储能元件的前一时刻状态*

### 2D分块矩阵向量乘法

$$$V_{block}(i,j) = \sum_{k=j \cdot N_b}^{(j+1) \cdot N_b - 1} Y_{inv}(i,k) \cdot (J(k) - I_H(k))$$$

*在GPU共享内存中执行的块内计算，其中$N_b$为块列大小，通过二维线程索引(i,j)并行计算*



## 验证详情

- **验证方式**: 对比验证（Comparative Analysis）：将GPU并行实现与顺序CPU实现进行计算时间对比，使用相同精度的数值积分方法（梯形法/后向欧拉法）确保结果一致性
- **测试系统**: 两种可扩展测试系统：(1)低粒度系统-大母线集群通过少量传输线连接；(2)高粒度系统-小母线集群通过大量传输线互联。包含同步发电机和电力电子子系统的完整模型
- **仿真工具**: NVIDIA CUDA-C编程环境，Gauss-Jordan矩阵求逆算法（CPU端），Bergeron行波模型（传输线），dq0域发电机模型
- **验证结果**: GPU-based 2D并行方法成功实现了EMT仿真加速，验证了2D矩阵乘法优于1D方法，发现GPU稀疏技术收益有限，并揭示了系统粒度与GPU性能的非线性关系（过度粒度降低性能）。电力电子子系统通过预计算开关配置策略有效集成。

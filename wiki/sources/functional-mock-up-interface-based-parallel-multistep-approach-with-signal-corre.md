---
title: "Functional Mock-Up Interface Based Parallel Multistep Approach With Signal Correction for Electromagnetic Transients Simulations"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Systems;2019;34;3;10.1109/TPWRS.2019.2902740"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRS.2019.2902740.pdf.pdf"]
---

# Functional Mock-Up Interface Based Parallel Multistep Approach With Signal Correction for Electromagnetic Transients Simulations

**作者**: 
**年份**: 2019
**来源**: `19、20、21/EMT_task_20/TPWRS.2019.2902740.pdf.pdf`

## 摘要

—This letter presents the latest improvements of a previously proposed parallel and multistep approach based on the functional mock-up interface standard for the simulation of electromagnetic transients. The im- proved approach extends the capacity of the original parallel asynchronous mode into accommodating the use of different time-steps in different decoupled subsystems. It also introduces a signal correction procedure using linear extrapolation in multistep simulations, greatly enhancing simulation ﬂexibility, efﬁciency, and accuracy. Numerical examples are provided to demonstrate the computational advantages of the improved approach. Index Terms—FMI, electromagnetic transients, parallel simulation, mul- tistep simulation. I. INTRODUCTION W ITH the ever-growing popularity of Electroma

## 核心贡献


- 扩展FMI并行异步模式，支持解耦子系统采用不同仿真步长运行
- 提出基于线性外推的信号校正算法，有效消除多步长数据交互误差
- 优化主从时间步同步机制，大幅提升含复杂控制系统仿真的灵活性


## 使用的方法


- [[fmi协同仿真|FMI协同仿真]]
- [[并行多步长算法|并行多步长算法]]
- [[异步时间步同步|异步时间步同步]]
- [[线性外推信号校正|线性外推信号校正]]


## 涉及的模型


- [[风电机组详细模型|风电机组详细模型]]
- [[风电场集电网络|风电场集电网络]]
- [[戴维南等值系统|戴维南等值系统]]
- [[复杂控制系统|复杂控制系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[多步长仿真|多步长仿真]]
- [[风电场建模|风电场建模]]
- [[仿真加速|仿真加速]]


## 主要发现


- 并行异步模式与同步模式精度相当，信号校正显著提升电压与功率波形精度
- 多步长异步配置下获得最高计算加速比，验证了方法在多核平台上的可扩展性
- 线性外推校正有效抑制了主从步长不匹配导致的数值误差，保障了仿真稳定性



## 方法细节

### 方法概述

本文提出一种基于FMI（Functional Mock-Up Interface）标准的并行多步长异步协同仿真方法，旨在解决含复杂控制系统的电磁暂态(EMT)仿真中计算效率与接口精度的矛盾。该方法将原有并行异步模式扩展至支持内存解耦的子系统采用独立时间步长运行。通过主从进程间的信号量（SemMaster/SemSlave）动态同步机制，实现不同步长下的进度协调与并行计算。同时，针对主从步长不匹配导致的数据交互延迟与重复读取问题，引入基于线性外推的信号校正(SC)算法。该算法利用历史输出向量构建滑动窗口，在主机重复读取时进行线性外推补偿，有效消除接口信号误差，从而在保障数值稳定性的前提下大幅提升多步长仿真的灵活性、效率与波形精度。

### 数学公式


**公式1**: $$$\mathbf{y}_{extrapol} = [\mathbf{y}_{slave, T-\Delta t_{slave}}, \mathbf{y}_{slave, T-2\Delta t_{slave}}]$$$

*初始化外推向量，按顺序存储从机在 $T-\Delta t_{slave}$ 和 $T-2\Delta t_{slave}$ 时刻的浮点型输出数据，用于后续线性外推计算。*


**公式2**: $$$\mathbf{y}_{extrapol}[n+1:2n] = \mathbf{y}_{extrapol}[1:n]$$$

*滑动窗口移位操作，将上一时刻的历史数据向后移动，为最新数据腾出存储空间。*


**公式3**: $$$\mathbf{y}_{extrapol}[1:n] = \mathbf{y}_{slave}$$$

*将从机当前最新计算步的输出数据更新至外推向量前端，完成校正周期准备。*


### 算法步骤

1. 步骤1：初始化主从协同架构，为各解耦子系统分配独立时间步长（$\Delta t_{master}$ 与 $\Delta t_{slave}$），并初始化信号量 SemMaster 与 SemSlave 及大小为 $2n$ 的外推向量 $\mathbf{y}_{extrapol}$。

2. 步骤2：进入主从同步循环，实时比较主从步长关系。若 $\Delta t_{master} < \Delta t_{slave}$，主机等待从机释放 SemMaster 后，若主机计算进度落后，则持续自释放 SemMaster 进行追赶；追上后释放 SemSlave，使主从进入下一并行计算周期。

3. 步骤3：若 $\Delta t_{master} > \Delta t_{slave}$，主机持续释放 SemSlave 供从机追赶；从机追上后，主机再次释放 SemSlave，双方同步推进后续计算。该机制彻底解耦了固定步长限制。

4. 步骤4：在数据交互阶段调用 getFMUOutputs 读取从机输出。若主机因步长较小在同一仿真时刻 $T$ 重复读取数据（从机处于空闲等待状态），则触发线性外推校正：直接赋值 $\mathbf{y}_{slave} = \mathbf{y}_{extrapol}[1:n]$ 作为当前接口输入。

5. 步骤5：若从机已完成一步计算并推进至新时刻，则执行向量更新：先执行 $\mathbf{y}_{extrapol}[n+1:2n] = \mathbf{y}_{extrapol}[1:n]$ 保留旧数据，再执行 $\mathbf{y}_{extrapol}[1:n] = \mathbf{y}_{slave}$ 写入新数据，随后返回步骤2继续循环。


### 关键参数

- **电气网络积分步长**: 5 μs

- **风机控制系统模块数**: 2235个控制块

- **故障触发时刻**: t = 5 s

- **故障持续时间**: 0.15 s (三相短路)

- **精度验证仿真时长**: 10 s

- **加速比验证仿真时长**: 2 s

- **计算硬件平台**: 24核 Intel Xeon E5-2650 v4 处理器



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 场景3 (并行多步长异步模式 + 信号校正) | 在10 s仿真区间内，风电场平均有功功率与34.5 kV母线A相电压波形平滑，信号校正有效抑制了步长不匹配引起的数值振荡与接口延迟。 | 与单核基准解（Original Case）波形高度重合，精度与场景5（同步模式）相当，未因异步并行引入额外误差。 |

| 场景5 (顺序多步长同步模式 + 信号校正) | 采用同步协调机制配合信号校正，电压与功率动态响应曲线准确捕捉了t=5 s故障期间的暂态过程。 | 作为精度参照基准，其计算耗时显著高于异步模式，但波形精度与场景3一致，验证了异步扩展的可靠性。 |

| 多核加速比测试 (场景1-5) | 在24核平台上随从机（风机）数量增加，所有协同场景均呈现计算时间下降趋势。 | 场景2与3（异步模式）获得最高加速比，突破原同步模式（场景1/4/5）的性能瓶颈，验证了多步长异步配置在多核架构上的最优可扩展性。 |



## 量化发现

- 电气网络固定采用 5 μs 积分步长，支持解耦子系统独立配置不同时间步长，实现真正的多步长异步并行。
- 含 2235 个控制模块的详细风机模型在FMI从机中运行，线性外推校正使主从接口数据交互误差大幅降低，波形精度与单核基准解一致。
- 在 24 核 Intel Xeon 平台上，并行多步长异步模式（场景2/3）相比原同步模式获得最高计算加速比，证实了方法在大规模多核集群上的强可扩展性。
- 三相故障（t=5 s，持续 0.15 s）工况下，校正后电压与功率暂态波形无发散或畸变，10 s 长时仿真保持数值稳定。


## 关键公式

### 历史状态存储方程

$$$\mathbf{y}_{extrapol} = [\mathbf{y}_{slave, T-\Delta t_{slave}}, \mathbf{y}_{slave, T-2\Delta t_{slave}}]$$$

*用于初始化或重置外推向量，缓存从机前两个计算步的浮点输出，为线性外推提供数据基础。*

### 滑动窗口移位方程

$$$\mathbf{y}_{extrapol}[n+1:2n] = \mathbf{y}_{extrapol}[1:n]$$$

*在从机完成新步长计算后执行，将旧数据向后平移，维持 $2n$ 维向量的时序连续性。*

### 最新状态更新方程

$$$\mathbf{y}_{extrapol}[1:n] = \mathbf{y}_{slave}$$$

*配合移位操作，将当前最新从机输出写入向量前端，完成校正数据池的刷新。*



## 验证详情

- **验证方式**: 纯数字仿真对比分析（与单核无协同基准解进行时域波形对比与加速比统计）
- **测试系统**: 3条风电场馈线连接集电网络与戴维南等值系统（含详细风机模型与复杂控制系统）
- **仿真工具**: 基于FMI 2.0标准的自定义EMT协同仿真平台（主从架构，支持信号量同步与线性外推校正）
- **验证结果**: 新方法在保持与单核基准解同等精度的前提下，通过异步多步长调度与线性外推信号校正机制，显著提升了含复杂控制系统的大规模EMT仿真效率，验证了其在多核平台上的高加速比与数值稳定性。

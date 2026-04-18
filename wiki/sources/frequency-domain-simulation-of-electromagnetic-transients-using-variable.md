---
title: "Frequency-Domain Simulation of Electromagnetic Transients Using Variable"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRD.2015.2449754.pdf.pdf"]
---

# Frequency-Domain Simulation of Electromagnetic Transients Using Variable

**作者**: 
**年份**: 2015
**来源**: `19、20、21/EMT_task_20/TPWRD.2015.2449754.pdf.pdf`

## 摘要

—This letter presents the extension of a previously proposed frequency-domain (FD) approach for the analysis of electromagnetic transients (EMTs), primarily due to a set of discrete switching events, in an electric power network. The method is based on dividing the analysis time window into a set of subwindows with equal or unequal time lengths and solving each in the FD. The sampling time step is also independently selected for each subwindow. The extended method, formerly proposed for a single transmission line, can readily use the concept of network equivalents, achieving efﬁcient EMT solutions of large systems, and can simultaneously accommodate slow and fast dynamics. Index Terms—Frequency-domain analysis, transient analysis. I. INTRODUCTION E LECTROMAGNETIC transients (EMTs) analysis

## 核心贡献


- 提出基于可变采样步长的频域仿真方法将时间窗划分为独立步长的子窗口
- 将频域方法从单条线路扩展至含频率相关网络等值的大规模电力系统
- 利用频域代数关系直接计算网络等值初始条件避免时域卷积与矩阵重三角化


## 使用的方法


- [[频域分析法|频域分析法]]
- [[可变时间步长|可变时间步长]]
- [[网络等值技术|网络等值技术]]
- [[节点导纳矩阵求解|节点导纳矩阵求解]]
- [[有理函数拟合|有理函数拟合]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[输电线路|输电线路]]
- [[集中参数电路|集中参数电路]]
- [[开关设备|开关设备]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频域仿真|频域仿真]]
- [[网络等值|网络等值]]
- [[变步长仿真|变步长仿真]]
- [[开关暂态分析|开关暂态分析]]
- [[频率相关建模|频率相关建模]]


## 主要发现


- 该方法在保持与PSCAD同等精度的前提下显著降低了整体计算耗时
- 各子窗口独立设置采样步长可同时高效捕捉快速与慢速电磁暂态过程
- 频域代数求解有效避免了时域卷积大幅提升了含频率相关等值网络的仿真效率



## 方法细节

### 方法概述

该方法将电磁暂态分析时间窗划分为多个长度可相等或不等的子时间窗，每个子窗独立设置采样步长。系统被虚拟划分为“研究区域”和“外部子系统”，外部子系统通过有理函数拟合降阶为频域网络等值（FDNE）。利用频域代数关系直接求解各子窗的节点电压与初始条件，彻底避免了传统时域方法中的卷积运算与导纳矩阵重复三角分解。通过灵活匹配开关事件时刻划分子窗，实现快慢动态过程的高效同步仿真。该方法将集中参数电路的初始条件概念推广至频变网络，使大规模电力系统在保持高精度的同时大幅降低计算负担，特别适用于含离散开关动作与多时间尺度动态的复杂暂态分析。

### 数学公式


**公式1**: $$$$ \mathbf{Y} \mathbf{V} = \mathbf{I}_{\text{calc}} + \mathbf{I}_{\text{known}} $$$$

*频域节点电压求解核心方程。其中$\mathbf{Y}$为包含研究系统参数的节点导纳矩阵，$\mathbf{V}$为接口节点电压向量，$\mathbf{I}_{\text{calc}}$为上一子窗传递的频变等效电流源，$\mathbf{I}_{\text{known}}$为研究区内已知的独立电流源。该方程用于在每个子时间窗内直接代数求解网络状态，替代时域步进积分。*


### 算法步骤

1. 步骤1（零初始条件频域求解）：在首个子时间窗内，假设$t=0$时刻系统初始条件为零，在频域内求解整个网络（含外部子系统与研究区），获取所有节点电压，特别是研究区与外部子系统之间的接口节点电压向量。

2. 步骤2（频域初始条件代数计算）：基于步骤1得到的接口节点电压，利用外部子系统的FDNE模型，在频域内通过代数运算直接求解状态变量（避免对ODE进行数值积分），生成下一子窗所需的频变电流源作为初始条件。

3. 步骤3（拓扑更新与当前子窗求解）：将步骤2计算的频变电流源注入接口节点。若研究区内发生开关动作等拓扑变化，在此步骤更新网络模型。随后利用核心方程$\mathbf{Y} \mathbf{V} = \mathbf{I}_{\text{calc}} + \mathbf{I}_{\text{known}}$在频域求解当前子窗的节点电压。

4. 步骤4（迭代推进）：重复步骤2和3，依次推进至后续所有子时间窗，直至完成整个分析时间窗的暂态仿真。若开关时刻落在子窗内部，可通过迭代或重新分配子窗边界处理。


### 关键参数

- **子时间窗划分策略**: 根据开关事件或动态特性变化点灵活设定起止时刻，无需等长

- **采样步长设置**: 各子窗独立选择（如快动态阶段采用15μs，慢动态阶段采用更大步长）

- **FDNE拟合阶数**: 随驱动点导纳矩阵中频率谐振点数量增加而提高，影响模型复杂度

- **开关导通电导**: 100 mho（断开状态设为0）

- **初始暂态采样点数**: 首个子窗采用1024个采样点以高精度捕捉初始冲击



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含两次开关动作的输电线路基准系统（文献[4]） | 在$t=0$闭合开关$S_1$，$t=0.05$ s闭合开关$S_2$。节点2电压暂态波形完整记录了初始合闸暂态与二次开关暂态。所提方法采用变步长策略，首个子窗使用1024个采样点，整体仿真精度与PSCAD/EMTDC采用固定15μs步长（共7334个采样点）的结果高度一致。 | MATLAB实现版CPU耗时0.49 s，PSCAD/EMTDC耗时0.64 s（未含线路拟合时间）；编译为MEX文件后耗时降至0.20 s，较MATLAB脚本提速2.4倍。 |



## 量化发现

- 在保持与PSCAD/EMTDC同等精度的前提下，MATLAB版仿真耗时为0.49 s，较PSCAD的0.64 s减少约23.4%。
- 若计入PSCAD的传输线有理函数拟合时间（8.1 s），所提频域方法整体计算效率提升超过一个数量级。
- MEX编译版执行时间仅0.20 s，较原生MATLAB代码提速2.4倍，验证了算法在高效编程环境下的巨大潜力。
- 首个子窗仅需1024个采样点即可高精度捕捉初始暂态过程，避免了全局采用极小步长导致的计算冗余。


## 关键公式

### 频域节点电压代数求解方程

$$$$ \mathbf{Y} \mathbf{V} = \mathbf{I}_{\text{calc}} + \mathbf{I}_{\text{known}} $$$$

*在每个子时间窗内，当接口电流源已知且网络拓扑（含开关状态）确定后，用于直接求解接口节点电压，替代时域步进积分。*



## 验证详情

- **验证方式**: 对比仿真分析
- **测试系统**: 文献[4]中的双开关输电线路基准测试系统（含外部子系统与研究区划分）
- **仿真工具**: MATLAB（所提频域算法）、PSCAD/EMTDC（时域基准对比）
- **验证结果**: 节点电压暂态波形与PSCAD结果高度一致，验证了变步长频域方法在捕捉快速开关暂态与慢速动态方面的准确性；计算效率显著优于传统时域方法，尤其在考虑模型拟合开销时优势更为突出。

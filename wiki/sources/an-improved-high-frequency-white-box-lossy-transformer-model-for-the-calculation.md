---
title: "An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients"
type: source
authors: ['N. Hooda']
year: 2017
journal: "Procedia Engineering, 186 (2017) 349-356. doi:10.1016/j.proeng.2017.03.211"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients.pdf"]
---

# An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients

**作者**: N. Hooda
**年份**: 2017
**来源**: `07&08/An improved high frequency white-box lossy transformer model for the calculation of power systems electromagnetic transients.pdf`

## 摘要

Rural water networks in the developing world are typically branched networks with a single water source. The main design decision to be made for such networks is the choice of pipe diameters from a discrete set of commercially available pipe diameters. Larger the pipe diameters, better the service (pressure), but higher is the capital cost. In general, each link (connection between two nodes) in the network can consist of several pipe segments of differing diameters. For such networks, existing design tools solve the constrained-optimization problem heuristically [1] [2]. In [3], an ILP formulation is proposed for the special case of one pipe diameter per link. This means that currently one can either get an optimal solution for the special case of one piped segment per link or get a non-o

## 核心贡献


- 提出多管段管径线性规划模型，保持全局最优并显著提升求解效率
- 开发集成GIS的JalTantra系统，实现树状供水管网自动化优化设计


## 使用的方法


- [[线性规划-lp|线性规划(LP)]]
- [[整数线性规划-ilp|整数线性规划(ILP)]]
- [[hazen-williams水头损失公式|Hazen-Williams水头损失公式]]
- [[约束优化算法|约束优化算法]]


## 涉及的模型


- [[树状供水管网模型|树状供水管网模型]]
- [[单水源无环网络|单水源无环网络]]
- [[多管段组合模型|多管段组合模型]]
- [[jaltantra优化系统|JalTantra优化系统]]


## 相关主题


- [[供水管网优化设计|供水管网优化设计]]
- [[管径离散选择|管径离散选择]]
- [[压力约束优化|压力约束优化]]
- [[线性规划应用|线性规划应用]]
- [[gis集成设计|GIS集成设计]]


## 主要发现


- 不预设管段限制的LP模型运行更快，且自然收敛至最多两种相邻管径最优解
- 新模型在求解精度与计算耗时上均优于传统启发式算法及单管径整数规划方法



## 方法细节

### 方法概述

本文针对单水源树状重力流供水管网的管径优化设计问题，提出了一种基于线性规划（LP）的全局最优求解框架。传统设计工具多采用启发式算法或整数线性规划（ILP），前者无法保证全局最优，后者在允许单管段组合多种管径时会因引入大量布尔变量和线性化约束导致计算复杂度呈指数级增长。本文突破性地摒弃了显式建模“每段管道最多使用两种相邻管径”的离散选择逻辑，转而将每条管道视为由所有可用商用管径分段组成的连续体，引入连续变量表示各管径的铺设长度。基于管径成本函数的凸性数学特性，该LP模型在满足节点最小压力与流量守恒约束时，求解器会自动收敛至仅含最多两种相邻非零管径长度的最优解。该方法成功将NP-hard的ILP问题转化为多项式时间可解的LP问题，在保证全局最优性的同时实现了计算效率的跨越式提升。

### 数学公式


**公式1**: $$$O(\cdot) = \sum_{i=1}^{N_L} \sum_{j=1}^{N_P} C_{ij}(D_{ij}) l_{ij}$$$

*目标函数：最小化全网管道总建设成本，其中$C_{ij}$为单位长度成本，$l_{ij}$为管段长度连续变量。*


**公式2**: $$$\sum_{j=1}^{N_P} l_{ij} = L_i$$$

*管道长度约束：确保每条链路中各管径分段长度之和等于该链路总设计长度$L_i$。*


**公式3**: $$$P_n \le H_R - E_n - \sum_{i \in S_n} \sum_{j=1}^{N_P} HL'_{ij} l_{ij}$$$

*节点压力约束：保证任意节点$n$的剩余水头不低于最小压力要求$P_n$，考虑了从水源到该节点路径上的累计水头损失。*


**公式4**: $$$HL'_{ij} = \frac{10.68 \cdot Q_i^{1.852}}{C_{HW,j} \cdot D_j^{4.87}}$$$

*Hazen-Williams单位长度水头损失公式：用于计算特定管径和流量下的摩擦水头损失系数，其中$Q_i$为链路流量，$C_{HW,j}$为粗糙系数，$D_j$为管径。*


### 算法步骤

1. 网络拓扑与参数初始化：输入单水源树状管网结构（节点高程、需水量、最小压力阈值、链路长度）及商用管材库（离散管径集合、对应单位成本、Hazen-Williams粗糙系数）。

2. 确定性流量分配：基于树状网络无环特性，从末端需水节点向水源逆向递推，直接计算每条链路的稳态设计流量$Q_i$，无需迭代水力平衡。

3. LP变量定义：为每条链路$i$的每种可用管径$j$创建连续决策变量$l_{ij}$，表示该管径在该链路中的实际铺设长度。

4. 构建目标函数：建立全网总成本最小化模型$O = \sum \sum C_{ij} l_{ij}$，将离散管径选择转化为连续长度优化。

5. 施加物理与工程约束：添加链路总长度守恒约束$\sum_j l_{ij} = L_i$；基于Hazen-Williams公式计算单位水损$HL'_{ij}$，构建节点最小压力约束不等式组。

6. 调用LP求解器：将构建的线性规划模型输入GLPK求解器，利用单纯形法或内点法进行多项式时间迭代求解。

7. 解后处理与结构提取：解析求解器输出的$l_{ij}$值，自动过滤长度为零的管径组合。依据凸性理论，每条链路仅保留长度大于零的至多两种相邻管径及其对应长度。

8. 输出优化方案：生成各链路的管径分段配置清单及对应造价，完成自动化设计。


### 关键参数

- **N_L**: 网络链路总数

- **N_P**: 可用商用管径种类数（实验取10）

- **L_i**: 第i条链路的总长度

- **C_{ij}**: 第j种管径的单位长度造价

- **P_n**: 节点n要求的最小服务压力

- **H_R**: 参考水源节点的供水水头

- **E_n**: 节点n的地面高程

- **Q_i**: 链路i的设计流量（由节点需水量确定）

- **C_{HW,j}**: 第j种管材的Hazen-Williams粗糙系数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Mokhada真实管网(37节点) | 优化总成本为24,181千卢比，求解耗时387毫秒。 | 较BRANCH启发式算法成本降低1.9%，速度提升308倍；较OnePipe ILP模型成本降低0.56%，速度略快。 |

| Gen_1000合成管网(1000节点) | 优化总成本为562,564千卢比，求解耗时2023毫秒。 | OnePipe ILP模型在100秒后超时未收敛，BRANCH因内存溢出崩溃；本模型在2秒内获得全局最优解。 |

| Shahpur真实管网(21节点) | 优化总成本为28,895千卢比，求解耗时318毫秒。 | 较BRANCH成本降低0.64%，速度提升109倍；较OnePipe成本降低2.13%。 |



## 量化发现

- 1000节点大规模管网求解时间仅2.023秒，而传统ILP模型在100秒超时限制下无法收敛，计算效率提升超50倍。
- LP模型约束数量与节点数呈线性关系（100节点仅200个约束），而显式双管径ILP模型约束数随管径种类呈指数爆炸（10节点即达860个约束）。
- 在全部6个测试网络中，本模型均实现全局最优造价，较启发式BRANCH工具平均降低成本约1.5%~2.5%。
- 求解结果严格遵循理论预期：每条链路自动收敛至最多两种相邻商用管径的组合，无需人工干预或额外整数约束。


## 关键公式

### 节点压力约束核心方程

$$$P_n \le H_R - E_n - \sum_{i \in S_n} \sum_{j=1}^{N_P} \left( \frac{10.68 \cdot Q_i^{1.852}}{C_{HW,j} \cdot D_j^{4.87}} \right) l_{ij}$$$

*用于在LP优化过程中确保管网末端及中间节点的水压满足最低服务标准，是连接水力计算与成本优化的关键桥梁。*

### 线性化管网造价目标函数

$$$O(\cdot) = \sum_{i=1}^{N_L} \sum_{j=1}^{N_P} C_{ij}(D_{ij}) l_{ij}$$$

*将离散管径选择转化为连续长度变量乘积，消除ILP中的非线性项与布尔变量，使问题可在多项式时间内求解。*



## 验证详情

- **验证方式**: 计算仿真与对比分析（基于真实工程数据与合成网络基准测试）
- **测试系统**: 6个单水源树状供水管网（3个印度马哈拉施特拉邦真实村庄管网：11~37节点；3个合成测试网络：5~1000节点）
- **仿真工具**: JalTantra优化系统（Java 7开发）、GLPK 4.55线性规划求解器、Java ILP 1.2a接口、Google Maps API（GIS集成）
- **验证结果**: 验证表明，所提LP模型在全部测试用例中均严格满足节点最小压力约束，且造价全局最优。相较于启发式BRANCH和ILP单管径模型，本方法在求解速度上实现数量级提升（毫秒级vs秒/百秒级），在1000节点规模下仍保持2秒内收敛，彻底克服了传统方法在大规模离散优化中的组合爆炸与次优缺陷。

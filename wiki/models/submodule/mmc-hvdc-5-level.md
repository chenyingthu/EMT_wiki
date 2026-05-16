---
title: "5电平MMC-HVDC系统 (5-Level MMC-HVDC)"
type: model
tags: [mmc, hvdc, 5-level, multi-level, modular-multilevel-converter]
created: "2026-05-04"
updated: "2026-05-16"
---

# 5电平MMC-HVDC系统 (5-Level MMC-HVDC)

## 概述

5电平MMC-HVDC系统是模块化多电平换流器在高压直流输电中的一种基础配置，每桥臂含4个子模块（N=4），通过级联半桥或全桥子模块在交流侧输出5电平阶梯波。作为MMC的入门级电平配置，5电平MMC常用于教学验证、小功率MMC-HVDC实验平台和算法初步验证。虽然工程级MMC通常采用数十至数百电平，5电平配置涵盖了MMC的核心工作原理，包括子模块电容均压、桥臂环流、NLM调制及直流故障特性等基本问题。

## 拓扑结构

5电平MMC的基本参数关系：
- 每桥臂子模块数：$N = 4$
- 交流侧输出电平数：$N_{level} = N + 1 = 5$
- 子模块电容电压额定值：$V_C = V_{dc} / N = V_{dc} / 4$
- 桥臂子模块总电压：$V_{arm} = \sum_{i=1}^{4} S_i \cdot V_{C,i}$

调制比与输出电压关系：

$$v_{ac} = M \cdot \frac{V_{dc}}{2} \cdot \sin(\omega t)$$

其中 $M \in [0, 1]$ 为调制比。

## EMT中的角色

5电平MMC-HVDC系统在EMT仿真中主要用于：

- **建模对象**：描述5电平MMC-HVDC系统在电力系统中的物理角色和电气特性
- **仿真场景**：适用于5电平MMC-HVDC系统相关的电磁暂态分析、故障响应、控制交互等场景
- **模型接口**：提供5电平MMC-HVDC系统的端口变量、状态方程和边界条件
- **验证基准**：可作为5电平MMC-HVDC系统仿真模型正确性的验证基准

## 数学模型

### 桥臂电压方程

MMC每相上下桥臂电压由各子模块输出电压叠加：

$$v_{p,j} = \sum_{i=1}^{N} S_{p,i,j} \cdot v_{C,p,i,j}, \quad v_{n,j} = \sum_{i=1}^{N} S_{n,i,j} \sum_{i=1}^{N} S_{n,i,j} \cdot v_{C,n,i,j}$$

其中 $S \in \{0,1\}$ 为子模块开关状态，$v_C$ 为电容电压，下标 $p$/$n$ 表示上下桥臂，$j \in \{a,b,c\}$ 表示三相。

### 电容电压动态

子模块电容电压变化由注入电流决定：

$$\frac{dv_{C}}{dt} = \frac{i_{sm}}{C_{sm}} = \frac{S_i \cdot i_{arm}}{C_{sm}}$$

对5电平系统，四个子模块电容电压标幺值可表示为：

$$\hat{V}_{C,i} = 1 + \Delta v_i, \quad i = 1,2,3,4$$

其中 $\Delta v_i$ 为纹波分量，均压算法使 $|\Delta v_i| < 0.1$（即 $<10\%$ 纹波）。

### 环流抑制控制

桥臂环流 $i_{cirj}$ 主要为二次谐波分量：

$$i_{cir,j} = \frac{i_{p,j} - i_{n,j}}{2}$$

通过在dq坐标系下注入负序二次谐波分量进行抑制：

$$v_{cir,d} = -2\omega L_{arm} i_{cir,q}, \quad v_{cir,q} = 2\omega L_{arm} i_{cir,d}$$

### 最近电平调制（NLM）

5电平调制波与阶梯波的差值：

$$v^*_{ac,j} = M \cdot \frac{V_{dc}}{2} \cdot \sin(\omega t + \theta_j)$$

最近电平选择规则：

$$N_{on,j} = \text{round}\left(\frac{v^*_{ac,j}}{V_{dc}/4}\right)$$

输出电平数 $N_{level} = N_{on} + 1 = 5$。

### 戴维南等效模型

将子模块群等效为电压源与阻抗的串联：

$$v_{th} = \sum_{i=1}^{N} S_i \cdot \bar{v}_{C,i}, \quad Z_{th} = \frac{N}{j\omega C_{eq}}$$

当 $N=4$ 时，等效精度与 $N$ 成正比。戴维南等效将计算复杂度从 $O(N^2)$ 降至 $O(N)$，实现15~20倍加速（Xu 2015）。

### 状态空间表示

5电平MMC完整状态空间方程：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

其中状态向量 $\mathbf{x} = [v_{C,1}, v_{C,2}, v_{C,3}, v_{C,4}, i_{cir,a}, i_{cir,b}, i_{cir,c}]^T$，输入向量 $\mathbf{u} = [v_{ac,a}, v_{ac,b}, v_{ac,c}, V_{dc}]^T$。

## 5电平与高电平MMC的主要区别

| 特性 | 5电平(N=4) | 高电平(N=100~400) |
|------|-----------|------------------|
| **阶梯波质量** | 粗糙，谐波含量高 | 平滑，近正弦波 |
| **等效开关频率** | 低 | 高（N倍） |
| **输出滤波器需求** | 需要LC滤波器 | 可省略或简化 |
| **电容电压纹波** | 较大（~10-15%） | 较小（<5%） |
| **环流幅值** | 比例较大 | 比例较小 |
| **控制复杂度** | 低 | 高（需均压算法） |
| **应用场景** | 教学、小功率实验 | 工程级HVDC输电 |

## 量化性能边界

**MMC AVM在低电平系统中的精度**（Xu 2014, 11电平四端MMC-MTDC）：
- 子模块电容 $C_{sm} \geq 20$ mF（电压纹波<2%）时AVM误差<2.5%
- 启动充电工况直流电压误差1%，交流充电电流误差<1%
- 极间直流故障下，改进AVM直流电压最大误差2.5%，交流电压误差2%
- 验证平台：PSCAD/EMTDC

**MMC戴维南等效模型加速比**（Xu 2015, 48电平系统）：
- 戴维南等效模型仿真速度比详细模型快15~20倍（$N=200$时）
- 排序算法复杂度从 $O(N^2)$ 降至 $O(N)$，仿真耗时与子模块数线性正比
- 对于5电平（N=4）的低电平系统，加速比不如高电平显著，但仍可通过各子模块独立建模获益

**MMC自适应模型精度**（Stepanov 2020, 401电平系统）：
- AVM/AEM/DEM三档自适应切换，模型切换过程外部电气特性误差<0.5%
- 稳态时切换至AVM/AEM可降低单步计算耗时65%~75%，整体加速比>3.5x
- 阻塞模式求解器迭代上限30次，实际收敛<6次

**MMC打靶法初始化**（del Giudice 2024, 128电平）：
- 两阶段AVM到Thévenin映射的打靶法初始化，直接从接近稳态启动
- 消除传统初始化所需的长时间仿真过渡，减少仿真启动等待时间

**数据缺口声明**：5电平MMC作为入门级配置，其相关模型数据大多来自高电平（48~400电平）系统外推，缺乏专门针对5电平（N=4）的定量加速比和精度基准测试。

## 关键技术挑战

- **电容电压纹波控制**：低电平配置下纹波比例更高，需更精确的均压算法
- **开关动作谐波**：5电平阶梯波谐波含量高，输出滤波器设计复杂
- **环流抑制带宽**：低电平系统环流幅值比例大，需要更高带宽的抑制策略
- **初始化瞬态**：5电平系统启动时电容充电过程更长

## 适用边界

5电平MMC适用于：
- 教学演示和算法验证
- 小功率实验平台（<1 MW）
- 控制策略初步验证

不适用于：
- 工程级HVDC输电（需>100电平）
- 高频开关暂态分析
- 精确谐波评估（需>21电平）

## 相关模型

- [[mmc-model]] - MMC通用模型
- [[half-bridge-smb]] - 半桥子模块
- [[full-bridge-smb]] - 全桥子模块
- [[vsc-hvdc]] - VSC-HVDC系统

## 相关方法

- [[average-value-model]] - 平均值模型
- [[nearest-level-modulation]] - 最近电平调制

## 相关主题

- [[real-time-simulation]] - 实时仿真
- [[co-simulation]] - 混合仿真

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Xu等 - Average-Value Models for Modular Multilevel Converters]] | 2014 | 提出11电平四端MMC-MTDC的AVM精度基准 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|Xu等 - A review of efficient modeling methods for MMC]] | 2015 | 综述MMC高效建模方法，给出15~20×加速数据 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Stepanov等 - Adaptive MMC Model]] | 2020 | 提出AVM/AEM/DEM三档自适应切换，<0.5%误差 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|del Giudice等 - Shooting method based MMC initialization]] | 2024 | 提出打靶法初始化，消除启动过渡过程 |

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
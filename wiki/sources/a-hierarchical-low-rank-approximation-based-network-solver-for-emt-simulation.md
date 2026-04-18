---
title: "A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2978128"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Zhang 等 - 2021 - A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation.pdf"]
---

# A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation

**作者**: 
**年份**: 2020
**来源**: `01/Zhang 等 - 2021 - A Hierarchical Low-Rank Approximation Based Network Solver for EMT Simulation.pdf`

## 摘要

—In electromagnetic transient (EMT) simulation, 80- 97% of the computational time is devoted to solving the network equations. A key observation is that the sub-matrix representing the interaction between two far-away groups of buses is usually sparse and can be approximated by a low-rank matrix. Based on this observation, we propose a novel low-rank approximation method which permits O(N log N)-time matrix-vector multi- plication for each network solution time step. Comprehensive numerical studies are conducted on a 39-bus system and a 179- bus system from the literature, and large cases created from the two systems. The results demonstrate that the proposed approach is up to 2.8× faster than the state-of-the-art sparse LU factorization based network solution, without compromising simulat

## 核心贡献


- 提出分层低秩近似算法求解网络方程，将单步计算复杂度降至O(N log N)。
- 建立算法的时间复杂度、内存占用与近似误差理论分析框架。
- 验证算法在保持精度的前提下，较稀疏LU分解求解器提速最高达2.8倍。


## 使用的方法


- [[分层低秩近似|分层低秩近似]]
- [[奇异值分解-svd|奇异值分解(SVD)]]
- [[快速矩阵向量乘法|快速矩阵向量乘法]]
- [[图划分网络分区|图划分网络分区]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[输电线路-π型等效|输电线路(π型等效)]]
- [[变压器-饱和模型|变压器(饱和模型)]]
- [[发电机-brandwajn模型|发电机(Brandwajn模型)]]
- [[负荷-恒定阻抗模型|负荷(恒定阻抗模型)]]
- [[网络导纳矩阵|网络导纳矩阵]]


## 相关主题


- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[网络方程求解|网络方程求解]]
- [[并行计算|并行计算]]
- [[大规模电力系统仿真|大规模电力系统仿真]]
- [[矩阵运算优化|矩阵运算优化]]


## 主要发现


- 在39节点与179节点系统中验证，求解速度较稀疏LU分解最高提升2.8倍。
- 仿真电压波形与商业软件EMTP-RV结果高度一致，未牺牲计算精度。
- 算法具备高度并行化特性，为后续多核或GPU硬件加速提供显著优化空间。



## 方法细节

### 方法概述

本文提出一种基于分层低秩近似的网络方程快速求解器，旨在突破传统EMT仿真中网络求解的计算瓶颈。传统方法依赖稀疏LU分解与前代回代，计算复杂度高且难以并行。该方法首先将节点电压方程重构为矩阵向量乘法形式$v(t)=G^{-1}i(t)$。随后，利用电力网络导纳矩阵的拓扑特性，设计自底向上的图划分算法，将母线按电气距离聚类并构建平衡二叉树。针对树中表征远距离或弱耦合母线组交互的非对角子矩阵，采用截断奇异值分解(SVD)进行低秩近似，仅保留主导奇异值及对应左右奇异向量，使近似误差严格低于预设阈值。在仿真每个时间步，通过遍历该层次数据结构执行快速矩阵向量乘法，将单步求解复杂度从$O(N^2)$降至$O(N \log N)$，在维持数值精度的同时显著提升计算效率并具备高度并行化潜力。

### 数学公式


**公式1**: $$$Gv(t) = i_{in}(t) + i_{his}(t - \Delta t)$$$

*EMT网络节点方程，G为导纳矩阵，v为节点电压向量，i_in为注入电流，i_his为历史电流*


**公式2**: $$$v(t) = G^{-1} i(t)$$$

*将网络方程重构为矩阵向量乘法形式，i(t)为总注入电流向量，作为快速求解的核心目标*


**公式3**: $$$A \approx A_r = \sum_{i=1}^r \sigma_i u_i v_i^*$$$

*截断SVD低秩近似公式，用前r个奇异值及向量近似原交互子矩阵A*


**公式4**: $$$\varepsilon = \|A - A_r\|_F = \sqrt{\sigma_{r+1}^2 + \dots + \sigma_p^2}$$$

*基于Eckart-Young-Mirsky定理的截断误差计算公式，用于控制近似精度*


**公式5**: $$$W(S_1, S_2) = \frac{\sum_{v_1 \in S_1, v_2 \in S_2} G_{v_i, v_j}}{\max\{|S_1|, |S_2|\}}$$$

*图划分权重函数，衡量两组母线间的平均电导，用于指导平衡合并*


### 算法步骤

1. 步骤1（网络图构建与自底向上划分）：基于全系统导纳矩阵G构建无向图H=(V,E)。初始化所有母线为独立节点，按层级执行平衡合并：优先合并度为1的节点与其唯一邻居；随后在剩余节点中迭代选取权重函数W(S1,S2)最大的节点对进行合并，确保每层每个节点仅合并一次。重复该过程直至所有节点合并为单一根节点，生成高度为O(log N)的平衡二叉树层次结构。

2. 步骤2（逆矩阵计算与分层低秩近似）：预处理阶段计算全网络导纳逆矩阵G^{-1}。从二叉树根节点开始递归遍历：若当前子矩阵维度或数值秩小于预设阈值r_th，则直接存储为显式矩阵；否则计算其完整SVD，根据预设误差阈值ε_th截断保留前r个奇异值及对应U、Σ、V矩阵。若秩仍大于r_th，则将子矩阵按行列索引划分为四个子块，对每个子块递归执行相同近似流程，直至所有交互子矩阵均被显式存储或低秩分解表示。

3. 步骤3（快速矩阵向量乘法求解）：在每个仿真时间步，先计算历史电流i_his(t-Δt)与注入电流i_in(t)之和得到i(t)。自顶向下遍历层次树执行矩阵向量乘法：若子矩阵为显式形式，直接计算v=G^{-1}i；若为低秩形式(U,Σ,V)，先计算中间向量x=Σ(Vi)，再计算v=Ux；若为子块组合形式，则递归调用子节点计算并合并结果。最终输出全系统节点电压向量v(t)，完成单步网络求解。


### 关键参数

- **r_th**: 预设秩阈值，控制低秩近似的最大保留秩数

- **ε_th**: 预设截断误差阈值，基于Frobenius范数控制SVD截断精度

- **N**: 电力系统母线总数

- **Δt**: EMT仿真时间步长



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统 | 在标准39节点测试系统中进行EMT暂态仿真，记录网络求解耗时与电压波形，验证算法在中小规模系统中的有效性 | 相比传统稀疏LU分解求解器，计算速度提升显著，最高达2.8倍 |

| 179节点系统及扩展大规模算例 | 在179节点系统及基于其扩展的大规模网络中验证算法可扩展性，单步求解时间随规模增长严格遵循O(N log N)趋势，内存占用可控 | 在大规模场景下保持最高2.8倍的加速比，且仿真电压波形与商业软件EMTP-RV结果高度一致，未牺牲计算精度 |



## 量化发现

- 网络方程求解时间占传统EMT仿真总耗时的80%-97%，本方法将其单步计算复杂度从O(N^2)降至O(N log N)
- 在39节点与179节点系统及扩展算例中，求解速度较最先进的稀疏LU分解求解器最高提升2.8倍
- 低秩近似截断误差严格受控于预设阈值ε_th，仿真电压波形与商业软件EMTP-RV结果高度一致，未牺牲计算精度
- 层次划分树高度为O(log N)，保证了快速矩阵向量乘法的递归深度与计算效率


## 关键公式

### 重构网络求解方程

$$$v(t) = G^{-1} i(t)$$$

*替代传统前代回代过程，将网络求解转化为矩阵向量乘法，是低秩近似加速的基础*

### 时间复杂度递推公式

$$$T(N) \leq \begin{cases} CN^2 & \text{if } N \leq r_{th} \\ CNr_{th} & \text{if rank}(G^{-1}) \leq r_{th} \\ 2T(N/2) + 2C(N/2)r_{th} + N & \text{otherwise} \end{cases}$$$

*用于严格证明快速矩阵向量乘法算法的整体时间复杂度为O(N log N)*



## 验证详情

- **验证方式**: 数值仿真对比验证
- **测试系统**: IEEE 39节点系统、179节点系统及基于两者构建的大规模扩展网络
- **仿真工具**: 自研分层低秩近似求解器、商业EMT软件EMTP-RV（作为精度基准）
- **验证结果**: 通过对比电压暂态波形，验证了所提方法在保持与EMTP-RV同等精度的前提下，网络求解速度最高提升2.8倍，理论误差界与时间复杂度分析均得到数值实验的充分验证。

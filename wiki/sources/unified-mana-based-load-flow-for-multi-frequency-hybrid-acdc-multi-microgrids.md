---
title: "Unified MANA-based load-flow for multi-frequency hybrid AC/DC multi-microgrids"
type: source
authors: ['Nasim Rashidirad']
year: 2023
journal: "Electric Power Systems Research, 220 (2023) 109313. doi:10.1016/j.epsr.2023.109313"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/39/Rashidirad 等 - 2023 - Unified MANA-based load-flow for multi-frequency hybrid ACDC multi-microgrids.pdf"]
---

# Unified MANA-based load-flow for multi-frequency hybrid AC/DC multi-microgrids

**作者**: Nasim Rashidirad
**年份**: 2023
**来源**: `39/Rashidirad 等 - 2023 - Unified MANA-based load-flow for multi-frequency hybrid ACDC multi-microgrids.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Unified MANA-based load-flow for multi-frequency hybrid AC/DC Nasim Rashidirad a,*, Jean Mahseredjian b, Ilhan Kocar c, U. Karaagac c b Polytechnique Montr´eal, Montr´eal, H3T 1J4, QC Canada In islanded hybrid AC/DC multi-microgrids (MMGs), interconnected AC microgrids (ACMGs) can operate with

## 核心贡献



- 提出基于改进增广节点分析（MANA）的统一潮流计算框架，适用于任意数量互联的多相微电网
- 解决了孤岛模式下各交流微电网频率独立及互联变流器耦合的多频潮流求解难题

## 使用的方法


- [[nodal-analysis]]

## 涉及的模型


- [[vsc-model]]
- [[network-equivalent]]

## 相关主题


- [[harmonic]]

## 主要发现



- MANA潮流框架可准确计算多频混合交直流多微电网的稳态运行点
- 该潮流解可为电磁暂态仿真提供高质量初始值，显著加快系统达到谐波稳态的速度

## 方法细节

### 方法概述

本文提出了一种基于改进增广节点分析（MANA）的统一潮流计算框架，用于求解多频孤岛混合AC/DC多微电网（MMGs）的稳态运行点。该方法将多微电网系统划分为三个子系统：交流微电网（ACMGs）、直流微电网（DCMGs）和互联变流器（ICs）。每个子系统具有独立的潮流变量和约束方程，包括节点约束和元件约束。通过构建统一的分块Jacobian矩阵，将各子系统的本地约束（J_ACMG、J_DCMG、J_IC）与子系统间的耦合约束（J_ACMG-IC、J_DCMG-IC、J_IC-ACMG、J_IC-DCMG）联立求解。该方法的关键创新在于将各孤岛ACMG的频率作为独立的潮流变量（多频特性），并通过IC的AC/DC双侧电流耦合实现多微电网的统一求解，适用于多相不平衡系统。

### 数学公式


**公式1**: $$$J_{MMG} \Delta X_{MMG} = - f_{MMG}$$$

*MANA-based MMG统一潮流方程，其中J_MMG为Jacobian矩阵，ΔX_MMG为所有潮流变量修正量，f_MMG为MANA函数向量（待最小化的失配函数）*


**公式2**: $$$$\begin{bmatrix} J_{ACMG} & 0 & J_{ACMG-IC} \\ 0 & J_{DCMG} & J_{DCMG-IC} \\ J_{IC-ACMG} & J_{IC-DCMG} & J_{IC} \end{bmatrix} \begin{bmatrix} \Delta X_{ACMG} \\ \Delta X_{DCMG} \\ \Delta X_{IC} \end{bmatrix} = - \begin{bmatrix} f_{ACMG} \\ f_{DCMG} \\ f_{IC} \end{bmatrix}$$$$

*扩展的分块矩阵形式，展示ACMG、DCMG和IC三个子系统间的耦合关系，其中非对角子矩阵表示子系统间的Jacobian耦合项*


**公式3**: $$$\Delta X_{ACMG_i} = [\Delta V_{ni}^T, \Delta I_{Li}^T, \Delta I_{Gi}^T, \Delta E_{Gi}^T, \Delta \omega_i]^T$$$

*第i个ACMG的变量向量，包含AC节点电压、负载电流、发电机电流、发电机内部电压和频率（关键的多频变量）*


**公式4**: $$$$J_{ACMG_i} = \begin{bmatrix} Y_{ni} & A_{ILi} & A_{IGi} & 0 & 0 \\ C_{Li} & D_{Li} & 0 & 0 & A_{L\omega i} \\ C_{Gi} & 0 & D_{Gi} & 0 & A_{G\omega i} \\ Y_{Gi} & 0 & B_{Gi} & Y_{GEi} & 0 \end{bmatrix}$$$$

*ACMG的Jacobian子矩阵，第一行表示AC节点约束（含节点导纳矩阵Y_ni），第二行表示频率相关的负载约束，第三行表示发电机下垂控制约束，第四行表示发电机内部电压约束*


**公式5**: $$$\Delta X_{DCMG_j} = [\Delta V_{nj}^T, \Delta I_{Lj}^T, \Delta I_{Gj}^T, \Delta E_{Gj}^T]^T$$$

*第j个DCMG的变量向量，包含DC节点电压、DC负载电流、DC变流器电流和内部电压（无频率变量）*


**公式6**: $$$$J_{IC_k} = \begin{bmatrix} D_{ICk} & 0 & D_{IC,dck} & 0 \\ B_{ICk} & Y_{ICk} & 0 & 0 \\ B_{IC,dck} & 0 & Y_{IC,dck} & 0 \end{bmatrix}$$$$

*第k个互联变流器（IC）的Jacobian子矩阵，包含AC侧和DC侧的电流-电压约束关系*


**公式7**: $$$$J_{IC_k-ACMG_i} = \begin{bmatrix} C_{ICk,i} & 0 & 0 & 0 & A_{IC\omega k,i} \\ Y_{ICk,i} & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$$$

*IC与ACMG间的耦合Jacobian子矩阵，第一行表示IC运行模式约束对ACMG节点电压和频率的偏导，体现多频耦合特性*


**公式8**: $$$$J_{IC_k-DCMG_j} = \begin{bmatrix} C_{IC,dck,j} & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ G_{IC,dck,j} & 0 & 0 & 0 \end{bmatrix}$$$$

*IC与DCMG间的耦合Jacobian子矩阵，表示IC约束对DCMG节点电压的偏导关系*


### 算法步骤

1. 系统分解：将多微电网系统划分为ACMGS、DCMGS和ICs三个子系统，识别各子系统的互联关系

2. 变量定义：为每个ACMG定义变量向量[ΔV_ni, ΔI_Li, ΔI_Gi, ΔE_Gi, Δω_i]，为每个DCMG定义[ΔV_nj, ΔI_Lj, ΔI_Gj, ΔE_Gj]，为每个IC定义[ΔI_ICk, ΔE_ICk, ΔI_IC,dck, ΔE_IC,dck]

3. 构建子系统Jacobian：分别构建J_ACMGi（含节点导纳、负载约束、发电机下垂控制）、J_DCMGj（含DC节点约束）和J_ICk（含AC/DC双侧约束）

4. 构建耦合Jacobian：根据IC的AC侧连接关系构建J_IC-ACMG（含频率耦合项A_ICω），根据DC侧连接构建J_IC-DCMG，以及J_ACMG-IC和J_DCMG-IC

5. 组装统一矩阵：按分块矩阵形式组装完整的J_MMG，确保ACMG、DCMG和IC的子矩阵位于对角，耦合矩阵位于非对角

6. 求解修正方程：求解线性方程组J_MMG ΔX_MMG = -f_MMG，得到所有子系统的电压、电流、内部电压和频率修正量

7. 迭代更新：更新各变量X = X + ΔX，检查收敛条件（如|ΔV| < ε和|Δω| < ε_ω），若未收敛则返回步骤3重新计算Jacobian并求解

8. EMT初始化：将收敛的稳态解作为电磁暂态仿真的初始条件，包括各DG和IC的内部状态变量


### 关键参数

- **ΔV_ni**: ACMG节点电压修正量（相量）

- **Δω_i**: 第i个ACMG频率修正量（关键的多频变量）

- **ΔI_ICk**: IC交流侧电流修正量

- **ΔI_IC,dck**: IC直流侧电流修正量

- **Y_ni**: ACMG节点导纳矩阵

- **A_Lωi**: 负载功率-频率耦合系数

- **A_Gωi**: 发电机下垂控制系数

- **C_ICk,i**: IC运行模式约束对ACMG电压的偏导

- **A_ICωk,i**: IC约束对ACMG频率的偏导（跨微电网频率耦合项）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 不平衡多微电网系统 | 测试系统包含两个孤岛ACMG（ACMG1和ACMG2）、一个DCMG、两个互联变流器（ICs）。ACMG1和ACMG2可独立运行在不同的频率（多频特性），通过IC实现功率交换。系统考虑了三相不平衡条件 | 相比传统单频潮流方法，本方法可处理多频孤岛工况；相比序贯求解方法，统一MANA框架减少了迭代次数，避免了多子系统间的反复协调循环 |



## 量化发现

- 各孤岛ACMG具有独立的频率变量Δω_i，系统表现为多频特性，频率差异通过IC的AC/DC/AC变换实现解耦
- IC数量增加会增强不同MG间潮流变量的耦合程度，但通过统一Jacobian矩阵可同时求解
- MANA框架可直接纳入基于电路的模型（如开关、变压器、电缆），无需额外简化
- 所求稳态解可直接用于EMT仿真的初始化，显著缩短达到谐波稳态的暂态过程时间
- 算法具有降低的迭代次数特性（reduced number of iterations），相比序贯方法计算效率更高


## 关键公式

### 统一MANA潮流方程

$$$$\begin{bmatrix} J_{ACMG} & 0 & J_{ACMG-IC} \\ 0 & J_{DCMG} & J_{DCMG-IC} \\ J_{IC-ACMG} & J_{IC-DCMG} & J_{IC} \end{bmatrix} \begin{bmatrix} \Delta X_{ACMG} \\ \Delta X_{DCMG} \\ \Delta X_{IC} \end{bmatrix} = - \begin{bmatrix} f_{ACMG} \\ f_{DCMG} \\ f_{IC} \end{bmatrix}$$$$

*用于同时求解多频AC/DC多微电网系统中所有子系统（ACMG、DCMG、IC）的稳态运行点，是本文的核心数学框架*

### ACMG多频变量定义

$$$\Delta X_{ACMG_i} = [\Delta V_{ni}^T, \Delta I_{Li}^T, \Delta I_{Gi}^T, \Delta E_{Gi}^T, \Delta \omega_i]^T$$$

*定义了每个孤岛ACMG的潮流变量，其中Δω_i是关键创新，将频率作为独立变量处理，实现多频系统的统一建模*



## 验证详情

- **验证方式**: 数值仿真验证
- **测试系统**: 包含两个ACMG、一个DCMG和两个IC的不平衡多微电网测试系统，ACMG可运行于不同频率
- **仿真工具**: 基于MANA的专用潮流计算程序（未明确提及具体商业软件，但参考文献涉及EMT仿真初始化）
- **验证结果**: 验证了所提MANA公式可有效处理多频孤岛多微电网的潮流计算，能够准确求得各ACMG的独立频率、节点电压和IC功率流，证实了统一求解框架在处理子系统间耦合变量的有效性，且所求解适用于EMT仿真的初始化

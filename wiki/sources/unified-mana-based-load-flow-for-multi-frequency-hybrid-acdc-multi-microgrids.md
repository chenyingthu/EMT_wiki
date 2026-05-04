---
title: "Unified MANA-based load-flow for multi-frequency hybrid AC/DC multi-microgrids"
type: source
authors: ['Nasim Rashidirad', 'Jean Mahseredjian', 'Ilhan Kocar', 'U. Karaagac']
year: 2023
journal: "Electric Power Systems Research"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/39/Rashidirad 等 - 2023 - Unified MANA-based load-flow for multi-frequency hybrid ACDC multi-microgrids.pdf"]
---

# Unified MANA-based load-flow for multi-frequency hybrid AC/DC multi-microgrids

**作者**: Nasim Rashidirad, Jean Mahseredjian, Ilhan Kocar, U. Karaagac
**年份**: 2023
**来源**: `39/Rashidirad 等 - 2023 - Unified MANA-based load-flow for multi-frequency hybrid ACDC multi-microgrids.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Unified MANA-based load-flow for multi-frequency hybrid AC/DC Nasim Rashidirad a,*, Jean Mahseredjian b, Ilhan Kocar c, U. Karaagac c b Polytechnique Montr´eal, Montr´eal, H3T 1J4, QC Canada In islanded hybrid AC/DC multi-microgrids (MMGs), interconnected AC microgrids (ACMGs) can operate with


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

这篇论文面对的是孤岛混合AC/DC多微电网的基频潮流初始化问题，直接服务于EMT仿真启动、运行点确定和变流器/控制约束设定。研究对象不是单个混合微电网，而是多个互联的AC微电网、DC微电网及其互联变流器组成的MMG；其中每个孤岛ACMG可以有自己的频率和下垂功率共享策略。难点在于：传统并网集群潮流默认公共频率，传统AC/DC混合微电网潮流通常只有一个孤岛AC子网，因此不能表达多个ACMG同时以不同频率运行；而序贯求解AC子网、DC子网和互联变流器会引入子系统间反复协调，在多子系统场景下实现复杂。本文贡献是把多频MMG写成统一的改进增广节点分析（MANA）潮流问题：每个ACMG、DCMG、互联变流器分别保留基于元件的节点约束和组件约束，再通过非对角Jacobian块表达IC与AC/DC侧的耦合。相对已有单频或序贯方法，创新点在于允许任意数量多相互联MG、将各孤岛ACMG频率作为潮流变量之一，并在一个统一Jacobian中同时求解电压、电流、内部电压、频率和IC接口量。

### 2. 模型、算法与实现技术

方法的核心是MANA式牛顿潮流：把系统未知量组织为ACMG变量、DCMG变量和IC变量，形成 J_MMG ΔX_MMG = -f_MMG。ACMG子系统包含节点电压、负载电流、发电机电流、发电机内部电压以及对应微电网频率等量；DCMG子系统包含DC节点电压、负载/发电或变流器电流、内部电压等量；IC子系统包含AC侧和DC侧接口电流、电压或内部等效量。对角Jacobian块描述各子系统本地的MANA约束，例如节点KCL、负载模型、DG/下垂控制、线路和等效导纳关系；非对角块描述互联变流器注入电流对所连接ACMG或DCMG节点变量的偏导，以及IC控制/功率约束对AC侧频率、AC/DC电压的偏导。计算流程是：识别ACMG、DCMG、IC及其连接关系；为每个子系统建立本地变量和残差；根据IC连接建立耦合Jacobian块；组装统一稀疏块矩阵；迭代求解修正量并更新所有子系统状态直到失配收敛。其机制意义在于，频率不再作为全网唯一常数，而是每个孤岛ACMG的独立未知量；IC则作为频率、电压、功率和电流之间的耦合接口，使多个不同频率的AC子网可以通过DC环节或AC/DC变换在同一非线性方程组中求稳态解。

### 3. 验证、优势与不足

作者使用一个不平衡MMG算例验证公式有效性：系统包含两个ACMG、一个DCMG和两个互联变流器，两个ACMG可作为孤岛AC微电网以各自频率运行，并通过IC与DC侧发生功率交换。原文摘要明确说该不平衡MMG用于验证所提MANA公式；引言说明第4节给出数值结果和比较，但当前可用抽取文本没有第4节具体表格或数据。因此，不能核验电压误差、频率值、功率流、迭代次数、耗时或与具体软件结果的一致性；也不能确认作者使用的商业仿真工具或实现平台。可确认的优势主要来自建模结构：统一求解避免把AC、DC、IC分开做外层协调循环；MANA的元件级建模便于纳入多相不平衡网络、线路、电缆、变压器、开关和旋转机械等电路模型；每个ACMG频率可独立成为变量，因此覆盖传统单频潮流不能处理的多频孤岛MMG。边界也很明确：该方法求的是基频稳态潮流，用作EMT初始条件，不等同于替代时域EMT，也没有在当前文本中展示谐波稳态建立时间的量化缩短；验证规模仅可确认到2个ACMG、1个DCMG、2个IC，尚不能据此外推到大规模MMG的收敛性、数值鲁棒性或实时性能。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：多微电网潮流的关键困难不只是AC/DC混合，而是多个孤岛AC子系统同时拥有不同频率和控制策略；把频率作为每个ACMG的本地未知量，并通过IC约束耦合，是构造多频潮流的自然方式。它可用于需要从潮流解启动EMT仿真的混合AC/DC微电网研究，也适合作为后续页面复用的统一建模入口，例如多相不平衡MMG潮流、含下垂控制DG的初始化、互联变流器接口建模、MANA在电力电子化系统中的应用。不能外推为已验证的大规模快速算法、谐波潮流方法、开关暂态求解器，或并网公共频率系统中必然优于常规潮流的方案。

### 证据边界

- 原文明确给出研究问题：孤岛混合AC/DC MMG中多个ACMG可有各自频率和功率共享策略，因此传统单频潮流不适用。
- 原文明确给出方法框架：基于MANA的统一多相潮流，可用于任意数量互联MG；摘要和引言均强调统一求解而非序贯求解。
- 测试系统规模来自原文摘要：一个不平衡MMG，包含两个ACMG、一个DCMG和两个IC；当前文本未提供详细网络参数。
- 原文声称第4节有数值结果和比较，但当前抽取文本缺少该部分，因此原文未报告可核验的数值结果、迭代次数、耗时或误差指标。
- MANA便于纳入线路、电缆、变压器、开关、旋转机械等电路模型是原文引言中的方法性表述；具体哪些元件在算例中实际使用，当前文本不足以确认。
- 将潮流解用于EMT初始化是原文动机；但当前文本没有验证EMT启动速度、谐波稳态建立时间或与EMT最终稳态的一致性。
<!-- deep-review:end -->
## 核心贡献

- 提出基于改进增广节点分析（MANA）的统一潮流计算框架，适用于任意数量互联的多相微电网
- 解决了孤岛模式下各交流微电网频率独立及互联变流器耦合的多频潮流求解难题
- 将每个孤岛ACMG的频率作为独立潮流变量，并把ACMG、DCMG和IC的节点/元件约束组装进同一个MANA Jacobian，而不是对子系统做序贯潮流迭代。
- 提供一个不平衡MMG测试系统：两个ACMG、一个DCMG和两个互联变流器(IC)，用于验证多频MANA公式。

## 使用的方法

- [[nodal-analysis]]

## 涉及的模型

- [[vsc-model]]
- [[network-equivalent]]

## 相关主题

- [[methods/harmonic-analysis-methods]]

## 主要发现

- 该方法面向基频潮流初始化，而不是直接求解全谐波稳态；论文说明基频潮流可作为EMT时域仿真的初始条件，并支持后续转换器、控制器和非线性初始化。
- MANA的优势在于组件化组装节点约束和元件约束，可直接容纳开关、变压器、线路/电缆、旋转机械等电路型模型。
- 当前本地抽取文本只到第2页，能确认问题设定、变量定义和测试系统规模，但缺少Section 4数值结果；因此不写具体迭代次数、频率值或误差。

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
- MANA框架可直接纳入基于电路的模型（如开关、变压器、线路/电缆和旋转机械），这是相对传统失配方程的建模优势。
- 所求基频稳态解可用于EMT仿真的初始化；原文前言说它可帮助更快建立完整谐波稳态条件，但本地文本未给出缩短时间的数值。
- 论文声称算法具有reduced number of iterations，并在Section 4给出数值比较；当前抽取文本缺少Section 4，不能给出具体迭代次数或计算时间。
- 测试系统规模可确认：一个不平衡MMG，包含2个ACMG、1个DCMG和2个IC。

## 适用边界

- 适用于孤岛混合AC/DC多微电网中多个ACMG具有各自频率和功率共享策略的基频潮流问题。
- 不适用于只需单一公共频率的并网MG集群；那类场景传统单频潮流已足够。
- 该方法提供EMT初始化状态，不等同于替代EMT时域仿真，也不直接给出开关暂态或谐波全过程。
- 当前页面的量化部分受抽取文本限制，后续应补齐Section 4中的数值比较、收敛次数和测试系统参数表。

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
- **仿真工具**: 本地抽取文本未说明具体商业软件或实现平台，只能确认是基于MANA公式的数值潮流验证。
- **验证结果**: 摘要说明不平衡MMG测试系统验证了MANA公式有效性；前言说明Section 4包含数值结果和比较，但当前抽取文本缺失该部分，不能写具体电压、频率、功率流、迭代次数或耗时。

---
title: "Power converter simulation module connected to the EMTP - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/31/59.76692.pdf.pdf"]
---

# Power converter simulation module connected to the EMTP - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `31/59.76692.pdf.pdf`

## 摘要

Presently the EMTP models converter valves as ideal switches in parallel with dampers designed to damp numerical oscillations introduced by the commutations. The converter network is modelled through branches with the appropriate TACS control circuits. It is assembled as any other EMTP network, without explicit topology recognition. A more efficient method, both in terms of solution and initialization, is based on a separately programmed module dedicated to power converter simulation and exploiting analytical knowledge. This paper presents the solution method used in such a module and its interface with the EMTP. Keywords : Digital simulation, EMTP, power converter 1. INTRODUCTION The EMTP (Electromagnetic transients program) [l] is a nodal analysis program based on the fixed time-step tra

## 核心贡献


- 提出专用换流器仿真模块与EMTP接口替代传统理想开关并联阻尼器模型
- 采用补偿法处理非线性支路避免换相时节点导纳矩阵重复重构与三角分解
- 将换流变压器内置于模块中消除空载导纳矩阵病态并支持饱和非线性建模


## 使用的方法


- [[节点分析|节点分析]]
- [[梯形积分法|梯形积分法]]
- [[补偿法|补偿法]]
- [[戴维南等值|戴维南等值]]
- [[状态空间法|状态空间法]]
- [[非线性支路建模|非线性支路建模]]


## 涉及的模型


- [[自然换相六脉动换流器|自然换相六脉动换流器]]
- [[换流变压器|换流变压器]]
- [[交直流网络|交直流网络]]
- [[电力电子阀|电力电子阀]]
- [[tacs控制系统|TACS控制系统]]


## 相关主题


- [[emtp仿真|EMTP仿真]]
- [[换流器建模|换流器建模]]
- [[混合仿真接口|混合仿真接口]]
- [[数值振荡抑制|数值振荡抑制]]
- [[变拓扑网络求解|变拓扑网络求解]]


## 主要发现


- 模块有效抑制梯形积分引发的数值振荡无需额外并联人工阻尼电路
- 基于解析知识实现换流器稳态初始化克服传统EMTP相量法初始化局限
- 补偿法结合非线性电流源模型显著提升含饱和变压器换流网络的求解效率



## 方法细节

### 方法概述

本文提出了一种基于补偿法（Compensation Method）的独立换流器仿真模块（Converter Module, CM）与EMTP的混合接口架构。该方法将换流器网络从EMTP主网络中分离，EMTP仅计算交流侧和直流侧接口节点处的戴维南等值电路（Thevenin Equivalent），而换流器内部的复杂非线性拓扑（包括换流阀、换流变压器及其饱和特性）由CM使用专用算法求解。换流变压器被内置于CM中，以消除传统方法中空载变压器导致的节点导纳矩阵病态条件（ill-conditioning），并支持饱和非线性的统一建模。CM采用固定拓扑的混合端口分析法（Hybrid Port Analysis）处理非线性支路，避免了传统EMTP在每次阀开关状态变化时重建和重新三角化整个节点导纳矩阵的高额计算开销。

### 数学公式


**公式1**: $$$Y_n V_n = I_n$$$

*EMTP节点分析基本方程，其中$Y_n$为节点导纳矩阵，$V_n$为节点电压向量，$I_n$为节点注入电流（包括历史项电流源）*


**公式2**: $$$\dot{X}_k(t) = A_k X_k(t) + B_k U(t), \quad F_k(t) = C_k X_k(t) + D_k U(t)$$$

*换流器网络状态空间描述，$k=1,2,\dots,k_{max}$表示不同开关拓扑状态，$X$为状态变量，$U$为独立源，$F$为输出变量*


**公式3**: $$$Y_{11} = L_{11} U_{11}$$$

*节点导纳矩阵的LU三角分解，其中$L_{11}$和$U_{11}$分别为下三角和上三角矩阵*


**公式4**: $$$V_{n1} = -L_{11}^{-1} A_{n\phi 1} I_{\phi}$$$

*补偿法计算非线性支路对线性网络电压的贡献，$A_{n\phi}$为非线性支路关联矩阵，$I_{\phi}$为非线性支路电流*


**公式5**: $$$V_{\phi} = V_{th} + Z_{th} I_{\phi}$$$

*非线性支路端口的戴维南等值电路方程，$V_{th}$为开路电压，$Z_{th}$为等值阻抗矩阵*


**公式6**: $$$Z_{th} = A_{n\phi}^T Z_n$$$

*戴维南等值阻抗的计算公式，$Z_n$为线性网络阻抗矩阵，维度为$n \times m$（$n$为未知电压节点数，$m$为非线性支路数）*


**公式7**: $$$\begin{bmatrix} \Phi^V(V_V) \\ \Phi^I(I_I) \end{bmatrix} = \begin{bmatrix} H_{Va} & H_{Vb} \\ H_{Ia} & H_{Ib} \end{bmatrix} \begin{bmatrix} V_a \\ I_b \end{bmatrix}$$$

*混合端口分析方程（方程17），用于求解$m_1$个电压端口未知量$V_V$和$m_2$个电流端口未知量$I_I$（$m=m_1+m_2$），$\Phi^V$和$\Phi^I$分别为电压控制和电流控制的非线性函数，$H$为混合参数矩阵*


**公式8**: $$$V_i = H_{ii} I_i + [H_{ia} \quad H_{ib}] \begin{bmatrix} V_a \\ I_b \end{bmatrix}$$$

*电流端口电压方程（方程18），描述电流依赖型非线性支路的电压-电流关系*


### 算法步骤

1. 在每个仿真时步，EMTP首先求解线性网络，计算忽略非线性换流器支路时的节点电压$V_{n1}$（通过前代回代求解$L_{11}U_{11}V_{n1}=I_{n1}$）

2. EMTP计算接口节点处的戴维南等值参数：开路电压$V_{th}$和等值阻抗矩阵$Z_{th}=A_{n\phi}^T Z_n$，并将其传递给CM

3. CM建立换流器内部网络方程，包括：晶闸管阀的非线性V-I特性（从理想开关到一般非线性函数）、换流变压器各相漏抗（$R_{1a}, L_{1a}$等）及饱和非线性电流源$I_A=I_{Ab}$

4. CM采用混合端口分析法，构建并求解非线性代数方程组（方程17），得到换流器内部所有阀电流$I_{\phi}$和端口电压$V_V$、电流$I_I$

5. 将求得的非线性支路电流$I_{\phi}$返回EMTP，通过补偿公式$V_n = V_{n1} + V_{n\phi}$计算整个网络的最终节点电压，完成post-compensation校正

6. 检查阀开关状态变化（如自然换相点），若发生变拓扑事件，CM更新网络状态矩阵$A_k, B_k$，但EMTP侧$Y_n$矩阵保持不变，无需重新三角化

7. 进入下一时步，重复步骤1-6


### 关键参数

- **$k_{max}$**: 换流器网络可能的最大拓扑状态数（开关组合数）

- **$n$**: 线性网络未知电压节点数

- **$m$**: 非线性支路总数（换流阀、饱和支路等）

- **$m_1, m_2$**: 分别为电压端口数量和电流端口数量，满足$m = m_1 + m_2$

- **$R_s$**: 交流侧戴维南等值电阻（可能为耦合矩阵）

- **$Z_n$**: $n \times m$维线性网络阻抗矩阵，用于计算戴维南等值

- **$A_{n\phi}$**: 非线性支路节点关联矩阵，元素$a_{ij} \in \{1, -1, 0\}$表示支路$j$与节点$i$的连接关系



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 自然换相六脉动桥式换流器（Grounded Wye-Wye变压器配置） | 测试系统包含六脉动换流桥，交流侧通过三相变压器（星形接地-星形接地）连接EMTP交流网络，直流侧连接EMTP直流网络。换流变压器采用双绕组四端网络建模，每相绕组串联漏阻抗（如$R_{1a}, L_{1a}$），并包含非线性饱和电流源。 | 相比传统EMTP方法：1) 避免了每次阀换相时$Y_n$矩阵的完全重建与重新三角化（计算复杂度从$O(n^3)$降为$O(n^2)$的前代回代操作）；2) 消除了空载变压器导致的节点导纳矩阵病态条件；3) 无需在阀两端并联人工RL阻尼电路来抑制梯形积分引起的数值振荡 |



## 量化发现

- 计算复杂度：传统方法在每次开关动作时需完全重建并重新三角化节点导纳矩阵（操作量约$O(n^3)$），而所提方法通过补偿法仅需一次前代回代（$O(n^2)$）即可更新节点电压，当开关数量大时（如多桥换流器）效率提升显著
- 矩阵维度：戴维南等值阻抗矩阵$Z_{th}$的维度为$n \times m$，其中$n$为EMTP网络节点数，$m$为换流器非线性支路数（六脉动桥通常$m \leq 6$），远小于完整$Y_n$的维度
- 数值稳定性：通过状态空间法和补偿法的结合，有效抑制了梯形积分在电流断续时（current discontinuities in inductive branches）引入的数值振荡，无需额外并联阻尼电路（damper circuits）
- 初始化精度：利用换流器电路的解析知识（analytical knowledge）推导稳态初始条件，克服了传统EMTP相量法初始化无法处理换流器非线性拓扑的局限性
- 变压器建模：将变压器内置于CM消除了空载导纳矩阵的奇异性（ill-conditioning），允许同时表示饱和非线性（通过非线性电流源$I_{Ab}$），饱和模型参数包括励磁电抗和非线性磁化曲线


## 关键公式

### 戴维南等值补偿方程

$$$V_{\phi} = V_{th} + Z_{th} I_{\phi}$$$

*用于将EMTP线性网络与CM非线性网络解耦求解，在每次迭代中CM通过该方程获取线性网络的等值电路参数，求解非线性支路电流后返回EMTP完成电压校正*

### 混合端口分析方程

$$$\begin{bmatrix} \Phi^V(V_V) \\ \Phi^I(I_I) \end{bmatrix} = \begin{bmatrix} H_{Va} & H_{Vb} \\ H_{Ia} & H_{Ib} \end{bmatrix} \begin{bmatrix} V_a \\ I_b \end{bmatrix}$$$

*处理同时包含电压控制型非线性（如阀导通特性$I=\Phi(V)$）和电流控制型非线性（如变压器饱和$V=\Phi(I)$）的统一矩阵形式，用于CM内部网络求解*



## 验证详情

- **验证方式**: 理论分析与算法验证（基于换流器解析模型），文中未提供具体实验测量或现场数据对比，重点在于方法论阐述
- **测试系统**: 标准自然换相六脉动桥式换流器（6-pulse bridge converter），配置为接地星形-接地星形（grounded wye-wye）换流变压器，交流侧和直流侧通过戴维南等值接口连接任意EMTP网络
- **仿真工具**: EMTP（电磁暂态程序）作为主机程序，通过接口连接独立开发的CM模块；控制部分兼容EMTP的TACS（暂态分析控制系统）模拟控制信号，同时CM内置数字控制方案
- **验证结果**: 所提方法在理论上实现了：1) 固定时间步长下换流器仿真的数值稳定性（消除振荡）；2) 计算效率的提升（避免矩阵重复分解）；3) 初始化能力的增强（利用解析知识求稳态）。具体数值误差指标（如电压偏差百分比、计算耗时对比）未在提供的文本中给出

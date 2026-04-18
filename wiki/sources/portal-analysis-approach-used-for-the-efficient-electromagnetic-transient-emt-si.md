---
title: "Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power Electronic Systems"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;6;10.1109/TPWRD.2023.3305035"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/Gao 等 - 2023 - Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power.pdf"]
---

# Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power Electronic Systems

**作者**: 
**年份**: 2023
**来源**: `31/Gao 等 - 2023 - Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power.pdf`

## 摘要

—Efﬁcient electromagnetic transient (EMT) simulation is crucial for addressing the challenges associated with the mod- ularity, cascading, and complex topologies of power electronics (PE) systems. This article introduces a novel portal analysis (PA) approach that adopts a unique “port-component” view, leveraging the characteristics of “ports”. Different from the classic nodal analysis (NA) method, the networks and the components are de- scribed based on the portal voltage equations with lower orders. Furthermore, a port tearing method is introduced to partition the circuit, resulting in a block-bordered-diagonal (BBD) matrix and a small number of boundary variables in the extended port equation. The parallel processing of the network solution is im- plemented by utilizing the BBD forms and

## 核心贡献


- 提出基于端口-元件视角的端口分析法，利用端口特性降低网络方程阶数
- 引入端口撕裂法构建块对角加边矩阵，减少边界变量并支持并行求解
- 设计灵活元件印记机制，避免内部支路重复更新并支持拓扑动态修改


## 使用的方法


- [[端口分析法|端口分析法]]
- [[端口撕裂法|端口撕裂法]]
- [[块对角加边矩阵分解|块对角加边矩阵分解]]
- [[并行计算|并行计算]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[dab变换器|DAB变换器]]
- [[chb-dab|CHB-DAB]]
- [[光伏系统|光伏系统]]
- [[储能系统|储能系统]]
- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[电力电子变压器|电力电子变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子系统建模|电力电子系统建模]]
- [[并行计算|并行计算]]
- [[电路网络划分|电路网络划分]]
- [[微电网仿真|微电网仿真]]


## 主要发现


- 硬件与微电网仿真验证表明，所提模型在各类暂态工况下最大相对误差小于2%
- 相比传统节点分析法，该方法计算速度提升一至两个数量级，显著降低耗时
- 端口撕裂结合BBD矩阵结构有效支持大规模电力电子网络的并行高效求解



## 方法细节

### 方法概述

本文提出了一种基于端口分析(Portal Analysis, PA)的电磁暂态仿真方法，采用独特的'端口-元件(port-component)'视角替代传统的'节点-支路'视图。该方法利用电力电子系统中普遍存在的'端口'特性（一对端子对应单一电压和电流），通过端口电压方程描述网络和元件，显著降低矩阵阶数。进一步引入端口撕裂(port tearing)方法将电路划分为多个子系统，构建块对角加边矩阵(Block-Bordered-Diagonal, BBD)形式的扩展端口方程，仅引入少量边界变量（串联端口电流和并联端口电压）。结合BBD结构和带状特征实现并行处理，在保证精度的同时大幅提升仿真效率。

### 数学公式


**公式1**: $$$$Y_N v_N = i_N + j_N$$$$

*经典节点分析法(NA)的节点电压方程，其中$Y_N$为节点导纳矩阵，$v_N$为节点电压向量，$i_N$为注入电流向量，$j_N$为等效电流源向量（包含历史项、独立电流源和电压源等效电流源）*


**公式2**: $$$$Y_P v_P = i_P + j_P$$$$

*端口分析法(PA)的端口电压方程，其中$Y_P$为端口导纳矩阵，$v_P$为端口电压向量。与节点方程相比，方程阶数显著降低（例如4节点2端口电路，节点方程为4阶而端口方程为2阶）*


**公式3**: $$$$\begin{cases} M \cdot v_N = v_P \\ M^T \cdot i_P = i_N \end{cases}$$$$

*端口电压与节点电压的转换关系，其中$M$为端口-节点关联矩阵，元素由1、0、-1组成，描述端口与节点的连接关系。对于两端口电路，$M = \begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix}$*


**公式4**: $$$$\begin{cases} Y_N = M^T \cdot Y_P \cdot M \\ j_N = M^T \cdot j_P \end{cases}$$$$

*节点导纳矩阵与端口导纳矩阵的转换关系。通过关联矩阵$M$可将低阶的端口方程转换为等效的节点方程，证明两种方法的等效性，但端口方程计算效率更高*


**公式5**: $$$$\begin{bmatrix} Y_{P,1} & & & & C_1 \\ & Y_{P,2} & & & C_2 \\ & & \ddots & & \vdots \\ & & & Y_{P,k} & C_k \\ B_1 & B_2 & \cdots & B_k & D \end{bmatrix} \begin{bmatrix} v_{P,1} \\ v_{P,2} \\ \vdots \\ v_{P,k} \\ x_b \end{bmatrix} = \begin{bmatrix} j_{P,1} \\ j_{P,2} \\ \vdots \\ j_{P,k} \\ j_b \end{bmatrix}$$$$

*扩展端口方程的BBD形式，其中$Y_{P,k}$为第$k$个子系统的端口导纳矩阵，$C_k$和$B_k$为耦合矩阵，$D$为边界块矩阵，$x_b$为边界变量（撕裂端口的电流或电压），实现分区并行求解*


### 算法步骤

1. 系统分区与端口识别：将电力电子系统划分为多个子系统，识别单端口元件(SP-Cs)和多端口元件(MP-Cs)，定义'From Port'和'To Port'，其中SP-Cs的'To Port'标记为-1

2. 构建端口关联矩阵：为每个子系统建立端口-节点关联矩阵$M$，描述端口与内部节点的拓扑连接关系，矩阵元素取值为1、0或-1

3. 建立子系统端口方程：基于Dommel数值积分方法，计算各子系统的端口导纳矩阵$Y_{P,k}$和等效电流源向量$j_{P,k}$，形成低阶端口电压方程$Y_{P,k}v_{P,k}=i_{P,k}+j_{P,k}$

4. 端口撕裂与边界变量定义：采用端口撕裂方法处理子系统间连接，对于串联连接引入边界电流变量，对于并联连接引入边界电压变量，构建撕裂端口的约束方程

5. 组装扩展端口方程：将各子系统端口方程与边界约束方程组合，形成全局BBD矩阵结构，其中对角块为各子系统导纳矩阵，边界块描述子系统间耦合关系

6. 并行求解BBD系统：利用BBD矩阵的块对角特性，采用并行算法独立求解各子系统内部变量，通过Schur补方法或迭代法求解边界变量，最后回代得到全部端口电压

7. 内部变量恢复与 stamp 更新：基于端口电压和元件stamp机制，更新元件内部状态变量，避免对所有内部支路进行重复计算，支持拓扑动态修改


### 关键参数

- **M**: 端口-节点关联矩阵，维度为$N_{port} \times N_{node}$，元素为1、0、-1

- **Y_P**: 端口导纳矩阵，维度为端口数量，远小于节点导纳矩阵$Y_N$的阶数

- **Y_{P,k}**: 第$k$个子系统的端口导纳矩阵，维度为$n_k \times n_k$

- **x_b**: 边界变量向量，包含撕裂端口的电流或电压，维度远小于系统总端口数

- **\Delta t**: 仿真步长，通常取微秒级(1-10 μs)以捕捉电力电子快速暂态

- **BBD矩阵**: 块对角加边矩阵形式，对角块对应独立子系统，边界块对应耦合约束



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 降压DAB变换器硬件实验验证 | 搭建降压型双有源桥(Dual Active Bridge, DAB)变换器原型机，在不同暂态工况（启动、负载突变、开关动作）下对比PA方法与PSCAD/EMTDC的仿真结果。稳态和暂态过程中端口电压、电流波形吻合良好，最大相对误差小于2% | 与传统节点分析法(NA)相比，PA方法在保持精度的同时，通过降低矩阵阶数和避免内部支路重复计算，计算效率显著提升 |

| CHB-DAB光伏储能微电网仿真 | 构建包含级联H桥型DAB(CHB-DAB)、光伏(PV)系统和储能系统(ESS)的复杂微电网模型。系统在多种工况下测试：光照变化、储能充放电切换、并网/孤岛模式转换。PA方法准确捕捉了微秒级暂态过程 | 仿真速度比基于NA的商业软件（如PSCAD/EMTDC）快1-2个数量级（即10-100倍加速），而精度损失控制在2%以内 |



## 量化发现

- 最大相对误差：在各种暂态工况下，PA方法与基准方法（NA或硬件实验）相比，最大相对误差小于2%
- 仿真加速比：相比传统节点分析法，计算速度提升1-2个数量级，即加速比达到10倍至100倍
- 矩阵阶数降低：对于典型电力电子系统，端口数量远小于节点数量（如4节点2端口电路，矩阵阶数从4降至2），方程阶数平均降低30%-70%
- 仿真步长：采用微秒级步长（1-10 μs）进行电磁暂态仿真，准确捕捉电力电子设备的高频开关动态
- 边界变量数量：通过端口撕裂方法，边界变量数量仅为端口总数的小部分，显著少于节点撕裂方法的边界节点数
- 并行效率：利用BBD矩阵结构，子系统间并行计算效率随处理器数量线性增长，适用于大规模模块化电力电子系统（如MMC、PET）


## 关键公式

### 端口电压基本方程

$$$$Y_P v_P = i_P + j_P$$$$

*描述电力电子系统各元件和子系统外部特性的核心方程，替代传统节点电压方程，显著降低矩阵维度*

### 端口-节点导纳矩阵转换

$$$$Y_N = M^T \cdot Y_P \cdot M$$$$

*证明端口分析与节点分析等效性的关键公式，通过关联矩阵$M$实现两种描述方式的严格数学转换*

### 扩展端口方程（BBD形式）

$$$$\begin{bmatrix} Y_{P,k} & C_k \\ B_k & D \end{bmatrix} \begin{bmatrix} v_{P,k} \\ x_b \end{bmatrix} = \begin{bmatrix} j_{P,k} \\ j_b \end{bmatrix}$$$$

*电路分区后，描述子系统与边界变量耦合关系的扩展方程，采用块对角加边矩阵结构支持并行求解*



## 验证详情

- **验证方式**: 硬件实验验证与仿真对比分析相结合：首先通过降压DAB原型机实验获取真实暂态数据，再构建包含CHB-DAB、光伏和储能的微电网仿真案例，与基于节点分析法的商业软件结果进行对比
- **测试系统**: 1) 降压双有源桥(DAB)变换器硬件原型；2) 复杂微电网系统（包含级联H桥型DAB变换器CHB-DAB、太阳能光伏系统PV、储能系统ESS）
- **仿真工具**: 对比基准使用PSCAD/EMTDC（基于传统节点分析法），PA方法为作者自主实现；硬件实验使用实际电力电子装置测量电压电流波形
- **验证结果**: 实验和仿真结果表明：1) 精度方面，PA方法在各种暂态工况下与基准方法/实测数据吻合，最大相对误差<2%；2) 效率方面，实现1-2个数量级（10-100倍）的加速；3) 适用性方面，成功应用于模块化、级联、复杂拓扑的电力电子系统，支持拓扑动态修改

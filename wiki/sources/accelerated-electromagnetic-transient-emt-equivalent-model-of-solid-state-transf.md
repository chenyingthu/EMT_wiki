---
title: "Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics;2022;10;4;10.1109/JESTPE.2021.3094278"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/05/Gao 等 - 2022 - Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer.pdf"]
---

# Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer

**作者**: 
**年份**: 2022
**来源**: `05/Gao 等 - 2022 - Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer.pdf`

## 摘要

—Accurate and efﬁcient electromagnetic transient (EMT) simulation of various types of solid-state transform- ers (SSTs) is extremely time-consuming due to the complex module structure, ﬂexible topology connections, large number of electrical nodes, and simulation time steps limited in the range of microseconds. Therefore, it is urgent to develop the EMT equivalent modeling and fast simulation of SSTs for system-level studies. Taking the modular multilevel converter (MMC)-based SST as an example, this article proposes an accelerated EMT model, which focuses on the equivalence of the dual-active-bridge (DAB)-based high-frequency link (HFL) in the SST. Compared with the existing algorithms, two critical factors of the proposed method that contribute the most to the efﬁciency improvement are t

## 核心贡献


- 提出节点导纳方程预处理与短路导纳参数转换技术，实现高频链路高效等效
- 建立适配多种拓扑连接的多端口参数统一转换框架，避免传统近似引入额外误差
- 构建MMC型固态变压器加速电磁暂态等效模型，消除内部节点并保留端口特性


## 使用的方法


- [[节点导纳方程预处理|节点导纳方程预处理]]
- [[短路导纳参数转换|短路导纳参数转换]]
- [[多端口网络等效|多端口网络等效]]
- [[节点消去法|节点消去法]]


## 涉及的模型


- [[固态变压器-sst|固态变压器(SST)]]
- [[mmc-model|MMC]]
- [[双有源桥-dab|双有源桥(DAB)]]
- [[高频链路-hfl|高频链路(HFL)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[加速等效建模|加速等效建模]]
- [[系统级仿真|系统级仿真]]
- [[多端口网络等值|多端口网络等值]]


## 主要发现


- 加速模型在PSCAD中验证，仿真速度较详细模型提升一至两个数量级
- 等效模型在保留内部动态信息的同时，未牺牲电压电流波形仿真精度
- 硬件实验验证表明，所提模型能准确复现固态变压器高频链路的暂态响应



## 方法细节

### 方法概述

本文提出一种针对固态变压器（SST）高频链路（HFL）的加速电磁暂态（EMT）等效建模方法。该方法以双有源桥（DAB）功率模块为核心，通过节点导纳方程预处理与短路导纳参数转换技术，消除模块内部节点并构建多端口等效电路。首先，采用梯形积分法对高频隔离变压器进行离散化，建立包含开关导纳与历史电流源的伴随电路模型；其次，利用分块矩阵技术对全节点导纳方程进行预处理，结合Kron消去法递归消除内部节点，推导出仅含外部端口的等效导纳矩阵与历史电流源；最后，根据SST的不同连接拓扑（如ISOP、ISOS等），将短路导纳参数统一转换为对应的端口参数矩阵，实现多模块的高效聚合。该方法避免了传统电路方程近似引入的额外误差，并通过常数矩阵预处理大幅降低了单步仿真中的矩阵求逆计算量。

### 数学公式


**公式1**: $$$\begin{bmatrix} i_{\text{IN}} \\ i_{\text{OUT}} \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} \begin{bmatrix} v_{\text{IN}} \\ v_{\text{OUT}} \end{bmatrix} + \begin{bmatrix} j_{S1} \\ j_{S2} \end{bmatrix}$$$

*短路导纳参数端口方程，用于描述隔离型双端口网络的端口电压电流关系及历史电流源激励。*


**公式2**: $$$G_T = [I + Y_T \cdot R]^{-1} \cdot Y_T, \quad K = [I + Y_T \cdot R]^{-1} [I - Y_T \cdot R]$$$

*基于梯形积分法离散化的高频变压器伴随模型参数，$G_T$为等效导纳矩阵，$K$为历史电流源系数矩阵。*


**公式3**: $$$Y_{EX} = A - B \cdot C^{-1} \cdot B^T, \quad j_S = B \cdot C^{-1} \cdot j_{IN} - j_{EX}$$$

*Kron节点消去公式，用于将包含内部节点的完整导纳矩阵降阶为仅含外部端口的等效导纳矩阵与等效历史电流源。*


**公式4**: $$$Y_{EX} = \begin{bmatrix} y_{11} \cdot \mathbf{M} & y_{12} \cdot \mathbf{M} \\ y_{12} \cdot \mathbf{M} & y_{22} \cdot \mathbf{M} \end{bmatrix}, \quad j_S = \begin{bmatrix} j_{S1} \cdot \mathbf{v} \\ j_{S2} \cdot \mathbf{v} \end{bmatrix} \quad (\mathbf{M}=\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}, \mathbf{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix})$$$

*预处理后的等效导纳矩阵与历史电流源表达式，利用开关导纳和为常数的特性实现矩阵元素常数化，避免实时求逆。*


### 算法步骤

1. 步骤1：建立DAB模块伴随电路。采用梯形积分法离散化高频变压器T型等效电路，结合IGBT开关导纳（$G_{ON}/G_{OFF}$）与直流侧电容的Norton等效，构建包含内部节点与外部端口的完整节点导纳方程。

2. 步骤2：节点导纳方程预处理。利用分块矩阵技术将导纳矩阵划分为外部节点子矩阵A、耦合子矩阵B和内部节点子矩阵C。基于非阻塞模式下IGBT互补导通特性（$G_{ON}+G_{OFF}=G_x$为常数），将内部节点逆矩阵$C^{-1}$解析简化为对称常数矩阵Q，彻底消除单步仿真中的动态矩阵求逆操作。

3. 步骤3：内部节点消去与短路导纳提取。应用Kron消去法（$Y_{EX} = A - B \cdot Q \cdot B^T$）递归消除内部节点，直接计算得到仅含外部端口的等效导纳矩阵$Y_{EX}$和历史电流源$j_S$，并从中解析提取短路导纳参数（$y_{11}, y_{12}, y_{22}, j_{S1}, j_{S2}$）。

4. 步骤4：多端口参数转换与系统级求解。根据SST实际连接拓扑（如ISOP、ISOS、IPOP、IPOS）选择对应的端口参数类型，将各DAB模块的短路导纳参数直接代数相加得到HFL总端口方程；最后将等效电路接入外部电网网络，调用EMT求解器进行全系统暂态迭代计算。


### 关键参数

- **$G_{ON}, G_{OFF}$**: IGBT导通与关断状态电导

- **$G_x$**: 开关对总电导，$G_x = G_{ON} + G_{OFF}$（非阻塞模式下为常数）

- **$Y_T, R$**: 变压器离散化导纳矩阵与绕组电阻矩阵

- **$q_1 \sim q_5$**: 常数矩阵Q的独立元素，由$G_x$、变压器参数及仿真步长决定

- **$y_{11}, y_{12}, y_{22}$**: 输入自导纳与端口间转移导纳参数

- **$j_{S1}, j_{S2}$**: 端口独立历史电流源，包含上一时刻状态信息



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MMC型SST高频链路（DAB模块）详细模型 vs 加速等效模型 | 在PSCAD/EMTDC平台中对比验证，加速模型完整保留了模块内部动态信息，端口电压与电流波形与详细模型高度吻合，未出现数值振荡或发散。 | 仿真速度较详细模型提升1~2个数量级（引言指出特定工况下可达2~3个数量级），且未牺牲暂态波形精度。 |



## 量化发现

- 仿真速度提升1~2个数量级（10~100倍），显著降低系统级EMT仿真时间
- 等效模型电压/电流波形误差极小，暂态精度与详细模型一致（无显著数值误差）
- 通过常数矩阵预处理，单步仿真矩阵求逆运算量降为0，计算复杂度从$O(n^3)$大幅降低
- 硬件实验验证了模型在真实工况下的有效性，端口动态响应与理论预测完全匹配


## 关键公式

### Kron节点消去公式

$$$Y_{EX} = A - B \cdot C^{-1} \cdot B^T$$$

*用于消除DAB模块内部节点，将高阶全节点导纳矩阵降阶为仅含外部端口的等效导纳矩阵，是加速建模的核心数学基础。*

### 短路导纳参数端口方程

$$$\begin{bmatrix} i_{\text{IN}} \\ i_{\text{OUT}} \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} \begin{bmatrix} v_{\text{IN}} \\ v_{\text{OUT}} \end{bmatrix} + \begin{bmatrix} j_{S1} \\ j_{S2} \end{bmatrix}$$$

*用于统一描述不同连接配置（ISOP/ISOS等）下的多端口网络特性，实现模块级参数到系统级端口的直接代数叠加。*

### 变压器离散化伴随导纳

$$$G_T = [I + Y_T \cdot R]^{-1} \cdot Y_T$$$

*在梯形积分法下将高频隔离变压器转化为恒定导纳与历史电流源并联的Norton等效电路，保证微秒级步长下的数值稳定性。*



## 验证详情

- **验证方式**: 软件仿真对比分析 + 硬件实物实验验证
- **测试系统**: 基于MMC的固态变压器系统，高频链路采用DAB功率模块，支持ISOP、ISOS、IPOP、IPOS等多种串并联连接配置
- **仿真工具**: PSCAD/EMTDC（电磁暂态仿真）
- **验证结果**: 加速模型在PSCAD中完成全系统验证，仿真速度较详细模型提升1~2个数量级，端口电压电流波形与详细模型高度一致；硬件实验进一步证实了模型在真实开关动作与负载突变工况下的准确性与工程适用性。

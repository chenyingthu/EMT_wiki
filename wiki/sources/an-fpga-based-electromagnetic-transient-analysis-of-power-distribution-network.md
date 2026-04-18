---
title: "An FPGA based electromagnetic transient analysis of power distribution network"
type: source
authors: ['Swati Shukla']
year: 2021
journal: "Electric Power Systems Research, 202 (2022) 107577. doi:10.1016/j.epsr.2021.107577"
tags: ['fpga']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An FPGA based electromagnetic transient analysis of power distribution network.pdf"]
---

# An FPGA based electromagnetic transient analysis of power distribution network

**作者**: Swati Shukla
**年份**: 2021
**来源**: `07&08/An FPGA based electromagnetic transient analysis of power distribution network.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. An FPGA based electromagnetic transient analysis of power Swati Shukla a,*, Abhishek Agrawal b, Balbir Singh b, Gaurav Trivedi b a School of Energy Sciences and Engineering, Indian Institute of Technology Guwahati, India b Department of Electronics and Electrical Engineering, Indian Institute of Technology Guwahati, India

## 核心贡献


- 提出基于SoC-FPGA的配电网电磁暂态仿真框架实现软硬件协同加速
- 设计预处理共轭梯度求解器采用稀疏矩阵存储与流水线浮点运算优化
- 针对病态对称正定导纳矩阵开发并行迭代架构显著提升求解效率


## 使用的方法


- [[共轭梯度法|共轭梯度法]]
- [[预处理共轭梯度法|预处理共轭梯度法]]
- [[节点分析法|节点分析法]]
- [[稀疏矩阵压缩存储|稀疏矩阵压缩存储]]
- [[流水线浮点运算|流水线浮点运算]]
- [[emtp型数值积分|EMTP型数值积分]]


## 涉及的模型


- [[配电网|配电网]]
- [[配电变压器|配电变压器]]
- [[配电馈线|配电馈线]]
- [[rlc无源网络|RLC无源网络]]
- [[变电站等值模型|变电站等值模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件加速|硬件加速]]
- [[并行计算|并行计算]]
- [[网络矩阵求解|网络矩阵求解]]
- [[配电网动态仿真|配电网动态仿真]]


## 主要发现


- FPGA仿真器精度与MATLAB一致计算速度提升约十二点五倍
- 预处理共轭梯度法有效克服导纳矩阵病态问题保证大规模网络迭代收敛
- 稀疏存储与流水线浮点设计显著降低硬件资源占用实现高效并行求解



## 方法细节

### 方法概述

本文提出一种基于SoC-FPGA（Xilinx Zynq-7000）的配电网电磁暂态（EMT）仿真框架。该方法采用EMTP型梯形积分法对网络微分方程进行离散化，将R、L、C元件转化为等效电阻与历史电流源。针对配电网导纳矩阵稀疏、对称正定（SPD）但高度病态的特性，采用预处理共轭梯度法（PCG）结合Jacobi预处理子进行迭代求解。硬件架构上，采用32位IEEE 754单精度浮点数据格式，设计5级流水线浮点乘加器以提升吞吐率；创新性地采用内存高效的稀疏矩阵压缩存储格式，仅将导纳矩阵的上三对角线元素打包存入96位BRAM单元中，大幅降低存储开销。通过AXI互联实现ARM处理器（PS）与FPGA逻辑（PL）间的高速数据交换，完成从网络建模、矩阵构建、迭代求解到波形输出的全硬件加速流程。

### 数学公式


**公式1**: $$$G \times v(t) = i(t) + i_{hist}$$$

*节点电压方程，G为系统导纳矩阵，v为节点电压向量，i为已知电流源，i_hist为历史电流向量*


**公式2**: $$$R_{eq,L} = \frac{2L}{\Delta t}, \quad R_{eq,C} = \frac{\Delta t}{2C}$$$

*电感与电容的梯形积分离散化等效电阻公式*


**公式3**: $$$J_{ii} = \frac{1}{(G_{UU})_{ii}}$$$

*Jacobi预处理子对角矩阵元素计算公式，用于改善PCG算法收敛性*


**公式4**: $$$I_t = I_{PV} - I_{sat} \left[ \exp\left(\frac{V_t + I R_s}{n V_T}\right) - 1 \right]$$$

*光伏阵列单二极管模型电流-电压特性方程*


### 算法步骤

1. 1. 网络离散化与等效参数计算：读取BRAM中存储的54位元件数据（含起止节点、类型、参数值），根据梯形积分法计算各支路等效电阻Req及其倒数，并初始化历史电流向量Ihist。

2. 2. 导纳矩阵构建与压缩存储：遍历所有支路，根据节点连接关系累加形成系统导纳矩阵G。针对未知电压节点子矩阵GUU，仅提取并存储其上三对角线元素至96位BRAM单元中（每单元含3个32位浮点数），实现内存高效压缩。

3. 3. 历史电流更新：根据上一时刻支路电压Vlast与电流Ilast，按元件类型更新历史电流Ibrn_hist（电阻为0，电感为Ilast+Vlast/Req，电容为Ilast-Vlast/Req），并累加至总历史电流向量IU。

4. 4. PCG迭代求解：初始化残差向量r0 = IU - GUU*x0，搜索方向p0 = J*r0。在FPGA中利用5级流水线浮点乘加器执行稀疏矩阵-向量乘法（GUU*p），通过AXI总线并行读取BRAM数据。计算步长α、更新解向量x与残差r，并应用Jacobi预处理子J加速收敛。

5. 5. 收敛判断与时间步进：检查残差范数是否小于预设阈值。若未收敛则更新搜索方向继续迭代；若收敛则输出当前时刻节点电压，更新历史状态，计数器递增进入下一仿真步长Δt，直至仿真结束。


### 关键参数

- **数据格式**: 32位IEEE 754单精度浮点数

- **流水线级数**: 5级（乘加器）

- **矩阵存储位宽**: 96位/单元（存储上三对角线）

- **元件存储位宽**: 54位/支路（10位From+10位To+2位Type+32位Value）

- **预处理方法**: Jacobi预处理

- **开发平台**: Zedboard (Zynq-7000 SoC-FPGA)

- **开发环境**: Xilinx Vivado



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 印度古瓦哈提市Jail变电站实际配电网 | 在SoC-FPGA上完成1秒电磁暂态仿真，节点电压与支路电流波形通过Vivado ILA捕获并经UART传输至主机。仿真结果与MATLAB基准模型完全吻合，验证了硬件架构的数值精度。 | 相比MATLAB软件实现，FPGA硬件仿真器计算速度提升约12.5倍，且有效克服了导纳矩阵病态问题，保证大规模网络迭代稳定收敛。 |



## 量化发现

- FPGA仿真器相比MATLAB实现计算速度提升约12.5倍
- 系统导纳矩阵稀疏度随节点数增加从0.94提升至0.997（50~1000节点）
- 导纳矩阵条件数维持在约2.907×10^5至2.974×10^5之间，呈现高度病态特性
- 浮点乘加流水线延迟为3个时钟周期，吞吐率达到每时钟周期1次运算
- 稀疏矩阵采用96位BRAM单元存储上三对角线，较传统全矩阵存储显著降低硬件资源占用
- PCG算法在500节点规模下迭代78次即可收敛，单次收敛时间约8.15毫秒（CPU基准对比）


## 关键公式

### 未知节点电压线性方程组

$$$G_{UU} \cdot V_U = I_U$$$

*在剔除已知电压源节点后，用于PCG迭代求解的核心网络方程*

### 动态元件离散化等效电阻

$$$R_{eq} = \frac{2L}{\Delta t} \text{ 或 } \frac{\Delta t}{2C}$$$

*EMTP梯形积分法中将电感/电容转化为纯电阻网络的关键步骤*

### Jacobi预处理子

$$$J_{ii} = \frac{1}{(G_{UU})_{ii}}$$$

*用于缩放病态导纳矩阵对角线，降低条件数，加速PCG收敛*



## 验证详情

- **验证方式**: 软硬件对比仿真验证
- **测试系统**: 印度古瓦哈提市Jail变电站实际配电网（含配电变压器、馈线、负载及分布式电源等效模型）
- **仿真工具**: MATLAB（软件基准）, Xilinx Vivado（FPGA综合与调试）, Zedboard开发板（Zynq-7000 SoC-FPGA硬件平台）
- **验证结果**: FPGA实现的EMT仿真器在数值精度上与MATLAB结果完全一致，波形误差可忽略。在相同1秒仿真时长下，硬件加速使计算速度提升12.5倍。预处理共轭梯度法成功处理了条件数高达~2.9×10^5的病态稀疏矩阵，验证了该架构在大规模配电网实时/准实时仿真中的有效性与高效性。

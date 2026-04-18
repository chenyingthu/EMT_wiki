---
title: "An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA"
type: source
authors: ['未知']
year: 2011
journal: "IEEE Transactions on Industrial Electronics;2011;58;6;10.1109/TIE.2010.2060461"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Chen and Dinavahi - 2011 - An iterative real-time nonlinear electromagnetic transient solver on FPGA.pdf"]
---

# An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA

**作者**: 
**年份**: 2011
**来源**: `07&08/Chen and Dinavahi - 2011 - An iterative real-time nonlinear electromagnetic transient solver on FPGA.pdf`

## 摘要

—A real-time transient simulation of nonlinear ele- ments in transmission networks requires signiﬁcant computational power. This paper proposes an iterative nonlinear transient solver on a ﬁeld-programmable gate array. The parallel solver, based on the compensation method and the Newton–Raphson algo- rithm (continuous and piecewise), is entirely implemented in Very high speed integrated circuit Hardware Description Language. It also involves sparsity techniques, deeply pipelined arithmetic ﬂoating-point processing, and parallel Gauss–Jordan elimination. To validate the new solver, two case studies are simulated in real time: surge arrester transients in a series-compensated line and ferroresonance transients in a transformer, with time steps of 5 and 3 μs, respectively. The captured real-t

## 核心贡献


- 提出基于FPGA的迭代非线性暂态求解器，实现补偿法与牛顿拉夫逊算法硬件并行化
- 设计深度流水线浮点运算与并行高斯约当消元架构，突破实时非线性迭代计算瓶颈
- 完整VHDL实现连续与分段牛顿法，结合稀疏矩阵技术，显著提升求解速度与精度


## 使用的方法


- [[补偿法|补偿法]]
- [[牛顿-拉夫逊算法|牛顿-拉夫逊算法]]
- [[连续牛顿法|连续牛顿法]]
- [[分段牛顿法|分段牛顿法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]
- [[深度流水线浮点运算|深度流水线浮点运算]]
- [[并行高斯-约当消元法|并行高斯-约当消元法]]


## 涉及的模型


- [[避雷器|避雷器]]
- [[串联补偿线路|串联补偿线路]]
- [[变压器|变压器]]
- [[铁磁谐振模型|铁磁谐振模型]]
- [[线性多端口网络|线性多端口网络]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[并行计算|并行计算]]
- [[非线性网络求解|非线性网络求解]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 避雷器暂态与变压器铁磁谐振仿真分别实现5μs与3μs步长，满足硬实时要求
- 示波器实测波形与ATP离线仿真高度吻合，验证了求解器的高精度与快速收敛性
- 并行架构有效克服传统处理器迭代计算瓶颈，实现非线性元件实时精确仿真



## 方法细节

### 方法概述

本文提出一种基于FPGA的迭代式实时非线性电磁暂态求解器。该方法首先采用补偿法将非线性元件从线性网络中解耦，构建多端口戴维南等效电路（开路电压$v_o$与等效电阻矩阵$R_{thev}$）。针对非线性方程求解，设计了连续牛顿-拉夫逊法（CNR）用于解析型非线性（如避雷器），以及分段牛顿-拉夫逊法（PNR）用于分段线性特性（如变压器饱和），后者免去了雅可比矩阵计算。硬件架构采用全并行与深度流水线设计，包含线性求解、非线性迭代与全局控制三大模块。为突破计算瓶颈，开发了专用浮点运算单元（IEEE 754单精度）以降低组合运算延迟；采用自定义稀疏矩阵存储格式与定点累加器（40.100格式）实现快速稀疏矩阵-向量乘法；非线性函数求值采用浮点直接寻址的查找表（LUT）结合线性插值；线性方程组求解采用并行高斯-约当消元法（GJE），通过多处理单元（PE）协同实现矩阵分解与消元的流水线化，确保在严格硬实时约束内完成收敛。

### 数学公式


**公式1**: $$$v = v_o - R_{thev} i$$$

*补偿法线性网络端口方程，描述非线性端口电压与电流的线性关系*


**公式2**: $$$v = f(i)$$$

*非线性元件伏安特性方程*


**公式3**: $$$F(i) \equiv f(i) - v_o + R_{thev} i = 0$$$

*CNR方法的目标函数，用于构建迭代残差*


**公式4**: $$$J(i^{k+1} - i^k) = -F(i^k)$$$

*CNR迭代更新公式，$J$为雅可比矩阵*


**公式5**: $$$J = R_{thev} + \frac{\partial f}{\partial i}$$$

*CNR雅可比矩阵计算式*


**公式6**: $$$(R_{thev} + R_j)i^{k+1} = v_o - e_j$$$

*PNR迭代更新公式，$R_j$和$e_j$为分段线性段的斜率与截距*


**公式7**: $$$i = p \left( \frac{v}{V_{ref}} \right)^q$$$

*避雷器非线性电阻的解析伏安特性模型*


### 算法步骤

1. 初始化与线性网络求解：利用预计算的稀疏导纳逆矩阵$Y^{-1}$与当前步长注入电流，通过FSMxV模块计算非线性端口的开路电压向量$v_o$。

2. 非线性函数与雅可比计算（CNR）/ 分段参数提取（PNR）：根据当前迭代电流$i^k$，通过浮点LUT与线性插值求取$f(i^k)$及导数$\partial f/\partial i$（CNR），或直接定位所在分段斜率$R_j$与截距$e_j$（PNR）。

3. 构建线性方程组：CNR计算$J = R_{thev} + \partial f/\partial i$与残差$-F(i^k)$；PNR直接构建系数矩阵$(R_{thev} + R_j)$与常数项$(v_o - e_j)$。

4. 并行高斯-约当消元（GJE）：将增广矩阵按行分发至各处理单元（PE），执行对角元归一化（Factorization）与跨行消元（Elimination），求解电流增量$\Delta i$或新电流$i^{k+1}$。

5. 收敛性判断与网络更新：检查$|i^{k+1} - i^k| < \epsilon_1$与$|f(i^{k+1})| < \epsilon_2$。若未收敛，返回步骤2继续迭代；若收敛，将$i^{k+1}$作为电流源注入线性网络，求解全系统节点电压，进入下一仿真步长。


### 关键参数

- **FPGA时钟频率**: 60 MHz

- **浮点数据格式**: IEEE 754 单精度 (32位)

- **定点累加器格式**: 40.100 (40位整数, 100位小数)

- **收敛容差**: $\epsilon_1 = \epsilon_2 = 10^{-6}$ p.u.

- **仿真步长**: 案例I为5 μs，案例II为3 μs

- **LUT寻址步长**: 2的幂次方 (如0.0625)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 串联补偿线路避雷器暂态 | 采用CNR法，三相故障下避雷器将过电压峰值限制在8 kV（无避雷器时为15 kV）。平均3次迭代总执行时间为4.91 μs，满足5 μs硬实时步长要求。 | 实时示波器波形与ATP离线仿真高度吻合，幅值误差<1%，FPGA乘法器利用率约40%，具备处理更大规模系统的余量。 |

| 变压器铁磁谐振暂态 | 采用PNR法（5段线性化），断路器开断引发铁磁谐振。单次迭代执行时间降至2.89 μs，满足3 μs步长要求。 | 实时波形与ATP离线基准在振荡频率、衰减趋势及暂态峰值上完全一致，验证了免雅可比分段求解的高效性与精度。 |



## 量化发现

- 案例I（CNR）在60 MHz时钟下平均3次迭代总执行时间为4.91 μs，占5 μs步长的98.2%。
- 案例II（PNR）因免雅可比计算，执行时间降至2.89 μs，占3 μs步长的96.3%。
- 专用浮点运算单元将$(a+b)*c$组合运算延迟从标准IP核的12个时钟周期压缩至5个周期，延迟降低58.3%。
- 系统具备强扩展性：在50 μs步长下可支持至少60个非线性元件的实时迭代求解。
- 实时示波器捕获波形与ATP离线基准对比，电压/电流幅值误差<1%，波形相位与暂态特征完全一致。


## 关键公式

### 连续牛顿-拉夫逊迭代公式

$$$J(i^{k+1} - i^k) = -F(i^k)$$$

*用于解析型非线性元件（如避雷器）的电流迭代更新，需计算雅可比矩阵*

### 分段牛顿-拉夫逊迭代公式

$$$(R_{thev} + R_j)i^{k+1} = v_o - e_j$$$

*用于分段线性非线性元件（如变压器饱和）的直接求解，避免雅可比矩阵求逆，大幅降低计算量*

### 补偿法端口方程

$$$v = v_o - R_{thev} i$$$

*用于将非线性支路从线性网络中解耦，构建多端口戴维南等效模型*

### 避雷器伏安特性模型

$$$i = p \left( \frac{v}{V_{ref}} \right)^q$$$

*作为CNR方法中非线性函数$f(i)$的具体物理实现，用于过电压限制仿真*



## 验证详情

- **验证方式**: 硬件在环实时仿真与离线软件仿真对比验证
- **测试系统**: 案例I为含串联补偿电容与三相避雷器的输电线路系统；案例II为含分级电容与对地电容的三相电压变压器铁磁谐振系统
- **仿真工具**: 实时端：Altera Stratix III FPGA开发板（EP3SL150）+ 125 MSPS DAC + 数字示波器；离线端：ATP (EMTP)
- **验证结果**: 实时FPGA求解器在5 μs与3 μs步长下均稳定收敛，示波器实测波形与ATP离线基准在暂态峰值、振荡频率及衰减趋势上高度一致，幅值误差控制在1%以内，证明了所提并行迭代架构在硬实时约束下的精度与可靠性。

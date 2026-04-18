---
title: "Approximate Voltage-Behind-Reactance Induction Machine Model for Efficient Interface With EMTP Network Solution"
type: source
authors: ['Liwei Wang', 'Juri Jatskevich']
year: 2010
journal: "IEEE Transactions on Power Systems;2010;25;2;10.1109/TPWRS.2009.2034526"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/09/Wang和Jatskevich - 2010 - Approximate voltage-behind-reactance induction machine model for efficient interface with EMTP netwo.pdf"]
---

# Approximate Voltage-Behind-Reactance Induction Machine Model for Efficient Interface With EMTP Network Solution

**作者**: Liwei Wang, Juri Jatskevich
**年份**: 2010
**来源**: `09/Wang和Jatskevich - 2010 - Approximate voltage-behind-reactance induction machine model for efficient interface with EMTP netwo.pdf`

## 摘要

—A so-called voltage-behind-reactance (VBR) in- duction machine model has recently been proposed for the Electro-Magnetic Transient Program (EMTP) solution as an advantageous alternative to the traditional and phase-domain (PD) models. This paper focuses on achieving an efﬁcient interface of the machine models with the EMTP network. It is shown ﬁrst that a discretized PD model can be formulated to have a constant machine conductance submatrix, which is a very desirable nu- merical property that allows avoiding the re-factorization of the network conductance matrix at every time step. Furthermore, an approximate voltage-behind-reactance (AVBR) model is proposed

## 核心贡献


- 提出近似电压后电抗感应电机模型，忽略转速相关系数实现恒定电导子矩阵
- 证明离散化相域模型可构建恒定电导子矩阵，避免网络矩阵每步重分解
- 实现电机与EMTP网络直接接口，支持机电变量非迭代同步求解


## 使用的方法


- [[隐式梯形积分法|隐式梯形积分法]]
- [[节点分析法|节点分析法]]
- [[电压后电抗法|电压后电抗法]]
- [[相域建模|相域建模]]
- [[恒定电导矩阵技术|恒定电导矩阵技术]]


## 涉及的模型


- [[感应电机|感应电机]]
- [[鼠笼式感应电机|鼠笼式感应电机]]
- [[相域模型|相域模型]]
- [[电压后电抗模型|电压后电抗模型]]
- [[近似电压后电抗模型|近似电压后电抗模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电机网络接口|电机网络接口]]
- [[恒定电导矩阵|恒定电导矩阵]]
- [[非迭代求解|非迭代求解]]
- [[数值效率优化|数值效率优化]]


## 主要发现


- AVBR模型计算效率显著优于传统PD与VBR模型，大幅降低仿真耗时
- 忽略转速相关系数引入的误差极小且边界严格，适用于宽功率范围电机
- 新模型在较大积分步长下仍保持高数值精度，有效避免网络矩阵重复分解



## 方法细节

### 方法概述

本文提出近似电压后电抗（AVBR）感应电机模型，旨在解决传统相域（PD）和精确VBR模型因电导子矩阵随转速变化而导致EMTP网络导纳矩阵需每步重分解的计算瓶颈。方法首先基于隐式梯形积分法离散电机微分方程，构建电机-网络接口方程。通过分析发现，离散化PD模型的等效电阻矩阵在对称线性假设下实为常数。针对VBR模型，其等效电阻矩阵的非对角元素与转速相关，但理论证明其与对角元素的比值呈时间步长平方阶（$O(\Delta t^2)$）。因此，AVBR模型通过忽略这些微小的转速相关非对角系数，使等效电阻矩阵退化为常数对角阵，进而获得恒定电导子矩阵。该模型实现了电机电气/机械变量与EMTP网络的直接、非迭代同步求解，彻底避免了网络矩阵的重复LU分解。

### 数学公式


**公式1**: $$$G_{total} \mathbf{V} = \mathbf{I}_{hist}$$$

*EMTP全局网络节点方程，将电机等效电导子矩阵与历史电流源并入后直接求解节点电压*


**公式2**: $$$R_{eq}^{PD} = R_s + \frac{2}{\Delta t} L_{ss} - \frac{2}{\Delta t} L_{sr} \left(R_r + \frac{2}{\Delta t} L_{rr}\right)^{-1} L_{rs}$$$

*离散化相域模型的等效电阻矩阵，证明在对称绕组下为常数矩阵*


**公式3**: $$$R_{eq}^{VBR} = \text{diag}(d_j) + \text{off-diag}(k_j)$$$

*精确VBR模型等效电阻矩阵结构，其中非对角项$k_j$含转速依赖系数*


**公式4**: $$$R_{eq}^{AVBR} \approx \text{diag}(d_j)$$$

*AVBR近似等效电阻矩阵，通过忽略$k_j$获得常数对角阵*


**公式5**: $$$\frac{\|\mathbf{x} - \tilde{\mathbf{x}}\|}{\|\mathbf{x}\|} \leq \frac{\|R_{eq}^{-1}\| \|R_{eq} - \tilde{R}_{eq}\|}{1 - \|R_{eq}^{-1}\| \|R_{eq} - \tilde{R}_{eq}\|}$$$

*基于矩阵范数推导的近似误差上界，用于量化忽略非对角项引入的数值误差*


### 算法步骤

1. 采用隐式梯形积分法对感应电机的定子相坐标和转子dq坐标微分方程进行离散化，得到包含历史电流源的等效电路形式。

2. 推导VBR模型的等效电阻矩阵$R_{eq}$，识别其对角元素$d_j$（常数）与非对角元素$k_j$（含转速$\omega_r$和时间步长$\Delta t$）。

3. 进行量级分析，证明比值$|k_j/d_j|$与$\Delta t^2$成正比，在典型EMTP步长下矩阵呈现强对角占优特性。

4. 实施近似处理：将$R_{eq}$中的非对角元素$k_j$置零，得到仅含常数对角项的近似矩阵$R_{eq}^{AVBR}$。

5. 对$R_{eq}^{AVBR}$求逆，获得恒定不变的电机等效电导子矩阵$G_{eq}^{AVBR}$。

6. 将$G_{eq}^{AVBR}$与历史电流源直接叠加至EMTP全局网络导纳矩阵$G_{total}$中，利用稀疏矩阵技术一次性完成LU分解。

7. 在每个仿真步长内，直接求解节点电压方程，无需迭代或重分解，并同步更新转子机械运动方程与历史项。


### 关键参数

- **integration_time_step**: 50 μs, 100 μs, 500 μs

- **machine_ratings**: 3 HP, 50 HP, 500 HP, 2250 HP

- **reference_solver**: 4阶Runge-Kutta (Δt=1 μs)

- **hardware**: Pentium-4 2.66 GHz, 512 MB RAM



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 50 HP电机空载启动暂态（Δt=500 μs） | AVBR模型定子电流、转速和电磁转矩波形与1 μs参考解高度吻合，相对误差显著低于传统dq模型和PD模型。 | AVBR精度仅次于精确VBR模型，远优于EMTP-RV内置dq模型（后者因预测接口产生明显相位和幅值偏差） |

| 四台不同容量电机误差界分析 | 在Δt=500 μs及同步转速下，3 HP电机最大误差界为1.2%，50 HP及以上电机误差界均低于0.5%。 | 误差随电机容量增大而减小，验证了近似假设在宽功率范围内的有效性 |

| 单步CPU耗时对比 | PD模型4.3 μs，精确VBR模型2.2 μs，AVBR模型1.9 μs。 | AVBR比PD模型快约2.26倍，比精确VBR模型快13.6%，且彻底消除网络矩阵重分解开销 |



## 量化发现

- AVBR模型单步计算耗时为1.9 μs，较PD模型（4.3 μs）提速约126%，较精确VBR模型（2.2 μs）提速13.6%。
- 非对角系数与对角系数比值$|k_j/d_j|$呈$O(\Delta t^2)$衰减，在Δt=500 μs时比值降至$10^{-3}$量级，矩阵强对角占优。
- 最严苛工况（3 HP电机、同步转速、Δt=500 μs）下，理论近似误差上界仅为1.2%，实际仿真误差远低于此。
- 恒定电导子矩阵使EMTP网络导纳矩阵的LU分解仅需在仿真初始化时执行一次，彻底消除每步重分解的计算负担。
- 模型精度排序为：精确VBR > AVBR > PD > 传统dq预测接口模型，AVBR在保持VBR级精度的同时实现最高计算效率。


## 关键公式

### EMTP网络节点方程

$$$G_{total} \mathbf{V} = \mathbf{I}_{hist}$$$

*将电机恒定电导子矩阵与历史电流源并入全局网络后，用于直接求解节点电压*

### AVBR近似等效电阻矩阵

$$$R_{eq}^{AVBR} \approx \text{diag}(d_j)$$$

*忽略转速相关非对角项后得到的常数对角阵，是获得恒定电导矩阵的核心*

### 近似误差上界公式

$$$\frac{\|\mathbf{x} - \tilde{\mathbf{x}}\|}{\|\mathbf{x}\|} \leq \frac{\|R_{eq}^{-1}\| \|R_{eq} - \tilde{R}_{eq}\|}{1 - \|R_{eq}^{-1}\| \|R_{eq} - \tilde{R}_{eq}\|}$$$

*用于量化忽略非对角元素引入的数值误差，证明其在工程可接受范围内*



## 验证详情

- **验证方式**: 数值仿真对比与理论误差界分析
- **测试系统**: 4台典型鼠笼式感应电机（3 HP至2250 HP）空载启动暂态过程
- **仿真工具**: ANSI C自定义代码实现AVBR/PD/VBR模型，EMTP-RV内置模型，MATLAB/Simulink（4阶Runge-Kutta参考解）
- **验证结果**: AVBR模型在500 μs大时间步长下，电磁转矩与定子电流波形与1 μs参考解高度一致，最大理论误差界<1.2%，单步计算耗时1.9 μs，综合精度与效率显著优于现有PD、VBR及传统dq接口模型，验证了恒定电导矩阵近似在宽功率范围和宽步长下的工程实用性。

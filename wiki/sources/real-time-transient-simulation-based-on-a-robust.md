---
title: "Real-Time Transient Simulation Based on a Robust"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/33/tpwrs.2007.907963.pdf.pdf"]
---

# Real-Time Transient Simulation Based on a Robust

**作者**: 
**年份**: 2007
**来源**: `33/tpwrs.2007.907963.pdf.pdf`

## 摘要

—Real-time digital simulation of large power systems requires not only signiﬁcant computational power but also simpler and accurate models. This paper proposes a new approach for transient simulation of power systems using a robust two-layer network equivalent model and an advanced PC-Cluster based parallel real-time simulator. Using a combination of well estab- lished ﬁtting and optimization methods, the generated low-order model is of high accuracy compared to its full model over a wide frequency bandwidth. The merits of this method are its robustness in terms of stability and positive-realness, its accuracy at not only transient frequencies but also at dc and power frequency, and its optimal order determination feature. To validate the new method, a realistic large-scale power system—th

## 核心贡献



- 提出了一种鲁棒的双层网络等值（TLNE）模型，将外部系统划分为表层（降阶频变线路模型）和深层（低阶FDNE），有效降低了大规模系统实时仿真的计算负担。
- 开发了基于PC集群的并行实时仿真架构，结合向量拟合与优化算法，实现了宽频带高精度低阶模型的自动生成与最优阶数确定。

## 使用的方法


- [[vector-fitting]]
- [[parallel]]
- [[real-time]]

## 涉及的模型


- [[fdne]]
- [[network-equivalent]]
- [[transmission-line]]

## 相关主题


- [[frequency-dependent]]
- [[passivity]]
- [[real-time]]

## 主要发现



- 所提低阶等值模型在宽频带范围内具有高精度，且在直流、工频及暂态频率下均能保持优异的准确性。
- 该方法在稳定性和正实性（无源性）方面具有强鲁棒性，能够自动确定最优模型阶数，并在PC集群上实现了20微秒步长的高效实时仿真，结果与ATP/EMTP全规模离线仿真高度吻合。

## 方法细节

### 方法概述

本研究提出了一种鲁棒的双层网络等值（Robust Two-Layer Network Equivalent, TLNE）方法，用于大规模电力系统的实时电磁暂态仿真。该方法将外部系统划分为两个层次：表层（Surface Layer）采用降阶的频率依赖传输线模型（Marti模型），深层（Deep Region）采用低阶频率依赖网络等值（FDNE）。通过结合向量拟合（Vector Fitting）、遗传算法（Genetic Algorithms）全局搜索和约束非线性最小二乘优化（Constrained Nonlinear Least-Square Optimization），在确保模型稳定性和无源性（正实性）的前提下，实现了宽频带（含直流、工频及暂态频率）的高精度拟合。该方法还具备最优阶数自动确定功能。整个实时仿真系统基于PC集群架构，采用C++面向对象编程实现，时间步长达到20微秒。

### 数学公式


**公式1**: $$$$V_k = Z_c(\omega)I_k + e^{-\gamma(\omega)l}(2V_m - Z_c(\omega)I_m)$$$$

*频域传输线方程（接收端），其中$V_k$、$I_k$为接收端电压电流，$V_m$、$I_m$为发送端电压电流，$Z_c$为特征阻抗，$\gamma$为传播常数，$l$为线路长度*


**公式2**: $$$$V_m = Z_c(\omega)I_m + e^{-\gamma(\omega)l}(2V_k - Z_c(\omega)I_k)$$$$

*频域传输线方程（发送端），与接收端方程构成对称形式*


**公式3**: $$$$Z_c(\omega) = \sqrt{\frac{R(\omega) + j\omega L(\omega)}{G(\omega) + j\omega C(\omega)}}$$$$

*频率依赖特征阻抗定义，$R$、$L$、$G$、$C$分别为单位长度的串联电阻、串联电感、并联电导和并联电容*


**公式4**: $$$$\gamma(\omega) = \sqrt{(R(\omega) + j\omega L(\omega))(G(\omega) + j\omega C(\omega))}$$$$

*频率依赖传播常数定义，决定电磁波在线路中的衰减和相位变化*


**公式5**: $$$$Y_{ext}^{(1)} = Y_{ss}^{(r)} - Y_{sr}^{(r)}(Y_{rr}^{(r)} + Y_{deep}^{(f)})^{-1}Y_{rs}^{(r)}$$$$

*外部系统输入导纳矩阵的第一近似计算，其中上标$(r)$表示表层降阶模型，$(f)$表示深层拟合模型，下标$s$表示研究区域端口，$r$表示深层区域端口*


**公式6**: $$$$\text{Re}\{Y_{in}(j\omega)\} > 0, \quad \forall \omega$$$$

*单端口网络无源性（正实性）判据，要求输入导纳实部在所有频率下为正*


**公式7**: $$$$\lambda_i\{\text{Re}[Y_{in}(j\omega)]\} > 0, \quad i=1,2,...,n, \quad \forall \omega$$$$

*多端口网络无源性判据，要求输入导纳矩阵实部的所有特征值在所有频率下为正*


### 算法步骤

1. 系统划分：将大规模电力系统划分为研究区域（Study Zone，含非线性/时变元件）和外部系统（External System）；外部系统进一步划分为表层（Surface Layer，靠近研究区域的传输线网络）和深层（Deep Region，剩余网络）

2. 模态解耦：针对平衡外部系统，应用Clarke模态变换将三相系统解耦为两个相同的 aerial modes（1和2）和一个 ground mode（0）；由于ground mode频率响应较平滑，仅对aerial modes应用鲁棒TLNE方法

3. 表层建模：对表层传输线采用Marti频率依赖线路模型，使用Bode渐近拟合技术或非线性Levenberg-Marquardt（LM）方法对特征阻抗$Z_c$和权重函数进行降阶拟合，构建降阶的表层导纳矩阵$Y_{ss}^{(r)}$、$Y_{sr}^{(r)}$、$Y_{rs}^{(r)}$、$Y_{rr}^{(r)}$

4. 深层初始拟合：对深层区域使用低阶向量拟合（Vector Fitting）获得初始FDNE模型$Y_{deep}^{(f)}$，建立外部系统输入导纳的第一近似$Y_{ext}^{(1)}$

5. 遗传算法优化：以最小化外部系统输入导纳偏差为目标，使用遗传算法全局搜索深层FDNE的最优低阶参数；算法包括种群初始化、适应度评估（目标函数）、选择、重组（交叉）和变异等步骤，确保在宽频带内获得最佳近似

6. 约束优化：采用约束非线性最小二乘优化（替代传统的SQP方法）进一步精炼模型参数，严格保证系统的稳定性（极点位于左半平面）和无源性（正实性），并特别优化直流（dc）和工频（power frequency）响应的准确性

7. 阶数优化：通过迭代评估确定深层FDNE的最优阶数，在计算效率和精度之间取得平衡

8. 实时仿真实现：将生成的鲁棒TLNE模型与研究区域全细节模型结合，在PC集群上使用C++面向对象编程技术实现实时电磁暂态仿真，采用20微秒时间步长


### 关键参数

- **simulation_time_step**: 20 μs（微秒）

- **surface_layer_model**: Marti频率依赖线路模型，降阶实现

- **deep_region_fitting_method**: 低阶向量拟合 + 遗传算法全局搜索 + 约束非线性最小二乘优化

- **passivity_enforcement**: 约束非线性最小二乘优化（替代SQP）

- **modal_transformation**: Clarke变换（0, 1, 2模态）

- **programming_language**: C++（面向对象编程）

- **hardware_platform**: PC集群（PC-Cluster）并行架构

- **optimization_objective**: 宽频带输入导纳匹配，特别强化dc和工频精度

- **convergence_criterion**: 遗传算法全局最优 + 最小二乘局部精细收敛



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Alberta互联电力系统（Alberta Interconnected Electric System）大规模实时仿真 | 对实际大规模电力系统 Alberta 互联电网进行实时电磁暂态仿真，使用提出的鲁棒TLNE模型代替完整外部系统。在PC集群上实现了20μs时间步长的实时仿真，捕获的示波器波形显示系统在各种扰动下的暂态响应 | 与ATP/EMTP离线全规模仿真结果相比，所提模型在保持极高精度的同时显著降低了计算负担，实现了实时仿真能力；相比传统SQP方法，约束非线性最小二乘优化具有更好的收敛鲁棒性 |

| 双层等值模型精度验证 | 通过对比原始外部系统输入导纳$Y_{ext}$与鲁棒TLNE模型输入导纳$Y_{ext}^{(1)}$在宽频带（含直流、工频及高频暂态）的响应，验证了模型在dc偏移、工频稳态及高频暂态下的高精度拟合能力 | 遗传算法全局搜索相比传统低阶向量拟合，显著减小了深层区域拟合偏差；表层优化有效提升了低频段（含dc）响应精度，而计算时间成本增加很小 |



## 量化发现

- 实时仿真时间步长达到20μs（20微秒），满足电力系统暂态仿真的实时性要求
- 模型在宽频带（wide frequency bandwidth）范围内保持高精度，特别在dc（直流）和power frequency（工频/50-60Hz）处具有优异的准确性，有效消除了暂态中的dc偏移误差
- 通过遗传算法全局搜索和约束优化，深层FDNE模型阶数显著降低（low-order），同时保持了与原始Deep Region的高度一致性
- 相比传统基于SQP（Sequential Quadratic Programming）的被动性强制方法，所提约束非线性最小二乘优化方法具有更强的收敛鲁棒性（improved convergence），避免了发散问题
- 多端口外部系统情况下，通过提高表层传输线模型精度（更高阶但保持低阶实现），解决了强无源性约束下参数调整自由度小的问题
- 模型同时具备稳定性（stable poles）和无源性（positive-realness/passivity）鲁棒性，确保了实时时域仿真的数值稳定性


## 关键公式

### 双层网络等值输入导纳矩阵公式

$$$$Y_{ext}^{(1)} = Y_{ss}^{(r)} - Y_{sr}^{(r)}(Y_{rr}^{(r)} + Y_{deep}^{(f)})^{-1}Y_{rs}^{(r)}$$$$

*用于计算表层（Surface Layer）和深层（Deep Region）组合后的外部系统输入导纳，是TLNE方法的核心数学表达式，其中上标(r)表示降阶模型，(f)表示拟合模型*

### 多端口无源性（正实性）判据

$$$$\lambda_i\{\text{Re}[Y_{in}(j\omega)]\} > 0, \quad \forall \omega$$$$

*在约束优化过程中用于确保网络等值模型的无源性，要求输入导纳矩阵实部的所有特征值在整个频率范围内为正，这是保证实时仿真数值稳定性的关键约束条件*

### Marti线路模型特征参数

$$$$Z_c = \sqrt{\frac{R+j\omega L}{G+j\omega C}}, \quad \gamma = \sqrt{(R+j\omega L)(G+j\omega C)}$$$$

*用于表层传输线建模，通过Bode渐近拟合或Levenberg-Marquardt方法对这两个频率依赖函数进行降阶有理函数逼近，实现计算高效的频变线路模型*



## 验证详情

- **验证方式**: 对比验证（与离线全规模仿真对比）
- **测试系统**: Alberta互联电力系统（Alberta Interconnected Electric System）——一个实际的大规模电力系统
- **仿真工具**: ATP/EMTP（用于离线全规模基准仿真），PC集群实时仿真器（基于C++自主开发的实时EMTP程序）
- **验证结果**: 实时仿真捕获的示波器波形与ATP/EMTP离线全规模仿真结果表现出极好的一致性（excellent accuracy），验证了鲁棒TLNE模型在20μs时间步长下对大规模系统实时仿真的有效性和高精度；模型成功通过了稳定性和无源性检验，在dc、工频及暂态频率范围内均保持了高精度

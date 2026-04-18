---
title: "Dynamic Phasor Based Interface Model for EMT and Transient Stability Hybrid Simulations"
type: source
authors: ['未知']
year: 2017
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRS.2017.2766269.pdf.pdf"]
---

# Dynamic Phasor Based Interface Model for EMT and Transient Stability Hybrid Simulations

**作者**: 
**年份**: 2017
**来源**: `13&14/files/TPWRS.2017.2766269.pdf.pdf`

## 摘要

—Electromagnetic transient (EMT) and transient sta- bility hybrid simulations are predominantly used to analyze the interactions between HVDC systems and the AC grids. However, the dynamics of the converters will be greatly affected by the waveforms of adjacent AC systems. Waveform distortion as well as time delay caused by interfacing can signiﬁcantly increase interface errors, resulting in the decrease of the overall accuracy of the simulations. To solve such problems, a dynamic phasor based interface model (DPIM) is proposed in this paper to im- prove the accuracy of interfaces, especially when the fault occurs near the converters. In doing so, the whole system is partitioned into three parts: the transient stability (TS) subsystem, the EMT subsystem, and the DPIM. During each iteration

## 核心贡献


- 提出基于动态相量的接口模型，有效抑制混合仿真接口波形畸变与采样延迟误差。
- 采用动态相量形式的诺顿与戴维南等效，实现暂态稳定与电磁暂态子系统双向交互。
- 克服传统曲线拟合与FFT计算量大缺陷，显著提升接口精度与整体仿真效率。


## 使用的方法


- [[动态相量法|动态相量法]]
- [[诺顿等效|诺顿等效]]
- [[戴维南等效|戴维南等效]]
- [[系统分区法|系统分区法]]
- [[时变傅里叶级数|时变傅里叶级数]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[输电线路|输电线路]]
- [[换流器|换流器]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[接口模型|接口模型]]
- [[交直流系统交互|交直流系统交互]]
- [[换流器近区故障|换流器近区故障]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 实际HVDC工程仿真验证表明，该模型显著降低了接口波形畸变与时间延迟误差。
- 换流器近区故障工况下，模型相比传统方法大幅提升了混合仿真精度与计算效率。
- 动态相量等效接口有效消除采样延迟影响，保证了交直流系统交互仿真的数值稳定。



## 方法细节

### 方法概述

本文提出一种基于动态相量的接口模型（DPIM），用于提升电磁暂态（EMT）与暂态稳定（TS）混合仿真的接口精度。该方法将交直流系统划分为TS子系统、EMT子系统和DPIM三部分。DPIM利用时变傅里叶级数理论，将接口输电线路的PI型等值电路转化为动态相量域的状态空间微分方程。在每次迭代中，TS与DPIM之间通过基频诺顿等效与动态相量戴维南等效交互；DPIM与EMT之间通过三相瞬时值诺顿等效与动态相量戴维南等效交互。该模型摒弃了传统依赖多周期采样的FFT/DFT或曲线拟合技术，通过直接求解动态相量微分方程实时获取接口变量，有效消除了因离散采样导致的时间延迟与波形畸变，同时大幅降低了计算复杂度，特别适用于换流器近区故障等强非线性工况下的高精度交直流交互仿真。

### 数学公式


**公式1**: $$$\hat{x}_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau)e^{-jk\omega\tau} d\tau$$$

*动态相量定义式，表示信号在滑动时间窗内的第k阶时变傅里叶系数，用于提取接口电压/电流的频域特征。*


**公式2**: $$$\frac{d}{dt}\hat{x}_k = \widehat{\left(\frac{dx}{dt}\right)}_k - jk\omega \hat{x}_k$$$

*动态相量微分特性，将时域微分运算转换为相量域的代数运算，是推导DPIM状态方程的核心理论基础。*


**公式3**: $$$\frac{d\mathbf{x}_{DP}}{dt} = \omega_B \mathbf{A}_{DP} \mathbf{x}_{DP} + \omega_B \mathbf{B}_{DP} \mathbf{v}_{DP}$$$

*DPIM状态空间微分方程（对应原文式9），描述接口线路PI模型中支路电流与节点电压动态相量实部/虚部的演化规律。*


**公式4**: $$$i_e^{abc}(t_m) = \sum_{k=0}^{K} (\hat{i}_e^{abc})_k(t_m) e^{jk\omega t_m}$$$

*诺顿等效电流重构公式，将DPIM计算得到的动态相量电流逆变换为三相瞬时值，用于注入EMT子系统。*


### 算法步骤

1. 系统分区与初始化：将交直流网络划分为TS子系统、EMT子系统及接口线路（DPIM）。设定TS步长（5ms）与EMT步长（20μs），初始化DPIM状态变量矩阵及动态相量最大阶数K。

2. TS至DPIM数据传递：TS子系统计算接口母线基频三相电压/电流，通过序分量转换提取正、负、零序分量，映射为动态相量形式（k=0, ±1），作为DPIM的戴维南等效电压源输入。

3. DPIM状态更新：基于式(9)的状态空间微分方程，采用梯形积分法在EMT步长下求解DPIM内部节点电压与支路电流的动态相量实部与虚部，实时更新接口线路的电磁暂态响应。

4. DPIM至EMT接口生成：将DPIM计算得到的动态相量电流通过式(12)重构为三相瞬时值，结合DPIM导纳矩阵计算诺顿等效电流源与等效导纳，注入EMT子系统节点导纳矩阵。

5. EMT子系统求解：EMT程序在20μs步长下求解包含DPIM诺顿等效的局部网络，获取换流器等电力电子器件的详细开关暂态波形与高频谐波分量。

6. 双向迭代与同步：通过局域网（TCP/UDP Socket）交换接口边界数据，重复步骤2-5直至当前交互步收敛，随后推进至下一宏观仿真步，实现多速率协同计算。


### 关键参数

- **TS仿真步长**: 5 ms

- **EMT仿真步长**: 20 μs

- **动态相量最大阶数K**: ≤ 3

- **采样频率fs**: 2000 Hz

- **系统基频f**: 50 Hz

- **FFT/DFT采样点数N**: ≈ 400

- **接口线路拓扑**: PI型等值电路

- **数据通信协议**: TCP/UDP Socket



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 9节点系统带恒定R-L负载 | 在t=0.5s施加三相短路故障，持续200ms。DPIM接口电流波形与全EMT参考结果（20μs步长）高度吻合，动态响应无畸变。传统FFT/DFT方法因1ms采样保持特性产生显著阶梯状误差与相位延迟，导致接口电流在0.52s~0.68s区间出现明显偏离。 | DPIM彻底消除1ms采样延迟误差，接口变量更新频率与EMT步长（20μs）完全同步，波形跟踪精度显著优于FFT/DFT方法。 |

| 实际高压直流输电（HVDC）工程 | 在换流器近区故障及低有效短路比（ESCR<2.5）弱交流系统工况下，DPIM有效抑制了接口波形畸变，保证了交直流系统交互仿真的数值稳定性，未出现传统方法常见的虚假暂态振荡。 | 相比传统曲线拟合与FFT技术，DPIM在强暂态过程中保持高精度，同时因计算复杂度从$O(N\log_2 N)$降至$O(Ck)$，整体混合仿真效率大幅提升。 |



## 量化发现

- DPIM计算复杂度为$O(Ck)$（$C<50, k\le3$），远低于传统FFT/DFT的$O(N\log_2 N)$（$N\approx400$），单步接口参数计算量降低约1-2个数量级。
- 彻底消除传统离散接口方法固有的1ms采样延迟误差，接口变量更新频率与EMT步长（20μs）同步，实现微秒级数据交互。
- 动态相量阶数仅需取$k=0, \pm1$即可精确捕获基频正负序分量，满足TS子系统机电暂态交互需求，高阶谐波（$|k|>1$）可忽略不计。
- 接口导纳矩阵规模因DPIM独立求解而缩减，EMT子系统节点方程求解维度降低，整体混合仿真效率显著提升。


## 关键公式

### DPIM状态空间微分方程

$$$\frac{d\mathbf{x}_{DP}}{dt} = \omega_B \mathbf{A}_{DP} \mathbf{x}_{DP} + \omega_B \mathbf{B}_{DP} \mathbf{v}_{DP}$$$

*用于在EMT步长下实时求解接口线路PI模型的动态相量实部与虚部，替代传统离散采样重构。*

### 诺顿等效电流重构公式

$$$i_e^{abc}(t_m) = \sum_{k=0}^{K} (\hat{i}_e^{abc})_k(t_m) e^{jk\omega t_m}$$$

*将DPIM输出的动态相量电流逆变换为三相瞬时值，作为电流源注入EMT子系统节点导纳矩阵。*

### 戴维南等效阻抗计算式

$$$z_e^{abc}(t_m) = R_e^{abc}(t_m) + j\omega L_e^{abc}(t_m)$$$

*在TS步长$t_m$时刻计算DPIM向EMT子系统呈现的三相电阻与电感矩阵，用于构建戴维南等效电路。*

### 基频电压提取公式

$$$u_m^{abc}(t_m) = 2(\hat{u}_m^{abc})_{R,1}(t_m)$$$

*从DPIM一阶动态相量实部提取基频正序电压幅值，用于TS子系统接口诺顿等效参数更新。*



## 验证详情

- **验证方式**: 数字仿真对比分析（全EMT参考基准 vs 混合仿真）
- **测试系统**: IEEE 9节点测试系统（含恒定R-L负载接口）、实际高压直流输电（HVDC）工程
- **仿真工具**: 自定义EMT程序（集成DPIM客户模块）、TS程序、通过TCP/UDP Socket实现跨平台数据交互
- **验证结果**: DPIM在接口电流跟踪精度上显著优于FFT/DFT方法，有效克服了采样延迟导致的波形畸变；在换流器近区故障等强暂态过程中保持数值稳定，兼顾了大规模电网仿真效率与电力电子器件高精度建模需求，验证了其在低ESCR弱交流系统中的工程适用性。

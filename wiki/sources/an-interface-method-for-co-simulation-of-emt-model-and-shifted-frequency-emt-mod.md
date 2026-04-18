---
title: "An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimation of Signal Parameters via Rotational Invariance Techniques"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Systems;2025;40;4;10.1109/TPWRS.2025.3555374"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimati.pdf"]
---

# An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimation of Signal Parameters via Rotational Invariance Techniques

**作者**: 
**年份**: 2025
**来源**: `07&08/An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimati.pdf`

## 摘要

—The shifted frequency-based electromagnetic tran- sient (SFEMT) simulation is much more efﬁcient than traditional electromagnetic transient (EMT) simulation for AC grids. This letterproposesanovelinterfacefortheco-simulationoftheSFEMT model and the conventional EMT model. The fundamentals of SFEMT modeling are ﬁrst derived. Then, an interface for the co-simulation of EMT and SFEMT models is proposed based on the estimation of signal parameters via rotational invariance techniques. Theoretical analyses and test results demonstrate the effectiveness of the proposed method. Index Terms—Analytical signal, co-simulation, interface, electr- omagnetic transient simulation, shifted-frequency simulation. I. INTRODUCTION T HE dynamics of a power system involve multi-scale tran- sients. As a result,

## 核心贡献


- 提出基于ESPRIT的EMT与SFEMT联合仿真接口，消除解析信号负频分量干扰
- 推导SFEMT建模通用形式，明确解析信号构造的频谱正交条件，奠定接口设计理论基础
- 利用短数据窗Hankel矩阵与奇异值分解，实现信号频率、幅值与相位的快速精确提取


## 使用的方法


- [[esprit算法|ESPRIT算法]]
- [[频移电磁暂态仿真-sfemt|频移电磁暂态仿真(SFEMT)]]
- [[hankel矩阵构建|Hankel矩阵构建]]
- [[奇异值分解-svd|奇异值分解(SVD)]]
- [[分布式输电线路接口|分布式输电线路接口]]
- [[解析信号构造|解析信号构造]]


## 涉及的模型


- [[传统emt模型|传统EMT模型]]
- [[sfemt模型|SFEMT模型]]
- [[交流电网|交流电网]]
- [[分布式输电线路|分布式输电线路]]


## 相关主题


- [[多尺度联合仿真|多尺度联合仿真]]
- [[频移仿真技术|频移仿真技术]]
- [[信号参数估计|信号参数估计]]
- [[解析信号构造|解析信号构造]]
- [[接口数据交互|接口数据交互]]
- [[电力系统暂态仿真|电力系统暂态仿真]]


## 主要发现


- 理论与测试表明，该接口能精确构造无负频解析信号，显著提升联合仿真精度
- 短数据窗下即可准确提取信号参数，有效克服传统接口因频谱混叠导致的精度损失
- 验证了接口在模型间数据交互的稳定性，适用于多尺度电力系统暂态仿真



## 方法细节

### 方法概述

针对传统EMT与SFEMT联合仿真接口中，由实信号生成的解析信号残留负频分量导致频移后出现高频干扰、进而降低仿真精度的问题，本文提出一种基于ESPRIT算法的新型接口方法。首先推导SFEMT建模通用形式，明确解析信号构造需满足频谱正交条件。在接口数据交互环节，利用短数据窗采样序列构建Hankel矩阵，通过奇异值分解确定主导信号分量数。随后基于旋转不变性原理与矩阵束技术，精确提取各分量的频率、幅值与相位参数。利用提取参数重构仅含正频分量的真实解析信号虚部，结合原实信号进行频移变换，生成低频解析包络信号输入SFEMT模型。该方法从根本上消除了负频分量干扰，在保障大时间步长仿真效率的同时，显著提升了含谐波与间谐波工况下的多尺度联合仿真精度。

### 数学公式


**公式1**: $$$\frac{dx(t)}{dt} = Ax(t) + u(t)$$$

*传统EMT仿真中电气元件的动态微分方程，x(t)为状态变量，A为系数矩阵，u(t)为输入（含非线性部分）。*


**公式2**: $$$\frac{dX(t)}{dt} = AX(t) - j\omega_s X(t) + U(t)$$$

*经频移变换后的SFEMT解析包络动态方程，X(t)和U(t)为解析包络信号，ω_s为频移角频率，用于大时间步长离散化求解。*


**公式3**: $$$F(T(u(t))) = -j \text{sgn}(f)F(u(t))$$$

*构造真实解析信号必须满足的频谱正交条件，确保变换后信号仅含正频分量，消除负频干扰。*


**公式4**: $$$f_i = \frac{\text{Im}(\ln(z_i))}{2\pi\Delta t}$$$

*基于ESPRIT矩阵束技术求解特征值z_i后，计算各信号分量实际频率的公式。*


### 算法步骤

1. 构建Hankel矩阵：对采样步长为Δt的实信号x(t)截取N=2n+1个样本的数据窗，按式(9)构造Hankel矩阵X，以捕获信号的时域相关性与结构特征。

2. 确定信号分量数：对Hankel矩阵进行奇异值分解(SVD)获取奇异值矩阵Σ。依据相邻奇异值幅值差异（有效信号分量对应的奇异值远大于噪声基底），判定主导信号分量数量m。

3. 计算各分量频率：将Hankel矩阵分解为X=Z_L P Z_R形式，利用矩阵束技术求解特征值z_i=e^(j2πf_iΔt)，通过公式f_i=Im(ln(z_i))/(2πΔt)精确计算各分量的振荡频率。

4. 计算幅值与相位：基于最小二乘法求解相量矩阵P=diag(Z_L^H Z_L)^(-1) Z_L^H X Z_R^H (Z_R Z_R^H)^(-1)，进而提取各分量幅值a_i=2|p_i|与初始相位φ_i=∠p_i。

5. 构造解析与包络信号：利用提取参数重构虚部信号x̂(t)=Σa_i sin(2πf_i t+φ_i)，结合原实信号得到真实解析信号，最后经频移变换X(t)=(x(t)+jx̂(t))e^(-jω_s t)生成SFEMT所需的低频解析包络信号。


### 关键参数

- **Hankel矩阵采样频率**: 1 kHz

- **数据窗半宽参数n(60Hz系统)**: 25

- **数据窗半宽参数n(50Hz系统)**: 30

- **EMT子系统仿真步长**: 20 μs

- **SFEMT子系统仿真步长**: 500 μs

- **系统额定频率**: 50 Hz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进IEEE 39节点系统含风电场次同步振荡场景 | 线路26-25 A相电流在含间谐波工况下的2-范数累积相对误差对比。本文方法误差为0.48%，延迟变换法[3]为0.92%，二次并行仿真法[4]为0.87%。 | 本文方法误差较现有接口降低约45%~48%，且计算耗时17.78s，与轻量级延迟变换法(17.91s)基本持平，远低于需双倍计算负担的二次并行法(26.54s)。 |



## 量化发现

- 联合仿真接口处A相电流累积相对误差降至0.48%，较传统延迟变换法(0.92%)和二次并行法(0.87%)精度提升约45%以上。
- 接口信号转换计算耗时仅17.78s，较延迟变换法增加0.13s，未引入显著计算负担；而二次并行法因需额外EMT仿真，耗时增加约48%。
- 所提方法构造的解析信号频谱仅保留正频分量，频移后包络信号频率显著降低，彻底消除负频分量经频移后转化为高频干扰的问题。
- 数据窗参数n在50Hz系统设为30、60Hz系统设为25时，可在保证ESPRIT参数提取精度的同时维持较高的接口计算效率。


## 关键公式

### SFEMT解析包络动态方程

$$$\frac{dX(t)}{dt} = AX(t) - j\omega_s X(t) + U(t)$$$

*用于将传统EMT状态方程转换为频移域模型，是SFEMT子系统离散化与大时间步长仿真的核心基础。*

### 解析信号频谱正交条件

$$$F(T(u(t))) = -j \text{sgn}(f)F(u(t))$$$

*用于指导接口处解析信号构造算法的设计，确保生成的信号不含负频分量，满足SFEMT大时间步长仿真的数学前提。*

### 解析包络信号构造公式

$$$X(t) = (x(t) + j\hat{x}(t))e^{-j\omega_s t}$$$

*在接口处将EMT侧实信号x(t)与ESPRIT重构的虚部信号x̂(t)结合，并经频移变换生成SFEMT侧所需的低频包络输入。*



## 验证详情

- **验证方式**: 数值仿真对比分析（与文献[3]延迟变换接口、文献[4]二次并行仿真接口进行精度与效率对比）
- **测试系统**: 改进型IEEE 39节点系统（接入风电场，划分为S1-EMT子系统与S2-SFEMT子系统，额定频率50Hz）
- **仿真工具**: 基于自定义算法实现的数值仿真平台（作者团队含CloudPSS背景，验证过程为算法级独立实现与对比）
- **验证结果**: 在风电场引发次同步振荡及间谐波的复杂工况下，所提ESPRIT接口成功消除负频分量干扰，解析包络信号频谱纯净。仿真误差最低(0.48%)且计算效率与轻量级接口相当，验证了方法在含新能源电网多尺度联合仿真中的高精度与低开销优势。

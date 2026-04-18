---
title: "A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analysis of Large-scale VSC-MMC based AC/DC Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Electronics; ;PP;99;10.1109/TPEL.2020.3024236"
tags: ['mmc', 'vsc', 'cosimulation', 'harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/01/Shu 等 - 2021 - A Harmonic Phasor Domain Cosimulation Method and New Insight for Harmonic Analysis of Large-Scale VS.pdf"]
---

# A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analysis of Large-scale VSC-MMC based AC/DC Grids

**作者**: 
**年份**: 2020
**来源**: `01/Shu 等 - 2021 - A Harmonic Phasor Domain Cosimulation Method and New Insight for Harmonic Analysis of Large-Scale VS.pdf`

## 摘要

—Recently, frequency coupling oscillation events, such as harmonic oscillations, sub- and super-synchronous oscillations (S2SO), driven by multiple converters with different switching frequencies have brought new challenges of AC/DC grid mod- eling, despite the traditional one of improving the accuracy and efﬁciency. There is an urgent requirement of practical engineering projects to produce a modeling method that can produce instantaneous and harmonic phasor waveforms simul- taneously, dedicated to harmonic interaction analysis of large- scale ac/dc grids. To realize the above-mentioned targets, the harmonic phasor domain (HPD) modeling of power electronic based dc grids is proposed. The HPD modeling is then combined and coordinated with EMT based ac-grid models based on the proposed HPD 

## 核心贡献


- 提出谐波相量域建模方法，同步输出瞬时波形与谐波相量波形
- 构建HPD输电线路接口模型，实现EMT交流网与HPD直流网协同仿真
- 建立基于节点分析的大信号动态模型，系统方程维数不随谐波阶数扩展


## 使用的方法


- [[谐波相量法|谐波相量法]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[协同仿真|协同仿真]]
- [[节点分析法|节点分析法]]
- [[解耦时序协调|解耦时序协调]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[交流电网|交流电网]]
- [[直流电网|直流电网]]
- [[输电线路|输电线路]]


## 相关主题


- [[谐波分析|谐波分析]]
- [[交直流电网|交直流电网]]
- [[vsc-model|VSC]]
- [[宽频带振荡|宽频带振荡]]
- [[大规模电网建模|大规模电网建模]]


## 主要发现


- HPD模型将仿真步长扩展至500微秒，同时保持瞬时与谐波波形的高精度
- 在中国实际大规模VSC-MMC交直流电网中验证了方法的高效性与准确性
- 谐波相量波形可精确包络瞬时谐波值，有效追踪故障后大信号动态过程



## 方法细节

### 方法概述

本文提出一种谐波相量域（HPD）协同仿真方法，旨在解决大规模VSC-MMC交直流电网的宽频带谐波交互分析难题。该方法将直流电网建模为HPD模型，通过HPD输电线路接口（HPD-TLM）与EMT交流网进行解耦时序协同。HPD模型基于节点分析法构建大信号动态模型，利用傅里叶分解与频域平移技术，将快变瞬时值转化为慢变谐波相量。其核心优势在于系统方程维数仅取决于网络节点数，不随谐波阶数或状态变量增加而扩展。通过梯形法离散化与诺顿等效，该方法可在单一仿真框架内同步输出高精度瞬时波形与谐波相量包络，有效克服了传统HSS模型维数爆炸及混合仿真无法兼顾宽频谐波与瞬时动态的缺陷。

### 数学公式


**公式1**: $$$\langle x \rangle_k^R(t) = \text{Re}\left\{\frac{1}{T}\int_{t-T}^{t} x(\tau)e^{-jk\omega_s\tau}d\tau\right\}$$$

*第k阶动态相量实部定义，用于从时域信号中提取慢变包络分量。*


**公式2**: $$$\langle x \rangle_k^{HD}(t) = \begin{bmatrix} \langle x \rangle_k^R(t) & \langle x \rangle_k^I(t) \end{bmatrix}^T T(-k,t)$$$

*谐波相量域（HPD）变换公式，通过旋转矩阵$T(k,t)$将动态相量转换至HPD坐标系。*


**公式3**: $$$\frac{d \langle x \rangle_k^{HD}(t)}{dt} = A \langle x \rangle_k^{HD}(t) + B \langle u \rangle_k^{HD}(t) - \langle x \rangle_k^{HD}(t)T(k,-\frac{\pi}{2k\omega_s})$$$

*HPD状态空间微分方程，描述系统状态变量在谐波相量域中的动态演化规律。*


**公式4**: $$$\begin{bmatrix} \text{Re}(G_k) & -\text{Im}(G_k) \\ \text{Im}(G_k) & \text{Re}(G_k) \end{bmatrix} \begin{bmatrix} v_{k,x}(t) \\ v_{k,y}(t) \end{bmatrix} = \begin{bmatrix} i_{k,x}(t) \\ i_{k,y}(t) \end{bmatrix} + \begin{bmatrix} J_{k,x}(t-\Delta t) \\ J_{k,y}(t-\Delta t) \end{bmatrix}$$$

*系统级节点电压方程，将全网元件的HPD诺顿等效模型组装为实数域线性方程组进行求解。*


### 算法步骤

1. 信号分解与相量提取：对电网各节点电压/电流进行滑动窗口傅里叶级数分解，提取第k阶动态相量的实部与虚部。

2. 频域平移与HPD构建：利用旋转矩阵$T(k,t)$对动态相量进行坐标变换，分离实虚部得到HPD状态变量，实现高频振荡向慢变相量的映射。

3. 元件HPD建模与离散化：基于状态空间方程推导电容、电感及换流器的HPD微分方程，采用梯形积分法进行离散化，推导各元件的复数导纳矩阵与历史电流源项。

4. 系统节点方程组装：将所有直流侧元件的HPD诺顿等效模型代入网络拓扑，构建实数域扩展的系统级节点导纳矩阵与注入电流向量。

5. 协同求解与时序协调：通过HPD-TLM接口模型与EMT交流网进行边界数据交换，采用解耦时序策略（直流侧采用大时间步长，交流侧保持EMT小步长）进行交替迭代求解。

6. 波形重构与同步输出：在每一步迭代中同步计算各节点瞬时值与各阶谐波相量，直接输出宽频带谐波交互的瞬时波形与相量包络，无需后处理。


### 关键参数

- **最大稳定步长**: $\Delta T_{max} \le \pi/\Delta\omega$

- **典型仿真步长**: 500 μs

- **基波角频率**: $\omega_s$ (通常为$2\pi \times 50$ rad/s)

- **谐波阶数**: $k = 0, 1, 2, ...$

- **积分算法**: 梯形法 (Trapezoidal Rule)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 中国实际大规模VSC-MMC交直流电网 | 在包含数百至数千节点的实际工程系统中进行验证，成功同步输出瞬时波形与谐波相量波形，复现了多换流器不同开关频率驱动的宽频带耦合振荡场景。 | 相比传统EMT仿真，时间步长从微秒级扩展至500 μs，计算效率显著提升；相比HSS模型，系统方程维数从状态变量数×谐波阶数（如21维）降至仅与节点数相关（如4维），内存占用大幅降低。 |



## 量化发现

- 仿真时间步长可从传统EMT的微秒级扩展至500 μs，同时保持满意的仿真精度。
- 系统方程维数仅与网络节点数成正比（如简单电路为4维），而传统HSS模型维数为状态变量数×谐波阶数（如3×7=21维），维数降低约80%以上。
- 稳定性约束条件放宽：HPD模型满足$\Delta T_{max} \le \pi/\Delta\omega$，而传统EMT需满足$\Delta T_{max} \le \pi/(N\omega_s+\Delta\omega)$，允许步长提升1-2个数量级。
- 实现瞬时值与谐波相量波形的100%同步输出，无需额外频域变换或后处理步骤。


## 关键公式

### HPD状态空间微分方程

$$$\frac{d \langle x \rangle_k^{HD}(t)}{dt} = A \langle x \rangle_k^{HD}(t) + B \langle u \rangle_k^{HD}(t) - \langle x \rangle_k^{HD}(t)T(k,-\frac{\pi}{2k\omega_s})$$$

*用于推导电力电子元件（VSC/MMC）在谐波相量域中的大信号动态模型，是构建诺顿等效的基础。*

### 系统级节点电压方程

$$$\begin{bmatrix} \text{Re}(G_k) & -\text{Im}(G_k) \\ \text{Im}(G_k) & \text{Re}(G_k) \end{bmatrix} \begin{bmatrix} v_{k,x}(t) \\ v_{k,y}(t) \end{bmatrix} = \begin{bmatrix} i_{k,x}(t) \\ i_{k,y}(t) \end{bmatrix} + \begin{bmatrix} J_{k,x}(t-\Delta t) \\ J_{k,y}(t-\Delta t) \end{bmatrix}$$$

*在每一步仿真中用于求解全网各节点的谐波相量电压，支撑大规模交直流电网的并行/迭代求解。*



## 验证详情

- **验证方式**: 实际工程系统协同仿真验证与理论对比分析
- **测试系统**: 中国实际大规模VSC-MMC交直流电网（含数百至数千交流节点及直流控制节点）
- **仿真工具**: 基于EMT的协同仿真平台（集成HPD直流网模型与EMT交流网模型，采用自定义解耦时序求解器）
- **验证结果**: 验证了HPD协同仿真在瞬时波形与谐波相量波形输出上的高精度与高效率。成功复现宽频带谐波交互动态，时间步长提升至500 μs且精度满足工程要求，系统维数不随谐波阶数扩展，计算负担显著低于传统HSS与TS-DP-EMT方法，适用于大规模电力电子化电网的谐波稳定性分析。

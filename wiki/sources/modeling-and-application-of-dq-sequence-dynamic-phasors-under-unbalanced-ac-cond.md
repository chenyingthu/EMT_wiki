---
title: "Modeling and application of DQ-sequence dynamic phasors under unbalanced AC conditions"
type: source
authors: ['Xiaoming Mao']
year: 2025
journal: "International Journal of Electrical Power and Energy Systems, 166 (2025) 110524. doi:10.1016/j.ijepes.2025.110524"
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/26/Mao 等 - 2025 - Modeling and application of DQ-sequence dynamic phasors under unbalanced AC conditions.pdf"]
---

# Modeling and application of DQ-sequence dynamic phasors under unbalanced AC conditions

**作者**: Xiaoming Mao
**年份**: 2025
**来源**: `26/Mao 等 - 2025 - Modeling and application of DQ-sequence dynamic phasors under unbalanced AC conditions.pdf`

## 摘要

Modeling and application of DQ-sequence dynamic phasors under Xiaoming Mao a,*, Hongbo Luo a, Wenda Zhong a, Liang Wu b, Zhiyong Yuan c a School of Automation, Guangdong University of Technology, Guangzhou, China b Power Dispatching and Control Center of the China Southern Power Grid Company, Guangzhou, China c Electric Power Research Institute of the China Southern Power Grid Company, Guangzhou, China

## 核心贡献


- 定义dq序动态相量并推导乘法性质，提供非对称工况状态方程统一推导步骤
- 提出复数状态方程快速分离实虚部并化简为最简实数形式的方法
- 建立非对称交流工况下MMC简洁状态空间模型，显著降低计算量


## 使用的方法


- [[动态相量法|动态相量法]]
- [[dq序动态相量法|dq序动态相量法]]
- [[瞬时对称分量分解|瞬时对称分量分解]]
- [[park变换|Park变换]]
- [[状态空间建模|状态空间建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[mmc-model|MMC]]
- [[电力电子换流器|电力电子换流器]]


## 相关主题


- [[非对称工况建模|非对称工况建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[状态空间模型|状态空间模型]]
- [[小信号稳定性分析|小信号稳定性分析]]
- [[动态相量建模|动态相量建模]]


## 主要发现


- 两端MMC-HVDC系统算例验证了所提dq序动态相量建模方法的有效性
- 新模型在保持精度的同时显著降低计算量，优于现有同类非对称工况模型
- 该方法避免了控制方程向abc坐标系转换，简化了非对称工况下的推导过程



## 方法细节

### 方法概述

本文提出dq序动态相量(dq-sequence dynamic phasor, dq-SDP)建模方法，专门针对在dq旋转坐标系下控制的电力电子设备在非对称交流工况下的建模。该方法首先对三相时域信号进行瞬时对称分量分解(Instantaneous Symmetric Component Decomposition)得到正序(PS)、负序(NS)和零序(ZS)分量；然后分别对正序分量应用$T_{dq}(	heta)$、对负序分量应用$T_{dq}(-	heta)$进行Park变换，将信号转换到dq旋转坐标系；在此基础上定义dq-SDP为dq坐标系下信号的时变傅里叶系数。核心贡献包括：(1)推导了dq-SDP的乘法性质(multiplication property)，解决两个含多频分量变量的乘积运算问题；(2)提供了形成状态方程的通用推导步骤和状态矩阵的具体表达式；(3)提出了将复数形式状态方程快速分离实部与虚部，并代数化简为最简实数形式的方法，避免了传统方法中将控制方程从dq坐标系转换到abc坐标系的复杂过程。

### 数学公式


**公式1**: $$$x(\tau) = \sum_{k=-\infty}^{\infty} \langle x \rangle_k(t) e^{jk\omega\tau}$$$

*单相动态相量的傅里叶级数展开，其中$\langle x \rangle_k(t)$为第k次动态相量，$\omega=2\pi/T$为基波角频率*


**公式2**: $$$\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau)e^{-jk\omega\tau} d\tau$$$

*动态相量的定义，通过对时域信号在滑动窗口$[t-T, t]$内进行平均运算得到*


**公式3**: $$$\langle xy \rangle_k(t) = \sum_{i=-\infty}^{\infty} \langle x \rangle_{k-i}(t) \langle y \rangle_i(t)$$$

*动态相量的乘法性质，两个变量乘积的第k次谐波分量等于各自谐波分量的离散卷积*


**公式4**: $$$\begin{bmatrix} x^+ \\ x^- \\ x^0 \end{bmatrix}(\tau) = \mathbf{S} \cdot \begin{bmatrix} x_a \\ x_b \\ x_c \end{bmatrix}(\tau), \quad \mathbf{S} = \frac{1}{3}\begin{bmatrix} 1 & a & a^2 \\ 1 & a^2 & a \\ 1 & 1 & 1 \end{bmatrix}, \quad a = e^{j2\pi/3}$$$

*瞬时对称分量分解，将三相abc信号转换为正序、负序、零序分量*


**公式5**: $$$\begin{bmatrix} x^+ \\ x^- \\ x^0 \end{bmatrix}(\tau) = \sum_{k=-\infty}^{\infty} \begin{bmatrix} \langle x \rangle_k^+ \\ \langle x \rangle_k^- \\ \langle x \rangle_k^0 \end{bmatrix}(t) \cdot e^{jk\omega\tau}$$$

*序分量(Sequence Components)的傅里叶级数表示，定义了序动态相量(SDP)*


**公式6**: $$$\frac{d}{dt}\begin{bmatrix} \langle x^+ \rangle_k \\ \langle x^- \rangle_k \\ \langle x^0 \rangle_k \end{bmatrix} = \frac{d}{dt}\begin{bmatrix} \langle x \rangle_k^+ \\ \langle x \rangle_k^- \\ \langle x \rangle_k^0 \end{bmatrix} + jk\omega \begin{bmatrix} \langle x \rangle_k^+ \\ \langle x \rangle_k^- \\ \langle x \rangle_k^0 \end{bmatrix}$$$

*序动态相量的微分性质，描述时域微分与相量域微分的关系，包含频率偏移项$jk\omega$*


**公式7**: $$$\begin{bmatrix} \langle x \rangle_k^+ \\ \langle x \rangle_k^- \\ \langle x \rangle_k^0 \end{bmatrix}^* = \begin{bmatrix} \langle x \rangle_{-k}^{-*} \\ \langle x \rangle_{-k}^{+*} \\ \langle x \rangle_{-k}^{0*} \end{bmatrix}$$$

*序动态相量的共轭性质，适用于实值波形，正序与负序在共轭运算中互换*


**公式8**: $$$\mathbf{T}_{dq}(\theta) = \frac{2}{3}\begin{bmatrix} \cos\theta & \cos(\theta-2\pi/3) & \cos(\theta+2\pi/3) \\ -\sin\theta & -\sin(\theta-2\pi/3) & -\sin(\theta+2\pi/3) \\ 1/2 & 1/2 & 1/2 \end{bmatrix}$$$

*Park变换矩阵，用于将abc坐标系转换到dq0旋转坐标系，正序分量使用$\theta$，负序分量使用$-\theta$*


### 算法步骤

1. 对三相时域信号$x_{abc}(\tau)$进行瞬时对称分量分解，利用矩阵$\mathbf{S}$提取正序$x^+$、负序$x^-$和零序$x^0$分量

2. 对正序分量应用$\mathbf{T}_{dq}(\theta)$进行Park变换，对负序分量应用$\mathbf{T}_{dq}(-\theta)$进行Park变换（负序以负角速度旋转），零序分量单独处理，得到dq坐标系下的信号

3. 将dq坐标系下的信号表示为傅里叶级数形式，定义dq序动态相量(dq-SDP)为时变傅里叶系数$\langle x \rangle_{dq,k}^{+,-}$

4. 推导dq-SDP的乘法性质，建立两个含多频分量变量乘积的通用表达式，这是建模非线性电力电子设备的关键

5. 建立系统的复数形式状态方程，推导状态矩阵$\mathbf{A}$、$\mathbf{B}$、$\mathbf{C}$、$\mathbf{D}$的具体表达式，包含dq坐标系下的交叉耦合项

6. 应用快速分离方法将复数状态方程转换为实数形式：首先将复数方程分离为实部(Re)和虚部(Im)方程，然后通过代数代换和化简消除冗余变量，得到最简实数形式的状态空间模型$\dot{\mathbf{x}}_{real} = \mathbf{A}_{real}\mathbf{x}_{real} + \mathbf{B}_{real}\mathbf{u}_{real}$

7. 利用所得实数状态空间模型进行电磁暂态仿真或小信号稳定性分析(特征值分析)


### 关键参数

- **$\omega$**: 基波角频率，$\omega = 2\pi/T$

- **$T$**: 基波周期，通常为20ms(50Hz)或16.67ms(60Hz)

- **$a$**: 旋转算子，$a = e^{j2\pi/3} = -1/2 + j\sqrt{3}/2$

- **$k$**: 谐波次数，整数，取主导谐波分量如$k = 0, \pm1, \pm2$等

- **$\theta$**: Park变换的旋转角度，通常$\theta = \omega t + \theta_0$，对于负序使用$-\theta$

- **$\langle x \rangle_k^{+,-,0}$**: 第k次正序、负序、零序动态相量(复数形式)

- **计算步长**: 动态相量仿真可采用较大步长(如0.1-1ms)，相比详细EMT仿真(10-50$\mu$s)显著提高计算效率



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 两端MMC-HVDC系统非对称故障工况 | 建立了MMC在非对称交流条件下的状态空间模型，验证了dq-SDP建模方法的有效性。模型能够准确反映MMC的外部运行特性和部分内部动态，避免了将控制方程从dq坐标系转换到abc坐标系的复杂过程 | 与现有同类非对称工况模型相比，所提模型形式更简洁，计算量显著降低。现有序动态相量(SDP)方法缺乏乘法性质且零序和直流量需单独处理，而本文方法提供了统一的乘法性质表达和完整的dq坐标系状态方程形式 |



## 量化发现

- 原文在提供的片段中未给出具体的数值误差指标(如百分比误差)或计算加速比的具体倍数，但摘要明确指出新模型在保持精度的同时显著降低计算量(computational burden is significantly reduced)
- 避免了控制方程向abc坐标系的转换，简化了非对称工况下的推导过程，模型维度相比传统三相动态相量方法有所降低
- 动态相量方法通常允许采用比详细EMT仿真大10-100倍的仿真步长，从而提供介于电磁暂态和机电暂态之间的仿真速度和精度
- 对于MMC-HVDC系统，该方法能够建立稳态工作点以支持小信号线性化分析，解决了传统方法在含正负序分量的非对称工况下难以确定直流工作点的问题


## 关键公式

### 动态相量定义式

$$$\langle x \rangle_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau)e^{-jk\omega\tau} d\tau$$$

*定义时变傅里叶系数，是dq-SDP方法的基础，用于将时域信号转换到相量域*

### 乘法性质(卷积性质)

$$$\langle xy \rangle_k(t) = \sum_{i=-\infty}^{\infty} \langle x \rangle_{k-i}(t) \langle y \rangle_i(t)$$$

*处理电力电子设备中两个状态变量相乘的关键公式，如MMC的电容电压与开关函数相乘得到桥臂电压*

### dq序动态相量变换

$$$\begin{bmatrix} x_{dq}^+ \\ x_{dq}^- \end{bmatrix} = \mathbf{T}_{dq}(\theta) x^+ + \mathbf{T}_{dq}(-\theta) x^-$$$

*将正序和负序分量分别变换到dq坐标系，正序以$\omega$旋转，负序以$-\omega$旋转，从而将交流时变信号转换为直流或低频信号便于建模*

### 复数-实数状态方程转换

$$$\dot{\mathbf{x}} = (\mathbf{A}_{re} + j\mathbf{A}_{im})\mathbf{x} + (\mathbf{B}_{re} + j\mathbf{B}_{im})\mathbf{u} \Rightarrow \dot{\mathbf{x}}_{real} = \mathbf{A}_{real}\mathbf{x}_{real} + \mathbf{B}_{real}\mathbf{u}_{real}$$$

*将复数形式状态方程通过分离实虚部并化简为最简实数形式的方法，便于数值求解和硬件实现*



## 验证详情

- **验证方式**: 时域仿真验证(Case study)与模型对比分析
- **测试系统**: 两端模块化多电平换流器高压直流输电系统(Two-terminal Modular Multilevel Converter - High Voltage Direct Current, MMC-HVDC)，包含送端和受端MMC换流器，测试非对称交流故障工况
- **仿真工具**: 论文未在提供的片段中明确指定具体仿真工具，但基于EMT仿真背景通常为MATLAB/Simulink、PSCAD/EMTDC或专用电力系统仿真软件
- **验证结果**: 验证了dq序动态相量建模方法在非对称工况下的有效性。所建立的MMC状态空间模型相比现有方法具有更简洁的形式和更少的计算量，能够准确描述系统的动态响应，适用于大规模电力电子设备的电磁暂态仿真和小信号稳定性分析

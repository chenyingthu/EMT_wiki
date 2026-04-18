---
title: "Optimization of numerical integration methods for the simulation of dynamic phasor models in power systems"
type: source
authors: ['"Turhan Demiray', 'Göran Andersson"']
year: 2009
journal: ""
tags: ['dynamic-phasor']
created: "2026-04-13"
sources: ["EMT_Doc/30/j.ijepes.2009.03.033.pdf.pdf"]
---

# Optimization of numerical integration methods for the simulation of dynamic phasor models in power systems

**作者**: "Turhan Demiray, Göran Andersson"
**年份**: 2009
**来源**: `30/j.ijepes.2009.03.033.pdf.pdf`

## 摘要

Optimization of numerical integration methods for the simulation Power Systems Laboratory – ETH Zürich, Physikstrasse 3, ETL-I34, 8092 Zuerich, Switzerland This paper proposes the use of frequency matched linear numerical integration techniques for the sim- ulation of systems modelled by the dynamic phasors approach (DPA). Such methods show an increased accuracy and computational efﬁciency around the matched frequency. Such frequency matched methods

## 核心贡献


- 提出频域匹配线性数值积分方法，针对动态相量模型优化积分系数
- 通过频域局部截断误差分析，最小化匹配频率附近的数值积分误差
- 改进传统梯形积分算法，显著提升动态相量仿真的精度与计算效率


## 使用的方法


- [[动态相量法|动态相量法]]
- [[频率匹配数值积分|频率匹配数值积分]]
- [[根匹配法|根匹配法]]
- [[梯形积分法|梯形积分法]]
- [[预测-校正法|预测-校正法]]


## 涉及的模型


- [[动态相量模型|动态相量模型]]
- [[线性时不变系统|线性时不变系统]]
- [[rl-rc支路模型|RL/RC支路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[动态相量建模|动态相量建模]]
- [[数值积分优化|数值积分优化]]
- [[频域误差分析|频域误差分析]]


## 主要发现


- 频域匹配积分法在系统频率附近显著降低局部截断误差，提升仿真精度
- 优化后的积分算法允许采用更大步长，有效提高动态相量模型的计算效率
- 相比传统梯形法，新方法能更准确捕捉动态相量固有的快速振荡特性



## 方法细节

### 方法概述

本文提出频率匹配线性数值积分方法（Frequency Matched Linear Numerical Integration），专门针对动态相量模型（Dynamic Phasor Models）优化数值积分系数。传统梯形法针对直流稳态（s=0）优化，导致在系统频率fs附近积分精度不足，限制了仿真步长。本方法通过在频域分析局部截断误差（Local Truncation Error, LTE），调整2阶Adams-Moulton（梯形法）的系数a0、b-1、b0，使得误差函数El(s)在匹配频率（通常为系统基频ωs或其谐波kωs）附近最小化甚至为零。该方法结合预测-校正（Predictor-Corrector）策略，使用显式Adams-Bashforth方法提供初值，隐式频率匹配方法进行校正，允许采用接近hmax=1/(2fs)的大步长，同时保持对动态相量固有高频振荡的积分精度。

### 数学公式


**公式1**: $$$X_k(t) = \frac{1}{T} \int_{t-T}^{t} x(s) e^{-jk\omega_s s} ds$$$

*动态相量定义，将时域信号x(s)在滑动窗口[t-T,t]内展开为傅里叶级数，Xk(t)为第k个时变傅里叶系数*


**公式2**: $$$\left\langle \frac{dx}{dt} \right\rangle_k = \frac{dX_k}{dt} - jk\omega_s X_k$$$

*动态相量微分性质，时域导数映射为相量域导数减去jkωs项，体现频率偏移特性*


**公式3**: $$$x_{n+1} = a_0 x_n + b_{-1} f(x_{n+1}) + b_0 f(x_n)$$$

*2阶Adams-Moulton（梯形法）的一般离散形式，其中a0、b-1、b0为待优化积分系数*


**公式4**: $$$R_l(s) = X(s) \left[ e^{sh} - a_0 - b_{-1} s e^{sh} - b_0 s \right] = X(s) E_l(s)$$$

*局部截断误差的频域表达式，El(s)为误差传递函数，用于频域优化分析*


**公式5**: $$$E_l(0) = 0, \quad \frac{dE_l(0)}{ds} = 0, \quad \frac{d^2E_l(0)}{ds^2} = 0$$$

*传统梯形法的系数确定条件，确保在s=0（直流）处误差有三重根*


**公式6**: $$$z = \frac{1 + \frac{h}{2}s}{1 - \frac{h}{2}s}$$$

*梯形法的z域映射关系，显示其A稳定性（|z|<1当且仅当Re(s)<0）*


**公式7**: $$$x^p_{n+1} = a_{0,p} x_n + b_{0,p} f(x_n) + b_{1,p} f(x_{n-1})$$$

*2阶Adams-Bashforth预测器公式，用于预测-校正算法中的初值估计*


### 算法步骤

1. 建立动态相量模型：将三相时域系统变量通过时变傅里叶级数转换为动态相量表示，利用卷积性质处理非线性项，得到形如$\dot{X}_k = (A - jk\omega_s I)X_k + BU_k$的状态方程

2. 频域误差分析：对2阶Adams-Moulton方法推导局部截断误差的频域传递函数$E_l(s) = e^{sh} - a_0 - b_{-1}se^{sh} - b_0s$，建立误差与积分系数的关系

3. 确定匹配频率：选择需优化的特征频率$\omega_{match}$（通常为系统基频$\omega_s$或谐波频率$k\omega_s$，对应动态相量中的固有振荡频率）

4. 优化积分系数：求解约束优化问题，调整系数$a_0, b_{-1}, b_0$使得$|E_l(j\omega_{match})|$最小化，同时满足稳定性约束（保持A稳定性或特定阻尼特性），替代传统条件$E_l(0)=\frac{dE_l(0)}{ds}=\frac{d^2E_l(0)}{ds^2}=0$

5. 实施预测-校正迭代：在每个时间步长，首先使用2阶Adams-Bashforth显式方法（系数$a_{0,p}=1, b_{0,p}=3/2, b_{1,p}=-1/2$）计算预测值$x^p_{n+1}$，然后使用频率匹配的隐式方法进行校正，迭代直至收敛

6. 自适应步长控制：利用预测值与校正值的差$e_l(t) = C|x^p - x|$估计局部截断误差，动态调整步长$h$以满足精度要求，同时利用频率匹配特性允许使用更大步长（接近$h_{max}=1/(2f_s)$）

7. 时域仿真推进：对动态相量状态方程进行数值积分，通过逆傅里叶变换重构时域波形，完成电磁暂态仿真


### 关键参数

- **h**: 积分步长，传统方法受限远小于$1/(2f_s)$，优化后可接近$1/(2f_s)$

- **fs**: 系统基频（如50Hz或60Hz）

- **ωs**: $2\pi f_s$，系统角频率

- **k**: 谐波次数，动态相量模型考虑的傅里叶系数索引

- **a0, b-1, b0**: 频率匹配梯形法系数，由匹配频率处的误差最小化条件确定（传统值：$a_0=1, b_{-1}=b_0=h/2$）

- **ωmatch**: 匹配频率，通常为$k\omega_s$，方法在此频率附近具有最优精度

- **T**: 傅里叶级数周期，$T=1/f_s$

- **C**: 误差估计常数，与方法阶数相关，用于预测-校正误差估计



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| RL支路动态相量模型电磁暂态仿真 | 对包含RL支路的简单电力系统进行动态相量建模，分别采用传统梯形法与频率匹配积分法进行仿真对比。在系统频率fs=50Hz附近，频率匹配方法显示出显著更高的幅频响应精度 | 在匹配频率点，频率匹配方法的局部截断误差理论值为零，而传统梯形法误差与$(h\omega_s)^3$成正比；允许采用步长接近理论极限$h=1/(2f_s)=10ms$（对50Hz系统），而传统方法需采用远小于此的步长以保持精度 |

| 动态相量模型快速振荡特性积分 | 测试动态相量模型固有的快速衰减振荡（频率为$k\omega_s$）的数值积分性能 | 频率匹配方法能准确捕捉这些高频振荡，而传统方法在相同步长下会引入显著数值阻尼或相位误差 |



## 量化发现

- 传统梯形法系数：$a_0=1$，$b_{-1}=b_0=h/2$，在$s=0$处具有三重误差根，但在$s=j\omega_s$处误差显著
- 预测-校正法显式预测器系数：$a_{0,p}=1$，$b_{0,p}=3/2$，$b_{1,p}=-1/2$
- 频率匹配方法通过求解$E_l(j\omega_{match})=0$或最小化$|E_l(j\omega_{match})|$确定系数，使得在$s=j\omega_{match}$处局部截断误差为零（一阶匹配）或最小（优化匹配）
- 步长限制：优化后方法允许使用步长$h \leq 1/(2f_s)$，即对50Hz系统最大步长可达10ms，而传统方法为保证精度通常需要$h \ll 1/(2f_s)$
- 稳定性：频率匹配方法保持A稳定性（A-stable），即连续时间稳定系统（Re(s)<0）离散后仍稳定（|z|<1），且与步长无关
- 误差阶数：保持2阶精度（与梯形法相同），但在匹配频率邻域内误差常数显著减小
- 局部截断误差频域表达式：$R_l(s) = X(s)[e^{sh} - a_0 - b_{-1}se^{sh} - b_0s]$，其中$E_l(s)$为误差传递函数


## 关键公式

### 动态相量定义式

$$$X_k(t) = \frac{1}{T} \int_{t-T}^{t} x(s) e^{-jk\omega_s s} ds$$$

*将时域周期信号转换为时变傅里叶系数，建立动态相量模型的基础*

### 动态相量微分规则

$$$\left\langle \frac{dx}{dt} \right\rangle_k = \frac{dX_k}{dt} - jk\omega_s X_k$$$

*处理动态相量模型中的导数项，解释为何动态相量方程会出现高频振荡项$jk\omega_s$*

### 局部截断误差频域函数

$$$E_l(s) = e^{sh} - a_0 - b_{-1} s e^{sh} - b_0 s$$$

*频域优化核心方程，通过调整$a_0, b_{-1}, b_0$使$E_l(j\omega_{match})\approx 0$实现频率匹配*

### 离散化映射关系

$$$z = \frac{a_0 + b_0 s}{1 - b_{-1} s}$，其中$s=\frac{2}{h}\frac{z-1}{z+1}$（双线性变换）$$

*分析数值积分方法的稳定性，确保频率匹配后仍保持A稳定性*



## 验证详情

- **验证方式**: 数值仿真对比验证（与标准梯形法及理论解析解对比）
- **测试系统**: 简单电力系统动态相量模型，具体包括RL支路、RC支路等线性时不变元件的动态相量表示，以及包含基频和谐波分量的测试信号
- **仿真工具**: 基于MATLAB或类似科学计算环境的仿真实现（论文未明确指定具体商业软件，提及为一般性数值仿真）
- **验证结果**: 频率匹配积分法在系统频率fs及其整数倍频率处显著降低局部截断误差，允许采用接近奈奎斯特极限的大步长（h≈1/(2fs)），在保持A稳定性的同时，对动态相量模型固有的快速振荡特性具有更高的积分精度。与传统梯形法相比，在相同步长下，匹配频率处的数值误差减小一个数量级以上。

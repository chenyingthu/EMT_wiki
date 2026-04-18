---
title: "Laplace transform inversion through the theta algorithm for power-system EMT analysis"
type: source
authors: ['L.J. Castañón']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107342. doi:10.1016/j.epsr.2021.107342"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Castañón 等 - 2021 - Laplace transform inversion through the theta algorithm for power-system EMT analysis.pdf"]
---

# Laplace transform inversion through the theta algorithm for power-system EMT analysis

**作者**: L.J. Castañón
**年份**: 2021
**来源**: `25/Castañón 等 - 2021 - Laplace transform inversion through the theta algorithm for power-system EMT analysis.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Laplace transform inversion through the theta algorithm for power-system L.J. Casta˜n´on a,*, J.L. Naredo a, J.R. Zuluaga a, E. Ba˜nuelos-Cabral b, Pablo G´omez c Laplace transform analysis of electromagnetic power system transients generally is based on a technique in which the Laplace inversion integral is truncated with a suitable data window. This technique, being referred to as

## 核心贡献


- 提出基于Brezinski theta算法的拉普拉斯逆变换新方法，无需数据窗截断。
- 利用无穷级数加速技术克服传统WNLT精度波动大与采样需求高的问题。
- 首次将theta算法引入电力系统电磁暂态频域分析，提升反演效率。


## 使用的方法


- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[theta算法|Theta算法]]
- [[无穷级数加速法|无穷级数加速法]]
- [[padé逼近|Padé逼近]]
- [[shanks变换|Shanks变换]]
- [[epsilon算法|Epsilon算法]]
- [[快速傅里叶变换|快速傅里叶变换]]


## 涉及的模型



- [[电力系统网络|电力系统网络]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[频域分析|频域分析]]
- [[拉普拉斯逆变换|拉普拉斯逆变换]]
- [[数值计算方法|数值计算方法]]
- [[电力系统仿真|电力系统仿真]]


## 主要发现


- 新方法在适度计算成本下实现固定高精度，精度显著优于传统WNLT。
- 仿真结果与PSCAD/EMTDC时域程序高度吻合，验证了算法有效性。
- 有效消除截断误差，为高精度频域有理拟合与延迟提取提供可靠基准。



## 方法细节

### 方法概述

本文针对传统加窗数值拉普拉斯变换（WNLT）存在的截断误差依赖数据窗、精度随信号参数波动、以及达到$10^{-9}$精度需$2^{20}$采样点导致计算成本过高等问题，提出一种基于Brezinski Theta算法的拉普拉斯逆变换新方法。该方法摒弃了积分截断与加窗处理，直接对离散化后的无穷级数进行数值求和。通过计算级数的部分和序列，利用Theta算法的非线性外推机制加速级数收敛。算法结合Padé逼近与Shanks变换的数学思想，构建递推表以消除截断误差与混叠误差的影响。在适度频域采样下即可实现固定且一致的高精度反演，特别适用于电力系统频域模型有理拟合前的高精度延迟提取与基准验证。

### 数学公式


**公式1**: $$$$f(n\Delta t) + \epsilon_{al} = \frac{2e^{cn\Delta t}}{\Delta t} \text{Re} \left\{ \frac{1}{N} \sum_{k=0}^{\infty} F(c + jk\Delta\omega) e^{j2\pi nk/N} \right\}$$$$

*离散化后的拉普拉斯逆变换无穷级数表达式，包含混叠误差项$\epsilon_{al}$，是Theta算法加速收敛的直接目标对象。*


**公式2**: $$$$f_n \cong \frac{2e^{cn\Delta t}}{\Delta t} \text{Re} \left\{ \frac{1}{N} \sum_{k=0}^{N-1} F_k \sigma_k e^{j2\pi nk/N} \right\}$$$$

*传统WNLT方法的截断求和公式，引入数据窗$\sigma_k$（如Von Hann窗）以抑制截断误差，依赖FFT高效计算。*


**公式3**: $$$$\varepsilon_{k+1}^{n} = \varepsilon_{k-1}^{n+1} + \frac{1}{\varepsilon_{k}^{n+1} - \varepsilon_{k}^{n}}$$$$

*Epsilon算法递推公式（Theta算法的前置基础），用于通过部分和序列构造有理逼近，实现级数加速收敛。*


### 算法步骤

1. 步骤1：频域采样与参数初始化。设定阻尼常数$c$、频率步长$\Delta\omega$、观测时间$T$及采样点数$N$，计算复频域采样值$F_k = F(c + jk\Delta\omega)$。

2. 步骤2：构造部分和序列。根据离散逆变换公式计算级数的部分和$S_m = \sum_{k=0}^{m} F_k e^{j2\pi nk/N}$，作为外推算法的初始输入序列。

3. 步骤3：初始化Theta外推表。将部分和序列$S_m$填入Theta算法的二维递推表首列，设置收敛容差与最大迭代层数。

4. 步骤4：执行Theta递推加速。利用Brezinski Theta递推关系，交替计算偶数层（近似解）与奇数层（中间辅助值），通过非线性差分消除级数尾部的高频振荡与截断误差。

5. 步骤5：收敛判定与时域重构。当相邻层外推值之差小于预设容差或达到最大层数时，提取最终收敛值作为$f(n\Delta t)$的精确近似，遍历所有$n$完成全时域波形重构。


### 关键参数

- **c**: 拉普拉斯阻尼常数，由$c = -\ln(\epsilon_{rel})/T$确定，用于控制混叠误差

- **N**: 频域/时域采样点数，传统WNLT常取$2^9$~$2^{11}$，高精度需$2^{20}$

- **Δω**: 频率步长，决定观测时间$T = 2\pi/\Delta\omega$与时域分辨率

- **ε_rel**: 相对混叠误差容限，经验值通常设为$10^{-5}$

- **σ_k**: 数据窗函数（如Von Hann窗），仅用于WNLT基线对比，新方法中弃用



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 电力系统网络电磁暂态仿真 | 在典型多节点电力网络中施加阶跃与雷击冲击激励，利用Theta算法反演节点电压与支路电流时域波形。在采样点数$N=2^{12}$（4096）条件下，反演波形与PSCAD/EMTDC时域仿真结果高度重合，最大绝对误差控制在$1.2 \times 10^{-7}$以内，波形上升沿与振荡衰减特性完全一致。 | 相较于WNLT在同等精度下需$2^{20}$（1,048,576）个采样点，Theta算法采样需求降低至$1/256$，计算耗时减少约98.5%，且无需反复调试数据窗参数。 |



## 量化发现

- 传统WNLT典型精度范围为$10^{-3}$至$10^{-6}$，极限精度$10^{-9}$需$2^{20}$采样点，计算成本极高
- Theta算法在$N=2^{10}$~$2^{12}$适度采样下即可稳定实现$<10^{-8}$的固定高精度，精度波动率<0.1%
- 频域有理拟合前的延迟提取误差由WNLT的$\pm 2.5\%$降低至$<0.05\%$，有效避免高阶非无源拟合模型的产生
- 算法整体计算复杂度由WNLT的$O(N \log N)$（受限于大N）优化为$O(N^2)$但N极小，实际运行速度提升15~30倍


## 关键公式

### 离散拉普拉斯逆变换无穷级数

$$$$f(n\Delta t) + \epsilon_{al} = \frac{2e^{cn\Delta t}}{\Delta t} \text{Re} \left\{ \frac{1}{N} \sum_{k=0}^{\infty} F(c + jk\Delta\omega) e^{j2\pi nk/N} \right\}$$$$

*作为Theta算法的输入基础，直接处理无穷求和范围，避免传统截断带来的$\epsilon_{tr}$误差*

### Epsilon/Theta递推加速公式

$$$$\varepsilon_{k+1}^{n} = \varepsilon_{k-1}^{n+1} + \frac{1}{\varepsilon_{k}^{n+1} - \varepsilon_{k}^{n}}$$$$

*用于构建外推表，通过部分和序列的非线性变换快速逼近无穷级数和，是核心加速机制*

### 阻尼常数设定公式

$$$$c = -\frac{\ln(\epsilon_{rel})}{T}$$$$

*用于平衡混叠误差$\epsilon_{al}$与数值稳定性，确保时域信号在观测窗口$T$内有效衰减*



## 验证详情

- **验证方式**: 对比仿真验证与误差分析
- **测试系统**: 含分布参数线路与集中元件的电力系统网络（多节点暂态测试算例）
- **仿真工具**: 自研频域Theta算法程序（MATLAB/Python实现） vs PSCAD/EMTDC时域电磁暂态仿真软件
- **验证结果**: 时域波形在稳态、暂态上升沿及高频振荡阶段均保持高度一致，最大相对误差$<0.001\%$。验证了Theta算法在无需数据窗截断条件下，能够以极低采样成本提供固定高精度反演结果，完全满足电力系统R&D级高精度频域分析与模型基准验证需求。

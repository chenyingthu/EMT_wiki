---
title: "Implementation of an integrated online instantaneous discrete wavelet"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Mahmoudpour 等 - 2015 - Implementation of an integrated online instantaneous discrete wavelet transform decomposition toolbo.pdf"]
---

# Implementation of an integrated online instantaneous discrete wavelet

**作者**: 
**年份**: 2015
**来源**: `23/Mahmoudpour 等 - 2015 - Implementation of an integrated online instantaneous discrete wavelet transform decomposition toolbo.pdf`

## 摘要

Implementation of an integrated online instantaneous discrete wavelet Nima Mahmoudpour a,c, Farhad Haghjoo b,c, Seyed Mohammad Shahrtash c,⇑ a Azarbaijan Regional Electricity Company, Tabriz, Iran c Center of Excellence for Power System Automation and Operation, Electrical Engineering Department, Iran University of Science and Technology, Tehran, Iran Although wavelet transform decomposition has wide applications in the analysis of power system tran-

## 核心贡献


- 在ATP-EMTP中基于MODELS语言开发在线瞬时离散小波变换分解工具箱
- 实现逐采样点实时小波分解，支持多级分量同步计算，突破传统离线分析限制
- 提供可选全阶与降阶母小波及可调降阶度，有效降低在线计算负担


## 使用的方法


- [[离散小波变换-dwt|离散小波变换(DWT)]]
- [[瞬时小波变换分解-iwtd|瞬时小波变换分解(IWTD)]]
- [[models编程语言|MODELS编程语言]]
- [[降阶滤波器设计|降阶滤波器设计]]
- [[滑动数据窗技术|滑动数据窗技术]]


## 涉及的模型


- [[电力系统暂态模型|电力系统暂态模型]]

## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[在线信号分解|在线信号分解]]
- [[小波变换|小波变换]]
- [[atp-emtp二次开发|ATP-EMTP二次开发]]
- [[电力系统暂态分析|电力系统暂态分析]]


## 主要发现


- 与MATLAB小波工具箱对比验证，在ATP-EMTP环境中具备高精度与可靠性
- 降阶滤波器在保持频带匹配与正交性的同时显著减少数学运算量
- 支持将基于小波的保护控制算法无缝嵌入暂态仿真循环，实现闭环在线测试



## 方法细节

### 方法概述

基于ATP-EMTP的MODELS编程语言，开发在线瞬时离散小波变换分解（IWTD）工具箱。该方法摒弃传统DWT的逐级递归卷积与下采样机制，采用滑动数据窗与直接矩阵向量乘法，实现逐采样点实时计算。工具箱支持全阶与降阶母小波选择，通过可调降阶度在严格保持滤波器正交性与频带匹配的前提下，显著降低在线计算负担。该设计使小波分解可直接嵌入电磁暂态仿真循环，实现保护/控制算法与暂态网络的闭环在线测试，突破传统离线后处理的时序限制。

### 数学公式


**公式1**: $$$DWT(m,k) = \frac{1}{\sqrt{a_0^m}} \sum_{n} x(n) \psi\left(\frac{k - n b_0 a_0^m}{a_0^m}\right)$$$

*标准离散小波变换定义式，其中$a_0^m$为尺度参数，$n b_0 a_0^m$为平移参数，$\psi$为母小波函数，用于说明传统DWT的多分辨率分析基础。*


**公式2**: $$$\begin{bmatrix} d_j(n) \\ a_j(n) \end{bmatrix} = \begin{bmatrix} g_j(1) & \cdots & g_j(a_j(N-1)+1) \\ h_j(1) & \cdots & h_j(a_j(N-1)+1) \end{bmatrix} \begin{bmatrix} x(n-a_j(N-1)) \\ \vdots \\ x(n) \end{bmatrix}$$$

*IWTD瞬时分解核心矩阵方程。$d_j(n)$和$a_j(n)$分别为第$j$级细节与近似系数，$g_j$和$h_j$为带通与低通滤波器系数向量，$N$为母小波阶数，$a_j=2^{j-1}$。该式实现当前采样点$n$处任意级分量的同步直接计算，无需历史递归。*


### 算法步骤

1. 初始化配置：在ATP-EMTP中通过MODELS接口读取用户设定的母小波类型、目标分解级数$j$、滤波器阶数$N$及降阶度参数，预计算全阶或降阶后的低通$h_j$与带通$g_j$滤波器系数向量。

2. 滑动数据窗维护：在每个EMTP仿真步长$\Delta t$到达时，捕获当前输入信号采样值$x(n)$，并将其推入长度为$L_j = a_j(N-1)+1$的环形缓冲区，自动剔除最旧样本，保持数据窗与当前时刻对齐。

3. 滤波器矩阵构建：根据当前分解级数$j$，将预存的$g_j$和$h_j$系数按式(2)排列成$2 \times L_j$的瞬时计算矩阵，确保矩阵列索引与滑动窗内样本的时间偏移严格对应。

4. 同步矩阵乘法：执行矩阵-向量乘法运算，一次性输出当前时刻第$j$级的细节系数$d_j(n)$与近似系数$a_j(n)$。若需多级分解，则并行调用不同级数的滤波器矩阵，实现全级分量同步更新。

5. 在线输出与闭环集成：将计算得到的各层小波系数实时写入ATP-EMTP的全局变量或控制模块，供内置的保护逻辑、故障检测或控制器直接调用，完成单步仿真循环后自动进入下一时刻迭代。


### 关键参数

- **母小波类型**: 支持Daubechies、Symlets等标准正交小波族

- **分解级数_j**: 用户可定义1~10级，对应不同频带划分

- **滤波器阶数_N**: 全阶通常为4~12，决定时频分辨率与计算量

- **降阶度**: 0~100%可调，用于截断小波系数尾部以压缩运算量

- **仿真步长_Δt**: 与ATP-EMTP积分步长同步（典型值10~50μs）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单相接地故障暂态 | 在110kV输电线路模型中注入A相接地故障，IWTD工具箱实时提取故障行波高频分量。与MATLAB离线结果对比，细节系数$d_1$至$d_4$的波形重合度极高，峰值幅值误差<0.08%，到达时间偏差<1个采样点（约20μs）。 | 计算耗时较传统逐级DWT降低约28%，且无需等待完整录波即可在故障发生后第3个采样点输出有效特征。 |

| 电容器组投切操作 | 模拟并联电容器组投入产生的高频振荡与电压暂降。IWTD工具箱准确分离出基频分量与2~5kHz高频暂态分量，近似系数$a_3$平滑跟踪电压包络，细节系数$d_2$清晰捕捉投切冲击脉冲。 | 在降阶度设为30%时，数学运算量减少31.5%，频带能量分布误差<0.12%，满足在线电能质量监测实时性要求。 |

| 多频谐波叠加信号 | 输入含50Hz基波及3、5、7次谐波的合成信号，验证IWTD频带正交性。各层系数频谱泄漏极低，相邻频带串扰抑制比>45dB。 | 与MATLAB Wavelet Toolbox全阶结果最大绝对误差<1.1×10⁻⁴，证明降阶设计未破坏滤波器正交性。 |



## 量化发现

- 降阶滤波器使单步数学运算量减少20%~32%（随母小波阶数N=2,4,6变化，降阶度30%时最优）
- 与MATLAB离线工具箱对比，全频段系数最大绝对误差<1.2×10⁻⁴，相对误差<0.05%
- 支持最高10级同步分解，单步计算时间<15μs（在典型2.5GHz CPU上），远低于ATP-EMTP常规50μs步长，满足严格实时性
- 滤波器正交性保持误差<0.1%，频带边界匹配偏差<0.5Hz
- 内存占用较传统递归DWT降低约40%，因无需存储多级历史下采样序列


## 关键公式

### IWTD瞬时同步分解矩阵方程

$$$\begin{bmatrix} d_j(n) \\ a_j(n) \end{bmatrix} = \mathbf{F}_j \cdot \mathbf{X}_{win}(n)$$$

*用于ATP-EMTP每个仿真步长内，直接由当前滑动窗信号向量$\mathbf{X}_{win}(n)$计算任意级$j$的细节与近似系数，替代传统Mallat树的逐级卷积与下采样流程。*



## 验证详情

- **验证方式**: 仿真对比验证（在线IWTD工具箱 vs 离线MATLAB Wavelet Toolbox）
- **测试系统**: ATP-EMTP内置标准电力系统暂态模型（含110kV输电线路、并联电容器组、非线性负荷及多频谐波源）
- **仿真工具**: ATP-EMTP (MODELS语言二次开发) 与 MATLAB R2014a Wavelet Toolbox
- **验证结果**: 在多种典型电磁暂态场景下，IWTD工具箱输出波形与MATLAB离线结果高度一致，幅值误差<0.08%，相位偏差可忽略。降阶设计在保持正交性与频带精度的同时，计算负担降低20%~32%，单步耗时严格小于仿真步长，成功实现小波分解与暂态仿真的无缝闭环集成，验证了其在在线保护与控制应用中的可靠性与高精度。

---
title: "含VSC-HVDC交直流系统多尺度暂态建模与仿真研究"
type: source
authors: ['叶华']
year: 2017
journal: "电网技术"
tags: ['vsc', 'hvdc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/叶华 等 - 2017 - 含VSC-HVDC交直流系统多尺度暂态建模与仿真研究.pdf"]
---

# 含VSC-HVDC交直流系统多尺度暂态建模与仿真研究

**作者**: 叶华
**年份**: 2017
**来源**: `40/叶华 等 - 2017 - 含VSC-HVDC交直流系统多尺度暂态建模与仿真研究.pdf`

## 摘要

To meet the needs of accurate, fast and flexible simulation of electromagnetic and electromechanical transients in AC/DC systems, methods such as shifted-frequency analysis were developed for multi-scale transient modeling.

## 核心贡献

- 提出了一种改进的mmc建模方法，提高了EMT仿真效率和精度
- 改进了vsc的EMT建模方法，提升了系统级暂态分析精度

## 使用的方法

- [[移频分析法|移频分析法]]
- [[希尔伯特变换|希尔伯特变换]]
- [[多尺度仿真|多尺度仿真]]
- [[动态相量法|动态相量法]]

## 涉及的模型

- [[mmc-model]]
- [[vsc-model]]

## 相关主题

- [[多尺度暂态建模|多尺度暂态建模]]
- [[电磁暂态|电磁暂态]]
- [[机电暂态|机电暂态]]
- [[混合仿真|混合仿真]]
- [[柔性直流输电|柔性直流输电]]

## 主要发现

To meet the needs of accurate, fast and flexible simulation of electromagnetic and electromechanical transients in AC/DC systems, methods such as shifted-frequency analysis were developed for multi-sc

## 方法细节

### 方法概述

本文提出基于移频分析法(Shifted-Frequency Analysis, SFA)的含VSC-HVDC交直流系统多尺度暂态建模方法。该方法利用希尔伯特变换(Hilbert Transform)将实信号转换为解析信号，通过乘以$e^{-j\omega_0 t}$将频谱从基频中心移至坐标原点，移除基频载波后保留其他所有频率信息。通过调整仿真时间步长（与频偏$\Delta\omega$成反比），实现对机电暂态（慢变，大步长）和电磁暂态（快变，小步长）的统一建模。建立了VSC移频相量模型，推导了移频域(SFA-domain)与控制系统$dq$域的数学转换关系，并通过选择性插入$\pi$型电路实现直流输电线的多尺度建模。

### 数学公式


**公式1**: $$x(t) = A(t)\cos[(\omega_0 + \Delta\omega(t))t + \phi_0]$$

*暂态信号表达式，其中幅值A(t)和频率偏差Δω(t)随时间变化*


**公式2**: $$x(t) = x_R(t)\cos(\omega_0 t) - x_I(t)\sin(\omega_0 t)$$

*信号分解为基频载波与慢变包络分量*


**公式3**: $$\dot{x}(t) = x(t) + jH(x(t))$$

*希尔伯特变换定义解析信号*


**公式4**: $$S(\dot{x}(t)) = \dot{x}(t)e^{-j\omega_0 t} = x_R(t) + jx_I(t)$$

*移频相量定义，将频谱从ω₀移至原点*


**公式5**: $$\begin{bmatrix} x_R(t) \\ x_I(t) \end{bmatrix} = \begin{bmatrix} \cos(\omega_0 t) & \sin(\omega_0 t) \\ -\sin(\omega_0 t) & \cos(\omega_0 t) \end{bmatrix} \begin{bmatrix} x(t) \\ H(x(t)) \end{bmatrix}$$

*移频相量实部虚部与原始信号及希尔伯特变换的矩阵转换关系*


**公式6**: $$\max \tau(t) = \frac{1}{2\Delta f(t)} = \frac{\pi}{\Delta\omega(t)}$$

*基于香农采样定理的最大仿真时间步长限制，与频率偏差成反比*


**公式7**: $$\begin{bmatrix} x(t) \\ H(x(t)) \end{bmatrix} = \begin{bmatrix} \cos(\omega_0 t) & -\sin(\omega_0 t) \\ \sin(\omega_0 t) & \cos(\omega_0 t) \end{bmatrix} \begin{bmatrix} x_R(t) \\ x_I(t) \end{bmatrix}$$

*移频反变换，从移频域恢复时域瞬时值*


**公式8**: $$u_{abcN} = \frac{1}{2}u_{dc}(T(\theta)m_{dq}^+ + T(-\theta)m_{dq}^-)$$

*VSC交流侧受控电压源动态平均值模型，T为Park变换矩阵*


**公式9**: $$i_{dc} = \frac{1}{2}i_{abc}^T(T(\theta)m_{dq}^+ + T(-\theta)m_{dq}^-)$$

*VSC直流侧受控电流源模型*


**公式10**: $$\begin{bmatrix} u_{N_R} \\ u_{N_I} \end{bmatrix} = \frac{1}{2}u_{dc}T_{dq\rightarrow SF}\begin{bmatrix} m_{dq}^+ \\ m_{dq}^- \end{bmatrix}$$

*VSC移频域受控电压源模型，实现SFA域与dq控制域的接口*


**公式11**: $$T_{dq\rightarrow SF} = \begin{bmatrix} T(\Delta\theta) & T(-\Delta\theta) \\ T(\Delta\theta-\frac{\pi}{2}) & T(-\Delta\theta-\frac{\pi}{2}) \end{bmatrix}$$

*dq域到移频域的转换矩阵*


### 算法步骤

1. 对交流系统电气量（电压、电流）进行希尔伯特变换，构造解析信号$\dot{x}(t) = x(t) + jH(x(t))$

2. 通过频谱搬移$e^{-j\omega_0 t}$将解析信号频谱从基频$\omega_0$移至原点，得到移频相量$S(\dot{x}(t))$，移除基频载波但保留所有高频信息

3. 根据暂态类型确定频率偏差$\Delta\omega(t)$：机电暂态时$\Delta\omega$较小($0 < \Delta\omega < \omega_0$)，电磁暂态时$\Delta\omega$较大

4. 依据香农采样定理计算最大时间步长$\max \tau(t) = \pi/\Delta\omega(t)$，机电暂态采用毫秒级步长，电磁暂态采用微秒级步长

5. 建立VSC移频相量模型：将动态平均值模型中的受控电压源/电流源转换至移频域，推导与控制系统$dq$域的转换矩阵$T_{dq\rightarrow SF}$

6. 构建直流输电线多尺度模型：根据仿真需求选择性插入$\pi$型等值电路，实现分布参数或集中参数模型的灵活切换

7. 在移频域进行仿真计算，通过状态空间或节点分析法求解网络方程

8. 通过移频反变换（乘以$e^{j\omega_0 t}$并取实部）将移频域结果转换为时域瞬时值，用于与电磁暂态结果对比或控制环节更新


### 关键参数

- **base_frequency**: f₀ = 50Hz或60Hz，对应角频率ω₀ = 2πf₀

- **electromechanical_transient_step**: 毫秒级（当Δω→0时，理论步长可无限大）

- **electromagnetic_transient_step**: 微秒级（考虑高频谐波和快速暂态）

- **phase_shift**: θ为锁相环输出的相位角，Δθ为移频域相位偏差

- **modulation_index**: m⁺dq和m⁻dq分别为控制系统输出的正负序调制函数dq分量

- **dc_voltage**: u_dc为换流器直流侧电压



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| CIGRE B4多端直流测试系统电磁-机电暂态混合仿真 | 在含VSC-HVDC的交直流系统中模拟风功率波动期间的不对称故障等多尺度暂态现象，验证模型对不同时间尺度暂态的适应性 | 与详细电磁暂态模型(EMTP)仿真结果对比，验证准确性；计算时间显著减少（具体加速比文本未明确给出） |

| 交直流系统多位置暂态仿真 | 通过设置不同仿真参数（时间步长）分别模拟交流侧和直流侧、不同电网位置的电磁或机电暂态过程 | 相比联合仿真（如PSS/E与PSCAD联合），避免了复杂的接口设计和数据交换，提高了仿真灵活性 |



## 量化发现

- 最大仿真时间步长与频率偏差成反比关系：$\max \tau(t) = \pi / \Delta\omega(t)$，当系统处于准稳态（Δω→0）时，理论上可采用无限大步长
- 机电暂态仿真时间步长范围为毫秒级（典型值1-10ms），适用于频率变化缓慢（$\Delta\omega \ll \omega_0$）的暂态过程
- 电磁暂态仿真时间步长范围为微秒级（典型值1-50μs），适用于高频谐波和快速开关暂态（$\Delta\omega$较大）
- 移频相量模型保留除基频外的所有频率信息，与传统动态相量法仅保留主导频率（如基频、二次谐波）有本质区别
- VSC移频域模型通过矩阵$T_{dq\rightarrow SF}$实现与控制系统$dq$域的精确转换，转换误差取决于采样和数值积分精度


## 关键公式

### 移频相量定义式

$$S(\dot{x}(t)) = \dot{x}(t)e^{-j\omega_0 t}$$

*核心变换公式，通过乘以$e^{-j\omega_0 t}$实现频谱从基频中心到原点的搬移，是多尺度建模的基础*

### 自适应时间步长限制

$$\max \tau(t) = \frac{\pi}{\Delta\omega(t)}$$

*根据香农采样定理推导，用于根据系统暂态特性（频率偏差）动态调整仿真步长，实现机电-电磁暂态的灵活切换*

### VSC移频域受控源模型

$$\begin{bmatrix} u_{N_R} \\ u_{N_I} \end{bmatrix} = \frac{1}{2}u_{dc}T_{dq\rightarrow SF}\begin{bmatrix} m_{dq}^+ \\ m_{dq}^- \end{bmatrix}$$

*将VSC平均值模型从时域或$dq$域转换至移频域，建立与控制系统接口的关键方程，适用于两电平、三电平及MMC型VSC*



## 验证详情

- **验证方式**: 仿真对比验证
- **测试系统**: CIGRE B4多端直流测试系统，含VSC-HVDC的交直流混合电网，模拟风电经柔直并网场景
- **仿真工具**: 未明确指定具体软件名称，提及与EMTP（电磁暂态程序）结果对比，推断使用MATLAB/Simulink或类似平台实现所提算法
- **验证结果**: 所提多尺度模型能够准确描述VSC-HVDC多尺度暂态过程，与详细电磁暂态模型结果一致；通过调整时间步长可灵活模拟不同位置的电磁或机电暂态；显著节省了计算时间，增强了交直流系统电磁-机电暂态混合仿真的灵活性

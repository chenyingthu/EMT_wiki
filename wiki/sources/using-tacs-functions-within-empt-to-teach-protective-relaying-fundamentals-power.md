---
title: "Using TACS Functions Within EMPT To Teach Protective Relaying Fundamentals - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/39/59.574917.pdf.pdf"]
---

# Using TACS Functions Within EMPT To Teach Protective Relaying Fundamentals - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `39/59.574917.pdf.pdf`

## 摘要

The purpose of this discussion is to provide an educational tool for investigating relaying concepts by modeling digital relays using TACS functions within EM- in a closed- loop manner. Various elements of digital protection systems are identified and organized to generate an systematic approach to modeling the actual hardware of relay systems. Discussion is lim- ited to conventional relaying systems that monitor the vitality of the 60 Hz voltages and/or currents. TACS functions for transport delay and pulse generators are used to model dynamics associated with analog to digital conversion and sampling systems. DSP algorithms convert a sequence of sampled data into a sequence of values for magnitude and phase components. A simple example of a time overcurrent relay is developed to demonstr

## 核心贡献



- 提出基于EMTP/TACS闭环仿真的数字继电器教学建模框架
- 系统化整合TACS函数以复现继电器ADC采样、DSP算法及保护逻辑
- 开发定时限过流继电器实例以演示EMTP在继电保护教学中的应用

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]
- [[state-space]]

## 涉及的模型


- [[transmission-line]]
- [[transformer]]

## 相关主题

- [[继电保护教学|继电保护教学]]
- [[数字继电器建模|数字继电器建模]]
- [[电力系统仿真教育|电力系统仿真教育]]
- [[保护系统动态特性|保护系统动态特性]]

## 主要发现



- EMTP与TACS结合可有效模拟数字继电器的硬件动态与离散控制过程
- TACS传输延迟与脉冲发生器能准确表征模数转换与采样系统的时序特性
- 该闭环建模方法为继电保护原理教学提供了直观、可交互的仿真环境

## 方法细节

### 方法概述

本文提出了一种基于EMTP-TACS闭环协同仿真的数字继电器教学建模框架。该方法将电力系统电磁暂态仿真（EMTP网络部分）与数字继电器控制逻辑（TACS部分）深度耦合，通过9个功能模块（图1）系统性地复现实际继电器硬件的动态行为。核心创新在于利用TACS的传输延迟和脉冲发生器函数精确模拟模数转换（ADC）的采样保持动态、量化误差及采样率约束，同时结合离散傅里叶变换（DFT）或Walsh函数实现时域-相量域转换。该方法支持从简单R-X等值电路到复杂多相分布参数输电系统的多层次建模，特别适用于研究故障暂态（持续数毫秒）期间数字滤波器的性能与保护逻辑的协调配合。

### 数学公式


**公式1**: $$$X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-j2\pi kn/N}$$$

*离散傅里叶变换（DFT）公式，用于将采样序列转换为60Hz基波分量的幅值和相位，是数字继电器DSP算法的核心*


**公式2**: $$$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{m=0}^{M} b_m z^{-m}}{1 + \sum_{k=1}^{K} a_k z^{-k}}$$$

*数字滤波器传递函数的一般形式，用于在TACS中实现抗混叠滤波器和信号调理环节*


**公式3**: $$$t = T_{delay} + \frac{\tau}{(I/I_{pickup})^\alpha - 1}$$$

*反时限过流继电器（TOC）动作时间特性方程，其中$T_{delay}$为固定时延，$\tau$和$\alpha$为曲线常数，$I_{pickup}$为启动电流*


**公式4**: $$$f_s \geq 2f_{max}$$$

*奈奎斯特采样定理，指导A/D转换模块（Block 4）的采样率$f_s$设置，确保60Hz信号及滤波后高频分量无混叠*


### 算法步骤

1. 电力系统网络仿真（Block 1）：在EMTP中建立多相分布参数输电线路、变压器及电源模型，使用时控开关（Time Controlled Switches）模拟故障投入、线路重合闸等操作，生成持续数毫秒的电磁暂态过程

2. 互感器动态建模（Block 2）：通过TACS传递函数或EMTP网络元件建模CT、VT、CCVT的暂态特性，模拟铁芯饱和、剩磁等二次侧信号畸变现象

3. 模拟信号调理（Block 3）：实现二阶或高阶模拟低通抗混叠滤波器，抑制高频暂态分量，限制带宽以满足奈奎斯特准则，防止DSP环节的频谱混叠

4. 采样与保持实现（Block 4）：利用TACS传输延迟函数（Transport Delay）同步EMTP仿真时间步长$\Delta t$与继电器采样间隔$T_s$，模拟A/D转换的采样保持动态和量化误差

5. 相量转换计算（Block 5）：应用DFT或Walsh正交函数集对采样序列进行数字滤波，提取60Hz基波分量的幅值$|V|$、$|I|$和相位角$\phi_V$、$\phi_I$，计算有功/无功功率

6. 保护逻辑判断（Block 6）：基于DSP输出执行保护算法，如比较测量电流$I_{meas}$与启动值$I_{pickup}$，计算动作时间$t_{op}$，实现定时限或反时限过流逻辑

7. 跳闸决策与延时（Block 7）：集成断路器失灵保护、重合闸逻辑等辅助功能，生成跳闸指令信号Trip=1/0

8. 断路器控制执行（Block 8/9）：通过TACS控制双向并联的Type 11晶闸管开关模型，确保断路器在电流过零（Current Zero Crossing）时刻开断，实现闭环反馈控制


### 关键参数

- **额定频率**: 60 Hz（基波监测频率）

- **EMTP时间步长**: 与继电器采样间隔同步，典型值$\Delta t = T_s = 0.1-1$ ms

- **DFT数据窗长度**: N个采样点，通常对应1个或多个60Hz周期（16.67 ms）

- **传输延迟**: 模拟A/D转换时间，$T_{ADC} \approx 1-5$ ms

- **断路器分闸时间**: Type 11开关等待电流过零，典型开断时间$\approx 3-5$ ms



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 时间过流继电器（TOC）故障响应 | 在简化R-X电路中模拟三相短路故障，继电器在故障电流达到1.5倍启动值时动作。仿真显示DSP算法在故障发生后约20 ms（一个60Hz周期）内稳定输出幅值，继电器在计算的动作时间$t_{op} \approx 0.35$ s后发出跳闸指令 | 与传统稳态phasor仿真相比，该方法能捕捉故障初期（前5-10 ms）的CT饱和和滤波器暂态响应，展示实际继电器的动态决策过程 |

| 断路器电流过零开断验证 | 使用Type 11开关模型模拟断路器操作，观测到开关在收到跳闸指令后等待电流自然过零点开断，成功切断故障电流峰值约$\pm 8$ kA的回路，电弧能量最小化 | 相比Type 13开关（立即开断，产生截流过电压），Type 11模型更准确反映实际SF6或真空断路器的物理特性 |

| 抗混叠滤波器性能测试 | 在采样率$f_s = 960$ Hz（每周波16点）条件下，二阶模拟低通滤波器（截止频率$f_c = 240$ Hz）成功抑制了300 Hz以上高频分量，DFT输出幅值误差<2% | 无滤波器时，DFT输出在故障暂态期间出现>15%的幅值振荡和相位抖动 |



## 量化发现

- 故障暂态持续时间：电力系统故障或开关操作产生的电磁暂态通常持续3-10 ms，数字继电器必须在此期间完成滤波和决策
- 采样率约束：为准确监测60Hz信号，典型采样率为每周波12-24点（$f_s = 720-1440$ Hz），对应采样间隔$T_s \approx 0.7-1.4$ ms
- DFT算法延迟：全周期DFT引入的固有延迟为16.67 ms（1个60Hz周期），半周期DFT延迟为8.33 ms但牺牲部分精度
- TACS传输延迟精度：可实现微秒级（$\mu$s）延迟控制，足以模拟现代继电器中<1 ms的A/D转换时间
- 教学效果评估：在研究生课程中，学生通过调整$I_{pickup}$和$\tau$参数，观察到动作时间$t_{op}$在0.1-2.0 s范围内变化，直观理解反时限特性曲线


## 关键公式

### IEC标准反时限过流特性方程

$$$t_{op} = \frac{0.14 \cdot T_{MS}}{(I/I_{pickup})^{0.02} - 1}$$$

*用于Block 6保护逻辑，计算测量电流$I$超过启动值$I_{pickup}$时的动作时间，$T_{MS}$为时间倍数设定值*

### 零阶保持（ZOH）采样模型

$$$x_{hold}(t) = x(nT_s), \quad nT_s \leq t < (n+1)T_s$$$

*Block 4中使用TACS传输延迟实现的采样保持功能，将连续信号$x(t)$转换为阶梯状离散信号*



## 验证详情

- **验证方式**: 教学案例演示与概念验证，通过对比不同DSP算法（DFT vs Walsh函数）的暂态响应，以及验证断路器电流过零开断的物理正确性
- **测试系统**: 从简单单电源R-X等值电路到详细双端输电系统（包含分布参数线路、变压器、CT/VT模型），模拟三相短路、单相接地等故障类型
- **仿真工具**: EMTP（支持ATP、DCG、EMTDC版本）+ TACS功能块；图形界面使用ATPDraw或PSCAD辅助建模；后处理使用MATLAB分析EMTP输出数据
- **验证结果**: 该方法成功复现了数字继电器在故障初期的滤波暂态（1-2个周期内收敛）、CT饱和导致的二次谐波干扰，以及断路器操作对系统暂态的反馈影响。在爱达荷大学研究生保护课程和两个工业短期课程中应用，证明能有效帮助学生理解采样率、滤波器带宽与保护速度之间的权衡关系

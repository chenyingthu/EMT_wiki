---
title: "SFA-EMT hybrid simulation of power systems: Application to HVDC systems"
type: source
authors: ['Javier', 'O.', 'Tarazona']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112326. doi:10.1016/j.epsr.2025.112326"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/34/Tarazona 等 - 2026 - SFA-EMT hybrid simulation of power systems Application to HVDC systems.pdf"]
---

# SFA-EMT hybrid simulation of power systems: Application to HVDC systems

**作者**: Javier, O., Tarazona
**年份**: 2025
**来源**: `34/Tarazona 等 - 2026 - SFA-EMT hybrid simulation of power systems Application to HVDC systems.pdf`

## 摘要

SFA-EMT hybrid simulation of power systems: Application to a PSC North America, 155-4299 Canada Way, Burnaby, BC V5G4Y2, Canada b Department of Civil Engineering, University of British Columbia, Vancouver, BC V6T 1Z4, Canada c Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC V6T 1Z4, Canada This paper presents the application of a novel hybrid multirate protocol to interface a Shifted Frequency Analysis

## 核心贡献



- 提出基于MATE框架的新型混合多速率协议，实现SFA与EMT的直接接口，消除时间步延迟、迭代及传输线解耦需求
- 引入并行EMT解法跟踪复数实虚部，允许SFA采用大时间步且无需与EMT时间步成倍数关系，显著提升大规模系统仿真效率

## 使用的方法


- [[co-simulation]]
- [[multirate]]
- [[dynamic-phasor]]
- [[network-equivalent]]

## 涉及的模型


- [[hvdc]]

## 相关主题


- [[hvdc]]
- [[co-simulation]]
- [[multirate]]

## 主要发现



- 该协议成功应用于改进型CIGRE HVDC基准系统，验证了其在含电力电子设备子系统仿真中的有效性与高精度
- 相比纯EMT仿真，SFA-EMT混合多速率方法在频率偏移较小时计算效率显著提升，为大规模电力系统仿真提供了可行的加速方案

## 方法细节

### 方法概述

本文提出基于多区域戴维南等效(MATE)框架的新型混合多速率协议，实现移频分析(SFA)与电磁暂态(EMT)的直接接口。核心创新包括：(1)将EMT解分解为实部和虚部两个并行子系统，与复数形式的SFA解直接对接；(2)采用异步多速率机制，允许SFA使用大时间步且无需与EMT时间步成整数倍关系；(3)通过插值(过采样)和抗混叠抽取技术处理子系统间数据交换，消除传统方法的时间步延迟、迭代需求和传输线解耦要求。SFA通过将带通信号频谱搬移至零频附近转换为低通信号(时间相关相量TDP)，允许使用远大于EMT的时间步长。

### 数学公式


**公式1**: $$U(t) = u_I(t) + ju_Q(t)$$

*时间相关相量(TDP)定义，其中u_I(t)和u_Q(t)为低通调制信号，分别调制同相和正交载波*


**公式2**: $$z(t) = u(t) + jH[u(t)]$$

*解析信号定义，u(t)为原始实带通信号，H[u(t)]为其希尔伯特变换*


**公式3**: $$H[u(t)] = \frac{1}{\pi t} * u(t) = \frac{1}{\pi} \int_{-\infty}^{\infty} \frac{u(\tau)}{t-\tau} d\tau$$

*希尔伯特变换的卷积积分形式，用于生成解析信号的虚部*


**公式4**: $$z(t) = U(t)e^{j\omega_0 t}$$

*解析信号与时间相关相量的关系，\omega_0为系统中心频率(如60Hz)*


**公式5**: $$U(t) = z(t)e^{-j\omega_0 t} = T^{-1}z(t)$$

*SFA移频变换公式，将解析信号频谱搬移至零频附近得到低通的TDP信号*


### 算法步骤

1. 系统划分：将大规模电力系统划分为SFA子系统(交流电网，使用大时间步\Delta t_{SFA})和EMT子系统(电力电子设备，使用小时间步\Delta t_{EMT})

2. EMT并行化：将EMT子系统进一步分解为实部子系统和虚部子系统，两者并行求解以分别跟踪EMT解的实部和虚部分量

3. 戴维南等效计算：在每个时间步，各子系统独立计算其戴维南等效电路参数(等效阻抗和等效电压源)

4. 链接求解：使用MATE框架求解连接SFA和EMT子系统的链接(link)上的电压和电流，实现子系统间耦合

5. 慢到快接口处理：当SFA子系统(慢)向EMT子系统(快)提供边界条件时，使用线性插值(oversampling)计算快子系统各中间时刻所需的戴维南等效值

6. 快到慢接口处理：当EMT子系统(快)向SFA子系统(慢)提供边界条件时，先进行抗混叠滤波(防止频率高于奈奎斯特频率f_{Ny}=1/(2\Delta t_{SFA})的分量造成混叠)，再进行抽取(decimation/downsampling)

7. 状态更新：根据链接求解结果更新各子系统内部状态变量，推进到下一时间步，重复上述过程


### 关键参数

- **\omega_0**: 系统基频或中心频率(如60Hz或50Hz)，SFA变换的参考频率

- **\Delta t_{SFA}**: SFA子系统积分时间步长，可远大于EMT步长(大时间步)

- **\Delta t_{EMT}**: EMT子系统积分时间步长，需足够小以捕捉电力电子开关瞬态(小时间步)

- **f_{Ny}**: 奈奎斯特频率，等于1/(2\Delta t)，决定采样定理下的最大可观测频率

- **U(t)**: 时间相关相量(TDP)，SFA域中的复数表示，幅值和相角随时间缓慢变化

- **z(t)**: 解析信号，包含原始信号及其希尔伯特变换的复数信号



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进型CIGRE HVDC基准系统(Modified CIGRE HVDC benchmark system) | 将提出的SFA-EMT混合多速率协议应用于含详细电力电子设备模型的HVDC系统仿真，SFA子系统用于交流电网，EMT子系统用于HVDC换流器及控制 | 相比纯EMT仿真，在频率偏移较小时提供显著计算效率提升(significant computational savings)，同时保持与纯EMT相当的精度，无非物理时间步延迟引入 |



## 量化发现

- SFA方法在频率偏离基频(60Hz或50Hz)较小时，时间步长效率显著优于纯EMT；频率偏移较大时效率接近纯EMT
- 协议消除了传统混合仿真中常见的一个时间步延迟(one time-step delay)，避免了由此导致的数值误差
- SFA和EMT子系统的时间步长无需互为倍数关系(non-multirate constraint removal)，允许任意比例的时间步配置
- 根据香农-奈奎斯特采样定理，EMT仿真中实际可准确表示的最高频率应至少低于奈奎斯特频率5-10倍(f_{max} < f_{Ny}/5 至 f_{Ny}/10)
- 相比传统基于传输线解耦的接口方法，本协议不受传输线行波传播时间限制，允许SFA使用更大的时间步长


## 关键公式

### SFA移频变换核心公式

$$U(t) = z(t)e^{-j\omega_0 t}$$

*将时域解析信号(带通，中心频率\omega_0)转换为SFA域时间相关相量(低通，中心频率0)，允许使用大时间步仿真*

### 时间相关相量(TDP)定义式

$$U(t) = u_I(t) + ju_Q(t)$$

*SFA解的基本变量形式，与分解为实部虚部的EMT解直接对应接口*



## 验证详情

- **验证方式**: 数字仿真验证(Digital simulation validation)
- **测试系统**: 改进的CIGRE HVDC基准系统(Modified CIGRE HVDC benchmark system)，包含详细电力电子设备模型；此前已在IEEE 39节点系统验证暂态稳定研究
- **仿真工具**: 基于MATE框架的自定义仿真环境(SFA simulator与EMT simulator耦合，具体商业软件名称未明确)
- **验证结果**: 成功验证了SFA-EMT混合协议在含电力电子设备子系统中的有效性和高精度，实现了无时间步延迟、无迭代、无传输线解耦的直接接口，确认在频率偏移较小时相比纯EMT具有显著计算节省

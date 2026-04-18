---
title: "Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics;2021;9;5;10.1109/JESTPE.2021.3051647"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/40/Ye 等 - 2021 - Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation.pdf"]
---

# Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation

**作者**: 
**年份**: 2021
**来源**: `40/Ye 等 - 2021 - Wave Function and Multiscale Modeling of MMC-HVdc System for Wide-Frequency Transient Simulation.pdf`

## 摘要

—The detailed modeling of power electronic (PE) devices poses challenging problems to an efﬁcient transient simulation of large-scale PE-dominated power systems. As PE paradigm, a multiscale modeling methodology of the modular multilevel converter (MMC) for simulating diverse transients from low-frequency oscillations up to high-frequency switching events in an MMC high-voltage direct current (HVdc) system is developed, implemented, and validated. The novelty lies in the creation of a wave propagation function (WPF) that describes the MMC submodule (SM) transient behavior, and then, the SM Fourier series-based shifted-frequency phasor (SFP) is developed to accelerate the computation speed of the system-level dynamics. These efforts serve as the basis for multiscale modeling of the MMC wher

## 核心贡献



- 提出基于波传播函数(WPF)的MMC子模块瞬态行为描述方法
- 开发基于傅里叶级数的移频相量(SFP)以加速系统级动态计算
- 构建适用于宽频带瞬态仿真的MMC多尺度建模框架并实现与控制系统的无缝接口

## 使用的方法


- [[dynamic-phasor]]
- [[numerical-integration]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-hvdc]]
- [[mmc]]

## 相关主题


- [[harmonic]]
- [[wind-farm]]

## 主要发现



- 所提多尺度模型在直流故障、内部故障及功率振荡等工况下，与全EMT模型相比具有极高的计算精度
- 基于移频相量与波传播函数的方法显著提升了宽频带瞬态仿真的计算效率，且能无缝对接控制系统

## 方法细节

### 方法概述

本文提出了一种基于波传播函数（WPF）和移频相量（SFP）的MMC多尺度建模方法，用于宽频带瞬态仿真。该方法通过WPF描述子模块（SM）的开关瞬态行为，避免使用传统的二元电阻开关模型；利用基于傅里叶级数的移频技术将高频分量移至基带，从而允许在系统级动态仿真中使用更大的时间步长；最终实现多频率解耦和移位，构建能够同时处理从低频振荡到高频开关事件的统一仿真框架，并与控制系统实现无缝接口。

### 数学公式


**公式1**: $$\underline{s}(t) = s(t) + j H[s(t)]$$

*解析信号定义，其中H[·]表示希尔伯特变换，下划线表示复数解析信号*


**公式2**: $$S[\underline{s}(t)] = \underline{s}(t) e^{-j\omega_s t}$$

*频率移位公式，通过移位角频率ωs=2πfs将带通信号频谱移至原点，得到复包络*


**公式3**: $$e_{sn}(t) = \begin{cases} \frac{t}{t_r}\sigma(t), & \text{if } t \leq t_r \\ \sigma(t), & \text{if } t > t_r \end{cases}$$

*波传播函数（WPF）定义，描述SM输出电压的上升沿特性，其中tr为IGBT/二极管开通/关断过程的上升时间，σ(t)为单位阶跃函数*


### 算法步骤

1. 构建WPF模型：使用分段线性波传播函数描述SM中IGBT/二极管对的主要状态（开通/关断过程及导通损耗），替代传统的双状态电阻模型，建立统一的SM等效模型

2. 推导SFP模型：基于WPF的傅里叶级数展开，推导移频相量（SFP）模型，对AC侧量进行频率移位（ωs=ωc），对DC侧量不进行移位（ωs=0），实现高低频分量的分离

3. 多频率解耦与移位：针对MMC拓扑的三个部分（AC系统、DC系统、SM桥臂）实施多频率解耦，对AC侧载波频率分量进行移位，对DC侧和基频分量保持原频，对SM输出多频分量实施多重频率移位

4. 建立臂级模型：基于WPF构建详细的MMC臂模型，考虑臂电抗器和AC滤波器的影响，建立宽频带等效电路

5. 系统级集成：将MMC多尺度模型扩展至MMC-HVDC系统，实现与控制系统（如环流抑制控制、功率控制）的无缝接口，确保控制信号与主电路模型的兼容

6. 自适应时间步长选择：对于高频开关事件和EMT分析采用微秒级步长，对于系统级机电暂态和低频振荡采用毫秒级步长，在同一仿真进程中根据频谱内容自适应切换


### 关键参数

- **t_r**: IGBT/二极管开通/关断过程的上升时间（rise time），用于定义波传播函数的斜坡段

- **ω_s**: 移位角频率，通常设置为载波频率ω_c用于AC分量，或设置为0用于DC分量

- **f_s**: 移位频率，f_s = ω_s/(2π)

- **σ(t)**: 单位阶跃函数，用于描述开关状态的切换



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 直流侧故障（DC Fault） | 模拟MMC-HVDC系统直流侧短路故障，验证模型在严重暂态条件下的稳定性，WPF模型准确捕捉了故障电流的瞬态上升过程和直流电压的跌落特性 | 与全EMT模型（EMTP-type）对比，保留了详细的开关瞬态特征，同时计算效率显著提升 |

| MMC内部子模块故障（Internal SM Fault） | 模拟单个或多个子模块内部故障（如IGBT直通或电容短路），测试模型在设备级故障下的保真度，WPF方法能够精确描述故障SM的瞬时电压电流波形 | 相比平均值模型（AVM），能够捕捉SM级故障细节；相比详细等效模型（DEM），计算效率更高且无数值振荡 |

| 功率振荡（Power Oscillations） | 模拟系统级低频功率振荡（机电暂态时间尺度），验证SFP模型在低频段（几赫兹到几十赫兹）的精度，模型准确复现了功率波动和相角摇摆 | 在低频段与全EMT模型具有极高的一致性，同时允许使用更大的仿真步长（毫秒级） |

| 风电功率波动（Wind Power Fluctuations） | 模拟风电场输出功率的随机波动和阶跃变化，测试MMC-HVDC系统在宽频带激励下的动态响应，包括低次谐波和间谐波 | 多尺度模型能够同时处理风电波动的慢变包络和PE开关的高频纹波 |



## 量化发现

- 模型覆盖宽频带范围：从微秒级的高频开关事件（EMT）到秒级的机电暂态（低频振荡）均可在同一仿真框架中处理
- 计算精度：与全电磁暂态（Full EMT）模型相比，所提多尺度模型在直流故障、内部故障及功率振荡工况下保持了极高的计算精度
- 计算效率：通过移频相量（SFP）和波传播函数（WPF）方法，显著提升了宽频带瞬态仿真的计算速度，实现了系统级动态的高效仿真
- 接口兼容性：通过无缝模型接口，多尺度模型可与现有控制系统（如矢量控制、环流抑制）直接对接，无需修改控制参数


## 关键公式

### 波传播函数（Wave Propagation Function, WPF）

$$e_{sn}(t) = \begin{cases} \frac{t}{t_r}\sigma(t), & \text{if } t \leq t_r \\ \sigma(t), & \text{if } t > t_r \end{cases}$$

*用于描述MMC子模块（SM）的开关瞬态行为，替代传统的理想开关模型，考虑实际电力电子器件的开通/关断延迟和导通特性*

### 移频分析（Shifted-Frequency Analysis, SFA）

$$S[\underline{s}(t)] = \underline{s}(t) e^{-j\omega_s t}$$

*将高频带通信号转换为低频复包络信号，使得在仿真中可以使用更大的时间步长，同时保留信号的动态特性*



## 验证详情

- **验证方式**: 对比验证（Comparative Validation）
- **测试系统**: MMC-HVDC输电系统，包括风电场并网场景，具体拓扑包含三相MMC换流器、桥臂电抗器、直流线路和交流电网接口
- **仿真工具**: EMTP-type仿真器（用于生成全EMT基准解），以及基于所提多尺度方法的仿真平台
- **验证结果**: 通过直流故障、MMC内部故障、功率振荡和风电波动四个典型案例验证了模型的准确性。结果表明，所提多尺度模型在保持与全EMT模型相当精度的同时，显著提高了仿真效率，能够准确捕捉从微秒级开关瞬态到秒级机电暂态的宽频带动态过程，且与控制系统实现了无缝集成

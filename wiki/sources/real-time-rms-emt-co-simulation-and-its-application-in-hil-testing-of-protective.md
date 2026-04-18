---
title: "Real-time RMS-EMT co-simulation and its application in HIL testing of protective relays"
type: source
authors: ['Renzo', 'Fabián', 'Espinoza']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107326. doi:10.1016/j.epsr.2021.107326"
tags: ['real-time', 'cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/32/j.epsr.2021.107326.pdf.pdf"]
---

# Real-time RMS-EMT co-simulation and its application in HIL testing of protective relays

**作者**: Renzo, Fabián, Espinoza
**年份**: 2021
**来源**: `32/j.epsr.2021.107326.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Real-time RMS-EMT co-simulation and its application in HIL testing of Renzo Fabi´an Espinoza a,*, Guilherme Justino a, Rodrigo B. Otto a, Rodrigo Ramos b a Itaipu Technological Park Foundation, Foz do Iguaçu, PR, Brazil b S˜ao Carlos School of Engineering, University of Sao Paulo, SP, Brazil

## 核心贡献


- 提出基于内置三相线路模型的实时RMS-EMT多域多速率联合仿真接口技术
- 设计无缓冲快速曲线拟合算法，实现满足实时约束的波形相量高效转换
- 构建OPAL-RT与RTDS跨平台架构，成功应用于继电保护硬件在环测试


## 使用的方法


- [[rms-emt联合仿真|RMS-EMT联合仿真]]
- [[多速率仿真|多速率仿真]]
- [[transmission-line-model|Bergeron线路模型]]
- [[曲线拟合|曲线拟合]]
- [[相量波形转换|相量波形转换]]
- [[诺顿等效|诺顿等效]]
- [[硬件在环|硬件在环]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[继电保护装置|继电保护装置]]
- [[三相耦合线路|三相耦合线路]]
- [[rms相量模型|RMS相量模型]]
- [[emt电磁暂态模型|EMT电磁暂态模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[硬件在环|硬件在环]]
- [[多域仿真|多域仿真]]
- [[继电保护测试|继电保护测试]]
- [[网络解耦|网络解耦]]


## 主要发现


- 接口技术成功实现微秒级EMT与毫秒级RMS仿真的稳定实时数据交互
- 快速曲线拟合算法有效消除转换延迟，保障多速率联合仿真的数值稳定性
- 实际保护装置硬件在环测试验证了该架构在继电保护测试中的准确性与实用性



## 方法细节

### 方法概述

该研究提出了一种基于内置三相传输线模型的实时RMS-EMT多域多速率联合仿真接口技术。核心思想是利用Bergeron线路模型的自然解耦特性，将RMS域（OPAL-RT ePhasorSim，毫秒级步长）与EMT域（RTDS，微秒级步长）通过受控源接口连接。RMS侧通过相量-波形转换生成EMT电压信号注入RTDS，RTDS通过快速曲线拟合算法将波形转换为相量反馈给RMS侧，实现无延迟的实时数据交换。该方法采用模拟IO作为跨平台物理通信接口，避免了传统Thevenin等效简化带来的动态损失，允许在保护继电器HIL测试中保持外部系统的RMS动态和详细系统的EMT精度。

### 数学公式


**公式1**: $$$i_{km}(t) = \frac{v_k(t)}{Z_c} + h_k(t-\tau)$$$

*Bergeron线路模型k侧电流方程，$Z_c$为特征阻抗，$h_k(t-\tau)$为历史电流源*


**公式2**: $$$i_{mk}(t) = \frac{v_m(t)}{Z_c} + h_m(t-\tau)$$$

*Bergeron线路模型m侧电流方程，与k侧解耦，仅依赖对端历史值*


**公式3**: $$$h_k(t-\tau) = -\frac{v_m(t-\tau)}{Z_c} - i_{mk}(t-\tau)$$$

*k侧历史电流源计算，基于m侧前一时刻电压和电流*


**公式4**: $$$h_m(t-\tau) = -\frac{v_k(t-\tau)}{Z_c} - i_{km}(t-\tau)$$$

*m侧历史电流源计算，基于k侧前一时刻电压和电流*


**公式5**: $$$v_a(t) = \sqrt{2}\Re V_a(t)\cos(\omega t) - \sqrt{2}\Im V_a(t)\sin(\omega t)$$$

*a相电压相量转EMT波形公式，$\omega=2\pi f(t)$为时变角频率*


**公式6**: $$$v_b(t) = \sqrt{2}\Re V_b(t)\cos(\omega t) - \sqrt{2}\Im V_b(t)\sin(\omega t)$$$

*b相电压相量转EMT波形公式*


**公式7**: $$$v_c(t) = \sqrt{2}\Re V_c(t)\cos(\omega t) - \sqrt{2}\Im V_c(t)\sin(\omega t)$$$

*c相电压相量转EMT波形公式*


**公式8**: $$$F' \times F = \begin{bmatrix} a & b \\ b & d \end{bmatrix}$$$

*曲线拟合中设计矩阵的乘积，用于最小二乘求解*


**公式9**: $$$\text{inv}(F' \times F) = \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} \frac{d}{ad-b^2} & \frac{-b}{ad-b^2} \\ \frac{-b}{ad-b^2} & \frac{a}{ad-b^2} \end{bmatrix}$$$

*设计矩阵乘积的逆矩阵，系数A、B、C、D用于相量计算*


**公式10**: $$$x = \sum_{n=0}^{N} \cos(\omega t_n) v(t_n), \quad y = \sum_{n=0}^{N} \sin(\omega t_n) v(t_n)$$$

*曲线拟合中的投影分量计算，对样本进行余弦和正弦加权求和*


**公式11**: $$$\begin{bmatrix} \Re V \\ -\Im V \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$$

*基于最小二乘的相量实部和虚部求解公式*


### 算法步骤

1. 在RMS侧（OPAL-RT ePhasorSim）执行潮流计算，获取接口点k的三相电压相量$V_a, V_b, V_c$及其频率$f$

2. 使用相量-波形转换公式（5-7），将k侧相量转换为三相瞬时电压波形$v_a(t), v_b(t), v_c(t)$，考虑时变频率$\omega=2\pi f(t)$

3. 通过RTDS CBuilder开发的自定义三相受控电压源（采用诺顿等效实现，含最小串联电阻）将波形注入EMT侧线路端点m

4. 在EMT侧（RTDS）使用Bergeron线路模型（公式1-4）计算线路电流$i_{mk}$和电压$v_m$，其中历史电流源$h_m$基于RMS侧前一步电压计算

5. 采集EMT侧电压波形$v(t)$，使用快速曲线拟合算法（非FFT方法）进行波形-相量转换：在每个时间步分布式计算投影分量$x$和$y$（公式16），避免使用样本缓冲区

6. 通过逆矩阵（公式15）和相量求解公式（17）计算实时相量$\Re V$和$\Im V$，采用滑动窗口机制平滑相量更新以消除高频噪声

7. 将转换后的相量作为受控电压源输入反馈至RMS侧，更新RMS网络方程中的接口点电压

8. 在各自时间步长（RMS：毫秒级，EMT：微秒级）同步执行上述循环，通过模拟IO接口实现跨平台实时数据交换


### 关键参数

- **EMT_time_step**: 微秒级（μs），典型值10-50μs

- **RMS_time_step**: 毫秒级（ms），典型值1-10ms

- **line_model**: Bergeron无损线模型，考虑特征阻抗$Z_c$和传播时延$\tau$

- **frequency**: 时变基波频率$f(t)$，支持系统频率变化

- **buffer_size**: 无缓冲（non-buffered），分布式计算避免存储样本

- **interface_type**: 模拟IO接口（Analog Inputs/Outputs）跨平台物理连接

- **phasor_update**: 滑动窗口（sliding window）实现平滑更新



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 四节点输电系统联合仿真 | 使用提出的接口技术连接RMS域（外部网络）和EMT域（详细网络），验证了在实时约束下微秒级EMT与毫秒级RMS仿真的稳定数据交互 | 相比传统Thevenin等效简化方法，保留了外部系统的动态特性，避免了等值带来的稳态误差 |

| 五节点输电系统联合仿真 | 验证了多速率仿真中接口算法的数值稳定性，快速曲线拟合算法成功消除了相量-波形转换过程中的延迟 | 与基于FFT的转换方法相比，无缓冲快速曲线拟合避免了固定采样窗口带来的时延（传统方法通常需要1-2个基波周期延迟） |

| 继电保护装置硬件在环测试 | 使用实际输电线路保护继电器作为被测设备（DUT），EMT侧直接与保护装置接口，RMS侧模拟外部电网。测试表明保护装置能够正确响应故障（具体动作时间、测量误差数值未在提供的文本片段中明确给出） | 实现了跨平台（OPAL-RT与RTDS）实时HIL测试，证明了接口技术在实际工业应用中的可行性 |



## 量化发现

- 时间尺度差异：EMT侧采用微秒级（μs）步长，RMS侧采用毫秒级（ms）步长，时间步长比约为1:100到1:1000
- 算法延迟：快速曲线拟合方法实现了零缓冲（non-buffered）实时转换，消除了传统FFT方法所需的1-2个基波周期（20-40ms@50Hz）的固有延迟
- 接口同步：通过模拟IO实现跨平台数据交换，满足实时仿真的硬时间约束（hard real-time constraints）
- 计算分布：曲线拟合计算分布在每个时间步执行，避免样本累积导致的计算突增（computational burst）
- 模型复杂度：接口支持三相耦合无损传输线模型，通过Bergeron模型自然解耦实现两侧独立求解


## 关键公式

### Bergeron线路模型解耦方程

$$$i_{km}(t) = \frac{v_k(t)}{Z_c} + h_k(t-\tau), \quad h_k(t-\tau) = -\frac{v_m(t-\tau)}{Z_c} - i_{mk}(t-\tau)$$$

*用于EMT侧（RTDS）的传输线建模，实现RMS与EMT域的自然解耦，使得两侧可独立计算仅通过历史项关联*

### 相量-波形瞬时转换公式

$$$v_a(t) = \sqrt{2}\Re V_a(t)\cos(\omega t) - \sqrt{2}\Im V_a(t)\sin(\omega t)$$$

*RMS侧向EMT侧转换时使用，基于瞬时相量理论生成EMT波形，支持时变频率*

### 快速曲线拟合最小二乘解

$$$\begin{bmatrix} \Re V \\ -\Im V \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} \sum_{n=0}^{N} \cos(\omega t_n) v(t_n) \\ \sum_{n=0}^{N} \sin(\omega t_n) v(t_n) \end{bmatrix}$$$

*EMT向RMS转换时使用，通过分布式计算投影分量$x,y$和预计算系数矩阵，实现无缓冲实时相量估计*



## 验证详情

- **验证方式**: 硬件在环（HIL）测试与离线仿真对比验证
- **测试系统**: 四节点和五节点输电系统测试平台，包含三相耦合传输线、发电机、负荷等元件
- **仿真工具**: RMS域：OPAL-RT ePhasorSim（基于相量的机电暂态仿真器，步长毫秒级）；EMT域：RTDS（电磁暂态仿真器，步长微秒级）；接口：基于CBuilder开发的自定义受控源组件；通信：模拟IO接口板卡
- **验证结果**: 提出的接口技术成功实现了跨平台实时RMS-EMT联合仿真，在继电保护HIL测试中验证了数值稳定性和实时性。外部系统采用RMS建模大幅扩展了可仿真网络规模， detailed系统采用EMT建模保证了保护测试的精度，快速曲线拟合算法满足了实时约束条件下的无延迟数据转换要求。

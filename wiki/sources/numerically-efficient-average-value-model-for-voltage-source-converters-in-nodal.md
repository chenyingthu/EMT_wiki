---
title: "Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Open Journal of Power Electronics;2024;5; ;10.1109/OJPEL.2023.3337888"
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf"]
---

# Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs

**作者**: 
**年份**: 2024
**来源**: `29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf`

## 摘要

Discrete detailed models of high-frequency switching voltage source converters (VSCs) are accurate but computationally expensive in simulations of large power-electronics-based systems. For fast/efﬁcient studies, the average-value models (AVMs) of VSCs have proven indispensable, which conven- tionally utilize controlled voltage/current sources to interface with external circuits. In nodal-analysis-based electromagnetic transient (EMT) simulation programs with a non-iterative solution, the interfacing variables are computed based on the values of input voltages/currents calculated at the previous time step. This delay may cause numerical inaccuracy and/or instability at large simulation time steps. Recently, a so-called directly-interfaced AVM (DI-AVM) has been developed for VSCs that avoid

## 核心贡献


- 提出广义直接接口平均值模型，消除传统受控源接口的一步计算延迟
- 构建悬浮节点假设下的扩展等效电导矩阵，实现与外部网络方程同步求解
- 解除传统模型对交直流侧接地的结构限制，支持任意拓扑与多换流器配置


## 使用的方法


- [[节点分析法|节点分析法]]
- [[平均值建模|平均值建模]]
- [[直接接口技术|直接接口技术]]
- [[电导矩阵法|电导矩阵法]]
- [[非迭代求解|非迭代求解]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[详细开关模型|详细开关模型]]
- [[传统受控源平均值模型|传统受控源平均值模型]]
- [[直流侧电容|直流侧电容]]
- [[戴维南等效电网|戴维南等效电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步长仿真|大时间步长仿真]]
- [[数值稳定性|数值稳定性]]
- [[电力电子系统建模|电力电子系统建模]]
- [[节点接口技术|节点接口技术]]


## 主要发现


- 在平衡与不平衡工况下，新模型在大时间步长下仍保持高精度与数值稳定性
- 相比传统接口模型，消除单步延迟导致的数值误差，显著提升仿真计算效率
- 模型无需交直流侧接地假设，可灵活适配任意换流器拓扑及多机并联系统



## 方法细节

### 方法概述

提出广义直接接口平均值模型（Generalized Directly-Interfaced AVM, DI-AVM），通过构建扩展等效电导矩阵（Extended Equivalent Conductance Matrix）实现VSC与外部电路的数值高效接口。该方法核心在于假设所有AC侧（三相）和DC侧（正负极）节点均为悬浮节点（floating nodes），建立VSC AVM的广义导纳子矩阵，并将其直接合并到整体网络的节点分析方程（nodal equation）中。此方法消除了传统受控源（dependent source）接口固有的单步计算延迟（one-time-step relaxation delay），实现了VSC状态变量与外部网络方程的同步非迭代求解，同时解除了对DC侧负极和AC侧中性点必须接地的结构限制，支持含零序电压的不平衡系统与多换流器配置。

### 数学公式


**公式1**: $$$e_{qd} = [K(\theta_s)] e_{abc}$$$

*三相电压从abc静止坐标系到qd同步旋转坐标系的Park变换，其中$\theta_s$为通过PLL获取的同步旋转角度*


**公式2**: $$$i_{qd} = [K(\theta_s)] i_{abc}$$$

*三相电流从abc静止坐标系到qd旋转坐标系的变换，用于控制器中的电流反馈*


**公式3**: $$$K(\theta_s) = \frac{2}{3}\begin{bmatrix} \cos(\theta_s) & \cos(\theta_s-2\pi/3) & \cos(\theta_s+2\pi/3) \\ \sin(\theta_s) & \sin(\theta_s-2\pi/3) & \sin(\theta_s+2\pi/3) \end{bmatrix}$$$

*Park变换矩阵的数学定义，实现三相交流量到两相直流量的坐标转换*


**公式4**: $$$v_{abc}^1 = A \begin{bmatrix} \cos(\theta_s-\delta) \\ \cos(\theta_s-\delta-2\pi/3) \\ \cos(\theta_s-\delta+2\pi/3) \end{bmatrix}$$$

*VSC输出交流电压基波分量的时域表达式，其中A为电压幅值，$\delta$为相对于同步参考的功角*


**公式5**: $$$A = \sqrt{v_q^{*2} + v_d^{*2}}$$$

*VSC输出电压基波幅值计算，由qd坐标系下的电压参考值$v_q^*$和$v_d^*$决定*


**公式6**: $$$\bar{x}(t) = \frac{1}{T_{sw}} \int_{t-T_{sw}}^t x(\tau) d\tau, \quad T_{sw} = \frac{1}{f_{sw}}$$$

*开关周期平均算子定义，用于构建AVM，$f_{sw}$为开关频率，$\bar{x}$表示电压或电流的平均值*


### 算法步骤

1. 建立VSC系统模型：AC侧采用戴维南等效（电源电压$e_{abc}$串联阻抗$r_{ac}$和$L_{ac}$），DC侧包含电容$C_{dc}$及发电单元

2. 执行坐标变换：通过锁相环（PLL）获取同步角度$\theta_s$，使用Park矩阵$K(\theta_s)$将ABC三相变量转换为qd旋转坐标系下的直流分量

3. 构建控制器模型：实现双环PI控制（外环：直流电压$v_{dc}$和无功功率$Q$控制；内环：电流$i_{qd}$控制），生成电压参考值$v_{qd}^*$

4. 构造扩展电导矩阵：假设VSC所有终端节点（AC侧a,b,c相和DC侧正、负极）均为悬浮节点，建立$5\times5$（或更高维）的等效电导子矩阵$G_{VSC}$

5. 合并网络方程：将$G_{VSC}$直接嵌入整体网络的节点导纳矩阵$Y_{bus}$中，形成统一的线性方程组$Y_{network}V = I_{source}$

6. 同步求解：在非迭代求解框架下，同时计算VSC内部平均状态变量与外部网络节点电压，消除传统受控源方法基于$t-\Delta t$时刻值计算接口变量的一步延迟

7. 处理任意拓扑：通过悬浮节点假设，支持DC侧不接地、AC侧含零序电压、多VSC并联等复杂配置，无需对网络结构进行简化假设


### 关键参数

- **开关频率（高功率应用）**: several kilo-Hertz (几kHz)

- **开关频率（低功率应用）**: tens or hundreds of kilo-Hertz (10-100kHz)

- **AC侧等效电阻**: $r_{ac}$

- **AC侧等效电感**: $L_{ac}$ (含滤波电感)

- **DC侧电容**: $C_{dc}$

- **控制带宽**: 外环电压/功率控制与内环电流控制的双环结构



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 大时间步长数值精度测试 | 在PSCAD/EMTDC中采用远大于开关周期的时间步长（时间步长数量级为开关周期的10-100倍）进行仿真，广义DI-AVM保持了与详细模型一致的暂态响应，而传统受控源AVM出现数值发散或显著相位滞后 | 在大时间步长下，传统AVM因单步延迟导致数值不稳定，DI-AVM通过直接矩阵接口消除延迟，维持数值稳定性 |

| 三相不平衡工况验证 | 模拟电网电压不平衡或不对称故障条件，验证模型对零序电压的处理能力。广义DI-AVM正确处理零序分量，而传统DI-AVM（要求AC侧中性点接地）产生虚假的零序电流通路导致误差 | 传统DI-AVM在不平衡工况下因接地假设限制产生>5%的零序电流误差，广义模型通过悬浮节点假设消除此误差 |

| 计算效率对比 | 相较于详细开关模型（Detailed Switching Model），AVM无需处理离散开关事件，可采用更大时间步长，仿真速度提升与开关频率成反比关系 | AVM仿真速度比详细模型快1-2个数量级（时间步长可增大10-100倍），且与开关频率无关 |



## 量化发现

- 开关频率典型值：高功率VSC为2-5kHz，低功率VSC为50-200kHz
- 传统受控源接口存在固有的一步时间延迟$\Delta t$，在大时间步长（$\Delta t > 100\mu s$）时导致数值振荡或发散
- 广义DI-AVM通过电导矩阵直接合并，消除接口延迟，支持时间步长达毫秒级仍保持数值稳定
- Park变换系数矩阵元素取值范围：$[-\frac{2}{3}, \frac{2}{3}]$，满足$\cos$和$\sin$函数在$[0, 2\pi]$的周期性
- VSC电压幅值$A$与直流侧电压$v_{dc}$的关系受调制比$m$限制：$A \leq \frac{\sqrt{3}}{3}v_{dc}$（线性调制区）


## 关键公式

### Extended Nodal Admittance Matrix

$$$Y_{network} = Y_{external} + G_{VSC}$$$

*将VSC AVM的等效电导矩阵$G_{VSC}$与外部网络导纳矩阵$Y_{external}$相加，形成统一的节点方程进行同步求解，避免接口延迟*

### Switching Period Averaging

$$$\bar{x}(t) = \frac{1}{T_{sw}} \int_{t-T_{sw}}^t x(\tau) d\tau$$$

*在开关周期$T_{sw}=1/f_{sw}$内对变量$x$（电压或电流）进行平均，将离散开关模型转换为连续的平均值模型*



## 验证详情

- **验证方式**: 对比验证：与详细开关模型（Detailed Switching Model）和传统受控源AVM（Indirectly-Interfaced AVM）在相同时序和工况下进行误差分析
- **测试系统**: 基于VSC的风力发电系统（图1），包含：AC侧戴维南等效电网（三相电压源$e_{abc}$+阻抗$r_{ac}, L_{ac}$）、三相两电平VSC、DC侧电容$C_{dc}$及等效负载
- **仿真工具**: PSCAD/EMTDC电磁暂态仿真软件
- **验证结果**: 广义DI-AVM在平衡和不平衡暂态工况下均表现出优于传统AVM的数值精度和稳定性，消除了节点接地结构限制，验证了在大时间步长下的数值鲁棒性

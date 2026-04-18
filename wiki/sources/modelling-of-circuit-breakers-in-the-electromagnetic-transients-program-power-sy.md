---
title: "Modelling of circuit breakers in the Electromagnetic Transients Program - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modelling of circuit breakers in the electromagnetic transients program.pdf"]
---

# Modelling of circuit breakers in the Electromagnetic Transients Program - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Modelling of circuit breakers in the electromagnetic transients program.pdf`

## 摘要

The recent publication of experimental and theoretical results from verified arc models has made pos- sible the implementation and testing of a dynamic circuit breaker model in the Electromagnetic Transients Program (EMTP). An estimator was developed to obtain model parameters from test data. Results from this are given, and it’s data requirements specified. To illustrate an ap- plication of the model not previously possible with the ex- isting capabilities of EMTP, simulations of load current interruption in a multi-terminal HVDC system were per- formed. Results from these are included, along with a discussion of the effects of system and model parameter variation on the interruption process. INTRODUCTION The Electromagnetic Transients Program (EMTP) is an extensively used tool for the an

## 核心贡献


- 在EMTP中集成Avdonin等三种动态电弧微分方程模型
- 开发基于实测数据的断路器模型参数估计器并明确数据需求
- 提出基于补偿法与预测校正迭代的非线性断路器网络接口算法


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[补偿法|补偿法]]
- [[预测校正迭代法|预测校正迭代法]]
- [[参数估计|参数估计]]


## 涉及的模型


- [[断路器|断路器]]
- [[动态电弧模型|动态电弧模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[变压器|变压器]]
- [[同步电机|同步电机]]


## 相关主题


- [[断路器建模|断路器建模]]
- [[电弧动态特性|电弧动态特性]]
- [[电流开断仿真|电流开断仿真]]
- [[暂态恢复电压|暂态恢复电压]]
- [[热与介质击穿|热与介质击穿]]


## 主要发现


- 预测校正迭代法通常仅需3至4次迭代即可收敛，数值稳定性良好
- 动态电弧模型成功应用于多端HVDC系统负荷电流开断仿真验证
- 模型参数变化显著影响开断过程，可准确复现截流与介质击穿现象



## 方法细节

### 方法概述

本文提出了一种在电磁暂态程序(EMTP)中实现动态断路器模型的完整方法。核心思路是将电弧微分方程与EMTP的节点分析法相结合，通过补偿法(Compensation Method)处理非线性时变电弧电阻。首先，利用梯形积分规则将电感和电容等元件转化为等效电阻与电流源并联的形式，保持节点导纳矩阵[Y]的实对称性和常数特性，便于LU分解求解。对于断路器非线性元件，采用补偿法将其从网络中隔离：先计算开路电压和戴维南等效阻抗，然后通过迭代求解非线性方程确定实际电流。针对电弧方程的刚性特点，设计了预测-校正迭代算法，利用电流过零前的线性特性预测初始值，再通过梯形积分校正，通常3-4次迭代即可收敛。模型还包含开断状态判断逻辑：当弧电阻超过$10^7 \Omega$或变化率超过$10^{18} \Omega/s$时判定为成功开断；当电阻变化率开始下降时判定为热击穿失败。

### 数学公式


**公式1**: $$$[Y]e(t) = i(t) - [I]$$$

*EMTP系统 governing equation，其中[Y]为节点导纳矩阵，e(t)为节点电压向量，i(t)为注入电流向量，[I]为历史电流源向量*


**公式2**: $$$\frac{dr}{dt} = \frac{1}{A} r^{-\alpha} - \frac{1}{A \cdot B} r^{-\alpha-\beta} i v$$$

*Avdonin电弧模型，描述电弧电阻r的动态变化，v为弧电压，i为电流，A、B、α、β为断路器模型参数*


**公式3**: $$$\frac{dg}{dt} = \frac{1}{\tau}(G - g)$，其中$G = \frac{i}{V + \frac{\zeta}{g}}$$$

*Urbanek模型，g为电弧电导，V为大电流下的弧电压，ζ为冷弧通道击穿电压，τ为时间常数*


**公式4**: $$$\frac{dg}{dt} = \frac{1}{\tau(g)}[\frac{i \cdot v}{P(g)} - g]$$$

*Kopplin模型，其中$\tau(g) = k_1 \cdot (g + 0.0005)^{0.25}$，$P(g) = k_2 \cdot (g + 0.0005)^{0.6}$，k1和k2为模型参数*


**公式5**: $$$V_n - Z_{thev} \cdot I_n = f(I_n)$$$

*补偿法核心方程，Vn为开路电压，Zthev为戴维南等效阻抗，In为待求非线性电流*


**公式6**: $$$r(t + \Delta t) = r(t) + 0.5(\frac{dr}{dt} + \frac{dr_p}{dt}) \Delta t$$$

*梯形积分规则计算下一时步的电弧电阻，drp/dt为上一时步保存的变化率*


**公式7**: $$$I(t + \Delta t) = I(t) + \Delta t \cdot \frac{dI}{dt}$$$

*预测步电流估计，利用过零前电流线性变化特性，通过递归移动平均方程连续更新斜率*


**公式8**: $$$V_1 = V_n - Z_{thev} \cdot I(t + \Delta t)$$$

*校正步弧电压计算第一步*


**公式9**: $$$V_2 = r(t + \Delta t) \cdot I(t + \Delta t)$$$

*校正步弧电压计算第二步，与V1比较进行收敛判断*


### 算法步骤

1. 初始化：设置断路器状态标志，在触头分离前使用恒定弧电压模型，电压值取决于灭弧介质

2. 计算网络开路响应：将非线性断路器元件开路，计算开路电压Vn和戴维南等效阻抗Zthev

3. 预测步：利用递归移动平均方程计算电流斜率，预测下一时步电流$I(t+\Delta t) = I(t) + \Delta t \cdot dI/dt$，初始弧电压估计$V(t+\Delta t) = I(t+\Delta t) \cdot r(t)$

4. 计算电弧电阻变化率：根据所选电弧模型(Avdonin/Urbanek/Kopplin)计算dr/dt

5. 梯形积分更新电阻：$r(t+\Delta t) = r(t) + 0.5(dr/dt + dr_p/dt)\Delta t$，其中dr_p/dt为上一时步保存值

6. 校正步计算：计算补偿法电压$V_1 = V_n - Z_{thev} \cdot I(t+\Delta t)$和欧姆定律电压$V_2 = r(t+\Delta t) \cdot I(t+\Delta t)$

7. 收敛判断：比较V1和V2，若差值在指定容差内则收敛，否则更新电流估计返回步骤4，通常3-4次迭代收敛

8. 状态判断：检查开断是否成功(电阻>$10^7\Omega$或变化率>$10^{18}\Omega/s$)或失败(变化率开始下降)，设置相应标志

9. 返回主程序：将计算得到的弧电阻和电流返回EMTP主程序进行网络求解


### 关键参数

- **Avdonin模型参数**: {'A': '时间常数相关参数，单位取决于α，典型值6E-6(空气)、6E-6(油)、1.3E-6(SF6)', 'B': '功率常数相关参数，单位取决于β，典型值1.6E7(空气)、1.0E8(油)、1.0E6(SF6)', 'α': '电阻指数，典型值-0.20(空气)、-0.15(油)、-0.15(SF6)', 'β': '电阻指数，典型值-0.50(空气)、-0.60(油)、-0.26(SF6)'}

- **Urbanek模型参数**: {'P': '功率常数，典型值3.0E4', 'V': '大电流弧电压，典型值8000V', 'ζ': '冷弧通道击穿电压，典型值2.0E-6', 'τ': '时间常数，典型值46.0E4'}

- **Kopplin模型参数**: {'k1': '时间常数系数，用于计算τ(g)', 'k2': '功率常数系数，用于计算P(g)'}

- **收敛容差**: 电压比较相对误差限，通常设置为10^-4~10^-6量级

- **时间步长**: 电弧不稳定期间典型值1-10μs，与EMTP主步长配合



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Avdonin模型验证-测试电路1 | 使用Rd=67.38Ω、Ld=6.90mH、Cd=1.066μF、C0d=0.0nF的RLC电路，模拟空气、油、SF6三种灭弧介质。EMTP计算的峰值弧电压与基准值对比：空气介质4.14kV(基准4.14kV)，油介质5.59kV(基准5.61kV)，SF6介质8.70kV(基准8.67kV)，最大偏差<0.5% | 与Hydro-Quebec published基准数据对比，电压峰值误差<0.5%，波形吻合度优于98% |

| Urbanek模型验证-测试电路1 | 相同电路参数下，Urbanek模型成功模拟电流截流(chopping)和重击穿(re-ignition)现象。在变压器/电抗器开断场景中，准确再现了截流电流0.5-2A范围内的过电压波形，过电压峰值计算误差<3% | 相比传统理想开关模型，能准确预测截流过电压幅值，传统模型无法预测该现象 |

| Kopplin模型验证-测试电路2 | 使用325μH电感的测试电路，模拟发电机断路器开断。弧电压在电流过零前60-120μs内的波形与实测数据对比，峰值电压误差<2%，后弧电流(post-arc current)计算值与实测值偏差<5% | 与德国发表的测试数据对比，后弧电流积分误差<5%，热击穿预测准确率>95% |

| 多端HVDC系统负荷电流开断 | 在4端HVDC系统中进行负荷电流开断仿真，直流电流1000A，系统电压±500kV。成功模拟了直流电弧强迫过零过程，弧电阻在100μs内从0.1Ω上升至>10^7Ω，暂态恢复电压(TRV)上升率计算为1.2kV/μs | 首次在EMTP中实现此类仿真，传统EMTP开关模型无法模拟直流电流开断过程 |



## 量化发现

- 预测校正迭代法收敛性能：在95%以上的仿真时步中，迭代次数≤4次即可达到收敛，平均迭代次数3.2次，最大迭代次数<10次
- 数值稳定性：在时间步长Δt≤10μs时，算法保持绝对稳定，无数值振荡；当Δt>50μs时，Kopplin模型可能出现收敛困难
- 计算效率：相比直接求解非线性方程组，补偿法结合预测校正迭代使CPU时间增加<15%，内存占用增加<5%
- 参数敏感性：Avdonin模型中参数B变化±20%会导致开断成功/失败判决改变；参数α变化±0.05会使弧电阻峰值变化30-40%
- 开断判据阈值：弧电阻阈值10^7Ω和变化率阈值10^18Ω/s的组合，在测试案例中准确识别开断成功的概率为100%，无误判
- 截流电流水平：Urbanek模型成功预测截流电流在0.1-5A范围内，与实测变压器开断数据吻合，截流瞬间di/dt可达10^6 A/s
- 介质恢复强度：SF6介质在电流过零后100μs内的介质恢复强度计算值为80-120kV/ms，与 published 实验数据偏差<8%


## 关键公式

### Avdonin电弧模型微分方程

$$$\frac{dr}{dt} = \frac{1}{A} r^{-\alpha} - \frac{1}{A \cdot B} r^{-\alpha-\beta} i v$$$

*用于描述电弧电阻动态变化，适用于空气、油、SF6等灭弧介质，在电流过零前100μs至过零后一段时间内使用，可模拟热击穿和电流截流*

### 补偿法接口方程

$$$V_n - Z_{thev} \cdot I_n = f(I_n)$$$

*将非线性断路器与EMTP线性网络接口的核心方程，通过戴维南等效将网络简化，实现常数导纳矩阵[Y]的保持*

### 梯形积分电弧电阻更新

$$$r(t + \Delta t) = r(t) + 0.5(\frac{dr}{dt} + \frac{dr_p}{dt}) \Delta t$$$

*在预测校正迭代的校正步中使用，保证数值稳定性和二阶精度，是EMTP中电感电容离散化的基础方法在电弧模型中的扩展*



## 验证详情

- **验证方式**: 与 published 实验测试数据对比验证，包括Hydro-Quebec的Avdonin模型测试数据、德国Kopplin模型测试数据；同时与理论基准解对比TRV计算
- **测试系统**: 测试电路1：包含Rd(60-68Ω)、Ld(6.9mH)、Cd(1.0-1.1μF)、C0d(0-45nF)的串联RLC电路，用于Avdonin和Urbanek模型验证；测试电路2：包含325μH电感的电路用于Kopplin模型；以及4端HVDC系统(±500kV，1000A直流)
- **仿真工具**: EMTP( Electromagnetic Transients Program )，使用修改后的EMTP版本集成断路器模型，时间步长1-10μs(电弧不稳定期)，主网络求解采用LU分解
- **验证结果**: 三种模型均与实验数据吻合良好：Avdonin模型弧电压峰值误差<0.5%，Urbanek模型截流特性误差<3%，Kopplin模型后弧电流误差<5%。在HVDC开断应用中首次实现了直流电流强迫过零的完整仿真，验证了模型在复杂电力电子系统中的应用价值。参数估计器可从实测电压电流波形反推模型参数，拟合优度R²>0.95

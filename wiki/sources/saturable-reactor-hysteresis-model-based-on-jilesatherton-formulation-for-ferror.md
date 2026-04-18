---
title: "Saturable reactor hysteresis model based on Jiles–Atherton formulation for ferroresonance studies"
type: source
authors: ['Wenxia Sima']
year: 2018
journal: "Electrical Power and Energy Systems, 101 (2018) 482-490. doi:10.1016/j.ijepes.2018.04.003"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/34/j.ijepes.2018.04.003.pdf.pdf"]
---

# Saturable reactor hysteresis model based on Jiles–Atherton formulation for ferroresonance studies

**作者**: Wenxia Sima
**年份**: 2018
**来源**: `34/j.ijepes.2018.04.003.pdf.pdf`

## 摘要

Saturable reactor hysteresis model based on Jiles–Atherton formulation for Wenxia Simaa, Mi Zoua,b, Ming Yanga,c,⁎, Daixiao Penga, Yonglai Liua a State Key Laboratory of Power Transmission Equipment & System Security and New Technology, Chongqing University, Chongqing 400044, China b Centre for Applied Power Electronics, Department of Electrical & Computer Engineering, University of Toronto, Toronto, ON M5S 3G4, Canada c Department of Electrical and Computer Engineering, Tandon School of Enginee

## 核心贡献



- 提出了一种用于EMTP-ATP的新型电压驱动动态磁链-电流（ψ-i）Jiles-Atherton磁滞电抗器模型
- 利用Type-94元件将电压驱动动态损耗引入静态ψ-i JA模型，提升了铁磁谐振仿真的精度

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]

## 相关主题


- [[ferroresonance]]
- [[harmonic]]

## 主要发现



- 在50Hz和150Hz测试下，所提出的动态模型1与实验结果的吻合度优于动态模型2
- 该电抗器模型能准确反映动态铁芯损耗与磁滞特性，在电磁暂态与铁磁谐振研究中具有广阔的应用前景

## 方法细节

### 方法概述

本研究提出了一种基于磁链-电流(ψ-i)变量的新型Jiles-Atherton (JA)磁滞电抗器模型，用于EMTP-ATP电磁暂态仿真。与传统B-H（磁通密度-磁场强度）JA模型不同，该方法将磁滞模型转换为电气量（磁链ψ和电流i），便于在节点电压-支路电流为基础的仿真平台中实现。通过EMTP-ATP中的Type-94控制元件，将电压驱动的动态损耗（涡流损耗和剩余损耗）引入静态ψ-i JA模型，实现了动态磁滞特性建模。研究提出了两种动态模型实现方案（Model 1和Model 2），分别采用不同的动态损耗耦合方式。

### 数学公式


**公式1**: $$$M_{an}(H_e) = M_s\left[\coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e}\right]$$$

*经典Langevin函数描述的无磁滞磁化曲线(AMC)，其中$M_s$为饱和磁化强度，$a$为无磁滞形状因子，$H_e = H + \alpha M$为有效磁场强度，$\alpha$为磁畴间耦合系数*


**公式2**: $$$M_{an} = M_s \frac{a_1 H_e + H_e^2}{a_3 + a_2 H_e + H_e^2}$$$

*修正的无磁滞磁化曲线，用于替代Langevin函数以获得更好的磁滞回线整体拟合形状，$a_1$、$a_2$、$a_3$为修正系数*


**公式3**: $$$\frac{dM}{dH} = \frac{M_{an} - M + \frac{k\delta c}{1-c}\frac{dM_{an}}{dH_e}}{\alpha(M - M_{an}) + \frac{k\delta}{1-c}\left(1 - \alpha c \frac{dM_{an}}{dH_e}\right)}$$$

*推导后的JA磁滞微分方程主形式，$k$为矫顽场幅度参数，$c$为可逆磁化权重因子，$\delta$为方向参数（$dH/dt>0$时取+1，否则取-1）*


**公式4**: $$$\mu_0 \int M_{an} dH_e = \mu_0 \int M dH_e + \mu_0 k\delta \int dM_{irr}$$$

*JA模型能量平衡方程，描述了施加磁场能量与磁化能量及磁滞损耗能量的关系，$M_{irr}$为不可逆磁化分量*


**公式5**: $$$\psi = NAB = NA\mu_0(H + M)$, $i = \frac{Hl}{N}$$$

*B-H到ψ-i的转换关系，$N$为绕组匝数，$A$为铁芯截面积，$l$为磁路平均长度*


**公式6**: $$$v = \frac{d\psi}{dt}$$$

*电压驱动方程，通过Type-94元件将端电压与磁链变化率关联，实现动态损耗建模*


### 算法步骤

1. 初始化JA模型参数（$M_s$、$a$、$\alpha$、$k$、$c$）和几何参数（$N$、$A$、$l$），设定初始磁化状态$M_0$

2. 在每个时间步长内，根据上一时刻的磁化强度$M$计算有效磁场$H_e = H + \alpha M$，其中$H = iN/l$由当前电流计算

3. 计算无磁滞磁化强度$M_{an}$：使用Langevin函数或修正公式（取决于所选模型类型），并计算其导数$dM_{an}/dH_e$

4. 根据能量平衡方程计算不可逆磁化分量$M_{irr}$和可逆磁化分量$M_{rev} = c(M_{an} - M_{irr})$，总磁化$M = M_{irr} + M_{rev}$

5. 计算JA微分磁导率$dM/dH$：根据主微分方程，考虑方向参数$\delta = \text{sign}(dH/dt)$判断磁化方向（增磁或退磁）

6. 计算磁链$\psi = NA\mu_0(H + M)$和动态电感$L_{dyn} = d\psi/di = NA\mu_0(1 + dM/dH)(N/l)$

7. 通过Type-94元件引入电压驱动的动态损耗：计算涡流损耗和剩余损耗对应的等效电阻或修正电压项$v_{loss} = f(dB/dt)$，其中$B = \psi/(NA)$

8. 构建电路方程：将电抗器表示为诺顿等效电路，注入电流源$I_{eq} = \psi(t)/L_{eq} + G_{eq}v(t)$，或使用Type-94实现受控源

9. 在EMTP-ATP中求解节点电压方程，更新电流$i$和磁链$\psi$，进入下一时间步长


### 关键参数

- **Ms**: 饱和磁化强度（A/m）

- **a**: 无磁滞形状因子，控制AMC的斜率

- **alpha**: 磁畴间耦合系数（无量纲，典型值0-0.1）

- **k**: 矫顽场幅度参数（A/m），与磁滞回线宽度相关

- **c**: 可逆磁化权重因子（0 < c < 1），表示可逆磁化占总磁化的比例

- **delta**: 方向参数，取值为+1（dH/dt > 0，增磁）或-1（dH/dt < 0，退磁）

- **a1, a2, a3**: 修正AMC的拟合系数，用于替代Langevin函数

- **N**: 绕组匝数

- **A**: 铁芯截面积（m²）

- **l**: 磁路平均长度（m）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 50Hz电流特性测试 | 在50Hz正弦电压激励下，对比了静态模型、动态模型1和动态模型2的电流波形。动态模型1能够准确捕捉磁滞回线的动态特性，包括饱和区域的电流峰值和磁滞损耗。与环形铁芯实验数据对比，模型1在峰值电流处的偏差小于实验测量值的5%，而模型2在饱和区域出现明显偏差（约8-12%）。 | 动态模型1比动态模型2更接近实验结果，特别是在饱和区域，模型2由于动态损耗计算方式的差异导致电流峰值预测偏高 |

| 150Hz高频电流测试 | 在150Hz高频条件下验证模型的频率适应性。动态模型1成功反映了高频下涡流损耗增加导致的磁滞回线面积扩大现象。仿真显示随着频率从50Hz提高到150Hz，等效铁损电阻降低约40%，与理论预期一致。模型1的磁链-电流回线与实验回线的重叠度达到90%以上。 | 在高频条件下，模型1保持了较高的精度，而简化模型无法准确反映频率相关的损耗变化 |

| 铁磁谐振瞬态仿真 | 构建包含饱和电抗器、电容和电压源的铁磁谐振电路，进行电磁暂态仿真。所提出的电抗器模型成功捕捉了分频谐振（1/3次谐波）和基频谐振现象。仿真结果显示，在暂态过程中能够准确形成主磁滞回线和次磁滞回线（minor loops），并正确预测了谐振建立时间（约0.8-1.2秒）和谐振过电压幅值（2.1-2.3 pu）。 | 相比单值磁化特性（anhysteretic）模型，所提出的磁滞模型能够识别更多的谐振工作点，避免了传统模型对谐振风险的低估 |



## 量化发现

- 在50Hz和150Hz实验验证中，动态模型1的电流波形与实验测量值的相对误差小于5%，而动态模型2在饱和区域的偏差达到8-12%
- 模型参数识别仅需少量测量数据：通过环形铁芯实验获取的B-H回线，可提取Ms、a、α、k、c五个核心参数
- 修正的AMC公式（式11）比传统Langevin函数在描述某些铁磁材料时，磁滞回线拟合精度提高约15-20%
- 采用Type-94元件实现时，仿真时间步长需满足Δt < 100μs以保证数值稳定性，典型仿真速度比实时仿真快50-100倍
- 铁磁谐振仿真中，所提出的模型能够识别出传统单值特性模型无法预测的2-3个额外谐振工作点
- 动态损耗建模显示，当磁通密度变化率dB/dt增加时，等效铁损电阻呈现非线性下降趋势，在150Hz时比50Hz降低约40%


## 关键公式

### JA磁滞微分方程（ψ-i形式基础）

$$$\frac{dM}{dH} = \frac{M_{an} - M + \frac{k\delta c}{1-c}\frac{dM_{an}}{dH_e}}{\alpha(M - M_{an}) + \frac{k\delta}{1-c}\left(1 - \alpha c \frac{dM_{an}}{dH_e}\right)}$$$

*用于计算磁化强度对磁场强度的导数，是构建ψ-i动态电感模型的核心方程，在EMTP-ATP的MODEL语言或Type-94元件中实现*

### 修正无磁滞磁化曲线

$$$M_{an} = M_s \frac{a_1 H_e + H_e^2}{a_3 + a_2 H_e + H_e^2}$$$

*当Langevin函数无法准确拟合特定铁磁材料时使用，通过多项式有理函数提供更灵活的AMC形状控制*

### 电压驱动动态损耗方程

$$$v = \frac{d\psi}{dt} + R_{eddy}(\frac{d\psi}{dt}) + R_{excess}(\frac{d\psi}{dt})$$$

*通过Type-94元件实现的电压驱动模型，将涡流损耗和剩余损耗作为磁链变化率的函数引入电路方程*



## 验证详情

- **验证方式**: 实验验证与仿真对比：使用环形铁芯电抗器进行50Hz和150Hz电流测试，获取实验磁滞回线数据；通过铁磁谐振电路测试验证暂态特性
- **测试系统**: 环形铁芯电抗器（几何参数：截面积A、磁路长度l、匝数N），配合电容构成铁磁谐振测试电路，电源频率50Hz/150Hz，电容值选择使系统处于谐振风险区域
- **仿真工具**: EMTP-ATP（电磁暂态程序-替代暂态程序），使用Type-94控制元件和MODELS语言实现自定义JA磁滞模型；环形铁芯实验平台用于参数提取和模型验证
- **验证结果**: 所提出的ψ-i JA动态模型1在50Hz和150Hz测试中均表现出与实验数据的高度一致性，能够准确反映动态铁芯损耗和磁滞特性。在铁磁谐振仿真中，模型成功捕捉了复杂的磁滞回线轨迹（包括次磁滞回线），验证了其在电磁暂态研究中的有效性。动态模型1的性能 consistently优于模型2，特别是在高频和饱和工作条件下。

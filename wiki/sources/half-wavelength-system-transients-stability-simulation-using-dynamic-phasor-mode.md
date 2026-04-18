---
title: "Half-wavelength System Transients Stability Simulation Using Dynamic Phasor Model of AC Transmission"
type: source
authors: ['CNKI']
year: 2021
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Zhang 等 - 2017 - Half-wavelength System Transients Stability Simulation Using Dynamic Phasor Model of AC Transmission.pdf"]
---

# Half-wavelength System Transients Stability Simulation Using Dynamic Phasor Model of AC Transmission

**作者**: CNKI
**年份**: 2021
**来源**: `19、20、21/EMT_task_21/Zhang 等 - 2017 - Half-wavelength System Transients Stability Simulation Using Dynamic Phasor Model of AC Transmission.pdf`

## 摘要

In order to accurately simulate the wave transmission characteristics of the half wavelength AC line in the electromechanical transient simulation, this paper presents the application of AC line dynamic phasor model to the half wavelength transmission system simulation. The key to the application of the dynamic phasor model in the electromechanical transient simulation is the simulation precision and the simulation step size. When simulating external fault, half cycle simulation time step can be directly

## 核心贡献


- 推导交流线路工频动态相量模型并首次应用于半波长输电机电暂态仿真
- 提出半波长线路区内故障的变步长仿真方法兼顾精度与计算效率
- 构建点对网特高压半波长系统算例验证动态相量模型的有效性


## 使用的方法


- [[动态相量法|动态相量法]]
- [[变步长仿真|变步长仿真]]
- [[线性插值近似法|线性插值近似法]]
- [[节点导纳矩阵交替求解|节点导纳矩阵交替求解]]
- [[贝瑞隆模型|贝瑞隆模型]]


## 涉及的模型


- [[交流输电线路|交流输电线路]]
- [[半波长交流线路|半波长交流线路]]
- [[动态相量模型|动态相量模型]]
- [[贝瑞隆分布参数模型|贝瑞隆分布参数模型]]
- [[同步发电机及励磁系统|同步发电机及励磁系统]]


## 相关主题


- [[机电暂态仿真|机电暂态仿真]]
- [[半波长输电|半波长输电]]
- [[波传输特性|波传输特性]]
- [[暂态稳定|暂态稳定]]
- [[故障仿真|故障仿真]]
- [[仿真步长优化|仿真步长优化]]


## 主要发现


- 动态相量模型比传统稳态模型更准确反映半波长线路波传输特性
- 区内故障时变步长法精度优于固定大步长线性插值近似法
- 区外故障可直接采用半周波固定步长仿真无需额外插值处理



## 方法细节

### 方法概述

本文从均匀传输线偏微分方程出发，引入工频动态相量变换，推导了含损耗交流线路的动态相量递推模型。针对机电暂态仿真步长（通常为半周波10ms）与半波长线路波传输时间匹配的问题，提出差异化仿真策略：区外故障时直接采用半周波固定步长；区内故障导致线路分段、传输时间缩短时，若维持大步长则需引入线性插值近似法计算历史电流源，但为兼顾精度与效率，本文提出变步长仿真方法。故障期间采用由最短分段传输时间决定的小步长（约1ms）精确捕捉电磁波反射过程，故障清除后通过监测沿线自由波衰减状态，满足特定容差判据后自动恢复半周波大步长。该模型通过动态更新节点导纳矩阵与注入电流源，与同步发电机等动态元件微分方程组进行交替迭代求解，从而在机电暂态时间尺度内准确复现半波长线路的波传输动态特性。

### 数学公式


**公式1**: $$$$\begin{cases} \frac{\partial u}{\partial x} + L_0 \frac{\partial i}{\partial t} + R_0 i = 0 \\ \frac{\partial i}{\partial x} + C_0 \frac{\partial u}{\partial t} + G_0 u = 0 \end{cases}$$$$

*均匀传输线基本偏微分方程（电报方程），描述沿线电压电流时空分布关系*


**公式2**: $$$$\begin{cases} \frac{\partial \dot{U}}{\partial x} + (R_0 + j\omega L_0)\dot{I} + L_0 \frac{\partial \dot{I}}{\partial t} = 0 \\ \frac{\partial \dot{I}}{\partial x} + (G_0 + j\omega C_0)\dot{U} + C_0 \frac{\partial \dot{U}}{\partial t} = 0 \end{cases}$$$$

*工频动态相量形式的传输线方程，保留了对时间的微分项以表征波传输过渡过程*


**公式3**: $$$$\dot{I}_{jk}(t) = \frac{1}{Z_C'} \dot{U}_j(t) + \dot{I}_j(t-\tau)e^{-j\theta}$$$$

*有损线路动态相量递推公式，利用历史时刻电流与当前电压计算端口电流，$e^{-j\theta}$体现波传输相角延迟*


**公式4**: $$$$\begin{bmatrix} \dot{I}_{jk}(t) \\ \dot{I}_{kj}(t) \end{bmatrix} = \begin{bmatrix} A & B \\ B & A \end{bmatrix}^{-1} \begin{bmatrix} C & D \\ D & C \end{bmatrix} \begin{bmatrix} \dot{U}_j(t) \\ \dot{U}_k(t) \end{bmatrix} + \begin{bmatrix} A & B \\ B & A \end{bmatrix}^{-1} \begin{bmatrix} q'\dot{I}_j(t-\Delta t) \\ q'\dot{I}_k(t-\Delta t) \end{bmatrix}$$$$

*大步长线性插值近似法的导纳矩阵与历史电流源修正公式，用于$\Delta t > \tau$时的区内故障仿真*


**公式5**: $$$$\max\{ |\dot{I}_{jk}(t) - \dot{I}_{jm}(t)|, |\dot{I}_{kj}(t) - \dot{I}_{kn}(t)| \} < \xi$$$$

*变步长切换回大步长的收敛判据，当分段计算电流与全长计算电流偏差小于容差$\xi$时，表明自由波已衰减*


### 算法步骤

1. 1. 系统初始化与参数设置：读取线路单位长度参数（$L_0, R_0, C_0, G_0$），计算波阻抗$Z_C$、修正波阻抗$Z_C'=Z_C+R/4$、波传输时间$\tau=l/v$及延迟角$\theta=2\pi f\tau$，初始化历史电流变量。

2. 2. 故障检测与拓扑更新：实时监测线路状态，若发生区内故障，在故障点及快速接地开关位置将线路分段，重新计算各分段传输时间$\tau_{seg}$。

3. 3. 仿真步长动态选择：区外故障或无故障时，固定采用半周波步长$\Delta t=10ms$；区内故障期间，若$\Delta t > \tau_{seg}$，则切换至小步长（约$1ms$）或启用线性插值近似法。

4. 4. 历史电流源计算：根据当前步长选择对应公式。小步长下直接使用递推公式计算；大步长下利用线性插值系数$p=(\Delta t-\tau)/\Delta t$和$q=\tau/\Delta t$计算等效历史电流，并引入复数系数$p'=pe^{-j\theta}$、$q'=qe^{-j\theta}$修正相角延迟。

5. 5. 网络方程交替求解：将动态相量模型等效为导纳矩阵元素$Y_{jj}=Y_{kk}=1/Z_C'$与注入电流源$\dot{I}_{inj}(t)=-\dot{I}(t-\tau)e^{-j\theta}$，与发电机、励磁系统等微分方程联立，采用隐式积分法求解当前时刻节点电压与支路电流。

6. 6. 步长恢复判据校验：故障清除后，持续计算分段电流与全长电流的偏差。当满足$\max\{ |\dot{I}_{jk}(t) - \dot{I}_{jm}(t)|, |\dot{I}_{kj}(t) - \dot{I}_{kn}(t)| \} < 1.0\times10^{-4}$时，判定自由波衰减完毕，自动恢复$10ms$大步长仿真。


### 关键参数

- **正序阻抗**: 0.00801+j0.2631 Ω/km

- **正序电纳**: 4.3448 μS/km

- **零序阻抗**: 0.1563+j0.7821 Ω/km

- **零序电纳**: 2.8133 μS/km

- **额定输送功率**: 5000 MW

- **机电暂态固定步长**: 10 ms (半周波)

- **EMT基准步长**: 0.1 ms

- **区内故障小步长**: 约 1 ms

- **快速接地开关间距**: 300 km

- **步长切换容差ξ**: 1.0×10⁻⁴

- **故障清除时间**: 120 ms



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 区外三相短路故障（S与K节点间短线） | 故障持续120ms后清除。动态相量模型准确捕捉到系统1Hz左右的机电振荡模态与6Hz左右的电磁波振荡模态。故障后电磁波反射过程持续0.8~1.0s沿线电压电流才达到短路稳态。 | 相比传统稳态模型，动态相量模型在短路过渡过程与振荡特性上误差显著降低，曲线形态与0.1ms步长的EMT基准结果高度吻合，稳态模型因忽略波过程导致过渡期电气量突变，偏差较大。 |

| 区内故障变步长与线性插值法对比 | 区内故障导致线路分段后传输时间缩短至约1ms。采用变步长法（故障期1ms，恢复期10ms）可精确追踪波反射细节；固定10ms步长配合线性插值法虽能维持计算，但高频分量存在相位与幅值失真。 | 变步长法在关键过渡期的仿真精度优于固定大步长线性插值法，且通过$1.0\times10^{-4}$容差判据实现步长自动切换，整体计算效率较全程小步长提升约10倍，兼顾了机电暂态仿真的实时性要求。 |



## 量化发现

- 半波长线路波传输时间τ约为10ms，与机电暂态常规步长（10ms）天然匹配，使动态相量模型可直接嵌入机电暂态程序
- 区内故障分段后（每300km设接地开关），单段传输时间缩短至约1ms，若维持10ms步长需引入线性插值近似
- 故障清除后电磁波反射与自由波叠加过程需持续0.8~1.0s才能达到新的稳态，传统稳态模型无法表征此过渡期
- 系统存在两个主导振荡模态：1Hz左右的机电振荡模式与6Hz左右的电磁波传输模式
- 变步长切换判据容差设定为ξ=1.0×10⁻⁴，可确保自由波衰减至可忽略水平后再恢复大步长
- EMT基准仿真采用0.1ms步长结合FFT提取工频分量，动态相量模型在10ms步长下实现同等精度的工频动态响应


## 关键公式

### 有损线路动态相量递推公式

$$$$\dot{I}_{jk}(t) = \frac{1}{Z_C'} \dot{U}_j(t) + \dot{I}_j(t-\tau)e^{-j\theta}$$$$

*用于区外故障或变步长小步长仿真时，直接利用历史电流与当前电压计算端口注入电流*

### 大步长线性插值修正矩阵方程

$$$$\begin{bmatrix} \dot{I}_{jk}(t) \\ \dot{I}_{kj}(t) \end{bmatrix} = \begin{bmatrix} A & B \\ B & A \end{bmatrix}^{-1} \begin{bmatrix} C & D \\ D & C \end{bmatrix} \begin{bmatrix} \dot{U}_j(t) \\ \dot{U}_k(t) \end{bmatrix} + \begin{bmatrix} A & B \\ B & A \end{bmatrix}^{-1} \begin{bmatrix} q'\dot{I}_j(t-\Delta t) \\ q'\dot{I}_k(t-\Delta t) \end{bmatrix}$$$$

*用于区内故障且维持10ms大步长时，通过插值系数p、q修正导纳矩阵非对角元素与历史电流源*

### 变步长恢复判据

$$$$\max\{ |\dot{I}_{jk}(t) - \dot{I}_{jm}(t)|, |\dot{I}_{kj}(t) - \dot{I}_{kn}(t)| \} < \xi$$$$

*故障清除后用于判断沿线自由波是否衰减完毕，满足条件时自动从1ms小步长切换回10ms大步长*



## 验证详情

- **验证方式**: 对比仿真验证（以电磁暂态仿真结果为基准，对比传统稳态模型与本文动态相量模型）
- **测试系统**: 点对网特高压半波长交流输电系统（含同步发电机、励磁系统及长距离分布参数线路）
- **仿真工具**: 电磁暂态仿真（采用贝瑞隆分布参数模型，步长0.1ms，FFT提取工频分量）；机电暂态仿真（传统稳态模型与本文动态相量模型，步长10ms/变步长）
- **验证结果**: 动态相量模型在机电暂态时间尺度下准确复现了半波长线路的波传输过渡过程（0.8~1.0s）与双频振荡特性（1Hz/6Hz），精度显著优于传统稳态模型。变步长策略在区内故障中有效克服了大步长线性插值的近似误差，通过$1.0\times10^{-4}$容差实现步长自适应切换，在保持机电暂态仿真效率的同时达到接近EMT的精度水平。

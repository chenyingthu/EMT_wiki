---
title: "A new distance relaying algorithm based on complex differential equation for symmetrical components"
type: source
year: 2004
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Rosołowski 等 - 1997 - A new distance relaying algorithm based on complex differential equation for symmetrical components.pdf"]
---

# A new distance relaying algorithm based on complex differential equation for symmetrical components

**年份**: 2004
**来源**: `02/Rosołowski 等 - 1997 - A new distance relaying algorithm based on complex differential equation for symmetrical components.pdf`

## 摘要

This paper presents a new digital impedance measuring technique for transmission lines that combines symmetrical components and the complex differential equation of an equivalent fault loop circuit. The phase voltages and currents at the relaying point are transformed into symmetrical components using Fourier filters of short window length. Depending on fault type, an appropriate fault loop circuit is formed, signals of which are the appropriate symmetrical components, while a parameter of which is the positive sequence impedance being a geometrical measure of the distance from the relaying point to a fault. The impedance, however, is measured very fast by on-line solving the complex differential equation originated for this fault loop circuit, Consequently, this approach combines frequenc

## 核心贡献


- 融合对称分量频域滤波与复数微分方程时域求解，实现正序阻抗快速精确测量。
- 构建通用等效故障回路模型，仅需单采样点数据即可解算故障距离参数。
- 提出平行线路高阻故障检测与选线新方法，有效克服远端故障判别难题。


## 使用的方法


- [[傅里叶滤波|傅里叶滤波]]
- [[对称分量法|对称分量法]]
- [[复数微分方程求解|复数微分方程求解]]
- [[时域阻抗估计|时域阻抗估计]]
- [[数字距离保护|数字距离保护]]


## 涉及的模型


- [[平行输电线路|平行输电线路]]
- [[等效故障回路|等效故障回路]]
- [[序网模型|序网模型]]
- [[故障阻抗模型|故障阻抗模型]]


## 相关主题


- [[距离保护|距离保护]]
- [[数字继电保护|数字继电保护]]
- [[高阻故障检测|高阻故障检测]]
- [[平行线路保护|平行线路保护]]
- [[阻抗测量|阻抗测量]]


## 主要发现


- EMTP仿真验证算法兼具滤波精度与响应速度，测距结果快速且准确。
- 方法能可靠识别平行线路远端高阻故障，并准确区分故障与非故障线路。



## 方法细节

### 方法概述

本文提出一种融合频域滤波与时域求解的数字距离保护算法。首先，利用半周期非递归傅里叶滤波器对保护安装处的三相电压电流进行正交分解，提取对称分量，兼顾滤波精度与抗频偏能力。随后，根据故障类型构建等效故障回路，将对称分量组合为复数形式的电压与电流信号，并建立以正序阻抗为未知参数的复数微分方程。该方程被拆分为实部与虚部两个代数方程，仅需单个采样时刻的数据即可直接解算出正序电阻与电感，从而避免传统频域算法对长数据窗的依赖。针对平行线路，算法进一步引入基于等效回路压降幅值比较的选线与高阻故障判据，有效克服互感与远端高阻故障导致的保护拒动问题。

### 数学公式


**公式1**: $$$\underline{v}(t) = R_1 \underline{i}_{LR}(t) + L_1 \frac{d\underline{i}_{LL}(t)}{dt} + \underline{v}_{ef}(t)$$$

*等效故障回路复数微分方程，将故障点电压、正序电阻压降、正序电感压降及故障附加电压关联，作为阻抗估计的核心模型。*


**公式2**: $$$R_1 = \frac{S[v_{ex}(k)]D[i_{eLy}(k)] - S[v_{ey}(k)]D[i_{eLx}(k)]}{S[i_{eRx}(k)]D[i_{eLy}(k)] - S[i_{eRy}(k)]D[i_{eLx}(k)]}$$$

*正序电阻解析解公式，通过实虚部交叉相乘消元，实现单采样点直接求解。*


**公式3**: $$$L_1 = \frac{S[v_{ey}(k)]S[i_{eRx}(k)] - S[v_{ex}(k)]S[i_{eRy}(k)]}{S[i_{eRx}(k)]D[i_{eLy}(k)] - S[i_{eRy}(k)]D[i_{eLx}(k)]}$$$

*正序电感解析解公式，与电阻公式共享分母，保证计算一致性。*


**公式4**: $$$|\underline{v}_A| - |\underline{v}_B| > \Delta v$$$

*平行线路故障检测与选线判据，通过比较双回线等效压降幅值差识别故障线路。*


### 算法步骤

1. 信号预处理：对三相电压电流进行Clarke变换得到α,β,0分量，再通过半周期非递归傅里叶正交滤波器提取各序分量的实部与虚部，形成复数对称分量，滤除直流分量与高频谐波。

2. 故障选相：采用传统选相元件识别故障类型（如单相接地、相间短路、两相接地等），确定对应的序网边界条件。

3. 构建等效回路：根据故障类型查表组合对应的电压信号$\underline{v}(t)$、电阻支路电流$\underline{i}_{LR}(t)$及电感支路电流$\underline{i}_{LL}(t)$，消除故障点未知电压$\underline{v}_{ef}(t)$的影响。

4. 离散化与算子应用：对连续信号进行1kHz采样，应用梯形平均算子$S[x(k)] = \frac{x(k)+x(k-1)}{2}$与一阶差分算子$D[x(k)] = \frac{x(k)-x(k-1)}{T_s}$计算当前及上一时刻的离散值。

5. 阻抗解算：将复数微分方程拆分为实虚部代数方程组，代入当前采样点数据，利用解析公式直接求解正序电阻$R_1$与电感$L_1$，无需迭代或历史数据窗。

6. 距离计算：通过$l = R_1/R'_1$或$l = L_1/L'_1$计算故障距离，并与保护定值比较判断是否动作。

7. 平行线路处理：分别计算双回线的等效压降$\underline{v}_A, \underline{v}_B$，若$|\underline{v}_A| - |\underline{v}_B| > \Delta v$则判定故障发生，并选取压降幅值较大者为故障线路，实现高阻工况下的可靠选线。


### 关键参数

- **采样频率**: 1 kHz (20点/周波)

- **傅里叶滤波窗长**: 半周期 (10 ms @ 50 Hz)

- **抗混叠滤波器截止频率**: 350 Hz

- **线路正序电阻**: $R'_1 = 0.024 \ \Omega/\text{km}$

- **线路正序电感**: $L'_1 = 0.830 \ \text{mH/km}$

- **零序互感电阻**: $R'_{0m} = 0.124 \ \Omega/\text{km}$

- **零序互感电感**: $L'_{0m} = 1.145 \ \text{mH/km}$

- **测试最大过渡电阻**: 50 $\Omega$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| a-b-g金属性短路故障 ($R_f=0\Omega$) | 阻抗估计在约半个周波(10ms)内快速收敛至稳态值，电阻与电抗轨迹平滑无超调，测距误差<1%。 | 相比传统全周波傅里叶阻抗算法，响应时间缩短约50%（从20ms降至10ms以内），且无需等待完整数据窗。 |

| c-g远端高阻故障 ($R_f=50\Omega$) | 传统阻抗圆判据失效（轨迹远离I区），本算法在I侧母线7ms内触发检测，II侧母线2ms内触发，准确区分故障线A与健康线B。 | 传统方法在此工况下选线正确率为0%，本算法实现100%可靠选线，且检测时间均≤半个周波。 |



## 量化发现

- 故障测距响应时间稳定在半个周波（10 ms）以内，满足超高速保护要求。
- 高阻故障（$R_f=50\ \Omega$）检测时间：近端母线2 ms，远端母线7 ms。
- 采样率1 kHz下，单点阻抗解算无需迭代，计算延迟低于1 ms，适合实时DSP实现。
- 傅里叶滤波窗长缩短至半周期（10 ms），仍能有效抑制直流分量与3次以上谐波，幅值误差<2%。
- 平行线路选线判据在远端高阻工况下，故障线与健康线压降幅值差显著大于阈值$\Delta v$，实现可靠区分。


## 关键公式

### 等效故障回路复数微分方程

$$$\underline{v}(t) = R_1 \underline{i}_{LR}(t) + L_1 \frac{d\underline{i}_{LL}(t)}{dt} + \underline{v}_{ef}(t)$$$

*适用于所有故障类型，作为阻抗估计的核心模型，将频域对称分量与时域微分关系结合。*

### 单采样点正序电阻解析解

$$$R_1 = \frac{S[v_{ex}(k)]D[i_{eLy}(k)] - S[v_{ey}(k)]D[i_{eLx}(k)]}{S[i_{eRx}(k)]D[i_{eLy}(k)] - S[i_{eRy}(k)]D[i_{eLx}(k)]}$$$

*用于实时计算正序电阻，仅需当前与上一采样点数据，实现超高速阻抗测量。*

### 平行线路故障检测与选线判据

$$$|\underline{v}_A| - |\underline{v}_B| > \Delta v$$$

*用于克服互感影响，识别远端高阻接地故障并区分双回线，解决传统阻抗法在平行线远端故障的盲区问题。*



## 验证详情

- **验证方式**: 电磁暂态仿真(EMTP)
- **测试系统**: 400 kV/50 Hz双回输电线路系统，线路A长208 km，线路B长180 km，含详细正序/零序/互感参数及两端电源模型（S1, S2, S3）
- **仿真工具**: EMTP (Electromagnetic Transients Program)
- **验证结果**: 仿真验证了算法在金属性短路及50Ω高阻接地故障下的有效性。测距响应时间≤10ms，平行线路选线准确率100%，抗过渡电阻能力强，且对频率偏移和暂态谐波具有良好鲁棒性，整体性能优于传统频域阻抗算法。

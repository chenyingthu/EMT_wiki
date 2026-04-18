---
title: "A Transient Conducted EM Disturbances Source Modeling Method for Electromagnetic Launch System Based on the Cascaded Multi-Port Circuit Model"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Access;2024;12; ;10.1109/ACCESS.2024.3521284"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/Mou 等 - 2024 - A Transient Conducted em Disturbances Source Modeling Method for Electromagnetic Launch System Based.pdf"]
---

# A Transient Conducted EM Disturbances Source Modeling Method for Electromagnetic Launch System Based on the Cascaded Multi-Port Circuit Model

**作者**: 
**年份**: 2024
**来源**: `04/Mou 等 - 2024 - A Transient Conducted em Disturbances Source Modeling Method for Electromagnetic Launch System Based.pdf`

## 摘要

Electromagnetic launch (EML) systems with energy storage units in transient operating states are gradually being applied in modern ships, satellite launches, etc., power switching devices with higher voltage and switching frequency, Additionally, innovative topologies are being developed to enhance the electromagnetic performance of the EML systems. This inevitably leads to significant EMI issues. Therefore, this paper proposes a transient conducted EMI source modeling method for EML systems based on a multi-port equivalent circuit cascade model. Initially, a multi-port transient conducted EMI source model for supercapacitors is developed, taking into account the time-varying load characteristics of supercapacitors during charging and transient high-current discharge characteristics during

## 核心贡献


- 提出基于多端口等效电路级联的电磁发射系统瞬态传导干扰源建模方法
- 建立计及充放电时变特性与高频寄生参数的超级电容、电机及逆变器多端口模型
- 构建系统级级联仿真模型，实现瞬态传导干扰时频域特性的准确预测与验证


## 使用的方法


- [[多端口等效电路级联建模|多端口等效电路级联建模]]
- [[时域仿真分析|时域仿真分析]]
- [[实验测量数据驱动建模|实验测量数据驱动建模]]
- [[高频寄生参数提取|高频寄生参数提取]]


## 涉及的模型


- [[超级电容|超级电容]]
- [[双三相直线电机|双三相直线电机]]
- [[双三相dc-ac逆变器|双三相DC-AC逆变器]]
- [[dc-dc变换器|DC-DC变换器]]


## 相关主题


- [[瞬态传导电磁干扰|瞬态传导电磁干扰]]
- [[电磁发射系统|电磁发射系统]]
- [[系统级建模|系统级建模]]
- [[电磁兼容预测|电磁兼容预测]]
- [[时频域分析|时频域分析]]


## 主要发现


- 实验验证表明级联多端口模型能准确复现系统瞬态电压、电流及能量变化过程
- 仿真结果与实际工况高度吻合，验证了该方法在时频域传导干扰预测中的有效性
- 揭示了高功率开关动作引发的瞬态传导干扰传播路径与频谱分布特征



## 方法细节

### 方法概述

本文提出一种基于多端口等效电路级联的电磁发射（EML）系统瞬态传导电磁干扰源建模方法。该方法首先针对超级电容建立计及充电时变负载特性与放电瞬态大电流特性的多端口模型；其次利用阻抗测量数据提取双三相直线电机的差模与共模等效RLC参数，并叠加反电动势源构建电机多端口模型；接着考虑IGBT开关过程的高频寄生参数，建立双三相DC-AC逆变器的多端口传导EMI模型；最后利用各功能模块端口间的级联特性，将上述模型级联形成系统级瞬态传导EMI源模型。通过时域仿真与实验测量对比，实现EML系统瞬态传导干扰时频域特性的准确预测，为EMI滤波器优化设计提供理论支撑。

### 数学公式


**公式1**: $$$C_{f1}(u) = ku(t)$$$

*超级电容充电瞬态支路中的时变电容模型，用于拟合充电初期端电压随时间非线性变化的特性，其中k为比例系数，u(t)为端电压。*


**公式2**: $$$Z_{CM}(\omega), Z_{DM}(\omega)$$$

*通过阻抗分析仪测量的双三相直线电机共模与差模阻抗频率响应曲线，用于提取等效RLC电路的谐振峰谷参数。*


### 算法步骤

1. 步骤1：超级电容多端口建模。将充电过程等效为瞬态支路（R0串联固定电容Cf0与时变电容Cf1(u)）、电压平衡支路（R1串联C1）和自放电支路（Rleak）；放电过程等效为含线路寄生参数（L1, L2, R3, R4）与负载（L3, R5）的脉冲电源模型，通过开关K1/K2实现充放电状态切换。

2. 步骤2：直线电机多端口建模。采用阻抗测量法获取电机定子绕组的DM与CM阻抗曲线，根据曲线上的并联与串联谐振频率点提取RLC等效参数；在每相绕组及中性点添加反电动势源（Ea, Eb, Ec）以模拟基频运行特性，双三相结构通过两组等效电路并联实现。

3. 步骤3：逆变器多端口建模。基于双三相逆变器拓扑，提取IGBT模块及母线的寄生电感/电容参数；利用各桥臂结构对称性，仅对单相桥臂进行详细EMI建模，再通过并联扩展至完整双三相结构，以准确反映开关过程产生的高du/dt与di/dt干扰。

4. 步骤4：系统级级联与仿真。将超级电容、逆变器、直线电机的多端口模型按实际电气连接进行端口级联；设置SPWM控制策略（30°电角度差，6kHz开关频率）与充放电时序（0-6s恒流充电，6s起每次放电2s、间隔1s）；运行瞬态时域仿真，提取直流侧LISN处的DM/CM干扰电流波形，并通过FFT转换至频域进行频谱分析。


### 关键参数

- **超级电容额定容量**: 1 F（低压实验平台）/ 33 F（典型EML系统）

- **直流母线电压**: 350 V（实验）/ 0-360 V变化范围

- **逆变器开关频率**: 4 kHz（实验验证）/ 6 kHz（典型系统仿真）

- **电机转速**: 3600 r/min

- **SPWM控制电角度差**: 30°

- **单次放电持续时间**: 2 s

- **放电间隔时间**: 1 s

- **仿真总时长**: 15 s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 低压实验平台充电/放电传导干扰验证 | 在350V/1F超级电容与PMSM构成的低压平台上，对比恒流与恒压充电模式下的CM/DM频谱。恒压充电CM干扰比恒流高约5 dB（主频点），DM干扰高约8 dB。放电过程端电压仿真与实测波形高度吻合，1秒内完成放电。 | CM频谱包络与实测一致，最大误差<5 dB；DM低频段吻合良好，15 MHz处因电缆与设备串联谐振及未建模均压板导致误差约15 dB。 |

| 典型EML系统瞬态放电时域特性 | 33F超级电容经双三相逆变器驱动直线电机，仿真显示单次放电期间端电压波动约20 V，放电电流峰值达7 kA。逆变器输出相电流峰值达8 kA，超前与滞后相电流满足30°电角度差，线电压波形符合实际SPWM调制特征。 | 时域电流波形与文献实测数据归一化对比完全一致，验证了多端口级联模型在瞬态大电流工况下的动态响应精度。 |

| 典型EML系统频域传导干扰预测 | 提取直流侧LISN处10 kHz-10 MHz频段的DM/CM干扰频谱。DM干扰在10-150 kHz及高频段最大误差<3 dB（150-300 kHz因分段测量跳变误差约13 dB）；CM干扰在10-150 kHz最大误差<5 dB。高频段（>10 MHz）干扰幅值因寄生参数串联谐振而上升。 | 相比传统频域建模方法，本方法预测精度提升3-6 dB，且能准确拟合高频噪声峰值点，低频段干扰幅值随频率升高逐渐衰减。 |



## 量化发现

- 超级电容单次放电端电压变化量约为20 V，放电电流峰值可达7-8 kA。
- 恒压充电模式下的CM干扰主频点幅值比恒流充电高约5 dB，DM干扰高约8 dB。
- DM传导干扰预测最大误差在10-150 kHz及高频段均<3 dB，CM干扰在10-150 kHz最大误差<5 dB。
- 相比传统频域等效电路建模，本方法在10 kHz-10 MHz全频段预测精度提升3-6 dB。
- 15 MHz处DM干扰仿真与实测误差约15 dB，主要归因于高频串联谐振及未计入均压板寄生参数。
- 双三相逆变器输出相电流满足30°电角度空间差，开关频率设定为6 kHz时系统瞬态响应稳定。


## 关键公式

### 超级电容时变电容模型

$$$C_{f1}(u) = ku(t)$$$

*用于超级电容充电瞬态支路建模，描述充电初期端电压非线性上升特性，k为电压-电容比例系数。*

### 电机阻抗等效RLC模型

$$$Z_{eq}(\omega) = R + j\omega L + \frac{1}{j\omega C}$$$

*基于DM/CM阻抗测量曲线的谐振峰谷点提取，用于构建直线电机高频等效电路，拟合宽频带阻抗特性。*



## 验证详情

- **验证方式**: 实验测量与仿真对比分析（时域波形对比、频域频谱包络对比、误差定量评估）
- **测试系统**: 低压EML实验平台（350V/1F超级电容、LISN、双三相逆变器、永磁同步电机）与典型EML系统仿真模型（33F超级电容、双三相直线电机、6kHz逆变器）
- **仿真工具**: 实验设备：CYBERTEK DP6070高压差分探头、NNBL 8229-HV型LISN、N9020A频谱分析仪、CMDM 8700 CM/DM分离器、RIGOL TDS3054B示波器；仿真平台：基于多端口等效电路级联的时域电路仿真环境（通常为MATLAB/Simulink或PLECS类EMT工具）
- **验证结果**: 时域仿真电压/电流波形与实测高度一致，频域DM/CM干扰频谱包络在10 kHz-10 MHz范围内最大误差控制在5 dB以内（特定频段除外），整体预测精度较传统方法提升3-6 dB，充分验证了级联多端口模型在EML系统瞬态传导EMI源预测中的准确性与工程适用性。

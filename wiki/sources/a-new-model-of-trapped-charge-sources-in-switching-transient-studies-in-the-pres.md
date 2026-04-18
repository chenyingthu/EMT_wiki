---
title: "A New Model of Trapped Charge Sources in Switching Transient Studies in the Presence of Shunt Reactors"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Access;2025;13; ;10.1109/ACCESS.2025.3544109"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Akafi-Mobarakeh 等 - 2025 - A New Model of Trapped Charge Sources in Switching Transient Studies in the Presence of Shunt Reacto.pdf"]
---

# A New Model of Trapped Charge Sources in Switching Transient Studies in the Presence of Shunt Reactors

**作者**: 
**年份**: 2025
**来源**: `02/Akafi-Mobarakeh 等 - 2025 - A New Model of Trapped Charge Sources in Switching Transient Studies in the Presence of Shunt Reacto.pdf`

## 摘要

Insulation coordination studies are of great importance in power grid reliability. In this paper, a new method is proposed for modeling trapped charge sources (TCS) in switching transient studies. The TCS is used to take into account the voltage stored in line capacitors during reclosing operation after fault occurrence. The proposed model is designed based on the active filter concept, thus overcoming the limitations of conventional TCS for simulating transient states in EMTP/ATPDraw. Given the natural frequencies of a transmission line to which the proposed TCS (PTCS) is connected, it injects the appropriate frequencies and eliminates voltage oscillations which limit the use of TCS. To verify the efficiency of the PTCS, it is implemented in a real system with a shunt reactor, and the res

## 核心贡献


- 提出基于有源滤波概念的陷落电荷源模型，消除并联电抗器引发的仿真电压振荡
- 实现含末端并联电抗器线路的最恶劣工况统计开关仿真，提升绝缘配合计算精度
- 突破传统电磁暂态软件局限，支持重合闸暂态过电压的精确建模与计算


## 使用的方法


- [[有源滤波法|有源滤波法]]
- [[j-marti频率相关模型|J-Marti频率相关模型]]
- [[统计开关仿真|统计开关仿真]]
- [[戴维南等值法|戴维南等值法]]
- [[emtp-atpdraw|EMTP/ATPDraw]]


## 涉及的模型


- [[陷落电荷源|陷落电荷源]]
- [[并联电抗器|并联电抗器]]
- [[输电线路|输电线路]]
- [[统计开关|统计开关]]
- [[系统等值阻抗|系统等值阻抗]]


## 相关主题


- [[开关暂态|开关暂态]]
- [[绝缘配合|绝缘配合]]
- [[重合闸过电压|重合闸过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[并联补偿|并联补偿]]


## 主要发现


- 新模型有效消除重合闸前电压振荡，仿真波形平滑且幅值符合预期
- 仿真结果与现场实测数据高度吻合，验证了模型在含电抗器系统中的准确性
- 准确计算线路最大开关过电压，为输电线路绝缘设计提供可靠技术依据



## 方法细节

### 方法概述

提出一种基于有源滤波概念的陷落电荷源（PTCS）新模型，用于解决含末端并联电抗器线路在重合闸仿真中传统TCS引发的电压振荡问题。该方法首先利用EMTP/ATP的LCC子程序提取输电线路的J-Marti频率相关模型参数（波阻抗与权函数），结合并联电抗器的阻抗特性，在拉普拉斯域推导注入电流源的传递函数。该传递函数通过配置零极点抵消线路与电抗器耦合产生的自然频率振荡，使断路器合闸前线路侧电压保持平滑直流。由于ATP的MODEL模块对高阶传递函数支持有限，研究在MATLAB中预先计算时域电流波形，并以100 kHz采样率提取43,000个数据点，通过ATP内置的MODEL编程块在每一步仿真中注入，从而实现高精度统计开关仿真。

### 数学公式


**公式1**: $$$V_k(s) = \frac{V_0}{s}$$$

*设定断路器合闸前线路侧期望的平滑直流陷落电压目标，$V_0$为陷落电压幅值（最恶劣工况取1 p.u.）。*


**公式2**: $$$I_s(s) = \frac{V_0}{s[1 + A^2(s)F(s)Z_c(s)]} \left[ \frac{1}{Z_c(s)} - A^2(s)F(s) \right]$$$

*PTCS注入电流的拉普拉斯域传递函数，用于计算消除线路-电抗器自然频率振荡所需的补偿电流。*


**公式3**: $$$F(s) = \frac{-2Z_c^2(s)}{R + Ls + Z_c(s)} + Z_c(s)$$$

*辅助阻抗函数，结合并联电抗器阻抗$(R+Ls)$与线路波阻抗$Z_c(s)$，构建传递函数的分母项。*


**公式4**: $$$Z_c(s) = H \frac{(s + z_1)(s + z_2) \dots (s + z_{n1})}{(s + p_1)(s + p_2) \dots (s + p_{n2})}$$$

*J-Marti模型波阻抗的有理分式拟合表达式，用于将频域参数转换为拉普拉斯域多项式以便解析推导。*


### 算法步骤

1. 在EMTP/ATPDraw中搭建含末端并联电抗器的输电线路模型，配置J-Marti频率相关线路模型并运行LCC例程。

2. 从LCC输出文件中提取三相线路的波阻抗$Z_c(s)$与传播权函数$A(s)$的有理分式拟合系数（包含分子/分母阶数及零极点位置）。

3. 将提取的系数代入公式(13)和(14)，在拉普拉斯域构建PTCS的传递函数，该函数以目标平滑直流电压$V_0/s$为约束，结合电抗器阻抗与线路历史项推导所需注入电流$I_s(s)$。

4. 在MATLAB中对传递函数进行拉普拉斯逆变换，生成时域电流波形$I_s(t)$，按10 μs仿真步长（100 kHz采样率）离散化，截取前43,000个采样点以适配ATP内存限制。

5. 将离散电流数据写入ATP的MODEL模块脚本（Type 60接口），利用类FORTRAN语法定义数组与条件判断逻辑，在断路器合闸前持续向线路注入补偿电流，合闸后自动切换至主电源。

6. 配置统计开关（STAT）模块，设定合闸时间概率分布，执行大规模蒙特卡洛仿真以获取绝缘配合最恶劣工况下的过电压统计分布。


### 关键参数

- **采样频率**: 100 kHz (对应10 μs仿真步长)

- **导入样本数**: 43,000个

- **并联电抗器容量**: 121 MVAr (占空载无功75%)

- **优化补偿度**: 53%

- **目标陷落电压幅值**: 1 p.u. (最恶劣工况)

- **MODEL接口类型**: Type 60

- **线路模型**: J-Marti频率相关模型 (LCC例程)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含75%补偿并联电抗器的400kV线路重合闸仿真 | PTCS成功消除合闸前电压振荡，波形平滑。统计开关仿真显示，含电抗器时过电压均值为1.573 p.u.，2.05倍标准差为0.976；不含电抗器时均值为1.632 p.u.，2.05σ为1.899。 | 较传统ATP默认TCS模型，彻底消除合闸前兆伏级虚假振荡，过电压分布离散度降低约48.6%（2.05σ从1.899降至0.976）。 |

| 电抗器补偿度优化对比（75% vs 53%） | 75%补偿下工频过电压叠加导致暂态过电压略升；降至53%补偿后，最大过电压分布改善约2%，实现暂态与稳态过电压的双目标优化。 | 优化后最大过电压幅值降低2%，验证了PTCS模型在电抗器容量整定与绝缘配合协同设计中的有效性。 |

| 765kV实际线路现场数据验证（Lakeville至Kammer站） | 仿真计算最大过电压为2.0 p.u.，现场实测为1.96 p.u.；PTCS初始电压0.645 p.u.与合闸前瞬时电压完全吻合，振荡波形趋势高度一致。 | 与现场录波数据对比，最大过电压计算误差仅约2%，显著优于传统方法在含电抗器工况下的发散结果。 |



## 量化发现

- 仿真最大过电压与现场实测值偏差仅约2%（2.0 p.u. vs 1.96 p.u.）。
- 引入PTCS后，含并联电抗器线路的统计过电压均值降至1.573 p.u.，较无电抗器工况（1.632 p.u.）降低约3.6%。
- 2.05倍标准差从1.899显著降至0.976，表明过电压分布离散度大幅收敛，绝缘配合评估更可靠。
- 将电抗器补偿度从75%优化至53%时，最大过电压幅值进一步改善2%。
- 模型采用100 kHz采样率与43,000个预计算样本，在ATP MODEL模块限制下实现高精度时域注入，无额外数值振荡。


## 关键公式

### PTCS注入电流传递函数

$$$I_s(s) = \frac{V_0}{s[1 + A^2(s)F(s)Z_c(s)]} \left[ \frac{1}{Z_c(s)} - A^2(s)F(s) \right]$$$

*用于计算消除线路-电抗器自然频率振荡所需的补偿电流，是PTCS模型的核心推导公式。*

### 目标平滑电压约束方程

$$$V_k(s) = \frac{V_0}{s}$$$

*设定断路器合闸前线路侧期望的直流陷落电压，作为有源滤波设计的参考基准。*

### 辅助阻抗函数

$$$F(s) = \frac{-2Z_c^2(s)}{R + Ls + Z_c(s)} + Z_c(s)$$$

*结合并联电抗器阻抗与线路波阻抗，构建传递函数的分母项，决定滤波器的零极点配置。*



## 验证详情

- **验证方式**: 现场实测数据对比分析 + 统计开关仿真验证
- **测试系统**: 伊朗南部实际400 kV电网（线路SA913，末端接121 MVAr并联电抗器）；美国AEP 765 kV线路（Lakeville至Kammer站，330英里，300 MVAr电抗器，350 Ω合闸电阻）
- **仿真工具**: EMTP/ATPDraw（含LCC例程与MODEL编程块）、MATLAB（时域波形预计算）
- **验证结果**: PTCS模型成功消除传统方法在含并联电抗器线路中引发的合闸前电压振荡，生成平滑的陷落电荷电压。统计仿真结果与现场录波数据高度吻合，最大过电压计算误差控制在2%以内，验证了该模型在绝缘配合最恶劣工况评估中的高精度与工程实用性。

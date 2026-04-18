---
title: "Accurate simulation model for a three-phase ferroresonant circuit in EMTP–ATP"
type: source
authors: ['Mi Zou']
year: 2018
journal: "Electrical Power and Energy Systems, 107 (2018) 68-77. doi:10.1016/j.ijepes.2018.11.016"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/05/j.ijepes.2018.11.016.pdf.pdf"]
---

# Accurate simulation model for a three-phase ferroresonant circuit in EMTP–ATP

**作者**: Mi Zou
**年份**: 2018
**来源**: `05/j.ijepes.2018.11.016.pdf.pdf`

## 摘要

Accurate simulation model for a three-phase ferroresonant circuit in College of Automation, Chongqing University of Posts and Telecommunications, Chongqing 400065, China Key Laboratory of Industrial Internet of Things and Networked Control, Ministry of Education, Chongqing University of Posts and Telecommunications, Chongqing 400065, This study presents a simulation model for a ferroresonant circuit. The proposed model includes a transformer model and a vacuum circuit breaker (VCB) model. Hyster

## 核心贡献


- 提出基于JA磁滞模型与磁电对偶变换的三相五柱变压器模型，精确刻画铁芯非线性
- 建立含截流、耐压与高频熄弧特性的真空断路器模型，提升开关暂态仿真精度
- 在EMTP-ATP中集成组件构建铁磁谐振仿真平台，实现多稳态振荡预测


## 使用的方法


- [[jiles-atherton磁滞模型|Jiles-Atherton磁滞模型]]
- [[磁电对偶变换|磁电对偶变换]]
- [[model语言与tacs开关|MODEL语言与TACS开关]]
- [[分岔分析|分岔分析]]
- [[相平面法|相平面法]]
- [[庞加莱映射|庞加莱映射]]


## 涉及的模型


- [[三相五柱变压器|三相五柱变压器]]
- [[真空断路器-vcb|真空断路器(VCB)]]
- [[ja磁滞电抗器|JA磁滞电抗器]]
- [[铁磁谐振电路|铁磁谐振电路]]
- [[绕组杂散电容模型|绕组杂散电容模型]]


## 相关主题


- [[铁磁谐振|铁磁谐振]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器非线性建模|变压器非线性建模]]
- [[开关暂态|开关暂态]]
- [[emtp-atp|EMTP-ATP]]


## 主要发现


- 基波与次谐波铁磁谐振实验验证表明，仿真与实测波形相似度均大于0.9
- 分岔图、相平面与庞加莱分析证实模型能准确复现铁磁谐振的多稳态特性
- 考虑截流与高频熄弧的断路器模型显著提升了开关暂态过电压的预测精度



## 方法细节

### 方法概述

本文提出一种在EMTP-ATP中精确模拟三相铁磁谐振的综合方法。首先，基于Jiles-Atherton (JA) 磁滞模型与磁电对偶变换原理，构建了三相五柱变压器的低频等效电路模型，将铁芯磁路（铁轭、铁芯柱）转化为对偶电气网络，精确刻画铁芯非线性磁滞特性与拓扑结构。其次，针对开关暂态对初始条件的敏感性，开发了包含截流水平、介质耐压恢复特性及高频电流熄弧能力的真空断路器(VCB)模型，并通过MODEL语言与TACS开关实现动态逻辑控制。最后，将变压器、VCB、串并联杂散电容与电源集成于EMTP-ATP平台，构建完整的铁磁谐振仿真电路。采用分岔分析、相平面轨迹与庞加莱映射等非线性动力学方法，对基波与次谐波谐振的多稳态特性进行深度验证与机理剖析。

### 数学公式


**公式1**: $$$i_{man} = i_{msat} \left[ \coth\left(\frac{i_{eff}}{a}\right) - \frac{a}{i_{eff}} \right]$$$

*JA模型无磁滞磁化曲线方程，用于计算有效电流对应的理想磁化电流*


**公式2**: $$$\frac{di_{man}}{di_{eff}} = \frac{i_{msat}}{a} \left[ \left(\frac{a}{i_{eff}}\right)^2 - \text{csch}^2\left(\frac{i_{eff}}{a}\right) \right]$$$

*无磁滞磁化曲线的微分形式，用于求解磁导率变化率*


**公式3**: $$$\frac{di_m}{dH} = \frac{i_{man} - i_m}{k/(1-c)} + c \frac{di_{man}}{di_{eff}} \quad (i>0)$$$

*JA磁滞微分方程，描述磁化电流随磁场强度的非线性变化轨迹*


**公式4**: $$$\bar{i}_{ch} = (2 f I_{load})^q$$$

*VCB截流水平计算公式，决定断路器提前截断电流的阈值*


**公式5**: $$$\bar{U}_b = A (t - t_{open}) + B$$$

*VCB介质耐压恢复特性方程，描述触头分离后间隙击穿电压随时间的线性增长*


**公式6**: $$$\frac{d\bar{i}}{dt} = C (t - t_{open}) + D$$$

*VCB高频电流熄弧能力方程，决定高频过零时电弧重燃或熄灭的临界条件*


### 算法步骤

1. 初始化标志位(Flag)与状态变量(State)，实时采集断路器两端瞬时电流$i(t)$与节点电压$U(t)$。

2. 根据式(4)-(6)计算当前时刻的截流阈值$\bar{i}_{ch}$、平均耐压值$\bar{U}_b$及高频熄弧率$d\bar{i}/dt$。

3. 第一级判断（截流检测）：若$t \ge t_{open}$，计算电流变化斜率；当$i(t) \le \bar{i}_{ch}$时触发截流，置Flag=1，State=0。

4. 第二级判断（高频熄弧评估）：检测电流过零趋势，若$i(t) - i(t-\Delta t) \le 0$且$di/dt \le \text{Slope}$，且当前State=0，则进入第三级判断。

5. 第三级判断（介质耐压击穿）：比较瞬时电压与耐压阈值，若$U(t) \ge \bar{U}_b$，则判定发生重击穿，置State=1。

6. 输出最终State参数至TACS开关，控制断路器支路的通断状态，完成暂态过程迭代。


### 关键参数

- **JA饱和电流_im_sat**: 6.84×10^3 A

- **JA形状参数_a**: 3.40 A/m

- **JA磁滞系数_c**: 0.55

- **JA耦合系数_alpha**: 1.81×10^-3

- **VCB耐压斜率_A**: 0.47×10^-6 V/s

- **VCB初始耐压_B**: 0.69×10^3 V

- **VCB熄弧斜率_C**: 1.00×10^12 A/s^2

- **VCB初始熄弧率_D**: 190.00×10^6 A/s

- **变压器变比**: 14:14

- **高压侧对地电容_CHG**: 26.25 μF

- **低压侧对地电容_CLG**: 56.50 μF

- **高低压间电容_CHL**: 23.50 μF

- **相间电容_CPH**: 7.25 μF



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 基波铁磁谐振 | 在$C_s=683\mu\text{F}$、$C_g=10\mu\text{F}$、$E_s=11.77\text{V}$条件下激发。实验稳态峰值电压为19.00V、14.21V、19.64V；仿真值为19.66V、14.82V、19.99V。过电压倍数实验值为1.61、1.21、1.67 p.u.，仿真值为1.67、1.26、1.70 p.u.。相平面轨迹闭合，庞加莱截面为单点，证实为工频周期振荡。 | 稳态电压峰值误差分别为3.47%、4.29%、1.78%，均小于5%；波形相似度>0.9，显著优于传统多项式/分段线性铁芯模型在暂态过程中的失真表现。 |

| 次谐波铁磁谐振 | 在$C_s=680\mu\text{F}$、$C_g=5\mu\text{F}$、$E_s=31.29\text{V}$条件下激发。实验稳态峰值电压为48.77V、32.18V、35.92V；仿真值为51.16V、30.93V、34.21V。过电压倍数实验值为1.56、1.03、1.15 p.u.，仿真值为1.64、0.99、1.09 p.u.。A相庞加莱截面出现3个离散点，相平面呈三分支闭合，验证3倍工频周期特性；B/C相保持单点周期特性。 | 稳态电压峰值误差分别为4.90%、3.88%、4.76%，均小于5%；成功复现次谐波多稳态分岔特征，高频谐波成分预测精度较未考虑截流/熄弧的模型提升显著。 |



## 量化发现

- 基波与次谐波铁磁谐振仿真波形与实验数据的相似度均大于0.9。
- 稳态电压峰值仿真误差严格控制在5%以内（最大误差4.90%）。
- 过电压倍数预测偏差小于0.06 p.u.（如A相基波实验1.61 p.u. vs 仿真1.67 p.u.）。
- 庞加莱映射准确复现多稳态特征：基波谐振截面为1个点，次谐波A相截面为3个点，与理论周期倍数完全一致。
- 考虑截流与高频熄弧的VCB模型使开关暂态过电压预测精度显著提升，避免了传统理想开关模型导致的数值振荡与物理失真。


## 关键公式

### Jiles-Atherton磁滞微分方程

$$$\frac{di_m}{dH} = \frac{i_{man} - i_m}{k/(1-c)} + c \frac{di_{man}}{di_{eff}}$$$

*用于在EMTP-ATP中构建变压器铁芯非线性磁滞电抗器，精确模拟磁通-电流动态关系*

### VCB介质耐压恢复方程

$$$\bar{U}_b = A (t - t_{open}) + B$$$

*用于判断断路器触头分离后间隙是否发生重击穿，是开关暂态过电压仿真的核心判据*

### VCB高频熄弧能力方程

$$$\frac{d\bar{i}}{dt} = C (t - t_{open}) + D$$$

*用于评估高频电流过零时电弧的熄灭或重燃概率，决定截流后的暂态振荡衰减特性*



## 验证详情

- **验证方式**: 实验室物理实验与EMTP-ATP数字仿真对比验证，结合非线性动力学分析（相平面轨迹、庞加莱映射、分岔分析）
- **测试系统**: 225 VA三相Y/Y接法降压变压器（额定电压15/15 V），串联/并联电容网络，真空断路器，0-220V调压器，无负载工况
- **仿真工具**: EMTP-ATP（内置MODEL语言与TACS开关），Tektronix A622电流探头，数字示波器
- **验证结果**: 模型在基波与次谐波工况下均实现高精度复现，稳态误差<5%，波形相似度>0.9，成功揭示铁磁谐振的多稳态与分岔特性，验证了JA磁滞模型与精细化VCB模型在电磁暂态仿真中的有效性。

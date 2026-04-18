---
title: "Characteristic Analysis of High-frequency Resonance of Flexible High Voltage Direct Current and Rese"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Guo 等 - 2020 - Characteristic Analysis of High-frequency Resonance of Flexible High Voltage Direct Current and Rese.pdf"]
---

# Characteristic Analysis of High-frequency Resonance of Flexible High Voltage Direct Current and Rese

**作者**: CNKI
**年份**: 2022
**来源**: `10/Guo 等 - 2020 - Characteristic Analysis of High-frequency Resonance of Flexible High Voltage Direct Current and Rese.pdf`

## 摘要

Time delay is the inherent feature of MMC-based HVDC transmission system which makes the output impedance of MMC presented “negative resistance and inductance” characteristics in high frequency ranges. Those characteristics may easily cause high-frequency resonant instability interacting with the capacitance feature of long AC lines. Firstly, the equivalent model of MMC and AC lines were derived. Secondly, the impedance model of MMC under dq coordinate was established considering the factors such as internal dynamic processes of MMC, PLL, circulating current suppression controller, time delay, etc. Thirdly, the effect of corresponding factors on impedance matrix in high-frequency ranges as well as resonant characteristics was analyzed. Fourthly, a damping control strategy was proposed to s

## 核心贡献


- 建立计及延时与多控制环节的MMC dq坐标系高频阻抗模型
- 揭示链路延时致负阻感特性与长线路电容交互引发高频振荡机理
- 提出高频振荡阻尼控制策略并完成基于简化模型的参数整定设计


## 使用的方法


- [[阻抗建模|阻抗建模]]
- [[状态空间法|状态空间法]]
- [[小信号分析|小信号分析]]
- [[dq坐标系变换|dq坐标系变换]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[阻尼控制|阻尼控制]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[换流变压器|换流变压器]]
- [[交流输电线路|交流输电线路]]
- [[锁相环|锁相环]]
- [[环流抑制控制器|环流抑制控制器]]
- [[双闭环控制器|双闭环控制器]]


## 相关主题


- [[vsc-model|VSC]]
- [[高频振荡|高频振荡]]
- [[阻抗特性分析|阻抗特性分析]]
- [[系统稳定性|系统稳定性]]
- [[阻尼控制|阻尼控制]]
- [[电压前馈|电压前馈]]


## 主要发现


- 链路延时使MMC高频阻抗呈负阻感特性，易与长线路电容交互失稳
- 所提阻尼策略能有效重塑高频阻抗特性，消除负阻感并抑制振荡
- 电磁暂态仿真验证了阻尼控制器参数设计的正确性及策略有效性



## 方法细节

### 方法概述

本文采用基于dq坐标系的阻抗建模法，结合状态空间与小信号分析，系统研究MMC-HVDC高频振荡机理。首先建立包含子模块电容动态、桥臂电感、换流变及直流线路的MMC主电路状态空间模型，并转化为传递函数形式。随后，将锁相环(PLL)、双闭环控制器、环流抑制控制器及系统固有链路延时($G_{de}=e^{-T_{de}s}$)纳入控制回路，推导MMC高频导纳/阻抗矩阵。通过广义奈奎斯特判据分析回路矩阵特征根轨迹，揭示延时、运行功率、电压前馈滤波器对“负阻感”特性及谐振频率的影响规律。针对高频振荡，提出基于简化MMC模型的阻尼控制策略，设计二阶/三阶带通-低通组合控制器重塑高频阻抗相位，确保阻抗交点处相位差小于180°，最终通过电磁暂态仿真验证策略有效性。

### 数学公式


**公式1**: $$$$\frac{\mathrm{d}\Delta \boldsymbol{x}_{\text{mmc}}}{\mathrm{d}t} = \boldsymbol{A}_{\text{mmc}} \cdot \Delta \boldsymbol{x}_{\text{mmc}} + \boldsymbol{B}_{\text{mmc}} \cdot \Delta \boldsymbol{u}_{\text{mmc}}$$$$

*MMC主电路在dq坐标系下的线性化状态空间方程，用于描述交直流侧电气动态*


**公式2**: $$$$\Delta i_{\text{sdq}} = \boldsymbol{M}_1 \cdot \Delta e^*_{\text{vdq}} + \boldsymbol{M}_2 \cdot \Delta u^*_{\text{cirdq}} + \boldsymbol{M}_3 \cdot \Delta u_{\text{sdq}}$$$$

*交流侧电流与参考电压、环流控制及PCC电压的传递函数关系*


**公式3**: $$$$Y_{\text{mmc}} = T_{p1}^{-1} ( E_{2\times2} - G_{de} N_1 M_8 )^{-1} N_2 \cdot (T_{p1} + T_{p2}T_{\text{PLL}}) + T_{p3}T_{\text{PLL}}$$$$

*计及链路延时$G_{de}=e^{-T_{de}s}$的MMC输出导纳矩阵完整表达式*


**公式4**: $$$$L = Y_{\text{mmc}} Z_{\text{sys}}$$$$

*系统回路矩阵，用于广义奈奎斯特稳定性判据分析*


**公式5**: $$$$Z_{\text{mmc}} = \frac{R_{\text{eq}} + L_{\text{eq}} s + G_i \cdot e^{-T_{de} s}}{1 + (G_i F_{\text{damp}} - G_{\text{ffw}}) \cdot e^{-T_{de} s}}$$$$

*加入阻尼控制器$F_{\text{damp}}$后的简化MMC单端口阻抗模型*


**公式6**: $$$$F_{\text{damp}} = \frac{k_s s}{s + 2\pi f_{\text{HPF}}} \cdot \frac{2\pi f_{\text{LPF1}}}{s + 2\pi f_{\text{LPF1}}} \cdot \frac{2\pi f_{\text{LPF2}}}{s + 2\pi f_{\text{LPF2}}}$$$$

*三阶高频振荡阻尼控制器传递函数，用于重塑阻抗相位特性*


### 算法步骤

1. 步骤1：建立MMC主电路12阶状态空间模型，选取直流电压、子模块电容交直流分量、直流/交流电流及环流为状态变量，推导至传递函数矩阵形式。

2. 步骤2：构建控制系统小信号模型，包含PLL动态($F_{\text{PLL}}(s)$)、功率外环、电流内环解耦控制、二倍频环流抑制控制器，并引入链路延时环节$G_{de}=e^{-T_{de}s}$。

3. 步骤3：通过坐标变换矩阵($T_{p1}, T_{p2}, T_{p3}$)将电气dq坐标系与控制系统dq坐标系耦合，推导计及延时的MMC导纳矩阵$Y_{\text{mmc}}$及其逆阻抗矩阵$Z_{\text{mmc}}$。

4. 步骤4：建立交流线路20段π型等效模型，计算系统侧阻抗$Z_{\text{sys}}$，构建回路矩阵$L=Y_{\text{mmc}}Z_{\text{sys}}$，利用广义奈奎斯特判据绘制特征根轨迹，识别包围(-1, j0)点的失稳频段。

5. 步骤5：忽略子模块电容高频波动，将MMC简化为$R_{\text{eq}}+L_{\text{eq}}s$串联结构，推导含阻尼控制器的单端口阻抗表达式，明确$F_{\text{damp}}$对阻抗幅值与相位的调节机理。

6. 步骤6：设计三阶阻尼控制器结构(高通+双低通)，通过扫参分析$k_s$、$f_{\text{HPF}}$、$f_{\text{LPF1}}$、$f_{\text{LPF2}}$对700Hz与1.8kHz关键频点相位差的影响，协调优化参数使交点相位差<180°。

7. 步骤7：在电磁暂态仿真平台搭建详细MMC-HVDC模型，设置550μs延时、功率阶跃及单相接地故障工况，投入阻尼控制器验证振荡抑制效果与故障穿越能力。


### 关键参数

- **链路延时范围**: 350~550 μs

- **PLL参数**: $k_{p\text{PLL}}=0.001$, $k_{i\text{PLL}}=0.01$

- **电流内环参数**: $k_{pi}=137$, $k_{ii}=4124$

- **环流抑制参数**: $k_{p\text{cir}}=100$, $k_{i\text{cir}}=2000$

- **电压前馈滤波器**: 一阶低通，带宽400Hz

- **阻尼控制器增益**: $k_s=0.01\sim0.03$

- **阻尼控制器带宽**: $f_{\text{HPF}}=30\text{Hz}$, $f_{\text{LPF1}}=300\text{Hz}$, $f_{\text{LPF2}}=1000\text{Hz}$

- **交流线路参数**: 500kV/118km, $r=0.0147\Omega/\text{km}$, $l=0.8047\text{mH}/\text{km}$, $c=14.354\text{nF}/\text{km}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 链路延时对高频振荡的影响 | 在无功功率为0、电压前馈带宽400Hz条件下，当延时增至165μs时系统特征根开始顺时针包围(-1, j0)点失稳；350μs延时下谐振频率约为1850Hz；550μs延时下谐振频率降至约720Hz。 | 相比无延时工况，550μs延时使系统高频阻抗相位在700Hz附近突破90°，呈现显著负阻感特性，失稳阈值降低至165μs。 |

| 电压前馈策略对比 | 直接电压前馈在1.8kHz附近引发强烈振荡；采用400Hz一阶低通滤波器或取消前馈后，振荡频率转移至695Hz附近，且无前馈工况的相位裕度更优。 | 低通滤波方案将1.8kHz负阻频段压缩至低频，但700Hz附近相位差仍接近临界值；无前馈方案稳定性相对提升约12°相位裕度。 |

| 三阶阻尼控制器抑制效果 | 在550μs延时、0.5pu有功工况下，投入三阶阻尼控制器($k_s=0.01$)后，1.8kHz处相位差由185°降至177°，0.65kHz处由181°降至164°；0.63s投入控制器后，系统高频振荡在0.15s内完全衰减，1.0s单相接地故障期间未引发二次振荡。 | 相比二阶控制器(1.8kHz相位差196°)，三阶结构使关键频点相位差降低9°~17°，成功将阻抗交点相位差控制在180°安全边界内，振荡抑制时间缩短至传统滤波方案的1/3。 |



## 量化发现

- MMC-HVDC系统链路延时临界失稳阈值为165μs，超过该值即呈现多频段负阻感特性
- 350μs延时对应高频谐振频率约1850Hz，550μs延时对应谐振频率约720Hz
- 直接电压前馈引发1.82kHz振荡，400Hz低通滤波或无前馈将振荡频率转移至695Hz附近
- 三阶阻尼控制器($k_s=0.01$)使1.8kHz处相位差从185°降至177°，0.65kHz处从181°降至164°
- 交流线路采用20段π型等效模型可精确模拟2kHz以下高频分布电容特性，误差<2%
- 阻尼控制器投入后，系统功率从0.8pu斜坡降至-1pu期间高频振荡幅值衰减至基值的3%以内


## 关键公式

### 计及延时的MMC导纳矩阵

$$$$Y_{\text{mmc}} = T_{p1}^{-1} ( E_{2\times2} - G_{de} N_1 M_8 )^{-1} N_2 \cdot (T_{p1} + T_{p2}T_{\text{PLL}}) + T_{p3}T_{\text{PLL}}$$$$

*用于分析PLL、环流抑制、电压前馈及链路延时对高频阻抗特性的综合影响*

### 广义奈奎斯特回路矩阵

$$$$L = Y_{\text{mmc}} Z_{\text{sys}}$$$$

*用于判断MMC与交流线路交互系统的稳定性，特征根包围(-1, j0)点即失稳*

### 含阻尼控制的简化阻抗模型

$$$$Z_{\text{mmc}} = \frac{R_{\text{eq}} + L_{\text{eq}} s + G_i \cdot e^{-T_{de} s}}{1 + (G_i F_{\text{damp}} - G_{\text{ffw}}) \cdot e^{-T_{de} s}}$$$$

*用于阻尼控制器参数整定，直观反映$F_{\text{damp}}$对高频阻抗幅相特性的重塑作用*

### 三阶高频阻尼控制器

$$$$F_{\text{damp}} = \frac{k_s s}{s + 2\pi f_{\text{HPF}}} \cdot \frac{2\pi f_{\text{LPF1}}}{s + 2\pi f_{\text{LPF1}}} \cdot \frac{2\pi f_{\text{LPF2}}}{s + 2\pi f_{\text{LPF2}}}$$$$

*通过高通与双低通级联结构，协调优化700Hz与1.8kHz频段的相位裕度，实现宽频振荡抑制*



## 验证详情

- **验证方式**: 电磁暂态仿真(EMT)与理论阻抗分析对比验证
- **测试系统**: 基于渝鄂背靠背柔直工程参数的MMC-HVDC系统，经500kV/118km交流线路接入等效电网，对站采用840kV直流电压源模拟
- **仿真工具**: 电磁暂态仿真软件(如PSCAD/EMTDC或RTDS)
- **验证结果**: 仿真验证了550μs延时下系统存在720Hz高频振荡；投入设计的三阶阻尼控制器后，振荡在0.15s内完全抑制；在0.8pu至-1pu功率斜坡及100ms单相接地故障工况下，系统保持同步稳定，PCC电压恢复迅速，未触发闭锁保护，证实了阻尼参数设计的正确性与工程适用性。

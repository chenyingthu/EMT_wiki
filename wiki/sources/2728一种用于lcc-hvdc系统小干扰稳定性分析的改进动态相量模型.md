---
title: "27&28/一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型.pdf"]
---

# 27&28/一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型

**作者**: 
**年份**: 2026
**来源**: `27&28/一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型.pdf`

## 摘要

With the widespread use of line commutated converter based high voltage direct current (LCC-HVDC) technology, and the couplings between AC and DC systems or the sending and receiving ends becoming more complicated, the stability of hybrid AC/DC power grids is becoming increasingly prominent. The small-signal stability analysis based on the linearized model is an important method to study the stability of hybrid AC/DC power grids. As the key equipment to connect AC and DC in hybrid AC/DC power grids, the linearized model of LCC converter is significant. Most existing literature derive the time-domain linearized model of LCC converter based on the quasi-steady assumption, which may introduce errors into the model. Therefore, this paper proposes a modified dynamic phasor model of LCC converte

## 核心贡献



- 提出考虑换相阀电流正弦变化规律的LCC改进动态相量模型，消除准稳态近似误差。
- 建立单极十二脉动LCC-HVDC系统时域线性化模型，支撑高精度小干扰稳定性分析。
- 揭示整流逆变侧控制器及锁相环参数对交直流混联系统小干扰稳定性的影响机理。


## 使用的方法



- [[动态相量法|动态相量法]]
- [[时域线性化建模|时域线性化建模]]
- [[模态分析法|模态分析法]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型



- [[lcc-model|LCC]]
- [[lcc-model|LCC]]
- [[锁相环-pll|锁相环(PLL)]]
- [[直流输电线路|直流输电线路]]
- [[换流变压器|换流变压器]]


## 相关主题



- [[小干扰稳定性分析|小干扰稳定性分析]]
- [[交直流混联电网|交直流混联电网]]
- [[换相过程建模|换相过程建模]]
- [[控制器参数灵敏度分析|控制器参数灵敏度分析]]


## 主要发现



- 改进模型有效修正传统准稳态假设的幅值与相角误差，显著提升线性化模型计算精度。
- 电磁暂态仿真验证表明所建时域线性化模型在动态响应与特征值分析上具备高准确性。
- 控制器与锁相环参数变化会显著改变系统主导振荡模态，直接影响小干扰稳定裕度。



## 方法细节

### 方法概述

本文提出一种考虑换相过程阀电流实际正弦变化规律的LCC改进动态相量模型，以消除传统准稳态假设引入的线性近似误差。首先基于动态相量理论推导6脉动LCC换流器交直流侧电压电流变换关系，将换相重叠期间的开关函数由线性近似修正为正弦函数，进而获得修正后的交流电流动态相量表达式。随后将该模型扩展至单极12脉动LCC-HVDC系统，分别建立整流器、逆变器、交直流网络、定电流/定关断角控制器及锁相环的时域线性化状态空间方程。通过坐标变换与接口变量匹配，将各子系统线性化模型互联，构建39阶全局时域线性化模型。最后基于该模型进行特征值分析与模态灵敏度计算，揭示控制器与PLL参数对小干扰稳定性的影响机理，并通过电磁暂态仿真验证模型精度。

### 数学公式


**公式1**: $$$S_{ia}' = \frac{\cos \alpha - \cos \omega t}{\cos \alpha - \cos(\alpha + \mu)}$$$

*换相上升沿修正开关函数，描述阀电流按正弦规律上升的实际物理过程*


**公式2**: $$$I_d' = \frac{2\sqrt{3}}{\pi} I_{dc} \frac{\cos \alpha + \cos(\alpha + \mu)}{2}$$$

*改进后交流电流动态相量的d轴分量表达式，用于构建换流器非线性代数模型*


**公式3**: $$$\Delta \dot{x} = A \Delta x + B \Delta u$$$

*全局系统时域线性化状态空间方程，用于小干扰稳定性特征值分析*


### 算法步骤

1. 基于动态相量理论，定义换相重叠角$\mu$与触发角$\alpha$，将传统准稳态假设下的线性开关函数替换为反映阀电流正弦变化规律的修正开关函数$S_{ia}'$。

2. 对修正开关函数进行傅里叶基频分量提取，推导换流母线交流电流动态相量的d轴与q轴分量表达式，建立6脉动LCC改进动态相量模型。

3. 考虑12脉动换流器由两个6脉动单元级联（$N_B=2$），将6脉动模型扩展至整流侧与逆变侧，分别建立包含触发角$\alpha$、超前触发角$\beta$及换相重叠角$\mu$的非线性代数方程组。

4. 在稳态工作点处对换流器模型、交流网络（含滤波器与无功补偿）、直流输电线路（T型等效）、PI控制器及二阶PLL进行泰勒级数一阶线性化，得到各子系统的状态空间矩阵。

5. 通过dq-xy坐标变换矩阵与触发角/相角偏差关系式，统一各子系统接口变量，将状态矩阵、输入矩阵与输出矩阵按系统拓扑互联，组装成39阶全局时域线性化模型。

6. 对全局状态矩阵$A$进行特征值分解，计算参与因子与灵敏度，分析主导振荡模态及控制器/PLL参数变化对系统小干扰稳定裕度的影响。


### 关键参数

- **系统阶数**: 39阶

- **额定直流功率**: 整流侧1010 MW / 逆变侧990 MW

- **换流变压器变比**: 整流侧345/211.42 kV / 逆变侧230/211.42 kV

- **换流变压器短路阻抗**: 0.18 pu

- **交流系统短路比**: 2.5 (整流/逆变侧)

- **交流系统阻抗角**: 整流侧84° / 逆变侧75°

- **控制器参考值**: $I_{dcref}$=1.0 pu, $\gamma_{ref}$=1.0 pu (15°)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 工况1：整流侧直流电流参考值阶跃 | 0.5s时$I_{dcref}$从1.0 pu降至0.95 pu，1.5s恢复至1.0 pu。对比$I_{dcr}$、$U_{dci}$、$U_r$、$P_{dci}$四个电气量的动态响应。 | SS2（改进模型）计算曲线与EMT仿真高度重合，稳态偏差<0.1%；SS1（未改进模型）在暂态过程中出现明显幅值衰减与相位滞后，动态超调误差约1.5%。 |

| 工况2：逆变侧关断角参考值阶跃 | 0.5s时$\gamma_{ref}$从1.0 pu (15°)降至0.95 pu (14.25°)，1.5s恢复。观察系统电压与功率的暂态振荡特性。 | SS2准确跟踪EMT的振荡频率与阻尼特性，幅值误差<0.2%；SS1因忽略换相电流正弦特性导致稳态工作点偏移，相角误差累积达2°以上。 |



## 量化发现

- 传统准稳态模型在正常工况（$\mu \approx 20^\circ$）下动态相量幅值误差约为1%，且相角存在超前或滞后误差。
- 改进模型消除了准稳态线性近似误差，时域动态响应与EMT仿真结果的幅值偏差<0.2%，相位偏差可忽略不计。
- 系统全局线性化模型阶数为39阶，特征值分析表明整流侧/逆变侧PI控制器参数及PLL带宽变化会显著改变主导振荡模态的阻尼比与频率。
- 在CIGRE标准测试系统下，改进模型的小干扰稳定性评估精度较未改进模型提升约一个数量级，有效支撑交直流混联电网的稳定性量化分析。


## 关键公式

### 改进换相开关函数

$$$S_{ia}' = \frac{\cos \alpha - \cos \omega t}{\cos \alpha - \cos(\alpha + \mu)}$$$

*用于描述换相重叠期间阀电流的实际正弦变化规律，替代传统线性近似*

### 改进交流电流d轴动态相量

$$$I_d' = \frac{2\sqrt{3}}{\pi} I_{dc} \frac{\cos \alpha + \cos(\alpha + \mu)}{2}$$$

*构建LCC换流器交直流侧电压电流变换关系的核心表达式*

### 全局时域线性化状态空间方程

$$$\Delta \dot{x} = A \Delta x + B \Delta u$$$

*用于39阶LCC-HVDC系统小干扰稳定性特征值分析与模态灵敏度计算*



## 验证详情

- **验证方式**: 对比分析（线性化模型计算结果 vs 电磁暂态仿真结果）
- **测试系统**: CIGRE直流输电第一标准测试系统（单极12脉动LCC-HVDC）
- **仿真工具**: MATLAB/Simulink（搭建SS1与SS2线性化模型）、PSCAD/EMTDC（搭建高精度电磁暂态模型）
- **验证结果**: 在直流电流与关断角参考值阶跃工况下，改进动态相量模型（SS2）的时域响应曲线与PSCAD/EMTDC电磁暂态仿真结果高度吻合，显著优于未改进模型（SS1），验证了模型在幅值与相角计算上的高精度，满足小干扰稳定性分析需求。

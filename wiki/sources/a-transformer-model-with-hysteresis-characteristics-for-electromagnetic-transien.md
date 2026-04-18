---
title: "A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM"
type: source
year: 2022
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/Wu 等 - 2017 - A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM.pdf"]
---

# A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM

**年份**: 2022
**来源**: `04/Wu 等 - 2017 - A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCADEM.pdf`

## 摘要

In order to research the inrush problems in HVDC transmission projects, a new three-phase transformer model with hysteresis characteristics of PSCAD/EMTDC was presented, which derives from ideas of the transformer model considering hysteresis characteristics in ATP-EMTP, in which it consists of Type96 and BCTRAN. This model added an excitation branch considering hysteresis characteristics based on the classical model. The hysteresis characteristics can be described effectively when using experimental data obtained. The simulation results show that the model reflects excitation characteristics well, and parameters are readily available, it’s easy for users to use it in PSCAD/EMTDC. It also studied the differences of excitation characteristics simulated by the hysteresis loop and the hystere

## 核心贡献


- 提出基于PSCAD的考虑磁滞特性三相变压器自定义电磁暂态仿真模型
- 采用可变电感法构建闭环控制逻辑实现磁滞回线工作点实时跟踪与轨迹转换
- 利用分段线性插值法拟合主次磁滞回线簇仅需最大磁滞回线数据即可建模


## 使用的方法


- [[自定义建模-ud|自定义建模(UD)]]
- [[可变电感法|可变电感法]]
- [[分段线性插值法|分段线性插值法]]
- [[延时比较法|延时比较法]]
- [[闭环控制逻辑|闭环控制逻辑]]


## 涉及的模型


- [[三相变压器|三相变压器]]
- [[换流变压器|换流变压器]]
- [[非线性电感|非线性电感]]
- [[bctran模型|BCTRAN模型]]
- [[umec模型|UMEC模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[励磁涌流|励磁涌流]]
- [[磁滞特性建模|磁滞特性建模]]
- [[高压直流输电|高压直流输电]]
- [[谐波分析|谐波分析]]


## 主要发现


- 采用磁滞中线替代完整磁滞回线模拟时励磁涌流峰值在暂态过程中保持一致
- 完整磁滞回线对涌流稳态过程及高次谐波特性具有更显著的影响
- 所提模型仅需最大磁滞回线数据即可准确反映变压器铁心非线性励磁特性



## 方法细节

### 方法概述

本文提出一种基于PSCAD/EMTDC的考虑铁心磁滞特性的三相变压器自定义电磁暂态仿真模型。该模型在经典变压器模型基础上并联非线性励磁支路，采用可变电感法构建闭环控制逻辑。通过分段线性插值法拟合最大磁滞回线与磁滞中线，并基于主回线数据推导次磁滞回线簇。利用延时比较法实时采集三相电流历史值，判断工作点在磁滞回线上的运动轨迹与转折点位置，实现磁滞回线与磁滞中线的动态切换。模型仅需最大磁滞回线试验数据即可运行，有效解决了PSCAD平台缺乏内置磁滞模型的问题，适用于高压直流换流变压器励磁涌流及谐波特性分析。

### 数学公式


**公式1**: $$$\frac{d_X}{d_{P1}} = \frac{\varphi_X - \varphi_N}{\varphi_{P1} - \varphi_N}$$$

*次磁滞回线上支路磁链差值比例关系，用于线性插值计算当前工作点磁链*


**公式2**: $$$\varphi_X = \frac{\varphi_{main}(\varphi_{P1} - \varphi_N) + d_{P1}\varphi_N}{\varphi_{P1} - \varphi_N + d_{P1}}$$$

*次磁滞回线上支路磁链$\varphi_X$的显式求解公式，结合主回线与中线数据动态更新*


**公式3**: $$$\frac{d\varphi_X}{di} = \frac{d\varphi_X}{dt} \frac{dt}{di} = u / \frac{di}{dt} = L$$$

*可变电感值计算核心关系式，通过磁链对电流的微分或电压电流变化率实时求解电感L*


**公式4**: $$$\begin{cases} I_k(t-\Delta t) - I_k(t-2\Delta t) < 0 \\ I_k(t) - I_k(t-\Delta t) < 0 \end{cases}$$$

*工作点轨迹判断逻辑，通过连续三个仿真步长的电流差分符号判定工作点位于磁滞回线下降段*


### 算法步骤

1. 数据采集与预处理：获取变压器铁心最大磁滞回线及磁滞中线试验数据（如Armco M4硅钢片数据），采用分段线性插值法生成连续的主磁滞回线上下支路与磁滞中线曲线，作为模型基础数据库。

2. 次磁滞回线簇动态拟合：以主磁滞回线上下支路为边界，根据当前工作点与饱和转折点的相对位置，利用线性插值公式动态计算次磁滞回线上下支路的磁链值，构建完整的内部次磁滞回线簇，确保多值特性准确映射。

3. 实时工作点跟踪与状态标识：在EMTDC每个仿真步长内，采集非线性电感三相电流$I_k(t)$，通过延时模块获取$I_k(t-\Delta t)$和$I_k(t-2\Delta t)$。计算相邻时刻电流差值，结合状态标识F1（左转折点）和F2（右转折点）及其历史值F10/F20，实时判定电流增减趋势及峰值点位置。

4. 轨迹切换逻辑判断：根据电流峰值点是否超出主磁滞回线饱和区，执行轨迹切换。若峰值在主环内，工作点沿磁滞回线运动；若进入单值饱和区或满足特定F1/F2状态跳变条件，则切换至磁滞中线循环程序，避免多值区域计算发散。

5. 可变电感闭环控制求解：根据当前磁链$\varphi_X$与电流$i$的微分关系或电压电流变化率计算瞬时电感值$L$，将$L$实时赋给PSCAD中的可变电感元件，形成“电流采样-磁链计算-电感更新-电路求解”的闭环控制回路，完成电磁暂态步进仿真。


### 关键参数

- **变压器额定容量**: 10 MVA

- **额定电压**: 15/30 kV

- **联结组别**: YNd11

- **短路阻抗**: 7.5%

- **空载损耗**: 1 kW

- **系统电压源**: 15 kV, 50 Hz

- **合闸初相角**: 90°

- **仿真步长/延时**: $\Delta t$ (EMTDC默认步长，通常为50μs或更小)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| PSCAD UD模型 vs ATP-EMTP BCTRAN模型空载合闸 | 三相励磁涌流波形趋势一致，A相峰值误差30.6%，B相2.3%，C相4.5%，整体衰减时间误差9.1%。UD模型稳态部分存在合理波动，更符合实际磁滞非线性特征。 | 与ATP-EMTP内置BCTRAN模型相比，峰值平均相对误差约12%，衰减时间误差约9.1%，验证了跨平台磁滞模拟的兼容性。 |

| PSCAD UD模型 vs 实际1kVA变压器试验录波 | B相励磁涌流最大峰值相对误差约1.6%，稳态峰值相对误差约13.3%。稳态电流呈尖顶波，三次谐波占主导，与实际录波高度吻合。 | 与实际物理试验对比，暂态峰值误差控制在2%以内，稳态误差约13.3%，满足工程精度需求。 |

| 磁滞回线(HL) vs 磁滞中线(HML)模拟对比 | 两种模拟方式下暂态励磁涌流峰值基本一致，但HL模型在稳态阶段的电感值动态变化更剧烈，导致高次谐波含量显著高于HML模型。 | HML可快速估算涌流峰值，但HL对稳态谐波特性影响更大，适用于保护定值与谐波分析场景。 |



## 量化发现

- UD模型与BCTRAN模型三相励磁涌流最大峰值平均相对误差约为12%，衰减时间相对误差约为9.1%~10%。
- UD模型与实际变压器试验录波的涌流最大峰值相对误差约为1.6%~2%，稳态峰值相对误差约为13.3%。
- 采用磁滞中线替代磁滞回线时，暂态励磁涌流峰值保持一致，但磁滞回线对稳态过程及高次谐波特性影响显著，三次谐波含量差异明显。
- 模型仅需最大磁滞回线试验数据即可完整拟合次磁滞回线簇，参数获取难度大幅降低，工程实用性提升。


## 关键公式

### 可变电感微分关系式

$$$\frac{d\varphi_X}{di} = L$$$

*用于在EMTDC每个仿真步长内，根据磁链-电流曲线的斜率实时计算非线性电感值，驱动闭环控制逻辑。*

### 次磁滞回线插值求解公式

$$$\varphi_X = \frac{\varphi_{main}(\varphi_{P1} - \varphi_N) + d_{P1}\varphi_N}{\varphi_{P1} - \varphi_N + d_{P1}}$$$

*当工作点位于主磁滞回线内部时，利用该公式动态计算次回线磁链，实现多值磁滞特性的精确映射。*

### 延时比较轨迹判断逻辑

$$$\begin{cases} I_k(t-\Delta t) - I_k(t-2\Delta t) < 0 \\ I_k(t) - I_k(t-\Delta t) < 0 \end{cases}$$$

*通过连续三个步长的电流差分符号判定工作点运动方向（上升/下降段），是磁滞回线实时跟踪的核心判据。*



## 验证详情

- **验证方式**: 跨平台仿真对比(ATP-EMTP BCTRAN/UMEC)与实际变压器空载合闸试验录波对比分析
- **测试系统**: 15kV/50Hz交流系统，10MVA YNd11三相电力变压器，以及1kVA/220/110V小型试验变压器
- **仿真工具**: PSCAD/EMTDC, ATP-EMTP
- **验证结果**: 模型在PSCAD平台成功实现磁滞特性模拟，与ATP-EMTP内置模型及实际试验波形高度吻合，暂态峰值误差控制在2%~12%以内，衰减时间误差约10%。验证了可变电感法与闭环控制逻辑在电磁暂态仿真中的有效性与工程实用性，为HVDC换流变励磁涌流及谐波研究提供了可靠工具。

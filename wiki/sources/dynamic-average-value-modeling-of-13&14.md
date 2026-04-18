---
title: "Dynamic Average-Value Modeling of"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2014.2340870.pdf.pdf"]
---

# Dynamic Average-Value Modeling of

**作者**: 
**年份**: 2014
**来源**: `13&14/files/TPWRD.2014.2340870.pdf.pdf`

## 摘要

—High-voltage direct-current (HVDC) systems play an important role in modern energy grids, whereas efﬁcient and ac- curate models are often needed for system-level studies. Due to the inherent switching in HVDC converters, the detailed switch-level models are computationally expensive for the simulation of large-signal transients and hard to linearize for small-signal frequency-domain characterization. In this paper, a dynamic average-value model (AVM) of the ﬁrst CIGRE HVDC bench- mark system is developed in a state-variable-based simulator, such as Matlab/Simulink, and nodal-analysis-based electromag- netic transient program (EMTP), such as PSCAD/EMTDC. The 12-pulse converters in the HVDC system are modeled with a set of nonlinear algebraic functions that are extracted numerically. The r

## 核心贡献


- 提出基于参数化方法的HVDC动态平均值模型，消除开关细节提升系统级仿真效率
- 在状态变量与节点分析平台中实现十二脉冲换流器非线性代数函数数值提取与建模
- 构建连续型等效模型支持大信号暂态预测，并具备直接线性化用于频域分析的能力


## 使用的方法


- [[动态平均值建模|动态平均值建模]]
- [[参数化方法|参数化方法]]
- [[节点分析法|节点分析法]]
- [[状态变量法|状态变量法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[十二脉冲换流器|十二脉冲换流器]]
- [[换流变压器|换流变压器]]
- [[交流滤波器|交流滤波器]]
- [[直流输电线路|直流输电线路]]
- [[平波电抗器|平波电抗器]]
- [[弱交流电网|弱交流电网]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[大信号暂态分析|大信号暂态分析]]
- [[系统级仿真|系统级仿真]]
- [[动态等值|动态等值]]
- [[换流器控制|换流器控制]]


## 主要发现


- 平均值模型在大信号暂态下与详细开关模型波形高度吻合，验证了时域仿真精度
- 消除开关动作使计算步长显著增大，仿真速度提升数个数量级且大幅降低计算成本
- 模型为连续系统可直接用于小信号线性化分析，但无法捕捉换相失败等开关瞬态现象



## 方法细节

### 方法概述

本文提出一种基于参数化方法的动态平均值模型（AVM），用于CIGRE HVDC基准系统的12脉冲电网换相换流器（LCC）。该方法通过在典型开关周期内对交直流变量进行快速平均，消除高频开关细节，将换流器抽象为多端口开关单元。交流侧变量经同步旋转坐标系（dq变换）转换为准直流信号，直流与交流端口间的非线性代数映射关系通过详细开关仿真在不同工况下数值提取，并以查找表形式存储。利用双6脉冲桥的拓扑对称性，将两个独立子模型折叠为单一等效模块。模型在状态变量型（Matlab/Simulink）与节点分析型（PSCAD/EMTDC）平台中实现，通过并联缓冲电路或引入快极点传递函数解决接口代数环问题，控制子系统保持与原详细模型一致，从而实现连续、高效的系统级大信号暂态仿真。

### 数学公式


**公式1**: $$$$\bar{x}(t) = \frac{1}{T_{sw}} \int_{t-T_{sw}}^{t} x(\tau) d\tau$$$$

*快速平均值定义公式，用于在典型开关周期$T_{sw}$内对任意电压或电流变量进行平均，消除开关纹波。*


**公式2**: $$$$v_{dc} = f_1(\alpha, i_{dc}, v_{ac}), \quad i_{ac} = f_2(\alpha, i_{dc}, v_{ac})$$$$

*参数化AVM核心代数关系，表征直流电压、交流电流与触发角及端口变量的非线性映射。*


**公式3**: $$$$Z_{eq} = \frac{v_{dc}}{i_{dc}}$$$$

*整流器侧等效动态阻抗定义，用于在状态变量仿真中建立端口接口关系。*


**公式4**: $$$$Y_{eq} = \frac{i_{dc}}{v_{dc}}$$$$

*逆变器侧等效动态导纳定义，用于节点分析型仿真中的接口匹配。*


**公式5**: $$$$v_{dc} = 2v_{dc1}, \quad i_{ac} = i_{ac1}$$$$

*基于双6脉冲桥对称性的折叠模型简化关系，将两个子模型合并为单一12脉冲等效模块。*


### 算法步骤

1. 定义典型开关周期$T_{sw}=T_{ac}/12$，建立同步旋转参考坐标系（dq轴）并对齐等效交流源电压矢量，使交流基波分量在坐标系中呈现为直流。

2. 在详细开关级仿真平台中遍历全工况范围（覆盖不同触发角$\alpha$、直流电流$I_{dc}$、交流电压幅值及相位），记录换流器交直流端口的瞬态波形数据。

3. 对记录的原始波形执行快速平均积分运算，提取各工况下的交直流变量平均值及功率因数角$\phi$。

4. 通过数值插值与拟合构建非线性代数函数$f_1, f_2, f_3$，建立输入（$\alpha, i_{dc}, v_{ac}$）到输出（$v_{dc}, i_{ac}, \phi$）的映射关系，并生成多维查找表供AVM调用。

5. 利用双桥串联对称性（$v_{dc}=2v_{dc1}, i_{ac}=i_{ac1}$）将两个独立的6脉冲AVM代数模块折叠为单一12脉冲等效模块，简化计算拓扑。

6. 在目标仿真环境（Simulink/PSCAD）中搭建代数模块，配置接口缓冲电路（大电阻/小电容）或快极点传递函数以消除代数环并确保输入输出因果兼容，最后集成原PI控制器与电压依赖型电流限制逻辑完成系统级联。


### 关键参数

- **短路比(SCR)**: 2.5

- **额定直流电压**: 500 kV

- **额定直流电流**: 2000 A

- **系统基频**: 50 Hz

- **典型开关周期**: $T_{sw} = T_{ac}/12 \approx 1.67$ ms

- **直流侧短路故障电阻**: 0.4 p.u.

- **Simulink求解器配置**: ODE23tb (隐式变步长)

- **PSCAD固定步长**: 110 $\mu$s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 直流参考电流阶跃变化 | 系统在稳态2000A运行，t=0.5s时直流电流参考值突降至1600A，t=1.0s时恢复至2000A。AVM准确预测了整流侧与逆变侧直流电流的下降与回升过程，以及伴随的直流电压上升与交流基波电压微小波动，波形与详细开关模型高度重合，无开关纹波。 | 详细模型需固定步长$\le 10 \mu$s，PSCAD AVM步长放宽至110 $\mu$s，Simulink AVM平均步长达1.6 ms（最大2 ms）。AVM在保证精度的前提下，仿真步长提升11~200倍，CPU计算时间显著降低。 |

| 直流线路中点短路故障 | t=0.5s时直流线路中点施加0.4 p.u.电阻短路，t=1.0s清除故障。AVM准确复现了控制器动作导致的直流电流骤降、整流侧触发角增大与逆变侧触发角减小至最小值的过程，以及故障清除后的系统恢复轨迹。 | AVM预测的直流电压跌落深度、电流限幅值及恢复时间与详细模型误差极小（基波与直流分量偏差<1%），验证了模型在大扰动非线性暂态下的强鲁棒性。 |



## 量化发现

- 仿真步长从详细模型的10 $\mu$s提升至PSCAD AVM的110 $\mu$s及Simulink AVM的1.6~2 ms，时间步长扩大11至200倍。
- 计算效率提升数个数量级，在相同仿真时长（0.5s~1.5s）内，AVM的CPU耗时远低于详细开关模型，适合系统级长时间暂态研究。
- 模型对直流变量与交流基波分量的预测误差<1%，波形高度吻合，但无法捕捉开关频率谐波、换相失败及阀级瞬态现象。
- 折叠模型（Collapsed AVM）相比独立双桥模型减少约50%的代数模块调用次数，进一步降低计算开销。


## 关键公式

### 快速平均值积分公式

$$$$\bar{x}(t) = \frac{1}{T_{sw}} \int_{t-T_{sw}}^{t} x(\tau) d\tau$$$$

*用于定义动态平均值建模的核心数学基础，在12脉冲换流器的典型开关周期内平滑开关纹波。*

### 参数化非线性代数映射方程

$$$$v_{dc} = f_1(\alpha, i_{dc}, v_{ac}), \quad i_{ac} = f_2(\alpha, i_{dc}, v_{ac})$$$$

*在AVM模块中替代详细开关网络，直接根据触发角与端口状态计算交直流端口变量，是模型连续化的核心。*

### 12脉冲折叠等效关系式

$$$$v_{dc} = 2v_{dc1}, \quad i_{ac} = i_{ac1}$$$$

*利用双6脉冲桥的对称性与串联特性，将两个独立子模型合并为单一等效模块，大幅简化系统拓扑与计算量。*



## 验证详情

- **验证方式**: 时域大信号暂态仿真对比分析
- **测试系统**: CIGRE HVDC第一基准系统（单极500kV/1000MW，12脉冲LCC，弱交流电网SCR=2.5）
- **仿真工具**: Matlab/Simulink (SimPowerSystems离散模块与ODE23tb求解器), PSCAD/EMTDC
- **验证结果**: AVM在直流参考电流阶跃与直流线路短路两种大扰动工况下，均能高精度复现详细开关模型的直流与交流基波暂态轨迹。模型消除了开关不连续性，支持更大仿真步长与隐式变步长求解，计算效率显著提升，验证了其在系统级大信号暂态预测中的准确性与工程实用性。

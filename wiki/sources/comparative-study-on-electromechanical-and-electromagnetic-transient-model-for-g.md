---
title: "Comparative study on electromechanical and electromagnetic transient model for grid-connected photov"
type: source
authors: ['未知']
year: 2014
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Sun 等 - 2014 - Comparative study on electromechanical and electromagnetic transient model for grid-connected photov.pdf"]
---

# Comparative study on electromechanical and electromagnetic transient model for grid-connected photov

**作者**: 
**年份**: 2014
**来源**: `10/Sun 等 - 2014 - Comparative study on electromechanical and electromagnetic transient model for grid-connected photov.pdf`

## 摘要

The computing speed of electromagnetic transient model for grid-connected photovoltaic power system is very slow because of its complexity. To solve this problem, a general electromechanical transient model for grid-connected photovoltaic power system is proposed, in which there are not electrical components and high frequency switching device, and it only consists of pure mathematic calculations, is simple and has fast calculation speed. By comparing the simulation results of this electromechanical transient model with electromagnetic transient model in PSCAD/EMTDC, we found that the simulation time is reduced greatly and the results are agreeable basically, which verifies the correctness and validity of the electromechanical transient model. The electromechanical transient model provides

## 核心贡献


- 提出不含电气元件与高频开关器件的并网光伏通用机电暂态模型
- 基于纯数学计算与传递函数构建光伏阵列、MPPT及逆变器外特性
- 屏蔽厂家内部拓扑差异，实现适用于大规模电站仿真的通用化建模


## 使用的方法


- [[传递函数建模|传递函数建模]]
- [[平均值模型|平均值模型]]
- [[pq解耦控制|PQ解耦控制]]
- [[dq坐标变换|dq坐标变换]]
- [[对比仿真验证|对比仿真验证]]


## 涉及的模型


- [[光伏电池|光伏电池]]
- [[mppt控制器|MPPT控制器]]
- [[dc-dc变换器|DC/DC变换器]]
- [[直流母线电容|直流母线电容]]
- [[并网逆变器|并网逆变器]]
- [[机电暂态模型|机电暂态模型]]
- [[电磁暂态模型|电磁暂态模型]]


## 相关主题


- [[机电暂态建模|机电暂态建模]]
- [[大规模光伏电站仿真|大规模光伏电站仿真]]
- [[新能源并网|新能源并网]]
- [[模型降阶|模型降阶]]
- [[仿真加速|仿真加速]]


## 主要发现


- 机电暂态模型仿真波形与电磁暂态模型基本吻合，验证了模型正确性
- 剔除高频开关与详细电路后，仿真计算时间大幅缩短，显著提升效率
- 该通用模型满足大电网机电暂态分析需求，具备大规模工程实用价值



## 方法细节

### 方法概述

本文提出一种面向并网光伏系统的通用性机电暂态建模方法。该方法摒弃了传统电磁暂态模型中复杂的电力电子开关器件与详细电路拓扑，转而基于系统外特性与平均值原理构建纯数学计算模型。模型将光伏阵列、MPPT控制器、DC/DC变换器、直流母线电容及并网逆变器统一抽象为传递函数与代数方程组合，通过dq坐标变换与PQ解耦控制实现外环功率与内环电流的动态描述。该模型屏蔽了不同厂家单级、双级或多级拓扑及具体控制算法的差异，仅依赖标准环境参数与外特性测试参数，可直接嵌入PSASP、PSS/E等商业机电暂态软件，显著提升大规模光伏电站的仿真效率，同时保留满足电网级暂态分析所需的动态精度。

### 数学公式


**公式1**: $$$I = I_{sc}' \left\{1 - C_1 \left[e^{U/(C_2 U_{oc}')} - 1\right]\right\}$$$

*光伏电池通用I-V特性方程，用于根据环境修正参数计算任意电压下的输出电流*


**公式2**: $$$V_{pvm1} = \frac{e^{-\gamma s}}{1 + Ts} V_{pvm} + \Delta V_{pvm}$$$

*MPPT控制器动态模型，采用一阶惯性环节、纯滞后环节与稳态跟踪误差组合表征最大功率点跟踪过程*


**公式3**: $$$\frac{dE_C}{dt} = P_{PV2} - P_{De}, \quad E_C = \frac{1}{2}CV_D^2$$$

*直流母线电容能量守恒方程，通过直流侧与交流侧功率差值积分维持直流电压动态平衡*


**公式4**: $$$i_d = \frac{b_{d2}s^2+b_{d1}s+1}{a_{d2}s^2+a_{d1}s+1}i_{d,ref}$$$

*逆变器内环电流控制传递函数，将dq轴电流参考值映射为实际输出电流，表征电流环动态响应*


### 算法步骤

1. 输入实时环境参数（光照强度S、温度T）至光伏电池通用行为模型，利用式(1)-(6)计算修正后的短路电流、开路电压及最大功率点电压/电流，生成当前工况下的U-I特性曲线。

2. 将光伏阵列最大功率点电压$V_{pvm}$输入MPPT传递函数模型，经纯滞后时间常数$\gamma$与一阶时间常数$T$滤波，叠加固定跟踪误差$\Delta V_{pvm}$，输出MPPT参考电压$V_{pvm1}$。

3. 根据实际系统拓扑类型选择DC/DC变换器映射关系：单级系统直接令$P_{pv2}=P_{pv1}$且$V_{pv1}=V_D$；双级/多级系统引入变换效率$\eta$计算$P_{pv2}=P_{pv1}\eta$，并令$V_{pv1}=V_{pvm1}$。

4. 基于直流母线电容能量守恒微分方程，以直流侧输入功率$P_{PV2}$与交流侧逆变器输出功率$P_{De}$的差值作为积分输入，实时更新直流母线电压$V_D$。

5. 逆变器外环接收直流电压偏差$(V_{D,ref}-V_D)$与无功功率偏差$(Q_{ref}'-Q_e)$，经PI或二阶传递函数生成dq轴电流参考值$I_{d,ref}$与$I_{q,ref}$，并通过饱和函数$Sat(\cdot)$施加电流限幅约束。

6. 逆变器内环将dq轴电流参考值输入二阶传递函数模型，计算实际输出电流$i_d$与$i_q$，经dq/abc反变换与锁相环同步后，作为受控电流源注入电网，完成机电暂态步长迭代。


### 关键参数

- **Um**: 17.4 V (最大功率点电压)

- **Im**: 3.56 A (最大功率点电流)

- **Uoc**: 21.8 V (开路电压)

- **Isc**: 3.78 A (短路电流)

- **Np**: 30 (并联数目)

- **Ns**: 24 (串联数目)

- **γ**: 0.05 s (MPPT纯滞后时间常数)

- **T**: 0.7 s (MPPT一阶时间常数)

- **Kp**: 3 (逆变器外环比例系数)

- **Ki**: 0.5 (逆变器外环积分系数)

- **bd1,bq1**: 0.003 s (内环超前时间常数)

- **ad1,aq1**: 0.0008 s (内环滞后时间常数)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 光照强度阶跃扰动测试 | 系统初始稳态运行于800 W/m²，无功参考设为0 Mvar。在10 s仿真中，光强突增至1500 W/m²。仿真结果显示：有功功率随光强增加快速上升，无功功率经短暂暂态后稳定于0（功率因数保持1）；A相并网电流幅值同步增大，光伏输出功率曲线平滑上升；直流母线电压经历约0.2 s的短暂波动后恢复至设定稳态值。机电暂态模型输出的功率、电流、电压波形与电磁暂态模型高度重合。 | 电磁暂态模型完成10 s仿真耗时46.6 s，机电暂态模型仅耗时4.1 s，计算速度提升约11.4倍，且动态波形吻合度满足工程暂态分析要求。 |



## 量化发现

- 机电暂态模型仿真步长可设为1 ms，而电磁暂态模型因2000 Hz开关频率需设为50 μs，步长扩大20倍
- 相同10 s仿真时长下，机电暂态模型计算时间从46.6 s降至4.1 s，效率提升约11.4倍
- 模型仅需4个标准环境参数（Isc, Uoc, Im, Um）即可完整表征光伏阵列外特性，无需厂家内部电路参数
- MPPT动态特性由纯滞后时间常数γ=0.05 s与一阶时间常数T=0.7 s精确拟合，稳态跟踪误差ΔVpvm可独立设定
- 逆变器内环在简化为PI控制时（ai2=bi2=0），二阶传递函数退化为标准一阶惯性环节，参数ad1=0.0008 s表征电流环响应速度


## 关键公式

### 光伏电池通用I-V特性方程

$$$I = I_{sc}' \left\{1 - C_1 \left[e^{U/(C_2 U_{oc}')} - 1\right]\right\}$$$

*用于任意光照与温度条件下光伏阵列输出特性的快速计算，替代详细半导体物理模型*

### MPPT控制器等效传递函数

$$$V_{pvm1} = \frac{e^{-\gamma s}}{1 + Ts} V_{pvm} + \Delta V_{pvm}$$$

*屏蔽具体MPPT算法（如扰动观察法、电导增量法），统一表征最大功率点跟踪的动态滞后与稳态误差*

### 直流母线能量平衡方程

$$$\frac{dE_C}{dt} = P_{PV2} - P_{De}, \quad E_C = \frac{1}{2}CV_D^2$$$

*连接直流侧与交流侧功率流动的核心环节，用于维持直流电压稳定并反映系统暂态能量交换*

### 逆变器内环电流控制传递函数

$$$i_d = \frac{b_{d2}s^2+b_{d1}s+1}{a_{d2}s^2+a_{d1}s+1}i_{d,ref}$$$

*基于dq坐标系电路方程推导，将复杂PWM开关过程等效为连续传递函数，实现机电暂态尺度的电流动态模拟*



## 验证详情

- **验证方式**: 对比仿真验证（机电暂态模型 vs 详细电磁暂态模型）
- **测试系统**: 双级式并网三相光伏发电系统（含光伏阵列、DC/DC升压电路、直流母线电容、电压源型并网逆变器及PQ解耦控制）
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在光照强度阶跃扰动工况下，两种模型的有功/无功功率、并网相电流、光伏输出功率及直流母线电压动态波形基本一致。机电暂态模型通过纯数学计算与传递函数等效，成功复现了电磁暂态模型的关键机电动态特征，同时避免了高频开关器件带来的小步长限制，验证了其在大规模光伏电站暂态仿真中的正确性、有效性与工程实用性。

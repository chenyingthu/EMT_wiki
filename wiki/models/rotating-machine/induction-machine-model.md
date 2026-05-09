---
title: "感应电机 (Induction Machine)"
type: model
tags: [induction-machine, asynchronous-machine, motor, load, dq0, slip]
created: "2026-04-29"
---

# 感应电机 (Induction Machine)


```mermaid
graph TD
    subgraph Ncmp[感应电机 (Induction Machine)]
        N0[**鼠笼式**: 铸铝/铜条转子]
        N1[**绕线式**: 三相绕组转子]
    end
```


## 定义与概述

感应电机（异步电机）是电力系统中应用主要的旋转电机类型，通过定子绕组产生的旋转磁场与转子感应电流相互作用产生电磁转矩。作为电力系统的主要负荷和工业驱动设备，感应电机在EMT仿真中需要精确建模以准确分析启动暂态、电压跌落响应和系统稳定性。本模型涵盖相域模型、dq0坐标变换模型、 deep bar效应建模，适用于机电暂态和电磁暂态仿真。

## 1. 物理对象概述

### 1.1 功能与分类

感应电机（异步电机）是电力系统中**主要应用的旋转电机**，占总发电容量60%以上：

**按转子结构分类**：
| 类型 | 结构 | 特点 | 应用 |
|------|------|------|------|
| **鼠笼式** | 铸铝/铜条转子 | 结构简单、坚固、成本低 | 通用电动机、风机、泵 |
| **绕线式** | 三相绕组转子 | 可调速、高启动转矩 | 起重机、卷扬机、大型风机 |

**按功率等级**：
- 小型：< 1 kW（家用电器）
- 中型：1 kW - 100 kW（工业驱动）
- 大型：100 kW - 10 MW（泵、压缩机）
- 特大型：> 10 MW（球磨机、矿井提升）

### 1.2 工作原理

**基本电磁原理**：
- 定子三相绕组产生旋转磁场（同步转速 $n_s = 60f/p$）
- 旋转磁场切割转子导条，感应转子电流
- 转子电流与气隙磁场相互作用产生转矩
- 转子转速 $n_r$ 始终低于同步转速（异步运行）

**转差率定义**：
$$s = \frac{n_s - n_r}{n_s} = \frac{\omega_s - \omega_r}{\omega_s}$$

典型运行范围：$s = 0.005 \sim 0.05$（额定负载）

### 1.3 运行激励

**电压激励**：
- 额定电压：380V / 6kV / 10kV（三相）
- 频率：50Hz / 60Hz
- 电压不平衡度：< 2%（正常运行）

## 2. 物理模型与数学描述

### 2.1 相域模型

**定子电压方程**：
$$
v_{abc,s} = R_s i_{abc,s} + \frac{d\psi_{abc,s}}{dt}$$

**转子电压方程**：
$$
v_{abc,r} = R_r i_{abc,r} + \frac{d\psi_{abc,r}}{dt} = 0$$

**磁链方程**：
$$
\psi_{abc,s} = L_{ss}i_{abc,s} + L_{sr}i_{abc,r}$$
$$
\psi_{abc,r} = L_{rs}i_{abc,s} + L_{rr}i_{abc,r}$$

### 2.2 dq0坐标变换模型

**同步旋转坐标系**：
$$
v_{dq0,s} = R_s i_{dq0,s} + \frac{d\psi_{dq0,s}}{dt} + \omega\begin{bmatrix} -\psi_q \\ \psi_d \\ 0 \end{bmatrix}$$

**转子坐标系**（转差频率）：
$$
v_{dq0,r} = R_r i_{dq0,r} + \frac{d\psi_{dq0,r}}{dt} + (\omega - \omega_r)\begin{bmatrix} -\psi_{qr} \\ \psi_{dr} \\ 0 \end{bmatrix} = 0$$

### 2.3 电磁转矩

**转矩公式**：
$$
T_e = \frac{3}{2}p(\psi_d i_q - \psi_q i_d) = \frac{3}{2}pL_m(i_{dr}i_q - i_{qr}i_d)$$

**机械方程**：
$$
J\frac{d\omega_r}{dt} = T_e - T_L - D\omega_r$$

## 3. EMT仿真建模

### 3.1 启动暂态

**启动特性**：
- 启动电流：5-7倍额定电流
- 启动转矩：1.5-2.5倍额定转矩
- 启动时间：取决于惯量和负载

**启动方式**：
- 直接启动
- 星-三角启动
- 软启动器
- 变频器启动

### 3.2 负荷模型

**负荷特性**：
- 恒转矩负载
- 平方转矩负载（风机、泵）
- 恒功率负载

**电压特性**：
$$
P = P_0\left(\frac{V}{V_0}\right)^{\alpha}, \quad Q = Q_0\left(\frac{V}{V_0}\right)^{\beta}$$

典型值：$\alpha = 0.1 \sim 1.2$, $\beta = 1.5 \sim 3.0$

## 4. 适用边界

**适用场景**：
- 电力系统负荷建模
- 电动机启动分析
- 电压稳定性研究
- 暂态稳定分析
- 谐波分析

**模型限制**：
- 集总参数假设
- 磁路饱和忽略或简化
- 温度效应
- 轴承摩擦非线性

## 代表性来源

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Induction Machine Modeling for Real-Time Electromagnetic Transient Simulation | 2016 | 提出适用于实时仿真的感应电机数值优化模型，解决固定时间步长下的数值稳定性问题 |
| Induction Motor Modeling for Electromagnetic Transient Program: A Comparison of Three Methods | 2016 | 系统比较相域、dq0坐标和电压Behind-Reactance三种感应电机EMT建模方法的精度与效率 |
| Real-Time Digital Simulation of Induction Machine with Nonlinear Characteristics | 2004 | 实现考虑磁路饱和与深槽效应的感应电机非线性特性实时数字仿真模型 |

## 相关方法
- [[state-space-method|状态空间法]] - 感应电机状态空间建模
- [[coordinate-transformation-model|坐标变换]] - dq0坐标变换
- [[average-value-model|平均值模型]] - 机电暂态简化
- [[numerical-integration|数值积分]] - 启动暂态仿真
- [[parameter-identification|参数辨识]] - 电机参数辨识

## 相关模型
- [[synchronous-machine-model|同步电机模型]] - 同步机与异步机对比
- [[dfig-model|DFIG模型]] - 双馈感应发电机
- [[load-model|负荷模型]] - 感应电机负荷
- [[transformer-model|变压器模型]] - 机端变压器

## 相关主题
- [[wind-farm-modeling]] - 风电场建模
- [[real-time-simulation]] - 电机实时仿真
- [[harmonic-analysis]] - 电机谐波分析
- [[network-equivalent]] - 负荷等值

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Modeling of ac machines using a voltage-behind-reactance for]] | 2010 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[development-of-data-translators-for-interfacing-13&14|Development of Data Translators for Interfacing Power-Flow P]] | 2013 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |

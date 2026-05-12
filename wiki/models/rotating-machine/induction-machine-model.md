---
title: "感应电机 (Induction Machine)"
type: model
tags: [induction-machine, asynchronous-machine, motor, load, dq0, slip]
created: "2026-04-29"
updated: "2026-05-12"
---

# 感应电机 (Induction Machine)



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

## 量化性能边界

**AVBR近似电压后电抗模型精度与效率**（Wang & Jatskevich 2010）：
- AVBR模型单步计算耗时1.9 μs，较PD模型（4.3 μs）提速约126%，较精确VBR模型（2.2 μs）提速13.6%
- 非对角系数与对角系数比值|k_j/d_j|呈O(Δt²)衰减，Δt=500 μs时比值降至10⁻³量级，矩阵强对角占优
- 最严苛工况（3 HP电机、同步转速、Δt=500 μs）下理论近似误差上界仅1.2%，实际误差远低于此
- 恒定电导子矩阵使EMTP网络导纳矩阵LU分解仅需初始化时执行一次，彻底消除每步重分解负担
- 验证覆盖4台典型鼠笼式感应电机（3 HP至2250 HP）空载启动暂态，ANSI C自定义代码实现

**NR节点缩减模型计算性能**（Vilchis-Rodriguez & Acha 2012）：
- 导纳矩阵维度从6×6满阵缩减为3×3对角阵，矩阵求逆计算量从O(n³)=216次乘法降至O(n)=3次，效率提升约98%
- NR-CC和NR-CF模型可使用1-5 ms大步长保持稳定，传统PD模型步长超过0.5 ms即出现数值不稳定
- NR-CC模型纯电流变量方案在相同步长下与VBR精度误差<0.1%，省去磁通-电流转换计算开销
- NR-CC定子电流瞬态响应与详细PD模型误差<0.5%，稳态误差<0.1%
- 恒定导纳矩阵Y_nrcc只需存储一次，内存访问次数减少约70%

**感应电机EMT模型典型参数范围**（学术文献与工程手册综合）：
- 定子电阻R_s：0.01-0.05 pu，转子电阻R_r'：0.01-0.05 pu
- 定子漏抗X_s：0.05-0.15 pu，转子漏抗X_r'：0.05-0.15 pu
- 励磁电抗X_m：2.0-5.0 pu（大中型电机），1.0-2.0 pu（小型电机）
- 满载功率因数：0.80-0.92（滞后），满载效率：85-97%
- 最大转矩（崩溃转矩）：2.0-3.0倍额定转矩，发生于转差率s_m=R_r'/X_r'
- 额定转差率：0.5-5%（大电机转差率更小）
- 直接启动电流：5-7倍额定电流，启动转矩：1.5-2.5倍额定转矩

**负荷建模与系统影响**：
- 感应电机负荷占工业总负荷60-80%，是系统电压稳定和暂态稳定的关键影响因素
- 大电机启动引起的电压暂降估算：ΔV ≈ (X_s + X_line)×I_start，典型值5-15%
- 负荷电压特性指数：P = P_0(V/V_0)^α，Q = Q_0(V/V_0)^β，α=0.1-1.2，β=1.5-3.0

**数据缺口声明**：不同功率等级和极对数感应电机的精确等效电路参数缺乏统一公开数据集。深度饱和效应对瞬态电抗的影响量化不足，尤其是大容量电机在故障工况下的暂态参数变化规律。感应电机聚合负荷模型在EMT仿真中的参数辨识精度和泛化能力缺乏系统验证。节点缩减模型（NR-CC/NR-CF）在深度饱和、逆变器供电及不平衡电网条件下的精度边界尚待进一步研究。

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

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[approximate-voltage-behind-reactance-induction-machine-model-for-efficient-inter|Approximate Voltage-Behind-Reactance Induction Machine Model]] | 2010 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance Induction Machine]] | 2010 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Modeling of AC Machines Using VBR Formulation]] | 2010 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling]] | 2011 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling]] | 2012 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain]] | 2019 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis]] | 2021 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation]] | 2023 |

---
title: "永磁同步电机 (PMSM)"
type: model
tags: [pmsm, synchronous-machine, permanent-magnet, motor, generator]
created: "2026-04-14"
updated: "2026-05-12"
---

# 永磁同步电机 (PMSM)



## 概述

永磁同步电机（Permanent Magnet Synchronous Machine, PMSM）是采用永磁体励磁的同步电机。相比电励磁同步电机，PMSM具有效率高、功率密度大、响应快等优点，广泛应用于风力发电、电动汽车和工业驱动领域。

## 主要特点

- 永磁体励磁，无需励磁绕组
- 高效率、高功率密度
-  dq轴电感不对称（凸极效应）
- 退磁风险（高温、大电流）
- 适用于变速恒频运行

## EMT建模方法

### 1. 传统dq0模型
- Park变换建立dq轴方程
- 适用于对称运行条件
- 计算效率高

### 2. 相域模型
- 直接在abc坐标系下建模
- 适用于不对称和故障条件
- 计算量大

### 3. 有限元耦合模型
- 基于FEA结果定义磁链
- 精确表征磁饱和和非线性
- 适用于高精度实时仿真

## 应用场景

- 直驱风力发电
- 电动汽车驱动
- 工业伺服系统
- 航空航天

## 相关方法
- [[state-space-method|状态空间法]] - PMSM状态空间建模
- [[fixed-admittance|恒导纳模型]] - 电机驱动恒导纳实现
- [[average-value-model|平均值模型]] - 变流器平均值等效
- [[numerical-integration|数值积分]] - 电机动态方程离散化

## 相关模型
- [[synchronous-machine-model|同步电机模型]] - 电励磁同步机对比
- [[vsc-model|VSC模型]] - 机侧/网侧换流器建模
- [[dfig-model|DFIG模型]] - 双馈风机对比
- [[induction-machine-model|感应电机模型]] - 异步电机对比

## 相关主题
- [[real-time-simulation|实时仿真]] - PMSM实时仿真
- [[frequency-dependent-modeling|频率相关建模]] - 电机宽频特性
- [[co-simulation|混合仿真]] - 多域协同仿真
- [[network-equivalent|网络等值]] - 风电场等值聚合

## 量化性能边界

**FD-PMSM磁链定义模型精度与效率**（Li 2025）：
- 实时仿真步长 < 1.0 µs（RTDS Novacor 2.0 平台实测，1.5 µs 与 2.0 µs 步长均稳定运行），满足亚微秒级 EMT 实时仿真需求
- FEA 降阶模型避免传统 LUT 反演预处理（耗时数小时），通过三线性插值直接求解电流导数，单点 FEA 计算仅需 1-2 秒，总预处理时间可控
- LUT 数据规模：7,381 条记录（覆盖电流 ±150 A，转子位置 0-360°），电流分辨率 30 A（精细）/ 60 A（粗粒），位置分辨率 1°（精细）/ 4°（粗粒）
- LUT 电流边界可扩展至 ±300 A，故障瞬态电流 200-250 A 超出标准范围时采用切平面外推保证数值稳定性
- 三线性插值中偏导数复用技术降低单步浮点运算量，在 7,381 条 FEA 数据规模下维持亚微秒实时性
- 验证覆盖理想源驱动 PMSM（开/短路、负载突变、三相接地故障）及 150 kW 电动汽车全动力总成（DC-DC、DC-AC 逆变器、FOC-MTPA 控制器），波形与高精度 FEA 软件一致

**PMSM 典型参数范围**：
- 定子电阻 $R_s$：0.01-0.1 Ω（含 IGBT 导通损耗等效）
- dq 轴电感 $L_d, L_q$：0.1-1.0 mH（凸极比 $L_q/L_d \approx 1.5-3.0$）
- 永磁体磁链 $\psi_{pm}$：0.05-0.3 Wb（取决于电机功率等级）
- 极对数 $p$：20-50（直驱风机），2-8（电动汽车）
- 直流母线电容 $C$：0.01-0.1 F（决定直流电压动态时间常数）
- 额定功率：1 kW-10 MW（覆盖伺服至风电全范围）

**多时间尺度降阶模型性能**（2024 Multi-timescale）：
- 全阶模型 17 个状态变量，时间尺度分离比 $\varepsilon \approx 0.004 \ll 0.1$，满足奇异摄动条件
- 降阶后仿真步长从 1-10 µs 放宽至 100 µs，计算速度提升 60-80%，误差控制在 $O(\varepsilon)$ 量级（典型 < 5%）
- 快动态（PLL、电流环 ~20 ms）与慢动态（机械轴系 ~5 s）分离实现自适应步长

**数据缺口声明**：FD-PMSM 模型在不同 LUT 粒度（如 60 A/4° 粗粒 vs 30 A/1° 精细）下的精度-效率权衡缺乏系统量化。永磁体温度-磁场耦合、局部退磁等退化效应在现有 EMT 模型中尚未充分建模。不同功率等级 PMSM 的统一参数数据集缺乏公开标准，现有参数分散于各厂家手册与文献中。直驱风电 PMSM 在故障工况下的凸极饱和暂态参数变化规律仍需进一步研究。

## 深度增强内容

 ## 1. 各类模型数学描述

### 1.1 详细电磁暂态模型（FEA-based Flux-Defined Model）

基于有限元分析（FEA）的磁链定义模型通过查表（LUT）方式直接引入磁饱和与空间谐波效应，避免传统集总参数模型的精度损失。

**磁链-电流关系**：
永磁同步电机的磁链是电流和转子位置的函数：
$$
\boldsymbol{\psi} = \boldsymbol{\psi}(i_d, i_q, \theta_r)
$$

其中 $\theta_r$ 为转子电角度。对于凸极PMSM，磁链在dq坐标系下表示为：
$$
\begin{cases}
\psi_d = \psi_d(i_d, i_q, \theta_r) \\
\psi_q = \psi_q(i_d, i_q, \theta_r)
\end{cases}
$$

**电压方程**：
$$
\begin{cases}
u_d = R_s i_d + \frac{d\psi_d}{dt} - \omega_r \psi_q \\
u_q = R_s i_q + \frac{d\psi_q}{dt} + \omega_r \psi_d
\end{cases}
$$

**电流导数直接计算法**（免求逆方法）：
传统方法需对 $\boldsymbol{\psi} = \mathbf{L}\mathbf{i}$ 进行查表反演求电流，而磁链定义法通过链式法则直接计算电流导数：
$$
\frac{d\mathbf{i}}{dt} = \left(\frac{\partial \boldsymbol{\psi}}{\partial \mathbf{i}}\right)^{-1} \left( \mathbf{u} - \mathbf{R}\mathbf{i} - \frac{\partial \boldsymbol{\psi}}{\partial \theta_r}\omega_r \right)
$$

其中 $\frac{\partial \boldsymbol{\psi}}{\partial \mathbf{i}}$ 为增量电感矩阵，通过三线性插值从FEA数据表获取。

**电磁转矩**：
$$
T_e = \frac{3}{2}p(\psi_d i_q - \psi_q i_d)
$$

### 1.2 平均值状态空间模型（dq0 Model）

适用于控制器设计与系统级仿真，假设正弦磁场分布且忽略谐波。

**定子电压方程**：
$$
\begin{bmatrix} u_d \\ u_q \end{bmatrix} = \begin{bmatrix} R_s & 0 \\ 0 & R_s \end{bmatrix} \begin{bmatrix} i_d \\ i_q \end{bmatrix} + \begin{bmatrix} \frac{d\psi_d}{dt} \\ \frac{d\psi_q}{dt} \end{bmatrix} + \omega_r \begin{bmatrix} -\psi_q \\ \psi_d \end{bmatrix}
$$

**磁链方程**（线性化模型）：
$$
\begin{cases}
\psi_d = L_d i_d + \psi_f \\
\psi_q = L_q i_q
\end{cases}
$$

**电磁转矩**（考虑凸极效应）：
$$
T_e = \frac{3}{2}p\left[\psi_f i_q + (L_d - L_q)i_d i_q\right]
$$

** id=0 控制简化模型**：
当采用 $i_d^* = 0$ 控制策略时，转矩方程线性化为：
$$
T_e = \frac{3}{2}p\psi_f i_q
$$

### 1.3 机电暂态降阶模型

适用于电力系统暂态稳定分析，忽略高频电磁动态，保留机电能量转换与直流环节动态。

**直流电压动态**：
$$
C u_{dc} \frac{du_{dc}}{dt} = P_s - P_g
$$

其中 $P_s$ 为机侧变流器功率，$P_g$ 为网侧变流器功率，$C$ 为直流母线电容。

**功率解耦控制方程**：
电网侧变流器采用电网电压定向控制（$u_{dg}=0$）时：
$$
\begin{cases}
P_g = \frac{3}{2}u_{qg}i_{dg} \\
Q_g = -\frac{3}{2}u_{qg}i_{qg}
\end{cases}
$$

**多时间尺度奇异摄动模型**：
将状态变量按时间尺度分离为快变子系统 $\mathbf{x}_f$（PLL、电流控制环，~20ms）和慢变子系统 $\mathbf{x}_s$（机械轴系、风轮，~5s）：

$$
\begin{cases}
\varepsilon \dot{\mathbf{x}}_f = \mathbf{f}_f(\mathbf{x}_f, \mathbf{x}_s, u) \\
\dot{\mathbf{x}}_s = \mathbf{f}_s(\mathbf{x}_f, \mathbf{x}_s, u)
\end{cases}
$$

其中 $\varepsilon = \tau_f/\tau_s \approx 0.004 \ll 0.1$ 为摄动小参数。降阶模型通过令 $\varepsilon \to 0$ 消去快动态，仿真步长可从 $1\,\mu\text{s}$ 放宽至 $100\,\mu\text{s}$。

### 1.4 半隐式延迟解耦模型（SILDP）

用于并行仿真加速，通过矩阵分裂将系统解耦为多个子系统。

**状态空间分裂**：
将状态变量分组（如三相电流 $i_a, i_b, i_c$ 和直流电压 $U_{dc}$），每组独立求解：
$$
\mathbf{A}_k \dot{\mathbf{x}}_k = \mathbf{B}_k \mathbf{x}_k + \mathbf{C}_k \mathbf{u}_k, \quad k=1,2,\dots,m
$$

**半步长延迟接口**：
子系统间通过受控源等效连接，引入 $\Delta t/2$ 的延迟实现解耦：
$$
\mathbf{u}_{eq}(t) = \mathbf{f}(\mathbf{x}_j(t-\Delta t/2))
$$

## 2. 仿真参数参考表

| 参数类别 | 参数名称 | 典型值/范围 | 来源论文 | 备注 |
|---------|---------|------------|---------|------|
| **电气参数** | 定子电阻 $R_s$ | 0.01-0.1 Ω | 论文5 | IGBT导通损耗等效 |
| | 直流电容 $C$ | 0.01-0.1 F | 论文1 | 决定直流电压动态时间常数 |
| | 极对数 $p$ | 20-50 (直驱风机) | 论文3 | 低速大转矩设计 |
| **控制参数** | 减载备用系数 $\eta_{del}$ | 0.90 (10%备用) | 论文4 | 频率响应预留 |
| | 频率滤波时间常数 $T_{fr}$ | 100-200 ms | 论文3 | 决定惯量响应延时 |
| | 电流环带宽 | 100-500 Hz | 论文3 | 快时间尺度 |
| **FEA数据** | 电流 LUT 范围 | ±150 A (扩展±300 A) | 论文7 | 故障电流可达200-250 A |
| | 电流步长 $\Delta i$ | 30 A | 论文7 | 精度与存储权衡 |
| | 位置步长 $\Delta\theta$ | 1° (电角度) | 论文7 | 空间谐波分辨率 |
| | LUT 记录数 | 7,381 条 | 论文7 | 三线性插值基础 |
| **仿真设置** | EMT 步长 | 1.0-50.0 µs | 论文6,7 | 详细模型需<1 µs |
| | 机电暂态步长 | 10 ms | 论文6 | 半个工频周期 |
| | FPGA 步长 | 10-200 ns | 论文2 | 纳秒级并行仿真 |
| | 多时间尺度步长 | 100 µs (降阶) | 论文3 | 比全阶快60-80% |
| **聚类等值** | 风速区间数 | 3 (低/中/高) | 论文4 | 3-6.05/6.05-7.75/7.75-22 m/s |
| | 等值机数量 | ≤3 台 | 论文4 | 表征上百台机组 |

## 3. 模型选择指南

| 应用场景 | 推荐模型 | 仿真步长 | 关键考虑因素 |
|---------|---------|---------|------------|
| **实时硬件在环(HIL)仿真**<br>（控制器测试） | FEA-based磁链定义模型 | < 1.0 µs | 需捕捉磁饱和与非线性；采用免求逆算法保证实时性；RTDS平台验证 |
| **变流器开关细节分析**<br>（IGBT损耗、EMI） | 详细开关模型 + SILDP | 10-200 ns | 需考虑导通电阻(0.01Ω)；适合FPGA大规模并行 |
| **风电场级机电暂态**<br>（电网稳定性） | 多时间尺度降阶模型 | 100 µs-10 ms | 保留频率响应特性；忽略PLL快动态(20ms)；计算效率提升60-80% |
| **大规模风电场等值**<br>（含调频控制） | 分群等值模型 | 10 ms | 按风速区间聚群(3群)；最多3台等值机；验证频率阶跃(±0.5Hz)响应 |
| **不对称故障分析** | 相域详细模型 | 50 µs | 适用于abc坐标系；考虑负序与零序分量 |
| **控制系统设计**<br>（矢量控制参数整定） | 平均值dq0模型 | 10-100 µs | 采用id=0控制；功率解耦；验证直流电压动态 |

## 4. 前沿研究方向

### 4.1 高保真FEA-ROM实时仿真技术
基于有限元降阶模型（ROM）的电磁暂态仿真成为热点。关键贡献包括：
- **免数据表求逆算法**：通过磁链数据直接计算电流导数，消除传统LUT反演的数小时预处理时间，实现FEA级精度与微秒级实时性的统一。
- **自适应插值与外推**：针对故障电流越限（>200A）场景，设计边界外推平滑策略，确保LUT数据在原始范围外（±150A）的数值稳定性。

### 4.2 多时间尺度混合仿真架构
针对直驱风电场全状态模型（17+状态变量）的"刚性"问题：
- **奇异摄动理论应用**：严格量化电气时间常数（~20ms）与机械时间常数（~5s）的分离比（ε≈0.004），构建5时间尺度降阶模型，在保证O(ε)精度（误差<5%）的同时将步长放宽100倍。
- **多速率接口技术**：不同子系统采用独立步长（电磁1µs vs 机械10ms），通过插值接口数据交换，解决异构时间尺度仿真效率瓶颈。

### 4.3 异构并行计算架构
- **FPGA纳秒级仿真**：利用定制硬件架构实现dq0定子电流解耦，单步计算耗时降至44ns，消除预测-校正环节，适用于大规模风电场实时仿真。
- **GPU加速SILDP**：基于半隐式延迟解耦（SILDP）将系统分裂为4+并行子系统，结合GPU流处理器实现矩阵运算并行化，显著加速详细模型仿真。

### 4.4 数据驱动与物理融合建模
- **三线性插值优化**：利用插值计算中的中间变量（偏导数）复用技术，降低单步浮点运算量，在7381条FEA数据规模下维持亚微秒实时性。
- **轨迹灵敏度分析**：量化风电机组电气参数可辨识性，为模型参数校准与误差分析提供理论依据，支撑风电场实测模型构建。

### 4.5 开放问题
1. **极端工况下的磁链表外推**：如何在高电流冲击（>300A）与高温退磁条件下，保证磁链LUT外推的物理一致性与数值稳定性？
2. **多机并行实时仿真扩展性**：当风电场规模达上百台机组时，当前<1µs的实时步长要求与计算资源限制的矛盾如何平衡？
3. **机电-电磁混合仿真接口**：如何设计严格的能量守恒接口，实现详细PMSM模型（EMT）与电网机电暂态模型（RMS）的高效联合仿真？

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[直驱式风电机组机电暂态建模及仿真|直驱式风电机组机电暂态建模及仿真]] | 2022 |
| [[直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法|直驱风力发电单元的电磁暂态半隐式延迟解耦与仿真方法]] | 2022 |
| [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech|An aggregation method of permanent magnet synchronous wind f]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[fixed-admittance-modeling-method-of-pmsg-based-on-compensation-of-impedance-基于虚拟|Fixed-admittance Modeling Method of PMSG Based on Compensati]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模|基于全阶模型的直驱风电机组多时间尺度等效惯量机理建模]] | 2024 |
| [[电力系统风力发电建模与仿真研究综述|电力系统风力发电建模与仿真研究综述]] | 2024 |
| [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time]] | 2025 |
| [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time]] | 2025 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-|Comprehensive Full-Scale Converter Wind Park Initialization ]] | 2025 |
| [[适用于电网频率响应分析的直驱型风电场实用化等值方法|适用于电网频率响应分析的直驱型风电场实用化等值方法]] | 2025 |
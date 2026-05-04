---
title: "新能源机组 (Renewable Energy Units)"
type: topic
tags: [renewable-energy, wind-power, pv, inverter, grid-connection, low-voltage-ride-through]
created: "2026-05-02"
---

# 新能源机组 (Renewable Energy Units)

## 概述

新能源机组(Renewable Energy Units)是指利用可再生能源发电的电力设备，主要包括风力发电机组和光伏发电系统。随着全球能源转型和碳中和目标的推进，新能源发电在电力系统中的占比快速提升，已成为现代电力系统的重要组成部分。新能源机组通常通过电力电子变流器并网，具有不同于同步发电机的运行特性，对电网的安全稳定运行提出了新的挑战。掌握新能源机组的建模方法、控制策略和并网特性，是分析高比例新能源电力系统的关键。

## 风力发电系统

### 机组类型

**双馈感应发电机(DFIG)**:
- 定子直接并网
- 转子通过变流器连接
- 变流器容量: 25-30%额定功率
- 转速范围: ±30%同步速

**永磁同步发电机(PMSG)**:
- 全功率变流器
- 永磁体励磁
- 高效率
- 齿轮箱/直驱型

**鼠笼感应发电机(SCIG)**:
- 定速运行
- 简单可靠
- 无功消耗大
- 已逐步淘汰

**半直驱**:
- 单级或两级齿轮箱
- 中速永磁发电机
- 变流器容量: 100%

### DFIG详细模型

**发电机方程**:
$$\begin{bmatrix} v_{sd} \\ v_{sq} \\ v_{rd} \\ v_{rq} \end{bmatrix} = \begin{bmatrix} R_s + pL_s & -\omega_1 L_s & pL_m & -\omega_1 L_m \\ \omega_1 L_s & R_s + pL_s & \omega_1 L_m & pL_m \\ pL_m & -s\omega_1 L_m & R_r + pL_r & -s\omega_1 L_r \\ s\omega_1 L_m & pL_m & s\omega_1 L_r & R_r + pL_r \end{bmatrix} \begin{bmatrix} i_{sd} \\ i_{sq} \\ i_{rd} \\ i_{rq} \end{bmatrix}$$

其中 $s = (\omega_1 - \omega_r)/\omega_1$ 为转差率

**转子侧变流器控制**:
- 定子磁链定向
- d轴: 无功功率控制
- q轴: 有功功率/转矩控制

**网侧变流器控制**:
- 直流电压控制
- 电网同步

### PMSG详细模型

**发电机方程**:
$$\begin{cases}
v_d = -R_s i_d + p\lambda_d - \omega_e \lambda_q \\
v_q = -R_s i_q + p\lambda_q + \omega_e \lambda_d
\end{cases}$$

**磁链方程**:
$$\begin{cases}
\lambda_d = L_d i_d + \lambda_m \\
\lambda_q = L_q i_q
\end{cases}$$

**变流器控制**:
- 机侧变流器: 最大功率点跟踪(MPPT)
- 网侧变流器: 直流电压控制+无功功率控制

### 风力机模型

**空气动力学**:
$$P_m = \frac{1}{2}\rho A C_p(\lambda, \beta) v_w^3$$

**风能利用系数**:
$$C_p(\lambda, \beta) = c_1(\frac{c_2}{\lambda_i} - c_3\beta - c_4)e^{-\frac{c_5}{\lambda_i}} + c_6\lambda$$

**叶尖速比**:
$$\lambda = \frac{\omega_r R}{v_w}$$

## 光伏发电系统

### 光伏电池模型

**单二极管模型**:
$$I = I_{ph} - I_0\left(e^{\frac{V+IR_s}{aV_t}} - 1\right) - \frac{V+IR_s}{R_{sh}}$$

**简化模型**:
$$I = I_{sc}\left(1 - e^{\frac{V-V_{oc}}{V_t}}\right)$$

**参数特性**:
- 短路电流 $I_{sc}$: 与辐照度成正比
- 开路电压 $V_{oc}$: 受温度影响
- 最大功率点随辐照度和温度变化

### 最大功率点跟踪

**扰动观察法**:
$$\Delta P > 0 \Rightarrow \text{同方向扰动}$$
$$\Delta P < 0 \Rightarrow \text{反方向扰动}$$

**电导增量法**:
$$\frac{dI}{dV} = -\frac{I}{V} \Rightarrow \text{最大功率点}$$

**改进算法**:
- 变步长
- 自适应
- 智能算法

### 光伏逆变器

**拓扑结构**:
- 单级式
- 双级式(升压+逆变)
- 多级式

**控制策略**:
- 电压源控制(VSM)
- 电流源控制
- 下垂控制

**并网要求**:
- 低电压穿越
- 频率响应
- 功率因数调节

## 并网变流器控制

### 矢量控制

**dq坐标变换**:
$$\begin{bmatrix} i_d \\ i_q \end{bmatrix} = \frac{2}{3}\begin{bmatrix} \cos\theta & \cos(\theta-120°) & \cos(\theta+120°) \\ -\sin\theta & -\sin(\theta-120°) & -\sin(\theta+120°) \end{bmatrix}\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$

**电流内环**:
$$\begin{cases}
v_d^* = v_d^{PI} - \omega L i_q \\
v_q^* = v_q^{PI} + \omega L i_d
\end{cases}$$

**功率外环**:
$$\begin{cases}
i_d^* = K_{pP}(P^* - P) + K_{iP}\int(P^* - P)dt \\
i_q^* = K_{pQ}(Q^* - Q) + K_{iQ}\int(Q^* - Q)dt
\end{cases}$$

### 锁相环(PLL)

**同步参考系PLL**:
$$\omega = \omega_{ff} + K_p v_q + K_i\int v_q dt$$

**增强型PLL**:
- 双二阶广义积分器
- 正负序分离
- 不平衡处理

**应用**:
- 电网同步
- 相位检测
- 频率估计

### 低电压穿越(LVRT)

**电压跌落要求**:
- 电压跌至20%额定电压
- 维持并网625ms
- 提供无功支撑

**控制策略**:
- 撬棒电路(Crowbar)
- 变流器电流限制
- 无功电流注入

**无功电流要求**:
$$I_q \geq 1.5(0.9 - V_T)I_N, \quad V_T < 0.9$$

## 电磁暂态模型

### 详细模型

**开关模型**:
- IGBT详细模型
- 二极管反向恢复
- PWM调制

**仿真步长**:
- 1-10μs
- 计算量大
- 精度高

**应用**:
- 变流器设计
- 控制参数优化
- 故障分析

### 平均值模型

**基本原理**:
忽略开关过程，用平均电压/电流表示

**开关函数**:
$$d = \frac{t_{on}}{T_s}$$
$$\bar{v} = d \cdot V_{dc}$$

**优势**:
- 大步长仿真(50-100μs)
- 计算效率高
- 适合系统级分析

### 等效模型

**电压源等效**:
$$\dot{V}_{eq} = \dot{V}_{PCC} + jX_{eq}\dot{I}$$

**电流源等效**:
$$\dot{I}_{eq} = \dot{I}_{PCC} - \frac{\dot{V}_{PCC}}{jX_{eq}}$$

**适用场景**:
- 潮流计算
- 机电暂态仿真
- 大规模系统分析

## 机电暂态模型

### 简化发电机模型

**DFIG简化**:
- 转子运动方程
- 一阶变流器模型
- 电流限制

**PMSG简化**:
- 电压源模型
- 电流限制圆
- 功率环动态

### 控制系统的简化

**PLL简化**:
- 一阶惯性环节
- 时间常数10-100ms

**电流环简化**:
- 快速响应假设
- 电流指令跟踪

**功率环简化**:
- 主导时间常数
- 带宽设计

## 并网影响

### 电网支撑能力

**频率响应**:
- 惯量支撑
- 一次调频
- 下垂控制

**电压支撑**:
- 无功调节
- 电压穿越
- 故障恢复

**阻尼贡献**:
- 有功阻尼
- 虚拟同步机
- 附加控制

### 电能质量问题

**谐波**:
- 开关谐波
- 电网背景谐波
- 谐振风险

**电压波动**:
- 功率波动
- 闪变
- 电压偏差

**三相不平衡**:
- 负序电流
- 保护误动
- 设备过热

### 稳定性影响

**功角稳定**:
- 等效惯量降低
- 振荡模式变化
- 稳定裕度

**电压稳定**:
- 无功需求
- 电压支撑
- 短路容量

**频率稳定**:
- 调频能力
- 快速功率变化
- 频率偏差

## 聚合模型

### 风电场聚合

**单机等值**:
- 容量加权
- 风速分布
-  wake效应

**多机等值**:
- 风速分组
- 典型机组
- 集电网络

**参数确定**:
- 等效风速
- 等效阻抗
- 控制参数

### 光伏电站聚合

**逆变器聚合**:
- 相同逆变器类型
- 容量等效
- 控制统一

**阵列等效**:
- 辐照度分布
- 温度分布
- 阴影遮挡

## 相关主题
- [[dfig-model]] - DFIG模型
- [[pmsm-model]] - 永磁同步发电机模型
- [[pv-system-model]] - 光伏系统模型
- [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]] - 跟网型逆变器
- [[renewable-energy-integration]] - 新能源并网

## 来源论文

参见 [[index.md]] 获取更多新能源机组相关文献。

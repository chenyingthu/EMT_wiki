---
title: "矢量控制 (Vector Control)"
type: method
tags: [vector-control, field-oriented-control, motor-drive, inverter, ac-machine]
created: "2026-05-04"
---

# 矢量控制 (Vector Control)

## 定义与边界

矢量控制（又称磁场定向控制，Field-Oriented Control, FOC）是一种通过坐标变换将交流电机电磁转矩与励磁解耦，实现类似直流电机控制性能的高性能交流调速方法。该方法通过Park变换将三相交流量转换为旋转坐标系下的直流量，独立控制磁链和转矩分量。

在电力系统分析中，矢量控制主要应用于：
- 并网逆变器的电流/功率控制
- 电机驱动系统的调速控制
- 柔性交流输电装置（STATCOM、UPFC等）
- 新能源发电设备的功率调节

**边界限定**：本方法基于线性化假设，大信号扰动下需考虑控制饱和与非线性效应。

## EMT中的作用

矢量控制是电力电子装置精确控制的核心技术：

- **解耦控制**：实现有功/无功、转矩/磁链的独立调节
- **动态响应**：获得比标量控制更快的动态响应
- **宽速域运行**：从低速到高速的宽范围稳定运行
- **并网控制**：实现新能源设备的友好并网

## 主要分支与机制

### 1. 直接磁场定向控制 (DFOC)

直接测量或计算转子磁链位置，实现精确磁场定向：
$$\theta_e = \int(\omega_r + \omega_s)dt$$

其中 $\omega_r$ 为转子转速，$\omega_s$ 为转差频率。

### 2. 间接磁场定向控制 (IFOC)

通过转差频率计算磁链位置，无需磁链传感器：
$$\omega_s = \frac{L_m i_{qs}^*}{\tau_r \psi_{dr}^*}$$

### 3. 直接转矩控制 (DTC)

直接控制定子磁链和电磁转矩，无需坐标变换：
$$T_e = \frac{3}{2}p\frac{\psi_s \times \psi_r}{L_m}$$

## 形式化表达

### Park变换

三相静止坐标到两相同步旋转坐标的变换：

$$
\begin{bmatrix} i_d \\ i_q \end{bmatrix}
=
\frac{2}{3}
\begin{bmatrix} \cos\theta & \cos(\theta-120°) & \cos(\theta+120°) \\ -\sin\theta & -\sin(\theta-120°) & -\sin(\theta+120°) \end{bmatrix}
\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}
$$

逆变换：

$$
\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}
=
\begin{bmatrix} \cos\theta & -\sin\theta \\ \cos(\theta-120°) & -\sin(\theta-120°) \\ \cos(\theta+120°) & -\sin(\theta+120°) \end{bmatrix}
\begin{bmatrix} i_d \\ i_q \end{bmatrix}
$$

### 同步电机转矩方程

旋转坐标系下电磁转矩：

$$T_e = \frac{3}{2}p[\psi_f i_q + (L_d-L_q)i_d i_q]$$

对于隐极机（$L_d=L_q$）：
$$T_e = \frac{3}{2}p\psi_f i_q$$

### 电流解耦控制

定子电压方程（考虑交叉耦合项）：

$$v_d = R_s i_d + L_d\frac{di_d}{dt} - \omega_e L_q i_q$$
$$v_q = R_s i_q + L_q\frac{di_q}{dt} + \omega_e L_d i_d + \omega_e \psi_f$$

前馈解耦补偿：
$$v_d^* = v_d' - \omega_e L_q i_q$$
$$v_q^* = v_q' + \omega_e L_d i_d + \omega_e \psi_f$$

### PI控制器设计

电流环PI参数（基于极点配置）：

$$K_p = \frac{L}{\tau_c}, \quad K_i = \frac{R}{\tau_c}$$

其中 $\tau_c$ 为期望的电流环时间常数。

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 参数准确 | 电机参数已知 | 影响解耦效果 |
| 速度范围 | 基速以下恒转矩 | 弱磁区需特殊处理 |
| 采样频率 | >10倍开关频率 | 保证控制精度 |
| 线性区 | 未饱和 | 考虑电压/电流限制 |

### 失效边界

- **参数失配**：电机实际参数与控制器参数偏差导致解耦失效
- **速度估计误差**：无传感器控制中低速估算不准
- **积分饱和**：PI控制器积分项饱和导致超调
- **采样延迟**：大延迟导致相位裕度不足、振荡

### 关键假设

1. 电机参数恒定时不变
2. 三相绕组对称
3. 磁路线性（无饱和）或已补偿
4. 逆变器增益恒定

## 代表性来源

### 经典文献

- Blaschke, F., "The Principle of Field Orientation as Applied to the New Transvector Closed-Loop Control System for Rotating-Field Machines," *Siemens Review*, 1971. - 矢量控制奠基论文
- Leonhard, W., "Control of Electrical Drives," *Springer*, 2001. - 电机控制经典教材

### 应用方法

- [[coordinate-transformation]] - 坐标变换
- [[dq-transformation]] - dq变换
- PI 控制器设计
- PWM 调制

### 相关控制

- 直接转矩控制
- 电压定向控制
- 构网型控制

## 与相关页面的关系

- [[coordinate-transformation-model]] - 坐标变换模型
- [[pi-controller-model]] - PI控制器模型
- [[pwm-modulator-model]] - PWM调制模型
- [[gfl-inverter-model]] - 跟网型逆变器模型
- [[synchronous-machine-model]] - 同步电机模型
- [[induction-machine-model]] - 感应电机模型

## 开放问题

- 参数在线辨识与自适应矢量控制
- 弱磁区深度弱磁与六步调制过渡
- 无传感器控制零速/低速运行
- 多电机并联运行的解耦控制

## 参考标准

- IEC 61800-9 - 可调速电气传动系统
- IEEE Std. 1566 - 高压直流输电变流器

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

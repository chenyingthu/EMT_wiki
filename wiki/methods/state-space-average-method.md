---
title: "状态空间平均法 (State-Space Average Method)"
type: method
tags: [state-space, average, converter, modeling, small-signal, power-electronics]
created: "2026-05-02"
---

# 状态空间平均法 (State-Space Average Method)

## 概述

状态空间平均法(State-Space Average Method, SSA)是电力电子变换器建模的经典方法，由R. D. Middlebrook于1976年提出。该方法通过对开关变换器在不同开关状态下的状态空间方程进行时间加权平均，得到描述变换器低频动态行为的连续时间模型，广泛应用于DC-DC变换器、逆变器和整流器的小信号分析与控制器设计。

## 基本原理

### 状态空间表示

**状态方程**：
$$\dot{x} = Ax + Bu$$
$$y = Cx + Du$$

其中：
- $x$: 状态变量向量（电感电流、电容电压）
- $u$: 输入向量
- $y$: 输出向量
- $A, B, C, D$: 系统矩阵

### 开关状态建模

**两状态变换器**（如Buck、Boost）：

状态1（开关导通，$0 < t < dT_s$）：
$$\dot{x} = A_1x + B_1u$$

状态2（开关关断，$dT_s < t < T_s$）：
$$\dot{x} = A_2x + B_2u$$

其中$d$为占空比，$T_s$为开关周期。

### 平均状态方程

**状态空间平均**：
$$\dot{x} = [dA_1 + (1-d)A_2]x + [dB_1 + (1-d)B_2]u$$

定义平均矩阵：
$$A_{avg} = dA_1 + (1-d)A_2$$
$$B_{avg} = dB_1 + (1-d)B_2$$

**假设条件**：
- 开关频率远高于系统自然频率
- 状态变量在一个开关周期内变化很小
- 忽略开关纹波影响

## 小信号模型

### 扰动线性化

**变量分解**：
$$d = D + \hat{d}$$
$$x = X + \hat{x}$$
$$u = U + \hat{u}$$

其中大写字母表示稳态值，带^符号表示小信号扰动。

### 稳态方程

$$0 = A_{avg}X + B_{avg}U$$
$$Y = C_{avg}X + D_{avg}U$$

**稳态解**：
$$X = -A_{avg}^{-1}B_{avg}U$$

### 小信号状态方程

$$\dot{\hat{x}} = A_{avg}\hat{x} + B_{avg}\hat{u} + [(A_1-A_2)X + (B_1-B_2)U]\hat{d}$$

定义：
$$E = (A_1-A_2)X + (B_1-B_2)U$$

则：
$$\dot{\hat{x}} = A_{avg}\hat{x} + B_{avg}\hat{u} + E\hat{d}$$

## 经典变换器建模

### Buck变换器

**电路参数**：
- 输入电压：$V_g$
- 输出电压：$V$
- 电感：$L$
- 电容：$C$
- 负载：$R$

**状态矩阵**：
$$A_1 = A_2 = \begin{bmatrix} 0 & -\frac{1}{L} \\ \frac{1}{C} & -\frac{1}{RC} \end{bmatrix}$$

$$B_1 = \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix}, \quad B_2 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

**直流增益**：
$$\frac{V}{V_g} = D$$

**传递函数**（占空比到输出）：
$$G_{vd}(s) = \frac{\hat{v}(s)}{\hat{d}(s)} = V_g\frac{1}{1 + s\frac{L}{R} + s^2LC}$$

### Boost变换器

**状态矩阵**：
$$A_1 = \begin{bmatrix} 0 & 0 \\ 0 & -\frac{1}{RC} \end{bmatrix}, \quad A_2 = \begin{bmatrix} 0 & -\frac{1}{L} \\ \frac{1}{C} & -\frac{1}{RC} \end{bmatrix}$$

$$B_1 = B_2 = \begin{bmatrix} \frac{1}{L} \\ 0 \end{bmatrix}$$

**直流增益**：
$$\frac{V}{V_g} = \frac{1}{1-D}$$

**传递函数**：
$$G_{vd}(s) = \frac{V_g}{(1-D)^2}\frac{1 - s\frac{L}{(1-D)^2R}}{1 + s\frac{L}{(1-D)^2R} + s^2\frac{LC}{(1-D)^2}}$$

### Buck-Boost变换器

**直流增益**：
$$\frac{V}{V_g} = -\frac{D}{1-D}$$

**特点**：输出电压极性反转

## 模型特性分析

### 频域特性

**控制-输出传递函数**：
$$G_{vd}(s) = K_d\frac{(1 + \frac{s}{\omega_{z1}})(1 - \frac{s}{\omega_{z2}})}{1 + \frac{s}{Q\omega_0} + (\frac{s}{\omega_0})^2}$$

**特征频率**：
| 参数 | Buck | Boost | Buck-Boost |
|-----|------|-------|-----------|
| 直流增益 | $D$ | $\frac{1}{1-D}$ | $\frac{-D}{1-D}$ |
| 谐振频率 | $\frac{1}{\sqrt{LC}}$ | $\frac{1-D}{\sqrt{LC}}$ | $\frac{1-D}{\sqrt{LC}}$ |
| 品质因数 | $R\sqrt{\frac{C}{L}}$ | $(1-D)R\sqrt{\frac{C}{L}}$ | $(1-D)R\sqrt{\frac{C}{L}}$ |

### 右半平面零点

**Boost变换器**：
$$\omega_{RHP} = \frac{(1-D)^2R}{L}$$

**影响**：
- 导致-90°相位滞后
- 限制闭环带宽
- 需要谨慎设计补偿器

## 扩展应用

### 多相变换器

**交错并联**：
- 相数：$N$
- 相位差：$\frac{2\pi}{N}$
- 等效频率：$N \cdot f_s$

**状态空间扩展**：
$$\dot{x} = A_{avg}x + B_{avg}u + \sum_{i=1}^{N}E_i\hat{d}_i$$

### 隔离型变换器

**变压器建模**：
- 理想变压器
- 励磁电感
- 漏感

**Flyback变换器**：
$$\frac{V}{V_g} = \frac{D}{1-D} \cdot \frac{N_2}{N_1}$$

### 逆变器建模

**单相全桥**：
- 双极性调制
- 单极性调制

**传递函数**：
$$G_{vd}(s) = V_{dc} \cdot H_{LPF}(s)$$

其中$H_{LPF}$为输出滤波器传递函数。

## 控制器设计

### 电压模式控制

**开环传递函数**：
$$T(s) = G_c(s) \cdot G_{vd}(s) \cdot H(s)$$

其中：
- $G_c(s)$: 补偿器传递函数
- $H(s)$: 反馈网络传递函数

**补偿器设计**：
| 类型 | 传递函数 | 应用 |
|-----|---------|------|
| 比例(P) | $K_p$ | 简单系统 |
| 比例积分(PI) | $K_p + \frac{K_i}{s}$ | Buck变换器 |
| 比例积分微分(PID) | $K_p + \frac{K_i}{s} + K_ds$ | 复杂系统 |
| Type III | 双极点双零点 | 宽范围调节 |

### 电流模式控制

**内环（电流环）**：
- 峰值电流控制
- 平均电流控制
- 滞环电流控制

**外环（电压环）**：
$$G_{v}(s) = \frac{G_c(s) \cdot G_{vi}(s)}{1 + T_i(s)}$$

**优点**：
- 一阶系统特性
- 易于补偿
- 自动限流

## 模型验证

### 时域验证

**阶跃响应**：
- 上升时间
- 超调量
- 调节时间

**负载突变**：
$$\Delta V_{max} = \frac{\Delta I_{load}}{8f_sC}$$

### 频域验证

**波特图**：
- 增益裕度 > 6 dB
- 相位裕度 > 45°

**阻抗分析**：
$$Z_{out}(s) = \frac{Z_{out,OL}(s)}{1 + T(s)}$$

## 局限性

### 基本假设限制

| 限制 | 原因 | 影响 |
|-----|------|------|
| 低频适用 | 忽略开关纹波 | 高频特性不准确 |
| 小信号假设 | 线性化处理 | 大信号暂态偏差 |
| 连续导通 | 假设CCM模式 | DCM需特殊处理 |
| 理想器件 | 忽略寄生参数 | 实际特性偏差 |

### 改进方法

**广义状态空间平均(GSSA)**：
- 考虑开关谐波
- 复数状态变量

**采样数据模型**：
- 精确离散化
- 适用于数字控制

## 相关方法
- [[average-value-model]] - 平均值模型
- [[small-perturbation-linearization]] - 小扰动线性化
- [[state-space-method]] - 状态空间法
- `pwm-modulation` - PWM调制

## 来源论文

参见 [[index.md]] 获取更多状态空间平均法相关文献。

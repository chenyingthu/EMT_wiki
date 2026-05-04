---
title: "相量模型 (Phasor Model)"
type: method
tags: [phasor, rms, steady-state, frequency-domain, electromechanical]
created: "2026-05-02"
---

# 相量模型 (Phasor Model)

## 概述

相量模型(Phasor Model)是基于工频正弦稳态假设的电力系统简化建模方法，用复数相量表示电压、电流的有效值和相位角。该模型忽略电磁暂态过程，假设系统始终处于准稳态，适用于机电暂态仿真、潮流计算和稳定性分析。相量模型将时域微分方程简化为复数代数方程，大幅降低计算复杂度，是分析电力系统慢动态过程(毫秒至秒级)的核心工具。

## 数学基础

### 正弦量表示

**瞬时值**:
$$v(t) = \sqrt{2}V\cos(\omega t + \theta_v)$$
$$i(t) = \sqrt{2}I\cos(\omega t + \theta_i)$$

**相量表示**:
$$\bar{V} = V\angle\theta_v = Ve^{j\theta_v}$$
$$\bar{I} = I\angle\theta_i = Ie^{j\theta_i}$$

**复数形式**:
$$\bar{V} = V(\cos\theta_v + j\sin\theta_v)$$

### 相量运算

**加减**:
$$\bar{V}_1 \pm \bar{V}_2 = (V_{1d} \pm V_{2d}) + j(V_{1q} \pm V_{2q})$$

**乘法**:
$$\bar{V}_1 \cdot \bar{V}_2 = V_1V_2\angle(\theta_1 + \theta_2)$$

**除法**:
$$\frac{\bar{V}_1}{\bar{V}_2} = \frac{V_1}{V_2}\angle(\theta_1 - \theta_2)$$

### 微分积分

**微分**:
$$\frac{dv}{dt} \rightarrow j\omega\bar{V}$$

**积分**:
$$\int v dt \rightarrow \frac{1}{j\omega}\bar{V}$$

## 元件相量模型

### 电阻

**时域**:
$$v_R(t) = Ri_R(t)$$

**相量域**:
$$\bar{V}_R = R\bar{I}_R$$

**特性**:
- 电压电流同相
- 纯有功功率

### 电感

**时域**:
$$v_L(t) = L\frac{di_L}{dt}$$

**相量域**:
$$\bar{V}_L = j\omega L\bar{I}_L = jX_L\bar{I}_L$$

**感抗**:
$$X_L = \omega L = 2\pi fL$$

**特性**:
- 电压超前电流90°
- 吸收无功功率

### 电容

**时域**:
$$i_C(t) = C\frac{dv_C}{dt}$$

**相量域**:
$$\bar{V}_C = \frac{1}{j\omega C}\bar{I}_C = -jX_C\bar{I}_C$$

**容抗**:
$$X_C = \frac{1}{\omega C} = \frac{1}{2\pi fC}$$

**特性**:
- 电压滞后电流90°
- 发出无功功率

### 阻抗

**定义**:
$$\bar{Z} = R + jX = |Z|\angle\phi$$

**阻抗模**:
$$|Z| = \sqrt{R^2 + X^2}$$

**阻抗角**:
$$\phi = \arctan\frac{X}{R}$$

## 功率计算

### 复功率

**定义**:
$$\bar{S} = \bar{V}\bar{I}^* = P + jQ$$

**有功功率**:
$$P = VI\cos\phi$$

**无功功率**:
$$Q = VI\sin\phi$$

**视在功率**:
$$S = VI = \sqrt{P^2 + Q^2}$$

### 功率因数

**定义**:
$$\cos\phi = \frac{P}{S}$$

**意义**:
- 功率传输效率
- 电流需求
- 损耗影响

## 网络方程

### 节点导纳方程

**矩阵形式**:
$$\mathbf{Y}\mathbf{V} = \mathbf{I}$$

**导纳矩阵元素**:
$$Y_{ii} = \sum_{j\neq i}y_{ij} + y_{i0}$$
$$Y_{ij} = -y_{ij}$$

### 功率方程

**节点功率**:
$$P_i = \sum_{j=1}^{n}V_iV_jY_{ij}\cos(\theta_i - \theta_j - \phi_{ij})$$
$$Q_i = \sum_{j=1}^{n}V_iV_jY_{ij}\sin(\theta_i - \theta_j - \phi_{ij})$$

## 适用条件

### 准稳态假设

**条件**:
- 基频50/60 Hz
- 波形正弦
- 幅值相位慢变

**时间尺度**:
- 机电暂态: ms~s
- 不适合: μs级电磁暂态

### 与EMT比较

| 特性 | 相量模型 | EMT模型 |
|-----|---------|---------|
| 时间步长 | 1-10 ms | 1-100 μs |
| 计算速度 | 快 | 慢 |
| 频率范围 | 基频 | 宽频 |
| 开关细节 | 无 | 有 |
| 谐波 | 无 | 有 |
| 适用分析 | 稳定性 | 过电压 |

## 发电机模型

### 经典模型

**电势方程**:
$$\bar{E}' = \bar{V} + jX'\bar{I}$$

**功率输出**:
$$P_e = \frac{E'V}{X'}\sin\delta$$

### 详细模型

**电压方程**:
$$\bar{E}_q = \bar{V} + (R_a + jX_q)\bar{I}$$

**功角特性**:
$$P_e = \frac{E_qV}{X_d}\sin\delta + \frac{V^2}{2}\left(\frac{1}{X_q} - \frac{1}{X_d}\right)\sin 2\delta$$

## 负荷模型

### 静态负荷

**恒阻抗**:
$$P = P_0\left(\frac{V}{V_0}\right)^2$$

**恒电流**:
$$P = P_0\frac{V}{V_0}$$

**恒功率**:
$$P = P_0$$

### 动态负荷

**感应电机**:
$$\frac{ds}{dt} = \frac{1}{2H}(T_m - T_e)$$

## 动态相量

### 时变相量

**定义**:
$$\bar{V}(t) = V(t)e^{j\theta(t)}$$

**瞬时电压**:
$$v(t) = Re[\sqrt{2}\bar{V}(t)e^{j\omega_0t}]$$

### 动态方程

**导数**:
$$\frac{d\bar{V}}{dt} = \frac{dV}{dt}e^{j\theta} + jV\frac{d\theta}{dt}e^{j\theta}$$

**应用**:
- 次同步振荡
- 电压动态
- 柔性建模

## 软件实现

### 商业软件
- PSS/E
- PowerWorld
- ETAP
- DIgSILENT

### 开源工具
- MATPOWER
- PSAT
- PandaPower

## 相关主题
- [[power-flow-calculation]] - 潮流计算
- [[electromechanical-simulation]] - 机电暂态仿真
- [[dynamic-phasor]] - 动态相量
- [[symmetrical-components]] - 对称分量

## 来源论文

参见 [[index.md]] 获取更多相量模型相关文献。

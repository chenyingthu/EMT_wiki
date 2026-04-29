---
title: "锁相环 (PLL)"
type: model
tags: [pll, phase-locked-loop, synchronization, grid-connection, control]
created: "2026-04-29"
---

# 锁相环 (Phase-Locked Loop, PLL)

## 1. 物理对象概述

### 1.1 功能与作用

锁相环是电力电子变换器与电网同步的核心控制单元：

**核心功能**：
- **相位跟踪**：实时跟踪电网电压相位角
- **频率估计**：估计电网频率
- **幅值检测**：检测电网电压幅值
- **正交信号生成**：生成正交的dq轴参考信号
- **不平衡/谐波适应**：在电网畸变条件下稳定运行

### 1.2 应用场景

| 应用 | PLL作用 | 特殊要求 |
|------|--------|---------|
| **并网逆变器** | 生成PWM参考相位 | 快速响应、低谐波敏感度 |
| **HVDC换流器** | 换相时刻同步 | 高可靠性 |
| **FACTS设备** | 电压相位参考 | 谐波抑制 |
| **电能质量** | 谐波检测参考 | 多频率跟踪 |
| **保护装置** | 故障相角参考 | 故障穿越 |

### 1.3 电网条件

**理想电网**：
- 正弦波形
- 三相平衡
- 频率恒定（50/60Hz）

**实际电网挑战**：
- **不平衡**：负序分量存在
- **谐波污染**：5、7、11、13次等
- **频率偏移**：±0.5Hz正常，±2Hz极端
- **电压跌落**：单相/三相故障
- **相位跳变**：故障清除后

## 2. 物理模型与数学描述

### 2.1 SRF-PLL (同步旋转坐标PLL)

#### 2.1.1 基本结构

**坐标变换**：
$$v_d = \frac{2}{3}(v_a \cos\theta + v_b \cos(\theta-120°) + v_c \cos(\theta+120°))$$
$$v_q = -\frac{2}{3}(v_a \sin\theta + v_b \sin(\theta-120°) + v_c \sin(\theta+120°))$$

**控制目标**：
- 理想：$v_q = 0$，$v_d = V_m$
- 控制目标：调节$\theta$使$v_q \to 0$

#### 2.1.2 线性化模型

**小信号模型**：

定义相位误差$\Delta\theta = \theta_{grid} - \theta_{pll}$

$$v_q \approx V_m \sin(\Delta\theta) \approx V_m \Delta\theta$$

**开环传递函数**：
$$G_{OL}(s) = \frac{V_m (k_p s + k_i)}{s^2}$$

**闭环传递函数**：
$$\frac{\theta_{pll}}{\theta_{grid}} = \frac{2\zeta\omega_n s + \omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

其中：
- $\omega_n = \sqrt{V_m k_i}$：自然频率
- $\zeta = \frac{k_p}{2}\sqrt{\frac{V_m}{k_i}}$：阻尼比

#### 2.1.3 参数设计

**典型参数**（50Hz电网）：

| 参数 | 快速响应 | 一般应用 | 抗扰优先 |
|------|---------|---------|---------|
| $\omega_n$ | 2π×50 rad/s | 2π×20 rad/s | 2π×10 rad/s |
| $\zeta$ | 0.707 | 0.707 | 1.0 |
| $k_p$ | 0.44 | 0.18 | 0.18 |
| $k_i$ | 31.0 | 4.93 | 1.23 |

**带宽选择**：
- 快PLL：100Hz带宽，1-2周波收敛
- 慢PLL：20Hz带宽，3-5周波收敛
- 典型：30-50Hz带宽

### 2.2 DSOGI-PLL (双二阶广义积分器PLL)

#### 2.2.1 SOGI结构

**二阶广义积分器**：
$$SOGI(s) = \frac{k\omega s}{s^2 + k\omega s + \omega^2}$$

**正交信号生成**：
- 输入：$v_\alpha$
- 输出：$v_\alpha$（同相），$v_\beta$（正交，-90°移相）

#### 2.2.2 DSOGI-PLL方程

**αβ轴电压**：
$$\frac{dv_\alpha}{dt} = k\omega(v_\alpha - \hat{v}_\alpha) - \omega \hat{v}_\beta$$
$$\frac{dv_\beta}{dt} = \omega \hat{v}_\alpha + k\omega(v_\beta - \hat{v}_\beta)$$

**优点**：
- 自适应滤波，抑制谐波
- 不平衡分量分离
- 频率自适应

### 2.3 抗不平衡改进型

#### 2.3.1 DDSRF-PLL (解耦双SRF-PLL)

**正负序分离**：

$$\mathbf{v}_{dq}^+ = \frac{1}{2}\begin{bmatrix} v_d - v_q' \\ v_q + v_d' \end{bmatrix}, \quad
\mathbf{v}_{dq}^- = \frac{1}{2}\begin{bmatrix} v_d + v_q' \\ v_q - v_d' \end{bmatrix}$$

其中$v_d', v_q'$为90°延时信号。

#### 2.3.2 滑动平均滤波

**MAF-PLL**：
$$MAF(s) = \frac{1 - e^{-sT_w}}{sT_w}$$

窗口时间：$T_w = T_{fundamental} = 20ms$（50Hz）

**特性**：
- 完全消除特定次谐波
- 引入1/2周波延时

## 3. EMT仿真模型

### 3.1 离散实现

**SRF-PLL离散化**：

**PI控制器**：
$$\omega[k] = k_p v_q[k] + k_i T_s \sum_{i=0}^{k} v_q[i]$$

**相位积分**：
$$\theta[k+1] = \theta[k] + T_s \cdot \omega[k]$$

**归一化**：
$$\theta = \text{mod}(\theta, 2\pi)$$

### 3.2 频率自适应

**频率估计更新**：
$$\omega_{pll}[k] = \omega_{ff} + \Delta\omega[k]$$

其中$\omega_{ff}$为前馈频率（314rad/s）。

**频率限幅**：
$$\omega_{min} \leq \omega_{pll} \leq \omega_{max}$$
典型：$2\pi \times 45 \leq \omega_{pll} \leq 2\pi \times 55$ rad/s

### 3.3 软件实现

**MATLAB/Simulink**：
```matlab
function [theta, omega] = srf_pll(v_abc, theta_prev, omega_ff, kp, ki, Ts)
    % 坐标变换
    v_dq = abc_to_dq(v_abc, theta_prev);
    v_q = v_dq(2);
    
    % PI控制
    error_integral = error_integral + v_q * Ts;
    omega = omega_ff + kp * v_q + ki * error_integral;
    
    % 限幅
    omega = max(2*pi*45, min(2*pi*55, omega));
    
    % 相位积分
    theta = theta_prev + omega * Ts;
    theta = mod(theta, 2*pi);
end
```

## 4. 典型参数

### 4.1 不同应用场景

| 应用 | 带宽 | 响应时间 | 特点 |
|------|------|---------|------|
| 并网逆变器 | 30-50Hz | 20-40ms | 快速跟踪 |
| HVDC | 10-20Hz | 50-100ms | 稳定优先 |
| 电能质量 | 5-10Hz | 100-200ms | 谐波抑制 |
| 微电网 | 20-30Hz | 30-60ms | 平衡响应 |

### 4.2 稳定性分析

**相位裕度**：45°-60°
**增益裕度**：>6dB
**最大超调**：<20%

## 5. 相关主题

- [[inverter-control|逆变器控制]] - 并网控制策略
- [[grid-synchronization|电网同步]] - 同步技术对比
- [[power-quality|电能质量]] - 谐波与不平衡

---

*本页面基于Karpathy LLM Wiki Pattern构建*

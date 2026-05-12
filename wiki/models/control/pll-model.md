---
title: "锁相环 (PLL)"
type: model
tags: [pll, phase-locked-loop, synchronization, grid-connection, control]
created: "2026-04-29"
updated: "2026-05-12"
---

# 锁相环 (Phase-Locked Loop, PLL)

## 定义与概述

锁相环是电力电子变换器与电网同步的核心控制单元，通过实时跟踪电网电压相位角、估计频率和生成正交参考信号，实现变换器的同步并网。在电网畸变（不平衡、谐波）条件下，改进型PLL（如DSOGI-PLL、MAF-PLL）能够保持稳定的同步性能。本模型涵盖SRF-PLL、DSOGI-PLL、DDSRF-PLL等拓扑，适用于并网逆变器、HVDC换流器、FACTS设备和电能质量分析。

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

## 5. 适用边界与限制

### 5.1 适用条件
- **电压范围**：额定电压±20%（低电压需特殊处理）
- **频率范围**：45-55Hz（超出需自适应算法）
- **谐波含量**：THD<10%（高谐波需改进型PLL）
- **不平衡度**：负序<5%（高不平衡需DSOGI-PLL）

### 5.2 模型限制
- **理想假设**：假设电网基波主导
- **非线性负载**：谐波负载可能影响同步精度
- **故障穿越**：严重故障期间可能失锁
- **噪声敏感**：测量噪声影响估计精度

### 量化性能边界

PLL 的 EMT 仿真精度取决于离散化数值精度（与变换器/电网模型一致）、PI 参数整定和外部电网强度，而非 PLL 算法框架本身的近似。以下汇总可引用的量化数据：

**SRF-PLL 仿真精度**：Luchini (2023) 在 ATP/ATPDraw 中验证了基于 SRF-PLL 的跟网型逆变器等效模型，与全开关基准模型相比，故障电流平均误差约 2.33%，仿真时间减少约 70%。Carreño (2026) 提出 RMS+ 模型用于 PLL 失稳分析，单换流器无穷大系统中 RMS+ 与 EMT 偏差小于 0.5%，而传统 RMS 模型在跨临界分岔边界完全失效（误差 100%）。

**DSOGI-PLL 改进效果**：Ranasinghe (2024) 提出带自适应带宽的改进型 DSOGI-PLL，在不对称故障下调节时间从 0.040 s 缩短至 0.016 s（-60%），超调从 0.272 rad 降至 0.113 rad（-58.5%）；90° 相位跳变下调节时间从 0.15 s 缩短至 0.03 s（-80%）；频率跟踪 RMSE 从 2.16 Hz 降至 0.001 Hz（衰减 99.95%）；SCR 稳定下限从 2.3 扩展至 1.0。

**弱网失稳边界**：Carreño (2026) 给出 SRF-PLL 跨临界分岔条件为 $K_p > 1/(i_P \cdot L)$，Hopf 分岔条件为 $K_i/K_p > \sqrt{V^2 - (i_P \cdot X)^2}/(i_P \cdot L)$；SCR < 2 时 Hopf 分岔临界功率下降约 40%（0.9 → 0.55 pu）。Li (2024) 指出弱网下 PLL 带宽与外环带宽接近并不必然引发失稳，但 70.3 Hz 谐振频率表明 PLL 参数不当可能激发中频段振荡。

**初始化影响**：Guilherme (2023) 证明 PLL 角度需包含低通滤波器相移补偿，否则产生 300 ms 以上的启动暂态。

**数据缺口声明**：PLL 的相位/频率稳态跟踪误差主要取决于电网条件（谐波含量、不平衡度）而非仿真精度限制；不同 PLL 拓扑（SRF、DSOGI、MAF、DDSRF）的对比缺乏统一标准化测试基准，跨文献比较需注意测试条件差异。

## 6. 相关主题与链接

### 6.1 相关模型
- [[gfl-inverter-model|跟网型变流器]] - 并网逆变器控制
- [[vsc-model|VSC模型]] - 电压源变换器
- [[coordinate-transformation-model|坐标变换模型]] - dq变换实现
- [[pi-controller-model|PI控制器]] - 锁相环PI参数设计

### 6.2 相关方法
- [[numerical-integration|数值积分]] - 相位角积分计算
- [[state-space-method|状态空间法]] - PLL小信号分析
- [[frequency-dependent-modeling|频率相关建模]] - 频率自适应

### 6.3 相关主题
- 逆变器控制 - 并网控制策略
- 电网同步 - 同步技术对比
- 电能质量 - 谐波与不平衡

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

---
title: "锁相环 (PLL)"
type: model
tags: [pll, phase-locked-loop, synchronization, grid-connection, control, dsogi-pll, srf-pll, rms-plus]
created: "2026-04-29"
updated: "2026-05-18"
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

**SOGI阻尼因子选择**：
Ranasinghe (2024) 表明，优化的SOGI阻尼因子值为 $k = 1.47$，可获得有利的settling time、overshoot和谐波抑制特性，对应阻尼比 $\zeta = \sqrt{2} \approx 1.414$。

#### 2.2.2 DSOGI-PLL方程

**αβ轴电压**：
$$\frac{dv_\alpha}{dt} = k\omega(v_\alpha - \hat{v}_\alpha) - \omega \hat{v}_\beta$$
$$\frac{dv_\beta}{dt} = \omega \hat{v}_\alpha + k\omega(v_\beta - \hat{v}_\beta)$$

**开环传递函数**（小信号模型）：
$$G_{ol,DSOGI-PLL}(s) = \frac{K_p s + K_i}{s} \cdot \frac{\omega_p}{s + \omega_p}$$

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

## 3. PLL失稳机理与RMS+模型

### 3.1 传统RMS模型的局限性

传统的RMS（均方根）电路模型将网络表示为纯阻抗矩阵，假设所有瞬态已稳定到正弦稳态。该模型无法捕捉PLL的以下两种小信号失稳机理：

1. **di/dt效应**：感性支路电流变化率影响电压降
2. **正反馈回路**：PLL角度通过电流命令影响有功功率注入，进而影响电网电压

**EMT vs RMS电路方程对比**：

$$RMS: u_{dq} = i_{dq}(jX) + V$$
$$EMT: u_{dq} = i_{dq}(jX) + L\frac{di_{dq}}{dt} + V$$

其中 $L\frac{di_{dq}}{dt}$ 项在RMS模型中被忽略，但这正是PLL失稳的关键机制。

### 3.2 分岔边界条件

Carreño (2026) 给出PLL小信号稳定性的完整边界条件：

**电压稳定条件**：
$$V > |i_P \cdot X|$$

**跨临界分岔条件**：
$$1 - K_p \cdot i_P \cdot L > 0$$

**Hopf分岔条件**：
$$K_p \cdot V^2 - (i_P \cdot X)^2 - K_i \cdot i_P \cdot L > 0$$

其中：
- $K_p, K_i$：PLL的比例和积分增益
- $i_P$：有功功率命令（p.u.）
- $L$：线路电感（p.u.）
- $X = \omega_n L$：线路电抗

**关键发现**：
- 跨临界分岔发生在 $K_p$ 超过极限值时
- Hopf分岔发生在 $K_i/K_p$ 比值超过极限时
- 高有功功率注入 ($i_P$) 和大电感 ($L$) 使系统更易失稳

### 3.3 RMS+电路模型

RMS+模型基于慢-快系统理论，在RMS模型基础上增加"等效电感矩阵"项：

$$V_{GFL} + Y_{redD}^{-1} Y_{redC} V_\infty = (Z_{eq} + L_p) I_{GFL}$$

其中：
- $Z_{eq}$：等效阻抗矩阵
- $L$：等效电感矩阵（捕捉电流导数对电压的敏感性）
- $p = d/dt$：微分算子

**L矩阵计算流程**：
1. 将支路电流表示为有源设备电流的线性组合
2. 利用最小二乘法恢复原始电感方程
3. 得到复数形式的等效电感

### 3.4 稳定性边界量化数据

**单换流器无穷大系统测试结果**（Carreño 2026）：

| 测试条件 | 参数设置 | 临界值 | 不稳定值 |
|---------|---------|--------|----------|
| Kp扫描（Ki=100固定）| Kp: 10→700 | Kp=547 | Kp=623 |
| Ki扫描（Kp=5固定）| Ki: 100→3000 | Ki=2322 | Ki=2600 |

**弱网SCR影响**：
- SCR < 2时，Hopf分岔临界功率下降约40%（从0.9 p.u.降至0.55 p.u.）
- SCR定义：$SCR = \frac{S_{sc}}{P_{vsc}} = \frac{V}{i_{Pmax} X}$

## 4. 自适应带宽DSOGI-PLL

### 4.1 暂态检测器

暂态检测器识别电网频率的突变，通过以下机制工作：

1. **检测触发**：监测频率变化率 (ROCOF)
2. **频率冻结**：当检测到暂态时，将频率输出冻结 $T_{fz}$ 周期
3. **SOGI输入稳定化**：冻结的频率提供给SOGI模块，减少暂态期间的滤波干扰

**参数设置**：
- 频率冻结周期：$T_{fz} = 1.4T$（T为基波周期）

### 4.2 自适应带宽控制

**带宽调整策略**：
- 正常运行时，带宽设置为较低值（如 $\omega_p = 1.4$ rad/s）
- 检测到相位误差超过阈值时，带宽快速增加（可增大8倍）
- 条件恢复后，带宽逐步回调至原始值

**目标**：
- 暂态期间：快速响应，最小化相位误差超调
- 稳态期间：抑制谐波，保持跟踪精度

### 4.3 性能量化对比

Ranasinghe (2024) 在IEEE 9总线系统和PSCAD仿真中验证：

**不对称故障下性能**：

| 指标 | 标准DSOGI-PLL | 自适应带宽DSOGI-PLL | 改善幅度 |
|------|--------------|-------------------|---------|
| Settling time | 0.040 s | 0.016 s | **-60%** |
| Overshoot | 0.272 rad | 0.113 rad | **-58.5%** |

**90°相位跳变下性能**：

| 指标 | 标准DSOGI-PLL | 自适应带宽DSOGI-PLL | 改善幅度 |
|------|--------------|-------------------|---------|
| Settling time | 0.15 s | 0.03 s | **-80%** |

**频率跟踪RMSE**：

| 测试场景 | 标准DSOGI-PLL | 自适应带宽DSOGI-PLL |
|---------|--------------|-------------------|
| 谐波注入 (THD 2%) | 0.16 rad | 0.016 rad |
| 谐波注入 (THD 4%) | 0.19 rad | 0.026 rad |
| 频率斜坡 (7Hz/s) | 0.18 rad | 0.014 rad |
| 频率RMSE | **2.16 Hz** | **0.001 Hz** |

### 4.4 弱网稳定性边界

在光伏电站-电网系统中测试（SCR接近1.1）：
- 标准DSOGI-PLL：系统故障清除后失稳（移除Line 8-9）
- 自适应带宽DSOGI-PLL：SCR可降低至**1.0**仍保持稳定

**关键改进**：SCR稳定下限从2.3扩展至1.0，扩展了**130%**。

## 5. EMT仿真模型

### 5.1 离散实现

**SRF-PLL离散化**：

**PI控制器**：
$$\omega[k] = k_p v_q[k] + k_i T_s \sum_{i=0}^{k} v_q[i]$$

**相位积分**：
$$\theta[k+1] = \theta[k] + T_s \cdot \omega[k]$$

**归一化**：
$$\theta = \text{mod}(\theta, 2\pi)$$

### 5.2 频率自适应

**频率估计更新**：
$$\omega_{pll}[k] = \omega_{ff} + \Delta\omega[k]$$

其中$\omega_{ff}$为前馈频率（314rad/s）。

**频率限幅**：
$$\omega_{min} \leq \omega_{pll} \leq \omega_{max}$$
典型：$2\pi \times 45 \leq \omega_{pll} \leq 2\pi \times 55$ rad/s

### 5.3 软件实现

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

## 6. 典型参数

### 6.1 不同应用场景

| 应用 | 带宽 | 响应时间 | 特点 |
|------|------|---------|------|
| 并网逆变器 | 30-50Hz | 20-40ms | 快速跟踪 |
| HVDC | 10-20Hz | 50-100ms | 稳定优先 |
| 电能质量 | 5-10Hz | 100-200ms | 谐波抑制 |
| 微电网 | 20-30Hz | 30-60ms | 平衡响应 |

### 6.2 稳定性分析

**相位裕度**：45°-60°
**增益裕度**：>6dB
**最大超调**：<20%

### 6.3 Carreño (2026) 测试系统参数

**WSCC 9总线系统**：
- 慢PLL：$K_p = 5$ p.u., $K_i = 100 \sim 3500$ p.u.
- 快PLL：$K_p = 500$ p.u., $K_i = 90 \times 10^3 \sim 500 \times 10^3$ p.u.
- 临界对：$K_i = 3014$ p.u.（稳定），$K_i = 3257$ p.u.（失稳）

**39总线新英格兰测试系统**：
- SRF-PLL参数：$K_p = 20$ p.u., $K_i = 200$ p.u.
- 状态变量：EMT模型270个 → RMS+模型108个
- 计算速度提升：**约14倍**

## 7. 适用边界与限制

### 7.1 适用条件
- **电压范围**：额定电压±20%（低电压需特殊处理）
- **频率范围**：45-55Hz（超出需自适应算法）
- **谐波含量**：THD<10%（高谐波需改进型PLL）
- **不平衡度**：负序<5%（高不平衡需DSOGI-PLL）

### 7.2 模型限制
- **理想假设**：假设电网基波主导
- **非线性负载**：谐波负载可能影响同步精度
- **故障穿越**：严重故障期间可能失锁
- **噪声敏感**：测量噪声影响估计精度

### 7.3 RMS+模型适用性

**适用场景**：
- PLL与其他控制器的时间尺度分离明确时
- 研究低频振荡（PLL模式）时
- 需要快速筛选大规模网络的同步稳定性时

**不适用场景**：
- 谐波稳定性分析
- 电容动态与PLL交互的高频振荡研究
- 快PLL（时间尺度分离不满足）场景

## 8. 相关主题与链接

### 8.1 相关模型
- [[gfl-inverter-model]] - 跟网型变流器并网控制
- [[vsc-model]] - 电压源变换器
- [[coordinate-transformation-model]] - dq坐标变换实现
- [[pi-controller-model]] - 锁相环PI参数设计

### 8.2 相关方法
- [[numerical-integration]] - 数值积分
- [[modal-analysis]] - 模态分析（特征值分析）
- [[phasor-model]] - 相量模型

### 8.3 相关主题
- [[power-electronics]] - 电力电子组件
- [[vsc-hvdc]] - VSC-HVDC换流器
- [[weak-grid-vsc]] - 弱网VSC等效

## 9. 量化性能边界汇总

**SRF-PLL仿真精度**：Luchini (2023) 在ATP/ATPDraw中验证了基于SRF-PLL的跟网型逆变器等效模型，与全开关基准模型相比，故障电流平均误差约2.33%，仿真时间减少约70%。Carreño (2026) 提出RMS+模型用于PLL失稳分析，单换流器无穷大系统中RMS+与EMT偏差小于0.5%，而传统RMS模型在跨临界分岔边界完全失效（误差100%）。

**DSOGI-PLL改进效果**：Ranasinghe (2024) 提出带自适应带宽的改进型DSOGI-PLL，在不对称故障下调节时间从0.040s缩短至0.016s（-60%），超调从0.272rad降至0.113rad（-58.5%）；90°相位跳变下调节时间从0.15s缩短至0.03s（-80%）；频率跟踪RMSE从2.16Hz降至0.001Hz（衰减99.95%）；SCR稳定下限从2.3扩展至1.0。

**弱网失稳边界**：Carreño (2026) 给出SRF-PLL跨临界分岔条件为 $K_p > 1/(i_P \cdot L)$，Hopf分岔条件为 $K_i/K_p > \sqrt{V^2 - (i_P \cdot X)^2}/(i_P \cdot L)$；SCR<2时Hopf分岔临界功率下降约40%（0.9→0.55pu）。Li (2024) 指出弱网下PLL带宽与外环带宽接近并不必然引发失稳，但70.3Hz谐振频率表明PLL参数不当可能激发中频段振荡。

**初始化影响**：Guilherme (2023) 证明PLL角度需包含低通滤波器相移补偿，否则产生300ms以上的启动暂态。
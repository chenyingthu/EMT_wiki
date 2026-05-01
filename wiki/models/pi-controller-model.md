---
title: "PI/PID控制器 (PI/PID Controller)"
type: model
tags: [pi-controller, pid-controller, control-system, feedback, regulator, power-electronics]
created: "2026-04-30"
---

# PI/PID控制器 (PI/PID Controller)

## 定义与概述

PI（比例-积分）和PID（比例-积分-微分）控制器是EMT仿真中最广泛使用的线性反馈控制器，用于电压调节、电流控制、功率控制等闭环控制回路。在电力系统EMT仿真中，PI控制器因其结构简单、参数整定成熟、对常值干扰具有无静差特性而被普遍采用。本模型涵盖模拟PI/PID、离散化实现、抗饱和设计，适用于各种电力电子和电力系统控制应用。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 误差信号调节
- 系统稳态精度保证
- 动态响应优化
- 扰动抑制

**控制器类型**:
| 类型 | 传递函数 | 特点 | 应用 |
|------|----------|------|------|
| P | $K_p$ | 快速响应、有静差 | 快速响应场合 |
| PI | $K_p + \frac{K_i}{s}$ | 无静差、相位滞后 | 电压/电流调节 |
| PD | $K_p + K_d s$ | 超前校正、预测 | 需要微分作用的场合 |
| PID | $K_p + \frac{K_i}{s} + K_d s$ | 综合性能最优 | 复杂动态系统 |

### 1.2 控制结构

**标准反馈结构**:
```
        误差e
  设定值 ──→⊕──→[控制器]──→[被控对象]──→ 输出
           ↑-                    │
           └────[反馈]───────────┘
```

**PI控制器时域方程**:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau$$

**PID控制器时域方程**:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

### 1.3 运行激励

**输入信号**：
- 误差信号：$e(t) = r(t) - y(t)$
- 参考值：设定目标值
- 反馈值：被控量测量值
- 扰动：负载变化、参数漂移

**输出信号**：
- 控制量：驱动被控对象的信号
- 饱和限制：上下限约束
- 速率限制：变化率约束

**动态要求**：
- 上升时间：响应速度
- 超调量：动态品质
- 调节时间：稳定速度
- 稳态误差：静态精度

## 2. 物理模型与数学描述

### 2.1 模拟域模型

#### 2.1.1 PI控制器

**传递函数**:
$$G_{PI}(s) = K_p + \frac{K_i}{s} = K_p \frac{1 + T_i s}{T_i s}$$

其中 $T_i = K_p/K_i$ 为积分时间常数。

**状态空间形式**:
$$\frac{dx_i}{dt} = e(t)$$
$$u(t) = K_p e(t) + K_i x_i(t)$$

**频率特性**:
- 低频（$\omega \ll 1/T_i$）：积分主导，增益以-20dB/dec下降，相位-90°
- 转折频率：$\omega_i = K_i/K_p = 1/T_i$
- 高频（$\omega \gg 1/T_i$）：比例主导，增益恒定，相位0°

#### 2.1.2 PID控制器

**理想PID传递函数**:
$$G_{PID}(s) = K_p + \frac{K_i}{s} + K_d s$$

**实际PID（含滤波）**:
$$G_{PID}(s) = K_p \left(1 + \frac{1}{T_i s} + \frac{T_d s}{1 + \frac{T_d}{N}s}\right)$$

其中 $N$ 为微分增益限制系数（通常5-20）。

**状态空间形式**:
$$\frac{dx_i}{dt} = e$$
$$\frac{dx_d}{dt} = \frac{N}{T_d}(e - x_d)$$
$$u = K_p e + K_i x_i + K_d \frac{N}{T_d}(e - x_d)$$

### 2.2 参数整定方法

#### 2.2.1 Ziegler-Nichols方法

**临界比例度法**:
1. 纯比例控制，增大增益直至临界振荡
2. 记录临界增益 $K_u$ 和振荡周期 $T_u$

**PID参数**:
| 控制器 | $K_p$ | $T_i$ | $T_d$ |
|--------|-------|-------|-------|
| P | $0.5K_u$ | - | - |
| PI | $0.45K_u$ | $0.83T_u$ | - |
| PID | $0.6K_u$ | $0.5T_u$ | $0.125T_u$ |

#### 2.2.2 对称最优法

针对二阶系统，优化相位裕度：
$$K_p = \frac{1}{2K_s T_s}$$
$$T_i = 4T_s$$

其中 $K_s$ 和 $T_s$ 为被控对象参数。

#### 2.2.3 模量最优法

最小化闭环传递函数模量偏差：
$$K_p = \frac{1}{2K_s T_s}$$
$$T_i = T_s$$

### 2.3 抗饱和设计

#### 2.3.1 积分饱和问题

当控制量达到饱和限时，积分器继续累积导致超调。

**条件积分（Clamping）**:
$$\frac{dx_i}{dt} = \begin{cases}
0, & \text{if } u_{unsat} > u_{max} \text{ and } e > 0 \\
0, & \text{if } u_{unsat} < u_{min} \text{ and } e < 0 \\
e, & \text{otherwise}
\end{cases}$$

#### 2.3.2 反计算抗饱和

```
        e
        │
        ▼
   ┌─────────┐
   │  Kp+Ki/s │──→⊕──→⊕──→ u_sat
   └─────────┘   ↑   ↑
                 │   └── 饱和环节
                 └────── 反馈回路 (u_unsat - u_sat)
```

**修正积分**:
$$\frac{dx_i}{dt} = e + \frac{1}{T_t}(u_{sat} - u_{unsat})$$

其中 $T_t$ 为跟踪时间常数。

## 3. EMT仿真模型

### 3.1 离散化方法

#### 3.1.1 后向欧拉法

**积分项离散化**:
$$x_i[k] = x_i[k-1] + K_i T_s e[k]$$

**微分项离散化**:
$$u_d[k] = K_d \frac{e[k] - e[k-1]}{T_s}$$

**完整PI离散**:
$$u[k] = K_p e[k] + x_i[k]$$
$$x_i[k] = x_i[k-1] + K_i T_s e[k]$$

#### 3.1.2 梯形法（Tustin）

**积分项**:
$$x_i[k] = x_i[k-1] + \frac{K_i T_s}{2}(e[k] + e[k-1])$$

**微分项（带滤波）**:
$$u_d[k] = \frac{2\tau - T_s}{2\tau + T_s} u_d[k-1] + \frac{2K_d}{2\tau + T_s}(e[k] - e[k-1])$$

其中 $\tau = T_d/N$。

#### 3.1.3 增量式PID

**增量形式**:
$$\Delta u[k] = K_p(e[k] - e[k-1]) + K_i T_s e[k] + \frac{K_d}{T_s}(e[k] - 2e[k-1] + e[k-2])$$

**优点**：
- 无积分饱和问题
- 便于实现无扰切换
- 计算量小

### 3.2 多速率实现

在EMT仿真中，控制器通常以比电路仿真更大的步长运行：

```
电路仿真:  Δt_circuit = 1-50 μs
控制仿真:  Δt_control = 100-1000 μs
```

**实现方式**:
- 每N个电路步长执行一次控制器
- 使用插值获取中间时刻的反馈值
- 控制输出在步长间保持恒定

### 3.3 定点数实现

用于DSP/FPGA实现：

**Q格式定点数**:
$$u_{fixed} = \text{round}(u \cdot 2^Q)$$

**系数缩放**:
$$K_p' = K_p \cdot 2^{Q_k}$$
$$K_i' = K_i T_s \cdot 2^{Q_k}$$

**防溢出**:
- 中间结果使用扩展精度
- 饱和限制防止溢出

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**标准PI控制器**:
```fortran
! PI控制器
REAL Kp, Ki, error, integral, output

! 积分项
INTEGRAL = INTEGRAL + Ki * DT * ERROR

! 输出计算
OUTPUT_UNSAT = Kp * ERROR + INTEGRAL

! 饱和限制
IF (OUTPUT_UNSAT > U_MAX) THEN
  OUTPUT = U_MAX
  ! 条件积分：积分不增加
  IF (ERROR > 0) INTEGRAL = INTEGRAL - Ki * DT * ERROR
ELSE IF (OUTPUT_UNSAT < U_MIN) THEN
  OUTPUT = U_MIN
  ! 条件积分：积分不减小
  IF (ERROR < 0) INTEGRAL = INTEGRAL - Ki * DT * ERROR
ELSE
  OUTPUT = OUTPUT_UNSAT
END IF
```

**抗饱和PI**:
```fortran
! 反计算抗饱和
TRACKING_GAIN = 1.0 / Ti  ! 跟踪增益
SATURATION_ERROR = OUTPUT - OUTPUT_UNSAT
INTEGRAL = INTEGRAL + Ki * DT * ERROR + DT * TRACKING_GAIN * SATURATION_ERROR
```

### 4.2 MATLAB/Simulink实现

**Simulink模型**:
```matlab
% PI Controller
Kp = 1.0;
Ki = 100.0;

% 使用PID Controller模块并设Kd=0
pid_controller = pid(Kp, Ki, 0);
```

**自定义S函数**:
```matlab
function sys = pi_controller_m(t, x, u, flag, params)
    Kp = params.Kp;
    Ki = params.Ki;
    Ts = params.Ts;
    
    switch flag
        case 2  % 更新离散状态
            error = u(1);
            integral = x(1);
            
            % 条件积分抗饱和
            u_unsat = Kp * error + integral;
            u_sat = max(min(u_unsat, params.Umax), params.Umin);
            
            if u_unsat == u_sat  % 未饱和
                sys = integral + Ki * Ts * error;
            else  % 饱和，积分不变
                sys = integral;
            end
            
        case 3  % 计算输出
            error = u(1);
            integral = x(1);
            sys = Kp * error + integral;
    end
end
```

### 4.3 C代码实现

**离散PI控制器**:
```c
typedef struct {
    float Kp;        // 比例增益
    float Ki;        // 积分增益
    float Ts;        // 采样周期
    float integral;  // 积分状态
    float Umax;      // 输出上限
    float Umin;      // 输出下限
} PI_Controller;

float PI_Update(PI_Controller *ctrl, float error) {
    float output_unsat, output;
    
    // 计算未饱和输出
    output_unsat = ctrl->Kp * error + ctrl->integral;
    
    // 饱和限制
    output = (output_unsat > ctrl->Umax) ? ctrl->Umax :
             (output_unsat < ctrl->Umin) ? ctrl->Umin : output_unsat;
    
    // 条件积分：仅当未饱和时更新积分
    if (output == output_unsat) {
        ctrl->integral += ctrl->Ki * ctrl->Ts * error;
    }
    
    return output;
}
```

## 5. 典型参数参考

### 5.1 电流环PI参数

| 应用 | $K_p$ | $K_i$ | 带宽 | 相位裕度 |
|------|-------|-------|------|----------|
| VSC电流环 | 0.5-2.0 | 50-200 | 200-500Hz | 60°-80° |
| 电机电流环 | 1.0-5.0 | 100-500 | 500-2000Hz | 60°-80° |
| 逆变器电流环 | 0.3-1.0 | 30-100 | 100-300Hz | 60°-80° |

### 5.2 电压环PI参数

| 应用 | $K_p$ | $K_i$ | 带宽 | 相位裕度 |
|------|-------|-------|------|----------|
| DC-Link电压 | 0.1-0.5 | 5-20 | 10-50Hz | 45°-60° |
| AC电压幅值 | 0.05-0.2 | 2-10 | 5-20Hz | 45°-60° |
| 无功功率 | 0.01-0.1 | 0.5-5 | 1-10Hz | 45°-60° |

### 5.3 功率环PI参数

| 应用 | $K_p$ | $K_i$ | 带宽 |
|------|-------|-------|------|
| 有功功率 | 0.005-0.02 | 0.1-0.5 | 1-5Hz |
| 频率调节 | 0.01-0.05 | 0.2-1.0 | 0.5-2Hz |
| 直流电压 | 0.1-0.5 | 2-10 | 5-20Hz |

### 5.4 整定经验公式

**电流内环（典型）**:
$$K_p = \frac{L}{\tau_{des}}$$
$$K_i = \frac{R}{\tau_{des}}$$

其中 $\tau_{des}$ 为期望时间常数（通常1-5ms）。

**电压外环（典型）**:
$$K_p = \frac{C}{10\tau_{current}}$$
$$K_i = \frac{K_p}{10\tau_{current}}$$

## 6. 相关主题与链接

### 6.1 相关模型
- [[vsc-model|VSC模型]] - 电压源换流器控制
- [[mmc-model|MMC模型]] - 模块化多电平换流器控制
- [[pll-model|锁相环]] - 同步参考坐标系

### 6.2 相关方法
- [[numerical-integration|数值积分]] - 控制器离散化
- [[multirate-method|多速率方法]] - 多时间尺度仿真

### 6.3 相关主题
- 矢量控制 - 电机控制策略
- 下垂控制 - 电网支撑控制
- 模型预测控制 - 先进控制策略

## 7. 适用边界与限制

### 7.1 适用条件
- **系统类型**：线性或弱非线性系统
- **扰动类型**：常值或慢变扰动
- **动态范围**：控制器带宽应远小于开关频率（通常<1/10）
- **采样频率**：根据香农定理，$f_s > 2f_{bw}$

### 7.2 模型限制
- **非线性系统**：对强非线性系统效果有限
- **时变系统**：参数时变需自适应调整
- **时延系统**：大时延可能导致不稳定
- **MIMO系统**：需解耦或多变量设计
- **约束处理**：简单饱和处理可能非最优

### 7.3 精度边界
| 实现方式 | 计算精度 | 适用范围 |
|---------|----------|----------|
| 模拟PI | 无限（理论） | 连续系统分析 |
| 双精度浮点 | ~1e-15 | 离线仿真 |
| 单精度浮点 | ~1e-7 | 实时仿真 |
| 32位定点 | ~1e-4 | FPGA/DSP |
| 16位定点 | ~1e-2 | 低成本实现 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Digital PI controller design for power electronic converters | 2012 | 电力电子变换器数字PI设计 |
| Anti-windup design for PI controllers in EMT simulation | 2015 | EMT仿真PI抗饱和设计 |
| Tuning of PI controllers for VSC-HVDC systems | 2018 | VSC-HVDC系统PI参数整定 |

## 相关方法
- [[numerical-integration|数值积分]] - 控制器离散化实现
- [[multirate-method|多速率方法]] - 多时间尺度仿真
- [[state-space-method|状态空间法]] - 控制系统状态分析

## 相关模型
- [[vsc-model|VSC模型]] - 电压源换流器控制
- [[mmc-model|MMC模型]] - 模块化多电平换流器控制
- [[pll-model|锁相环]] - 同步参考坐标系
- [[coordinate-transformation-model|坐标变换]] - dq变换实现

## 相关主题
- [[vector-control-model|矢量控制模型]] - 电机控制策略
- [[droop-control-model|下垂控制模型]] - 电网支撑控制
- 先进控制策略 - 模型预测控制
- [[real-time-simulation|实时仿真]] - 控制器实时实现

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

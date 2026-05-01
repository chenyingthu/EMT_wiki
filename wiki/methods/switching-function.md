---
title: "开关函数法 (Switching Function Method)"
type: method
tags: [switching-function, power-electronics, converter-modeling, emt-simulation, averaged-model]
created: "2026-04-30"
---

# 开关函数法 (Switching Function Method)

## 定义与概述

开关函数法是电力电子装置电磁暂态建模的核心方法，通过数学函数描述功率半导体器件（IGBT、二极管等）的导通/关断状态，将离散的开关动作转化为连续的数学表达。在EMT仿真中，该方法广泛应用于MMC、VSC、DC-DC变换器等电力电子装置的建模，是实现详细模型与平均值模型之间灵活转换的基础工具。

## 1. 理论基础

### 1.1 基本开关函数定义

**单相开关函数**:
$$S(t) = \begin{cases} 1, & \text{开关导通} \\ 0, & \text{开关关断} \end{cases}$$

**PWM调制开关函数**:
$$S_i = \begin{cases} 1, & v_m > v_c \\ 0, & v_m \leq v_c \end{cases}, \quad i=a,b,c$$

其中：
- $v_m$: 正弦调制波
- $v_c$: 三角载波

### 1.2 占空比与等效控制

**占空比计算**:
$$d_i = \frac{1}{T_s}\int_{t-T_s}^{t} S_i(\tau) d\tau$$

其中：
- $T_s$: 开关周期
- $d_i \in [0, 1]$: 占空比

**桥臂平均开关函数**:
$$S = \frac{1}{N} \sum_{i=1}^{N} S_i$$

用于MMC平均值模型中将N个子模块的投切状态平均化。

### 1.3 状态空间平均

**状态空间平均方程**:
$$\dot{x}(t) = \left[ A_{on}d(t) + A_{off}(1-d(t)) \right] x(t) + \left[ B_{on}d(t) + B_{off}(1-d(t)) \right] u(t)$$

其中：
- $A_{on}, A_{off}$: 导通/关断状态系统矩阵
- $B_{on}, B_{off}$: 导通/关断状态输入矩阵
- $d(t)$: 时变占空比

## 2. EMT仿真应用

### 2.1 MMC桥臂建模

**半桥子模块开关函数**:
$$i_{ck}(t) = S_k(t) \cdot i_{arm}(t)$$

其中：
- $i_{ck}$: 第k个子模块电容电流
- $S_k$: 第k个子模块开关函数
- $i_{arm}$: 桥臂电流

**带闭锁功能的统一模型**:
$$i_{ck}(t) = (b(t) + \bar{b}(t)S_k(t)) i(t)$$

其中：
- $b(t)$: 闭锁信号（1=闭锁，0=正常）
- $\bar{b}(t)$: 闭锁信号取反

**全桥子模块开关函数**:
$$i_{ck}(t) = b(t)(S_{1k}(t) - S_{3k}(t)) i_{arm}(t) + \bar{b}(t) i(t)$$

利用两组开关函数差值控制正常模式充放电，闭锁时切换为二极管续流路径。

### 2.2 VSC并网变流器

**三相VSC开关函数向量**:
$$\mathbf{S}_{abc} = \begin{bmatrix} S_a \\ S_b \\ S_c \end{bmatrix}$$

**交流侧电压合成**:
$$\mathbf{v}_{abc} = \mathbf{S}_{abc} \cdot V_{dc} - \mathbf{v}_{neutral}$$

其中：
- $V_{dc}$: 直流侧电压
- $\mathbf{v}_{neutral}$: 中性点电压

### 2.3 DC-DC变换器

**Buck变换器开关函数**:
$$v_{out} = S(t) \cdot V_{in}$$

**Boost变换器开关函数**:
$$i_{in} = S(t) \cdot i_L$$

## 3. 实现技术

### 3.1 详细模型实现

**理想开关模型**:
```fortran
! PSCAD/EMTDC 开关函数实现
IF (V_CONTROL .GT. 0.0) THEN
    S = 1.0  ! 导通
ELSE
    S = 0.0  ! 关断
ENDIF

! 更新支路导纳
IF (S .EQ. 1.0) THEN
    G_SWITCH = G_ON   ! 导通电阻倒数
ELSE
    G_SWITCH = G_OFF  ! 关断电阻倒数
ENDIF
```

### 3.2 平均值模型实现

**MATLAB状态空间平均**:
```matlab
function dx = switching_function_model(t, x, params)
    % 提取参数
    d = params.duty_cycle;      % 占空比
    Aon = params.A_on;
    Aoff = params.A_off;
    Bon = params.B_on;
    Boff = params.B_off;
    u = params.input;
    
    % 计算等效系统矩阵
    A_eq = Aon * d + Aoff * (1 - d);
    B_eq = Bon * d + Boff * (1 - d);
    
    % 状态方程
    dx = A_eq * x + B_eq * u;
end
```

### 3.3 广义状态空间平均

**傅里叶系数展开**:
$$\langle x \rangle_k(t) = \frac{1}{T}\int_{t-T}^{t} x(\tau)e^{-jk\omega_s \tau} d\tau$$

**微分性质**:
$$\left\langle \frac{dx}{dt} \right\rangle_q = \frac{d\langle x \rangle_q}{dt} - jq\omega_s \langle x \rangle_q$$

**乘积卷积性质**:
$$\langle xy \rangle_q = \sum_{i=-\infty}^{\infty} \langle x \rangle_{q-i} \langle y \rangle_i$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

```fortran
! MMC桥臂开关函数模块
SUBROUTINE SWITCHING_FUNCTION(N_SM, S_ARRAY, I_ARM, I_CAP)
    INTEGER N_SM
    REAL S_ARRAY(N_SM)
    REAL I_ARM
    REAL I_CAP(N_SM)
    
    ! 计算各子模块电容电流
    DO K = 1, N_SM
        I_CAP(K) = S_ARRAY(K) * I_ARM
    END DO
    
    ! 桥臂总电压合成
    V_ARM = 0.0
    DO K = 1, N_SM
        V_ARM = V_ARM + S_ARRAY(K) * V_CAP(K)
    END DO
END SUBROUTINE
```

### 4.2 MATLAB/Simulink实现

```matlab
classdef SwitchingFunctionMMC < handle
    properties
        N_sm          % 子模块数量
        S_vec         % 开关函数向量
        V_cap         % 电容电压
    end
    
    methods
        function obj = SwitchingFunctionMMC(N)
            obj.N_sm = N;
            obj.S_vec = zeros(N, 1);
            obj.V_cap = zeros(N, 1);
        end
        
        function update_switching_state(obj, gate_signals)
            % 更新开关函数
            obj.S_vec = gate_signals > 0;
        end
        
        function v_arm = calculate_arm_voltage(obj)
            % 计算桥臂等效电压
            v_arm = sum(obj.S_vec .* obj.V_cap);
        end
        
        function i_cap = calculate_capacitor_current(obj, i_arm)
            % 计算各电容电流
            i_cap = obj.S_vec * i_arm;
        end
    end
end
```

## 5. 典型参数参考

| 应用场景 | 开关频率 | 仿真步长 | 平均开关函数阶数 | 计算加速比 |
|----------|----------|----------|------------------|------------|
| MMC-HVDC | 50-200 Hz | 10-50 μs | 基波+2次谐波 | 10-50倍 |
| 两电平VSC | 2-10 kHz | 1-10 μs | 基波 | 5-20倍 |
| DC-DC变换器 | 10-100 kHz | 0.1-1 μs | 基波 | 50-200倍 |
| 级联H桥 | 1-5 kHz | 5-20 μs | 基波+3次谐波 | 10-30倍 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[mmc-model|MMC模型]] - 开关函数在MMC建模中的核心应用
- [[vsc-model|VSC模型]] - 两电平/三电平变流器开关函数
- [[average-value-model|平均值模型]] - 基于开关函数的平均化方法

### 6.2 相关方法
- [[state-space-method|状态空间法]] - 开关函数与状态空间结合
- [[dynamic-phasor|动态相量法]] - 频域开关函数方法
- [[numerical-integration|数值积分]] - 开关事件与离散时间积分
- [[thevenin-norton-equivalent|戴维南-诺顿等效]] - 开关函数与等效电路结合

### 6.3 相关主题
- [[real-time-simulation|实时仿真]] - 开关函数在实时仿真中的应用
- [[multirate-method|多速率方法]] - 开关频率与仿真步长协调
- [[vsc-hvdc|VSC-HVDC]] - 高压直流输电开关函数应用
- [[harmonic-analysis|谐波分析]] - 开关函数谐波特性

## 7. 适用边界与限制

### 7.1 适用条件
- **周期性开关**: 适用于PWM、方波调制等周期性开关策略
- **理想开关假设**: 忽略开关瞬态（开通/关断时间、死区时间）
- **已知调制策略**: 需要明确的调制波和载波信息

### 7.2 失效边界
- **非周期开关**: 随机开关、滞环控制等难以用固定开关函数描述
- **谐振型变换器**: 软开关、谐振开关动作复杂
- **宽频暂态**: 极高频率下寄生参数效应显著
- **故障工况**: 短路、闭锁等异常工况下开关函数失效

### 7.3 精度边界
| 应用场景 | 稳态误差 | 暂态误差 | 适用频段 |
|----------|---------|---------|----------|
| 详细开关模型 | <0.1% | <1% | DC-1MHz |
| 状态空间平均 | <1% | <5% | DC-10kHz |
| 广义状态空间平均 | <2% | <8% | DC-开关频率 |
| 平均值模型 | <5% | <15% | DC-基频 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| A review of efficient modeling methods for modular multilevel converters | 2015 | MMC开关函数建模综述，桥臂平均开关函数 |
| An accelerated detailed equivalent model for modular multilevel converters | 2023 | 结合开关函数与恒定导纳矩阵，30-60%加速 |
| 模块化多电平换流器时间尺度变换建模和仿真 | 2022 | 开关函数与时间尺度变换结合，206倍加速 |
| 适用于电磁暂态高效仿真的变流器分段广义状态空间平均模型 | 2019 | 分段广义状态空间平均，P-GSSA方法 |

## 相关模型

- [[mmc-model|MMC模型]] - 开关函数在MMC建模中的核心应用
- [[vsc-model|VSC模型]] - 两电平/三电平变流器开关函数建模
- [[average-value-model|平均值模型]] - 基于开关函数的平均化方法
- DC-DC变换器模型 - 开关函数在直流变换器中的应用
- 级联H桥模型 - 多电平变换器开关函数

## 相关主题

- [[real-time-simulation|实时仿真]] - 开关函数在实时仿真中的应用
- [[multirate-method|多速率方法]] - 开关频率与仿真步长协调
- [[vsc-hvdc|VSC-HVDC]] - 高压直流输电开关函数应用
- [[harmonic-analysis|谐波分析]] - 开关函数谐波特性分析

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*

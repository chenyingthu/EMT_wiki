---
title: "坐标变换 (Coordinate Transformation)"
type: model
tags: [coordinate-transformation, park, clarke, dq0, abc, synchronous-frame, rotating-frame]
created: "2026-04-30"
updated: "2026-05-11"
---

# 坐标变换 (Coordinate Transformation)



## 定义与概述

坐标变换是电力系统EMT仿真和控制系统设计中的数学工具，通过将三相交流量转换为旋转坐标系下的直流量，实现交流系统的解耦控制。Park变换和Clarke变换是最核心的变换方法，本模型涵盖abc/αβ/dq0之间的正变换与反变换、零序分量处理、以及不同参考坐标系的选择，适用于电机控制、换流器控制和电力系统分析的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 将时变交流量转换为时不变直流量
- 实现有功/无功解耦控制
- 简化控制器设计
- 便于稳态分析

**变换类型**:
| 变换 | 名称 | 输入 | 输出 | 特点 |
|------|------|------|------|------|
| Clarke | 静止变换 | abc | αβ0 | 三相→两相静止 |
| Park | 旋转变换 | αβ | dq | 静止→同步旋转 |
| 综合 | Clarke+Park | abc | dq0 | 三相→同步旋转 |
| 反变换 | Inverse | dq0 | abc | 旋转→三相 |

### 1.2 坐标系定义

**abc坐标系**:
```
        a轴
         │
         │
    c轴 ─┼─ b轴
```
三相轴彼此相差120°，固定在定子上。

**αβ坐标系（静止）**:
```
      β轴
       │
       │
 α轴 ──┴──
```
两相静止坐标系，α轴与a轴重合。

**dq坐标系（旋转）**:
```
      q轴
       │
       │  θ
 d轴 ──┴──
```
以角速度ω旋转，d轴与a轴夹角为θ=ωt。

### 1.3 运行激励

**输入信号**：
- 三相电压/电流：$v_a, v_b, v_c$
- 参考角度：$	heta = \omega t + \theta_0$
- 角频率：$	heta = \int \omega dt$

**输出信号**：
- 直流量：$v_d, v_q$（或 $i_d, i_q$）
- 零序分量：$v_0$（或 $i_0$）
- 静止分量：$v_\alpha, v_\beta$

**应用场景**：
- 锁相环（PLL）输出角度
- 电机转子位置
- 电网同步参考

## 2. 物理模型与数学描述

### 2.1 Clarke变换（静止变换）

#### 2.1.1 等幅值Clarke变换

**正变换（abc → αβ0）**:
$$\begin{bmatrix} v_\alpha \\ v_\beta \\ v_0 \end{bmatrix} =
\frac{2}{3} \begin{bmatrix}
1 & -\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}
\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

**标量形式**：
$$v_\alpha = \frac{2}{3}\left(v_a - \frac{v_b + v_c}{2}\right)$$
$$v_\beta = \frac{1}{\sqrt{3}}(v_b - v_c)$$
$$v_0 = \frac{1}{3}(v_a + v_b + v_c)$$

**反变换（αβ0 → abc）**:
$$\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix} =
\begin{bmatrix}
1 & 0 & 1 \\
-\frac{1}{2} & \frac{\sqrt{3}}{2} & 1 \\
-\frac{1}{2} & -\frac{\sqrt{3}}{2} & 1
\end{bmatrix}
\begin{bmatrix} v_\alpha \\ v_\beta \\ v_0 \end{bmatrix}$$

#### 2.1.2 等功率Clarke变换

**正变换**:
$$\begin{bmatrix} v_\alpha \\ v_\beta \\ v_0 \end{bmatrix} =
\sqrt{\frac{2}{3}} \begin{bmatrix}
1 & -\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{bmatrix}
\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

**特点**：
- 等幅值变换：峰值保持，功率不守恒（需系数修正）
- 等功率变换：功率守恒，幅值缩小$\sqrt{3/2}$倍

**功率计算（等幅值）**:
$$P = \frac{3}{2}(v_d i_d + v_q i_q)$$
$$Q = \frac{3}{2}(v_q i_d - v_d i_q)$$

### 2.2 Park变换（旋转变换）

#### 2.2.1 标准Park变换

**正变换（αβ → dq）**:
$$\begin{bmatrix} v_d \\ v_q \end{bmatrix} =
\begin{bmatrix}
\cos\theta & \sin\theta \\
-\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix} v_\alpha \\ v_\beta \end{bmatrix}$$

**标量形式**：
$$v_d = v_\alpha \cos\theta + v_\beta \sin\theta$$
$$v_q = -v_\alpha \sin\theta + v_\beta \cos\theta$$

**反变换（dq → αβ）**:
$$\begin{bmatrix} v_\alpha \\ v_\beta \end{bmatrix} =
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix} v_d \\ v_q \end{bmatrix}$$

#### 2.2.2 直接abc→dq0变换

**综合变换矩阵**:
$$\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix} =
\frac{2}{3} \begin{bmatrix}
\cos\theta & \cos(\theta-120°) & \cos(\theta+120°) \\
-\sin\theta & -\sin(\theta-120°) & -\sin(\theta+120°) \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}
\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

**展开形式**：
$$v_d = \frac{2}{3}\left[v_a \cos\theta + v_b \cos(\theta-120°) + v_c \cos(\theta+120°)\right]$$
$$v_q = -\frac{2}{3}\left[v_a \sin\theta + v_b \sin(\theta-120°) + v_c \sin(\theta+120°)\right]$$
$$v_0 = \frac{1}{3}(v_a + v_b + v_c)$$

**反变换**：
$$\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix} =
\begin{bmatrix}
\cos\theta & -\sin\theta & 1 \\
\cos(\theta-120°) & -\sin(\theta-120°) & 1 \\
\cos(\theta+120°) & -\sin(\theta+120°) & 1
\end{bmatrix}
\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix}$$

### 2.3 对称分量坐标系

**瞬时有功/无功功率**：
$$P = v_d i_d + v_q i_q$$
$$Q = v_q i_d - v_d i_q$$

**dq轴物理意义**（电压定向）：
- $v_d$：有功电压分量
- $v_q$：无功电压分量
- $i_d$：有功电流分量
- $i_q$：无功电流分量

**电流定向控制**：
- $i_d$：磁通电流（电机控制）
- $i_q$：转矩电流（电机控制）

### 2.4 参考坐标系选择

#### 2.4.1 电网电压定向（VOC）

**定向方式**：
- d轴与电网电压矢量重合
- $v_q = 0$
- $v_d = |\vec{v}|$

**功率表达式**：
$$P = v_d i_d$$
$$Q = -v_d i_q$$

**优点**：有功/无功解耦控制。

#### 2.4.2 定子磁链定向

**同步电机控制**：
- d轴与定子磁链重合
- $i_d$控制磁链
- $i_q$控制转矩

#### 2.4.3 转子磁链定向

**感应电机控制**：
- d轴与转子磁链重合
- 实现最大转矩电流比

## 3. EMT仿真模型

### 3.1 连续时间实现

**角度积分**:
$$\theta(t) = \int_0^t \omega(\tau) d\tau + \theta_0$$

或离散形式：
$$\theta[k] = \theta[k-1] + \omega[k] T_s$$

**三角函数计算**：
使用查找表（LUT）或CORDIC算法优化。

### 3.2 离散时间实现

**前向欧拉离散**:
$$\theta[k+1] = \theta[k] + \omega[k] T_s$$

**三角函数计算优化**：
```matlab
% 使用查找表
theta_idx = floor(theta * LUT_SIZE / (2*pi));
cos_val = cos_lut(theta_idx + 1);
sin_val = sin_lut(theta_idx + 1);

% 或线性插值
frac = theta * LUT_SIZE / (2*pi) - theta_idx;
cos_val = (1-frac) * cos_lut(theta_idx + 1) + frac * cos_lut(theta_idx + 2);
```

### 3.3 多相系统扩展

**n相Clarke变换**:
$$v_\alpha = \frac{2}{n}\sum_{k=0}^{n-1} v_k \cos\left(\frac{2\pi k}{n}\right)$$
$$v_\beta = \frac{2}{n}\sum_{k=0}^{n-1} v_k \sin\left(\frac{2\pi k}{n}\right)$$

**五相系统**:
$$v_{x1} = \frac{2}{5}\sum_{k=0}^{4} v_k \cos\left(\frac{4\pi k}{5}\right)$$
$$v_{y1} = \frac{2}{5}\sum_{k=0}^{4} v_k \sin\left(\frac{4\pi k}{5}\right)$$

### 3.4 数字实现考虑

**定点数实现**：
- 角度：Q15格式，0-2π映射到0-32767
- 三角函数：查表或CORDIC
- 乘法：防止溢出，保留足够精度

**量化误差**：
- 角度量化：决定三角函数精度
- 系数量化：变换矩阵元素精度

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**Clarke变换**:
```fortran
! Clarke变换
V_ALPHA = (2.0/3.0) * (VA - 0.5*VB - 0.5*VC)
V_BETA = (1.0/SQRT(3.0)) * (VB - VC)
V_ZERO = (VA + VB + VC) / 3.0
```

**Park变换**:
```fortran
! Park变换
! 计算三角函数
COS_THETA = COS(THETA)
SIN_THETA = SIN(THETA)

! 旋转变换
V_D = V_ALPHA * COS_THETA + V_BETA * SIN_THETA
V_Q = -V_ALPHA * SIN_THETA + V_BETA * COS_THETA

! 反变换
V_ALPHA_REF = V_D_REF * COS_THETA - V_Q_REF * SIN_THETA
V_BETA_REF = V_D_REF * SIN_THETA + V_Q_REF * COS_THETA
```

**综合abc→dq0**:
```fortran
! 直接abc到dq0
V_D = (2.0/3.0) * (VA*COS(THETA) 
     + VB*COS(THETA-2*PI/3) 
     + VC*COS(THETA+2*PI/3))
     
V_Q = -(2.0/3.0) * (VA*SIN(THETA) 
      + VB*SIN(THETA-2*PI/3) 
      + VC*SIN(THETA+2*PI/3))
      
V_ZERO = (VA + VB + VC) / 3.0
```

**反变换dq0→abc**:
```fortran
! 反变换
VA = V_D*COS(THETA) - V_Q*SIN(THETA) + V_ZERO
VB = V_D*COS(THETA-2*PI/3) - V_Q*SIN(THETA-2*PI/3) + V_ZERO
VC = V_D*COS(THETA+2*PI/3) - V_Q*SIN(THETA+2*PI/3) + V_ZERO
```

### 4.2 MATLAB/Simulink实现

**Simulink模块**:
```matlab
% 使用Simulink的Transformations库
% abc-to-dq0 Transform
% dq0-to-abc Transform
```

**自定义函数**:
```matlab
function [vd, vq, v0] = abc_to_dq0(va, vb, vc, theta)
    % Clarke变换
    valpha = (2/3) * (va - 0.5*vb - 0.5*vc);
    vbeta = (1/sqrt(3)) * (vb - vc);
    v0 = (va + vb + vc) / 3;
    
    % Park变换
    vd = valpha * cos(theta) + vbeta * sin(theta);
    vq = -valpha * sin(theta) + vbeta * cos(theta);
end

function [valpha, vbeta] = abc_to_alphabeta(va, vb, vc)
    valpha = (2/3) * (va - 0.5*vb - 0.5*vc);
    vbeta = (1/sqrt(3)) * (vb - vc);
end

function [vd, vq] = alphabeta_to_dq(valpha, vbeta, theta)
    vd = valpha * cos(theta) + vbeta * sin(theta);
    vq = -valpha * sin(theta) + vbeta * cos(theta);
end

function [va, vb, vc] = dq0_to_abc(vd, vq, v0, theta)
    va = vd*cos(theta) - vq*sin(theta) + v0;
    vb = vd*cos(theta-2*pi/3) - vq*sin(theta-2*pi/3) + v0;
    vc = vd*cos(theta+2*pi/3) - vq*sin(theta+2*pi/3) + v0;
end
```

**CORDIC算法实现**（FPGA优化）:
```matlab
function [cos_theta, sin_theta] = cordic(theta, iterations)
    % CORDIC算法计算三角函数
    % 适用于FPGA实现
    
    % 初始化
    x = 0.60725;  % 1/K缩放因子
    y = 0;
    z = theta;
    
    % 迭代
    for i = 0:iterations-1
        if z >= 0
            x_new = x - y/2^i;
            y_new = y + x/2^i;
            z = z - atan(1/2^i);
        else
            x_new = x + y/2^i;
            y_new = y - x/2^i;
            z = z + atan(1/2^i);
        end
        x = x_new;
        y = y_new;
    end
    
    cos_theta = x;
    sin_theta = y;
end
```

### 4.3 C代码实现

**实时坐标变换**:
```c
#include <math.h>

typedef struct {
    float va, vb, vc;
    float valpha, vbeta, vzero;
    float vd, vq;
    float theta;
} Transform_Data;

// Clarke变换
void clarke_transform(Transform_Data *data) {
    data->valpha = (2.0f/3.0f) * (data->va - 0.5f*data->vb - 0.5f*data->vc);
    data->vbeta = (1.0f/sqrtf(3.0f)) * (data->vb - data->vc);
    data->vzero = (data->va + data->vb + data->vc) / 3.0f;
}

// Park变换
void park_transform(Transform_Data *data) {
    float cos_theta = cosf(data->theta);
    float sin_theta = sinf(data->theta);
    
    data->vd = data->valpha * cos_theta + data->vbeta * sin_theta;
    data->vq = -data->valpha * sin_theta + data->vbeta * cos_theta;
}

// 反Park变换
void inv_park_transform(float vd, float vq, float theta, 
                        float *valpha, float *vbeta) {
    float cos_theta = cosf(theta);
    float sin_theta = sinf(theta);
    
    *valpha = vd * cos_theta - vq * sin_theta;
    *vbeta = vd * sin_theta + vq * cos_theta;
}

// 综合abc到dq0
void abc_to_dq0(float va, float vb, float vc, float theta,
                float *vd, float *vq, float *v0) {
    float valpha = (2.0f/3.0f) * (va - 0.5f*vb - 0.5f*vc);
    float vbeta = (1.0f/sqrtf(3.0f)) * (vb - vc);
    *v0 = (va + vb + vc) / 3.0f;
    
    float cos_theta = cosf(theta);
    float sin_theta = sinf(theta);
    
    *vd = valpha * cos_theta + vbeta * sin_theta;
    *vq = -valpha * sin_theta + vbeta * cos_theta;
}

// dq0到abc
void dq0_to_abc(float vd, float vq, float v0, float theta,
                float *va, float *vb, float *vc) {
    float cos_theta = cosf(theta);
    float sin_theta = sinf(theta);
    float cos_theta_120 = cosf(theta - 2*PI/3);
    float sin_theta_120 = sinf(theta - 2*PI/3);
    float cos_theta_240 = cosf(theta + 2*PI/3);
    float sin_theta_240 = sinf(theta + 2*PI/3);
    
    *va = vd * cos_theta - vq * sin_theta + v0;
    *vb = vd * cos_theta_120 - vq * sin_theta_120 + v0;
    *vc = vd * cos_theta_240 - vq * sin_theta_240 + v0;
}
```

## 5. 典型参数参考

### 5.1 角度表示

| 表示方式 | 范围 | 精度 | 应用 |
|----------|------|------|------|
| 弧度 | $0$ to $2\pi$ | 浮点 | 通用 |
| 角度 | $0°$ to $360°$ | 浮点 | 直观显示 |
| 定点Q15 | $0$ to $32767$ | 15bit | DSP/FPGA |
| 定点Q31 | $0$ to $2^{31}-1$ | 31bit | 高精度 |

### 5.2 坐标系特性

| 坐标系 | 变量类型 | 优势 | 劣势 |
|--------|----------|------|------|
| abc | 交流时变 | 物理直观 | 控制复杂 |
| αβ | 交流时变 | 降维 | 仍需处理交流 |
| dq | 直流恒定 | 解耦控制 | 需要角度信息 |

### 5.3 应用场景

| 应用 | 参考坐标系 | d轴定向 | q轴定向 |
|------|------------|---------|---------|
| 电网换流器 | 同步旋转 | 电网电压 | 超前90° |
| 永磁同步电机 | 转子旋转 | 转子磁链 | 超前90° |
| 感应电机 | 转子旋转 | 转子磁链 | 转矩分量 |
| 同步电机 | 转子旋转 | 转子d轴 | 转子q轴 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[pll-model|锁相环]] - 角度生成
- [[vsc-model|VSC模型]] - 换流器控制
- [[synchronous-machine-model|同步电机]] - 转子定向

### 6.2 相关方法
- [[state-space-method|状态空间法]] - 坐标系建模
- [[numerical-integration|数值积分]] - 角度积分

### 6.3 相关主题
- 矢量控制 - 基于dq0的控制策略
- 锁相环 - 角度同步
- 瞬时功率理论 - p-q理论

## 7. 适用边界与限制

### 7.1 适用条件
- **系统类型**：三相对称或不对称系统
- **频率范围**：基波频率稳定
- **角度精度**：足够分辨三角函数
- **计算资源**：支持三角函数或查表

### 7.2 模型限制
- **谐波影响**：dq变换对谐波呈现为交流量
- **不平衡系统**：需考虑零序分量
- **角度跳变**：2π处需特殊处理
- **数值精度**：三角函数计算误差

### 7.3 量化性能边界

坐标变换是精确的数学变换（在无限精度算术下无信息损失），其 EMT 仿真精度主要受限于数字实现中的数值精度和角度同步误差，而非变换本身的近似。因此不适用与传统物理模型相同的精度边界评估框架。数字实现中，64 位浮点三角函数运算可达到约 $10^{-15}$ 相对精度，32 位浮点约 $10^{-7}$，16 位定点约 $10^{-4}$，而角度同步误差（如 PLL 跟踪误差）通常是限制 dq 变换精度的主导因素。建议用户根据具体应用选择足够的数值精度，重点关注角度同步环节而非变换算法本身。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[new-multiphase-mode-domain-transmission-line-model|New multiphase mode domain transmission line model]] | 1999 |
| [[mode-domain-multiphase-transmission-line-model-use-in-transient-studies-power-de|Mode domain multiphase transmission line model - use in tran]] | 2004 |
| [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow|Multiprocessor based generator module for a real-time power ]] | 2004 |
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 |
| [[comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g|Comparative study on electromechanical and electromagnetic t]] | 2014 |
| [[a-steady-state-initialization-procedure-for-generic-voltage-source-converters-in|A steady-state initialization procedure for generic voltage-]] | 2023 |
| [[average-value-model-for-voltage-source-converters-with-direct-interfacing-in-emt|Average-Value Model for Voltage-Source Converters With Direc]] | 2023 |
| [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond|Modeling and application of DQ-sequence dynamic phasors unde]] | 2025 |

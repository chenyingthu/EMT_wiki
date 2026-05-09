---
title: "矢量控制 (Vector Control)"
type: model
tags: [vector-control, foc, dtc, field-oriented-control, motor-control, torque-control]
created: "2026-04-30"
---

# 矢量控制 (Vector Control)


```mermaid
graph TD
    subgraph Ncmp[矢量控制 (Vector Control)]
        N0[FOC: 磁场定向控制]
        N1[DTC: 直接转矩控制]
        N2[DFOC: 直接磁场定向]
        N3[IFOC: 间接磁场定向]
    end
```


## 定义与概述

矢量控制（Vector Control/Field Oriented Control, FOC）是交流电机高性能控制的核心方法，通过坐标变换将交流电机的定子电流分解为产生磁场的励磁分量和产生转矩的转矩分量，实现类似于直流电机的解耦控制。本模型涵盖感应电机和同步电机的矢量控制原理、电流环/速度环设计、直接转矩控制（DTC），适用于电机驱动系统EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 实现交流电机转矩快速响应
- 解耦磁通和转矩控制
- 宽范围调速控制
- 高效率运行

**矢量控制类型**:
| 类型 | 名称 | 特点 | 应用 |
|------|------|------|------|
| FOC | 磁场定向控制 | 电流解耦控制 | 永磁/感应电机 |
| DTC | 直接转矩控制 | 直接控制转矩 | 大功率驱动 |
| DFOC | 直接磁场定向 | 无需速度传感器 | 低成本应用 |
| IFOC | 间接磁场定向 | 基于电流模型 | 通用驱动 |

### 1.2 控制结构

**双闭环结构**:
```
  速度给定 ──→[速度环PI]──→ 电流给定 ──→[电流环PI]──→ 电压给定
                  ↑                              │
                  │                              ▼
              实际转速                        PWM输出
                  ↑                              │
                  └────────[电机]←───────────────┘
```

**三闭环结构**（位置控制）:
位置环 → 速度环 → 电流环

### 1.3 运行激励

**给定信号**：
- 速度给定：$\omega^*$ 或 $n^*$
- 转矩给定：$T_e^*$（转矩控制模式）
- 磁链给定：$\psi^*$（弱磁控制时变化）

**反馈信号**：
- 定子电流：$i_a, i_b, i_c$
- 转子位置：$\theta_r$（或速度$\omega_r$）
- 直流母线电压：$V_{dc}$

**输出信号**：
- 三相电压给定：$v_a^*, v_b^*, v_c^*$
- PWM占空比：$d_a, d_b, d_c$

## 2. 物理模型与数学描述

### 2.1 感应电机矢量控制

#### 2.1.1 转子磁场定向

**基本假设**：
- d轴与转子磁链矢量重合
- $\psi_{qr} = 0$，$\psi_{dr} = \psi_r$

**转矩方程**:
$$T_e = \frac{3}{2} \frac{p}{2} \frac{L_m}{L_r} \psi_{dr} i_{qs}$$

**磁链方程**:
$$\psi_{dr} = L_m i_{ds}$$

**转子电压方程**:
$$0 = R_r i_{dr} + \frac{d\psi_{dr}}{dt} - (\omega_e - \omega_r)\psi_{qr}$$
$$0 = R_r i_{qr} + \frac{d\psi_{qr}}{dt} + (\omega_e - \omega_r)\psi_{dr}$$

#### 2.1.2 电流解耦控制

**转差频率**:
$$\omega_{slip} = \omega_e - \omega_r = \frac{L_m}{\tau_r} \frac{i_{qs}^*}{\psi_{dr}^*}$$

其中 $\tau_r = L_r/R_r$ 为转子时间常数。

**电流指令**:
$$i_{ds}^* = \frac{\psi_r^*}{L_m}$$
$$i_{qs}^* = \frac{2}{3} \frac{2}{p} \frac{L_r}{L_m} \frac{T_e^*}{\psi_r^*}$$

**定子电压方程**（考虑解耦）:
$$v_{ds} = R_s i_{ds} + \sigma L_s \frac{di_{ds}}{dt} - \omega_e \sigma L_s i_{qs}$$
$$v_{qs} = R_s i_{qs} + \sigma L_s \frac{di_{qs}}{dt} + \omega_e \frac{L_m}{L_r} \psi_{dr} + \omega_e \sigma L_s i_{ds}$$

其中 $\sigma = 1 - L_m^2/(L_s L_r)$ 为漏磁系数。

#### 2.1.3 前馈解耦

**解耦项**:
$$v_{d,dec} = -\omega_e \sigma L_s i_{qs}$$
$$v_{q,dec} = \omega_e \frac{L_m}{L_r} \psi_{dr} + \omega_e \sigma L_s i_{ds}$$

**解耦控制结构**:
```
i_d* ──→[PI]──→⊕──→ v_d
               ↑+
               └── 解耦项 (-ω_e σL_s i_q)
               
i_q* ──→[PI]──→⊕──→ v_q
               ↑+
               └── 解耦项 (ω_e L_m/L_r ψ_r + ω_e σL_s i_d)
```

### 2.2 永磁同步电机矢量控制

#### 2.2.1 转子磁场定向

**d轴沿永磁体磁链方向**:
$$\lambda_f = \psi_{pm}$$

**转矩方程**:
$$T_e = \frac{3}{2} \frac{p}{2} [\lambda_f i_q + (L_d - L_q) i_d i_q]$$

**控制策略**:

**$i_d=0$控制（隐极电机，$L_d=L_q$）**:
$$T_e = \frac{3}{2} \frac{p}{2} \lambda_f i_q$$
$$i_d^* = 0$$
$$i_q^* = \frac{2}{3} \frac{2}{p} \frac{T_e^*}{\lambda_f}$$

**最大转矩电流比（MTPA，凸极电机）**:
$$i_d^* = \frac{\lambda_f}{2(L_q - L_d)} - \sqrt{\frac{\lambda_f^2}{4(L_q - L_d)^2} + i_q^{*2}}$$

**弱磁控制（高速区）**:
$$i_d^* = \frac{\lambda_f - \sqrt{\lambda_f^2 + 4(L_q - L_d)^2 (I_{max}^2 - i_q^{*2})}}{2(L_d - L_q)}$$

#### 2.2.2 电流环设计

**d轴电流环**:
$$v_d = R_s i_d + L_d \frac{di_d}{dt} - \omega_e L_q i_q$$

**q轴电流环**:
$$v_q = R_s i_q + L_q \frac{di_q}{dt} + \omega_e L_d i_d + \omega_e \lambda_f$$

**PI参数整定**（模量最优）:
$$K_p = \frac{L}{2\tau_{des}}$$
$$K_i = \frac{R}{2\tau_{des}}$$

其中 $\tau_{des}$ 为期望时间常数（通常0.5-2ms）。

### 2.3 直接转矩控制（DTC）

#### 2.3.1 基本原理

**直接控制量**：
- 定子磁链：$\psi_s$
- 电磁转矩：$T_e$

**磁链估算**:
$$\vec{\psi}_s = \int (\vec{v}_s - R_s \vec{i}_s) dt$$

**转矩估算**:
$$T_e = \frac{3}{2} \frac{p}{2} (\psi_\alpha i_\beta - \psi_\beta i_\alpha)$$

#### 2.3.2 开关表

**磁链和转矩滞环控制**:

| H_ψ | H_T | S_a | S_b | S_c | 说明 |
|-----|-----|-----|-----|-----|------|
| 1 | 1 | 1 | 0 | 0 | 增磁链，增转矩 |
| 1 | -1 | 0 | 1 | 1 | 增磁链，减转矩 |
| -1 | 1 | 0 | 1 | 0 | 减磁链，增转矩 |
| -1 | -1 | 1 | 0 | 1 | 减磁链，减转矩 |

#### 2.3.3 扇区判断

**定子磁链角度**:
$$\theta_s = \arctan\left(\frac{\psi_\beta}{\psi_\alpha}\right)$$

**扇区划分**: 将空间分为6个60°扇区。

## 3. EMT仿真模型

### 3.1 电流环模型

#### 3.1.1 离散PI实现

**d轴电流环**:
```
e_d = i_d* - i_d
v_d_unsat = K_p_d * e_d + x_i_d - ω_e * L_q * i_q
x_i_d = x_i_d + K_i_d * T_s * e_d + K_aw * (v_d_sat - v_d_unsat)
```

**q轴电流环**:
```
e_q = i_q* - i_q
v_q_unsat = K_p_q * e_q + x_i_q + ω_e * (L_d * i_d + λ_f)
x_i_q = x_i_q + K_i_q * T_s * e_q + K_aw * (v_q_sat - v_q_unsat)
```

#### 3.1.2 电流指令生成

**MTPA查表**:
```matlab
% 预计算MTPA曲线
T_range = 0:T_max/1000:T_max;
for k = 1:length(T_range)
    Te = T_range(k);
    % 解MTPA方程
    iq_mtp(k) = fzero(@(iq) mtpa_equation(iq, Te, lambda_f, Ld, Lq), sqrt(Te));
    id_mtp(k) = mtpa_id(iq_mtp(k), lambda_f, Ld, Lq);
end
% 生成查表
MTPA_Table = griddedInterpolant(T_range, [id_mtp; iq_mtp]);
```

### 3.2 速度环模型

**速度PI控制**:
$$e_\omega = \omega^* - \omega$$
$$T_e^* = K_{p\omega} e_\omega + K_{i\omega} \int e_\omega dt$$

**转矩限幅**:
$$|T_e^*| \leq T_{max} = \min(T_{rated}, T_{flux}, T_{current})$$

**速度观测器**（无传感器）:
**滑模观测器**:
$$\frac{d\hat{i}_\alpha}{dt} = \frac{v_\alpha - R_s \hat{i}_\alpha - z_\alpha}{L_s}$$
$$\frac{d\hat{i}_\beta}{dt} = \frac{v_\beta - R_s \hat{i}_\beta - z_\beta}{L_s}$$

其中 $z_\alpha, z_\beta$ 为滑模控制项。

### 3.3 弱磁控制

**电压约束**:
$$v_d^2 + v_q^2 \leq V_{max}^2 = \left(\frac{V_{dc}}{\sqrt{3}}\right)^2$$

**弱磁启动判断**:
$$\sqrt{v_d^2 + v_q^2} > V_{max} - V_{margin}$$

**弱磁控制策略**:
- **方法一**：负向d轴电流指令
- **方法二**：电压闭环调节磁链给定
- **方法三**：MTPV（最大转矩电压比）轨迹

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**电流环控制**:
```fortran
! dq轴电流PI控制
! d轴
ERROR_ID = ID_REF - ID
VD_UNSAT = KP_D * ERROR_ID + INTEGRAL_D - WE * LQ * IQ

! 积分（带抗饱和）
IF (VD_UNSAT .LE. VD_MAX .AND. VD_UNSAT .GE. VD_MIN) THEN
  INTEGRAL_D = INTEGRAL_D + KI_D * DT * ERROR_ID
END IF

! 饱和限制
VD = MAX(MIN(VD_UNSAT, VD_MAX), VD_MIN)

! q轴
ERROR_IQ = IQ_REF - IQ
VQ_UNSAT = KP_Q * ERROR_IQ + INTEGRAL_Q + WE * (LD * ID + LAMBDA_F)

IF (VQ_UNSAT .LE. VQ_MAX .AND. VQ_UNSAT .GE. VQ_MIN) THEN
  INTEGRAL_Q = INTEGRAL_Q + KI_Q * DT * ERROR_IQ
END IF

VQ = MAX(MIN(VQ_UNSAT, VQ_MAX), VQ_MIN)

! 反Park变换
VALPHA = VD * COS(THETA_E) - VQ * SIN(THETA_E)
VBETA = VD * SIN(THETA_E) + VQ * COS(THETA_E)

VA = VALPHA + V0
VB = -0.5*VALPHA + SQRT(3)/2*VBETA + V0
VC = -0.5*VALPHA - SQRT(3)/2*VBETA + V0
```

**速度环控制**:
```fortran
! 速度PI控制
ERROR_W = W_REF - W_MECH
TORQUE_REF = KP_W * ERROR_W + INTEGRAL_W

! 积分（带限幅）
IF (TORQUE_REF .LE. T_MAX .AND. TORQUE_REF .GE. -T_MAX) THEN
  INTEGRAL_W = INTEGRAL_W + KI_W * DT * ERROR_W
END IF

! 限幅
TORQUE_REF = MAX(MIN(TORQUE_REF, T_MAX), -T_MAX)

! 生成电流指令（i_d=0控制）
ID_REF = 0.0
IQ_REF = TORQUE_REF / (1.5 * P * LAMBDA_F / 2)
```

**DTC实现**:
```fortran
! 磁链估算
PSI_ALPHA = INTEGRAL(V_ALPHA - RS * I_ALPHA)
PSI_BETA = INTEGRAL(V_BETA - RS * I_BETA)

! 转矩估算
TE = 1.5 * (P/2) * (PSI_ALPHA * I_BETA - PSI_BETA * I_ALPHA)

! 磁链幅值
PSI_S = SQRT(PSI_ALPHA**2 + PSI_BETA**2)

! 扇区判断
THETA_S = ATAN2(PSI_BETA, PSI_ALPHA)
SECTOR = INT((THETA_S + PI) / (PI/3)) + 1

! 滞环比较
H_PSI = SIGN(1.0, PSI_REF - PSI_S)
H_TE = SIGN(1.0, TE_REF - TE)

! 查开关表选择电压矢量
CALL SWITCHING_TABLE(H_PSI, H_TE, SECTOR, SA, SB, SC)
```

### 4.2 MATLAB/Simulink实现

**FOC控制器**:
```matlab
function [vd, vq, id_ref, iq_ref] = foc_controller(omega_ref, omega, id, iq, theta_e, params)
    % 速度环
    e_omega = omega_ref - omega;
    torque_ref = params.Kp_w * e_omega + params.integral_w;
    torque_ref = max(min(torque_ref, params.T_max), -params.T_max);
    params.integral_w = params.integral_w + params.Ki_w * params.Ts * e_omega;
    
    % 电流指令（MTPA）
    [id_ref, iq_ref] = mtpa_lookup(torque_ref, params.MTPA_table);
    
    % d轴电流环
    e_id = id_ref - id;
    vd_unsat = params.Kp_d * e_id + params.integral_d - params.we * params.Lq * iq;
    params.integral_d = params.integral_d + params.Ki_d * params.Ts * e_id;
    vd = max(min(vd_unsat, params.V_max), -params.V_max);
    
    % q轴电流环
    e_iq = iq_ref - iq;
    vq_unsat = params.Kp_q * e_iq + params.integral_q + ...
              params.we * (params.Ld * id + params.lambda_f);
    params.integral_q = params.integral_q + params.Ki_q * params.Ts * e_iq;
    vq = max(min(vq_unsat, params.V_max), -params.V_max);
end

function [id, iq] = mtpa_lookup(Te, table)
    % 查表获取MTPA电流指令
    id = table.id(Te);
    iq = table.iq(Te);
end
```

### 4.3 C代码实现

**实时FOC算法**:
```c
typedef struct {
    float Kp_d, Ki_d, integral_d;
    float Kp_q, Ki_q, integral_q;
    float Kp_w, Ki_w, integral_w;
    float Ld, Lq, Ls, Rs, lambda_f;
    float V_max, I_max, T_max;
    float Ts;
} FOC_Params;

void foc_update(FOC_Params *params, float omega_ref, float omega, 
                float id, float iq, float theta_e, float *vd, float *vq) {
    float e_omega, torque_ref;
    float e_id, e_iq;
    float vd_unsat, vq_unsat;
    
    // 速度环
    e_omega = omega_ref - omega;
    torque_ref = params->Kp_w * e_omega + params->integral_w;
    
    // 转矩限幅
    if (torque_ref > params->T_max) torque_ref = params->T_max;
    if (torque_ref < -params->T_max) torque_ref = -params->T_max;
    
    // 积分更新
    params->integral_w += params->Ki_w * params->Ts * e_omega;
    
    // 电流指令（i_d=0控制）
    float id_ref = 0.0f;
    float iq_ref = torque_ref / (1.5f * params->lambda_f);
    
    // 电流限幅
    float i_max = sqrtf(params->I_max*params->I_max - id_ref*id_ref);
    if (iq_ref > i_max) iq_ref = i_max;
    if (iq_ref < -i_max) iq_ref = -i_max;
    
    // d轴电流环
    e_id = id_ref - id;
    float we = omega * params->lambda_f; // 电角速度
    vd_unsat = params->Kp_d * e_id + params->integral_d - we * params->Lq * iq;
    params->integral_d += params->Ki_d * params->Ts * e_id;
    
    // q轴电流环
    e_iq = iq_ref - iq;
    vq_unsat = params->Kp_q * e_iq + params->integral_q + 
               we * (params->Ld * id + params->lambda_f);
    params->integral_q += params->Ki_q * params->Ts * e_iq;
    
    // 电压限幅
    float v_max = params->V_max;
    *vd = (vd_unsat > v_max) ? v_max : (vd_unsat < -v_max) ? -v_max : vd_unsat;
    *vq = (vq_unsat > v_max) ? v_max : (vq_unsat < -v_max) ? -v_max : vq_unsat;
}
```

## 5. 典型参数参考

### 5.1 PMSM电流环参数

| 电机类型 | $K_{p,d}$ | $K_{i,d}$ | $K_{p,q}$ | $K_{i,q}$ | 带宽 |
|----------|-----------|-----------|-----------|-----------|------|
| 小功率(<1kW) | 5-20 | 500-2000 | 5-20 | 500-2000 | 500-2000Hz |
| 中功率(1-10kW) | 2-10 | 200-1000 | 2-10 | 200-1000 | 300-1000Hz |
| 大功率(>10kW) | 1-5 | 100-500 | 1-5 | 100-500 | 200-500Hz |

### 5.2 感应电机电流环参数

| 功率等级 | $K_{p,d}$ | $K_{i,d}$ | $K_{p,q}$ | $K_{i,q}$ | $\tau_r$ |
|----------|-----------|-----------|-----------|-----------|----------|
| <1kW | 5-15 | 300-1000 | 5-15 | 300-1000 | 50-100ms |
| 1-10kW | 2-8 | 150-500 | 2-8 | 150-500 | 100-200ms |
| >10kW | 1-5 | 80-300 | 1-5 | 80-300 | 200-500ms |

### 5.3 速度环参数

| 应用 | $K_{p,\omega}$ | $K_{i,\omega}$ | 带宽 |
|------|----------------|----------------|------|
| 伺服控制 | 0.5-2 | 5-20 | 50-200Hz |
| 传动控制 | 0.1-0.5 | 1-5 | 10-50Hz |
| 风机/泵 | 0.05-0.2 | 0.5-2 | 1-10Hz |

## 6. 相关主题与链接

### 6.1 相关模型
- [[pmsm-model|PMSM模型]] - 永磁同步电机
- [[induction-machine-model|感应电机]] - 异步电机
- [[pi-controller-model|PI控制器]] - 电流环/速度环

### 6.2 相关方法
- [[coordinate-transformation-model|坐标变换]] - abc/dq0变换
- [[pll-model|锁相环]] - 角度同步

### 6.3 相关主题
- DTC直接转矩控制 - 替代控制策略
- 弱磁控制 - 高速区运行
- 无传感器控制 - 速度观测器

## 7. 适用边界与限制

### 7.1 适用条件
- **电机类型**：PMSM、感应电机、同步磁阻电机
- **速度范围**：基速以下恒转矩，基速以上恒功率
- **电流限制**：不超过额定电流
- **电压限制**：不超过逆变器容量

### 7.2 模型限制
- **参数敏感性**：依赖准确的电机参数
- **饱和效应**：磁路饱和未完全建模
- **交叉耦合**：高动态时耦合效应增强
- **逆变器非线性**：死区、压降影响
- **参数变化**：温升、老化导致参数漂移

### 7.3 精度边界
| 控制方式 | 转矩响应 | 速度精度 | 适用场景 |
|---------|----------|----------|----------|
| $i_d=0$ | 2-5ms | ±0.1% | 隐极PMSM |
| MTPA | 2-5ms | ±0.1% | 凸极PMSM |
| DTC | 0.1-0.5ms | ±0.5% | 大功率 |
| 无传感器 | 5-10ms | ±0.5% | 低成本 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Vector control of AC machines | 2012 | 交流电机矢量控制综述 |
| Comparison of FOC and DTC for induction motor drives | 2015 | FOC与DTC比较 |
| MTPA control of PMSM for electric vehicle applications | 2019 | 电动汽车PMSM MTPA控制 |

## 相关方法
- [[numerical-integration|数值积分]] - 电流环离散化
- [[state-space-method|状态空间法]] - 电机状态方程
- [[coordinate-transformation-model|坐标变换模型]] - abc/dq0变换

## 相关模型
- [[pmsm-model|PMSM模型]] - 永磁同步电机
- [[induction-machine-model|感应电机]] - 异步电机
- [[pi-controller-model|PI控制器]] - 电流环/速度环
- [[pll-model|锁相环]] - 角度同步

## 相关主题
- DTC直接转矩控制 - 替代控制策略
- 弱磁控制 - 高速区运行
- 无传感器控制 - 速度观测器
- [[real-time-simulation|实时仿真]] - 矢量控制实时实现

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

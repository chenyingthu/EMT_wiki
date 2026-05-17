---
title: "下垂控制 (Droop Control)"
type: model
tags: [droop-control, primary-control, frequency-control, voltage-control, microgrid, distributed-generation]
created: "2026-04-30"
updated: "2026-05-18"
---

# 下垂控制 (Droop Control)

## 定义与概述

下垂控制是分布式电源并联运行和微电网控制的核心理论，通过模拟同步发电机的下垂特性，实现多台变换器或发电机之间的功率均分，无需高速通信。本模型涵盖P-f和Q-V下垂控制、虚拟同步机（VSM）增强下垂、多机并联稳定性分析，适用于微电网、MTDC电网和分布式发电系统的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 实现多电源并联功率均分
- 提供一次频率/电压调节
- 无通信依赖的分散控制
- 增强系统惯性和阻尼

**下垂控制类型**:
| 类型 | 控制量 | 适用场景 | 特点 |
|------|--------|----------|------|
| P-f下垂 | 有功-频率 | 交流微电网 | 传统发电机特性 |
| Q-V下垂 | 无功-电压 | 交流微电网 | 电压调节 |
| P-V下垂 | 有功-电压 | 直流微电网 | MTDC电压控制 |
| VSM | 虚拟同步机 | 低惯量系统 | 增加虚拟惯性 |
| 自适应下垂 | 动态调整 | 变化工况 | 改善均流 |

### 1.2 控制原理

**同步发电机下垂特性**:
```
  f
  │
f_max ────┬────────
          │  斜率 = -kf
          │  ╱
f_nom ────┼─/──────
          │/
f_min ────┴────────
          P_min   P_max
          └──→ P
```

**基本下垂方程**:
$$f = f_{nom} - k_p (P - P_{nom})$$
$$V = V_{nom} - k_q (Q - Q_{nom})$$

其中：
- $k_p$：有功下垂系数（Hz/W 或 Hz/kW）
- $k_q$：无功下垂系数（V/var 或 V/kvar）

### 1.3 运行激励

**输入信号**：
- 本地测量功率：P, Q
- 参考值：$f_{nom}, V_{nom}, P_{nom}, Q_{nom}$
- 下垂系数：$k_p, k_q$

**输出信号**：
- 频率给定：$f^*$
- 电压幅值给定：$V^*$
- 角度给定：$\theta^*$（通过积分）

**并联系统**：
- 系统频率：由所有单元共同决定
- 功率分配：与下垂系数成反比

## 2. 物理模型与数学描述

### 2.1 传统下垂控制

#### 2.1.1 P-f下垂

**频率给定**:
$$f^* = f_{nom} - k_p (P - P_{nom})$$

**角度积分**:
$$\theta^* = 2\pi \int f^* dt$$

**下垂系数设计**:
$$k_p = \frac{\Delta f_{max}}{P_{rated}}$$

其中 $\Delta f_{max}$ 为最大频率偏差（通常±0.5Hz）。

**多机并联功率分配**:
$$P_i : P_j = \frac{1}{k_{p,i}} : \frac{1}{k_{p,j}}$$

#### 2.1.2 Q-V下垂

**电压给定**:
$$V^* = V_{nom} - k_q (Q - Q_{nom})$$

**下垂系数设计**:
$$k_q = \frac{\Delta V_{max}}{Q_{rated}}$$

其中 $\Delta V_{max}$ 为最大电压偏差（通常±5%）。

#### 2.1.3 综合下垂控制

**dq坐标系下的实现**:
```
P, Q ──→[下垂控制]──→ f*, V*
                    │
                    ▼
               θ* = ∫f*dt
                    │
                    ▼
              [电压环]──→ v_d*, v_q*
```

**功率计算**:
$$P = v_d i_d + v_q i_q$$
$$Q = v_q i_d - v_d i_q$$

### 2.2 直流下垂控制

#### 2.2.1 P-V下垂

**电压给定**:
$$V_{dc}^* = V_{dc,nom} - k_{dc} (P - P_{nom})$$

**MTDC应用**:
$$V_{dc,i} = V_{dc}^* - k_{dc,i} P_i$$

**功率分配**:
$$P_i = -\frac{V_{dc,i} - V_{dc}^*}{k_{dc,i}}$$

#### 2.2.2 直流电网稳态

**n端系统**:
$$\sum_{i=1}^{n} P_i = -P_{loss}$$

求解公共直流电压：
$$V_{dc} = \frac{\sum V_{dc,i}^*/k_{dc,i}}{\sum 1/k_{dc,i}}$$

### 2.3 虚拟同步机（VSM）

#### 2.3.1 二阶转子方程

**摆动方程**:
$$J \frac{d\omega}{dt} = T_m - T_e - D(\omega - \omega_{nom})$$

或：
$$J \frac{d\omega}{dt} = \frac{P_{ref} - P}{\omega} - D(\omega - \omega_{nom})$$

其中：
- $J$：虚拟转动惯量（kg·m²）
- $D$：阻尼系数（N·m·s/rad）
- $P_{ref}$：功率参考

**标幺化形式**:
$$2H \frac{d\omega}{dt} = P_{ref} - P - D_p (\omega - \omega_{nom})$$

其中 $H$ 为惯性时间常数（s）。

#### 2.3.2 VSM控制结构

```
Pref ──→⊕──→[1/(2Hs)]──→ ω ──→∫──→ θ
        ↑-                    │
        │                     ▼
        └────[Dp]←───────────┘
                    
Qref ──→⊕──→[1/Dq]──→ V*
        ↑-
        └─────[Q]
```

**有功环**（转子方程）:
$$\omega = \omega_{nom} + \frac{1}{2Hs}(P_{ref} - P) - \frac{D_p}{2H}(\omega - \omega_{nom})$$

**无功环**（一阶）:
$$V^* = V_{nom} + \frac{1}{D_q}(Q_{ref} - Q)$$

### 2.4 自适应下垂控制

#### 2.4.1 一致性控制

**动态下垂系数**:
$$k_p = k_{p0} + \Delta k_p$$

**功率分配误差反馈**:
$$\frac{d\Delta k_p}{dt} = -\alpha (P_i - P_{avg})$$

#### 2.4.2 线路阻抗补偿

**考虑线路压降**:
$$V^* = V_{nom} - k_q Q - I \cdot Z_{line}$$

**虚拟阻抗**:
$$v_d^* = V_{nom} - R_v i_d + \omega L_v i_q$$
$$v_q^* = -R_v i_q - \omega L_v i_d$$

## 3. EMT仿真模型

### 3.1 传统下垂离散化

**频率计算**:
$$f[k] = f_{nom} - k_p (P[k] - P_{nom})$$

**角度积分**:
$$\theta[k+1] = \theta[k] + 2\pi f[k] T_s$$

**功率滤波**（避免高频噪声）:
$$P_{f}[k] = (1-\alpha) P_{f}[k-1] + \alpha P[k]$$

其中 $\alpha = \omega_c T_s / (1 + \omega_c T_s)$，$\omega_c$ 为截止频率。

### 3.2 VSM离散化

**角速度更新**:
$$\omega[k+1] = \omega[k] + \frac{T_s}{2H}[P_{ref} - P[k] - D_p(\omega[k] - \omega_{nom})]$$

**角度更新**:
$$\theta[k+1] = \theta[k] + \omega[k+1] T_s$$

### 3.3 多机并联模型

**n台并联系统**:
$$\begin{bmatrix} f \\ V \end{bmatrix} =
\begin{bmatrix} f_{nom} \\ V_{nom} \end{bmatrix} -
\begin{bmatrix}
k_{p,1} & & \\
& \ddots & \\
& & k_{p,n}
\end{bmatrix}
\begin{bmatrix} P_1 - P_{nom,1} \\ \vdots \\ P_n - P_{nom,n} \end{bmatrix}$$

**系统频率**:
$$f_{sys} = \frac{\sum (f_{nom,i}/k_{p,i}) - \sum (P_{nom,i}/k_{p,i}) + P_{load}}{\sum (1/k_{p,i})}$$

### 3.4 小信号模型

**单台VSM小信号**:
$$\Delta \dot{\omega} = -\frac{D_p}{2H} \Delta \omega - \frac{1}{2H} \Delta P$$
$$\Delta \dot{\theta} = \Delta \omega$$

**多机系统**:
$$\begin{bmatrix} \Delta \dot{\omega}_1 \\ \Delta \dot{\omega}_2 \end{bmatrix} =
\begin{bmatrix} -\frac{D_1}{2H_1} & 0 \\ 0 & -\frac{D_2}{2H_2} \end{bmatrix}
\begin{bmatrix} \Delta \omega_1 \\ \Delta \omega_2 \end{bmatrix} -
\begin{bmatrix} \frac{1}{2H_1} & 0 \\ 0 & \frac{1}{2H_2} \end{bmatrix}
\begin{bmatrix} \Delta P_1 \\ \Delta P_2 \end{bmatrix}$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**传统下垂控制**:
```fortran
! 下垂控制
! 功率计算（滤波后）
P_MEAS = V_D * I_D + V_Q * I_Q
P_FILT = (1-ALPHA) * P_FILT_OLD + ALPHA * P_MEAS

! 频率给定
F_REF = F_NOM - KP * (P_FILT - P_NOM)

! 角度积分
THETA = THETA + 2*PI*F_REF*DT

! 限制角度范围
IF (THETA > 2*PI) THETA = THETA - 2*PI
IF (THETA < 0) THETA = THETA + 2*PI

! 无功下垂
Q_MEAS = V_Q * I_D - V_D * I_Q
Q_FILT = (1-ALPHA) * Q_FILT_OLD + ALPHA * Q_MEAS

V_REF = V_NOM - KQ * (Q_FILT - Q_NOM)

! 电压环（可选）
V_D_REF = V_REF
V_Q_REF = 0.0
```

**虚拟同步机**:
```fortran
! VSM实现
! 功率滤波
P_FILT = (1-ALPHA) * P_FILT_OLD + ALPHA * P_MEAS

! 转子方程（角速度更新）
DWDT = (P_REF - P_FILT - DP * (OMEGA - OMEGA_NOM)) / (2*H)
OMEGA = OMEGA + DWDT * DT

! 角度积分
THETA = THETA + OMEGA * DT

! 限制
IF (THETA > 2*PI) THETA = THETA - 2*PI

! 无功控制（一阶）
V_REF = V_NOM + (Q_REF - Q_FILT) / DQ

! 电压限幅
V_REF = MAX(MIN(V_REF, V_MAX), V_MIN)
```

### 4.2 MATLAB/Simulink实现

**传统下垂控制**:
```matlab
function [theta_ref, v_ref] = droop_control(p_meas, q_meas, params)
    % 功率滤波
    persistent p_filt q_filt theta
    if isempty(p_filt)
        p_filt = 0; q_filt = 0; theta = 0;
    end
    
    alpha = params.wc * params.Ts / (1 + params.wc * params.Ts);
    p_filt = (1-alpha) * p_filt + alpha * p_meas;
    q_filt = (1-alpha) * q_filt + alpha * q_meas;
    
    % 下垂方程
    f_ref = params.f_nom - params.kp * (p_filt - params.p_nom);
    v_ref = params.v_nom - params.kq * (q_filt - params.q_nom);
    
    % 角度积分
    theta = theta + 2*pi*f_ref*params.Ts;
    theta = mod(theta, 2*pi);
    theta_ref = theta;
end
```

**虚拟同步机**:
```matlab
function [theta, omega, v_ref] = vsm_control(p_meas, q_meas, p_ref, q_ref, params)
    % 状态变量
    persistent omega_int theta_int
    if isempty(omega_int)
        omega_int = params.omega_nom;
        theta_int = 0;
    end
    
    % 功率滤波
    alpha = params.wc * params.Ts / (1 + params.wc * params.Ts);
    p_filt = (1-alpha)*p_filt + alpha*p_meas;
    
    % 转子方程（角速度）
    domega = (p_ref - p_filt - params.Dp*(omega_int - params.omega_nom)) / (2*params.H);
    omega_int = omega_int + domega * params.Ts;
    
    % 角度积分
    theta_int = theta_int + omega_int * params.Ts;
    theta_int = mod(theta_int, 2*pi);
    
    % 无功控制
    v_ref = params.v_nom + (q_ref - q_filt) / params.Dq;
    
    theta = theta_int;
    omega = omega_int;
end
```

**多机并联仿真**:
```matlab
function f_sys = parallel_droop(n_machines, p_load, params)
    % 计算系统频率
    sum_fk = sum(params.f_nom ./ params.kp);
    sum_pk = sum(params.p_nom ./ params.kp);
    sum_inv_kp = sum(1./params.kp);
    
    f_sys = (sum_fk - sum_pk + p_load) / sum_inv_kp;
    
    % 各机功率
    for i = 1:n_machines
        p_i(i) = (params.f_nom(i) - f_sys) / params.kp(i) + params.p_nom(i);
    end
end
```

### 4.3 C代码实现

**下垂控制器**:
```c
typedef struct {
    float f_nom, v_nom;
    float p_nom, q_nom;
    float kp, kq;
    float wc;  // 滤波截止频率
    float Ts;
    
    // 状态变量
    float p_filt, q_filt;
    float theta;
} Droop_Controller;

void droop_init(Droop_Controller *ctrl, float f_nom, float v_nom, 
                float kp, float kq, float wc, float Ts) {
    ctrl->f_nom = f_nom;
    ctrl->v_nom = v_nom;
    ctrl->kp = kp;
    ctrl->kq = kq;
    ctrl->wc = wc;
    ctrl->Ts = Ts;
    ctrl->p_filt = 0;
    ctrl->q_filt = 0;
    ctrl->theta = 0;
}

void droop_update(Droop_Controller *ctrl, float p_meas, float q_meas,
                  float *f_ref, float *v_ref, float *theta_ref) {
    // 功率滤波
    float alpha = ctrl->wc * ctrl->Ts / (1.0f + ctrl->wc * ctrl->Ts);
    ctrl->p_filt = (1.0f - alpha) * ctrl->p_filt + alpha * p_meas;
    ctrl->q_filt = (1.0f - alpha) * ctrl->q_filt + alpha * q_meas;
    
    // 下垂方程
    *f_ref = ctrl->f_nom - ctrl->kp * (ctrl->p_filt - ctrl->p_nom);
    *v_ref = ctrl->v_nom - ctrl->kq * (ctrl->q_filt - ctrl->q_nom);
    
    // 角度积分
    ctrl->theta += 2.0f * PI * (*f_ref) * ctrl->Ts;
    
    // 角度限幅 [0, 2π]
    while (ctrl->theta >= 2.0f * PI) ctrl->theta -= 2.0f * PI;
    while (ctrl->theta < 0) ctrl->theta += 2.0f * PI;
    
    *theta_ref = ctrl->theta;
}
```

## 5. 典型参数参考

### 5.1 交流下垂系数

| 应用 | $k_p$ (Hz/kW) | $k_q$ (V/kvar) | 频率范围 | 电压范围 |
|------|---------------|----------------|----------|----------|
| 微电网 | 0.1-1.0 | 0.01-0.1 | ±0.5Hz | ±5% |
| 储能系统 | 0.5-2.0 | 0.05-0.2 | ±1.0Hz | ±10% |
| 柴油发电机 | 0.05-0.2 | 0.005-0.02 | ±0.2Hz | ±2% |

### 5.2 VSM参数

| 参数 | 符号 | 典型值 | 说明 |
|------|------|--------|------|
| 惯性常数 | H | 0.5-5s | 虚拟惯性 |
| 阻尼系数 | Dp | 20-200 | p.u. |
| 无功阻尼 | Dq | 0.1-1.0 | p.u. |
| 功率滤波 | wc | 10-50 rad/s | 截止频率 |

### 5.3 直流下垂系数

| 电压等级 | $k_{dc}$ (V/kW) | 电压范围 |
|----------|-----------------|----------|
| 380V | 0.1-1.0 | ±5% |
| 750V | 0.5-5.0 | ±5% |
| 1500V | 2-20 | ±5% |
| ±500kV | 1-10k | ±5% |

### 5.4 下垂系数设计公式

**有功下垂**:
$$k_p = \frac{\Delta f_{max}}{P_{rated}}$$

**无功下垂**:
$$k_q = \frac{\Delta V_{max}}{Q_{rated}}$$

**惯量设计**:
$$H = \frac{E_{kin}}{S_{rated}}$$

其中 $E_{kin}$ 为期望的虚拟动能。

## 6. 关键技术挑战

### 6.1 PQ能力边界约束与下垂指令的冲突

当下垂环根据 $P$、$Q$ 偏差计算出参考点超出 RIC（额定电流约束）与 PWM 饱和约束交集时，内环限幅激活导致外环下垂指令被覆盖，GFM 暂态行为偏离下垂预期。EVR（增强型电压调节）策略通过优先保留电压支撑能力部分缓解此问题，但无法完全消除约束冲突。

### 6.2 虚拟阻抗设计与电压降落的矛盾

虚拟阻抗增大可改善功率共享精度，但同时引入更大电压降落，在弱网场景中可能导致 PCC 电压进一步跌落。设计时需在共享精度和电压维持之间做权衡。

### 6.3 时间尺度分离被破坏导致环路交互失稳

下垂环带宽必须远低于电压环和电流环带宽。若下垂系数 $k_p$ 过大，频率对有功偏差的响应速度与内环带宽重叠，引起环路交互振荡。

### 6.4 多逆变器并联的功率共享精度

线路阻抗 $(R+jX)$ 的不一致性（尤其是 $R/X$ 较大时）、滤波器参数差异和测量位置偏差均导致实际功率分配偏离下垂系数预设值。倒下垂（$P$-$V$、$Q$-$f$）可部分补偿高 $R/X$ 场景的共享误差，但增加了控制复杂度。

### 6.5 故障期间下垂与 IEEE 1547 无功支撑要求的冲突

IEEE 1547 标准要求 GFM 在故障期间提供无功电流支撑，优先级高于有功下垂。此时下垂关系被让位于电压穿越逻辑，需要在控制架构中显式处理模式切换。

## 7. 量化性能边界

| 场景 | 方法 | 精度/性能指标 | 来源 |
|------|------|-------------|------|
| 动态负载 | CPID vs FDR | CPID 频率偏差 <0.37%，FDR 更低 | Nurunnabi 2025 |
| 动态负载 | CPID vs FDR | CPID 电压偏差 <2.9% | Nurunnabi 2025 |
| 黑启动稳态 | FDR + 二次 PI | 电压与优化解误差 <1%，频率精确收敛 60 Hz | Nguyen 2021 |
| 并联 GFM/GFL | EVR | 无功共享精度优于 FDR，满足 IEEE 1547 | Nurunnabi 2025 |
| L/LC/LCL 滤波器 | FDR/EVR | PQ 运行域差异显著（LCL > LC > L） | Nurunnabi 2025 |
| 故障穿越 | EVR vs FDR | EVR 电压支撑时间更长 | Nurunnabi 2025 |

**Nguyen 2021 光储GFM黑启动下垂控制模型**:
- 提出一次下垂（P-f/Q-V）+ 二次PI恢复的两级控制架构
- 下垂环根据PCC有功/无功实时调节电压幅值和频率参考，二次PI补偿稳态偏差
- 黑启动完成时稳态电压与优化解误差<1%，频率精确收敛至 60 Hz
- 覆盖变压器励磁、线路充电和负荷阶跃等多种工况
- 验证平台：PSCAD高保真EMT模型，改进IEEE 9节点系统

**Nurunnabi 2025 GFM逆变器PQ能力与下垂边界**:
- 系统界定GFM逆变器下垂控制受额定电流约束（RIC）和PWM饱和约束的双重限制
- CPID（受控比例-积分-微分）方法引入微分项改善动态响应，频率偏差 <0.37%
- EVR（增强型电压调节）在限幅时保留电压支撑能力，优于 FDR
- 动态负载时电压偏差 <2.9%，满足 IEEE 1547 标准
- 含 L、LC、LCL 三种滤波器拓扑的 PQ 运行域对比（SVPWM 增强 PQ 容量）
- 验证方式：EMT 仿真 + 实时 HIL

**下垂模型多机并联特性（经典结论）**:
- 多机并联时各单元频率相同，有功分配近似与下垂系数倒数成正比：$m_{p1} P_1 \approx m_{p2} P_2$
- 线路阻抗比 $R/X$ 显著时功率共享偏离下垂预设值，需改用 P-V/Q-f 倒下垂或虚拟阻抗补偿
- 下垂环带宽必须远低于电压环和电流环带宽以保证时间尺度分离
- 下垂系数设计：$k_p = \Delta f_{max}/P_{rated}$，$k_q = \Delta V_{max}/Q_{rated}$
- VSM 的惯性时间常数 $H$ 典型值 0.5-5s，阻尼系数 $D_p$ 典型值 20-200 p.u.
- 直流下垂系数 $k_{dc}$ 按电压等级设计：380V 系统 0.1-1.0 V/kW，±500kV 系统 1-10 kV/kW

**数据缺口声明**：下垂控制模型页的量化数据主要来自GFM逆变器控制文献和经典数值分析结论，缺乏独立针对下垂控制模型精度的系统验证。不同下垂控制变体（传统下垂、VSM、自适应下垂）在相同测试条件下的横向精度对比数据缺失。下垂系数取值的通用设计准则缺乏系统研究。

## 8. 相关主题与链接

### 8.1 相关模型
- [[mtdc-model]] — 多端直流下垂控制
- [[pll-model]] — 角度同步
- [[pi-controller-model]] — 功率环控制

### 8.2 相关方法
- [[state-space-method]] — 小信号稳定性分析
- [[numerical-integration]] — 角度积分
- [[fixed-admittance]] — 系统级仿真

### 8.3 相关主题
- 二次控制 — 恢复频率/电压
- 虚拟阻抗 — 改善功率均分
- 一致性控制 — 分布式协同

## 来源论文

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]] — Nguyen 等 2021，在 PSCAD 中构建光储混合 GFM 黑启动模型，提出一次下垂 + 二次 PI 两级控制架构，验证电压 <1% 误差和频率精确收敛至 60 Hz
- [[advancing-grid-forming-inverter-technology-comprehensive-pq-capability-and-perfo]] — Nurunnabi 等 2025，系统推导 GFM 逆变器 PQ 能力边界（RIC + PWM 饱和），提出 CPID 和 EVR 两种增强下垂方法，含 L/LC/LCL 滤波器对比，EMT 仿真 + 实时 HIL 验证
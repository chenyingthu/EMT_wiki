---
title: "EMI滤波器 (EMI Filter)"
type: model
tags: [emi-filter, filter, common-mode, differential-mode, conducted-emission, emc]
created: "2026-04-30"
---

# EMI滤波器 (EMI Filter)

## 定义与概述

EMI滤波器是电力电子系统中用于抑制电磁干扰的关键无源/有源网络，通过衰减传导干扰信号确保设备满足EMC标准。在EMT仿真中，EMI滤波器模型用于分析开关噪声传播、评估滤波性能、设计阻尼特性。本模型涵盖传导EMI滤波器、共模/差模滤波网络、有源EMI抑制，适用于变频器、逆变器、开关电源的EMI特性分析。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 衰减共模干扰（CM）
- 衰减差模干扰（DM）
- 提供阻抗失配以反射噪声
- 保护敏感设备

**滤波器类型**:
| 类型 | 频率范围 | 拓扑 | 应用 |
|------|----------|------|------|
| 低通滤波器 | DC-30MHz | LC/RC | 开关电源 |
| 共模滤波器 | 150kHz-30MHz | 共模电感 | 电机驱动 |
| 差模滤波器 | 10kHz-1MHz | X电容+差模电感 | PFC电路 |
| 混合滤波器 | 全频段 | CM+DM组合 | 逆变器 |
| 有源滤波器 | 10kHz-1MHz | 运放/晶体管 | 低频EMI |

### 1.2 滤波器结构

**典型EMI滤波器拓扑**:
```
        L1 (DM)          L2 (CM)
L ──[====]──┬──────────────[≈≈]──┬──→ Load
            │      │             │
           ─┴─Cx  ─┴─Cy1        ─┴─Cy2
            │      │             │
N ──[====]──┴────────[≈≈]────────┴──→
            │                      │
           GND (PE)               GND
```

**元件功能**:
- **Cx**: X电容（差模，线对线）
- **Cy**: Y电容（共模，线对地）
- **Lcm**: 共模电感（双线绕制）
- **Ldm**: 差模电感（漏感）

### 1.3 EMI频谱特征

**传导干扰频段**:
```
频率范围          频段名称              限值标准
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9kHz-150kHz      低频传导              CISPR 11
150kHz-30MHz     传导发射              CISPR 11/22
30MHz-1GHz       辐射发射              CISPR 11/22
```

**典型噪声源**:
- 开关频率谐波（几kHz-几百kHz）
- 开关边沿高频（几MHz-几十MHz）
- 寄生振荡（几十MHz-几百MHz）

## 2. 物理模型与数学描述

### 2.1 二阶LC低通滤波器

#### 2.1.1 传递函数

**标准LC低通**:
$$H(s) = \frac{1}{s^2LC + s\frac{L}{R_L} + 1}$$

**截止频率**:
$$f_c = \frac{1}{2\pi\sqrt{LC}}$$

**特性阻抗**:
$$Z_0 = \sqrt{\frac{L}{C}}$$

**阻尼系数**:
$$\zeta = \frac{1}{2R}\sqrt{\frac{L}{C}}$$

#### 2.1.2 频率响应

**幅度响应**:
$$|H(j\omega)| = \frac{1}{\sqrt{(1-\omega^2LC)^2 + (\omega L/R)^2}}$$

**衰减斜率**:
- 低于fc: 0 dB/decade
- 高于fc: -40 dB/decade（理想二阶）

### 2.2 共模滤波器模型

#### 2.2.1 共模等效电路

**单相共模**:
```
        Lcm
   ┌────[≈≈]────┐
   │            │
   │     ┬──┬   │
   │    ─┴──┴─  │
   │      Cy    │
   │            │
   └────────────┘
          │
         GND
```

**共模阻抗**:
$$Z_{CM}(s) = sL_{CM} + \frac{1}{sC_Y}$$

**共模谐振频率**:
$$f_{CM} = \frac{1}{2\pi\sqrt{L_{CM}C_Y}}$$

#### 2.2.2 共模电感模型

**带磁芯损耗**:
$$Z_{CM} = R_{core} + sL_{CM} + \frac{1}{sC_{par}}$$

其中：
- $R_{core}$: 磁芯损耗等效电阻
- $C_{par}$: 绕组寄生电容
- $L_{CM}$: 共模电感量

### 2.3 差模滤波器模型

#### 2.3.1 差模等效电路

**π型滤波器**:
```
   ┌──Cx1──┬────┬──Cx2──┐
   │       │    │       │
   Ldm    ─┴─  ─┴─    Ldm
   │       Cm   Cm      │
   │       │    │       │
   └───────┴────┴───────┘
```

**差模传递函数**:
$$H_{DM}(s) = \frac{1}{s^2L_{DM}C_{eq} + s\frac{L_{DM}}{R} + 1}$$

其中 $C_{eq} = C_{X1} + C_{X2} + C_m$

#### 2.3.2 漏感利用

共模电感的漏感可用作差模电感：
$$L_{DM} = (1-k)L_{CM}$$

其中 $k$ 为耦合系数（通常0.98-0.995）。

### 2.4 高阶滤波器

#### 2.4.1 多级LC滤波器

**两级π型**:
$$H(s) = H_1(s) \cdot H_2(s)$$

**级联衰减**:
$$A_{total} = A_1 + A_2 \quad \text{(dB)}$$

#### 2.4.2 Butterworth响应

**N阶Butterworth**:
$$|H(j\omega)| = \frac{1}{\sqrt{1+(\omega/\omega_c)^{2N}}}$$

**最大平坦特性**: 在通带内无纹波

### 2.5 有源EMI滤波器

#### 2.5.1 电流补偿型

**原理**: 注入抵消电流
$$i_{cancel} = -G \cdot i_{noise}$$

**残余电流**:
$$i_{res} = i_{noise} + i_{cancel} = i_{noise}(1-G)$$

#### 2.5.2 电压补偿型

**注入电压**:
$$v_{inj} = -G \cdot v_{noise}$$

**环路增益限制**:
有效频率范围受运放带宽限制。

## 3. EMT仿真模型

### 3.1 离散化实现

**LC滤波器离散模型**:
```
Vout[k] = (2*Vout[k-1] - Vout[k-2] + (Ts^2/LC)*Vin[k]) / (1 + Ts/(2RC))
```

**状态空间形式**:
```
x[k+1] = A*x[k] + B*u[k]
y[k] = C*x[k] + D*u[k]
```

### 3.2 共模/差模分离

**共模电压**:
$$v_{CM} = \frac{v_1 + v_2}{2}$$

**差模电压**:
$$v_{DM} = v_1 - v_2$$

**分离网络**:
```fortran
! 共模/差模分离
V_CM = (V_L + V_N) / 2.0
V_DM = V_L - V_N

! 分别通过CM和DM滤波器
V_CM_OUT = CM_FILTER(V_CM)
V_DM_OUT = DM_FILTER(V_DM)

! 重构输出
V_L_OUT = V_CM_OUT + V_DM_OUT/2.0
V_N_OUT = V_CM_OUT - V_DM_OUT/2.0
```

### 3.3 EMI频谱分析

**FFT分析流程**:
1. 时域仿真获取电流/电压波形
2. 加窗（Hanning/Hamming）
3. FFT变换
4. CISPR准峰值检波器模拟

**准峰值检波器**:
$$\tau_{charge} = 1 \text{ ms}, \quad \tau_{discharge} = 160 \text{ ms}$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**LC低通滤波器**:
```fortran
! LC滤波器离散模型
! 电感电流
I_L = I_L_OLD + DT/L * (V_IN - V_C)
! 电容电压
V_C = V_C_OLD + DT/C * I_L
! 输出
V_OUT = V_C

! 阻尼（可选）
IF (R_DAMP > 0) THEN
  I_R = V_C / R_DAMP
  I_C = I_L - I_R
  V_C = V_C_OLD + DT/C * I_C
END IF
```

**共模滤波器**:
```fortran
! 共模电感模型
V_CM = (V_L + V_N) / 2.0

! 磁芯饱和模型（可选）
IF (ABS(I_CM) > I_SAT) THEN
  L_CM_EFF = L_CM * I_SAT / ABS(I_CM)
ELSE
  L_CM_EFF = L_CM
END IF

! 共模电流
I_CM = I_CM_OLD + DT/L_CM_EFF * (V_CM - V_CY)
! Y电容电压
V_CY = V_CY_OLD + DT/CY * I_CM
```

**EMI测量（CISPR频段）**:
```fortran
! 准峰值检波器简化模型
V_QP = V_QP_OLD + DT/TAU_CHARGE * (V_PEAK - V_QP_OLD)
IF (V_PEAK < V_QP) THEN
  V_QP = V_QP_OLD - DT/TAU_DISCHARGE * V_QP_OLD
END IF

! CISPR 11 B类限值 (dBμV)
! 150kHz-500kHz: 66-56 (线性下降)
! 500kHz-5MHz: 56
! 5MHz-30MHz: 60
```

### 4.2 MATLAB/Simulink实现

**S域滤波器模型**:
```matlab
function v_out = lc_filter(v_in, params)
    % LC低通滤波器
    s = tf('s');
    L = params.L;
    C = params.C;
    R = params.R_load;
    
    % 传递函数
    H = 1 / (s^2*L*C + s*L/R + 1);
    
    % 离散化
    Hd = c2d(H, params.Ts, 'tustin');
    
    % 滤波
    v_out = lsim(Hd, v_in, []);
end

function [cm, dm] = mode_separation(v1, v2)
    % 共模/差模分离
    cm = (v1 + v2) / 2;
    dm = v1 - v2;
end

function [f, mag] = emi_spectrum(v, Ts)
    % EMI频谱分析
    N = length(v);
    window = hanning(N);
    v_win = v .* window;
    
    % FFT
    V_fft = fft(v_win);
    V_mag = abs(V_fft(1:N/2+1)) * 2/N;
    
    % 频率轴
    f = (0:N/2)/(N*Ts);
    
    % 转换为dBμV
    mag = 20*log10(V_mag / 1e-6);
end
```

## 5. 典型参数参考

### 5.1 单相逆变器EMI滤波器

| 参数 | 符号 | 典型值 | 说明 |
|------|------|--------|------|
| 共模电感 | Lcm | 1-10 mH | 双线绕制 |
| Y电容 | Cy | 1-10 nF | 安全限值影响 |
| X电容 | Cx | 0.1-2 μF | 差模滤波 |
| 差模电感 | Ldm | 10-100 μH | 漏感或独立 |
| 截止频率 | fc | 1-10 kHz | 低于开关频率 |

### 5.2 三相变频器滤波器

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 共模电感 | 3×10 mH | 三相磁环 |
| Y电容 | 10 nF/相 | 受漏电流限制 |
| X电容 | 4.7 μF | 线间连接 |
| 差模电感 | 50 μH | 每相独立 |

### 5.3 CISPR 11限值（B类设备）

| 频率范围 | 准峰值限值 | 平均值限值 |
|----------|------------|------------|
| 150kHz-500kHz | 66-56 dBμV | 56-46 dBμV |
| 500kHz-5MHz | 56 dBμV | 46 dBμV |
| 5MHz-30MHz | 60 dBμV | 50 dBμV |

## 6. 相关主题与链接

### 6.1 相关模型
- [[igbt-model|IGBT模型]] - 主要噪声源
- [[pwm-modulator-model|PWM调制器]] - 谐波分析
- [[inductor-model|电感模型]] - 磁饱和特性
- [[capacitor-model|电容模型]] - ESR/ESL影响
- [[vsc-model|VSC模型]] - 典型应用场景

### 6.2 相关方法
- FFT分析 - 频谱处理
- [[frequency-dependent-modeling|频率相关建模]] - 宽频特性
- [[multirate-method|多速率方法]] - EMI与系统级仿真

### 6.3 相关主题
- EMC设计 - 电磁兼容
- 传导干扰 - 测试方法
- 开关噪声 - 产生机理
- 磁元件设计 - 共模电感

## 7. 适用边界与限制

### 7.1 适用条件
- **频率范围**: 传导干扰频段（<30MHz）
- **线性区域**: 元件工作在线性区
- **温度范围**: 元件额定温度
- **电压等级**: 不超过元件耐压

### 7.2 模型限制
- **辐射EMI**: 未建模空间辐射
- **非线性磁芯**: 大信号饱和简化处理
- **温度影响**: 参数温度漂移未建模
- **寄生参数**: 部分PCB寄生参数忽略

### 7.3 精度边界
| 频率范围 | 预期精度 | 主要误差来源 |
|----------|----------|--------------|
| <100kHz | ±5% | 元件公差 |
| 100kHz-1MHz | ±10% | 寄生参数 |
| 1MHz-10MHz | ±20% | 分布参数 |
| >10MHz | ±30% | 辐射耦合 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| EMI filter design for inverter applications | 2015 | 逆变器EMI滤波器设计 |
| Common-mode noise modeling in motor drives | 2018 | 电机驱动共模噪声建模 |
| Active EMI filter for power converters | 2020 | 有源EMI滤波器技术 |
| High-frequency modeling of EMI filters | 2019 | EMI滤波器高频特性 |

## 相关方法
- [[vector-fitting|矢量拟合]] - 频变阻抗拟合
- [[frequency-dependent-modeling|频率相关建模]] - 宽频特性建模
- [[multirate-method|多速率方法]] - EMI与系统级仿真

## 相关模型
- [[igbt-model|IGBT模型]] - 主要噪声源
- [[pwm-modulator-model|PWM调制器]] - 谐波分析
- [[inductor-model|电感模型]] - 共模电感磁饱和
- [[capacitor-model|电容模型]] - ESR/ESL影响

## 相关主题
- 电磁兼容设计 - EMC标准与测试
- 传导干扰 - 测试方法
- 开关噪声 - 产生机理
- 磁元件设计 - 共模电感设计

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

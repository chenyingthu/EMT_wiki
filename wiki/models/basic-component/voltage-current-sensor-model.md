---
title: "电压电流传感器 (Voltage/Current Sensor)"
type: model
tags: [sensor, voltage-sensor, current-sensor, measurement, transducer, isolation]
created: "2026-04-30"
---

# 电压电流传感器 (Voltage/Current Sensor)


```mermaid
graph TD
    subgraph Ncmp[电压电流传感器 (Voltage/Current Sen…]
        N0[PT/CT: 电压/电流]
        N1[霍尔传感器: 电流]
        N2[罗氏线圈: 电流]
        N3[电容分压: 电压]
        N4[光纤传感器: 电压/电流]
    end
```


## 定义与概述

电压电流传感器是电力系统EMT仿真和控制中的关键测量元件，用于将高电压大电流转换为可测量的低电平信号，同时提供电气隔离。传感器的带宽、精度和延迟特性直接影响控制系统性能和测量精度。本模型涵盖霍尔传感器、罗氏线圈、电压互感器、电容分压器等测量设备，适用于保护、计量和控制系统的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 电压/电流信号转换
- 高低压电气隔离
- 信号调理和滤波
- 过压过流保护

**传感器类型**:
| 类型 | 测量量 | 原理 | 带宽 | 精度 | 应用 |
|------|--------|------|------|------|------|
| PT/CT | 电压/电流 | 电磁感应 | 50Hz-5kHz | 0.1-1% | 保护/计量 |
| 霍尔传感器 | 电流 | 霍尔效应 | DC-100kHz | 0.5-2% | 变频器 |
| 罗氏线圈 | 电流 | 电磁感应 | 1Hz-10MHz | 1-3% | 暂态测量 |
| 电容分压 | 电压 | 容性分压 | DC-1MHz | 0.1-1% | 高压测量 |
| 光纤传感器 | 电压/电流 | 法拉第效应 | DC-10MHz | 0.2-1% | 高压隔离 |

### 1.2 传感器结构

**电磁式电压互感器(PT)**:
```
高压 ──→[一次绕组]──┬── 低压输出
              │      │
             铁芯   二次绕组
              │      │
接地 ──→──────┴──────┘
```

**电磁式电流互感器(CT)**:
```
一次电流 ──→穿芯──┬── 二次电流
                │
               铁芯
                │
            二次绕组
                │
            负载电阻
```

**霍尔电流传感器**:
```
被测电流 ──→导体──┬── 霍尔元件 ──→ 输出电压
              │
           聚磁环
              │
           激励电流
```

### 1.3 运行激励

**输入信号**：
- 一次电压：数十V至数百kV
- 一次电流：mA至数十kA
- 频率：DC至MHz
- 谐波：含多次谐波

**输出信号**：
- 二次电压：100V（PT标准）
- 二次电流：5A/1A（CT标准）
- 传感器输出：mV-V级
- 数字输出：经ADC转换

**性能指标**：
- 变比精度
- 相位误差
- 带宽
- 响应时间

## 2. 物理模型与数学描述

### 2.1 电磁式PT模型

#### 2.1.1 等效电路

**T型等效电路**:
```
Vp ──R1──┬──L1──┬──┬── R2 ── Vs
         │      │  │
        ─┴─     │  └─ L2
         │      │
         Rm    ─┴─
         │      │
        ─┴─     Cs
         │
        ─┴─
```

**参数**：
- $R_1, L_1$：一次侧电阻漏感
- $R_2, L_2$：二次侧电阻漏感
- $R_m$：铁损等效电阻
- $L_m$：励磁电感
- $C_s$：分布电容

#### 2.1.2 变比误差

**理想变比**：
$$n = \frac{V_p}{V_s} = \frac{N_1}{N_2}$$

**实际变比**：
$$n_{actual} = \frac{N_1}{N_2} + \epsilon$$

**比差**（变比误差）:
$$\epsilon = \frac{n_{nominal} V_s - V_p}{V_p} \times 100\%$$

**角差**（相位误差）:
$$\delta = \theta_p - \theta_s$$

**精度等级**：
| 等级 | 比差(%) | 角差(分) | 应用 |
|------|---------|----------|------|
| 0.1 | ±0.1 | ±5 | 计量 |
| 0.2 | ±0.2 | ±10 | 计量 |
| 0.5 | ±0.5 | ±20 | 计量/保护 |
| 1.0 | ±1.0 | ±40 | 保护 |
| 3.0 | ±3.0 | - | 保护 |

### 2.2 电磁式CT模型

#### 2.2.1 等效电路

**等效电路**:
```
Ip ──┬── 理想变流器 ──┬── Is
    │              │
   励磁支路       Zb(负载)
    │              │
   Rm||Lm         Rs
```

**励磁特性**:
$$I_e = \frac{V_s}{Z_m} = \frac{I_s Z_b}{R_m || j\omega L_m}$$

**变比关系**:
$$N_1 I_p = N_2 (I_s + I_e)$$

#### 2.2.2 饱和特性

**拐点电压**:
$$V_k = k \cdot f \cdot B_{sat} \cdot A \cdot N_2$$

**饱和后特性**:
$$L_m = \begin{cases}
L_{m0}, & V_s < V_k \\
L_{m0} \frac{V_k}{V_s}, & V_s \geq V_k
\end{cases}$$

**剩磁影响**:
$$B_r = \text{剩磁通密度}$$
$$\phi(t) = \int v_s(t) dt + \phi_r$$

### 2.3 霍尔电流传感器

#### 2.3.1 霍尔效应原理

**霍尔电压**:
$$V_H = \frac{R_H I_c B}{d}$$

其中：
- $R_H$：霍尔系数
- $I_c$：控制电流
- $B$：磁感应强度
- $d$：半导体厚度

**与待测电流关系**:
$$B = \frac{\mu_0 N I_p}{l}$$
$$V_H = K_H I_p$$

其中 $K_H$ 为传感器灵敏度。

#### 2.3.2 频率响应

**传递函数**:
$$H(s) = \frac{K_{dc}}{1 + s\tau}$$

**带宽**：通常DC-100kHz

**响应时间**：1-10μs

### 2.4 罗氏线圈

#### 2.4.1 工作原理

**感应电压**:
$$v(t) = -M \frac{di(t)}{dt}$$

其中 $M$ 为互感系数。

**积分器还原**:
$$i(t) = -\frac{1}{M} \int v(t) dt$$

#### 2.4.2 积分器设计

**有源积分器**:
$$H(s) = -\frac{1}{sRC}$$

**频率范围**：1Hz-10MHz

**低频截止**：由积分器时间常数决定

## 3. EMT仿真模型

### 3.1 PT/CT离散化

**PT模型**:
```
Vs[k] = (Vp[k]/n) * (1 + epsilon) * exp(j*delta)
```

**CT模型（考虑饱和）**:
```
phi[k+1] = phi[k] + Vs[k]*Ts
if phi > phi_sat:
    Lm = Lm0 * phi_sat/phi
Ie = Vs/(Rm + jw*Lm)
Is = (Np/Ns)*Ip - Ie
```

### 3.2 传感器动态模型

**一阶惯性**:
$$\tau \frac{dV_{out}}{dt} + V_{out} = K \cdot V_{in}$$

**离散化**:
$$V_{out}[k+1] = (1-\alpha) V_{out}[k] + \alpha K V_{in}[k+1]$$

其中 $\alpha = T_s/\tau$。

**采样延迟**:
$$V_{out}[k] = K \cdot V_{in}[k - N_d]$$

其中 $N_d = T_d/T_s$ 为延迟步数。

### 3.3 噪声模型

**白噪声**:
$$V_{noise} = K_n \cdot \text{randn}()$$

**量化噪声**:
$$V_{quant} = \frac{V_{range}}{2^{N_{bits}}}$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**PT模型**:
```fortran
! 电压互感器模型
! 理想变比
VS = VP / N_RATIO

! 比差和角差修正
VS_MAG = ABS(VS) * (1.0 + EPSILON/100.0)
VS_ANG = ANGLE(VS) + DELTA * PI/180.0
VS_OUT = VS_MAG * EXP(J*VS_ANG)

! 带宽限制（一阶惯性）
VS_FILT = (1-ALPHA) * VS_FILT_OLD + ALPHA * VS_OUT
```

**CT模型（含饱和）**:
```fortran
! 电流互感器模型
! 磁链计算
FLUX = FLUX + VS * DT

! 饱和判断
FLUX_SAT = B_SAT * A_CORE * N2
IF (ABS(FLUX) > FLUX_SAT) THEN
  ! 饱和处理
  LM = LM0 * FLUX_SAT / ABS(FLUX)
ELSE
  LM = LM0
END IF

! 励磁电流
IE = VS / CMPLX(RM, OMEGA*LM)

! 二次电流
IS = (N1/N2) * IP - IE
```

**霍尔传感器**:
```fortran
! 霍尔电流传感器
! 增益和偏移
VH = K_H * IP + V_OFFSET

! 带宽限制
VH_FILT = (1-ALPHA) * VH_FILT_OLD + ALPHA * VH

! 噪声
VH_OUT = VH_FILT + NOISE_AMP * RAND()
```

### 4.2 MATLAB/Simulink实现

**PT/CT模型**:
```matlab
function vs = pt_model(vp, params)
    % 理想变比
    vs_ideal = vp / params.ratio;
    
    % 比差修正
    vs_mag = abs(vs_ideal) * (1 + params.ratio_error/100);
    
    % 角差修正
    angle_shift = params.angle_error * pi/180;
    vs_ang = angle(vs_ideal) + angle_shift;
    
    vs = vs_mag * exp(1j*vs_ang);
    
    % 带宽限制
    persistent vs_filt
    if isempty(vs_filt), vs_filt = vs; end
    alpha = params.Ts / params.tau;
    vs_filt = (1-alpha) * vs_filt + alpha * vs;
    
    vs = vs_filt;
end

function is = ct_saturation_model(ip, params)
    persistent flux
    if isempty(flux), flux = 0; end
    
    % 二次电压
    vs = flux / params.Ts;  % 简化
    
    % 磁链更新
    flux = flux + vs * params.Ts;
    
    % 饱和判断
    flux_sat = params.b_sat * params.a_core * params.n2;
    if abs(flux) > flux_sat
        lm = params.lm0 * flux_sat / abs(flux);
    else
        lm = params.lm0;
    end
    
    % 励磁电流
    ie = vs / (params.rm + 1j*params.omega*lm);
    
    % 二次电流
    is = (params.n1/params.n2) * ip - ie;
end
```

## 5. 典型参数参考

### 5.1 PT参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 变比 | 110kV/100V | 一次/二次 |
| 精度 | 0.2/0.5级 | 计量/保护 |
| 容量 | 50-500VA | 负载能力 |
| 带宽 | 50Hz-5kHz | 谐波测量 |

### 5.2 CT参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 变比 | 1000/5A | 一次/二次 |
| 精度 | 0.5/5P级 | 计量/保护 |
| 拐点电压 | 100-500V | 饱和特性 |
| 剩磁 | 0.6-0.8 | p.u. |

### 5.3 霍尔传感器参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 量程 | ±50A-±2000A | 电流范围 |
| 带宽 | DC-100kHz | 频率响应 |
| 响应时间 | 1-5μs | 上升时间 |
| 线性度 | 0.1-1% | 误差 |

### 5.4 罗氏线圈参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 灵敏度 | 1-100mV/kA | 输出/电流 |
| 带宽 | 1Hz-10MHz | 频率范围 |
| 相位误差 | <1° | 精度 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[transformer-model|变压器模型]] - PT/CT类似变压器
- [[pi-controller-model|PI控制器]] - 使用传感器信号
- [[pll-model|锁相环]] - 电压测量应用

### 6.2 相关方法
- 信号处理 - 传感器信号调理
- 滤波技术 - 噪声抑制

### 6.3 相关主题
- 测量系统 - 精度分析
- 保护系统 - 继电器配合
- 计量系统 - 电能计量

## 7. 适用边界与限制

### 7.1 适用条件
- **频率范围**：取决于传感器类型
- **幅值范围**：额定值±20%
- **温度范围**：-40°C至+85°C
- **负载范围**：额定负载±25%

### 7.2 模型限制
- **温度漂移**：未建模温度影响
- **老化效应**：长期使用精度下降
- **外部干扰**：EMC影响未建模
- **安装影响**：邻近效应未考虑

### 7.3 精度边界
| 传感器类型 | 精度 | 带宽 | 延迟 |
|-----------|------|------|------|
| PT/CT | ±0.1-3% | 5kHz | 1-10ms |
| 霍尔 | ±0.5-2% | 100kHz | 1-10μs |
| 罗氏线圈 | ±1-3% | 10MHz | <1μs |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Modeling of instrument transformers for EMT simulation | 2013 | 互感器EMT建模 |
| Transient performance of current transformers | 2016 | CT暂态性能 |
| Hall effect sensors in power electronic applications | 2018 | 霍尔传感器应用 |

## 相关方法
- [[numerical-integration|数值积分]] - 传感器动态模型离散化
- [[state-space-method|状态空间法]] - CT饱和状态分析
- [[frequency-dependent-modeling|频率相关建模]] - 宽频响应特性

## 相关模型
- [[transformer-model|变压器模型]] - PT/CT类似变压器结构
- [[pi-controller-model|PI控制器]] - 使用传感器信号的控制器
- [[pll-model|锁相环]] - 电压测量应用
- [[emi-filter-model|EMI滤波器]] - 传感器噪声抑制

## 相关主题
- 测量系统 - 传感器精度分析
- 保护系统 - 继电器配合
- 计量系统 - 电能计量
- 信号处理 - 传感器信号调理

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

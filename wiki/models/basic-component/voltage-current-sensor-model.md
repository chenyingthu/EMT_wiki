---
title: "电压电流传感器 (Voltage/Current Sensor)"
type: model
tags: [sensor, voltage-sensor, current-sensor, measurement, transducer, isolation]
created: "2026-04-30"
updated: "2026-05-11"
---

# 电压电流传感器 (Voltage/Current Sensor)



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

### 7.3 量化性能边界

电压电流传感器的 EMT 建模精度已有可核验的量化结果，但以下数据均绑定具体传感器型号、测量条件和验证场景，不能外推为通用能力：

- **Oliveira (2021)** 提出了基于散射参数（S参数）的多端口黑盒建模方法，用于超高压电压互感器（EHV-VT）的宽频建模。S参数模型在 MHz 频段的幅频特性拟合误差 **<3%**，高频谐振峰频率定位偏差 **<2%**；引入白/灰盒融合技术后，低频段（<100 kHz）导纳幅值测量误差从 **>15%** 降低至 **<3%**。测量频带成功扩展至 **50 MHz**，完整覆盖 VFTO 特征频段（100 kHz~50 MHz）。验证基于实际 500 kV GIS 中 EHV-VT，不自动适用于其他电压等级或不同 VT 结构（Oliveira 2021）。

- **司马文霞 (2021)** 提出了基于导纳互差法的电容式电压互感器（CVT）宽频非线性耦合模型。在典型 35 kV CVT 上验证：中间变压器铁芯饱和时，所提模型励磁涌流第一峰值误差仅为 **1.71%**，远低于传统模型的 **77.79%**；模型在 **5 Hz~1 MHz** 频段的电压传递特性归一化均方误差（NMSE）为 **0.91%**；雷电冲击电压第一峰值仿真误差为 **3.11%**。验证基于典型 35 kV CVT 实物，不自动适用于其他电压等级或不同制造结构的 CVT（司马文霞 2021）。

- **Chaudhary (2004)** 在 EPRI/DCG EMTP Version 2.0 中实现了 CT 和 CVT 的暂态模型。CT 模型可模拟频率高达数 kHz 的暂态过程，但限于变压器模型无分布电容，不适用于更高频率。FORTRAN 接口支持每时步数据交换，典型仿真步长 50-100 μs 时，继电器算法处理延迟 **<1 μs**。验证基于 230 kV 输电系统（1200:5 A CT、ARMCO M4 铁芯），不自动适用于其他 CT 型号或饱和程度（Chaudhary 2004）。

这些量化数据不构成对电压电流传感器建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与失败模式

### 适用条件
- **频率范围**：取决于传感器类型
- **幅值范围**：额定值±20%
- **温度范围**：-40°C至+85°C
- **负载范围**：额定负载±25%

### 失效边界
- **温度漂移**：未建模温度影响
- **老化效应**：长期使用精度下降
- **外部干扰**：EMC影响未建模
- **安装影响**：邻近效应未考虑

### 关键假设
1. 传感器工作在额定频率范围（忽略超频段谐振效应）
2. 二次负载在额定范围内（负载变化影响变比精度）
3. CT 铁芯未深度饱和（深度饱和下励磁电流急剧增大）
4. 测量信号远大于噪声基底（忽略信噪比限制）

## 代表性来源

- [[expanding-the-measuring-range-via-s-parameters-in-a-ehv-voltage-transformer-mode|Oliveira (2021) - Expanding the measuring range via S-parameters in a EHV voltage transformer modelling]]
- [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|司马文霞 (2021) - 考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]]
- [[protection-system-representation-in-the-electromagnetic-transients-program-power|Chaudhary (2004) - Protection system representation in the Electromagnetic Transients Program]]

## 与相关页面的关系

- [[transformer-model|变压器模型]] - PT/CT类似变压器结构
- [[pi-controller-model|PI控制器]] - 使用传感器信号的控制器
- [[pll-model|锁相环]] - 电压测量应用
- [[emi-filter-model|EMI滤波器]] - 传感器噪声抑制

## 开放问题

- 宽禁带器件高频开关下传感器的带宽需求
- 数字式传感器（合并单元）的 EMT 建模
- 光学传感器在暂态测量中的精度验证
- 传感器饱和与保护系统配合的闭环仿真

## 参考标准

- IEC 60044 - 互感器标准
- IEEE Std. C37.110 - CT 保护应用导则
- IEEE Std. C57.13 - 互感器标准要求

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

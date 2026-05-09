---
title: "电容 (Capacitor)"
type: model
tags: [capacitor, capacitance, passive-component, esr, esl, frequency-dependent]
created: "2026-04-30"
---

# 电容 (Capacitor)


```mermaid
graph TD
    subgraph Ncmp[电容 (Capacitor)]
        N0[陶瓷电容: 陶瓷]
        N1[电解电容: 氧化铝]
        N2[薄膜电容: 聚酯/聚丙烯]
        N3[超级电容: 活性炭]
        N4[电力电容: 浸渍纸/膜]
    end
```


## 定义与概述

电容是存储电荷的无源元件，在EMT仿真中广泛用于建模能量存储、滤波、耦合和去耦等电路功能。实际电容器具有等效串联电阻（ESR）和等效串联电感（ESL），这些寄生参数在高频暂态仿真中显著影响其电气特性。本模型涵盖理想电容、含寄生参数模型、频率相关模型，适用于电力电子、输电系统和电磁兼容EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 存储电场能量
- 滤波和平滑
- 耦合与去耦
- 功率因数校正
- 储能

**电容器类型**:
| 类型 | 介质 | 容量范围 | 电压范围 | 特点 |
|------|------|----------|----------|------|
| 陶瓷电容 | 陶瓷 | pF-μF | <1kV | 高频好、小体积 |
| 电解电容 | 氧化铝 | μF-mF | <600V | 大容量、有极性 |
| 薄膜电容 | 聚酯/聚丙烯 | nF-μF | <2kV | 低损耗、稳定 |
| 超级电容 | 活性炭 | F级 | <3V | 超大容量、功率密度高 |
| 电力电容 | 浸渍纸/膜 | μF-mF | 1-35kV | 高压大功率 |

### 1.2 物理结构

**平板电容器**:
$$C = \frac{\varepsilon_0 \varepsilon_r A}{d}$$

其中：
- $A$：极板面积
- $d$：极板间距
- $\varepsilon_r$：相对介电常数

**寄生参数来源**：
- ESR：引线电阻、极板电阻、介质损耗
- ESL：引线电感、极板几何电感
- 介质损耗：极化弛豫、电导损耗

### 1.3 运行激励

**电压激励**：
- 额定电压：由介质强度决定
- 纹波电压：交流分量叠加在直流上
- 浪涌电压：短时过电压（通常为额定电压的1.1-1.3倍）

**电流激励**：
- 纹波电流：$I_{rms} = \sqrt{\sum I_k^2}$
- 脉冲电流：充放电峰值电流
- dV/dt限制：$I_{max} = C \cdot (dV/dt)_{max}$

**频率范围**：
- 陶瓷电容：GHz级
- 电解电容：通常<100kHz
- 电力电容：50/60Hz + 谐波

## 2. 物理模型与数学描述

### 2.1 理想电容模型

**电压-电流关系**:
$$i(t) = C \frac{dv(t)}{dt}$$
$$v(t) = v(0) + \frac{1}{C} \int_0^t i(\tau) d\tau$$

**储能**:
$$W_C = \frac{1}{2} C v^2(t)$$

**阻抗（频域）**:
$$Z_C(j\omega) = \frac{1}{j\omega C} = -j\frac{1}{\omega C}$$

### 2.2 含寄生参数模型

#### 2.2.1 等效串联电路

**ESR-ESL模型**:
```
    ESL      ESR
  ━━━////━━━━/\/\/\━┓
                    ┃
  ━━━━━━━━━━━━━━━━━━┻━
         C
```

**阻抗表达式**:
$$Z(j\omega) = ESR + j\omega ESL + \frac{1}{j\omega C}$$
$$= ESR + j\left(\omega ESL - \frac{1}{\omega C}\right)$$

**谐振频率**:
$$f_0 = \frac{1}{2\pi\sqrt{ESL \cdot C}}$$

在谐振频率处，电容器呈现纯电阻特性（阻抗=ESR）。

#### 2.2.2 介质损耗模型

**损耗角正切**:
$$\tan\delta = \frac{P_{loss}}{P_{reactive}} = \omega C \cdot ESR$$

**品质因数**:
$$Q = \frac{1}{\tan\delta} = \frac{1}{\omega C \cdot ESR}$$

**介质损耗功率**:
$$P_{loss} = I_{rms}^2 \cdot ESR = V_{rms}^2 \cdot \omega C \cdot \tan\delta$$

### 2.3 频率相关模型

#### 2.3.1 复介电常数模型

$$\varepsilon^*(\omega) = \varepsilon'(\omega) - j\varepsilon''(\omega)$$

**电容频率特性**:
$$C(\omega) = C_0 \frac{\varepsilon'(\omega)}{\varepsilon_0}$$

**有效ESR**:
$$ESR(\omega) = \frac{\varepsilon''(\omega)}{\omega \varepsilon'(\omega) C}$$

#### 2.3.2 德拜弛豫模型

对于极性介质：
$$\varepsilon^*(\omega) = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + j\omega\tau}$$

其中：
- $\varepsilon_s$：静态介电常数
- $\varepsilon_\infty$：高频介电常数
- $\tau$：弛豫时间常数

### 2.4 非线性电容模型

#### 2.4.1 电压相关电容

陶瓷电容（高介电常数）呈现电压依赖性：
$$C(V) = \frac{C_0}{1 + \alpha V^2}$$

或经验公式：
$$C(V) = C_{max} \left[1 - k\left(\frac{V}{V_{rated}}\right)^2\right]$$

#### 2.4.2 超级电容模型

**双电层电容**:
$$C = C_{dl} + C_{ps}$$

其中：
- $C_{dl}$：双电层电容（恒定）
- $C_{ps}$：赝电容（电压/电流相关）

**传输线模型**:
将超级电容建模为分布RC网络，考虑多孔电极中的离子传输。

## 3. EMT仿真模型

### 3.1 理想电容模型

**梯形法离散化**:

历史项形式：
$$i_{n+1} = \frac{2C}{\Delta t} v_{n+1} + I_{hist}$$

其中历史项：
$$I_{hist} = -\left(i_n + \frac{2C}{\Delta t} v_n\right)$$

**等效导纳**:
$$G_{eq} = \frac{2C}{\Delta t}$$

**节点导纳矩阵贡献**:
$$Y_{nn} = \begin{bmatrix} G_{eq} & -G_{eq} \\ -G_{eq} & G_{eq} \end{bmatrix}$$

### 3.2 含ESR-ESL模型

#### 3.2.1 状态空间形式

选择电容电压和电感电流为状态变量：
$$\frac{d}{dt}\begin{bmatrix} v_C \\ i_L \end{bmatrix} = 
\begin{bmatrix} 0 & \frac{1}{C} \\ -\frac{1}{L} & -\frac{R}{L} \end{bmatrix}
\begin{bmatrix} v_C \\ i_L \end{bmatrix} +
\begin{bmatrix} 0 \\ \frac{1}{L} \end{bmatrix} v_{in}$$

#### 3.2.2 EMT离散化

使用梯形法：
$$\begin{bmatrix} v_{C,n+1} \\ i_{L,n+1} \end{bmatrix} = 
A_d \begin{bmatrix} v_{C,n} \\ i_{L,n} \end{bmatrix} + B_d v_{in,n+1}$$

其中 $A_d = (I - \frac{\Delta t}{2}A)^{-1}(I + \frac{\Delta t}{2}A)$

### 3.3 频率相关电容模型

#### 3.3.1 矢量拟合法

使用有理函数逼近阻抗：
$$Z(s) = R_0 + \sum_{i=1}^{N} \frac{R_i}{s - p_i}$$

转换为等效电路：
- $R_0$：高频电阻
- 每个极点对应一个RL并联支路

#### 3.3.2 Foster等效电路

```
  R0      L1      L2      LN
━/\/\/\━////┳━/\/\/\━////┳━...━/\/\/\━////┓
           ┃            ┃            ┃
          C1           C2           CN
           ┃            ┃            ┃
━━━━━━━━━━━┻━━━━━━━━━━━━┻━━━━...━━━━┻━━━━━
```

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**理想电容**:
```fortran
CAPACITOR
  C = 100.0e-6    ! 电容值(F)
  V0 = 0.0        ! 初始电压(V)
```

**含ESR/ESL**:
```fortran
! 使用串联RLC元件
C_BRANCH
  C = 100.0e-6
  R_SERIES = 0.01  ! ESR (Ohm)
  L_SERIES = 10e-9 ! ESL (H)
```

**超级电容**:
```fortran
! 分布参数模型
SUPERCAP
  C_total = 100.0   ! 总容量(F)
  N_segments = 10   ! 分段数
  R_leakage = 10k   ! 漏电阻(Ohm)
```

### 4.2 MATLAB/Simulink实现

**Simscape模型**:
```matlab
% 理想电容
C = capacitor('C', 100e-6);

% 含ESR/ESL
R_esr = resistor('ESR', 0.01);
L_esl = inductor('ESL', 10e-9);
C_ideal = capacitor('C', 100e-6);
% 串联连接
```

**自定义模型（非线性电容）**:
```matlab
function i = nonlinear_capacitor(v, v_prev, dt, C0, alpha)
    C_eff = C0 / (1 + alpha * v^2);
    i = C_eff * (v - v_prev) / dt;
end
```

### 4.3 SPICE实现

**基本电容**:
```spice
C1 node1 node2 100u IC=0
```

**含ESR/ESL**:
```spice
* 使用子电路
XCAP1 node1 node2 CAP_ESL_ESR C=100u ESR=0.01 ESL=10n

.SUBCKT CAP_ESL_ESR PLUS MINUS C=100u ESR=0.01 ESL=10n
R1 PLUS 1 ESR
L1 1 2 ESL
C1 2 MINUS C
.ENDS
```

**行为模型**:
```spice
* 电压相关电容
B1 node1 node2 I=C0/(1+0.1*V(node1,node2)^2)*ddt(V(node1,node2))
```

### 4.4 实时仿真考虑

**步长限制**:
含ESL的电容需满足：
$$\Delta t < 2\sqrt{ESL \cdot C}$$

**数值稳定性**:
- 极小电容（$C < 1 pF$）：导纳 $G_{eq} = 2C/\Delta t$ 可能过小
- 极大电容（$C > 1 F$）：导纳可能过大导致矩阵病态

**多速率仿真**:
- 小电容（<1μF）：需小步长（<1μs）
- 大电容（>1mF）：可大步长（>10μs）

## 5. 典型参数参考

### 5.1 电力电子用电容

| 类型 | 容量 | 额定电压 | ESR | ESL | 应用 |
|------|------|----------|-----|-----|------|
| 电解 | 100-10000μF | 16-450V | 0.01-0.5Ω | 20-100nH | 整流滤波 |
| 薄膜 | 0.1-10μF | 400-2000V | 1-10mΩ | 10-50nH | 逆变器DC-Link |
| 陶瓷 | 0.01-10μF | 25-100V | 1-50mΩ | 0.1-5nH | 高频去耦 |
| 超级 | 1-5000F | 2.5-3V | 0.1-10mΩ | 10-50nH | 储能 |

### 5.2 高压电力电容

| 电压等级 | 容量范围 | 应用 |
|----------|----------|------|
| 1-10kV | 10-1000kvar | 配电系统补偿 |
| 35-110kV | 1-50Mvar | 输电系统补偿 |
| 220-500kV | 50-300Mvar | 高压并联补偿 |

### 5.3 介质特性

| 介质 | $\varepsilon_r$ | $\tan\delta$ (50Hz) | 温度系数 |
|------|-----------------|---------------------|----------|
| 空气 | 1 | 0 | 可忽略 |
| 陶瓷(NP0) | 15-100 | 0.0001-0.001 | ±30ppm/°C |
| 陶瓷(X7R) | 2000-4000 | 0.01-0.03 | ±15% |
| 铝氧化物 | 8-10 | 0.001-0.01 | - |
| 聚丙烯 | 2.2 | 0.0002 | -200ppm/°C |
| 聚酯 | 3.3 | 0.005 | - |

## 6. 相关主题与链接

### 6.1 相关模型
- [[resistor-model|电阻模型]] - 阻性元件
- [[inductor-model|电感模型]] - 感性元件
- [[bess-model|储能系统模型]] - 超级电容应用

### 6.2 相关方法
- [[numerical-integration|数值积分]] - 电容离散化方法
- [[vector-fitting|矢量拟合]] - 频率相关建模

### 6.3 相关主题
- 滤波器设计 - 电容滤波应用
- 功率因数校正 - 无功补偿
- 电磁兼容 - 去耦电容设计

## 7. 适用边界与限制

### 7.1 适用条件
- **容量范围**：pF 至 kF级
- **电压范围**：mV 至数百kV
- **频率范围**：DC 至GHz（取决于类型）
- **温度范围**：-55°C 至 +150°C（取决于介质）
- **纹波电流**：不超过额定值

### 7.2 模型限制
- **介质非线性**：高介电常数陶瓷的电压依赖性
- **老化效应**：电解电容容量衰减
- **温度效应**：ESR随温度变化显著
- **自愈效应**：薄膜电容击穿后自愈
- **频率限制**：分布参数模型仅在有限频段准确

### 7.3 精度边界
| 模型类型 | 频率范围 | 精度 | 适用场景 |
|---------|----------|------|----------|
| 理想电容 | DC-1kHz | ±10% | 低频储能分析 |
| 含ESR | 1kHz-100kHz | ±5% | 滤波器设计 |
| 含ESR+ESL | 100kHz-10MHz | ±10% | EMI/EMC分析 |
| 分布参数 | >10MHz | ±15% | 高频电路 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| High-frequency modeling of DC-link capacitors for power electronic converters | 2016 | DC-Link电容高频建模 |
| Frequency-dependent equivalent circuit modeling of electrolytic capacitors | 2018 | 电解电容等效电路模型 |
| Electrochemical modeling of supercapacitors for EMT simulation | 2020 | 超级电容电化学建模 |

## 相关方法
- [[numerical-integration|数值积分]] - 电容离散化方法
- [[vector-fitting|矢量拟合]] - 频率相关阻抗拟合
- [[state-space-method|状态空间法]] - ESR-ESL模型状态方程

## 相关模型
- [[resistor-model|电阻模型]] - ESR等效电阻
- [[inductor-model|电感模型]] - ESL等效电感
- [[bess-model|电池储能系统]] - 超级电容储能应用
- [[emi-filter-model|EMI滤波器]] - 滤波电容设计

## 相关主题
- [[harmonic-analysis|谐波分析]] - 电容滤波与谐波
- 功率因数校正 - 无功补偿
- 电磁兼容 - 去耦电容设计
- 热建模 - 电容发热与寿命

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |

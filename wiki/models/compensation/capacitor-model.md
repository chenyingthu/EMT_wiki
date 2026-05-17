---
title: "电容 (Capacitor)"
type: model
tags: [capacitor, capacitance, passive-component, esr, esl, frequency-dependent]
created: "2026-04-30"
updated: "2026-05-11"
---

# 电容 (Capacitor)



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

### 7.3 量化性能边界

电容模型的 EMT 仿真精度已有可核验的量化结果，但以下数据均绑定具体电容器类型、建模方法和验证条件，不能外推为通用能力：

- **Iravani & Wang (2004)** 在 EMTP 平台上构建了 TEHMP161A 型耦合电容器电压互感器（CCVT）的全元件级时域数字模型。分压器-排流线圈回路自然振荡频率精确测定为 **13.956 kHz**，该模态主导近端故障下的高频暂态响应。串联电抗器杂散电容 Cc 从 0 pF 增至 1500 pF 时，频响曲线第一谷点频率偏移至约 **640 Hz**，证实 Cc 对低频段谐振特性具有决定性影响。负载功率因数低于 **0.6** 滞后时，>300 Hz 频段幅频响应衰减显著增加。验证基于 Haefely-Trench TEHMP161A 型 CCVT 实物，不自动适用于其他型号或电压等级（Iravani & Wang 2004）。

- **司马文霞 (2021)** 提出了 CVT 宽频非线性耦合模型，模型在 **5 Hz~1 MHz** 频段的电压传递特性归一化均方误差（NMSE）为 **0.91%**，验证了电容分压器宽频建模的精度。该数据来自典型 35 kV CVT 的扫频测试，电容分压器作为 CVT 的核心组件，其频率响应特性在此得到量化验证（司马文霞 2021，详见 [[voltage-current-sensor-model]]）。

这些量化数据不构成对电容建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。


## 适用边界与失败模式

### 适用条件
- **容量范围**：pF 至 kF级
- **电压范围**：mV 至数百kV
- **频率范围**：DC 至GHz（取决于类型）
- **温度范围**：-55°C 至 +150°C（取决于介质）
- **纹波电流**：不超过额定值

### 失效边界
- **介质非线性**：高介电常数陶瓷的电压依赖性
- **老化效应**：电解电容容量衰减
- **温度效应**：ESR随温度变化显著
- **自愈效应**：薄膜电容击穿后自愈
- **频率限制**：分布参数模型仅在有限频段准确

### 关键假设
1. 介质均匀且各向同性（实际介质存在局部缺陷）
2. 寄生参数 ESR/ESL 为常数（实际随频率和温度变化）
3. 漏电流可忽略（实际随温度和电压升高）
4. 电容值不随直流偏置变化（高介电常数陶瓷显著偏离此假设）

## 代表性来源

- [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo]] Iravani & Wang (2004) — 耦合电容器电压互感器 CCVT 宽频暂态响应建模
- [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] 司马文霞 (2021) — CVT 宽频非线性耦合模型

## 来源论文

| 论文 | 年份 |
|------|------|
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo]] | 2004 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
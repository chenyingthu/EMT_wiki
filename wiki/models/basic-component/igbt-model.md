---
title: "IGBT (绝缘栅双极晶体管)"
type: model
tags: [igbt, power-semiconductor, switching, thermal, gate-driver, power-electronics]
created: "2026-04-30"
updated: "2026-05-11"
---

# IGBT (绝缘栅双极晶体管)


## 定义与概述

IGBT（Insulated Gate Bipolar Transistor）是电压控制的双极型功率半导体器件，结合了MOSFET的高输入阻抗和双极晶体管的低导通压降优点，在EMT仿真中广泛用于建模逆变器、变流器和电力电子开关。本模型涵盖开关特性、导通损耗、开关损耗、热模型，适用于中高压大容量电力电子系统的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 电压控制开关
- 功率放大
- 高速开关
- 能量转换控制

**IGBT类型**:
| 类型 | 阻断电压 | 电流 | 开关频率 | 特点 | 应用 |
|------|----------|------|----------|------|------|
| 穿通(PT) | 600-1200V | 10-800A | <20kHz | 低饱和压降 | 工业驱动 |
| 非穿通(NPT) | 600-1700V | 10-400A | <30kHz | 正温度系数 | 新能源 |
| 场截止(FS) | 600-6500V | 50-3600A | <50kHz | 低损耗 | 轨道交通 |
| 沟槽栅 | 600-1700V | 10-800A | <100kHz | 高可靠性 | 电动汽车 |

### 1.2 物理结构

**等效电路**:
```
         C (集电极)
         |
    ━━━━━┳━━━━━
         |
    ━━━━━┻━━━━━  PNP晶体管
         |
    ━━━━━┳━━━━━  MOSFET
    G    ┃
  (栅极)┗━━━━━━━ E (发射极)
```

**内部结构**:
- **MOSFET部分**：提供电压控制和高输入阻抗
- **PNP晶体管**：提供电导率调制降低导通压降
- **寄生晶闸管**：可能导致闩锁效应

**寄生参数**：
- 栅极电容 $C_{ge}$, $C_{gc}$, $C_{ce}$
- 寄生电感 $L_g$, $L_c$, $L_e$
- 体二极管（反并联）

### 1.3 运行激励

**栅极驱动电压**：
- 正向驱动：+15V（导通）
- 负向偏置：-5至-15V（关断增强）
- 阈值电压：4-6V

**集电极-发射极电压**：
- 额定电压：600V-6.5kV（取决于型号）
- 安全工作区：由最大电压、电流、功率限制

**电流**：
- 连续电流：由结温限制
- 脉冲电流：2-4倍额定电流（脉宽<1ms）
- 短路电流：5-10倍额定电流（<10μs）

## 2. 物理模型与数学描述

### 2.1 静态特性模型

#### 2.1.1 输出特性

$$I_C = f(V_{CE}, V_{GE})$$

**饱和区**（$V_{GE} > V_{GE,th}$，$V_{CE}$较小）：
$$V_{CE,sat} = V_T \ln\left(\frac{I_C}{I_{C0}}\right) + R_{on} I_C$$

**有源区**（$V_{GE}$控制）：
$$I_C = \frac{K}{2}(V_{GE} - V_{GE,th})^2 (1 + \lambda V_{CE})$$

其中：
- $K$：跨导参数
- $\lambda$：沟道长度调制系数
- $V_{GE,th}$：栅极阈值电压

#### 2.1.2 传输特性

$$I_C = \frac{K}{2}(V_{GE} - V_{GE,th})^2, \quad V_{GE} > V_{GE,th}$$

### 2.2 导通电阻模型

**等效导通电阻**:
$$R_{on} = R_{channel} + R_{drift} + R_{substrate}$$

**MOSFET沟道电阻**:
$$R_{channel} = \frac{1}{K(V_{GE} - V_{GE,th})}$$

**漂移区电阻**（电导率调制）:
$$R_{drift} = \frac{W_{drift}}{q \mu_n N_D A} \cdot f(\text{modulation})$$

**总导通压降**:
$$V_{CE,sat} = V_{bi} + I_C \cdot R_{on}$$

其中 $V_{bi}$ 为双极结压降（约0.7V）。

### 2.3 开关暂态模型

#### 2.3.1 开通过程

**开通时间组成**:
- 开通延迟 $t_{d(on)}$：栅极电容充电至阈值
- 上升时间 $t_r$：集电极电流上升
- 米勒平台：栅极电压保持恒定

**栅极充电**:
$$V_{GE}(t) = V_{GG} (1 - e^{-t/\tau})$$

其中 $\tau = R_G (C_{ge} + C_{gc})$。

**电流上升**:
$$\frac{dI_C}{dt} = \frac{g_m (V_{GG} - V_{GE,th})}{L_{loop}}$$

#### 2.3.2 关断过程

**关断时间组成**:
- 关断延迟 $t_{d(off)}$：栅极放电
- 下降时间 $t_f$：电流下降
- 拖尾电流：双极载流子清除

**拖尾电流模型**:
$$I_{tail}(t) = I_{tail,0} \cdot e^{-t/\tau_{tail}}$$

其中 $\tau_{tail}$ 为少数载流子寿命。

#### 2.3.3 开关损耗计算

**开通损耗**:
$$E_{on} = \int_0^{t_{on}} v_{CE}(t) \cdot i_C(t) dt$$

近似计算：
$$E_{on} \approx \frac{1}{2} V_{DC} \cdot I_C \cdot t_{ri} + \frac{1}{6} V_{DC} \cdot I_C \cdot t_{fv}$$

**关断损耗**:
$$E_{off} = \int_0^{t_{off}} v_{CE}(t) \cdot i_C(t) dt$$

近似计算：
$$E_{off} \approx \frac{1}{6} V_{DC} \cdot I_C \cdot t_{rv} + \frac{1}{2} V_{DC} \cdot I_{tail} \cdot t_{tail}$$

**开关损耗功率**:
$$P_{sw} = f_{sw} (E_{on} + E_{off})$$

### 2.4 栅极电容模型

**输入电容**:
$$C_{ies} = C_{ge} + C_{gc}$$

**输出电容**:
$$C_{oes} = C_{ce} + C_{gc}$$

**反向传输电容**:
$$C_{res} = C_{gc}$$

**米勒电容**（电压相关）:
$$C_{gc} = \frac{C_{gc0}}{(1 + V_{CE}/V_0)^n}$$

### 2.5 热模型

#### 2.5.1 瞬态热阻抗

**Foster网络**:
$$Z_{th}(t) = \sum_{i=1}^{n} R_{th,i} (1 - e^{-t/\tau_{th,i}})$$

**Cauer网络**（物理意义明确）:
```
  Tj ─Rth1─┬─Rth2─┬─Rth3─ Tc
          Cth1   Cth2   Cth3
           │      │      │
          ─┴──────┴──────┴─
```

#### 2.5.2 结温计算

**瞬态结温**:
$$T_j(t) = T_a + \int_0^t P_d(\tau) \frac{dZ_{th}(t-\tau)}{dt} d\tau$$

**稳态结温**:
$$T_j = T_a + P_d \cdot R_{th,ja}$$

**热导率调制**:
导通电阻随温度变化：
$$R_{on}(T) = R_{on,25} [1 + \alpha (T - 25)]$$

## 3. EMT仿真模型

### 3.1 理想开关模型

**开关函数**:
$$S = \begin{cases}
1, & V_{GE} > V_{GE,th} \text{且} t > t_{delay} \\
0, & V_{GE} < V_{GE,th}
\end{cases}$$

**等效电路**:
```
导通:  R_on (1-100mΩ)
关断:  R_off (>1MΩ)
```

**EMT实现**:
$$G_{eq} = S \cdot G_{on} + (1-S) \cdot G_{off}$$

### 3.2 详细开关模型

#### 3.2.1 状态机模型

**状态定义**:
- OFF：关断状态（$V_{GE} < V_{th}$）
- TURNING_ON：开通过程
- ON：导通状态
- TURNING_OFF：关断过程

**状态转换**:
```
    VGE>Vth      ton完成      VGE<Vth      toff完成
OFF ───────→ TURNING_ON ────→ ON ───────→ TURNING_OFF ────→ OFF
```

#### 3.2.2 分段线性开关模型

**开通波形**:
| 阶段 | 时间 | $I_C$ | $V_{CE}$ |
|------|------|-------|----------|
| 延迟 | $t_{d(on)}$ | 0 | $V_{DC}$ |
| 电流上升 | $t_{ri}$ | 线性上升 | $V_{DC}$ |
| 电压下降 | $t_{fv}$ | $I_{load}$ | 指数下降 |

**关断波形**:
| 阶段 | 时间 | $I_C$ | $V_{CE}$ |
|------|------|-------|----------|
| 延迟 | $t_{d(off)}$ | $I_{load}$ | $V_{CE,sat}$ |
| 电压上升 | $t_{rv}$ | $I_{load}$ | 线性上升 |
| 电流下降 | $t_{fi}$ | 线性下降 | $V_{DC}$ |
| 拖尾 | $t_{tail}$ | 指数衰减 | $V_{DC}$ |

### 3.3 平均模型

用于系统级仿真（忽略开关细节）：

**等效电压源**:
$$V_{eq} = d \cdot V_{DC} - R_{eq} \cdot I_{load}$$

其中 $d$ 为占空比，$R_{eq}$ 为等效电阻。

**损耗模型**:
$$P_{loss} = I_{rms}^2 R_{on} + f_{sw} (E_{on} + E_{off})$$

### 3.4 栅极驱动模型

**驱动电路等效**:
```
  VGG+ ─/\/\/\──┬── G
       Rgon    │
  VGG- ─/\/\/\──┘
       Rgoff
```

**栅极电流**:
$$I_G = \begin{cases}
\frac{V_{GG+} - V_{GE}}{R_{gon}}, & \text{开通} \\
\frac{V_{GG-} - V_{GE}}{R_{goff}}, & \text{关断}
\end{cases}$$

**栅极电压**:
$$\frac{dV_{GE}}{dt} = \frac{I_G}{C_{ge} + C_{gc}(V_{CE})}$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**理想IGBT**:
```fortran
IGBT
  RON = 1.0e-3     ! 导通电阻(Ohm)
  VON = 0.0        ! 导通压降(V)
  VTH = 5.0        ! 阈值电压(V)
```

**详细模型**:
```fortran
IGBT_DETAILED
  VGE_TH = 5.0
  GFS = 20.0       ! 跨导
  RON = 5.0e-3
  COFF = 1.0e-9    ! 关断电容
  VGE_MAX = 15.0
```

**开关特性**:
```fortran
! 定义开关时间
TON_DELAY = 100.0e-9   ! 开通延迟
TON_RISE = 50.0e-9     ! 上升时间
TOFF_DELAY = 200.0e-9  ! 关断延迟
TOFF_FALL = 100.0e-9   ! 下降时间
TAIL_TIME = 500.0e-9   ! 拖尾时间
```

### 4.2 MATLAB/Simulink实现

**Simscape模型**:
```matlab
% IGBT
IGBT = igbt('IGBT');
IGBT.Vth = 5.0;
IGBT.Ron = 0.01;
IGBT.Roff = 1e6;
IGBT.Vf = 0.8;
```

**自定义详细模型**:
```matlab
function dydt = igbt_model(t, y, v_ge, v_ce, params)
    i_c = y(1);      % 集电极电流
    q_s = y(2);       % 存储电荷
    
    % 栅极控制
    if v_ge > params.Vth
        g_m = params.K * (v_ge - params.Vth);
    else
        g_m = 0;
    end
    
    % 电流方程
    di_c = (g_m * v_ce - i_c) / params.tau_sw;
    
    % 存储电荷（用于拖尾）
    dq_s = params.I_C_on - q_s/params.tau_tail;
    
    dydt = [di_c; dq_s];
end
```

**损耗计算**:
```matlab
function [P_cond, P_sw] = igbt_losses(I_c, V_dc, f_sw, params)
    % 导通损耗
    V_ce_sat = params.V_ce0 + params.R_on * I_c;
    P_cond = V_ce_sat * I_c;
    
    % 开关损耗（查表）
    E_on = interp2(params.E_on_table, I_c, V_dc);
    E_off = interp2(params.E_off_table, I_c, V_dc);
    P_sw = f_sw * (E_on + E_off);
end
```

### 4.3 SPICE实现

**基本模型**:
```spice
.SUBCKT IGBT C G E
Q1 C G E QMOD
.MODEL QMOD NPN(
+ IS=1e-13 BF=50 VAF=100
+ CJE=1n CJC=500p CJS=200p
+ TF=100n TR=1u)
.ENDS
```

**改进模型**（含MOSFET-BJT）:
```spice
.SUBCKT IGBT_DETAILED C G E PARAMS: VTH=5 RON=0.01
M1 C G X X PMOS W=1 L=1
Q1 C X E NPN
R1 X E {RON}
.ENDS
```

### 4.4 实时仿真考虑

**步长限制**:
- 详细开关模型：$\Delta t < t_{switch}/10$
- 典型IGBT：步长 < 50ns
- 可使用插值法处理开关事件

**模型简化策略**:
| 仿真类型 | 推荐模型 | 步长 |
|----------|----------|------|
| 器件级 | 详细物理 | <10ns |
| 变流器级 | 分段线性 | 10-100ns |
| 系统级 | 平均/理想 | 1-10μs |

**并行计算**:
- 多电平换流器可并行化每个IGBT模型
- 热模型可与电路解耦计算

## 5. 典型参数参考

### 5.1 中压IGBT模块

| 参数 | 1200V/300A | 1700V/600A | 3300V/1200A | 6500V/750A |
|------|------------|------------|-------------|------------|
| $V_{CE,sat}$ | 1.7V | 2.0V | 2.5V | 3.5V |
| $t_{on}$ | 100ns | 150ns | 200ns | 400ns |
| $t_{off}$ | 300ns | 400ns | 600ns | 1000ns |
| $C_{ies}$ | 10nF | 20nF | 40nF | 60nF |
| $R_{th,jc}$ | 0.15K/W | 0.08K/W | 0.02K/W | 0.03K/W |

### 5.2 开关损耗特性（典型值）

| 条件 | $E_{on}$ (mJ) | $E_{off}$ (mJ) | 总损耗 |
|------|---------------|----------------|--------|
| 600V/300A | 8 | 12 | 20 |
| 1200V/600A | 30 | 45 | 75 |
| 1700V/1200A | 80 | 120 | 200 |
| 3300V/1500A | 300 | 400 | 700 |

### 5.3 栅极驱动参数

| 参数 | 最小值 | 典型值 | 最大值 |
|------|--------|--------|--------|
| $V_{GE,on}$ | 13V | 15V | 18V |
| $V_{GE,off}$ | -15V | -8V | -5V |
| $R_{gon}$ | 1Ω | 5Ω | 50Ω |
| $R_{goff}$ | 1Ω | 5Ω | 50Ω |
| $Q_g$ | - | 1-5μC | - |

## 6. 相关主题与链接

### 6.1 相关模型
- [[diode-model|二极管模型]] - 反并联二极管
- [[vsc-model|VSC模型]] - IGBT在换流器中的应用
- [[mmc-model|MMC模型]] - 多电平换流器
- [[transformer-model|变压器模型]] - 隔离驱动

### 6.2 相关方法
- [[average-value-model|平均值模型]] - 系统级仿真
- 热建模 - 温度相关特性

### 6.3 相关主题
- PWM控制 - 脉宽调制
- 软开关 - 零电压/电流开关
- 驱动电路 - 栅极驱动设计
- 保护电路 - 过流/过压保护

## 7. 适用边界与限制

### 7.1 适用条件
- **电压范围**：600V-6.5kV（取决于型号）
- **电流范围**：10A-3.6kA
- **频率范围**：通常<100kHz（硬开关）
- **温度范围**：-40°C至+150°C（结温）
- **dv/dt**：通常<10kV/μs
- **di/dt**：取决于栅极电阻

### 7.2 模型限制
- **电磁效应**：未考虑EMI/EMC辐射
- **老化效应**：未建模退化过程
- **宇宙射线**：未考虑单粒子烧毁
- **热耦合**：电-热耦合需外部迭代
- **集肤效应**：高频连接件电阻变化

### 7.3 量化性能边界

IGBT 作为开关器件的 EMT 仿真性能已有可核验的量化结果，但以下数据均绑定具体建模方法和验证条件，不能外推为通用能力：

- **Na (2023)** 提出了结合半步长后向欧拉法与插值/外推策略的改进算法，用于固定步长 EMT 仿真中开关器件（含二极管、IGBT、晶闸管）的暂态模拟。在 IGBT/二极管/电感电路测试中，虚假开关损耗从普通插值法的 **212.6 μJ** 大幅降低至约 **2 μJ**，消除率超过 **99%**。该方法彻底消除了传统瞬时插值法固有的"提前一个时间步"数值误差，电感电流/电压波形与 0.1 μs 参考解的相位偏差趋近于零。验证基于自研 EMT 仿真程序和特定电力电子拓扑，不自动适用于大规模网络或多开关频繁动作场景（Na 2023）。

这些量化数据不构成对 IGBT 建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与失败模式

### 适用条件
- **电压范围**：600V-6.5kV（取决于型号）
- **电流范围**：10A-3.6kA
- **频率范围**：通常<100kHz（硬开关）
- **温度范围**：-40°C至+150°C（结温）
- **dv/dt**：通常<10kV/μs
- **di/dt**：取决于栅极电阻

### 失效边界
- **电磁效应**：未考虑EMI/EMC辐射
- **老化效应**：未建模退化过程
- **宇宙射线**：未考虑单粒子烧毁
- **热耦合**：电-热耦合需外部迭代
- **集肤效应**：高频连接件电阻变化

### 关键假设
1. 栅极驱动信号理想（忽略驱动电路非理想特性）
2. 温度分布均匀（实际模块内存在温度梯度）
3. 开关过程一维近似（忽略多维载流子分布效应）
4. 寄生参数为常数（实际随频率和温度变化）

## 代表性来源

- [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu|Na (2023) - An improved high-accuracy interpolation method for switching devices in EMT simulation]]
- [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model (2021)]]
- [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation (2019)]]
- [[hierarchical-device-level-modular-multilevel-converter-modeling-for-parallel-and|Hierarchical Device-Level MMC Modeling (2020)]]

## 与相关页面的关系

- [[diode-model|二极管模型]] - 反并联续流二极管
- [[vsc-model|VSC模型]] - IGBT在换流器中的应用
- [[mmc-model|MMC模型]] - 多电平换流器
- [[average-value-model|平均值模型]] - 系统级仿真简化

## 开放问题

- SiC/GaN宽禁带IGBT的EMT建模方法
- 多芯片并联IGBT模块的均流建模
- IGBT老化退化模型的EMT实现
- 电-热-机械多物理场耦合仿真

## 参考标准

- IEC 60747-9 - 半导体器件IGBT标准
- JEDEC JESD24-3 - IGBT开关特性测试方法
- ABB/IFFM - IGBT模块参数提取指南

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

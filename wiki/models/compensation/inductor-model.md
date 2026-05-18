---
title: "电感 (Inductor)"
type: model
tags: [inductor, inductance, passive-component, saturation, core-loss, magnetic]
created: "2026-04-30"
updated: "2026-05-18"
---

# 电感 (Inductor)



## 定义与概述

电感是存储磁场能量的无源元件，在EMT仿真中用于建模线圈、扼流圈、变压器绕组等。实际电感器具有绕组电阻、磁芯损耗（磁滞和涡流）以及饱和非线性特性，这些效应在大电流暂态仿真中尤为重要。本模型涵盖理想电感、饱和电感、含损耗模型，适用于电力系统、电力电子和电机仿真的EMT分析。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 存储磁场能量
- 限制电流变化率
- 滤波和平滑
- 阻抗匹配
- 能量传输（变压器）

**电感器类型**:
| 类型 | 磁芯 | 电感范围 | 电流范围 | 特点 |
|------|------|----------|----------|------|
| 空心电感 | 空气 | nH-mH | 大 | 线性、无饱和 |
| 铁氧体电感 | 铁氧体 | μH-mH | 中小 | 高频、低损耗 |
| 铁心电感 | 硅钢片 | mH-H | 大 | 高磁导率、有饱和 |
| 粉芯电感 | 铁粉/合金粉 | μH-mH | 中 | 软饱和、分布式气隙 |
| 叠片电感 | 硅钢叠片 | mH-H | 大 | 低频、大功率 |

### 1.2 物理结构

**螺线管电感**:
$$L = \frac{\mu_0 \mu_r N^2 A}{l}$$

其中：
- $N$：匝数
- $A$：截面积
- $l$：磁路长度
- $\mu_r$：相对磁导率

**环形电感**:
$$L = \frac{\mu_0 \mu_r N^2 A}{2\pi r_{mean}}$$

**寄生参数**：
- 绕组电阻 $R_w$：取决于导线材料和截面积
- 匝间电容 $C_w$：相邻匝之间的分布电容
- 铁损：磁滞损耗 + 涡流损耗

### 1.3 运行激励

**电流激励**：
- 额定电流：由发热限制决定
- 饱和电流：磁芯开始饱和的电流
- 脉冲电流：短时过电流能力
- 纹波电流：交流分量有效值

**电压激励**：
- 工作电压：由绝缘等级决定
- dI/dt限制：$V_{max} = L \cdot (dI/dt)_{max}$
- 过电压：开关瞬态产生的感应电压

**频率范围**：
- 电力电感：50/60Hz + 谐波
- 电力电子：kHz至MHz级
- 射频电感：MHz至GHz级

## 2. 物理模型与数学描述

### 2.1 理想电感模型

**电压-电流关系**:
$$v(t) = L \frac{di(t)}{dt}$$
$$i(t) = i(0) + \frac{1}{L} \int_0^t v(\tau) d\tau$$

**储能**:
$$W_L = \frac{1}{2} L i^2(t)$$

**阻抗（频域）**:
$$Z_L(j\omega) = j\omega L$$

### 2.2 含绕组电阻模型

**串联RL模型**:
$$v(t) = R_w i(t) + L \frac{di(t)}{dt}$$

**品质因数**:
$$Q = \frac{\omega L}{R_w} = \frac{\text{无功功率}}{\text{有功功率}}$$

**时间常数**:
$$\tau = \frac{L}{R_w}$$

### 2.3 磁芯饱和模型

#### 2.3.1 分段线性饱和模型

$$L(i) = \begin{cases}
L_0, & |i| < I_{sat} \\
L_{sat} + (L_0 - L_{sat}) \frac{I_{sat}}{|i|}, & |i| \geq I_{sat}
\end{cases}$$

其中：
- $L_0$：小信号电感（线性区）
- $L_{sat}$：饱和电感（通常为$L_0$的1-5%）
- $I_{sat}$：饱和电流

#### 2.3.2 反正切饱和模型

$$\lambda(i) = \frac{2}{\pi} \lambda_{sat} \arctan\left(\frac{\pi L_0 i}{2\lambda_{sat}}\right)$$

**动态电感**:
$$L_d(i) = \frac{d\lambda}{di} = \frac{L_0}{1 + \left(\frac{\pi L_0 i}{2\lambda_{sat}}\right)^2}$$

#### 2.3.3 Frolich方程

$$B = \frac{H}{\alpha + \beta |H|}$$

转换为$i-\lambda$关系：
$$\lambda = \frac{N A H}{\alpha + \beta |H|} = \frac{L_0 i}{1 + k|i|}$$

其中 $L_0 = N^2 A / (l \alpha)$，$k = N \beta / (l \alpha)$

### 2.4 磁芯损耗模型

#### 2.4.1 Steinmetz方程

$$P_{core} = k_h f^\alpha B_m^\beta$$

其中：
- $k_h$：磁滞损耗系数
- $f$：频率
- $B_m$：最大磁密
- $\alpha, \beta$：材料常数（通常$\alpha \approx 1.2-1.6$，$\beta \approx 2-3$）

#### 2.4.2 改进Steinmetz方程 (iGSE)

考虑任意波形：
$$P_{core} = \frac{1}{T} \int_0^T k_i \left|\frac{dB}{dt}\right|^\alpha (\Delta B)^{\beta-\alpha} dt$$

其中 $k_i$ 由材料特性确定。

#### 2.4.3 涡流损耗

经典涡流损耗：
$$P_{eddy} = \frac{\pi^2 t^2 B_m^2 f^2}{6\rho}$$

其中：
- $t$：叠片厚度
- $\rho$：电阻率

**等效电阻模型**:
将铁损等效为与电感并联的电阻：
$$R_{core} = \frac{\omega^2 L^2}{P_{core}/I^2}$$

### 2.5 高频寄生参数模型

#### 2.5.1 分布电容效应

**等效电路**:
```
        L
    ━━━━////━━━━
    ┃          ┃
    /          /
  Cw          Rw
    /          /
    ┃          ┃
    ━━━━━━━━━━━━
```

**自谐振频率**:
$$f_{SRF} = \frac{1}{2\pi\sqrt{L \cdot C_w}}$$

高于自谐振频率时，电感呈现容性。

#### 2.5.2 趋肤效应

高频时绕组电阻增加：
$$R_{ac} = R_{dc} \cdot k_{skin}$$

**趋肤深度**:
$$\delta = \sqrt{\frac{\rho}{\pi f \mu}}$$

**圆导线的电阻增加系数**:
$$k_{skin} \approx 1 + \frac{1}{3}\left(\frac{d}{2\delta}\right)^4, \quad d < 2\delta$$

## 3. EMT仿真模型

### 3.1 线性电感模型

**梯形法离散化**:

历史项形式：
$$i_{n+1} = \frac{\Delta t}{2L} v_{n+1} + I_{hist}$$

其中历史项：
$$I_{hist} = i_n + \frac{\Delta t}{2L} v_n$$

**等效导纳**:
$$G_{eq} = \frac{\Delta t}{2L}$$

**等效电路**:
```
  ━━━━/\/\/\━━━━
       Geq
  ━━━━||⇄||━━━━  Ihist电流源
```

### 3.2 非线性饱和电感模型

#### 3.2.1 割线电感法

使用瞬时割线电感：
$$L_{sec} = \frac{\lambda(i)}{i}$$

**迭代求解**:
$$i_{n+1}^{k+1} = \frac{\Delta t}{2L_{sec}(i_{n+1}^k)} v_{n+1} + I_{hist}$$

#### 3.2.2 微分电感法

使用微分电感（增量电感）：
$$L_d = \frac{d\lambda}{di}$$

**牛顿-拉夫逊迭代**:
$$\Delta i = -\frac{f(i^k)}{f'(i^k)}$$

其中 $f(i) = i - \frac{\Delta t}{2L_d(i)} v_{n+1} - I_{hist}$

#### 3.2.3 磁链状态变量法

选择磁链为状态变量：
$$\frac{d\lambda}{dt} = v$$
$$i = f^{-1}(\lambda)$$

**梯形法**:
$$\lambda_{n+1} = \lambda_n + \frac{\Delta t}{2}(v_{n+1} + v_n)$$
$$i_{n+1} = f^{-1}(\lambda_{n+1})$$

### 3.3 含铁损模型

#### 3.3.1 并联电阻模型

```
        L
    ━━━━////━━━━
    ┃          ┃
    /          /
  Rcore       Rw
    /          /
    ┃          ┃
    ━━━━━━━━━━━━
```

**离散化**:
将铁损等效电阻与电感并联组合离散化。

#### 3.3.2 时域铁损模型

考虑磁滞回线：
$$v = R_w i + N A \frac{dB}{dt}$$

使用Preisach或Jiles-Atherton磁滞模型描述$B-H$关系。

### 3.4 互感模型

#### 3.4.1 双绕组互感

$$\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} =
\begin{bmatrix} L_1 & M \\ M & L_2 \end{bmatrix}
\frac{d}{dt}\begin{bmatrix} i_1 \\ i_2 \end{bmatrix}$$

其中 $M = k\sqrt{L_1 L_2}$，$k$为耦合系数。

**离散化**:
$$\begin{bmatrix} i_{1,n+1} \\ i_{2,n+1} \end{bmatrix} =
G_{eq} \begin{bmatrix} v_{1,n+1} \\ v_{2,n+1} \end{bmatrix} +
\begin{bmatrix} I_{1,hist} \\ I_{2,hist} \end{bmatrix}$$

其中 $G_{eq} = \frac{\Delta t}{2} L^{-1}$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**线性电感**:
```fortran
INDUCTOR
  L = 10.0e-3    ! 电感值(H)
  I0 = 0.0       ! 初始电流(A)
  R_SERIES = 0.1 ! 绕组电阻(Ohm)
```

**饱和电感**:
```fortran
SATURABLE_INDUCTOR
  L_AIR = 0.1e-3    ! 饱和后电感(H)
  L_UNSAT = 10.0e-3 ! 未饱和电感(H)
  I_SAT = 10.0      ! 饱和电流(A)
```

**Type-96饱和变压器/电感**:
```fortran
! 使用96型元件模拟饱和电感
BRANCH
  INDUCTANCE = L0
  SATURATION = FLUX_CURRENT_CURVE
```

### 4.2 MATLAB/Simulink实现

**Simscape模型**:
```matlab
% 线性电感
L = inductor('L', 10e-3);

% 饱和电感
L_sat = inductor('L', 10e-3, 'Saturation', flux_current_table);
```

**自定义饱和模型**:
```matlab
function di = saturated_inductor(t, i, v, L0, L_sat, I_sat)
    % 分段线性饱和特性
    if abs(i) < I_sat
        L_eff = L0;
    else
        L_eff = L_sat;
    end
    di = v / L_eff;
end
```

**Simulink实现**:
```matlab
% 使用查找表实现非线性电感
lambda_i_table = [0, 0.1, 0.2, 0.3, 0.4, 0.5; ...  % 电流
                  0, 1.0, 1.9, 2.5, 2.8, 3.0];    % 磁链
L_table = gradient(lambda_i_table(2,:)) ./ gradient(lambda_i_table(1,:));
```

### 4.3 EMTP/ATP实现

**Type-93电感**:
```
BRANCH
  IND=10.0mH
```

**Type-96饱和电感**:
```
SATURABLE_TRANSFORMER
  INDUCTANCE = 10.0mH
  FLUX_CURVE
    0.0    0.0
    10.0   0.1
    20.0   0.15
    50.0   0.18
  END_FLUX_CURVE
```

### 4.4 实时仿真考虑

**步长限制**:
- 线性电感：$\Delta t < 2\sqrt{L \cdot C_w}$（考虑寄生电容）
- 饱和电感：迭代收敛可能需要更小步长

**数值稳定性**:
- 极小电感（$L < 1 \mu H$）：导纳 $G_{eq} = \Delta t/(2L)$ 可能过大
- 极大电感（$L > 100 H$）：导纳可能过小导致数值问题

**非线性收敛**:
- 严重饱和时可能需要子步迭代
- 或使用预测-校正法提高稳定性

## 5. 典型参数参考

### 5.1 电力电子用电感

| 应用 | 电感值 | 电流 | 饱和电流 | 频率 |
|------|--------|------|----------|------|
| Buck电感 | 1-100μH | 1-50A | 1.2-1.5倍额定 | 50-500kHz |
| Boost电感 | 10-1000μH | 1-30A | 1.2-1.5倍额定 | 50-500kHz |
| EMI滤波 | 0.1-10mH | 1-30A | 不饱和 | 100kHz-10MHz |
| PFC电感 | 0.1-10mH | 5-50A | 1.5-2倍峰值 | 20-200kHz |

### 5.2 电力系统用电抗器

| 类型 | 电感值 | 额定电流 | 电压等级 | 用途 |
|------|--------|----------|----------|------|
| 串联电抗器 | 1-100mH | 100-5000A | 6-500kV | 限流 |
| 并联电抗器 | 1-10H | 10-500A | 110-1000kV | 无功补偿 |
| 中性点电抗器 | 0.1-1H | 10-100A | 110-500kV | 接地补偿 |
| 滤波电抗器 | 0.1-10mH | 10-1000A | 0.4-35kV | 谐波滤波 |

### 5.3 磁芯材料特性

| 材料 | $\mu_r$ | $B_{sat}$ (T) | 损耗 | 频率范围 |
|------|---------|---------------|------|----------|
| 空气 | 1 | ∞ | 无 | DC-GHz |
| 铁氧体(MnZn) | 2000-15000 | 0.3-0.5 | 低 | <2MHz |
| 铁氧体(NiZn) | 50-2000 | 0.3-0.5 | 中 | 1-100MHz |
| 硅钢 | 2000-8000 | 1.8-2.0 | 中 | <1kHz |
| 非晶合金 | 5000-100000 | 1.4-1.6 | 低 | <10kHz |
| 铁粉芯 | 10-100 | 1.0-1.5 | 中高 | <100MHz |

## 6. 相关主题与链接

### 6.1 相关模型
- [[transformer-model]] - 多绕组磁耦合
- [[resistor-model]] - 绕组电阻
- [[capacitor-model]] - 寄生电容

### 6.2 相关方法
- [[numerical-integration|数值积分]] - 电感离散化
- [[state-space-method|状态空间法]] - 饱和模型求解

### 6.3 相关主题
- 磁饱和 - 非线性磁特性
- 铁损计算 - 磁芯损耗
- EMI滤波器 - 电感应用

## 7. 适用边界与限制

### 7.1 适用条件
- **电感范围**：nH 至 kH级
- **电流范围**：mA 至数十kA
- **频率范围**：DC 至数百MHz（取决于类型）
- **温度范围**：-55°C 至 +200°C
- **饱和范围**：$L_{sat}/L_0$ 通常0.01-0.1

### 7.2 模型限制
- **饱和模型**：分段线性模型仅在有限范围准确
- **磁滞效应**：经典模型未考虑磁滞回线
- **温度效应**：电感和电阻随温度变化
- **直流偏置**：叠加直流时的增量电感变化
- **高频效应**：分布参数在极高频显著

### 7.3 量化性能边界

电感器的 EMT 仿真精度高度依赖于饱和模型、铁损模型和高频寄生参数的准确度。目前公开文献中缺乏针对电感器 EMT 建模方法的独立量化性能评估。

**数据缺口声明**：截至当前知识范围，未找到针对电感器（含饱和/铁损/高频寄生参数）EMT 建模精度的独立量化性能数据。Pordanjani (2022) 提出了三种基于 Hopkinson 类比、Buntenbach 类比和对偶原理的分布式电路方法，用于电感器在 EMT 软件中的详细电磁建模，并以二维 FEM 为参考进行了验证，但原文未报告可核验的误差百分比、计算时间倍数或网格规模等数值结果。建议用户根据具体应用场景（频率范围、饱和程度、精度要求）选择合适的电感模型（线性/饱和/含铁损），并通过与实测或 FEM 参考模型对比验证仿真精度。

这些量化数据不构成对电感器建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 来源论文

- [[electromagnetic-modeling-of-inductors-in-emt-type-software-by-three-circuit-base]] — Pordanjani 等 (2022)：提出三种分布式磁路类比方法（Hopkinson/Buntenbach/对偶原理），将电感器几何网格离散为EMTP可执行电路，与二维FEM交叉验证，无气隙nRMSE 1.13%~1.19%，有气隙nRMSE 1.52%~1.67%，线性工况比FEM快约30倍，饱和工况快约10倍。

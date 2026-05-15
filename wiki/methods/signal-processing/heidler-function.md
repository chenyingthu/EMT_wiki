---
title: "Heidler 雷电流函数 (Heidler Function)"
type: method
tags: [heidler-function, lightning, return-stroke, emt, current-waveform, lemp, cigre, iec-62305]
created: "2026-05-04"
updated: "2026-05-15"
---

# Heidler 雷电流函数 (Heidler Function)

## 定义

Heidler 函数是由 Franz Heidler 于 1985 年提出的一种描述雷电回击（return stroke）电流波形的数学解析表达式。该函数以幂函数和指数函数的组合形式，能够精确拟合实测雷电流的波前陡升和波尾缓降特性，是 EMT 仿真中雷电暂态分析（LEMP — Lightning Electromagnetic Pulse）的标准电流源模型之一。

Heidler 函数的核心优势在于其解析可微性：导数存在闭式表达，便于在数值积分中直接计算电流变化率 $di/dt$，而无需数值微分引入的噪声。这使得它在基于 Bergeron 行波模型或状态空间方法的 EMT 程序中实现简洁且稳定。

**边界限定**：本函数描述下行负地闪（downward negative lightning）的回击电流波形，包括首回击（first stroke）和后续回击（subsequent stroke）。不包括云内放电（intra-cloud）、上行闪电（upward lightning）或多回击叠加的复杂波形——后者需使用多 Heidler 函数叠加形式（De Conti & Visacro 2007）。

## EMT 中的角色

Heidler 函数是雷电暂态仿真的核心输入源，贯穿直击雷和感应雷两类场景：

- **直击雷过电压计算**：雷电流注入杆塔顶部或导线，计算绝缘子串电压、杆塔电位升（GPR）和闪络风险。Heidler 函数的 $di/dt$ 直接影响杆塔电感压降 $L_t \cdot di/dt$ 和避雷器动作时机。
- **感应雷过电压计算**：雷电流通过电磁耦合在线路感应过电压。Heidler 函数的波前陡度决定感应场的峰值，进而决定耦合到导线的电压幅值。
- **绝缘配合设计**：依据 IEC 62305 和 IEEE Std. 1243 标准，Heidler 函数用于生成标准雷电冲击波形（10/350 μs 直击雷波形、0.25/100 μs 后续回击波形），评估绝缘水平。
- **接地系统暂态响应**：雷电流通过接地极泄放入地，Heidler 函数的高频分量（波前部分）激发接地系统的频变阻抗效应，影响 GPR 峰值和波形。

## 核心机制

### 1. Heidler 函数原始表达式

Heidler (1985) 提出的原始形式为：

$$i(t) = \frac{I_m}{\eta} \cdot \frac{(t/\tau_1)^n}{1 + (t/\tau_1)^n} \cdot e^{-t/\tau_2}$$

其中：

- $I_m$：峰值电流（kA）
- $\tau_1$：波前时间常数（μs），控制电流上升速率
- $\tau_2$：波尾时间常数（μs），控制电流衰减速率
- $n$：幂指数（通常取 $n = 10$），控制波前形状陡度
- $\eta$：峰值归一化因子，确保 $i(t_{peak}) = I_m$

**峰值归一化因子**的闭式表达为：

$$\eta = \exp\left[-\left(\frac{\tau_1}{\tau_2}\right) \left(\frac{n \cdot \tau_2}{\tau_1}\right)^{1/n}\right]$$

**峰值时刻**为：

$$t_{peak} = \tau_1 \left(\frac{n \cdot \tau_2}{\tau_1}\right)^{1/n}$$

当 $n = 10$、$\tau_1 = 0.25$ μs、$\tau_2 = 2.5$ μs（后续回击典型值）时：

$$t_{peak} = 0.25 \times \left(\frac{10 \times 2.5}{0.25}\right)^{0.1} = 0.25 \times 10^{0.1} \approx 0.396 \text{ μs}$$

**电流变化率（导数）**的闭式表达为：

$$\frac{di}{dt} = \frac{I_m}{\eta \cdot \tau_1} \cdot \left[ \frac{n(t/\tau_1)^{n-1}}{1 + (t/\tau_1)^n} - \frac{(t/\tau_1)^{2n}}{(1 + (t/\tau_1)^n)^2} - \frac{\tau_1}{\tau_2} \cdot \frac{(t/\tau_1)^n}{1 + (t/\tau_1)^n} \right] \cdot e^{-t/\tau_2}$$

在 $t = t_{peak}$ 处，$di/dt = 0$；最大变化率出现在波前约 1/3 峰值时刻处。

### 2. 峰值电流变化率

最大电流变化率 $(di/dt)_{max}$ 出现在 $t \approx 0.27 \cdot t_{peak}$ 处，其近似值为：

$$(di/dt)_{max} \approx \frac{I_m}{0.27 \cdot t_{peak}}$$

对于后续回击（$I_m = 40$ kA, $t_{peak} \approx 0.4$ μs）：

$$(di/dt)_{max} \approx \frac{40}{0.108} \approx 370 \text{ kA/μs}$$

对于首回击（$I_m = 200$ kA, $t_{peak} \approx 3$ μs）：

$$(di/dt)_{max} \approx \frac{200}{0.81} \approx 247 \text{ kA/μs}$$

### 3. 参数选择与标准波形

#### IEC 62305 标准参数

IEC 62305（雷电防护）定义了标准雷电冲击电流波形参数：

| 参数 | 首回击（典型值） | 后续回击（典型值） |
|------|-----------------|-------------------|
| 峰值电流 $I_m$ | 10–200 kA（中值 50 kA） | 2–100 kA（中值 35 kA） |
| 波前时间 $T_1$ | 1–200 μs（中值 10 μs） | 0.25–5 μs（中值 0.5 μs） |
| 半峰值时间 $T_2$ | 50–2500 μs（中值 250 μs） | 10–200 μs（中值 50 μs） |
| 标准波形 | 10/350 μs | 0.25/100 μs 或 1/100 μs |

**10/350 μs 波形**（直击雷保护等级 I）：
- 波前时间 $T_f = 10$ μs（10% 到 90% 峰值）
- 半峰值时间 $T_{1/2} = 350$ μs
- 对应 Heidler 参数：$\tau_1 \approx 1.25$ μs, $\tau_2 \approx 50$ μs, $n = 10$

**0.25/100 μs 波形**（后续回击）：
- 波前时间 $T_f = 0.25$ μs
- 半峰值时间 $T_{1/2} = 100$ μs
- 对应 Heidler 参数：$\tau_1 \approx 0.031$ μs, $\tau_2 \approx 14.4$ μs, $n = 10$

#### CIGRE 波形参数

CIGRE Working Group 33-01 (1991) 基于瑞士 Mount San Salvatore 的实测数据统计得出：

| 参数 | 首回击 | 后续回击 |
|------|--------|---------|
| 峰值电流中值 | 31.1 kA | 13.5 kA |
| 波前时间中值 | 3.83 μs | 0.5 μs |
| 波尾时间中值 | 77.5 μs | 50 μs |
| 最大陡度中值 | 24.3 kA/μs | 80 kA/μs |

CIGRE 波形在 PSCAD 中已封装为标准模块，参数可调，推荐用于敏感性分析。

#### Morro do Cachimbo 实测数据

巴西 Morro do Cachimbo 观测站的实测负地闪电流数据（Visacro et al. 2004）为 Heidler 参数标定提供了实证基础。典型实测波形（De Conti 2020 引用）：

- 峰值电流 $I_p = 16$ kA
- 10% 到 90% 上升时间：0.6 μs
- 衰减到 50% 峰值时间：16.6 μs
- 最大陡度：29.6 kA/μs

该波形由两个 Heidler 函数叠加拟合（De Conti & Visacro 2007），以再现实测波形的凹陷（concavity）和多峰特征。

### 4. 多 Heidler 函数叠加（De Conti & Visacro 扩展）

原始 Heidler 函数为单峰对称波形，无法再现实测雷电流的凹陷（concave shape）和多峰特征。De Conti & Visacro (2007) 提出使用多个 Heidler 函数叠加的形式：

$$i(t) = \sum_{k=1}^{K} c_k \cdot \frac{I_m}{\eta_k} \cdot \frac{(t/\tau_{1,k})^n}{1 + (t/\tau_{1,k})^n} \cdot e^{-t/\tau_{2,k}}$$

其中 $K$ 为叠加函数数量（通常 $K = 2$ 或 $3$），每个函数有独立的系数 $c_k$、时间常数 $\tau_{1,k}$、$\tau_{2,k}$ 和归一化因子 $\eta_k$。

**首回击双峰波形**（2 个 Heidler 函数）：
- 第一个函数：控制主峰，对应 $\tau_{1,1} \approx 1.5$ μs, $\tau_{2,1} \approx 30$ μs
- 第二个函数：控制凹陷后的次峰，对应 $\tau_{1,2} \approx 5$ μs, $\tau_{2,2} \approx 80$ μs
- 系数 $c_1 + c_2 = 1$，控制两峰相对幅度

**后续回击单峰波形**（1 个 Heidler 函数）：
- 后续回击波形较平滑，通常单函数即可拟合
- 对应 $\tau_{1} \approx 0.031$ μs, $\tau_{2} \approx 14.4$ μs, $n = 10$

### 5. 波形参数与 Heidler 参数的映射

实际工程中，通常已知标准波形的波前时间 $T_f$ 和半峰值时间 $T_{1/2}$，需将其映射为 Heidler 参数 $\tau_1$、$\tau_2$。近似映射关系为：

$$\tau_1 \approx \frac{T_f}{2 \cdot (2^{1/n} - 1)}$$

$$\tau_2 \approx \frac{T_{1/2}}{\ln(2) + (T_{1/2}/T_f) \cdot \ln(2)}$$

当 $n = 10$ 时：

| 波形类型 | $T_f$ (μs) | $T_{1/2}$ (μs) | $\tau_1$ (μs) | $\tau_2$ (μs) |
|---------|-----------|---------------|--------------|--------------|
| 后续回击 (0.25/100) | 0.25 | 100 | 0.031 | 14.4 |
| 后续回击 (1/100) | 1.0 | 100 | 0.125 | 45.8 |
| 首回击 (10/350) | 10 | 350 | 1.25 | 50.0 |
| CIGRE 首回击 | 3.83 | 77.5 | 0.48 | 17.5 |

**注意**：上述映射为近似值，精确参数需通过数值优化使合成波形满足 $T_f$ 和 $T_{1/2}$ 约束。

## 形式化表达

### 核心公式汇总

**Heidler 函数（n=10）**：

$$i(t) = \frac{I_m}{\eta} \cdot \frac{(t/\tau_1)^{10}}{1 + (t/\tau_1)^{10}} \cdot e^{-t/\tau_2}$$

**归一化因子**：

$$\eta = \exp\left[-\left(\frac{\tau_1}{\tau_2}\right) \left(\frac{10 \cdot \tau_2}{\tau_1}\right)^{0.1}\right]$$

**峰值时刻**：

$$t_{peak} = \tau_1 \cdot \left(\frac{10 \cdot \tau_2}{\tau_1}\right)^{0.1}$$

**电流变化率**：

$$\frac{di}{dt} = \frac{I_m}{\eta \cdot \tau_1} \cdot \left[ \frac{10(t/\tau_1)^9}{1 + (t/\tau_1)^{10}} - \frac{(t/\tau_1)^{20}}{(1 + (t/\tau_1)^{10})^2} - \frac{\tau_1}{\tau_2} \cdot \frac{(t/\tau_1)^{10}}{1 + (t/\tau_1)^{10}} \right] \cdot e^{-t/\tau_2}$$

**多函数叠加**：

$$i(t) = \sum_{k=1}^{K} c_k \cdot i_k(t; \tau_{1,k}, \tau_{2,k}, \eta_k)$$

### 雷击过电压中的关键表达式

**杆塔顶部电压**（直击雷）：

$$U_t(t) = R_g \cdot i(t) + L_t \cdot \frac{di}{dt}$$

其中 $R_g$ 为接地电阻，$L_t$ 为杆塔等效电感（典型值 1–3 μH/m）。

**绝缘子串电压**（反击闪络评估）：

$$U_{ins}(t) = U_t(t) - U_{coupling}(t)$$

其中 $U_{coupling}$ 为导线与杆塔之间的电磁耦合电压。

**感应过电压**（Rusck 模型，Heidler 作为电流源）：

$$E_z(t) = \frac{\mu_0}{2\pi} \cdot \frac{di}{dt} \cdot \ln\left(\frac{r_2}{r_1}\right)$$

其中 $r_1$、$r_2$ 为观测点到雷电通道的距离。

## 关键技术挑战

### 1. 波前/波尾时间的精确映射

标准波形参数（$T_f$、$T_{1/2}$）到 Heidler 参数（$\tau_1$、$\tau_2$）的映射存在非线性。当 $n \neq 10$ 时（某些文献使用 $n = 8$ 或 $n = 12$），映射关系发生变化。实践中需通过数值优化（如最小二乘拟合实测波形）确定精确参数。

### 2. 多峰波形拟合

首回击电流的凹陷（concave）和多峰特征无法用单 Heidler 函数再现。De Conti & Visacro (2007) 的双函数叠加方法需要 6 个自由参数（$c_1, \tau_{1,1}, \tau_{2,1}, c_2, \tau_{1,2}, \tau_{2,2}$），拟合过程可能陷入局部最优。实际工程中常采用预设参数表而非实时拟合。

### 3. 高频分量与数值稳定性

Heidler 函数的波前部分包含丰富的高频分量（波前 0.25 μs 对应频率分量可达 ~1 MHz）。在 EMT 仿真中，若时间步长 $\Delta t$ 过大（如 $\Delta t > T_f/10$），会引入数值振荡和相位误差。建议 $\Delta t \leq 0.025$ μs（后续回击）或 $\Delta t \leq 0.1$ μs（首回击）。

### 4. 极性效应

实测数据显示，正极性回击电流的波前通常比负极性更平缓（正极性 $T_f$ 中值约 15 μs，负极性约 10 μs）。标准 Heidler 函数未区分极性，在精确极性敏感分析中需引入极性修正因子。

### 5. 通道阻抗效应

原始 Heidler 函数假设雷电流在通道底部测量，未考虑通道阻抗对波形的衰减和畸变。实际雷击杆塔时，电流从杆塔顶部注入，通道阻抗会导致波前展宽和峰值降低。Yamanaka et al. (2021) 的杆塔等效电路模型指出，通道效应可使峰值降低 10–30%。

## 量化性能边界

| 来源 | 验证场景 | 关键数据 |
|------|---------|---------|
| Heidler 1985 | 原始公式提出 | 解析可微，闭式导数，适用于单峰雷电流波形拟合 |
| CIGRE WG 33-01 1991 | Mount San Salvatore 实测统计 | 首回击峰值中值 31.1 kA，波前 3.83 μs，陡度 24.3 kA/μs；后续回击峰值 13.5 kA，波前 0.5 μs，陡度 80 kA/μs |
| Visacro et al. 2004 | Morro do Cachimbo 实测 | 负地闪峰值 16 kA，上升时间 0.6 μs，50% 衰减时间 16.6 μs，最大陡度 29.6 kA/μs |
| De Conti & Visacro 2007 | 双 Heidler 函数叠加拟合 | 双峰波形拟合误差 < 5%，2 函数即可再现凹陷特征 |
| Schroeder et al. 2018 | 138 kV 线路雷击仿真 | 首回击和后续回击波形通过 Heidler 叠加复现，杆塔顶部 GPR 峰值差异显著（频率相关土壤模型下 GPR 降低 45–80%） |
| Yin et al. 2023 | Y 型复合杆塔雷击响应 | CIGRE 波形参数（Tf=3.83 μs, Tt=77.5 μs, Icrest=31.1 kA）用于闪络临界电流分析，波前敏感性分析显示 Tf 从 1.2 μs 到 8 μs 变化时闪络电压曲线显著偏移 |
| De Conti 2020 | 三相紧凑配电网感应过电压 | Heidler 函数叠加拟合实测电流波形，16 kA 峰值，0.6 μs 上升，29.6 kA/μs 最大陡度，与 Morro do Cachimbo 数据吻合 |
| IEC 62305 | 标准雷电冲击波形 | 10/350 μs（直击雷）和 0.25/100 μs（后续回击）波形参数，对应 $\tau_1 \approx 1.25$ μs, $\tau_2 \approx 50$ μs 和 $\tau_1 \approx 0.031$ μs, $\tau_2 \approx 14.4$ μs |

## 适用边界与选择指南

### 适用条件

- **下行负地闪**：Heidler 函数最初针对下行负地闪标定，对正极性闪电需修正参数
- **单回击或后续回击**：单个 Heidler 函数适用于波形平滑的后续回击
- **标准工程评估**：IEC 62305 和 IEEE 1243 标准推荐的雷电防护评估
- **EMT 仿真输入源**：PSCAD/EMTDC、MATLAB/Simulink 等 EMT 程序的标准电流源模块

### 失效边界

- **上行闪电**：上行闪电电流波形与下行闪电不同，Heidler 函数不适用
- **云内放电**：云内闪电电流波形较平缓，峰值通常 < 10 kA，波前 > 100 μs
- **多回击叠加**：连续多回击（3 次以上）的复杂波形需更复杂的叠加模型
- **通道阻抗显著场景**：高杆塔（> 50 m）或长接地极场景，通道效应不可忽略
- **极性敏感分析**：正极性闪电的波前比负极性更平缓，标准参数不适用

### 方法选择指南

| 应用场景 | 推荐形式 | 理由 |
|---------|---------|------|
| 后续回击仿真（平滑波形） | 单 Heidler 函数 | 单函数即可精确拟合，计算开销最低 |
| 首回击仿真（多峰/凹陷） | 双 Heidler 函数叠加 | De Conti & Visacro 2007 方法，拟合误差 < 5% |
| 标准绝缘配合（IEC 62305） | 10/350 μs 参数 | 直击雷保护等级 I 标准波形 |
| 快速敏感性分析 | CIGRE PSCAD 模块 | 参数预封装，Tf/Tt 可调 |
| 精确极性分析 | 极性修正 Heidler | 需引入正极性参数修正因子 |

## 相关方法

- [[lightning-transient-analysis]] — 雷击暂态分析
- [[lightning-overvoltage]] — 雷击过电压
- [[switching-transient]] — 操作过电压（对比雷电波 vs 操作波）
- [[insulation-coordination]] — 绝缘配合
- [[grounding-system-model]] — 接地系统模型
- [[surge-arrester-model]] — 避雷器模型
- [[corona-effect-modeling]] — 电晕效应建模（雷电波传播中的电晕衰减）
- [[earth-return-impedance]] — 地回路阻抗（雷电流泄放中的大地效应）
- [[transmission-line-model]] — 输电线路模型
- [[bergeron-model]] — 贝杰龙行波模型

## 来源论文

- **Heidler, F. (1985)** — *Traveling Current Source Model for LEMP Calculation*. Proceedings of the 7th International Conference on Lightning Protection, Planegg-Martinsried, Germany. 原始提出 Heidler 函数，用于雷电电磁脉冲（LEMP）计算的行电流源模型。
- **CIGRE Working Group 33-01 (1991)** — *Guide to Procedures for Estimating the Lightning Performance of Transmission Lines*. Study Committee 33. 基于 Mount San Salvatore 实测数据统计首回击和后续回击的电流波形参数，定义 CIGRE 标准波形。
- **De Conti, A. & Visacro, S. (2007)** — *Analytical representation of single- and double-peaked lightning current waveforms*. IEEE Transactions on Electromagnetic Compatibility, 49(2), 448–451. 提出多 Heidler 函数叠加方法，拟合单峰和双峰雷电流波形，再现实测凹陷特征。
- **Visacro, S. et al. (2004)** — *Statistical analysis of lightning current parameters: measurements at Morro do Cachimbo station*. Journal of Geophysical Research, 109(D01105). 巴西 Morro do Cachimbo 观测站的实测负地闪电流统计数据，为 Heidler 参数标定提供实证基础。
- **IEC 62305** — *Protection against lightning*. International Electrotechnical Commission standard. 定义标准雷电冲击电流波形（10/350 μs 和 0.25/100 μs）及参数范围。
- **IEEE Std. 1243 (1997)** — *IEEE Guide for Improving the Lightning Performance of Transmission Lines*. 输电线路雷电性能估算标准，推荐 Heidler 函数作为雷电电流源模型。
- **Schroeder, M.A.O. et al. (2018)** — *Evaluation of the impact of different frequency dependent soil models on lightning overvoltages*. Electric Power Systems Research, 159, 40–49. 在 138 kV 线路上使用 Heidler 叠加波形仿真首回击和后续回击，评估土壤频变模型对 GPR 和绝缘子过电压的影响。
- **Yin, K. et al. (2023)** — *Lightning transient response of bifurcation structure pylon and its empirical expression with high accuracy*. International Journal of Electrical Power and Energy Systems, 148, 108967. 使用 CIGRE 波形参数（Tf=3.83 μs, Tt=77.5 μs）进行 Y 型复合杆塔闪络临界电流分析，波前敏感性分析。
- **De Conti, A. (2020)** — *Lightning-induced voltage analysis on a three-phase compact distribution line considering different cable configurations*. Electric Power Systems Research, 187, 106429. 使用双 Heidler 函数叠加拟合 Morro do Cachimbo 实测波形，计算紧凑配电网感应过电压。

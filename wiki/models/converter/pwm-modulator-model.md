---
title: "PWM调制器 (PWM Modulator)"
type: model
tags: [pwm, modulator, power-electronics, switching, carrier, spwm, svpwm]
created: "2026-04-30"
updated: "2026-05-19"
---

# PWM调制器 (PWM Modulator)


## 定义与概述

PWM（脉冲宽度调制）调制器是电力电子变换器EMT仿真的核心控制环节，通过调制载波与参考波的比较产生开关信号，控制功率器件的通断。本模型涵盖正弦PWM（SPWM）、空间矢量PWM（SVPWM）、特定谐波消除PWM（SHEPWM）等调制策略，适用于两电平/多电平变换器的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 将连续参考信号转换为离散开关信号
- 控制输出电压/电流的平均值
- 决定输出波形质量和谐波特性
- 影响变换器损耗和效率

**PWM类型**:
| 类型 | 调制方式 | 优点 | 缺点 | 应用 |
|------|----------|------|------|------|
| SPWM | 正弦波调制 | 实现简单 | 电压利用率低 | 通用逆变器 |
| SVPWM | 空间矢量 | 电压利用率高15% | 计算复杂 | 电机驱动 |
| THIPWM | 三次谐波注入 | 电压利用率高 | 谐波增加 | 三相系统 |
| SHEPWM | 特定谐波消除 | 低开关损耗 | 离线计算 | 大功率 |
| DPWM | 不连续PWM | 减少开关损耗 | 谐波稍大 | 高效率应用 |

### 1.2 调制原理

**基本结构**:
```
  参考波 v_ref
       │
       ▼
    ┌──┴──┐    比较    ┌──────┐
    │     ├─⊕──────→│ 开关 │──→ 输出
    │载波 │         │ 信号 │
    │ v_c│←────────┘      └──────┘
    └──┬──┘
       │
    三角波/锯齿波
```

**调制比定义**:
- 幅值调制比：$m_a = \frac{V_{ref,peak}}{V_{c,peak}}$
- 频率调制比：$m_f = \frac{f_c}{f_{ref}}$

### 1.3 运行激励

**输入信号**：
- 参考电压：三相或单相正弦参考
- 直流母线电压：$V_{dc}$
- 调制比：$0 \leq m_a \leq 1.15$（取决于调制方式）
- 载波频率：$f_c = 1-20$ kHz

**输出信号**：
- 开关信号：$S \in \{0, 1\}$ 或 $\{-1, 0, 1\}$
- 占空比：$d = \frac{t_{on}}{T_s}$
- 输出电压：$v_{out} = S \cdot V_{dc}$

**性能指标**：
- THD：总谐波失真
- WTHD：加权谐波失真
- 开关损耗：与开关频率和电流相关

## 2. 物理模型与数学描述

### 2.1 正弦PWM（SPWM）

#### 2.1.1 双极性SPWM

**两电平变换器**:
$$v_{ao} = \begin{cases}
+\frac{V_{dc}}{2}, & v_{ref} > v_c \\
-\frac{V_{dc}}{2}, & v_{ref} < v_c
\end{cases}$$

**占空比计算**:
$$d = \frac{1 + m_a \sin(\omega t)}{2}$$

**输出电压基波**:
$$V_{1,rms} = \frac{m_a V_{dc}}{2\sqrt{2}}$$

**线性调制范围**: $0 \leq m_a \leq 1$

#### 2.1.2 单极性SPWM

**半桥变换器**:
$$v_{ao} = \begin{cases}
+V_{dc}, & v_{ref} > v_c \text{ 且 } v_{ref} > 0 \\
0, & v_{ref} < v_c \text{ 且 } v_{ref} > 0 \\
0, & v_{ref} > -v_c \text{ 且 } v_{ref} < 0 \\
-V_{dc}, & v_{ref} < -v_c \text{ 且 } v_{ref} < 0
\end{cases}$$

**优点**：等效开关频率加倍，谐波特性更好。

### 2.2 三次谐波注入PWM（THIPWM）

**注入三次谐波**:
$$v_{ref}' = v_{ref} - \frac{\max(v_a, v_b, v_c) + \min(v_a, v_b, v_c)}{2}$$

或注入15%三次谐波：
$$v_{ref}' = m_a V_c \left[\sin(\omega t) + \frac{1}{6}\sin(3\omega t)\right]$$

**电压利用率**:
$$V_{1,rms} = \frac{1.15 V_{dc}}{2\sqrt{2}}$$

**线性范围**: $0 \leq m_a \leq 1.15$

### 2.3 空间矢量PWM（SVPWM）

#### 2.3.1 电压矢量定义

**基本电压矢量**:
$$\vec{V} = \frac{2}{3}(v_a + v_b e^{j120°} + v_c e^{j240°})$$

**两电平变换器**:
| 状态 | $S_a$ | $S_b$ | $S_c$ | 矢量 | 幅值 |
|------|-------|-------|-------|------|------|
| V0 | 0 | 0 | 0 | $\vec{V}_0$ | 0 |
| V1 | 1 | 0 | 0 | $\vec{V}_1$ | $2V_{dc}/3$ |
| V2 | 1 | 1 | 0 | $\vec{V}_2$ | $2V_{dc}/3$ |
| V3 | 0 | 1 | 0 | $\vec{V}_3$ | $2V_{dc}/3$ |
| V4 | 0 | 1 | 1 | $\vec{V}_4$ | $2V_{dc}/3$ |
| V5 | 0 | 0 | 1 | $\vec{V}_5$ | $2V_{dc}/3$ |
| V6 | 1 | 0 | 1 | $\vec{V}_6$ | $2V_{dc}/3$ |
| V7 | 1 | 1 | 1 | $\vec{V}_7$ | 0 |

**空间矢量图**:
```
          V3(010)
            │
    V2(110)─┼─V4(011)
           /│\
          / │ \
    V1(101)│V5(101)
            │
          V6(100)
```

#### 2.3.2 矢量作用时间计算

**扇区判断**: 根据参考电压角度确定所在扇区。

**作用时间计算**（以第一扇区为例）:
$$\begin{cases}
T_1 = \frac{\sqrt{3} T_s}{V_{dc}} \left(\frac{\sqrt{3}}{2}v_\alpha - \frac{1}{2}v_\beta\right) \\
T_2 = \frac{\sqrt{3} T_s}{V_{dc}} v_\beta \\
T_0 = T_s - T_1 - T_2
\end{cases}$$

**过调制处理**:
- 线性区：$T_1 + T_2 \leq T_s$
- 过调制：按比例缩小作用时间

**电压利用率**:
$$V_{1,rms} = \frac{V_{dc}}{\sqrt{6}} \approx \frac{1.15 V_{dc}}{2\sqrt{2}}$$

### 2.4 载波波形分析

#### 2.4.1 三角载波

**双沿调制**:
$$v_c(t) = \frac{2}{T_s}(t \mod T_s) - 1$$

**谐波特性**:
- 载波频率倍数处的谐波
- 边带谐波：$f_{side} = mf_c \pm nf_{ref}$

#### 2.4.2 锯齿载波

**单沿调制**:
$$v_c(t) = \frac{t \mod T_s}{T_s}$$

**特点**:
- 非对称调制
- 偶次谐波增加
- 较少使用

### 2.5 谐波分析

#### 2.5.1 双极性SPWM谐波

**Bessel函数描述**:
$$v_{ao}(t) = \frac{V_{dc}}{2} m_a \sin(\omega_{ref} t) + \text{谐波项}$$

**主要谐波频率**:
- $f_c \pm 2f_{ref}$
- $2f_c \pm f_{ref}$
- $2f_c \pm 3f_{ref}$

**THD近似**:
$$THD \approx \sqrt{\sum_{n=2}^{\infty} \left(\frac{V_n}{V_1}\right)^2} \approx 80\% \text{（单相）}$$

#### 2.5.2 SVPWM谐波优势

相比SPWM：
- 相同开关频率下THD降低约30%
- 电压利用率提高15%
- 更适合电机驱动

## 3. EMT仿真模型

### 3.1 自然采样法

**直接比较**:
在每个仿真步长比较参考值和载波值：
$$S(t) = \begin{cases}
1, & v_{ref}(t) > v_c(t) \\
0, & v_{ref}(t) < v_c(t)
\end{cases}$$

**缺点**:
- 需要极小步长捕捉开关时刻
- 仿真效率低

### 3.2 规则采样法

**单更新（Single-update）**:
在每个载波周期更新一次占空比：
$$d[k] = \frac{v_{ref}(kT_c)}{V_{c,peak}}$$

**双更新（Double-update）**:
在三角波的峰值和谷值都更新占空比，等效开关频率加倍。

### 3.3 平均模型

**占空比模型**:
忽略开关细节，直接使用占空比：
$$\bar{v}_{ao} = d \cdot V_{dc} = m_a V_{dc} \sin(\omega t)$$

**适用场景**:
- 系统级仿真
- 控制策略验证
- 稳态分析

**限制**:
- 无法分析开关谐波
- 无法分析开关损耗

### 3.4 多电平PWM

#### 3.4.1 NPC三电平SPWM

**载波层叠（PD）**:
```
      v_c1 (上)
      ────────
      
      v_ref
      
      ────────
      v_c2 (下)
```

**输出电平**: $+V_{dc}/2$, $0$, $-V_{dc}/2$

#### 3.4.2 MMC载波移相（CPS-PWM）

**N个子模块**:
- 载波相位差：$360°/N$
- 等效开关频率：$N \cdot f_c$
- 谐波抵消效果显著

**载波生成**:
$$v_{c,k} = \sin(2\pi f_c t + \frac{2\pi(k-1)}{N})$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**SPWM调制器**:
```fortran
! SPWM调制器
REAL Vref(3)      ! 三相参考电压
REAL Vc           ! 载波幅值
REAL Vtri         ! 三角波值
INTEGER S(3)      ! 开关信号

! 生成三角载波（0到1）
Vtri = ABS(2.0 * MOD(TIME * FC, 1.0) - 1.0)

! 比较产生开关信号
DO I = 1, 3
  IF (Vref(I) > Vtri) THEN
    S(I) = 1
  ELSE
    S(I) = 0
  END IF
END DO
```

**SVPWM实现**:
```fortran
! SVPWM调制
REAL Valpha, Vbeta    ! 参考电压在alpha-beta坐标系
REAL Vdc              ! 直流电压
REAL Ts               ! 开关周期
REAL T1, T2, T0       ! 矢量作用时间
INTEGER Sector        ! 扇区

! Clarke变换
Valpha = (2.0*Va - Vb - Vc) / 3.0
Vbeta = (Vb - Vc) / SQRT(3.0)

! 扇区判断
Angle = ATAN2(Vbeta, Valpha)
Sector = INT((Angle + PI) / (PI/3.0)) + 1

! 计算作用时间
X = SQRT(3.0) * Ts * Vbeta / Vdc
Y = Ts * (1.5*Valpha - SQRT(3.0)*Vbeta/2.0) / Vdc
Z = Ts * (-1.5*Valpha - SQRT(3.0)*Vbeta/2.0) / Vdc

! 根据扇区选择
SELECT CASE (Sector)
  CASE (1)
    T1 = -Z
    T2 = X
  CASE (2)
    T1 = Z
    T2 = Y
  ...
END SELECT

! 过调制处理
IF (T1 + T2 > Ts) THEN
  T1 = T1 * Ts / (T1 + T2)
  T2 = T2 * Ts / (T1 + T2)
END IF

T0 = Ts - T1 - T2
```

### 4.2 MATLAB/Simulink实现

**SPWM模块**:
```matlab
% PWM Generator
pwm = pwmGenerator('CarrierFreq', 10e3, 'SampleTime', 1e-6);

% 或自定义实现
fc = 10e3;  % 载波频率
fs = 100e6; % 仿真步长对应的采样率
t = 0:1/fs:0.1;

% 三角载波
carrier = sawtooth(2*pi*fc*t, 0.5);

% 参考波
Vref = 0.8 * sin(2*pi*50*t);

% PWM信号
pwm_signal = double(Vref > carrier);
```

**SVPWM实现**:
```matlab
function [Sa, Sb, Sc] = svpwm(Vabc, Vdc, Ts)
    % Clarke变换
    Valpha = (2*Vabc(1) - Vabc(2) - Vabc(3)) / 3;
    Vbeta = (Vabc(2) - Vabc(3)) / sqrt(3);
    
    % 扇区判断
    Vref1 = Vbeta;
    Vref2 = sqrt(3)/2 * Valpha - 0.5 * Vbeta;
    Vref3 = -sqrt(3)/2 * Valpha - 0.5 * Vbeta;
    
    N = sign(Vref1) + 2*sign(Vref2) + 4*sign(Vref3);
    sector = [0; 4; 6; 2; 3; 1; 5]; % 扇区映射
    Sector = sector(N + 4);
    
    % 计算作用时间
    X = sqrt(3) * Ts * Vbeta / Vdc;
    Y = Ts * (1.5*Valpha + sqrt(3)*Vbeta/2) / Vdc;
    Z = Ts * (-1.5*Valpha + sqrt(3)*Vbeta/2) / Vdc;
    
    % 根据扇区选择
    switch Sector
        case 1, T1 = -Z; T2 = X;
        case 2, T1 = Z; T2 = Y;
        case 3, T1 = X; T2 = -Y;
        case 4, T1 = -X; T2 = Z;
        case 5, T1 = -Y; T2 = -Z;
        case 6, T1 = Y; T2 = -X;
    end
    
    % 过调制处理
    if T1 + T2 > Ts
        T1 = T1 * Ts / (T1 + T2);
        T2 = T2 * Ts / (T1 + T2);
    end
    T0 = Ts - T1 - T2;
    
    % 生成开关信号（七段式）
    Ta = (T1 + T2 + T0/2) / Ts;
    Tb = (T2 + T0/2) / Ts;
    Tc = T0/2 / Ts;
    
    % 输出开关状态
    Sa = Ta > 0.5;
    Sb = Tb > 0.5;
    Sc = Tc > 0.5;
end
```

### 4.3 FPGA实现

**Verilog代码**:
```verilog
module pwm_generator (
    input clk,
    input reset,
    input [15:0] duty,      // 占空比 (0-65535)
    input [15:0] period,    // 周期计数
    output reg pwm_out
);

    reg [15:0] counter;
    
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            counter <= 16'd0;
            pwm_out <= 1'b0;
        end else begin
            if (counter >= period - 1)
                counter <= 16'd0;
            else
                counter <= counter + 1'b1;
                
            pwm_out <= (counter < duty);
        end
    end
endmodule
```

## 5. 典型参数参考

### 5.1 调制参数

| 应用 | 载波频率 | 调制比 | 开关频率 | 输出频率 |
|------|----------|--------|----------|----------|
| 电机驱动 | 2-10 kHz | 0.8-1.0 | 2-10 kHz | 0-200 Hz |
| 光伏逆变器 | 10-20 kHz | 0.9-1.0 | 10-20 kHz | 50/60 Hz |
| HVDC | 1-2 kHz | 0.9-1.15 | 1-2 kHz | 50/60 Hz |
| 高频电源 | 50-100 kHz | 0.5-0.9 | 50-100 kHz | DC |

### 5.2 谐波特性比较

| 调制方式 | 基波幅值 | THD | WTHD | 开关损耗 |
|----------|----------|-----|------|----------|
| SPWM | 0.5$m_a V_{dc}$ | ~80% | ~2% | 基准 |
| THIPWM | 0.577$V_{dc}$ | ~75% | ~1.8% | 基准 |
| SVPWM | 0.577$V_{dc}$ | ~75% | ~1.8% | 基准 |
| DPWM | 0.577$V_{dc}$ | ~85% | ~2.2% | -33% |

### 5.3 死区时间

| 应用 | 死区时间 | 影响 |
|------|----------|------|
| IGBT (600V) | 1-3 μs | 小 |
| IGBT (1700V) | 3-5 μs | 中 |
| MOSFET | 0.5-1 μs | 小 |
| SiC MOSFET | 0.2-0.5 μs | 很小 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[vsc-model]] — 两电平换流器
- [[mmc-model]] — 多电平换流器
- [[igbt-model]] — 开关器件

### 6.2 相关方法
- [[average-value-model]] — 忽略开关细节的平均值模型
- [[multirate-method]] — 调制与电路不同步长

### 6.3 相关主题
- 谐波分析 - PWM谐波特性
- 死区补偿 - 死区效应补偿
- 过调制 - 过调制区控制

## 7. 适用边界与限制

### 7.1 适用条件
- **调制比**: $0 \leq m_a \leq 1.15$（线性区）
- **载波频率**: 通常1-20 kHz
- **调制比**: $m_f \geq 21$（减少谐波）
- **开关频率**: 远高于基波频率

### 7.2 模型限制
- **死区效应**: 未建模死区引起的电压损失
- **器件非线性**: 未考虑开关瞬态
- **最小脉宽**: 极短脉宽可能无法实现
- **共模电压**: 产生高频共模电压

### 7.3 量化性能边界

PWM 调制器的 EMT 仿真精度取决于载波频率、调制策略和离散化方法。不同建模精度层次对应不同的计算代价和适用场景，以下汇总可引用的量化数据：

**全开关模型（Detailed Switching Model）**：保留每个 IGBT/二极管的开通关断过程，理论上精度最高，但受以下约束限制：开关频率 2-20 kHz 时，时间步长需 ≤ 1 μs（Nyquist 约束的 2-10 倍以捕捉上升沿）；每个开关周期内包含 2 次开关事件，每次事件需触发局部截断误差校正。以 401 电平 MMC 为例，每个桥臂含 200 个子模块，每个子模块含 2 个开关器件，全开关模型每秒需模拟 401×6×f_sw ≈ 4.8-48 亿次开关事件，在 CPU 上单步仿真耗时可达数十毫秒。

**调制指数等效建模**：Bahirat (2015) 在风电场 MMC-HVDC EMT 建模中验证了调制指数等效方法的有效性。通过等效变换将调制波直接映射为桥臂平均电压，降低计算复杂度的同时保持了调制特性在全频段的准确性。该方法在开关频率附近的精度损失 < 2%，但计算速度提升 10-50 倍（取决于子模块数量）。

**SPWM 直接接口 AVM**：Ebrahimi (2023) 提出了 SPWM 变流器的直接接口平均值模型，消除了传统 AVM 在开关频率附近的精度损失。在载波频率 ± 2 倍基波频率范围内（f_c ± 2f_ref），直接接口 AVM 的电压误差 < 0.3%，与全开关模型在主要谐波频率处吻合良好，适用于需要 1-5 ms 观测窗口的系统级 EMT 分析。

**NLM 等效模型**：Zhao (2023) 对 MMC 的最近电平调制（NLM）进行了闭环电压控制等效建模，将调制波占空比分解为稳态分量和直流电压均衡闭环修正分量。在 0-500 Hz 范围内误差小于 0.5%，在 500 Hz-2 kHz 范围内误差 < 5%，验证了等效模型在低频和中频段的精度与毫秒级开关模型一致。Yu (2014) 的查找表 NLM 实现将子模块穷举排序替换为解析查表，加速比达 5000 倍。

**SVPWM 性能优势量化**：SVPWM 相比 SPWM 电压利用率提高约 15%（从 0.5 Vdc 基波幅值提升至 0.577 Vdc），这是因为空间矢量合成允许在直流母线电压利用上超过线性调制极限。在相同开关频率下，SVPWM 的 THD 较 SPWM 降低约 30%（SPWM THD ≈ 80% → SVPWM THD ≈ 55-60%），但 SVPWM 的扇区判断和矢量时间计算在每个开关周期需 12-20 次三角函数运算，比 SPWM 的简单比较多消耗 5-10% 的 CPU 时间。

**MMC 载波移相（CPS-PWM）量化**：对 N 个子模块的 MMC，载波相位差 360°/N 导致等效开关频率提升 N 倍。N=200 时，等效开关频率为 200×f_c，基波频率处（50 Hz）的谐波簇被展宽并相互抵消，THD 从单载波的 ~50% 降至 < 5%。但代价是每个子模块需独立追踪其载波相位，总 CPU 消耗为单载波模型的 N 倍。

**数据缺口声明**：不同 PWM 策略（SPWM、SVPWM、SHEPWM、DPWM）在 EMT 仿真中精度和效率的量化对比缺乏统一基准，表格中的数值来自各自论文的孤立测试。不同采样方法（自然采样、规则采样、双更新）对仿真精度的影响缺少独立评估；自然采样和规则采样的精度差异在 0.1% 以内（据工程经验，未找到标准化文献数据）。

## 相关模型
- [[vsc-model]] — 两电平换流器
- [[mmc-model]] — 多电平换流器
- [[igbt-model]] — 开关器件
- [[coordinate-transformation-model]] — SVPWM矢量计算

## 相关主题
- [[harmonic-analysis]] — PWM谐波特性
- [[real-time-simulation]] — 调制器实时实现

---

## 来源论文
- Gao 等 (2014) — 基于平均化理论的PWM变流器EMT快速仿真方法（GPU并行，6×加速）
- Zhao 等 (2023) — MMC最近电平调制等效模型（0-500 Hz误差<0.5%，毫秒级精度）
- Ebrahimi (2023) — SPWM直接接口AVM（消除开关频率附近精度损失）
- Bahirat (2015) — 调制指数等效方法（风电场MMC-HVDC验证）
- Yu (2014) — 查找表NLM实现（5000×加速）
- [[average-value-model]] 相关平均模型论文见该页面

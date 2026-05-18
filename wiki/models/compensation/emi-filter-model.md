---
title: "EMI滤波器 (EMI Filter)"
type: model
tags: [emi-filter, filter, common-mode, differential-mode, conducted-emission, emc]
created: "2026-04-30"
updated: "2026-05-18"
---

# EMI滤波器 (EMI Filter)

## 定义

EMI滤波器（Electromagnetic Interference Filter）是电力电子系统中用于抑制电磁干扰的无源/有源网络，通过衰减传导干扰信号确保设备满足EMC（Electromagnetic Compatibility）标准。其核心功能包括：

- **共模干扰（CM）衰减**：抑制相线/中性线对地共模噪声
- **差模干扰（DM）衰减**：抑制相间差模噪声
- **阻抗失配反射**：在噪声传播路径上形成高阻抗失配，反射噪声源
- **敏感设备保护**：为逆变器/变频器等电力电子设备提供干净电源

在EMT仿真中，EMI滤波器模型用于分析开关噪声传播路径、评估滤波性能、设计阻尼特性。典型应用场景包括：变频器驱动系统、光伏逆变器并网、电动汽车充电器、工业开关电源。

## EMT中的作用

电力电子变换器是系统中最主要的EMI噪声源。开关动作产生的高速$dV/dt$和$dI/dt$通过功率回路耦合到电网侧，产生传导EMI。EMI滤波器在EMT仿真中承担三类角色：

**1. 噪声注入点建模**：作为逆变器输出端的后处理环节，EMI滤波器需要与开关器件模型（如[[igbt-model]]）联动，仿真噪声从开关节点经滤波器传播至电网的过程。

**2. 滤波性能评估**：通过FFT频谱分析（仿真波形加窗后进行傅里叶变换），对比滤波器输入/输出频谱，定量评估插入损耗。

**3. 阻尼设计验证**：检验滤波器与负载阻抗的交互效应，避免因阻尼不足引发谐振（尤其是两级LC滤波器的高阻抗节点）。

**关键挑战**：EMI滤波器在EMT中的核心问题是**噪声源等效建模**——实际开关噪声是宽频带脉冲，精确建模需要详细开关瞬态数据；次要问题是**无源元件高频特性**（集总参数模型在10 MHz以上失效，需采用[[frequency-dependent-modeling|频率相关建模]]）。

## 物理模型与数学描述

### 1.1 二阶LC低通滤波器

#### 传递函数与频率特性

标准LC低通滤波器的传递函数为：

$$H(s) = \frac{1}{s^2LC + s\frac{L}{R_L} + 1}$$

截止频率：

$$f_c = \frac{1}{2\pi\sqrt{LC}}$$

特性阻抗：

$$Z_0 = \sqrt{\frac{L}{C}}$$

阻尼系数：

$$\zeta = \frac{1}{2R_L}\sqrt{\frac{L}{C}}$$

**幅度响应**：

$$|H(j\omega)| = \frac{1}{\sqrt{(1-\omega^2LC)^2 + (\omega L/R_L)^2}}$$

**衰减斜率**：
- 低于$f_c$：0 dB/decade
- 高于$f_c$：-40 dB/decade（理想二阶）

#### 阻尼类型与选择

欠阻尼（$\zeta < 1$）在截止频率附近产生谐振峰，适用于需要快速阶跃响应的场景；过阻尼（$\zeta > 1$）则平滑无峰，但响应慢。工程设计通常取$\zeta = 0.707$（Butterworth响应）以获得最大平坦通带。

### 1.2 共模滤波器模型

#### 共模等效电路

共模噪声通过相线和中性线的对称耦合传播到地。共模电感（CM Choke）利用双线绕制结构，对共模电流呈现高阻抗，而对差模电流几乎无阻抗（因为磁通相互抵消）。

**共模阻抗**：

$$Z_{CM}(s) = sL_{CM} + \frac{1}{sC_Y}$$

**共模谐振频率**：

$$f_{CM} = \frac{1}{2\pi\sqrt{L_{CM}C_Y}}$$

其中$L_{CM}$为共模电感量，$C_Y$为Y电容（线对地电容）。

#### 磁芯损耗模型

实际共模电感包含磁芯损耗和绕组寄生电容：

$$Z_{CM}(s) = R_{core} + sL_{CM} + \frac{1}{sC_{par}}$$

其中：
- $R_{core}$：磁芯损耗等效电阻，反映磁滞损耗和涡流损耗
- $C_{par}$：绕组寄生电容，由线圈匝间电容和层间电容构成
- $L_{CM}$：共模电感量

### 1.3 差模滤波器模型

#### π型滤波器

差模滤波通常采用π型结构（电容-电感-电容）：

$$H_{DM}(s) = \frac{1}{s^2L_{DM}C_{eq} + s\frac{L_{DM}}{R_L} + 1}$$

其中等效电容：$C_{eq} = C_{X1} + C_{X2} + C_m$

$C_{X1}$、$C_{X2}$为X电容（线间电容），$C_m$为寄生互容。

#### 漏感利用

共模电感的漏感（即耦合系数$k$不为1的剩余部分）可作为差模电感使用：

$$L_{DM} = (1-k)L_{CM}$$

其中耦合系数$k$通常为0.98–0.995（高耦合系数意味着漏感仅$2\%$–$5\%$）。

### 1.4 高阶滤波器

#### Butterworth响应

N阶Butterworth滤波器的幅度响应为：

$$|H(j\omega)| = \frac{1}{\sqrt{1+(\omega/\omega_c)^{2N}}}$$

其特点是在通带内无纹波，最大平坦。

#### 级联衰减

两级LC级联时，总衰减为各级衰减的线性叠加（dB单位）：

$$A_{total} = A_1 + A_2 \quad \text{(dB)}$$

### 1.5 有源EMI滤波器

#### 电流补偿型

有源滤波器通过注入抵消电流来抑制噪声：

$$i_{cancel} = -G \cdot i_{noise}$$

残余电流：

$$i_{res} = i_{noise} + i_{cancel} = i_{noise}(1-G)$$

其中$G$为环路增益（>$1$时有效抑制）。

#### 电压补偿型

$$v_{inj} = -G \cdot v_{noise}$$

有效频率范围受运放带宽限制（通常$10$ kHz–$1$ MHz）。

## EMT中的噪声传播路径

### 2.1 噪声耦合机制

在VSC系统中，EMI噪声从功率器件传播到电网有三条主要路径：

**路径A（传导路径）**：开关节点电压通过DC-Link电容和交流滤波电容耦合到电网侧。这是低频噪声（150 kHz–1 MHz）的主要传播方式。DC-Link电容的ESR和ESL决定了高频旁路能力。

**路径B（磁场耦合）**：开关电流在功率回路周围产生磁场，通过空间耦合到控制电路和传感器线路。此路径在高频（$>$10 MHz）占主导。

**路径C（地环路）**：多个设备共地时，开关电流通过地阻抗返回，形成地环路噪声。

### 2.2 CM/DM耦合矩阵

CM和DM噪声在系统中并非完全解耦，存在通过寄生电容的耦合：

$$v_{CM} = \frac{v_1 + v_2}{2}, \quad v_{DM} = v_1 - v_2$$

实际系统中，CM电压通过$Y$电容与DM形成耦合网络。VSC逆变器的CM电压波动（由PWM零矢量时间不均衡引起）是CM噪声的主要来源。

### 2.3 开关噪声源等效

将开关节点电压等效为噪声源时，可用电压源叠加模型：

$$v_{noise}(t) = \sum_{n=1}^{N} V_n \sin(2\pi n f_{sw} t)$$

其中$V_n$为$n$次谐波幅值，与开关边沿的上升/下降时间（$\tau_{rise}$）密切相关：

$$V_n \propto \frac{1}{n}\left(1 - e^{-2\pi n f_{sw} \tau_{rise}}\right)$$

高速开关（SiC/GaN器件，$\tau_{rise}<5$ ns）产生的高频谐波可延伸至100 MHz以上。

## 量化性能边界

### 3.1 插入损耗评估

EMI滤波器性能的核心指标是插入损耗（Insertion Loss）：

$$IL_{dB} = 20\log_{10}\left|\frac{v_{without}}{v_{with}}\right|$$

典型值（150 kHz–30 MHz频段）：
| 滤波器类型 | 150 kHz | 1 MHz | 10 MHz | 30 MHz |
|-----------|---------|-------|--------|--------|
| 单级LC | 20 dB | 40 dB | — | — |
| 两级LC | 30 dB | 50 dB | 40 dB | — |
| CM共模滤波器 | — | 25 dB | 35 dB | 30 dB |
| π型DM滤波器 | 25 dB | 45 dB | 35 dB | — |

原文未报告可核验的数值结果。上述数据基于标准LC滤波器理论计算和典型工程经验值，不同拓扑的实际插入损耗可能偏差$\pm 10$ dB。

### 3.2 谐振风险

两级LC滤波器的高阻抗节点与后端高阻性负载交互时可能激发谐振：

$$f_{res} = \frac{1}{2\pi}\sqrt{\frac{1}{L_1C_1} + \frac{1}{L_2C_2}}$$

阻尼电阻$R_d$的推荐值（Butterworth设计）：

$$R_d = 2\sqrt{\frac{L_1}{C_1}} = 2\sqrt{\frac{L_2}{C_2}}$$

### 3.3 仿真步长约束

EMI滤波器的EMT仿真受高频特性约束。共模电感高频模型（$>$10 MHz）若采用集总参数，需要极小仿真步长：

$$\Delta t \leq \frac{1}{10 f_{max}} = \frac{1}{10 \times 30 \text{ MHz}} \approx 3.3 \text{ ns}$$

采用[[multirate-method|多速率方法]]时，EMI分析可用较大步长（$1$–$5$ μs），而开关瞬态用ns级步长。

## EMT仿真模型

### 3.1 离散化实现

LC滤波器的时域离散化（梯形法则）：

$$i_L[k+1] = i_L[k] + \frac{\Delta t}{L}(v_{in}[k] - v_C[k])$$

$$v_C[k+1] = v_C[k] + \frac{\Delta t}{C}i_L[k]$$

输出电压：

$$v_{out}[k+1] = v_C[k+1] + R_d \cdot i_L[k+1]$$

### 3.2 共模/差模分离

**共模电压**：

$$v_{CM} = \frac{v_L + v_N}{2}$$

**差模电压**：

$$v_{DM} = v_L - v_N$$

分离后分别通过独立滤波器，最后重构：

$$v_L^{out} = v_{CM}^{out} + \frac{v_{DM}^{out}}{2}, \quad v_N^{out} = v_{CM}^{out} - \frac{v_{DM}^{out}}{2}$$

### 3.3 EMI频谱分析

FFT频谱分析的仿真流程：

1. 时域仿真获取电压/电流波形
2. 加窗（Hanning或Hamming窗减少频谱泄漏）
3. FFT变换获取频谱
4. 施加CISPR准峰值检波器

**准峰值检波器参数**（CISPR 16-1-1）：

$$\tau_{charge} = 1 \text{ ms}, \quad \tau_{discharge} = 160 \text{ ms}$$

## 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**LC低通滤波器**：
```fortran
! 电感电流更新
I_L = I_L_OLD + DT/L * (V_IN - V_C)
! 电容电压更新
V_C = V_C_OLD + DT/C * I_L
! 阻尼电阻（可选）
IF (R_DAMP > 0) THEN
  I_R = V_C / R_DAMP
  I_C = I_L - I_R
  V_C = V_C_OLD + DT/C * I_C
END IF
```

**共模电感模型**：
```fortran
V_CM = (V_L + V_N) / 2.0
IF (ABS(I_CM) > I_SAT) THEN
  L_CM_EFF = L_CM * I_SAT / ABS(I_CM)  ! 饱和效应
ELSE
  L_CM_EFF = L_CM
END IF
I_CM = I_CM_OLD + DT/L_CM_EFF * (V_CM - V_CY)
V_CY = V_CY_OLD + DT/CY * I_CM
```

**EMI测量（CISPR频段）**：
```fortran
! 准峰值检波器
V_QP = V_QP_OLD + DT/TAU_CHARGE * (V_PEAK - V_QP_OLD)
IF (V_PEAK < V_QP) THEN
  V_QP = V_QP_OLD - DT/TAU_DISCHARGE * V_QP_OLD
END IF
```

### 4.2 MATLAB/Simulink实现

```matlab
function v_out = lc_filter(v_in, L, C, R, Ts)
    % 离散状态空间模型
    A = [0 -1/L; 1/C -1/(R*C)];
    B = [1/L; 0];
    Cmat = [0 1];
    D = 0;
    sys = ss(A, B, Cmat, D);
    sysd = c2d(sys, Ts, 'tustin');
    v_out = lsim(sysd, v_in);
end

function [cm, dm] = mode_separation(v1, v2)
    cm = (v1 + v2) / 2;  % 共模
    dm = v1 - v2;         % 差模
end

function [f, mag_dBuV] = emi_spectrum(v, Ts, window_type)
    N = length(v);
    if strcmp(window_type, 'hanning')
        w = hanning(N);
    else
        w = hamming(N);
    end
    V_fft = fft(v .* w);
    V_mag = abs(V_fft(1:N/2+1)) * 2 / N;
    f = (0:N/2) / (N * Ts);
    mag_dBuV = 20*log10(V_mag / 1e-6);
end
```

## 典型参数参考

### 5.1 单相逆变器EMI滤波器

| 参数 | 符号 | 典型值 | 说明 |
|------|------|--------|------|
| 共模电感 | $L_{CM}$ | 1–10 mH | 双线绕制，磁芯高磁导率 |
| Y电容 | $C_Y$ | 1–10 nF | 受漏电流限制（$<5$ mA） |
| X电容 | $C_X$ | 0.1–2 μF | 差模滤波，耐压需满足AC额定 |
| 差模电感 | $L_{DM}$ | 10–100 μH | 漏感利用或独立绕制 |
| 截止频率 | $f_c$ | 1–10 kHz | 低于开关频率（通常$<0.1 f_{sw}$） |
| 阻尼电阻 | $R_d$ | 1–10 Ω | Butterworth设计 |

### 5.2 三相变频器滤波器

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 共模电感 | $3 \times 10$ mH | 三相磁环或三相共模电感 |
| Y电容 | 10 nF/相 | 受总漏电流$<15$ mA限制 |
| X电容 | 4.7 μF | 线间连接 |
| 差模电感 | 50 μH/相 | 每相独立绕制 |

### 5.3 CISPR 11传导发射限值（B类设备）

| 频率范围 | 准峰值限值 | 平均值限值 |
|----------|------------|------------|
| 150 kHz–500 kHz | 66–56 dBμV（线性下降） | 56–46 dBμV |
| 500 kHz–5 MHz | 56 dBμV | 46 dBμV |
| 5 MHz–30 MHz | 60 dBμV | 50 dBμV |

## 相关主题与链接

### 相关模型

- [[igbt-model]] — 主要EMI噪声源，开关边沿高频谐波产生
- [[pwm-modulator-model]] — PWM调制产生的谐波频谱分析
- [[inductor-model]] — 共模电感高频建模，磁饱和特性
- [[capacitor-model]] — X/Y电容的ESR/ESL高频特性
- [[vsc-model]] — 典型EMI滤波器应用场景

### 相关方法

- [[frequency-dependent-modeling]] — 无源元件宽频特性（>10 MHz）
- [[multirate-method]] — EMI高频分析与系统级仿真的时间尺度分离

## 适用边界与限制

### 适用条件

- **频率范围**：传导干扰频段（9 kHz–30 MHz），超出此频段需考虑辐射EMI模型
- **线性区域**：无源元件工作在线性区（磁芯未饱和）
- **集总参数假设**：PCB走线长度$<\lambda/20$（约30 MHz以下成立）

### 失效边界

- **高频辐射**：>30 MHz时集总参数模型失效，需分布参数模型
- **非线性磁芯**：大电流导致磁芯饱和，共模电感量显著下降
- **温度影响**：磁芯材料参数（$B_{sat}$、损耗）随温度变化，$100°C$以上需补偿
- **寄生参数**：绕组间电容、PCB分布电感在高频下不可忽略（>$5$ MHz时需精确提取）

### 关键假设

1. CM和DM可解耦处理（实际通过寄生电容存在耦合）
2. 负载阻抗已知且恒定（失配会改变滤波器响应）
3. 磁芯为线性材料（弱信号假设）
4. PCB走线寄生参数以集总参数等效

### 开放问题

- 宽禁带器件（SiC/GaN）的高频开关（$\tau_{rise}<5$ ns）对EMI滤波器设计的量化影响尚缺乏系统性EMT建模研究
- 有源EMI滤波器的实时闭环控制EMT仿真实现尚无成熟方法
- 含磁芯饱和的非线性共模电感EMT模型精度有待提高
- PCB分布参数（走线电感、过孔阻抗）对EMI滤波器性能的定量影响尚需实验验证

## 参考标准

- **CISPR 11** — 工业、科学和医疗设备射频骚扰特性限值
- **CISPR 22/32** — 信息技术设备电磁兼容
- **IEC 60939** — 电磁干扰抑制用无源滤波器总规范
- **IEEE 519** — 谐波控制建议（电网侧谐波限值）

## 来源论文

> 注：本页面涉及的主题（EMI滤波器EMT建模）在EMT_LLM_Wiki的论文收集范围内无直接对应论文。上述内容基于EMT Wiki关联知识页中的EMI相关内容（[[igbt-model]]和[[inductor-model]]）和电力电子基础理论构建。量化数据基于理论计算和工程经验值，原文未报告可核验的独立数值实验数据。
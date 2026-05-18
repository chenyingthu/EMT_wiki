---
title: "继电保护 (Relay Protection)"
type: topic
tags: [protection, relay, fault, security, power-system, automation]
created: "2026-05-02"
updated: "2026-05-19"
---

# 继电保护 (Relay Protection)

## 定义与边界

继电保护是电力系统中利用测量、判据、逻辑和执行设备识别故障并隔离故障元件的安全自动化体系。它不是单一算法，也不是只由动作速度衡量的装置能力；保护是否有效取决于一次系统模型、故障场景、互感器和通信链路、整定规则、断路器动作以及保护配合。

在 EMT Wiki 中，本页是继电保护主题综合页。具体继电器或保护设备模型应阅读 [[protection-control-device]]、`[[distance-relay]]`、和 [[impedance-relay]]；保护算法如何在 EMT 中表达，应阅读 [[protection-relay-modeling]]。

## EMT 中的作用

EMT 仿真用于检查继电保护在快速暂态和非正弦波形下的动作边界，特别是：

- 故障初始角、故障阻抗、直流偏置和谐波对测量判据的影响。
- 线路、变压器、母线和换流器接口故障下的误动、拒动和选择性。
- 电力电子设备限流、PLL、直流故障和行波暂态对传统工频保护的挑战。
- 实时仿真和 HIL 中保护装置闭环测试的时序一致性。

## 主要分支与机制

继电保护在 EMT 建模中按信号处理链路组织，包含以下五类核心机制：

### 1. 过流与定时限保护

通过过流、欠压、零序、负序或频率偏差启动，适合配电和后备保护讨论，但需绑定定值和延时。核心判据为：

$$I_{\mathrm{rms}} > I_{\mathrm{pickup}} \quad \text{且} \quad t > t_{\mathrm{delay}}$$

反时限特性（IEC 标准反时限，$k=0.14$, $\alpha=0.02$）：

$$t_{\mathrm{op}} = \frac{0.14 \cdot T_{\mathrm{MS}}}{(I/I_{\mathrm{pickup}})^{0.02} - 1}$$

其中 $T_{\mathrm{MS}}$ 为时间倍数设定值。

### 2. 距离保护

以测量阻抗 $Z=V/I$ 或补偿后的相间/接地阻抗为判据，受故障电阻、互感、负荷电流和换流器电流限制影响。相间距离和接地距离（零序补偿）的阻抗计算：

$$Z_{\phi\phi} = \frac{V_{\phi\phi}}{I_{\phi\phi}}, \qquad Z_{\phi g} = \frac{V_{\phi}}{I_{\phi} + k_0 I_0}$$

其中 $k_0 = (Z_0 - Z_1)/3Z_1$ 为零序补偿系数。

### 3. 差动保护

比较保护区两端或多端电流，依赖同步、CT 饱和和制动特性。变压器涌流和外部故障穿越是常见边界。差动保护判据：

$$I_{\mathrm{diff}} = \left|\sum_{j=1}^{n} I_j\right|, \qquad I_{\mathrm{rest}} = \frac{1}{2}\sum_{j=1}^{n} |I_j|$$

动作条件：$I_{\mathrm{diff}} > k \cdot I_{\mathrm{rest}} + I_{\mathrm{min}}$，其中制动系数 $k$ 通常取 $0.2$~$0.5$，$I_{\mathrm{min}}$ 为最小动作电流。

二次谐波制动（防涌流）：$I_2/I_1 > k_{2nd}$，通常 $k_{2nd}=0.15$~$0.20$；五次谐波制动：$I_5/I_1 > k_{5th}$，通常 $k_{5th}=0.35$~$0.40$。

### 4. 行波与暂态保护

利用故障产生的高频行波、模态分量或波头到达时间，要求线路模型、采样和滤波链条足够细。在 EMT 中，这类保护需要详细传输线模型（分布参数），仿真步长通常需 $\Delta t \leq 1$ μs 以捕捉波头细节。

### 5. 广域和系统保护

结合 [[wide-area-monitoring-protection]]、PMU/WAMS 和通信链路，实现低频振荡、失步或电压稳定控制。在 EMT 中，广域保护的挑战在于多端数据同步和通信延迟对保护判据的影响。

## EMT 建模：保护系统闭环链路

保护系统进入 EMT 仿真的核心框架（据 [[protection-system-representation-in-the-electromagnetic-transients-program-power]]，Chaudhary 2004）为：

$$\mathbf{x}_{\mathrm{relay}}(t+\Delta t) = f(\mathbf{x}_{\mathrm{relay}}(t), \mathbf{u}_{\mathrm{CT}}(t), \mathbf{u}_{\mathrm{CVT}}(t))$$

其中继电器状态 $\mathbf{x}_{\mathrm{relay}}$ 包括计数器、积分器和存储样本；$\mathbf{u}_{\mathrm{CT}}$、$\mathbf{u}_{\mathrm{CVT}}$ 分别为电流互感器和电压互感器的输出。该框架将保护系统作为动态子系统接入 EMT 仿真，实现"系统暂态→互感器变换→继电器算法处理→保护决策反馈→系统状态更新"的闭环。

### 互感器 EMT 建模

**电流互感器（CT）**：Type 96 伪非线性磁滞电感模型，磁链梯形积分更新：

$$\psi_{k+1} = \psi_k + \Delta t \cdot (v_s - R_s i_s)_k$$

当 $|\psi| > \mathrm{FLXSAT}$（饱和磁链）时铁芯进入饱和区，二次电流传变误差在严重饱和工况下可达 $60\%$~$80\%$，持续 $3$~$5$ 个工频周期。在 EMTP 中必须设置 $Z_{\mathrm{emtp}} > 10^{-6}$ Ω 以避免矩阵条件数 $>10^{12}$ 导致数值发散。

**电容式电压互感器（CVT）**：线性电路模型模拟其剩余电压瞬变，衰减时间常数与文献对比误差 $<5\%$。

### 继电器算法 EMT 表达

数字继电器在 EMT 中的功能块建模（据 [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]]，Boise 2004）包含 9 个模块：

1. **电力系统网络仿真**（Block 1）：EMTP 时域节点方程 $[G]\mathbf{V}(t)=\mathbf{I}(t)$
2. **互感器动态**（Block 2）：CT/CVT 暂态特性建模
3. **模拟信号调理**（Block 3）：二阶低通抗混叠滤波器，$f_c=240$ Hz
4. **采样与保持**（Block 4）：TACS 传输延迟实现零阶保持（ZOH），$T_s \approx 0.7$~$1.4$ ms（每周波 12~24 点）
5. **相量转换**（Block 5）：DFT 或 Walsh 函数，$X(k) = \sum_{n=0}^{N-1} x(n)e^{-j2\pi kn/N}$
6. **保护逻辑判断**（Block 6）：定时限或反时限过流判据
7. **跳闸决策与延时**（Block 7）：断路器失灵保护、重合闸逻辑
8. **断路器控制**（Block 8/9）：Type 11 晶闸管开关等待电流过零开断

### RMS-EMT 实时联合仿真接口

实时 HIL 测试需要 RMS 域（OPAL-RT ePhasorSim，毫秒级步长）与 EMT 域（RTDS，微秒级步长）的联合仿真（据 [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective]]，Espinoza 2021）。接口基于 Bergeron 传输线模型自然解耦：

$$i_{km}(t) = \frac{v_k(t)}{Z_c} + h_k(t-\tau), \qquad h_k(t-\tau) = -\frac{v_m(t-\tau)}{Z_c} - i_{mk}(t-\tau)$$

波形-相量快速曲线拟合（非 FFT 方法）消除传统 FFT 所需 $1$~$2$ 个基波周期（$20$~$40$ ms @ 50 Hz）的固有延迟：

$$\begin{bmatrix} \Re V \\ -\Im V \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} \sum_{n=0}^{N}\cos(\omega t_n)v(t_n) \\ \sum_{n=0}^{N}\sin(\omega t_n)v(t_n) \end{bmatrix}$$

## 形式化表达

继电保护统一抽象为判据和动作逻辑：

$$
g(z_k,p) > 0 \Rightarrow \delta_k = 1,\qquad
t_{\mathrm{trip}} = t_{\mathrm{detect}} + t_{\mathrm{logic}} + t_{\mathrm{breaker}}
$$

其中 $z_k$ 是测量和滤波后的电压、电流、阻抗或序分量，$p$ 是整定参数，$\delta_k$ 是动作命令。任何动作时间或选择性结论都应说明 $t_{\mathrm{detect}}$、通信延迟和断路器模型是否被纳入。

## 关键技术挑战

### CT/CVT 暂态误差

CT 在严重饱和工况下（剩磁 $>80\%$ 饱和磁通），二次电流传变误差可达 $60\%$~$80\%$，持续 $3$~$5$ 个工频周期。CVT 剩余电压瞬变需精确建模以避免保护误动。在 EMT 中，CT 建模必须包含磁滞特性和饱和曲线（Type 96 非线性电感），且 $Z_{\mathrm{emtp}}$ 必须设为非零值。

### 采样率与 DFT 延迟矛盾

数字继电器在 $f_s = 720$~$1440$ Hz（每周波 12~24 点）采样时，全周期 DFT 引入 $16.67$ ms（@ 60 Hz）固有延迟，半周期 DFT 为 $8.33$ ms 但牺牲精度。在故障暂态持续仅 $3$~$10$ ms 的场景下，这个延迟要求与保护快速动作需求形成矛盾。TACS 传输延迟可实现微秒级精度，但受限于仿真步长 $\Delta t$。

### 谐波制动与变压器涌流

变压器差动保护中，涌流含 $2$~$5$ 次谐波分量，需要谐波制动（$k_{2nd}=0.15$~$0.20$，$k_{5th}=0.35$~$0.40$）；但区外故障电流中也含有谐波，制动系数过大会延长动作时间。EMT 仿真可验证制动判据在不同故障场景下的安全性与速动性。

### 换流器型电源故障电流受限

高比例逆变器电源系统中，换流器可能限制故障电流幅值或改变相位，导致传统过流、距离和方向元件边界变化。在 EMT 中，换流器的限流特性（LVRT、Crowbar 等）与保护判据的交互需要详细建模验证。

### 实时 HIL 接口延迟

RMS-EMT 联合仿真中，相量-波形转换引入的延迟直接影响保护 HIL 测试的真实性。传统 FFT 方法需要 $1$~$2$ 个基波周期（$20$~$40$ ms）缓冲窗口，快速曲线拟合方法通过分布式计算实现零缓冲转换，但需要滑动窗口平滑相量更新以消除高频噪声。

## 适用边界与失败模式

- 标准定值、典型动作时间和经验灵敏度不能脱离电压等级、保护类型和工程规程直接写成通用结论。
- 换流器型电源可能限制故障电流幅值或改变相位，导致传统过流、距离和方向元件边界变化。
- 只在稳态相量模型中验证保护，可能遗漏暂态饱和、行波反射、谐波制动和重合闸瞬态。
- 若通信链路、采样同步和断路器失灵逻辑缺失，纵联保护和广域保护结论应降级。
- CT 模型精度受限于 EMTP 变压器模型无分布电容，不适用于更高频率（$>$ 数 kHz）。
- FORTRAN 接口支持每时步数据交换，典型仿真步长 $50$~$100$ μs 时继电器算法处理延迟 $<1$ μs，满足实时性要求，但需确保 $Z_{\mathrm{emtp}} > 10^{-6}$ Ω 以避免数值发散。

## 保护配合原则

| 配合类型 | 原则 | 实现方法 |
|----------|------|----------|
| 时间配合 | 靠近故障点的保护先动作 | 逐级增加延时（$0.3$~$0.5$ s） |
| 电流配合 | 故障电流大的保护先动作 | 定值阶梯设置 |
| 阻抗配合 | 距离故障近的保护先动作 | 阻抗定值阶梯 |
| 方向配合 | 判别故障方向 | 方向元件 |

## 典型保护动作时间

| 保护类型 | 动作时间 | 适用场景 |
|----------|----------|----------|
| 过流速断 | $0$~$0.1$ s | 近端故障 |
| 过流延时 | $0.3$~$2$ s | 后备保护 |
| 距离 I 段 | $0$~$0.1$ s | 线路 $80\%$~$85\%$ |
| 距离 II 段 | $0.3$~$0.5$ s | 全线+相邻线路 |
| 差动保护 | $0.02$~$0.05$ s | 变压器、母线 |
| 行波保护 | $0.001$~$0.01$ s | 超高速保护 |

## 保护误动/拒动原因分析

| 现象 | 可能原因 | 对策 |
|------|----------|------|
| 误动 | 涌流、CT 饱和 | 谐波制动、比率制动 |
| 误动 | 负荷波动、振荡 | 增加延时、阻抗圆特性 |
| 拒动 | 故障电阻过大 | 自适应阻抗特性 |
| 拒动 | 故障电流受限（逆变器） | 新型保护判据 |
| 误动 | 电磁干扰 | 屏蔽、滤波 |
| 拒动 | 定值不当 | 重新整定、校核 |

## 开放问题

- 如何在高比例逆变器电源系统中重新校核传统保护判据。
- 如何把现场录波、EMT 仿真和 HIL 测试组织成可追溯的保护证据链。
- 如何在不公开厂家固件细节的前提下建立可复审的保护模型。

## 来源论文

- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] — Chaudhary 2004：EMTP 中集成保护系统的完整框架（CT/CVT 暂态模型 + FORTRAN 接口 + 闭环交互），230 kV 系统验证，CT 饱和误差 $40$~$60\%$
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]] — Boise 2004：基于 EMTP-TACS 的数字继电器教学框架，9 个功能模块，复现 A/D 采样、DFT 相量提取和跳闸控制，DFT 延迟 $16.67$ ms
- [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective]] — Espinoza 2021：OPAL-RT ePhasorSim 与 RTDS 实时 RMS-EMT 联合仿真接口，Bergeron 传输线解耦，非缓冲快速曲线拟合消除 FFT 固有延迟
- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] — Rosołowski 1997：基于对称分量复数微分方程的距离保护算法
- [[application-of-wavelet-singular-entropy-theory-in-transient-protection-and-accel]] — 小波奇异熵理论在暂态保护中的应用
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]] — 双回线路单端行波保护方案
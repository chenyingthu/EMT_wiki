---
title: "复数微分方程求解 (Complex Differential Equation Solving)"
type: method
tags: [complex, differential-equation, numerical, solver, impedance, protection, dynamic-phasor, shifted-frequency]
created: "2026-05-02"
updated: "2026-05-18"
---

# 复数微分方程求解 (Complex Differential Equation Solving)

## 定义与边界

复数微分方程求解是把电压、电流、磁链、阻抗或包络等电气量表示为复变量，并在复数域或等价的实部-虚部增广系统中求解其动态关系的方法集合。它不是一种单一积分器；实际实现通常仍需调用[[trapezoidal-rule]]、[[backward-euler]]、[[newton-raphson-method]]或直接代数解算。

在 EMT Wiki 中，本页覆盖两类使用场景：

- **保护与故障分析**：用复数瞬时量、对称分量或阻抗变量表达故障回路方程，在复数域中求阻抗轨迹或故障参数估计值。
- **多尺度 EMT**：用解析信号、动态相量或频移包络把实数 EMT 变量改写为复变量，再进行离散化和网络接口求解——此时复变量是频移（shifted-frequency）或包络（envelope）建模的核心。

本页不把复数表示本身等同于精度提升或计算加速。任何效率、误差或动作时间结论都必须绑定具体论文、算例、步长、滤波器和比较基线。

## EMT 中的角色

复数微分方程在 EMT 仿真中有两条核心应用路径：

### 保护与阻抗估计

在保护应用中，复数形式把等效故障回路中的电压、电流和正序阻抗写成紧凑的复数微分方程，然后拆成实部和虚部方程求未知参数。[[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym|Rosołowski 等 1997]]记录的代表性做法是：先用短窗傅里叶滤波得到对称分量，再按故障类型构造复数等效故障回路，用实虚部方程在采样瞬间同步求正序阻抗（$R_1$ 和 $L_1$）。

### 多尺度与动态相量

在多尺度 EMT 中，复变量常来自解析信号或[[dynamic-phasor]]。这类模型把工频或目标频带附近的量搬移为低频包络，有助于表达慢变化分量。但[[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Parvari 等 2026]]提醒：**频移不会消除电路固有暂态模态**，反而会将特征值平移 $\pm j\omega_0$（式(27)），导致动态相量模型的时间步长约束可能比原 EMT 更严格。

## 核心机制

### 1. 复数微分方程的基本形式

复数微分方程的一般形式为：

$$\frac{d\mathbf{z}}{dt} = \mathbf{f}(\mathbf{z}, \mathbf{z}^*, t), \quad \mathbf{z} = \mathbf{x} + j\mathbf{y} \tag{1}$$

若函数显式依赖共轭项 $\mathbf{z}^*$，通常不能简单套用复解析函数理论，而应转为实部-虚部增广系统：

$$\frac{d}{dt}\begin{bmatrix}\mathbf{x} \\ \mathbf{y}\end{bmatrix} = \begin{bmatrix}\operatorname{Re}\mathbf{f}(\mathbf{x}+j\mathbf{y}, \mathbf{x}-j\mathbf{y}, t) \\ \operatorname{Im}\mathbf{f}(\mathbf{x}+j\mathbf{y}, \mathbf{x}-j\mathbf{y}, t)\end{bmatrix} \tag{2}$$

对线性或线性化系统，复变量也可写为：

$$\dot{\mathbf{z}} = \mathbf{A}\mathbf{z} + \mathbf{B}\mathbf{u} \tag{3}$$

经过隐式离散化后，求解器面对的是复线性系统或等价的实增广线性系统。若系统含非线性元件或控制器限幅，仍需形成残差并用[[newton-raphson-method]]或其他[[iterative-solvers]]求解。

### 2. 故障回路复数微分方程（Rosołowski 1997）

对于距离保护场景，等效故障回路的一般复数微分方程为：

$$\tilde{v}(t) = R_1\tilde{i}_R(t) + L_1\frac{d\tilde{i}_L(t)}{dt} + \tilde{v}_e(t) \tag{4}$$

其中 $\tilde{v}(t)$、$\tilde{i}_R(t)$、$\tilde{i}_L(t)$ 和 $\tilde{v}_e(t)$ 是等效回路中的复值电压电流信号和源。将式(4)按实部/虚部展开，得到两个实数方程：

$$S[v_{ex}(k)] = S[i_{\phi R}(k)]R_1 + D[i_{\phi L}(k)]L_1 \tag{5}$$

其中 $S[\cdot]$ 和 $D[\cdot]$ 分别是采样时刻的信号算子和微分算子。由两个方程可同步求解 $R_1$ 和 $L_1$，无需等待滤波窗。

### 3. 动态相量特征值平移（Parvari 2026）

原始电路的状态空间方程为：

$$\frac{d\mathbf{x}(t)}{dt} = \mathbf{A}\mathbf{x}(t) \tag{6}$$

经动态相量变换后，伴随电路的状态方程为：

$$\frac{d\mathbf{X}(t)}{dt} + j\omega_0\mathbf{X}(t) = \mathbf{A}\mathbf{X}(t) \tag{7}$$

其特征值集合为：

$$\Lambda_{\text{comp}} = \{\lambda \pm j\omega_0 : \lambda \in \Lambda_{\text{main}}\} \tag{8}$$

这意味着 EMT 时间步长约束为：

$$\Delta t_{\text{EMT}} \ll \frac{1}{\max\{|\lambda| : \lambda \in \Lambda_{\text{main}}\}} \tag{9}$$

而动态相量模型要求的时间步长为：

$$\Delta t_{\text{DP}} \ll \frac{1}{\max\{|\lambda \pm j\omega_0| : \lambda \in \Lambda_{\text{main}}\}} \tag{10}$$

式(10)表明：**动态相量模型要求的时间步长可能比 EMT 更小**，而非通常认为的"可以用更大的步长"。这一结论成立的条件是电路特征值 $|\lambda|$ 较小（即暂态衰减慢）；若阻尼足够大（$\sigma$ 增大 10-100 倍），大时间步长下的误差可忽略。

## 分类与变体

| 类型 | 机制 | 常见用途 | 证据边界 |
|------|------|----------|-----------|
| **复阻抗/复故障回路方程** | 用复电压、电流和阻抗参数写等效回路，直接在采样瞬间求解 $R$ 和 $X$ | [[distance-protection]]、阻抗继电器、故障测距 | 1kHz 采样+350Hz 抗混叠滤波下约半周期（10ms）可达满意精度；故障电阻增大时误差增加 |
| **实部-虚部增广 ODE/DAE** | 把复方程转成两倍维度的实系统，与通用 EMT 求解器或稀疏线性代数接口 | 含非线性元件或控制器限幅的一般复系统 | 维度加倍使计算量增大约 2 倍；但表达更直接，避免复数运算歧义 |
| **解析信号与频移包络** | 通过 Hilbert 变换或积分因子构造复包络，用于 [[dynamic-phasor]] 或 [[multirate-method]] | 宽频开关暂态与工频慢过程的混合仿真 | 仅对目标频带附近分量有效；宽频开关过程需保留完整 EMT 表征 |
| **复数梯形/伴随模型** | 将复状态方程用梯形积分离散为导纳和历史源 | 频变电缆、动态相量网络、包络模型 | 历史项需随步长和频移频率一致更新；传输线的延迟效应施加独立上限 |
| **移频分析（SFA）** | 将工频 $\omega_0$ 附近分量平移到低频包络域，在 GPU 上实现比实时更快的仿真 | 大规模系统快于实时仿真、电力系统并行计算 | 步长增大时误差缓慢增长；存在数值振荡风险；需与基准 EMT 对比校核 |

## 关键技术挑战

### C1：共轭项方程的实部-虚部耦合

当复微分方程显式依赖 $\mathbf{z}^*$ 时（如某些非线性磁路模型），不能直接套用复解析微分法则。必须展开为实部-虚部耦合的增广系统，此时 Jacobian 矩阵的维度加倍，可能影响收敛性。

### C2：动态相量特征值平移导致的时间步长收紧

由式(8)-(10)可知，动态相量将特征值平移 $\pm j\omega_0$，若 $|\omega_0| \gg |\lambda_{\max}|$，则 $|\lambda \pm j\omega_0| \approx \omega_0$，此时 $\Delta t_{\text{DP}}$ 的上限约为 $1/\omega_0$（约 2.65ms for 60Hz），而 EMT 的约束可能因 $|\lambda_{\max}|$ 很大而更小。因此**动态相量并不自动允许更大时间步长**——步长选择应基于 $\Delta t_{\text{DP}}$ 约束（式(10)）而非 $\Delta t_{\text{EMT}}$ 约束。

### C3：复数量测噪声与阻抗轨迹放大

当电流接近零或噪声较大时，直接用 $Z = V/I$ 计算阻抗会导致轨迹放大误差。Rosołowski 方法通过半个周期短窗 Fourier 滤波提供对称分量估计，但滤波本身引入相位延迟，需在阻抗估计中作补偿。

### C4：开关动作与暂态模态的自动覆盖

开关切换瞬间，电路拓扑变化导致特征值集合突变。Parvari 指出：对开关电路，每个开关状态组合对应一组特征值；$\Delta t$ 的选择应取所有组合的 $\max\{|\lambda|, |\lambda \pm j\omega_0|\}$ 的倒数。这意味着复杂电网中开关动作可能强制减小时间步长。

### C5：传输线延迟效应的独立约束

传输线具有固有延迟 $\tau_d$（ latency），离散化后的时间步长必须满足 $\Delta t < \tau_d$。对于动态相量域的传输线模型，Parvari 指出延迟约束仍然成立，但不受特征值约束——因此传输线引入了 **独立于特征值的时间步长上界**，与级联 LC 电路（无限多个极点）的分析形成对比。

## 量化性能边界

### 距离保护阻抗估计（Rosołowski 1997）

- **采样条件**：$f_s = 1\text{kHz}$（每周期 20 样本），模拟抗混叠滤波截止频率 $f_c = 350\text{Hz}$
- **响应速度**：约**半个工频周期**（10ms for 50Hz）得到可接受的阻抗估计
- **高阻故障**：50Ω 故障电阻下阻抗轨迹偏离动作区，对并联线路的双端阻抗判据失效；但修正算法（式(13)-(14)）可在 2-7ms 内检测并识别故障线路
- **并行线路检测**：双端电压差分法（式(14)）检测时间：近端约 7ms，远端约 2ms

### 动态相量时间步长约束（Parvari 2026）

Parvari 给出了三类阻尼条件下 $R$、$L$、$C$ 参数与推荐步长的对照表：

| 阻尼条件 | $R$ [Ω] | $L$ [mH] | $C$ [μF] | 特征值 | 推荐 $\Delta t_{\text{EMT}}$ [μs] | 推荐 $\Delta t_{\text{DP}}$ [μs] |
|----------|---------|----------|----------|--------|-------------------------------|-------------------------------|
| 轻阻尼 | 1.0 | 0.00282 | 10.0 | $-0.05 \pm j188$ | 266 | 88 |
| 中阻尼 | 1.0 | 0.02829 | 1.0 | $-0.5 \pm j188$ | 266 | 88 |
| 强阻尼 | 1.0 | 0.2827 | 0.1 | $-5.0 \pm j188$ | 266 | 88 |

**关键结论**：轻阻尼（$\lambda = -0.05 \pm j188$）时，动态相量要求的时间步长（88μs）比 EMT（266μs）更小约 3 倍；强阻尼（$\lambda = -5.0 \pm j188$）时误差在两种步长下均可忽略。

### 移频分析 GPU 加速（Zhang 2024）

- **精度**：以 50μs 步长 EMT 为基准，SFA 仿真在 100μs/500μs/1ms 步长下的相对误差随时间缓慢增长，首周期误差较小
- **加速比**：OpenCL 框架下任务并行执行对 IEEE-118 规模系统（2×-8× 复制）可达显著加速（详见原文表）
- **适用范围**：SFA 适用于工频附近分量主导的暂态过程；开关暂态和宽频谐波需保留 EMT 表征

## 适用边界与选择指南

| 场景 | 推荐方法 | 理由 |
|------|----------|------|
| 距离保护阻抗估计（单端） | 复数故障回路方程（Rosołowski） | 采样瞬间同步求解 $R$、$X$，半周期响应，无需等待完整滤波窗 |
| 并行线路高阻故障检测 | 双端电压差分法（式(13)-(14)） | 利用双端电气量差分，不依赖阻抗轨迹形状判别 |
| 多尺度 EMT（工频慢过程） | 动态相量包络模型 | 将 $\omega_0$ 附近分量频移为低频包络，慢过程可用大步长；**但需按式(10)验证步长可行性** |
| 大规模系统快于实时仿真 | 移频分析（SFA）+ GPU 并行 | 频移后计算量降低，GPU 异构并行可实现比实时更快的仿真 |
| 开关电路（频繁切换） | 需逐开关状态组合验证步长约束 | 每种拓扑对应一组特征值，最大特征值决定步长上限 |
| 传输线分布参数系统 | 独立满足 $\Delta t < \tau_d$ 约束 | 传输线延迟是独立约束，不受特征值分析支配 |

**选择决策**：
1. 若只需工频阻抗估计（保护继电器）→ 复数故障回路方程
2. 若要混合宽频+工频仿真 → 动态相量分段多速率，但**必须用式(10)验证步长**
3. 若要大系统实时/超实时仿真 → 移频分析 GPU 加速，但需保留宽频分量详情
4. 若涉及开关切换 → 必须用所有开关组合的特征值验证 $\Delta t$ 可行性

## 相关方法 / 相关模型 / 相关主题

- [[distance-protection]]：复数故障回路方程的直接应用场景
- [[time-domain-impedance-estimation]]：复数方程用于阻抗估计的另一种形式
- [[dynamic-phasor]]：复数包络/频移建模的理论基础
- [[shifted-frequency-analysis]]：移频分析与动态相量的工程实现
- [[multirate-method]]：动态相量与 EMT 多速率接口方法
- [[trapezoidal-rule]] 与 [[backward-euler]]：复数状态方程离散化时常用的底层积分规则
- [[dae-solvers]]：复变量与网络约束耦合后形成的复数 DAE
- [[newton-raphson-method]]：非线性复系统求解的迭代方法
- [[symmetrical-components]]：保护场景中复数变量由序分量组合而来

## 来源论文

- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]]：Rosołowski 等 1997。用对称分量构造复数等效故障回路，并拆成实虚部求正序阻抗。提供半周期响应（10ms）和并行线路检测（2-7ms）的量化数据。

- [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]]：Parvari 等 2026。用特征值分析证明动态相量不自动允许更大时间步长——平移后特征值模增大，导致 $\Delta t_{\text{DP}} < \Delta t_{\text{EMT}}$。提供 Table 3 阻尼参数-步长映射数据。

- [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste]]：Zhang 等 2024。SFA 在 GPU（OpenCL）上的快于实时仿真实现，提供误差-步长曲线和加速比数据。

- [[multi-scale-formulation-of-admittance-based-modeling-of-cables]]：多尺度导纳建模中复变量用于电缆的梯形积分递归卷积改写。

- [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems]]：多速率接口中复变量结构一致性的理论保证。
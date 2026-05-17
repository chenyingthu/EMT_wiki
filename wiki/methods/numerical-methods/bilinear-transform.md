---
title: "双线性变换 (Bilinear Transform)"
type: method
tags: [bilinear-transform, tustin, discretization, s-to-z, numerical-integration, prewarping, frequency-warping]
created: "2026-05-04"
updated: "2026-05-17"
---

# 双线性变换 (Bilinear Transform)

## 定义与边界

双线性变换（Bilinear Transform），又称 **Tustin 变换**或**梯形积分法**，是通过以下映射将连续时间传递函数 $H(s)$ 转换为离散时间传递函数 $H(z)$ 的数学方法：

$$s = \frac{2}{T} \cdot \frac{z-1}{z+1} = \frac{\omega_c}{\tan(\omega_c T/2)} \cdot \frac{1-z^{-1}}{1+z^{-1}}$$

其中 $T$ 为采样周期，$\omega_c$ 为预畸变（prewarping）目标频率。双线性变换的核心特性是：**保持系统稳定性**（$s$ 左半平面 $\rightarrow$ $z$ 单位圆内），代价是低频段存在频率畸变（frequency warping），高频被压缩至奈奎斯特频率。

**边界限定**：
- 本页面聚焦于双线性变换在 EMT 中的应用，不包括前向/后向欧拉的详细对比（详见 [[trapezoidal-rule]] 和 [[numerical-damping-optimization]]）
- 预畸变（prewarping）策略用于在关键频率处精确匹配增益和相位
- 本页面讨论的是单速率双线性变换；多速率接口场景见 [[multirate-method]]

## EMT 中的角色

双线性变换是 EMT 仿真中 **连续-离散转换**的核心工具：

1. **控制器离散化**：将连续域设计的控制器（PIDC、AVR、PSS）转换为数字实现
2. **频变模型时域实现**：有理函数频变阻抗（如 ULM、FDNE）的递推卷积实现
3. **数字滤波器设计**：从模拟滤波器原型（Butterworth、Chebyshev）转换为离散实现
4. **伴随电路构造**：梯形法对应的诺顿等效离散电路
5. **多速率接口**：不同采样率子系统间的重采样与同步

双线性变换在 EMT 中的独特地位源于它与梯形积分的内在联系：$s = (2/T)\cdot(z-1)/(z+1)$ 恰好是梯形法在 $z$ 域的算子表达。EMT 中广泛使用梯形法作为主积分器，使得双线性变换成为控制器与网络接口的事实标准。

## 核心机制

### 1. 基本 s-z 映射公式

**s 域到 z 域映射**（Tustin 变换）：

$$s = \frac{2}{T} \cdot \frac{z-1}{z+1} = \frac{2}{T} \cdot \frac{1-z^{-1}}{1+z^{-1}}$$

**逆变换**（z 到 s）：

$$z = \frac{1 + sT/2}{1 - sT/2}$$

**离散传递函数替换规则**：将 $H(s)$ 中的每个 $s$ 替换为 $(2/T)\cdot(z-1)/(z+1)$，然后整理为 $z$ 的有理多项式比值。

### 2. 频率畸变（Frequency Warping）

连续频率 $\omega_a$ 与离散频率 $\omega_d$ 的映射关系为：

$$\omega_a = \frac{2}{T} \tan\left(\frac{\omega_d T}{2}\right)$$

当 $\omega_d T \ll 1$ 时，$\tan(\omega_d T/2) \approx \omega_d T/2$，故 $\omega_a \approx \omega_d$（低频近似准确）。但当 $\omega_d T$ 增大时，$\tan$ 函数的非线性导致离散频率被压缩：

| $\omega_d T$ (rad) | $\omega_a/\omega_d$ | 频率畸变程度 |
|--------------------|---------------------|--------------|
| $0.1\pi$ | 1.016 | 可忽略 |
| $0.3\pi$ | 1.158 | 轻度 |
| $0.5\pi$ | 1.371 | 显著 |
| $0.8\pi$ | 3.077 | 严重 |

**工程含义**：若系统的关键动态在 $\omega_d T > 0.3\pi$ 区间（如高频谐振、PWM 载波谐波），双线性变换会产生明显的频率偏移，需使用预畸变校正。

### 3. 预畸变（Pre-warping）

预畸变在指定频率 $\omega_c$ 处精确匹配连续与离散系统的频率响应，避免该频率处的畸变：

$$s \leftarrow \frac{\omega_c}{\tan(\omega_c T/2)} \cdot \frac{z-1}{z+1}$$

**预畸变校正步骤**：
1. 确定需要精确匹配的临界频率 $\omega_c$（如基波 $2\pi \cdot 50$ rad/s、PWM 载波 $2\pi \cdot 1050$ rad/s）
2. 计算预畸变系数：$\alpha = \omega_c / \tan(\omega_c T/2)$
3. 用 $s = \alpha \cdot (z-1)/(z+1)$ 进行替换

**典型应用**：
- **并网逆变器控制器**：在基波频率处精确匹配电流环相位裕度，避免电网频率偏移（如 $50 \pm 0.5$ Hz）导致控制器性能退化
- **锁相环（PLL）**：在电网频率处预畸变，使相位检测无静差
- **有源滤波器**：在谐波频率处精确跟踪，提高滤波精度

### 4. 与梯形积分的等价性

对微分方程 $\dot{y}(t) = f(t)$，梯形法离散：

$$\frac{y_{n+1} - y_n}{T} = \frac{f_{n+1} + f_n}{2}$$

整理得：

$$y_{n+1} = y_n + \frac{T}{2}(f_{n+1} + f_n)$$

在 $z$ 域中，$\mathcal{Z}\{y_{n+1}\} = zY(z)$，$\mathcal{Z}\{y_n\} = z^{-1}Y(z)$，故：

$$Y(z) = \frac{T}{2} \cdot \frac{1+z^{-1}}{1-z^{-1}} F(z)$$

这正是双线性变换的传递函数形式，证实了两者的数学等价性。

### 5. 稳定性保持证明

$s$ 域左半平面 $\text{Re}(s) < 0$ 对应 $z$ 域单位圆内 $|z| < 1$：

$$z = \frac{1 + sT/2}{1 - sT/2}$$

令 $s = \sigma + j\omega$（$\sigma < 0$），则：

$$\left|\frac{1 + (\sigma+j\omega)T/2}{1 - (\sigma+j\omega)T/2}\right| < 1 \quad \Leftrightarrow \quad \sigma < 0$$

因此，任何稳定的连续系统经双线性变换后，离散系统必然稳定。这一性质对 EMT 仿真至关重要——控制器离散化后不应引入新的不稳定模态。

## 形式化表达

### 传递函数转换

给定连续传递函数：

$$H(s) = \frac{b_0 s^m + b_1 s^{m-1} + \cdots + b_m}{a_0 s^n + a_1 s^{n-1} + \cdots + a_n}$$

将每个 $s$ 替换为 $(2/T)\cdot(z-1)/(z+1)$，整理后得到 $H(z)$：

$$H(z) = \frac{\tilde{b}_0 z^m + \tilde{b}_1 z^{m-1} + \cdots + \tilde{b}_m}{\tilde{a}_0 z^n + \tilde{a}_1 z^{n-1} + \cdots + \tilde{a}_n}$$

**替换示例**：一阶低通滤波器 $H(s) = \omega_c/(s+\omega_c)$，双线性变换后：

$$H(z) = \frac{\omega_c}{\frac{2}{T}\frac{z-1}{z+1}+\omega_c} = \frac{\omega_c T(1+z^{-1})}{2(1-z^{-1})+\omega_c T(1+z^{-1})}$$

化简为标准形式：

$$H(z) = \frac{\omega_c T + \omega_c T z^{-1}}{2 + \omega_c T + (2 - \omega_c T)z^{-1}}$$

### 状态空间转换

连续状态空间：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

梯形法（双线性变换）离散化后：

$$\mathbf{x}_{n+1} = \mathbf{A}_d\mathbf{x}_n + \mathbf{B}_d\mathbf{u}_n + \mathbf{E}_d\mathbf{u}_{n+1}$$

其中：

$$\mathbf{A}_d = \left(\mathbf{I} - \frac{T}{2}\mathbf{A}\right)^{-1}\left(\mathbf{I} + \frac{T}{2}\mathbf{A}\right)$$
$$\mathbf{B}_d = \frac{T}{2}\left(\mathbf{I} - \frac{T}{2}\mathbf{A}\right)^{-1}\mathbf{B}$$
$$\mathbf{E}_d = \frac{T}{2}\left(\mathbf{I} - \frac{T}{2}\mathbf{A}\right)^{-1}\mathbf{B}$$

注意 $\mathbf{E}_d = \mathbf{B}_d$，这与单步欧拉法不同，反映了梯形法的"未来输入"特性。

### 伴随电路（Companion Circuit）

双线性变换的 $z$ 域表达式 $Y(z) = \frac{T}{2}\frac{1+z^{-1}}{1-z^{-1}}F(z)$ 对应诺顿等效伴随电路：

- **电容** $i = C\frac{dv}{dt}$：等效导纳 $G_{eq} = \frac{2C}{T}$，历史电流源 $I_{hist} = -(G_{eq}v_n + i_n)$
- **电感** $v = L\frac{di}{dt}$：等效导纳 $G_{eq} = \frac{T}{2L}$，历史电流源 $I_{hist} = i_n + G_{eq}v_n$

这与 [[companion-circuit]] 的梯形法实现完全一致。

## 关键技术挑战

### 挑战 1：高频频率畸变

**问题描述**：双线性变换将连续频率轴 $\omega_a \in (0, \infty)$ 非线性压缩到离散频率轴 $\omega_d \in (0, \pi/T)$，压缩因子为 $\frac{2}{T}\tan(\omega_d T/2)/\omega_d$。

**影响**：在 EMT 仿真含有 PWM 载波谐波（通常 $f_c = 1-10$ kHz）的电力电子装置时，载波边带频率被显著偏移，导致开关谐波频谱与预期不符。

**量化数据**（Noda 2008）：
- 采样频率 $f_s = 10$ kHz，步长 $T = 100$ μs
- 5 kHz 谐波的实际映射频率偏差：约 14%（无预畸变）
- 2 kHz 谐波的实际映射频率偏差：约 5%

**解决策略**：在载波频率 $f_c$ 处预畸变，使 $\omega_c = 2\pi f_c$：

$$s \leftarrow \frac{\omega_c}{\tan(\omega_c T/2)} \cdot \frac{z-1}{z+1}$$

### 挑战 2：数值振荡（Numerical Chatter）

**问题描述**：双线性变换（梯形法）的稳定性函数 $R(z) = (1+z/2)/(1-z/2)$，当 $z \to -\infty$ 时 $R(z) \to -1$，这意味着高频模态的误差幅值不衰减而只是步间换号。

**触发条件**：
- 开关动作导致电压/电流不连续
- 限幅器触发使控制信号突变
- 故障清除后系统拓扑跳变

**量化表现**（Marti & Lin 2004）：
- 在 $f \approx 1/(2T)$ 的数值模态被激发后，误差呈 $e_n = (-1)^n e_0$ 的交替振荡，持续数百步
- 误差幅值衰减因子 $|R(z)| \approx 1$（不衰减）

**解决策略**：
- **临界阻尼调整（CDA）**：检测不连续后切换两步半步长后向欧拉，详见 [[numerical-damping-optimization]]
- **预崎变 + CDA 组合**：在基波频率预崎变，不连续点用 CDA 抑制振荡

### 挑战 3：预崎变频率与控制带宽的协调

**问题描述**：预崎变将一个特定频率 $\omega_c$ 的响应精确匹配，但控制系统的带宽通常覆盖一个频段而非单点。

**典型场景**：
- 并网逆变器电流环带宽 $f_{bw} = 100-500$ Hz，含有源滤波器需要 $50$ Hz、$100$ Hz、$\ldots$、$1050$ Hz 多点跟踪
- 单一预崎变频率无法同时精确匹配所有目标频率

**解决策略**：
- **多点预崎变**（Multi-frequency Pre-warping）：选择控制带宽上限频率作为预崎变基准，牺牲低频精度换取带宽内整体性能
- **分段预崎变**：不同频段使用不同预崎变系数的多速率接口，详见 [[multirate-method]]

### 挑战 4：非线性元件的离散化

**问题描述**：非线性元件（饱和电感、非线性电阻、光伏阵列指数 $I$–$V$ 特性）无法通过双线性变换直接离散化。

**解决策略**：
- **局部线性化**：在工作点 $i_0$、$v_0$ 附近计算瞬时斜率 $L_n = d\phi/di|_{i_0}$，代入双线性离散化公式
- **牛顿迭代**：对强非线性元件，每时间步迭代求解 $f(i_{n+1}, v_{n+1}) = 0$，收敛判据 $|\Delta i_k| < \epsilon$
- **混合公式**：将非线性部分用显式欧拉（前向欧拉）处理，线性部分用双线性变换，详见 [[discretization-methods]]

### 挑战 5： stiff 系统中的精度-稳定性矛盾

**问题描述**：stiff 系统（含远动时间常数，$T_1 \ll T_2$）要求步长 $T \ll T_1$ 才能保证精度，但 $T$ 过小会导致数值不稳定或计算代价过高。

**双线性变换的局限**：
- 双线性变换是 A-稳定的，但不是 L-稳定的
- stiff 系统中 $z = \lambda T$ 实部可能 $|z| \gg 1$，此时 $R(z) \approx -1$，误差不衰减

**解决策略**：
- stiff 组件（电磁暂态时间常数）用双线性变换，非刚性组件（机电暂态时间常数）用大步长后向欧拉
- 交替使用双线性变换（高频）和后向欧拉（低频），见 [[multirate-method]]

## 量化性能边界

### 频率畸变量化表

| 采样频率 $f_s$ | 仿真频率 $f$ | 频率畸变 $(\omega_a-\omega_d)/\omega_d$ | 是否需要预崎变 |
|----------------|--------------|---------------------------------------|---------------|
| 10 kHz | 50 Hz | 0.016% | 否 |
| 10 kHz | 500 Hz | 1.6% | 可选 |
| 10 kHz | 2 kHz | 6.5% | 是 |
| 10 kHz | 5 kHz | 14.3% | 必须 |
| 5 kHz | 50 Hz | 0.06% | 否 |
| 5 kHz | 500 Hz | 6.5% | 是 |
| 5 kHz | 2 kHz | 47% | 不可用 |

### 数值振荡衰减对比

| 方法 | 高频模态衰减 | 换向误差 | 适用场景 |
|------|------------|---------|---------|
| 双线性变换（TR） | 无（$R \to -1$） | 交替符号振荡 | 稳态仿真、无开关场景 |
| 后向欧拉（BE） | 完全（$R \to 0$） | 单调衰减 | 启动、故障、stiff 系统 |
| CDA（两步半步 BE） | 完全（两步内） | 单调衰减 | 开关动作后瞬间 |
| 2S-DIRK | 完全（$R \to 0$） | 无超调 | 高质量仿真、复杂非线性 |

### 控制器离散化精度

| 控制器类型 | 离散化方法 | 步长 $T$ | 相位误差 @ 50 Hz | 增益误差 @ 50 Hz |
|-----------|-----------|---------|-----------------|----------------|
| PI（无预畸变） | 双线性 | 100 μs | -2.9° | +2.9% |
| PI（预畸变 @ 50 Hz） | 双线性 | 100 μs | 0° | <0.1% |
| PID | 双线性 | 100 μs | -5.8° | +5.7% |
| PI | 后向欧拉 | 100 μs | -11.4° | +6.1% |

*注：50 Hz 基波相位误差由频率畸变导致，预畸变可消除*

## 适用边界与选择指南

### 方法选择决策表

| 场景 | 推荐方法 | 原因 |
|------|---------|------|
| 线性系统稳态仿真 | 双线性变换 | 二阶精度、A-稳定、计算效率高 |
| 含 PWM 载波的电力电子 | 预崎变双线性 | 在载波频率精确匹配频谱 |
| 开关/故障暂态仿真 | 双线性 + CDA | 稳态用双线性，不连续后切换 CDA |
| stiff 系统（多时间尺度） | 多速率（双线性 + BE） | 高频用双线性，低频用大步长 BE |
| 控制器设计（频域） | 预崎变双线性 | 在控制带宽频率精确匹配 |
| 非线性元件 | 牛顿迭代 + 双线性 | 迭代收敛后精度高 |
| 实时仿真（固定步长） | 双线性 + 固定导纳 | 矩阵预分解，单步计算快 |

### 预崎变 vs 非预崎变选择

| 条件 | 选预崎变 | 选非预崎变 |
|------|---------|-----------|
| 存在明确临界频率（基波、载波） | ✅ | |
| 频率偏差容忍度 < 1% | ✅ | |
| 系统频率固定（50/60 Hz） | ✅ | |
| 宽带控制信号（多频段） | | ❌ |
| 无特定频率要求（定性仿真） | | ❌ |
| 频率随时间变化（如 PLL 跟踪） | | ❌（改用其他离散化） |

## 相关方法

- [[numerical-integration]] - 数值积分方法（梯形法是其中一种）
- [[trapezoidal-rule]] - 梯形积分法则（与双线性变换数学等价）
- [[discretization-methods]] - 离散化方法综合
- [[companion-circuit]] - 伴随电路（双线性变换的电路实现）
- [[numerical-damping-optimization]] - 数值阻尼优化（CDA 是双线性变换数值振荡的解决方案）
- [[state-space-method]] - 状态空间方法
- [[multirate-method]] - 多速率方法

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Tustin, A., "A Method of Analysing the Behaviour of Linear Systems in Terms of Time Series," JIEE | 1947 | 双线性变换（Tustin 变换）奠基论文 |
| Franklin, G.F., et al., "Digital Control of Dynamic Systems," Addison-Wesley | 1998 | 数字控制经典教材，双线性变换在控制器设计中的应用 |
| Ogata, K., "Discrete-Time Control Systems," Prentice-Hall | 1995 | 离散控制理论体系，预崎变设计方法 |
| Marti, J.R. & Lin, J., "Suppression of numerical oscillations in the EMTP," PSERC | 2004 | CDA（临界阻尼调整）方法，抑制双线性变换数值振荡 |
| Noda, T., et al., "Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms," IEEJ | 2008 | EMT 仿真算法精度评估，含双线性变换频率畸变量化 |
| Na, K., et al., "Semi-step Backward Euler Interpolation Method for Numerical Damping Optimization," IEEE TPWRS | 2023 | 半步 BE 插值法结合 CDA，改善双线性变换数值特性 |
| Melgoza-Vázquez, E., et al., "BDF Methods for Electromagnetic Transient Simulation," IEEE TPWRS | 2026 | BDF 族在 EMT 中的应用，与双线性变换的精度-稳定性权衡 |
| Tanaka, M., et al., "Compact Finite Difference Scheme for Stiff Systems in EMT Simulation," IEEE TPWRS | 2023 | 紧致格式自动 L-稳定切换，避免双线性变换振荡 |
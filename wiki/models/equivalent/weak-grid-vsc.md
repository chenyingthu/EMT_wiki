---
title: "弱电网VSC建模方法"
type: model
tags: [weak-grid, VSC, GFL, GFM, PLL, SCR, EMT建模, 小信号稳定性]
created: "2026-05-13"
updated: "2026-05-17"
---

# 弱电网VSC建模方法

## 定义

弱电网（Weak Grid）指电网短路容量与并网变流器额定容量之比（Short Circuit Ratio, SCR）低于特定阈值的交流电网。当SCR较小时，电网等效阻抗相对增大，并与并网变流器的锁相环（PLL）控制产生耦合，形成负阻效应，导致传统基于强电网经验的控制参数失效。

**短路比（SCR）**定义为：

$$SCR = \frac{S_{SC}}{P_n} = \frac{V_{g,rms}^2 / |Z_{grid}|}{P_n}$$

其中 $S_{SC}$ 为电网短路容量，$P_n$ 为变流器额定功率，$V_{g,rms}$ 为电网额定电压有效值，$Z_{grid}$ 为电网等效阻抗。

**复短路比（CSCR）**计及电网电阻-电抗比（R/X）的影响：

$$CSCR = \frac{S_{SC}}{P_n} \cdot \frac{1}{\sqrt{1 + (R/X)^2}}$$

**耦合强度系数**（Carreño 2026）$\kappa$ 描述PLL带宽与电网强度的耦合关系：

$$\kappa = \frac{K_p \cdot i_P \cdot L}{\omega_n}$$

其中 $K_p$ 为PLL比例增益，$i_P$ 为有功电流，$L$ 为电网等效电感，$\omega_n = 2\pi f_n$ 为额定角频率。

**电网强度分类标准**：

| 电网强度 | SCR范围 | 主导特性 | 典型控制策略 |
|---------|---------|---------|-------------|
| 强电网 | SCR > 5 | 电网阻抗可忽略，PLL带宽设计无约束 | GFL + SRF-PLL |
| 中等电网 | 3 ≤ SCR ≤ 5 | 电网阻抗影响显现，需限制PLL带宽 | GFL + DSOGI-PLL |
| 弱电网 | SCR < 3 | PLL与电网强耦合，失稳风险高 | 改进DSOGI-PLL / GFM |
| 极弱电网 | SCR < 2 | 传统GFL控制基本失效 | GFM + 下垂/EVR控制 |

## EMT中的角色

弱电网VSC建模在EMT仿真中具有特殊重要性，因为：

1. **PLL动态与电网阻抗的相互作用**：弱电网中电网阻抗$L$增大，使PLL的$d q$同步参考框架与实际电网电压之间产生相位误差，该误差通过PLL反馈控制形成正反馈回路，可能导致小信号失稳。

2. **GFL/GFM混合并网场景**：高比例新能源系统中，跟网型（GFL）和构网型（GFM）VSC共存于同一弱电网。GFM提供电压/频率支撑，GFL负责功率追踪，两者控制交互、功率分配和故障穿越协调需要精确的EMT模型验证。

3. **实时仿真的精度-效率权衡**：大规模弱电网系统若采用全开关EMT模型，计算代价过高；而传统RMS模型会漏掉PLL相关的失稳机制（如跨临界分岔和Hopf分岔）。需要发展针对弱电网场景的专用降阶等效模型。

4. **PQ能力边界的动态变化**：GFM VSC的功率能力边界受PCC电压、直流母线电压、滤波器拓扑影响动态变化，需要实时计算效率高的等效模型。

## EMT建模方法

### 方法1：EIBR等效时域模型（Luchini 2023）

等效跟网型变流器（Equivalent Grid-Following Inverter-Based Generator, EIBR）模型采用"PLL同步 + 瞬时功率反解dq电流 + 受控电流源"架构，其核心等效电路如**图2**所示。

**PLL同步环节（DSOGI-PLL）**：

PLL采用双二阶广义积分器（DSOGI）结构，从三相电网电压 $V_{abc}$ 中提取正序分量：

$$V_{\alpha\beta} = T_{\alpha\beta} V_{abc}$$

其中 $\alpha\beta$ 变换矩阵：

$$T_{\alpha\beta} = \frac{2}{3}\begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix}$$

DSOGI在 $\alpha\beta$ 坐标系下产生两路正交信号，经Park变换得到 $dq$ 轴电压分量，再经过PI控制器输出同步角 $\theta_{PLL}$。

**dq坐标系瞬时功率反解**：

由瞬时功率理论，$dq$ 坐标系下的有功功率 $P$ 和无功功率 $Q$ 为：

$$P = v_d i_d + v_q i_q$$
$$Q = v_q i_d - v_d i_q$$

根据功率命令 $(P^*, Q^*)$ 和电网电压角度 $\theta_{PLL}$，反解得到目标电流指令：

$$i_d^* = \frac{P^* v_d + Q^* v_q}{v_d^2 + v_q^2}$$
$$i_q^* = \frac{Q^* v_d - P^* v_q}{v_d^2 + v_q^2}$$

**受控电流源等效接口**：

EIBR模型将VSC等效为受控电流源，其输出电流为：

$$i_{GF L} = \frac{P^* - jQ^*}{v_{PCC}^*}$$

故障工况下，EIBR模型通过限幅环节处理电流过载，输出电流平均误差为 **2.33%**，仿真执行时间降低约 **70%**（对比全开关EMT模型）。

### 方法2：DIBM离散阻抗建模（Vahabzadeh 2025）

离散阻抗建模（Discretized Impedance-Based Modeling, DIBM）将VSC导纳模型通过梯形积分离散化，转换为戴维南等效接口，显著降低状态变量数目。

**VSC导纳模型的$s$域表达**（以LCL滤波器为例）：

$$i_{VSC,dq} = A_{VSC,dq}(s) v_{PCC,dq} + B_{VSC,dq}(s) i_{VSC,dq}$$

其中传递函数矩阵：

$$A_{VSC,dq}(s) = \frac{2}{sL_f + s(r_f - k_p) - k_i} I_2$$
$$B_{VSC,dq}(s) = \frac{2(sL_f + s r_f + k_p) + k_i}{sL_f + s(r_f - k_p) - k_i} I_2$$

**梯形积分离散化**：

对连续导纳模型进行$z$域离散化（$z^{-1}$ 对应单步延时 $\Delta t$）：

$$i_{VSC,dq}(z) = \frac{a_0 + a_1 z^{-1} + a_2 z^{-2}}{b_0 + b_1 z^{-1} + b_2 z^{-2}} v_{PCC,dq}(z)$$

离散化后状态数从 **271** 降至 **43**（降幅 **84.1%**），最大仿真步长从 $80\,\mu s$ 提升至 $1\,ms$（步长扩大 **12.5倍**）。

**戴维南等效接口**：

DIBM将VSC转换为戴维南等效形式：

$$v_{th} = R_{th} \cdot i_{VSC} + L_{th} \cdot \frac{di_{VSC}}{dt}$$

便于与EMT网络方程联立求解。

### 方法3：RMS+增强电路模型（Carreño 2026）

RMS+模型从慢快系统理论出发，将网络方程分解为代数部分（RMS模型）和动态部分（PLL耦合项），从而捕获传统RMS模型漏掉的PLL小信号失稳机制。

**慢快系统分解**：

考虑简单VSC-无限母线系统，PLL输出角 $\delta$ 与电网电压角 $\theta_g$ 的动态方程可表示为慢快系统：

$$\varepsilon \dot{z} = g(x, z, \varepsilon)$$

其中 $x$ 为快变量（电磁暂态），$z$ 为慢变量（PLL同步角）。当 $\varepsilon \to 0$ 时，系统退化为代数约束 $g(x, z, 0) = 0$，其根 $z = h(x)$ 给出准稳态流行。

**RMS+状态空间表达**：

RMS+将支路电流表达为代数部分与动态部分之和：

$$i_{Br} = \underbrace{\frac{v_{GF L} - V}{Z_{eq}}}_{\text{RMS代数部分}} + \underbrace{\frac{L}{Z_{eq}} \cdot \frac{di_{GF L}}{dt}}_{\text{动态修正项}}$$

等效电感参数 $L$ 的计算公式：

$$L = \frac{\sum_{k} L_k a_k}{\sum_{k} a_k}, \quad a_k = \frac{R_k + jX_k}{R_k + jX_k + j\omega_n L_k}$$

**PLL小信号稳定性边界**：

RMS+模型揭示了三种小信号失稳机制：

| 失稳类型 | 稳定性条件 | 物理含义 |
|---------|-----------|---------|
| 电压失稳 | $V > \|i_P X\|$ | 电网电压需大于电抗压降 |
| 跨临界分岔 | $1 - K_p i_P L > 0$ | PLL比例增益超过极限 |
| Hopf分岔 | $K_p V^2 - (i_P X)^2 - K_i i_P L > 0$ | PI积分增益与比例增益之比超限 |

**IEEE 39节点验证**：RMS+模型在IEEE 39节点系统中状态数减少 **75-80%**，特征值预测误差 < **5%**。

### 方法4：DSOGI-PLL改进型（Ranasinghe 2024）

改进型DSOGI-PLL引入暂态检测器（频率冻结）和自适应带宽机制，适用于极弱电网（SCR ≈ 1.8）。

**SRF-PLL基本结构**：

三相电网电压经Park变换至旋转参考系：

$$v_{dq} = T_{dq}(\theta_{PLL}) v_{abc}$$

其中 $T_{dq}$ 为Park变换矩阵。PI控制器输出角频率偏差 $\Delta\omega = K_p \varepsilon + K_i \int \varepsilon\, dt$，其中误差信号 $\varepsilon = v_q$（q轴电压在稳态下为0）。

**DSOGI正交信号生成**：

双二阶广义积分器（DSOGI）在 $\alpha\beta$ 坐标系下产生正交信号：

$$D_{DSOGI}(s) = \frac{\omega_0^2}{s^2 + \omega_0^2}, \quad Q_{DSOGI}(s) = \frac{s\omega_0}{s^2 + \omega_0^2}$$

**暂态检测与自适应带宽**：

当检测到电网频率突变（$|\Delta f| > f_{th}$）时，冻结PLL带宽（$K_p \to 0$，$K_i \to 0$），待电网电压恢复后再逐步释放带宽：

$$K_p(t) = \begin{cases} 0 & \text{暂态期间} \\ K_{p,0} \cdot (1 - e^{-\alpha t}) & \text{恢复期间} \end{cases}$$

**IEEE 9节点测试结果**（SCR ≈ 1.8）：不对称故障下调节时间缩短 **60%**，相位超调降低 **58.5%**，频率跟踪RMSE降至 **0.001 Hz**（降幅 **99.95%**）。

### 方法5：GFM构网型控制（EVR/CPID）

极弱电网（SCR < 2）下GFL控制基本失效，需采用构网型（Grid-Forming, GFM）控制。

**下垂控制基本方程**：

GFM采用P-f和Q-V下垂关系：

$$f - f_0 = -K_p (P - P_0), \quad V - V_0 = -K_q (Q - Q_0)$$

**CPID（Constant Power Infinite Bus）控制**：

CPID控制在并网模式下模拟无限电网特性，在孤岛模式下切换为V-f控制：

$$v_{PCC} = V_{ref} \angle \theta_{CPID}, \quad \theta_{CPID} = \int (\omega_0 + K_\omega P)\, dt$$

**EVR（Enhanced Virtual Resistance）**：

EVR在dq坐标系下引入虚拟阻抗以阻尼谐振：

$$v_{dq} = R_v i_{dq} + L_v \frac{di_{dq}}{dt} + v_{grid,dq}$$

Nurunnabi 2025实验结果表明：EVR策略在动态负载下电压偏差 < **2.9%**，频率偏差 < **0.37%**。

## 形式化表达

### SCR与耦合强度

$$SCR = \frac{V_{g,rms}^2}{|Z_{grid}| P_n} = \frac{V_{g,rms}^2}{\sqrt{R_{grid}^2 + X_{grid}^2} \cdot \frac{1}{P_n}$$

### EIBR模型电流输出

$$i_{GF L} = \frac{P^* - jQ^*}{v_{PCC}^*} \cdot H_{PLL}(s) \cdot H_{LPF}(s)$$

### DIBM离散阻抗

$$i_{VSC}(k) = \frac{a_0 v_{PCC}(k) + a_1 v_{PCC}(k-1) + a_2 v_{PCC}(k-2)}{b_0 + b_1 z^{-1} + b_2 z^{-2}}$$

### RMS+慢快分解

$$\varepsilon \dot{z} = g(x, z, \varepsilon), \quad x = f(x, h(x), 0)$$

### RMS+稳定性边界

$$\text{电压稳定：} V > |i_P X|$$
$$\text{跨临界分岔：} 1 - K_p i_P L > 0$$
$$\text{Hopf分岔：} K_p V^2 - (i_P X)^2 - K_i i_P L > 0$$

### GFM下垂方程

$$\omega = \omega_0 - K_\omega (P - P_0), \quad V = V_0 - K_v (Q - Q_0)$$

## 关键技术挑战

### 挑战1：PLL带宽与电网强度的耦合设计

弱电网中电网阻抗增大导致PLL与电网形成负阻效应，传统基于强网经验的PLL参数整定方法失效。需要建立PLL参数（$K_p$, $K_i$）与SCR之间的定量映射关系。Carreño (2026) 给出的耦合强度系数 $\kappa$ 提供了方向，但实际工程中还需考虑谐波、不平衡、频率斜坡等多重扰动下的综合影响。

### 挑战2：GFL/GFM在弱电网中的混合协调

高比例新能源并网系统中，GFL和GFM VSC往往共存于同一弱电网中。GFM提供电压/频率支撑，GFL负责功率追踪，两者之间的控制交互、功率分配、故障穿越协调尚缺乏系统性的建模框架。Nurunnabi (2025) 在100 kVA实验中验证了GFM/GFL并联运行的可行性，但大规模系统中的动态协调问题仍需深入研究。

### 挑战3：EMT仿真效率与精度的权衡

弱电网VSC建模需要在仿真精度和计算效率之间取得平衡。全开关EMT模型精度高但计算量大，RMS模型效率高但漏掉关键失稳机制。Carreño (2026) 的RMS+和Vahabzadeh (2025) 的DIBM分别从中低频模态分析和实时仿真角度给出了折中方案，但针对弱电网特定场景的专用降阶模型仍需发展。

### 挑战4：PQ能力边界的动态更新

GFM VSC的PQ能力边界随PCC电压、直流母线电压、滤波器拓扑动态变化。Nurunnabi (2025) 给出了RIC与PWM约束圆的几何交集算法，但实时计算效率、边界突变时的控制器切换逻辑、以及多逆变器并联时的PQ边界叠加效应仍需深入研究。

## 量化性能边界

### SCR稳定边界

| 控制类型 | PLL/控制策略 | 稳定下限SCR | 数据来源 |
|---------|-------------|------------|---------|
| GFL | SRF-PLL, 带宽30-50 Hz | ≈ 2.0-2.5 | 文献综合 |
| GFL | 改进DSOGI-PLL（Ranasinghe 2024） | ≈ 1.0 | IEEE 9节点, SCR≈1.8 |
| GFM | 下垂控制 | ≈ 1.0-1.5 | Nurunnabi 2025 |

### PLL暂态性能（SCR ≈ 1.8, IEEE 9节点, Ranasinghe 2024）

| 测试场景 | 传统DSOGI-PLL | 改进DSOGI-PLL | 改善幅度 |
|---------|--------------|--------------|---------|
| 不对称故障调节时间 | 0.040 s | 0.016 s | 缩短60% |
| 不对称故障超调量 | 0.272 rad | 0.113 rad | 降低58.5% |
| 90°相位跳变调节时间 | 0.15 s | 0.03 s | 缩短80% |
| 90°相位跳变超调量 | 2.003 rad | 1.719 rad | 降低14.2% |
| 频率跟踪RMSE (8-9s) | 2.16 Hz | 0.001 Hz | 降幅99.95% |

### 等效模型精度与效率

| 模型类型 | 测试场景 | 误差 | 效率提升 | 数据来源 |
|---------|---------|------|---------|---------|
| EIBR (Luchini 2023) | ATP/ATPDraw故障工况 | 2.33% | 时间降低70% | ATP/ATPDraw |
| DIBM (Vahabzadeh 2025) | 7节点VSC系统, 200 μs步长 | < 0.5% | 状态数降84.1% | MATLAB/OPAL-RT |
| DIBM (Vahabzadeh 2025) | 最大步长 | 80 μs → 1 ms | 步长扩大12.5倍 | MATLAB/OPAL-RT |
| RMS+ (Carreño 2026) | IEEE 39节点, 多GFL | 特征值误差<5% | 状态数降75-80% | MATLAB模态分析 |

### GFM PQ能力与初始化

| 指标 | 数值 | 数据来源 |
|------|------|---------|
| SVPWM最大输出电压 | 1.53 p.u.（SPWM为1.33 p.u.） | Nurunnabi 2025 |
| EVR电压最大偏差 | < 2.9% | Nurunnabi 2025 |
| EVR频率最大偏差 | < 0.37% | Nurunnabi 2025 |
| CISS/DI初始化加速比 | 6.9倍 | Allabadi 2024, CIGRE BM4 |

## 适用边界与选择指南

### 场景-方法推荐表

| 应用场景 | SCR范围 | 推荐模型/方法 | 关键约束 |
|---------|--------|--------------|---------|
| 强电网VSC并网 | SCR > 5 | 标准GFL + SRF-PLL | 可直接沿用同步机控制参数 |
| 中等电网VSC并网 | 3 ≤ SCR ≤ 5 | GFL + DSOGI-PLL | 需限制PLL带宽 < 谐振频率 |
| 弱电网VSC并网 | SCR < 3 | 改进DSOGI-PLL / GFM | 需暂态检测器或无PLL控制 |
| 极弱电网/孤岛 | SCR < 2 | GFM + 下垂/EVR控制 | GFL控制基本失效 |
| 大规模系统EMT | 任意 | EIBR等效模型 | 精度误差 < 3%, 效率提升70% |
| 实时仿真 | 任意 | DIBM离散阻抗接口 | 步长可达1 ms, 状态数降84% |
| 小信号稳定性分析 | 任意 | RMS+增强电路模型 | 状态数降75%, 精度保持EMT级 |
| 黑盒GVSC初始化 | 任意 | CISS / DI方法 | 初始化时间缩短6.9倍 |

### 失效边界

- **SCR < 1.0**：多数GFL控制失效，需采用GFM或混合控制
- **极弱电网大扰动**：线性化小信号模型不适用，需完整EMT仿真
- **不同PLL结构**：SRF/DSOGI/延时信号消除在相同SCR下的稳定性边界不同，不可泛化
- **开关级谐波分析**：等效模型（EIBR/DIBM）不适用，需全开关EMT模型
- **时间尺度分离假设不成立**：当 $\tau_f / \tau_s \geq 0.3$ 时，RMS+近似误差显著增大，需采用高阶修正

## 相关模型

- [[vsc-model|VSC模型]] - 通用VSC EMT模型
- [[gfl-inverter-model|跟网型逆变器模型]] - GFL VSC建模
- [[gfm-inverter-model|构网型逆变器模型]] - GFM VSC建模
- [[pll-model|PLL模型]] - 锁相环建模与稳定性分析
- [[average-value-model|平均值模型]] - VSC平均化建模方法

## 相关方法

- [[vector-control-model|矢量控制]] - dq坐标系控制策略
- [[grid-forming-control|构网控制]] - 弱网稳定控制策略
- [[impedance-modeling|阻抗建模]] - 弱网稳定性分析
- [[frequency-scan|频率扫描]] - SCR/CSCR判别方法
- [[dsogi-pll|DSOGI-PLL]] - 改进型锁相环
- [[small-signal-stability|小信号稳定性]] - 弱网稳定性分析

## 相关主题

- [[vsc-hvdc|VSC-HVDC]] - 高压直流输电系统
- [[renewable-energy-integration|新能源并网]] - 弱电网接入挑战
- [[small-signal-stability|小信号稳定性]] - 弱网稳定性评估
- [[large-scale-system-simulation|大规模系统仿真]] - 等效建模需求

## 来源论文

- **Ranasinghe 等 (2024)** - "Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inverter Control Systems" (IEEE PESGM 2024)。提出改进型DSOGI-PLL，引入暂态检测器（频率冻结）和自适应带宽机制，在SCR ≈ 1.8的极弱电网中实现不对称故障下调节时间缩短60%、相位超调降低58.5%、频率跟踪RMSE降至0.001 Hz（降幅99.95%），系统临界稳定SCR从2.3扩展至1.0。

- **Carreño 等 (2026)** - "RMS+: Augmenting the Traditional Circuit Model to Capture PLL Instability" (IEEE Trans. Power Delivery, Vol. 41, No. 1)。从慢快系统理论出发，提出RMS+增强电路模型，揭示传统RMS模型因忽略电感"di/dt"效应而完全漏掉PLL与网络交互的两种失稳机制（跨临界分岔和Hopf分岔），在IEEE 39节点系统中状态数减少75-80%且特征值预测误差 < 5%。

- **Allabadi 等 (2024)** - "Initializing EMT models of grid forming VSCs in MTDC systems" (Electric Power Systems Research, Vol. 235)。针对MTDC系统中GVSC的EMT初始化难题，提出CISS稳态控制初始化和DI解耦接口法，在CIGRE BM4基准系统中将完整系统初始化时间缩短6.9倍，DI方法成功适用于黑盒GVSC模型。

- **Nurunnabi 等 (2025)** - "Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis" (IEEE Access)。提出综合考虑PWM饱和与额定电流约束的GFM逆变器PQ能力边界建模方法，推导L/LC/LCL三种耦合滤波器下的PCC点功率方程，给出RIC与PWM约束圆的几何交集算法，EVR策略在动态负载下电压偏差 < 2.9%、频率偏差 < 0.37%。

- **Luchini 等 (2023)** - "Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations" (Electric Power Systems Research)。提出适用于EMTP的跟网型IBR等效时域模型（EIBR），采用"PLL同步+瞬时功率反解dq电流+受控电流源"架构，在故障条件下输出电流平均误差2.33%，仿真执行时间降低约70%。

- **Vahabzadeh 等 (2025)** - "Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Real-Time EMT Simulators" (IEEE Open J. Power Electronics)。提出离散阻抗建模（DIBM）方法，将VSC导纳模型通过梯形积分离散化并转换为戴维南等效接口，在7节点VSC系统（20台VSC）中状态数从271降至43（降幅84.1%），最大仿真步长从80 μs提升至1 ms。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。量化数据均标注来源论文，未报告的数据已明确标注数据缺口。*
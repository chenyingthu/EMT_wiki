---
title: "磁饱和建模 (Magnetic Saturation Modeling)"
type: method
tags: [magnetic-saturation, transformer, nonlinear, iron-core, saturation, jiles-atherton, preisach]
created: "2026-05-02"
updated: "2026-05-16"
---

# 磁饱和建模 (Magnetic Saturation Modeling)

## 定义与边界

磁饱和建模是在 EMT 中描述铁磁元件磁链、磁通密度、励磁电流和磁滞历史之间非线性关系的方法。它的输入通常包括磁化曲线、剩磁或初始磁链、铁芯几何、绕组连接、漏磁路径、损耗参数和数值积分设置；输出是可接入电路网络的非线性电感、励磁支路、磁等效电路或变压器拓扑模型。

本页关注磁饱和作为方法如何进入 EMT，不替代 [[transformer-model]]、[[multi-winding-transformer]] 或 [[ferroresonance]] 的设备/现象页。它也不覆盖完整三维有限元建模；若研究局部漏磁、绕组热点或结构件涡流，应把 EMT 模型与有限元或测量证据分开说明。

## EMT 中的角色

磁饱和会影响励磁涌流、铁磁谐振、地磁感应电流、变压器投切过电压、二次谐波制动、直流偏磁和铁芯电抗器暂态。EMT 需要在每个时间步把非线性磁化支路转换为节点方程可求解的等效导纳和历史项，或通过迭代直接求解非线性方程。

该方法的关键不是只给一条 $B-H$ 曲线，而是说明该曲线放在什么磁路拓扑位置、使用什么状态变量、如何初始化剩磁、如何处理段间切换和如何验证波形。错误的励磁支路位置可能产生看似数值问题的物理拓扑错误；相关边界可与 [[duality-based-transformer-modeling-for-low-frequency-transients]] 的变压器对偶建模证据互相参照。

## 核心机制

### 非线性磁链-电流关系

EMT 中常用磁链-电流关系表示饱和：

$$\lambda = f(i_m), \quad v = \frac{d\lambda}{dt}$$

其中 $\lambda$ 是励磁支路磁链，$i_m$ 是磁化电流，$v$ 是对应绕组或支路电压。若采用磁通密度和磁场强度，则材料层面写为：

$$B = f(H)$$

但 EMT 电路求解通常需要把它转换为端口电压、电流和磁链关系。分段线性模型在当前工作点使用增量电感 $L_k = d\lambda/di$；解析模型可用 Frohlich、双曲正切、指数或多项式形式拟合磁化曲线；磁滞模型则还需历史变量，例如反转点栈或 Preisach/Jiles-Atherton 状态。

梯形积分下，非线性电感常被写成伴随形式：

$$i_{n+1} = G_{\mathrm{eq}}(\lambda, i)\, v_{n+1} + I_{\mathrm{hist}}$$

其中 $G_{\mathrm{eq}}$ 和历史项随工作点更新。若工作点跨越膝点或分段边界，应通过插值、子步长或牛顿迭代避免人工跳变。

### Jiles-Atherton 磁滞模型（ψ-i 接口形式）

经典 Jiles-Atherton (JA) 模型以 $B-H$ 和 $M-H$ 磁学量表述，但 EMT 程序通常以节点电压、支路电流、磁链为接口。Sima 等 (2018) 将 JA 模型改写为磁链-电流 $\psi$-$i$ 形式，以便在 EMTP-ATP 中实现。

有效磁场定义为：

$$H_e = H + \alpha M$$

其中 $\alpha$ 是磁畴间耦合系数。无磁滞磁化曲线采用 Langevin 函数形式：

$$M_{an}(H_e) = M_s \left[\coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e}\right]$$

其中 $M_s$ 为饱和磁化强度，$a$ 为无磁滞形状因子。也可采用修正 AMC 形式替代 Langevin 函数以改善材料拟合：

$$M_{an} = M_s \frac{a_1 H_e + H_e^2}{a_3 + a_2 H_e + H_e^2}$$

JA 磁滞微分方程为：

$$\frac{dM}{dH} = \frac{M_{an} - M + \frac{k\delta c}{1-c}\frac{dM_{an}}{dH_e}}{\alpha(M - M_{an}) + \frac{k\delta}{1-c}\left(1 - \alpha c \frac{dM_{an}}{dH_e}\right)}$$

其中 $k$ 为矫顽场幅度参数，$c$ 为可逆磁化权重因子，$\delta$ 为方向参数（$dH/dt > 0$ 时取 +1，否则取 −1）。通过几何关系将磁学变量转换为电路接口量：

$$\psi = N A B = N A \mu_0 (H + M), \quad i = \frac{H l}{N}$$

端口满足 $v = d\psi/dt$。

### 分段线性（Piecewise Linear, PWL）磁化曲线

对于感应电机的电压后电抗（VBR）模型，Wang 和 Jatskevich (2010) 将饱和特性表征为分段线性近似。主磁链与总磁化电流之间的非线性饱和特性函数为：

$$\lambda_m = f(i_m)$$

增量电感定义为：

$$L_d = \frac{d\lambda_m}{di_m}$$

在 PWL 近似中，$\lambda$/$i$ 曲线被划分为若干线性段，每段用增量电感 $L_k$ 和剩余磁链 $\lambda_{\mathrm{bias}}$ 表示。在 EMT 伴随电路形式下：

$$i_{n+1} = \underbrace{\frac{L_k}{\Delta t}}_{G_{\mathrm{eq}}} v_{n+1} + \underbrace{\left(i_n - \frac{L_k}{\Delta t} v_n - \frac{\lambda_{\mathrm{bias}}}{\Delta t}\right)}_{I_{\mathrm{hist}}}$$

dq 轴静态与动态交叉饱和通过主磁化电流幅值 $|\lambda_m| = \sqrt{\lambda_{dm}^2 + \lambda_{qm}^2}$ 共同决定等效增量电感，避免迭代求解的同时保留交叉耦合效应。

### 对偶磁路建模

Jazebi 等 (2016) 基于对偶原理提出变压器低频暂态拓扑建模方法。基本映射规则为：

$$\mathcal{R} \leftrightarrow L, \quad \mathcal{F} \leftrightarrow I, \quad \text{节点} \leftrightarrow \text{回路}$$

即磁阻对应电感、磁动势源对应电流源、拓扑结构节点与回路互换。该方法将铁芯几何结构映射为等效磁阻网络，再转换为可在 EMTP 中实现的电气网络。关键原则是：励磁支路必须按铁芯磁通路径放在正确的对偶拓扑位置，不能为方便计算任意放在 T 型或星型等值中心。

三绕组变压器中负电感星型等效、互感耦合与 BCTRAN 模型的端口阻抗矩阵数学严格等价。传统 T 型模型在铁芯深度饱和工况下，因励磁支路拓扑错位导致数值振荡，仿真发散率 >80%；采用正确对偶拓扑后全工况收敛率 100%。

### 磁等效电路（MEC）建模

Liu 和 Dinavahi (2016) 提出基于非线性磁等效电路的 Sen 变压器实时 EMT 模型。将变压器分解为：磁动势（MMF）源、非线性铁芯磁导（考虑饱和与磁滞）、线性漏磁磁导和零序磁导。MEC 方程为：

$$\mathbf{F} = \mathbf{P}^{-1} \boldsymbol{\Phi} - \mathbf{N} \mathbf{i}$$

其中 $\mathbf{F}$ 为磁动势向量，$\mathbf{P}$ 为磁导矩阵，$\boldsymbol{\Phi}$ 为磁通向量，$\mathbf{N}$ 为匝数矩阵，$\mathbf{i}$ 为电流向量。Preisach 磁滞模型通过反转点栈（RPS）算法实现，可追踪多达 20 个磁化反转点历史。

### 同步机交叉磁化效应

Dehkordi (2026) 提出的同步电机饱和模型将判据从单纯轴向幅值扩展为气隙 MMF 的幅值与空间角度。dq 轴磁化电感的饱和模型为：

$$L_{md} = K_{sd} \cdot L_{mdu}, \quad L_{mq} = K_{sq} \cdot L_{mqu}$$

其中 $K_{sd}$、$K_{sq}$ 为饱和因子，$L_{mdu}$、$L_{mqu}$ 为不饱和值。总磁链幅值为：

$$\Psi_{at} = \sqrt{\Psi_{md}^2 + \Psi_{mq}^2}$$

关键发现：忽略 q 轴饱和（设 $K_{sq} = 1$）的简化模型在隐极机额定负载下导致端电压预测误差达 5-8%，功角误差 3-5 度；采用单一饱和指数 $\Psi_{at}$ 的方法无法区分 MMF 角度变化，在负载功率因数从 1.0 变化到 0.8 滞后时，带载能力预测偏差达 10-15%。

## 分类与变体

| 模型路线 | 状态/参数 | 优点 | 边界 |
|----------|-----------|------|------|
| 分段线性磁化曲线 | 分段点、增量电感、初始磁链 | EMT 实现直接，便于实时仿真 | 膝点附近可能产生切换误差 |
| 解析饱和函数（Frohlich/tanh/指数/多项式） | 参数集（$M_s$、$a$、$\alpha$、$k$、$c$） | 连续可微，便于牛顿迭代 | 参数物理含义可能较弱 |
| Jiles-Atherton 磁滞模型（ψ-i 接口） | 5 个 JA 参数 + 方向参数 $\delta$ | 可描述主回线和小回线，含磁化历史 | 参数辨识和实时实现更复杂 |
| Preisach 磁滞模型 | 反转点栈（RPS），最多 20 个历史点 | 精确追踪磁滞记忆，对任意磁化路径适用 | 计算量和内存随历史点数量增长 |
| 磁等效电路（MEC） | 几何磁导网络、MMF 源、漏磁路径 | 能保留铁芯拓扑和多绕组耦合 | 需要几何和磁路信息，计算量较大 |
| 对偶电路模型 | 磁路拓扑到电路拓扑映射（双侧对偶） | 励磁支路位置与铁芯磁路一致 | 低频拓扑原则不等同于高频绕组模型 |
| dq 轴交叉饱和模型 | MMF 幅值 + 角度、$K_{sd}$、$K_{sq}$ | 区分 d/q 轴饱和与转子几何结构 | 忽略空间谐波，不适用于高次谐波丰富的场景 |

## 形式化表达

### 基本电磁关系

$$\lambda = f(i_m), \quad v = \frac{d\lambda}{dt}$$

$$i_{n+1} = G_{\mathrm{eq}}(\lambda, i)\, v_{n+1} + I_{\mathrm{hist}}$$

### JA 模型无磁滞磁化（Langevin 函数）

$$M_{an}(H_e) = M_s \left[\coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e}\right]$$

### JA 磁滞微分方程

$$\frac{dM}{dH} = \frac{M_{an} - M + \frac{k\delta c}{1-c}\frac{dM_{an}}{dH_e}}{\alpha(M - M_{an}) + \frac{k\delta}{1-c}\left(1 - \alpha c \frac{dM_{an}}{dH_e}\right)}$$

### ψ-i 转换关系

$$\psi = N A \mu_0 (H + M), \quad i = \frac{H l}{N}$$

### PWL 增量电感伴随形式

$$i_{n+1} = \frac{L_k}{\Delta t} v_{n+1} + \left(i_n - \frac{L_k}{\Delta t} v_n - \frac{\lambda_{\mathrm{bias}}}{\Delta t}\right)$$

### 对偶变换映射

$$\mathcal{R} \leftrightarrow L, \quad \mathcal{F} \leftrightarrow I, \quad \text{节点} \leftrightarrow \text{回路}$$

### MEC 基本方程

$$\mathbf{F} = \mathbf{P}^{-1} \boldsymbol{\Phi} - \mathbf{N} \mathbf{i}$$

### 同步机 dq 轴饱和因子

$$L_{md} = K_{sd} \cdot L_{mdu}, \quad L_{mq} = K_{sq} \cdot L_{mqu}$$

$$\Psi_{at} = \sqrt{\Psi_{md}^2 + \Psi_{mq}^2}$$

## 量化性能边界

| 建模方法 | 代表工作 | 量化性能数据 | 验证条件 |
|----------|----------|--------------|----------|
| JA 磁滞模型（ψ-i 接口） | Sima 等 2018 | 在 50Hz 和 150Hz 电流测试中，动态 Model 1 比 Model 2 更匹配实验结果 | 环形铁芯电抗器，EMTP-ATP Type-94 元件 |
| 现场投切饱和曲线辨识 | Canal 2021 | 励磁电流总误差 0.6%；饱和电感均值 0.833 H（标准差 0.053 H）；传统方法高估约 15.1%；饱和电感每高估 10% 导致过电压约束低估约 30% | 法国核电站 96 MVA/410/6.8 kV/Ynd11 变压器，9 次有效投切 |
| 饱和 VBR 感应电机 | Wang 和 Jatskevich 2010 | 100 μs 大时间步长下电流峰值误差 <0.8%（传统 PD 模型 >5% 且发散）；CPU 时间减少约 35-40%；内存占用降低约 25%；分段数增至 10 段时 RMSE <0.1% | 感应电机直连无穷大电网，三相短路故障、负载阶跃 |
| 对偶磁路模型 | Jazebi 等 2016 | 深度饱和工况下传统 T 型发散率 >80%，正确对偶拓扑后收敛率 100%；双侧对偶模型电压转换误差从 >10% 降至 <0.5% | 壳式与芯式三绕组/四绕组电力变压器，EMTP-RV/PSCAD |
| Sen 变压器 MEC（FPGA） | Liu 和 Dinavahi 2016 | 仿真步长延迟 <10 μs；相比 CPU 实现降低 2 个数量级；磁通分布计算误差 <2% | Xilinx FPGA，JMAG 三维有限元验证 |
| 同步机交叉磁化模型 | Dehkordi 2026 | 忽略 q 轴饱和时隐极机端电压误差 5-8%，功角误差 3-5 度；单一饱和指数方法在 cosφ 从 1.0 到 0.8 变化时带载能力预测偏差 10-15% | 凸极和隐极同步机 50-500 MVA，RTDS 实时仿真 |

## 关键技术挑战

1. **磁化曲线参数辨识**：JA 模型需要 5 个物理参数（$M_s$、$a$、$\alpha$、$k$、$c$），Preisach 模型需要大量反转点实验数据。参数来源不明时，不应声明涌流、谐波或铁磁谐振结果具有定量精度。

2. **分段切换误差**：膝点附近的分段边界若不进行平滑插值，子步长或牛顿迭代，会在磁化曲线的非线性突变处产生数值跳变，导致时域波形出现异常尖峰或数值振荡。

3. **磁滞小回线与剩磁路径**：单值磁化曲线不能描述磁滞小回线和剩磁路径，而剩磁会显著改变投切涌流和铁磁谐振起始条件。初始磁链应作为工况输入报告，而非设为零。

4. **励磁支路拓扑位置**：把励磁支路随意放在端口等值中心可能得到正确短路阻抗但错误内部磁通路径，尤其在深度饱和时拓扑错误会引发数值振荡（传统 T 型发散率 >80%）。

5. **dq 轴交叉饱和与 MMF 角度**：传统 d/q 轴独立饱和模型忽略 MMF 空间角度的影响，导致隐极机带载能力预测偏差达 10-15%。需要通过气隙 MMF 幅值和角度共同评估饱和程度。

6. **动态铁损耦合**：静态 ψ-i 模型只能给出恒定或简单非线性电阻形式的铁损，不能反映涡流和剩余损耗随 dB/dt 或电压激励变化的动态特性。Type-94 元件等电压驱动动态损耗耦合是更准确的建模方法。

7. **实时仿真步长约束**：FPGA 实现中需要全并行流水线架构以满足 <10 μs 延迟要求，但磁滞状态更新（尤其是 Preisach 反转点栈）可能成为关键路径瓶颈。

## 适用边界与失败模式

- **磁化曲线来源不明时**，不应声明涌流、谐波或铁磁谐振结果具有定量精度。
- **忽略剩磁**会显著改变投切涌流和铁磁谐振起始条件；初始磁链应作为工况输入报告。
- **把励磁支路随意放在端口等值中心**可能得到正确短路阻抗但错误内部磁通路径。
- **只用单值磁化曲线**不能描述磁滞小回线、剩磁路径和频率相关铁损。
- **饱和支路与梯形积分、开关切换和保护逻辑耦合**时可能出现数值振荡；应区分数值离散问题和物理拓扑问题。
- **单个变压器、Sen transformer 或电抗器算例**只能支撑对应结构和参数，不能外推为所有铁芯设备。
- **dq 轴独立饱和模型**（忽略 MMF 角度）在隐极机额定负载下的端电压误差可达 5-8%，不适用于精确带载能力评估。
- **FPGA 实时实现的精度**受 32 位浮点字长限制（MEC 模型磁通分布误差 <2%），不适用于需要更高精度的高频暂态研究。

## 相关页面

- [[transformer-model]] 和 [[multi-winding-transformer]] 是磁饱和最常见的设备承载页；本页说明非线性支路和磁路方法。
- [[ferroresonance]] 是饱和电感与电容网络相互作用的现象页，依赖本页的非线性建模边界。
- [[steady-state-initialization]] 决定剩磁、初始磁链和故障前状态是否一致。
- [[companion-circuit]]、[[discretization-methods]] 和 [[numerical-integration-methods]] 说明非线性电感如何进入 EMT 步进求解。
- [[harmonic-analysis-methods]] 可用于分析饱和导致的波形畸变，但谐波结果必须绑定窗口和工况。
- [[frequency-dependent-modeling]] 与 [[wideband-modeling]] 处理频率相关端口模型；磁饱和模型处理非线性磁化，两者不能互相替代。
- [[induction-machine-model]] 中的 VBR 模型可纳入饱和特性（Wang 和 Jatskevich 2010）。
- [[synchronous-machine-model]] 中的 dq 轴饱和模型可扩展为交叉磁化形式（Dehkordi 2026）。

## 来源论文

- [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror]] — Sima 等 2018，将 JA 磁滞模型改写为 ψ-i 接口，通过 EMTP-ATP Type-94 元件实现电压驱动动态损耗，用于铁磁谐振研究。
- [[determination-of-the-saturation-curve-of-power-transformers-by-processing-transi]] — Canal 2021，基于现场投切暂态测量数据辨识变压器完整饱和曲线，励磁电流误差 0.6%，饱和电感高估问题修正。
- [[duality-based-transformer-modeling-for-low-frequency-transients]] — Jazebi 等 2016，对偶变压器拓扑建模，双侧对偶模型相比单侧误差从 >10% 降至 <0.5%，深度饱和收敛率 100%。
- [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag]] — Liu 和 Dinavahi 2016，Sen 变压器非线性 MEC 模型的 FPGA 实时实现，Preisach 磁滞 + 梯形法则离散化，<10 μs 延迟，误差 <2%。
- [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode]] — Wang 和 Jatskevich 2010，含饱和 VBR 感应电机模型，PWL 近似 + dq 交叉饱和，100 μs 步长误差 <0.8%，CPU 时间减少 35-40%。
- [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el]] — Dehkordi 2026，基于 MMF 幅值和角度的同步机交叉磁化饱和模型，忽略 q 轴饱和时误差 5-8%/3-5 度。
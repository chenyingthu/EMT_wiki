---
title: "机电暂态建模 (Electromechanical Modeling)"
type: method
tags: [electromechanical, transient, stability, rotor-angle, swing-equation, generator, classical-model, park-equation, DAE, electromechanical-electromagnetic-hybrid-simulation]
created: "2026-05-02"
updated: "2026-05-18"
---

# 机电暂态建模 (Electromechanical Modeling)

## 定义与边界

机电暂态建模是把同步机转子运动、励磁和调速等慢动态、负荷动态以及网络基频约束组织成可求解动态模型的方法。它关注扰动后功角、转速、机端电压和有功/无功交换的低频演化，通常用于暂态稳定、低频振荡和 EMT-TS 混合仿真的外部系统表示。

本页讨论"模型怎样构成"。它不替代 [[swing-equation]] 对转子运动方程的专门说明，也不替代 [[excitation-system]]、[[power-system-stabilizer]] 或 [[small-signal-stability]] 的控制/稳定性页面。若研究对象是开关过程、行波、谐波、非平衡瞬时电流或阀级换相，应使用 EMT 模型或在 [[electromechanical-electromagnetic-hybrid-simulation]] 中明确接口边界。

## EMT 中的作用

在纯 EMT 仿真中，机电模型常作为同步机机械子系统和控制子系统的一部分：电磁网络按瞬时值求解，转子机械方程按较慢状态推进，二者通过电磁转矩或电磁功率耦合。在混合仿真中，机电模型更常表示外部大电网，向 EMT 区域提供基频等值电压、阻抗或注入功率，并接收 EMT 区域提取的边界相量或功率。

因此，机电暂态建模的价值不是复现全部波形细节，而是在可接受计算量下保留影响同步稳定和低频动态的主导状态。模型边界必须说明：哪些设备在相量域表示，哪些设备保留 EMT 细节，边界量如何从瞬时波形转换为相量或序分量。

## 核心状态与方程结构

多机机电暂态模型通常写成 DAE：

$$
\dot{x}=f(x,y,u,t), \qquad 0=g(x,y,u,t)
$$

其中 $x$ 包括转子角、转速、暂态/次暂态电势、励磁和调速状态、动态负荷状态等；$y$ 包括节点电压幅值和相角、网络电流或代数控制变量；$u$ 表示故障、切除、控制参考和保护动作。

同步机机械接口通常来自转子功率不平衡：

$$
\dot{\delta}_i=\omega_i-\omega_s
$$

$$
M_i\dot{\omega}_i=P_{m,i}-P_{e,i}-D_i(\omega_i-\omega_s)
$$

这里 $P_{e,i}$ 不是固定函数，而由所选同步机电磁模型和网络代数方程共同决定。经典模型可把内部电势 $E'$ 视为恒定并通过电抗接入网络；两轴或次暂态模型则需要 $E'_q,E'_d,E''_q,E''_d$ 等状态与 d-q 电流共同更新。更详细的同步机表示见 [[synchronous-machine-model]]。

网络侧在机电暂态中通常采用基频相量约束：

$$
\bar{I}=Y(\sigma,t)\bar{V}
$$

其中 $\sigma$ 表示拓扑、故障类型和切除状态。对不平衡故障，可使用三序网络或三相相量模型；若负序、零序、直流偏置或谐波会影响结论，应避免只使用正序近似。

## 同步机电磁模型层级

机电暂态中的同步机电磁模型按精度从低到高分为五层，各层对 EMT 建模范畴的贡献和局限如下：

### 经典模型（$E'$ 近似恒定）

忽略阻尼绕组和励磁动态，假设内部电势幅值 $E'$ 在暂态过程中恒定。电磁方程退化为代数约束，通过暂态电抗 $X'_d$ 接入网络。精度最低但计算最快，适用于首摆功角稳定的快速筛查。

**EMT 建模要点**：只需注入恒定电压源与 $X'_d$ 串联，步长可取 1–10 ms。

### 两轴/暂态模型（保留 $E'_q,E'_d$）

保留 d/q 轴暂态电势差异和励磁绕组动态，阻尼绕组仍被忽略。电磁方程升为微分方程，需与转子运动方程联立迭代求解。

**EMT 建模要点**：需维护 $E'_q, E'_d$ 两个状态量，定子电压方程含 $\omega\psi_d, \omega\psi_q$ 耦合项，步长通常 0.5–2 ms。

### 次暂态/Park 模型（保留 $E''_q,E''_d$ 及阻尼绕组）

在暂态模型基础上进一步保留阻尼绕组产生的次暂态电势 $E''_q, E''_d$，能捕捉故障初期 $10$–$100$ ms 的快速电磁暂态。代价是状态数增多（d 轴 2 个阻尼绕组 + q 轴 1–2 个阻尼绕组）。

**EMT 建模要点**：dq 坐标系下 6–7 阶同步机模型，步长需降至 50–500 μs 才能保真。适用于需要与 EMT 接口的故障初期电流和转矩计算。

### Park 变换与dq坐标接口

无论采用哪一层同步机模型，电磁方程均需经 Park 变换投影至转子 dq 坐标系：

$$
\begin{bmatrix}v_d\\v_q\end{bmatrix}=
\begin{bmatrix}\cos\delta & \sin\delta\\-\sin\delta & \cos\delta\end{bmatrix}
\begin{bmatrix}v_a\\v_b\end{bmatrix}
$$

d 轴绕组磁链方程：

$$
\psi_d = L_d i_d - L_{ad} i_{fd} - L_{add} i_{kd}
$$

$$
\psi_{fd} = -L_{ad} i_d + L_{ffd} i_{fd} + L_{fkd} i_{kd}
$$

q 轴绕组磁链方程同理。该方程组构成机电暂态模型与网络代数方程耦合的核心。

### 动态负荷模型

感应电机或复合负荷的机电暂态特性通过定子暂态阻抗或机电转矩方程描述：

$$
\frac{T_j}{\omega_s}\frac{d\omega_m}{dt}=T_e(\omega_m, v)-T_L
$$

动态负荷对 FIDVR（空调压缩机堵转）场景的电压恢复特性有显著影响，参数不确定性是主要误差来源。

## EMT-机电混合仿真接口

混合仿真是机电暂态模型最重要的 EMT 应用场景。核心问题是如何在 EMT 区域（开关级细节）和 TS 区域（基频相量等值）之间建立误差可控的边界等值。

### 诺顿/戴维南接口

最常用的接口形式：将 TS 外部系统等值为诺顿电流源 $I_{eq}=Y_{eq}V_{bus}$ 并联导纳 $Y_{eq}$，或将 EMT 侧边界电压源与串联阻抗等值为戴维南形式。接口 PI 支路通过时域差分化后作为历史电流源注入网络方程。

### 动态相量接口模型（DPIM）

动态相量接口模型（DPIM）将接口线路的 PI 等值电路转化为动态相量域状态空间方程，替代传统 FFT/DFT 多周期采样参数提取：

$$
\frac{d\bar{I}_{line}}{dt}=j\omega_s\bar{I}_{line}+G\bar{V}_{send}-G\bar{V}_{recv}
$$

其中 $\bar{I}_{line}$ 为线路电流的基频动态相量。DPIM 将 $O(N^2\log N)$ 的 FFT 计算降为 $O(N^2)$ 矩阵运算，单步接口参数计算量降低约 1–2 个数量级，同时消除传统接口固有的 1 ms 采样延迟。

### 接口启动的钳位策略

混合仿真启动时，为避免潮流不匹配导致的暂态冲击，在接口母线并联幅值、相角与目标潮流一致的临时理想电压源，监测钳位电源输出功率。当功率低于额定直流功率的 5% 或达到预设时间（约 0.6 s）时切除，使 EMT 侧与 TS 侧从受控支撑过渡到自由耦合运行。

## 模型层级与变体

| 层级 | 主要假设 | 适用问题 | 主要边界 |
|------|----------|----------|----------|
| 经典模型 | $E'$ 近似恒定，忽略励磁和阻尼绕组细节 | 首摆功角稳定的初步筛查 | 不适合控制限幅、饱和和多摆阻尼研究 |
| 两轴/暂态模型 | 保留 d/q 轴暂态电势和电抗差异 | 多机暂态稳定、励磁影响 | 参数和初值一致性要求更高 |
| 次暂态/Park 模型 | 保留更快电磁状态和阻尼绕组近似 | EMT 接口、故障初期电流和转矩耦合 | 若仍在相量域求解，不能等同于全 EMT |
| 动态负荷模型 | 感应电机、恢复负荷或复合负荷 | FIDVR、电压恢复和低频动态 | 负荷参数和相别不确定性常主导误差 |
| 机电-EMT 接口模型 | 外部系统相量/序分量等值，内部区域 EMT | 大系统与局部电力电子或配电细节耦合 | 接口位置、提取窗和时序会引入误差 |

## 形式化表达

### 多机 DAE 系统

$$
\dot{x}=f(x,y,u,t),\quad 0=g(x,y,u,t)
$$

- 机械状态：$\delta_i$（功角），$\omega_i$（转速），$E'_i$ 或 $E''_i$（暂态/次暂态电势）
- 代数状态：$V_i$（幅值），$\theta_i$（相角），$I_i$（网络电流）

### 机电接口关键公式

**转子运动方程**（每机）：

$$
M_i\frac{d\omega_i}{dt}=P_{m,i}-P_{e,i}-D_i(\omega_i-\omega_s)
$$

**接口功率匹配**：

$$
P_{e,i}=Re(\bar{V}_i\bar{I}_i^*),\quad Q_{e,i}=Im(\bar{V}_i\bar{I}_i^*)
$$

**阻尼转矩系数**（Park 坐标系下）：

$$
D_{e,i}= \frac{\partial P_{e,i}}{\partial \Delta\omega_i}\bigg|_{\Delta\omega=0}
$$

### 动态相量域差分形式（DPIM）

$$
\frac{\bar{I}^{(k+1)}-\bar{I}^{(k)}}{\Delta t}=j\omega_0\bar{I}^{(k)}+G\bar{V}_{send}^{(k)}-G\bar{V}_{recv}^{(k)}
$$

等效导纳 $G=1/(R+j\omega_0 L)$ 用于 PI 线路段。

## 关键技术挑战

### 接口误差累积

当换流器有效短路比（ESCR）低于 2.5 时，换流器动态受邻近交流系统波形影响显著。波形畸变和接口时延（通常 1 交互步延迟）会放大整体误差，导致混合仿真精度退化。

### 离散事件同步

空调电机堵转、换相失败等离散事件的状态（哪一相、哪个换流器）必须作为外部输入传递给相量模型。若仅靠连续电压电流量对齐，相量模型可能判断出不同的堵转相数，导致 EMT-相量边界在切换点发散。

### 模式切换判据设计

故障后从混合模式切回纯相量域时，需同时满足：①故障清除后延迟 $0.2$ s；②边界电压变化率低于 $0.005$ pu；③双域边界电压偏差持续 $3$–$5$ 个工频周期低于 $0.005$ pu。三条件均满足后才触发切换，防止快暂态波动误触发。

### 缓冲区自动划分

对大规模交直流混联系统，哪些交流母线必须纳入 EMT 区域缺乏可重复判据。无功扰动–电压灵敏度法（S$_ {VQ}$=$\Delta V_i/\Delta Q_{inj}$）是量化接口边界电气影响范围的有效工具。

### 饱和与磁路非线性

饱和效应使 $d$ 轴电感随电流变化，$q$ 轴暂态特性与 $d$ 轴不再解耦。忽略饱和可能导致首摆后功角曲线与实测偏差 $10$%–$30$%。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 机电模型与混合模型主导频率偏差 | $<0.02$ Hz（0.357 vs 0.37 Hz） | Wang 等 2013，EPRI36 低频振荡分析 |
| 阻尼比偏差 | $<0.3$% | Wang 等 2013 |
| 直流功率/电压误差（混合仿真稳态） | $<1$% | Chen 等 2020，ADPSS 实测 |
| 触发角/关断角偏差 | $<1°$ | Chen 等 2020 |
| 钳位启动达稳态时间 | $<0.6$ s | Chen 等 2020 |
| 单方式建模时间压缩比 | 15 h → 0.5 h（30×） | Chen 等 2020 |
| DPIM 计算复杂度 | $O(N^2)$ vs FFT $O(N^2\log N)$ | Shu 等 2017 |
| 模式切换延迟 | $0.2$ s（避开快动态） | Huang & Vittal 2018 |
| 缓冲区电压偏差阈值 | $0.005$ pu | Huang & Vittal 2018 |

**注**：原文未报告可核验的步长/误差扫描曲线，上述量化数据均来自对应论文表格或方法描述中的具体数值。

## 适用边界与选择指南

**选经典模型**：首摆功角稳定快速筛查、多机系统参数扫描（步长 5–10 ms）。

**选两轴/暂态模型**：多机暂态稳定分析、励磁控制影响评估（步长 1–5 ms）。

**选次暂态/Park 模型**：需要与 EMT 区域接口、故障初期转矩计算（步长 50–500 μs）。

**选动态相量接口**：HVDC 换流器近区故障、弱交流系统、接口采样延迟敏感场景。

**不适用**：开关谐波（需全 EMT）、饱和磁性元件详细分析（需非线性磁路模型）、保护动作瞬态（需电磁暂态）。

## 与相关页面的关系

- [[electromechanical-simulation]]：使用本页模型进行时域推进和事件仿真。
- [[transient-stability]]：说明大扰动后保持同步的稳定性概念。
- [[transient-stability-analysis]]：把模型转化为时域、直接法或混合法评估流程。
- [[swing-equation]]：给出转子机械运动的核心方程。
- [[excitation-system]] 和 [[power-system-stabilizer]]：描述影响机电阻尼和暂态电势的控制环节。
- [[electromechanical-electromagnetic-hybrid-simulation]]：说明机电模型与 EMT 区域的接口实现。
- [[synchronous-machine-model]]：同步机电磁建模的详细内容（dq 方程、饱和、阻尼绕组）。

## 来源论文

- [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Hassani 等 2022]]：在统一 MATLAB 平台对比 TD、DP、3pPD、PD 四种方法，揭示"DP 因大步长而更快"常见判断的局限性。
- [[electromechanical-electromagnetic-hybrid-simulation-technology-with-large-number|Chen 等 2020]]：提出含大量电磁直流模型的混合仿真自动化建模与钳位启动策略，30×建模效率提升。
- [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Shu 等 2017]]：提出 DPIM 接口，将 FFT 采样法接口计算复杂度从 $O(N^2\log N)$ 降至 $O(N^2)$，消除 1 ms 采样延迟。
- [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-|Huang & Vittal 2018]]：提出模式切换机制（0.2 s 延迟 + 0.005 pu 双门槛），实现混合到纯相量域的安全退回。
- [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Wang 等 2013]]：在 ADPSS 平台验证机电模型用于低频振荡分析的有效性，主导频率偏差 <0.02 Hz，阻尼比偏差 <0.3%。
- [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Yu 等 2014]]：MMC 机电暂态建模的多端 HVDC 系统应用。
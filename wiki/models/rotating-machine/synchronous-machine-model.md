---
title: "同步电机模型 (Synchronous Machine)"
type: model
tags: [synchronous-machine, generator, park, vbr, phase-domain, dq0, cross-saturation, emt]
created: "2026-04-13"
updated: "2026-05-19"
---

# 同步电机模型 (Synchronous Machine)

## 概述

同步电机是电力系统中最重要的发电设备，其电磁暂态（EMT）建模需要在定子、转子绕组的耦合电磁关系与磁路饱和特性之间取得精度与效率的平衡。同步机模型的核心任务是将磁链方程、电压方程、机械运动方程联立求解，并根据应用场景（机电暂态、EMT详细仿真、实时仿真）选择适当的建模粒度。

同步电机模型的 EMT 仿真面临三大挑战：① **坐标变换与dq轴耦合**——转子旋转导致定子电感矩阵随转角变化，使相域模型的网络方程随转子位置改变；② **磁路饱和非线性**——尤其是凸极机的 d-q 轴交叉饱和效应，端电压预测误差可达 5-8%；③ **数值效率**——传统相域模型每步需更新整个网络导纳矩阵并求逆，计算代价高昂。围绕这三大挑战，学术界发展了经典dq模型、相域（Phase Domain, PD）模型、电压源后向转子（VBR）模型和交叉磁化饱和模型等多个建模路径，各有适用场景与精度边界。

## 主要模型类型

### 1. 经典dq模型（qd Reference Frame）

经典dq模型通过 Park 变换将 abc 相域定子变量变换到转子 dq 轴参考坐标系，使得定子电感矩阵变为常数（仅 d-q 軸之间存在耦合），大幅简化了磁链方程的表达：

$$
\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix} = \begin{bmatrix} R_s & 0 & 0 \\ 0 & R_s & 0 \\ 0 & 0 & R_s \end{bmatrix} \begin{bmatrix} i_d \\ i_q \\ i_0 \end{bmatrix} + \frac{d}{dt}\begin{bmatrix} \lambda_d \\ \lambda_q \\ \lambda_0 \end{bmatrix} - \omega_r \begin{bmatrix} -\lambda_q \\ \lambda_d \\ 0 \end{bmatrix} \tag{qd-V}
$$

其中 $R_s$ 为定子电阻，$\omega_r$ 为转子电角速度。转子侧方程包含励磁绕组 $f_d$ 和阻尼绕组 $k_d$（d 轴）以及 $k_q1$、$k_q2$（q 轴）：

$$
\begin{aligned}
v_{fd} &= R_{fd} i_{fd} + \frac{d\lambda_{fd}}{dt} \\
v_{kd} &= R_{kd} i_{kd} + \frac{d\lambda_{kd}}{dt} \\
v_{kq1} &= R_{kq1} i_{kq1} + \frac{d\lambda_{kq1}}{dt} \\
v_{kq2} &= R_{kq2} i_{kq2} + \frac{d\lambda_{kq2}}{dt}
\end{aligned} \tag{qd-R}
$$

**特点**：dq 变换后电感矩阵常数化，数值效率高；但 interface with 外部 EMT 网络时需要逆变换回 abc 相域，增加了计算复杂度。经典dq模型是机电暂态分析（TS）的主力模型，**不适用于需要三相瞬时波形的 EMT 详细仿真**。

**适用场景**：机电暂态稳定性分析（功角稳定性、低频振荡）、潮流初始化、小扰动阻尼分析。

### 2. 相域模型（Phase Domain, PD）

相域模型直接在 abc 自然坐标系下建模，避免了 dq 逆变换的接口开销。定子电压方程：

$$
\mathbf{v}_{abcs} = \mathbf{R}_s \mathbf{i}_{abcs} + \frac{d\boldsymbol{\lambda}_{abcs}}{dt} \tag{PD-V}
$$

其中定子磁链 $\boldsymbol{\lambda}_{abcs} = \mathbf{L}_s(\theta_r)\mathbf{i}_{abcs} + \mathbf{L}_{sr}(\theta_r)\mathbf{i}_{qdr}$，$\mathbf{L}_s(\theta_r)$ 是随转角 $\theta_r$ 变化的 $3\times3$ 电感矩阵。由于转子旋转，$\mathbf{L}_s(\theta_r)$ 每步变化，导致与外部网络的节点导纳矩阵耦合也需要更新。

转子电压方程（dq 参考坐标系）：

$$
\mathbf{v}_{qdr} = \mathbf{R}_r \mathbf{i}_{qdr} + \frac{d\boldsymbol{\lambda}_{qdr}}{dt} \tag{PD-R}
$$

其中 $\mathbf{i}_{qdr} = [i_{kq1}, i_{kq2}, i_{fd}, i_{kd}]^\top$。

**特点**： stator 电路在 abc 相域直接与 EMT 网络接口，无需坐标逆变换；但电感矩阵 $\mathbf{L}_s(\theta_r)$ 随转子转动连续变化，每步需更新整个网络节点导纳矩阵并求逆，计算量大。PD 模型是 EMTP-type 仿真的经典选择。

**经典 PD 模型离散化**（梯形积分，步长 $\tau$）：

$$
\mathbf{v}_{abcs}(k) = -\mathbf{R}_s\mathbf{i}_{abcs}(k) + \frac{2}{\tau}\boldsymbol{\lambda}_{abcs}(k) + \mathbf{e}_{sh}(k) \tag{PD-Disc}
$$

其中 $\mathbf{e}_{sh}(k)$ 为历史电压源项，$\mathbf{e}_{sh}(k) = -\mathbf{R}_s\mathbf{i}_{abcs}(k-1) - \frac{2}{\tau}\boldsymbol{\lambda}_{abcs}(k-1) - \mathbf{v}_{abcs}(k-1)$。

**适用场景**：需要三相不对称工况的 EMT 仿真、换相故障分析、需要保留丰富谐波信息的场景。

### 3. VBR模型（电压源后向转子）

VBR（Voltage Behind Reactance）模型将同步机表示为诺顿等效——并联电导（恒定或缓变）与受控电流源的组合——使得 interface with EMT 网络时只需注入电流源而不必重组网络导纳矩阵，显著改善了数值效率与稳定性。

VBR 模型的核心是将转子方程代入定子方程，消去转子电流，得到等效阻抗矩阵 $\mathbf{R}_{eq}$ 和历史电压源 $\mathbf{e}_h$：

$$
\mathbf{v}_{abcs}(k) = \mathbf{R}_{eq}(k)\mathbf{i}_{abcs}(k) + \mathbf{e}_h(k) \tag{VBR}
$$

其中 $\mathbf{R}_{eq}(k) = -\mathbf{R}_s - \frac{2}{\tau}\mathbf{L}_s(\theta_r(k)) + \frac{8}{3\tau^2}\mathbf{L}_{sr}(\theta_r(k))\left(\mathbf{R}_r + \frac{2}{\tau}\mathbf{L}_r\right)^{-1}\mathbf{L}_{rs}(\theta_r(k))$。

**VBR 模型与 PD 模型的核心区别**：

| 特性 | PD模型 | VBR模型 |
|------|--------|---------|
| 定子电感矩阵 | 随转角变化 | 随转角变化（合并到 $R_{eq}$） |
| 节点导纳更新 | 每步更新 | 每步更新（但形式更紧凑） |
| 网络接口 | 需要重组网络导纳矩阵 | 注入等效电流源，更简洁 |
| 数值稳定性 | 中等 | 改善（特征值模量从 PD 的 2.498 降至 1.031） |
| 允许最大步长 | ~150 μs（0.25%误差） | ~500 μs（0.25%误差） |

**可饱和 VBR 模型**（Wang & Jatskevich 2011）：引入 saliency factor 方法表征主磁路饱和和 d-q 轴交叉饱和。饱和因子定义为 $K_{sq} = \lambda_{qm}/\lambda_{dm}$（q 轴与 d 轴主磁链之比），交叉磁化效应通过双饱和指数模型表征：

$$
\lambda_d = f_d(i_d, i_{fd}, i_{kd}) + f_{cross}(i_q) \quad \text{（d轴含交叉项）} \tag{Sat-VBR}
$$

分段线性方法（Piecewise Linear Method）用于在离散 EMTP 求解中高效处理饱和特性：通过预计算的饱和折线段，在每一时间步根据当前磁链水平查表得到对应的等效电导注入，避免非线性迭代。

**忽略 q 轴饱和的影响**：端电压预测误差达 5-8%，功角误差 3-5°（Dehkordi 2026），带载能力预测偏差 10-15%（负载功率因数 0.8 滞后时）。

### 4. 恒定导纳相域模型（Constant Admittance PD / E-PD）

恒定导纳模型（Xia et al. 2019）通过引入等效阻抗矩阵的常数分解，使网络节点导纳矩阵在所有转子位置均保持恒定：

$$
\mathbf{R}_{eq}(k) = -\mathbf{R}_s + \mathbf{K}^{-1}(\theta_r)\mathbf{R}_{ab}\mathbf{K}(\theta_r) \tag{E-PD-R}
$$

其中 $\mathbf{R}_{ab} = \mathbf{R}_a + \mathbf{R}_b$ 被分解为常数对角矩阵 $\mathbf{R}_a$ 和仅含一个非零元素 $R_{b2}$ 的 $\mathbf{R}_b$，使得等效阻抗中只有 $R_{b2}$ 项通过 Park 变换矩阵 $\mathbf{K}(\theta_r)$ 依赖转角，其余项均为常数。

**E-PD 模型优势**：

- 单步浮点运算量：175 FLOPs（VBR: 298 FLOPs, CC-PD: 316 FLOPs），降低 41.3%
- 恒定等效导纳矩阵彻底消除了因转子位置变化导致的整个网络导纳矩阵更新与求逆操作
- 验证基于 845 MVA 圆柱转子同步机接理想电压源及多机网络故障场景

### 5. 交叉磁化饱和模型（Cross-Magnetization Model）

交叉磁化模型（Dehkordi et al. 2026）基于双饱和指数方法，区分 d 轴和 q 轴的饱和特性，并考虑 d-q 轴之间的交叉磁化效应：

$$
\lambda_d = K_{sd}(i_d, i_{fd}) \cdot f_{cross,q}(i_q) \quad \text{（d轴饱和含q轴互效应）} \tag{Cross-Sat}
$$

其中 $K_{sd}$ 为 d 轴饱和因子，$f_{cross,q}$ 为 q 轴饱和对 d 轴磁链的交叉贡献。交叉磁化模型是凸极机（水轮发电机）的专用模型，对隐极机（汽轮发电机）精度影响较小。

**精度对比**：忽略 q 轴饱和（设 $K_{sq}=1$）在凸极机额定负载下导致端电压误差 5-8%，功角误差 3-5°；采用单一饱和指数方法无法区分 MMF 角度变化，带载能力偏差 10-15%。

## 关键技术

### 电磁暂态建模

同步电机的 EMT 详细模型需要同时求解定子、转子两侧的耦合微分方程组。在 EMT 仿真中，定子侧采用三相瞬时值表示（abc 坐标系或 PD 坐标），转子侧在 dq 旋转坐标系表示，两者通过 Park 变换矩阵耦合：

$$
\mathbf{v}_{abcs} = \mathbf{R}_s \mathbf{i}_{abcs} + \frac{d}{dt}\left[\mathbf{L}_s(\theta_r)\mathbf{i}_{abcs} + \mathbf{L}_{sr}(\theta_r)\mathbf{i}_{qdr}\right] \tag{Mech-V}
$$

$$
\mathbf{v}_{qdr} = \mathbf{R}_r \mathbf{i}_{qdr} + \frac{d}{dt}\left[\mathbf{L}_{rs}(\theta_r)\mathbf{i}_{abcs} + \mathbf{L}_r\mathbf{i}_{qdr}\right] \tag{Mech-R}
$$

电磁转矩的相域表达（Xia 2019）：

$$
T_e = \frac{p}{2}\left[ -\frac{1}{2}(\mathbf{i}_{abcs})^\top\frac{\partial\mathbf{L}_s(\theta_r)}{\partial\theta_r}\mathbf{i}_{abcs} + (\mathbf{i}_{abcs})^\top\frac{\partial\mathbf{L}_{sr}(\theta_r)}{\partial\theta_r}\mathbf{i}_{qdr} \right] \tag{Te-PD}
$$

### 饱和处理

同步电机饱和特性通常通过开路饱和曲线（$\lambda$-$i$ 特性）描述，在 EMT 求解中需要处理两种饱和场景：

1. **d轴饱和**：主要影响励磁电流和端电压幅值
2. **q轴饱和与交叉饱和**：影响凸极机的转矩特性和功角特性

分段线性方法（Piecewise Linear, PWL）在 EMTP 离散求解中的优势是不需要非线性迭代：通过预定义的饱和折线表，在每个时间步根据当前磁链值直接查表得到等效电导，O(1) 复杂度。无饱和时 $\mathbf{G}_{sat} = 0$；饱和时 $\mathbf{G}_{sat}$ 按当前 $\lambda$ 所处折线段斜率加入节点导纳矩阵。

### 接口技术

同步机与 EMT 网络的接口是混合仿真中的关键环节。主流接口方式有三种：

**诺顿等效接口**：将同步机表示为电流源 $\mathbf{i}_{eq}$ 与等效导纳 $\mathbf{Y}_{eq}$ 的并联，直接注入网络节点方程 $\mathbf{Y}_{node}\mathbf{v} = \mathbf{i}_{inj}$。适用于 PD 模型和 VBR 模型。

**伴随电路接口**：将同步机模型转换为等效的伴随电路表示，与 EMTP 的节点分析框架兼容。适用于 dq 经典模型与 EMT 网络的接口。

**多速率接口**：机电侧（摇摆方程）步长 1-10 ms，EMT 侧步长 1-50 μs，步长比 $N = \Delta t_{TS}/\Delta t_{EMT} \approx 100 \sim 1000$。通过多项式外推/插值在接口边界同步数据（Jalili-Marandi 2009）。

## 应用场景

| 场景 | 推荐模型 | 原因 |
|------|----------|------|
| 短路故障 EMT 分析 | PD 模型或 VBR 模型 | 需要三相瞬时波形，保留不对称信息 |
| 励磁系统动态研究 | dq 模型 + 励磁系统联立 | 关注转子侧电磁暂态，dq 坐标系自然 |
| 稳定性分析（功角） | 摇摆方程（[[swing-equation]]） | 机电暂态时间尺度，dq 模型足够 |
| 机电-EMT 混合仿真 | VBR 模型 + 多速率接口 | 兼顾精度与接口效率 |
| 实时仿真（RTDS/OPAL） | VBR 模型或 E-PD 模型 | 大步长（50-500 μs）下保持稳定 |
| 风电场同步机聚合 | 等值聚合模型 | 大规模系统简化，保留动态特性 |
| 不对称运行分析 | PD 模型（保留 abc 相） | 无需 dq 变换，不对称工况精度高 |

## 量化性能边界

**VBR同步电机模型精度与效率**（Wang & Jatskevich 2011）：

| 指标 | 数值 |
|------|------|
| VBR 允许最大步长（0.25% 误差容限） | 500 μs |
| PD 模型需步长（相同误差容限） | 150 μs |
| dq 模型允许步长 | ~10 μs |
| VBR vs PD CPU 时间比（相同步长） | 减少 50%（2 倍加速） |
| 1 ms 大步长时 MicroTran/ATP 误差 | >4% / 数值发散 |
| VBR 1 ms 大步长误差 | 稳定且 <0.25% |
| 离散特征值模量（PD → VBR） | 2.498 → 1.031 |
| 验证基准 | 835 MVA SMIB 三相短路，RK4 1 μs 参考解 |

**E-PD 恒定导纳模型计算效率**（Xia et al. 2019）：

| 指标 | E-PD | VBR | CC-PD |
|------|------|-----|-------|
| 单步 FLOPs | 175 | 298 | 316 |
| 网络导纳更新 | 无（恒定） | 每步更新 | 每步更新 |
| 验证基准 | 845 MVA 圆柱转子 + 多机网络故障 |

**交叉磁化饱和模型精度**（Dehkordi et al. 2026）：

| 场景 | 误差（忽略 q 轴饱和） |
|------|----------------------|
| 端电压预测误差（额定负载，凸极机） | 5-8% |
| 功角预测误差 | 3-5° |
| 带载能力偏差（PF=0.8 滞后） | 10-15% |
| 验证基准 | 50-500 MVA 凸极/隐极机，RTDS 50 μs EMT |

## 相关模型

- [[synchronous-machine-model]]：本页面
- [[swing-equation]]：同步机机械运动方程，机电暂态核心工具
- [[induction-machine-model]]：感应电机与同步电机的对比
- [[vsc-model]]：新能源并网 VSC 接口
- [[transformer-model]]：机端变压器模型
- [[fdne-model]]：外部网络频变等值
- [[excitation-system]]：励磁控制系统，与同步机强耦合

## 相关方法

- [[state-space-method]]：状态空间方法（EMT 求解框架）
- [[nodal-analysis]]：节点分析方法（EMTP 核心算法）
- [[co-simulation]]：机电-电磁混合仿真
- [[real-time-simulation]]：实时仿真（RTDS/OPAL）
- [[coordinate-transformation-model]]：Park dq 坐标变换

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|----------|
| Wang & Jatskevich | 2011 | 可饱和 VBR 模型，分段线性饱和处理，d-q 轴交叉饱和（无对应源页面） |
| Xia et al. | 2019 | E-PD 恒定导纳模型，175 FLOPs/步，消除网络导纳矩阵更新（无对应源页面） |
| Dehkordi et al. | 2026 | 交叉磁化模型，q 轴饱和误差量化（5-8% 电压误差）（无对应源页面） |
| Jalili-Marandi et al. | 2009 | 机电-EMT 混合仿真接口协议，步长比与误差边界 |
| Hiramatsu et al. | 2012 | 饱和对暂态稳定的影响，x'q 对甩负荷电压预测的重要性 |

## 证据边界

本页给出的量化性能数据均来自对应来源论文的验证结果。VBR 模型的 500 μs 最大步长结论基于 835 MVA SMIB 系统三相短路工况；E-PD 175 FLOPs 基准基于 845 MVA 圆柱转子机；交叉饱和误差数据基于 50-500 MVA 凸极机 RTDS 验证。实际系统的允许步长和精度边界受机器参数、网络强度、故障类型等多因素影响，不可跨场景直接套用。
---
title: "电缆建模 (Cable Modeling)"
type: topic
tags: [cable, underground-cable, submarine-cable, skin-effect, frequency-dependent]
created: "2026-04-14"
updated: "2026-05-16"
---

# 电缆建模 (Cable Modeling)

## 定义与概述

电缆建模研究地下电缆、海底电缆和混合架空-电缆线路在 EMT 仿真中的参数计算、频率相关效应和时域实现。与架空线路相比，电缆具有导体、绝缘、屏蔽、护套、铠装和土壤/海水回路等多层结构，集肤效应、邻近效应、护套回流和介质损耗会显著影响暂态传播。

在 EMT 语境下，电缆模型通常需要在宽频精度、数值稳定性和计算成本之间折中。工频或慢暂态可使用固定参数模型；雷电、开关冲击、直流故障行波和 VSC-HVDC 宽频振荡则需要频率相关模型。

电缆的频变参数计算是 EMT 仿真的核心挑战之一。由于金属屏蔽层、铠装层和大地的有损返回路径，传统解析公式难以准确描述高频行为。Morales 等 (2023) 提出的 MoM-SO (Method of Moments - Self and Mutual) 框架将几何平均距离法与频域积分方程结合，可显式纳入集肤效应和邻近效应。

电缆模型的 EMT 实现分为两类路径：**特征线法 (MoC)** 复用通用线路模型结构，通过矢量拟合提取特性导纳 $Y_c$ 和传播函数 $H$ 的有理近似；**导纳矩阵有理拟合 (FLE)** 将节点导纳矩阵 $Y_n$ 分解为开路响应 $Y_{oc}$ 和短路响应 $Y_{sc}$ 分别拟合。

## EMT 中的角色

电缆模型在 EMT 仿真中承担双重角色：**电气建模对象**（多导体传输线）和**系统接口组件**（与电网其他部分的连接）。

电缆模型的核心挑战是**宽频参数计算**与**时域递推实现**的组合：

1. **多层几何结构**：单芯电缆含芯线导体、内绝缘层、金属护套/屏蔽、外绝缘层、铠装钢丝和外护套；埋地电缆还需考虑土壤和海水返回路径
2. **频变阻抗计算**：集肤效应使 $R(\omega)$ 随频率增加；邻近效应在多导体紧密排列时显著；铠装的螺线管效应增加附加阻抗
3. **模态解耦与变换**：电缆的相域阻抗矩阵 $Z$ 和导纳矩阵 $Y$ 通过特征值分解得到模态域表达，模态变换矩阵 $T_v$ 可能是频率相关 (FDCM) 或固定常数 (CM)
4. **时域等效电路**：频域参数通过矢量拟合或有理逼近转化为状态空间 $\pi$ 型链路或递推卷积形式

电缆模型的 EMT 精度直接决定海上风电送出系统故障行波保护、换相失败快速响应等关键工况的仿真可信度。

## 电缆参数计算

### 基本电报方程

电缆单位长度参数由以下方程描述：

$$\frac{partial V}{partial z} = -Z' \cdot I = -(R' + j\omega L') \cdot I \tag{1}$$

$$\frac{\partial I}{\partial z} = -Y' \cdot V = -(G' + j\omega C') \cdot V \tag{2}$$

其中 $Z' = R' + j\omega L'$ 为串联阻抗矩阵，$Y' = G' + j\omega C'$ 为并联导纳矩阵。

定义传播常数 $\gamma = \sqrt{Z' \cdot Y'}$，特性导纳 $Y_c = \sqrt{Z' / Y'}$，则电压和电流通解为：

$$V(z) = V^+ e^{-\gamma z} + V^- e^{\gamma z} \tag{3}$$

$$I(z) = I^+ e^{-\gamma z} + I^- e^{\gamma z} = \frac{V^+}{Z_c} e^{-\gamma z} - \frac{V^-}{Z_c} e^{\gamma z} \tag{4}$$

### 频变参数计算方法

**方法 1：MoM-SO 几何平均距离法**

Morales 等 (2023) 提出的新工具基于 Method of Moments - Self and Mutual (MoM-SO) 理论，将导体分割为多个子单元，用几何平均距离 (GMD) 和几何平均距离自感 (GMDA) 计算子单元间电阻和电感：

$$R_{ij} = \frac{\rho_i}{2\pi r_i} \cdot \frac{1}{\text{GMD}_{ij}} \cdot \text{SelfResistanceCorrection}(\omega, r_i) \tag{5}$$

$$L_{ij} = \frac{\mu_0}{2\pi} \ln\left(\frac{\text{GMD}_{ij}}{\text{GMR}_{ij}}\right) + \Delta L_{\text{skin}} + \Delta L_{\text{proximity}} \tag{6}$$

Skin effect correction: $\Delta L_{\text{skin}} = \frac{\mu_0}{2\pi} \cdot \frac{1}{4\delta}$，其中 $\delta = \sqrt{2\rho/(\omega\mu)}$ 为集肤深度。

**方法 2：Sommerfeld 积分法**

对于埋地电缆，外部阻抗由 Sommerfeld 积分给出 (Camara 2024)：

$$z_0 = \frac{j\omega\mu_0}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-2h\bar{u}_1}}{\bar{u}_1 + \bar{u}_2} e^{j r_j \lambda} d\lambda \tag{7}$$

其中 $\bar{u}_1 = \sqrt{\lambda^2 + \gamma_1^2}$，$\bar{u}_2 = \sqrt{\lambda^2 + \gamma_2^2}$，$h$ 为电缆埋深，$\gamma_1 = \sqrt{j\omega\mu_0(\sigma_1 + j\omega\varepsilon_1)}$。

**方法 3：多层大地广义参数**

对于需考虑多层土壤的系统，Tsiamitros 等和 Xue 等提出了广义闭式表达式，突破传统 Carson 单一土壤假设限制。该方法将大地阻抗计算从无穷积分转化为有限项有理函数，避免了数值积分的不收敛问题。

### 电缆结构参数（典型值）

**单芯 XLPE 电缆单位长度参数典型范围：**

| 参数 | 典型范围 (工频) | 频变特性 | 备注 |
|------|----------------|---------|------|
| $R'$ (Ω/km) | 0.02–0.5 | 集肤效应显著，$R \propto \sqrt{\omega}$ | 铜导体 400 mm² @ 20°C |
| $L'$ (mH/km) | 0.2–2.0 | 大地返回路径影响 | 与敷设方式强相关 |
| $C'$ (μF/km) | 0.1–0.5 | 介质材料决定 | XLPE @ 20°C |
| $G'$ (μS/km) | 0.01–1.0 | 绝缘老化、温度 | 可忽略 |

**三芯铠装电缆特殊参数：**

| 参数 | 物理机制 | 计算方法 |
|------|---------|---------|
| 螺线管效应电感 | 铠装钢丝磁化产生的附加电感 | 3D FEM 或 2.5D 近似 |
| 护套回流损耗 | 金属护套中环流产生的 $I^2R$ 损耗 | 护套接地方式 (单点/交叉互联) |
| 邻近效应阻抗 | 多导体间电磁耦合导致电流分布不均匀 | MoM-SO 子单元细分法 |

## 电缆 EMT 建模方法

### 方法 1：恒定参数模型 (Constant Parameter)

适用于工频稳态和低频控制研究，参数不随频率变化：

$$Z' = R_{dc} + j\omega L_{dc}, \quad Y' = G_{dc} + j\omega C_{dc} \tag{8}$$

**优点**：计算最快，适合潮流和工频机电仿真
**缺点**：不能捕捉高频暂态和行波传播特性
**适用场景**：工频负载流、短路计算、稳态分析

### 方法 2：频率相关模型 (Frequency Dependent, FD)

采用矢量拟合将频域阻抗/导纳矩阵拟合成有理函数：

$$Z'(s) \approx \sum_{k=1}^{N} \frac{r_k}{s - p_k} + d + s \cdot h \tag{9}$$

其中 $p_k$ 为极点，$r_k$ 为留数，$d$ 和 $h$ 为直接馈通项。

**优点**：宽频精度高，自动捕捉集肤效应和邻近效应
**缺点**：拟合阶数高时计算量大，无源性可能违规
**适用场景**：开关暂态、雷电冲击、VSC-HVDC 振荡

### 方法 3：通用线路模型 (Universal Line Model, ULM)

结合特征线法和延迟提取技术，将特性导纳和传播函数解耦为：

$$Y_c(s) = \sqrt{Z'(s) / Y'(s)}, \quad H(s) = e^{-\ell \sqrt{Z'(s) Y'(s)}} \tag{10}$$

模态域分解通过特征值实现：

$$H_m = T_v^{-1} \cdot H \cdot T_v, \quad Y_{cm} = T_v^{-1} \cdot Y_c \cdot T_v \tag{11}$$

**优点**：物理意义清晰，延迟利用降低计算复杂度
**缺点**：模态变换矩阵频率相关时精度下降
**适用场景**：长电缆线路、行波保护验证、海底电缆

### 方法 4：折叠线等效 (Folded Line Equivalent, FLE)

将节点导纳矩阵分解为开路和短路响应两部分分别拟合：

$$Y_n = \begin{bmatrix} Y_s & Y_m \\ Y_m & Y_s \end{bmatrix} \Rightarrow \begin{bmatrix} Y_{oc} & 0 \\ 0 & Y_{sc} \end{bmatrix} = K \cdot Y_n \cdot K^{-1} \tag{12}$$

其中 $K = \begin{bmatrix} I_n & I_n \\ I_n & -I_n \end{bmatrix}$。

**优点**：可独立拟合最小特征值，避免插值不稳定；支持延迟利用
**缺点**：实现复杂，无商业软件支持
**适用场景**：高频域精度要求高的场合

### 方法 5：宽频 Krylov 降阶模型

Loaiza-Elejalde 等 (2026) 提出的方法结合恒定模态变换矩阵与有理 Krylov 拟合：

$$Y_n(s) \approx V \cdot (\sigma I + A)^{-1} \cdot W + D \tag{13}$$

其中 $V, W$ 为 Krylov 投影矩阵，$A$ 为降阶系统矩阵。

**优点**：计算效率高，适合实时仿真
**缺点**：恒定 $T_v$ 可能导致端口无源性违规
**适用场景**：VSC-HVDC 宽频相互作用分析

### 建模方法对比

| 建模方法 | 适用频段 | 计算复杂度 | 数值稳定性 | 典型应用 |
|---------|---------|-----------|-----------|---------|
| 恒定参数 | DC–60 Hz | O(n) | 优 | 工频潮流 |
| 频率相关 (FD) | 0.1 Hz–10 kHz | O(n²) | 良 | 开关暂态 |
| ULM | DC–1 MHz | O(n³) | 良 | 雷电冲击、行波保护 |
| FLE | DC–1 MHz | O(n³) | 优 | 高精度海底电缆 |
| 宽频降阶 | DC–100 kHz | O(n log n) | 良 | VSC-HVDC 宽频分析 |

## 关键技术挑战

### 挑战 1：多层有损介质的参数计算

**问题**：海底电缆同时经由海水和海床返回，两者均为有损介质。传统 EMT 程序假设外部介质之一为无损，不能直接处理"双有损埋设"场景。

**解决方案**：Camara 等 (2024) 用准 TEM 近似将全波表达式转化为可用于时域的闭式解析，绕过了无穷积分的数值困难。引入修正后的内外阻抗计算：

$$Z_{total} = Z_{in} + Z_{external}(\sigma_{sea}, \sigma_{seabed}, h_{burial}) \tag{14}$$

**验证**：数值拉普拉斯变换 (NLT) 基准验证表明，0.1 Hz–10 MHz 频域内误差 < 0.01%。

### 挑战 2：螺线管效应对铠装电缆阻抗的影响

**问题**：三芯铠装电缆的钢丝铠装呈螺旋状缠绕，与直线导体假设下的传统 Cable Constants 公式不符。螺线管效应导致额外电感，且电感值与铠装钢丝的磁导率 $\mu_r$ 和节距角 $\theta$ 相关。

**量化数据** (Chrysochos 2023)：
- 磁导率 $\mu_r = 90$ 时，螺线管效应导致的附加感抗可达总感抗的 15–25%
- 节距角 $\theta = 2.5°$ vs $\theta = 5°$ 时，等效电感变化约 8%
- 3D FEM vs 2.5D 方法在 50 Hz 处偏差可达 12%

**解决方案**：使用 3D 有限元法或 MoM-SO 方法直接计算螺旋导体的自感和互感。

### 挑战 3：频变模型的无源性强制

**问题**：矢量拟合得到的有理函数逼近可能在某些频段违反无源性（端口特性导纳实部为负），导致时域仿真非物理发散。

**解决方案**：Passivity enforcement 通过特征值水平约束调整留数，确保 $Y(\j\omega)$ 的所有特征值实部为正。

**量化指标**：Glover (2019) 方法中，极点-留数比值约束 < 某阈值可消除 > 90% 的无源性违规。

### 挑战 4：长电缆的延迟补偿与插值不稳定

**问题**：当时间步长 $\Delta t$ 与传播延迟 $\tau = \ell / v$ 不匹配时，直接递推会产生数值振荡。延迟比 $N = \tau / \Delta t$ 必须为整数才能避免插值。

**解决方案**：
- **延迟利用 (Latency Exploitation)**：将延迟作为滤波器的额外极点提取，无需整数约束
- **自适应时间步**：在波动明显时段自动减小 $\Delta t$

**典型数据**：对于 100 km 电缆，$\tau \approx 0.5$ ms，$\Delta t = 50$ μs 时 $N = 10$，无需插值。

### 挑战 5：测量融合与参数不确定性

**问题**：当几何参数不足（铠装钢丝精确数量、土壤电阻率 $\rho_{soil}$）时，仿真结果与实测偏差较大。

**解决方案**：
- **阻抗测量融合**：利用时域反射计 (TDR) 数据修正 $R(\omega)$ 和 $L(\omega)$
- **S 参数嵌入**：$S_{11}$ 测量数据直接嵌入拟合过程，确保模型与实测一致

**关键参数**：土壤电阻率 $\rho_{soil}$ 从 100 Ω·m 到 10000 Ω·m 变化时，海底电缆的等效阻抗变化可达 40%。

## 量化性能边界

| 建模方法 | 适用场景 | 关键性能指标 | 代表数据 |
|---------|---------|------------|---------|
| MoM-SO 参数计算 | 集肤/邻近效应 | 计算精度 vs FEM | 偏差 < 2% (Morales 2023) |
| ULM 海底电缆 | 75 kV HVDC submarine | 时间域误差 vs NLT | < 0.1% (Camara 2024) |
| FLE | 宽频 nodal admittance | 82 poles (Yoc) + 80 poles (Ysc) | 极点-留数比 = 1.25 |
| 3D FEM 螺线管 | 三芯铠装电缆 | 感抗附加量 | 15–25% @ $\mu_r = 90$ |
| 宽频 Krylov 降阶 | VSC-HVDC 交互 | 状态变量减少 | 5× 降阶 (Loaiza 2026) |
| 无源性强制 | 数值稳定性 | 违规消除率 | > 90% |
| 延迟提取 | ULM 时域实现 |  rms-error 最小化 | 收敛 |

## 适用边界与选择指南

| 应用场景 | 推荐模型 | 关键考量 | 步长要求 |
|---------|---------|---------|---------|
| 工频负载流 | 恒定参数 | 精度足够，计算最快 | 无要求 |
| 开关过电压 | FD/ULM | 捕捉高频振荡 (> 1 kHz) | Δt < 10 μs |
| 雷电冲击 | ULM | 行波传播精度 | Δt < 1 μs |
| VSC-HVDC 宽频 | 宽频降阶/FLE | 0.1 Hz–100 kHz 全频覆盖 | Δt < 0.1 μs |
| 实时仿真 | 状态空间实现 | 固定步长稳定性 | Δt = 50–100 μs |
| 参数不确定 | 测量融合模型 | S 参数修正 | 无要求 |
| 海底埋设电缆 | MoC/FLE (Camara) | 双有损介质处理 | Δt < 5 μs |

**选择决策**：

1. **精度优先**：FLE + NLT 验证
2. **速度优先**：宽频 Krylov 降阶
3. **通用工具**：MoM-SO 参数计算 + ULM 时域
4. **特殊结构**：3D FEM (螺线管效应) 或 MoM-SO (邻近效应)

## 技术演进脉络

### 1999–2005：早期线路建模探索

- **小波变换多分辨率线路模型** (2001)：突破 J. Marti 模型模变换矩阵常数假设，利用 DWT 实现多分辨率时域仿真
- **非均匀线路 (NUL) 建模** (2001)：基于链式矩阵乘法处理参数随距离变化特性，扩展线路模型适用范围
- **混合换位线路模型** (2001)：利用连续换位特性简化频域矩阵，提升多导体线路仿真效率

### 2006–2010：模型稳定性贡献

- **ULM 无源性强制方法** (2008)：解决有理函数带外逼近误差导致的数值不稳定，三层防御策略确保稳定性
- **数值稳定性改进方法** (2010)：基于留极点比值约束的频域拟合，消除宽频模型时域失稳问题

### 2011–2015：状态空间与并行计算

- **状态空间 $\pi$ 型线路模型** (2011)：采用级联 $\pi$ 型电路空间离散化，RL 模块拟合频变参数
- **平行线路模态解耦** (2012)：解耦与宽频有理拟合结合，解决平行线路互感耦合精度问题
- **FPGA 实时非线性求解器** (2011)：补偿法解耦非线性元件，实现迭代式实时电磁暂态求解

### 2016–2020：多层土壤与全频变建模

- **多层大地广义参数框架** (2021)：突破 Carson 假设，严格推导多层大地返回阻抗与导纳
- **全频变 FLE 延迟利用模型** (2017)：折叠线等效与延迟利用结合，降低大规模仿真计算复杂度
- **频域双端口模态解耦评估** (2017)：系统评估实常数变换矩阵近似精度与线路长度关系

### 2021–2026：开源实现与测量融合

- **ULM 在 ATP 开源实现** (2021)：两阶段混合架构实现免费平台的通用线路模型
- **大地返回导纳电缆模型** (2021)：准 TEM 近似闭式解析替代 Pollaczek 积分，提升埋地电缆仿真效率
- **宽频 Krylov 降阶拟合** (2026)：恒定变矩阵与有理 Krylov 拟合结合，实现宽频模型高效降阶

## 相关方法

- [[vector-fitting|矢量拟合]] — 频变参数有理函数拟合
- [[state-space-method|状态空间法]] — 频变模型状态空间实现
- [[nodal-analysis|节点分析]] — 电缆网络节点方程求解
- [[numerical-integration|数值积分]] — 频变模型离散化实现
- [[passivity-enforcement|无源性强制]] — 宽频模型稳定性保证
- [[fdne-model|频变网络等值 (FDNE)]] — 电缆网络宽频等值
- [[universal-line-model]] — ULM 通用线路模型

## 相关模型

- [[cable-model|电缆模型]] — 地下/海底电缆元件模型
- [[transmission-line-model|输电线路模型]] — 架空线路与电缆联合建模
- [[fdne-model|频变网络等值 (FDNE)]] — 电缆网络宽频等值
- [[transformer-model|变压器模型]] — 电缆-变压器接口建模
- [[grounding-system-model|接地系统模型]] — 电缆护套与接地

## 相关主题

- [[frequency-dependent-modeling|频率相关建模]] — 宽频参数建模框架
- [[real-time-simulation|实时仿真]] — 电缆模型实时实现
- [[co-simulation|混合仿真]] — 电缆-设备联合仿真
- [[parallel-computing|并行计算]] — 大规模电缆网络并行求解
- [[harmonic-analysis|谐波分析]] — 电缆谐波阻抗分析
- [[vsc-hvdc]] — VSC-HVDC 电缆系统
- [[wind-farm-modeling]] — 海上风电场电缆连接

## 来源论文

- [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca]] — 邻近效应对快速暂态仿真的影响 (2005)
- [[a-new-tool-for-calculation-of-line-and-cable-parameters]] — 线路与电缆参数计算新工具 (Morales 2023)
- [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati]] — 多导体电缆建模含测量同轴波传播 (2022)
- [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables]] — 螺线管效应对三芯铠装电缆串联阻抗影响 (Chrysochos 2023)
- [[time-domain-modeling-of-a-subsea-buried-cable]] — 海底埋设电缆时域建模 (Camara 2024)
- [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models]] — ULM 线路/电缆模型时延估计 (Loaiza-Elejalde 2026)
- [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti]] — 基于恒定变换矩阵和有理 Krylov 拟合的宽频模型 (2026)
- [[validation-of-frequency-dependent]] — 频率相关模型验证 (2026)
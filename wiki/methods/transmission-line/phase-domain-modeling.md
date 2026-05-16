---
title: "相域建模 (Phase-Domain Modeling)"
type: method
tags: [phase-domain, abc, three-phase, instantaneous, unbalanced, coupled]
created: "2026-05-02"
updated: "2026-05-17"
---

# 相域建模 (Phase-Domain Modeling)

## 定义与边界

相域建模是在物理相坐标或导体坐标中直接表示电压、电流、磁链和端口约束的方法。三相系统中常写作 abc 建模；多导体线路和电缆中也可扩展为导体域或相域矩阵。

本页讨论 EMT 方法层面的相域建模，不等同于某个具体软件、某个设备模型或"永远更精确"的结论。相域模型能保留不平衡、互耦和开关细节，但可信度仍取决于参数、频带、离散化、事件处理和验证来源。

## EMT 中的作用

EMT 主网络通常以节点电压和支路电流的瞬时值求解，因此相域建模是许多元件的自然接口。它适合：

- 不平衡故障、非全相运行和单相设备接入。
- 变压器连接、接地通道、三角形环流和零序路径。
- 电力电子开关、PWM、限流和保护闭环。
- 频率相关线路、电缆护套、平行线路互耦和非换位线路。
- 电机与网络的 abc 端口接口，即使内部状态使用 dq 坐标。

当研究对象近似平衡、线性且关注基频相量时，[[symmetrical-components]] 和 [[sequence-network-model]] 可能更紧凑；当关注控制器内部变量时，[[dq-transformation]] 可能更便于表达。

## 核心方程

### 基本电压电流关系

相域网络变量可写为

$$
\mathbf{v}_{abc}=
\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix},
\qquad
\mathbf{i}_{abc}=
\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}.
$$

线性集中参数支路的一般形式为

$$
\mathbf{v}_{abc}
=\mathbf{R}\mathbf{i}_{abc}
+\frac{d}{dt}\boldsymbol{\psi}_{abc},
\qquad
\boldsymbol{\psi}_{abc}=\mathbf{L}(\mathbf{x},t)\mathbf{i}_{abc}.
$$

其中 $\mathbf{L}$ 可以包含自感、互感、转子位置依赖或饱和状态依赖。离散化后，支路通常通过 [[companion-circuit]] 形成等效导纳和历史源，进入 [[nodal-admittance-matrix]]：

$$
\mathbf{Y}_{n+1}\mathbf{v}_{n+1}
=\mathbf{i}_{src,n+1}+\mathbf{i}_{hist,n+1}.
$$

若开关、饱和或控制约束使方程非线性，上式会成为需要迭代求解的残差系统。

### 同步电机的相域端口方程

对于同步电机的相域建模，定子侧使用三相相坐标，接口量是端口相电压和相电流，可直接并入网络节点方程；转子侧使用随转子旋转的 dq 坐标，核心状态量是励磁绕组和阻尼绕组磁链。

定子电压方程把端电压表示为电阻压降、等效磁链变化项和 VBR 内部电势：

$$
\mathbf{v}_{abc} = \mathbf{R}_s \mathbf{i}_{abc} + \frac{d\boldsymbol{\psi}_{abc}}{dt}.
$$

隐式梯形法把转子磁链递推成当前定子电流、上一时步定子电流、历史磁链和励磁电压的线性组合。

### 恒定诺顿导纳的代数推导

传统 PD 和 VBR 模型的等效导纳随转子位置变化；若用人工阻尼绕组实现常导纳，则参数选择会引入额外物理假设并可能影响高频暂态。

**E-PD 模型**（Xia et al. 2019）重新整理机器方程，把转子位置相关项从诺顿导纳中转移到受控电流源/历史项中，使电机对网络呈现"恒定诺顿导纳并联受控电流源"：

$$
\mathbf{i}_{abc,n+1} = \mathbf{G}_{eq} \mathbf{v}_{abc,n+1} + \mathbf{i}_{hist,n+1}.
$$

其中 $\mathbf{G}_{eq}$ 在仿真全过程不随转子角改变。E-PD 每步计算约 175 FLOPs，低于 VBR 的 298 FLOPs 和 CC-PD 的 316 FLOPs。

### 相域磁路表示法

Yonezawa 2023 提出的磁路表示法把同步机相域方程改写成类似变压器磁路表示的网络：

- 电枢三相电流和转子侧励磁/阻尼绕组电流作为接口输入，经电流控制电流源转换为等效磁动势。
- 随转子电气角 $\theta$ 变化的定子自感、定转子互感等电感矩阵元素，用受控电阻或等效磁导表示。
- 电压控制电流源与 1H 电感构成的微分环节求磁链对时间的导数，得到感应电动势。

控制子系统用上一时间步电流估算转矩并预测当前转速/角度，据此更新时变电感网络参数；EMT 求解器再联立求解外部电网、电机电气回路和磁路网络。

### 感应电机的相域诺顿等值

对于感应电机，Multi-scale Induction Machine Model（解析信号法）推导出对任意转子位置、且不随磁化电感饱和变化而改变的 abc 相域诺顿内导纳：

$$
\mathbf{i}_{abc} = \mathbf{G}_{eq} \mathbf{v}_{abc} + \mathbf{i}_{hist}.
$$

其中 $\mathbf{G}_{eq}$ 不随 $\theta_r$ 和磁化电感变化进入网络矩阵。通过解析信号和可调 shift frequency，模型可在瞬时波形模型和动态相量包络模型之间连续覆盖。

### 相域频变线路的 FpF-ULM 模型

Noda 2015 将频率分区拟合（FpF）引入 ULM 相域线路建模：

- **特征导纳矩阵**：FpF 直接拟合为常数项加若干稳定极点留数项，使其时域卷积可化为递归历史量：

$$
\mathbf{Y}_c(s) = \mathbf{Y}_c^\infty + \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k}.
$$

- **传播函数矩阵**：ULM 思想显式保留行波传播时延，因为不同传播模态到达时间不同：

$$
\mathbf{H}(s) = \mathbf{P}(s) e^{-\mathbf{\Gamma}(s)l}.
$$

FpF 通过按频段处理和自适应加权，使宽频拟合更贴近不同频段的误差结构。

## 典型模型对象

| 对象 | 相域表示 | 关键边界 |
|---|---|---|
| 输电线路 | 多相阻抗、导纳、传播和历史项矩阵 | 频率相关、换位、地回路和互耦需说明 |
| 变压器 | 绕组连接、漏抗、磁化和中性点约束 | 零序通路和饱和不能用理想三相平均替代 |
| 同步电机 | abc 端口、电感矩阵或 VBR/E-PD 等值源接口 | 内部 dq 与外部 abc 的同步离散化需验证；E-PD 提供恒定导纳 |
| 感应电机 | abc 端口、诺顿等值内导纳、解析信号接口 | 恒定内导纳减少网络导纳变化；shift frequency 控制多尺度 |
| 变流器 | 开关函数、受控源、平均值模型或 Norton 注入 | PWM、采样延迟、限流和拓扑切换影响结果 |
| 故障和保护 | 相别、故障阻抗、断路器和测量链 | 动态电弧和互感器暂态需要专门模型 |

## 与坐标变换的关系

相域建模并不排斥坐标变换。常见组合包括：

- 主网络保持 abc，相域端口直接求解。
- 电机内部用 dq 或 VBR 状态，端口通过 abc 等效接入网络。
- VSC 控制器测量 abc 电压电流，经 dq 变换生成指令，再反变换为调制参考。
- 线路模型在内部使用模态通道，最终仍把端口量变回相域。

关键是记录坐标变换发生在哪里、哪些状态被保留、哪些历史项被映射，以及变换误差是否进入主网络。

## EMT 建模方法分类

### 1. 经典相域模型（PD）

原始相域模型直接保留时变电感矩阵 $\mathbf{L}(\theta)$：

$$
\boldsymbol{\psi}_{abc} = \mathbf{L}(\theta) \mathbf{i}_{abc}.
$$

网络矩阵每步随转子角更新，计算量大但物理意义直接。

### 2. 电压后电抗模型（VBR）

VBR-EMTP 模型把转子动态对定子的影响重组为"电抗后电压"与等效阻抗/历史源：

- 定子在 abc 相坐标中直接作为网络接口。
- 转子在 dq 坐标中保留磁链状态。
- 通过隐式梯形离散得到非迭代、同步求解的等效电路。

50 μs 步长下 VBR 与高精度 RK4 参考解基本一致；1 ms 步长下 VBR 仍保持稳定，而传统模型发散。在 0.25% 相对误差容限下，VBR 可用 500 μs 步长，PD 约 150 μs，传统 qd 接口约 10 μs。

### 3. 恒定导纳相域模型（E-PD / CC-PD）

E-PD 模型（Xia et al. 2019）通过代数推导把转子角相关性从矩阵系数转移到历史源：

- 网络总导纳矩阵无需随转子位置反复更新。
- 适合节点数多、机器多、矩阵分解成本高的 EMT 仿真。
- 每步计算约 175 FLOPs，低于 VBR 的 298 FLOPs。

### 4. 磁路表示相域模型

Yonezawa 2023 的磁路法用基本电路元件搭建同步机模型：

- 不要求修改 EMT 程序源码。
- 便于用户加入空间谐波或绕组不平衡。
- 100 μs 步长运行时与 10 μs 参考模型波形级一致。

### 5. 解析信号多尺度相域模型

感应电机的解析信号法通过 shift frequency 实现多尺度覆盖：

- $f_{ref}=0$：瞬时波形模型。
- $f_{ref}=f_{sync}$：动态相量包络模型。
- 恒定诺顿内导纳便于与 abc 相域网络仿真器集成。

## 形式化表达汇总

**相域基本变量：**

$$
\mathbf{v}_{abc} = \begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}, \quad \mathbf{i}_{abc} = \begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}, \quad \boldsymbol{\psi}_{abc} = \begin{bmatrix} \psi_a \\ \psi_b \\ \psi_c \end{bmatrix}.
$$

**时变电感磁链关系：**

$$
\boldsymbol{\psi}_{abc} = \mathbf{L}(\theta) \mathbf{i}_{abc}.
$$

**诺顿等值（恒定导纳）：**

$$
\mathbf{i}_{abc,n+1} = \mathbf{G}_{eq} \mathbf{v}_{abc,n+1} + \mathbf{i}_{hist,n+1}.
$$

**VBR 等值电路：**

$$
\mathbf{v}_{abc} = \mathbf{R}_s \mathbf{i}_{abc} + \frac{d\boldsymbol{\psi}_{abc}}{dt}.
$$

**频变线路特征导纳的矩阵部分分式展开：**

$$
\mathbf{Y}_c(s) = \mathbf{Y}_c^\infty + \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k}.
$$

## 关键技术挑战

### 挑战 1：时变电感矩阵的处理

随转子角变化的 $\mathbf{L}(\theta)$ 若每步更新网络导纳矩阵，会导致 $O(N^3)$ 的矩阵重分解成本。解决方案包括：

- **恒定导纳转移法**：将转子角相关性转移到历史源（如 E-PD 模型）。
- **预测-校正法**：用上一时步值预测当前电感矩阵。

### 挑战 2：相域与 dq 坐标的接口同步

电机内部用 dq 状态、外部用 abc 端口时，两者的时间同步误差会注入网络：

- 延迟一步的端电压会导致接口误差。
- 需要迭代或预测校正来闭合接口。

VBR-EMTP 通过同步求解避免延迟，但计算量增加。

### 挑战 3：零序回路和不平衡的显式建模

相域模型的优势是可直接表示零序和不平衡通道，但：

- 变压器三角形连接会阻断零序电流。
- 接地阻抗选择影响零序路径。
- 非全相运行需要特殊处理。

### 挑战 4：开关事件和数值振荡

相域模型中开关动作会导致：

- 网络拓扑突变引起数值振荡。
- 历史项重置不当会产生虚假能量。
- 需要事件定位和一致性初始化。

### 挑战 5：频变参数和宽频建模

相域线路模型的频变参数需要：

- 稳定的矩阵有理函数拟合（VF 或 FpF）。
- 显式时延项处理（不同模态传播时间不同）。
- 计算效率和精度之间的权衡。

## 量化性能边界

| 模型 | 计算效率 | 步长容限 | 精度 | 适用场景 |
|------|----------|----------|------|----------|
| 经典 PD | 基线 | ~150 μs | 高 | 教学、单机 |
| VBR-EMTP | ~50x vs 传统 | 500 μs（@0.25%误差） | 高 | 多机系统 |
| E-PD | 175 FLOPs/step | ~50 μs | 高 | 大规模网络 |
| 磁路模型 | 中等 | 100 μs | 与10 μs参考一致 | 可编辑结构 |
| FpF-ULM | 依赖极点阶数 | 取决于频率范围 | 宽频带高 | 频变线路 |

**来源**：
- Xia et al. 2019：E-PD 每步 175 FLOPs，VBR 298 FLOPs，CC-PD 316 FLOPs。
- VBR-EMTP：500 μs 步长@0.25% 误差容限，传统 qd 接口仅 10 μs。
- Yonezawa 2023：100 μs 步长与 10 μs 参考波形级一致。
- Noda 2015：FpF-ULM 用于 500 kV 双回架空线路的宽频暂态验证。

## 适用边界与选择指南

| 场景 | 推荐模型 | 说明 |
|------|----------|------|
| 大规模多机 EMT 网络 | E-PD / VBR-EMTP | 恒定导纳减少矩阵重构 |
| 空间谐波和不平衡 | 磁路模型 | 可编辑结构支持用户自定义 |
| 多尺度仿真 | 解析信号法 | shift frequency 切换波形/包络 |
| 频变线路宽频暂态 | FpF-ULM | 按频段自适应加权拟合 |
| 平衡小系统教学 | 经典 PD | 物理意义直接 |
| 实时仿真 | E-PD + 恒定导纳 | 网络矩阵不变，计算量小 |

**失败模式**：
- 参数矩阵缺少物理来源，虽然形式上是相域，结果仍不可验证。
- 忽略互感、接地、电缆护套或三角形环流，会削弱相域模型的主要价值。
- 对强开关和断续事件不做事件定位或历史项重置，会产生数值振荡和虚假能量。
- 时变电感矩阵若每步更新不一致，可能导致网络矩阵频繁重构或接口延迟。
- 平均值模型不能自动代表开关级 EMT；开关模型也不自动代表器件寄生和高频封装效应。

## 优势与代价

相域模型的优势是边界条件直接、相别清楚、零序和不平衡通道显式，并且可自然表示开关和非线性。代价是矩阵规模和耦合程度较高，某些设备会出现时变电感或频变矩阵，实时仿真和大规模网络中需要矩阵复用、端口等效或模型降阶。

因此页面不应写"相域一定更准确"或"dq 一定更快"。精度和效率要看被建模对象、数值方法、步长、稀疏结构和验证目标。

## 与相关页面的关系

- [[three-phase-instantaneous-model]]：三相瞬时量模型入口。
- [[coordinate-transformation]]：相域与 alpha-beta、dq、序分量和模态域之间的变换。
- [[dq-transformation]]：控制器和电机内部旋转坐标。
- [[symmetrical-components]] 和 [[sequence-network-model]]：基频不平衡相量分析。
- [[time-domain-formulation]]：相域方程如何进入 EMT 时域求解。
- [[nodal-admittance-matrix]] 和 [[companion-circuit]]：相域网络离散和求解结构。
- voltage-behind-reactance (VBR) 同步机模型：VBR 同步机模型的 EMT 接口。
- [[synchronous-machine-model]]：同步电机模型的综合入口。

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Xia et al. 2019 - An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix | 2019 | E-PD 恒定诺顿导纳模型，175 FLOPs/step |
| Yonezawa 2023 - A phase-domain synchronous machine modeling technique by using magnetic circuit representation | 2023 | 磁路表示法，可编辑结构 |
| Noda 2015 - Application of frequency-partitioning fitting to the phase-domain frequency-dependent modeling | 2015 | FpF-ULM 相域频变线路 |
| Multi-scale Induction Machine Model in the Phase Domain with Constant Inner Impedance | 2019 | 解析信号多尺度，shift frequency 控制 |
| A Voltage Behind Reactance Synchronous Machine Model for the EMTP-Type Solution | 2019 | VBR-EMTP 同步求解接口 |
| Application of Frequency Partitioning Fitting to the Phase-Domain Frequency-Dependent Modeling | 2015 | 宽频线路的 FpF 辨识 |

## 修订与证据使用注意事项

后续扩展应优先补充模型输入、输出、端口变量、参数来源和验证对象。不要新增未绑定来源的典型步长、平台能力、误差百分比或"完全捕捉所有暂态"等强断言。
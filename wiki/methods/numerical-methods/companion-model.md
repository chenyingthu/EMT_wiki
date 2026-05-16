---
title: "伴随模型 (Companion Model)"
type: method
tags: [companion-model, discrete-time, equivalent-circuit, trapezoidal, emt, state-space, nodal-analysis]
created: "2026-05-02"
updated: "2026-05-16"
---

# 伴随模型 (Companion Model)

## 定义

伴随模型（Companion Model）是将连续时间动态元件（电感、电容、状态空间子系统）通过隐式数值积分离散化为"当前未知量的线性项 + 历史源项"的等效电路或端口模型，使每个时间步的暂态求解化为代数方程组的求解。形式上可写为：

$$
\mathbf{y}_{n+1} = \mathbf{Y}_{eq}\,\mathbf{u}_{n+1} + \mathbf{y}_{hist}^n \tag{1}
$$

其中 $\mathbf{u}_{n+1}$ 是当前时刻端口电压或电流（未知量），$\mathbf{Y}_{eq}$ 是由元件参数和积分步长 $\Delta t$ 决定的等效导纳/阻抗矩阵，$\mathbf{y}_{hist}^n$ 是由上一时刻状态和输入计算的历史源项。

伴随模型是 EMT 仿真中**设备模型与网络求解器之间的接口契约**：模型提供当前等效导纳/阻抗及历史源，求解器提供当前节点电压/支路电流，二者交替推进时间步。

## EMT 中的角色

EMT 仿真求解网络级微分-代数方程组（DAE），核心挑战在于储能元件（$L$、$C$）和状态空间子系统（控制系统、多端口电力电子）的离散化与联解。伴随模型将这一挑战拆解为两步：

1. **局部离散化**：每个储能元件或状态空间集群独立形成"导纳 + 历史源"的端口表示
2. **全局网络求解**：所有端口模型装配进统一节点导纳矩阵 $\mathbf{G}$，一次求解得到所有节点电压

随后各模型用节点电压回代更新内部状态，进入下一时间步。这一范式最早由 Dommel（1969）在 EMTP 中建立，后续扩展至状态空间集群（SSN）和描述符状态空间方程（DSE）。

## 核心机制

### 1. 单元件梯形积分伴随模型

对电感 $L$ 的电压-电流关系 $v_L = L\,\frac{\mathrm{d}i_L}{\mathrm{d}t}$，使用梯形积分（Trapezoidal Rule）：

$$
i_{L,n+1} = i_{L,n} + \frac{\Delta t}{2L}\left(v_{L,n} + v_{L,n+1}\right)
$$

整理为伴随电路形式：

$$
i_{L,n+1} = \underbrace{\frac{2L}{\Delta t}}_{G_{eq}}\,v_{L,n+1} + \underbrace{\left[i_{L,n} - \frac{2L}{\Delta t}\,v_{L,n}\right]}_{I_{hist}} \tag{2}
$$

式(2)对应诺顿伴随电路：等效电导 $G_{eq} = 2L/\Delta t$ 与历史电流源 $I_{hist}$ 并联。

对电容 $C$ 的电流-电压关系 $i_C = C\,\frac{\mathrm{d}v_C}{\mathrm{d}t}$，梯形积分同理得伴随电路为等效电阻 $R_{eq} = \Delta t/(2C)$ 与历史电压源 $E_{hist} = v_{C,n} - \frac{\Delta t}{2C}\,i_{C,n}$ 的串联（戴维南形式）。

### 2. 状态空间方程的离散伴随形式

对一般状态空间模型：

$$
\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u} \tag{3}
$$
$$
\mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u} \tag{4}
$$

使用梯形积分离散化（第 $n+1$ 步）：

$$
\mathbf{x}_{n+1} = \mathbf{x}_n + \frac{\Delta t}{2}\left(\dot{\mathbf{x}}_n + \dot{\mathbf{x}}_{n+1}\right)
$$

代入式(3)并整理，得：

$$
\left(\mathbf{I} - \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_{n+1} = \left(\mathbf{I} + \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_n + \frac{\Delta t}{2}\mathbf{B}\left(\mathbf{u}_n + \mathbf{u}_{n+1}\right) \tag{5}
$$

将式(5)代入输出方程式(4)，可写成式(1)的端口形式 $\mathbf{y}_{n+1} = \mathbf{Y}_{eq}\,\mathbf{u}_{n+1} + \mathbf{y}_{hist}^n$，其中 $\mathbf{Y}_{eq}$ 由 $\mathbf{C}$、$\mathbf{A}$、$\mathbf{B}$、$\mathbf{D}$ 和步长 $\Delta t$ 共同决定。

### 3. 状态空间集群节点法（SSN）

Dufour 等（2011）提出的 SSN 方法将任意规模的状态空间集群离散化后，等效为端口伴随模型接入全局节点导纳矩阵，实现状态空间子系统与节点网络的同步求解，而非事后迭代拼接。

SSN 集群分为两类：
- **V型（诺顿等效）**：$\mathbf{i}_{n+1} = \mathbf{Y}_{eq}\mathbf{v}_{n+1} + \mathbf{i}_{hist}^n$，端口电流注入方程
- **I型（戴维南等效）**：$\mathbf{v}_{n+1} = \mathbf{Z}_{eq}\mathbf{i}_{n+1} + \mathbf{v}_{hist}^n$，端口电压源代入节点方程

SSN 的7步算法：

> **Step 1**：求解稳态（复频域 $\mathbf{s}x = \mathbf{A}x + \mathbf{B}u$），初始化状态
> **Step 2**：推进至下一时刻点 $t_{n+1}$
> **Step 3**：确定开关位置，组装离散状态空间方程（对应 th 置换）
> **Step 4**：计算所有历史项，更新集群方程
> **Step 5**：如有需要，更新含所有集群贡献的全局节点导纳矩阵 $\mathbf{G}$
> **Step 6**：从各集群贡献更新右端项 $\mathbf{J}$
> **Step 7**：求解节点方程 $\mathbf{G}\mathbf{V} = \mathbf{J}$，回代至各集群更新状态

### 4. 描述符状态空间方程（DSE）

Sinkar 等（2021）提出的 DSE 方法用修正节点分析（MNA）直接从网表生成描述符方程：

$$
\mathbf{E}\dot{\mathbf{x}} = -\mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u} \tag{6}
$$

其中 $\mathbf{E}$ 可为奇异矩阵（允许线性相关状态），状态向量 $\mathbf{x}$ 包含节点电压、支路电流和电压源电流等 MNA 变量。梯形离散化后：

$$
\left(\mathbf{E} + \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_{n+1} = \left(\mathbf{E} - \frac{\Delta t}{2}\mathbf{A}\right)\mathbf{x}_n + \frac{\Delta t}{2}\mathbf{B}\left(\mathbf{u}_n + \mathbf{u}_{n+1}\right) \tag{7}
$$

DSE 与伴随电路（CC）接口时，将 DSE 子网转化为端口诺顿等效：

$$
\mathbf{i}_p(t) = \mathbf{G}_n\,\mathbf{v}_p(t) + \mathbf{I}_{hist} \tag{8}
$$

其中 $\mathbf{G}_n$ 由离散化矩阵和端口输入矩阵计算，$\mathbf{I}_{hist}$ 汇集上一时刻内部状态与源的影响。接口误差在 LCC-HVDC 算例中端口相电流最大绝对误差 0.003 kA，相对误差 0.15%（Sinkar 等 2021）。

### 5. 固定导纳模型

[[fixed-admittance]] 是一种特殊伴随模型路线，要求等效导纳矩阵在开关状态变化时**保持不变**。其优势是拓扑变化后无需重建 $\mathbf{G}$ 矩阵，缺点是精度受限（隐式积分精度优势部分损失）。典型应用场景：大规模线性网络（如频变线路）的预因子化 LU 分解加速。

## 形式化表达

| 积分方法 | 等效矩阵 | 历史项形式 | 数值阻尼 |
|---------|---------|-----------|---------|
| 梯形规则（Trapezoidal） | $\mathbf{Y}_{eq} = \frac{2\mathbf{C}}{\Delta t}$ 或 $\frac{\Delta t}{2\mathbf{L}}$ | $\mathbf{y}_{hist} = \mathbf{y}_n - \mathbf{Y}_{eq}\mathbf{u}_n$ | 无（中性与高频振荡风险） |
| 后向欧拉（Backward Euler） | $\mathbf{Y}_{eq} = \frac{\mathbf{C}}{\Delta t}$ 或 $\frac{\Delta t}{\mathbf{L}}$ | $\mathbf{y}_{hist} = \mathbf{y}_n$ | 正阻尼（数值耗散，低频精度略降） |
| Bilinear（Tustin）变换 | 与梯形规则等价（无频率预畸变） | 同梯形规则 | 无 |
| Gear（隐式多步）方法 | 变步长自适应 | 依赖多步历史 | 自适应阻尼 |

对 $R$ 支路：欧姆定律直接离散化，无历史项。

## 关键技术挑战

### 数值振荡

梯形积分在储能元件单独接地或开关动作时可能产生非物理高频振荡（ghost oscillations）。原因是梯形规则在开关瞬间的状态不连续导致等效历史源计算出现符号错误。解法：

1. **电阻切换法**（Damping Resistor）：开关断开瞬间在节点并联一个大阻尼电阻，吸收振荡能量
2. **历史项修正**：开关动作后重建历史源，而非仅更新开关状态
3. **后向欧拉起步**：仿真初始阶段使用后向欧拉建立稳态，再切换至梯形

### 开关事件处理

开关动作后的伴随模型面临三个问题：

1. **拓扑变化**：开关状态变化后 $\mathbf{G}$ 矩阵结构和历史源都需要重建
2. **电感电流初始值**：开关闭合瞬间电感电流不能突变，但历史源基于上一时刻 $i_L$ 计算，需重新初始化
3. **电容电压初始值**：同理，电容电压在开关闭合瞬间保持不变，开关后第一个时间步应基于该约束计算历史源

### 状态空间集群的开关组合爆炸

纯状态空间法对含 $m$ 个开关的系统，需要为 $2^m$ 种开关组合预先生成矩阵集。当 $m$ 较大时内存和时间急剧增加。SSN 方法通过**将状态空间集群作为整体接入节点网络**，将开关组合限制在集群内部，全局矩阵不受开关影响，从而缓解该问题。

### 变步长适配

变步长 EMT 中，历史源公式中的 $\Delta t$ 随时间步变化。若直接使用当前步长代入基于上一时刻 $\Delta t$ 计算的历史源，会产生截断误差传播。正确做法：

$$
\mathbf{y}_{hist}^{n+1} = \mathbf{y}_{hist}^n + \mathbf{Y}_{eq}\left(\mathbf{u}_n - \mathbf{u}_{n+1}\right) + \mathbf{Q}\left(\Delta t_n, \Delta t_{n+1}\right)
$$

其中 $\mathbf{Q}$ 是步长变化的修正项。对 SSN 集群还需重新计算 $\mathbf{Y}_{eq}$ 矩阵。

### 频变元件的离散伴随无源性

对含有频率相关参数的元件（如频变线路模型），其等效伴随模型在某些频段可能呈现**负阻尼**（无源性破坏），导致数值不稳定。处理方法：

1. **复频域拟合**：先对频变阻抗做矢量拟合（Vector Fitting），分解为 R-L-C 并联组合，再分别离散化
2. **无源性强迫**（Passivity Enforcement）：离散化后检查系统矩阵特征值，确保 $\mathrm{Re}(\lambda) \geq 0$
3. **递归卷积替代**：对延迟历史项使用递归卷积而非单历史源近似

## 量化性能边界

| 性能指标 | 数值 | 来源 |
|---------|------|------|
| DSE vs CC 速度比（大系统） | CC 约快 1.3 倍 | Sinkar 等 2021 |
| DSE-CC 接口误差（相电流） | 最大绝对误差 0.003 kA，相对误差 0.15% | Sinkar 等 2021 |
| SSN 预计算矩阵数量削减（三相系统，2组开关） | 从 $2^6 = 64$ 降至 $2^3 + 2^3 = 16$ | Dufour 等 2011 |
| 梯形 vs 后向欧拉数值阻尼 | 梯形规则无阻尼；后向欧拉在 $f\Delta t > 0.1$ 时显著耗散 | 工频 50Hz、$\Delta t = 50\mu s$ 下 $f\Delta t = 0.0025$ |
| 数值振荡频率（无阻尼 LC） | $f_{osc} = 1/(2\pi\sqrt{LC})$，与数值步长无关 | 解析 |

**注**：上表数据均来自原文可直接核验部分；Dufour 2011 原文验证章节中 IEEE 39 / 118 节点等系统测试的具体误差数字和运行时间表在当前可提取文本中不完整，未予引用。

## 适用边界与选择指南

| 场景 | 推荐方法 | 原因 |
|------|---------|------|
| 大规模线性网络，固定步长 | 梯形积分伴随电路（CC） | 稀疏矩阵求解效率高 |
| 含控制器的状态空间子系统 | SSN 或 DSE | 便于控制器接口、自动方程生成 |
| 开关组合多、实时仿真 | SSN 分组并行 | 避免矩阵组合爆炸，分组可并行 |
| 需要小信号/特征值分析 | DSE | 显式形成连续域状态矩阵，便于特征值提取 |
| 开关频繁的非线性系统 | 后向欧拉起步 + 梯形 | 初始阶段阻尼，后切换保证精度 |
| 频变线路等高精度需求 | 递归卷积 + 矢量拟合 | 避免伴随模型无源性破坏 |

## 相关页面

- [[companion-circuit]]：伴随模型的电路装配形式（具体元件层面的伴随电路图）
- [[trapezoidal-rule]]：梯形积分规则的精度、阻尼特性和实现细节
- [[backward-euler]]：后向欧拉方法的数值阻尼特性
- [[numerical-integration]]：数值积分方法的分类总览
- [[state-space-method]]：状态空间法在 EMT 中的建模与求解
- [[thevenin-norton-equivalent]]：戴维南/诺顿等效与伴随模型的端口对应关系
- [[fixed-admittance]]：固定导纳模型的特殊处理
- [[switch-modeling]]：开关模型的建立与事件处理
- [[dae-solvers]]：微分-代数方程组求解器与伴随模型的关系

## 来源论文

[[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] — Dufour 等 2011 提出了 SSN 状态空间集群节点法，将状态空间子系统作为集群接入节点导纳矩阵，实现并行求解和开关组合削减。

[[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — Sinkar 等 2021 比较了传统伴随电路（CC）和描述符状态空间方程（DSE）两种 EMT 建模路线，给出了 DSE-CC 接口的误差边界（0.003 kA / 0.15%）和速度对比（CC 约快 1.3 倍）。

[[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode]] — Dey 等 2021 用 TCSC 次同步共振算例比较了离散时间映射、动态相量和频域扫描三种 SSR 模型，其中离散时间模型基于梯形积分离散伴随形式，与伴随模型方法论直接相关。

[[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us]] — 该文支撑降维伴随模型机制：子模块先形成节点导纳和历史源，再通过 Schur 补递归消去内部节点，外部求解后反向回代恢复内部状态。

[[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss]] — 支撑线路伴随模型中的特性导纳、延时历史源和集中电阻近似组合。

[[双端口子模块mmc电磁暂态通用等效建模方法]] — 支撑双端口 MMC 子模块中后向欧拉伴随电容、节点分块消去和反向回代的中文来源证据。
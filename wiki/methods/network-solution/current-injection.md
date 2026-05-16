---
title: "电流注入法 (Current Injection Method)"
type: method
tags: [current-injection, inverter, interfacing, emt, modeling, nodal-analysis, companion-circuit, fixed-admittance]
created: "2026-05-02"
updated: "2026-05-16"
---

# 电流注入法 (Current Injection Method)

## 定义

电流注入法（Current Injection Method）是 EMT 网络方程中将外部设备、受控源或离散化元件表示为节点注入电流的核心接口技术。其本质是将元件的端口电气行为映射为两类标准量：**进入节点导纳矩阵 $\mathbf{Y}$ 的等效导纳**，和**进入右端电流向量 $\mathbf{i}$ 的历史电流源或受控电流注入**。

该方法是 [[nodal-analysis]] 和 [[companion-circuit]] 框架在实际 EMT 仿真中的衔接枢纽——所有动态元件（电感、电容、线路、开关）经伴随电路离散化后形成统一的诺顿等效形式，再通过电流注入接口接入节点方程统一求解。

## EMT 中的角色

在 EMT 仿真中，电流注入法承担三类功能：

1. **接口功能**：将换流器、电机、负荷等外部设备接入节点方程，使网络求解器只需处理标准代数方程 $\mathbf{Y}_n\mathbf{v}=\mathbf{i}$
2. **离散化适配功能**：将 [[companion-circuit]] 产生的历史电流源正确排列到注入向量中，确保数值积分的历史信息不被遗漏
3. **步长解耦功能**：通过将时变项放入右端向量而非左端矩阵，实现 LU 分解与步进的解耦（见 [[fixed-admittance]]）

核心挑战在于：不同类型元件的注入量更新时间步和幅值特性差异很大——开关器件在微秒级跳变，而电机电磁暂态在毫秒级——接口设计必须兼容这种异构时间尺度。

## 核心机制

### 统一数学形式

电流注入接口的通用形式为：

$$\mathbf{i}_{k+1} = \mathbf{Y}_{\mathrm{eq}}\mathbf{v}_{k+1} + \mathbf{i}_{\mathrm{hist},k+1}$$

其中：
- $\mathbf{Y}_{\mathrm{eq}}$：等效导纳矩阵块（进入 $\mathbf{Y}_n$ 的装配区）
- $\mathbf{i}_{\mathrm{hist},k+1}$：历史电流源向量（包含上一时刻状态、积分历史项、控制输出）

若采用梯形法离散化（见 [[trapezoidal-rule]]），对连接在节点 $p$ 和 $q$ 之间的电感和电容，等效导纳和历史电流源分别为：

**电感**（$G_{\mathrm{eq},L} = \Delta t/(2L)$）：
$$i_{L,k} = G_{\mathrm{eq},L}\,v_{L,k} + \underbrace{\left(i_{L,k-1} + G_{\mathrm{eq},L}\,v_{L,k-1}\right)}_{I_{\mathrm{hist},L}^{k-1}}$$

**电容**（$G_{\mathrm{eq},C} = 2C/\Delta t$）：
$$i_{C,k} = G_{\mathrm{eq},C}\,v_{C,k} - \underbrace{\left(G_{\mathrm{eq},C}\,v_{C,k-1} + i_{C,k-1}\right)}_{I_{\mathrm{hist},C}^{k-1}}$$

对于受控电流源（如 VSC 直流侧注入），接口形式为：
$$i_{\mathrm{dc},k+1} = \frac{P_k}{V_{c,k}}$$

其中 $P_k$ 为当前有功功率指令，$V_{c,k}$ 为直流电容电压。

### 接口执行步骤

电流注入接口的标准执行流程：

1. **读取上一时刻状态**：从存储器读取 $v_{k}$、$i_{k}$、控制状态量
2. **计算历史项**：对每个动态元件，用离散化公式计算 $I_{\mathrm{hist}}$
3. **更新受控源**：根据控制算法（如矢量控制、PWM 调制）更新受控电流/电压源输出
4. **装配右端向量**：将所有历史源和独立源累加到 $\mathbf{i}$ 向量对应位置
5. **求解节点方程**：执行 $\mathbf{Y}_n\mathbf{v}_{k+1}=\mathbf{i}_{k+1}$（若 $\mathbf{Y}_n$ 不变则只做前代回代）
6. **回代计算支路量**：从节点电压回代计算各支路电流
7. **保存当前状态**：将 $v_{k+1}$、$i_{k+1}$ 存入存储器供下一步使用

### 不同积分公式的等效电导对比

| 元件类型 | 梯形法 $G_{\mathrm{eq}}$ | 后向欧拉 $G_{\mathrm{eq}}$ | 特点 |
|---------|------------------------|---------------------------|------|
| 电感 $L$ | $\Delta t/(2L)$ | $\Delta t/L$ | 后向欧拉数值阻尼更强 |
| 电容 $C$ | $2C/\Delta t$ | $C/\Delta t$ | 后向欧拉使等效阻抗更大 |

## EMT 建模方法

### 方法 1：诺顿等效电流注入（标准法）

这是最基础的电流注入形式。每个动态支路表示为一个诺顿等效——并联的电导 $G_{\mathrm{eq}}$ 和电流源 $I_{\mathrm{hist}}$：

$$i_k = G_{\mathrm{eq}}\,v_k + I_{\mathrm{hist}}$$

**特点**：
- 与 [[nodal-admittance-matrix]] 完全兼容
- 等效电导恒定（步长不变时），可复用 LU 分解
- 需要在每个时步更新 $I_{\mathrm{hist}}$

**适用范围**：线性 R、L、C 元件，恒定参数线路，Bergeron 模型

### 方法 2：受控源电流注入（换流器接口）

对于 VSC、LCC 等换流器，交流侧和直流侧的接口量是受控源：

**交流侧受控电压源**：
$$v_{ca} = \frac{1}{2}d_a V_{\mathrm{dc}}$$
其中 $d_a = m\cos(\omega t + \delta)$ 为 A 相调制函数（来自矢量控制输出）

**直流侧受控电流源**：
$$i_{\mathrm{dc}} = \frac{P}{V_c}$$

**特点**：
- 换流器内部动态被压缩为端口注入量
- 避免详细开关拓扑，显著降低计算量（加速比 50%~70%，见来源论文）
- 需要保留调制函数与直流电压的耦合关系

**适用范围**：VSC-HVDC 平均值模型、LCC 逆变器 PAVM、储能变流器

### 方法 3：开关函数电流注入（详细开关模型）

在详细开关模型中，开关状态通过开关函数 $S(t) \in \{0,1\}$ 影响注入电流：

$$i_{\mathrm{sw},k+1} = S_k \cdot G_{\mathrm{eq}}\,v_{k+1} + I_{\mathrm{hist},k}$$

当 $S_k$ 变化时，$\mathbf{Y}_n$ 拓扑不变（因为使用恒导纳模型，见 [[fixed-admittance]]），但 $I_{\mathrm{hist}}$ 需要修正以反映开关动作时刻的等效电路跳变。

**特点**：
- 保留详细开关动态（开关谐波、故障瞬态）
- 需要脉冲源对或插值算法精确捕捉开关时刻
- 矩阵不变，但历史源处理复杂

**适用范围**：需要开关谐波分析的工况、故障暂态详细研究

### 方法 4：延迟接口电流注入（松耦合系统）

当换流器控制系统与 EMT 网络以松耦合方式连接时，使用上一时间步的量注入当前步：

$$i_{k+1}^{\mathrm{delayed}} = f(u_k, x_k)$$

其中 $u_k$ 和 $x_k$ 分别为 $k$ 时刻的控制输入和状态。

**特点**：
- 减少联立求解规模
- 引入步长相关误差（延迟 $\Delta t$）
- 适用于控制带宽远低于 EMT 步长倒数的情形

**适用范围**：多速率仿真、硬件在环（HIL）接口、大规模系统与控制器的分层仿真

### 方法 5：功率平衡电流注入（非线性源项）

对于功率控制型换流器，注入电流由功率设定值决定：

$$i = \frac{P + jQ}{v^*}$$

**特点**：
- 在低电压或相角快速变化时数值敏感（可能出现奇异性）
- 需要限幅和保护逻辑配合
- 适用于稳态运行点附近的小扰动分析

**适用范围**：潮流初始化、稳态运行研究、功率设定值跟踪

## 形式化表达

### 标准诺顿等效接口

对一般多端口元件，电流注入接口的矩阵形式为：

$$\begin{bmatrix} i_1 \\ i_2 \\ \vdots \\ i_n \end{bmatrix} = \begin{bmatrix} Y_{11} & Y_{12} & \cdots & Y_{1n} \\ Y_{21} & Y_{22} & \cdots & Y_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ Y_{n1} & Y_{n2} & \cdots & Y_{nn} \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} + \begin{bmatrix} i_{\mathrm{hist},1} \\ i_{\mathrm{hist},2} \\ \vdots \\ i_{\mathrm{hist},n} \end{bmatrix}$$

### VSC 交流侧接口方程

三相受控电压源形式：

$$v_{ca} = \frac{1}{2}d_a V_{\mathrm{dc}}, \quad v_{cb} = \frac{1}{2}d_b V_{\mathrm{dc}}, \quad v_{cc} = \frac{1}{2}d_c V_{\mathrm{dc}}$$

其中调制函数由矢量控制给出：

$$d_a = m\cos(\omega t + \delta), \quad d_b = m\cos(\omega t + \delta - 120^\circ), \quad d_c = m\cos(\omega t + \delta + 120^\circ)$$

### 直流侧功率平衡接口

$$i_{\mathrm{dc}} = \frac{P_{\mathrm{dc}}}{V_c} = \frac{1}{V_c}\sum_{phase} v_{phase}\,i_{phase}$$

### 伴随电感/电容历史源

**电感（梯形法）**：
$$I_{\mathrm{hist},L}^{k-1} = i_{L,k-1} + \frac{\Delta t}{2L}v_{L,k-1}$$

**电容（梯形法）**：
$$I_{\mathrm{hist},C}^{k-1} = -\left(\frac{2C}{\Delta t}v_{C,k-1} + i_{C,k-1}\right)$$

## 关键技术挑战

### 挑战 1：开关动作与历史源同步

当开关状态在时步内部变化时，历史源基于旧拓扑计算但方程基于新拓扑求解，导致非物理能量注入。

**缓解方法**：
- 插值定位开关动作时刻，减小事件时间误差
- CDA 算法（见 [[companion-circuit]]）在检测到跳变后切换为后向欧拉一步，利用数值阻尼衰减高频振荡
- 重初始化历史源，切断错误能量注入路径

### 挑战 2：控制采样与 EMT 步长不一致

数字控制器以固定采样周期 $T_s$ 更新输出，而 EMT 以仿真步长 $\Delta t$ 步进。当 $T_s \gg \Delta t$ 时，控制输出在多个 EMT 步长内保持不变；当 $T_s < \Delta t$ 时，需要子步更新接口。

**缓解方法**：
- 多速率接口：在控制采样时刻注入，保持 EMT 步长不变
- 子步更新：在控制周期内插值生成中间注入量
- 同步采样：将控制采样时刻对齐到最近的 EMT 步长边界

### 挑战 3：低电压下功率型电流源奇异性

当端口电压 $v \to 0$ 时，$i = P/v^*$ 趋向无穷大，导致数值奇异。

**缓解方法**：
- 在 $v$ 低于阈值时切换为电流限幅模式
- 采用 $i = P/\max(|v|, \epsilon)\,v^*$ 形式的正则化表达式
- 配合保护逻辑，在故障检测后旁路功率控制回路

### 挑战 4：端口方向约定不统一

不同建模者对"正注入电流"的定义可能相反（流入节点 vs 流出节点），导致等效电流源符号错误。

**缓解方法**：
- 在接口文档中明确约定：注入电流按 KCL 约定（流入为正）
- 在每个新元件接入时进行一致性检查
- 参考 [[companion-circuit]] 中规定的标准接口方向

### 挑战 5：LCC 换相过程的物理约束缺失

电流注入法只提供外部端口的等效电流，不包含换相过程中换相电压和直流电流约束的内部物理机制。换相失败、关断角跌落等故障模式不能仅由外部注入电流决定。

**缓解方法**：
- 保留换流器的内部等效电路（如 PAVM 中的换相失败检测模块），不做完全等效
- 在接口处注入换相失败判据，用事件驱动方式触发保护动作

## 量化性能边界

| 接口类型 | 精度损失 | 计算加速比 | 适用步长 | 失效场景 |
|---------|---------|-----------|---------|---------|
| 诺顿等效标准注入 | 无（恒步长） | 矩阵复用（1次 LU + N 次回代） | 任意 $\Delta t$ | 非线性元件迭代 |
| 受控源注入（VSC AVM） | <2%（稳态）/ <3%（暂态） | 50%~70% CPU 时间减少 | $\geq 40\mu$s | 开关谐波分析 |
| 受控源注入（VSC 全频谱） | <1.5%（暂态峰值） | 50%~60% CPU 时间减少 | $\geq 5\mu$s | 器件级应力分析 |
| 开关函数注入（详细开关） | 无精度损失 | 1x（基准对比） | $< 1\mu$s | 实时仿真 |
| 延迟接口松耦合 | $\propto \Delta t / T_s$ 延迟 | 步数减少比 = $T_s / \Delta t$ | 任意 | 控制带宽 > 1/(2$\Delta t$) |
| 功率平衡注入 | 数值奇异性风险 | 依赖控制策略 | $V > \epsilon$ | 低电压/故障穿越 |

**来源说明**：
- 50%~70% 加速比数据来自 [[a-vsc-hvdc-model-with-reduced-computational-intensity]]（2012 IEEE PESGM），测试系统为 100MW/100kV 两端 VSC-HVDC，PSCAD/EMTDC 仿真
- 误差数据（<2% 稳态、<3% 暂态）来自同一论文的对比验证
- 矩阵复用加速比计算：设系统有 $N$ 个动态元件，LU 分解复杂度 $O(N^3)$，前代回代复杂度 $O(N^2)$；使用恒导纳模型后每步只需 $O(N^2)$ 前代回代

## 适用边界与选择指南

| 应用场景 | 推荐接口类型 | 关键判据 |
|---------|------------|---------|
| 系统级 EMT 仿真（换流器数量 > 10） | 受控源注入（AVM） | 计算效率优先，详细开关动态非必要 |
| 换流器故障暂态分析 | 开关函数注入或受控源全频谱模式 | 需要开关谐波或闭锁动态 |
| 控制器参数扫描/优化 | 受控源注入（AVM） | 需要换流器动态响应，但计算量可控 |
| 硬件在环（HIL）接口 | 延迟接口松耦合 | 控制采样周期 $T_s$ 远大于 $\Delta t$ |
| 潮流初始化/稳态运行点计算 | 功率平衡注入 | 端口电压正常，无故障穿越需求 |
| MMC 子模块详细模型 | 诺顿等效 + 子模块级 ADC | 需要端到端精度 |

**不适用场景**：
- 换流器内部子模块动态研究（需详细等效电路）
- 器件级损耗和热应力分析（需半导体物理模型）
- 宽频带谐波和电磁干扰研究（需详细开关模型）

## 相关方法

- [[nodal-analysis]] — 节点分析框架，电流注入的装配目标
- [[nodal-admittance-matrix]] — 节点导纳矩阵的结构和装配规则
- [[companion-circuit]] — 伴随电路离散化，产生诺顿等效的标准方法
- [[fixed-admittance]] — 恒导纳策略，将开关状态变化从矩阵转移到右端向量
- [[vsc-model]] — VSC 换流器的物理建模，决定注入接口的设备含义
- [[lcc-model]] — LCC 换流器的物理建模，换相过程需要特殊处理
- [[average-value-model]] — 平均值模型，常与受控源注入配合使用
- [[trapezoidal-rule]] — 梯形积分公式，产生标准伴随电路离散化
- [[backward-euler]] — 后向欧拉公式，提供数值阻尼用于抑制振荡

## 来源论文

- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] — VSC-HVDC 动态平均值模型中受控电压源/电流源接口（2012 IEEE PESGM），提供 50%~70% CPU 加速比量化数据
- [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-]] — 多 VSC 开关事件用脉冲源对表示，避免频繁矩阵重构（PSCAD/EMTDC 多 VSC 两电平开关场景）
- [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] — LCC 逆变器 PAVM 中的电流源接口和换相失败检测（线换相逆变器平均值建模）
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — 伴随电路离散策略系统比较（Sinkar 2021），对比梯形法、后向欧拉、Gear-2 的精度和稳定性
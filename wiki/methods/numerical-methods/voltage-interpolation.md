---
title: "电压插值法 (Voltage Interpolation Method)"
type: method
tags: [voltage, interpolation, switching, inverter, emt, numerical, time-event, zero-crossing]
created: "2026-05-02"
updated: "2026-05-16"
---

# 电压插值法 (Voltage Interpolation Method)

## 定义与边界

电压插值法是在固定步长 EMT 中处理开关、触发或阈值事件的一类时间定位与状态重构方法。"电压"来自常见开关判据（节点电压穿越阈值），但实际实现也可能插值电流、门极信号、载波比较量、历史源或状态变量。

设事件函数 $g(t)$ 在相邻时间步 $t_n$ 和 $t_{n+1}$ 之间变号（即 $g(t_n) \cdot g(t_{n+1}) < 0$），则事件时刻 $t_z$ 可用线性插值估计：

$$
t_z = t_n + \alpha \Delta t, \quad \alpha = \frac{g(t_n)}{g(t_n) - g(t_{n+1})} \tag{1}
$$

其中 $\Delta t$ 为固定仿真步长，$\alpha \in [0,1]$ 为插值因子。开关前后状态按线性插值重构：

$$
\mathbf{x}(t_z^-) = (1-\alpha)\mathbf{x}_n + \alpha\mathbf{x}_{n+1}^{\text{old}} \tag{2}
$$

其中 $\mathbf{x}_{n+1}^{\text{old}}$ 为用开关前网络求得的状态量。本页讨论开关事件的数值接口，不把插值写成所有电力电子仿真的充分条件。器件寄生参数、门极动态、保护逻辑、矩阵更新和积分公式仍可能主导误差。

## EMT 中的作用

固定步长 EMT 在 $t_n$ 和 $t_{n+1}$ 之间推进。如果开关动作实际发生在步内，而仿真只在网格点改变拓扑或等效源，可能产生：

1. **事件时刻偏差**：开关动作被强制平移到下一网格点，相位误差积累
2. **历史项不一致**：梯形法历史项 $\mathbf{i}_{n+1} = f(\mathbf{v}_{n+1}, \mathbf{v}_n)$ 在拓扑突变后使用错误的上一时刻状态
3. **数值振荡（Chatter）**：梯形法在电感电压不连续处产生高频振荡
4. **虚假开关损耗**：非物理的电流截断导致功率计算错误

电压插值法的作用是：
- 在步内定位阈值穿越或触发时刻（式(1)）
- 在开关前后重构节点电压、支路电流和状态变量（式(2)）
- 与 [[trapezoidal-rule]] 或 [[backward-euler]] 历史项一起处理不连续
- 为 [[inverter-model]]、[[ideal-switch-model]]、[[detailed-switch-model]] 和 [[lcc-model]] 等页面提供开关时间接口背景

## 核心机制

### 线性阈值插值

线性阈值插值是最基础的电压插值方法。设开关判据为节点电压 $v_k(t)$ 穿越阈值 $V_{\text{th}}$：

$$
g(t) = v_k(t) - V_{\text{th}}
$$

若 $g(t_n) \cdot g(t_{n+1}) < 0$，则事件时刻由式(1)给出。该方法假设事件函数在步内单调，当 $g(t)$ 含高频振荡或斜率接近零时，定位可能不稳。

### 插值与阻尼积分联用（Na 2023）

Na 等提出的改进方法将插值/外推与半步长 Backward Euler 解耦合：

$$
\mathbf{x}(t_z + \Delta t/2) \leftarrow \text{BE}(\mathbf{x}(t_z^-), \Delta t/2) \tag{3}
$$

$$
\mathbf{x}(t_z + 3\Delta t/2) \leftarrow \text{TR}(\mathbf{x}(t_z + \Delta t/2), \Delta t) \tag{4}
$$

其中式(3)用半步 BE 避免不连续点注入振荡，式(4)用梯形法恢复后续精度。半步 BE 的等效导纳与全步梯形法兼容，是其能避免额外矩阵处理开销的实现基础。

### 矩阵指数法与 Dense Output（Li 2020）

矩阵指数法将电路在给定开关拓扑下写成状态空间方程 $\mathbf{x}' = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$，通过矩阵指数 $\exp(\Delta t \mathbf{A})$ 传播状态。对常值输入 $\mathbf{u}$，采用增广矩阵：

$$
\mathbf{x}_{\text{aug}} = \begin{bmatrix} \mathbf{x} \\ 1 \end{bmatrix}, \quad \mathbf{A}_{\text{aug}} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{0} & \mathbf{0} \end{bmatrix} \tag{5}
$$

$$
\mathbf{x}(t_0 + \Delta t) = \begin{bmatrix} \mathbf{I} & \mathbf{0} \end{bmatrix} \exp(\Delta t \mathbf{A}_{\text{aug}}) \mathbf{x}_{\text{aug}}(t_0) \tag{6}
$$

Dense output formula 从矩阵指数计算过程中提取步内状态（如半步点），使开关事件可精确定位而不依赖步首/步末两点线性插值。

### 临界阻尼调整（CDA）

CDA 在开关后用 Backward Euler 替代梯形法，利用 BE 的数值阻尼特性抑制振荡：

| 参数 | 梯形法 (TR) | 临界阻尼调整 (CDA) |
|------|-------------|-------------------|
| 稳定性 | A 稳定 | L 稳定 |
| 极点位置 | $z = 1$（纯虚轴） | $z \approx 1$（实轴，阻尼） |
| 数值振荡 | 可能激发 | 抑制 |
| 矩阵结构 | 对称 | 与 TR 相同 |

CDA 的优势是半步 BE 的导纳矩阵与一步 TR 相同，无需额外矩阵分解。

## 形式化表达

### 事件函数与插值因子

事件函数 $g(t)$ 可为电压、电流、功率或任意标量判据：

$$
g(t) = \begin{cases}
v_k(t) - V_{\text{th}} & \text{电压阈值} \\
i_l(t) & \text{电流过零} \\
P(t) - P_{\text{th}} & \text{功率阈值}
\end{cases} \tag{7}
$$

插值因子：

$$
\alpha = \frac{g(t_n)}{g(t_n) - g(t_{n+1})} = \frac{g(t_n)}{\Delta g_{n,n+1}} \tag{8}
$$

### 状态重构

状态向量插值（对任意连续状态量 $\mathbf{x}$）：

$$
\mathbf{x}(t_z^-) = \mathbf{x}_n + \alpha(\mathbf{x}_{n+1}^{\text{old}} - \mathbf{x}_n) \tag{9}
$$

电感电流历史项重构（关键：不连续电压不应注入历史源）：

$$
i_L(t_z^+) = i_L(t_z^-) \quad \text{（电流连续）} \tag{10}
$$

电容电压重构：

$$
v_C(t_z^+) = v_C(t_z^-) \quad \text{（电压连续）} \tag{11}
$$

### 多事件排序

设同一时刻检测到 $m$ 个开关事件，按事件函数绝对值排序：

$$
|\alpha_1| \leq |\alpha_2| \leq \cdots \leq |\alpha_m| \tag{12}
$$

事件 1 先发生，插值到 $t_{z,1}$ 后更新网络拓扑，再对事件 2 进行插值重构。

## EMT 建模方法

### 方法 1：线性阈值插值

**原理**：利用两端点线性估计事件时刻  
**数学表达**：式(1)、式(9)  
**特点**：实现简单、计算量小  
**适用场景**：PWM 调制、二极管自然换相、触发信号  
**失效场景**：事件函数非单调、高频振荡、斜率接近零

### 方法 2：插值 + 半步 BE 阻尼（Na 2023）

**原理**：半步 BE 数值阻尼抑制不连续点振荡  
**数学表达**：式(3)、式(4)  
**特点**：保持固定步长框架、避免额外矩阵更新  
**适用场景**：IGBT/二极管电路、晶闸管换相、含电感支路开关  
**量化数据**：Na 2023 报告比普通插值虚假损耗降低，耗时差异见原文

### 方法 3：矩阵指数 + Dense Output

**原理**：状态空间解析传播 + 步内状态提取  
**数学表达**：式(5)、式(6)  
**特点**：一阶精度面向速度、三阶精度面向精度  
**适用场景**：VSC-HVDC、TCR、可变拓扑电力电子  
**量化数据**：原文未给出具体加速比数字

### 方法 4：临界阻尼调整（CDA）

**原理**：BE 数值阻尼替代 TR 振荡极点  
**数学表达**：$\mathbf{Y}_{\text{BE}} = \mathbf{Y}_{\text{TR}}$，$\mathbf{i}_{\text{hist}}^{\text{BE}}$ 仅依赖上一时刻电流  
**特点**：矩阵结构兼容、插值框架不变  
**适用场景**：梯形法开关振荡抑制、实时 EMT  
**量化数据**：原文未报告具体数值

### 方法 5：外推同步

**原理**：事件后状态外推到固定网格点  
**数学表达**：$\mathbf{x}_{n+1} = \mathbf{x}(t_z^+) + \beta(\mathbf{x}(t_z^+) - \mathbf{x}(t_z^-))$，$\beta$ 为外推因子  
**特点**：保持固定步长框架  
**失效场景**：突变后误差放大

## 关键技术挑战

### 挑战 1：事件函数非单调

当 $g(t)$ 在步内多次穿越阈值（如振荡电流），线性插值可能误判最近过零点。**应对策略**：结合符号检测和过零时刻历史记录，优先判定首次穿越。

### 挑战 2：多开关事件排序冲突

多个阀在同一步内强耦合时，独立插值每个阀可能破坏网络一致性。**应对策略**：按式(12)排序后依次重构网络拓扑，或采用迭代求解器处理耦合事件。

### 挑战 3：电感电压不连续与历史源重构

开关导致电感电压不连续时，若不修正历史电流源，梯形法会将虚假电压注入下一时刻。**应对策略**：事件后第一段使用 BE（式(3)），或显式重算历史项。

### 挑战 4：实时平台 Deadline 约束

事件回溯和矩阵重构可能破坏实时平台的计算截止时间。**应对策略**：预分析最坏情况事件序列，预留足够时间裕度，或采用 CDA 而非回溯法。

### 挑战 5：精度与效率权衡

缩小步长可提高开关时刻精度，但计算代价线性增长。**应对策略**：事件前后使用自适应步长，或结合矩阵指数法在固定步长内提供高精度输出。

## 量化性能边界

| 方法 | 精度 | 计算开销 | 适用步长 | 已知量化数据 |
|------|------|----------|----------|-------------|
| 线性阈值插值 | $O(\Delta t)$ | 1 次插值 | 任意 | — |
| 插值 + 半步 BE | $O(\Delta t^2)$ | ~2× 线性插值 | $\leq 1 \mu s$ | Na 2023 报告虚假损耗降低 |
| 矩阵指数（三阶） | $O(\Delta t^3)$ | Padé 近似计算 | 任意 | 原文未给具体数值 |
| CDA | 依赖 BE 精度 | 1 次矩阵求解 | $\leq 1 \mu s$ | — |
| 外推同步 | $O(\Delta t^2)$ | 1 次外推 | 任意 | — |

## 适用边界与选择指南

| 场景 | 推荐方法 | 原因 |
|------|----------|------|
| PWM 逆变器调制 | 线性阈值插值 | 开关时刻可预测 |
| 二极管自然换相 | 插值 + 半步 BE | 避免电流截断 |
| 晶闸管强触发 | 插值 + 半步 BE | 换相过程电压不连续 |
| VSC-HVDC 可变拓扑 | 矩阵指数 + Dense Output | 高阶精度 |
| 实时 EMT 平台 | CDA | 矩阵结构兼容 |
| 多开关耦合系统 | 插值 + 半步 BE + 多事件排序 | 拓扑一致性 |

## 相关页面

- [[interpolation-method]] — 插值方法通用入口
- [[numerical-oscillation-suppression]] — 插值不足时的振荡处理
- [[companion-circuit]] — 历史源和储能元件离散化
- [[fixed-admittance]] — 减少开关矩阵更新的替代路线
- [[emt-simulation-verification]] — 开关插值结果验证框架
- [[offline-to-realtime-porting]] — 实时平台的 Deadline 约束评估
- [[backward-euler]] — BE 数值阻尼基础
- [[trapezoidal-rule]] — 梯形法历史项结构

## 来源论文

- [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu]] — Na 2023，插值 + 半步 BE 方法，虚假开关损耗降低，chatter 抑制
- [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo]] — Li 2020，矩阵指数 + Dense Output，三阶/一阶两种求解器，L 稳定性
- [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da]] — 插值/CDA 稳定性分析，CQLF 切换系统框架
- [[a-new-model-of-trapped-charge-sources-in-switching-transient-studies-in-the-pres]] — Akafi-Mobarakeh 2025，合闸暂态陷落电荷建模（PTCS）
- [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-.md]] — 混合仿真模式切换机制，与电压插值接口相关
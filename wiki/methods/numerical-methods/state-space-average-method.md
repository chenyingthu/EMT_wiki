---
title: "状态空间平均法 (State-Space Average Method)"
type: method
tags: [state-space, average, converter, modeling, small-signal, power-electronics, SSA, GSSA, P-GSSA]
created: "2026-05-02"
updated: "2026-05-16"
---

# 状态空间平均法 (State-Space Average Method)

## 定义

状态空间平均法（State-Space Averaging，SSA）将开关周期内多个电路状态方程按持续时间加权平均，形成连续时间平均模型。设开关导通子区间的状态方程为 $\dot{x}=A_1x+B_1u$、$y=C_1x+D_1u$，关断子区间为 $\dot{x}=A_2x+B_2u$、$y=C_2x+D_2u$，若占空比为 $d$、开关周期为 $T_s$，则平均状态方程为：

$$\dot{\bar{x}}=\left[dA_1+(1-d)A_2\right]\bar{x}+\left[dB_1+(1-d)B_2\right]\bar{u}$$

$$\bar{y}=\left[dC_1+(1-d)C_2\right]\bar{x}+\left[dD_1+(1-d)D_2\right]\bar{u}$$

SSA 由 Cuk 于 1976 年提出，与 [[switching-function-method]] 互补——开关函数给出二值或连续占空比，状态空间平均法给出对应状态方程。它不同于 [[switch-modeling]]：后者处理器件通断事件和拓扑变化，SSA 有意将开关周期内的细节压缩掉。SSA 也是 [[average-value-model]] 的常见推导路径之一。

## EMT 中的角色

在 EMT 仿真中，状态空间平均法常用于：

- 为 DC-DC 变换器、VSC、MMC 子系统建立低频等值，支撑控制器设计和小扰动线性化
- 在系统级 EMT 或混合仿真中减少开关事件数量（{{c N}} 个开关周期可合并为 1 个分段 {{c N}} 个时间尺度扩展）
- 为详细开关模型和平均值模型之间的切换提供状态变量映射
- 导出控制和阻抗小信号模型（与 [[small-perturbation-linearization]] 联用）

其核心挑战是：**开关周期内状态变化较大时平均化误差扩大**，尤其在低开关频率、强谐振或故障瞬间。因此 SSA 不能单独回答器件应力、死区波形、开关损耗、反向恢复或 EMI 问题——这些问题需要 [[switch-modeling]]、详细等值模型或器件级模型补充。

## 核心方程

### 基本 SSA 建模

设载波为 $v_c$、调制波为 $v_m$，PWM 开关函数为：

$$S_i = \begin{cases} 1 & v_m > v_c \\ 0 & v_m \le v_c \end{cases}, \quad i = a,b,c$$

对于周期性开关动作的 PWM 变流器，在单个开关周期 $T_s$ 上对状态方程平均化：

$$x(t) = x(t_0) + \int_{t_0}^{t}\left[f(x(s)) + \sum_{i=1}^{N}f_i(x(s)) \cdot b_i(d_i(x(s)) - \mathrm{tri}(s,T_s))\right]ds$$

其中 $d_i$ 为第 $i$ 相的占空比（$d_i = \frac{1}{T_s}\int_{t-T_s}^{t}S_i(\tau)d\tau$）。稳态时取 $D$、$X$、$U$ 为工作点，对扰动 $\hat{x}$、$\hat{u}$、$\hat{d}$ 做一阶近似，得小信号模型：

$$\dot{\hat{x}} = A_{\mathrm{avg}}\hat{x} + B_{\mathrm{avg}}\hat{u} + \left[(A_1-A_2)X + (B_1-B_2)U\right]\hat{d}$$

该式只保留工作点附近的一阶动态。大信号切换、模式跳变和非连续导通需要重新建模。

### 分段状态空间平均法 (P-SSA)

分段状态空间平均法（Piecewise SSA，P-SSA）将仿真时间 $T_L$ 分解为若干子区间 $[t_n, t_{n+1}]$，在每个分段子区间上建立独立的分段平均方程：

$$m: \quad \dot{y}(\tau) = T_n\left[A_0y(\tau)+b_0+\sum_{i=1}^{m}(A_i y(\tau)+b_i)D_i(\tau)\right]$$

其中 $D_i(\tau) = \frac{1}{L_s/T_n}\int_{L_s/T_n-N}^{L_s/T_n}S_i(\tau)d\tau$，$T_n$ 为第 $n$ 段分段时长。P-SSA 的分段原则是**将占空比相似、动作特性一致的开关周期合并**，以 1~3 个载波周期为宜。稳态分段可取 2~3 个开关周期，暂态分段限制为单个开关周期。

### 广义状态空间平均法 (GSSA)

广义状态空间平均法（Generalized SSA，GSSA）以傅里叶变换为基础，对时域状态变量 $x(t)$ 在区间 $(t-T_s, t)$ 内展开为傅里叶级数：

$$x(t) = \sum_{q=-\infty}^{\infty}x_q(t)e^{jq\omega_st}, \quad x_q(t) = \frac{1}{T_s}\int_{t-T_s}^{t}x(t)e^{-jq\omega_st}dt$$

利用傅里叶变换的微分性质 $\frac{dx_q}{dt} = f_q(x)_q - jq\omega_sx_q$ 和卷积性质 $xy_q = \sum_{i=-\infty}^{\infty}x_{q-i}y_i$，建立状态方程：

$$\dot{x}_q(t) = f_q(x)_q - jq\omega_sx_q(t), \quad q = 0, \pm 1, \pm 2, \ldots$$

保留的谐波阶数 $q$ 越高，模型越接近详细模型；当只保留 $q=0$（基波分量）时，GSSA 退化为基本 SSA。理论上 GSSA 可以包含任意高频分量，突破 SSA 的局限，但阶数过高会导致求解运算量增大。

### 分段广义状态空间平均法 (P-GSSA)

分段广义状态空间平均法（Piecewise GSSA，P-GSSA）将分段方法与 GSSA 有机结合，在分段子区间 $T_n = [t_n, t_{n+1}]$ 上对状态变量进行傅里叶展开。当选取的交流分量次数为 $q$ 时，三相 PWM 逆变器的 P-GSSA 状态方程为：

$$\dot{x}_0(t) = A_0x_0(t) + b_0 + \sum_{i=1}^{m}(A_ix_0(t)+b_i)S_i(t)$$

$$\dot{x}_q(t) = A_0x_q(t) + b_0 + \sum_{i=1}^{m}(A_ix_q(t)+b_i)S_i(t) - jq\omega_sx_q(t), \quad |q| \ge 1, \quad t \in T_n$$

对应的分段平均向量场为：

$$f_P(\tau, y) = \sum_{q=-\infty}^{\infty}\int_k^{k+1}\left[A_0y(\tau)_q + b_0 + \sum_{i=1}^{m}(A_i y(\tau)_q + b_i)S_i(\tau)\right]d\tau$$

分段 GSSA 实现了"动态变尺度"：对于 10kHz 开关频率，若合理分段取 2 个周期仍保证精度，分段时间从 $100\mu s$ 扩展到 $200\mu s$，等效于将"开关频率"从 10kHz 降到 5kHz，从而提升仿真效率。

### 混合 SSA-GSSA 模型

针对三相双有源桥（3p-DAB）变流器，Berger 等（2018）提出混合 SSA-GSSA 建模方法。当 $0° \le d \le 30°$ 时，控制到输出传递函数为：

$$G_{vd}(s) = \frac{\hat{v}_o(s)}{\hat{d}(s)} = \frac{\omega_s L_s / R}{sR_c + 1} \cdot \frac{mR_V}{m\omega_s L_s}$$

输入阻抗 $Z_D(s)$ 为：

$$Z_D(s) = \frac{\hat{v}_i(s)}{\hat{i}_i(s)} = \left(\frac{\omega_s L_s}{mR_V}\right)^2 \cdot \frac{sR_c+1}{R_V}$$

null 输入阻抗 $Z_N(s)$ 为：

$$Z_N(s) = -\frac{\hat{v}_i(s)}{\hat{i}_i(s)}\bigg|_{\hat{v}_o(s)=0} = \frac{\omega_s L_i}{mV_o d}$$

其中 $d$ 为相移角，$m$ 为变压器变比，$R_c$ 为等效电容电阻，$\omega_s = 2\pi f_s$。当 $30° < d \le 90°$ 时，传递函数形式不同（见 Berger 2018 式 (20)-(23)）。**SSA 在相移角较大时（$d > 30°$）精度显著下降**，因为 $\dot{x}$ 的变化不再"缓慢"——这正是 SSA 基本假设被破坏的区域。

## 形式化表达

### SSA 方程总结

| 方程 | 表达式 | 说明 |
|------|--------|------|
| 开关函数 | $S_i = 1(v_m > v_c)$ | PWM 比较运算 |
| 占空比 | $d_i = \frac{1}{T_s}\int_{t-T_s}^{t}S_i(\tau)d\tau$ | 开关周期平均 |
| 状态平均 | $\dot{\bar{x}} = [dA_1+(1-d)A_2]\bar{x}+[dB_1+(1-d)B_2]\bar{u}$ | 核心平均化方程 |
| 小信号 | $\dot{\hat{x}} = A_{\mathrm{avg}}\hat{x}+B_{\mathrm{avg}}\hat{u}+[(A_1-A_2)X+(B_1-B_2)U]\hat{d}$ | 扰动线性化 |
| GSSA 傅里叶 | $x(t) = \sum_{q=-\infty}^{\infty}x_q(t)e^{jq\omega_st}$ | 谐波展开 |
| P-GSSA | $\dot{x}_q(t) = A_0x_q+b_0+\sum_i(A_ix_q+b_i)S_i-jq\omega_sx_q$ | 分段+谐波 |

### 3p-DAB SSA 传递函数（$0° \le d \le 30°$）

| 传递函数 | 表达式 |
|----------|--------|
| $G_{vd}(s)$ | $\cfrac{mR_V\omega_s / R}{sR_c+1} \cdot \cfrac{1}{m\omega_s L_s}$ |
| $G_{vg}(s)$ | $\cfrac{mRd\;\omega_s / R}{sR_c+1} \cdot \cfrac{1}{m\omega_s L_s}$ |
| $Z_D(s)$ | $\left(\cfrac{\omega_s L_s}{mR_V}\right)^2 \cdot \cfrac{sR_c+1}{R_V}$ |
| $Z_N(s)$ | $-\cfrac{\omega_s L_i}{mV_o d}$ |
| $Z_o(s)$ | $-\cfrac{R}{sR_c+1}$ |

## EMT 建模方法

### 方法 1：基本 SSA 模型

**原理**：在开关周期 $T_s$ 上对两个子区间的状态方程加权平均，得到连续平均模型。该方法与 Dommel 算法结合形成的暂态模型被广泛认可并应用于变流器稳态设计与暂态稳定性研究。

**EMT 实现**：
- 步长可取为开关周期的 10 倍甚至更大（Wang 2019: 开关频率 1kHz 时步长 $10\mu s$）
- 每个开关周期计算一次占空比 $d_i$，然后组装平均状态矩阵 $[dA_1+(1-d)A_2]$
- 适用于 CCM（连续导通模式）PWM 变流器

**局限性**：忽略开关纹波和采样效应；不适用于 DCM、故障态、闭锁态。

### 方法 2：分段 SSA 模型 (P-SSA)

**原理**：将仿真时间按占空比变化分段，每段独立建立平均方程。分段依据是相邻开关周期占空比的方差是否小于设定阈值 $\varepsilon_1$。

**EMT 实现**：
- 检测开关函数占空比方差 $\sigma_r$，若 $\sigma_r < \varepsilon_1$ 则将连续 $r$ 个周期合并
- 稳态分段 2~3 个周期，暂态分段 1 个周期
- 通过分段实现变步长，暂态自动收窄步长，稳态自动放宽步长

**量化性能**：Wang 2019 对 10kHz 三相 PWM 逆变器的测试表明，稳态分段数约 989 段时误差为 1.32%（表1）。

### 方法 3：广义 SSA 模型 (GSSA)

**原理**：保留状态变量的多个傅里叶谐波分量（$|q| \le q_{\max}$），利用傅里叶级数展开克服 SSA 只能描述基频分量的局限。

**EMT 实现**：
- 选取 $q_{\max}$（通常不超过 10 阶），每个时间步需要求解 $2q_{\max}+1$ 个状态方程
- 利用傅里叶变换的微分和卷积性质，状态方程中每出现 $x$ 的乘积项就产生卷积和
- 精度与 $q_{\max}$ 正相关，$q_{\max}=0$ 时退化为 SSA

**局限性**：要求状态变量在开关周期内满足傅里叶变换条件；阶数选择缺乏严格依据；高阶时计算量大。

### 方法 4：分段 GSSA 模型 (P-GSSA)

**原理**：在分段子区间上应用 GSSA，兼顾分段（变步长效率）和谐波展开（精度）双重优势。

**EMT 实现**：
- 每个分段区间独立确定谐波阶数 $q$，通过误差反馈自适应调整
- 分段依据"近周期性"原则（占空比方差阈值 $\varepsilon_1$），分段时长 1~3 个开关周期
- Wang 2019 提出的分段决策流程：检测变工况时刻 $\rightarrow$ 动态调整分段数 $n$ $\rightarrow$ 各段独立求解

**量化性能**（Wang 2019 算例）：
- 开关频率 10kHz / 暂态 / 分段数 1243：误差 0.49%
- 开关频率 10kHz / 稳态 / 分段数 989：误差 1.32%
- 开关频率 1kHz / 暂态 / 分段数 126：误差 4.08%
- 误差随开关频率升高而减小，与 $T_s = 1/f_c$ 大致成正比

### 方法 5：混合 SSA-GSSA 模型

**原理**：对不同传递函数采用不同的建模精度——$G_{vd}(s)$、$G_{vg}(s)$、$Z_o(s)$ 用 SSA 足够精确；对 $Z_D(s)$、$Z_N(s)$ 需要 GSSA 才能保证精度（Berger 2018）。

**EMT 实现**：
- 在 EMTP 中实现 SSA 部分（6 个状态变量：$\hat{v}_o, \hat{i}_i, \hat{d}, \hat{v}_i$）
- 对于 null 输入阻抗 $Z_N(s)$，需要用 GSSA 获得相移角 $d$ 的非线性影响
- 混合策略：在相移角 $d > 30°$ 的工作点，将 SSA 部分切换为 GSSA

**关键发现**（Berger 2018）：SSA 在 $d > 30°$ 时对 $Z_D(s)$ 和 $Z_N(s)$ 的预测不准确，需要用 GSSA。SSA 在 $0° \le d \le 30°$ 范围内仍是有用的工程近似，但超出该范围后基本假设被破坏。

### 方法 6：考虑死区的 SSA 模型

**原理**：在基本 SSA 中显式引入死区效应。桥臂关断时引入额外的零电压插值阶段，等效电路中的占空比函数需要修正为含死区补偿项的形式：

$$d_i^{\mathrm{eff}} = d_i - \frac{t_{\mathrm{dead}}}{T_s}$$

**EMT 实现**：
- MMC 子模块中上桥臂关断后、下桥臂导通前存在插零阶段
- 需要在状态方程中引入额外的状态向量描述插零拓扑
- 该方法将 SSA 扩展到 MMC 等多电平变流器的闭锁工况

## 量化性能边界

| 建模方法 | 适用场景 | 精度 | 效率提升 | 代表性局限 |
|----------|----------|------|----------|------------|
| 基本 SSA | CCM PWM，稳态小扰动 | 中等（基频） | 10×~100×（vs 详细开关） | 不适用 DCM、故障态 |
| P-SSA | 含工况切换的变流器 | 中等偏高 | 5×~20× | 分段依据缺乏严格数学证明 |
| GSSA | 谐波敏感任务 | 高（多谐波） | 3×~10× | 阶数选择难，计算量大 |
| P-GSSA | 大规模新能源并网变流器 | 高 | 5×~50×（Wang 2019） | 傅里叶条件限制 |
| 混合 SSA-GSSA | 3p-DAB，小信号稳定性分析 | 精确 | 10×~30× | $d>30°$ 时 SSA 失效 |
| 死区补偿 SSA | MMC，含死区逆变器 | 中等 | 5×~15× | 需额外状态变量 |

**典型量化数据**：

- **Wang 2019（P-GSSA）**：10kHz 三相 PWM 逆变器，稳态误差 1.32%，暂态误差 0.49%，仿真效率提升约 5×（相比详细开关模型）
- **Berger 2018（混合 SSA-GSSA）**：3p-DAB $Z_N(s)$ 在 $d=60°$ 时，SSA 预测误差 > 30%，GSSA 误差 < 5%
- **原文未报告**可核验的 SSA 方法在 > 100 电平 MMC 或 > 10MW 换流站中的量化性能边界数据

## 关键技术挑战

### 挑战 1：纹波敏感性与谐波保留的矛盾

SSA 在开关周期上平均化，直接丢弃了开关纹波。对于电容电压纹波、开关谐波和 EMI 问题，平均模型无法提供可信赖的结果。**解决路径**：GSSA 保留更多谐波分量（$|q|=1,2,\ldots$），但阶数选择（$q_{\max}$）缺乏通用判据；或者在 EMT 中保留开关模型，仅在接口处使用 SSA 等效。

### 挑战 2：分段依据的严格数学证明

P-SSA 和 P-GSSA 的分段原则（"占空比方差 < 阈值"）是工程经验性的，缺乏严格的数学证明。Wang 2019 的仿真结果表明该方法有效，但对于其他拓扑（多电平、MMC）分段阈值的普适性尚未建立。**解决路径**：基于李雅普诺夫稳定性或误差界的自适应分段算法是该方向的研究前沿。

### 挑战 3：null 输入阻抗 $Z_N(s)$ 的建模困难

Berger 2018 指出，null 输入阻抗 $Z_N(s)$ 的推导是 SSA 在 DAB 建模中最具挑战性的部分，因为它涉及控制相位 $\hat{d}$ 的非线性效应。用 SSA 推导的 $Z_N(s)$ 在 $d>30°$ 后误差显著，而 GSSA 需要在闭环系统中移除控制器才能获得解析表达式。**解决路径**：混合 SSA-GSSA 方法（在 SSA 框架下处理非线性项，用 GSSA 处理阻抗）是当前最优实践。

### 挑战 4：模型切换时的状态一致性

平均状态与详细开关状态之间切换时，电感电流、电容电压和历史项必须匹配。切换瞬间若状态不一致，会导致 EMT 仿真中的数值冲击或不稳定。**解决路径**：切换前执行状态映射（通过 $d$ 重建平均状态），或采用双模型并行运行逐步过渡。

### 挑战 5：数字控制的采样延迟建模

离散或采样数据模型将采样-保持（S&H）和计算延迟引入 SSA 框架，需要额外状态变量描述数字控制器的记忆效应。对于高频 PWM（> 20kHz）或载波频率接近奈奎斯特频率的场景，采样延迟效应不可忽略。**解决路径**：在 SSA 状态方程中引入延时项 $e^{-sT_d}$，或用 z 域离散化替代 s 域连续模型。

## 适用边界与选择指南

| 场景 | 推荐方法 | 不适用 |
|------|----------|--------|
| DC-DC 降压/升压，CCM，稳态 | 基本 SSA | DCM，故障态 |
| 含工况切换（大信号扰动） | P-SSA 或 P-GSSA | 高频谐振分析 |
| 谐波敏感（谐振变换器、故障态） | GSSA 或 P-GSSA | 基频动态分析 |
| 大规模新能源并网（光伏/风电 DC-AC） | P-GSSA | - |
| 3p-DAB 小信号稳定性分析 | 混合 SSA-GSSA | $d > 30°$ 用 SSA |
| MMC 含死区/闭锁工况 | 死区补偿 SSA | 基本 SSA |
| 数字控制器（采样延迟敏感） | 离散 SSA（z 域） | 连续 SSA |
| 高开关频率（> 20kHz）EMI 分析 | 详细等值模型（[[detailed-equivalent-model]]） | SSA |

## 变体体系

| 变体 | 处理对象 | 主要边界 |
|------|----------|----------|
| 基本 SSA | 连续导通、固定拓扑 PWM | 忽略开关纹波和采样效应 |
| 小信号 SSA | 工作点附近控制设计 | 不适合大扰动和限幅动作 |
| P-SSA | 不同运行区间分别平均 | 需要明确区间切换规则 |
| GSSA | 保留若干傅里叶系数/谐波 | 截断频带决定可见动态 |
| P-GSSA | 变步长谐波保留 | 傅里叶条件和阶数选择 |
| 混合 SSA-GSSA | DAB 阻抗精确建模 | $d$ 工作范围限制 |
| 离散/采样 SSA | 数字控制和采样延迟 | 依赖采样/保持和计算延迟建模 |

## 相关方法 / 相关模型 / 相关主题

- [[average-value-model]] — SSA 常用于构造 AVM 的内部动态
- [[switching-function-method]] — 开关函数给出占空比，SSA 给出对应状态方程
- [[small-perturbation-linearization]] — 在 SSA 工作点附近导出控制和阻抗小信号模型
- [[state-space-method]] — 更一般的状态变量建模框架
- [[dynamic-phasor]] — 另一类保留选定频率系数的平均化表示
- [[detailed-equivalent-model]] — SSA 与详细等值模型之间的切换接口
- [[switch-modeling]] — 详细开关模型，SSA 的精度对比基准

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti|Wang 等 - 2019]] | 2019 | 提出 P-GSSA 方法，应用于大规模新能源并网变流器；稳态 1.32%/暂态 0.49% 误差；分段决策流程 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation with SVC]] | 2009 | SVC 动态相量混合仿真，SSA 作为 EMT-TS 接口基准 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Berger 等 - 2018]] | 2018 | 混合 SSA-GSSA 建模 3p-DAB；$Z_D$/$Z_N$ 传递函数推导；SSA 在 $d>30°$ 精度失效 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Berger 等 - 2018b]] | 2018 | 同一工作的第二部分 |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient|Comparison and Selection of Grid-Tied Inverter Models]] | 2021 | 并网逆变器模型对比（SSA/AVM/DEM），量化误差边界 |
| [[多有源桥型电力电子变压器简化电磁暂态等效模型|多有源桥型 PET 简化模型]] | 2023 | 多有源桥型电力电子变压器的 SSA 简化等效建模 |
| [[考虑死区特性的全桥型mmc状态空间平均化建模方法|考虑死区特性的全桥型 MMC SSA]] | 2024 | 含死区补偿的 MMC 状态空间平均化建模方法 |
| [[线性开关电路电磁暂态分析的状态方程法|线性开关电路状态方程法]] | — | 状态方程法与 EMT 开关电路分析的关系 |
---
title: "经济调度 (Economic Dispatch)"
type: method
tags: [economic-dispatch, generation, optimization, lambda-iteration, lagrange, power-system-operation, optimal-power-flow]
created: "2026-05-02"
updated: "2026-05-16"
---

# 经济调度 (Economic Dispatch)

## 定义与边界

经济调度（Economic Dispatch, ED）是在给定系统拓扑、负荷水平、机组可用状态和运行约束下，分配各发电单元有功出力以实现某一经济目标（通常为燃料成本最小化）的优化问题。它是电力系统运行与规划中的核心决策问题之一，与[[optimal-power-flow]]（含安全约束的扩展形式）和发电机组启停决策（Unit Commitment, UC）共同构成电力系统优化调度体系。

ED 的边界条件需要明确界定：

- **时间尺度**：ED 运行于分钟至小时级调度时间尺度，输出的是给定调度时段（15 min、1 h 或 4 h）内的机组出力设定值，不包含启停决策或跨时段耦合约束。
- **问题类型**：ED 是静态优化问题（单时段独立求解），而非动态优化或多阶段决策问题。
- **与 EMT 的关系**：ED 不是电磁暂态核心求解方法。它运行在稳态或准稳态时间尺度，输出运行点、出力计划和边界条件；EMT 仿真求解瞬时电压电流和设备控制动态。将 ED 结果用于 EMT 研究时，应把它视为**工况生成和初始化来源**，而不是 EMT 网络方程、伴随电路或开关暂态的替代。

## EMT 中的角色

ED 在 EMT 仿真工作流中承担**前处理工况设定**的角色，具体表现为：

1. **稳态运行点初始化**：ED 提供各发电机有功出力设定值，结合[[power-flow-calculation]]给出节点电压幅值/相角，作为 EMT 仿真 $t=0$ 时刻的初始条件。正确的初始化使仿真从系统实际运行点而非零状态启动，抑制虚假启动暂态（参见 [[steady-state-initialization]]）。

2. **慢-快时间尺度接口**：在 [[electromechanical-electromagnetic-hybrid-simulation]] 中，机电侧调度或 ED 层给出慢时间尺度的有功分配，EMT 侧保留局部三相瞬时动态和电力电子控制响应。接口变量通常是 PCC 有功 $P$ 和无功 $Q$ 指令，经 [[interface-technique]] 注入 EMT 侧。

3. **工况筛选与批量仿真**：可再生能源并网研究（如 [[renewable-energy-integration]]）中，先用 ED 或 OPF 筛选高负荷、弱电压、潮流重载等典型工况，再对关键场景进行 EMT 时域精细仿真，评估谐波、换相失败或控制稳定性。

4. **运行边界约束 EMT 验证**：ED 的等式约束（功率平衡）和不等式约束（线路热极限、电压限值）通过 OPF 变为安全约束后，约束边界内的运行点由 EMT 仿真验证暂态稳定性。ED 本身不提供动态安全边界，该功能需由 [[small-signal-stability]] 或 [[transient-stability]] 分析承担。

ED 通常不解析开关波形、谐波、暂态过电压、换流器保护动作或快速控制环细节；这些需要 EMT 模型和时域仿真支撑。

## 输入与输出

### 典型输入

| 输入类型 | 具体内容 | 在 EMT 中的角色 |
|---------|---------|----------------|
| 机组成本曲线 | 二次型 $C_i(P_{Gi}) = a_i P_{Gi}^2 + b_i P_{Gi} + c_i$ 或分段线性报价 | 定义优化目标 |
| 机组出力限值 | $P_{Gi}^{\min} \leq P_{Gi} \leq P_{Gi}^{\max}$ | 约束条件 |
| 爬坡限制 | $\Delta P_{Gi}^{\max}$（上爬/下爬速率） | 约束条件 |
| 系统负荷 | $P_D, Q_D$（给定调度时段） | 功率平衡等式右端 |
| 备用需求 | 正/负旋转备用容量 | 约束条件 |
| 网络模型 | 线路参数、变压器变比（可选） | 影响网损 $P_{\text{loss}}$ 计算 |
| 无功/电压约束 | 节点电压限值、无功出力限值（可选） | 约束条件 |

### 典型输出

| 输出类型 | 具体内容 | 在 EMT 中的角色 |
|---------|---------|----------------|
| 机组有功出力 | $P_{G1}^*, P_{G2}^*, \dots, P_{GN}^*$ | 发电机初始化设定值 |
| 系统边际成本 | 拉格朗日乘子 $\lambda^*$（元/MWh） | 经济信号，不直接参与 EMT |
| 约束影子价格 | 紧绑定约束的对偶变量 | 评估约束紧张度 |
| 网损估计 | $P_{\text{loss}}$ | 精确功率平衡需网损项 |
| 稳态运行点 | 节点电压幅值/相角、线路功率 | 经 PF 转换后作为 [[steady-state-initialization]] 输入 |

## 数学形式

### 基本经济调度（无约束版本）

在忽略网络约束（令 $P_{\text{loss}} = 0$）且机组成本函数为严格凸可微的简化条件下，基本 ED 写为：

$$
\min_{P_G} \quad \sum_{i=1}^{N_G} C_i(P_{Gi}) = \sum_{i=1}^{N_G} \left( a_i P_{Gi}^2 + b_i P_{Gi} + c_i \right) \tag{1}
$$

满足功率平衡约束：

$$
\sum_{i=1}^{N_G} P_{Gi} = P_D \tag{2}
$$

以及机组出力边界约束：

$$
P_{Gi}^{\min} \leq P_{Gi} \leq P_{Gi}^{\max}, \quad i = 1, 2, \dots, N_G \tag{3}
$$

#### 拉格朗日乘子法求解

构造拉格朗日函数：

$$
\mathcal{L} = \sum_{i=1}^{N_G} C_i(P_{Gi}) + \lambda \left( P_D - \sum_{i=1}^{N_G} P_{Gi} \right) \tag{4}
$$

对每台机组求一阶最优性条件：

$$
\frac{\partial \mathcal{L}}{\partial P_{Gi}} = \frac{dC_i}{dP_{Gi}} - \lambda = 0, \quad i = 1, 2, \dots, N_G \tag{5}
$$

对于二次型成本函数 $C_i(P_{Gi}) = a_i P_{Gi}^2 + b_i P_{Gi} + c_i$，有：

$$
\frac{dC_i}{dP_{Gi}} = 2a_i P_{Gi} + b_i \tag{6}
$$

联立式 (5) 和 (6) 得到各机组的增量成本率与系统边际成本 $\lambda$ 的关系：

$$
P_{Gi}^* = \frac{\lambda - b_i}{2a_i}, \quad i = 1, 2, \dots, N_G \tag{7}
$$

将式 (7) 代入功率平衡约束 (2)，可求解 $\lambda$：

$$
\sum_{i=1}^{N_G} \frac{\lambda - b_i}{2a_i} = P_D \tag{8}
$$

解得：

$$
\lambda^* = \frac{2\sum_{i=1}^{N_G} \frac{b_i}{2a_i} + P_D}{\sum_{i=1}^{N_G} \frac{1}{2a_i}} \tag{9}
$$

式 (9) 给出了系统边际成本 $\lambda^*$ 的解析表达式，各机组最优出力由式 (7) 直接计算。**这正是 $\lambda$ 迭代法的核心原理**：通过协调各机组的增量成本率使之外等于系统边际成本 $\lambda^*$，从而实现全局经济最优。

#### 迭代 $\lambda$ 算法

当成本函数为分段线性或含阀点效应（Valve Point Effect）时，解析解不存在，需用数值迭代求 $\lambda$：

```
算法 1：λ迭代法
输入：负荷 P_D，机组参数 (a_i, b_i, c_i, P_i^min, P_i^max)
输出：各机组最优出力 P_Gi^*，系统边际成本 λ^*

1. 初始化 λ_low, λ_high（覆盖所有机组增量成本范围）
2. 重复直到 |∑P_Gi(λ) - P_D| < ε：
   a. λ_mid = (λ_low + λ_high) / 2
   b. 对每台机组 i：
        若 2a_i>0，计算 P_Gi(λ_mid) = (λ_mid - b_i)/(2a_i)
        否则令 P_Gi(λ_mid) = P_i^max（低端机组优先满发）
   c. 计算总出力 P_sum = ∑P_Gi(λ_mid)
   d. 若 P_sum > P_D：λ_low = λ_mid（供给过多，提高边际成本目标）
      若 P_sum < P_D：λ_high = λ_mid（供给不足，降低边际成本目标）
3. 返回 P_Gi^*, λ^*
```

该算法的收敛性取决于成本函数的凸性假设。对于严格凸成本函数，$\lambda$ 迭代在 $O(N_G \log(1/\epsilon))$ 次迭代内收敛。

### 含网损修正的经济调度

当考虑网络约束和网损时，功率平衡约束修正为：

$$
\sum_{i=1}^{N_G} P_{Gi} = P_D + P_{\text{loss}}(\mathbf{P}_G) \tag{10}
$$

网损 $P_{\text{loss}}$ 是各节点注入功率的非线性函数，通常用 B 系数法近似：

$$
P_{\text{loss}} = \sum_i \sum_j P_{Gi} B_{ij} P_{Gj} + \sum_i B_{i0} P_{Gi} + B_{00} \tag{11}
$$

其中 $B_{ij}$ 为网损 B 系数矩阵元素（由网络参数和潮流分布决定）。增量网损修正各机组的等价边际成本：

$$
\frac{dC_i}{dP_{Gi}} = \lambda \left( 1 + \frac{\partial P_{\text{loss}}}{\partial P_{Gi}} \right) \tag{12}
$$

**注意**：B 系数法是在特定潮流分布下线性化的结果，不适用于重载或大范围潮流变化的场景。

### 安全约束经济调度（SCED）

安全约束经济调度（Security Constrained Economic Dispatch, SCED）在基本 ED 基础上叠加线路热极限和节点电压约束：

$$
\min \quad \sum_{i=1}^{N_G} C_i(P_{Gi}) \tag{13}
$$

满足：

$$
\sum_{i=1}^{N_G} P_{Gi} = P_D + P_{\text{loss}} \tag{14}
$$

$$
P_{Gi}^{\min} \leq P_{Gi} \leq P_{Gi}^{\max} \tag{15}
$$

$$
|P_{ij}(\mathbf{P}_G)| \leq P_{ij}^{\max}, \quad \forall (i,j) \in \text{lines} \tag{16}
$$

$$
|V_k^{\min}| \leq |V_k| \leq |V_k^{\max}|, \quad \forall k \in \text{buses} \tag{17}
$$

式 (16) 线路潮流约束和式 (17) 节点电压约束使 SCED 的可行域可能收缩，导致最优解与无约束 ED 不同。SCED 等价于 [[optimal-power-flow]] 的简化版本（无安全约束的 OPF 包含电压约束）。

### 多时段经济调度

当调度时段 $t = 1, 2, \dots, T$ 跨期耦合时（爬坡约束、备用约束），问题变为多时段优化：

$$
\min \quad \sum_{t=1}^T \sum_{i=1}^{N_G} C_i(P_{Gi}(t)) \tag{18}
$$

满足每时段功率平衡和跨时段爬坡约束：

$$
\sum_{i=1}^{N_G} P_{Gi}(t) = P_D(t), \quad \forall t \tag{19}
$$

$$
-P_{Gi}^{\text{ramp}} \leq P_{Gi}(t) - P_{Gi}(t-1) \leq P_{Gi}^{\text{ramp}}, \quad \forall i,t \tag{20}
$$

式 (20) 限制了相邻时段间机组出力的变化率，刻画了发电机爬坡能力的物理限制。多时段 ED 的维数为 $N_G \times T$，当 $N_G$ 和 $T$ 均较大时，问题规模可能超出传统求解器的实时计算能力。

## 形式化表达

### 核心公式汇总

| 编号 | 公式 | 含义 |
|------|------|------|
| (1) | $\min \sum C_i(P_{Gi})$ | 目标函数：总燃料成本最小化 |
| (2) | $\sum P_{Gi} = P_D$ | 等式约束：功率平衡 |
| (3) | $P_i^{\min} \leq P_{Gi} \leq P_i^{\max}$ | 不等式约束：机组出力限值 |
| (6) | $dC_i/dP_{Gi} = 2a_i P_{Gi} + b_i$ | 增量成本率（二次成本） |
| (7) | $P_{Gi}^* = (\lambda - b_i)/(2a_i)$ | 机组最优出力（$\lambda$ 迭代核心） |
| (9) | $\lambda^* = (2\sum b_i/(2a_i) + P_D) / \sum 1/(2a_i)$ | 系统边际成本解析解 |
| (10) | $\sum P_{Gi} = P_D + P_{\text{loss}}$ | 含网损的功率平衡 |
| (11) | $P_{\text{loss}} = \sum_i \sum_j P_{Gi} B_{ij} P_{Gj}$ | B 系数网损近似 |
| (12) | $dC_i/dP_{Gi} = \lambda(1 + \partial P_{\text{loss}}/\partial P_{Gi})$ | 网损修正的等微增率条件 |
| (16) | $|P_{ij}| \leq P_{ij}^{\max}$ | 线路热极限约束 |
| (20) | $|P_{Gi}(t) - P_{Gi}(t-1)| \leq P_i^{\text{ramp}}$ | 爬坡约束 |

### 等微增率条件的几何意义

等微增率条件 $\frac{dC_i}{dP_{Gi}} = \lambda$ 的几何含义是：在系统边际成本 $\lambda$ 固定时，各机组按照"增量成本率随出力增加上升最快（斜率 $2a_i$ 最大）的机组先增加出力"的原则分配负荷，直至所有机组的增量成本率都等于 $\lambda^*$。这等价于按各机组成本曲线的切线斜率从低到高依次上网——成本最低的机组先满发，然后次低的机组补上，直到边际成本达到平衡。

## 关键技术挑战

### 挑战1：成本函数的非线性与非凸性

实际机组的成本曲线常含**阀点效应**（Valve Point Effect），即汽轮机调节阀开启时的非线性跳变：

$$
C_i(P_{Gi}) = a_i P_{Gi}^2 + b_i P_{Gi} + c_i + |d_i \sin(e_i (P_{Gi}^{\min} - P_{Gi}))| \tag{21}
$$

阀点项的存在使成本函数不再严格凸，增量成本率在阀点处不单调，$\lambda$ 迭代可能收敛到局部最优或振荡不收敛。

**解决思路**：用分段线性逼近阀点效应，将问题分解为若干凸子问题；或使用进化算法（GA、PSO）处理非凸性，但无法保证全局最优。

### 挑战2：大规模系统的实时计算

当系统含数千台机组（如中国国家电网含数千台火电机组）时：

- 变量维数：$N_G$ 可达 $O(10^3)$~ $O(10^4)$
- 约束数量：含爬坡、备用、N-1 安全约束时，约束总数达 $O(10^4)$~ $O(10^5)$
- 计算时间要求：实时调度要求在秒级完成（调度周期 $1 \sim 15$ min 内需多次重算）

**解决思路**：拉格朗日松弛分解（将搞合约束松弛后用子梯度法迭代求解）、Benders 分解（将安全约束行生成）、或并行优化（将多区域系统解耦并行求解）。

### 挑战3：新能源不确定性建模

风电、光伏出力的不确定性使负荷 $P_D$ 不再是确定性参数。含新能源的 ED 通常用场景法（Scenario Approach）处理：

$$
\min \quad \sum_{s=1}^{N_s} p_s \sum_{i=1}^{N_G} C_i(P_{Gi}^s) \tag{22}
$$

满足每场景功率平衡：

$$
\sum_{i=1}^{N_G} P_{Gi}^s = P_D^s, \quad \forall s \tag{23}
$$

其中 $p_s$ 为场景 $s$ 的概率，$P_D^s$ 为该场景下的负荷。新能源渗透率提高使备用需求增加，ED 的约束条件随之扩展。

### 挑战4：离散控制与混合整数优化

含储能（ESS）、抽水蓄能、机组的启停状态时，决策变量含整数：

$$
\min \quad \sum_t \sum_i \left[ C_i(P_{Gi}(t)) + S_i^{\text{start}} u_i(t) + S_i^{\text{stop}} v_i(t) \right] \tag{24}
$$

满足最小启停时间约束：

$$
(u_i(t) - u_i(t-1)) + (v_i(t) - v_i(t-1)) \leq 1 \tag{25}
$$

$$
\sum_{\tau = t - T_i^{\text{on}}+1}^t u_i(\tau) \geq T_i^{\text{on}} (u_i(t) - u_i(t-1)) \tag{26}
$$

这是混合整数规划（MIP）问题，计算复杂度为 NP-hard，实时求解困难。

### 挑战5：EMS/SCADA 接口与数据质量

ED 的输入（成本参数、机组限值、负荷预测）来自能源管理系统（EMS）或数据采集与监控系统（SCADA）。数据质量问题包括：

- 机组成本曲线未及时更新（老旧报价数据）
- 负荷预测误差传递导致 ED 结果偏离实际最优
- 机组出力遥测延迟或丢帧导致状态估计不准确

**解决思路**：ED 结果需要通过状态估计（State Estimation）进行坏数据检测，或在 [[electromechanical-electromagnetic-hybrid-simulation]] 接口处进行一致性校验。

## 量化性能边界

| 指标 | 典型范围 | 说明 |
|------|---------|------|
| $\lambda$ 迭代收敛精度 | $\epsilon \leq 10^{-4}$ pu | 功率不平衡量容限 |
| 单机组 ED 求解时间 | $O(N_G)$ 线性（无约束）$\sim O(N_G^{1.5})$（含安全约束） | 主流商业求解器实测 |
| 大规模系统（$N_G > 500$）实时求解 | 需分解或并行化，否则超过秒级 | 中国国家电网级别系统的实际挑战 |
| 新能源替代率 | 取决于调峰能力，通常 $< 60\%$（受爬坡约束限制） | DEZhou 风电场实测（Wang et al. 2022） |
| 成本节约（ED vs 无调度） | $3\% \sim 8\%$ 燃料成本下降 | 取决于负荷曲线和机组组合 |
| 调度周期 | $5 \sim 15$ min（实时调度），$1 \sim 24$ h（日前调度） | 与电网调度规程相关 |

## 适用边界与选择指南

| 场景 | 推荐方法 | 不适用场景 |
|------|---------|-----------|
| 小型系统（$N_G \leq 50$）、凸成本、无约束 | $\lambda$ 迭代法 | 含阀点效应的大系统 |
| 中型系统（$N_G \leq 500$）、含网损修正 | 序列二次规划（SQP） | 需要实时性的大系统 |
| 大规模系统（$N_G > 1000$）、需安全约束 | 拉格朗日松弛 + Benders 分解 | 需保证全局最优性的研究 |
| 含新能源不确定性 | 随机规划（场景法）/ 鲁棒优化 | 算力受限的实时调度 |
| 含启停和最小启停时间 | 混合整数规划（MIP） | 实时性要求高的场景 |
| 作为 EMT 工况初始化来源 | 确定 ED → [[power-flow-calculation]] → EMT | 直接做暂态稳定性分析 |

## 相关方法

- [[power-flow-calculation]] — 提供 ED 出力目标的稳态网络解，是把调度出力转化为 EMT 初值的必要环节
- [[optimal-power-flow]] — 将经济目标与潮流方程、线路约束、电压约束统一进优化框架，是 ED 的安全约束扩展
- [[steady-state-initialization]] — 说明如何把稳态运行点转换为 EMT 初始状态
- [[electromechanical-electromagnetic-hybrid-simulation]] — 机电侧 ED/OPF 输出作为接口边界条件向 EMT 侧提供运行点
- [[emt-simulation]] — 关注瞬时值时域仿真，与经济调度处于不同建模层级
- [[transient-stability]] — ED 的约束边界需经暂态稳定分析验证动态安全性
- [[small-signal-stability]] — 小扰动下系统稳定性由特征根分析评估，不在 ED 范畴内

## 来源论文

本页内容基于电力系统优化调度领域通用模型和算法，未引用特定论文的原始量化结果。具体成本系数、市场规则和求解器性能数据需绑定实际数据源。
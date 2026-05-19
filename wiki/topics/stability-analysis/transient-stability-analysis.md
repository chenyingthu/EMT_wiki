---
title: "暂态稳定性分析 (Transient Stability Analysis)"
type: topic
tags: [transient-stability, stability, rotor-angle, power-system, direct-methods, time-domain, hybrid-methods]
created: "2026-05-02"
updated: "2026-05-03"
---

# 暂态稳定性分析 (Transient Stability Analysis)



<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="880" height="70" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="450" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">应用场景</text>
  <rect x="30" y="40" width="150" height="30" rx="6" fill="#fff" stroke="#2563eb" stroke-width="1"/>
  <text x="105" y="59" text-anchor="middle" font-size="11" fill="#1e40af">系统规划设计</text>
  <rect x="195" y="40" width="150" height="30" rx="6" fill="#fff" stroke="#2563eb" stroke-width="1"/>
  <text x="270" y="59" text-anchor="middle" font-size="11" fill="#1e40af">运行方式安排</text>
  <rect x="360" y="40" width="150" height="30" rx="6" fill="#fff" stroke="#2563eb" stroke-width="1"/>
  <text x="435" y="59" text-anchor="middle" font-size="11" fill="#1e40af">保护整定配合</text>
  <rect x="525" y="40" width="150" height="30" rx="6" fill="#fff" stroke="#2563eb" stroke-width="1"/>
  <text x="600" y="59" text-anchor="middle" font-size="11" fill="#1e40af">紧急控制策略</text>
  <rect x="690" y="40" width="150" height="30" rx="6" fill="#fff" stroke="#2563eb" stroke-width="1"/>
  <text x="765" y="59" text-anchor="middle" font-size="11" fill="#1e40af">安全稳定计算</text>
  <line x1="450" y1="80" x2="450" y2="105" stroke="#333" stroke-width="1.5" marker-end="url(#arr1)"/>
  <defs><marker id="arr1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#333"/></marker></defs>
  <rect x="10" y="110" width="880" height="70" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="450" y="128" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">分析方法</text>
  <rect x="30" y="140" width="250" height="30" rx="6" fill="#fff" stroke="#16a34a" stroke-width="1"/>
  <text x="155" y="159" text-anchor="middle" font-size="11" fill="#166534">时域仿真法 (TDS)</text>
  <rect x="295" y="140" width="250" height="30" rx="6" fill="#fff" stroke="#16a34a" stroke-width="1"/>
  <text x="420" y="159" text-anchor="middle" font-size="11" fill="#166534">直接法 (EAC/能量函数)</text>
  <rect x="560" y="140" width="300" height="30" rx="6" fill="#fff" stroke="#16a34a" stroke-width="1"/>
  <text x="710" y="159" text-anchor="middle" font-size="11" fill="#166534">混合方法 (SIME/BCU)</text>
  <line x1="450" y1="180" x2="450" y2="205" stroke="#333" stroke-width="1.5" marker-end="url(#arr1)"/>
  <rect x="10" y="210" width="880" height="70" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="450" y="228" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">稳定判据与指标</text>
  <rect x="30" y="240" width="160" height="30" rx="6" fill="#fff" stroke="#d97706" stroke-width="1"/>
  <text x="110" y="259" text-anchor="middle" font-size="11" fill="#92400e">转子角/角速度判据</text>
  <rect x="205" y="240" width="160" height="30" rx="6" fill="#fff" stroke="#d97706" stroke-width="1"/>
  <text x="285" y="259" text-anchor="middle" font-size="11" fill="#92400e">临界清除时间 (CCT)</text>
  <rect x="380" y="240" width="160" height="30" rx="6" fill="#fff" stroke="#d97706" stroke-width="1"/>
  <text x="460" y="259" text-anchor="middle" font-size="11" fill="#92400e">能量裕度指标</text>
  <rect x="555" y="240" width="160" height="30" rx="6" fill="#fff" stroke="#d97706" stroke-width="1"/>
  <text x="635" y="259" text-anchor="middle" font-size="11" fill="#92400e">稳定裕度灵敏度</text>
  <rect x="730" y="240" width="130" height="30" rx="6" fill="#fff" stroke="#d97706" stroke-width="1"/>
  <text x="795" y="259" text-anchor="middle" font-size="11" fill="#92400e">TSI 综合指标</text>
  <line x1="450" y1="280" x2="450" y2="305" stroke="#333" stroke-width="1.5" marker-end="url(#arr1)"/>
  <rect x="10" y="310" width="880" height="70" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="450" y="328" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">控制措施</text>
  <rect x="30" y="340" width="180" height="30" rx="6" fill="#fff" stroke="#7c3aed" stroke-width="1"/>
  <text x="120" y="359" text-anchor="middle" font-size="11" fill="#5b21b6">预防控制 (发电再调度)</text>
  <rect x="225" y="340" width="180" height="30" rx="6" fill="#fff" stroke="#7c3aed" stroke-width="1"/>
  <text x="315" y="359" text-anchor="middle" font-size="11" fill="#5b21b6">紧急控制 (切机/切负荷)</text>
  <rect x="420" y="340" width="180" height="30" rx="6" fill="#fff" stroke="#7c3aed" stroke-width="1"/>
  <text x="510" y="359" text-anchor="middle" font-size="11" fill="#5b21b6">直流功率调制</text>
  <rect x="615" y="340" width="250" height="30" rx="6" fill="#fff" stroke="#7c3aed" stroke-width="1"/>
  <text x="740" y="359" text-anchor="middle" font-size="11" fill="#5b21b6">WAMS广域监测与控制</text>
  <rect x="10" y="400" width="12" height="12" rx="2" fill="#dbeafe" stroke="#2563eb"/>
  <text x="27" y="410" font-size="10" fill="#333">应用场景</text>
  <rect x="120" y="400" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a"/>
  <text x="137" y="410" font-size="10" fill="#333">分析方法</text>
  <rect x="230" y="400" width="12" height="12" rx="2" fill="#fef3c7" stroke="#d97706"/>
  <text x="247" y="410" font-size="10" fill="#333">稳定判据</text>
  <rect x="340" y="400" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="357" y="410" font-size="10" fill="#333">控制措施</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 暂态稳定性分析：应用场景→分析方法→稳定判据→控制措施四层体系架构</p>
## 核心原理详解

### 技术概述
暂态稳定性分析是电力系统电磁暂态仿真领域的重要技术，对提高仿真精度和效率具有重要意义。

### 理论基础
该技术建立在严格的电磁场理论和电路分析基础之上，通过数学建模描述系统的动态行为。

### 核心机制
- **物理建模**：基于物理定律建立准确的数学模型
- **数值求解**：采用高效的数值算法求解系统方程
- **参数分析**：研究关键参数对系统性能的影响

### 技术优势
- 提高仿真精度和计算效率
- 支持复杂系统的详细分析
- 为工程设计和优化提供理论支撑

## 概述

暂态稳定性分析是电力系统安全评估的核心内容，研究电力系统在遭受大扰动（如短路故障、线路跳闸、发电机跳闸等）后，同步电机是否能够保持同步运行并最终恢复到稳定平衡状态的能力。暂态稳定性关注的是系统在扰动后**第一摇摆周期**（通常为故障后1-3秒）内的动态行为。

### 暂态稳定性的定义

根据IEEE定义，暂态稳定性是指电力系统在给定初始运行工况下，遭受大扰动后达到一个可以接受的稳态运行点的能力。暂态失稳的主要表现形式是：

- **转子角失稳**：发电机转子之间相对角度持续增大，导致同步运行破坏
- **电压崩溃**：关键母线电压持续下降，无法恢复
- **频率崩溃**：系统频率持续偏离额定值

### 暂态稳定性分析的重要性

| 应用场景 | 分析目的 |
|---------|---------|
| 系统规划设计 | 评估网络结构、机组配置的稳定性 |
| 运行方式安排 | 确定安全运行边界和传输极限 |
| 保护整定配合 | 验证保护动作时间满足稳定要求 |
| 紧急控制策略 | 制定切机、切负荷等控制措施 |
| 安全稳定计算 | 在线安全评估和预防控制 |


## EMT中的作用

暂态稳定性分析 (Transient Stability Analysis) 在EMT仿真中的核心作用：

- **研究范围**：界定暂态稳定性分析 (Transient Stability Analysis)在EMT仿真中的研究边界和应用场景
- **分析方法**：提供暂态稳定性分析 (Transient Stability Analysis)相关的EMT分析方法和工具
- **系统影响**：分析暂态稳定性分析 (Transient Stability Analysis)对电力系统电磁暂态特性的影响
- **仿真验证**：为暂态稳定性分析 (Transient Stability Analysis)相关研究提供仿真验证框架
## 形式化表达

从EMT仿真角度，暂态稳定性分析 (Transient Stability Analysis)可形式化表达为：

$$
\begin{cases}
\dot{\delta}_i = \omega_i - \omega_0 \\
\frac{2H_i}{\omega_0}\dot{\omega}_i = P_{mi} - P_{ei} - D_i(\omega_i - \omega_0) \quad (i = 1, 2, \ldots, n)
\end{cases}
$$
## 摇摆方程 (Swing Equation)

### 基本形式

同步电机的转子运动由摇摆方程描述：

$$
M\frac{d^2\delta}{dt^2} = P_m - P_e - D\frac{\mathrm{d}\delta}{\mathrm{d}t}
$$

或采用标幺值形式：

$$
\frac{2H}{\omega_0}\frac{d^2\delta}{dt^2} = P_m - P_e - D\frac{\mathrm{d}\delta}{\mathrm{d}t}
$$

其中：
- $M$：惯性常数（单位：MJ/MVA·s）
- $H$：惯性时间常数（单位：s）
- $\delta$：转子角度（单位：rad或度）
- $\omega_0$：同步角速度（377 rad/s，60Hz系统）
- $P_m$：机械输入功率（标幺值）
- $P_e$：电磁输出功率（标幺值）
- $D$：阻尼系数

### 状态空间形式

将二阶方程转化为一阶方程组：

$$
\begin{cases}
\frac{\mathrm{d}\delta}{\mathrm{d}t} = \omega - \omega_0 \\
\frac{2H}{\omega_0}\frac{\mathrm{d}\omega}{\mathrm{d}t} = P_m - P_e - D(\omega - \omega_0)
\end{cases}
$$

### 电磁功率表达式

对于单机无穷大系统：

$$
P_e = \frac{E'V}{X_{eq}}\sin\delta = P_{max}\sin\delta
$$

其中：
- $E'$：发电机暂态内电势
- $V$：无穷大母线电压
- $X_{eq}$：等值电抗
- $P_{max}$：最大传输功率


## 时域仿真方法 (Time-Domain Simulation)

### 基本原理

时域仿真通过数值积分求解微分-代数方程组（DAE）：

$$
\begin{cases}
\dot{x} = f(x, y, u) & \text{(微分方程)} \\
0 = g(x, y, u) & \text{(代数方程)}
\end{cases}
$$

其中 $x$ 为状态变量，$y$ 为代数变量，$u$ 为控制输入。

### 数值积分方法

#### 1. 隐式梯形法 (Trapezoidal Rule)

$$
x_{n+1} = x_n + \frac{h}{2}[f(x_n, y_n) + f(x_{n+1}, y_{n+1})]
$$

**优点**：
- A-稳定，数值稳定性好
- 适合求解刚性系统
- 允许较大步长

**缺点**：
- 每步需迭代求解非线性方程
- 计算量较大

#### 2. 龙格-库塔法 (Runge-Kutta)

四阶龙格-库塔公式：

$$
x_{n+1} = x_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
$$

其中：
$$
\begin{aligned}
k_1 &= f(t_n, x_n) \\
k_2 &= f(t_n + \frac{h}{2}, x_n + \frac{h}{2}k_1) \\
k_3 &= f(t_n + \frac{h}{2}, x_n + \frac{h}{2}k_2) \\
k_4 &= f(t_n + h, x_n + hk_3)
\end{aligned}
$$

#### 3. 预测-校正法 (Predictor-Corrector)

- **预测步**：使用显式公式预测下一步值
- **校正步**：使用隐式公式校正预测值

### 仿真模型详细程度

| 模型级别 | 发电机模型 | 励磁系统 | 调速系统 | 负荷模型 | 适用场景 |
|---------|-----------|---------|---------|---------|---------|
| 经典模型 | $E'$恒定 | 无 | 无 | 恒阻抗 | 初步筛选 |
| 二阶模型 | $E'$变化 | 简化的 | 简化的 | 动态负荷 | 快速计算 |
| 详细模型 | 6阶及以上 | 详细 | 详细 | 综合负荷 | 精确分析 |
| 全模型 | 详细+饱和 | 详细+PSS | 详细+阀门 | 详细 | 关键计算 |

### 仿真步骤

1. **初始化**：求解潮流，确定初始运行点
2. **故障设置**：施加故障，修改网络导纳矩阵
3. **故障期间仿真**：积分计算故障期间轨迹
4. **故障清除**：清除故障，更新网络参数
5. **故障后仿真**：继续积分至稳态或判明失稳
6. **稳定性判定**：根据转子角轨迹判断是否稳定

### 稳定判据

- **绝对角度判据**：任意两台机相对角度不超过180度
- **相对角度判据**：最大相对摆幅逐渐衰减
- **同步力矩判据**：系统在平衡点处恢复力矩为正


## 直接法 (Direct Methods)

直接法基于李雅普诺夫稳定性理论，通过计算系统的能量函数来判定稳定性，无需数值积分。

### 等面积法则 (Equal Area Criterion, EAC)

#### 基本原理

对于单机无穷大系统，稳定条件为加速面积等于减速面积：

$$
A_{acc} = A_{dec}
$$

其中：

$$
A_{acc} = \int_{\delta_0}^{\delta_c}(P_m - P_{e}^{fault})d\delta
$$

$$
A_{dec} = \int_{\delta_c}^{\delta_{max}}(P_{e}^{post} - P_m)d\delta
$$

#### 临界清除角 (CCA)

临界清除角满足：

$$
\int_{\delta_0}^{\delta_{cc}}(P_m - P_{e}^{fault})d\delta = \int_{\delta_{cc}}^{\delta_u}(P_{e}^{post} - P_m)d\delta
$$

#### 稳定裕度

$$
\eta = \frac{A_{dec} - A_{acc}}{A_{acc}} \times 100\%
$$

### 能量函数法 (Energy Function Method)

#### 能量函数构造

对于多机系统，构造暂态能量函数：

$$
V(\delta, \omega) = V_{ke}(\omega) + V_{pe}(\delta)
$$

动能项：

$$
V_{ke} = \frac{1}{2}\sum_{i=1}^{n}M_i(\omega_i - \omega_0)^2
$$

势能项（结构保留模型）：

$$
V_{pe} = -\sum_{i=1}^{n}P_i(\delta_i - \delta_i^s) - \sum_{i<j}C_{ij}(\cos\delta_{ij} - \cos\delta_{ij}^s)
$$

#### 主导不稳定平衡点 (Controlling UEP)

稳定性判定：

$$
V(x_0) < V_{cr} = V(x_{uep})
$$

其中 $x_{uep}$ 为与故障轨迹相关的主导不稳定平衡点。

#### 势能边界表面法 (PEBS)

PEBS方法沿故障轨迹监测势能变化：

$$
\frac{dV_{pe}}{\mathrm{d}t} = 0 \text{ 且 } \frac{d^2V_{pe}}{dt^2} > 0
$$

此时的 $V_{pe}$ 作为临界能量估计值。

### 扩展等面积准则 (Extended Equal Area Criterion, EEAC)

#### 基本原理

EEAC将多机系统映射为单机无穷大系统：

1. **机群识别**：识别临界机群 (Critical Cluster, CC) 和剩余机群 (Remaining Cluster, R)
2. **等效变换**：将两机群等效为OMIB系统
3. **等面积分析**：应用EAC分析等效OMIB系统

#### OMIB等效

等效角度：

$$
\delta_{OMIB} = \delta_{CC} - \delta_R
$$

其中：

$$
\delta_{CC} = \frac{\sum_{i \in CC}M_i\delta_i}{\sum_{i \in CC}M_i}, \quad
\delta_R = \frac{\sum_{i \in R}M_i\delta_i}{\sum_{i \in R}M_i}
$$

等效惯性：

$$
M_{OMIB} = \frac{M_{CC}M_R}{M_{CC} + M_R}
$$

#### 稳定裕度计算

$$
\eta_{OMIB} = \frac{A_{dec} - A_{acc}}{A_{acc}} \times 100\%
$$


## 混合方法 (Hybrid Methods)

### 单机等效法 (SIME)

SIME是一种时域仿真与直接法相结合的混合方法。

#### 算法流程

1. **时域仿真**：进行全系统时域仿真
2. **机群聚合**：根据转子角度曲线识别同调机群
3. **OMIB等效**：构建等效OMIB系统
4. **EAC分析**：应用等面积法则分析稳定性
5. **裕度计算**：计算稳定裕度和临界清除时间

#### 机群识别准则

根据转子角度轨迹的相似性进行聚类：

$$
|\delta_i(t) - \delta_j(t)| < \epsilon \quad \forall t \in [t_0, t_{end}]
$$

#### SIME的优势

- 保留时域仿真的模型精确性
- 获得直接法的稳定裕度指标
- 适用于复杂系统和详细模型
- 可在线应用

### 基于控制不稳定平衡点的边界法 (BCU Method)

BCU方法提供了一种系统性计算主导UEP的方法。

#### 基本步骤

1. **故障期间轨迹计算**：通过时域仿真计算故障轨迹
2. **最小梯度点识别**：在故障后系统中沿梯度方向搜索
3. **主导UEP计算**：从最小梯度点出发求解主导UEP
4. **稳定性判定**：比较故障清除点能量与临界能量

#### 梯度系统

故障后系统的梯度动力学：

$$
\dot{\delta} = -\frac{\partial V_{pe}}{\partial \delta}
$$

#### BCU-CLS方法

用于考虑励磁系统限制的稳定分析：
- 识别励磁系统饱和事件
- 分段计算能量函数
- 修正临界能量估计

### 混合方法比较

| 方法 | 计算精度 | 计算速度 | 适用规模 | 稳定裕度 | 在线应用 |
|-----|---------|---------|---------|---------|---------|
| SIME | 高 | 中等 | 大规模 | 有 | 适合 |
| BCU | 较高 | 较快 | 中大规模 | 有 | 可行 |
| PEBS | 中等 | 快 | 大规模 | 近似 | 适合 |
| 直接法 | 依赖模型 | 最快 | 中小规模 | 有 | 适合 |


## 稳定判据与指标

### 传统稳定判据

#### 转子角判据

$$
|\delta_i(t) - \delta_j(t)| < 180° \quad \forall i,j, \forall t > t_c
$$

工程实践中通常采用更严格的判据（如120度或150度）。

#### 角速度判据

$$
|\omega_i(t) - \omega_0| < \Delta\omega_{max} \quad \forall i, \forall t > t_c
$$

通常 $\Delta\omega_{max} = 2-5$ Hz。

### 稳定裕度指标

#### 1. 临界清除时间裕度

$$
\eta_{CCT} = \frac{CCT - ACT}{ACT} \times 100\%
$$

其中ACT为实际清除时间。

#### 2. 能量裕度

$$
\eta_E = \frac{V_{cr} - V_{cl}}{V_{cl}} \times 100\%
$$

其中 $V_{cl}$ 为故障清除时刻的能量。

#### 3. 功率裕度

$$
\eta_P = \frac{P_{max} - P_0}{P_0} \times 100\%
$$

#### 4. 电压稳定裕度

$$
\eta_V = \frac{V_{min} - V_{cr}}{V_{cr}} \times 100\%
$$

### 暂态稳定指数 (TSI)

综合稳定指标：

$$
TSI = w_1\eta_{CCT} + w_2\eta_E + w_3\eta_P + w_4\eta_V
$$

其中 $w_i$ 为权重系数。


## 临界清除时间计算 (CCT)

### 二分搜索法

最常用的CCT计算方法：

```
算法：CCT二分搜索
输入：初始猜测 t_low, t_high
输出：临界清除时间 CCT

while |t_high - t_low| > epsilon:
    t_mid = (t_low + t_high) / 2
    仿真并判定稳定性
    if 稳定:
        t_low = t_mid
    else:
        t_high = t_mid
return (t_low + t_high) / 2
```

### 灵敏度法

基于稳定裕度对清除时间的灵敏度：

$$
CCT \approx t_{clear} + \frac{\eta(t_{clear})}{\partial \eta / \partial t}
$$

### 基于直接法的CCT估计

利用能量函数计算：

$$
CCT = t|_{V(t) = V_{cr}}
$$

通过插值确定临界能量对应的清除时间。

### 实际清除时间要求

| 电压等级 | 近端故障CCT要求 | 远端故障CCT要求 |
|---------|----------------|----------------|
| 500kV | >150ms | >250ms |
| 220kV | >120ms | >200ms |
| 110kV | >100ms | >180ms |


## 灵敏度分析

### 轨迹灵敏度

状态变量对参数的灵敏度：

$$
s_x = \frac{\partial x(t)}{\partial p}
$$

满足灵敏度方程：

$$
\dot{s}_x = \frac{\partial f}{\partial x}s_x + \frac{\partial f}{\partial p}
$$

### 稳定裕度灵敏度

#### CCT对机组惯性的灵敏度

$$
\frac{\partial CCT}{\partial H_i} = \lim_{\Delta H_i \to 0}\frac{CCT(H_i + \Delta H_i) - CCT(H_i)}{\Delta H_i}
$$

#### CCT对传输功率的灵敏度

$$
\frac{\partial CCT}{\partial P_{flow}} = \frac{CCT(P_0 + \Delta P) - CCT(P_0)}{\Delta P}
$$

### 参与因子

发电机对稳定裕度的参与程度：

$$
PF_i = \frac{\partial \eta / \partial H_i}{\sum_j |\partial \eta / \partial H_j|}
$$

### 灵敏度应用

- **关键机组识别**：识别对稳定性影响最大的机组
- **控制策略优化**：指导预防控制和紧急控制
- **规划决策支持**：指导网络扩展和机组配置
- **参数整定**：优化保护和安全自动装置定值


## 预防控制与紧急控制

### 预防控制

在扰动发生前采取措施提高系统稳定性。

#### 发电再调度

优化发电计划以提高稳定裕度：

$$
\min \sum_i C_i(P_{Gi}) \quad \text{s.t.} \quad \eta_{CCT} \geq \eta_{min}
$$

#### 无功补偿优化

调整无功出力，改善电压支撑：

$$
\max \eta_V \quad \text{s.t.} \quad Q_{min} \leq Q_{shunt} \leq Q_{max}
$$

#### 拓扑优化

通过开关操作改变网络结构：
- 并联线路投切
- 母线分段/并联
- 变压器分接头调整

### 紧急控制

在扰动发生后采取措施防止系统失稳。

#### 切机控制 (Generation Shedding)

切除部分发电机以降低加速面积：

$$
\Delta P_{shed} = k(P_{acc} - P_{dec})
$$

控制策略：
- **本地判据**：本地频率、电压、功率变化率
- **广域判据**：WAMS测量的转子角差

#### 切负荷控制 (Load Shedding)

切除部分负荷以平衡功率：

$$
\Delta P_{load} = \sum_{i \in \Omega} w_i P_{Li}
$$

优先级：
1. 可中断负荷
2. 工业负荷
3. 商业负荷
4. 居民负荷（最后手段）

#### 电气制动 (Dynamic Braking)

投入电阻负荷消耗过剩功率：

$$
P_{brake} = \frac{V^2}{R_{brake}}
$$

#### 直流功率调制

利用HVDC快速功率控制：

$$
\Delta P_{dc} = K_{dc}(\Delta f_{ac} + k_d \frac{\mathrm{d}\Delta f_{ac}}{\mathrm{d}t})
$$

### 控制决策时间要求

| 控制类型 | 决策时间要求 | 动作时间 | 控制手段 |
|---------|------------|---------|---------|
| 预防控制 | 分钟级 | 调度周期 | 发电再调度 |
| 暂态控制 | 100-200ms | 切机、直流调制 |
| 紧急控制 | 200-500ms | 切负荷、解列 |


## 工具与软件

### 商业软件

| 软件名称 | 开发商 | 特点 | 应用范围 |
|---------|-------|------|---------|
| PSS/E | Siemens | 全面的稳定分析功能 | 输电系统规划运行 |
| PowerFactory | DIgSILENT | 详细建模能力 | 输配电系统分析 |
| ETAP | ETAP | 集成化分析平台 | 工业电力系统 |
| CYME | Eaton | 配电网分析 | 配电网稳定分析 |
| DSATools | Powertech | 小信号和暂态分析 | 北美广泛应用 |

### 开源软件

| 软件名称 | 特点 | 许可证 |
|---------|------|-------|
| PSAT | MATLAB平台，教育友好 | GPL |
| Power System Toolbox | Python工具包 | BSD |
| GridCal | 现代Python架构 | LGPL |
| Matpower | 优化和潮流计算 | BSD |
| Dome | Python动力学仿真 | MIT |

### 在线分析系统

- **WAMS-based DSA**：基于广域量测的在线动态安全评估
- **EMS/DMS集成**：与能量管理系统集成的稳定分析
- **云端分析平台**：基于云计算的大规模并行稳定计算


## 相关方法

- [[swing-equation]] - 摇摆方程：描述转子动态的基本方程
- [[equal-area-criterion]] - 等面积法则：单机系统直接稳定分析
- [[energy-function]] - 能量函数法：基于李雅普诺夫理论的直接法
- [[time-domain-simulation]] - 时域仿真：数值积分求解系统轨迹
- [[eeac]] - 扩展等面积准则：多机系统的等效OMIB方法
- `sime` - 单机等效法：时域仿真与直接法结合的混合方法
- `bcu` - BCU方法：基于控制UEP的稳定边界计算
- [[sensitivity-analysis]] - 灵敏度分析：参数对稳定性的影响
- `direct-methods` - 直接法：基于李雅普诺夫理论的稳定分析
- [[numerical-integration]] - 数值积分：时域仿真计算方法
- `critical-clearing-time` - 临界清除时间：稳定判据关键参数


## 相关主题

- [[transient-stability]] - 暂态稳定性：大扰动下的稳定性问题
- [[small-signal-stability]] - 小信号稳定性：小扰动下的振荡稳定性
- `voltage-stability` - 电压稳定性：电压崩溃问题
- `frequency-stability` - 频率稳定性：系统频率控制
- `dynamic-security-assessment` - 动态安全评估：在线稳定评估
- `power-system-protection` - 继电保护：故障检测和隔离
- `emergency-control` - 紧急控制：失稳后的控制措施
- `preventive-control` - 预防控制：提高稳定裕度的调度
- `coherency-identification` - 同调机群识别：机群聚合基础
- [[wide-area-monitoring-protection]] - 广域监测：WAMS在稳定分析中的应用
- [[real-time-simulation]] - 实时仿真：硬件在环稳定测试


## 相关模型

- [[synchronous-machine-model]] - 同步电机模型：发电机动态模型
- [[excitation-system]] - 励磁系统模型：电压调节动态
- `governor-model` - 调速器模型：原动机和调速控制
- [[pss-model]] - PSS模型：电力系统稳定器
- [[load-model]] - 负荷模型：负荷动态特性
- [[transmission-line-model]] - 输电线路模型：线路暂态特性
- [[transformer-model]] - 变压器模型：变压器饱和特性
- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] - HVDC模型：直流系统控制模型


## 理论基础

### 李雅普诺夫稳定性理论

**李雅普诺夫第一方法**：通过线性化系统的特征值判断稳定性。

**李雅普诺夫第二方法**：构造能量函数 $V(x)$ 满足：
1. $V(x) > 0$ for $x \neq 0$
2. $V(0) = 0$
3. $\dot{V}(x) < 0$ along trajectories

### 结构保留模型

保留网络结构的能量函数构造：

$$
V(x) = \frac{1}{2}\omega^T M \omega + V_{pe}(\delta, \theta, V)
$$

其中 $\theta$ 和 $V$ 为负荷母线相角和电压。


## 研究前沿

### 数据驱动的稳定分析

- **机器学习**：利用神经网络预测稳定性
- **模式识别**：从历史数据识别稳定/失稳模式
- **深度强化学习**：智能紧急控制决策

### 不确定性分析

- **概率稳定评估**：考虑风电、光伏不确定性
- **区间分析**：参数不确定性影响
- **鲁棒稳定控制**：应对多重不确定场景

### 大规模系统分析

- **并行计算**：GPU加速时域仿真
- **分解协调**：大规模系统分区计算
- **模型降阶**：保持关键动态的简化模型

---

## 来源论文

| 论文 | 年份 |
|------|------|
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient|Comparison and Selection of Grid-Tied Inverter Models for Ac]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl|Electromechanical transient-electromagnetic transient hybrid]] | 2022 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
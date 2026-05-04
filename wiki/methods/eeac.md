---
title: "EEAC (Extended Equal Area Criterion)"
type: method
tags: [eeac, equal-area, transient-stability, direct-method, single-machine-equivalent]
created: "2026-05-02"
---

# 扩展等面积准则 (EEAC)

## 概述

扩展等面积准则(Extended Equal Area Criterion, EEAC)是电力系统暂态稳定性分析的直接法，由薛禹胜院士于1988年提出。该方法将多机系统等效为单机无穷大系统(SMIB)，应用等面积法则快速评估暂态稳定性，可定量计算稳定裕度和临界切除时间。

EEAC的核心创新在于将复杂的多机系统暂态稳定问题转化为等效的双机系统问题，进而简化为单机无穷大系统问题，从而可以应用经典的等面积法则进行快速稳定性评估。该方法既保留了直接法计算速度快的优势，又克服了传统直接法难以处理多机系统的局限性。

## 理论基础

### 李雅普诺夫稳定性理论

EEAC的理论基础建立在李雅普诺夫直接法之上。对于电力系统这样的非线性动态系统，李雅普诺夫稳定性理论提供了判断系统稳定性的有效工具。

**李雅普诺夫函数定义**：
设 $V(x)$ 是定义在状态空间原点邻域内的标量函数，若满足：
1. $V(0) = 0$
2. $V(x) > 0$ 对所有 $x \neq 0$ 成立
3. $\dot{V}(x) \leq 0$ 对所有 $x \neq 0$ 成立

则系统在原点是稳定的。对于电力系统，能量函数可以作为李雅普诺夫函数。

**稳定性区域估计**：
EEAC利用李雅普诺夫函数的水平集来估计稳定性区域：
$$\Omega_c = \{x | V(x) < V_{cr}\}$$

其中 $V_{cr}$ 是临界能量值，对应于不稳定平衡点(UEP)处的能量值。

### 能量函数理论

电力系统的能量函数可以分解为动能和势能两部分：

$$V(\delta, \omega) = V_{ke}(\omega) + V_{pe}(\delta)$$

**动能部分**：
$$V_{ke} = \frac{1}{2} \sum_{i=1}^{n} M_i \omega_i^2$$

**势能部分**：
$$V_{pe} = -\sum_{i=1}^{n} P_{mi}(\delta_i - \delta_i^s) - \sum_{i=1}^{n-1}\sum_{j=i+1}^{n} E_i E_j B_{ij}[\cos(\delta_{ij}) - \cos(\delta_{ij}^s)]$$

其中：
- $M_i$: 第 $i$ 台机组的惯性时间常数
- $\omega_i$: 第 $i$ 台机组的角速度偏差
- $\delta_i$: 第 $i$ 台机组的功角
- $\delta_i^s$: 第 $i$ 台机组的稳定平衡点功角
- $E_i$: 第 $i$ 台机组的内电势幅值
- $B_{ij}$: 节点导纳矩阵的虚部

### 暂态能量转换

在故障期间和故障清除后，系统的暂态能量发生转换：

**故障期间能量积累**：
$$\Delta V_{fault} = \int_{t_0}^{t_c} \sum_{i=1}^{n} (P_{mi} - P_{ei}^{fault}) \omega_i dt$$

**故障清除后能量耗散**：
$$\Delta V_{post} = \int_{t_c}^{t_{max}} \sum_{i=1}^{n} (P_{ei}^{post} - P_{mi}) \omega_i dt$$

稳定条件为故障期间积累的能量能够被故障清除后耗散：
$$\Delta V_{fault} < \Delta V_{post,max}$$

## 多机等效原理

### 双机等效模型

EEAC的核心是将 $n$ 机系统动态等值为双机系统，进一步简化为单机无穷大系统。

**机组分群**：
将系统中的机组划分为两个互补的集合：
- **临界群(Critical Machines, C)**：功角趋于领先的机组群，失稳时功角会单调增大
- **非临界群(Non-critical Machines, N)**：功角趋于落后的机组群，相对保持稳定

$$C = \{i | \delta_i \text{ 趋于增大}\}$$
$$N = \{j | \delta_j \text{ 趋于稳定或减小}\}$$

**等效功角计算**：
利用惯性中心(Center of Inertia, COI)概念，将各群内的机组等效为一台等值机：

$$\delta_C = \frac{\sum_{i \in C} M_i \delta_i}{\sum_{i \in C} M_i}$$

$$\delta_N = \frac{\sum_{j \in N} M_j \delta_j}{\sum_{j \in N} M_j}$$

**等效角速度**：
$$\omega_C = \frac{\sum_{i \in C} M_i \omega_i}{\sum_{i \in C} M_i}$$

$$\omega_N = \frac{\sum_{j \in N} M_j \omega_j}{\sum_{j \in N} M_j}$$

**等效惯性常数**：
$$M_C = \sum_{i \in C} M_i$$

$$M_N = \sum_{j \in N} M_j$$

### OMIB等效

将双机系统等效为单机无穷大系统(One-Machine Infinite Bus, OMIB)：

**等效功角**：
$$\delta_{eq} = \delta_C - \delta_N$$

**等效角速度**：
$$\omega_{eq} = \omega_C - \omega_N = \frac{d\delta_{eq}}{dt}$$

**等效惯性常数**：
$$M_{eq} = \frac{M_C M_N}{M_C + M_N}$$

这个等效惯性常数是两个惯性常数的并联等效值，反映了两个机组群之间的相对运动特性。

**等效电磁功率**：

故障前功率：
$$P_e^{pre} = P_{C}^{pre} - P_{N}^{pre}$$

故障期间功率：
$$P_e^{fault} = P_{C}^{fault} - P_{N}^{fault}$$

故障清除后功率：
$$P_e^{post} = P_{C}^{post} - P_{N}^{post}$$

其中各群的功率为：
$$P_{C} = \sum_{i \in C} P_{ei}, \quad P_{N} = \sum_{j \in N} P_{ej}$$

**等效机械功率**：
$$P_m = \frac{M_N P_{mC} - M_C P_{mN}}{M_C + M_N}$$

其中：
$$P_{mC} = \sum_{i \in C} P_{mi}, \quad P_{mN} = \sum_{j \in N} P_{mj}$$

### 等效参数物理意义

OMIB等效将多机系统的复杂相对运动简化为单一的自由度：

1. **等效功角** $\delta_{eq}$：反映临界群相对于非临界群的领先程度
2. **等效角速度** $\omega_{eq}$：反映两群之间的相对滑动速度
3. **等效惯性** $M_{eq}$：决定系统响应的惯性特性
4. **等效功率**：决定系统的加速和减速特性

## 等面积法则的完整推导

### 系统运动方程

OMIB系统的摇摆方程为：

$$M_{eq} \frac{d^2\delta_{eq}}{dt^2} = P_m - P_e(\delta_{eq})$$

两边同乘以 $\frac{d\delta_{eq}}{dt} = \omega_{eq}$：

$$M_{eq} \omega_{eq} \frac{d\omega_{eq}}{dt} = [P_m - P_e(\delta_{eq})] \frac{d\delta_{eq}}{dt}$$

积分得：

$$\frac{1}{2} M_{eq} \omega_{eq}^2 - \frac{1}{2} M_{eq} \omega_{eq,0}^2 = \int_{\delta_{eq,0}}^{\delta_{eq}} [P_m - P_e(\delta)] d\delta$$

### 加速面积

**定义**：故障期间过剩功率对功角的积分

$$A_{acc} = \int_{\delta_0}^{\delta_c} (P_m - P_e^{fault}) d\delta$$

其中：
- $\delta_0$：故障前初始功角（稳定平衡点）
- $\delta_c$：故障清除时刻功角
- $P_m$：等效机械功率（恒定）
- $P_e^{fault}$：故障期间等效电磁功率

**物理意义**：
加速面积代表故障期间转子积累的动能增量。当 $P_m > P_e^{fault}$ 时，$A_{acc} > 0$，表示转子加速并获得动能。

**计算方法**：
对于经典模型，电磁功率可以表示为：
$$P_e^{fault} = P_{max}^{fault} \sin(\delta - \gamma^{fault}) + P_0^{fault}$$

因此加速面积为：
$$A_{acc} = P_m(\delta_c - \delta_0) - P_{max}^{fault}[\cos(\delta_0 - \gamma^{fault}) - \cos(\delta_c - \gamma^{fault})] - P_0^{fault}(\delta_c - \delta_0)$$

### 减速面积

**定义**：故障清除后恢复功率对功角的积分

$$A_{dec} = \int_{\delta_c}^{\delta_u} (P_e^{post} - P_m) d\delta$$

其中：
- $\delta_u$：最大摇摆角（对应 $\omega_{eq} = 0$）
- $P_e^{post}$：故障清除后等效电磁功率

**物理意义**：
减速面积代表故障清除后系统能够耗散的最大动能。当 $P_e^{post} > P_m$ 时，系统可以减速并恢复稳定。

**最大减速面积**：
系统稳定的极限情况是 $\delta_u$ 达到不稳定平衡点 $\delta_{uep}$：

$$A_{dec,max} = \int_{\delta_c}^{\delta_{uep}} (P_e^{post} - P_m) d\delta$$

### 稳定裕度

**稳定性判据**：
根据能量守恒原理，系统稳定的条件是：
$$A_{dec} \geq A_{acc}$$

**稳定裕度定义**：
$$\eta = \frac{A_{dec} - A_{acc}}{A_{acc}} \times 100\%$$

或采用归一化形式：
$$\eta = \frac{A_{dec} - A_{acc}}{A_{dec,max}} \times 100\%$$

**裕度解释**：
- $\eta > 0$（或 $\eta > 0\%$）：系统稳定，裕度为正
- $\eta < 0$（或 $\eta < 0\%$）：系统不稳定，裕度为负
- $\eta = 0$：临界状态，处于稳定边界

**裕度物理意义**：
稳定裕度定量表征了系统距离不稳定边界的远近程度。裕度越大，系统越稳定；裕度越小，系统越接近失稳。

### 稳定边界确定

不稳定平衡点(UEP)的确定是等面积法则应用的关键。

**求解方法**：
$$P_m - P_e^{post}(\delta_{uep}) = 0$$

$$P_{max}^{post} \sin(\delta_{uep} - \gamma^{post}) + P_0^{post} = P_m$$

解得：
$$\delta_{uep} = \arcsin\left(\frac{P_m - P_0^{post}}{P_{max}^{post}}\right) + \gamma^{post}$$

在多摆情况下，可能存在多个不稳定平衡点，需要选择控制不稳定平衡点(CUEP)。

## 临界切除时间计算

### 临界切除角

临界切除角 $\delta_{cr}$ 是使系统刚好达到稳定边界的故障清除角。

**计算公式**：
由等面积法则：
$$A_{acc}(\delta_{cr}) = A_{dec,max}(\delta_{cr})$$

$$\int_{\delta_0}^{\delta_{cr}} (P_m - P_e^{fault}) d\delta = \int_{\delta_{cr}}^{\delta_{uep}} (P_e^{post} - P_m) d\delta$$

对于经典二阶模型，可解析求解：

$$P_m(\delta_{cr} - \delta_0) - P_{max}^{fault}[\cos(\delta_0 - \gamma^{fault}) - \cos(\delta_{cr} - \gamma^{fault})]$$
$$= P_{max}^{post}[\cos(\delta_{cr} - \gamma^{post}) - \cos(\delta_{uep} - \gamma^{post})] - P_m(\delta_{uep} - \delta_{cr})$$

这是一个关于 $\delta_{cr}$ 的超越方程，通常采用数值方法求解。

### 临界切除时间

**计算方法**：
通过求解摇摆方程获得功角随时间变化的轨迹 $\delta(t)$，然后找到满足 $\delta(t_{cr}) = \delta_{cr}$ 的时间 $t_{cr}$。

**简化计算**：
对于小幅扰动，可采用线性近似：
$$t_{cr} = \sqrt{\frac{2M_{eq}(\delta_{cr} - \delta_0)}{P_m - P_e^{fault}(\delta_0)}}$$

**精确计算**：
采用数值积分求解：
$$t_{cr} = \int_{\delta_0}^{\delta_{cr}} \frac{d\delta}{\omega(\delta)}$$

其中 $\omega(\delta)$ 由能量守恒确定：
$$\omega(\delta) = \sqrt{\frac{2}{M_{eq}} \int_{\delta_0}^{\delta} (P_m - P_e^{fault}) d\delta'}$$

### 灵敏度分析

**裕度对切除时间的灵敏度**：
$$\frac{\partial \eta}{\partial t_c} = \frac{\partial \eta}{\partial \delta_c} \cdot \frac{d\delta_c}{dt_c}$$

这个灵敏度可用于指导继电保护的整定。

## 临界群识别算法

### 轨迹特征分析

**功角轨迹特征**：
故障后各机组的功角轨迹 $\delta_i(t)$ 呈现不同的动态特性：

1. **临界机组特征**：
   - 功角快速单调增大
   - 角速度保持正值并持续增加
   - 加速度在故障期间为正

2. **非临界机组特征**：
   - 功角摆动或缓慢变化
   - 角速度在零附近振荡
   - 加速度正负交替

**识别指标**：

**角速度指标**：
$$\omega_i(t_c) = \frac{d\delta_i}{dt}\bigg|_{t=t_c}$$

**加速度指标**：
$$\alpha_i = \frac{d^2\delta_i}{dt^2}\bigg|_{t=0^+} = \frac{P_{mi} - P_{ei}(0^+)}{M_i}$$

**功角分离度**：
$$\Delta\delta_i(t) = \delta_i(t) - \delta_{COI}(t)$$

其中惯性中心功角：
$$\delta_{COI} = \frac{\sum_{k=1}^{n} M_k \delta_k}{\sum_{k=1}^{n} M_k}$$

### 聚类方法

**K-means聚类**：
基于故障切除时刻的功角-角速度状态进行聚类：

$$\min \sum_{k=1}^{2} \sum_{i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|^2$$

其中特征向量：
$$\mathbf{x}_i = [\delta_i(t_c), \omega_i(t_c), \alpha_i]^T$$

**层次聚类**：
采用自底向上的凝聚式聚类：
1. 初始状态：每台机组作为一个独立类
2. 计算类间距离：欧氏距离或马氏距离
3. 合并最近的两类
4. 重复直到只剩两类

**动态聚类**：
考虑时变特性的动态聚类：
$$d_{ij}(t) = \sqrt{[\delta_i(t) - \delta_j(t)]^2 + [\omega_i(t) - \omega_j(t)]^2}$$

### 模式识别

**失稳模式分类**：

1. **一摆失稳(First-swing Instability)**：
   - 首摆期间功角失稳
   - 最大功角小于 $360°$
   - EEAC精度最高

2. **多摆失稳(Multi-swing Instability)**：
   - 后续摇摆期间失稳
   - 首次摇摆看似稳定
   - 需要时域仿真配合

3. **复杂失稳模式**：
   - 多个临界机组群
   - 非单调失稳特性
   - 需要多群EEAC扩展

**主导失稳模式识别**：
通过灵敏度分析确定主导失稳模式：
$$S_i = \frac{\partial \eta}{\partial P_{mi}}$$

灵敏度最大的机组构成主导失稳模式。

### 临界群验证

**轨迹一致性验证**：
计算假设临界群的轨迹一致性指标：
$$R_{CN} = \frac{\max_{i \in C} \delta_i - \min_{i \in C} \delta_i}{\max_{j \in N} \delta_j - \min_{j \in N} \delta_j}$$

$R_{CN} \ll 1$ 表示群内一致性好，群间分离明显。

**裕度收敛性验证**：
不同时刻计算的稳定裕度应满足：
$$\eta(t_1) \approx \eta(t_2), \quad \forall t_1, t_2 > t_c$$

若裕度收敛，说明临界群识别正确。

## 时变EEAC与渐进EEAC

### 时变等效参数

传统EEAC使用恒定等效参数，时变EEAC考虑参数随时间变化：

**时变等效功角**：
$$\delta_{eq}(t) = \delta_C(t) - \delta_N(t)$$

**时变等效惯性**：
由于机组可能分群变化，等效惯性可能时变：
$$M_{eq}(t) = \frac{M_C(t) M_N(t)}{M_C(t) + M_N(t)}$$

**时变功率曲线**：
考虑网络拓扑变化的功率曲线：
$$P_e^{post}(\delta, t) = \sum_{i \in C}\sum_{j \in N} E_i E_j B_{ij}(t) \sin(\delta_{ij})$$

### 渐进EEAC

渐进EEAC沿时域轨迹逐步计算稳定裕度：

**算法流程**：
1. 在 $t_c$ 时刻识别临界群
2. 计算等效参数
3. 计算当前裕度 $\eta(t_c)$
4. 沿轨迹前进 $\Delta t$
5. 在 $t_c + \Delta t$ 更新临界群和等效参数
6. 重新计算裕度
7. 直到裕度收敛或失稳

**收敛判据**：
$$|\eta(t_k) - \eta(t_{k-1})| < \varepsilon$$

**优势**：
- 适应临界群变化
- 处理多摆失稳
- 提高复杂情况精度

### 混合方法

**时域-EEAC混合**：
结合时域仿真和EEAC分析：

1. **时域仿真阶段**：
   - 进行短时域仿真
   - 获取功角轨迹
   - 识别临界群

2. **EEAC分析阶段**：
   - 基于轨迹计算等效参数
   - 应用等面积法则
   - 计算稳定裕度

3. **迭代精化**：
   - 根据裕度调整仿真时间
   - 重新识别临界群
   - 直到结果收敛

**互补优势**：
- 时域仿真提供完整动态行为
- EEAC提供量化裕度和灵敏度
- 兼顾计算速度和结果精度

## 与其他直接法的对比

### PEBS法

**势能边界表面法(Potential Energy Boundary Surface)**：

| 特性 | EEAC | PEBS |
|------|------|------|
| 理论基础 | 等面积法则 | 李雅普诺夫稳定性 |
| 系统处理 | 多机等效 | 全系统分析 |
| 稳定性判据 | 面积比较 | 能量比较 |
| 裕度定义 | 面积裕度 | 能量裕度 |
| 计算速度 | 极快 | 快 |
| 精度 | 一摆高精 | 可处理多摆 |

**关系**：
EEAC可以视为PEBS法的特例，两者在数学上是等价的。EEAC提供的面积裕度与PEBS的能量裕度通过等效转换相关联。

### BCU法

**边界控制不稳定平衡点法(Boundary of stability region based Controlling Unstable Equilibrium Point)**：

| 特性 | EEAC | BCU |
|------|------|-----|
| UEP确定 | 等效系统CUEP | 降维系统CUEP |
| 计算复杂度 | 低 | 中等 |
| 可靠性 | 一摆可靠 | 较高 |
| 保守性 | 可能乐观 | 保守 |

**BCU优势**：
- 系统性降维方法
- 严格的稳定性边界估计
- 适用于复杂失稳模式

**EEAC优势**：
- 计算更简单快速
- 物理概念清晰
- 工程应用广泛

### SIME法

**单机等效法(SIngle Machine Equivalent)**：

SIME与EEAC在本质上是相同的，都是将多机系统等效为OMIB。两者的主要区别：

| 特性 | EEAC | SIME |
|------|------|------|
| 起源 | 中国电科院(1988) | 意大利(1997) |
| 等效方法 | 惯性中心 | 混合方法 |
| 临界群识别 | 基于轨迹 | 基于预测 |
| 应用侧重 | 在线评估 | 离线分析 |

**共同特点**：
- 都采用OMIB等效
- 都应用等面积法则
- 都提供定量裕度

**差异**：
- 临界群识别策略不同
- 等效参数计算略有差异
- 应用场景侧重不同

### 综合对比

| 方法 | 速度 | 精度 | 裕度 | 适用场景 |
|------|------|------|------|----------|
| 时域仿真 | 慢 | 最高 | 无 | 离线详细分析 |
| EEAC | 极快 | 高(一摆) | 有 | 在线评估 |
| SIME | 极快 | 高(一摆) | 有 | 在线评估 |
| PEBS | 快 | 高 | 有 | 离线分析 |
| BCU | 中等 | 较高 | 有 | 复杂模式 |

## 在线安全评估应用

### 快速筛选

EEAC的核心应用是大量故障场景的快速筛选：

**应用场景**：
- N-1故障扫描
- N-2故障扫描
- 多重故障分析

**计算流程**：
1. 对每个故障场景进行潮流计算
2. 识别临界群
3. 计算OMIB等效参数
4. 应用等面积法则计算裕度
5. 按裕度排序故障场景

**筛选效率**：
相比时域仿真，EEAC可将计算速度提高2-3个数量级。

### 稳定裕度排序

**裕度指标体系**：
- 电压裕度：$\eta_V$
- 功角裕度：$\eta_\delta$
- 综合裕度：$\eta = \min(\eta_V, \eta_\delta)$

**排序算法**：
按裕度从小到大排序，裕度最小的场景即为最危险的故障。

**结果应用**：
- 确定关注集(COI, Contingency of Interest)
- 指导保护整定
- 优化运行方式

### 实时稳定性监测

**广域测量系统(WAMS)集成**：
EEAC可与WAMS结合实现实时稳定性评估：

1. **数据获取**：PMU实时测量功角、频率
2. **状态估计**：滤波和状态估计
3. **临界群识别**：基于实时数据识别
4. **裕度计算**：在线计算稳定裕度
5. **预警发布**：裕度低于阈值时发出预警

**计算周期**：
- 数据刷新：20-100ms
- 裕度计算：< 1s
- 预警响应：< 5s

## 预防控制和紧急控制应用

### 灵敏度分析

**裕度对控制量的灵敏度**：

**机械功率灵敏度**：
$$S_{Pi} = \frac{\partial \eta}{\partial P_{mi}}$$

**励磁电压灵敏度**：
$$S_{Ei} = \frac{\partial \eta}{\partial E_i}$$

**网络参数灵敏度**：
$$S_{Bij} = \frac{\partial \eta}{\partial B_{ij}}$$

**灵敏度计算方法**：
利用EEAC的解析特性，可以直接解析计算灵敏度，无需差分近似。

### 预防控制优化

**控制目标**：
在最小的控制代价下，使所有故障场景的裕度满足：
$$\eta_k \geq \eta_{min}, \quad \forall k \in \text{故障集}$$

**优化模型**：
$$\min \sum_{i} c_i \Delta P_i$$

约束：
$$\eta_k^{(0)} + \sum_{i} S_{ki} \Delta P_i \geq \eta_{min}, \quad \forall k$$
$$\Delta P_i^{min} \leq \Delta P_i \leq \Delta P_i^{max}$$

**求解方法**：
- 线性规划(LP)
- 二次规划(QP)
- 内点法

**控制手段**：
- 发电机出力调整
- 负荷转移
- 无功补偿投切
- 变压器分接头调整

### 紧急控制策略

**实时决策**：
当故障发生且裕度评估显示系统处于不稳定边缘时，需要快速决策。

**紧急切机**：
根据灵敏度选择最有效的机组切除：
$$\max \frac{\partial \eta}{\partial P_{m,i}}$$

**紧急切负荷**：
根据负荷对裕度的影响选择切除负荷点。

**控制量计算**：
所需控制量由裕度缺口确定：
$$\Delta P_{control} = \frac{|\eta|}{S} \times P_{base}$$

**策略优化**：
考虑控制代价和控制效果的多目标优化：
$$\min (w_1 \cdot \text{控制代价} + w_2 \cdot \text{控制量})$$

**执行时序**：
1. 故障检测(20-100ms)
2. 裕度评估(200-500ms)
3. 策略计算(100-300ms)
4. 控制执行(根据通道延时)

### 安全稳定控制系统

EEAC已应用于实际的安稳控制系统：

**分层控制架构**：
- 就地层：快速保护动作
- 站控层：本地安稳控制
- 区域层：协调控制
- 全网层：优化决策

**控制策略表**：
基于EEAC离线计算生成控制策略表，在线匹配执行。

## 软件实现与工程应用

### 主要软件实现

**中国电科院电力系统分析软件**：
- PSASP：电力系统分析综合程序
- 集成EEAC模块用于暂态稳定分析
- 在线稳定分析系统

**BCTC在线稳定分析系统**：
- 基于EEAC的实时稳定评估
- 预防控制和紧急控制决策支持
- 应用于多个省级电网

**RTDS实时数字仿真器**：
- EEAC算法集成
- 硬件在环测试
- 保护与控制策略验证

**其他商业软件**：
- PSS/E：通过外部接口调用
- PowerFactory：用户自定义模块
- MATLAB/Simulink：自定义实现

### 工程应用案例

**三峡电力系统稳定分析**：
- 世界上最大的水电站
- 采用EEAC进行大量故障扫描
- 制定安稳控制策略

**特高压交直流混联电网**：
- 华东、华北特高压电网
- 直流闭锁故障的快速评估
- 多直流协调控制

**新能源并网稳定分析**：
- 风电场、光伏电站大规模并网
- 低惯量系统的稳定特性
- EEAC适应性改进

**省级电网在线评估**：
- 江苏、浙江、广东等电网
- 实时稳定裕度监测
- 辅助调度决策

### 应用效果

**计算效率**：
- 相比时域仿真加速100-1000倍
- 支持万级故障场景扫描
- 实时评估响应时间< 1s

**计算精度**：
- 一摆失稳识别率> 95%
- 裕度误差< 10%
- 临界切除时间误差< 50ms

**工程价值**：
- 提高电网安全运行水平
- 优化运行方式
- 减少不必要的控制措施
- 提高输电能力

## 发展与展望

### 方法扩展

**多群EEAC**：
扩展EEAC处理多群失稳模式，将系统分为多个机组群进行分析。

**考虑负荷特性**：
引入动态负荷模型，提高复杂负荷情况下的分析精度。

**考虑HVDC和FACTS**：
将直流输电和柔性交流输电系统纳入EEAC框架。

### 与人工智能结合

**机器学习辅助**：
- 神经网络预测临界群
- 深度学习提取特征
- 强化学习优化控制

**混合智能系统**：
EEAC提供物理基础，AI提供学习能力，形成混合智能系统。

### 未来发展方向

**新型电力系统适应性**：
- 高比例新能源接入
- 电力电子化系统
- 分布式能源协调

**实时性提升**：
- 并行计算
- 硬件加速
- 边缘计算

**标准化推广**：
- 国际标准制定
- 行业规范推广
- 教育培训

## 相关方法

- [[equal-area-criterion]] - 等面积法则
- [[energy-function]] - 能量函数法
- [[transient-stability]] - 暂态稳定性
- `sime` - 单机等效法
- `pebs` - 势能边界表面法
- `bcu` - 边界控制不稳定平衡点法
- `online-security-assessment` - 在线安全评估
- `preventive-control` - 预防控制
- `emergency-control` - 紧急控制
- `critical-machine` - 临界机组识别
- `lyapunov-stability` - 李雅普诺夫稳定性理论

## 参考标准与规范

- IEEE Std 1204-1997: IEEE Guide for Planning DC Links Terminating at AC Locations
- DL/T 1764-2017: 电力系统安全稳定导则
- GB/T 26399-2011: 电力系统安全稳定控制技术导则

## 来源论文

参见 [[index]] 获取更多EEAC相关文献，包括薛禹胜院士1988年原创论文及后续系列研究论文。

---

*注：本页面基于薛禹胜院士提出的EEAC理论编写，该方法是中国电力系统分析领域具有自主知识产权的重要成果。*

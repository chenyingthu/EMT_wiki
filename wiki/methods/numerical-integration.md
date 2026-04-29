---
title: "数值积分"
type: method
tags: [numerical-integration, emt, trapezoidal, dirk, implicit-integration, stability]
created: "2026-04-13"
---

# 数值积分

## 概述

数值积分（Numerical Integration）是EMT仿真中将连续时间微分代数方程（DAE）离散为逐时步代数方程的核心方法。电感、电容、线路、变流器控制和等效网络都需要通过积分公式生成伴随电路、状态更新式或节点注入历史项。

在EMTP类求解器中，数值积分与[[nodal-analysis|节点分析法]]、[[state-space-method|状态空间法]]、开关事件处理以及设备等效模型共同决定仿真精度、数值阻尼和计算成本。不同积分方法（梯形法、后向欧拉法、DIRK、紧凑格式等）面向不同的稳定性与效率需求。

## 核心原理

### 动态元件离散化

典型EMT离散化将动态元件写成等效导纳加历史源形式：

$$
i(t_k) = G_{\mathrm{eq}} v(t_k) + I_{\mathrm{hist}}(t_{k-1})
$$

其中 $G_{\mathrm{eq}}$ 由积分公式、元件参数和步长决定，历史源汇总上一时刻的电压、电流或状态变量。

### 常用积分方法对比

| 方法 | 公式 | 精度阶数 | 稳定性 | 阻尼特性 |
|------|------|---------|--------|---------|
| **前向欧拉 (FE)** | $x_{n+1} = x_n + h f(t_n, x_n)$ | 1阶 | 条件稳定 | 无 |
| **后向欧拉 (BE)** | $x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})$ | 1阶 | A稳定 | 强阻尼 |
| **梯形法 (TR)** | $x_{n+1} = x_n + \frac{h}{2}[f_n + f_{n+1}]$ | 2阶 | A稳定 | 无（可能振荡） |
| **2S-DIRK** | 见下文 | 2-3阶 | L稳定可调 | 可控 |
| **3S-DIRK** | 见下文 | 3-4阶 | L稳定 | 强阻尼 |
| **Gear法** | 多步法 | 2-6阶 | 刚性稳定 | 可调 |

### A稳定性与L稳定性

**A稳定（A-Stable）**：数值方法对所有 $\text{Re}(\lambda) < 0$ 的测试方程 $\dot{x} = \lambda x$ 都稳定。

**L稳定（L-Stable）**：除A稳定外，还满足 $\lim_{\text{Re}(\lambda) \to -\infty} |R(\lambda h)| = 0$，即对无穷大负实部特征值完全阻尼。

**关键区别**：
- 梯形法是A稳定但非L稳定（$R(\infty) = -1$）
- 后向欧拉是L稳定（$R(\infty) = 0$）
- L稳定方法能完全抑制高频数值振荡

### 梯形法的数值振荡问题

梯形法在开关动作或故障后可能产生高频数值振荡：

$$
x_{n+1} = x_n + \frac{h}{2}(\lambda x_n + \lambda x_{n+1})
$$

特征根：

$$
z = \frac{1 + \lambda h/2}{1 - \lambda h/2}
$$

当 $\lambda h \to -\infty$，$z \to -1$，导致符号交替振荡。

**临界阻尼调整（CDA）**：在事件点后使用半步长后向欧拉抑制振荡。

## 主要积分方法详解

### 梯形法（Trapezoidal Rule, TR）

**公式**：

$$
x_{n+1} = x_n + \frac{h}{2}[f(t_n, x_n) + f(t_{n+1}, x_{n+1})]
$$

**局部截断误差**：$O(h^3)$

**在EMT中的应用**：
- 电感：$i_L(t) = \frac{\Delta t}{2L} v_L(t) + [i_L(t-\Delta t) + \frac{\Delta t}{2L} v_L(t-\Delta t)]$
- 电容：$i_C(t) = \frac{2C}{\Delta t} v_C(t) - [\frac{2C}{\Delta t} v_C(t-\Delta t) + i_C(t-\Delta t)]$

**频率畸变**：

梯形法引入的频率畸变：

$$
\omega_{actual} = \frac{2}{\Delta t} \tan\left(\frac{\omega_{sim} \Delta t}{2}\right)
$$

当 $\omega_{sim} \to \omega_{NY} = \pi/\Delta t$（奈奎斯特频率），$\omega_{actual} \to \infty$。

### 后向欧拉法（Backward Euler, BE）

**公式**：

$$
x_{n+1} = x_n + h f(t_{n+1}, x_{n+1})
$$

**特点**：
- L稳定，无数值振荡
- 1阶精度，误差较大
- 等效电导：$G_{eq} = \frac{\Delta t}{L}$（电感），$G_{eq} = \frac{C}{\Delta t}$（电容）

### 2S-DIRK（2-Stage Diagonally Implicit Runge-Kutta）

**一般形式**：

$$
\begin{aligned}
k_1 &= f(t_n + c_1 h, x_n + h a_{11} k_1) \\
k_2 &= f(t_n + c_2 h, x_n + h a_{21} k_1 + h a_{22} k_2) \\
x_{n+1} &= x_n + h(b_1 k_1 + b_2 k_2)
\end{aligned}
$$

**单参数族**（通过参数 $\lambda$ 控制特性）：

| 参数值 | 特性 | 应用场景 |
|--------|------|---------|
| $\lambda = 1-\sqrt{2}/2 \approx 0.293$ | L稳定，强阻尼 | 抑制数值振荡 |
| $\lambda = (3-\sqrt{3})/6 \approx 0.211$ | 3阶精度 | 高精度需求 |
| $\lambda = 1/4$ | 2阶精度，平衡 | 通用仿真 |
| $\lambda = (2\pm\sqrt{2})/4$ | 可调阻尼 | 灵活控制 |

**等效导纳**：$G_{eq} = \lambda \cdot \frac{\Delta t}{L}$（恒定，便于矩阵复用）

### 3S-DIRK（3-Stage DIRK）

**变阶变步长3S-DIRK**：

$$
\begin{aligned}
k_1 &= f(t_n, x_n) \\
k_2 &= f(t_n + c_2 h, x_n + h a_{21} k_1 + h a_{22} k_2) \\
k_3 &= f(t_n + c_3 h, x_n + h(a_{31} k_1 + a_{32} k_2 + a_{33} k_3)) \\
x_{n+1} &= x_n + h(b_1 k_1 + b_2 k_2 + b_3 k_3)
\end{aligned}
$$

**特点**：
- 3阶精度，L稳定
- 支持变阶（2阶/3阶切换）
- 支持变步长，通过局部截断误差估计调整步长

**局部截断误差估计**：

$$
\text{LTE} = \frac{\|x_{n+1}^{(3)} - x_{n+1}^{(2)}\|}{2^p - 1}
$$

### Gear法（向后微分公式, BDF）

**k阶BDF公式**：

$$
\sum_{j=0}^{k} \alpha_j x_{n+j} = h \beta_k f(t_{n+k}, x_{n+k})
$$

**常用阶数**：
- BDF2（2阶）：$\alpha_0 = 1/3, \alpha_1 = -4/3, \alpha_2 = 1, \beta_2 = 2/3$
- 阶数越高精度越高，但稳定性降低

**在EMT中的应用**：
- 用于刚性系统（时间常数差异大）
- 多步法需启动过程（从低阶开始）

## 适用边界

### 适用场景
- 需要逐时步保持电感、电容、频变网络和电力电子开关动态时
- 常规EMT网络（梯形法）
- 含频繁开关、故障切换（L稳定方法）
- 刚性系统（Gear法或DIRK）

### 不适用场景
- 目标频带明确的窄带模型（应采用频率匹配积分）
- 超高速暂态（需极小步长，考虑状态空间或解析解）
- 强非线性系统（需配合迭代或分段线性化）

### 注意事项
- 梯形法在不连续事件后可能保留数值振荡，需配合CDA或L稳定方法
- 大步长提高效率，但应由模型目标、控制带宽、开关频率约束
- 变步长算法需评估计算开销是否值得

## 技术演进脉络

### 1960-1970年代 (经典方法)
- **梯形法确立**
  - EMTP采用梯形法作为标准积分方法
  - 后向欧拉用于初始化
  - 数值振荡问题被发现

### 1980-1990年代 (振荡抑制)
- **临界阻尼调整（CDA）**
  - 在开关时刻插入半步长后向欧拉
  - 抑制梯形法数值振荡
  - 保持整体2阶精度

- **Gear法引入**
  - 用于刚性系统
  - 多步法提高精度
  - 稳定性分析完善

### 2000年代 (DIRK方法)
- **2S-DIRK引入EMT**
  - 可调参数控制阻尼特性
  - L稳定选项抑制振荡
  - 恒定等效导纳便于矩阵复用

### 2010年代 (变阶变步长)
- **3S-DIRK变阶变步长**
  - 自动调整阶数和步长
  - 误差控制自适应
  - 提高计算效率

- **紧凑格式**
  - 兼顾稳定性与突变处理
  - 单步多阶段计算

### 2020年代 (混合与优化)
- **混合积分策略**
  - 按元件类型选择积分方法
  - 正常工况用梯形法
  - 事件点用L稳定方法

- **大步长优化**
  - 3S-DIRK支持大步长
  - 保持精度和稳定性
  - 适用于实时仿真

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally]] | 2008 | 将2S-DIRK用于EMT离散化，讨论精度与振荡抑制 |
| [[optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas|Optimization of numerical integration methods for the simulation of dynamic phasors]] | 2009 | 面向动态相量模型的频率匹配积分 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact scheme for electromagnetic transients]] | 2023 | 用紧凑格式兼顾稳定性与突变处理 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Numerical Integration]] | 2023 | 在MMC等效中结合混合积分、解耦和恒导纳思想 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK based EMT simulations]] | 2024 | 讨论2S-DIRK在EMT应用中的补充处理 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step-size electromagnetic transients]] | 2024 | 面向较大步长EMT的隐式积分 |

## 相关方法
- [[nodal-analysis|节点分析法]]
- [[state-space-method|状态空间法]]
- [[fixed-admittance|恒导纳模型]]
- [[average-value-model|平均值模型]]
- [[multirate-method|多速率方法]]

## 相关主题
- [[topics/dynamic-phasor|动态相量]]
- [[topics/real-time-simulation|实时仿真]]
- [[topics/parallel-computing|并行计算]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP]] | 2004 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Runge-Kutta Method]] | 2008 |
| [[第29-卷-第34-期-中-国-电-机-工-程-学-报-vol29-no34-dec-5-2009|考虑任意重事件发生的多步变步长电磁暂态仿真算法]] | 2009 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step size electromagnetic transients]] | 2021 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact scheme for electromagnetic transients]] | 2023 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK based EMT simulations]] | 2024 |
| [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi|Three-stage implicit integration for large time-step-size electromagnetic transients]] | 2024 |

## 深度增强内容

### 1. 核心原理详解

#### 1.1 稳定性分析框架

**线性测试方程**：

$$
\dot{x} = \lambda x, \quad \text{Re}(\lambda) < 0
$$

应用于数值方法得：

$$
x_{n+1} = R(z) x_n, \quad z = \lambda h
$$

其中 $R(z)$ 为**稳定性函数**。

**各方法的稳定性函数**：

| 方法 | $R(z)$ | $R(\infty)$ |
|------|--------|-------------|
| 前向欧拉 | $1 + z$ | $\infty$（不稳定） |
| 后向欧拉 | $\frac{1}{1-z}$ | 0（L稳定） |
| 梯形法 | $\frac{1+z/2}{1-z/2}$ | -1（A稳定） |
| 2S-DIRK | $\frac{1+(1-2\lambda)z}{(1-\lambda z)^2}$ | $0$（$\lambda=1-\sqrt{2}/2$） |

**稳定区域**：
- A稳定：稳定区域包含整个左半平面
- L稳定：A稳定 + $R(\infty) = 0$

#### 1.2 局部截断误差分析

局部截断误差（LTE）表示单步误差：

$$
\text{LTE} = x(t_{n+1}) - x_{n+1} = C_p h^{p+1} x^{(p+1)}(t_n) + O(h^{p+2})
$$

其中 $p$ 为方法阶数，$C_p$ 为误差常数。

| 方法 | 阶数 $p$ | 误差常数 $C_p$ |
|------|---------|---------------|
| 后向欧拉 | 1 | $-1/2$ |
| 梯形法 | 2 | $-1/12$ |
| 2S-DIRK（$\lambda=1/4$） | 2 | 可调 |
| 3S-DIRK | 3 | 可调 |

#### 1.3 频率响应畸变

数值积分在频域引入的畸变可通过 $s$ 平面映射分析。

**梯形法的双线性变换**：

$$
s = \frac{2}{h} \frac{z-1}{z+1}
$$

对应连续频率 $\omega$ 与离散频率 $\omega_d$ 关系：

$$
\omega = \frac{2}{h} \tan\left(\frac{\omega_d h}{2}\right)
$$

**畸变特性**：
- 低频（$\omega h \ll 1$）：畸变小，$\omega \approx \omega_d$
- 高频（$\omega h \to \pi$）：畸变大，$\omega \to \infty$
- 奈奎斯特频率（$\omega_d = \pi/h$）：$\omega \to \infty$

### 2. 算法流程

#### 阶段一：网络预处理
1. **元件分类**：
   - 线性动态元件（L、C）
   - 非线性元件（饱和电感）
   - 开关器件

2. **积分方法分配**：
   - 常规网络：梯形法
   - 含电力电子：L稳定方法（2S-DIRK/BE）
   - 刚性系统：Gear法

3. **等效导纳计算**：
   - 电感：$G_{eq,L} = \frac{\Delta t}{\alpha L}$
   - 电容：$G_{eq,C} = \frac{C}{\alpha \Delta t}$
   - 其中 $\alpha$ 取决于积分方法

#### 阶段二：时域推进
1. **预测**（多步法）：用历史值预测新值
2. **校正**（隐式法）：求解非线性方程
3. **收敛判断**：检查迭代残差
4. **历史源更新**：为下一步计算历史项

#### 阶段三：事件处理
1. **开关动作检测**：
   - 自然换相（过零点）
   - 强制换相（触发信号）

2. **振荡抑制策略**：
   - CDA：插入半步长BE
   - 方法切换：TR $\to$ L稳定方法
   - 插值修正：精确计算开关时刻

3. **重启动**：
   - 多步法需重新初始化
   - 变步长方法调整步长

### 3. 参数选取指南

#### 3.1 时间步长选择

| 应用场景 | 推荐步长 | 选择依据 | 注意事项 |
|---------|---------|---------|---------|
| **常规输电网络** | 50-100 μs | 工频周期(20ms)的1/200-1/400 | 确保奈奎斯特频率>2kHz |
| **MMC详细建模** | 10-20 μs | 子模块电容电压波动 | 避免虚假损耗 |
| **两电平VSC** | 1-10 μs | IGBT开关暂态 | 捕捉开关细节 |
| **实时仿真** | 20-50 μs | 实时约束 | 配合恒导纳模型 |
| **大步长仿真** | 200-500 μs | 3S-DIRK | 需验证精度 |

#### 3.2 积分方法选择

| 场景 | 推荐方法 | 参数设置 | 理由 |
|------|---------|---------|------|
| **稳态运行** | 梯形法 | 固定步长 | 2阶精度，无耗散 |
| **故障/开关** | 2S-DIRK | $\lambda = 1-\sqrt{2}/2$ | L稳定，抑制振荡 |
| **初始化** | 后向欧拉 | 大步长 | L稳定，快速收敛 |
| **变步长** | 3S-DIRK | 变阶变步长 | 自适应效率 |
| **刚性系统** | Gear法 | 2-3阶 | 刚性稳定 |

#### 3.3 混合积分策略

**元件级混合**：
- 输电线：梯形法（线性）
- 发电机：梯形法（详细模型）
- 换流器：2S-DIRK（开关频繁）

**时间级混合**：
- 正常工况：梯形法
- 事件前1-2步：切换L稳定方法
- 事件后恢复期：切回梯形法

### 4. 性能分析

#### 4.1 计算复杂度

| 方法 | 每步计算量 | 矩阵分解 | 适用规模 |
|------|-----------|---------|---------|
| 梯形法 | $O(n)$ | 每步（变导纳）或一次（恒导纳） | 大规模 |
| 后向欧拉 | $O(n)$ | 同上 | 大规模 |
| 2S-DIRK | $2 \times O(n)$ | 两次求解 | 中等规模 |
| 3S-DIRK | $3 \times O(n)$ | 三次求解 | 中小规模 |
| Gear法 | $O(n)$ | 多步历史存储 | 大规模 |

#### 4.2 精度与效率权衡

| 方法 | 精度 | 效率 | 稳定性 | 综合推荐 |
|------|------|------|--------|---------|
| 梯形法 | ★★★ | ★★★★★ | ★★★ | 通用首选 |
| 2S-DIRK | ★★★ | ★★★★ | ★★★★★ | 电力电子 |
| 3S-DIRK | ★★★★ | ★★★ | ★★★★★ | 高精度 |
| Gear法 | ★★★★ | ★★★★ | ★★★★ | 刚性系统 |

#### 4.3 数值振荡对比

| 工况 | 梯形法 | 2S-DIRK(L) | 3S-DIRK(L) | BE |
|------|--------|-----------|-----------|-----|
| 开关后 | 有振荡 | 无振荡 | 无振荡 | 无振荡 |
| 故障后 | 有振荡 | 无振荡 | 无振荡 | 无振荡 |
| 稳态 | 精确 | 良好 | 精确 | 有阻尼 |

### 5. 最佳实践与注意事项

#### 5.1 数值振荡抑制

**识别数值振荡**：
- 波形出现高频振荡（频率接近奈奎斯特频率）
- 振荡幅值不随时间衰减
- 改变步长后振荡频率改变

**抑制方法**：
1. **CDA（Critical Damping Adjustment）**：
   - 在事件点插入半步长后向欧拉
   - 随后恢复梯形法
   - 整体保持2阶精度

2. **方法切换**：
   - 检测到事件前切换L稳定方法
   - 事件后稳定再切回梯形法

3. **插值技术**：
   - 精确计算开关时刻
   - 线性插值或高阶插值

#### 5.2 步长控制

**固定步长**：
- 简单，适合实时仿真
- 需按最严重要求选择步长

**变步长**：
- 通过LTE估计调整步长
- 公式：$h_{new} = h_{old} \left(\frac{\tau}{\text{LTE}}\right)^{1/(p+1)}$
- 需设置最大/最小步长限制

**步长限制因素**：
- 开关频率
- 控制带宽
- 线路传播时间
- 稳定性约束

#### 5.3 初始化

**稳态初始化**：
- 使用潮流计算结果
- 相量域到瞬时值转换
- 谐波稳态计算

**非初始化方法**：
- 从全零初始开始
- 后向欧拉大步长过渡
- 逐步减小步长至正常值

#### 5.4 误差控制

**局部误差估计**：
- 使用同阶或高阶公式对比
- 嵌入式Runge-Kutta方法
- 3S-DIRK的变阶策略

**全局误差控制**：
- 误差积累监测
- 关键变量检查
- 能量守恒验证

### 6. 与其他方法的协同

#### 6.1 与节点分析法结合

数值积分生成伴随电路后，与节点分析结合：

$$
Y_{eq} v = i_{inj} - i_{hist}
$$

- $Y_{eq}$：等效导纳矩阵（依赖于积分方法）
- $i_{hist}$：历史电流源（依赖于积分方法和前一步状态）

#### 6.2 与状态空间法结合

状态空间离散化：

$$
x_{n+1} = \Phi x_n + \Gamma u_n
$$

其中 $\Phi$、$\Gamma$ 由积分方法决定：
- 梯形法：$\Phi = (I - \frac{h}{2}A)^{-1}(I + \frac{h}{2}A)$
- 后向欧拉：$\Phi = (I - hA)^{-1}$

#### 6.3 与多速率方法结合

不同子系统可采用不同积分方法：
- 快子系统（电力电子）：小步长 + L稳定方法
- 慢子系统（输电网）：大步长 + 梯形法
- 接口处理：插值/外推 + 稳定性保证

---

**注**：以上内容整合了2004-2025年间数值积分在EMT仿真中的最新研究成果，涵盖2S-DIRK、3S-DIRK、紧凑格式、混合积分等前沿进展。

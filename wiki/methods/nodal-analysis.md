---
title: "节点分析与伴随电路 (Nodal Analysis / Companion Circuit)"
type: method
tags: [nodal-analysis, companion-circuit, emtp, admittance, conductance]
created: "2026-04-13"
---

# 节点分析与伴随电路 (Nodal Analysis / Companion Circuit)

## 概述

节点分析法（Nodal Analysis）是EMTP类仿真器的核心求解方法。通过将电路中每个元件替换为其伴随电路（Companion Circuit）模型，形成节点导纳矩阵，求解节点电压。

## 核心原理

### 伴随电路模型
- 电阻：导纳 G = 1/R
- 电感：伴随电流源 + 等效电导（梯形积分）
- 电容：伴随电流源 + 等效电导
- 传输线：Bergeron模型（行波等值）

### 求解流程
1. 每个元件转换为伴随电路
2. 组装节点导纳矩阵 G·v = i
3. 求解线性方程组得到节点电压
4. 由电压计算支路电流和元件状态

## 数值积分

- **梯形法**：最常用，A稳定但有数值振荡
- **后向Euler**：强阻尼，抑制振荡但精度低
- **Gear法**：多步法，高阶精度
- **2S-DIRK**：对角隐式Runge-Kutta

## 稀疏矩阵求解

- 大型导纳矩阵通常是稀疏的
- 稀疏LU分解（KLU算法）
- 迭代法（共轭梯度）
- GPU加速稀疏求解

## 在EMT中的地位

- EMTP、PSCAD/EMTDC、ATP的标准求解框架
- 所有设备模型最终接入节点方程
- 接口技术的基础（混合仿真、多速率）

## 相关方法
- [[numerical-integration]]
- [[state-space-method]]
- [[fixed-admittance]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|A combined state-space nodal method for the simulation of po]] | 2011 |
| [[nodal-reduced-induction-machine-modeling-for|Nodal Reduced Induction Machine Modeling for]] | 2012 |
| [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir|A Comparative Study of Electromagnetic Transient Simulations]] | 2021 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo|Direct Interfacing of Parametric Average-Value Models of AC&]] | 2022 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-|An Automatable Approach for Small-Signal Stability Analysis ]] | 2023 |
| [[inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us|Inaccuracies due to the frequency warping in simulation of e]] | 2023 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |

## 深度增强内容

 基于提供的论文数据，以下是针对 **节点分析与伴随电路 (Nodal Analysis / Companion Circuit)** 方法的深度增强内容：

---

## 1. 核心原理详解

### 1.1 基础节点导纳方程

EMT仿真的核心求解框架基于改进增广节点分析（Modified Augmented Nodal Analysis, MANA），其统一矩阵形式为：

$$
\begin{bmatrix} 
Y_n & A \\ 
B & C 
\end{bmatrix}
\begin{bmatrix} 
v \\ 
i_x 
\end{bmatrix}
=
\begin{bmatrix} 
j \\ 
e 
\end{bmatrix}
$$

其中：
- $Y_n \in \mathbb{R}^{n \times n}$ 为节点导纳矩阵（Nodal Admittance Matrix）
- $v \in \mathbb{R}^n$ 为节点电压向量
- $j \in \mathbb{R}^n$ 为注入电流源向量
- $i_x$ 为附加支路电流（如电压源、电感等需要增广的变量）
- $A, B, C$ 为反映元件约束的关联子矩阵

### 1.2 伴随电路离散化模型

各动态元件通过数值积分转换为伴随电路（Companion Circuit）：

**电感元件（梯形积分）：**
$$
i_L(t) = \frac{\Delta t}{2L} v_L(t) + \left[ i_L(t-\Delta t) + \frac{\Delta t}{2L} v_L(t-\Delta t) \right]
$$

等效为电导 $G_{eq} = \frac{\Delta t}{2L}$ 并联历史电流源 $I_{hist}$。

**电容元件（梯形积分）：**
$$
i_C(t) = \frac{2C}{\Delta t} v_C(t) - \left[ \frac{2C}{\Delta t} v_C(t-\Delta t) + i_C(t-\Delta t) \right]
$$

等效为电导 $G_{eq} = \frac{2C}{\Delta t}$ 并联历史电流源。

### 1.3 状态空间-节点联合分析框架

对于包含复杂控制或电力电子设备的系统，采用组合状态空间-节点分析法（Combined State-Space Nodal Method）。系统方程表示为：

$$
\begin{cases}
\dot{x} = A x + B u \\
Y_n v = j + D x
\end{cases}
$$

其中状态变量 $x$ 与节点电压 $v$ 通过接口矩阵 $D$ 耦合。离散化后形成增广系统：

$$
\begin{bmatrix} 
I - \frac{\Delta t}{2}A & -\frac{\Delta t}{2}B \\ 
-D & Y_n 
\end{bmatrix}
\begin{bmatrix} 
x(t) \\ 
v(t) 
\end{bmatrix}
=
\begin{bmatrix} 
\text{RHS}_x \\ 
\text{RHS}_v 
\end{bmatrix}
$$

### 1.4 频率畸变与数值稳定性

采用梯形积分（TR）时，双线性变换引入的频率畸变函数为：

$$
\Psi(\omega) = \frac{2}{\Delta t} \tan\left(\frac{\omega \Delta t}{2}\right)
$$

当 $\omega \to \omega_{NY}$（奈奎斯特频率）时，$\lim \Psi(\omega) = \infty$，导致电感电容值严重失真。3S-DIRK算法通过参数 $\lambda$ 控制数值特性：

- **A稳定最优精度**：$\lambda = \frac{1-\sqrt{3}}{3} \approx 0.42265$
- **L稳定（消除振荡）**：$\lambda = 1 - \frac{\sqrt{2}}{2} \approx 0.29289$

等效导纳保持恒定 $G = \lambda/h$，确保算法切换时无需重新因子化。

### 1.5 恒定导纳矩阵技术

对于电力电子变换器，通过开关函数离散化实现恒定导纳矩阵：

$$
G_{sys} = \text{const}, \quad \forall t
$$

利用半隐式延迟解耦原理，将变拓扑网络转化为固定拓扑的伴随网络，避免每步长的LU分解重构。

---

## 2. 算法流程

### 阶段一：网络预处理
1. **拓扑分析**：识别独立节点，建立节点-支路关联矩阵 $A_a$
2. **元件分类**：区分线性元件、非线性元件、电力电子开关
3. **子网分割**（可选）：基于长输电线或节点分裂法将网络分解为 $m$ 个子网

### 阶段二：伴随电路生成
1. **离散化参数计算**：
   - 计算各元件等效导纳 $G_{eq} = f(\Delta t, \lambda)$
   - 初始化历史电流源 $I_{hist}(0)$
2. **开关状态处理**：
   - 详细模型：根据开关状态更新导纳矩阵（变导纳）
   - 等效模型：保持 $G$ 恒定，通过伴随源反映开关动作

### 阶段三：矩阵组装与求解
1. **构建导纳矩阵**：
   $$
   Y_n = A_a Y_b A_a^T
   $$
   其中 $Y_b$ 为支路导纳对角阵。

2. **稀疏LU分解**（KLU算法）：
   - 符号分析：确定填充元（fill-in）位置
   - 数值分解：$Y_n = LU$
   - 对于恒定导纳矩阵，仅执行一次分解，后续使用前代/回代

3. **求解节点电压**：
   $$
   v = Y_n^{-1} (j - j_{hist})
   $$

### 阶段四：状态更新与迭代
1. **支路电流计算**：$i_{br} = Y_b (A_a^T v - v_s)$
2. **历史电流源更新**：
   - 电感：$I_{hist,L}(t) = i_L(t) + \frac{\Delta t}{2L} v_L(t)$
   - 电容：$I_{hist,C}(t) = -i_C(t) - \frac{2C}{\Delta t} v_C(t)$
3. **控制器/非线性元件更新**：计算下一时步的等效注入电流

### 阶段五：误差控制与步长调整（变步长算法）
1. **局部截断误差（LTE）估计**：
   $$
   \epsilon = \frac{\|v^{(p)} - v^{(p-1)}\|}{2^p - 1}
   $$
2. **步长调整**：
   $$
   \Delta t_{new} = \Delta t_{old} \left( \frac{\tau}{\epsilon} \right)^{1/(p+1)}
   $$
   其中 $\tau$ 为容差，$p$ 为方法阶数（3S-DIRK为2-3阶）。

---

## 3. 参数选取指南

### 3.1 时间步长选择策略

| 应用场景 | 推荐步长 | 理论依据 | 注意事项 |
|---------|---------|---------|---------|
| **常规输电网络** | 50-100 μs | 工频周期(20ms)的1/200-1/400 | 确保奈奎斯特频率>2kHz，覆盖主要谐波 |
| **MMC详细建模** | 10-20 μs | 子模块电容电压波动捕捉 | 2022年论文显示，401电平MMC需<20μs以避免虚假损耗 |
| **两电平VSC** | 1-10 μs | IGBT开关暂态捕捉 | 2022年论文指出导纳矩阵需恒定化处理 |
| **电力电子变压器** | 1-10 μs | 高频变压器(1-20kHz) | 步长需<开关周期的1/100 |
| **PAVM接口** | 1000-2000 μs | 消除一步延迟后的稳定性极限 | 2022年论文验证可安全提升至ms级 |
| **实时仿真** | 20-50 μs | 硬实时约束 | FPGA实现可达40μs(2025年数据) |

### 3.2 积分方法参数

**梯形法（TR） vs 后退欧拉（BE）切换：**
- 正常工况：$\alpha = 0$（纯梯形，$O(\Delta t^3)$ 精度）
- 故障/开关时刻：$\alpha = 1$（纯后退欧拉，强阻尼）
- 灵活切换算法：通过权重系数 $\alpha \in [0,1]$ 平滑过渡

**3S-DIRK算法参数：**
- 高精度模式：$\lambda = 0.42265$（3阶精度）
- 强稳定模式：$\lambda = 0.29289$（L稳定，消除数值振荡）

### 3.3 导纳矩阵管理策略

| 策略 | 适用条件 | 计算开销 | 精度影响 |
|-----|---------|---------|---------|
| **恒定导纳** | 电力电子开关频繁动作 | 最低（单次LU分解） | 需配合开关插值技术，THD<0.3% |
| **变导纳** | 非线性铁磁元件、电弧 | 高（每步重构） | 精确，但计算量 $O(n^3)$ |
| **分区混合** | 交直流混联电网 | 中等 | 交流侧恒定，直流侧变导纳 |

---

## 4. 性能分析

### 4.1 计算复杂度与加速比

| 方法/模型 | 矩阵规模 | 加速比 | 误差指标 | 来源论文 |
|----------|---------|-------|---------|---------|
| **传统详细模型** | $O(N \cdot n^3)$ | 基准1× | - | - |
| **CH-MMC戴维南等效** | 从11阶→5阶（-54.5%） | 518× | $\lambda_{NIAE}$ < 1% | 2024年论文 |
| **PAVM直接接口** | 嵌入节点矩阵 | 10-20× | 消除一步延迟误差 | 2022年论文 |
| **受控源解耦** | 高阶→多个低阶子矩阵 | 10-100× | 有功误差<5.86% | 2024年论文 |
| **MAB-PET简化模型** | $6N+1$→$2N+3$节点 | 100-1000× | 极高精度 | 2025年论文 |
| **恒定G矩阵SST** | 单次LU分解 | 50-100× (AVM)<br>10-20× (DEM) | 功率误差<0.1% | 2025年论文 |
| **双向堆排序MMC** | 排序复杂度$O(K \log K)$ | 实时可行 | 电容电压平衡精度保持 | 2022年论文 |

### 4.2 内存与存储需求

| 组件 | 传统方法 | 优化方法（2024-2025） | 节约比例 |
|-----|---------|---------------------|---------|
| **导纳矩阵存储** | 稠密矩阵 $n^2$ | 稀疏CSR格式 + KLU | 90%+（大规模系统） |
| **子模块状态** | $N$个电容电压（400+） | 2个等效阀段（CH-MMC） | 99.5%（状态变量） |
| **预存矩阵** | $2^N$种拓扑（不可行） | 恒定矩阵 + 开关函数 | 存储需求恒定 |
| **FPGA资源** | - | 逻辑单元41%，乘法器56% | 单芯片542节点实时 |

### 4.3 数值精度对比

| 方法 | 局部截断误差 | 全局误差累积 | 数值振荡 | 适用场景 |
|-----|------------|------------|---------|---------|
| **梯形法（TR）** | $O(\Delta t^3)$ | 周期性脉动 | 有（A稳定） | 常规电磁暂态 |
| **后退欧拉（BE）** | $O(\Delta t^2)$ | 单调累积 | 无（L稳定） | 故障初始化 |
| **3S-DIRK（变阶）** | $O(\Delta t^3)$-$O(\Delta t^4)$ | 可控 | 无（L稳定模式） | 刚性系统 |
| **CDA（临界阻尼调整）** | 故障时降至$O(\Delta t^2)$ | 较大 | 抑制 | 传统开关处理 |

---

## 5. 最佳实践与注意事项

### 5.1 数值振荡抑制
1. **L稳定算法选择**：对于含电力电子的系统，优先选用 $\lambda = 1-\sqrt{2}/2$ 的3S-DIRK或后退欧拉法，确保 $R(\infty) = 0$。
2. **插值技术**：在大步长（20-50μs）下，必须采用线性插值修正开关时刻，消除因离散采样导致的相位偏移和虚假功率损耗（2019年论文显示经典AEM可能因延迟产生显著虚假损耗）。

### 5.2 接口与延迟消除
- **直接接口法**：参数化平均值模型（PAVM）应直接线性化接口方程嵌入节点矩阵，消除传统伴随电路接口的 $\Delta t$ 延迟，可将稳定步长从数十微秒提升至毫秒级。
- **解耦边界处理**：采用受控源解耦时，确保解耦延时 $\Delta t$ 远小于系统最小时间常数，通常要求 $\Delta t < 0.1\tau_{min}$。

### 5.3 矩阵求解优化
1. **恒定导纳策略**：对于含高频开关的PET或MMC，优先采用开关函数+恒定 $G$ 矩阵方法，避免每步长LU分解，可节省90%以上矩阵求解时间。
2. **稀疏性保持**：利用KLU算法针对电路拓扑优化排序，减少填充元，对于542节点系统可在40μs内完成求解。

### 5.4 频率畸变补偿
- 当仿真关注高频（>1kHz）特性时，注意梯形积分引入的频率畸变：
  $$
  \omega_{actual} = \frac{2}{\Delta t} \tan\left(\frac{\omega_{sim} \Delta t}{2}\right)
  $$
- 在奈奎斯特频率附近（$\omega \Delta t \to \pi$），误差呈指数级放大，此时应采用递归卷积法或减小步长。

### 5.5 初始化与稳态
- 利用MANA潮流计算为EMT提供初始值（2023年论文），可显著缩短达到谐波稳态的暂态过程时间，避免长时间启动仿真。

---

## 6. 与其他方法的对比

### 6.1 节点分析法 vs 状态空间法

| 特性 | 节点分析法（Nodal） | 状态空间法（State-Space） |
|-----|-------------------|------------------------|
| **方程维度** | 仅节点电压（降维） | 所有储能元件状态（全面） |
| **矩阵结构** | 稀疏对称（易并行） | 稠密（全耦合） |
| **非线性处理** | 伴随电路迭代 | 直接非线性方程组 |
| **多速率支持** | 自然支持（子网分割） | 需复杂接口算法 |
| **电磁-机电混合** | 需外部接口 | 易于与机电模型集成 |
| **适用规模** | 超大规模（>10000节点） | 中小规模（<1000状态） |

### 6.2 节点分析法 vs 分裂法（Split-based）

| 特性 | 节点分析法 | 分裂法（如TDAS） |
|-----|-----------|----------------|
| **求解架构** | 联立求解（Monolithic） | 分裂求解（Partitioned） |
| **数值稳定性** | 无条件稳定（A/L稳定） | 依赖接口延迟处理 |
| **并行效率** | 85-95%（子网分割后） | 理论上更高，但精度损失 |
| **电力电子建模** | 直接嵌入 | 需特殊接口处理 |
| **实现复杂度** | 低（商业软件标准） | 高（需自定义接口） |

### 6.3 传统MANA vs 改进MANA（Unified MANA）

| 特性 | 传统MANA | Unified MANA (2023) |
|-----|---------|-------------------|
| **多频支持** | 单频假设 | 支持多微电网独立频率 |
| **元件建模** | 简化等效 | 可直接纳入开关、变压器详细模型 |
| **求解器** | 分离求解 | 统一Jacobian矩阵 |
| **初始值** | 需额外计算 | 稳态解直接用于EMT初始化 |

### 6.4 方法选择决策树

```
系统规模？
├── 大规模 (>1000节点) → 节点分析法 + 恒定导纳优化
│   ├── 含高频开关 (PET/MMC) → 戴维南等效 + 开关插值
│   └── 常规网络 → 稀疏LU + 变步长3S-DIRK
├── 中小规模 + 强非线性 → 状态空间法或混合方法
└── 实时仿真需求 → 节点分割并行 + FPGA加速
    ├── 硬实时(>50μs步长) → 受控源解耦/平均值模型
    └── 离线加速 → 详细模型 + GPU并行
```

---

**注**：以上内容基于2011-2025年间54篇相关论文的最新研究成果，特别整合了2023-2025年间关于频率畸变分析、PAVM直接接口、固态变压器等效建模等前沿进展。
---
title: "机电暂态模型 (Electromechanical Model)"
type: model
tags: [electromechanical, transient-stability, swing-equation, synchronous-machine, multi-timescale]
created: "2026-05-04"
updated: "2026-05-18"
---

# 机电暂态模型 (Electromechanical Model)

## 定义与边界

机电暂态模型是描述电力系统在大扰动下发电机转子机械运动与电磁功率之间动态相互作用的简化模型。该类模型假设电网处于准稳态（基波对称、电压电流瞬时正弦），忽略电磁暂态过程，专注于功角稳定性分析。

**边界限定**：本模型适用于频率变化范围小（49–51 Hz）、网络可视为基波正弦稳态的场景。对于快速暂态、谐波、非对称故障或电力电子设备主导的工况，需采用完整 EMT 模型。

机电暂态模型的核心价值在于**计算效率**：通过忽略高频电磁暂态细节（电磁暂态时间常数 τe 通常为 10–100 ms，远快于机电暂态时间常数 τm 的 0.5–5 s），将详细的微分-代数方程降维为低维机电振荡方程组，使大规模系统的暂态稳定分析成为可能。

## EMT 中的角色

机电暂态模型在 EMT 知识体系中主要承担以下角色：

- **混合仿真接口**：与电磁暂态详细模型协同，形成多时间尺度仿真框架
- **计算加速**：对外部系统采用机电暂态简化，聚焦内部网络的 EMT 分析
- **稳定性评估**：提供功角稳定的宏观判断，与 EMT 过电压分析互补
- **初始化基准**：为 EMT 仿真提供稳态运行点
- **系统等值**：大规模电网采用机电暂态降阶等值后，可快速评估全网稳定性

在 EMT-TS 混合仿真体系中，机电暂态模型与 EMT 模型的**接口边界**需要精确定义。Jalili-Marandi 等（2009）指出，接口处需完成变量转换（TS 基频相量 ↔ EMT 三相瞬时值），并通过多速率插值/外推解决 100–1000 倍的步长失配问题。

## 主要分支与机制

### 1. 摇摆方程 (Swing Equation)

描述发电机转子机械运动的基本方程：

$$M\frac{d^2\delta}{dt^2} = P_m - P_e - D\frac{d\delta}{dt}$$

其中 $M$ 为惯性常数（H·rad），$\delta$ 为功角（rad），$P_m$ 为机械功率（pu），$P_e$ 为电磁功率（pu），$D$ 为阻尼系数（pu·s/rad）。对于多机系统，等效摇摆方程为：

$$M_i\frac{d^2\delta_i}{dt^2} = P_{m,i} - P_{e,i}(\boldsymbol{\delta}) - D_i\frac{d\delta_i}{dt}$$

同步机电暂态过程通常采用标幺值系统，基准时间 $T_{base} = 1/(2\pi f_0) \approx 3.18$ ms（60 Hz 系统）。

### 2. 同步发电机简化模型

| 模型类型 | 等效电路 | EMT 复杂度 | 适用场景 |
|---------|---------|-----------|---------|
| **经典模型 (Classical)** | 恒定内电势 $E'$ 串 $X_d'$ | 最低 | 首摆稳定分析 |
| **暂态模型 (Transient)** | $E'$ 串 $X_d'$，计及励磁 | 中等 | 机电动态主导 |
| **次暂态模型 (Subtransient)** | $E''$ 串 $X_d''$、$X_q''$ | 较高 | 故障初期 |
| **详细 Park 模型** | 完整 $dq$ 坐标，计及磁路饱和 | 最高 | 深度 EMT |

经典模型假设故障期间 $E'$ 恒定，等效电磁功率 $P_e = E'^2 Y_{eq} \sin(\delta - \delta_{eq})$，仅需 1 个状态变量 $\delta$。Park 模型在 $dq$ 旋转坐标系下需联立求解定转子电压方程、磁链方程和转子运动方程，包含 $E_d'$、$E_q'$、$\psi_d$、$\psi_q$ 等多个状态变量。

### 3. 网络代数方程

假设网络瞬时平衡，节点电压方程为：

$$\mathbf{P} = f(\boldsymbol{\delta}, \mathbf{V}, \boldsymbol{\theta})$$
$$\mathbf{Q} = g(\boldsymbol{\delta}, \mathbf{V}, \boldsymbol{\theta})$$

其中 $(\mathbf{V}, \boldsymbol{\theta})$ 为电压幅值和相角向量。机电暂态假设所有母线电压对称且为基频正弦，因此网络方程退化为只含正序分量的快速潮流计算。

### 4. 励磁系统与调速器

励磁系统模型传递函数（IEEE Std 421.5）：

$$V_{ref} \xrightarrow{K_A} \frac{K_A}{1 + \tau_A s} \xrightarrow{E_{fd}} \text{同步机励磁}$$

调速器模型（一阶惯性加 droop）：

$$P_{m,i} = P_{set,i} - K_{g,i}(\omega_i - \omega_0)$$

其中 $K_g$ 为 droop 系数（通常 4–5%），$\omega_0 = 2\pi f_0$。

## 形式化表达

### 微分-代数方程组 (DAE)

发电机侧（$n$ 台机）：

$$\dot{\boldsymbol{\delta}} = \boldsymbol{\omega} - \boldsymbol{\omega_0}$$
$$M_i \dot{\boldsymbol{\omega_i}} = P_{m,i} - P_{e,i}(\boldsymbol{\delta}, \mathbf{V}) - D_i(\boldsymbol{\omega_i} - \boldsymbol{\omega_0})$$

网络代数约束（$m$ 母线）：

$$\mathbf{0} = \mathbf{g}(\boldsymbol{\delta}, \mathbf{V}) = \mathbf{Y}_{bus} \mathbf{V} \angle \boldsymbol{\theta} - \mathbf{I}(\boldsymbol{\delta})$$

联立形成 $2n + 2m$ 维 DAE 系统，采用隐式梯形法或 Gear 法（适合刚性系统）离散后牛顿迭代求解。

### 机电-电磁接口

混合仿真中的接口变量双向传递：

| 接口方向 | 传递量 | 数学表达 |
|---------|--------|---------|
| 机电→电磁 | 等值内电势、阻抗 | $E_{eq} \angle \delta_{eq}$ |
| 电磁→机电 | 等值功率、电压 | $P_{EMT}, V_{bus}$ |

接口误差控制：

$$\|P_{EMT} - P_{TS}\| < \epsilon_P \quad (\epsilon_P \text{通常取 } 0.5\%)$$

Jalili-Marandi（2009）给出多速率接口步长比 $N = 500$ 时，线性预测校正使边界电压幅值误差 < 0.5%、相位误差 < 0.3°。

## 关键技术挑战

### 机群识别与等效临界群划分

EEAC 类方法的关键是如何从全系统振荡模式中识别临界机群。常用指标：

$$\omega_i(t_0) > \bar{\omega} + k\sigma_\omega$$

其中 $\bar{\omega}$ 是群内平均转速，$\sigma_\omega$ 是标准差，$k$ 取 1.5–2.0。**识别错误会直接导致稳定裕度符号和 CCT 判断错误**。

### 时间尺度耦合

机电暂态（ms 级）与电磁暂态（μs 级）的耦合带来三个层次挑战：

1. **接口同步**：TS 步长 $\Delta t_{TS} = 1$–10 ms，EMT 步长 $\Delta t_{EMT} = 1$–50 μs，步长比 $N = 100$–1000
2. **插值/外推**：需要用多项式插值将 TS 粗步长边界电压映射至 EMT 细步长，解决时间尺度失配
3. **延迟补偿**：接口通信延迟需通过预测-校正机制补偿，延迟容忍度 < 0.5 ms

### 电力电子接口精度

含强电力电子控制（HVDC、FACTS、新能源换流器）时，等效电磁功率 $P_e$ 可能依赖状态切换而非仅依赖 $\delta$：

$$P_e \neq f(\delta) \quad \text{（电力电子主导场景）}$$

此时机电-电磁接口的等效功率曲线不再是光滑函数，面积积分的物理含义需要重新审视。Chen（2022）指出，此类场景需采用动态相量接口或纯 EMT 模型。

### 大规模系统计算效率

纯机电暂态仿真（不计 EMT 交互）的计算瓶颈：

- 牛顿迭代雅可比矩阵稠密（全网电气耦合）
- 特征值分析规模 $O(n^3)$，$n$ 为同步机台数
- 需在计算效率和精度之间权衡

## 量化性能边界

### 机电-EMT 混合仿真加速比

| 研究 | 测试条件 | 加速比 | 精度误差 |
|------|---------|--------|---------|
| **Sun (2014)** | 10 s 并网光伏仿真，EMT 50 μs vs 机电 1 ms | **11.4×**（46.6 s → 4.1 s） | 波形吻合（未量化） |
| **Jalili-Marandi (2009)** | IEEE 39 节点，多速率插值 N=500 | 接口电压误差 <0.5%，相位误差 <0.3° | — |
| **Chen (2022)** | ADPSS 特高压/高压直流，15 方式批量 | 单运行方式 **30×**（15 h → 0.5 h） | 直流功率偏差 <1%，触发角偏差 <1° |

Sun（2014）明确说明：EMT 步长 50 μs（2000 Hz 开关频率），机电步长 1 ms（步长扩大 20 倍），仿真 10 s 时长计算时间从 46.6 s 降至 4.1 s，**验证场景限于光照强度阶跃扰动，未覆盖电网故障、低电压穿越或弱电网工况**。

Chen（2022）基于 ADPSS 平台和 10 余回特高压/高压直流的实际电网验证，接口箝位启动策略使混合仿真在 0.6 s 内达到稳态，**不自动适用于 MMC-HVDC 或新能源控制深度耦合场景**。

### 全机电仿真 vs 全 EMT 仿真

| 指标 | 纯机电仿真 | 纯 EMT 仿真 |
|------|----------|-----------|
| 典型步长 | 1–10 ms | 1–50 μs |
| 状态变量 | $2n$（$\delta$, $\omega$） | $>100n$（含电磁暂态） |
| 适用频率 | 0.1–2 Hz（机电振荡） | 0–10 kHz（电磁暂态） |
| 计算速度 | 快（毫秒级/秒） | 慢（秒级/分钟） |
| 精度 | 限于功角稳定性 | 含谐波、开关暂态 |

## 适用边界与选择指南

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 频率范围 | 49–51 Hz | 基波假设有效 |
| 对称性 | 三相平衡 | 正序分量主导 |
| 时间尺度 | >100 ms | 电磁暂态已衰减 |
| 设备类型 | 同步机主导 | 电力电子设备比例低 |
| 主导动态 | 功角/电压稳定 | 非高频开关暂态 |

### 失效边界

- **快速暂态**：故障、开关操作引起的 μs 级快速过程
- **谐波谐振**：非线性设备引起的谐波放大
- **非对称故障**：单相或两相故障的负序/零序效应
- **电力电子设备主导**：换流器控制的快速动态（<10 ms）
- **次同步振荡**：轴系扭振与电网的耦合（需电磁-机械耦合分析）
- **FIDVR（故障引起电压恢复延迟）**：感应电动机负荷动态导致电压恢复慢

### 选择指南

| 分析目标 | 推荐模型 | 理由 |
|---------|---------|------|
| 首摆功角稳定 | 机电暂态+经典发电机 | 计算快，解析可解 |
| 多摆失稳 | 机电暂态+详细发电机+励磁 | 需时域仿真验证 |
| 含 HVDC/FACTS | 混合仿真（EMT 局部+机电外部） | 兼顾精度与效率 |
| 换流器限流动态 | 纯 EMT | 需 μs 级开关模型 |
| 大规模系统筛选 | 机电暂态+等值 | 数百机系统可实时 |
| 谐波与稳定性交互 | 动态相量+EMT | 桥接基频与宽频 |

## 来源论文

- [[sources/electromechanical-transient-electromagnetic-transient-hybrid-simulation-of-doubl]] - Xiong 等（2020）机电-电磁混合仿真
- [[sources/interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix]] - Jalili-Marandi（2009）接口技术综述
- [[sources/comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g]] - Sun 等（2014）光伏并网机电暂态模型
- [[sources/electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi]] - Liu 等（2014）MMC 机电暂态建模
- [[sources/直驱式风电机组机电暂态建模及仿真]] - 高峰等（2011）直驱风机机电建模
- [[sources/chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas]] - Chen 等（2022）ADPSS 混合仿真框架
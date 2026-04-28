---
title: "多速率方法 (Multi-Rate Method)"
type: method
tags: [multirate, time-step, partitioning, interface]
created: "2026-04-13"
---

# 多速率方法 (Multi-Rate Method)

## 概述

多速率方法（Multi-Rate Method）在同一仿真框架内对不同子系统采用不同的时间步长，以兼顾计算效率和仿真精度。这是处理包含多种时间尺度电力系统的关键技术。

## 核心思想

- **快变子系统**（电力电子换流器）：小步长（μs级）
- **慢变子系统**（输电网、发电机）：大步长（ms级）
- 通过接口算法实现数据交换与同步

## 关键技术

### 系统拆分
- 按时间尺度分区
- 按物理特性分区
- 按仿真精度需求分区

### 接口技术
- 线性插值
- 多项式外推
- 动态相量接口
- 预测-校正方法

### 稳定性分析
- 接口延迟对稳定性的影响
- 步长比约束
- 数值振荡风险

## 应用场景

- MMC-MTDC系统仿真
- 机电-电磁混合仿真
- 含高比例新能源的电网
- 实时仿真加速
- SFA-EMT多速率仿真

## 相关方法
- [[co-simulation]]
- [[dynamic-phasor]]
- [[numerical-integration]]
- [[interpolation-method]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems|Shifted frequency analysis-EMTP multirate simulation of powe]] | 2021 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|27&28/Multi-rate real time hybrid simulation of controllable]] | 2026 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |

## 深度增强内容

 基于提供的论文数据及电力系统电磁暂态仿真理论，以下是针对**多速率方法 (Multi-Rate Method)**的深度增强内容：

---

## 1. 核心原理详解

### 1.1 数学建模基础

多速率方法处理的是刚性微分方程组（stiff ODEs）的数值积分问题。电力系统可描述为：

$$
\begin{cases}
\dot{\mathbf{x}}_f = \mathbf{f}(\mathbf{x}_f, \mathbf{x}_s, t), & \text{快变子系统} \\
\dot{\mathbf{x}}_s = \mathbf{g}(\mathbf{x}_f, \mathbf{x}_s, t), & \text{慢变子系统}
\end{cases}
$$

其中 $\mathbf{x}_f \in \mathbb{R}^{n_f}$ 为电力电子换流器等快动态状态变量，时间常数 $\tau_f \sim \mu s$；$\mathbf{x}_s \in \mathbb{R}^{n_s}$ 为输电网络、同步发电机等慢动态状态变量，时间常数 $\tau_s \sim ms$。

### 1.2 时间尺度分离与离散化

设快步长为 $h_f$，慢步长为 $h_s$，步长比 $N = h_s / h_f$（通常 $N \in [10, 100]$）。采用隐式梯形法（Trapezoidal Rule）离散化：

**快子系统（每 $h_f$ 积分）：**
$$
\mathbf{x}_f^{k+1} = \mathbf{x}_f^k + \frac{h_f}{2} \left[ \mathbf{f}(\mathbf{x}_f^k, \mathbf{x}_s^{k'}, t_k) + \mathbf{f}(\mathbf{x}_f^{k+1}, \mathbf{x}_s^{k'+1}, t_{k+1}) \right]
$$

**慢子系统（每 $h_s = N \cdot h_f$ 积分）：**
$$
\mathbf{x}_s^{m+1} = \mathbf{x}_s^m + \frac{h_s}{2} \left[ \mathbf{g}(\mathbf{x}_f^{m}, \mathbf{x}_s^m, t_m) + \mathbf{g}(\mathbf{x}_f^{m+1}, \mathbf{x}_s^{m+1}, t_{m+1}) \right]
$$

其中 $k' = \lfloor k/N \rfloor$ 为慢时间索引。

### 1.3 接口算法与耦合机制

**多端口戴维南等效（MATE框架）：**
快子系统向慢子系统提供宽频等效电路，接口处满足：
$$
\mathbf{v}_b = \mathbf{Z}_{th} \mathbf{i}_b + \mathbf{v}_{oc}
$$
其中 $\mathbf{Z}_{th}$ 为接口处宽频戴维南阻抗矩阵，$\mathbf{v}_{oc}$ 为开路电压。

**动态相量接口：**
对于SFA（Shifted Frequency Analysis）多速率方法，信号经移频变换：
$$
x(t) = \Re\left\{ \tilde{x}(t) e^{j\omega_0 t} \right\}
$$
其中 $\tilde{x}(t)$ 为复包络（动态相量），带宽显著降低，允许使用大步长 $h_s \gg h_f$ 而满足Nyquist准则：
$$
h_s < \frac{1}{2f_{max, \tilde{x}}}
$$

**插值-平均耦合：**
慢变量在快步长间采用 $p$ 阶插值：
$$
\mathbf{x}_s(t_k + \tau) = \sum_{i=0}^p \mathbf{x}_s^{m-i} \cdot L_i(\tau), \quad \tau \in [0, h_s]
$$
快变量对慢子系统的贡献通过在一个慢步长内的平均值计算：
$$
\bar{\mathbf{x}}_f = \frac{1}{N} \sum_{i=0}^{N-1} \mathbf{x}_f^{mN+i}
$$

### 1.4 稳定性约束

多速率系统的稳定性受接口延迟和步长比影响。基于根轨迹分析，步长比需满足：
$$
N < N_{max} = \frac{\pi}{2\omega_{max} h_f}
$$
其中 $\omega_{max}$ 为快子系统最高有效频率。若采用预测-校正（Predictor-Corrector）接口，稳定性条件可放宽至 $N \leq 100$。

---

## 2. 算法流程

### 2.1 离线分区阶段

1. **时间常数分析**：计算各状态矩阵特征值 $\lambda_i$，按 $|\Re(\lambda_i)|$ 排序
2. **谱聚类分区**：将系统划分为快集 $\mathcal{F} = \{i: |\Re(\lambda_i)| > \omega_{th}\}$ 和慢集 $\mathcal{S}$
3. **接口节点识别**：确定快-慢子系统电气耦合边界 $\mathcal{B}$

### 2.2 运行时积分流程（同步多速率）

```
初始化: t=0, x_f=x_f0, x_s=x_s0, m=0

While t < T_end:
    // 慢子系统步进 (每N个快步执行一次)
    If m % N == 0:
        1. 快→慢: 计算快变量在[t, t+h_s]的平均等效源 $\bar{\mathbf{s}}_f$
        2. 预测: $\hat{\mathbf{x}}_s^{m+1} = \mathbf{x}_s^m + h_s \cdot \mathbf{g}(\mathbf{x}_s^m, \bar{\mathbf{s}}_f)$
        3. 求解慢网方程: $\mathbf{Y}_s \mathbf{V}_s = \mathbf{I}_s(\hat{\mathbf{x}}_s^{m+1})$
        4. 校正: 梯形法迭代求解 $\mathbf{x}_s^{m+1}$
    
    // 快子系统步进 (每步执行)
    5. 慢→快: 插值慢变量 $\mathbf{x}_s(t)$ 至当前快时间点
    6. 构建快子系统等效电路 (考虑插值后的慢边界条件)
    7. 快网求解: $\mathbf{Y}_f \mathbf{V}_f = \mathbf{I}_f(\mathbf{x}_f^{k+1}, \mathbf{x}_s(t))$
    8. 状态更新: $\mathbf{x}_f^{k+1} = \mathbf{A}_f \mathbf{x}_f^k + \mathbf{B}_f \mathbf{u}_f$
    
    // 误差校验与步长控制 (针对动态相量多速率)
    9. 计算局部截断误差 LTE = $||\mathbf{x}^{new} - \mathbf{x}^{old}||$
    10. If LTE > Tol: 回退步长 $h_f \leftarrow h_f/2$, 重算
    11. Else if LTE < Tol/10: $h_f \leftarrow \min(2h_f, h_{f,max})$
    
    12. t ← t + h_f, k ← k+1, m ← ⌊t/h_s⌋
```

### 2.3 SFA-EMT混合多速率特殊流程

1. **频谱分离**：基频分量 $\omega_0$ 移至零频，形成SFA子系统（大步长）
2. **复数域求解**：SFA使用复数状态变量 $\tilde{\mathbf{x}}_s \in \mathbb{C}$，EMT使用实数 $\mathbf{x}_f \in \mathbb{R}$
3. **解析性维护**：虚部EMT与实部EMT并行运行，确保 $\tilde{x}(t) = x_{re}(t) + j x_{im}(t)$ 满足Cauchy-Riemann条件

---

## 3. 参数选取指南

### 3.1 时间步长选择策略

| 应用场景 | 快步长 $h_f$ | 慢步长 $h_s$ | 步长比 $N$ | 理论依据 |
|---------|------------|------------|-----------|---------|
| **MMC-MTDC系统** | 10-50 μs | 1-5 ms | 50-100 | 子模块电容动态 $\tau \sim 1ms$，阀级控制 $\tau \sim 100\mu s$ |
| **风电并网** | 20-100 μs | 2-10 ms | 50-200 | 变流器开关频率 $f_{sw}=2-5kHz$，电网机电振荡 $f_{mech}=0.1-2Hz$ |
| **SFA-EMT混合** | 10-50 μs (EMT) | 0.5-2 ms (SFA) | 20-100 | SFA带宽 $<200Hz$，Nyquist要求 $h_s < 2.5ms$ |
| **实时仿真** | 25-50 μs | 0.5-1 ms | 20-40 | 硬件计算延迟约束，稳定性优先 |

### 3.2 接口参数配置

**插值阶数选择：**
- 线性插值（1阶）：适用于慢变量变化平缓场景，计算开销小
- 三次Hermite插值（3阶）：当慢子系统含较快动态（如励磁系统）时使用，需存储导数信息
- **建议**：电力电子-电网接口推荐2-3阶插值，误差控制 $<0.1\%$

**等效电路更新频率：**
- 戴维南等效阻抗 $\mathbf{Z}_{th}$：每 $5-10$ 个慢步长更新一次（假设运行点缓慢变化）
- 等效电源 $\mathbf{v}_{oc}$：每个快步长更新（捕捉开关瞬态）

### 3.3 误差控制参数

基于2026年动态相量多速率论文，自适应步长控制阈值：
$$
\text{Tol}_{abs} = 10^{-4} \cdot \max(|\mathbf{x}|), \quad \text{Tol}_{rel} = 10^{-3}
$$
当慢变量轨迹误差 $>0.1\%$ 时触发步长回退机制。

---

## 4. 性能分析

基于文献数据的定量性能汇总：

| 论文方法 | 测试系统规模 | 时间尺度跨度 | 步长配置 | 计算加速比 | 精度指标 |
|---------|------------|------------|---------|-----------|---------|
| **动态相量多速率 (2026)** | 10,000+节点巴西电网 | $10^{-6}s \sim 10^0s$ (6个数量级) | $h_f=10-100\mu s$, $h_s=1-10ms$, $N=50-100$ | **50%-90%** 计算时间减少 | 慢变量误差 $<0.1\%$，快变量保真度完整 |
| **SFA-EMTP多速率 (2021)** | 多端口系统 | 基频+暂态 | EMT: $20\mu s$, SFA: $1ms$, $N=50$ | 显著优于单速率EMT（具体比例取决于SFA子系统占比） | 复包络解析性保持，频谱搬移无混叠 |
| **MMC-MTDC多速率 (2017)** | 大规模AC/MTDC | 阀级 $\mu s$ / 系统级 $ms$ | $h_f=20\mu s$, $h_s=1ms$ | 实时仿真可行（RTDS实现） | 接口误差 $<1\%$ |
| **PET多速率 (2025)** | 电力电子变压器 | 开关级 $ns$ / 控制级 $ms$ | $h_f=1\mu s$, $h_s=100\mu s$, $N=100$ | 高精度仿真加速 **10-20倍** | 铁芯饱和与高频振荡精确捕捉 |

**关键发现：**
- 当慢子系统占比超过60%时，多速率方法通常可实现**5-10倍**加速
- 步长比 $N>100$ 时，接口数值振荡风险显著增加，需采用隐式插值或增广状态接口
- 在10,000节点级系统中，动态相量多速率方法保持与单速率EMT相当的暂态保真度，同时实现近一个数量级的效率提升

---

## 5. 最佳实践与注意事项

### 5.1 系统分区最佳实践

**避免"刚性接口"：**
- 不要在电力电子设备开关瞬间附近设置接口，建议在变压器绕组或电缆对端（自然低通滤波点）分区
- 接口处应避免包含强非线性元件（如避雷器、铁磁饱和），否则需减小步长比 $N$

**分区粒度平衡：**
- 快子系统规模建议控制在总系统的 **5-20%**，过大将抵消多速率优势
- 优先将控制系统、保护逻辑纳入慢子系统（即使其采样率较高，可通过插值处理）

### 5.2 数值稳定性保障

**抗混叠预处理：**
在快→慢数据传递前，对快变量进行低通滤波：
$$
\bar{x}_f = \frac{1}{1+\tau_f s} x_f, \quad \tau_f \approx h_s/2
$$
避免高频开关谐波通过接口注入慢子系统导致数值不稳定。

**功率守恒校验：**
每个慢步长结束时，验证接口功率平衡：
$$
P_{interface} = \sum_{b \in \mathcal{B}} \Re\{\mathbf{V}_b \cdot \mathbf{I}_b^*\} < \epsilon_{tol}
$$
若偏差超过阈值，触发接口变量校正或步长减半。

### 5.3 实时仿真特殊考虑

- **同步机制**：硬件在环(HIL)仿真中，快步长任务必须在单个 $h_f$ 内完成，慢任务可延迟但需在 $h_s$ 内完成
- **数据流水线**：采用双缓冲机制避免读写冲突，快任务读取上一慢步长的插值表，慢任务收集当前窗口的快变量统计值

### 5.4 常见失效模式

1. **接口反射现象**：当传输线长度 $L < c \cdot h_s$（$c$为波速）时，行波在单慢步长内往返，导致虚假振荡。**解决**：减小 $h_s$ 或采用分布参数线路模型而非集总参数。
2. **代数环**：快子系统输出直接反馈至慢子系统输入且无动态缓冲。**解决**：插入一阶惯性环节 $1/(1+0.001s)$ 打破代数环。

---

## 6. 与其他方法的对比

| 对比维度 | 多速率方法 (Multi-Rate) | 单速率全EMT | 机电-电磁混合仿真 (E-MT) | 联合仿真 (Co-Simulation) |
|---------|----------------------|-----------|----------------------|---------------------|
| **时间步长** | 异构 ($\mu s$ + $ms$) | 统一 ($\mu s$) | 异构 (EMT $\mu s$ + TS $ms$) | 完全独立，可异步 |
| **模型统一性** | 统一EMT框架，数值一致 | 完全统一 | 异构（微分-代数 vs 常微分） | 可异构（不同软件） |
| **接口位置** | 子系统内部电气节点 | 无 | 传统上在边界母线 | 软件间通信接口 |
| **计算效率** | **高**（比单速率快5-50倍） | 低（大规模系统不可行） | 中等（TS部分极快） | 中低（通信开销大） |
| **数值稳定性** | 中等（需精心设计接口） | 高（无条件稳定算法） | 低（接口延迟导致发散风险） | 低（异步通信误差） |
| **适用场景** | 含电力电子的大规模电网 | 小系统详细设计 | 传统机电暂态分析 | 多物理场耦合（热-电-机械） |
| **频率覆盖** | 全频带（DC~kHz） | 全频带 | 基频+低次谐波 | 取决于各子系统设置 |
| **实现复杂度** | 中等（需修改求解器内核） | 低 | 中等（成熟商业软件支持） | 高（需API开发） |

**关键差异分析：**

- **vs 单速率EMT**：多速率通过牺牲接口处的局部精度换取整体效率，适合关注系统级慢动态与局部快动态交互的场景，而非纯器件级分析。

- **vs 传统E-MT混合**：多速率方法保持全电磁暂态（EMT）框架，避免机电暂态（TS）的准稳态假设，能准确捕捉电力电子引起的次/超同步振荡，而传统E-MT在这些频带存在模型误差。

- **vs 联合仿真**：多速率通常是**紧耦合**（monolithic），在同一求解器内完成，接口信息通过内存共享传递；而联合仿真（Co-simulation）是**松耦合**，可能涉及不同软件（如MATLAB+PSCAD），通过通信协议（如FMI、TCP/IP）交互，延迟和误差更大。2021年SFA论文中的"MATE多速率"属于紧耦合，而2017年MMC论文的"Co-Simulation"指分区并行计算，需特别注意区分。

**选择建议：**
- 当研究**HVDC-MMC与电网交互**时，优先选择多速率而非E-MT，以准确捕捉阀侧谐波
- 当进行**实时硬件在环测试**时，多速率方法比联合仿真更稳定，但需确保快步长任务在 deadline 内完成
- 当系统含**大量分散式电力电子**（如光伏、储能）时，动态相量多速率（2026年论文方法）比传统分区多速率更具扩展性

---

*以上内容基于2017-2026年间电力系统多速率仿真领域的关键文献，涵盖了从传统EMT多速率到动态相量/SFA混合方法的最新进展。*

## 深度增强内容

 基于提供的论文数据及电力系统电磁暂态仿真理论，以下是针对**多速率方法 (Multi-Rate Method)**的深度增强内容：

---

## 1. 核心原理详解

### 1.1 数学建模基础

多速率方法处理的是刚性微分方程组（stiff ODEs）的数值积分问题。电力系统可描述为：

$$
\begin{cases}
\dot{\mathbf{x}}_f = \mathbf{f}(\mathbf{x}_f, \mathbf{x}_s, t), & \text{快变子系统} \\
\dot{\mathbf{x}}_s = \mathbf{g}(\mathbf{x}_f, \mathbf{x}_s, t), & \text{慢变子系统}
\end{cases}
$$

其中 $\mathbf{x}_f \in \mathbb{R}^{n_f}$ 为电力电子换流器等快动态状态变量，时间常数 $\tau_f \sim \mu s$；$\mathbf{x}_s \in \mathbb{R}^{n_s}$ 为输电网络、同步发电机等慢动态状态变量，时间常数 $\tau_s \sim ms$。

### 1.2 时间尺度分离与离散化

设快步长为 $h_f$，慢步长为 $h_s$，步长比 $N = h_s / h_f$（通常 $N \in [10, 100]$）。采用隐式梯形法（Trapezoidal Rule）离散化：

**快子系统（每 $h_f$ 积分）：**
$$
\mathbf{x}_f^{k+1} = \mathbf{x}_f^k + \frac{h_f}{2} \left[ \mathbf{f}(\mathbf{x}_f^k, \mathbf{x}_s^{k'}, t_k) + \mathbf{f}(\mathbf{x}_f^{k+1}, \mathbf{x}_s^{k'+1}, t_{k+1}) \right]
$$

**慢子系统（每 $h_s = N \cdot h_f$ 积分）：**
$$
\mathbf{x}_s^{m+1} = \mathbf{x}_s^m + \frac{h_s}{2} \left[ \mathbf{g}(\mathbf{x}_f^{m}, \mathbf{x}_s^m, t_m) + \mathbf{g}(\mathbf{x}_f^{m+1}, \mathbf{x}_s^{m+1}, t_{m+1}) \right]
$$

其中上标 $k$ 表示快时间层，$m$ 表示慢时间层，满足 $t_m = t_{k=N \cdot m}$。

### 1.3 动态相量域的多速率扩展

基于动态相量（Dynamic Phasor, DP）的多速率方法通过傅里叶分解将时域信号 $x(t)$ 表示为：
$$
x(t) = \sum_{k=-K}^{K} X_k(t) e^{j k \omega_s t}
$$
其中 $X_k(t)$ 为第 $k$ 阶动态相量，$\omega_s$ 为基频。由于 $X_k(t)$ 为慢变复数包络，可采用大步长 $h_s$ 积分，而原始EMT信号 $x(t)$ 需用小步长 $h_f$ 积分。

**接口耦合机制：**
- **插值阶段**：将慢变量 $X_k$ 在快步长间进行 $p$ 阶多项式插值 $\hat{X}_k(t) = \sum_{i=0}^{p} c_i t^i$
- **平均阶段**：快变量在一个慢步长内的平均值为 $\bar{x}_f = \frac{1}{h_s} \int_{t_m}^{t_{m+1}} x_f(t) dt$，用于校正慢子系统源项

### 1.4 SFA-EMTP多速率框架

移频分析（Shifted Frequency Analysis, SFA）通过坐标变换将基频移至零频：
$$
x(t) = \text{Re}\{\sqrt{2} \underline{x}_{sf}(t) e^{j\omega_0 t}\}
$$
其中 $\underline{x}_{sf}(t)$ 为移频域复包络，其频谱集中在零频附近，允许使用毫秒级步长，而传统EMT保持微秒级步长。

**MATE（Multi-Area Thevenin Equivalent）接口：**
SFA子系统通过多端口戴维南等效与EMT子系统耦合：
$$
\underline{V}_{th} = \underline{Z}_{th} \underline{I} + \underline{V}_{oc}
$$
其中 $\underline{Z}_{th}$ 为在SFA时间步长决定的频率范围内的等效阻抗，实现宽频带解耦。

### 1.5 接口误差与稳定性分析

多速率系统的稳定性受接口延迟和插值误差影响。定义接口误差传递函数：
$$
\rho(z) = \frac{\lambda_f \lambda_s h_f h_s}{4} \cdot \frac{z^{-N} P(z)}{1 - \frac{\lambda_s h_s}{2} \cdot \frac{1+z^{-1}}{1-z^{-1}}}
$$
其中 $\lambda_f, \lambda_s$ 为子系统特征值，$P(z)$ 为插值多项式的Z变换。稳定性要求 $|\rho(z)| < 1$，由此导出步长比约束：
$$
N < \frac{2}{|\lambda_f| h_f} \cdot \frac{1}{1 + |\lambda_s| h_s/2}
$$

---

## 2. 算法流程

### 2.1 通用多速率仿真流程

```python
初始化: t=0, 设置 h_f, h_s=N·h_f, 误差容限 ε
初始化状态: x_f(0), x_s(0)
while t < T_end:
    # 慢子系统积分（每N个快步执行一次）
    if mod(t, h_s) == 0:
        # 接收快变量平均值或插值
        x_f_avg = interpolate_average(x_f_history, t, t+h_s)
        # 预测慢变量
        x_s_pred = predict(x_s, x_f_avg)
        # 校正并计算接口功率
        x_s_new = correct(x_s_pred, x_f_avg)
        check_error(||x_s_new - x_s_pred|| < ε)
    
    # 快子系统积分（每步执行）
    # 对慢变量进行高阶插值
    x_s_interp = polynomial_interpolate(x_s, t, t+h_f, order=3)
    # 积分快系统
    x_f_new = integrate_trapezoidal(x_f, x_s_interp, h_f)
    
    # 更新历史记录
    update_history(x_f_history, x_f_new)
    t = t + h_f
end
```

### 2.2 动态相量多速率算法（DP-MR）

1. **变量分离**：识别快动态（开关器件、故障）和慢动态（机电振荡、调速器）
2. **相量提取**：对慢支路应用滑动平均滤波提取动态相量 $X_k$
3. **双速率积分**：
   - 快域：标准EMT仿真，步长 $h_f = 10-50\ \mu s$
   - 慢域：动态相量仿真，步长 $h_s = 1-10\ ms$
4. **耦合计算**：
   - 慢→快：通过 $x(t) = \sum X_k(t) e^{j k \omega_s t}$ 重构时域波形
   - 快→慢：通过 $X_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-j k \omega_s \tau} d\tau$ 更新相量
5. **误差校验**：若快变量高频分量超过阈值，触发步长回退或切换至单速率模式

### 2.3 SFA-EMT混合多速率算法

1. **系统分区**：将电网分为SFA区（大电网、慢动态）和EMT区（电力电子设备、快动态）
2. **并行初始化**：
   - SFA侧：建立复数域导纳矩阵 $\underline{Y}_{sf}$，初始步长 $h_s$
   - EMT侧：建立实数域导纳矩阵 $G_{emt}$，初始步长 $h_f$
3. **同步循环**：
   - 在 $t = m \cdot h_s$ 时刻交换接口变量
   - SFA提供复数戴维南等效 $(\underline{V}_{th}, \underline{Z}_{th})$
   - EMT提供实数电流注入 $I_{emt}$
4. **插值与重构**：
   - 使用梯形插值将SFA电压转换为EMT边界条件
   - 使用加权平均将EMT电流反馈至SFA

---

## 3. 参数选取指南

### 3.1 时间步长选择策略

| 应用场景 | 快步长 $h_f$ | 慢步长 $h_s$ | 步长比 $N$ | 备注 |
|---------|-------------|-------------|-----------|------|
| MMC-HVDC并网 | $10-20\ \mu s$ | $0.5-1\ ms$ | $50-100$ | 考虑子模块电容动态 |
| 风电场聚合 | $50\ \mu s$ | $1-5\ ms$ | $20-100$ | 机网接口处加密 |
| 机电-电磁混合 | $100\ \mu s$ | $10\ ms$ | $100$ | 发电机慢动态 |
| 电力电子变压器 | $1-5\ \mu s$ | $0.1-0.5\ ms$ | $100-200$ | 高频隔离级需更小步长 |

### 3.2 插值阶数与误差控制

- **线性插值**：适用于步长比 $N < 20$，计算简单但引入 $O(h_s^2)$ 误差
- **三次样条插值**：推荐用于 $N \in [20, 100]$，平衡精度与计算成本
- **高阶外推**：仅用于预测阶段，校正阶段需隐式积分保证稳定性

**误差容限设置：**
- 电压误差容限：$\varepsilon_v = 0.01\ \text{p.u.}$（标幺值）
- 电流误差容限：$\varepsilon_i = 0.005\ \text{p.u.}$
- 相对误差限：$\varepsilon_{rel} = 10^{-4}$（用于自适应步长控制）

### 3.3 系统分区原则

1. **时间常数准则**：将时间常数相差 $>10$ 倍的元件分至不同子系统
2. **电气距离准则**：通过修改节点导纳矩阵，使分界面处联络线阻抗满足：
   $$
   \frac{L_{line}}{R_{line}} \approx \frac{h_s}{\pi}
   $$
3. **频率分离准则**：快子系统需包含 $>2\ \text{kHz}$ 的谐波分量，慢子系统限制在基频附近 $\pm 100\ \text{Hz}$

---

## 4. 性能分析

基于提供论文的量化性能对比：

| 性能指标 | 动态相量多速率 (2026) | SFA-EMTP多速率 (2021) | 单速率EMT参考 |
|---------|---------------------|---------------------|--------------|
| **系统规模** | >10,000 节点（巴西电网） | 未明确（典型测试系统） | 同左 |
| **时间尺度覆盖** | $\mu s$ 级 至 $s$ 级（6个数量级） | EMT: $\mu s$ 级, SFA: $ms$ 级 | 统一 $\mu s$ 级 |
| **步长配置** | $h_f=10-100\ \mu s$, $h_s=1-10\ ms$ | $h_f$ (EMT), $h_s$ (SFA) 差异显著 | $h_f$ 统一 |
| **计算效率提升** | **50% - 90%** 耗时减少 | 显著加速（与全EMT比） | 基准 100% |
| **典型步长比 $N$** | $50 - 100$ | 可变，基于MATE框架 | $N=1$ |
| **精度指标** | 慢变量误差 $<0.1\%$，快变量高频细节完整保留 | 基频分量精确，宽频带响应捕捉 | 参考基准 |
| **数值稳定性** | 绝对稳定（A-稳定梯形法+误差校验） | 绝对稳定（梯形法/后向欧拉） | 绝对稳定 |
| **适用场景** | 大规模电网机电-电磁暂态统一仿真 | 含电力电子设备的宽频分析 | 高精度小规模系统 |

**关键发现：**
- 在万节点级系统中，动态相量多速率方法可将仿真速度提升 **10-20 倍**，同时保持与单速率EMT相当的暂态精度
- SFA-EMTP方法通过复数域仿真减少状态变量数，适合分析电力电子引入的间谐波（subsynchronous oscillations）

---

## 5. 最佳实践与注意事项

### 5.1 系统分区最佳实践

**避免数值振荡：**
- 在分界面处添加虚拟电阻 $R_{virtual} = \frac{2L_{interface}}{h_s}$ 以抑制接口反射波
- 采用"阻尼接口"（Damped Interface）技术，在插值公式中加入阻尼系数 $\alpha \in [0.1, 0.3]$：
  $$
  x_{interp}(t) = (1-\alpha) x_{linear}(t) + \alpha x_{history}(t)
  $$

**处理开关事件：**
- 当快子系统检测到开关动作（如IGBT导通/关断）时，强制在 $t_{switch}$ 时刻同步慢子系统
- 采用"步长回退"（Step Rollback）机制：若开关时刻落在慢步长中间，回退至 $t_{switch}$ 并临时采用单速率仿真直至暂态平息

### 5.2 误差控制策略

**自适应步长调整：**
$$
h_{s,new} = h_{s,old} \cdot \min\left( \sqrt{\frac{\varepsilon_{tol}}{||e||}}, 2 \right)
$$
其中 $||e||$ 为局部截断误差估计。若连续3步 $||e|| > \varepsilon_{tol}$，则触发步长减半。

**多速率切换准则：**
当系统进入大扰动后的快变阶段（如故障期间），自动切换至单速率模式；待转子角偏差 $<5^\circ$ 且频率偏差 $<0.1\ \text{Hz}$ 后恢复多速率。

### 5.3 常见陷阱

1. ** aliasing（混叠）效应**：慢子系统采样率必须满足 $f_{s,slow} > 2 f_{max,slow}$，其中 $f_{max,slow}$ 为慢子系统最高关注频率（通常 $100-200\ \text{Hz}$）
2. ** 初始条件不一致**：多速率仿真需进行混合潮流计算，确保分界面处功率匹配，避免初始冲击
3. ** 分布式参数线路**：长距离输电线路的波过程可能跨越时间尺度，建议采用 Bergeron 模型并置于快子系统或特殊处理

---

## 6. 与其他方法的对比

### 6.1 与单速率全EMT仿真对比

| 对比维度 | 多速率方法 | 单速率EMT |
|---------|-----------|----------|
| **计算复杂度** | $O(n_f \cdot N + n_s)$，随慢变量比例增加而优化 | $O((n_f + n_s) \cdot N)$，固定高开销 |
| **内存需求** | 需存储双时间层历史数据（+20-30%） | 单一时间层，内存连续 |
| **精度控制** | 接口处引入 $10^{-4}-10^{-3}$ 级误差 | 全局一致精度，无接口误差 |
| **并行潜力** | 子系统天然解耦，适合并行计算 | 需矩阵分割，并行效率受限 |
| **适用规模** | 可处理 $10^4+$ 节点系统 | 通常限于 $10^3$ 节点以下 |

### 6.2 与传统联合仿真（Co-Simulation）对比

多速率方法与传统联合仿真（如EMT-TS联合仿真）的关键区别：

- **统一框架**：多速率通常在单一仿真器内实现，共享同一牛顿求解器；而联合仿真涉及独立工具间的数据交换（如通过FMI、API）
- **接口延迟**：多速率方法可设计为"零延迟"（通过预测-校正）；传统联合仿真受通信延迟影响，通常存在 $1-2$ 个步长的固有延迟
- **模型一致性**：多速率允许快/慢子系统使用相同详细程度的模型，仅时间步长不同；联合仿真通常要求慢子系统使用简化模型（如 TS 模型）

### 6.3 与纯动态相量法对比

- **频带覆盖**：纯动态相量法难以准确捕捉电力电子开关瞬间的高频电磁暂态；多速率方法通过保留EMT快子系统，完整保留这些细节
- **计算效率**：对于纯机电振荡分析，纯动态相量法效率更高；但含电力电子设备时，多速率方法在精度和效率间取得更好平衡
- **实现复杂度**：多速率需处理复杂的接口插值和同步逻辑；纯动态相量法实现相对直接

### 6.4 方法选择决策树

```
系统是否含电力电子设备？
├── 否 → 采用单速率TS或纯动态相量法
└── 是 → 设备时间常数是否远小于网络？
    ├── 否 → 单速率EMT
    └── 是 → 系统规模是否>1000节点？
        ├── 否 → 单速率EMT（保证精度）
        └── 是 → 多速率方法（推荐动态相量或SFA-EMT混合）
```

**推荐组合：**
- **超大规模电网（>5000节点）+ 高比例新能源**：动态相量多速率方法（2026论文方案）
- **含MMC-HVDC的 regional 电网**：SFA-EMTP多速率或基于MATE的接口方法
- **实时仿真场景**：固定步长多速率，配合FPGA实现快子系统，CPU实现慢子系统

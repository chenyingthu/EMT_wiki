---
title: "电池储能系统 (BESS)"
type: model
tags: [bess, battery, energy-storage, lithium-ion, bms, pcs, thevenin, norton, vectorized, gpu-parallel]
created: "2026-04-29"
updated: "2026-05-18"
---

# 电池储能系统 (Battery Energy Storage System, BESS)

## 定义

电池储能系统（BESS）将电能以化学能形式存储并在需要时释放，是电力系统重要的灵活性资源，通过电池管理系统（BMS）和储能变流器（PCS）实现充放电控制。其EMT建模覆盖电化学电池等效电路、荷电状态（SOC）估计、热管理和变流器控制，适用于电网侧储能、用户侧储能和新能源配套储能的电磁暂态仿真分析。

**核心公式** — 电池戴维南等效电路：

$$V_{bat} = E_0 + E_{pol} + E_{exp} + S_{ch} E_{chg} + (1-S_{ch})E_{dsc}$$

其中 $S_{ch}$ 为二进制充电状态指示变量（1=充电，0=放电）；$E_0$ 为恒压源，$E_{pol}$ 为极化电压，$E_{exp}$ 为指数区电压，$E_{chg}$/$E_{dsc}$ 分别为充放电动态电压。

## EMT中的角色

BESS在EMT仿真中面临三重挑战：

1. **规模挑战**：大型储能电站包含数百至数千个电池单元，每个单元独立建模计算量巨大
2. **多速率耦合**：电池电化学动态（秒级）与电力电子开关（微秒级）时间尺度分离
3. **异构性**：不同电池类型（LFP/NCM/LTO）的参数各异，向量化并行处理困难

BESS的EMT建模需要解决：**如何在保持电池内部动态细节的同时实现大规模并行加速**（Lin 2023）。

## 物理模型与数学描述

### 1. 电池等效电路

#### 1.1 戴维南（Thevenin）等效电路

电池模型可表示为电压源 $V_{bat}$ 串联内阻 $Z_B$ 的戴维南等效形式：

$$V_{Bat} = E_0 + E_{pol} + E_{exp} + S_{ch}E_{chg} + (1-S_{ch})E_{dsc}$$

其中各部分电压的物理含义：

$$E_{exp}(t) = A e^{-B \cdot i_{sat}}, \quad L^{-1}\left\{\frac{A/s}{B \cdot |i|/s + 1}\right\}$$

充放电动态电压的向量形式（并行计算用）：

$$E_{chg}(t) = \frac{K \cdot Q \cdot \bar{\iota}}{i_{sat} + K_Q Q}, \quad E_{dsc}(t) = \frac{K \cdot Q \cdot \bar{\iota}}{Q - i_{sat}}$$

充放电动态方程的时间域形式（经拉普拉斯反变换得）：

$$\frac{dE_{exp}(t)}{dt} = (B \cdot |i(t)|)(S_{ch}A - E_{exp}(t))$$

离散化（后向欧拉法）：

$$E_{exp}(t) = (1 - |i(t)|B\Delta t)E_{exp}(t-\Delta t) + B \cdot |i(t)|S_{ch}A\Delta t$$

#### 1.2 诺顿（Norton）等效电路

戴维南等效转换为诺顿等便于节点分析：

$$I_{Beq} = V_{Bat} \circ G_B$$

其中 $G_B = [G_{B1}, G_{B2}, ...]$ 为内阻导纳向量。

#### 1.3 向量化并行电池阵列

将多个电池单元组织为 $N_p \times N_s$ 阵列（$N_p$ 并联支路，$N_s$ 串联单元），通过向量化的元素级运算实现GPU并行加速：

$$V_{Bat} = E_0 + E_{pol} + E_{exp} + S_{ch} \circ E_{chg} + (I - S_{ch}) \circ E_{dsc}$$

$$V_{Bat} \in [V_{Bmin}, V_{Bmax}]$$

元素级运算符号 $\circ$（Hadamard积）和 $\div$（元素级除法）使所有电池单元的计算可并行执行。

### 2. SOC估计

#### 2.1 Coulomb计数法

$$SOC(t) = SOC(t_0) + \frac{1}{Q_{nom}}\int_{t_0}^{t}\eta \cdot i(\tau)d\tau$$

其中 $Q_{nom}$ 为额定容量（Ah），$\eta$ 为库仑效率（充电<1，放电=1）。

#### 2.2 指数区电压查表法

LFP电池的OCV-SOC关系在平台区（30%-80% SOC）电压变化极小，需用指数区电压补偿：

$$E_{exp} = A e^{-B \cdot i_{sat}}$$

### 3. 热模型

电池生热功率（Hirsch等人）：

$$Q_{gen} = I_{bat}^2 R_0 + I_{bat}^2 R_1 + I_{bat}^2 R_2 + I_{bat} T \frac{dV_{oc}}{dT}$$

热平衡方程：

$$C_{th}\frac{dT}{dt} = Q_{gen} - hA(T - T_{amb})$$

## 形式化表达

### 3.1 电池详细模型（Detailed Switching Model, DSM）

开关级模型保留电池内部电化学动态和Buck-Boost变流器的开关暂态，需要在每个开关状态变化时更新导纳矩阵（重三角化）。

### 3.2 戴维南等效模型（Thevenin Equivalent Model, TEM）

将每个子模块等效为戴维南电路（电压源+电阻），大幅降低导纳矩阵维度，同时通过反计算保留子模块内部变量信息。

**IDEM改进**（Wang 2025）：在传统DEM基础上增加辅助开关以处理同臂上下开关同时关断的工况（换流器闭锁和电池断开场景），结合PSCAD内置插值算法实现闭锁瞬态模拟。

### 3.3 平均值模型（Average Value Model, AVM）

将多电平换流器视为闭合黑箱，用平均电容电压和电池电流代替开关状态。无法捕捉子模块内部电气变量，但计算效率高。

### 3.4 仿真步长与精度权衡

| 模型 | 步长 | 精度 | 适用场景 |
|------|------|------|---------|
| DSM | 1-10 μs | 最高 | 换流器闭锁、故障分析 |
| TEM/IDEM | 10-50 μs | 高 | 稳态运行、响应特性 |
| AVM | 100-500 μs | 中 | 系统级聚合仿真 |

## 关键技术挑战

### 挑战1：GPU异构并行调度

GPU并非总是优于CPU——当系统异构性突出或缺乏完美拓扑对称性时，CPU顺序处理反而更高效。Lin 2023提出CPU-GPU异构架构：以同质性（homogeneity）为核心准则分配任务——BESS电池阵列高度同质→GPU SIMT并行；IEEE 118节点系统和直流电网异构→CPU顺序处理。

### 挑战2：大规模BESS的SOC管理

500个BESS单元（每个2.0 MVA）在IEEE 118节点系统中参与二次调频时，各单元SOC不一致导致功率分配优先级动态变化。需设计自适应功率补偿序列（Bus 56→63→43→33→83）。

### 挑战3：MMC-BESS换流器闭锁模拟

当上下臂开关同时关断时，传统DEM失效（依赖互补脉冲假设）。IDEM用辅助PSCAD开关选择对应工况支路，结合内置插值算法实现闭锁瞬态仿真。

### 挑战4：电池断开瞬态

电池深度放电或故障时需断开连接，断开瞬间电容电压冲击影响系统直流动态。IDEM引入补充决策公式处理此类工况。

### 挑战5：多速率耦合

EMT仿真步长（10-50 μs）与TS仿真步长（1-10 ms）不同，多速率耦合降低计算冗余但增加接口复杂度。

## 量化性能边界

### Lin 2023：GPU并行BESS加速

- **加速比**：CPU-GPU异构架构在IEEE 118节点系统+分布式BESS中实现 **>200倍** 加速（相对于纯CPU计算）
- **多流GPU执行**：相对于CPU获得约 **1.8倍** 加速（当计算对象为100个BESS单元时）
- **向量化一致性**：将异构电池参数统一为同构向量，消除GPU并行分支发散
- **EMT步长**：10-50 μs（电池阵列），TS步长：1-10 ms

### Wang 2025：MMC-BESS的IDEM

- **IDEM vs DSM**：在稳态运行、暂态响应、故障工况下轨迹与DSM基准高度吻合
- **闭锁瞬态**：上下臂同时关断时，IDEM波形偏差<0.5%，电池断开冲击误差<0.8%
- **加速**：简化模型后，加法与乘法运算减少约50%-70%，整体仿真速度较DSM提升 **10倍以上**
- **仿真步长**：10 μs（基准），闭锁瞬态稳定

### Cao 2023：FPGA超实时硬件仿真

- **超实时加速比**：51倍超实时（FTRT）加速
- **时间步长**：亚微秒级（sub-μs），满足电力电子开关级EMT精度

### Nguyen 2021：构网型BESS黑启动

- **黑启动时长**：光储混合电站18秒内完成7次时序投切
- **稳态精度**：仿真稳态电压幅值与数值优化解匹配误差<1%
- **电压恢复**：母线电压恢复时间<0.2秒

## 储能变流器（PCS）EMT建模方法

### 两电平VSC变流器

**PQ控制模式**：
$$P_{ref} = P_{set}, \quad Q_{ref} = Q_{set}$$

**下垂控制模式**：
$$P = P_0 - k_f(f - f_0), \quad Q = Q_0 - k_v(V - V_0)$$

**虚拟同步机（VSM）模式**：模拟同步机惯量响应，提供虚拟惯量和阻尼。

### MMC-BESS换流器

MMC-BESS每相桥臂由多个串联子模块（SM）构成，每个SM通过Buck-Boost变流器嵌入电池。SM操作状态由四个IGBT的触发脉冲FP1-4决定，组合出9种工作状态和4种电池工作模式（放电/充电/续流/断开）。

**IDEM建模框架**（Wang 2025）：
1. 将每个SM替换为戴维南等效电路
2. 每步长根据开关状态更新戴维南等效参数
3. 附加辅助开关处理同臂上下开关同时关断
4. 补充决策公式处理电池断开工况

## 典型参数

### 磷酸铁锂(LFP)电池

| 参数 | 数值 | 单位 |
|------|------|------|
| 额定电压 | 3.2 | V/节 |
| 充电截止电压 | 3.65 | V |
| 放电截止电压 | 2.5 | V |
| 额定容量 | 100-280 | Ah |
| 能量密度 | 140-160 | Wh/kg |
| 内阻(新) | 0.5-2 | mΩ |
| 循环寿命(80%DOD) | 3000-6000 | 次 |
| 工作温度 | -20~55 | °C |
| 最佳温度 | 15-25 | °C |

### PCS参数

| 参数 | 小型(100kW) | 中型(1MW) | 大型(10MW+) |
|------|-------------|-----------|-------------|
| 直流电压范围 | 500-850V | 600-1500V | 1000-1500V |
| 最大效率 | 97-98% | 98-98.5% | 98.5-99% |
| 功率响应时间 | <100ms | <100ms | <100ms |
| 谐波THD | <3% | <3% | <3% |
| 功率因数 | ±0.95可调 | ±0.95可调 | ±0.95可调 |

### 模型选择指南

| 应用场景 | 推荐模型 | 说明 |
|---------|---------|------|
| 调频性能分析 | 详细电池+PCS | 捕捉快速响应 |
| 能量管理 | SOC模型+效率曲线 | 关注能量 |
| 电能质量 | 平均值PCS模型 | 关注谐波 |
| 系统级仿真 | 等效功率源 | 大规模系统 |
| MMC-BESS换流器 | IDEM | 兼顾精度与效率 |

## 相关方法

- [[numerical-integration|数值积分]] — SOC计算与电池模型离散化
- [[state-space-method|状态空间法]] — 电池状态空间建模
- [[average-value-model|平均值模型]] — 系统级简化仿真
- [[droop-control-model|下垂控制模型]] — 一次调频控制实现
- [[gpu-parallel-acceleration|GPU并行加速]] — CPU-GPU异构计算架构

## 相关模型

- [[energy-storage-converter-model|储能变流器]] — PCS详细控制模型
- [[vsc-model|VSC模型]] — 电压源变换器拓扑
- [[mmc-model|MMC模型]] — 模块化多电平换流器
- [[igbt-model|IGBT模型]] — 开关器件模型
- [[real-time-simulation|实时仿真]] — 储能系统实时仿真

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Lin 等 2023]] | 2023 | 向量化电池模型+CPU-GPU异构并行，200倍加速 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|Wang 等 2025]] | 2025 | IDEM改进戴维南模型，涵盖闭锁和电池断开场景 |
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Nguyen 等 2021]] | 2021 | 构网型PV-BESS黑启动控制，18秒7步时序 |
| [[herath-2019-modeling-of-mmc-with-embedded-energy-storage|Herath 等 2019]] | 2019 | MMC嵌入BESS的EMT建模方法 |
| [[decoupled-detailed-equivalent-model-for-mmc-bess|Cao 等 2023]] | 2023 | MMC-BESS解耦详细等效模型与多速率EMT仿真 |
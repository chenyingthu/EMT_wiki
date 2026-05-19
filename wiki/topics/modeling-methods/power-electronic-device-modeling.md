---
title: "电力电子设备建模 (Power Electronic Device Modeling)"
type: topic
tags: [power-electronics, switch, igbt, diode, converter, emt, wide-bandgap, thermal]
created: "2026-05-01"
book-chapter: "7"
---

# 电力电子设备建模 (Power Electronic Device Modeling)

## 定义

电力电子设备建模是指在电磁暂态（EMT）仿真中，用数学模型表示功率半导体器件（IGBT、MOSFET、GTO、SiC MOSFET、GaN HEMT、二极管等）及其组成的变换器拓扑的技术总和。电力电子设备具有**强非线性**（导通/关断状态突变）、**多时间尺度**（μs 级开关与 ms 级机电动态共存）和**高频开关**（kHz~MHz）等特征，对其进行准确的暂态建模是电网安全稳定分析、保护整定和控制策略验证的基础。

## EMT 中的角色

在 EMT 仿真中，电力电子设备建模面临三大核心矛盾：

1. **精度与效率的矛盾**：详细开关模型（DSM）精度最高，但每次开关动作都要求重构导纳矩阵并重新分解，计算成本随系统规模呈线性增长；平均值模型（AVM）计算效率高，但丢失所有开关纹波细节
2. **多时间尺度的耦合**：开关微秒级暂态过程（如 IGBT 关断的拖尾电流）与电网毫秒级动态过程（如电压恢复）在同一仿真步长内耦合，多速率方法（Multi-rate）是解决途径之一
3. **非线性的数值处理**：开关状态变化导致节点导纳矩阵不对称，传统梯形积分法（Trapezoidal）在此类不连续点产生数值振荡，需要 CDA（Critical Damping Adjustment）或插值方法抑制

## 核心机制：四层建模体系

### 层次一：器件物理层

功率半导体器件的 EMT 建模从器件物理行为出发，描述其电气特性。

**理想开关模型**是最简形式，将器件视为二值电阻：

$$
R_{sw}(t) = \begin{cases} R_{on} \approx 10^{-3} \sim 10^{-6} \, \Omega & \text{导通状态} \\ R_{off} \approx 10^{6} \sim 10^{12} \, \Omega & \text{关断状态} \end{cases}
$$

**IGBT 详细物理模型**描述集电极电流与端电压、米勒电容、结温的耦合关系：

$$
i_C(t) = f(v_{CE}, v_{GE}, T_j, \frac{dv_{CE}}{dt})
$$

关键参数包括阈值电压 $V_{th}$、跨导 $g_m$、米勒电容 $C_{gc}$ 和拖尾电流时间常数 $\tau_{tail}$。拖尾电流是 IGBT 关断过程中特有的尾电流，其时间常数 $\tau_{tail} \in [0.2,\, 1.0]\, \mu s$ 影响关断损耗和电压尖峰。

**SiC MOSFET** 与硅基 IGBT 相比，开关速度快 10 倍（20–100 ns），导通电阻随温度变化（10–100 mΩ），高频建模需考虑寄生电感、电容的谐振效应。

**热-电耦合模型**将功率损耗与结温相互作用：

$$
T_j(t) = T_a + \int_0^t P_{loss}(\tau) \cdot Z_{th}(t - \tau) \, d\tau
$$

其中 $Z_{th}$ 为 Foster 或 Cauer 热网络模型的瞬态热阻抗。结温估算误差每升高 1°C，器件可靠性约降低 2%/°C。

### 层次二：变换器拓扑层

**详细开关模型（DSM）** 对每个开关器件独立建模，精度最高，支持器件级损耗分析，适用于小系统或关键时段的精细仿真。

**平均值模型（AVM）** 对开关周期进行平均化处理，用占空比 $d(t)$ 调制直流侧电压：

$$
\bar{v}_{out}(t) = d(t) \cdot V_{dc}
$$

适用条件：开关频率 $f_{sw} \gg f_{fund}$（通常 $f_{sw} > 10 f_{fund}$）。计算效率比 DSM 高 1–2 个数量级，但丢失所有开关纹波。

**详细等效模型（DEM）** 将子模块电容和开关状态进行戴维南等效聚合：

$$
v_{arm}^{eq} = \sum_{j=1}^{N} s_j \cdot v_{C_j}, \quad R_{arm}^{eq} = \sum_{j=1}^{N} R_{eq}
$$

MMC 子模块数 $N \geq 100$ 时，DEM 使仿真规模从百级扩展至千级，加速比可达 50:1（[2015]）。

### 层次三：开关事件处理层

**变导纳方法**：开关动作触发导纳矩阵重构，计算精度高但每次开关都需要重新分解矩阵：

$$
Y_n(t) = Y_{fixed} + \sum_{sw} y_{sw}(t)
$$

**恒导纳方法（ADC / Fixed-Admittance）**：导纳矩阵恒定，用历史电流源 $i_{hist}$ 补偿开关非线性，计算效率高，适合实时仿真：

$$
i_k = Y_{fix} \cdot v_k + i_{hist}(s_k)
$$

ADC 方法以微秒级步长（1–10 μs）实现实时仿真，精度损失 < 5%（[2018]）。

**插值与精确开关时刻处理（Na et al. 2023）**：利用半步长 Backward Euler（BE）解提高插值精度。传统插值法在开关时刻 $t_{sw}$ 使用状态变量更新前的值计算，产生虚假开关振荡；半步长 BE 方法的电压值：

$$
V(t) = Y_{old} [I_{source}(t) + I_{history}(t - \Delta t)]
$$

在开关时刻更接近真实值，消除了虚假开关损耗（spurious switching losses），精度提升约 20%。

开关时刻检测（线性插值）：

$$
t_{sw} = t_n + \frac{v_{th} - v_n}{v_{n+1} - v_n} \Delta t
$$

### 层次四：多电平变换器层

**半桥子模块（HBSM）**：

$$
v_{SM} = s_{up} \cdot v_C, \quad i_{SM} = (s_{up} - s_{low}) \cdot i_{arm}
$$

电容电压更新（梯形积分）：

$$
v_C(t + \Delta t) = v_C(t) + \frac{\Delta t}{2C_{SM}} [i_C(t) + i_C(t + \Delta t)]
$$

**桥臂戴维南等效**：

$$
R_{eq} = \frac{\Delta t}{2C_{SM}}, \quad v_{th} = v_C(t) + R_{eq} \cdot i_C(t)
$$

桥臂聚合：

$$
R_{arm}^{eq} = N \cdot R_{eq}, \quad v_{arm}^{th} = \sum_{j=1}^{N} v_{th,j}
$$

## 形式化表达

### 器件级参数体系

| 参数类别 | 参数名称 | 典型值/范围 | 单位 | 备注 |
|---------|---------|------------|------|------|
| **IGBT** | 额定电压 | 600–6500 | V | 取决于应用 |
| | 额定电流 | 10–3600 | A | 芯片面积相关 |
| | 导通压降 | 1.5–3.0 | V | $V_{CE(sat)}$ |
| | 开关时间 | 0.1–2.0 | μs | 开通+关断合计 |
| | 拖尾时间 | 0.2–1.0 | μs | 关断拖尾电流 |
| **SiC MOSFET** | 额定电压 | 600–1700 | V | 高压应用 |
| | 导通电阻 | 10–100 | mΩ | 随温度正相关 |
| | 开关时间 | 20–100 | ns | 比 IGBT 快 10 倍 |
| **二极管** | 反向恢复时间 | 20–500 | ns | 快恢复二极管 |
| | 正向压降 | 0.7–2.0 | V | 取决于类型 |

### 仿真步长选择

| 应用场景 | 推荐模型 | 步长建议 | 关键考量 |
|---------|---------|---------|---------|
| 系统级分析 | AVM / 恒导纳 | 20–50 μs | 效率优先 |
| 直流故障分析 | DEM | 10–20 μs | 闭锁准确捕捉 |
| 开关损耗评估 | 详细器件 | 0.1–1 μs | 精确捕捉 |
| 实时 HIL 测试 | ADC | 1–10 μs | 确定性延迟 |
| 热设计验证 | 热-电耦合 | 1–10 ms | 热时间常数 |

## 量化性能边界

### 精度-效率权衡曲线

| 建模方法 | 精度 | 效率 | 适用规模 |
|---------|------|------|---------|
| 详细开关模型（DSM） | ★★★★★ | ★☆☆☆☆ | ≤ 10 节点 |
| 详细等效模型（DEM） | ★★★★☆ | ★★★☆☆ | 百级子模块 |
| 平均值模型（AVM） | ★★★☆☆ | ★★★★☆ | 系统级 |
| 恒导纳（ADC） | ★★★☆☆ | ★★★★★ | 实时仿真 |

### 代表性量化数据

- **[2015]** DEM 模型使 MMC 仿真规模从 100 子模块扩展至 5000+，加速比 50:1
- **[2018]** ADC 方法实现微秒级步长实时仿真，精度损失 < 5%
- **[2019]** FPGA 实现 MMC 详细模型，542 节点系统 10 μs 步长实时仿真
- **[2021]** 详细 IGBT 模型预测开关损耗误差 < 3%，但计算量增加 100 倍
- **[2022]** 单芯片 FPGA 实现 VSC-HVDC 全系统实时仿真
- **[2023]** Na et al. 半步长 BE 插值精度提升 20%，消除虚假开关损耗

## 关键技术挑战

### 挑战一：宽禁带半导体（WBG）高频建模
SiC/GaN 器件开关频率 > 100 kHz，传统的 μs 级 EMT 步长无法捕捉开关瞬态过程。寄生参数（寄生电感 $L_s$、电容 $C_{oss}$）的提取与建模是核心难题；EMI/EMC 联合仿真需要宽带器件模型（DC–100 MHz）。

### 挑战二：开关事件数值不连续性
开关状态变化导致节点方程系数矩阵突变，Trapezoidal 积分法在此产生数值振荡（numerical oscillation）。常用抑制方法：① CDA（Critical Damping Adjustment）——在开关时刻将梯形积分切换为 Backward Euler；② 插值法（Interpolation）——精确检测开关时刻并回溯计算；③ 状态切换法（State transition）——在开关点前后使用不同积分方法。

### 挑战三：热-电-机械多物理场耦合
功率模块的电磁损耗产生热量，热导致器件参数变化（导通电阻正温度系数），机械应力影响焊层可靠性。三场联合仿真计算代价高，实时应用困难。结温监测的在线估算误差需 < 2°C 才能支持可靠性预警。

### 挑战四：实时仿真计算确定性
硬件在环（HIL）测试要求仿真步长恒定、延迟可控。ADC 方法是主流，但补偿源 $i_{hist}$ 的计算精度影响等效性；千级子模块 MMC 的实时化仍依赖 FPGA 或多核 CPU 的精细分区。

## 适用边界与选择指南

- **理想开关模型**：适合系统级大规模仿真（> 1000 节点），但不适用于开关损耗和器件应力分析
- **IGBT 详细物理模型**：适合保护配合和可靠性评估，计算成本高（相对 AVM 增加 100 倍）
- **平均值模型**：适合控制策略验证，频率必须满足 $f_{sw} > 10 f_{fund}$ 的平均化条件
- **恒导纳方法（ADC）**：适合实时 HIL 测试，需验证虚拟损耗是否在可接受范围（< 5%）
- **详细等效模型（DEM）**：适合大规模 MMC（子模块数 > 100），千级子模块时加速比 50:1
- **热-电耦合模型**：适合功率模块热设计和结温在线监测，支持可靠性评估

## 技术演进脉络

### 1990s–2000s：基础开关模型
- **理想开关**：二值电阻模型成为 EMT 标准
- **CDA 技术**：解决开关虚假振荡问题
- **EMTP 标准**：经典开关处理流程建立（Anderson 1969，WEPRI）

### 2000s–2010s：详细器件建模
- **IGBT 物理模型**：考虑拖尾电流和米勒效应
- **热-电耦合**：功率模块热阻抗网络建模
- **宽带隙器件**：SiC/GaN 器件高频建模需求出现

### 2010s–2020s：高效聚合方法
- **DEM 模型**：MMC 详细等效，支持千级子模块
- **ADC 方法**：恒导纳实现实时仿真
- **多速率技术**：开关细节与系统动态解耦

### 2020s–2026：智能化与多物理场
- **AI 辅助建模**：神经网络逼近开关行为，加速详细模型
- **多物理场耦合**：电磁-热-机械-流体联合仿真
- **数字孪生**：在线参数更新与故障预警

## 相关方法

- [[switch-modeling]] — 开关器件建模核心技术
- [[average-value-model]] — 变换器平均化方法
- [[fixed-admittance]] — ADC 恒导纳实时仿真
- [[numerical-integration-methods]] — 开关离散化数值积分方法
- [[multirate-method]] — 开关与系统多速率解耦

## 相关模型

- [[igbt-model]] — 绝缘栅双极晶体管详细模型
- [[diode-model]] — 功率二极管模型
- [[mmc-model]] — 模块化多电平换流器
- [[vsc-model]] — 电压源换流器
- [[converter-transformer-model]] — 电力电子变压器

## 相关主题

- [[vsc-hvdc]] — 柔性直流输电
- [[real-time-simulation]] — 电力电子实时测试
- [[co-simulation]] — 多求解器协同仿真
- [[harmonic-analysis]] — 电力电子谐波分析

---

## 来源论文

> 注：以下论文以 PDF 文件名记录，未必与 wiki/sources/ 中的页面一一对应。实际引用时请以论文标题和年份为准。

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| Na et al. — Improved High-Accuracy Interpolation for Switching Devices in EMT | 2023 | 半步长 BE 插值，消除虚假开关损耗 |
| Nzale et al. — Accurate Time-Domain Simulation of Power Electronic Circuits | 2021 | 开关数值振荡抑制方法 |
| 电力系统电磁暂态仿真 IGBT 详细建模及应用 | 2019 | 中文 IGBT 详细建模工程实践 |
| Comparison of ATP-EMTP and NETOMAC Programs | 2004 | EMTP 电力电子仿真对比 |
| Accelerated Sparse Matrix Computation for EMT | 2019 | 电力电子系统稀疏矩阵加速 |
| GPU-Based Power Converter Transient Simulation | 2020 | GPU 加速变换器仿真 |
| Harmonic-Preserved Average-Value Model for Converters in EMT | 2026 | 谐波保持型 AVM |
| A Bridge-Arm-Module-Based Fixed-Admittance ADC Model | 2025 | MMC 桥臂 ADC 模型 |
| Numerically Efficient Average-Value Model for VSC | 2024 | 高效 AVM 数值方法 |
| An Improved High-Accuracy Interpolation Method for Switching Devices | 2023 | 插值精度提升（与上述 Na 2023 同一篇） |
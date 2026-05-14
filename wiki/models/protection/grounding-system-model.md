---
title: "接地系统 (Grounding System)"
type: model
tags: [grounding, earthing, soil, frequency-dependent, step-voltage, touch-voltage]
created: "2026-04-29"
updated: "2026-05-12"
---

# 接地系统 (Grounding System)




## 定义与概述

接地系统是电力系统安全运行的重要保障，提供故障电流通路、限制过电压、保障人身和设备安全。接地系统模型需要考虑土壤电阻率、接地极几何形状、频变特性等因素。本模型涵盖均匀土壤和分层土壤模型、接地电阻计算、跨步电压和接触电压分析、频变接地阻抗，适用于变电站接地网设计和雷电过电压分析。

## 1. 物理对象概述

### 1.1 功能与作用

接地系统是电力系统安全运行的重要保障：

**核心功能**：
- **故障电流疏散**：提供低阻抗路径，快速清除故障
- **过电压保护**：限制雷电和操作过电压
- **人身安全**：限制接触电压和跨步电压
- **设备保护**：提供等电位连接，防止地电位升高损坏设备
- **参考电位**：为控制和测量系统提供零电位参考

### 1.2 接地类型

| 类型 | 定义 | 应用场景 |
|------|------|---------|
| **工作接地** | 系统中性点接地 | 变压器中性点、发电机中性点 |
| **保护接地** | 设备外壳接地 | 开关柜、变压器外壳、杆塔 |
| **防雷接地** | 避雷针/线接地 | 变电站、线路杆塔 |
| **信号接地** | 弱电系统接地 | 通信、控制、测量系统 |

### 1.3 接地装置类型

**自然接地体**：
- 金属管道（水管、油管）
- 电缆金属外皮
- 建筑物钢筋

**人工接地体**：
- **垂直接地极**：钢管/角钢/铜棒，长度2.5-3m
- **水平接地极**：扁钢/圆钢，埋深0.6-0.8m
- **接地网**：变电站主接地网，网格5-10m
- **放射形接地**：线路杆塔，3-8根放射线

## 2. 物理模型与数学描述

### 2.1 接地电阻

**垂直接地极**（均匀土壤）：
$$
R = \frac{\rho}{2\pi L}\ln\frac{4L}{d}$$

**水平接地极**：
$$
R = \frac{\rho}{2\pi L}\ln\frac{L^2}{hd}$$

**接地网**：
$$
R = \frac{\rho}{4}\sqrt{\frac{\pi}{A}} + \frac{\rho}{L_{total}}$$

其中，$\rho$为土壤电阻率，$L$为接地极长度，$d$为等效直径，$h$为埋深，$A$为接地网面积。

### 2.2 跨步电压和接触电压

**跨步电压**（两脚间）：
$$
E_{step} = \frac{\rho I}{2\pi}\left(\frac{1}{x} - \frac{1}{x+s}\right)$$

**接触电压**（手脚间）：
$$
E_{touch} = \frac{\rho I}{2\pi}\left(\frac{1}{2x} + \frac{1}{D}\right)$$

其中，$s = 1m$为步距，$D$为接地网等效直径。

**安全限值**（IEEE 80）：
- 跨步电压：$E_{step} \leq \frac{116 + 0.7\rho_s}{\sqrt{t}}$
- 接触电压：$E_{touch} \leq \frac{116 + 1.5\rho_s}{\sqrt{t}}$

## 3. 频变特性

**接地阻抗频变**：
- 高频时：集肤效应显著，有效截面积减小
- 土壤频变：土壤介电常数和电导率随频率变化
- 接地阻抗：$Z_g(f) = R_g + j\omega L_g$

**时域模型**：
通过矢量拟合建立有理函数模型：
$$
Z_g(s) = R_0 + \sum_{k=1}^{N}\frac{R_k}{s - p_k}$$

## 4. 适用边界

**适用场景**：
- 变电站接地网设计
- 线路杆塔接地
- 雷电过电压分析
- 故障电流分布计算
- 人身安全评估

**模型限制**：
- 土壤均匀性假设
- 忽略化学腐蚀影响
- 季节性变化
- 接地极间互耦

## 量化性能边界

**接地电阻典型范围**（IEEE 80，均匀土壤假设）：
- 变电站接地网：0.1-5 Ω（ρ = 10-500 Ω·m，A = 100×100 m²）
- 输电线路杆塔：10-50 Ω（ρ = 100-1000 Ω·m，L = 30-50 m 放射线）
- 垂直接地极（L = 2.5 m）：R ≈ ρ/(2πL)·ln(4L/d) = 0.3ρ 至 0.4ρ（单位Ω）
- 水平接地极（L = 30 m，h = 0.8 m）：R ≈ 0.05ρ 至 0.1ρ

**安全限值**（IEEE Std 80，50/60 Hz）：
- 跨步电压：E_step ≤ (116 + 0.7ρ_s)/√t（V），ρ_s 为表层土壤电阻率
- 接触电压：E_touch ≤ (116 + 1.5ρ_s)/√t（V），t 为故障持续时间（s）
- 典型允许跨步电压范围：200-2000 V（t = 0.5 s，ρ_s = 100-5000 Ω·m）

**频变接地阻抗**：
- 工频（50/60 Hz）：Z_g ≈ R_g，感性分量可忽略
- 雷电流频率范围（10 kHz-1 MHz）：Z_g可升至直流电阻的 2-10 倍，受集肤效应和土壤频变影响
- 矢量拟合阶数 N = 4-8 可实现误差 < 2% 的宽频接地阻抗拟合（Alipio 2020）
- 土壤频变参数（ρ(f)、ε_r(f)）在 f > 1 MHz 时显著降低接地阻抗幅值，不可忽略

**EMT仿真步长**：
- 工频接地分析：步长 50-100 μs
- 雷电暂态接地：步长 0.01-0.1 μs（需考虑波过程）
- 频变接地等效电路实现：步长 1-10 μs（矢量拟合有理函数转换）

**数据缺口声明**：不同土壤类型（黏土/砂土/岩石/冻土）和不同季节（干/湿/冻结）下接地电阻的系统测量数据缺乏统一公开数据库。频变土壤参数的实验验证数据主要集中在 1 MHz 以下，更高频段的接地响应数据不足。大型接地网的多端口频变等值模型在大规模 EMT 仿真中的计算效率（内存/CPU）缺乏系统对比。

## 相关方法
- [[vector-fitting|矢量拟合]] - 接地阻抗频变拟合
- [[nodal-analysis|节点分析]] - 接地网节点分析
- [[state-space-method|状态空间法]] - 频变接地状态实现
- [[frequency-dependent-modeling|频率相关建模]] - 宽频接地建模
- [[numerical-integration|数值积分]] - 雷电响应仿真

## 相关模型
- [[cable-model|电缆模型]] - 电缆金属护套接地
- [[transformer-model|变压器模型]] - 变压器中性点接地
- [[transmission-line-model|输电线路模型]] - 杆塔接地
- [[surge-arrester-model|避雷器]] - 防雷接地

## 相关主题
- [[frequency-dependent-modeling]] - 频变接地建模
- [[harmonic-analysis]] - 接地谐波阻抗
- [[real-time-simulation]] - 接地系统实时仿真
- [[network-equivalent]] - 接地网等值

## 来源论文

| 论文 | 年份 |
|------|------|
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe|Extension of a modal-domain transmission line model for incl]] | 2016 |
| [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o|Influence of frequency characteristics of soil on lightning ]] | 2016 |
| [[an-improved-approach-for-modeling-lightning-transients-of-wind-turbines|An improved approach for modeling lightning transients of wi]] | 2018 |
| [[electromagnetic-disturbances-in-gas-insulated-substations-and-vft-calculations|Electromagnetic disturbances in gas-insulated substations an]] | 2018 |
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[an-electromagnetic-model-for-the-calculation-of-tower-surge-impedance-based-on-t|An Electromagnetic Model for the Calculation of Tower Surge ]] | 2020 |
| [[an-electromagnetic-model-for-the-calculation-of-tower-surge-impedance-based-on-t|An Electromagnetic Model for the Calculation of Tower Surge ]] | 2020 |
| [[an-electromagnetic-model-for-the-calculation-of-tower-surge-impedance-based-on-t|An Electromagnetic Model for the Calculation of Tower Surge ]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[ground-potential-rise-in-wind-farms-due-to-direct-lightning|Ground Potential Rise in Wind Farms due to Direct Lightning]] | 2021 |
| [[ground-potential-rise-in-wind-farms-due-to-direct-lightning|Ground Potential Rise in Wind Farms due to Direct Lightning]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient|Comparison of soil modeling concerning physical factors: App]] | 2023 |
| [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient|Comparison of soil modeling concerning physical factors: App]] | 2023 |
| [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient|Comparison of soil modeling concerning physical factors: App]] | 2023 |
| [[electrical-power-and-energy-systems-148-2023-108967|Electrical Power and Energy Systems 148 (2023) 108967]] | 2023 |
| [[electrical-power-and-energy-systems-148-2023-108967|Electrical Power and Energy Systems 148 (2023) 108967]] | 2023 |
| [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-|Calculation of lightning-induced voltages on a large-scale d]] | 2025 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
## EMT中的作用

接地系统 (Grounding System) 在EMT仿真中主要用于：

- **建模对象**：描述接地系统 (Grounding System)在电力系统中的物理角色和电气特性
- **仿真场景**：适用于接地系统 (Grounding System)相关的电磁暂态分析、故障响应、控制交互等场景
- **模型接口**：提供接地系统 (Grounding System)的端口变量、状态方程和边界条件
- **验证基准**：可作为接地系统 (Grounding System)仿真模型正确性的验证基准

## 数学模型

### 基本方程

接地系统 (Grounding System)的数学模型基于以下基本物理定律：

$$
\text{待补充：基于接地系统 (Grounding System)的物理特性建立数学描述}
$$

### 状态空间表示

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})
$$

$$
\mathbf{y} = \mathbf{g}(\mathbf{x}, \mathbf{u})
$$

其中 $\mathbf{x}$ 为状态向量，$\mathbf{u}$ 为输入向量，$\mathbf{y}$ 为输出向量。


*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
---
title: "避雷器 (Surge Arrester)"
type: model
tags: [surge-arrester, zno, metal-oxide, overvoltage-protection, lightning]
created: "2026-04-29"
updated: "2026-05-12"
---

# 避雷器 (Surge Arrester)




## 定义与概述

避雷器是限制过电压、保护电气设备的关键保护装置，通过非线性电阻特性在过电压时导通泄放能量，过电压消失后恢复高阻态。金属氧化物避雷器（MOV/ZnO）是现代电力系统的主流类型，具有优异的非线性特性和快速响应能力。本模型涵盖指数模型、分段线性模型、IEEE模型、热模型，适用于雷电过电压保护和绝缘配合分析。

## 1. 物理对象概述

### 1.1 功能与作用

避雷器是限制过电压、保护电气设备的关键保护装置：

**核心功能**：
- **雷电过电压保护**：泄放雷电流，限制设备端过电压
- **操作过电压保护**：限制开关操作产生的过电压
- **工频续流阻断**：过电压消失后切断工频续流
- **绝缘配合**：与被保护设备绝缘水平配合

**保护原理**：
当过电压超过避雷器动作电压时，避雷器从高阻态变为低阻态，将过电压能量泄放入地；过电压消失后，避雷器恢复高阻态，阻断工频续流。

### 1.2 结构类型

#### 1.2.1 金属氧化物避雷器 (MOV/ZnO)

**结构组成**：
- **ZnO阀片**：非线性电阻主体
- **绝缘外套**：硅橡胶/瓷套
- **金属端子**：接线端子
- **压力释放装置**：故障时安全泄压

**特性优势**（对比碳化硅SiC）：
- 无间隙设计（简化结构）
- 优异的非线性（α>30）
- 快速响应（ns级）
- 无续流（阻断工频电流）

#### 1.2.2 带间隙避雷器

**类型**：
- 管式避雷器（排气式）
- 阀式避雷器（SiC+间隙）
- 串联间隙MOV（用于特高压）

### 1.3 运行激励

**过电压类型**：
| 类型 | 幅值 | 波形 | 频率 |
|------|------|------|------|
| 直击雷 | 100-300kV | 1.2/50μs | - |
| 感应雷 | 50-150kV | 1.2/50μs | - |
| 操作过电压 | 2-4 p.u. | 100-1000μs | - |
| 工频过电压 | 1.3-1.5 p.u. | 持续 | 50Hz |

**电流范围**：
- 泄漏电流（正常运行）：< 1mA
- 标称放电电流：5-20kA
- 最大放电电流：65-200kA

## 2. 物理模型与数学描述

### 2.1 非线性V-I特性

#### 2.1.1 指数模型

$$I = k \cdot V^\alpha$$

其中：
- $k$：材料常数
- $\alpha$：非线性系数（ZnO: 30-50，SiC: 3-5）

#### 2.1.2 分段线性模型

**小电流区**（泄漏区）：
$$I = G_{leak} \cdot V, \quad I < 1mA$$

**中电流区**（工作区）：
$$I = I_{ref} \left(\frac{V}{V_{ref}}\right)^\alpha$$

**大电流区**（饱和区）：
$$V = V_{sat} + I \cdot R_{res}, \quad I > 10kA$$

#### 2.1.3 IEEE模型

$$\frac{V}{V_{ref}} = C_1 \left(\frac{I}{I_{ref}}\right)^{1/\alpha_1} + C_2 \left(\frac{I}{I_{ref}}\right)^{1/\alpha_2}$$

典型参数：
- $C_1 = 0.9, C_2 = 0.1$
- $\alpha_1 = 35, \alpha_2 = 15$

### 2.2 动态特性

#### 2.2.1 响应时间

**响应过程**：
1. 延迟时间：~1ns（电子响应）
2. 上升时间：~10ns（建立导电通道）
3. 峰值时间：~50ns

**动态模型**：
$$V(t) = V_{static}(I(t)) + L_{eq} \frac{dI}{dt}$$

其中$L_{eq}$为等效电感（引线+阀片分布电感），典型值0.1-1μH。

#### 2.2.2 多柱并联模型

大型避雷器多柱并联：
$$I_{total} = \sum_{i=1}^{N} I_i(V), \quad V = V(I_{total})$$

**电流分布不均**：
由于阀片参数分散性，电流分布不均匀系数：$K_{dis} = 1.05 - 1.15$

### 2.3 热模型

**能量吸收**：
$$E_{abs} = \int_0^T V(t) \cdot I(t) dt$$

**温升方程**：
$$C_{th} \frac{dT}{dt} = P_{loss} - \frac{T - T_{amb}}{R_{th}}$$

其中：
- $C_{th}$：热容
- $R_{th}$：热阻
- $P_{loss} = V \cdot I$

**热崩溃**：
当$P_{loss} > P_{diss}$时，温度持续上升导致热崩溃。

## 3. EMT仿真模型

### 3.1 静态非线性电阻模型

**指数电阻模型**：
$$R(V) = R_0 \cdot \left(\frac{V}{V_{ref}}\right)^{-\alpha}$$

**电流控制型**：
$$V(I) = V_{ref} \left(\frac{I}{I_{ref}}\right)^{1/\alpha}$$

**实现方式**（EMTP）：
```
NONLINEAR_RESISTOR
- Type: Exponential
- Vref: 1kV
- Iref: 1A
- Alpha: 35
- Vmin: 0.1kV
- Vmax: 100kV
```

### 3.2 分段线性模型

**多段线性近似**：

| 段 | 电压范围 | 电流范围 | 电阻 |
|---|---------|---------|------|
| 1 | 0-0.9Vref | 0-1mA | 900MΩ |
| 2 | 0.9-1.1Vref | 1mA-1A | 200Ω |
| 3 | 1.1-2.0Vref | 1A-10kA | 0.1Ω |
| 4 | >2.0Vref | >10kA | 0.01Ω |

### 3.3 频率相关模型

考虑高频响应的等效电路：

```
        L_lead
    ━━━━/\/\/━━━━┳━━━━/\/\/━━━━┓
                ┃            ┫
              ┌─┴─┐          ═ C_par
              │R(V)│          ┫
              └───┘          ┻━━━━┛
```

**参数典型值**：
- $L_{lead}$：引线电感，0.1-1μH
- $C_{par}$：寄生电容，10-100pF

## 4. 典型参数

### 4.1 ZnO避雷器参数（110kV系统）

| 参数 | 数值 | 单位 |
|------|------|------|
| 系统电压 | 110 | kV |
| 额定电压 | 102 | kVrms |
| 持续运行电压 | 81.6 | kVrms |
| 参考电压 | 148 | kVdc |
| 1mA直流电压 | 148 | kVdc |
| 标称放电电流 | 10 | kA |
| 残压(8/20μs, 10kA) | 266 | kV |
| 保护水平 | 2.36 | p.u. |
| 荷电率 | 0.55 | - |

**残压比**：
- 10kA残压/1mA电压 ≈ 1.8-2.0

### 4.2 保护配合

**绝缘配合原则**：
$$BIL_{equipment} \geq 1.2 \times V_{residual,max}$$

**保护距离**：
$$L_{max} = \frac{BIL - V_{res}}{2S}$$

其中$S$为雷电波陡度（kV/μs）。

### 4.3 模型选择

| 研究类型 | 推荐模型 | 说明 |
|---------|---------|------|
| 雷电过电压 | 分段线性+电感 | 考虑引线电感 |
| 操作过电压 | 指数模型 | 中等电流区 |
| 绝缘配合 | 残压-电流曲线 | 稳态分析 |
| 多雷击 | 热模型 | 能量累积 |

### 4.4 适用边界与限制

#### 4.4.1 适用条件
- **电压等级**：10kV-1000kV系统
- **电流范围**：1mA泄漏至200kA雷电流
- **温度范围**：-40°C至+40°C（环境温度）
- **海拔高度**：<2000m（高海拔需修正）

#### 4.4.2 模型限制
- **老化效应**：长期运行老化未考虑
- **污秽影响**：表面污秽闪络未建模
- **多柱并联**：电流分布不均简化
- **热崩溃**：动态热过程简化

## 量化性能边界

**非线性V-I特性**（ZnO避雷器）：
- 非线性系数 α = 30-50（ZnO），远高于 SiC（α = 3-5）
- 泄漏电流（正常工作电压下）：< 1 mA
- 1 mA 参考电压与额定电压之比：约 1.4-1.6（110 kV 系统典型值 148 kVdc / 102 kVrms）
- 残压比（10 kA 残压/1 mA 电压）：1.8-2.0

**响应时间**：
- ZnO 阀片电子响应：< 1 ns
- 导电通道建立：约 10 ns
- 完整电压钳位响应：约 50 ns
- 引线电感影响（L_lead = 0.1-1 μH）：di/dt 每 1 kA/μs 产生 0.1-1 kV 附加压降

**能量吸收能力**：
- 单柱 ZnO 阀片比能量：2-8 kJ/kV（额定电压），具体取决于阀片尺寸和配方
- 多柱并联不均流系数：K_dis = 1.05-1.15
- 热崩溃临界温度：约 120-150°C（超过后 Zno 阀片非线性特性退化）
- 110 kV 避雷器典型热容：C_th ≈ 500-2000 J/K，热阻 R_th ≈ 0.5-2.0 K/W

**保护配合参数**（IEEE/ IEC 60099）：
- 绝缘配合原则：设备 BIL ≥ 1.2 × 残压（标称放电电流下）
- 最大保护距离取决于雷电波陡度 S（kV/μs）：L_max = (BIL - V_res)/(2S)
- 标称放电电流：5-20 kA（10 kA 为 110 kV 以上系统标准值）
- 最大放电电流：65-200 kA（取决于避雷器等级）

**EMT建模精度**：
- 指数模型（单 α）：在 10^-6 至 10^4 A 范围内误差约 ±5%
- 分段线性模型（4-5 段）：误差约 ±3%，适用于保护配合
- 双指数模型（IEEE：C1 = 0.9/α1 = 35，C2 = 0.1/α2 = 15）：在大电流区精度优于单指数
- 频变模型（含 L_lead 和 C_par）：需步长 < 0.1 μs 以捕获高频响应

**数据缺口声明**：不同厂家 ZnO 阀片的实际 V-I 特性曲线存在制造分散性，模型中使用的等效参数（α、C1、C2、R_lead）与实际产品的系统比对数据不足。避雷器老化对 EMT 模型参数（泄漏电流增大、残压升高）的定量影响缺乏长期实验数据积累。高频（> 1 MHz）下的寄生参数模型（L_distributed、C_inter-wafer）验证数据不足。

## 相关方法
- [[vector-fitting|矢量拟合]] - 频变特性有理函数拟合
- [[frequency-dependent-modeling|频率相关建模]] - 高频响应建模
- [[numerical-integration|数值积分]] - 热模型计算
- [[state-space-method|状态空间法]] - 避雷器状态建模
- [[passivity-enforcement|无源性强制]] - 频变模型无源性

## 相关模型
- [[transmission-line-model|输电线路模型]] - 线路雷电入侵波
- [[transformer-model|变压器模型]] - 变压器绝缘配合
- [[circuit-breaker-model|断路器模型]] - 操作过电压配合
- [[grounding-system-model|接地系统模型]] - 接地网设计
- [[cable-model|电缆模型]] - 电缆过电压保护

## 相关主题
- [[frequency-dependent-modeling]] - 频变建模应用
- [[harmonic-analysis]] - 谐波与避雷器配合
- [[real-time-simulation]] - 避雷器实时仿真
- [[network-equivalent]] - 网络等值与保护


---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on|EMTP Modeling Of Electromagnetic Transients - Power Delivery]] | 2004 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea|Modeling a voltage source converter assisted resonant curren]] | 2019 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co|Analysis of low frequency interactions of DFIG wind turbine ]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth-19、20、21|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat|Modelica-based simulation of electromagnetic transients usin]] | 2021 |
| [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-|A Thévenin-Type Version of the Extended Modal-Domain Model f]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-|Calculation of lightning-induced voltages on a large-scale d]] | 2025 |

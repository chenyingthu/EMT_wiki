---
title: "电池储能系统 (BESS)"
type: model
tags: [bess, battery, energy-storage, lithium-ion, bms, pcs]
created: "2026-04-29"
---

# 电池储能系统 (Battery Energy Storage System, BESS)


```mermaid
graph TD
    subgraph Ncmp[电池储能系统 (BESS)]
        N0[**磷酸铁锂(LFP)**: 130-160 Wh/kg]
        N1[**三元锂(NCM)**: 200-250 Wh/kg]
        N2[**钛酸锂(LTO)**: 70-80 Wh/kg]
        N3[**钠离子**: 100-150 Wh/kg]
        N4[**液流电池**: 20-40 Wh/kg]
    end
```


## 定义与概述

电池储能系统（BESS）是将电能以化学能形式存储并在需要时释放的电力系统设备，通过电池管理系统（BMS）和储能变流器（PCS）实现充放电控制。作为电力系统重要的灵活性资源，BESS在削峰填谷、频率调节、可再生能源平滑和备用电源等方面发挥关键作用。本模型涵盖电化学电池等效电路模型、SOC估计、热模型、PCS变流器控制，适用于电网侧储能、用户侧储能和新能源配套储能的EMT仿真分析。

## 1. 物理对象概述

### 1.1 功能与结构

电池储能系统是电力系统重要的灵活性资源，主要功能：

**核心功能**：
- **削峰填谷**：负荷低谷充电，高峰放电
- **频率调节**：快速响应频率偏差（AGC）
- **可再生能源平滑**：平抑风电/光伏波动
- **备用电源**：提供紧急功率支撑
- **电能质量改善**：抑制电压闪变、谐波

**系统组成**：
```
AC Grid ←→ 变压器 ←→ PCS ←→ DC Bus ←→ BMS ←→ Battery Pack
                            ↕
                         HVAC (温控)
```

- **电池簇 (Battery Cluster)**：多节电池串并联
- **BMS (电池管理系统)**：SOC估计、均衡控制、保护
- **PCS (储能变流器)**：AC/DC双向变换
- **温控系统**：维持电池工作温度（15-25°C）

### 1.2 电池技术类型

| 技术 | 能量密度 | 循环寿命 | 响应速度 | 应用场景 |
|------|---------|---------|---------|---------|
| **磷酸铁锂(LFP)** | 130-160 Wh/kg | 3000-6000次 | <100ms | 电网储能 |
| **三元锂(NCM)** | 200-250 Wh/kg | 1000-2000次 | <100ms | 电动汽车 |
| **钛酸锂(LTO)** | 70-80 Wh/kg | 15000+次 | <10ms | 调频 |
| **钠离子** | 100-150 Wh/kg | 2000-4000次 | <100ms | 成本敏感 |
| **液流电池** | 20-40 Wh/kg | 10000+次 | <1s | 长时储能 |

### 1.3 运行激励

**电气激励**：
- 电压：500-1500V（大型储能）
- 电流：充放电倍率C-rate（0.5C-3C）
- 功率：MW级（电网侧）至kW级（用户侧）

**控制激励**：
- 调度指令：AGC信号、计划曲线
- 本地控制：频率/电压下垂响应
- 保护动作：过压、欠压、过温保护

## 2. 物理模型与数学描述

### 2.1 等效电路模型

#### 2.1.1 Thevenin模型

等效电路：开路电压串联电阻和RC网络

$$V_{bat} = V_{oc}(SOC) - I_{bat} R_0 - V_{RC1} - V_{RC2}$$

**RC网络动态**：
$$\tau_1 \frac{dV_{RC1}}{dt} + V_{RC1} = I_{bat} R_1$$
$$\tau_2 \frac{dV_{RC2}}{dt} + V_{RC2} = I_{bat} R_2$$

其中：
- $V_{oc}(SOC)$：开路电压（SOC函数）
- $R_0$：欧姆内阻
- $R_1, C_1$：电化学极化
- $R_2, C_2$：浓差极化

#### 2.1.2 二阶RC模型

状态空间形式：
$$\frac{d}{dt} \begin{bmatrix} V_{RC1} \\ V_{RC2} \\ SOC \end{bmatrix} =
\begin{bmatrix} -1/\tau_1 & 0 & 0 \\ 0 & -1/\tau_2 & 0 \\ 0 & 0 & 0 \end{bmatrix}
\begin{bmatrix} V_{RC1} \\ V_{RC2} \\ SOC \end{bmatrix} +
\begin{bmatrix} 1/C_1 \\ 1/C_2 \\ -\eta/Q_{nom} \end{bmatrix} I_{bat}$$

**输出方程**：
$$V_{bat} = V_{oc}(SOC) - I_{bat} R_0 - V_{RC1} - V_{RC2}$$

### 2.2 SOC估计

#### 2.2.1 Coulomb计数法

$$SOC(t) = SOC_0 - \frac{1}{Q_{nom}} \int_0^t \eta \cdot I_{bat}(\tau) d\tau$$

其中：
- $Q_{nom}$：额定容量（Ah）
- $\eta$：库仑效率（充电<1，放电=1）

#### 2.2.2 开路电压法

$$SOC = f^{-1}(V_{oc})$$

典型LFP电池OCV-SOC关系：
| SOC | 0% | 20% | 50% | 80% | 100% |
|-----|-----|-----|-----|-----|------|
| V_oc(V) | 2.5 | 3.25 | 3.3 | 3.32 | 3.6 |

**特点**：LFP平台区（30%-80% SOC）电压变化小，难以准确估计

### 2.3 热模型

**能量平衡方程**：
$$C_{th} \frac{dT}{dt} = Q_{gen} - Q_{loss}$$

**生热功率**：
$$Q_{gen} = I_{bat}^2 R_0 + I_{bat}^2 R_1 + I_{bat}^2 R_2 + I_{bat} T \frac{dV_{oc}}{dT}$$

**散热功率**：
$$Q_{loss} = h A (T - T_{amb})$$

## 3. EMT仿真模型

### 3.1 电池详细模型

**二阶RC模型实现**：
- 时变电感/电阻元件
- 考虑温度依赖参数
- 老化模型（容量衰减、内阻增加）

**老化模型**：
$$Q_{aging} = Q_0 \cdot (1 - \alpha \cdot N_{cycle}^\beta \cdot e^{-E_a/(RT)})$$

### 3.2 PCS变流器模型

**两电平VSC**：
- 双向AC/DC变换
- PWM调制（载波频率2-8kHz）
- LCL滤波器

**控制策略**：

**PQ控制模式**：
- $P_{ref}$：有功功率指令（充电/放电）
- $Q_{ref}$：无功功率指令（电压支撑）

**下垂控制模式**：
$$P = P_0 - k_f (f - f_0)$$
$$Q = Q_0 - k_v (V - V_0)$$

**虚拟同步机(VSM)模式**：
- 模拟同步机惯量响应
- 提供虚拟惯量和阻尼

### 3.3 系统级模型

**等效模型**：
- 受控功率源：$P_{out} = P_{ref} \cdot \eta(P)$
- 一阶惯性：$\tau \frac{dP_{out}}{dt} + P_{out} = P_{ref}$
- 响应时间：100ms-1s

## 4. 典型参数

### 4.1 磷酸铁锂(LFP)电池参数

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

### 4.2 储能变流器(PCS)参数

| 参数 | 小型(100kW) | 中型(1MW) | 大型(10MW+) |
|------|-------------|-----------|-------------|
| 直流电压范围 | 500-850V | 600-1500V | 1000-1500V |
| 最大效率 | 97-98% | 98-98.5% | 98.5-99% |
| 功率响应时间 | <100ms | <100ms | <100ms |
| 谐波THD | <3% | <3% | <3% |
| 功率因数 | ±0.95可调 | ±0.95可调 | ±0.95可调 |

### 4.3 模型选择指南

| 应用场景 | 推荐模型 | 说明 |
|---------|---------|------|
| 调频性能分析 | 详细电池+PCS | 捕捉快速响应 |
| 能量管理 | SOC模型+效率曲线 | 关注能量 |
| 电能质量 | 平均值PCS模型 | 关注谐波 |
| 系统级仿真 | 等效功率源 | 大规模系统 |

## 5. 适用边界与限制

### 5.1 适用条件
- **时间尺度**：毫秒级至小时级（电磁暂态至能量管理）
- **频率范围**：DC至开关频率（通常<10kHz）
- **温度范围**：-20°C至55°C（超出需特殊考虑）
- **SOC范围**：10%-90%（超出范围参数非线性增强）

### 5.2 模型限制
- **电化学细节**：Thevenin模型不捕捉内部电化学过程
- **老化效应**：需要额外的老化模型叠加
- **热耦合**：简化热模型，复杂热管理需多物理场仿真
- **故障模式**：不涵盖内部短路等故障机理

### 5.3 精度边界
| 模型类型 | 电压精度 | 电流精度 | SOC精度 | 适用场景 |
|---------|---------|---------|---------|---------|
| 详细模型 | ±1% | ±2% | ±3% | 短时高动态 |
| 平均值模型 | ±3% | ±5% | ±5% | 系统级仿真 |
| 等效功率源 | ±5% | - | ±10% | 长时间尺度 |

## 6. 代表性来源

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Battery Energy Storage System Modeling for EMT Simulation | 2018 | BESS EMT建模综合方法 |
| Lithium-Ion Battery Model for Electromagnetic Transient Studies | 2019 | 锂电池暂态仿真模型 |
| Grid-Scale Battery Storage EMT Modeling and Validation | 2020 | 电网级储能EMT建模与验证 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[energy-storage-converter-model|储能变流器]] - 储能PCS控制
- [[vsc-model|VSC模型]] - 电压源变换器
- [[igbt-model|IGBT模型]] - 开关器件模型
- [[inductor-model|电感模型]] - 滤波电感设计
- [[capacitor-model|电容模型]] - 直流电容模型

### 6.2 相关方法
- [[numerical-integration|数值积分]] - SOC计算方法
- [[state-space-method|状态空间法]] - 电池模型状态空间
- [[pi-controller-model|PI控制器]] - 功率环控制
- [[droop-control-model|下垂控制]] - 一次调频控制

### 6.3 相关主题
- [[vsc-model|VSC模型]] - 储能变流器
- 电池管理系统(BMS) - BMS控制策略
- 频率调节 - 一次/二次调频
- 新能源并网 - 风光储联合

## 相关方法
- [[numerical-integration|数值积分]] - SOC计算与电池模型离散化
- [[state-space-method|状态空间法]] - 电池状态空间建模
- [[average-value-model|平均值模型]] - 系统级简化仿真
- [[droop-control-model|下垂控制模型]] - 一次调频控制实现

## 相关模型
- [[energy-storage-converter-model|储能变流器]] - PCS详细控制模型
- [[vsc-model|VSC模型]] - 电压源变换器拓扑
- [[igbt-model|IGBT模型]] - 开关器件模型
- [[inductor-model|电感模型]] - 滤波电感设计
- [[capacitor-model|电容模型]] - 直流电容模型

## 相关主题
- [[vsc-hvdc|VSC-HVDC]] - 储能接入高压直流
- 频率调节 - 一次/二次调频
- 新能源并网 - 风光储联合运行
- [[real-time-simulation|实时仿真]] - 储能系统实时仿真
- 微电网 - 储能微电网应用

---

*本页面基于Karpathy LLM Wiki Pattern构建*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Control and Simulation of a Grid-Forming Inverter for Hybrid]] | 2021 |
| [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution|Active Damping Control and Parameter Calculation for Resonan]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[design-and-implementation-of-scalable-communication-interfaces-for-reliable-and-|Design and Implementation of Scalable Communication Interfac]] | 2025 |

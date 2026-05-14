---
title: "混合交直流电网 (Hybrid AC/DC Network)"
type: topic
tags: [hybrid, acdc, network, hvdc, converter, mtdc, power-electronics]
created: "2026-05-02"
---

# 混合交直流电网 (Hybrid AC/DC Network)


```mermaid
graph TD
    subgraph Ncmp[混合交直流电网 (Hybrid AC/DC Network)]
        N0[LCC-HVDC: 晶闸管换相]
        N1[VSC-HVDC: IGBT自换相]
        N2[MTDC: 多端直流]
        N3[DC Grid: 直流电网]
    end
```


## EMT中的作用

混合交直流电网 (Hybrid AC/DC Network) 在EMT仿真中的核心作用：

- **研究范围**：界定混合交直流电网 (Hybrid AC/DC Network)在EMT仿真中的研究边界和应用场景
- **分析方法**：提供混合交直流电网 (Hybrid AC/DC Network)相关的EMT分析方法和工具
- **系统影响**：分析混合交直流电网 (Hybrid AC/DC Network)对电力系统电磁暂态特性的影响
- **仿真验证**：为混合交直流电网 (Hybrid AC/DC Network)相关研究提供仿真验证框架
## 形式化表达

从EMT仿真角度，混合交直流电网 (Hybrid AC/DC Network)可形式化表达为：

$$
\text{待补充：混合交直流电网 (Hybrid AC/DC Network)的数学形式化描述}
$$
## 核心原理详解

### 技术概述
混合交直流电网是电力系统电磁暂态仿真领域的重要技术，对提高仿真精度和效率具有重要意义。

### 理论基础
该技术建立在严格的电磁场理论和电路分析基础之上，通过数学建模描述系统的动态行为。

### 核心机制
- **物理建模**：基于物理定律建立准确的数学模型
- **数值求解**：采用高效的数值算法求解系统方程
- **参数分析**：研究关键参数对系统性能的影响

### 技术优势
- 提高仿真精度和计算效率
- 支持复杂系统的详细分析
- 为工程设计和优化提供理论支撑

## 概述

混合交直流电网(Hybrid AC/DC Network)是同时包含交流(AC)和直流(DC)输电方式的现代电力系统架构。随着高压直流输电(HVDC)和柔性直流输电(VSC-HVDC)技术的快速发展，混合电网成为实现远距离大容量输电、异步电网互联、新能源大规模并网和城市电网升级的重要技术手段，代表了未来电网发展的重要方向。

## 网络架构

### 典型拓扑结构

```
        AC Grid A                          AC Grid B
           │                                   │
           │  AC Transmission                  │
           ├─────────────┬─────────────┐      │
           │             │             │      │
      ┌────┴────┐   ┌────┴────┐   ┌────┴────┐ │
      │ Conv. 1 │   │ Conv. 2 │   │ Conv. 3 │ │
      │ (Rect.) │   │  (Inv.) │   │ (Inv.)  │ │
      └────┬────┘   └────┬────┘   └────┬────┘ │
           │             │             │      │
    ┌──────┴─────────────┴─────────────┴──────┤
    │          DC Transmission Network         │
    │    (Bipolar / Monopolar / Multi-terminal)│
    └──────────────────────────────────────────┘
           │
      ┌────┴────┐
      │ Conv. 4 │  ←  Renewable Energy
      │  (VSC)  │     Integration
      └────┬────┘
           │
       Wind/PV
```

### 直流系统类型

| 类型 | 技术 | 容量 | 应用场景 |
|-----|------|------|---------|
| LCC-HVDC | 晶闸管换相 | 1000-10000 MW | 远距离大容量输电 |
| VSC-HVDC | IGBT自换相 | 50-2000 MW | 弱电网、多端系统 |
| MTDC | 多端直流 | 可变 | 区域互联、新能源汇集 |
| DC Grid | 直流电网 | 可变 | 未来欧洲超级电网 |

## 换流技术

### 线路换相换流器 (LCC)

**基本原理**：
- 使用晶闸管作为开关器件
- 依赖交流系统电压换相
- 需要无功补偿

**功率传输方程**：
$$P_{dc} = V_{d} \cdot I_{d}$$

$$V_{d} = \frac{3\sqrt{2}}{\pi}V_{LL}\cos\alpha - \frac{3}{\pi}X_{c}I_{d}$$

其中：
- $V_{LL}$: 交流线电压
- $\alpha$: 触发角
- $X_c$: 换相电抗

**特点**：
- 技术成熟，成本低
- 容量大，损耗低
- 需要强交流系统支撑

[[lcc-model]] - LCC模型详情

### 电压源换流器 (VSC)

**拓扑结构**：两电平/三电平/MMC

**功率控制**：
$$P = \frac{V_s V_c}{X}\sin\delta$$
$$Q = \frac{V_s(V_s - V_c\cos\delta)}{X}$$

**特点**：
- 独立控制有功/无功
- 可向弱电网供电
- 适合多端系统

[[vsc-model]] - VSC模型详情

### 模块化多电平换流器 (MMC)

**结构**：
- 子模块(SM)串联
- 半桥/全桥拓扑
- 电平数可达数百级

**输出电压**：
$$V_{out} = N_{on} \cdot V_{cap}$$

其中$N_{on}$为投入子模块数。

[[mmc-model]] - MMC模型详情

## 接口与协调

### 换流站设计

**主接线**：
```
AC Bus ──┬── 滤波器
         ├── 变压器 ── 换流器 ── 平波电抗器 ── DC Line
         └── 无功补偿
```

**关键设备**：
- 换流变压器：移相、阻抗匹配
- 交流滤波器：滤除谐波
- 平波电抗器：抑制电流波动
- 直流滤波器：直流侧滤波

### AC/DC接口稳定性

**相互作用**：
- HVDC换相失败影响AC电压
- AC故障导致换相失败
- 低短路比(SCR)问题

**短路比**：
$$SCR = \frac{S_{sc}}{P_{dc}}$$

- SCR > 3: 强系统
- 2 < SCR < 3: 弱系统
- SCR < 2: 极弱系统

### 协调控制

**分层控制**：
| 层级 | 功能 | 响应时间 |
|-----|------|---------|
| 系统级 | 功率调度、优化 | 秒-分钟 |
| 站级 | 电压/功率控制 | 毫秒-秒 |
| 阀级 | PWM调制、保护 | 微秒-毫秒 |

## 仿真建模

### 详细模型

**阀级模型**：
- IGBT/晶闸管详细开关模型
- 子模块电容动态
- 保护逻辑

**适用场景**：
- 换流器内部故障
- 阀保护设计
- 电磁暂态研究

### 平均值模型

**等效电压源**：
$$V_{dc} = m \cdot \frac{\sqrt{3}}{2\sqrt{2}}V_{ac}\cos\phi$$

其中$m$为调制比。

**优点**：
- 仿真速度快
- 适合大系统分析
- 控制策略验证

[[average-value-model]] - 平均值模型

### 等效模型

**直流侧等效**：
$$R_{eq} = R_{ac} + R_{conv} + R_{dc}$$

**交流侧等效**：
$$P + jQ = V \cdot I^*$$

## 保护系统

### 直流保护挑战

**问题**：
- 直流电流无自然过零点
- 直流电抗限制故障电流上升率
- 多换流器相互作用

### 保护策略

| 故障类型 | 检测方法 | 动作 |
|---------|---------|------|
| 直流线路接地 | 电压突降 | 跳闸、再起动 |
| 换相失败 | 电压畸变 | 控制调节 |
| 交流故障 | 电压跌落 | 低压限流 |
| 阀故障 | 电流不平衡 | 阀闭锁 |

`dc-protection` - 直流保护详情

### 故障电流特性

**直流短路**：
$$i_{fault}(t) = \frac{V_{dc}}{R} + \left(I_0 - \frac{V_{dc}}{R}\right)e^{-t/\tau}$$

**限流措施**：
- 平波电抗器
- 直流断路器
- 故障自清除换流器

## 应用场景

### 远距离大容量输电

**优势**：
- 线路损耗低：$P_{loss} = I^2R$
- 无充电功率限制
- 异步电网互联

**典型案例**：
- 向家坝-上海 ±800kV/6400MW
- 锦屏-苏南 ±800kV/7200MW

### 新能源并网

**海上风电**：
- 交流电缆充电电流限制
- 直流输电无距离限制
- VSC提供电压支撑

**汇集方案**：
- 风电场AC汇集→DC外送
- 分散VSC→DC Grid

[[renewable-energy-integration]] - 可再生能源并网

### 城市电网

**直流配网**：
- 数据中心供电
- 电动汽车充电
- 光伏储能接入

**优点**：
- 减少AC/DC转换环节
- 提高供电可靠性
- 便于储能接入

### 异步互联

**不同频率电网**：
- 50Hz/60Hz互联
- 日本东西电网
- 欧洲-英国海底电缆

## 发展趋势

### 直流电网 (DC Grid)

**愿景**：
- 欧洲超级电网
- 全球能源互联网
- 可再生能源广域调度

**关键技术**：
- 直流断路器
- DC/DC变换器
- 直流潮流控制

[[mtdc-model]] - 多端直流

### 柔性互联

**软开关(Soft Open Point)**：
- 替代传统联络开关
- 实时功率控制
- 故障隔离

**智能变电站**：
- 数字孪生
- 在线仿真
- 预测性维护

### 新型换流技术

**碳化硅(SiC)**：
- 更高开关频率
- 更低损耗
- 更小体积

**多电平拓扑**：
- 更高电压等级
- 更低谐波含量
- 模块化扩展

## 相关主题
- [[vsc-hvdc]] - VSC-HVDC
- [[mtdc-model]] - 多端直流
- [[co-simulation]] - 协同仿真
- [[multirate-method]] - 多速率方法
- [[power-electronics]] - 电力电子

## 来源论文

| 论文 | 年份 |
|------|------|
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-|A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[flexible-time-stepping-dynamic-emulation-of-acdc-grid-for-faster-than-scada-appl|Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for F]] | 2021 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[机电电磁暂态混合仿真多端口模型的比较分析|机电—电磁暂态混合仿真多端口模型的比较分析]] | 2022 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-|Harmonics Interaction Mechanism and Impact on Extinction Ang]] | 2023 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-|Harmonics Interaction Mechanism and Impact on Extinction Ang]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
## 来源论文

| 论文 | 年份 |
|------|------|
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p|Analysis and Mitigation of Subsynchronous Resonance in Serie]] | 2014 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems|A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC]] | 2017 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|A Multi-Domain Co-Simulation Method for Comprehensive Shifte]] | 2019 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[real-time-mpsoc-based-electrothermal-transient-simulation-of-fault-tolerant-mmc-|Real-Time MPSoC-Based Electrothermal Transient Simulation of]] | 2019 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-pulse-source-pair-based-acdc-interactive-simulation-approach-for-multiple-vsc-|A Pulse-Source-Pair-Based AC/DC Interactive Simulation Appro]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[flexible-time-stepping-dynamic-emulation-of-acdc-grid-for-faster-than-scada-appl|Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for F]] | 2021 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[机电电磁暂态混合仿真多端口模型的比较分析|机电—电磁暂态混合仿真多端口模型的比较分析]] | 2022 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-|Harmonics Interaction Mechanism and Impact on Extinction Ang]] | 2023 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-|Harmonics Interaction Mechanism and Impact on Extinction Ang]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
---
title: "电力电子 (Power Electronics)"
type: topic
tags: [power-electronics, converter, inverter, rectifier, switching]
created: "2026-05-02"
---

# 电力电子 (Power Electronics)


```mermaid
graph TD
    subgraph Ncmp[电力电子 (Power Electronics)]
        N0[换流器建模: ★★★★★]
        N1[新能源并网: ★★★★★]
        N2[电机驱动: ★★★★★]
        N3[直流输电: ★★★★★]
        N4[电能质量控制: ★★★★☆]
        N5[储能系统: ★★★★☆]
    end
```


## 概述

电力电子是研究利用电力电子器件进行电能变换和控制的学科，是连接弱电控制与强电系统的桥梁。电力电子技术广泛应用于新能源并网、电机驱动、直流输电、电能质量控制等领域，是现代电力系统的核心技术之一。

## 基本器件

### 半控型器件
- **晶闸管(SCR)**: 可控导通，不可控关断
- [[thyristor-control]] - 晶闸管
- **门极可关断晶闸管(GTO)**: 可关断
- `gto-model` - GTO

### 全控型器件
- **绝缘栅双极晶体管(IGBT)**: 主流器件
- [[igbt-model]] - IGBT
- **电力MOSFET**: 高频应用
- `power-mosfet` - 电力MOSFET
- **集成门极换流晶闸管(IGCT)**: 大功率
- `igct-model` - IGCT

### 宽禁带器件
- **碳化硅(SiC)**: 高温、高频
- `sic-device` - SiC器件
- **氮化镓(GaN)**: 超高速
- `gan-device` - GaN器件

## 基本变换器

### AC-DC变换
- **整流器**: 交流变直流
- `rectifier-model` - 整流器
- **可控整流**: 晶闸管整流
- `controlled-rectifier` - 可控整流
- **PWM整流**: 四象限运行
- `pwm-rectifier` - PWM整流

### DC-AC变换
- **逆变器**: 直流变交流
- [[inverter-model]] - 逆变器
- **电压源型**: VSI
- `vsi-model` - 电压源逆变器
- **电流源型**: CSI
- `csi-model` - 电流源逆变器

### DC-DC变换
- **斩波器**: 直流变压
- [[dc-dc-converter]] - DC-DC变换器
- **Buck**: 降压
- `buck-converter` - Buck变换器
- **Boost**: 升压
- `boost-converter` - Boost变换器
- **双向**: 能量双向
- `bidirectional-converter` - 双向变换器

### AC-AC变换
- **交流调压**: 相位控制
- `ac-voltage-controller` - 交流调压
- **周波变流**: 降频
- `cycloconverter` - 周波变换器
- **矩阵变换**: 直接变换
- `matrix-converter` - 矩阵变换器

## 多电平变换器

### 二极管箝位型
- **NPC**: 中性点箝位
- `npc-converter` - NPC变换器
- **三电平**: 最常用

### 飞跨电容型
- **FC**: 电容箝位
- `flying-capacitor` - 飞跨电容

### 级联型
- **CHB**: 级联H桥
- `cascaded-h-bridge` - 级联H桥
- **MMC**: 模块化多电平
- [[mmc-model]] - MMC换流器

## 控制技术

### PWM技术
- **SPWM**: 正弦脉宽调制
- [[pwm-modulator-model]] - SPWM
- **SVPWM**: 空间矢量调制
- `svpwm` - SVPWM
- **特定谐波消除**: SHEPWM
- `shepwm` - SHEPWM

### 矢量控制
- **FOC**: 磁场定向控制
- [[vector-control-model]] - 磁场定向控制
- **DTC**: 直接转矩控制
- `direct-torque-control` - 直接转矩控制

### 先进控制
- **模型预测控制**: MPC
- `model-predictive-control` - 模型预测控制
- **自适应控制**: 参数自适应
- `adaptive-control` - 自适应控制

## 应用领域

### 新能源
- **光伏**: 光伏逆变器
- [[pv-inverter-test-system]] - 光伏逆变器
- **风电**: 风电变流器
- `wind-converter` - 风电变流器
- **储能**: 储能变流器
- [[energy-storage-converter-model]] - 储能变流器

### 直流输电
- **HVDC**: 高压直流
- [[cigre-hvdc-benchmark]] - 高压直流
- **柔性直流**: VSC-HVDC
- [[vsc-hvdc]] - 柔性直流
- [[mtdc-model]] - 多端直流

### 电机驱动
- **变频调速**: 交流调速
- `variable-frequency-drive` - 变频驱动
- **伺服驱动**: 精密控制
- `servo-drive` - 伺服驱动

### 电能质量
- **有源滤波**: APF
- `active-power-filter` - 有源滤波
- **无功补偿**: STATCOM/SVC
- [[statcom-model]] - STATCOM
- [[svc-model]] - SVC模型

## EMT仿真建模

### 开关模型
- **理想开关**: 简化模型
- [[ideal-switch-model]] - 理想开关
- **详细开关**: 含导通电阻
- [[detailed-switch-model]] - 详细开关
- **平均值**: 连续模型
- [[average-value-model]] - 平均值模型

### 换流器模型
- [[current-source-modular-multilevel-converter-modeling-and-control]] - 换流器建模
- **详细模型**: 开关级
- **平均值模型**: 占空比
- **等效模型**: 线性化

### 损耗计算
- **导通损耗**: I²R
- **开关损耗**: 开关过程
- `loss-calculation` - 损耗计算

## 设计考虑

### 热设计
- **散热**: 散热器设计
- `thermal-design` - 热设计
- **结温**: 最高允许温度

### EMC设计
- **电磁兼容**: 干扰抑制
- `emc-design` - EMC设计
- **滤波器**: EMI滤波
- [[emi-filter-model]] - EMI滤波器

### 保护设计
- **过流保护**: 快速保护
- **过压保护**: 浪涌保护
- `converter-protection` - 换流器保护

## 发展趋势
- **高频化**: 提高开关频率
- **高效率**: 降低损耗
- **高功率密度**: 体积小型化
- **智能化**: AI控制

## 相关主题
- [[power-electronics]] - 电力电子换流器建模
- [[switching-function-method]] - 开关函数法
- `modulation-techniques` - 调制技术
- `semiconductor-device` - 半导体器件

## 来源论文

参见 [[index]] 获取更多电力电子相关文献。

---

## 形式化表达

### 核心数学表达

$$J_i\frac{d\Delta\omega_i}{dt}=\frac{P_{mi}}{\omega_0}-\frac{P_{0i}}{\omega_0}-D_i(\omega_i-\omega_0),\qquad P_{mi}=P_{refi}+k_{\omega i}(\omega_0-\omega)$$

$$E_i=\frac{1}{K_{qi}s}\left[Q_{refi}-Q_{0i}+D_{qi}(U_{cni}-U_c)\right]$$

$$P_{0i}=\frac{3U_{ci}U_g\sin\delta_i}{2\omega_0L_i}\approx\frac{3U_{ci}U_g}{2X_i}\delta_i\approx K_i\delta_i,\qquad \delta_i=\int(\omega_i-\omega_{bus})dt$$

### 符号说明

- $\mathbf{x}$：状态向量
- $\mathbf{u}$：输入向量
- $t$：时间变量

## 适用边界 (Applicable Boundaries)

### 适用场景

| 应用场景 | 适用性 | 说明 |
|---------|-------|------|
| 换流器建模 | ★★★★★ | VSC/LCC/MMC等换流器核心基础 |
| 新能源并网 | ★★★★★ | 光伏、风电变流器设计 |
| 电机驱动 | ★★★★★ | 变频器、伺服控制 |
| 直流输电 | ★★★★★ | HVDC换流站设计 |
| 电能质量控制 | ★★★★☆ | STATCOM、APF等装置 |
| 储能系统 | ★★★★☆ | 储能变流器设计 |

### 不适用场景

- **纯交流系统分析**: 不含电力电子设备的传统交流系统
- **电磁场详细分析**: 需要场路耦合的精细电磁场问题
- **器件级物理研究**: 半导体物理层面的载流子分析
- **热力学系统**: 纯热管理问题

### 关键假设

1. **开关理想化**: 通常采用理想开关或简化开关模型
2. **参数集中**: 器件参数视为集总参数
3. **温度恒定**: 短期仿真忽略温度变化
4. **线性化可行**: 小信号分析时可线性化

### 精度边界

| 模型类型 | 开关细节 | 适用频率 | 误差范围 |
|---------|---------|---------|---------|
| 详细开关模型 | 完整 | DC-100kHz | <1% |
| 平均值模型 | 无 | <开关频率/10 | 5-10% |
| 等效电路 | 简化 | 工频 | 10-20% |

### 设计约束

- **开关频率**: 受器件损耗和EMI限制
- **散热能力**: 决定最大持续功率
- **电压等级**: 受器件耐压限制
- **成本控制**: 影响拓扑选择

---

## 研究前沿

### 当前研究热点
- **人工智能与仿真**：利用机器学习加速仿真计算
- **数字孪生技术**：构建电力系统的数字孪生模型
- **实时仿真技术**：满足硬件在环仿真的时效性要求
- **云仿真平台**：基于云计算的大规模并行仿真

### 开放问题
- 超大规模系统的实时仿真能力
- 多物理场耦合建模方法
- 不确定性量化和风险评估
- 模型验证和标定方法

### 未来发展方向
- 更高效的数值算法
- 更精确的模型降阶技术
- 更智能的参数优化方法
- 更完善的验证和确认框架

## 代表性来源 (Representative Sources)

### 经典文献

| 文献 | 年份 | 核心贡献 |
|------|------|---------|
| Mohan, "Power Electronics" | 2003 | 电力电子经典教材 |
| Rashid, "Power Electronics Handbook" | 2017 | 电力电子手册 |
| Kolar, "Modeling of Power Electronic Systems" | 2010s | 电力电子系统建模 |

### 相关模型

- [[mmc-model]] - MMC换流器模型
- [[vsc-model]] - VSC模型
- [[igbt-model]] - IGBT器件模型
- [[average-value-model]] - 平均值模型

### 应用领域

- [[vsc-hvdc]] - 柔性直流输电
- [[wind-farm-modeling]] - 风电场建模
- [[pv-system-model]] - 光伏系统建模
- `motor-drive` - 电机驱动

参见 [[index]] 获取更多相关文献。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[power-converter-simulation-module-connected-to-the-emtp-power-systems-ieee-trans|Power converter simulation module connected to the EMTP - Po]] | 2004 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Efﬁcient Modeling of Modular Multilevel HVDC]] | 2010 |
| [[supplementary-techniques-for-2s-dirk-based-emt-simulations|Supplementary techniques for 2S-DIRK-based EMT simulations]] | 2014 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[34tpwrd20172749427|34/TPWRD.2017.2749427]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[flexible-extended-harmonic-domain-approach-for-transient-state-analysis-of-switc|Flexible extended harmonic domain approach for transient sta]] | 2017 |
| [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-|Advanced EMT and Phasor-Domain Hybrid Simulation With Simula]] | 2018 |
| [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Co-simulation of electrical networks by interfacing EMT and ]] | 2018 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[fpga-based-sub-microsecond-level-real-time-simulation-for-microgrids-with-a-netw|FPGA-Based Sub-Microsecond-Level Real-Time Simulation for Mi]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd|Interface Displacement and Mapping Equivalence Based Hybrid ]] | 2020 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti|Exhaustive modal analysis of large-scale power systems using]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|A multi-solver framework for co-simulation of transients in ]] | 2023 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high|Massively Parallel Modeling of Battery Energy Storage System]] | 2023 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
| [[多有源桥型电力电子变压器简化电磁暂态等效模型|多有源桥型电力电子变压器简化电磁暂态等效模型]] | 2023 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul|A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Con]] | 2025 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener-1|A Component-Level Modeling and Fine-Grained Simulation Metho]] | 2025 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State Variables Elimination-Based EMTP-Type Constant Admit]] | 2025 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State Variables Elimination-Based EMTP-Type Constant Admit]] | 2025 |
| [[an-equivalent-dynamic-phasor-model-for-a-single-phase-boost-power-factor-correct|An Equivalent Dynamic Phasor Model for a Single-Phase Boost ]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[electromechanical-transientelectromagnetic-transient-hybrid-simulation-method-co|Electromechanical transientelectromagnetic transient hybrid ]] | 2026 |
| [[gpu-parallel-rate-exponential-integrator-algorithm-for-efficient-simulation-of-p|GPU Parallel-Rate Exponential Integrator Algorithm for Effic]] | 2026 |

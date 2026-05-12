---
title: "模块化多电平换流器 (MMC)"
type: model
tags: [mmc, hvdc, converter, sub-module, arm]
created: "2026-04-13"
updated: "2026-05-12"
---

# 模块化多电平换流器 (MMC)

## 概述

模块化多电平换流器（Modular Multilevel Converter, MMC）是当前高压直流输电（HVDC）和柔性交流输电系统的主流拓扑。由多个子模块（SM）级联构成桥臂，具有模块化、可扩展、低谐波等优势。

## EMT建模方法

### 1. 详细模型
- 每个子模块单独建模
- 包含开关动态和电容电压
- 计算量极大，适用于少量SM

### 2. 平均值模型 (AVM)
- 桥臂平均化处理
- 忽略开关纹波，保留低频动态
- 计算效率提升1-2个数量级
- 增强平均值模型（考虑环流）

### 3. 等效模型
- Thevenin等效桥臂
- 嵌套快速求解方法
- 任意多端口子模块结构

### 4. 固定导纳模型
- ADC建模，避免矩阵重构
- 适用于实时仿真
- FPGA硬件实现

### 5. 动态相量模型
- 频域MMC建模
- 适用于混合仿真
- 宽频暂态分析

## 关键技术挑战

- 子模块电容电压平衡
- 环流抑制控制
- 直流故障穿越
- 损耗建模（虚假功率问题）
- 大规模MMC-MTDC系统仿真

## 量化性能边界

**Gnanarathna 2010 DEM — 基于戴维南等效的MMC详细等效模型（Detailed Equivalent Model）**:
- 采用梯形积分法将每个子模块等效为戴维南电路，再将桥臂内N个子模块聚合为单一戴维南等效电路
- 仿真速度较详细开关模型提升 **310x**，相对误差 < **0.1%**
- 验证系统：2400个开关元件的MMC-HVDC，仿真时间从5s缩短至30s（PSCAD/EMTDC）
- 起动、功率反向、交流故障等工况均验证，波形与详细模型高度重合
- 数据缺口：原文验证基于单一MMC-HVDC系统，MMC-MTDC多端工况下的加速比未单独报告

**Xu 2018 Schur补法 — 任意多端口子模块高速EMT等效模型**:
- 基于Schur补数技术递归消去子模块内部节点，构建连接外部网络的多端口诺顿等效电路
- 节点规模从 **802个缩减至4个**/桥臂，计算效率提升 **2～3个数量级**
- 相对误差 < **0.1%**，完整保留子模块内部动态信息
- 支持半桥、全桥、双扣位等多种子模块结构，无需解析推导
- 数据缺口：对极高子模块数（N > 500）的性能表现未系统评估

**Xu 2015 综述 — 多种等效模型横向对比**:
- 戴维南等效模型在N=200时加速比≈15～20x（vs详细开关模型）
- 梯形积分法比后退欧拉法慢约2x，但精度高 **0.2～0.4%**
- 电磁暂态平均简化模型在交直流故障中仍保持较高精度
- 数据缺口：多种模型间缺乏统一基准测试系统和标准化工况

**Gao 2023 混合数值积分MMC模型**:
- 采用混合数值积分（BE+蛙跳法）实现MMC内外动态方程完全解耦，桥臂等效电导恒定
- 仿真速度提升 **5～15x**（vs详细开关模型）
- 稳态误差 < **0.5%**，暂态峰值误差 < **1%**
- 验证平台：EMTP-type仿真，波形与详细模型高度重合
- 数据缺口：FBSM拓扑下的加速比和精度未单独报告

**Parvari 2023 加速DEM — 欧拉积分恒定导纳模型**:
- 采用欧拉积分替代梯形积分，恶化开关状态下的导纳矩阵更新频率（仅闭锁工况更新）
- HBSM加速比提升 **+30%**，FBSM加速比提升 **+60%**（vs传统DEM）
- 4站MMC-MTDC（200FBSM/站）：31.0s vs 84.7s（传统DEM）
- 数据缺口：欧拉积分引入的数值误差增量未与梯形法量化对比

**Stepanov 2020 自适应MMC模型（AVM/AEM/DEM）**:
- AVM/AEM/DEM三档自适应切换，模型切换过程外部电气特性误差 < **0.5%**
- 验证系统：401电平MMC，仿真平台PSCAD/EMTDC
- 闭锁模式求解器迭代上限30次，实际收敛 < **6次**
- 稳态时切换至AVM/AEM可降低单步计算耗时65～75%，整体加速比 > **3.5x**
- 数据缺口：多端MTDC工况下的自适应切换策略未验证

**del Giudice 2024 打靶法MMC初始化**:
- 两阶段AVM到Thévenin映射的打靶法初始化，直接从接近稳态启动
- 消除传统初始化所需的长时间仿真过渡
- 兼容不同详细程度的MMC模型，支持包含调制策略与电容电压平衡算法的复杂控制方案
- 数据缺口：具体初始加速比和稳态逼近误差在原文摘要中未量化报告

**数据缺口声明**：MMC建模的加速比高度依赖于子模块数N、子模块类型（HBSM/FBSM/CDSM）和仿真平台。不同模型间的横向对比缺乏统一基准（详细模型步长、硬件配置不同）。大多数验证在离线EMT环境完成，实时硬件平台（FPGA/RTDS/OPAL-RT）下的数据仅少数文献报告。特别是多端MTDC工况下的自适应模型切换策略仍缺乏充分验证。

## 相关方法
- [[average-value-model]]
- [[fixed-admittance]]
- [[state-space-method]]
- [[dynamic-phasor]]

## 相关模型
- [[vsc-model|VSC模型]] - 两电平/三电平换流器对比
- [[fdne-model|频变网络等值(FDNE)]] - MMC外部网络等值
- [[transformer-model|换流变压器]] - MMC换流变建模
- [[cable-model|电缆模型]] - 直流电缆连接
- [[mtdc-model|MTDC模型]] - 多端MMC系统

## 相关主题
- [[vsc-hvdc]]
- [[real-time-simulation]]
- [[co-simulation]]
- [[frequency-dependent-modeling]]
- [[parallel-computing]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[efcient-modeling-of-modular-multilevel-hvdc-15|Efﬁcient Modeling of Modular Multilevel HVDC]] | 2010 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[ahmed-等-a-computationally-efficient-continuous-model-for-the-modular-multilevel-|Ahmed et al. | A Computationally Efficient Continuous Model for t]] | 2014 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Opera]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed ]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters|Improved Accuracy Average Value Models of Modular Multilevel]] | 2016 |
| [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us|High-Speed EMT Modeling of MMCs With Arbitrary Multiport Sub]] | 2018 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep|An Enhanced Average Value Model of Modular Multilevel Conver]] | 2018 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified High-Speed EMT Equivalent and Implementation Method ]] | 2018 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula|Adaptive Modular Multilevel Converter Model for Electromagne]] | 2020 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[spurious-power-and-its-elimination-in-modular-multilevel-converter-models|Spurious power and its elimination in modular multilevel con]] | 2020 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With ]] | 2021 |
| [[parallelization-of-mmc-detailed-equivalent-model|Parallelization of MMC detailed equivalent model]] | 2021 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave Function and Multiscale Modeling of MMC-HVdc System for]] | 2021 |
| [[an-equivalent-hybrid-model-for-a-large-scale-modular-multilevel-converter-and-co|An Equivalent Hybrid Model for a Large-Scale Modular Multile]] | 2022 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-|High-frequency oscillation analysis and suppression strategy]] | 2022 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume|An Efficient Half-Bridge MMC Model for EMTP-Type Simulation ]] | 2023 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters|An accelerated detailed equivalent model for modular multile]] | 2023 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-|Generalized Electromagnetic Transient Equivalent Modeling an]] | 2023 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled Detailed Equivalent Model for Parallel and Multi-R]] | 2026 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
---
title: "变压器模型 (Transformer)"
type: model
tags: [transformer, hysteresis, saturation, frequency-dependent, white-box]
created: "2026-04-13"
---

# 变压器模型 (Transformer)

## 概述

变压器是电力系统中最关键的设备之一，其EMT建模需要准确表征磁路饱和、磁滞、频率特性和绕组间耦合等非线性特性。

## 主要模型类型

### 1. 经典模型
- 线性互感模型
- 饱和励磁支路
- 适用于稳态和小信号分析

### 2. 磁滞模型
- Jiles-Atherton磁滞公式
- Preisach模型
- 现场磁滞曲线测量
- 适用于铁磁谐振研究

### 3. 白盒模型
- 基于详细设计参数
- 高频白盒变压器模型
- 接口因子法
- 阻尼因子模型

### 4. 对偶电路模型
- 磁路-电路对偶建模
- 多芯变压器对偶电路
- UMEC（统一磁电耦合）模型
- Sen变压器模型

### 5. 频变模型
- 高频响应建模
- 绕组间电容
- 雷电冲击响应
- 宽频阻抗拟合

## 特殊效应

### 磁饱和
- 励磁电流畸变
- 铁芯饱和曲线
- 直流偏磁效应

### 磁滞
- 剩磁效应
- 励磁涌流
- 铁磁谐振

### 集肤效应和涡流
- 绕组频变电阻
- 铁芯涡流损耗
- 螺线管效应（三芯电缆）

## 应用场景

- 励磁涌流分析
- 铁磁谐振研究
- 雷电冲击响应
- 直流偏磁（GIC）
- 高频暂态分析

## 相关方法
- [[nodal-analysis]]
- [[vector-fitting]]
- [[state-space-method]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[ferroresonance]]


## 论文方法分析
> 基于 44 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 并行仿真框架设计 | 2 | A Novel Decoupled EMT Approach and Parallel Simulation Framework for M |
| 开关插值技术 | 2 | A Numerically Efficient and Accurate Model for Real-Time Simulation of |
| EMTP电磁暂态仿真 | 2 | Analysing a power transformer⠒s internal response to system transients |
| 数字时域仿真 | 2 | Digital Time-Domain Investigation of Transient Behavior of Coupling Ca |
| 频域分析 | 2 | Digital Time-Domain Investigation of Transient Behavior of Coupling Ca |
| 状态空间法 | 2 | Interfacing Factor-Based White-Box Transformer Modeling Method |
| 状态空间平均法(SSA) | 2 | Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Sol |
| 广义状态空间平均法(GSSA) | 2 | Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Sol |
| 动态相量法 | 2 | Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Sol |
| 混合平均建模 | 2 | Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Sol |
| 戴维南-诺顿等效建模 | 2 | 级联H桥型电力电子变压器的闭锁状态等效建模方法 |
| 终端导纳矩阵频率特性提取 | 1 | A high frequency transformer model for the EMTP - Power Delivery, IEEE |
| 有理函数逼近（含实极点/零点与共轭复极点/零点） | 1 | A high frequency transformer model for the EMTP - Power Delivery, IEEE |
| 无源RLC网络综合实现 | 1 | A high frequency transformer model for the EMTP - Power Delivery, IEEE |
| EMTP-RV电磁暂态仿真 | 1 | A link between EMTP-RV and FLUX3D for transformer energization studies |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 电力变压器 | 6 |
| 固态变压器(SST) | 5 |
| 多绕组变压器 | 4 |
| 双有源桥(DAB) | 3 |
| 级联H桥型电力电子变压器(CHB-PET) | 3 |
| 模块化固态变压器(MSST) | 2 |
| 双有源桥(DAB)DC-DC变换器 | 2 |
| 高频链路(HFL) | 2 |
| 耦合电容电压互感器(CCVT) | 2 |
| 降压变压器 | 2 |
| 串联电抗器 | 2 |
| 铁磁谐振抑制电路 | 2 |
| 负载模型 | 2 |
| 电力电子变压器(PET) | 2 |
| 功率模块(PM) | 2 |
### 验证方式分布
- **仿真**: 11 篇
- **仿真/对比**: 7 篇
- **仿真与实验对比**: 5 篇
- **仿真对比**: 4 篇
- **实验测量与仿真对比**: 2 篇
- **实验与仿真对比**: 2 篇
- **仿真与实验对比验证**: 2 篇
- **实验**: 1 篇
- **仿真验证与对比分析**: 1 篇
- **实验测量与理论对比**: 1 篇
- **计算对比/仿真**: 1 篇
- **现场开关暂态实验与EMT仿真对比**: 1 篇
- **仿真对比（与ANSYS Maxwell有限元仿真结果进行对比验证）**: 1 篇
- **仿真与对比**: 1 篇
- **仿真与实测故障数据对比**: 1 篇
- **仿真与对比验证（在完整HVDC链路时域仿真中，将换相电压波形与添加杂散电容的经典模型进行对比）**: 1 篇
- **实验与仿真**: 1 篇
- **仿真与现场试验对比**: 1 篇
## 技术演进脉络
### 1998年 (1篇)
- **Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Vo**
  - 💡 首次在EMTP中构建了完整集成CCVT变压器饱和特性、多级抽头、保护及铁磁谐振抑制电路细节的高保真数字模型。
  - 开发了基于EMTP的CCVT高精度数字时域模型，完整涵盖变压器饱和特性、抽头位置及保护抑制电路。
  - 通过仿真结果与实测数据对比，验证了模型在预测铁磁谐振等复杂暂态现象方面的高准确性。
### 1999年 (1篇)
- **电磁暂态计算中新的变压器模型**
  - 💡 提出了一种基于T型等值电路且直接采用有名值处理非标准变比的变压器块元件模型，有效克服了传统模型在空载消元失败及归算繁琐方面的缺陷。
  - 提出了一种基于T型等值电路的新型变压器模型，能够同时计及变比、相间耦合、联结组及相移等特性。
  - 采用有名值直接处理非标准变比，避免了传统标幺制归算的复杂过程，提高了计算直观性与效率。
### 2004年 (6篇)
- **A high frequency transformer model for the EMTP - Power Delivery, IEEE Transacti**
  - 💡 将终端导纳矩阵的有理函数逼近与无源RLC网络综合相结合，实现了兼顾高频精度、无源性与EMTP直接兼容性的变压器终端等效建模方法。
  - 提出了一种基于终端导纳矩阵频率特性的高频变压器EMTP模型。
  - 采用有理函数逼近技术精确拟合变压器在宽频范围内的导纳特性。
- **A transformer model for winding fault studies - Power Delivery, IEEE Transaction**
  - 💡 提出了一种基于简化漏磁系数评估且完全兼容EMTP的变压器绕组内部故障建模方法。
  - 提出了一种完全兼容EMTP软件的变压器内部故障建模方法
  - 开发了一种简便有效的变压器线圈间漏磁系数评估方法
- **A Z-transform model of transformers for the study of electromagnetic transients **
  - 💡 将变压器频变短路阻抗与增益函数结合并转化为Z变换离散模型，实现了分布参数变压器在EMT程序中的高效暂态仿真。
  - 提出结合频变短路阻抗与增益函数的Z变换变压器模型
  - 建立绕组两侧暂态电压电流的离散域直接映射关系
- **An improved low-frequency transformer model for use in GIC studies**
  - 💡 将Jiles-Atherton磁滞理论与涡流损耗效应无缝集成至EMTP变压器模型中，实现了无需外部干预的自动剩磁追踪与高精度GIC暂态仿真。
  - 将Jiles-Atherton磁滞理论成功嵌入EMTP型变压器仿真程序中。
  - 在同一模型中统一集成了铁芯涡流损耗效应。
- **Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Vo**
  - 💡 构建了涵盖变压器非线性饱和、多级抽头、保护及铁磁谐振抑制电路的CCVT全细节数字时域模型。
  - 开发了包含变压器饱和特性、抽头位置及保护抑制电路的CCVT详细EMTP模型
  - 通过仿真与实测数据对比验证了模型预测铁磁谐振等暂态响应的准确性
- **Three phase transformer modelling for fast electromagnetic transient studies - P**
  - 💡 首次系统对比多种三相变压器模型在快速电磁暂态（小电流开断过电压）仿真中的性能，并基于现场试验给出模型选择准则。
  - 系统评估了五种通用三相变压器模型在快速电磁暂态仿真中的适用性与性能差异
  - 明确了频率相关电容、漏感及相间与零序互感等关键参数对开断过电压仿真的影响机制
### 2009年 (1篇)
- **A link between EMTP-RV and FLUX3D for transformer energization studies**
  - 💡 提出并实现了EMTP-RV电磁暂态程序与FLUX3D三维有限元场求解器的程序化耦合，兼顾了大电网仿真效率与变压器铁芯物理细节精度。
  - 开发了EMTP-RV与FLUX3D之间的程序化耦合接口。
  - 实现了大型电力系统网络仿真与变压器铁芯三维精细磁场仿真的协同计算。
### 2013年 (1篇)
- **Dual Reversible Transformer Model for the**
  - 💡 提出了一种结构不变、双向可逆的变压器对偶等效电路模型，统一了多种低频暂态工况下的建模方法。
  - 提出了一种基于对偶原理的物理一致的单相双绕组变压器等效电路模型。
  - 统一了终端等效电路与拓扑等效电路，实现了模型的双向可逆性。
### 2014年 (2篇)
- **EMTP model of a bidirectional multilevel solid state transformer for distributio**
  - 💡 首次在EMTP/ATP环境中构建面向配电系统研究的双向多电平固态变压器全系统电磁暂态模型，实现谐波抑制与电能质量提升的协同仿真
  - 在ATP/EMTP平台中开发了适用于配电系统研究的双向MV/LV固态变压器电磁暂态模型
  - 在中压侧引入多电平NPC拓扑结构，有效降低了系统电压与电流谐波
- **Interfacing Factor-Based White-Box Transformer Modeling Method**
  - 💡 首次将基于ε因子损耗缩放的集中参数白盒变压器模型通过状态空间与诺顿等效无缝集成至EMTP平台，兼顾了计算效率、仿真精度与制造商数据隐私。
  - 提出基于状态方程与诺顿等效的白盒变压器模型与EMTP程序高效接口方法。
  - 利用矩阵对角化技术显著提升计算效率，且除时域离散外无其他数学近似。
### 2015年 (2篇)
- **Analysing a power transformer⠒s internal response to system transients using a h**
  - 💡 提出了一种无需变压器内部几何结构先验知识，仅依赖外部可获取数据即可实现系统级暂态与内部物理响应耦合分析的混合建模方法。
  - 提出了一种结合黑盒系统级仿真与灰盒物理结构分析的混合建模方法，用于评估变压器内部暂态响应。
  - 突破了传统方法对变压器内部几何结构先验知识的依赖，仅通过外部测试、铭牌数据和通用设计原则即可构建模型。
- **Duality-Based Transformer Model Including**
  - 💡 首次将涡流效应与对偶原理深度融合，构建了可直接用于主流EMT软件的高频变压器等效电路模型，并严格定义了电-磁元件的物理连接规则。
  - 提出了一种基于对偶原理的通用方法，用于构建包含绕组和铁芯涡流效应的电力变压器高频等效电路。
  - 推导了基于几何尺寸和材料参数的频变漏感和绕组电阻解析计算公式。
### 2016年 (2篇)
- **Duality-Based Transformer Modeling for Low-Frequency Transients**
  - 💡 构建了基于对偶原理的统一变压器拓扑建模框架，正确处理非线性磁化特性并从根本上澄清了低频暂态仿真中数值不稳定性的真实成因。
  - 澄清了变压器建模中的物理概念并消除了关于数值不稳定性的常见误解。
  - 提出了基于对偶原理的低频暂态统一拓扑建模技术。
- **Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Transformer Electromag**
  - 💡 首次将非线性磁等效电路与全并行流水线FPGA架构深度融合，实现了Sen变压器高保真、低延迟的实时电磁暂态HIL仿真。
  - 提出了一种基于非线性磁等效电路的Sen变压器高保真实时电磁暂态模型。
  - 在FPGA上设计了全并行与流水线硬件架构，实现了最低延迟与最小硬件资源消耗。
### 2017年 (1篇)
- **An improved high frequency white-box lossy transformer model for the calculation**
  - 💡 将复杂的多管段分支供水网络优化问题转化为线性规划形式，首次在保证最优性的同时实现高效求解。
  - 提出了一种适用于多管段分支供水网络的线性规划模型，突破了传统方法仅能处理单管段或次优解的局限。
  - 在保证全局最优解的前提下，显著提升了模型的计算运行效率。
### 2018年 (2篇)
- **Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Solid State T**
  - 💡 提出结合动态相量与状态空间平均的混合建模方法，克服了传统SSA在三相DAB稳定性分析中的精度局限，并实现了EMT仿真环境下的加速预测。
  - 揭示了传统状态空间平均法(SSA)在三相DAB小信号稳定性分析中精度不足的问题。
  - 开发了基于动态相量概念的广义状态空间平均法(GSSA)模型。
- **Small Signal Dynamic Phasor Model of Three-Phase DAB Converter for Solid State T**
  - 💡 提出基于动态相量的广义状态空间平均法及混合建模策略，解决了传统SSA在三相DAB小信号稳定性分析中精度不足的问题，并实现了EMT程序中的加速仿真。
  - 指出传统状态空间平均法(SSA)在三相DAB变换器小信号稳定性分析中存在精度不足的问题。
  - 提出基于动态相量概念的广义状态空间平均法(GSSA)模型，专门用于Y-∆型3p-DAB变换器。
### 2019年 (1篇)
- **Measurement-based frequency-dependent model of a HVDC transformer for electromag**
  - 💡 首次结合现场导纳频率扫描、特征值缩放与模态揭示变换，构建了兼顾数值稳定性、无源性及地耦合精度的HVDC变压器宽频黑盒模型。
  - 首次将黑盒建模技术应用于HVDC变压器，成功构建了宽频五端子频率相关模型。
  - 提出了一种新颖的特征值缩放方法，有效将测量数据中的励磁电流修正至物理合理水平。
### 2020年 (2篇)
- **Application of Duality-Based Equivalent Circuits for Modeling Multilimb Transfor**
  - 💡 利用常规可获取的替代参数集替代传统所需的内部铁芯尺寸与材料信息，实现了对偶原理在多肢变压器EMT建模中的工程化便捷应用。
  - 提出了一种基于对偶原理的等效电路建模方法，无需变压器内部铁芯设计参数即可实现高精度EMT建模。
  - 模型全面计及饱和、磁滞、深度饱和及剩磁效应，并支持任意数量绕组的灵活配置。
- **Time-Domain Implementation of Damping Factor White-Box Transformer Model for Inc**
  - 💡 首次提出利用对角化结构与实数运算将d因子白盒变压器模型高效嵌入EMT程序，兼顾端口等效与内部过电压计算。
  - 提出了一种将d因子白盒变压器模型直接集成到EMT仿真程序中的时域实现流程。
  - 充分利用模型的对角结构并结合实数算术运算，显著提升了暂态仿真的计算效率。
### 2021年 (6篇)
- **Determination of the saturation curve of power transformers by processing transi**
  - 💡 利用现场开关暂态录波数据直接反演变压器磁化饱和曲线，解决了传统仿真模型参数难以准确获取的工程难题。
  - 提出了一种从开关暂态测量记录中直接识别三相变压器饱和曲线的方法
  - 构建了适用于低频（<1 kHz）暂态仿真的简化变压器等效模型
- **Expanding the measuring range via S-parameters in a EHV voltage transformer mode**
  - 💡 创新性地采用S参数替代Y参数进行高频测量，突破了传统方法在MHz频段的测量瓶颈，显著提升了GIS电压互感器VFTO仿真的可靠性。
  - 提出采用S参数替代Y参数进行频域测量，将电压互感器建模的有效频率范围成功扩展至50 MHz。
  - 构建了多端口无源黑箱有理函数模型，能够准确复现VFTO特征谐振及暂态传播特性。
- **Hierarchical Modeling Scheme for High-Speed Electromagnetic Transient (EMT) Simu**
  - 💡 通过递归降维导纳矩阵获取相腿广义诺顿等效，在保持高精度的同时大幅降低EMT仿真计算复杂度。
  - 提出了一种针对电力电子变压器的分层建模方案以解决详细EMT仿真计算耗时过长的问题。
  - 通过递归降低导纳矩阵维度，高效获取各相腿的广义诺顿等效模型。
- **级联H桥型电力电子变压器的闭锁状态等效建模方法**
  - 💡 提出了一种基于戴维南-诺顿等效的CHB-PET闭锁状态建模方法，并通过共享状态变量存储单元实现了闭锁与非闭锁模型的高效无缝集成。
  - 推导了CHB-PET在部分闭锁和完全闭锁状态下的戴维南-诺顿等效参数。
  - 提出了一种与非闭锁模型共用状态变量存储单元的集成实施方法。
- **级联H桥型电力电子变压器的闭锁状态等效建模方法**
  - 💡 提出了一种适用于CHB-PET闭锁状态的戴维南-诺顿等效建模及状态变量共享集成方法，解决了多工况高效仿真的难点。
  - 推导了部分闭锁与完全闭锁状态下的戴维南-诺顿等效参数，明确了闭锁阶段的电路特征。
  - 提出了闭锁等效模型与非闭锁模型共用状态变量存储单元的集成方法，提升了多工况切换的兼容性。
- **考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型**
  - 💡 通过导纳互差并联耦合宽频导纳子模型与电磁对偶非线性子模型，实现了同时兼顾CVT宽频特性与中间变压器饱和非线性的精确建模。
  - 提出基于状态方程离散化与诺顿等效的CVT宽频导纳子模型构建方法。
  - 基于电磁对偶原理建立计及中间变压器铁芯饱和特性的工频非线性子模型。
### 2022年 (4篇)
- **A Transformer Model With Hysteresis Characteristics for Electromagnetic Transien**
  - 💡 将ATP-EMTP中Type96与BCTRAN结合的磁滞建模思想成功移植至PSCAD/EMTDC平台，提出了一种参数易得、便于工程应用的考虑磁滞特性的变压器电磁暂态仿真新模型。
  - 提出了一种在PSCAD/EMTDC中结合经典模型与磁滞励磁支路的三相变压器新模型。
  - 借鉴ATP-EMTP的Type96与BCTRAN建模思想，实现了仅需最大磁滞回线实测数据即可准确反映铁心磁滞特性的实用化建模方法。
- **Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Tran**
  - 💡 提出基于节点导纳预处理与短路导纳参数转换的DAB高频链路等效方法，突破传统详细模型计算瓶颈，实现固态变压器系统级电磁暂态仿真的高效加速。
  - 提出了一种针对MMC型固态变压器高频链路的加速电磁暂态等效模型。
  - 通过节点导纳方程预处理与短路导纳参数转换显著降低了系统矩阵阶数与计算复杂度。
- **Electromagnetic Modeling of Transformers in EMT-Type Software by a Circuit-Based**
  - 💡 将有限元级别的详细几何与磁路建模转化为纯电路形式，实现了在EMT软件中高效、精确地模拟变压器内部电磁行为及故障。
  - 提出了一种完全基于电路的变压器建模方法，可直接无缝集成于EMT型仿真软件中。
  - 实现了变压器详细几何结构与磁通路径的建模，并考虑铁芯饱和效应，精度可与有限元法媲美。
- **New Compact White-Box Transformer Model for the Calculation of Electromagnetic T**
  - 💡 通过电感耦合子矩阵降阶技术实现变压器白盒模型的紧凑化，在维持高计算精度的同时突破了传统模型规模过大导致的软件兼容性与计算效率瓶颈。
  - 提出了一种用于电磁暂态计算的新型紧凑型变压器白盒模型。
  - 通过降低主绕组分段与阻尼辅助回路间电感耦合子矩阵的秩，实现了模型规模的缩减。
### 2023年 (5篇)
- **A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized**
  - 💡 将多绕组变压器详细建模、子模块解耦技术与并行计算架构相结合，实现了兼顾宽频带高精度与高计算效率的MSST电磁暂态仿真。
  - 提出了一种针对MSST子模块的解耦EMT建模方法，有效克服了复杂拓扑难以获取宽频带解析表达式的难题。
  - 建立了多绕组变压器的详细模型，完整保留了原始模型的宽频动态特性。
- **A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized**
  - 💡 提出了一种融合多绕组变压器详细建模、子模块解耦与并行计算架构的新型EMT仿真方法，在保留宽带动态特性的同时大幅提升了模块化固态变压器的仿真效率。
  - 提出了多绕组变压器的详细建模方法，解决了复杂子模块动态难以解析表达的问题。
  - 开发了子模块解耦EMT建模技术，有效克服了传统模型频带窄和精度不足的缺陷。
- **On-site measurement of the hysteresis curve for improved modelling of transforme**
  - 💡 提出并验证了利用便携式设备在现场直接测量变压器真实磁滞/饱和曲线的技术，有效解决了传统工厂测试数据缺失导致的EMT建模精度不足问题。
  - 提出了一种利用便携式测量系统在现场直接获取变压器磁滞与饱和曲线的方法。
  - 验证了基于实测曲线的建模方法相比传统有效值估算能显著提升EMT仿真精度。
- **Optimized high-frequency white-box transformer model for implementation in ATP-E**
  - 💡 提出了一套面向ATP-EMTP平台的高频白盒变压器模型降阶与适配方法论，解决了大型详细等效电路在EMTP软件中难以实现与易发数值不稳定的瓶颈问题。
  - 提出了三种通用的模型降阶方法，在不牺牲计算精度的前提下有效缩减了白盒变压器模型的规模。
  - 开发了针对ATP-EMTP环境的特定适配技术，解决了大型变压器详细等效电路在该软件中难以实现的问题。
- **一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型**
  - 💡 将半隐式延迟解耦技术引入CHB-PET仿真，通过矩阵分裂实现细粒度解耦与恒定导纳矩阵，突破了高维复杂拓扑电磁暂态仿真的效率瓶颈。
  - 基于状态方程与矩阵分裂及延迟技术，建立了双有源桥(DAB)的半隐式延迟解耦模型。
  - 推导了外端口及级联H桥在不同串并联组合下的等值解耦电路，实现了变换级与模块间的细粒度解耦。
### 2024年 (1篇)
- **Adaptive Variable Step Size Calculation Method for Transient Temperature Rise an**
  - 💡 将POD降阶技术与适用于非线性问题的αATS自适应变步长策略相结合，实现了变压器瞬态流热耦合问题的高精度与超高效计算。
  - 推导了变压器绕组瞬态温升计算的有限元离散方程。
  - 引入POD降阶算法，有效解决了传统瞬态计算中条件数过大及方程阶数过高的问题。
### 2025年 (4篇)
- **Enhancements to Terminal Duality-based models for three-phase multi-limb multi-w**
  - 💡 首次将零序路径电感与铁轭分布机制融入TDM框架，并结合参考节点稳定技术，实现了三柱多绕组变压器在不平衡工况下高精度、高稳定性的EMT建模。
  - 首次在三柱变压器TDM模型中引入零序路径电感，完善了不平衡工况下的磁路等效。
  - 推导了零序路径电感的闭合计算公式，确保模型开路零序阻抗与用户给定值精确匹配。
- **Multirate EMT Simulation of Power Electronic Transformers With High-Precision Fi**
  - 💡 提出结合高精度触发信号的多速率EMT仿真框架，通过频率驱动的子系统划分与交错等效交互算法，突破高频开关器件对仿真步长的限制，实现PET仿真效率与精度的双重提升。
  - 提出基于频率差异的PET多速率EMT仿真方法，为不同子系统分配优化的仿真时间步长。
  - 开发子系统间的数据传输方法与交错等效多速率交互算法，确保多速率协同与仿真稳定性。
- **Simplified EMT Model of Multiple-Active-Bridge Based Power Electronic Transforme**
  - 💡 首次将广义状态空间平均法与傅里叶分解结合，构建了兼顾高精度与超快仿真速度的含储能MAB-PET四端口等效EMT模型。
  - 提出基于开关函数法与Dommel算法的功率模块等效建模方法。
  - 构建多端口功率模块聚合模式的PET等效模型。
- **Universal Decoupled Equivalent Circuit Models of Solid-State Transformer for Acc**
  - 💡 结合开关函数、直流链路解耦与开关插值技术，构建了适用于复杂多模块固态变压器的通用高效EMT等效建模框架。
  - 提出基于开关函数的通用解耦等效电路模型，可统一适用于全桥、DAB及三电平等多种功率变换器。
  - 引入直流链路解耦策略实现恒定G矩阵，显著减少了EMT求解过程中的系统节点数量。
### 2026年 (2篇)
- **A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-Sta**
  - 💡 将隐式-显式Gear积分法、开关函数等效建模与步内开关插值技术深度融合，突破了传统SST电磁暂态仿真中计算效率与精度的瓶颈。
  - 提出基于隐式-显式Gear积分法的开关函数详细等效模型，实现高效准确的电磁暂态仿真。
  - 利用ImEx求解器特性实现电路解耦、节点缩减及常数导纳矩阵构建，提升数值稳定性。
- **Experimental research on high-voltage transformer transient characteristics**
  - 💡 将机电暂态与电磁暂态并行仿真技术结合在线数据接口，实现了无需系统等值即可在真实大电网背景下高精度检验高压线路保护装置。
  - 提出了一种基于机电-电磁暂态混合仿真的高压线路保护装置检验方案，避免了传统电磁暂态仿真的系统等值限制。
  - 开发了在线数据接口，实现了调度EMS系统实时数据断面自动导入仿真系统，还原真实电网运行工况。
## 关键发现汇总
- [1998] **Digital Time-Domain Investigation of Transient Behavior of C**: 所建模型能准确复现故障与开关操作等工况下CCVT输出波形的暂态偏差。
- [1998] **Digital Time-Domain Investigation of Transient Behavior of C**: 仿真成功捕捉并量化了铁磁谐振现象及其对保护继电器动作可靠性的潜在影响。
- [1998] **Digital Time-Domain Investigation of Transient Behavior of C**: 频域与时域联合分析表明，CCVT内部非线性电感与电容参数是决定其暂态保真度的核心因素。
- [1999] **电磁暂态计算中新的变压器模型**: 模型成功实现了非标准变比变压器的直接有名值计算，无需进行复杂的电压等级归算。
- [1999] **电磁暂态计算中新的变压器模型**: 与EMTP标准程序的计算结果对比表明，该模型在主要电磁暂态功能上具有高度一致性与正确性。
- [1999] **电磁暂态计算中新的变压器模型**: 新模型有效避免了传统理想变压器模型在空载运行时消元失败的问题，提升了数值求解的稳定性。
- [2004] **A high frequency transformer model for the EMTP - Power Deli**: 模型通过有理函数逼近导纳矩阵，在给定频率范围内准确表征变压器高频特性。
- [2004] **A high frequency transformer model for the EMTP - Power Deli**: RLC网络实现形式保证了模型可直接用于EMTP，无需额外转换或离散化。
- [2004] **A high frequency transformer model for the EMTP - Power Deli**: 相比传统内部绕组模型，该终端模型大幅降低了计算规模，适用于系统级暂态研究。
- [2004] **A transformer model for winding fault studies - Power Delive**: 所提模型能够准确复现变压器任意匝间与匝地故障的电磁暂态过程
- [2004] **A transformer model for winding fault studies - Power Delive**: 实验验证表明该故障模型具有较高的仿真精度与工程实用性
- [2004] **A Z-transform model of transformers for the study of electro**: 增益函数在50Hz至数千Hz频段幅值归一化接近1，高频段呈现明显谐振特性
- [2004] **A Z-transform model of transformers for the study of electro**: Z变换模型能准确拟合200MVA自耦变压器的实测频响数据
- [2004] **A Z-transform model of transformers for the study of electro**: 离散化模型有效避免了传统S平面卷积的复杂计算，适配EMT步进仿真
- [2004] **An improved low-frequency transformer model for use in GIC s**: 单相配电变压器的仿真波形与实测记录数据高度吻合。
- [2004] **An improved low-frequency transformer model for use in GIC s**: JA模型能够准确反映变压器铁芯的剩磁通量及GIC引起的半周波饱和现象。
- [2004] **An improved low-frequency transformer model for use in GIC s**: 集成模型有效兼顾了磁滞与涡流损耗，显著提升了低频地磁感应电流研究的仿真精度。
- [2004] **Digital Time-Domain Investigation of Transient Behavior of C**: EMTP仿真结果与Haefely-Trench实测数据高度吻合，验证了模型精度
- [2004] **Digital Time-Domain Investigation of Transient Behavior of C**: 模型能够准确复现并预测CCVT在故障和开关操作下的铁磁谐振现象
- [2004] **Digital Time-Domain Investigation of Transient Behavior of C**: 成功量化了不同组件参数及抑制装置对CCVT暂态响应的影响程度
- [2004] **Three phase transformer modelling for fast electromagnetic t**: 五种变压器模型在模拟小感性电流开断过电压时表现出显著的精度与可靠性差异
- [2004] **Three phase transformer modelling for fast electromagnetic t**: 包含频率相关电容和零序互感耦合的模型能最准确地复现实际过电压波形特征
- [2004] **Three phase transformer modelling for fast electromagnetic t**: 仿真结果与现场测试数据高度吻合，证实了推荐模型在快速暂态研究中的有效性
- [2009] **A link between EMTP-RV and FLUX3D for transformer energizati**: 耦合方法在测试算例中表现出良好的数值鲁棒性与足够的计算精度。
- [2009] **A link between EMTP-RV and FLUX3D for transformer energizati**: 成功结合EMTP的大规模网络建模能力与FLUX3D的铁芯几何及磁特性精细表征能力。
- [2009] **A link between EMTP-RV and FLUX3D for transformer energizati**: 能够准确捕捉五柱变压器等复杂结构中的磁通分布与饱和非线性效应。
- [2013] **Dual Reversible Transformer Model for the**: 模型在励磁涌流、串联铁磁谐振和GIC工况下的电磁暂态响应与实验室实测数据高度吻合。
- [2013] **Dual Reversible Transformer Model for the**: 该模型在深度饱和条件下能够准确复现从不同绕组侧驱动时产生的暂态行为差异。
- [2014] **EMTP model of a bidirectional multilevel solid state transfo**: 所建SST模型在不同运行工况下均能稳定实现双向功率流动与电压变换
- [2014] **EMTP model of a bidirectional multilevel solid state transfo**: 中压侧多电平拓扑结合PWM策略显著降低了注入电网的谐波含量
## 来源论文

| 论文 | 年份 |
|------|------|
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-voltage-transformer-13&14|Digital Time-Domain Investigation of Transient Behavior of C]] | 1998 |
| [[电磁暂态计算中新的变压器模型|电磁暂态计算中新的变压器模型]] | 1999 |
| [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-|A Z-transform model of transformers for the study of electro]] | 2004 |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP - Power Deli]] | 2004 |
| [[a-transformer-model-for-winding-fault-studies-power-delivery-ieee-transactions-o|A transformer model for winding fault studies - Power Delive]] | 2004 |
| [[an-improved-low-frequency-transformer-model-for-use-in-gic-studies|An improved low-frequency transformer model for use in GIC s]] | 2004 |
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo|Digital Time-Domain Investigation of Transient Behavior of C]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[a-link-between-emtp-rv-and-flux3d-for-transformer-energization-studies|A link between EMTP-RV and FLUX3D for transformer energizati]] | 2009 |
| [[dual-reversible-transformer-model-for-the-13&14|Dual Reversible Transformer Model for the]] | 2013 |
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio|EMTP model of a bidirectional multilevel solid state transfo]] | 2014 |
| [[interfacing-factor-based-white-box-transformer-modeling-method|Interfacing Factor-Based White-Box Transformer Modeling Meth]] | 2014 |
| [[analysing-a-power-transformers-internal-response-to-system-transients-using-a-hy|Analysing a power transformer⠒s internal response to system ]] | 2015 |
| [[duality-based-transformer-model-including-13&14|Duality-Based Transformer Model Including]] | 2015 |
| [[duality-based-transformer-modeling-for-low-frequency-transients|Duality-Based Transformer Modeling for Low-Frequency Transie]] | 2016 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[an-improved-high-frequency-white-box-lossy-transformer-model-for-the-calculation|An improved high frequency white-box lossy transformer model]] | 2017 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[application-of-duality-based-equivalent-circuits-for-modeling-multilimb-transfor|Application of Duality-Based Equivalent Circuits for Modelin]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[determination-of-the-saturation-curve-of-power-transformers-by-processing-transi|Determination of the saturation curve of power transformers ]] | 2021 |
| [[expanding-the-measuring-range-via-s-parameters-in-a-ehv-voltage-transformer-mode|Expanding the measuring range via S-parameters in a EHV volt]] | 2021 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[级联h桥型电力电子变压器的闭锁状态等效建模方法-33|级联H桥型电力电子变压器的闭锁状态等效建模方法]] | 2021 |
| [[级联h桥型电力电子变压器的闭锁状态等效建模方法-40|级联H桥型电力电子变压器的闭锁状态等效建模方法]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien|A Transformer Model With Hysteresis Characteristics for Elec]] | 2022 |
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Accelerated Electromagnetic Transient (EMT) Equivalent Model]] | 2022 |
| [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based|Electromagnetic Modeling of Transformers in EMT-Type Softwar]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized-03|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[a-novel-decoupled-emt-approach-and-parallel-simulation-framework-for-modularized|A Novel Decoupled EMT Approach and Parallel Simulation Frame]] | 2023 |
| [[on-site-measurement-of-the-hysteresis-curve-for-improved-modelling-of-transforme|On-site measurement of the hysteresis curve for improved mod]] | 2023 |
| [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e|Optimized high-frequency white-box transformer model for imp]] | 2023 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[adaptive-variable-step-size-calculation-method-for-transient-temperature-rise-and-fall|Adaptive Variable Step Size Calculation Method for Transient]] | 2024 |
| [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w|Enhancements to Terminal Duality-based models for three-phas]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |
| [[experimental-research-on-high-voltage-transformer-transient-characteristics|Experimental research on high-voltage transformer transient ]] | 2026 |
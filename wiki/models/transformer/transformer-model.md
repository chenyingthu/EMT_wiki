---
title: "变压器模型 (Transformer)"
type: model
tags: [transformer, hysteresis, saturation, frequency-dependent, white-box]
created: "2026-04-13"
updated: "2026-05-12"
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

## 量化性能边界

**Gustavsen 2019 HVDC变压器端口宽频黑盒建模**:
- 基于矢量网络分析仪和专用接线盒的5端口导纳扫频测量，频率范围 **5 Hz至10 MHz**
- 导纳矩阵拟合误差 **<1.5%**，并通过无源性验证（全频段特征值>0）
- 经特征值缩放后，50Hz工频励磁电流从测量虚高值恢复至实际水平，相对误差 **<3%**
- 模型提取计算耗时仅约 **1分钟**（CPU时间）
- 验证对象：法国-英国IFA2000工程单相206MVA HVDC变压器（400/√3, 118, 118/√3 kV）
- 完整HVDC链路仿真中，换相过电压峰值预测精度较传统"50Hz模型+杂散电容"提升约 **30%**
- 数据缺口：方法验证未覆盖铁心饱和、大扰动非线性或雷击/故障全场景

**Morched 1993 变压器高频EMTP端口等效模型**:
- 基于节点导纳矩阵有理函数逼近，模型有效频带 **60 Hz至200 kHz**
- 三相双绕组变压器经模态分解与矩阵平均后，需独立拟合的导纳函数从 **21个减少至6个**，计算效率提升约 **71%**
- 典型拟合配置：**6个实极点 + 15对复共轭极点**，表征集肤效应、涡流损耗及杂散电容
- 高频RC支路初始参数估计经优化后变化幅度通常 **<5%**
- 验证对象：125 MVA, 215/44 kV三相三柱式变压器（含不可访问Δ接第三绕组），阶跃响应与现场录波幅值、谐振频率及衰减时间常数一致
- EMTP长时暂态仿真（数秒级）无数值振荡或发散
- 数据缺口：缺少与更多容量等级、不同铁芯拓扑变压器的系统性对比验证

**Chandrasena 2004 配电变压器GIC低频模型**（3 kVA, 115 V/2300 V单相，M4硅钢片）:
- 基于Jiles-Atherton磁滞理论的改进变压器模型，在EMTDC中实现
- 额定工况（1.0 p.u., 60Hz）励磁电流RMS仿真误差 **1.98%**，功率因数误差仅 **3%**（实测0.672 vs 仿真0.692）
- 1.1 p.u.电压下，新模型励磁电流最大误差 **5.38%**，优于传统电阻模型的11.25%
- 1.1 p.u.时相位角偏差 **2.57°**，导致功率因数误差在高电压时扩大
- 数据缺口：验证仅基于单相小容量样机，未在大型三相多柱变压器和实际GIC注入场景下验证

**Jazebi 2015 对偶原理变压器宽频模型**（含涡流效应，1 kVA单相变压器）:
- 基于几何尺寸和材料参数的解析Cauer等效电路，适用 **1 Hz至1 MHz** 宽频范围
- 等效电阻与电感计算误差 **<5%**（对比有限元FEM）
- 忽略涡流效应时高频阻抗幅值误差 **>30%**，证明涡流建模对MHz级暂态至关重要
- 7阶模型有效预测范围延伸至 **15 MHz以上**；实验室实测谐振频率最大偏差约20%（归因于介电常数不确定性与制造公差）
- 数据缺口：主要验证两绕组单相变压器，三相多柱/非圆柱绕组结构的验证尚未充分展开

**Filizadeh 2025 大规模电网变压器与FDNE模型**:
- 大型电网基准系统（含202台变压器、58条线路、72台同步机），77极点FDNE覆盖 **1 Hz至1 kHz**，计算效率提升 **2.16倍**（10秒仿真：26秒→12秒）
- 12核并行架构实现 **14.4倍** 加速（含15,136个控制模块及非线性开关器件）
- 混合协同仿真中EMT子步长可设置为PDT步长的1/5
- 数据缺口：该文为综述性特写，FDNE加速数据来自大型电网而非变压器专项验证

**数据缺口声明**：变压器EMT建模的量化数据主要来自小容量单相样机（1-3 kVA）或特定工程对象（IFA2000 HVDC），不同拓扑、容量等级和铁芯结构的横向对比验证不充分。宽频模型的拟合精度和加速比高度依赖于测量条件、有理函数阶数和验证场景，不同研究间的直接比较需注意方法差异。

## 相关方法
- [[nodal-analysis]]
- [[vector-fitting]]
- [[state-space-method]]
- [[average-value-model]]
- [[dynamic-phasor]]
- [[numerical-integration]]
- [[interpolation-method]]
- [[passivity-enforcement]]
- [[fixed-admittance]]
- [[prony-analysis]]

## 相关模型
- [[fdne-model]]
- [[vsc-model]]
- [[mmc-model]]
- [[transmission-line-model]]
- [[cable-model]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[ferroresonance]]
- [[real-time-simulation]]
- [[parallel-computing]]
- [[co-simulation]]
- [[vsc-hvdc]]
- [[network-equivalent]]
- [[wind-farm-modeling]]


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
  - 💡 提出基于节点导纳预处理与短路导纳参数转换的DAB高频链路等效方法，贡献传统详细模型计算瓶颈，实现固态变压器系统级电磁暂态仿真的高效加速。
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
  - 💡 提出结合高精度触发信号的多速率EMT仿真框架，通过频率驱动的子系统划分与交错等效交互算法，贡献高频开关器件对仿真步长的限制，实现PET仿真效率与精度的双重提升。
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
## 来源论文

| 论文 | 年份 |
|------|------|
| [[电磁暂态计算中新的变压器模型|电磁暂态计算中新的变压器模型]] | 1999 |
| [[电磁暂态计算中新的变压器模型|电磁暂态计算中新的变压器模型]] | 1999 |
| [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-|A Z-transform model of transformers for the study of electro]] | 2004 |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP - Power Deli]] | 2004 |
| [[a-transformer-model-for-winding-fault-studies-power-delivery-ieee-transactions-o|A transformer model for winding fault studies - Power Delive]] | 2004 |
| [[an-improved-low-frequency-transformer-model-for-use-in-gic-studies|An improved low-frequency transformer model for use in GIC s]] | 2004 |
| [[computation-of-the-periodic-steady-state-in-systems-with-nonlinear-components-us|Computation of the periodic steady state in systems with non]] | 2004 |
| [[decision-tree-based-methodology-for-high-impedance-fault-detection|Decision tree-based methodology for high impedance fault det]] | 2004 |
| [[modelling-of-circuit-breakers-in-the-electromagnetic-transients-program-power-sy|Modelling of circuit breakers in the Electromagnetic Transie]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee|Multiphase power flow solutions using EMTP and Newtons metho]] | 2004 |
| [[power-converter-simulation-module-connected-to-the-emtp-power-systems-ieee-trans|Power converter simulation module connected to the EMTP - Po]] | 2004 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power|Using TACS Functions Within EMPT To Teach Protective Relayin]] | 2004 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[noda-a-binary-frequency-region-partitioning-algorithm-for-the-identification-of-|Noda | A Binary Frequency-Region Partitioning Algorithm for ]] | 2007 |
| [[numerical-integration-by-the-2-stage-diagonally|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2008 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode|Including Magnetic Saturation in Voltage-Behind-Reactance In]] | 2010 |
| [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat|Modeling of ac machines using a voltage-behind-reactance for]] | 2010 |
| [[能量回馈型电力电子负载的控制方法|能量回馈型电力电子负载的控制方法]] | 2010 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[magnetically-saturable-voltage-behind-reactance-model-for-induction-machines|Magnetically Saturable Voltage Behind Reactance Model for In]] | 2011 |
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 |
| [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Comparison between electromechanical transient model and ele]] | 2013 |
| [[development-of-data-translators-for-interfacing-13&14|Development of Data Translators for Interfacing Power-Flow P]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio|EMTP model of a bidirectional multilevel solid state transfo]] | 2014 |
| [[基于adpss的电力系统和牵引供电系统机电电磁暂态混合仿真|基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[analysing-a-power-transformers-internal-response-to-system-transients-using-a-hy|Analysing a power transformer⠒s internal response to system ]] | 2015 |
| [[duality-based-transformer-model-including-13&14|Duality-Based Transformer Model Including]] | 2015 |
| [[duality-based-transformer-modeling-for-low-frequency-transients|Duality-Based Transformer Modeling for Low-Frequency Transie]] | 2016 |
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror|Saturable reactor hysteresis model based on Jiles–Atherton f]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t-22|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[small-signal-dynamic-phasor-model-of-three-phase-dab-converter-for-solid-state-t|Small Signal Dynamic Phasor Model of Three-Phase DAB Convert]] | 2018 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[mmc-upfc电磁-机电混合仿真技术研究|MMC-UPFC电磁-机电混合仿真技术研究]] | 2019 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[stability-of-algorithms-for-electro-magnetic-transient-simulation-of-networks-wi|Stability of Algorithms for Electro-Magnetic-Transient Simul]] | 2019 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co|Analysis of low frequency interactions of DFIG wind turbine ]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[基于模块化双有源桥变流器的直流变电站设计方案|基于模块化双有源桥变流器的直流变电站设计方案]] | 2020 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[determination-of-the-saturation-curve-of-power-transformers-by-processing-transi|Determination of the saturation curve of power transformers ]] | 2021 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat|Modelica-based simulation of electromagnetic transients usin]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[级联h桥型电力电子变压器的闭锁状态等效建模方法-33|级联H桥型电力电子变压器的闭锁状态等效建模方法]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien|A Transformer Model With Hysteresis Characteristics for Elec]] | 2022 |
| [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien|A Transformer Model With Hysteresis Characteristics for Elec]] | 2022 |
| [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix|Analysis and Prospect of Development of China]] | 2022 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir|Characteristic Analysis of High-frequency Resonance of Flexi]] | 2022 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode|Efficient steady state analysis of the grid using electromag]] | 2022 |
| [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based|Electromagnetic Modeling of Transformers in EMT-Type Softwar]] | 2022 |
| [[electromagnetic-modeling-of-inductors-in-emt-type-software-by-three-circuit-base|Electromagnetic modeling of inductors in EMT-type software b]] | 2022 |
| [[electromechanical-electromagnetic-hybrid-simulation-technology-with-large-number|Electromechanical-electromagnetic Hybrid Simulation Technolo]] | 2022 |
| [[electromechanical-electromagnetic-transient-hybrid-simulation-of-an-acdc-hybrid-|Electromechanical-electromagnetic transient hybrid simulatio]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte|Multi-timescale simulator of nonlinear electrical elements b]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb|The Averaged-value Model of a Flexible Power Electronics Bas]] | 2022 |
| [[the-averaged-value-model-of-a-flexible-power-electronics-based-substation-in-hyb|The Averaged-value Model of a Flexible Power Electronics Bas]] | 2022 |
| [[基于umec的双芯sen变压器电磁暂态模型|基于UMEC的双芯Sen变压器电磁暂态模型]] | 2022 |
| [[基于umec的双芯sen变压器电磁暂态模型|基于UMEC的双芯Sen变压器电磁暂态模型]] | 2022 |
| [[级联h桥型电力电子变压器的电磁暂态等效建模方法|级联H桥型电力电子变压器的电磁暂态等效建模方法]] | 2022 |
| [[级联h桥型电力电子变压器的电磁暂态等效建模方法|级联H桥型电力电子变压器的电磁暂态等效建模方法]] | 2022 |
| [[高频隔离型电力电子变压器电磁暂态加速仿真方法与展望|高频隔离型电力电子变压器电磁暂态加速仿真方法与展望]] | 2022 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[electromagnetic-transient-emt-simulation-algorithms-for-evaluation-of-large-scal|Electromagnetic Transient (EMT) Simulation Algorithms for Ev]] | 2023 |
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie|Equivalent Modeling Method of Parallel Elements for Fast Ele]] | 2023 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[on-site-measurement-of-the-hysteresis-curve-for-improved-modelling-of-transforme|On-site measurement of the hysteresis curve for improved mod]] | 2023 |
| [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e|Optimized high-frequency white-box transformer model for imp]] | 2023 |
| [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp|Real-time simulation for detailed wind turbine model based o]] | 2023 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[analytical-calculation-method-of-outer-loop-controller-parameters-of-hvdc-conver|Analytical Calculation Method of Outer Loop Controller Param]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[accelerating-electromagnetic-transient-simulations-using-graphical-processing-un|Accelerating electromagnetic transient simulations using gra]] | 2025 |
| [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc|Analysis on dynamic characteristic of control mode for +/-80]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers Wi]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[中-国-电-机-工-程-学-报-37|中  国  电  机  工  程  学  报]] | 2025 |
| [[基于fpga的变电站实时仿真培训系统|基于FPGA的变电站实时仿真培训系统]] | 2025 |
| [[electromechanical-transientelectromagnetic-transient-hybrid-simulation-method-co|Electromechanical transientelectromagnetic transient hybrid ]] | 2026 |
| [[experimental-research-on-high-voltage-transformer-transient-characteristics|Experimental research on high-voltage transformer transient ]] | 2026 |
| [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el|Modeling of cross-magnetization effects in saturated synchro]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |

## 深度增强内容

## 1. 各类模型数学描述

### 1.1 磁滞-饱和详细模型 (Jiles-Atherton based)

针对铁磁谐振与励磁涌流分析，基于Jiles-Atherton理论的磁滞模型数学描述如下：

**无磁滞磁化强度（Anhysteretic Magnetization）**：
$$M_{an} = M_s \left[ \coth\left(\frac{H_{eff}}{a}\right) - \frac{a}{H_{eff}} \right]$$

其中有效磁场强度 $H_{eff} = H + \alpha M$，$M_s$为饱和磁化强度，$a$为形状参数，$\alpha$为内部耦合系数。

**磁滞微分方程**：
$$\frac{dM}{dH} = \frac{M_{an} - M}{\delta k - c(M_{an} - M)}$$

其中 $\delta = \text{sign}(dH/dt)$ 表示磁场变化方向，$k$为磁滞损耗系数，$c$为可逆磁化系数。

**分段线性插值实现**：
对于PSCAD/EMTDC实现，采用可变电感法：
$$L_{eq}(i_m) = \frac{\lambda_{max}}{i_{m}} \cdot \frac{B(i_m)}{H(i_m)}$$

通过闭环控制逻辑实时跟踪磁滞回线工作点，主次磁滞回线簇通过最大磁滞回线的分段线性插值生成：
$$\lambda_{minor}(i) = \lambda_{major}(i) \cdot k_{scale} + \lambda_{offset}$$

### 1.2 高频白盒状态空间模型 (Interfacing Factor Based)

基于接口因子法的白盒变压器模型采用状态空间描述：

**连续时间状态方程**：
$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

其中状态向量 $\mathbf{x} = [\mathbf{v}_{int}^T, \mathbf{i}_{L}^T]^T$ 包含内部节点电压和电感支路电流，输入 $\mathbf{u}$ 为外部端子电压。

**诺顿等效接口**：
通过梯形积分离散化（步长 $\Delta t$），得到EMTP兼容的诺顿等效：
$$\mathbf{i}_{eq}(t) = \mathbf{G}_{eq}\mathbf{v}(t) + \mathbf{i}_{hist}(t-\Delta t)$$

等效电导矩阵：
$$\mathbf{G}_{eq} = \mathbf{C}(\mathbf{I} - \frac{\Delta t}{2}\mathbf{A})^{-1}\frac{\Delta t}{2}\mathbf{B} + \mathbf{D}$$

**对角化优化**：
通过对角化变换 $\mathbf{x} = \mathbf{T}\mathbf{z}$，将状态矩阵 $\mathbf{A}$ 转换为模态形式 $\mathbf{\Lambda} = \text{diag}(\lambda_1, \lambda_2, ..., \lambda_n)$，降低65%-70%的计算耗时。

### 1.3 对偶Cauer电路模型 (Duality-Based Model)

基于磁路-电路对偶原理的双侧Cauer等效模型：

**磁路方程**：
$$\frac{d\Phi_k}{dt} = -\sum_{j=1}^{n} R_{mj}\Phi_j + N_k i_k$$

其中 $R_{mj}$ 为磁阻，$\Phi_j$ 为磁通，$N_k$ 为绕组匝数。

**对偶电路转换**：
通过 $v = d\Phi/dt$ 和 $i = \mathcal{F}/N$ 的变量替换，得到双侧Cauer网络：
$$v_k = L_{k}\frac{di_k}{dt} + \sum_{j\neq k} M_{kj}\frac{di_j}{dt} + R_k i_k$$

**频变参数解析计算**：
基于麦克斯韦方程的几何参数解析公式：
$$L_{leak}(\omega) = \mu_0 N^2 \frac{h}{b} \cdot \frac{1}{3}\left(1 + \frac{b}{w}\right) \cdot F_{skin}(\omega)$$

$$R_{ac}(\omega) = R_{dc} \cdot \left[1 + \frac{(m^2-1)}{3}\cdot \Delta^4\right], \quad \Delta = \frac{d_{wire}}{\delta_{skin}}$$

其中 $\delta_{skin} = \sqrt{\frac{2\rho}{\omega\mu}}$ 为集肤深度。

### 1.4 广义动态相量模型 (GSSA) - 适用于SST

针对固态变压器(SST)中的双有源桥(DAB)变换器，建立混合动态相量模型：

**动态相量定义**：
$$\langle x \rangle_k(t) = \frac{1}{T}\int_{t-T}^t x(\tau)e^{-jk\omega_s\tau}d\tau$$

**状态空间平均混合模型**：
$$\frac{d}{dt}\langle \mathbf{x} \rangle_k = (\mathbf{A}_k - jk\omega_s\mathbf{I})\langle \mathbf{x} \rangle_k + \sum_{i}\mathbf{B}_{k-i}\langle \mathbf{u} \rangle_i$$

对于三相DAB，保留基波和3次谐波（$k = \pm 1, \pm 3$），状态矩阵维度为8阶：
- SSA部分（电容电压）：2阶
- GSSA部分（三相电流实部/虚部）：6阶

相比开关级模型（>20阶），简化60%以上，在0至$f_s/2$频段内误差<3%。

### 1.5 黑盒S参数端口模型

用于GIS中VFTO（特快速暂态过电压）研究的宽带黑盒模型：

**多端口导纳矩阵**：
$$\mathbf{Y}(s) = \sum_{m=1}^{M}\frac{\mathbf{R}_m}{s-p_m} + \mathbf{D} + s\mathbf{E}$$

其中 $\mathbf{R}_m$ 为留数矩阵，$p_m$ 为极点（含实极点和共轭复极点对）。

**无源性约束**：
$$\mathbf{Y}(s) + \mathbf{Y}^H(s) \geq 0, \quad \forall s=j\omega$$

**S参数转换**：
$$\mathbf{S} = (\mathbf{Y}_0 - \mathbf{Y})(\mathbf{Y}_0 + \mathbf{Y})^{-1}$$

测量频带扩展至50 MHz，幅频特性拟合误差<3%。

### 1.6 绕组故障详细模型

基于线圈分割法的内部故障模型：

**扩展电感矩阵**：
将标准6阶BCTRAN矩阵扩展为7阶（匝地故障）或8阶（匝间故障）：
$$\mathbf{L}_{fault} = \begin{bmatrix} 
\mathbf{L}_{11} & \mathbf{L}_{12} & \mathbf{L}_{1f} \\
\mathbf{L}_{21} & \mathbf{L}_{22} & \mathbf{L}_{2f} \\
\mathbf{L}_{f1} & \mathbf{L}_{f2} & \mathbf{L}_{ff}
\end{bmatrix}$$

**故障子绕组电感计算**：
基于几何漏磁系数 $\sigma$：
$$L_f = \sigma \cdot \mu_0 N_f^2 \frac{A_{core}}{l_{mean}} \cdot k_c$$

其中 $k_c$ 为考虑绕组重叠区域的修正系数。

---

## 2. 仿真参数参考表

| 模型类型 | 关键参数 | 典型取值/范围 | 来源论文 |
|---------|---------|--------------|----------|
| **磁滞模型** | 饱和磁化强度 $M_s$ | 1.6-2.0 T (硅钢片) | A Transformer Model With Hysteresis |
| | 磁滞损耗系数 $k$ | 20-50 A/m | |
| | 插值段数 | 最大回线分段：20-50段 | |
| **高频白盒** | 有效频带 | 60 Hz - 200 kHz | A high frequency transformer model |
| | 有理函数极点 | 6实极点 + 15对复极点 | |
| | 导纳矩阵维度 | 21个→6个（模态分解后） | |
| | 拟合误差 | <5%（高频阻抗） | |
| **紧凑白盒** | 原矩阵维度 | 1278×1278 (n=213段, N=5组) | New Compact White-Box |
| | SVD降秩后 | $\sum r_k \ll 1065$ | |
| | 电感分支数 | 817,281→可处理范围 | |
| **动态相量** | 保留谐波次数 | $k=\pm1,\pm3$ | Small Signal Dynamic Phasor |
| | 状态矩阵维度 | 8阶（总） | |
| | 适用频段 | 0 - $f_s/2$ (如0-5kHz) | |
| | 相移控制范围 | $0^\circ \leq d \leq 90^\circ$ | |
| **阻尼因子** | 状态变量数 $N$ | 88 (案例变压器) | Time-Domain Implementation |
| | 外部端子 $n_1$ | 6 | |
| | 内部节点 $n_2$ | 40 | |
| | 初始化误差 | $<10^{-12}$ | |
| **对偶Cauer** | 等效电路阶数 | 2阶(至1MHz), 7阶(至15MHz) | Duality-Based Transformer Model |
| | 涡流电阻 $R_{eddy}$ | 频变：$R_{ac} \propto \sqrt{f}$ | |
| **S参数** | 测量频带 | DC - 50 MHz | Expanding the measuring range |
| | 端口数 | 多端口（一次/二次/接地） | |
| **故障模型** | 漏磁系数 $\sigma$ | 0.01-0.5（随故障位置变化） | A transformer model for winding fault |
| | 电流误差 | <10%（幅值/相位） | |
| **GIC模型** | 低频扩展 | 0.01-100 Hz | An improved low-frequency model |
| | 额定工况误差 | 1.98% (电流RMS) | |
| | 功率因数误差 | 3% | |

---

## 3. 模型选择指南

### 3.1 按暂态 phenomena 选择

| 应用场景 | 推荐模型 | 关键特性 | 计算成本 |
|---------|---------|---------|---------|
| **励磁涌流分析** | 磁滞-饱和模型 (Jiles-Atherton) | 剩磁追踪、主次回线、铁芯饱和 | 中 |
| **铁磁谐振研究** | 对偶电路模型 + 磁滞 | 非线性电感拓扑、磁滞损耗 | 中-高 |
| **雷电冲击/VFTO** | 高频白盒或S参数黑盒 | 宽频(>1MHz)、杂散电容、集肤效应 | 高 |
| **GIC/直流偏磁** | 低频改进模型 + 涡流 | 0.01-1Hz精确、半波饱和、热效应 | 低-中 |
| **内部故障定位** | 扩展BCTRAN/线圈分割 | 子绕组互感、故障端口建模 | 中 |
| **固态变压器(SST)** | 动态相量模型(GSSA) | 开关平均、宽频小信号、多端口 | 低 |
| **实时仿真(RTDS)** | 接口因子白盒 + 对角化 | 准实时(步长1μs)、诺顿等效 | 中 |
| **大规模系统仿真** | 紧凑降阶模型 (SVD) | 低秩近似、ATP兼容 | 低 |

### 3.2 按频率范围选择

- **工频-低频(0-1kHz)**：对偶电路模型或改进GIC模型，重点考虑磁滞和涡流损耗
- **中频(1kHz-100kHz)**：阻尼因子白盒模型，适用于操作过电压
- **高频(100kHz-50MHz)**：S参数黑盒或高频白盒模型，考虑绕组电容和波过程

### 3.3 按数据可用性选择

- **设计参数完整**：白盒模型（基于几何尺寸）
- **仅端口测试数据**：黑盒模型（矢量拟合/Y参数）
- **有限元辅助**：混合灰盒模型（白/黑盒融合）

---

## 4. 前沿研究方向

### 4.1 模型降阶与计算效率优化
基于**奇异值分解(SVD)的低秩分解**技术，将大规模白盒模型（如1278阶电感矩阵）压缩为紧凑等效电路，同时保持宽频精度。最新研究实现：
- 辅助回路数量从1065个降至$\sum r_k$（有效秩）
- ATP-EMTP元件数量限制突破（从10^6级降至可处理范围）
- 六种不同降阶变体适配不同精度-效率权衡需求

### 4.2 宽频统一建模
开发覆盖**工频至MHz**的统一变压器模型，解决传统分段模型（低频磁路 vs 高频电路）的不连续问题：
- 双侧Cauer电路实现1Hz-15MHz连续建模
- 接口因子法实现状态空间与EMTP求解器无缝集成
- 零额外节点的电阻网络优化，消除数值振荡

### 4.3 多物理场耦合
- **磁-热耦合**：在GIC研究中集成涡流损耗与热点温度计算
- **磁-机械耦合**：变压器振动与铁芯磁致伸缩的联合建模

### 4.4 数据驱动与混合建模
- **白/灰盒融合**：结合有限元仿真（FLUX3D）与端口测量（S参数），解决高阻抗端子低频测量精度问题（误差从>15%降至<3%）
- **现场数据验证**：利用实际开关暂态录波数据校准模型参数

### 4.5 电力电子化变压器建模
针对**固态变压器(SST)**和**电力电子变压器(PET)**：
- 双有源桥(DAB)的广义状态空间平均(GSSA)模型，保留谐波交互
- 级联H桥(CHB)闭锁状态的戴维南-诺顿等效建模
- 高频链路(HFL)的宽频阻抗建模

### 4.6 内部故障与保护配合
- **分布式参数故障模型**：基于线圈分割的精确故障定位，漏磁系数随故障位置非线性变化建模
- **内部过电压评估**：阻尼因子模型计算内部节点过电压（可达2.5-3.0 pu），为绝缘配合提供依据

### 4.7 实时仿真与硬件在环(HIL)
- **并行仿真框架**：解耦EMT方法实现多核并行加速
- **FPGA实现**：基于状态空间的实数运算优化（复数转2×2实数块矩阵），支持步长1μs的准实时仿真

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

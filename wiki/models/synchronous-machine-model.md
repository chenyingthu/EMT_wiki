---
title: "同步电机模型 (Synchronous Machine)"
type: model
tags: [synchronous-machine, generator, park, vbr, phase-domain]
created: "2026-04-13"
---

# 同步电机模型 (Synchronous Machine)

## 概述

同步电机是电力系统中最主要的发电设备，其EMT建模需要准确表征电磁暂态过程中的定子、转子绕组耦合关系以及磁路饱和特性。

## 主要模型类型

### 1. 经典模型
- Park变换（dq0轴）
- 恒定磁链假设
- 适用于机电暂态

### 2. 相域模型
- 直接在abc坐标系下建模
- 无需坐标变换
- 十二相同步电机相域模型
- 适合不对称工况

### 3. VBR模型（电压源后向转子）
- Voltage Behind Reactance
- 提高数值稳定性
- 适用于EMT-机电混合仿真

### 4. 交叉磁化模型
- 饱和交叉磁化效应
- d-q轴耦合
- 适用于饱和工况

### 5. 等值聚合模型
- 风电场同步机聚合
- 保留动态特性
- 大规模系统简化

## 关键技术

### 电磁暂态建模
- 定子绕组暂态
- 转子回路暂态
- 阻尼绕组效应

### 饱和处理
- 开路饱和曲线
- 负载饱和特性
- 交叉饱和效应

### 接口技术
- 与EMT仿真器的接口
- 混合仿真中的等值
- 可变步长适应性

## 应用场景

- 短路故障分析
- 励磁系统研究
- 稳定性分析
- 机电-电磁混合仿真
- 不对称运行分析

## 相关方法
- [[state-space-method]]
- [[nodal-analysis]]

## 相关主题
- [[co-simulation]]
- [[network-equivalent]]


## 论文方法分析
> 基于 11 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 电压后电抗(VBR)建模 | 2 | A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type |
| 节点分析法 | 2 | An Efficient Phase Domain Synchronous Machine Model With Constant Equi |
| 相域建模技术 | 1 | A phase-domain synchronous machine modeling technique by using magneti |
| 磁路表示法 | 1 | A phase-domain synchronous machine modeling technique by using magneti |
| 基本电路元件等效 | 1 | A phase-domain synchronous machine modeling technique by using magneti |
| EMT仿真程序(XTAP)集成 | 1 | A phase-domain synchronous machine modeling technique by using magneti |
| EMTP型节点分析法 | 1 | A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type |
| dq/abc混合坐标系离散化 | 1 | A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type |
| 非迭代同步接口技术 | 1 | A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type |
| 相域建模 | 1 | An Efficient Phase Domain Synchronous Machine Model With Constant Equi |
| 诺顿等效电路 | 1 | An Efficient Phase Domain Synchronous Machine Model With Constant Equi |
| 恒定等效导纳矩阵 | 1 | An Efficient Phase Domain Synchronous Machine Model With Constant Equi |
| 方程重构优化 | 1 | An Efficient Phase Domain Synchronous Machine Model With Constant Equi |
| 基于Modelica的声明式/方程建模 | 1 | Electromagnetic Transient Modeling of Asynchronous Machine in Modelica |
| 变步长数值求解器 | 1 | Electromagnetic Transient Modeling of Asynchronous Machine in Modelica |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 同步电机 | 4 |
| 励磁绕组 | 2 |
| 电枢绕组 | 1 |
| 转子绕组 | 1 |
| 阻尼绕组 | 1 |
| 同步电机(full-order) | 1 |
| VBR同步电机模型 | 1 |
| 单机无穷大系统(SMIB) | 1 |
| 恒定电导相域模型(CC-PD) | 1 |
| 电抗后电压模型(VBR) | 1 |
| 三相鼠笼式异步电机（单笼与双笼） | 1 |
| 绕线式异步电机 | 1 |
| 三相异步电机 | 1 |
| 鼠笼式感应电机（单笼与双笼） | 1 |
| 绕线式转子电机 | 1 |
### 验证方式分布
- **仿真/对比**: 4 篇
- **仿真对比**: 2 篇
- **仿真与对比**: 2 篇
- **仿真**: 1 篇
- **仿真对比验证**: 1 篇
- **实验**: 1 篇
## 技术演进脉络
### 2006年 (1篇)
- **A Voltage-Behind-Reactance Synchronous Machine Model for the EMTP-Type Solution**
  - 💡 提出了一种结合dq/abc混合坐标与EMTP节点分析的非迭代同步接口VBR同步电机模型，实现了高精度与高效率的统一。
  - 将电压后电抗(VBR)公式扩展至EMTP型节点分析求解框架
  - 实现了电机模型与外部网络的非迭代、同步接口
### 2007年 (1篇)
- **Re-examination of Synchronous Machine**
  - 💡 首次系统论证了三种主流同步电机EMT模型的连续域等价性，并明确了离散化接口下VBR模型的精度优势。
  - 证明了dq模型、相域模型和电压后电抗模型在连续时间域内数学等价。
  - 验证了三种模型均适用于电力系统不对称运行工况。
### 2013年 (1篇)
- **Synchronous Machine Exciter Circuit Model In A**
  - 💡 基于MANA公式实现同步电机励磁绕组与外部励磁电路的直接同步电气连接，突破了传统补偿方法的拓扑限制。
  - 实现了基于MANA公式的相域同步电机模型，提供与励磁绕组的直接同步电气连接。
  - 提出了一种简单的电流源接口，可将励磁电路无缝接入现有的dq0型同步电机模型。
### 2018年 (1篇)
- **Field Validated Generic EMT-Type Model of a Full Converter Wind Turbine Based on**
  - 💡 提出了一种结合开关等效电路与平均值模型的通用混合EMT建模方法，在保证仿真精度的同时大幅提升计算速度，并通过现场实测数据验证了IV型风电机组模型的工程适用性。
  - 提出了一种针对特定IV型风电机组的通用EMT模型，有效克服了制造商黑盒模型限制分析的问题。
  - 开发了基于新型开关等效电路和平均值模型的混合EMT架构，支持采用更大仿真步长。
### 2019年 (1篇)
- **An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Adm**
  - 💡 提出了一种无需人工阻尼绕组且导纳矩阵恒定的相域同步电机建模方法，通过方程重构实现了EMTP仿真中计算效率与精度的双重提升。
  - 提出了一种适用于EMTP仿真的新型相域同步电机模型，其等效导纳矩阵为常数且与转子位置无关。
  - 通过重构电机方程，将模型表示为并联恒定诺顿导纳的电流源形式，显著降低了计算负担。
### 2022年 (1篇)
- **Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation**
  - 💡 首次将相域建模与恒定电导技术结合应用于十二相同步电机，实现了EMTP型仿真中高精度接口与高效率计算的统一。
  - 推导了适用于EMTP型电磁暂态仿真的十二相同步电机连续时间相域模型。
  - 提出了恒定电导相域（CC-PD）模型，避免了每个时间步网络电导矩阵的重复分解。
### 2023年 (1篇)
- **A phase-domain synchronous machine modeling technique by using magnetic circuit **
  - 💡 将变压器建模中成熟的磁路表示法创新性地应用于同步电机相域建模，实现了无需dq0变换且仅由基本电路元件构成的高精度EMT模型。
  - 提出了一种仅使用基本电路元件的同步电机相域建模新方法。
  - 引入磁路表示法替代传统时变电感矩阵，彻底避免了dq0坐标变换。
### 2024年 (3篇)
- **Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy**
  - 💡 将声明式方程建模语言Modelica与变步长求解器引入异步机电磁暂态仿真，突破了传统固定步长过程式编程的局限。
  - 在Modelica环境中完整实现了三种参考坐标系下的异步机电磁暂态模型
  - 系统评估并验证了Modelica模型在仿真精度与计算性能方面的表现
- **Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy**
  - 💡 将声明式方程建模语言Modelica与变步长求解器结合应用于异步电机电磁暂态仿真，突破了传统固定步长伴随电路法的编程与效率局限。
  - 在Modelica中完整实现了三种参考系下的三相鼠笼式及绕线式异步电机的电磁暂态模型。
  - 系统对比并验证了Modelica声明式建模与传统EMTP程序化建模在精度与计算性能上的差异。
- **Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in **
  - 💡 将频率平移与人工阻尼绕组技术结合，在相域构建了具有恒定电导矩阵的同步电机模型，突破了传统EMT仿真中时间步长与精度的制约。
  - 提出基于相域解析信号的同步电机模型，实现与外部网络的直接接口。
  - 应用频率平移技术消除定子交流载波，支持大时间步长仿真。
### 2026年 (1篇)
- **Modeling of cross-magnetization effects in saturated synchronous machines for el**
  - 💡 提出基于MMF幅值与相角的饱和评估方法，在EMT同步机模型中显式引入交叉磁化效应，突破了传统d/q轴独立饱和建模的局限
  - 开发了将交叉磁化效应纳入饱和算法的EMT同步机模型
  - 提出基于磁动势(MMF)幅值和相角的饱和评估新方法
## 关键发现汇总
- [2006] **A Voltage-Behind-Reactance Synchronous Machine Model for the**: 所提模型在仿真中展现出比现有EMTP电机模型更高的计算精度
- [2006] **A Voltage-Behind-Reactance Synchronous Machine Model for the**: 非迭代接口显著提升了电磁暂态仿真的计算效率
- [2006] **A Voltage-Behind-Reactance Synchronous Machine Model for the**: 有效避免了传统补偿法中的迭代收敛问题或诺顿等效的一步延迟
- [2007] **Re-examination of Synchronous Machine**: 三种同步电机模型在连续时间域的微分方程可相互代数推导，本质完全等价。
- [2007] **Re-examination of Synchronous Machine**: 计算机仿真表明所有模型均可准确模拟单机无穷大系统的不对称故障运行。
- [2007] **Re-examination of Synchronous Machine**: 离散化后与EMTP网络接口时，VBR模型因结构优势展现出最高的仿真精度。
- [2013] **Synchronous Machine Exciter Circuit Model In A**: MANA相域模型成功实现了励磁电路与电机绕组的同步精确求解，避免了传统补偿法的拓扑限制与精度损失。
- [2013] **Synchronous Machine Exciter Circuit Model In A**: 电流源接口有效兼容现有dq0模型，为励磁系统暂态性能及故障条件分析提供了可靠工具。
- [2018] **Field Validated Generic EMT-Type Model of a Full Converter W**: 混合模型架构允许使用更大的仿真时间步长，显著提升了电磁暂态仿真的计算效率。
- [2018] **Field Validated Generic EMT-Type Model of a Full Converter W**: 模型动态响应与现场实测数据高度一致，证明了其在实际工况下的准确性与可靠性。
- [2018] **Field Validated Generic EMT-Type Model of a Full Converter W**: 所实现的故障穿越控制策略能够有效应对电网扰动，满足并网规范要求。
- [2019] **An Efficient Phase Domain Synchronous Machine Model With Con**: 所提模型在电磁暂态仿真中保持了与传统模型一致的精度。
- [2019] **An Efficient Phase Domain Synchronous Machine Model With Con**: 恒定导纳矩阵消除了转子位置变化导致的矩阵频繁更新，大幅提升了计算速度。
- [2019] **An Efficient Phase Domain Synchronous Machine Model With Con**: 对比测试表明，该模型的计算效率显著优于现有的恒定电导相域模型和电抗后电压模型。
- [2022] **Phase-domain model of twelve-phase synchronous machine for E**: 所提PD模型有效消除了qd0模型的接口误差，在大步长仿真下仍保持数值稳定性。
- [2022] **Phase-domain model of twelve-phase synchronous machine for E**: CC-PD模型通过固定网络电导矩阵显著减少了计算量，大幅提升了含十二相电机系统的仿真效率。
- [2022] **Phase-domain model of twelve-phase synchronous machine for E**: 测试结果表明两种模型在电磁暂态分析中均具备高精度与高计算效率。
- [2023] **A phase-domain synchronous machine modeling technique by usi**: 在无限大母线系统仿真中，所提模型的电气与机械动态响应与传统同步电机模型高度一致。
- [2023] **A phase-domain synchronous machine modeling technique by usi**: 该模型成功克服了传统Park模型在三相不平衡（如电枢内部短路）工况下无法使用的局限。
- [2024] **Electromagnetic Transient Modeling of Asynchronous Machine i**: 基于Modelica与变步长求解器的模型在电机顺序启动仿真中实现了快速且高精度的时域计算
- [2024] **Electromagnetic Transient Modeling of Asynchronous Machine i**: 声明式建模显著提升了代码抽象层级与可读性，避免了传统过程式编程的繁琐实现
- [2024] **Electromagnetic Transient Modeling of Asynchronous Machine i**: 基于Modelica与变步长求解器的模型在电机顺序启动仿真中实现了快速且高精度的时域响应。
- [2024] **Electromagnetic Transient Modeling of Asynchronous Machine i**: 声明式建模在保持与传统固定步长法同等精度的同时，显著提升了代码的简洁性与模型可维护性。
- [2024] **Multi-scale Modeling of Synchronous Machine With Constant Co**: 模型在保持高精度的同时显著提升了多尺度暂态仿真的计算效率。
- [2024] **Multi-scale Modeling of Synchronous Machine With Constant Co**: 恒定电导矩阵避免了网络导纳矩阵的逐时步更新，有效支持了大时间步长计算。
- [2026] **Modeling of cross-magnetization effects in saturated synchro**: 基于MMF幅值与相角的方法能准确捕捉传统d/q轴解耦模型忽略的交叉磁化效应
- [2026] **Modeling of cross-magnetization effects in saturated synchro**: 传统简化假设会显著改变同步发电机负载能力的预测结果
- [2026] **Modeling of cross-magnetization effects in saturated synchro**: 新模型能有效复现同步发电机的时间常数、负载极限及短路电流等关键暂态行为
## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution|A Voltage-Behind-Reactance Synchronous Machine Model for the]] | 2006 |
| [[re-examination-of-synchronous-machine|Re-examination of Synchronous Machine]] | 2007 |
| [[synchronous-machine-exciter-circuit-model-in-a|Synchronous Machine Exciter Circuit Model In A]] | 2013 |
| [[field-validated-generic-emt-type-model-of-a-full-converter-wind-turbine-based-on|Field Validated Generic EMT-Type Model of a Full Converter W]] | 2018 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm|An Efficient Phase Domain Synchronous Machine Model With Con]] | 2019 |
| [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation|Phase-domain model of twelve-phase synchronous machine for E]] | 2022 |
| [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-|A phase-domain synchronous machine modeling technique by usi]] | 2023 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy--16|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[multi-scale-modeling-of-synchronous-machine-with-constant-conductance-matrix-in-|Multi-scale Modeling of Synchronous Machine With Constant Co]] | 2024 |
| [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el|Modeling of cross-magnetization effects in saturated synchro]] | 2026 |
---
title: "电缆模型 (Cable)"
type: model
tags: [cable, underground, submarine, frequency-dependent, multi-core]
created: "2026-04-13"
---

# 电缆模型 (Cable)

## 概述

电力电缆（地下电缆、海底电缆）的EMT建模需要考虑集肤效应、邻近效应、绝缘层、护套接地等复杂因素。相比架空线路，电缆的电磁耦合更强，频率相关特性更显著。

## 主要特性

### 频率相关阻抗
- 导体集肤效应
- 邻近效应（多芯电缆）
- 护套涡流效应
- 螺线管效应（三芯铠装电缆）

### 导纳参数
- 绝缘层电容
- 护套接地
- 半导体层影响

### 暂态特性
- 行波传播
- 反射与折射
- 截断电荷
-  trapped charge放电

## 建模方法

### 相域模型
- 直接多导体建模
- 考虑相间耦合

### 模域模型
- 模态变换解耦
- 频率相关变换矩阵

### 频变模型
- 矢量拟合阻抗
- 无源性强制
- 递归卷积计算

## 特殊问题

- 海底电缆长距离暂态
- 多芯电缆螺线管效应
- 土壤电离化（接地故障）
- 混合架空线-电缆线路

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]

## 相关模型
- [[transmission-line-model|输电线路模型]] - 架空线与电缆对比
- [[fdne-model|频变网络等值(FDNE)]] - 电缆网络等值
- [[transformer-model|变压器模型]] - 电缆-变压器接口
- [[grounding-system-model|接地系统模型]] - 电缆护套接地

## 相关主题
- [[frequency-dependent-modeling]]
- [[transmission-line-model]]
- [[real-time-simulation]]
- [[parallel-computing]]
- [[network-equivalent]]


## 论文方法分析
> 基于 28 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| MoM-SO（矩量法-表面算子）理论 | 2 | A new tool for calculation of line and cable parameters |
| 数值拉普拉斯变换(NLT) | 2 | An accurate analysis of lightning overvoltages in mixed overhead-cable |
| 电磁暂态(EMT)仿真 | 2 | An Investigation of Electromagnetic Transients for a Mixed Transmissio |
| 准TEM近似法 | 2 | Earth return admittance impact on crossbonded underground cables |
| 部分分式展开(PFE) | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 约束线性最小二乘法 | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 有理函数逼近 | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 特征线法(MoC) | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 级联阻抗与并联导纳频变参数计算 | 1 | A new tool for calculation of line and cable parameters |
| 传统Line/Cable Constants与FEM对比分析 | 1 | A new tool for calculation of line and cable parameters |
| 闭式解析表达式评估 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 误差分析 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 参数灵敏度分析 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 电磁暂态仿真 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 幂等分解（Idempotent Decomposition） | 1 | Admittance-based modelling of cables and overhead lines by idempotent  |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 地下电缆 | 6 |
| 通用线路模型(ULM) | 6 |
| 架空线路 | 5 |
| 电力电缆 | 3 |
| 输电线路 | 2 |
| 地上电缆 | 2 |
| 电缆（Cables） | 2 |
| 地下电缆系统 | 2 |
| 频变相位模型(FDPM) | 2 |
| 多导体地下电缆系统 | 2 |
| 混合架空-地下线路 | 1 |
| 多分层土壤 | 1 |
| 绞合导线 | 1 |
| 双回路电缆系统 | 1 |
| 大地返回阻抗模型 | 1 |
### 验证方式分布
- **仿真/对比**: 9 篇
- **仿真对比**: 7 篇
- **仿真与对比**: 3 篇
- **仿真**: 3 篇
- **实验/测量对比**: 1 篇
- **仿真与对比验证**: 1 篇
- **仿真与实测对比**: 1 篇
- **实验**: 1 篇
- **电磁瞬态仿真与近似模型对比**: 1 篇
- **仿真验证与对比分析**: 1 篇
## 技术演进脉络
### 2010年 (2篇)
- **Improvement of Numerical Stability for the Computation of Transients in Lines an**
  - 💡 基于部分分式展开误差估计提出约束线性最小二乘拟合方法，从根本上解决了频变线路/电缆模型在时域卷积计算中的数值不稳定问题。
  - 提出基于传递函数参数估计时域卷积数值误差的量化方法
  - 推导留数与极点比值的约束条件以将时域误差限制在安全边界内
- **Improvement of Numerical Stability for the Computation of Transients in Lines an**
  - 💡 通过建立时域卷积数值误差与频域部分分式参数的映射关系，引入残差/极点比值约束实现相域稳定拟合。
  - 提出基于传递函数参数估计时域卷积数值误差的量化方法
  - 建立残差与极点比值的约束条件以将时域误差限制在安全边界内
### 2016年 (1篇)
- **An Efficient and Accurate Calculation of Electric Field and Temperature Distribu**
  - 💡 提出了一种基于实测复阻抗特性的通用方法，可快速构建适用于EMTP仿真的磁芯频率相关非线性集总参数等效电路。
  - 提出了一种基于复阻抗测量数据的磁芯频率相关非线性等效电路建模方法。
  - 构建了适用于kHz~MHz频段及kA级电流范围的通用集总参数模型。
### 2018年 (2篇)
- **Efficiently computing the electrical parameters of cables with arbitrary cross-s**
  - 💡 首次将二维矩量法与准静电场离散化相结合，突破了传统闭式近似公式对电缆几何形状的限制，实现了任意截面电缆并联导纳矩阵的高效精确提取。
  - 提出了一种基于二维矩量法的准静电场离散化公式，用于快速计算任意形状电缆的并联导纳矩阵。
  - 结合已有的串联阻抗提取方法，实现了电缆全频域单位长度电气参数的高效精确提取。
- **Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Tran**
  - 💡 提出一种将低频拟合与直流校正分离的两阶段分区拟合策略，从根本上解决了传统宽频有理拟合在直流附近精度差且易引发数值不稳定的问题。
  - 提出仅针对低频样本的两阶段拟合流程，有效改善方程组的数值条件并降低拟合难度。
  - 引入直流校正项精确补偿近直流频段的带外样本，显著提升低频拟合精度。
### 2019年 (1篇)
- **Effects of cable insulations’ physical and geometrical parameters on sheath tran**
  - 💡 提出基于有限元暂态电流计算的介质损耗评估方法，并从过电压与损耗双重视角优化确定了电缆保护套的最优相对介电常数。
  - 系统研究了电缆绝缘物理与几何参数对护套暂态电压及绝缘损耗的影响机制。
  - 提出了一种基于有限元模型数值计算暂态电流的电缆绝缘介质损耗计算方法。
### 2020年 (3篇)
- **Analytical study of the frequency‐dependent earth conduction effects on undergro**
  - 💡 构建了适用于均匀与分层大地的频变大地参数精确解析框架，并首次量化给出了近似模型在地下电缆EMT仿真中的频率适用边界与分层模型选用准则。
  - 系统对比了新型大地阻抗/导纳精确公式与传统近似公式的计算差异
  - 明确了近似大地模型在电磁暂态仿真中适用的频率上限
- **Effect of frequency-dependent soil parameters on wave propagation and transient **
  - 💡 系统评估了多种频率相关土壤模型对多相地下电缆波传播及暂态特性的影响，并揭示了现有EMT仿真工具中FD土壤例程的局限性。
  - 系统总结并对比了多种频率相关土壤参数模型与独立实测数据。
  - 验证了Longmire/Smith模型在拟合实测土壤数据方面具有最佳吻合度。
- **Partitioned fitting and DC correction in transmission line/cable models for wide**
  - 💡 提出结合高频分区拟合与独立直流校正的两阶段策略，同步解决宽频线路模型中的数值不稳定与直流响应失真问题。
  - 提出两阶段分区拟合流程，将高频拟合与低频/直流校正分离处理。
  - 详细推导并给出了基于分区拟合的状态空间实现在时域EMT程序中的具体实现方法。
### 2021年 (4篇)
- **An accurate analysis of lightning overvoltages in mixed overhead-cable lines**
  - 💡 综合应用扩展传输线方法、频率相关土壤与接地模型，结合数值拉普拉斯变换，克服了传统恒定参数假设在高频雷电暂态分析中的精度局限。
  - 系统评估了扩展传输线方法、频率相关土壤模型及接地系统建模在暂态分析中的适用性。
  - 在频域内对比研究了经典与扩展传输线方法下架空线与电缆的波传播特性。
- **Earth return admittance impact on crossbonded underground cables**
  - 💡 量化了大地返回导纳（位移电流）对短段交叉互联地下电缆暂态过电压的阻尼效应，修正了传统保守建模的局限性。
  - 系统评估了大地返回导纳对交叉互联地下电缆暂态过电压的影响机制。
  - 针对1 km与300 m短段电缆长度开展对比，明确了导纳效应在短段中的显著性。
- **Modal propagation characteristics and transient analysis of multiconductor cable**
  - 💡 将频变土壤模型与同时修正阻抗和导纳的广义大地公式相结合，全面量化了其对多导体电缆系统模态传播与电磁瞬态特性的影响。
  - 提出了同时考虑大地导电效应对电缆串联阻抗和并联导纳影响的广义大地公式。
  - 将Longmire-Smith频变土壤模型引入多导体电缆系统的波传播特性分析中。
- **Multi-scale formulation of admittance-based modeling of cables**
  - 💡 将导纳建模、FLE变换与FAST变步长解析信号技术深度融合，突破了传统电缆模型的时间步长限制，实现了多尺度暂态的高效统一仿真。
  - 提出了一种基于相坐标的多尺度电缆模型，利用全耦合节点导纳矩阵替代传统的特征线法。
  - 采用折叠线等效（FLE）变换有效解决了节点导纳矩阵有理拟合过程中的精度问题。
### 2022年 (1篇)
- **Algorithm for fast calculating the energization overvoltages along a power cable**
  - 💡 将模态解耦与数值拉普拉斯逆变换相结合，突破了传统商业软件在电缆投切过电压计算中耗时长的瓶颈，实现了高精度与高效率的统一。
  - 提出了一种基于模态理论与数值拉普拉斯逆变换的快速计算电缆投切过电压的新算法。
  - 通过相模变换将耦合电缆导体解耦为独立模态，并在复频域推导电压解析公式。
### 2023年 (8篇)
- **A new tool for calculation of line and cable parameters**
  - 💡 将MoM-SO理论集成至EMT参数计算工具中，首次在同一框架内统一解决邻近效应、混合线路/电缆拓扑及多分层介质的精确建模问题。
  - 提出基于MoM-SO理论的新型参数计算工具，突破传统EMT软件内置程序的局限。
  - 实现集肤效应与邻近效应的精确建模，显著提升电缆暂态仿真精度。
- **Admittance-based modelling of cables and overhead lines by idempotent decomposit**
  - 💡 首次将幂等分解技术引入节点导纳矩阵的有理拟合过程，从根本上解决了低频最小特征值拟合失真问题，并实现了适用于任意长度线路的高效全耦合相域建模。
  - 提出了一种基于节点导纳矩阵幂等分解的电缆与架空线路新型建模方法。
  - 通过对幂等矩阵而非完整导纳矩阵进行有理拟合，有效克服了低频段最小特征值可观测性差的问题。
- **Algorithms for fast calculation of energization overvoltage of hybrid overhead l**
  - 💡 提出结合全频域频变参数、模态变换与改进NILT的解析算法，在保证工程精度的同时大幅降低混合线路合闸过电压的计算耗时。
  - 提出了一种基于全频域频率相关参数的混合线路合闸过电压快速计算算法。
  - 结合相模变换与改进的数值拉普拉斯逆变换(NILT)实现了频域到时域的高效转换。
- **An Investigation of Electromagnetic Transients for a Mixed Transmission System W**
  - 💡 提出基于精确大地返回阻抗公式的等效均匀大地法及混合输电系统参数建模新流程，突破了传统传输线理论在复杂混合线路EMT仿真中的精度瓶颈。
  - 推导了综合考虑空气、海水与海床介质的海底电缆大地返回阻抗精确表达式。
  - 基于精确公式提出了一种适用于海底电缆的新型等效均匀大地法(EHEM)。
- **Assessment of the transmission line theory in the modeling of multiconductor und**
  - 💡 首次基于全波FDTD基准严格验证了传输线理论及接地返回导纳闭式近似在多导体地下电缆快速暂态分析中的有效性、高精度与计算高效性。
  - 基于全波FDTD方法对传输线理论中两种接地返回阻抗/导纳计算方法进行了严格独立的验证。
  - 系统评估了用于计算地下电缆系统接地返回导纳的闭式近似公式的准确性与适用性。
- **Impact of solenoid effects on series impedance of three-core armoured cables**
  - 💡 首次系统构建三维有限元模型量化了螺线管效应对三芯铠装电缆串联阻抗及电磁暂态特性的影响，弥补了传统2.5D方法的精度缺陷。
  - 提出了基于有限元法的三维全电磁场模型，用于精确计算三芯铠装电缆在工频及高频下的串联阻抗。
  - 揭示了传统二维半(2.5D)方法因忽略螺线管效应而导致阻抗计算存在显著偏差的问题。
- **Morales 等 | A new tool for calculation of line and cable parameters**
  - 💡 将MoM-SO理论引入EMT参数计算，开发出兼顾高精度、复杂几何/环境建模能力与计算效率的统一化线路电缆参数计算工具。
  - 提出基于MoM-SO理论的新型参数计算工具，显著提升EMT仿真中线路与电缆参数的计算精度。
  - 实现了对集肤效应、邻近效应、多股绞线及多层土壤环境的精确建模。
- **Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagati**
  - 💡 通过频域融合程序将实测同轴波传播特性无缝嵌入宽频多导体行波模型，实现了复杂接地电缆系统高频瞬态电压应力的精确仿真。
  - 提出将实测同轴波传播特性融入宽频多导体电缆模型的方法，显著提升高频电压波前阻尼的仿真精度。
  - 设计频域融合程序，在增强高频性能的同时对非共轴传播模式的影响极小。
### 2024年 (3篇)
- **Advanced Wideband Line/Cable Modeling for Transient Studies**
  - 💡 通过最小相位时延优化、自适应模式分组与衰减频率截断的协同改进，从根本上解决了大规模短距离线路/电缆EMT仿真中的数值不稳定难题。
  - 提出基于最小相位基的最优时延计算方法，有效降低传播函数相位振荡并提升拟合精度。
  - 设计基于时延接近度的自适应模式分组新策略，显著缓解高留数/极点比导致的数值不稳定问题。
- **Assessment of the accuracy of the modal-domain line models with real and frequen**
  - 💡 系统量化了实数频不变变换矩阵在含地线非对称架空线路电磁暂态仿真中的精度偏差，并明确了相域模型的适用边界。
  - 系统评估了采用实数且频不变变换矩阵的模态域线路模型在含地线架空线路电磁暂态仿真中的精度局限性。
  - 揭示了地线数量增加和土壤电阻率升高会显著加剧模态域模型的仿真电压误差。
- **Time-domain modeling of a subsea buried cable**
  - 💡 结合准TEM全波近似与EMT时域算法，首次实现了双损耗介质中海底埋设厚铠装电缆的高精度时域建模。
  - 提出了一种适用于EMT程序的海底埋设高压直流电缆时域建模方法。
  - 基于全波公式的准TEM近似推导单位长度参数，突破了传统EMT要求单一介质无损的限制。
### 2025年 (2篇)
- **Accuracy assessment of analytical expressions for the ground return impedance of**
  - 💡 确立并验证了De Conti-Lima闭式表达式在宽频带（至10 MHz）及宽间距地下电缆系统中计算大地返回阻抗的精度与稳定性优势，克服了传统近似公式的局限。
  - 系统评估了Saad-Gaba-Giroux与De Conti-Lima两种闭式表达式在计算大地返回阻抗时的性能差异。
  - 深入分析了两种表达式对土壤参数变化的敏感性及其在宽间距双回路电缆系统中的适用性。
- **Frequency and transient responses of A 275 kV pressure oil-filled cable: Model v**
  - 💡 针对传统管型电缆建模局限，建立了高精度的频率相关详细模型，并通过多工况现场实测数据全面验证了其在EMT暂态仿真中的可靠性。
  - 系统分析了275 kV充油电缆的频率响应与电磁暂态特性。
  - 深入研究了电缆内部传播特性（护套间模式与护套-管道模式）。
### 2026年 (1篇)
- **Time-delay estimation through all-pass functions for ULM line and cable models**
  - 💡 首次将全通函数与延迟均衡技术结合用于ULM时延估计，从根本上保证了有理拟合模型的因果性与最小相位特性。
  - 提出了一种基于全通滤波器和延迟均衡的迭代时延估计新方法。
  - 确保合成的传播矩阵H模型严格满足因果性和最小相位特性。
## 关键发现汇总
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 新方法有效消除了非整数倍仿真步长延迟导致的插值误差累积
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 约束拟合算法显著提升了频变线路与电缆模型在EMTP中的长期数值稳定性
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 所提方法可直接应用于各类多导体电力电缆与输电线路的宽频暂态仿真
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 新方法有效抑制了由非整数倍仿真步长延迟引起的插值误差
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 通过约束拟合使时域数值误差被严格限制在安全范围内
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 与现有模型对比验证表明该方法显著提升了宽频线路/电缆暂态计算的数值稳定性
- [2016] **An Efficient and Accurate Calculation of Electric Field and **: 模型在kHz至MHz频段及kA级电流范围内能准确复现磁芯的阻抗特性。
- [2016] **An Efficient and Accurate Calculation of Electric Field and **: 与实测数据对比验证了该等效电路模型在高频大电流暂态仿真中的高精度。
- [2018] **Efficiently computing the electrical parameters of cables wi**: 频域计算结果与有限元法（FEM）高度吻合，且在高频下显著优于传统近似公式。
- [2018] **Efficiently computing the electrical parameters of cables wi**: 该方法能够准确捕捉邻近效应和集肤效应对任意截面电缆阻抗和导纳矩阵的影响。
- [2018] **Efficiently computing the electrical parameters of cables wi**: 基于提取参数进行的EMTP时域暂态仿真运行稳定，计算时间合理，满足工程应用需求。
- [2018] **Partitioned Fitting and DC Correction for the Simulation of **: 两阶段拟合显著改善了低频段的数值条件，避免了传统宽频拟合中的大残差极点比问题。
- [2018] **Partitioned Fitting and DC Correction for the Simulation of **: 直流校正项确保了模型在直流处的精确响应，同时消除了高频段的非自然偏差。
- [2018] **Partitioned Fitting and DC Correction for the Simulation of **: 在HVDC线路/电缆算例中验证了FDM/DC方法相比传统ULM具有更高的电磁暂态仿真精度与稳定性。
- [2019] **Effects of cable insulations’ physical and geometrical param**: 在0-2ms暂态过程中，220kV电缆绝缘层与保护套产生的介质损耗分别为34.362 W/m和3.365 W/m。
- [2019] **Effects of cable insulations’ physical and geometrical param**: 绝缘相对介电常数与保护套厚度显著影响电缆电容、传播常数及护套最大过电压幅值。
- [2020] **Analytical study of the frequency‐dependent earth conduction**: 传统近似大地模型在高频段会引入显著误差，必须设定明确的频率使用边界
- [2020] **Analytical study of the frequency‐dependent earth conduction**: 分层大地结构与均匀大地假设下的波传播特性存在显著差异，不可随意忽略
- [2020] **Analytical study of the frequency‐dependent earth conduction**: 引入完整大地导纳与传播项的精确模型可大幅改善地下电缆宽频暂态响应的仿真精度
- [2020] **Effect of frequency-dependent soil parameters on wave propag**: Longmire/Smith模型与实测频率相关土壤数据的吻合度最高。
- [2020] **Effect of frequency-dependent soil parameters on wave propag**: 在100Hz下，高土壤电阻率引起的暂态响应衰减显著大于低电阻率情况。
- [2020] **Effect of frequency-dependent soil parameters on wave propag**: 采用不同土壤模型计算的交叉互联电缆暂态电压响应与现有EMT工具结果存在显著差异。
- [2020] **Partitioned fitting and DC correction in transmission line/c**: 分区拟合方法成功避免了大留数/极点比，彻底消除了时域仿真中的数值不稳定现象。
- [2020] **Partitioned fitting and DC correction in transmission line/c**: 该方法在不牺牲高频精度的前提下，准确复现了线路/电缆的直流稳态电压与电流。
- [2020] **Partitioned fitting and DC correction in transmission line/c**: 结合不同积分与插值方案的测试验证了该状态空间模型在宽频EMT研究中的鲁棒性与适用性。
- [2021] **An accurate analysis of lightning overvoltages in mixed over**: 频率相关土壤与接地特性会显著改变电缆护套过电压的峰值与波形。
- [2021] **An accurate analysis of lightning overvoltages in mixed over**: 传统恒定参数模型在kHz至MHz高频段会引入明显的雷电过电压计算误差。
- [2021] **An accurate analysis of lightning overvoltages in mixed over**: 扩展传输线方法结合NLT能准确复现混合线路的雷电暂态传播过程。
- [2021] **Earth return admittance impact on crossbonded underground ca**: 引入大地返回导纳显著提升了电缆暂态响应的阻尼水平。
- [2021] **Earth return admittance impact on crossbonded underground ca**: 在300 m短段长度及高土壤电阻率条件下，大地返回导纳对过电压的影响最为突出。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[parametric-study-of-transient-electromagnetic-fields|Parametric Study of Transient Electromagnetic Fields]] | 2011 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[wwwelseviercomlocateepsr|www.elsevier.com/locate/epsr]] | 2018 |
| [[electromagnetic-transient-studies-of-large-distribution-systems-using-frequency-|Electromagnetic transient studies of large distribution syst]] | 2019 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[high-performance-computing-engines-for-the-fpga-based-simulation-of-the-ulm|High performance computing engines for the FPGA-based simula]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[extension-of-vances-closed-form-approximation-to-calculate-the-ground-admittance|Extension of Vance]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |
## 深度增强内容

 基于提供的论文数据，以下是针对 **电缆模型 (Cable Model)** 的深度增强内容：

---

## 电缆模型深度解析

## 1. 各类模型数学描述

### 1.1 频变多导体电缆基本方程

电缆的电磁行为由频变电报方程描述：

$$
\begin{aligned}
\frac{d\mathbf{V}(x, \omega)}{dx} &= -\mathbf{Z}(\omega)\mathbf{I}(x, \omega) \\
\frac{d\mathbf{I}(x, \omega)}{dx} &= -\mathbf{Y}(\omega)\mathbf{V}(x, \omega)
\end{aligned}
$$

其中 $\mathbf{Z}(\omega) = \mathbf{R}(\omega) + j\omega\mathbf{L}(\omega)$ 为串联阻抗矩阵，$\mathbf{Y}(\omega) = \mathbf{G}(\omega) + j\omega\mathbf{C}$ 为并联导纳矩阵。对于 $n$ 导体电缆系统，$\mathbf{Z}, \mathbf{Y} \in \mathbb{C}^{n \times n}$。

传播常数矩阵和特征阻抗矩阵分别为：
$$
\begin{aligned}
\boldsymbol{\gamma}(\omega) &= \sqrt{\mathbf{Z}(\omega)\mathbf{Y}(\omega)} = \mathbf{T}(\omega)\boldsymbol{\lambda}(\omega)\mathbf{T}^{-1}(\omega) \\
\mathbf{Z}_c(\omega) &= \sqrt{\mathbf{Z}(\omega)\mathbf{Y}^{-1}(\omega)}
\end{aligned}
$$

其中 $\mathbf{T}(\omega)$ 为模态变换矩阵，$\boldsymbol{\lambda}(\omega) = \text{diag}\{\gamma_1, \gamma_2, ..., \gamma_n\}$。

### 1.2 通用线路模型 (ULM) 数学框架

ULM将频变特性通过有理函数逼近实现时域仿真。传播矩阵 $\mathbf{H}(s)$ 和特征导纳 $\mathbf{Y}_c(s)$ 的矢量拟合(VF)表示为：

$$
\mathbf{H}(s) \approx \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s-p_k}e^{-s\tau_k} + \mathbf{D}, \quad s = j\omega
$$

$$
\mathbf{Y}_c(s) \approx \sum_{k=1}^{M} \frac{\mathbf{r}_k}{s-q_k} + \mathbf{D}_y + s\mathbf{E}_y
$$

其中 $\tau_k$ 为模态时延，$\mathbf{R}_k, \mathbf{r}_k$ 为留数矩阵，$p_k, q_k$ 为极点。

**关键约束条件**（基于约束线性最小二乘法）：
$$
\left| \frac{\text{Residue}}{\text{Pole}} \right| \leq \epsilon_{\text{stab}}
$$

该约束确保时域卷积的数值稳定性，避免大留数/极点比导致的误差放大。

### 1.3 分频段宽频带模型 (Partitioned Fitting)

针对宽频带 (0.001 Hz – 1 MHz) 建模，采用两阶段分解：

$$
\mathbf{H}(s) = \underbrace{\mathbf{H}_{DC}(s)}_{\text{低频校正}} + \underbrace{\mathbf{H}_{AC}(s)}_{\text{高频拟合}}
$$

**第一阶段（高频拟合）**：在 $[1\text{ Hz}, 1\text{ MHz}]$ 频段进行标准矢量拟合，排除直流附近数据以避免病态条件。

**第二阶段（DC校正）**：使用低阶有理函数补偿低频特性：
$$
\mathbf{H}_{DC}(s) = \sum_{k=1}^{N_{DC}} \frac{\mathbf{R}_k^{DC}}{s-p_k^{DC}}, \quad N_{DC} \ll N
$$

### 1.4 实测数据融合模型 (Measurement-Based Coaxial Mode)

对于高频同轴模态（>500 kHz），传统几何参数计算存在显著误差。融合模型表示为：

$$
\alpha_{\text{fusion}}(\omega) = 
\begin{cases} 
\alpha_{\text{geom}}(\omega), & \omega \leq \omega_c \\
\alpha_{\text{meas}}(\omega) \cdot \left(1 + \delta_{\text{stranding}}(\omega)\right), & \omega > \omega_c
\end{cases}
$$

其中 $\omega_c$ 为截止频率，$\delta_{\text{stranding}}$ 为绞线效应修正因子（通常 40-60% 增量）。波阻抗融合通过高频滤波实现：
$$
Z_{\text{coax}}^{\text{eff}}(s) = Z_{\text{coax}}^{\text{geom}}(s) \cdot \frac{1}{1 + (s/\omega_c)^{n_{\text{filter}}}}
$$

### 1.5 全通函数时延估计模型 (All-Pass Delay Estimation)

为保证因果性（传播速度 $\leq c$）和最小相位特性，将传播函数分解为：

$$
\mathbf{H}(s) = \mathbf{H}_{\text{min}}(s) \cdot \mathbf{A}(s)
$$

其中 $\mathbf{A}(s)$ 为全通函数矩阵，满足 $|\mathbf{A}(j\omega)| = \mathbf{I}$。通过迭代优化：
$$
\min_{\tau} \| \angle \mathbf{H}(j\omega) - \angle \mathbf{H}_{\text{min}}(j\omega, \tau) - \omega\tau \|_2
$$

确保所有零点位于左半平面（最小相位），且时延估计满足：
$$
\tau_{\text{est}} \geq \frac{l}{c} \cdot \sqrt{\varepsilon_r \mu_r}
$$

---

## 2. 仿真参数参考表

| 参数类别 | 参数名称 | 推荐值/范围 | 适用场景 | 来源文献 |
|---------|---------|------------|---------|----------|
| **频率范围** | 宽频带建模下限 | 0.001 Hz | 长电缆充电、极化效应 | [Partitioned fitting, 2020] |
| | 宽频带建模上限 | 1 MHz (可扩展) | 雷电、VFTO暂态 | [Partitioned fitting, 2020] |
| | 实测融合截止频率 | 500 kHz | 同轴模态过渡 | [Multi-conductor cable, 2023] |
| **有理拟合** | 矢量拟合容差 | 0.1% – 0.01% | 频域逼近精度 | [Advanced wideband, 2024] |
| | 直流校正阶数 $N_{DC}$ | 2 – 4 | 低频特性补偿 | [Partitioned fitting, 2020] |
| | 高频拟合阶数 $N$ | 20 – 50 | 主模型阶数 | [Partitioned fitting, 2020] |
| **稳定性约束** | 留数/极点比阈值 $\epsilon_{\text{stab}}$ | $10^3$ – $10^4$ | 数值稳定性控制 | [Improvement of Numerical Stability, 2010] |
| | 快速衰减模式截断 | 幅值 $< 10^{-3}$ | 高频振荡抑制 | [Advanced wideband, 2024] |
| **时延估计** | 因果性速度上限 | $c$ (光速) | 保证物理可实现性 | [Time-delay estimation, 2026] |
| | 迭代收敛容差 | $10^{-8}$ (NLT参考) | 高精度时延提取 | [Time-delay estimation, 2026] |
| **模式分组** | 96电缆系统分组数 | 8 组 (原36组) | 计算效率优化 | [Advanced wideband, 2024] |
| | 双回架空线分组数 | 4 组 (原10组) | 矩阵降维 | [Advanced wideband, 2024] |
| **损耗修正** | 同轴模态高频增量 | +40% – +60% | 1MHz附近衰减 | [Multi-conductor cable, 2023] |
| | 绞线效应修正频段 | >100 kHz |  Skin-effect修正 | [Multi-conductor cable, 2023] |

---

## 3. 模型选择指南

### 3.1 基于暂态类型的模型选择

| 暂态类型 | 频率范围 | 推荐模型 | 关键配置 | 注意事项 |
|---------|---------|---------|---------|----------|
| **工频稳态** | 50/60 Hz | 恒定参数π型等效 | 单π或级联π | 仅适用于短电缆 (<10 km) |
| **开关操作暂态** | 100 Hz – 10 kHz | 频变相域模型 (FD) | 考虑护套接地方式 | 需包含大地返回路径 |
| **雷电冲击** | 10 kHz – 1 MHz | 宽频带分频拟合模型 | DC校正+高频实测融合 | 必须考虑同轴模态衰减修正 (误差可降低50%以上) |
| **VFTO/极快速暂态** | >1 MHz | 实测数据融合模型 | 包含半导电层损耗 | 传统几何模型失效，必须用实测数据修正 |
| **海底电缆长距离** | 0.001 Hz – 10 kHz | 分频段ULM+交叉互联模型 | 极低速模式单独处理 | 考虑护套涡流和海水环境 |
| **混合线路** | 全频段 | 统一线路模型 (ULM) + 全通时延 | 自适应模式分组 | 架空线与电缆连接处阻抗匹配 |

### 3.2 基于电缆结构的特殊考虑

**三芯铠装电缆 (Three-Core Armored)**：
- 必须考虑**螺线管效应** (Triple Helix Effect)：钢丝铠装产生附加电感 $L_{\text{armor}} \approx \mu_0 \mu_r n^2 A / l$
- 护套-铠装间存在强电磁耦合，建议采用**相域直接建模**而非模域变换

**交叉互联电缆 (Cross-Bonded)**：
- 护套回路阻抗矩阵 $\mathbf{Z}_{\text{sheath}}$ 呈现周期性边界条件
- 建议采用**级联多段模型**，每段代表一个交叉互联大段

**高压直流 (HVDC) 电缆**：
- 必须启用**直流校正** (DC Correction)，否则稳态电压误差显著
- 空间电荷极化效应需扩展频变电容模型：$C(\omega) = C_{\infty} + \frac{C_0 - C_{\infty}}{1+(j\omega\tau)^{\alpha}}$

---

## 4. 前沿研究方向

### 4.1 数据驱动的电缆模型修正 (Measurement-Based Modeling)
传统基于几何参数的模型在高频段（>500 kHz）误差显著。**最新趋势**是将实测同轴传播特性（衰减常数 $\alpha$ 和波速 $v$）通过贝叶斯推断或机器学习融合进解析模型，解决绞线效应和半导电层损耗的建模难题。关键突破点在于保持低频特性不变的同时修正高频阻尼。

### 4.2 因果性与无源性强制保持的宽频带拟合
当前研究聚焦于通过**全通函数迭代** (All-Pass Iteration) 和**约束优化**确保模型的物理可实现性：
- **因果性**：传播速度在任何频率下不超过光速，避免非物理的前驱波 (Precursor)
- **无源性**：阻抗/导纳矩阵正定性保证，通过 Hamiltonian 矩阵特征值检验实现

### 4.3 自适应模式分组与模型降阶
针对多导体电缆系统（如96芯海底电缆），通过**传播速度聚类**将相似模式分组，可将状态空间维度从 $N \times n$ 降低至 $N \times m$ ($m \ll n$)。最新方法基于**时延相近性**和**衰减率阈值**双重准则，在保持波形精度 (>99.9%) 的前提下减少计算量 70% 以上。

### 4.4 土壤电离化与接地故障暂态建模
地下电缆故障时，土壤可能发生电离化导致电导率 $\sigma$ 随电场强度 $E$ 变化：$\sigma(E) = \sigma_0 + k|E|^{\beta}$。当前研究致力于将此非线性效应纳入频变电缆模型，用于准确评估故障电流分布和地电位升 (GPR)。

### 4.5 多物理场耦合：热-电暂态联合仿真
电缆暂态伴随的导体发热会改变材料参数（电阻率、介质损耗）。前沿方向是建立**电热耦合模型**，通过时变温度 $T(t)$ 修正频变参数：
$$
R(\omega, T) = R(\omega, T_0)[1 + \alpha_T(T - T_0)]
$$
实现电磁暂态与长期热稳定的统一仿真框架。

## 深度增强内容

 # 电缆模型深度增强内容

## 1. 各类模型数学描述

### 1.1 频变多导体电缆基本方程

电缆的电磁行为由频变参数电报方程描述：

$$
\frac{\partial \mathbf{V}(x, s)}{\partial x} = -\mathbf{Z}(s)\mathbf{I}(x, s) \\
\frac{\partial \mathbf{I}(x, s)}{\partial x} = -\mathbf{Y}(s)\mathbf{V}(x, s)
$$

其中 $\mathbf{Z}(s) = \mathbf{R}(s) + s\mathbf{L}(s)$ 为串联阻抗矩阵，$\mathbf{Y}(s) = \mathbf{G}(s) + s\mathbf{C}$ 为并联导纳矩阵。对于 $n$ 导体系统，$\mathbf{V}, \mathbf{I} \in \mathbb{C}^{n \times 1}$。

### 1.2 通用线路模型(ULM)数学框架

#### 特性阻抗与传播函数
特性阻抗矩阵和传播矩阵定义为：
$$
\mathbf{Z}_c(s) = \sqrt{\mathbf{Z}(s)\mathbf{Y}^{-1}(s)} \\
\mathbf{H}(s) = e^{-\sqrt{\mathbf{Z}(s)\mathbf{Y}(s)} \cdot l} = e^{-\boldsymbol{\Gamma}(s) \cdot l}
$$

其中 $l$ 为电缆长度，$\boldsymbol{\Gamma}(s)$ 为传播常数矩阵。

#### 有理函数逼近
ULM采用部分分式展开(PFE)逼近频变参数：
$$
\mathbf{Z}_c(s) \approx \mathbf{D} + s\mathbf{E} + \sum_{m=1}^{N} \frac{\mathbf{R}_m}{s - p_m}
$$

$$
\mathbf{H}(s) \approx \sum_{m=1}^{N_h} \frac{\mathbf{R}_m^h}{s - p_m^h} e^{-s\tau_m}
$$

其中 $\tau_m$ 为模态时延，$\mathbf{R}_m$ 为留数矩阵，$p_m$ 为极点。

### 1.3 分频段拟合与直流校正模型

针对宽频建模(0.001 Hz - 1 MHz)，采用两阶段逼近策略：

#### 阶段一：频域分区
$$
\mathbf{H}(s) = \underbrace{\mathbf{H}_{DC}(s)}_{\text{低频校正项}} + \underbrace{\mathbf{H}_{AC}(s)}_{\text{高频主模型}}
$$

其中高频主模型在 $[f_{min}, f_{max}]$（通常为1 Hz - 1 MHz）进行拟合，低频校正项采用低阶有理函数：
$$
\mathbf{H}_{DC}(s) = \sum_{k=1}^{N_{dc}} \frac{\mathbf{R}_k^{dc}}{s - p_k^{dc}}
$$

#### 阶段二：约束优化
通过约束线性最小二乘法消除大留数/极点比：
$$
\min_{\mathbf{R}, p} \sum_{i} \left\| \mathbf{H}(j\omega_i) - \mathbf{H}_{fit}(j\omega_i) \right\|_F^2 \\
\text{s.t.} \quad \left| \frac{R_m}{p_m} \right| < \epsilon_{max}, \quad \forall m
$$

### 1.4 实测同轴特性融合模型

对于高频精度要求（>500 kHz），融合实测与解析模型：

#### 修正的传播函数
$$
\mathbf{H}_{hybrid}(s) = \mathbf{W}(s) \odot \mathbf{H}_{classic}(s) + [\mathbf{I} - \mathbf{W}(s)] \odot \mathbf{H}_{measured}(s)
$$

其中 $\mathbf{W}(s)$ 为频率相关权重矩阵，$\odot$ 表示Hadamard积。对于同轴模态：
$$
\alpha_{coax}(s) = \alpha_{classic}(s) \cdot \left(1 + \delta_{sk}(s) + \delta_{sc}(s)\right)
$$

$\delta_{sk}$ 和 $\delta_{sc}$ 分别表示绞线效应和半导电层损耗的修正系数，在1 MHz处典型值为0.4-0.6。

### 1.5 基于全通函数的时延估计模型

为保证因果性与最小相位特性，采用全通滤波器迭代修正：

#### 相位解缠与延迟均衡
定义全通函数 $A(s) = \prod_{k} \frac{s - z_k}{s + z_k}$，其中 $\text{Re}(z_k) > 0$。传播函数的相位修正为：
$$
\phi_{corrected}(\omega) = \phi_{original}(\omega) + \arg\{A(j\omega)\} - \omega\tau_{est}
$$

迭代优化目标：
$$
\tau_{opt} = \arg\min_{\tau} \left\| \frac{d}{d\omega} \left[ \arg\{\mathbf{H}(j\omega)\} + \omega\tau \right] \right\|_2
$$

约束条件：
$$
v_{mode} = \frac{\omega}{\text{Im}\{\gamma(\omega)\}} < c \quad \text{(光速限制)}
$$

### 1.6 自适应模式分组模型

对于 $n$ 导体系统，通过幂等分解(Idempotent Decomposition)将传播模式分组：

$$
\mathbf{H}(s) = \sum_{g=1}^{N_g} \mathbf{P}_g \cdot h_g(s, \tau_g)
$$

其中 $\mathbf{P}_g$ 为第 $g$ 组投影矩阵，满足 $\sum_g \mathbf{P}_g = \mathbf{I}$ 且 $\mathbf{P}_g \mathbf{P}_h = \delta_{gh}\mathbf{P}_g$。

分组依据时延相近性：
$$
|\tau_i - \tau_j| < \Delta\tau_{th} \Rightarrow i,j \in \text{同一组}
$$

## 2. 仿真参数参考表

| 参数类别 | 参数名称 | 推荐值/范围 | 适用场景 | 来源文献 |
|---------|---------|------------|---------|----------|
| **频率范围** | 低频截止 | 0.001 Hz | 直流暂态、长电缆充电 | [Partitioned fitting, 2020] |
| | 高频截止 | 1 MHz - 10 MHz | 雷电冲击、陡波前过电压 | [Multi-Conductor Cable, 2023] |
| | 快速衰减模式阈值 | $\|H(j\omega)\| < 10^{-3}$ | 抑制高频相位振荡 | [Advanced Wideband, 2024] |
| **拟合精度** | 矢量拟合容差 | 0.5% | 平衡精度与计算效率 | [Advanced Wideband, 2024] |
| | 均方根误差 | < 0.1% | 宽频带精确建模 | [Multi-Conductor Cable, 2023] |
| | 直流校正阶数 | 2-4阶 | 低频段精度补偿 | [Partitioned fitting, 2020] |
| **数值稳定性** | 留数/极点比限制 | $\|R/p\| < 10^3$ | 避免时域卷积不稳定 | [Partitioned fitting, 2020] |
| | 最大迭代次数 | 20-50次 | 全通函数时延估计 | [Time-delay estimation, 2026] |
| **模式分组** | 96电缆系统分组数 | 8组 | 降低矩阵维度 | [Advanced Wideband, 2024] |
| | 双回架空-电缆系统 | 4组 | 混合线路建模 | [Advanced Wideband, 2024] |
| **时延参数** | 同轴模态时延 | 实测值±5% | 高频波传播 | [Multi-Conductor Cable, 2023] |
| | 护套-大地回路时延 | 解析计算值 | 低频电磁暂态 | [Multi-Conductor Cable, 2023] |
| **空间离散** | 分段长度 | < 1/10最小波长 | 雷电过电压分析 | [NLT Cable Analysis] |

## 3. 模型选择指南

### 3.1 按暂态类型选择

| 应用场景 | 推荐模型 | 关键配置 | 精度指标 |
|---------|---------|---------|---------|
| **工频稳态与开关操作** | 分区拟合模型 + DC校正 | 低频段0.001-1 Hz精细拟合 | 直流电压误差 < 0.1% |
| **雷电过电压(>1MHz)** | 实测融合模型 | 同轴模态采用实测衰减系数 | 波前衰减误差 < 5% |
| **长距离海底电缆** | 全通函数时延估计ULM | 严格因果性约束($v<c$) | 无超光速传播 |
| **宽频带混合线路** | 自适应分组宽频模型 | 快速衰减模式截断阈值$10^{-3}$ | 相位振荡抑制 > 90% |
| **多芯电缆暂态** | MoM-SO精确参数模型 | 考虑邻近效应与螺线管效应 | 阻抗计算误差 < 2% |

### 3.2 按电缆结构选择

**单芯高压电缆(HVDC/AC)**
- 首选：标准ULM模型 + 频变阻抗
- 特殊考虑：金属护套接地方式（单端接地/交叉互联）影响导纳矩阵$\mathbf{Y}$结构

**三芯铠装电缆**
- 首选：考虑螺线管效应的修正模型
- 关键参数：铠装层磁导率频变特性与涡流损耗

**同轴电缆（高频通信/测量）**
- 首选：实测融合模型（>500 kHz）
- 关键修正：半导电层复介电常数 $\varepsilon_r(\omega) = \varepsilon'(\omega) - j\varepsilon''(\omega)$

### 3.3 按计算资源选择

| 资源限制 | 策略 | 模型简化 |
|---------|------|---------|
| **实时仿真** | 模式降阶 | 采用自适应分组，将$N$模态压缩至$N/4$组 |
| **大系统仿真** | 混合建模 | 电缆用ULM，架空线用 Bergeron 模型 |
| **长期暂态** | 宽频压缩 | 快速衰减模式在$10^{-3}$幅值处截断 |

## 4. 前沿研究方向

### 4.1 数据-物理融合建模(Data-Physics Fusion)
基于2023年实测融合模型的演进方向：
- **机器学习辅助修正**：利用神经网络学习几何参数与实测衰减的映射关系，替代固定修正系数$\delta_{sk}, \delta_{sc}$
- **在线参数辨识**：通过分布式光纤传感(DAS)实时更新电缆模型参数，实现数字孪生

### 4.2 宽频因果性与无源性强制
基于2024-2026年研究趋势：
- **Hamiltonian系统理论应用**：构建保证无源性的结构保持模型，避免有理拟合后的无源性强制后处理
- **分数阶微积分**：采用分数阶导数描述电缆的频变特性，减少所需极点数量：
  $$
  \mathbf{Z}(s) = \mathbf{R}_0 + \mathbf{L}_0 s + \sum_{k} \mathbf{L}_k s^{\alpha_k}, \quad 0 < \alpha_k < 1
  $$

### 4.3 多物理场耦合建模
- **热-电耦合**：考虑绝缘层温度依赖的介电损耗$\tan\delta(T)$，建立电热联合暂态模型
- **机械-电磁耦合**：海底电缆敷设状态下的几何形变对阻抗矩阵$\mathbf{Z}$的影响

### 4.4 高效数值算法
- **幂等分解快速算法**：利用$\mathbf{P}_g$的幂等特性开发$O(n)$复杂度的时域卷积算法
- **GPU加速矢量拟合**：针对大规模电缆系统（>100导体）的并行极点-留数计算

### 4.5 开放问题
1. **极低频(ELF)建模**：0.001 Hz以下电缆参数的准确测量与模型验证仍缺乏标准方法
2. **非均匀土壤**：多层土壤电离化状态下的频变大地返回阻抗准确建模
3. **老化电缆**：绝缘材料老化导致的局部介电常数不均匀性对高频暂态的影响量化
